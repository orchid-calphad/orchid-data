#!/usr/bin/env python3
"""ORCHID contributions: validate corrections, new data, paper suggestions and TDB files; apply accepted
corrections; credit contributors.

Contribution files (contributions/README.md, contributions/SCHEMA.md):

  contributions/corrections/*.jsonl   one correction of a released value per line
  contributions/data/*.json|*.csv     new values (types B contributor-extracted, C new measurements, D calculated);
                                      files named TEMPLATE* are templates and are not validated
  contributions/papers/*.jsonl        type A: paper / assessment suggestions (DOI only) -> extraction queue
  contributions/tdb/<name>/metadata.json (+ the .tdb file)   type E: new assessments / TDB files
  contributors.json                   accepted contributors (credit; CONTRIBUTORS.md is written from it)

Checks reuse the release rules: units and ranges per property, elements against the chemical system, the
physical phase rule and the phase mapping of the release (tools/phase_rule.py of orchid-project.org, when the
release tools are available: --release-tools DIR), duplicates against the release and within the contribution,
quote length (240 characters at most), page numbers, DOI and ORCID syntax, licence consent (CC BY 4.0).

Nothing here posts, downloads or sends anything. Standard library only; deterministic.

  python3 contributions/tools/orchid_contrib.py validate [FILES...] [--data .] [--release-tools ../orchid-project.org/tools]
  python3 contributions/tools/orchid_contrib.py validate --changed-from origin/main      # files changed in a PR
  python3 contributions/tools/orchid_contrib.py credit [--check]   # CONTRIBUTORS.md, CITATION.cff, Zenodo metadata
  python3 contributions/tools/orchid_contrib.py convert FILE       # contributed rows -> ORCHID records (JSON lines)
"""
from __future__ import annotations

import argparse
import base64
import csv
import glob
import gzip
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.dirname(os.path.dirname(HERE))   # the orchid-data repository
QUOTE_MAX = 240
LICENCE = "CC-BY-4.0"
TIERS = ("contributed_unverified", "verified")
CONTRIB_TYPES = {"A": "paper suggestion", "B": "contributor-extracted values", "C": "new measurements",
                 "D": "calculated data", "E": "new assessment / TDB"}
EVIDENCE_CLASSES = ("experimental", "model", "dft", "unspecified")
CALCULATED_CLASSES = ("model", "dft")
TDB_LICENCES = ("CC-BY-4.0", "CC0-1.0", "MIT", "BSD-3-Clause", "ODbL-1.0", "CC-BY-SA-4.0")
TRANSITION_KINDS = ("eutectic", "peritectic", "monotectic", "syntectic", "eutectoid", "peritectoid", "monotectoid",
                    "quasi-peritectic", "congruent melting", "congruent transformation", "polymorphic", "magnetic",
                    "order-disorder", "critical point", "metatectic/catatectic", "other")
DATA_TYPES = ("invariant reactions", "phase boundaries / compositions", "phase transitions", "formation enthalpy",
              "mixing / partial quantities", "heat capacity / entropy", "activity / EMF / vapour pressure",
              "crystal structure / lattice", "CALPHAD assessment (TDB)", "DFT / calculated", "other")
ELEMENTS = (
    "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr "
    "Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir "
    "Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr").upper().split()
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
ORCID_RE = re.compile(r"^(?:https?://orcid\.org/)?(\d{4}-\d{4}-\d{4}-\d{3}[\dX])$")
PAGE_RE = re.compile(r"^[A-Za-z]{0,3}\d{1,5}$")   # 12, S3, e101
ATOL = 1e-9

# property -> (canonical unit, low, high, sign rule). Contributed values use the canonical unit (the release
# normalisation); corrections of a released value keep the record's unit and are range-checked when it is canonical.
PROPERTIES = {
    "INVARIANT_TEMPERATURE": ("K", 1.0, 6000.0, None),
    "TRANSITION_TEMPERATURE": ("K", 1.0, 6000.0, None),
    "PHASE_COMPOSITION": (None, None, None, None),
    "PHASE_ASSEMBLAGE": (None, None, None, None),
    "HM_FORM": ("kJ/mol-atom", -500.0, 100.0, "negative_expected"),
    "GM_FORM": ("kJ/mol-atom", -500.0, 100.0, "negative_expected"),
    "SM_FORM": ("J/mol-atom/K", -100.0, 100.0, None),
    "HM_MIX": ("kJ/mol-atom", -300.0, 300.0, None),
    "GM_MIX": ("kJ/mol-atom", -300.0, 100.0, None),
    "SM_MIX": ("J/mol-atom/K", -100.0, 100.0, None),
    "PARTIAL_ENTHALPY": ("kJ/mol", -1000.0, 1000.0, None),
    "CHEMICAL_POTENTIAL": ("kJ/mol", -2000.0, 500.0, None),
    "CPM": ("J/mol-atom/K", 0.0, 500.0, "positive"),
    "SM": ("J/mol-atom/K", 0.0, 1000.0, "positive"),
    "HEAT_CONTENT": ("kJ/mol-atom", -1000.0, 1000.0, None),
    "TRANSITION_ENTHALPY": ("kJ/mol-atom", -500.0, 500.0, None),
    "ACTIVITY": ("1", 0.0, 1.0, "positive"),
    "ACTIVITY_COEFFICIENT": ("1", 0.0, 1e6, "positive"),
    "EMF": ("mV", -5000.0, 5000.0, None),
    "VAPOR_PRESSURE": ("Pa", 0.0, 1e9, "positive"),
    "LATTICE_A": ("nm", 0.05, 10.0, "positive"),
    "LATTICE_B": ("nm", 0.05, 10.0, "positive"),
    "LATTICE_C": ("nm", 0.05, 10.0, "positive"),
    "LATTICE_ALPHA": ("°", 0.0, 180.0, "positive"),
    "LATTICE_BETA": ("°", 0.0, 180.0, "positive"),
    "LATTICE_GAMMA": ("°", 0.0, 180.0, "positive"),
    "MOLAR_VOLUME": ("cm3/mol", 0.0, 1000.0, "positive"),
    "BULK_MODULUS": ("GPa", 0.0, 2000.0, "positive"),
}
OBSERVATION = {"INVARIANT_TEMPERATURE": "invariant_reaction", "TRANSITION_TEMPERATURE": "phase_transition",
               "PHASE_COMPOSITION": "phase_region_vertex_set", "PHASE_ASSEMBLAGE": "phase_assemblage_node"}
TEMPERATURE_PROPS = ("INVARIANT_TEMPERATURE", "TRANSITION_TEMPERATURE")
UNCERTAINTY_COMPONENTS = ("sigma_printed", "sigma_method", "sigma_composition", "sigma_scatter", "sigma_conversion")

# correctable fields of a released record: name -> kind
CORRECTABLE = {
    "value": "number", "unit": "unit", "temperature_K": "temperature", "pressure_Pa": "pressure",
    "evidence_class": "evidence_class", "transition_kind": "transition_kind", "property": "property",
    "system": "system", "phases": "phase_labels", "phase_compositions": "phase_compositions",
    "overall_composition": "composition", "reference_state": "reference_state", "uncertainty": "uncertainty",
    "quote_page": "page", "locator.page": "page", "locator.row": "row", "extraction_accepted": "retraction",
}


