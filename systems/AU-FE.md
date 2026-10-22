# Au–Fe system

> Au–Fe system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-FE.html · Markdown: https://data.orchid-project.org/systems/AU-FE.md

10 accepted literature values from 1 paper(s) (experimental 7, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-FE.json) · [CSV](https://data.orchid-project.org/systems/AU-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-FE/AuFe-09Liu.json) · [Markdown](https://data.orchid-project.org/systems/AU-FE.md)

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
| AuFe-09Liu.tdb | Y. Liu, Y. Ge, D. Yu, J. Alloys Compd., 476, 79-83(2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) | `62024cbf6a5a64b2e47a21dc686240050056f7de3116f214f717ad5406a4c3d9` | [viewer](https://orchid-project.org/phase-diagrams/#AU-FE/AuFe-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuFe-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuFe-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuFe-09Liu.tdb | 1706.1 | LIQUID (x(Fe) 0.91092) + FCC_A1 (x(Fe) 0.97623) + BCC_A2 (x(Fe) 0.97905) |
| AuFe-09Liu.tdb | 1445.86 | LIQUID (x(Fe) 0.55299) + FCC_A1#2 (x(Fe) 0.72411) + FCC_A1 (x(Fe) 0.91087) |
| AuFe-09Liu.tdb | 1110.84 | FCC_A1 (x(Fe) 0.50773) + FCC_A1#2 (x(Fe) 0.97804) + BCC_A2 (x(Fe) 0.9909) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-FE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Fe system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1706 | liq + bcc -> fcc | L: Fe 0.911; bcc: Fe 0.979; fcc: Fe 0.976 | model | [1] Liu 2009 | Table 2, p. 3, row 1 |  |
| 1706 | liq + bcc -> fcc | L: Fe 0.897; bcc: Fe 0.977; fcc: Fe 0.972 | experimental | [1] Liu 2009; _cites Buckley 1963_ | Table 2, p. 3, row 2 |  |
| 1446 | liq + fcc -> fcc | L: Fe 0.553; fcc: Fe 0.724 | model | [1] Liu 2009 | Table 2, p. 3, row 3 |  |
| 1444 | liq + fcc -> fcc | fcc: Fe 0.959 | experimental | [1] Liu 2009; _cites Buckley 1963_ | Table 2, p. 3, row 6 |  |
| 1441 | liq + fcc -> fcc | L: Fe 0.566; fcc: Fe 0.694 | experimental | [1] Liu 2009; _cites Isaac 1907_ | Table 2, p. 3, row 4 |  |
| 1441 | liq + fcc -> fcc | L: Fe 0.57; fcc: Fe 0.745 | experimental | [1] Liu 2009; _cites Raub 1950_ | Table 2, p. 3, row 5 |  |
| 1176 | fcc -> fcc + bcc | fcc: Fe 0.56 | experimental | [1] Liu 2009; _cites Raub 1950_ | Table 2, p. 3, row 9 |  |
| 1133 | fcc -> fcc + bcc | fcc: Fe 0.978; bcc: Fe 0.994 | experimental | [1] Liu 2009; _cites Seigle 1956_ | Table 2, p. 3, row 10 |  |
| 1111 | fcc -> fcc + bcc | fcc: Fe 0.508; bcc: Fe 0.991 | model | [1] Liu 2009 | Table 2, p. 3, row 7 |  |
| 1103 | fcc -> fcc + bcc |  | experimental | [1] Liu 2009; _cites Isaac 1907_ | Table 2, p. 3, row 8 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
