# Licences of the ORCHID data release

ORCHID's own data are released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0,
<https://creativecommons.org/licenses/by/4.0/>), as are the SGTE, Materials Project and OQMD data from which parts of
them are derived. The table lists every folder of this repository with the source of its content and the licence that
applies. Attributions, citations and the statements of changes that CC BY 4.0 requires are in `NOTICE.md`.

| Path | Content and source | Licence |
|---|---|---|
| `literature/` (values, systems, papers, contexts, quality reports) | values, conditions, phases and provenance read from published papers by ORCHID | CC BY 4.0 (ORCHID) |
| `literature/` `quote` fields, and the quotes shown in `systems/`, `compounds/`, `papers/` | short excerpts of the source papers (the passage of running text that states the value, or a table caption and the row it was read from), kept so that each value can be verified | **not relicensed**: the publishers' copyright; reproduced as short quotations |
| `literature/dft_parity.json`, `parquet/dft_parity.parquet` | ORCHID literature values paired with Materials Project and OQMD formation energies | CC BY 4.0 (ORCHID; Materials Project and OQMD data CC BY 4.0) |
| `literature/kim2017_crosscheck.json`, `.md` | comparison with the experimental formation enthalpies of Kim et al. 2017 (per-formula medians of their CSV) | ORCHID comparison CC BY 4.0; the Kim et al. values: MIT (Figshare 10.6084/m9.figshare.7289723), notice in `NOTICE.md` |
| `phase-diagrams/` | binary phase diagrams calculated by ORCHID with pycalphad from the SGTE binary collection | CC BY 4.0 (derived from SGTE, Hallstedt 2025, CC BY 4.0) |
| `hulls/dft-mp/` | convex hulls derived from Materials Project release 2026.04.13 | CC BY 4.0 (Materials Project) |
| `hulls/dft-oqmd/` | convex hulls derived from OQMD v1.8 | CC BY 4.0 (OQMD) |
| `hulls/calphad-sgte/` | assessed CALPHAD isotherms calculated from the SGTE binary collection | CC BY 4.0 (derived from SGTE) |
| `phases/` | ORCHID phase registry; `models[].tdb_definition.verbatim` holds PHASE / CONSTITUENT / TYPE_DEFINITION statements copied from SGTE TDB files | CC BY 4.0 (ORCHID; the verbatim statements: SGTE binary collection, CC BY 4.0) |
| `assessed-phase-assemblages/` | points (T, x, P) and phase names located by ORCHID inside the phase fields of assessed handbook diagrams, with citations | CC BY 4.0 (ORCHID); see "Handbook-derived points" in `NOTICE.md`; no handbook drawing or text is included |
| `espei/` | ESPEI datasets built by ORCHID from the literature values, the assessed points and Materials Project / OQMD energies | CC BY 4.0 (ORCHID; Materials Project and OQMD data CC BY 4.0) |
| `bibliography/` | Crossref bibliographic metadata (titles, authors, ORCID iDs, venues, dates, licence URLs, reference lists) | CC0 1.0 (Crossref metadata) |
| `bibliography/` | ORCHID-derived fields (roles, evidence counts, typed relations, systems, DOI checks) | CC BY 4.0 (ORCHID) |
| `parquet/` | Parquet tables of the same release | as the folder each table is built from |
| `systems/`, `compounds/`, `papers/`, `bibliography/pages/`, `index.*`, `llms*.txt` | static pages generated from the data | as the data shown; quotes as above |
| `zenodo/`, `hf/`, `README.md`, `SCHEMA.md` files, `DATASET_CARD.md`, `CITATION.cff` | documentation and metadata | CC BY 4.0 (ORCHID) |

The source papers, their page images and their full text are not redistributed. Code that builds these files is in
the ORCHID website repository and is licensed separately.
