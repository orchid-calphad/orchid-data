"""Tests of the contribution checks (contributions/tools/orchid_contrib.py) on a small synthetic release.

Runs without the full data release; when the release tools of orchid-project.org are found (ORCHID_RELEASE_TOOLS
or ../orchid-project.org/tools) the physical phase rule tests run as well.
"""
import gzip
import json
import os
import shutil
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRIB = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(CONTRIB, "tools"))
import orchid_contrib as oc  # noqa: E402

TOOLS = os.environ.get("ORCHID_RELEASE_TOOLS") or os.path.join(os.path.dirname(os.path.dirname(CONTRIB)),
                                                               "orchid-project.org", "tools")
HAVE_TOOLS = os.path.exists(os.path.join(TOOLS, "phase_rule.py"))
EXAMPLES = os.path.join(CONTRIB, "examples")
WHO = {"name": "Example Contributor", "orcid": "0000-0002-1825-0097"}

RECORDS = [
    {"id": "ORC-RZXYDDJGWB", "system": "AG-AL", "property": "PHASE_COMPOSITION", "observation_type": "phase_region_vertex_set",
     "temperature_K": 590.15, "paper": "doi:10.1016/j.jallcom.2004.04.126", "locator": {"page": 2, "row": 1},
     "phases": [{"label": "ζ"}], "phase_compositions": [{"phase": "ζ", "composition": {"AG": 0.6192, "AL": 0.3808}}],
     "evidence_class": "experimental", "flags": {"extraction_accepted": True}},
    {"id": "ORC-HFORMCUZR2", "system": "CU-ZR", "property": "HM_FORM", "observation_type": "equilibrium_property",
     "value": -15.0, "unit": "kJ/mol-atom", "temperature_K": 298.15, "paper": "doi:10.1000/paper.one",
     "quote": "The enthalpy of formation of CuZr2 is -15.0 kJ/mol.", "quote_page": 4,
     "phases": [{"label": "CuZr2", "model_phase": "CUZR2"}], "evidence_class": "experimental",
     "flags": {"extraction_accepted": True}, "merged_ids": ["ORC-OLDDUPLICATE"]},
]
PHASES = {"system": "CU-ZR", "phases": [
    {"id": "phase:cu-zr:cuzr2", "system": "CU-ZR", "names": [],
     "models": [{"phase_name": "CUZR2", "stoichiometric": True, "composition": {"CU": 1 / 3, "ZR": 2 / 3}}]},
    {"id": "phase:cu-zr:liquid", "system": "CU-ZR", "names": [], "models": [{"phase_name": "LIQUID", "stoichiometric": False}]},
    {"id": "phase:cu-zr:fcc-a1", "system": "CU-ZR", "names": [], "models": [{"phase_name": "FCC_A1", "stoichiometric": False}]},
    {"id": "phase:cu-zr:hcp-a3", "system": "CU-ZR", "names": [], "models": [{"phase_name": "HCP_A3", "stoichiometric": False}]},
]}


@pytest.fixture()
def repo(tmp_path):
    lit = tmp_path / "literature"
    lit.mkdir()
    with gzip.open(lit / "orchid-literature.jsonl.gz", "wt", encoding="utf-8") as fh:
        for r in RECORDS:
            fh.write(json.dumps(r) + "\n")
    (lit / "papers.json").write_text(json.dumps({"doi:10.1000/paper.one": {"doi": "10.1000/paper.one"}}))
    (tmp_path / "phases" / "systems").mkdir(parents=True)
    (tmp_path / "phases" / "systems" / "CU-ZR.json").write_text(json.dumps(PHASES))
    for d in ("corrections", "data", "papers", "tdb"):
        (tmp_path / "contributions" / d).mkdir(parents=True)
    return tmp_path


def run(repo, rel_path, content, tools=False):
    p = repo / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, (list, dict)) and str(rel_path).endswith(".jsonl"):
        content = "\n".join(json.dumps(x, ensure_ascii=False) for x in content) + "\n"
    elif isinstance(content, (list, dict)):
        content = json.dumps(content, ensure_ascii=False)
    p.write_text(content, encoding="utf-8")
    rel = oc.Release(str(repo), TOOLS if tools else None)
    rep = oc.Report()
    recs = oc.validate([str(p)], rel, rep)
    return rep, recs


def msgs(rep, level="error"):
    return " | ".join(m for lv, _, _, m in rep.items if lv == level)


def correction(**kw):
    c = {"record_id": "ORC-RZXYDDJGWB", "field": "temperature_K", "old": 590.15, "new": 591.15,
         "evidence": {"page": 2, "quote": "Table 1 lists 318 °C."}, "contributor": dict(WHO), "licence_consent": "CC-BY-4.0"}
    c.update(kw)
    return c


