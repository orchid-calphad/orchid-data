# ORCHID data

Open data of the **ORCHID** project (Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery),
served at <https://data.orchid-project.org> and browsable at <https://orchid-project.org>.

**Release v2026.10. Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.**

| Folder | Content |
|---|---|
| `literature/` | Thermodynamic and phase-equilibrium values read from published papers: one JSON per chemical system (`systems/`), full dumps (`orchid-literature.csv.gz`, `orchid-literature.jsonl.gz`), papers, experimental contexts, DFT-vs-experiment parity data. Fields are documented in `literature/SCHEMA.md`. |
| `phase-diagrams/` | Binary phase diagrams calculated with pycalphad from the SGTE binary collection (Hallstedt 2025, CC BY 4.0), each tied to its TDB file by SHA-256. |
| `hulls/` | Binary convex hulls from the Materials Project and OQMD (CC BY 4.0) and assessed CALPHAD isotherms. |
| `phases/` | Phase registry (binary systems): one entry per phase with its names (TDB, papers, corpus, Materials Project, OQMD), CALPHAD models, stability in the calculated diagrams, example references, and a structure type only when certain. Fields in `phases/SCHEMA.md`. |
| `assessed-phase-assemblages/` | Assessed phase assemblages: one (T, x, P) point deep inside each named phase field of the expert-drawn (assessed) binary diagrams compiled in Okamoto's Desk Handbook, with the assemblage, phase-registry ids, basis, confidence, SGTE cross-check and ESPEI ZPF datasets; evidence class `assessed_phase_diagram`. Data only (no page images or handbook text). Fields in `assessed-phase-assemblages/SCHEMA.md`. |
| `espei/` | ESPEI 0.9.1 datasets built from the literature values and from DFT, one folder per evidence class (`experimental/`, `model/`, `invariants/`, `dft/literature`, `dft/mp`, `dft/oqmd`), every value with its ORCHID observation id, source DOI, uncertainty and ESPEI weight; `index.csv`, `references.bib`, `VALIDATION.md`, `UNCERTAINTY_SUMMARY.md`, `dft/CALIBRATION.md`. Fields in `espei/SCHEMA.md`. |
| `bibliography/` | Every paper ORCHID knows: Crossref bibliographic metadata (CC0), roles in ORCHID, evidence counts and typed relations with provenance (papers and edges as JSONL / CSV / Parquet, one JSON per paper and per system, BibTeX, CSL-JSON, JSON-LD); DOIs matched from printed references checked against Crossref (`DOI_MISMATCHES.md`). `pages/` are static web views. Fields in `bibliography/SCHEMA.md`. |
| `parquet/` | Analysis-ready Parquet tables of the same release (see Formats). |
| `zenodo/` | Zenodo deposition metadata and file manifests of the nine release records; DOIs in `zenodo/dois.json`. |
| `systems/`, `compounds/`, `papers/`, `bibliography/pages/` | Static no-JavaScript pages (HTML, Markdown, CSV) generated from the data; not part of the Zenodo records. |
| `contributions/` | Corrections, new values, paper suggestions and TDB files contributed by pull request, with their templates, checks (`contributions/tools/orchid_contrib.py`) and tests; not part of the Zenodo records. See `CONTRIBUTING.md`. |

## Machine-learning use
Literature values, DFT parity rows and assessed phase-assemblage points carry `chemical_system`, `paper_id` and two
deterministic 5-fold assignments: `fold_lso` = int(sha256(chemical_system), 16) mod 5 (leave-chemical-system-out) and
`fold_lpo` = int(sha256(paper_id), 16) mod 5 (leave-paper-out). Do not split rows at random: values of one table, paper
or system are correlated and many are re-listed from the same original measurement. Subsystems (unaries, binaries of a
ternary) are systems of their own; drop them from training for strict extrapolation to unseen chemistry. Details:
`DATASET_CARD.md`, "Machine-learning use".

## Licence and attribution
ORCHID's data are released under **CC BY 4.0**, as are the SGTE, Materials Project and OQMD data from which they are
derived; cite ORCHID and the original sources. Each literature value carries its citation, DOI, page and the sentence
it was read from: a short excerpt kept for verification, which remains under the publisher's copyright and is not
relicensed. Source papers, page images and full texts are not redistributed. Attributions, the Kim et al. 2017 (MIT)
and Crossref (CC0) notices and statements of changes: `NOTICE.md`; licence per folder: `LICENSES.md`.

