# Er–V system

> Er–V system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-V.html · Markdown: https://data.orchid-project.org/systems/ER-V.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-V.json) · [CSV](https://data.orchid-project.org/systems/ER-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-V/ErV-09Wan.json) · [Markdown](https://data.orchid-project.org/systems/ER-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErV-09Wan.tdb | C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, J. Alloys Compd., 478, 197-201(2009). [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) | `0cbb8cd639da9723c84b8a15e69a524c76de7dcb260632eb4b8f9ae4422d9950` | [viewer](https://orchid-project.org/phase-diagrams/#ER-V/ErV-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErV-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErV-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErV-09Wan.tdb | 2143.46 | LIQUID (x(V) 0.11565) + LIQUID#2 (x(V) 0.97463) + BCC_A2 (x(V) 0.99944) |
| ErV-09Wan.tdb | 1753.09 | HCP_A3 (x(V) 0.00607) + LIQUID (x(V) 0.04484) + BCC_A2 (x(V) 0.99975) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–V system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2144.15 | Monotectic: L1 -> L2 + (V) | L1: V 0.115; L2: V 0.975; (V): V 0.999 | model | [1] Wang 2009 | Table 5, p. 5, row 2 |  |
| 2143.15 | Monotectic: L1 -> L2 + (V) | L1: V 0.114; L2: V 0.975; (V): V 0.999 | experimental | [1] Wang 2009; _cites ref. 29 1871_ | Table 5, p. 5, row 1 |  |
| 1753.15 | Eutectic: L -> (Er) + (V) | L: V 0.043; (Er): V 0.004; (V): V 0.9999 | experimental | [1] Wang 2009; _cites ref. 29 1871_ | Table 5, p. 5, row 3 |  |
| 1753.15 | Eutectic: L -> (Er) + (V) | L: V 0.045; (Er): V 0.006; (V): V 1 | model | [1] Wang 2009 | Table 5, p. 5, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009). [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
