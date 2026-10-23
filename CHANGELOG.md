# Changelog

## Unreleased — ESPEI datasets, bibliography, literature re-export (2026-10-23)

**Literature values re-exported** from the record store db-v2.1 v2.1.19r: 77,540 values (was 76,432; general
tables 45,088), 76,600 accepted, 1,391 systems, 4,881 papers and cited works. Every table value now carries
`reader_agreement` / `reader_agreement_label`: `multi_reader` 41,809, `single_reader_text_layer` 2,385,
`single_reader` 894 (806 accepted; the data explorer shows a "single reader" badge; treat as unconfirmed); a blind
second Claude read (`claude-opus-5.5#2`) counts as a second reader. DFT benchmark 7,888 points; Kim et al. 2017
cross-check unchanged (162 formulas, MAE 3.85 kJ/mol-atom). Phase registry, Parquet tables and static pages rebuilt.

New dataset **ORCHID ESPEI datasets from the literature** (`espei/`, Zenodo record `espei`,
10.5281/zenodo.PENDING-espei, `hasPart` of the umbrella; Version 1, machine-extracted): 7,639 ESPEI 0.9.1
datasets with 19,419 values — experimental 1,679, model
758, invariant ZPF 2,143, DFT literature
479, Materials Project 1,290, OQMD
1,290 — gated by the published literature values, each value with its observation id,
source DOI, uncertainty (printed, ESPEI default or DFT sigma calibrated against experiment) and ESPEI weight;
validated with ESPEI check_dataset / load_datasets. Built by `tools/build_espei_bundle.py` (orchid-project.org).

New dataset **ORCHID bibliography** (`bibliography/`, Zenodo record `bibliography`, 10.5281/zenodo.PENDING-bibliography,
`hasPart` of the umbrella; Version 1, machine-extracted): 9,569 works (7,813 with DOI),
their roles in ORCHID, evidence counts and 60,237 typed relations with provenance; Crossref metadata (CC0).
DOIs that upstream matchers found for printed references (handbook source lines, cited sources of values, TDB header
citations) are now checked against Crossref (first author, year ±1, title, journal): `doi_match` verified
5,385, weak 104 (kept, flagged), no Crossref record
23; 19 mismatched DOIs were dropped (works kept without
DOI; `bibliography/DOI_MISMATCHES.md`). Hugging Face configs `bibliography_papers`, `bibliography_edges`. Built by
`tools/build_bibliography.py` (orchid-project.org).

Release metadata: nine Zenodo records (eight datasets plus the umbrella); `zenodo/espei.metadata.json`,
`zenodo/bibliography.metadata.json`, umbrella `hasPart`, `zenodo/dois.json` placeholders.

## Unreleased — assessed phase assemblages v1 (2026-10-23)

New dataset **ORCHID assessed phase assemblages (binary systems)** (`assessed-phase-assemblages/`, Zenodo record
`assessed-phase-assemblages`, 10.5281/zenodo.PENDING-assessed-phase-assemblages, `hasPart` of the umbrella; Version 1,
machine-extracted): one (T, x, P) point deep inside each named phase field of the expert-drawn (assessed) binary
diagrams compiled in Okamoto's Desk Handbook (annotation run-20261021h-full), evidence class `assessed_phase_diagram`.
23,131 points from 2,178 diagrams (area centroid 21,618, pole of inaccessibility 1,513), with phase-registry ids,
coordinate uncertainty from the axis calibration, naming basis, confidence, review state, a cross-check against the
calculated SGTE diagrams (82.3% agreement where comparable) and citations (original evaluation first, the handbook
as compilation). Two-phase points carry phases with unknown compositions; 11,962 also carry a drawing-based tie_line
block (low credence). ESPEI ZPF datasets, one per diagram (1,070; default with null endpoints, and a tie-line
variant), validated with ESPEI 0.9.1. Data only: no page images, crops or handbook text (build-time guard). Built by
`tools/build_assessed_assemblages.py` (orchid-project.org).

## Unreleased — phase registry v0 (2026-10-23)

