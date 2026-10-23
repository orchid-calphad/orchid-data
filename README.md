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
| `parquet/` | Analysis-ready Parquet tables of the same release (see Formats). |
| `zenodo/` | Zenodo deposition metadata and file manifests of the seven release records; DOIs in `zenodo/dois.json`. |
| `systems/`, `compounds/`, `papers/` | Static no-JavaScript pages (HTML, Markdown, CSV) generated from the data; not part of the Zenodo records. |

## Licence and attribution
Derived data: **CC BY 4.0** — cite ORCHID and the original sources. Each literature value carries its citation, DOI,
page and the one sentence it was read from (quoted under fair use). Source papers, page images and full texts are not
redistributed. Third-party data (SGTE, Materials Project, OQMD) keep their own licences and citations: see `NOTICE.md`
and `LICENSES.md`.

## Citing
Release v2026.10 is archived on Zenodo as six citable datasets, each its own record and DOI, plus an umbrella
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
| ORCHID data | umbrella: documentation, licences, `DATASET_CARD.md`, Parquet manifest, Zenodo metadata | [10.5281/zenodo.PENDING-orchid-data](https://doi.org/10.5281/zenodo.PENDING-orchid-data) |

Machine-readable: a top-level `cite_as` object (text, BibTeX, DOI) in every index/catalog JSON and in each
`literature/systems/*.json`; `orchid.cite_as` metadata in the Parquet files; `literature/CITATION.txt` beside the
CSV; `CITATION.cff` here and in `literature/`, `phase-diagrams/`, `hulls/`, `phases/`, `assessed-phase-assemblages/`. Zenodo deposition metadata and file
manifests: `zenodo/` (see `zenodo/README.md`). Changes: `CHANGELOG.md`.

Authors: R. Arróyave (Texas A&M University), J. Saal (Citrine Informatics), D. Shin (Oak Ridge National Laboratory).

## Formats
Besides the JSON (the reference format), `parquet/` holds analysis-ready Parquet tables (zstd) built from the same
release by `tools/build_parquet.py` in the website repository: `literature_values` (one typed row per value, with a
by-paper `split` column for ML), `papers`, `experimental_context`, `dft_parity`, `phase_diagram_index`,
`phase_diagram_invariants` and `hull_vertices`. `parquet/MANIFEST.json` gives row counts, schemas and content hashes.
`DATASET_CARD.md` is the datasheet (Hugging Face dataset-card format) with loading examples for `datasets`, pandas and
DuckDB; `hf/README.md` is the same card for a future Hugging Face mirror.
