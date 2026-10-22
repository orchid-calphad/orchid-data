# Th–Zn system

> Th–Zn system: 29 accepted literature values (invariant reaction 17, phase transition 12) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TH-ZN.html · Markdown: https://data.orchid-project.org/systems/TH-ZN.md

29 accepted literature values from 1 paper(s) (experimental 19, model 10); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/TH-ZN.json) · [CSV](https://data.orchid-project.org/systems/TH-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#TH-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#TH-ZN/ThZn-10Li.json) · [Markdown](https://data.orchid-project.org/systems/TH-ZN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ThZn-10Li.tdb | Z.S. Li, X.J. Liu, M.Z. Wen, C.P. Wang, A.T. Tang, F.S. Pan, J. Nucl. Mater., 396, 170-75(2010). [doi:10.1016/j.jnucmat.2009.10.068](https://doi.org/10.1016/j.jnucmat.2009.10.068) | `f6e94ddb75cfa754d4b024b74d1f2e5fafb57ef1405bdfc68137d16b2e88e863` | [viewer](https://orchid-project.org/phase-diagrams/#TH-ZN/ThZn-10Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ThZn-10Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ThZn-10Li.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ThZn-10Li.tdb | 1631.66 | FCC_A1 (x(Zn) 0.00196) + BCC_A2 (x(Zn) 0.00222) + LIQUID (x(Zn) 0.14785) |
| ThZn-10Li.tdb | 1316.1 | FCC_A1 (x(Zn) 0.00135) + LIQUID (x(Zn) 0.28142) + TH2ZN_C16 (x(Zn) 0.33333) |
| ThZn-10Li.tdb | 1316.1 | FCC_A1 (x(Zn) 0.00135) + LIQUID (x(Zn) 0.28154) + TH2ZN_C16 (x(Zn) 0.33333) |
| ThZn-10Li.tdb | 1312.11 | THZN2 (x(Zn) 0.66667) + LIQUID (x(Zn) 0.73893) + THZN4_D13 (x(Zn) 0.8) |
| ThZn-10Li.tdb | 1312.11 | THZN2 (x(Zn) 0.66667) + LIQUID (x(Zn) 0.73903) + THZN4_D13 (x(Zn) 0.8) |
| ThZn-10Li.tdb | 1312.11 | THZN2 (x(Zn) 0.66667) + LIQUID (x(Zn) 0.73879) + THZN4_D13 (x(Zn) 0.8) |
| ThZn-10Li.tdb | 1271.16 | THZN4_D13 (x(Zn) 0.8) + LIQUID (x(Zn) 0.8669) + TH2ZN17 (x(Zn) 0.89474) |
| ThZn-10Li.tdb | 1271.16 | THZN4_D13 (x(Zn) 0.8) + LIQUID (x(Zn) 0.86673) + TH2ZN17 (x(Zn) 0.89474) |
| ThZn-10Li.tdb | 1217.32 | TH2ZN_C16 (x(Zn) 0.33333) + LIQUID (x(Zn) 0.49951) + THZN2 (x(Zn) 0.66667) |
| ThZn-10Li.tdb | 692.67 | TH2ZN17 (x(Zn) 0.89474) + LIQUID (x(Zn) 0.99999) + HCP_A3 (x(Zn) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/TH/TH-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/TH/TH-ZN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Th–Zn system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1633.15 | Catatectic reaction: βTh ↔ αTh + L | βTh: Zn 0; αTh: Zn 0 | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 1 |  |
| 1631.65 | Catatectic reaction: βTh ↔ αTh + L | βTh: Zn 0.0022; αTh: Zn 0.002; L: Zn 0.148 | model | [1] Li 2010 | Table 5, p. 5, row 2 |  |
| 1318.15 | eutectic: L M ThZn4+ Th2Zn17 |  | experimental | [1] Li 2010 | p. 3 | “Five eutectic reactions of the L M aTh + Th2Zn, L M ThZn2+ ThZn4, L M ThZn4+ Th2Zn17, L M Th2Zn + ThZn2 and L M Th2Zn17 + Zn exist in this system with the following eutectic temperatures and Zn atom percentages: 1040 °C and 30.5 at.% Zn, 945 °C and 48.6 at.% Zn, 1045 °C and 74.4 at.% Zn, 995 °C and 86.8 at.% Zn, 419.58 °C and 0 at.% Zn.” |
| 1318.15 | Eutectic reaction: L ↔ ThZn2 + ThZn4 | L: Zn 0.744; ThZn2: Zn 0.667; ThZn4: Zn 0.8 | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 5 |  |
| 1317.15 | Eutectic reaction: L ↔ αTh + Th2Zn | L: Zn 0.281; αTh: Zn 0.0014; Th2Zn: Zn 0.333 | model | [1] Li 2010 | Table 5, p. 5, row 4 |  |
| 1314.15 | Eutectic reaction: L ↔ ThZn2 + ThZn4 | L: Zn 0.74; ThZn2: Zn 0.667; ThZn4: Zn 0.8 | model | [1] Li 2010 | Table 5, p. 5, row 6 |  |
| 1313.15 | eutectic: L M aTh + Th2Zn |  | experimental | [1] Li 2010 | p. 3 | “Five eutectic reactions of the L M aTh + Th2Zn, L M ThZn2+ ThZn4, L M ThZn4+ Th2Zn17, L M Th2Zn + ThZn2 and L M Th2Zn17 + Zn exist in this system with the following eutectic temperatures and Zn atom percentages: 1040 °C and 30.5 at.% Zn, 945 °C and 48.6 at.% Zn, 1045 °C and 74.4 at.% Zn, 995 °C and 86.8 at.% Zn, 419.58 °C and 0 at.% Zn.” |
| 1313.15 | Eutectic reaction: L ↔ αTh + Th2Zn | L: Zn 0.305; αTh: Zn 0; Th2Zn: Zn 0.333 | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 3 |  |
| 1272.15 | Eutectic reaction: L ↔ ThZn4 + Th2Zn17 | L: Zn 0.867; ThZn4: Zn 0.8; Th2Zn17: Zn 0.895 | model | [1] Li 2010 | Table 5, p. 5, row 8 |  |
| 1268.15 | eutectic: L M Th2Zn + ThZn2 |  | experimental | [1] Li 2010 | p. 3 | “Five eutectic reactions of the L M aTh + Th2Zn, L M ThZn2+ ThZn4, L M ThZn4+ Th2Zn17, L M Th2Zn + ThZn2 and L M Th2Zn17 + Zn exist in this system with the following eutectic temperatures and Zn atom percentages: 1040 °C and 30.5 at.% Zn, 945 °C and 48.6 at.% Zn, 1045 °C and 74.4 at.% Zn, 995 °C and 86.8 at.% Zn, 419.58 °C and 0 at.% Zn.” |
| 1268.15 | Eutectic reaction: L ↔ ThZn4 + Th2Zn17 | L: Zn 0.868; ThZn4: Zn 0.8; Th2Zn17: Zn 0.895 | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 7 |  |
| 1218.15 | Eutectic reaction: L ↔ Th2Zn + ThZn2 | L: Zn 0.486; Th2Zn: Zn 0.333; ThZn2: Zn 0.667 | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 9 |  |
| 1218.15 | eutectic: L M ThZn2+ ThZn4 |  | experimental | [1] Li 2010 | p. 3 | “Five eutectic reactions of the L M aTh + Th2Zn, L M ThZn2+ ThZn4, L M ThZn4+ Th2Zn17, L M Th2Zn + ThZn2 and L M Th2Zn17 + Zn exist in this system with the following eutectic temperatures and Zn atom percentages: 1040 °C and 30.5 at.% Zn, 945 °C and 48.6 at.% Zn, 1045 °C and 74.4 at.% Zn, 995 °C and 86.8 at.% Zn, 419.58 °C and 0 at.% Zn.” |
| 1218.15 | Eutectic reaction: L ↔ Th2Zn + ThZn2 | L: Zn 0.499; Th2Zn: Zn 0.333; ThZn2: Zn 0.667 | model | [1] Li 2010 | Table 5, p. 5, row 10 |  |
| 692.73 | eutectic: L M Th2Zn17 + Zn |  | experimental | [1] Li 2010 | p. 3 | “Five eutectic reactions of the L M aTh + Th2Zn, L M ThZn2+ ThZn4, L M ThZn4+ Th2Zn17, L M Th2Zn + ThZn2 and L M Th2Zn17 + Zn exist in this system with the following eutectic temperatures and Zn atom percentages: 1040 °C and 30.5 at.% Zn, 945 °C and 48.6 at.% Zn, 1045 °C and 74.4 at.% Zn, 995 °C and 86.8 at.% Zn, 419.58 °C and 0 at.% Zn.” |
| 692.73 | Eutectic reaction: L ↔ Th2Zn17 + (Zn) | L: Zn 1; Th2Zn17: Zn 0.895; (Zn): Zn 1 | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 11 |  |
| 692.67 | Eutectic reaction: L ↔ Th2Zn17 + (Zn) | L: Zn 1; Th2Zn17: Zn 0.895; (Zn): Zn 1 | model | [1] Li 2010 | Table 5, p. 5, row 12 |  |

## Other properties

### Phase transition (12)

Table: Phase transition, Th–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1287.15 K | 1287.15 | Congruent reaction: L ↔ Th2Zn17; _L: Zn 0.895; Th2Zn17: Zn 0.895_ | model | [1] Li 2010 | Table 5, p. 5, row 20 |  |
| Phase transition | 1288.15 K | 1288.15 | Congruent reaction: L ↔ Th2Zn17; _L: Zn 0.895; Th2Zn17: Zn 0.895_ | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 19 |  |
| Phase transition | 1288.15 K | 1288.15 | Th2Zn17 | experimental | [1] Li 2010 | p. 3 | “and vapor pressure method, and found that the melting points of these compounds (Th2Zn, ThZn2, ThZn4 and Th2Zn17) under constrained vapor conditions were 1055 °C, 1105 °C, 1095 °C and 1015 °C, respectively.” |
| Phase transition | 1325.15 K | 1325.15 | Congruent reaction: L ↔ Th2Zn; _L: Zn 0.333; Th2Zn: Zn 0.333_ | model | [1] Li 2010 | Table 5, p. 5, row 14 |  |
| Phase transition | 1328.15 K | 1328.15 | Congruent reaction: L ↔ Th2Zn; _L: Zn 0.333; Th2Zn: Zn 0.333_ | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 13 |  |
| Phase transition | 1328.15 K | 1328.15 | Th2Zn | experimental | [1] Li 2010 | p. 3 | “and vapor pressure method, and found that the melting points of these compounds (Th2Zn, ThZn2, ThZn4 and Th2Zn17) under constrained vapor conditions were 1055 °C, 1105 °C, 1095 °C and 1015 °C, respectively.” |
| Phase transition | 1368.15 K | 1368.15 | Congruent reaction: L ↔ ThZn4; _L: Zn 0.8; ThZn4: Zn 0.8_ | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 17 |  |
| Phase transition | 1368.15 K | 1368.15 | ThZn4 | experimental | [1] Li 2010 | p. 3 | “and vapor pressure method, and found that the melting points of these compounds (Th2Zn, ThZn2, ThZn4 and Th2Zn17) under constrained vapor conditions were 1055 °C, 1105 °C, 1095 °C and 1015 °C, respectively.” |
| Phase transition | 1371.15 K | 1371.15 | Congruent reaction: L ↔ ThZn4; _L: Zn 0.8; ThZn4: Zn 0.8_ | model | [1] Li 2010 | Table 5, p. 5, row 18 |  |
| Phase transition | 1378.15 K | 1378.15 | Congruent reaction: L ↔ ThZn2; _L: Zn 0.667; ThZn2: Zn 0.667_ | experimental | [1] Li 2010; _cites Okamoto 2000_ | Table 5, p. 5, row 15 |  |
| Phase transition | 1378.15 K | 1378.15 | Congruent reaction: L ↔ ThZn2; _L: Zn 0.667; ThZn2: Zn 0.667_ | model | [1] Li 2010 | Table 5, p. 5, row 16 |  |
| Phase transition | 1378.15 K | 1378.15 | ThZn2 | experimental | [1] Li 2010 | p. 3 | “and vapor pressure method, and found that the melting points of these compounds (Th2Zn, ThZn2, ThZn4 and Th2Zn17) under constrained vapor conditions were 1055 °C, 1105 °C, 1095 °C and 1015 °C, respectively.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z.S. Li, X.J. Liu, M.Z. Wen, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Al–Th and Th–Zn systems, Journal of Nuclear Materials 396, 170-175 (2010). [doi:10.1016/j.jnucmat.2009.10.068](https://doi.org/10.1016/j.jnucmat.2009.10.068)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