# ------------------------------------------------------------------------------------------------ helpers --
def canon(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def num(x):
    if isinstance(x, bool):
        return None
    if isinstance(x, (int, float)):
        return float(x) if math.isfinite(float(x)) else None
    if isinstance(x, str) and re.fullmatch(r"\s*[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?\s*", x):
        return float(x)
    return None


def orcid_ok(orcid):
    """ISO 7064 mod 11-2 checksum of an ORCID iD (bare or https://orcid.org/ form)."""
    m = ORCID_RE.match(str(orcid or "").strip())
    if not m:
        return False
    digits = m.group(1).replace("-", "")
    total = 0
    for ch in digits[:-1]:
        total = (total + int(ch)) * 2
    check = (12 - total % 11) % 11
    return digits[-1] == ("X" if check == 10 else str(check))


def orcid_bare(orcid):
    m = ORCID_RE.match(str(orcid or "").strip())
    return m.group(1) if m else None


def norm_doi(doi):
    d = str(doi or "").strip()
    d = re.sub(r"(?i)^(https?://(dx\.)?doi\.org/|doi:)", "", d)
    return d.lower()


def system_elements(system):
    els = [e.strip().upper() for e in str(system or "").split("-") if e.strip()]
    return els


def system_ok(system):
    els = system_elements(system)
    return (len(els) >= 1 and all(e in ELEMENTS for e in els) and els == sorted(els) and len(set(els)) == len(els)
            and "-".join(els) == str(system))


def contribution_id(row):
    """Deterministic id of a contributed value: hash of its content without the contributor."""
    body = {k: v for k, v in row.items() if k not in ("contributor", "licence_consent", "note")}
    h = hashlib.sha256(canon(body).encode()).digest()
    return "ORC-C" + base64.b32encode(h).decode()[:10]


class Report:
    def __init__(self):
        self.items = []   # (level, file, line, message)

    def error(self, f, line, msg):
        self.items.append(("error", f, line, msg))

    def warn(self, f, line, msg):
        self.items.append(("warning", f, line, msg))

    def info(self, f, line, msg):
        self.items.append(("notice", f, line, msg))

    @property
    def errors(self):
        return [i for i in self.items if i[0] == "error"]

    def render(self, github=False):
        out = []
        for lvl, f, line, msg in self.items:
            if github:
                out.append("::%s file=%s%s::%s" % (lvl, f, ",line=%d" % line if line else "", msg))
            else:
                out.append("%s %s%s: %s" % (lvl.upper(), f, ":%d" % line if line else "", msg))
        return "\n".join(out)


# ------------------------------------------------------------------------------------------- release --
class Release:
    """Read-only view of the released data used by the checks (lazy)."""

    def __init__(self, data=DATA_ROOT, release_tools=None, root=None):
        self.data = data            # released data (literature/, phases/, phase-diagrams/)
        self.root = root or data    # the repository holding the contribution files
        self.release_tools = release_tools
        self._records = None
        self._papers = None
        self._rule = None
        self._rule_error = None
        self._tdb_phases = {}

    @property
    def records(self):
        if self._records is None:
            self._records = {}
            p = os.path.join(self.data, "literature", "orchid-literature.jsonl.gz")
            if os.path.exists(p):
                with gzip.open(p, "rt", encoding="utf-8") as fh:
                    for line in fh:
                        r = json.loads(line)
                        self._records[r["id"]] = r
                        for m in r.get("merged_ids") or []:
                            self._records.setdefault(m, {"merged_into": r["id"]})
        return self._records

    def by_system(self, system):
        return [r for r in self.records.values() if r.get("system") == system and "merged_into" not in r]

    @property
    def paper_dois(self):
        if self._papers is None:
            p = os.path.join(self.data, "literature", "papers.json")
            self._papers = set()
            if os.path.exists(p):
                for pid, e in json.load(open(p, encoding="utf-8")).items():
                    if e.get("doi"):
                        self._papers.add(norm_doi(e["doi"]))
                    if pid.startswith("doi:"):
                        self._papers.add(norm_doi(pid[4:]))
        return self._papers

    def tdb_phases(self, system):
        """Model phase names of the system's TDB files in the phase registry (empty: no TDB)."""
        if system not in self._tdb_phases:
            names = set()
            p = os.path.join(self.data, "phases", "systems", "%s.json" % system)
            if os.path.exists(p):
                for ph in json.load(open(p, encoding="utf-8")).get("phases", []):
                    for m in ph.get("models") or []:
                        names.add(str(m.get("phase_name", "")).upper())
            self._tdb_phases[system] = names
        return self._tdb_phases[system]

    @property
    def rule(self):
        """tools/phase_rule.PhaseRule of the release (None when the release tools are not available)."""
        if self._rule is None and self._rule_error is None:
            tools = self.release_tools
            if not tools or not os.path.exists(os.path.join(tools, "phase_rule.py")):
                self._rule_error = "release tools not found (pass --release-tools <orchid-project.org>/tools)"
                return None
            sys.path.insert(0, tools)
            try:
                import phase_rule  # noqa: E402
                self._rule = phase_rule.PhaseRule(self.data)
            except Exception as exc:   # pragma: no cover - environment problem, reported
                self._rule_error = "release tools failed to load: %s" % exc
        return self._rule


# ---------------------------------------------------------------------------------- value checks --
def check_composition(comp, elements, where, rep, f, line, require_sum=True):
    if not isinstance(comp, dict) or not comp:
        rep.error(f, line, "%s: composition must be an object {ELEMENT: mole fraction}" % where)
        return
    tot = 0.0
    for el, x in comp.items():
        if str(el).upper() not in elements:
            rep.error(f, line, "%s: element %s is not in the chemical system %s" % (where, el, "-".join(elements)))
        v = num(x)
        if v is None or v < 0 or v > 1:
            rep.error(f, line, "%s: mole fraction of %s must be a number in [0, 1] (got %r)" % (where, el, x))
        else:
            tot += v
    if require_sum and len(comp) == len(elements) and abs(tot - 1.0) > 0.011:
        rep.error(f, line, "%s: mole fractions sum to %.4f, not 1" % (where, tot))
    if tot > 1.011:
        rep.error(f, line, "%s: mole fractions sum to %.4f (> 1)" % (where, tot))


def check_value(prop, unit, value, rep, f, line, where="value"):
    v = num(value)
    if v is None:
        rep.error(f, line, "%s: not a number (%r)" % (where, value))
        return None
    spec = PROPERTIES.get(prop)
    if spec and spec[0] is not None and unit == spec[0]:
        _, lo, hi, sign = spec
        if v < lo or v > hi:
            rep.error(f, line, "%s %g %s outside the plausible range [%g, %g] for %s" % (where, v, unit, lo, hi, prop))
        if sign == "negative_expected" and v > 0:
            rep.warn(f, line, "%s %g %s is positive: formation quantities are usually negative; check the printed "
                              "sign on the page" % (where, v, unit))
        if sign == "positive" and v <= 0 and prop not in ("ACTIVITY_COEFFICIENT",):
            rep.error(f, line, "%s %g must be positive for %s" % (where, v, prop))
    return v


def check_page(page, rep, f, line, where="page"):
    if page is None or not PAGE_RE.match(str(page).strip()):
        rep.error(f, line, "%s: a printed page number is required (e.g. 5, S3; got %r)" % (where, page))
        return False
    return True


def check_quote(quote, rep, f, line, required=True):
    q = " ".join(str(quote or "").split())
    if not q:
        if required:
            rep.error(f, line, "quote: the sentence or table row on the page that states the value is required")
        return False
    if len(q) > QUOTE_MAX:
        rep.error(f, line, "quote: %d characters; at most %d (one sentence or table row, reproduced under fair use)"
                  % (len(q), QUOTE_MAX))
        return False
    return True


def check_contributor(c, rep, f, line):
    if not isinstance(c, dict) or not str(c.get("name") or "").strip():
        rep.error(f, line, "contributor.name is required (the name to credit; a GitHub handle is acceptable)")
        return
    if c.get("orcid") not in (None, "") and not orcid_ok(c["orcid"]):
        rep.error(f, line, "contributor.orcid %r is not a valid ORCID iD (checksum or format)" % c["orcid"])
    extra = set(c) - {"name", "orcid", "github", "affiliation", "credit_opt_in"}
    if extra:
        rep.error(f, line, "contributor: unexpected field(s) %s (no e-mail or other personal data)" % sorted(extra))


def check_consent(v, rep, f, line):
    if v != LICENCE:
        rep.error(f, line, 'licence_consent must be "%s": you agree that the contributed data are released under '
                           "CC BY 4.0 with credit to you" % LICENCE)


# ------------------------------------------------------------------------------------- corrections --
def current_value(rec, field):
    if field == "phases":
        return [p.get("label") for p in rec.get("phases") or []]
    if field == "phase_compositions":
        return [{"phase": p.get("phase"), "composition": p.get("composition")} for p in rec.get("phase_compositions") or []]
    if field == "extraction_accepted":
        return bool((rec.get("flags") or {}).get("extraction_accepted"))
    cur = rec
    for part in field.split("."):
        cur = cur.get(part) if isinstance(cur, dict) else None
    return cur


def same(a, b):
    na, nb = num(a), num(b)
    if na is not None and nb is not None:
        return abs(na - nb) <= max(ATOL, 1e-9 * max(abs(na), abs(nb)))
    if isinstance(a, str) and isinstance(b, str):
        return " ".join(a.split()) == " ".join(b.split())
    return canon(a) == canon(b)


def check_new(kind, new, rec, rel, rep, f, line):
    els = system_elements(rec.get("system"))
    if kind == "number":
        check_value(rec.get("property"), rec.get("unit"), new, rep, f, line, "new value")
    elif kind == "unit":
        spec = PROPERTIES.get(rec.get("property"))
        if not isinstance(new, str) or not new.strip():
            rep.error(f, line, "new unit must be a non-empty string")
        elif spec and spec[0] and new != spec[0]:
            rep.warn(f, line, "new unit %r is not the release unit of %s (%s); the maintainers will convert"
                     % (new, rec.get("property"), spec[0]))
    elif kind == "temperature":
        v = num(new)
        if v is None or not (1.0 < v <= 6000.0):
            rep.error(f, line, "new temperature_K must be a number in (1, 6000] K (got %r); convert °C to K" % new)
    elif kind == "pressure":
        v = num(new)
        if v is None or v <= 0:
            rep.error(f, line, "new pressure_Pa must be a positive number in Pa")
    elif kind == "evidence_class":
        if new not in EVIDENCE_CLASSES:
            rep.error(f, line, "new evidence_class must be one of %s" % list(EVIDENCE_CLASSES))
    elif kind == "transition_kind":
        if new not in TRANSITION_KINDS:
            rep.error(f, line, "new transition_kind must be one of %s" % list(TRANSITION_KINDS))
    elif kind == "property":
        if new not in PROPERTIES and not re.fullmatch(r"(ACR|LATTICE)_[A-Z0-9_]+", str(new)):
            rep.error(f, line, "new property must be a controlled property code (SCHEMA.md), got %r" % new)
    elif kind == "system":
        if not system_ok(new):
            rep.error(f, line, "new system must be element symbols, uppercase, sorted, joined by '-' (got %r)" % new)
    elif kind == "phase_labels":
        if not isinstance(new, list) or not new or not all(isinstance(x, str) and x.strip() for x in new):
            rep.error(f, line, "new phases must be a list of printed phase labels")
    elif kind == "phase_compositions":
        if not isinstance(new, list) or not new:
            rep.error(f, line, "new phase_compositions must be a list of {phase, composition}")
        else:
            for i, pc in enumerate(new):
                if not isinstance(pc, dict) or not pc.get("phase"):
                    rep.error(f, line, "phase_compositions[%d]: phase is required" % i)
                    continue
                check_composition(pc.get("composition"), els, "phase_compositions[%d]" % i, rep, f, line)
    elif kind == "composition":
        check_composition(new, els, "overall_composition", rep, f, line)
    elif kind == "reference_state":
        if not isinstance(new, dict) or not new:
            rep.error(f, line, "new reference_state must be {ELEMENT: {phase}}")
        else:
            for el, st in new.items():
                if el.upper() not in els:
                    rep.error(f, line, "reference_state: %s is not in the system" % el)
                if not isinstance(st, dict) or not st.get("phase"):
                    rep.error(f, line, "reference_state.%s: {phase: ...} required" % el)
    elif kind == "uncertainty":
        if not isinstance(new, dict) or num(new.get("value")) is None or num(new["value"]) < 0:
            rep.error(f, line, "new uncertainty must be {value >= 0, basis: printed, kind}")
        elif new.get("basis") != "printed":
            rep.error(f, line, "a corrected uncertainty must be the printed one (basis: printed)")
    elif kind == "page":
        check_page(new, rep, f, line, "new page")
    elif kind == "row":
        if not isinstance(new, int) or new < 1:
            rep.error(f, line, "new row must be a positive integer")
    elif kind == "retraction":
        if new is not False:
            rep.error(f, line, "extraction_accepted can only be corrected to false (the row is not a value of the "
                               "paper, e.g. a misread or a value of another system)")


def validate_corrections(path, rel, rep, seen):
    f = relpath(path, rel.root)
    for line, row in read_jsonl(path, rep, f):
        need = ("record_id", "field", "old", "new", "evidence", "contributor", "licence_consent")
        miss = [k for k in need if k not in row]
        if miss:
            rep.error(f, line, "missing field(s) %s" % miss)
            continue
        extra = set(row) - set(need) - {"note", "status"}
        if extra:
            rep.error(f, line, "unexpected field(s) %s" % sorted(extra))
        check_contributor(row["contributor"], rep, f, line)
        check_consent(row["licence_consent"], rep, f, line)
        ev = row["evidence"] if isinstance(row["evidence"], dict) else {}
        if not isinstance(row["evidence"], dict):
            rep.error(f, line, "evidence must be {page, quote}")
        check_page(ev.get("page"), rep, f, line, "evidence.page")
        check_quote(ev.get("quote"), rep, f, line)
        if set(ev) - {"page", "quote", "figure_or_table", "doi"}:
            rep.error(f, line, "evidence: unexpected field(s) %s" % sorted(set(ev) - {"page", "quote", "figure_or_table", "doi"}))
        field = row["field"]
        if field not in CORRECTABLE:
            rep.error(f, line, "field %r cannot be corrected; allowed: %s" % (field, sorted(CORRECTABLE)))
            continue
        rid = row["record_id"]
        rec = rel.records.get(rid)
        if rec is None:
            rep.error(f, line, "record %s is not in the release (literature/orchid-literature.jsonl.gz)" % rid)
            continue
        if "merged_into" in rec:
            rep.error(f, line, "record %s was merged into %s; correct that record" % (rid, rec["merged_into"]))
            continue
        key = (rid, field)
        if key in seen:
            rep.error(f, line, "duplicate correction of %s.%s (also %s)" % (rid, field, seen[key]))
        seen[key] = "%s:%d" % (f, line)
        if same(row["old"], row["new"]):
            rep.error(f, line, "old and new are the same")
        cur = current_value(rec, field)
        if not same(row["old"], cur):
            if same(row["new"], cur):
                rep.info(f, line, "already applied in the release (%s.%s = %s)" % (rid, field, canon(cur)))
                continue
            rep.error(f, line, "old %s does not match the release value of %s.%s (%s)"
                      % (canon(row["old"]), rid, field, canon(cur)))
        check_new(CORRECTABLE[field], row["new"], rec, rel, rep, f, line)
        pg = rec.get("quote_page") or (rec.get("locator") or {}).get("page")
        if pg is not None and PAGE_RE.match(str(ev.get("page") or "")) and str(ev["page"]) != str(pg) and field not in ("quote_page", "locator.page"):
            rep.warn(f, line, "evidence.page %s differs from the record's page %s (fine if the value is restated there)"
                     % (ev["page"], pg))
        if field == "value" and num(row["new"]) is not None and num(cur) is not None and num(cur) * num(row["new"]) < 0:
            rep.warn(f, line, "the correction changes the sign; the maintainers check the printed sign on the page")


# ------------------------------------------------------------------------------------ new data --
CSV_COLUMNS = ("contribution_type", "system", "property", "value", "unit", "value_printed", "unit_printed",
               "temperature_K", "pressure_Pa", "phases", "reaction", "transition_kind", "overall_composition",
               "phase_compositions", "reference_state", "evidence_class", "method_kind", "method_details",
               "doi", "dataset_doi", "page", "table", "row", "quote", "sigma_printed", "sigma_printed_kind",
               "sigma_method", "sigma_composition", "sigma_scatter", "sigma_conversion", "contributor_name",
               "contributor_orcid", "licence_consent")


def parse_pairs(s):
    """'CU:0.333;ZR:0.667' -> {'CU': 0.333, 'ZR': 0.667} (numbers when they parse)."""
    out = {}
    for part in [p for p in str(s or "").split(";") if p.strip()]:
        k, _, v = part.partition(":")
        out[k.strip().upper()] = num(v) if num(v) is not None else v.strip()
    return out


def csv_row_to_json(row):
    """One row of the CSV template -> the JSON form of a contributed value."""
    g = lambda k: (row.get(k) or "").strip()   # noqa: E731
    phases = []
    for p in [x for x in g("phases").split(";") if x.strip()]:
        lab, _, mp = p.partition("=")
        phases.append({"label": lab.strip(), **({"model_phase": mp.strip()} if mp.strip() else {})})
    state = {"phases": phases}
    for k in ("temperature_K", "pressure_Pa"):
        if g(k):
            state[k] = num(g(k)) if num(g(k)) is not None else g(k)
    if g("overall_composition"):
        state["overall_composition"] = parse_pairs(g("overall_composition"))
    if g("phase_compositions"):
        try:
            state["phase_compositions"] = json.loads(g("phase_compositions"))
        except ValueError:
            state["phase_compositions"] = g("phase_compositions")
    if g("reference_state"):
        state["reference_state"] = {k: {"phase": v} for k, v in parse_pairs(g("reference_state")).items()}
    if g("reaction") or g("transition_kind"):
        state["reaction"] = {k: v for k, v in (("printed", g("reaction")), ("type", g("transition_kind"))) if v}
    prov = {k: (int(g(k)) if k == "row" and g(k).isdigit() else g(k)) for k in ("doi", "dataset_doi", "page", "table", "row", "quote") if g(k)}
    unc = {}
    if g("sigma_printed"):
        unc["sigma_printed"] = {"value": num(g("sigma_printed")), "kind": g("sigma_printed_kind") or None}
    for k in ("sigma_method", "sigma_composition", "sigma_scatter", "sigma_conversion"):
        if g(k):
            unc[k] = {"value": num(g(k))}
    out = {"contribution_type": g("contribution_type"), "system": g("system"), "property": g("property"),
           "value": num(g("value")) if g("value") else None, "unit": g("unit") or None}
    for k in ("value_printed", "unit_printed"):
        if g(k):
            out[k] = g(k)
    out.update({"state": state, "evidence_class": g("evidence_class"),
                "method": {k: v for k, v in (("kind", g("method_kind")), ("details", g("method_details"))) if v},
                "provenance": prov, "uncertainty": unc,
                "contributor": {k: v for k, v in (("name", g("contributor_name")), ("orcid", g("contributor_orcid"))) if v},
                "licence_consent": g("licence_consent")})
    return out


def read_data_file(path, rep, f):
    if path.endswith(".csv"):
        with open(path, encoding="utf-8", newline="") as fh:
            rd = csv.DictReader(fh)
            unknown = set(rd.fieldnames or []) - set(CSV_COLUMNS)
            if unknown:
                rep.error(f, 1, "unknown CSV column(s) %s; use the columns of TEMPLATE.csv" % sorted(unknown))
            return [(i + 2, csv_row_to_json(r)) for i, r in enumerate(rd)]
    try:
        d = json.load(open(path, encoding="utf-8"))
    except ValueError as exc:
        rep.error(f, None, "not valid JSON: %s" % exc)
        return []
    rows = d.get("records") if isinstance(d, dict) else d
    if not isinstance(rows, list):
        rep.error(f, None, 'expected {"records": [...]} or a list of values')
        return []
    return [(i + 1, r) for i, r in enumerate(rows)]


def to_record(row, f=None, line=None):
    """Contributed value (JSON form) -> ORCHID record (literature SCHEMA.md fields; source: contributed)."""
    st = row.get("state") or {}
    prov = row.get("provenance") or {}
    prop = row.get("property")
    doi = norm_doi(prov.get("doi") or prov.get("dataset_doi"))
    phases = [{"label": p.get("label"), **({"model_phase": p["model_phase"]} if p.get("model_phase") else {})}
              for p in st.get("phases") or [] if isinstance(p, dict)]
    rx = st.get("reaction") or {}
    rec = {
        "id": contribution_id(row),
        "source": "contributed",
        "system": row.get("system"),
        "elements": system_elements(row.get("system")),
        "record_kind": "contributed",
        "observation_type": OBSERVATION.get(prop) or ("structural_property" if str(prop).startswith("LATTICE")
                                                       else "equilibrium_property"),
        "property": prop,
        "value": row.get("value"),
        "unit": row.get("unit"),
        "temperature_K": st.get("temperature_K", row.get("value") if prop in TEMPERATURE_PROPS else None),
        "temperature_basis": "contributed" if st.get("temperature_K") is not None else None,
        "pressure_Pa": st.get("pressure_Pa", 101325),
        "pressure_basis": "contributed" if st.get("pressure_Pa") is not None else "assumed_default_1_atm_not_printed",
        "phases": phases,
        "phase_compositions": [dict(pc, basis="mole_fraction", composition_source="contributed")
                               for pc in st.get("phase_compositions") or [] if isinstance(pc, dict)],
        "overall_composition": st.get("overall_composition"),
        "reference_state": st.get("reference_state"),
        "reaction": {"printed": rx.get("printed"), "type": rx.get("type")} if rx else None,
        "transition_kind": rx.get("type"),
        "evidence_class": row.get("evidence_class"),
        "origin": {"class": row.get("evidence_class"), "basis": "contributed_type_%s" % row.get("contribution_type"),
                   "measured_in": ("doi:" + doi) if doi else None,
                   "own_work_of_paper": row.get("contribution_type") in ("C", "D")},
        "method": row.get("method") or None,
        "paper": ("doi:" + doi) if doi else None,
        "quote": prov.get("quote"),
        "quote_page": prov.get("page"),
        "locator": {"artifact": "table" if prov.get("table") else ("dataset" if prov.get("dataset_doi") else "text_passage"),
                    "label": prov.get("table"), "page": prov.get("page"), "row": prov.get("row")},
        "uncertainty": ({"value": (row.get("uncertainty") or {})["sigma_printed"].get("value"), "basis": "printed",
                         "note": (row.get("uncertainty") or {})["sigma_printed"].get("kind")}
                        if (row.get("uncertainty") or {}).get("sigma_printed") else None),
        "uncertainty_contributed": {k: v for k, v in (row.get("uncertainty") or {}).items() if k in UNCERTAINTY_COMPONENTS} or None,
        "contribution": {"type": row.get("contribution_type"), "file": f, "line": line,
                         "dataset_doi": norm_doi(prov.get("dataset_doi")) or None, "licence": LICENCE},
        "contributors": [{k: v for k, v in (("name", (row.get("contributor") or {}).get("name")),
                                             ("orcid", orcid_bare((row.get("contributor") or {}).get("orcid"))),
                                             ("role", "contributed the value")) if v}],
        "flags": {"extraction_accepted": False, "review_state": "contributed_unverified",
                  "contribution_tier": "contributed_unverified", "espei_ready": False, "espei_certified": False,
                  "calphad_check": "not_available"},
    }
    return {k: v for k, v in rec.items() if v is not None}


def validate_data(path, rel, rep, seen):
    f = relpath(path, rel.root)
    out = []
    for line, row in read_data_file(path, rep, f):
        if not isinstance(row, dict):
            rep.error(f, line, "each value must be an object")
            continue
        n0 = len(rep.errors)
        t = row.get("contribution_type")
        if t not in ("B", "C", "D"):
            rep.error(f, line, "contribution_type must be B (values you read from a paper), C (new measurements with "
                               "a citable DOI) or D (calculated data); A and E have their own folders")
            continue
        check_contributor(row.get("contributor"), rep, f, line)
        check_consent(row.get("licence_consent"), rep, f, line)
        system = row.get("system")
        if not system_ok(system):
            rep.error(f, line, "system must be element symbols, uppercase, sorted, joined by '-' (e.g. CU-ZR), got %r" % system)
            continue
        els = system_elements(system)
        prop = row.get("property")
        spec = PROPERTIES.get(prop)
        if spec is None:
            rep.error(f, line, "property %r is not one of the contributable codes %s" % (prop, sorted(PROPERTIES)))
            continue
        unit = row.get("unit")
        if spec[0] is not None:
            if unit != spec[0]:
                rep.error(f, line, "unit of %s must be %r (the release unit; give the printed unit in unit_printed), got %r"
                          % (prop, spec[0], unit))
            check_value(prop, spec[0], row.get("value"), rep, f, line)
        st = row.get("state")
        if not isinstance(st, dict):
            rep.error(f, line, "state is required: phases, temperature_K, pressure_Pa, composition, reference state")
            continue
        # the value as an equilibrium state
        phases = st.get("phases") or []
        if not phases or not all(isinstance(p, dict) and str(p.get("label") or "").strip() for p in phases):
            rep.error(f, line, "state.phases: the phase(s) of the state, each {label (as printed), model_phase (optional)}")
            phases = [p for p in phases if isinstance(p, dict)]
        tdb = rel.tdb_phases(system)
        for p in phases:
            mp = p.get("model_phase")
            if mp and tdb and str(mp).upper() not in tdb:
                rep.error(f, line, "model_phase %r is not a phase of the %s TDB files (%s)" % (mp, system, ", ".join(sorted(tdb))))
        T = st.get("temperature_K")
        if prop in TEMPERATURE_PROPS:
            if T is not None and num(T) is not None and num(row.get("value")) is not None and abs(num(T) - num(row["value"])) > 1e-6:
                rep.error(f, line, "state.temperature_K differs from the value of a %s" % prop)
        elif num(T) is None or not (1.0 < num(T) <= 6000.0):
            rep.error(f, line, "state.temperature_K is required (K; 298.15 for standard values), got %r" % T)
        P = st.get("pressure_Pa")
        if P is not None and (num(P) is None or num(P) <= 0):
            rep.error(f, line, "state.pressure_Pa must be positive (Pa)")
        if st.get("overall_composition") is not None:
            check_composition(st["overall_composition"], els, "state.overall_composition", rep, f, line)
        for i, pc in enumerate(st.get("phase_compositions") or []):
            if not isinstance(pc, dict) or not pc.get("phase"):
                rep.error(f, line, "state.phase_compositions[%d]: {phase, composition} required" % i)
                continue
            check_composition(pc.get("composition"), els, "state.phase_compositions[%d]" % i, rep, f, line)
        if prop == "PHASE_COMPOSITION" and not st.get("phase_compositions"):
            rep.error(f, line, "PHASE_COMPOSITION needs state.phase_compositions")
        if prop in TEMPERATURE_PROPS and len(els) >= 2 and len(phases) < 2:
            rep.error(f, line, "a reaction / transition needs the phases taking part (state.phases)")
        rx = st.get("reaction") or {}
        if rx.get("type") and rx["type"] not in TRANSITION_KINDS:
            rep.error(f, line, "state.reaction.type must be one of %s" % list(TRANSITION_KINDS))
        if prop.endswith("_FORM") or prop.endswith("_MIX") or prop in ("PARTIAL_ENTHALPY", "CHEMICAL_POTENTIAL"):
            rs = st.get("reference_state")
            if not isinstance(rs, dict) or not rs:
                rep.error(f, line, "state.reference_state is required for %s: {ELEMENT: {phase}} for every element" % prop)
            else:
                for el in els:
                    if not isinstance(rs.get(el), dict) or not rs[el].get("phase"):
                        rep.error(f, line, "state.reference_state.%s: {phase: ...} required" % el)
                for el in rs:
                    if el not in els:
                        rep.error(f, line, "state.reference_state: %s is not in the system" % el)
        if prop not in TEMPERATURE_PROPS and prop not in ("PHASE_ASSEMBLAGE",) and len(els) >= 2 \
                and not st.get("overall_composition") and not st.get("phase_compositions"):
            rep.error(f, line, "state: the composition is required (overall_composition or phase_compositions)")
        # evidence class and method
        ec = row.get("evidence_class")
        if t in ("B", "C") and ec not in ("experimental", "model", "dft", "unspecified"):
            rep.error(f, line, "evidence_class must be one of %s" % list(EVIDENCE_CLASSES))
        if t == "C" and ec != "experimental":
            rep.error(f, line, "type C (new measurements) is experimental; calculated values are type D")
        if t == "D" and ec not in CALCULATED_CLASSES:
            rep.error(f, line, "type D (calculated) needs evidence_class dft or model; it is never mixed with experiment")
        m = row.get("method") or {}
        if t in ("C", "D") and not str(m.get("kind") or "").strip():
            rep.error(f, line, "method.kind is required for type %s (e.g. drop calorimetry, DTA, EPMA; VASP-PBE)" % t)
        if t == "D":
            need = ("code", "functional") if ec == "dft" else ("software", "tdb_or_model")
            miss = [k for k in need if not str(m.get(k) or "").strip()]
            if miss:
                rep.error(f, line, "type D %s method metadata missing: method.%s" % (ec, ", method.".join(miss)))
        # provenance
        prov = row.get("provenance") or {}
        doi, ddoi = prov.get("doi"), prov.get("dataset_doi")
        for k, d in (("doi", doi), ("dataset_doi", ddoi)):
            if d and not DOI_RE.match(norm_doi(d)):
                rep.error(f, line, "provenance.%s %r is not a DOI (10.xxxx/...)" % (k, d))
        if t == "B":
            if not doi:
                rep.error(f, line, "type B needs provenance.doi (the paper the value was read from)")
            check_page(prov.get("page"), rep, f, line, "provenance.page")
            check_quote(prov.get("quote"), rep, f, line)
        elif t in ("C", "D"):
            if not (doi or ddoi):
                rep.error(f, line, "type %s needs a citable DOI: provenance.doi (published paper) or provenance.dataset_doi "
                                   "(deposit unpublished data first, e.g. on Zenodo, and cite its DOI)" % t)
            if prov.get("quote"):
                check_quote(prov.get("quote"), rep, f, line, required=False)
        # uncertainty components (names of the release's uncertainty_budget)
        unc = row.get("uncertainty") or {}
        if not isinstance(unc, dict):
            rep.error(f, line, "uncertainty must be an object of components %s" % list(UNCERTAINTY_COMPONENTS))
            unc = {}
        for k, c in unc.items():
            if k not in UNCERTAINTY_COMPONENTS:
                rep.error(f, line, "uncertainty.%s: unknown component; use %s (sigma_reading and sigma_effective are "
                                   "computed by ORCHID)" % (k, list(UNCERTAINTY_COMPONENTS)))
                continue
            v = num((c or {}).get("value")) if isinstance(c, dict) else None
            if v is None or v < 0:
                rep.error(f, line, "uncertainty.%s.value must be a number >= 0 in the value's unit" % k)
        if t == "C" and not unc.get("sigma_printed") and not unc.get("sigma_method"):
            rep.warn(f, line, "type C without sigma_printed or sigma_method: the release will use the method-class floor")
        if len(rep.errors) > n0:
            continue
        rec = to_record(row, f, line)
        # duplicates: within the contribution set and against the release
        key = dup_key(rec)
        if key in seen:
            rep.error(f, line, "duplicate of %s in this contribution" % seen[key])
        seen[key] = "%s:%d" % (f, line)
        hit = release_duplicate(rec, rel)
        if hit == rec["id"]:
            rep.info(f, line, "already released as %s" % hit)
        elif hit:
            rep.error(f, line, "already in the release as %s (same system, property, state, value and source); "
                               "to change it, send a correction instead" % hit)
        if doi and norm_doi(doi) in rel.paper_dois and t == "B":
            rep.info(f, line, "the paper is already in the ORCHID corpus; this value is checked against its records")
        # physical phase rule of the release (ESPEI usability; liquid / temperature impossibilities are errors)
        rule = rel.rule
        if rule is None:
            rep.info(f, line, "phase rule not run: %s" % rel._rule_error)
        else:
            res = rule.classify(rec)
            if res.get("result") == "fail":
                if res.get("reason") in ("liquid_impossible_at_T", "temperature_implausible"):
                    rep.error(f, line, "physical phase rule: %s (%s)" % (res["reason"], res.get("detail")))
                else:
                    rep.warn(f, line, "not ESPEI-ready under the release phase rule: %s (%s)"
                             % (res.get("reason"), res.get("detail")))
            else:
                rep.info(f, line, "physical phase rule of the release: %s (%s)" % (res.get("result"), ", ".join(
                    "%s -> %s" % (p.get("label"), p.get("registry_id") or p.get("kind")) for p in res.get("phases") or []) or res.get("basis")))
        out.append(rec)
    return out


def dup_key(rec):
    return (rec.get("system"), rec.get("property"), round(num(rec.get("value")) or 0.0, 6),
            round(num(rec.get("temperature_K")) or 0.0, 2), canon(sorted(p.get("label") or "" for p in rec.get("phases") or [])),
            rec.get("paper"))


def release_duplicate(rec, rel):
    v, T = num(rec.get("value")), num(rec.get("temperature_K"))
    labels = sorted((p.get("label") or "").lower() for p in rec.get("phases") or [])
    if rec["id"] in rel.records:
        return rec["id"]
    for r in rel.by_system(rec.get("system")):
        if r.get("property") != rec.get("property") or r.get("paper") != rec.get("paper") or rec.get("paper") is None:
            continue
        rv, rT = num(r.get("value")), num(r.get("temperature_K"))
        if v is not None and rv is not None and abs(v - rv) > max(1e-6, 1e-4 * abs(v)):
            continue
        if T is not None and rT is not None and abs(T - rT) > 0.5:
            continue
        if labels and sorted((p.get("label") or "").lower() for p in r.get("phases") or []) != labels:
            continue
        return r["id"]
    return None


# ------------------------------------------------------------------------------ type A and type E --
def validate_papers(path, rel, rep, seen):
    f = relpath(path, rel.root)
    for line, row in read_jsonl(path, rep, f):
        dois = row.get("dois") or ([row["doi"]] if row.get("doi") else [])
        if not dois:
            rep.error(f, line, "doi (or dois) is required")
        for d in dois:
            nd = norm_doi(d)
            if not DOI_RE.match(nd):
                rep.error(f, line, "%r is not a DOI" % d)
                continue
            if nd in seen:
                rep.warn(f, line, "DOI %s already suggested (%s)" % (nd, seen[nd]))
            seen[nd] = "%s:%d" % (f, line)
            if nd in rel.paper_dois:
                rep.info(f, line, "DOI %s is already in the ORCHID corpus" % nd)
        for s in row.get("systems") or ([row["system"]] if row.get("system") else []):
            if not system_ok(s):
                rep.error(f, line, "system %r: element symbols, uppercase, sorted, joined by '-'" % s)
        for dt in row.get("data_types") or []:
            if dt not in DATA_TYPES:
                rep.error(f, line, "data_types: %r is not one of %s" % (dt, list(DATA_TYPES)))
        if row.get("contributor") is not None:
            check_contributor(row["contributor"], rep, f, line)
        extra = set(row) - {"doi", "dois", "system", "systems", "data_types", "why", "contributor", "issue", "suggested"}
        if extra:
            rep.error(f, line, "unexpected field(s) %s" % sorted(extra))


def validate_tdb(path, rel, rep, seen):
    f = relpath(path, rel.root)
    try:
        m = json.load(open(path, encoding="utf-8"))
    except ValueError as exc:
        rep.error(f, None, "not valid JSON: %s" % exc)
        return
    if m.get("contribution_type") != "E":
        rep.error(f, None, 'contribution_type must be "E"')
    if m.get("licence") not in TDB_LICENCES:
        rep.error(f, None, "licence is required and must be one of %s (SPDX id); ORCHID only redistributes openly "
                           "licensed TDB files" % list(TDB_LICENCES))
    if m.get("licence_holder") in (None, ""):
        rep.error(f, None, "licence_holder: who holds the rights (you, your institution, the journal, ...)")
    if not m.get("rights_confirmed") is True:
        rep.error(f, None, "rights_confirmed must be true: you have the right to release this file under the licence")
    check_contributor(m.get("contributor"), rep, f, None)
    system = m.get("system")
    if not system_ok(system):
        rep.error(f, None, "system %r: element symbols, uppercase, sorted, joined by '-'" % system)
        return
    d = m.get("assessment_doi")
    if not d or not DOI_RE.match(norm_doi(d)):
        rep.error(f, None, "assessment_doi: the DOI of the paper that publishes the assessment is required")
    tdbf = os.path.join(os.path.dirname(path), str(m.get("tdb_file") or ""))
    if not m.get("tdb_file") or not os.path.isfile(tdbf):
        rep.error(f, None, "tdb_file %r not found next to metadata.json" % m.get("tdb_file"))
        return
    text = open(tdbf, encoding="utf-8", errors="replace").read()
    els = {x.upper() for x in re.findall(r"(?im)^\s*ELEM(?:ENT)?\s+(\S+)", text)} - {"/-", "VA"}
    phases = re.findall(r"(?im)^\s*PHASE\s+(\S+)", text)
    if not phases:
        rep.error(f, None, "the TDB file has no PHASE statements")
    missing = set(system_elements(system)) - els
    if missing:
        rep.error(f, None, "the TDB file does not define element(s) %s of the system" % sorted(missing))
    if len(text.encode()) > 20 * 1024 * 1024:
        rep.error(f, None, "the TDB file is larger than 20 MB")
    sha = hashlib.sha256(open(tdbf, "rb").read()).hexdigest()
    if m.get("sha256") and m["sha256"] != sha:
        rep.error(f, None, "sha256 in metadata.json does not match the file (%s)" % sha)
    if sha in seen:
        rep.error(f, None, "the same TDB file is already contributed (%s)" % seen[sha])
    seen[sha] = f
    try:   # optional: the TDB must load in pycalphad when pycalphad is installed
        from pycalphad import Database  # type: ignore
        Database(tdbf)
    except ImportError:
        rep.info(f, None, "pycalphad not installed: TDB parsed for ELEMENT / PHASE statements only")
    except Exception as exc:
        rep.error(f, None, "pycalphad cannot read the TDB file: %s" % str(exc)[:200])


# --------------------------------------------------------------------------------- contributors --
def validate_contributors(path, rel, rep):
    f = relpath(path, rel.root)
    try:
        d = json.load(open(path, encoding="utf-8"))
    except ValueError as exc:
        rep.error(f, None, "not valid JSON: %s" % exc)
        return
    names = set()
    for i, c in enumerate(d.get("contributors") or [], 1):
        if not str(c.get("name") or "").strip():
            rep.error(f, None, "contributors[%d]: name required" % i)
        if c.get("orcid") and not orcid_ok(c["orcid"]):
            rep.error(f, None, "contributors[%d]: invalid ORCID %r" % (i, c["orcid"]))
        if c.get("name") in names:
            rep.error(f, None, "contributors[%d]: %s listed twice" % (i, c.get("name")))
        names.add(c.get("name"))
        if not isinstance(c.get("credit_opt_in"), bool):
            rep.error(f, None, "contributors[%d]: credit_opt_in must be true or false" % i)
        bad = set(c) - {"name", "orcid", "github", "affiliation", "credit_opt_in", "roles", "contributions", "since"}
        if bad:
            rep.error(f, None, "contributors[%d]: unexpected field(s) %s" % (i, sorted(bad)))


# ------------------------------------------------------------------------------------ dispatcher --
def read_jsonl(path, rep, f):
    out = []
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except ValueError as exc:
                rep.error(f, i, "not valid JSON: %s" % exc)
                continue
            if not isinstance(row, dict):
                rep.error(f, i, "each line must be a JSON object")
                continue
            out.append((i, row))
    return out


def relpath(path, root):
    try:
        return os.path.relpath(path, root).replace(os.sep, "/")
    except ValueError:
        return path


def kind_of(path, root):
    r = relpath(os.path.abspath(path), root)
    base = os.path.basename(r)
    if base.startswith("TEMPLATE") or base.startswith("README") or base.endswith(".md"):
        return None
    if r == "contributors.json":
        return "contributors"
    if r.startswith("contributions/corrections/") and r.endswith(".jsonl"):
        return "corrections"
    if r.startswith("contributions/data/") and (r.endswith(".json") or r.endswith(".csv")):
        return "data"
    if r.startswith("contributions/papers/") and r.endswith(".jsonl"):
        return "papers"
    if r.startswith("contributions/tdb/") and base == "metadata.json":
        return "tdb"
    return None


def all_files(root):
    pats = ["contributions/corrections/*.jsonl", "contributions/data/*.json", "contributions/data/*.csv",
            "contributions/papers/*.jsonl", "contributions/tdb/*/metadata.json", "contributors.json"]
    out = []
    for p in pats:
        out += glob.glob(os.path.join(root, p))
    return sorted(out)


def changed_files(root, base):
    r = subprocess.run(["git", "-C", root, "diff", "--name-only", "--diff-filter=ACMR", "%s...HEAD" % base],
                       capture_output=True, text=True, check=True)
    out = []
    for name in r.stdout.split():
        p = os.path.join(root, name)
        if name.startswith("contributions/tdb/") and not name.endswith("metadata.json"):
            p = os.path.join(root, os.path.dirname(name), "metadata.json")
        if os.path.exists(p) and p not in out:
            out.append(p)
    return out


def validate(paths, rel, rep):
    seen_corr, seen_data, seen_pap, seen_tdb = {}, {}, {}, {}
    records = []
    for p in paths:
        k = kind_of(p, rel.root)
        if k == "corrections":
            validate_corrections(p, rel, rep, seen_corr)
        elif k == "data":
            records += validate_data(p, rel, rep, seen_data)
        elif k == "papers":
            validate_papers(p, rel, rep, seen_pap)
        elif k == "tdb":
            validate_tdb(p, rel, rep, seen_tdb)
        elif k == "contributors":
            validate_contributors(p, rel, rep)
    return records


# ---------------------------------------------------------------------- acceptance (next release) --
def accepted_check_key(record_id, field):
    """Key of the maintainer's page check in tools/literature_visual_checks.json for an accepted correction."""
    return "contributed_correction:%s:%s" % (record_id, field)


def apply_corrections(records, corrections, visual_checks):
    """Apply accepted corrections to release records (dict id -> record), in place; return the applied keys.

    A correction is accepted when the maintainers' page check `contributed_correction:<id>:<field>` exists in the
    visual checks with verdict `confirmed`. The value before is kept in `corrections[]` (gate `contributed`,
    with the contributor) and the contributor is added to the record's `contributors`; nothing is overwritten
    silently and the original stays in the record's history.
    """
    applied = []
    for c in corrections:
        key = accepted_check_key(c["record_id"], c["field"])
        chk = visual_checks.get(key)
        rec = records.get(c["record_id"])
        if not chk or chk.get("verdict") != "confirmed" or rec is None:
            continue
        before = current_value(rec, c["field"])
        if not same(before, c["old"]):
            continue
        new = c["new"]
        if c["field"] == "phases":
            old_ph = {p.get("label"): p for p in rec.get("phases") or []}
            rec["phases_stored"] = rec.get("phases")
            rec["phases"] = [old_ph.get(lb, {"label": lb, "label_source": "contributed_correction"}) for lb in new]
        elif c["field"] == "phase_compositions":
            rec["phase_compositions"] = [dict(pc, basis="mole_fraction", composition_source="contributed_correction") for pc in new]
        elif c["field"] == "extraction_accepted":
            rec.setdefault("flags", {})["extraction_accepted"] = False
            rec["flags"]["espei_ready"] = False
            rec["flags"]["espei_certified"] = False
        elif "." in c["field"]:
            a, b = c["field"].split(".", 1)
            rec.setdefault(a, {})[b] = new
        else:
            rec[c["field"]] = new
        who = {k: v for k, v in (("name", c["contributor"].get("name")), ("orcid", orcid_bare(c["contributor"].get("orcid"))),
                                 ("role", "corrected %s" % c["field"])) if v}
        rec.setdefault("corrections", []).append({
            "gate": "contributed", "field": c["field"], "before": before, "after": new,
            "rule": "contributed_correction", "evidence": {"page": c["evidence"].get("page"), "quote": c["evidence"].get("quote")},
            "contributor": who,
            "visual_check": {k: chk[k] for k in ("page", "pdf_sha256_prefix", "image_sha256", "verdict", "seen", "checked") if chk.get(k) is not None}})
        if who not in rec.setdefault("contributors", []):
            rec["contributors"].append(who)
        applied.append(key)
    return applied


# ---------------------------------------------------------------------------------------- credit --
CREDIT_BEGIN = "<!-- contributors:begin (written by contributions/tools/orchid_contrib.py credit) -->"
CREDIT_END = "<!-- contributors:end -->"
MAINTAINER_FAMILY = ("Arróyave", "Saal", "Shin")


def load_contributors(data):
    p = os.path.join(data, "contributors.json")
    if not os.path.exists(p):
        return []
    return [c for c in json.load(open(p, encoding="utf-8")).get("contributors") or []]


def contributors_md(contribs):
    lines = [CREDIT_BEGIN, "", "| Name | ORCID | Contributions |", "|---|---|---|"]
    for c in sorted(contribs, key=lambda c: c["name"].lower()):
        o = orcid_bare(c.get("orcid"))
        lines.append("| %s | %s | %s |" % (c["name"].replace("|", "/"), "[%s](https://orcid.org/%s)" % (o, o) if o else "",
                                           ", ".join(c.get("roles") or []) or "contributor"))
    if not contribs:
        lines.append("| (none yet) | | |")
    lines += ["", CREDIT_END]
    return "\n".join(lines)


def zenodo_contributor(c):
    e = {"name": ", ".join(reversed(c["name"].rsplit(" ", 1))) if " " in c["name"] else c["name"],
         "type": "DataCurator" if set(c.get("roles") or []) <= {"corrections", "reviews"} else "DataCollector"}
    if c.get("affiliation"):
        e["affiliation"] = c["affiliation"]
    if orcid_bare(c.get("orcid")):
        e["orcid"] = orcid_bare(c["orcid"])
    return e


def credit_outputs(data):
    """{relative path: new text} for CONTRIBUTORS.md, CITATION.cff and the Zenodo metadata files.

    Opt-in only (credit_opt_in: true). Zenodo: `contributors` (DataCurator for corrections / reviews, DataCollector
    otherwise). CITATION.cff (CFF 1.2 has no contributor role): opted-in contributors are listed after the
    maintainers as authors only when the PI policy `cff_authors` in contributors.json is true; otherwise CITATION.cff
    is left unchanged and credit is given in Zenodo and CONTRIBUTORS.md.
    """
    p = os.path.join(data, "contributors.json")
    cfg = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    contribs = cfg.get("contributors") or []
    opted = [c for c in contribs if c.get("credit_opt_in") is True]
    out = {}
    md_path = os.path.join(data, "CONTRIBUTORS.md")
    if os.path.exists(md_path):
        md = open(md_path, encoding="utf-8").read()
        if CREDIT_BEGIN in md and CREDIT_END in md:
            a, rest = md.split(CREDIT_BEGIN, 1)
            _, b = rest.split(CREDIT_END, 1)
            out["CONTRIBUTORS.md"] = a + contributors_md(contribs) + b
    zc = [zenodo_contributor(c) for c in sorted(opted, key=lambda c: c["name"].lower())]
    for zp in [".zenodo.json"] + sorted(relpath(x, data) for x in glob.glob(os.path.join(data, "zenodo", "*.metadata.json"))):
        full = os.path.join(data, zp)
        if not os.path.exists(full):
            continue
        txt = open(full, encoding="utf-8").read()
        d = json.loads(txt)
        meta = d.get("metadata") if isinstance(d.get("metadata"), dict) else d
        if (meta.get("contributors") or []) == zc:
            continue    # unchanged: leave the file's bytes alone
        if zc:
            meta["contributors"] = zc
        else:
            del meta["contributors"]
        lines = txt.split("\n")
        indent = (len(lines[1]) - len(lines[1].lstrip(" "))) or None if len(lines) > 1 else None
        new = json.dumps(d, ensure_ascii="\\u" in txt, indent=indent) + ("\n" if txt.endswith("\n") else "")
        out[zp] = new
    cff = os.path.join(data, "CITATION.cff")
    if os.path.exists(cff) and cfg.get("cff_authors") is True:
        txt = open(cff, encoding="utf-8").read()
        txt = re.sub(r"\n  # contributors:begin.*?# contributors:end", "", txt, flags=re.S)
        block = ["  # contributors:begin (opt-in; contributions/tools/orchid_contrib.py credit)"]
        for c in sorted(opted, key=lambda c: c["name"].lower()):
            given, _, family = c["name"].rpartition(" ")
            block.append('  - family-names: "%s"' % (family or c["name"]).replace('"', "'"))
            if given:
                block.append('    given-names: "%s"' % given.replace('"', "'"))
            if orcid_bare(c.get("orcid")):
                block.append('    orcid: "https://orcid.org/%s"' % orcid_bare(c["orcid"]))
            if c.get("affiliation"):
                block.append('    affiliation: "%s"' % c["affiliation"].replace('"', "'"))
        block.append("  # contributors:end")
        if len(block) > 2:
            txt = re.sub(r"(\nauthors:\n(?:  .*\n|    .*\n)+?)(?=[a-z])", lambda m: m.group(1) + "\n".join(block) + "\n", txt, count=1)
        out["CITATION.cff"] = txt
    return out


def cmd_credit(a):
    stale = []
    for rp, txt in sorted(credit_outputs(a.data).items()):
        full = os.path.join(a.data, rp)
        cur = open(full, encoding="utf-8").read() if os.path.exists(full) else None
        if cur != txt:
            stale.append(rp)
            if not a.check:
                open(full, "w", encoding="utf-8").write(txt)
    if a.check:
        if stale:
            print("credit: stale %s (run: python3 contributions/tools/orchid_contrib.py credit)" % ", ".join(stale))
            return 1
        print("credit: up to date")
        return 0
    print("credit: wrote %s" % (", ".join(stale) or "nothing (up to date)"))
    return 0


# ------------------------------------------------------------------------------------------- CLI --
def cmd_validate(a):
    rel = Release(a.release_data or a.data, a.release_tools, a.data)
    if a.files:
        paths = [os.path.abspath(p) for p in a.files]
    elif a.changed_from:
        paths = changed_files(a.data, a.changed_from)
    else:
        paths = all_files(a.data)
    rep = Report()
    if a.require_release_tools and rel.rule is None:
        rep.error("contributions", None, rel._rule_error)
    records = validate(paths, rel, rep)
    github = bool(os.environ.get("GITHUB_ACTIONS"))
    txt = rep.render(github)
    if txt:
        print(txt)
    print("validated %d file(s): %d error(s), %d warning(s), %d contributed value(s) converted"
          % (len(paths), len(rep.errors), sum(1 for i in rep.items if i[0] == "warning"), len(records)))
    if a.json:
        json.dump({"files": [relpath(p, rel.root) for p in paths], "items": [dict(zip(("level", "file", "line", "message"), i)) for i in rep.items],
                   "records": records}, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    return 1 if rep.errors else 0


def cmd_convert(a):
    rel = Release(a.release_data or a.data, a.release_tools, a.data)
    rep = Report()
    for p in a.files:
        for r in validate_data(os.path.abspath(p), rel, rep, {}):
            print(canon(r))
    if rep.items:
        print(rep.render(), file=sys.stderr)
    return 1 if rep.errors else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("files", nargs="*")
    v.add_argument("--changed-from", help="validate the contribution files changed since this git ref")
    v.add_argument("--json", help="write the report and the converted records to this file")
    v.add_argument("--require-release-tools", action="store_true")
    c = sub.add_parser("credit")
    c.add_argument("--check", action="store_true")
    k = sub.add_parser("convert")
    k.add_argument("files", nargs="+")
    for p in (v, c, k):
        p.add_argument("--data", default=DATA_ROOT, help="the orchid-data repository with the contribution files (default: this one)")
        p.add_argument("--release-data", help="the released data to check against (default: --data)")
        p.add_argument("--release-tools", default=os.environ.get("ORCHID_RELEASE_TOOLS") or
                       os.path.join(os.path.dirname(DATA_ROOT), "orchid-project.org", "tools"))
    a = ap.parse_args(argv)
    return {"validate": cmd_validate, "credit": cmd_credit, "convert": cmd_convert}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