New dataset **ORCHID phase registry (binary systems)** (`phases/`, Zenodo record `phase-registry`,
10.5281/zenodo.PENDING-phase-registry, `hasPart` of the umbrella): 10,496 phases in 1,241 binary systems, 43,251 names
(TDB 22,556, paper labels 8,463, corpus 10,916, Materials Project 658, OQMD 658), 22,556 TDB phase declarations, stability from the
calculated diagrams, up to 10 example references per phase (9,927 phases with references, 3,014 distinct DOIs).
Structure types: 6,259 from the standard phase name (tier A), 150 DFT-supported (tier B: unique Materials Project +
OQMD on-hull match), 1,253 assessment-declared (tier C, assessor-stated: exactly one consistent structure in the
Hallstedt 2025 crystallographic table for that phase name and system), 1,305 liquid and 231 gas; 1,240 phases in the
review queue with candidates, 58 without candidates. Every TDB model carries `tdb_definition`: the verbatim PHASE,
CONSTITUENT and TYPE_DEFINITION statements with line numbers (8,392 distinct type definitions), a parsed view
(type codes, sublattices, site ratios, constituents with major-constituent markers, magnetic model, order/disorder
partner), parameter counts by kind and interaction order, and links to the file on orchid-project.org and in
orchid-calphad/orchid-pipeline. Built by `tools/build_phase_registry.py` (orchid-project.org).

File layout: every file stays below 45 MB (GitHub warns at 50 MB). `phases/registry.json` (7.8 MB) is a compact index
of all phases (id, system, names, structure summary with tier and prototype, counts, `detail` file); the full records,
including `models[].tdb_definition` and `references`, are in `phases/systems/<SYS>.json` (one per system, largest
0.37 MB). JSON-LD, CSV and Parquet are unchanged.

AI-ready access: `phases/structure_types.csv` and `phases/structure_types.parquet` (1,563 structure types; row counts
and content hashes in `phases/parquet.json`); Hugging Face configs `phases` (`phases/registry.parquet`) and
`structure_types` in `DATASET_CARD.md` / `hf/README.md`, with column descriptions and the tier definitions; static,
JavaScript-free pages `phases/pages/<SYS>.html|.md` for the 1,241 binary systems (every phase with id, names,
tier/basis, prototype, Strukturbericht, Pearson symbol, space group, stability summary, verbatim PHASE and
CONSTITUENT statements, example DOIs; schema.org Dataset / DefinedTerm JSON-LD) and `phases/pages/index.html|.md`,
linked from the system pages and listed in `sitemap.xml`, `llms.txt`, `llms-full.txt` and `index.md`. The static pages
are web views and not part of the Zenodo record.

## v2026.10 — Version 1, machine-extracted (2026-10-22)

First citable release of the ORCHID data, archived on Zenodo as four datasets, each its own record and DOI, plus
the umbrella record *ORCHID data* that links them (DataCite `isPartOf` / `hasPart`).

**Status.** Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

### Records

| Record | DOI | Content |
|---|---|---|
| ORCHID data (umbrella) | 10.5281/zenodo.PENDING-orchid-data | README, CHANGELOG, DATASET_CARD, licences and attributions, Parquet manifest, Zenodo metadata |
| ORCHID literature values | 10.5281/zenodo.PENDING-literature | `literature/` (except the DFT benchmark files); Parquet `literature_values`, `papers`, `experimental_context` |
| ORCHID calculated binary phase diagrams | 10.5281/zenodo.PENDING-phase-diagrams | `phase-diagrams/`; Parquet `phase_diagram_index`, `phase_diagram_invariants` |
| ORCHID binary convex hulls (MP, OQMD, assessed CALPHAD) | 10.5281/zenodo.PENDING-hulls | `hulls/`; Parquet `hull_vertices` |
| ORCHID DFT-vs-experiment formation-enthalpy benchmark | 10.5281/zenodo.PENDING-dft-benchmark | `literature/dft_parity.json`, `literature/kim2017_crosscheck.*`; Parquet `dft_parity` |

File lists with sizes and SHA-256: `zenodo/<record>.files.json`.

### Contents and counts

- **Literature values:** 76,432 values from 1,322 papers covering 1,390 chemical systems; 75,491 accepted
  (reader agreement plus deterministic checks). Evidence classes: experimental 36,918, model 28,148 (13,586 linked to
  the exact TDB file by SHA-256), DFT 6,162, unspecified 5,204. Record kinds: invariant-reaction tables 26,693,
  general tables 43,980, running text 5,759 (each with a verbatim quote and page). Bibliography of 4,877 reporting
  papers and cited works; experimental context of 225 papers (1,504 items).
- **Calculated binary phase diagrams:** 2,774 SGTE binary databases (Hallstedt 2025), 2,720 calculated with
  pycalphad 0.11.2 and 54 failed; 24,828 invariant equilibria.