def value(**kw):
    v = {"contribution_type": "C", "system": "CU-ZR", "property": "HM_FORM", "value": -16.2, "unit": "kJ/mol-atom",
         "state": {"phases": [{"label": "CuZr2", "model_phase": "CUZR2"}], "temperature_K": 298.15, "pressure_Pa": 101325,
                   "overall_composition": {"CU": 0.3333, "ZR": 0.6667},
                   "reference_state": {"CU": {"phase": "FCC_A1"}, "ZR": {"phase": "HCP_A3"}}},
         "evidence_class": "experimental", "method": {"kind": "drop solution calorimetry"},
         "provenance": {"dataset_doi": "10.5281/zenodo.0000000"},
         "uncertainty": {"sigma_printed": {"value": 0.6, "kind": "2 sd"}},
         "contributor": dict(WHO), "licence_consent": "CC-BY-4.0"}
    v.update(kw)
    return v


# ------------------------------------------------------------------------------------------ helpers --
def test_orcid_checksum():
    assert oc.orcid_ok("0000-0002-1825-0097")
    assert oc.orcid_ok("https://orcid.org/0000-0001-7548-8686")
    assert oc.orcid_ok("0000-0002-1694-233X")
    assert not oc.orcid_ok("0000-0002-1825-0098")
    assert not oc.orcid_ok("0000-0002-1825")


def test_system_and_doi():
    assert oc.system_ok("CU-ZR") and not oc.system_ok("ZR-CU") and not oc.system_ok("CU-XX") and not oc.system_ok("Cu-Zr")
    assert oc.norm_doi("https://doi.org/10.1000/ABC") == "10.1000/abc"


# -------------------------------------------------------------------------------------- corrections --
def test_valid_correction(repo):
    rep, _ = run(repo, "contributions/corrections/a.jsonl", [correction()])
    assert not rep.errors, msgs(rep)


def test_correction_errors(repo):
    rows = [correction(record_id="ORC-NOPE"),
            correction(field="method", old="EDX", new="WDS"),
            correction(old=600.0),
            correction(new=-5.0),
            correction(evidence={"page": "two", "quote": "x" * 241}),
            correction(contributor={"name": "A", "email": "a@b.c"}),
            correction(licence_consent="yes")]
    rep, _ = run(repo, "contributions/corrections/a.jsonl", rows)
    m = msgs(rep)
    for needle in ("not in the release", "cannot be corrected", "does not match the release value", "(1, 6000]",
                   "printed page number", "at most 240", "personal data", "licence_consent"):
        assert needle in m, needle


def test_correction_duplicate_merged_and_applied(repo):
    rows = [correction(), correction(),
            correction(record_id="ORC-OLDDUPLICATE", field="value", old=-15.0, new=-14.0),
            correction(old=589.0, new=590.15)]
    rep, _ = run(repo, "contributions/corrections/a.jsonl", rows)
    m = msgs(rep)
    assert "duplicate correction" in m and "merged into ORC-HFORMCUZR2" in m
    assert "already applied" in msgs(rep, "notice")


def test_correction_value_range_and_sign(repo):
    rows = [{**correction(), "record_id": "ORC-HFORMCUZR2", "field": "value", "old": -15.0, "new": 15.0,
             "evidence": {"page": 4, "quote": "The enthalpy of formation of CuZr2 is 15.0 kJ/mol."}},
            {**correction(), "record_id": "ORC-HFORMCUZR2", "field": "unit", "old": "kJ/mol-atom", "new": "kJ/mol",
             "evidence": {"page": 4, "quote": "per mole of formula unit"}}]
    rep, _ = run(repo, "contributions/corrections/a.jsonl", rows)
    assert not rep.errors, msgs(rep)
    w = msgs(rep, "warning")
    assert "positive" in w and "changes the sign" in w and "not the release unit" in w


def test_correction_phase_compositions(repo):
    bad = correction(field="phase_compositions", old=[{"phase": "ζ", "composition": {"AG": 0.6192, "AL": 0.3808}}],
                     new=[{"phase": "ζ", "composition": {"AG": 0.7, "CU": 0.3}}])
    rep, _ = run(repo, "contributions/corrections/a.jsonl", [bad])
    assert "CU is not in the chemical system" in msgs(rep)


# ------------------------------------------------------------------------------------------ new data --
def test_valid_data_and_conversion(repo):
    rep, recs = run(repo, "contributions/data/a.json", {"records": [value()]})
    assert not rep.errors, msgs(rep)
    (r,) = recs
    assert r["id"].startswith("ORC-C") and r["source"] == "contributed"
    assert r["flags"]["review_state"] == "contributed_unverified" and r["flags"]["extraction_accepted"] is False
    assert r["contributors"][0]["orcid"] == "0000-0002-1825-0097"
    assert r["uncertainty"] == {"value": 0.6, "basis": "printed", "note": "2 sd"}
    assert r["reference_state"]["ZR"]["phase"] == "HCP_A3"
    assert oc.contribution_id(value()) == r["id"]   # deterministic


