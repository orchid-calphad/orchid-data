# ORCHID data

> ORCHID data: 73,542 literature values (invariant reactions, phase transitions, phase compositions, thermochemical and structural data) from 1,321 papers, 2,720 calculated binary phase diagrams and DFT/CALPHAD convex hulls; CC BY 4.0.

HTML: https://data.orchid-project.org/ · Markdown: https://data.orchid-project.org/index.md

This is the data site of ORCHID (Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery, [orchid-project.org](https://orchid-project.org/)). Every value carries its evidence class (experimental, model, DFT, unspecified; never mixed or averaged), its source paper and DOI, and the table row or short verbatim passage and page it was read from. Release: `orchid-literature 2026-10-23 (record store db-v2.1: invariant/general v2.1.19r, text+context fixup-20261022)`.

Status: Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

## Browse without JavaScript

- [Chemical systems](https://data.orchid-project.org/systems/index.html) — 1863 pages (also [Markdown](https://data.orchid-project.org/systems/index.md)): literature values, invariants, formation enthalpies, calculated phase diagrams.
- [Compounds](https://data.orchid-project.org/compounds/index.html) — 1460 formation-enthalpy pages with DFT comparison.
- [Reporting papers](https://data.orchid-project.org/papers/index.html) — citation, DOI, systems, number of values.
- [Phase registry](https://data.orchid-project.org/phases/pages/index.html) — 1241 binary-system pages, 10,430 phases: names, structure (when certain), stability, TDB PHASE/CONSTITUENT statements, example DOIs.
- [Bibliography](https://data.orchid-project.org/bibliography/pages/index.html) — 9,569 papers ORCHID knows (read, cited as original sources, behind TDB files and assessed diagrams, discovery leads) with roles, evidence counts and typed relations; per paper and per system.
- Interactive tools: [data explorer](https://orchid-project.org/data-explorer/), [phase diagrams](https://orchid-project.org/phase-diagrams/), [phase registry](https://orchid-project.org/phases/), [DFT vs experiment](https://orchid-project.org/dft-parity/).

## Folder guide

Table: Folders of the data site

| Path | Content |
|---|---|
| [literature/](https://data.orchid-project.org/literature/SCHEMA.md) | Literature records: index.json, systems/\<SYS>.json, papers.json, contexts.json, dft_parity.json, full CSV/JSONL dumps; fields in SCHEMA.md. |
| [phase-diagrams/](https://data.orchid-project.org/phase-diagrams/index.json) | Calculated binary phase diagrams (pycalphad, SGTE binary collection): index.json and sgte/\<TDB>.json (phase regions, invariants, grid). |
| hulls/ | Binary convex hulls: dft-mp/ (Materials Project), dft-oqmd/ (OQMD), calphad-sgte/ (assessed CALPHAD), one JSON per system. |
| [phases/](https://data.orchid-project.org/phases/SCHEMA.md) | Phase registry (binary systems): registry.json (compact index) / .csv / .parquet / .jsonld, structure_types.json / .parquet, review_queue.json, CONFLICTS.md, systems/\<SYS>.json (full records), pages/\<SYS>.html\|.md (static pages); fields in SCHEMA.md. |
| [assessed-phase-assemblages/](https://data.orchid-project.org/assessed-phase-assemblages/README.md) | Assessed phase assemblages: one (T, x, P) point deep inside each named phase field of expert-drawn (assessed) binary diagrams (evidence class assessed_phase_diagram): records.jsonl.gz / .csv / .parquet, exclusions, ESPEI ZPF datasets (espei-zpf/, espei-zpf-with-tie-lines/); fields in SCHEMA.md. |
| [espei/](https://data.orchid-project.org/espei/README.md) | ESPEI datasets from the literature, one folder per evidence class (experimental/, model/, invariants/, dft/literature, dft/mp, dft/oqmd), with uncertainties and weights, plus optional tagged phase constraints (derived/invariant-brackets, derived/liquid-stability, assessed/): index.csv, references.bib, VALIDATION.md, UNCERTAINTY_SUMMARY.md, UPSTREAM_CORRECTIONS.md, dft/CALIBRATION.md; fields in SCHEMA.md. |
| [bibliography/](https://data.orchid-project.org/bibliography/README.md) | Bibliography: every paper ORCHID knows, with Crossref metadata, roles, evidence counts and typed relations: papers.parquet / .csv / .jsonl, edges.parquet / .csv / .jsonl, papers/\<key>.json, systems/\<SYS>.json, orchid-bibliography.bib / .csl.json, DOI_MISMATCHES.md, pages/ (static pages); fields in SCHEMA.md. |
| [systems/](https://data.orchid-project.org/systems/index.html) | Static pages per chemical system: \<SYS>.html, \<SYS>.md, \<SYS>.csv. |
| [compounds/](https://data.orchid-project.org/compounds/index.html) | Static pages per compound (reduced formula): \<FORMULA>.html, \<FORMULA>.md. |
| [papers/](https://data.orchid-project.org/papers/index.html) | Index of reporting papers. |
| parquet/ | Columnar copies of the tables, where present. |
| zenodo/ | Zenodo release metadata: one deposition record per citable dataset plus the umbrella record, with file manifests (sizes, SHA-256). |
| contributions/ | Corrections, new values, paper suggestions and TDB files contributed by pull request, with templates, checks and tests (CONTRIBUTING.md, contributions/SCHEMA.md); not part of the Zenodo records. [How to contribute](https://orchid-project.org/contribute/). |
| [llms.txt](https://data.orchid-project.org/llms.txt), [llms-full.txt](https://data.orchid-project.org/llms-full.txt) | Guides for language models and agents. |

## Licence and citation

Release v2026.10 is archived on Zenodo as eight citable datasets, each with its own DOI, linked by an umbrella record: [ORCHID data](https://doi.org/10.5281/zenodo.PENDING-orchid-data); [ORCHID literature values](https://doi.org/10.5281/zenodo.PENDING-literature); [ORCHID calculated binary phase diagrams](https://doi.org/10.5281/zenodo.PENDING-phase-diagrams); [ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)](https://doi.org/10.5281/zenodo.PENDING-hulls); [ORCHID DFT-vs-experiment formation-enthalpy benchmark](https://doi.org/10.5281/zenodo.PENDING-dft-benchmark); [ORCHID phase registry (binary systems)](https://doi.org/10.5281/zenodo.PENDING-phase-registry); [ORCHID assessed phase assemblages (binary systems)](https://doi.org/10.5281/zenodo.PENDING-assessed-phase-assemblages); [ORCHID ESPEI datasets from the literature](https://doi.org/10.5281/zenodo.PENDING-espei); [ORCHID bibliography](https://doi.org/10.5281/zenodo.PENDING-bibliography).

Derived data: CC BY 4.0. Cite the ORCHID release ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original source of every value you use (its paper and DOI). Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Licences of the DFT and CALPHAD sources: [LICENSES.md](https://data.orchid-project.org/LICENSES.md), [NOTICE.md](https://data.orchid-project.org/NOTICE.md).

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID DFT-vs-experiment formation-enthalpy benchmark (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-dft-benchmark
- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID assessed phase assemblages (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-assessed-phase-assemblages
- R. Arróyave, J. Saal, D. Shin, ORCHID ESPEI datasets from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-espei
- R. Arróyave, J. Saal, D. Shin, ORCHID bibliography (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-bibliography
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162, https://doi.org/10.1038/sdata.2017.162; for every diagram used, its original evaluation (citations[role=original_evaluation], DOI where matched) and H. Okamoto, Desk Handbook: Phase Diagrams for Binary Alloys, 2nd ed., ASM International (2010) as the compilation; the original source of every value you use (each dataset's `reference` / `bibtex`, references.bib; index.csv lists the DOIs); the papers themselves when you use their data (doi / citation of each bibliography record).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_dft_benchmark_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID DFT-vs-experiment formation-enthalpy benchmark}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-dft-benchmark},
  url       = {https://doi.org/10.5281/zenodo.PENDING-dft-benchmark},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_assessed_assemblages_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID assessed phase assemblages (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-assessed-phase-assemblages},
  url       = {https://doi.org/10.5281/zenodo.PENDING-assessed-phase-assemblages},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_espei_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID ESPEI datasets from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-espei},
  url       = {https://doi.org/10.5281/zenodo.PENDING-espei},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_bibliography_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID bibliography}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-bibliography},
  url       = {https://doi.org/10.5281/zenodo.PENDING-bibliography},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