## Contributing
Found a wrong value, or know a paper ORCHID should read? Every value on the data pages has a **report** link that
opens a pre-filled GitHub issue; papers can be suggested with an issue form, and data are contributed by pull request
to `contributions/`, where every value is checked automatically and then against its page by a maintainer. See
`CONTRIBUTING.md` (licences: CC BY 4.0 for data, MIT and DCO sign-off for code), `CODE_OF_CONDUCT.md`,
`GOVERNANCE.md` and `CONTRIBUTORS.md`, or https://orchid-project.org/contribute/.

## Citing
Release v2026.10 is archived on Zenodo as eight citable datasets, each its own record and DOI, plus an umbrella
record that links them (`isPartOf` / `hasPart`). Cite the dataset you use and the umbrella record, and the original
source of every value (its paper and DOI).

| Dataset | Content | DOI |
|---|---|---|
| ORCHID literature values | `literature/` (except the DFT benchmark files), Parquet `literature_values`, `papers`, `experimental_context` | [10.5281/zenodo.PENDING-literature](https://doi.org/10.5281/zenodo.PENDING-literature) |
| ORCHID calculated binary phase diagrams | `phase-diagrams/`, Parquet `phase_diagram_index`, `phase_diagram_invariants` | [10.5281/zenodo.PENDING-phase-diagrams](https://doi.org/10.5281/zenodo.PENDING-phase-diagrams) |
| ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) | `hulls/`, Parquet `hull_vertices` | [10.5281/zenodo.PENDING-hulls](https://doi.org/10.5281/zenodo.PENDING-hulls) |
| ORCHID DFT-vs-experiment formation-enthalpy benchmark | `literature/dft_parity.json`, `literature/kim2017_crosscheck.*`, Parquet `dft_parity` | [10.5281/zenodo.PENDING-dft-benchmark](https://doi.org/10.5281/zenodo.PENDING-dft-benchmark) |
| ORCHID phase registry (binary systems) | `phases/` (registry JSON, CSV, Parquet, JSON-LD, structure types, review queue) | [10.5281/zenodo.PENDING-phase-registry](https://doi.org/10.5281/zenodo.PENDING-phase-registry) |
| ORCHID assessed phase assemblages (binary systems) | `assessed-phase-assemblages/` (JSONL, CSV, Parquet, ESPEI ZPF datasets, exclusions) | [10.5281/zenodo.PENDING-assessed-phase-assemblages](https://doi.org/10.5281/zenodo.PENDING-assessed-phase-assemblages) |
| ORCHID ESPEI datasets from the literature | `espei/` (ESPEI JSON per evidence class, index, references, validation, DFT calibration) | [10.5281/zenodo.PENDING-espei](https://doi.org/10.5281/zenodo.PENDING-espei) |
| ORCHID bibliography | `bibliography/` (papers, edges, per-paper and per-system JSON, BibTeX, CSL-JSON, JSON-LD), Parquet `bibliography_papers`, `bibliography_edges` | [10.5281/zenodo.PENDING-bibliography](https://doi.org/10.5281/zenodo.PENDING-bibliography) |
| ORCHID data | umbrella: documentation, licences, `DATASET_CARD.md`, Parquet manifest, Zenodo metadata | [10.5281/zenodo.PENDING-orchid-data](https://doi.org/10.5281/zenodo.PENDING-orchid-data) |

Machine-readable: a top-level `cite_as` object (text, BibTeX, DOI) in every index/catalog JSON and in each
`literature/systems/*.json`; `orchid.cite_as` metadata in the Parquet files; `literature/CITATION.txt` beside the
CSV; `CITATION.cff` here and in `literature/`, `phase-diagrams/`, `hulls/`, `phases/`, `assessed-phase-assemblages/`, `espei/`,
`bibliography/`. Zenodo deposition metadata and file
manifests: `zenodo/` (see `zenodo/README.md`). Changes: `CHANGELOG.md`.

Authors: R. Arróyave (Texas A&M University), J. Saal (Citrine Informatics), D. Shin (Oak Ridge National Laboratory).

## Formats
Besides the JSON (the reference format), `parquet/` holds analysis-ready Parquet tables (zstd) built from the same
release by `tools/build_parquet.py` in the website repository: `literature_values` (one typed row per value, with a
by-paper `split` column for ML), `papers`, `experimental_context`, `dft_parity`, `phase_diagram_index`,
`phase_diagram_invariants` and `hull_vertices`. `parquet/MANIFEST.json` gives row counts, schemas and content hashes.
`DATASET_CARD.md` is the datasheet (Hugging Face dataset-card format) with loading examples for `datasets`, pandas and
DuckDB; `hf/README.md` is the same card for a future Hugging Face mirror.
