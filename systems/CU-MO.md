# Cu–Mo system

> Cu–Mo system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-MO.html · Markdown: https://data.orchid-project.org/systems/CU-MO.md

4 accepted literature values from 1 paper(s) (experimental 2, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-MO.json) · [CSV](https://data.orchid-project.org/systems/CU-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-MO/CuMo-00Wan.json) · [Markdown](https://data.orchid-project.org/systems/CU-MO.md)

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
| 2788.2 | Monotectic: L2 -> (Mo) + L1 | L2: Mo 92.8 (basis unresolved); (Mo): Mo 98.9 (basis unresolved); L1: Mo 16.8 (basis unresolved) | unspecified | [1] Wang 2000; _cites Brewer 1980_ | Table 7, p. 7, row 3 |  |
| 2787.6 | Monotectic: L2 -> (Mo) + L1 | L2: Mo 93.22 (basis unresolved); (Mo): Mo 98.96 (basis unresolved); L1: Mo 15.89 (basis unresolved) | experimental | [1] Wang 2000 | Table 7, p. 7, row 4 |  |
| 1357.3 | Eutectic: L1 -> (Cu) + (Mo) | L1: Mo 0.119; (Cu): Mo 0.023; (Mo): Mo 99.962 (basis unresolved) | experimental | [1] Wang 2000 | Table 7, p. 7, row 2 |  |
| 1356.6 | Eutectic: L1 -> (Cu) + (Mo) | L1: Mo 0.101; (Cu): Mo 0.092; (Mo): Mo 99.958 (basis unresolved) | unspecified | [1] Wang 2000; _cites Brewer 1980_ | Table 7, p. 7, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cui Ping Wang, Xing Jun Liu, Ikuo Ohnuma, Ryosuke Kainuma, Kiyohito Ishida, Shi Ming Hao, Phase equilibria in the Cu-Fe-Mo and Cu-Fe-Nb systems, JPE 21, 54-62 (2000). [doi:10.1361/105497100770340426](https://doi.org/10.1361/105497100770340426)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
