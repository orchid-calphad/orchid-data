# ORCHID data

> ORCHID data: 76,432 literature values (invariant reactions, phase transitions, phase compositions, thermochemical and structural data) from 1,322 papers, 2,720 calculated binary phase diagrams and DFT/CALPHAD convex hulls; CC BY 4.0.

HTML: https://data.orchid-project.org/ · Markdown: https://data.orchid-project.org/index.md

This is the data site of ORCHID (Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery, [orchid-project.org](https://orchid-project.org/)). Every value carries its evidence class (experimental, model, DFT, unspecified; never mixed or averaged), its source paper and DOI, and the table row or one verbatim sentence and page it was read from. Release: `orchid-literature 2026-10-22 (record store db-v2.1: invariant/general v2.1.19p, text+context fixup-20261022)`.

## Browse without JavaScript

- [Chemical systems](https://data.orchid-project.org/systems/index.html) — 1813 pages (also [Markdown](https://data.orchid-project.org/systems/index.md)): literature values, invariants, formation enthalpies, calculated phase diagrams.
- [Compounds](https://data.orchid-project.org/compounds/index.html) — 1477 formation-enthalpy pages with DFT comparison.
- [Reporting papers](https://data.orchid-project.org/papers/index.html) — citation, DOI, systems, number of values.
- Interactive tools: [data explorer](https://orchid-project.org/data-explorer/), [phase diagrams](https://orchid-project.org/phase-diagrams/), [DFT vs experiment](https://orchid-project.org/dft-parity/).

## Folder guide

Table: Folders of the data site

| Path | Content |
|---|---|
| [literature/](https://data.orchid-project.org/literature/SCHEMA.md) | Literature records: index.json, systems/\<SYS>.json, papers.json, contexts.json, dft_parity.json, full CSV/JSONL dumps; fields in SCHEMA.md. |
| [phase-diagrams/](https://data.orchid-project.org/phase-diagrams/index.json) | Calculated binary phase diagrams (pycalphad, SGTE binary collection): index.json and sgte/\<TDB>.json (phase regions, invariants, grid). |
| hulls/ | Binary convex hulls: dft-mp/ (Materials Project), dft-oqmd/ (OQMD), calphad-sgte/ (assessed CALPHAD), one JSON per system. |
| [systems/](https://data.orchid-project.org/systems/index.html) | Static pages per chemical system: \<SYS>.html, \<SYS>.md, \<SYS>.csv. |
| [compounds/](https://data.orchid-project.org/compounds/index.html) | Static pages per compound (reduced formula): \<FORMULA>.html, \<FORMULA>.md. |
| [papers/](https://data.orchid-project.org/papers/index.html) | Index of reporting papers. |
| parquet/ | Columnar copies of the tables, where present. |
| [llms.txt](https://data.orchid-project.org/llms.txt), [llms-full.txt](https://data.orchid-project.org/llms-full.txt) | Guides for language models and agents. |

## Licence and citation

Derived data: CC BY 4.0. Cite the ORCHID release ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original source of every value you use (its paper and DOI). Quoted sentences are single sentences reproduced under fair use so values can be checked; source papers, page images and full text are not redistributed. Licences of the DFT and CALPHAD sources: [LICENSES.md](https://data.orchid-project.org/LICENSES.md), [NOTICE.md](https://data.orchid-project.org/NOTICE.md).

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
