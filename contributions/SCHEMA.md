# ORCHID contributions: file formats, checks and acceptance

How to contribute, in plain words: [README.md](README.md) and [CONTRIBUTING.md](../CONTRIBUTING.md). This page is
the field reference. All checks are in `contributions/tools/orchid_contrib.py` (standard library only) and run on
every pull request (`.github/workflows/contributions.yml`).

Licence: every contribution to this repository is released under **CC BY 4.0** with credit to the contributor
(`licence_consent: "CC-BY-4.0"` on every line or value). Code under `contributions/tools/` is MIT, like the ORCHID
tools; commits carry a DCO sign-off (`git commit -s`).

Personal data: the only personal fields are `contributor.name` (a GitHub handle is fine), the optional
`contributor.orcid`, `contributor.affiliation` and `contributor.github`. No e-mail addresses or other personal data;
the checks reject unknown contributor fields.

## Contribution types

| type | what | where | required evidence |
|---|---|---|---|
| A | suggest a paper or assessment (DOI only) | `contributions/papers/queue.jsonl` (or the issue form) | DOI |
| B | values you read from a published paper | `contributions/data/*.json` or `*.csv` | DOI, printed page, quote (at most 240 characters) |
| C | new measurements | `contributions/data/` | a citable DOI: the paper, or the deposited dataset (unpublished data are first deposited, e.g. on Zenodo) |
| D | calculated data (DFT, CALPHAD model, ...) | `contributions/data/` | DOI + method metadata; own evidence class (`dft` or `model`), never mixed with experiment |
| E | a new assessment / TDB file | `contributions/tdb/<name>/` (`metadata.json` + the `.tdb`) | assessment DOI, an open licence, rights confirmed |
| correction | an error in a released value | `contributions/corrections/*.jsonl` (or the issue form) | printed page + quote |

## Corrections (`contributions/corrections/*.jsonl`, one JSON object per line)

```json
{"record_id": "ORC-RZXYDDJGWB", "field": "temperature_K", "old": 590.15, "new": 591.15,
 "evidence": {"page": 2, "quote": "the sentence or table row on the page, at most 240 characters"},
 "contributor": {"name": "Your Name", "orcid": "0000-0000-0000-0000"},
 "licence_consent": "CC-BY-4.0", "note": "optional free text"}
```

| field | rule |
|---|---|
| `record_id` | an `id` of the release (`literature/orchid-literature.jsonl.gz`); a merged duplicate id is rejected with the id it was merged into |
| `field` | one of `value`, `unit`, `temperature_K`, `pressure_Pa`, `evidence_class`, `transition_kind`, `property`, `system`, `phases` (list of printed labels), `phase_compositions` (list of `{phase, composition}`), `overall_composition`, `reference_state`, `uncertainty` (`{value, basis: "printed", kind}`), `quote_page`, `locator.page`, `locator.row`, `extraction_accepted` (only `false`: the row is not a value of the paper) |
| `old` | must equal the value in the release (otherwise the record has changed; a correction whose `new` is already in the release is reported as applied) |
| `new` | parses for the field: numbers; temperatures in K, (1, 6000]; pressure > 0 Pa; controlled vocabularies (`evidence_class`, `transition_kind`, property codes, system ids); mole fractions in [0, 1], elements of the record's system, summing to 1; the plausible range and sign of the property in its release unit (table below); a sign change or a unit other than the release unit is a warning for the maintainers |
| `evidence.page` | the printed page (`5`, `S3`) |
| `evidence.quote` | the sentence or table row that shows the right value, at most 240 characters (fair use) |
| `contributor` | `name` required; `orcid` optional, checksum-verified |
| `licence_consent` | exactly `"CC-BY-4.0"` |

One correction per record and field in a pull request.

## New values (`contributions/data/*.json` or `*.csv`; types B, C, D)

Templates: [`data/TEMPLATE.json`](data/TEMPLATE.json) and [`data/TEMPLATE.csv`](data/TEMPLATE.csv) (files named
`TEMPLATE*` are not checked). A JSON file is `{"records": [ ... ]}`. Every value is an observation of an
equilibrium state, never a bare number:

