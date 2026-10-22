# Bi–Y system

> Bi–Y system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-Y.html · Markdown: https://data.orchid-project.org/systems/BI-Y.md

10 accepted literature values from 1 paper(s) (experimental 6, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-Y.json) · [CSV](https://data.orchid-project.org/systems/BI-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-Y/BiY-11Wan.json) · [Markdown](https://data.orchid-project.org/systems/BI-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiY-11Wan.tdb | S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 32, 441-46(2011). [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) | `ac3d63c817a8399a6b4a113fd2c037e46b0c7d1b3a9c872f978c765786aed982` | [viewer](https://orchid-project.org/phase-diagrams/#BI-Y/BiY-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiY-11Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiY-11Wan.tdb | 1804.07 | BIY_B1 (x(Y) 0.5) + BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.67558) |
| BiY-11Wan.tdb | 1804.06 | BIY_B1 (x(Y) 0.5) + BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.67578) |
| BiY-11Wan.tdb | 1804.06 | BIY_B1 (x(Y) 0.5) + BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.67581) |
| BiY-11Wan.tdb | 1751.97 | LIQUID (x(Y) 0.9736) + HCP_A3 (x(Y) 0.99984) + BCC_A2 (x(Y) 1) |
| BiY-11Wan.tdb | 1751.97 | LIQUID (x(Y) 0.97362) + HCP_A3 (x(Y) 0.99984) + BCC_A2 (x(Y) 1) |
| BiY-11Wan.tdb | 1417.65 | BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.81825) + HCP_A3 (x(Y) 0.99795) |
| BiY-11Wan.tdb | 1417.65 | BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.81825) + HCP_A3 (x(Y) 0.99795) |
| BiY-11Wan.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(Y) 0) + LIQUID (x(Y) 1.000e-5) + BIY_B1 (x(Y) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Y system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2293.15 | Congruent: L -> BiY | L: Y 0.5; BiY: Y 0.5 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 3 |  |
| 2292.65 | Congruent: L -> BiY | L: Y 0.5; BiY: Y 0.5 | model | [1] Wang 2011 | Table 4, p. 5, row 4 |  |
| 1804.05 | Peritectic: L + BiY -> Bi3Y5 | L: Y 0.676; BiY: Y 0.5; Bi3Y5: Y 0.625 | model | [1] Wang 2011 | Table 4, p. 5, row 6 |  |
| 1803.15 | Peritectic: L + BiY -> Bi3Y5 | BiY: Y 0.5; Bi3Y5: Y 0.625 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 5 |  |
| 1418.15 | Eutectic: L -> Bi3Y5 + (αY) | L: Y 0.815; Bi3Y5: Y 0.625; (αY): Y 1 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 7 |  |
| 1418.15 | eutectic: L (81.5 at.% Y) M aY + Bi3Y5 |  | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | p. 2 | “Schmidt et al.\[18\] also determined two eutectic reactions: L (\<0.1 at.% Y) M (Bi) + BiY at 269 C and L (81.5 at.% Y) M aY + Bi3Y5 at 1145 C.” |
| 1417.65 | Eutectic: L -> Bi3Y5 + (αY) | L: Y 0.818; Bi3Y5: Y 0.625; (αY): Y 0.998 | model | [1] Wang 2011 | Table 4, p. 5, row 8 |  |
| 544.55 | Eutectic: L -> (Bi) + BiY | L: Y 0; (Bi): Y 0; BiY: Y 0.5 | model | [1] Wang 2011 | Table 4, p. 5, row 2 |  |
| 542.15 | Eutectic: L -> (Bi) + BiY | (Bi): Y 0; BiY: Y 0.5 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 1 |  |
| 542.15 | eutectic: L (\<0.1 at.% Y) M (Bi) + BiY |  | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | p. 2 | “Schmidt et al.\[18\] also determined two eutectic reactions: L (\<0.1 at.% Y) M (Bi) + BiY at 269 C and L (81.5 at.% Y) M aY + Bi3Y5 at 1145 C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011). [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
