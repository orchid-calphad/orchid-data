# Na–Zn system

> Na–Zn system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NA-ZN.html · Markdown: https://data.orchid-project.org/systems/NA-ZN.md

10 accepted literature values from 1 paper(s) (experimental 7, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NA-ZN.json) · [CSV](https://data.orchid-project.org/systems/NA-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NA-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NA-ZN/NaZn-09Liu.json) · [Markdown](https://data.orchid-project.org/systems/NA-ZN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NaZn-09Liu.tdb | Y. Liu, Y. Ge, D. Yu, J. Alloys Compd., 476, 79-83(2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) | `837dc17668b272cc6642ac721c05572f455e7a6d2a2ef98a1d817c669bf9bb18` | [viewer](https://orchid-project.org/phase-diagrams/#NA-ZN/NaZn-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaZn-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaZn-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NaZn-09Liu.tdb | 830.01 | LIQUID#2 (x(Zn) 0.09415) + NAZN13_D23 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.9446) |
| NaZn-09Liu.tdb | 692.59 | NAZN13_D23 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.99984) + HCP_A3 (x(Zn) 1) |
| NaZn-09Liu.tdb | 370.83 | BCC_A2 (x(Zn) 0) + LIQUID (x(Zn) 1.000e-4) + NAZN13_D23 (x(Zn) 0.92857) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NA/NA-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NA/NA-ZN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Na–Zn system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 830 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 0.945 | model | [1] Liu 2009 | Table 4, p. 4, row 1 |  |
| 830 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 0.975 | experimental | [1] Liu 2009; _cites Hausler 1958_ | Table 4, p. 4, row 4 |  |
| 830 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Mathewson 1906_ | Table 4, p. 4, row 2 |  |
| 821 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Cetin 1991_ [doi](https://doi.org/10.1007/bf02663664) | Table 4, p. 4, row 3 |  |
| 693 | liq \<-> NaZn13 + hcp | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 0.9998 | model | [1] Liu 2009 | Table 4, p. 4, row 5 |  |
| 692.4 | liq \<-> NaZn13 + hcp | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Hausler 1958_ | Table 4, p. 4, row 6 |  |
| 371 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Mathewson 1906_ | Table 4, p. 4, row 8 |  |
| 371 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Cetin 1991_ [doi](https://doi.org/10.1007/bf02663664) | Table 4, p. 4, row 9 |  |
| 371 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 1.000e-4 | model | [1] Liu 2009 | Table 4, p. 4, row 7 |  |
| 370 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Hausler 1958_ | Table 4, p. 4, row 10 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