def test_data_errors(repo):
    st = value()["state"]
    rows = [value(unit="J/mol"), value(value=-900.0), value(system="ZR-CU"),
            value(state={**st, "reference_state": None}),
            value(state={**st, "overall_composition": {"CU": 0.5, "NI": 0.5}}),
            value(state={**st, "phases": [{"label": "CuZr2", "model_phase": "CUZR3"}]}),
            value(state={k: v for k, v in st.items() if k != "temperature_K"}),
            value(provenance={}),
            value(contribution_type="B", provenance={"doi": "10.1000/x"}),
            value(contribution_type="D", evidence_class="dft", method={"kind": "DFT"}),
            value(contribution_type="D", evidence_class="experimental"),
            value(uncertainty={"sigma_effective": {"value": 1}}),
            value(contribution_type="Z")]
    rep, _ = run(repo, "contributions/data/a.json", rows)
    m = msgs(rep)
    for needle in ("unit of HM_FORM must be", "outside the plausible range", "system must be", "reference_state is required",
                   "NI is not in the chemical system", "not a phase of the CU-ZR TDB", "temperature_K is required",
                   "citable DOI", "printed page number", "quote: the sentence", "method.code, method.functional",
                   "type D (calculated) needs evidence_class", "unknown component", "contribution_type must be"):
        assert needle in m, needle


def test_duplicates(repo):
    dup_release = value(contribution_type="B", value=-15.0, provenance={"doi": "10.1000/paper.one", "page": 4,
                                                                         "quote": "The enthalpy of formation of CuZr2 is -15.0 kJ/mol."})
    rep, _ = run(repo, "contributions/data/a.json", [value(), value(note="same value again"), dup_release])
    m = msgs(rep)
    assert "duplicate of contributions/data/a.json:1" in m
    assert "already in the release as ORC-HFORMCUZR2" in m


def test_csv_template_row(repo):
    head = ",".join(oc.CSV_COLUMNS)
    row = ('C,CU-ZR,HM_FORM,-16.2,kJ/mol-atom,,,298.15,101325,CuZr2=CUZR2,,,CU:0.3333;ZR:0.6667,,CU:FCC_A1;ZR:HCP_A3,'
           'experimental,drop solution calorimetry,,,10.5281/zenodo.0000000,,,,,0.6,2 sd,,,,,Example Contributor,'
           '0000-0002-1825-0097,CC-BY-4.0')
    rep, recs = run(repo, "contributions/data/a.csv", head + "\n" + row + "\n")
    assert not rep.errors, msgs(rep)
    assert recs[0]["phases"] == [{"label": "CuZr2", "model_phase": "CUZR2"}]
    assert recs[0]["id"] == oc.contribution_id(oc.csv_row_to_json(dict(zip(oc.CSV_COLUMNS, row.split(",")))))


def test_templates_are_skipped(repo):
    assert oc.kind_of(str(repo / "contributions/data/TEMPLATE.json"), str(repo)) is None
    assert oc.kind_of(str(repo / "contributions/data/x.json"), str(repo)) == "data"


@pytest.mark.skipif(not HAVE_TOOLS, reason="release tools (orchid-project.org/tools) not available")
def test_phase_rule_liquid_impossible(repo):
    liq = value(contribution_type="C", property="HM_MIX", value=-5.0,
                state={"phases": [{"label": "liquid"}], "temperature_K": 300.0, "overall_composition": {"CU": 0.5, "ZR": 0.5},
                       "reference_state": {"CU": {"phase": "LIQUID"}, "ZR": {"phase": "LIQUID"}}})
    rep, _ = run(repo, "contributions/data/a.json", [liq], tools=True)
    assert "liquid_impossible_at_T" in msgs(rep)
    rep, _ = run(repo, "contributions/data/b.json", [value()], tools=True)
    assert not rep.errors and "phase rule of the release: pass" in msgs(rep, "notice")


# --------------------------------------------------------------------------------- types A and E --
def test_paper_suggestions(repo):
    rows = [{"doi": "10.1000/new.paper", "system": "CU-ZR", "data_types": ["formation enthalpy"], "why": "calorimetry"},
            {"doi": "10.1000/paper.one"}, {"doi": "not-a-doi", "system": "ZR-CU", "data_types": ["gossip"]}]
    rep, _ = run(repo, "contributions/papers/queue.jsonl", rows)
    m = msgs(rep)
    assert "not a DOI" in m and "sorted" in m and "data_types" in m and m.count("|") == 2
    assert "already in the ORCHID corpus" in msgs(rep, "notice")


