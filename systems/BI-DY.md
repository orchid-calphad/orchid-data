# Bi–Dy system

> Bi–Dy system: 14 accepted literature values (invariant reaction 12, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-DY.html · Markdown: https://data.orchid-project.org/systems/BI-DY.md

14 accepted literature values from 1 paper(s) (experimental 8, model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-DY.json) · [CSV](https://data.orchid-project.org/systems/BI-DY.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-DY) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-DY/BiDy-13Wan.json) · [Markdown](https://data.orchid-project.org/systems/BI-DY.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiDy-13Wan.tdb | J. Wang, C. Li, C. Guo, Z. Du, B. Wu, Thermochim. Acta, 566, 44-49(2013). [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) | `24b216373fd672e503023ee5355b36c6af3d86c60f9dc8b348e62a3e14170f5c` | [viewer](https://orchid-project.org/phase-diagrams/#BI-DY/BiDy-13Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiDy-13Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiDy-13Wan.tdb | 1719.23 | BIDY_B1 (x(Dy) 0.5) + BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.67184) |
| BiDy-13Wan.tdb | 1719.23 | BIDY_B1 (x(Dy) 0.5) + BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.67194) |
| BiDy-13Wan.tdb | 1719.23 | BIDY_B1 (x(Dy) 0.5) + BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.67164) |
| BiDy-13Wan.tdb | 1654.15 | LIQUID (x(Dy) 0.97461) + HCP_A3 (x(Dy) 1) + BCC_A2 (x(Dy) 1) |
| BiDy-13Wan.tdb | 1419.77 | BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.82656) + HCP_A3 (x(Dy) 1) |
| BiDy-13Wan.tdb | 1419.77 | BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.82664) + HCP_A3 (x(Dy) 1) |
| BiDy-13Wan.tdb | 543.54 | RHOMBOHEDRAL_A7 (x(Dy) 0) + LIQUID (x(Dy) 0.00426) + BIDY_B1 (x(Dy) 0.5) |
| BiDy-13Wan.tdb | 543.54 | RHOMBOHEDRAL_A7 (x(Dy) 0) + LIQUID (x(Dy) 0.00421) + BIDY_B1 (x(Dy) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-DY.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-DY.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Dy system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2048 | congruent melting: L -> BiDy | L: Bi 0.5; BiDy: Bi 0.5, Dy 0.5 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 5 |  |
| 2048 | congruent melting: L -> BiDy | L: Bi 0.5; BiDy: Bi 0.5, Dy 0.5 | model | [1] Wang 2013 | Table 2, p. 2, row 6 |  |
| 1719 | peritectic: L + BiDy -> Bi3Dy5 | L: Bi 0.335; BiDy: Bi 0.5, Dy 0.5; Bi3Dy5: Bi 0.375, Dy 0.625 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 3 |  |
| 1719 | peritectic: L + BiDy -> Bi3Dy5 | L: Bi 0.33; BiDy: Bi 0.5, Dy 0.5; Bi3Dy5: Bi 0.375, Dy 0.625 | model | [1] Wang 2013 | Table 2, p. 2, row 4 |  |
| 1719 | peritectic |  | model | [1] Wang 2013 | p. 5 | “The peritectic temperature for the formation of the intermetallic compound Bi3 Dy5 is 1719 K, and the congruent melting temperature of BiDy is 2023 K, the eutectic temperatures of the reactions, L ↔ Hcp A3 (Dy) + Bi3 Dy5 and L ↔ Rhomb (Bi) + BiDy, are 1420 and 543.5 K, respectively.” |
| 1693 | peritectic: L + BiDy ↔ Bi3 Dy5 |  | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | p. 2 | “According to measured data, the compound Bi3 Dy5 is formed by the peritectic reactions, L + BiDy ↔ Bi3 Dy5 at 1693 K, and the compound BiDy melts congruently at about 2048 K.” |
| 1428 | eutectic: L ↔ Hcp A3 (Dy) + Bi3 Dy5 |  | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | p. 2 | “There are two eutectic reactions, L ↔ Hcp A3 (Dy) + Bi3 Dy5 at 1428 K and L ↔ Rhomb (Bi) + BiDy at 544 K.” |
| 1420 | eutectic: L -> Bi3Dy5 + Hcp_A3 (Dy) | L: Bi 0.185; Bi3Dy5: Bi 0.375, Dy 0.625 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 1 |  |
| 1420 | eutectic: L -> Bi3Dy5 + Hcp_A3 (Dy) | L: Bi 0.175; Bi3Dy5: Bi 0.375, Dy 0.625 | model | [1] Wang 2013 | Table 2, p. 2, row 2 |  |
| 544 | eutectic: L ↔ Rhomb (Bi) + BiDy |  | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | p. 2 | “There are two eutectic reactions, L ↔ Hcp A3 (Dy) + Bi3 Dy5 at 1428 K and L ↔ Rhomb (Bi) + BiDy at 544 K.” |
| 543.5 | eutectic: L -> BiDy + Rhomb_A7 (Bi) | L: Bi 0.995; BiDy: Bi 0.5, Dy 0.5 | model | [1] Wang 2013 | Table 2, p. 2, row 8 |  |
| 542 | eutectic: L -> BiDy + Rhomb_A7 (Bi) | L: Bi 0.99; BiDy: Bi 0.5, Dy 0.5 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 7 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Bi–Dy system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2023 K | 2023 | congruent transformation | model | [1] Wang 2013 | p. 5 | “The peritectic temperature for the formation of the intermetallic compound Bi3 Dy5 is 1719 K, and the congruent melting temperature of BiDy is 2023 K, the eutectic temperatures of the reactions, L ↔ Hcp A3 (Dy) + Bi3 Dy5 and L ↔ Rhomb (Bi) + BiDy, are 1420 and 543.5 K, respectively.” |
| Phase transition | 2048 K | 2048 | congruent transformation | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | p. 2 | “According to measured data, the compound Bi3 Dy5 is formed by the peritectic reactions, L + BiDy ↔ Bi3 Dy5 at 1693 K, and the compound BiDy melts congruently at about 2048 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013). [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