| field | rule |
|---|---|
| `contribution_type` | `B`, `C` or `D` |
| `system` | element symbols, uppercase, sorted, joined by `-` (`CU-ZR`) |
| `property`, `unit`, `value` | a property code below, in its release unit (give the printed number and unit in `value_printed`, `unit_printed`); in the plausible range |
| `state.phases` | the phase(s) of the state: `{label (as printed), model_phase (optional)}`; `model_phase` must be a phase of the system's TDB files in the phase registry (`phases/systems/<SYS>.json`) when the system has one |
| `state.temperature_K`, `state.pressure_Pa` | K (298.15 for standard values); Pa (101325 assumed when absent). For invariant / transition temperatures the value is the temperature |
| `state.overall_composition`, `state.phase_compositions` | mole fractions of the system's elements; required except for invariant / transition temperatures and assemblages; `PHASE_COMPOSITION` needs `phase_compositions` |
| `state.reference_state` | `{ELEMENT: {phase}}` for every element; required for formation, mixing and partial quantities and chemical potentials |
| `state.reaction` | `{printed, type}` for invariants and transitions; `type` from the release vocabulary (`eutectic`, `peritectic`, ...) |
| `evidence_class` | `experimental`, `model`, `dft` (`unspecified` only for type B when the paper does not say); C is `experimental`; D is `dft` or `model` |
| `method` | `kind` required for C and D; D with `dft`: `code`, `functional`; D with `model`: `software`, `tdb_or_model` |
| `provenance` | B: `doi`, `page`, `quote` (at most 240 characters), optional `table`, `row`; C and D: `doi` or `dataset_doi` |
| `uncertainty` | the separate components of the release uncertainty budget (literature `SCHEMA.md`, `uncertainty_budget`), each `{value, ...}` in the value's unit: `sigma_printed` `{value, kind}` as printed; `sigma_method` (your estimate of the method's systematic error); `sigma_composition` `{value, dx}`; `sigma_scatter` `{value, n_sources}`; `sigma_conversion` `{value, note}`. `sigma_reading`, the method-class floor and `sigma_effective` are computed by ORCHID at release (`tools/uncertainty_budget.py`); a contributed `sigma_method` below the calibrated floor of its class is raised to the floor |
| `contributor`, `licence_consent` | as for corrections |

Property codes and release units (range checked; the sign rule is a warning for formation quantities, an error for
quantities that must be positive):

| property | unit | range |
|---|---|---|
| `INVARIANT_TEMPERATURE`, `TRANSITION_TEMPERATURE` | K | 1 to 6000 |
| `PHASE_COMPOSITION`, `PHASE_ASSEMBLAGE` | (mole fractions in `state`) | |
| `HM_FORM`, `GM_FORM` | kJ/mol-atom | -500 to 100 (positive: warning) |
| `SM_FORM`, `SM_MIX` | J/mol-atom/K | -100 to 100 |
| `HM_MIX` | kJ/mol-atom | -300 to 300 |
| `GM_MIX` | kJ/mol-atom | -300 to 100 |
| `PARTIAL_ENTHALPY` | kJ/mol | -1000 to 1000 |
| `CHEMICAL_POTENTIAL` | kJ/mol | -2000 to 500 |
| `CPM`, `SM` | J/mol-atom/K | > 0 (500, 1000) |
| `HEAT_CONTENT`, `TRANSITION_ENTHALPY` | kJ/mol-atom | -1000 to 1000, -500 to 500 |
| `ACTIVITY`, `ACTIVITY_COEFFICIENT` | 1 | (0, 1], > 0 |
| `EMF` | mV | -5000 to 5000 |
| `VAPOR_PRESSURE` | Pa | > 0 |
| `LATTICE_A`, `LATTICE_B`, `LATTICE_C` | nm | 0.05 to 10 |
| `LATTICE_ALPHA`, `LATTICE_BETA`, `LATTICE_GAMMA` | ° | 0 to 180 |
| `MOLAR_VOLUME` | cm3/mol | > 0 |
| `BULK_MODULUS` | GPa | > 0 |

Other checks (the release gates, reused): elements of every composition and reference state against the system;
the **physical phase rule** of the release (`tools/phase_rule.py` of orchid-project.org: a liquid below the lowest
liquid temperature of the system's calculated diagrams, or a phase equilibrium far below the elements' melting
points, is an error; a phase that does not map to the system's TDB, or a compound property ESPEI cannot fit, is a
warning: the value is accepted but not ESPEI-ready); **duplicates** within the pull request and against the release
(same system, property, state, value and source: send a correction instead).

### What a contributed value becomes

