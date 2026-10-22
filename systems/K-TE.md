# K–Te system

> K–Te system: 11 accepted literature values (invariant reaction 11) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/K-TE.html · Markdown: https://data.orchid-project.org/systems/K-TE.md

11 accepted literature values from 1 paper(s) (experimental 6, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/K-TE.json) · [CSV](https://data.orchid-project.org/systems/K-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#K-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#K-TE/KTe-14Che.json) · [Markdown](https://data.orchid-project.org/systems/K-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 11 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| KTe-14Che.tdb | Y. Chen, Y. Liu, M. Chu, L. Wang, J. Alloys Compd., 588, 605-10(2014). [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) | `1493e709e213dad3cf3bd1ea0109537e11313335cf72ccc23e7a7403d033d4fa` | [viewer](https://orchid-project.org/phase-diagrams/#K-TE/KTe-14Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/KTe-14Che.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| KTe-14Che.tdb | 914.75 | K2TE_C1 (x(Te) 0.33333) + K5TE3 (x(Te) 0.375) + LIQUID (x(Te) 0.42971) |
| KTe-14Che.tdb | 684.65 | K5TE3 (x(Te) 0.375) + KTE (x(Te) 0.5) + LIQUID (x(Te) 0.52559) |
| KTe-14Che.tdb | 669.19 | KTE (x(Te) 0.5) + LIQUID (x(Te) 0.54773) + K2TE3 (x(Te) 0.6) |
| KTe-14Che.tdb | 526.2 | K2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.76453) + HEXAGONAL_A8 (x(Te) 1) |
| KTe-14Che.tdb | 336.53 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0) + K2TE_C1 (x(Te) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/K/K-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/K/K-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the K–Te system (11)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 923 | Na5Te3 -> liq + K2Te |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 4 |  |
| 915 | Na5Te3 -> liq + K2Te | Na5Te3: Te 0.43 | model | [1] Chen 2014 | Table 5, p. 6, row 3 |  |
| 902 | Na5Te3 -> liq + K2Te |  | experimental | [1] Chen 2014; _cites Schewe-Miller_ | Table 5, p. 6, row 5 |  |
| 688 | KTe -> liq + K5Te3 |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 7 |  |
| 685 | KTe -> liq + K5Te3 | KTe: Te 0.53 | model | [1] Chen 2014 | Table 5, p. 6, row 6 |  |
| 669 | liq -> K2Te3 + KTe | liq: Te 0.55 | model | [1] Chen 2014 | Table 5, p. 6, row 8 |  |
| 660 | liq -> K2Te3 + KTe |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 9 |  |
| 526 | liq -> K2Te3 + Te | liq: Te 0.76 | model | [1] Chen 2014 | Table 5, p. 6, row 10 |  |
| 525 | liq -> K2Te3 + Te |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 11 |  |
| 336 | liq -> K + K2Te |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 2 |  |
| 335 | liq -> K + K2Te | K: Te 1.000e-4 | model | [1] Chen 2014 | Table 5, p. 6, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014). [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