def test_tdb_contribution(repo):
    d = repo / "contributions/tdb/cu-zr-example"
    d.mkdir(parents=True)
    (d / "CuZr-example.tdb").write_text("ELEMENT CU FCC_A1 63.546 0 0 !\nELEMENT ZR HCP_A3 91.224 0 0 !\n"
                                         "PHASE LIQUID % 1 1.0 !\nCONSTITUENT LIQUID :CU,ZR: !\n")
    meta = {"contribution_type": "E", "system": "CU-ZR", "tdb_file": "CuZr-example.tdb", "assessment_doi": "10.1000/assess",
            "licence": "CC-BY-4.0", "licence_holder": "the authors", "rights_confirmed": True, "contributor": dict(WHO)}
    rep, _ = run(repo, "contributions/tdb/cu-zr-example/metadata.json", meta)
    assert not [e for e in rep.errors], msgs(rep)
    rep, _ = run(repo, "contributions/tdb/cu-zr-example/metadata.json", {**meta, "licence": "proprietary", "system": "AL-CU"})
    m = msgs(rep)
    assert "licence is required" in m and "does not define element(s) ['AL']" in m


# ------------------------------------------------------------------------ acceptance and credit --
def test_apply_corrections(repo):
    recs = {r["id"]: json.loads(json.dumps(r)) for r in RECORDS}
    c = correction()
    assert oc.apply_corrections(recs, [c], {}) == []          # no page check: not applied
    chk = {oc.accepted_check_key(c["record_id"], c["field"]): {"verdict": "confirmed", "page": 2, "checked": "2026-10-24",
                                                              "seen": "Table 1 row 1: 318 °C"}}
    assert oc.apply_corrections(recs, [c], chk) == ["contributed_correction:ORC-RZXYDDJGWB:temperature_K"]
    r = recs["ORC-RZXYDDJGWB"]
    assert r["temperature_K"] == 591.15
    assert r["corrections"][-1]["before"] == 590.15 and r["corrections"][-1]["gate"] == "contributed"
    assert r["contributors"] == [{"name": "Example Contributor", "orcid": "0000-0002-1825-0097", "role": "corrected temperature_K"}]
    assert oc.apply_corrections(recs, [c], chk) == []          # never applied twice (old no longer matches)


def test_credit(repo):
    (repo / "CONTRIBUTORS.md").write_text("# Contributors\n\n%s\n%s\n" % (oc.CREDIT_BEGIN, oc.CREDIT_END))
    (repo / ".zenodo.json").write_text(json.dumps({"title": "x", "creators": []}, indent=2) + "\n")
    (repo / "CITATION.cff").write_text('cff-version: 1.2.0\ntitle: "x"\nauthors:\n  - family-names: "Arróyave"\n'
                                       '    given-names: "Raymundo"\nversion: "1"\n')
    cfg = {"cff_authors": False, "contributors": [
        {"name": "Ada Lovelace", "orcid": "0000-0002-1825-0097", "credit_opt_in": True, "roles": ["corrections"]},
        {"name": "Quiet Person", "credit_opt_in": False, "roles": ["data"]}]}
    (repo / "contributors.json").write_text(json.dumps(cfg))
    out = oc.credit_outputs(str(repo))
    assert "Ada Lovelace" in out["CONTRIBUTORS.md"] and "Quiet Person" in out["CONTRIBUTORS.md"]
    z = json.loads(out[".zenodo.json"])
    assert z["contributors"] == [{"name": "Lovelace, Ada", "type": "DataCurator", "orcid": "0000-0002-1825-0097"}]
    assert "CITATION.cff" not in out
    cfg["cff_authors"] = True
    (repo / "contributors.json").write_text(json.dumps(cfg))
    cff = oc.credit_outputs(str(repo))["CITATION.cff"]
    assert cff.index("Arróyave") < cff.index("Lovelace") < cff.index("\nversion:") and "Quiet" not in cff
    rep, _ = run(repo, "contributors.json", cfg)
    assert not rep.errors, msgs(rep)


# ------------------------------------------------------------------------- dry run of three PRs --
@pytest.mark.parametrize("name,target,ok", [
    ("pr1-valid-correction.jsonl", "contributions/corrections/pr1.jsonl", True),
    ("pr2-invalid-correction.jsonl", "contributions/corrections/pr2.jsonl", False),
    ("pr3-data-contribution.json", "contributions/data/pr3.json", True)])
def test_example_payloads(repo, name, target, ok):
    (repo / target).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(os.path.join(EXAMPLES, name), repo / target)
    rel = oc.Release(str(repo), TOOLS if HAVE_TOOLS else None)
    rep = oc.Report()
    oc.validate([str(repo / target)], rel, rep)
    assert (not rep.errors) == ok, msgs(rep)