`orchid_contrib.py convert FILE` prints the ORCHID records (literature `SCHEMA.md` fields): a new id `ORC-C...`
(a hash of the content, stable), `source: "contributed"`, `record_kind: "contributed"`, `contribution {type, file,
line, dataset_doi, licence}`, `contributors [{name, orcid, role}]`, the state fields, `uncertainty` (the printed
sigma), `uncertainty_contributed` (the components as given), and
`flags {review_state: contributed_unverified, contribution_tier: contributed_unverified, extraction_accepted: false,
espei_ready: false, espei_certified: false}`. A contributed value never overwrites a released value.

Tiers: `contributed_unverified` -> `verified` when a maintainer or a second, independent contributor has checked the
value against its page (type B) or its dataset (C, D); the check is recorded like a correction's page check (below).
Only then is `extraction_accepted` set. `espei_ready` and `espei_certified` are decided by the same rules as every
other value (complete state, phase mapped to a model, the physical phase rule, agreement with a CALPHAD prediction).

## Paper suggestions (type A, `contributions/papers/queue.jsonl`)

```json
{"doi": "10.xxxx/...", "systems": ["CU-ZR"], "data_types": ["formation enthalpy"], "why": "calorimetry of five compounds",
 "contributor": {"name": "optional"}, "issue": 12}
```

`data_types` from: invariant reactions; phase boundaries / compositions; phase transitions; formation enthalpy;
mixing / partial quantities; heat capacity / entropy; activity / EMF / vapour pressure; crystal structure / lattice;
CALPHAD assessment (TDB); DFT / calculated; other. A DOI already in the corpus is reported, not rejected. The queue
is read by the extraction pipeline (orchid-pipeline); suggestions from the issue form are added by the maintainers.

## New assessments / TDB files (type E, `contributions/tdb/<name>/`)

`metadata.json`: `{contribution_type: "E", system, tdb_file, assessment_doi, licence (SPDX: CC-BY-4.0, CC0-1.0, MIT,
BSD-3-Clause, ODbL-1.0, CC-BY-SA-4.0), licence_holder, rights_confirmed: true, contributor, sha256 (optional)}`.
Checks: the file exists, defines every element of the system and has PHASE statements, is at most 20 MB, is not
already contributed; it must load in pycalphad when pycalphad is installed.

## Credit (`contributors.json`, `CONTRIBUTORS.md`)

Accepted contributors are added by the maintainers to `contributors.json`:
`{name, orcid, github, affiliation, credit_opt_in (true/false), roles [corrections, reviews, data, assessments,
code, papers], contributions [pull request numbers], since}`. `orchid_contrib.py credit` writes the table in
`CONTRIBUTORS.md` and, for opted-in contributors only, the `contributors` of the Zenodo metadata (`.zenodo.json`,
`zenodo/*.metadata.json`; DataCurator for corrections and reviews, DataCollector for data); with the policy
`cff_authors: true` (PI decision) they are also listed in `CITATION.cff` after the maintainers. `credit --check`
runs in CI and before every release (`tools/zenodo_release.py credit` in orchid-project.org). Records whose
correction or verification was accepted carry the contributor in their own `contributors` field.

## Acceptance procedure (maintainers)

1. **CI green.** The pull request passes `orchid_contrib.py validate` and the DCO check.
2. **Page check.** A maintainer opens the cited page (the PDF is never committed) and compares it with the
   contribution; for C and D, the deposited dataset.
3. **Record the check** in `tools/literature_visual_checks.json` of orchid-project.org, with the key
   `contributed_correction:<record_id>:<field>` (corrections) or `contributed_value:<ORC-C id>` (new values):
   `{key, kind: "contributed_correction" | "contributed_value", page, pdf_sha256_prefix, image_sha256, verdict
   ("confirmed" or "rejected"), seen (what the page shows, in the maintainer's words), checked (date),
   contribution ("<file>:<line>", pull request number)}`. No page image or page text is published.
4. **Merge** the pull request and add the contributor to `contributors.json` (with their opt-in choice).
5. **Next release.** The export applies every confirmed correction (`orchid_contrib.apply_corrections`): the new
   value replaces the old in the record, the old value is kept in the record's `corrections[]` (`gate:
   "contributed"`, `before`, `after`, `evidence`, `contributor`, `visual_check`), and the contributor is added to the
   record's `contributors`. A confirmed new value moves from `contributed_unverified` to `verified`. The literature
   gates, the uncertainty budget and the ESPEI bundle are then rebuilt as for every release, and
   `orchid_contrib.py credit` updates the credit files.
6. A rejected contribution is closed with the reason; the check stays in `literature_visual_checks.json`
   (`verdict: "rejected"`) so the same question is not reviewed twice.
