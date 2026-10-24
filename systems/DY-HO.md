# Dy–Ho system

> Dy–Ho system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/DY-HO.html · Markdown: https://data.orchid-project.org/systems/DY-HO.md

2 accepted literature values from 1 paper(s) (experimental 1, model 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/DY-HO.json) · [CSV](https://data.orchid-project.org/systems/DY-HO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#DY-HO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#DY-HO/DyHo-00Nor-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/DY-HO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/DY-HO.html) · [Markdown](https://data.orchid-project.org/systems/DY-HO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| DyHo-00Nor-LB.tdb | S. Norgren, J. Phase Equilib., 21, 148-56(2000). [doi:10.1361/105497100770340200](https://doi.org/10.1361/105497100770340200) | `fd6734f5d9c985eb7d2620d338a6aa504eb2455d8d3f8c9380a3c6d2af22fc72` | [viewer](https://orchid-project.org/phase-diagrams/#DY-HO/DyHo-00Nor-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/DyHo-00Nor-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/DyHo-00Nor-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| DyHo-00Nor-LB.tdb | 1729.62 | LIQUID (x(Ho) 0.75934) + BCC_A2 (x(Ho) 0.7643) + HCP_A3 (x(Ho) 0.7678) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/DY/DY-HO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/DY/DY-HO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Dy–Ho system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1731 | peritectic |  | experimental | [1] Norgren 2000; _cites Spedding 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990126-4) | p. 3; `ORC-OKCXPXHFCG.509b95` | “The calculated peritectic temperature is 1730 K and the experimental one is 1731 K.” |
| 1730 | peritectic |  | model | [1] Norgren 2000 | p. 3; `ORC-OKCXPXHFCG.85636f` | “The calculated peritectic temperature is 1730 K and the experimental one is 1731 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Susanne Norgren, Thermodynamic assessment of the Ho-Tb, Ho-Dy, Ho-Er, Er-Tb, and Er-Dy systems, JPE 21, 148-156 (2000). [doi:10.1361/105497100770340200](https://doi.org/10.1361/105497100770340200)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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
