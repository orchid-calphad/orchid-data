# Changelog

## Unreleased — phase registry v0 (2026-10-23)

New dataset **ORCHID phase registry (binary systems)** (`phases/`, Zenodo record `phase-registry`,
10.5281/zenodo.PENDING-phase-registry, `hasPart` of the umbrella): 10,496 phases in 1,241 binary systems, 43,229 names
(TDB 22,556, paper labels 8,463, corpus 10,916, Materials Project 647, OQMD 647), 22,556 TDB phase declarations, stability from the
calculated diagrams, up to 10 example references per phase (9,927 phases with references, 3,014 distinct DOIs).
Structure types only when certain: 6,259 from the standard phase name (tier A), 150 DFT-supported (tier B: unique
Materials Project + OQMD on-hull match), 1,305 liquid and 231 gas; 2,493 phases in the review queue with candidates,
58 without candidates. Built by `tools/build_phase_registry.py` (orchid-project.org).

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
