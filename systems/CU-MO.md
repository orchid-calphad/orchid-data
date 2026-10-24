# Cu–Mo system

> Cu–Mo system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-MO.html · Markdown: https://data.orchid-project.org/systems/CU-MO.md

4 accepted literature values from 1 paper(s) (experimental 2, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-MO.json) · [CSV](https://data.orchid-project.org/systems/CU-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-MO/CuMo-00Wan.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CU-MO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CU-MO.html) · [Markdown](https://data.orchid-project.org/systems/CU-MO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuMo-00Wan.tdb | C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, S.M. Hao, K. Ishida, J. Phase Equilib., 21, 54-62(2000). [doi:10.1361/105497100770340426](https://doi.org/10.1361/105497100770340426) | `3ccd24b6fa9938a1a01da83360891968a4e69bdd6613055d436115165d0d74de` | [viewer](https://orchid-project.org/phase-diagrams/#CU-MO/CuMo-00Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuMo-00Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuMo-00Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuMo-00Wan.tdb | 2787.54 | LIQUID (x(Mo) 0.11127) + LIQUID#2 (x(Mo) 0.90111) + BCC_A2 (x(Mo) 0.98441) |
| CuMo-00Wan.tdb | 1357.04 | FCC_A1 (x(Mo) 1.500e-4) + LIQUID (x(Mo) 7.900e-4) + BCC_A2 (x(Mo) 0.99944) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-MO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-MO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–Mo system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2788.2 | monotectic: L2 -> (Mo) + L1 | L2: Mo 92.8 (basis unresolved); (Mo): Mo 98.9 (basis unresolved); L1: Mo 16.8 (basis unresolved) | unspecified | [1] Wang 2000; _cites Brewer 1980_ | Table 7, p. 7, row 3 |  |
| 2787.6 | monotectic: L2 -> (Mo) + L1 | L2: Mo 93.22 (basis unresolved); (Mo): Mo 98.96 (basis unresolved); L1: Mo 15.89 (basis unresolved) | experimental | [1] Wang 2000 | Table 7, p. 7, row 4 |  |
| 1357.3 | eutectic: L1 -> (Cu) + (Mo) | L1: Mo 0.119; (Cu): Mo 0.023; (Mo): Mo 99.962 (basis unresolved) | experimental | [1] Wang 2000 | Table 7, p. 7, row 2 |  |
| 1356.6 | eutectic: L1 -> (Cu) + (Mo) | L1: Mo 0.101; (Cu): Mo 0.092; (Mo): Mo 99.958 (basis unresolved) | unspecified | [1] Wang 2000; _cites Brewer 1980_ | Table 7, p. 7, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cui Ping Wang, Xing Jun Liu, Ikuo Ohnuma, Ryosuke Kainuma, Kiyohito Ishida, Shi Ming Hao, Phase equilibria in the Cu-Fe-Mo and Cu-Fe-Nb systems, JPE 21, 54-62 (2000). [doi:10.1361/105497100770340426](https://doi.org/10.1361/105497100770340426)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