- **Binary convex hulls:** Materials Project 2026.04.13 (3,828 systems, 12,829 vertices), OQMD v1.8 (3,916
  systems, 15,314 vertices), assessed SGTE CALPHAD isotherms at 298.15 K (2,695 assessments, 1,223 systems).
- **DFT-vs-experiment benchmark:** 7,826 literature x DFT points (3,738 Materials Project, 4,088 OQMD) from 4,188
  records and 962 compounds; default subset MAE 10.9 kJ/mol-atom (1,231 MP pairs) and 9.6 (1,294 OQMD pairs).
  Kim et al. 2017 cross-check: 162 formulas in common, MAE 3.85 kJ/mol-atom, 19 differing by more than 10.
- **Parquet:** seven tables with a by-paper train/validation/test split (59,967 / 7,527 / 8,938 values).

### Clean-up before release (details: `literature/QUALITY_FIXES.md`, `literature/quality_fixes.json`)

- **Duplicates:** 3,510 exact duplicates merged in 3,314 groups (the removed ids are listed in the surviving record's `merged_ids`).
- **Controlled vocabularies:** `transition_kind` for 21,444 records (187 printed variants, 15,910 relabelled; the
  printed form kept in `transition_kind_printed`); 504 malformed property codes mapped (raw code in
  `property_code_raw`).
- **Garbled fields:** 2 non-page `quote_page` values set to null (`page_unreadable`); `temperature_bound` and
  `reference_state` normalised to objects; 1 reader comment not printed in the quote dropped.
- **DFT-parity outliers:** 238 large residuals examined: 47 per-formula values labelled per atom converted
  (`basis_corrected_from_formula`), 31 unsigned magnitudes flagged and excluded from the default parity set
  (`unsigned_in_print`), 160 flagged `dft_outlier_unexplained` and kept.
- **Energy units:** mixing and partial quantities converted to kJ/mol-atom when the per-atom basis is explicit
  (1,132) and to `kJ/mol (basis unstated)` otherwise (1,995; 9 heuristic per-atom labels demoted); 2,680
  formation values per atom only by a magnitude heuristic are flagged `basis_inferred_from_magnitude`.
- **Field placement:** fields not printed in a value's quote or row were removed (only their existence is
  recorded, `has_dropped_fields`).
- **Website and data site:** "prototype" / "in review" labels replaced by the Version 1 status; counts in
  `DATASET_CARD.md` recomputed from the data.

### Citation metadata

- Top-level `cite_as` (text, BibTeX, DOI of the dataset and of the umbrella record, sources to cite as well) in
  `literature/index.json`, every `literature/systems/*.json`, `phase-diagrams/index.json`, the three hull catalogs,
  `literature/dft_parity.json` and `parquet/MANIFEST.json`; `orchid.cite_as`, `orchid.doi`, `orchid.citation` and
  `orchid.dataset` key-value metadata in every Parquet file; `literature/CITATION.txt` beside the CSV (a comment line
  would break CSV readers); `CITATION.cff` at the top and in `literature/`, `phase-diagrams/` and `hulls/`; a
  "Please cite" box with BibTeX on every static page.
- The hull catalogs now differ from the open-tdb copies only by the added `cite_as` key.

### Known limitations

- Version 1 is machine-extracted; a hand-checked precision sample is in progress. Values in figures are not
  included and coverage is uneven across systems.
- 2,765 formation values have a per-atom vs per-formula basis the paper does not state (`kJ/mol (basis unstated)`,
  not converted); 2,680 are per atom only by a magnitude heuristic.
- Uncertainties with basis `stated_default` (23,133) or `reading_resolution` (6,936) are placeholders; only
  `printed` (3,742) and `printed_range` (23) are the source's own.
- `experimental` values cited from older work carry the citing paper's reading; `unspecified` values may be
  experimental or calculated. `flag_source_disputed` (512), `flag_magnitude_suspect` (499) and
  `flag_system_mismatch` (495) mark values to check; 44 values are printed without a sign by the paper's
  convention (`flag_unsigned_in_print`).
- `flag_espei_ready` is an automatic completeness flag, not a review verdict; do not feed values to an optimizer
  without review.
- Calculated phase diagrams and hulls are model results, not measurements; 54 SGTE files did not calculate; DFT
  hulls are at 0 K and Materials Project and OQMD energies are not comparable with each other.
