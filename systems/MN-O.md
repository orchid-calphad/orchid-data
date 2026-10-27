# Mn–O system

> Mn–O system: 352 accepted literature values (model expression 113, formation 103, heat capacity / entropy / enthalpy 69, invariant reaction 53) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MN-O.html · Markdown: https://data.orchid-project.org/systems/MN-O.md

352 accepted literature values from 2 paper(s) (experimental 172, model 162, unspecified 18); 2 calculated phase diagram(s). 12 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/MN-O.json) · [CSV](https://data.orchid-project.org/systems/MN-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MN-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MN-O/MnO-03Gru-LB.json) · [phases (16)](https://data.orchid-project.org/phases/pages/MN-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MN-O.html) · [Markdown](https://data.orchid-project.org/systems/MN-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 172 |
| model | 162 |
| unspecified | 18 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 53 |
| phase transition | 13 |
| formation | 103 |
| mixing / partial | 1 |
| heat capacity / entropy / enthalpy | 69 |
| model expression | 113 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MnO-03Gru-LB.tdb | A.N. Grundy, B. Hallstedt, L.J. Gauckler, J. Phase Equilib., 24, 21-39(2003). [doi:10.1007/s11669-003-0004-6](https://doi.org/10.1007/s11669-003-0004-6) | `2f59cdf668abb9e9b63c4e51c301e56a79ea939461bfe9b832d2f4fccf8acab9` | [viewer](https://orchid-project.org/phase-diagrams/#MN-O/MnO-03Gru-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnO-03Gru-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnO-03Gru-LB.json) |
| MnO-10Kje.tdb | L. Kjellqvist, M. Selleby, J. Phase Equilib. Diffus., 31, 113-34(2010). [doi:10.1007/s11669-009-9643-6](https://doi.org/10.1007/s11669-009-9643-6) | `bd1f5b2a6c1bd76ecf6bb6078f7eb9b9f0ebd2b5d2cd94ace3139aed8273e1ea` | [viewer](https://orchid-project.org/phase-diagrams/#MN-O/MnO-10Kje.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnO-10Kje.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnO-10Kje.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MnO-03Gru-LB.tdb | 2341.85 | GAS (x(O) 7.000e-5) + ION#2 (x(O) 0.01139) + ION (x(O) 0.46845) |
| MnO-03Gru-LB.tdb | 2057.03 | ION (x(O) 0.00598) + ION#2 (x(O) 0.47748) + B1_OXIDE (x(O) 0.50019) |
| MnO-03Gru-LB.tdb | 1882.41 | ION (x(O) 0.5525) + MN3O4_H11 (x(O) 0.57143) + GAS (x(O) 1) |
| MnO-03Gru-LB.tdb | 1518.46 | BCC_A2 (x(O) 0) + ION (x(O) 3.600e-4) + B1_OXIDE (x(O) 0.50002) |
| MnO-03Gru-LB.tdb | 1503.51 | BCC_A2 (x(O) 0) + LIQUID (x(O) 0) + FCC_A1 (x(O) 0) |
| MnO-03Gru-LB.tdb | 1442.97 | MN3O4_H11 (x(O) 0.57143) + MN3O4_ALPHA (x(O) 0.57143) + GAS (x(O) 1) |
| MnO-03Gru-LB.tdb | 1411.01 | FCC_A1 (x(O) 0) + BCC_A2 (x(O) 0) + B1_OXIDE (x(O) 0.50001) |
| MnO-03Gru-LB.tdb | 1359.99 | CUB_A13 (x(O) 0) + FCC_A1 (x(O) 0) + B1_OXIDE (x(O) 0.50001) |
| MnO-03Gru-LB.tdb | 1237.26 | MN3O4_ALPHA (x(O) 0.57143) + MN2O3_D53 (x(O) 0.6) + GAS (x(O) 1) |
| MnO-03Gru-LB.tdb | 980 | CUB_A13 (x(O) 0) + CBCC_A12 (x(O) 0) + B1_OXIDE (x(O) 0.5) |
| MnO-10Kje.tdb | 2341.85 | GAS (x(O) 7.000e-5) + ION#2 (x(O) 0.01139) + ION (x(O) 0.46842) |
| MnO-10Kje.tdb | 2056.71 | ION (x(O) 0.00598) + ION#2 (x(O) 0.47748) + B1_OXIDE (x(O) 0.50019) |
| MnO-10Kje.tdb | 1878.72 | ION (x(O) 0.55266) + SPINEL_H11 (x(O) 0.57144) + GAS (x(O) 1) |
| MnO-10Kje.tdb | 1833.45 | B1_OXIDE (x(O) 0.53321) + ION (x(O) 0.54684) + SPINEL_H11 (x(O) 0.57123) |
| MnO-10Kje.tdb | 1518.46 | BCC_A2 (x(O) 0) + ION (x(O) 3.600e-4) + B1_OXIDE (x(O) 0.50002) |
| MnO-10Kje.tdb | 1443.79 | SPINEL_H11 (x(O) 0.57148) + MN3O4_A (x(O) 0.57161) + GAS (x(O) 1) |
| MnO-10Kje.tdb | 1442.89 | B1_OXIDE (x(O) 0.5104) + MN3O4_A (x(O) 0.57132) + SPINEL_H11 (x(O) 0.57139) |
| MnO-10Kje.tdb | 1411.01 | FCC_A1 (x(O) 0) + BCC_A2 (x(O) 0) + B1_OXIDE (x(O) 0.50001) |
| MnO-10Kje.tdb | 1359.99 | CUB_A13 (x(O) 0) + FCC_A1 (x(O) 0) + B1_OXIDE (x(O) 0.50001) |
| MnO-10Kje.tdb | 980 | CUB_A13 (x(O) 0) + CBCC_A12 (x(O) 0) + B1_OXIDE (x(O) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MN/MN-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MN/MN-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mn–O system (53)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2158 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Schurmann 1984_ [doi](https://doi.org/10.1002/srin.198405356) | Table 2, p. 4, row 18; `ORC-UAQ4UQWI5U` |  |
| 2148 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Fischer 1961_ [doi](https://doi.org/10.1002/srin.196103182) | Table 2, p. 4, row 13; `ORC-NSRKRO72AL` |  |
| 2148 | monotectic: L1 + L2 + MnO | MnO: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Schurmann 1984_ [doi](https://doi.org/10.1002/srin.198405356) | Table 2, p. 4, row 4; `ORC-YMISGP5H2F` |  |
| 2124 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | model | [1] Grundy 2003 | Table 2, p. 4, row 21; `ORC-5LDD7Y4H52` |  |
| 2123 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Glasser 1958_ [doi](https://doi.org/10.2475/ajs.256.6.398) | Table 2, p. 4, row 15; `ORC-Q5Z6NTSGQH` |  |
| 2123 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Tromel 1976_ | Table 2, p. 4, row 17; `ORC-TW7MF3J2FD` |  |
| 2115 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Schenck 1964_ [doi](https://doi.org/10.1002/srin.196402318) | Table 2, p. 4, row 19; `ORC-IA643BOB2O` |  |
| 2063 | monotectic: L1 + L2 + MnO | MnO: Mn 0.5, O 0.5; Liquid: O 0.495 | experimental | [1] Grundy 2003; _cites Tromel 1976_ | Table 2, p. 4, row 3; `ORC-WCISZWP3TD` |  |
| 2057 | monotectic: L1 + L2 + MnO | MnO: Mn 0.5, O 0.5; Liquid: O 0.477 | model | [1] Grundy 2003 | Table 2, p. 4, row 5; `ORC-YZCL5ACVD3` |  |
| 2033 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Hed 1967_ [doi](https://doi.org/10.1149/1.2426584) | Table 2, p. 4, row 16; `ORC-6PDLODDU2L` |  |
| 2023 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Schenck 1957_ [doi](https://doi.org/10.1002/srin.195702172) | Table 2, p. 4, row 14; `ORC-4IXVUCBZJ3` |  |
| 1973 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Benedicks 1930_ | Table 2, p. 4, row 11; `ORC-GURFZJMJTM` |  |
| 1863 | β-Mn3O4 -> Liq + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Von 1937_ | Table 2, p. 4, row 37; `ORC-4EOYRLEVJW` |  |
| 1858 | congruent melting: MnO -> Liquid | MnO: Mn 0.5, O 0.5; Liquid: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Andrew 1931_ | Table 2, p. 4, row 12; `ORC-LJFRXU3ZPD` |  |
| 1853 | β-Mn3O4 -> Liq + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Tromel 1976_ | Table 2, p. 4, row 42; `ORC-3RAQEM6RSR` |  |
| 1846 | β-Mn3O4 -> Liq + O2(g) (in air/O2) | Liquid: O 0.548 | model | [1] Grundy 2003 | Table 2, p. 4, row 44; `ORC-3XFZ5DZG4I` |  |
| 1840 | β-Mn3O4 -> Liq + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Hahn 1960_ [doi](https://doi.org/10.2475/ajs.258.1.66) | Table 2, p. 4, row 38; `ORC-VNLGGF7NHT` |  |
| 1838 | β-Mn3O4 -> Liq + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Hed 1967_ [doi](https://doi.org/10.1149/1.2426584) | Table 2, p. 4, row 41; `ORC-R5JV5EKXXX` |  |
| 1835 | eutectic: L2 + β-Mn3O4 + MnO | MnO: Mn 0.5, O 0.5; Liquid: O 0.546 | model | [1] Grundy 2003 | Table 2, p. 4, row 10; `ORC-3L743IJS2E` |  |
| 1835 | β-Mn3O4 -> Liq + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Van 1958_ | Table 2, p. 4, row 39; `ORC-MXRFYATJD2` |  |
| 1835 | β-Mn3O4 -> Liq + O2(g) (in air/O2) |  | unspecified | [1] Grundy 2003; _cites Pankratz 1982_ | Table 2, p. 4, row 43; `ORC-NWWLWCWN7A` |  |
| 1833 | eutectic: L2 + β-Mn3O4 + MnO | MnO: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Schmahl 1969_ [doi](https://doi.org/10.1002/srin.196904332) | Table 2, p. 4, row 8; `ORC-CVGVSMCO43` |  |
| 1833 | eutectic: L2 + β-Mn3O4 + MnO | MnO: Mn 0.5, O 0.5; Liquid: O 0.54 | experimental | [1] Grundy 2003; _cites Tromel 1976_ | Table 2, p. 4, row 9; `ORC-TE3YJ62T6A` |  |
| 1833 | β-Mn3O4 -> Liq + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Schmahl 1969_ [doi](https://doi.org/10.1002/srin.196904332) | Table 2, p. 4, row 40; `ORC-U62YWFAX46` |  |
| 1828 | eutectic: L2 + β-Mn3O4 + MnO | MnO: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Hed 1967_ [doi](https://doi.org/10.1149/1.2426584) | Table 2, p. 4, row 7; `ORC-B3HKXHSTP7` |  |
| 1813 | eutectic: L2 + β-Mn3O4 + MnO | MnO: Mn 0.5, O 0.5 | experimental | [1] Grundy 2003; _cites Hahn 1960_ [doi](https://doi.org/10.2475/ajs.258.1.66) | Table 2, p. 4, row 6; `ORC-GRZ6CBJKAX` |  |
| 1518 | Mn + L1 + MnO | MnO: Mn 0.5, O 0.5; Liquid: O 3.600e-4 | model | [1] Grundy 2003 | Table 2, p. 4, row 2; `ORC-MKIBQWNK52` |  |
| 1515 | Mn + L1 + MnO | MnO: Mn 0.5, O 0.5; Liquid: O 1.000e-4 | experimental | [1] Grundy 2003; _cites Schenck 1964_ [doi](https://doi.org/10.1002/srin.196402318) | Table 2, p. 4, row 1; `ORC-DJM5PSR7DJ` |  |
| 1473 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Schmier 1966_ [doi](https://doi.org/10.1002/zaac.19663460310) | Table 2, p. 4, row 26; `ORC-MRYPNLAKTS` |  |
| 1450 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Ramano 1973_ | Table 2, p. 4, row 28; `ORC-WBYV73YS5U` |  |
| 1449.2 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Keller 1985_ [doi](https://doi.org/10.1002/bbpc.19850890815) | Table 2, p. 4, row 33; `ORC-VTTMHKP5FP` |  |
| 1445 | α-Mn3O4-β-Mn3O4 |  | unspecified | [1] Grundy 2003; _cites Pankratz 1982_ | Table 2, p. 4, row 34; `ORC-CH6GAP4ZXT` |  |
| 1445 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Southard 1942_ [doi](https://doi.org/10.1021/ja01260a007) | Table 2, p. 4, row 22; `ORC-L5Z3ZYHLKZ` |  |
| 1443 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Irani 1962_ [doi](https://doi.org/10.1016/0022-3697%2862%2990530-9) | Table 2, p. 4, row 25; `ORC-62KPDYNCU2` |  |
| 1443 | α-Mn3O4-β-Mn3O4 |  | model | [1] Grundy 2003 | Table 2, p. 4, row 36; `ORC-DGU4RM25XF` |  |
| 1443 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites McMurdie 1948_ [doi](https://doi.org/10.6028/jres.041.046) | Table 2, p. 4, row 35; `ORC-R4CUIWBXRX` |  |
| 1433 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Van 1958_ | Table 2, p. 4, row 24; `ORC-MMOIQ6FLH3` |  |
| 1430 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Metselaar 1981_ [doi](https://doi.org/10.1016/0022-4596%2881%2990064-5) | Table 2, p. 4, row 30; `ORC-34LZG73LSJ` |  |
| 1429.2 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Keller 1985_ [doi](https://doi.org/10.1002/bbpc.19850890815) | Table 2, p. 4, row 32; `ORC-TU2IWJPMTO` |  |
| 1407.6 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Keller 1985_ [doi](https://doi.org/10.1002/bbpc.19850890815) | Table 2, p. 4, row 31; `ORC-FS2QHQXAMY` |  |
| 1403 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Driessens 1967_ [doi](https://doi.org/10.1016/s0020-1693%2800%2993169-4) | Table 2, p. 4, row 27; `ORC-VNZBPJCOWY` |  |
| 1368 | α-Mn3O4-β-Mn3O4 |  | experimental | [1] Grundy 2003; _cites Tromel 1976_ | Table 2, p. 4, row 29; `ORC-ANNXCC7SBD` |  |
| 1350 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | unspecified | [1] Grundy 2003; _cites Pankratz 1982_ | Table 2, p. 4, row 52; `ORC-6I5UA6UUCB` |  |
| 1243 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Kissinger 1956_ | Table 2, p. 4, row 47; `ORC-TL5FOKUXZA` |  |
| 1223 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites McMurdie 1948_ [doi](https://doi.org/10.6028/jres.041.046) | Table 2, p. 4, row 53; `ORC-GMSRDPXH43` |  |
| 1213 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Meyer 1908_ [doi](https://doi.org/10.1002/zaac.19080570105) | Table 2, p. 4, row 45; `ORC-NUVT7M3PRP` |  |
| 1157.4 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Ingraham 1966_ [doi](https://doi.org/10.1179/cmq.1966.5.2.109) | Table 2, p. 4, row 50; `ORC-UEBCQP62ZY` |  |
| 1154 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Schmahl 1963_ [doi](https://doi.org/10.1002/srin.196304016) | Table 2, p. 4, row 49; `ORC-TLQ367CPGF` |  |
| 1153 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | model | [1] Grundy 2003 | Table 2, p. 4, row 54; `ORC-6ZM6JO5ZNM` |  |
| 1150 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Hahn 1960_ [doi](https://doi.org/10.2475/ajs.258.1.66) | Table 2, p. 4, row 46; `ORC-QZG3IMXNE6` |  |
| 1144 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Schwerdtfeger 1967_ | Table 2, p. 4, row 51; `ORC-ZUGDSJK5KI` |  |
| 958 | Mn2O3 -> α-Mn3O4 + O2(g) (in air/O2) |  | experimental | [1] Grundy 2003; _cites Klingsberg 1960_ | Table 2, p. 4, row 48; `ORC-I2YMXU6VWZ` |  |
| 800 | MnO2 -> Mn2O3 + O2(g) (in air/O2) | MnO2: O 0.666667; Mn2O3: O 0.6 | unspecified | [1] Grundy 2003; _cites Pankratz 1982_ | Table 2, p. 5, row 5; `ORC-PNFBWIVWJY` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Mn–O system (103)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -194.854 kJ/mol-atom | 298.15 | experimental | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 25; `ORC-X7TRQ4WAKF` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -194.77 kJ/mol-atom | 298.15 | experimental | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 26; `ORC-FR3Y2JBCSB` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -192.518 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003 | Table 11, p. 16, row 33; `ORC-DQIKEJQME3` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.922 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 30; `ORC-F4EHAU27AH` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.922 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Brewer 1953_ [doi](https://doi.org/10.1021/cr60161a001) | Table 11, p. 16, row 27; `ORC-S6ZFMTAZN7` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.8 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 31; `ORC-3CJIFHYOXB` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.62 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 32; `ORC-FGUU4LFVAP` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.504 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 11, p. 16, row 29; `ORC-GWWB7P3GW5` |  |
| Bixbyite (Mn2O3) | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.254 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Mah 1960_ | Table 11, p. 16, row 28; `ORC-L423E62UHS` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -206.35 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Roth 1929_ [doi](https://doi.org/10.1002/ange.19290424102) | Table 11, p. 16, row 15; `ORC-5XFZM5QTXJ` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -201.266 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 16; `ORC-SCL3HUZ64I` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -201.206 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 17; `ORC-PU4GVT75GB` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.397 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 21; `ORC-RO25SZGUBN` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.364 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Shomate 1943_ [doi](https://doi.org/10.1021/ja01245a016) | Table 11, p. 16, row 18; `ORC-IPRFS25TUD` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.216 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Robie 1968_ | Table 11, p. 16, row 20; `ORC-JAYG4SP7LI` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.2 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 23; `ORC-VQPXQR5AQX` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.156 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Mah 1960_ | Table 11, p. 16, row 19; `ORC-GWEIPCQBVT` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.014 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 22; `ORC-EFXJVKAD2G` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -197.534 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003 | Table 11, p. 16, row 24; `ORC-JYMEPN5NSB` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -196.78 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Ruff 1913_ [doi](https://doi.org/10.1002/cber.19130460159) | Table 11, p. 16, row 14; `ORC-ED4AB7EXCW` |  |
| Hausmannite (Mn3O4) | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -196.181 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Le 1896_ | Table 11, p. 16, row 13; `ORC-VH7ZWPJY45` |  |
| Manganosite (Mn1−xO) |  | -411.14 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Guntz 1896_ | Table 11, p. 16, row 2; `ORC-WAQJPXVCJK` |  |
| Manganosite (Mn1−xO) |  | -404.03 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Roth 1929_ [doi](https://doi.org/10.1002/ange.19290424102) | Table 11, p. 16, row 3; `ORC-U5XKINV654` |  |
| Manganosite (Mn1−xO) |  | -389.79 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 4; `ORC-AKC4QCPOHQ` |  |
| Manganosite (Mn1−xO) |  | -389.37 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 5; `ORC-SZJGE5PSTY` |  |
| Manganosite (Mn1−xO) |  | -386.74 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003 | Table 11, p. 16, row 12; `ORC-TSYW5S3ADL` |  |
| Manganosite (Mn1−xO) |  | -385.48 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 9; `ORC-EKHWVLVWVH` |  |
| Manganosite (Mn1−xO) |  | -385.39 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Robie 1968_ | Table 11, p. 16, row 8; `ORC-FC4FMBT2O7` |  |
| Manganosite (Mn1−xO) |  | -385.35 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Southard 1942_ [doi](https://doi.org/10.1021/ja01260a007) | Table 11, p. 16, row 6; `ORC-6R5MG6VPFR` |  |
| Manganosite (Mn1−xO) |  | -385.19 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Rossini 1952_ | Table 11, p. 16, row 7; `ORC-ATRKGWLBIE` |  |
| Manganosite (Mn1−xO) |  | -384.9 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 11; `ORC-M3ULRKNQ64` |  |
| Manganosite (Mn1−xO) |  | -382.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 10; `ORC-LKV4XNSC36` |  |
| Manganosite (Mn1−xO) |  | -380.58 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Le 1896_ | Table 11, p. 16, row 1; `ORC-2J7DUS6LE5` |  |
| Mn1-xO |  | -411.14 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Guntz 1896_ | Table 11, p. 16, row 47; `ORC-H4EFLCYION` |  |
| Mn1-xO |  | -404.03 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Roth 1929_ [doi](https://doi.org/10.1002/ange.19290424102) | Table 11, p. 16, row 48; `ORC-M2T3RSMBVF` |  |
| Mn1-xO |  | -389.79 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 49; `ORC-6F33HL5YRA` |  |
| Mn1-xO |  | -389.37 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 50; `ORC-WPD42KSW4N` |  |
| Mn1-xO |  | -386.74 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003 | Table 11, p. 16, row 57; `ORC-ANU4FCX2YK` |  |
| Mn1-xO |  | -385.48 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 54; `ORC-NU2SDWSBWH` |  |
| Mn1-xO |  | -385.39 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Robie 1968_ | Table 11, p. 16, row 53; `ORC-SE3UPZXEZP` |  |
| Mn1-xO |  | -385.35 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Southard 1942_ [doi](https://doi.org/10.1021/ja01260a007) | Table 11, p. 16, row 51; `ORC-74SSZTGNH6` |  |
| Mn1-xO |  | -385.19 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Rossini 1952_ | Table 11, p. 16, row 52; `ORC-FNRDXBWRPX` |  |
| Mn1-xO |  | -384.9 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 56; `ORC-BFKLZDMVAI` |  |
| Mn1-xO |  | -382.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 55; `ORC-FUCKRQN4I6` |  |
| Mn1-xO |  | -380.58 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Grundy 2003; _cites Le 1896_ | Table 11, p. 16, row 46; `ORC-DEVWLYMVWM` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -194.854 kJ/mol-atom | 298.15 | experimental | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 70; `ORC-QU32DJ43IU` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -194.77 kJ/mol-atom | 298.15 | experimental | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 71; `ORC-TRAHZTSFDI` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -192.518 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003 | Table 11, p. 16, row 78; `ORC-FSQZRGEMZ2` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.922 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 75; `ORC-AZI5RBTUF2` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.922 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Brewer 1953_ [doi](https://doi.org/10.1021/cr60161a001) | Table 11, p. 16, row 72; `ORC-K2UML42INX` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.8 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 76; `ORC-LWCVT3URBT` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.62 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 77; `ORC-VJEZAA45MU` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.504 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 11, p. 16, row 74; `ORC-DVCLIEWPM4` |  |
| Mn2O3 | [Mn2O3](https://data.orchid-project.org/compounds/Mn2O3.html) | -191.254 kJ/mol-atom | 298.15 | model | -194.313 (mp-aaacotap) | -195.424 (oqmd-33708) | [1] Grundy 2003; _cites Mah 1960_ | Table 11, p. 16, row 73; `ORC-GRJAEOBYLQ` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -206.35 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Roth 1929_ [doi](https://doi.org/10.1002/ange.19290424102) | Table 11, p. 16, row 60; `ORC-FODYDWIRAG` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -201.266 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 61; `ORC-VVCEA7QBGW` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -201.206 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 62; `ORC-Y3OF7NGIA4` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.397 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 66; `ORC-T535JAFTM4` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.364 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Shomate 1943_ [doi](https://doi.org/10.1021/ja01245a016) | Table 11, p. 16, row 63; `ORC-ZEYWTZTVRV` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.216 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Robie 1968_ | Table 11, p. 16, row 65; `ORC-YXNU7TWNL6` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.2 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 68; `ORC-HORKDQ3MSC` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.156 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Mah 1960_ | Table 11, p. 16, row 64; `ORC-ZND33RTFIX` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -198.014 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 67; `ORC-Q5OLE6YC6B` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -197.534 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003 | Table 11, p. 16, row 69; `ORC-IAZM4Q7YXJ` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -196.78 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Ruff 1913_ [doi](https://doi.org/10.1002/cber.19130460159) | Table 11, p. 16, row 59; `ORC-6YP2G43BAO` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | -196.181 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [1] Grundy 2003; _cites Le 1896_ | Table 11, p. 16, row 58; `ORC-KWTNDMGT4W` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 196.181 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Le 1896_ | Table 1, p. 5, row 1; `ORC-P3442DZZI6` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 196.78 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Ruff 1913_ [doi](https://doi.org/10.1002/cber.19130460159) | Table 1, p. 5, row 2; `ORC-OF7YZ4OCHX` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 197.534 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Grundy 2003_ | Table 1, p. 5, row 12; `ORC-JOYPE76SKL` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 197.914 kJ/mol-atom | 298.15 | model | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010 | Table 1, p. 5, row 13; `ORC-OOK4XMA4V5` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 198.014 kJ/mol-atom | 298.15 | unspecified | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Knacke 2010_ | Table 1, p. 5, row 10; `ORC-SJQNK6QQKR` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 198.156 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Mah 1960_ | Table 1, p. 5, row 7; `ORC-QOMRTGICZ5` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 198.2 kJ/mol-atom | 298.15 | unspecified | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Kubaschewski 1993_ | Table 1, p. 5, row 11; `ORC-S2J5QCW5R6` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 198.216 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Robie 1968_ | Table 1, p. 5, row 8; `ORC-QZ2I3A6NYV` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 198.364 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Shomate 1943_ [doi](https://doi.org/10.1021/ja01245a016) | Table 1, p. 5, row 6; `ORC-NRMMC4OTJO` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 198.397 kJ/mol-atom | 298.15 | unspecified | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Pankratz 1982_ | Table 1, p. 5, row 9; `ORC-3BTH25KMV7` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 201.206 kJ/mol-atom | 298.15 | unspecified | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Ulich 1940_ | Table 1, p. 5, row 5; `ORC-IRJXYJDNH7` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 201.266 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Siemonsen 1939_ | Table 1, p. 5, row 4; `ORC-ZPFJ3SIJDS` |  |
| Mn3O4 | [Mn3O4](https://data.orchid-project.org/compounds/Mn3O4.html) | 206.35 kJ/mol-atom | 298.15 | experimental | -197.834 (mp-aaaabbtn) | -200.053 (oqmd-5975) | [2] Kjellqvist 2010; _cites Roth 1929_ [doi](https://doi.org/10.1002/ange.19290424102) | Table 1, p. 5, row 3; `ORC-O4LF5UQABA` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -175.007 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 82; `ORC-6G3UCCQEJ7` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -175.007 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 81; `ORC-S4PUE2YZBX` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -174.73 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Le 1896_ | Table 11, p. 16, row 79; `ORC-UT4IICGN6R` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -174 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 88; `ORC-YKGBS4VI2S` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.947 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Shomate 1943_ [doi](https://doi.org/10.1021/ja01245a016) | Table 11, p. 16, row 83; `ORC-77MUO2SSTH` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.753 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Rossini 1952_ | Table 11, p. 16, row 84; `ORC-RPJZ575UDS` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.633 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 89; `ORC-RYSDFCFCR2` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.613 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Mah 1960_ | Table 11, p. 16, row 86; `ORC-6WRQHNF6DI` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.493 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003 | Table 11, p. 16, row 90; `ORC-3WAEFRWWHR` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.46 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 87; `ORC-JNC22JLYEC` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.333 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Brewer 1953_ [doi](https://doi.org/10.1021/cr60161a001) | Table 11, p. 16, row 85; `ORC-SAKGZUE6OT` |  |
| MnO2 | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -166.913 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Mixter 1910_ [doi](https://doi.org/10.2475/ajs.s4-30.177.193) | Table 11, p. 16, row 80; `ORC-JNWIJCB6DJ` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -175.007 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Siemonsen 1939_ | Table 11, p. 16, row 36; `ORC-6MEP3VUEHP` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -175.007 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Ulich 1940_ [doi](https://doi.org/10.1002/srin.194001311) | Table 11, p. 16, row 37; `ORC-VK3JCM3HZI` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -174.73 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Le 1896_ | Table 11, p. 16, row 34; `ORC-LV2XM5E2UV` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -174 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Knacke 1991_ | Table 11, p. 16, row 43; `ORC-6X7VMCRTJJ` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.947 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Shomate 1943_ [doi](https://doi.org/10.1021/ja01245a016) | Table 11, p. 16, row 38; `ORC-X6UOHCZYKT` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.753 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Rossini 1952_ | Table 11, p. 16, row 39; `ORC-E3OVE2BMWZ` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.633 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 11, p. 16, row 44; `ORC-OMTU4J5NWQ` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.613 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Mah 1960_ | Table 11, p. 16, row 41; `ORC-7KXME5J3A6` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.493 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003 | Table 11, p. 16, row 45; `ORC-7XK3NJVYAK` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.46 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Pankratz 1982_ | Table 11, p. 16, row 42; `ORC-CQWVFKMNOT` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -173.333 kJ/mol-atom | 298.15 | model | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Brewer 1953_ [doi](https://doi.org/10.1021/cr60161a001) | Table 11, p. 16, row 40; `ORC-QIQPGIMLAL` |  |
| Pyrolusite (MnO2) | [MnO2](https://data.orchid-project.org/compounds/MnO2.html) | -166.913 kJ/mol-atom | 298.15 | experimental | -174.236 (mp-aaaabcrz) | -168.93 (oqmd-677684) | [1] Grundy 2003; _cites Mixter 1910_ [doi](https://doi.org/10.2475/ajs.s4-30.177.193) | Table 11, p. 16, row 35; `ORC-2IE4CVLKVW` |  |

## Other properties

### Phase transition (13)

Table: Phase transition, Mn–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 300 K | 300 | a-Mn2O3 -> b-Mn2O3 | experimental | [2] Kjellqvist 2010 | p. 5; `ORC-RNTKOKGSI7` | “a-Bixbyite (a-Mn2O3) transforms to b-Mn2O3 (Strukturbericht D53) at around 300 K.” |
| Phase transition | 300 K | 300 | alpha-Mn2O3 + beta-Mn2O3 | experimental | [1] Grundy 2003; _cites Geller 1970_ [doi](https://doi.org/10.1103/physrevb.1.3763) | p. 3; `ORC-KSDQLOUI5J` | “Orthorhombic ␣-bixbyite (␣-Mn2O3) transforms to cubic ␤-bixbyite\[59\] at around 300 K.” |
| Phase transition | 1408 K | 1408 | alpha-Mn3O4 + beta-Mn3O4 | experimental | [1] Grundy 2003; _cites Driessens 1967_ [doi](https://doi.org/10.1016/s0020-1693%2800%2993169-4) | p. 3; `ORC-ZCN4Z6AIVZ.bd0d56` | “The measured temperatures at which this transformation takes place are between 1408 K,\[52\] 1430 K,\[54\] 1433 K,\[30\] and 1473 K \[51\] with a larger number of other measurements\[5,20,55-57\] grouped between 1443 and 1450 K (Table 2).” |
| Phase transition | 1430 K | 1430 | alpha-Mn3O4 + beta-Mn3O4 | experimental | [1] Grundy 2003; _cites Metselaar 1981_ [doi](https://doi.org/10.1016/0022-4596%2881%2990064-5) | p. 3; `ORC-ZCN4Z6AIVZ.216912` | “The measured temperatures at which this transformation takes place are between 1408 K,\[52\] 1430 K,\[54\] 1433 K,\[30\] and 1473 K \[51\] with a larger number of other measurements\[5,20,55-57\] grouped between 1443 and 1450 K (Table 2).” |
| Phase transition | 1433 K | 1433 | alpha-Mn3O4 + beta-Mn3O4 | experimental | [1] Grundy 2003; _cites Van 1958_ | p. 3; `ORC-ZCN4Z6AIVZ.4eb528` | “The measured temperatures at which this transformation takes place are between 1408 K,\[52\] 1430 K,\[54\] 1433 K,\[30\] and 1473 K \[51\] with a larger number of other measurements\[5,20,55-57\] grouped between 1443 and 1450 K (Table 2).” |
| Phase transition | 1473 K | 1473 | alpha-Mn3O4 + beta-Mn3O4 | experimental | [1] Grundy 2003; _cites Schmier 1966_ [doi](https://doi.org/10.1002/zaac.19663460310) | p. 3; `ORC-ZCN4Z6AIVZ.ec4663` | “The measured temperatures at which this transformation takes place are between 1408 K,\[52\] 1430 K,\[54\] 1433 K,\[30\] and 1473 K \[51\] with a larger number of other measurements\[5,20,55-57\] grouped between 1443 and 1450 K (Table 2).” |
| Phase transition | 1519 K | 1519 | delta-Mn + liquid | experimental | [1] Grundy 2003; _cites Fernandez 1990_ | p. 1; `ORC-7ZBCJ5JB63.57272f` | “Manganese exists in four modifications: ␣-Mn (up to 980 K), ␤-Mn (up to 1360 K), ␥-Mn (up to 1411 K), and ␦-Mn (up to the melting temperature of 1519 K).” |
| Phase transition | 1835 K | 1835 | beta-Mn3O4 + liquid | experimental | [1] Grundy 2003; _cites Van 1958_ | p. 1; `ORC-UCL5HMODEN.90637b` | “The temperature of melting in air has been determined a number of times\[20,27-30\] (Table 2) with measured temperatures ranging from 1835 K\[30\] to 1863 K.\[28\]” |
| Phase transition | 1858 K | 1858 | other | experimental | [1] Grundy 2003; _cites Andrew 1931_ | p. 1; `ORC-FYQG6H6VCM.8eda8f` | “The melting temperature of Mn1-xO has been determined a number of times (Table 2), either by measuring the melting point of pure MnO,\[18,20\] giving 2123 and 2115 K respectively, or by extrapolating the liquidus line of pseudobinary systems (MnO-FeO,\[15,21-24\] MnO-SiO2\[25\]) to pure MnO, giving temperatures ranging from 1858 K\[21\] to 2158 K.\[24\]” |
| Phase transition | 1863 K | 1863 | beta-Mn3O4 + liquid | experimental | [1] Grundy 2003; _cites Von 1937_ | p. 1; `ORC-UCL5HMODEN.b005ba` | “The temperature of melting in air has been determined a number of times\[20,27-30\] (Table 2) with measured temperatures ranging from 1835 K\[30\] to 1863 K.\[28\]” |
| Phase transition | 2115 K | 2115 | other | experimental | [1] Grundy 2003; _cites Tromel 1976_ | p. 1; `ORC-FYQG6H6VCM.4f92ea` | “The melting temperature of Mn1-xO has been determined a number of times (Table 2), either by measuring the melting point of pure MnO,\[18,20\] giving 2123 and 2115 K respectively, or by extrapolating the liquidus line of pseudobinary systems (MnO-FeO,\[15,21-24\] MnO-SiO2\[25\]) to pure MnO, giving temperatures ranging from 1858 K\[21\] to 2158 K.\[24\]” |
| Phase transition | 2123 K | 2123 | other | experimental | [1] Grundy 2003; _cites Schenck 1964_ [doi](https://doi.org/10.1002/srin.196402318) | p. 1; `ORC-FYQG6H6VCM.970c3b` | “The melting temperature of Mn1-xO has been determined a number of times (Table 2), either by measuring the melting point of pure MnO,\[18,20\] giving 2123 and 2115 K respectively, or by extrapolating the liquidus line of pseudobinary systems (MnO-FeO,\[15,21-24\] MnO-SiO2\[25\]) to pure MnO, giving temperatures ranging from 1858 K\[21\] to 2158 K.\[24\]” |
| Phase transition | 2158 K | 2158 | other | experimental | [1] Grundy 2003; _cites Schurmann 1984_ [doi](https://doi.org/10.1002/srin.198405356) | p. 1; `ORC-FYQG6H6VCM.a6a691` | “The melting temperature of Mn1-xO has been determined a number of times (Table 2), either by measuring the melting point of pure MnO,\[18,20\] giving 2123 and 2115 K respectively, or by extrapolating the liquidus line of pseudobinary systems (MnO-FeO,\[15,21-24\] MnO-SiO2\[25\]) to pure MnO, giving temperatures ranging from 1858 K\[21\] to 2158 K.\[24\]” |

### Mixing / partial (1)

Table: Mixing / partial, Mn–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of mixing; _printed: ΔSmelt_ | 10.4 J/mol (basis unstated)/K |  | MnO; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 3, p. 5, row 4; `ORC-BWL3BLDTVI` |  |

### Heat capacity / entropy / enthalpy (69)

Table: Heat capacity / entropy / enthalpy, Mn–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: °S298_ | 22.1 J/mol-atom/K | 298.15 | Bixbyite (Mn2O3); _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 20; `ORC-3GRVCMQMND` |  |
| Entropy; _printed: °S298_ | 22.42 J/mol-atom/K | 298.15 | Bixbyite (Mn2O3); _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 10, p. 15, row 22; `ORC-3HDXSOGTYT` |  |
| Entropy; _printed: °S298_ | 22.74 J/mol-atom/K | 298.15 | Bixbyite (Mn2O3); _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Robie 1985_ [doi](https://doi.org/10.1016/0021-9614%2885%2990069-2) | Table 10, p. 15, row 19; `ORC-G7U7JFOHLD` |  |
| Entropy; _printed: °S298_ | 22.106 J/mol-atom/K | 298.15 | Bixbyite (Mn2O3); _alloy: O 0.6_ | model | [1] Grundy 2003; _cites King 1954_ [doi](https://doi.org/10.1021/ja01641a063) | Table 10, p. 15, row 18; `ORC-PP2NFA3E5X` |  |
| Entropy; _printed: °S298_ | 22.106 J/mol-atom/K | 298.15 | Bixbyite (Mn2O3); _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 17; `ORC-PYPGC4RCCH` |  |
| Entropy; _printed: °S298_ | 22.106 J/mol-atom/K | 298.15 | Bixbyite (Mn2O3); _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 21; `ORC-RSRD2EBVOK` |  |
| Entropy; _printed: °S298_ | 22.25 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 9; `ORC-3Q3LCG52BR` |  |
| Entropy; _printed: °S298_ | 24.0486 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003 | Table 10, p. 15, row 16; `ORC-5V2BEV4KMD` |  |
| Entropy; _printed: °S298_ | 21.37 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Millar 1928_ | Table 10, p. 15, row 11; `ORC-7TYNBTU644` |  |
| Entropy; _printed: °S298_ | 22.1143 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 14; `ORC-FMFGEFAQDJ` |  |
| Entropy; _printed: °S298_ | 23.4429 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Robie 1985_ [doi](https://doi.org/10.1016/0021-9614%2885%2990069-2) | Table 10, p. 15, row 12; `ORC-FXUOBSZCBE` |  |
| Entropy; _printed: °S298_ | 22.01 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 15; `ORC-GMLBH3XJA6` |  |
| Entropy; _printed: °S298_ | 23.8 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites ONeill 1993_ [doi](https://doi.org/10.1007/bf01046534) | Table 10, p. 15, row 10; `ORC-HLATPR5ZLM` |  |
| Entropy; _printed: °S298_ | 23.8714 J/mol-atom/K | 298.15 | Hausmannite (Mn3O4); _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Chhor 1986_ [doi](https://doi.org/10.1016/0021-9614%2886%2990047-9) | Table 10, p. 15, row 13; `ORC-QQCUAVJ424` |  |
| Entropy; _printed: °S298_ | 53.17 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003; _cites Kelley 1943_ [doi](https://doi.org/10.1021/ja01245a015) | Table 10, p. 15, row 4; `ORC-2HXHT4UL4M` |  |
| Entropy; _printed: °S298_ | 59.8 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 5; `ORC-6DEP4MWNVT` |  |
| Entropy; _printed: °S298_ | 59.75 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003; _cites Todd 1951_ [doi](https://doi.org/10.1021/ja01152a099) | Table 10, p. 15, row 7; `ORC-CQUK5Y6ZG7` |  |
| Entropy; _printed: °S298_ | 59.02 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003 | Table 10, p. 15, row 8; `ORC-D5HRASPPTR` |  |
| Entropy; _printed: °S298_ | 59.02 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003; _cites Shapiro 1999_ [doi](https://doi.org/10.1006/jcht.1998.0479) | Table 10, p. 15, row 1; `ORC-UA3REZOUZX` |  |
| Entropy; _printed: °S298_ | 62.47 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003; _cites Millar 1928_ | Table 10, p. 15, row 3; `ORC-UGH5B57PSC` |  |
| Entropy; _printed: °S298_ | 59.75 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 2; `ORC-V4DQRBYKEZ` |  |
| Entropy; _printed: °S298_ | 59.87 J/mol (basis unstated)/K | 298.15 | Manganosite (Mn1−xO) | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 6; `ORC-WHSPFWF3NX` |  |
| Entropy; _printed: °S298_ | 59.75 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 32; `ORC-54L7DWPLNB` |  |
| Entropy; _printed: °S298_ | 59.87 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 36; `ORC-56CTOQFEEO` |  |
| Entropy; _printed: °S298_ | 53.17 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003; _cites Kelley 1943_ [doi](https://doi.org/10.1021/ja01245a015) | Table 10, p. 15, row 34; `ORC-DXRWUNAKEN` |  |
| Entropy; _printed: °S298_ | 59.75 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003; _cites Todd 1951_ [doi](https://doi.org/10.1021/ja01152a099) | Table 10, p. 15, row 37; `ORC-EKU3VJ3NLA` |  |
| Entropy; _printed: °S298_ | 62.47 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003; _cites Millar 1928_ | Table 10, p. 15, row 33; `ORC-JO6K2VVJJI` |  |
| Entropy; _printed: °S298_ | 59.02 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003; _cites Shapiro 1999_ [doi](https://doi.org/10.1006/jcht.1998.0479) | Table 10, p. 15, row 31; `ORC-QSVYWHCMXS` |  |
| Entropy; _printed: °S298_ | 59.8 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 35; `ORC-VCGCDMGIRZ` |  |
| Entropy; _printed: °S298_ | 59.02 J/mol (basis unstated)/K | 298.15 | Mn1-xO | model | [1] Grundy 2003 | Table 10, p. 15, row 38; `ORC-ZLO4EGDRJS` |  |
| Entropy; _printed: °S298_ | 22.106 J/mol-atom/K | 298.15 | Mn2O3; _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 51; `ORC-CDMRI5LRBD` |  |
| Entropy; _printed: °S298_ | 22.106 J/mol-atom/K | 298.15 | Mn2O3; _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 47; `ORC-GY5SFCOBM5` |  |
| Entropy; _printed: °S298_ | 22.106 J/mol-atom/K | 298.15 | Mn2O3; _alloy: O 0.6_ | model | [1] Grundy 2003; _cites King 1954_ [doi](https://doi.org/10.1021/ja01641a063) | Table 10, p. 15, row 48; `ORC-HQLPJZHQ3S` |  |
| Entropy; _printed: °S298_ | 22.74 J/mol-atom/K | 298.15 | Mn2O3; _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Robie 1985_ [doi](https://doi.org/10.1016/0021-9614%2885%2990069-2) | Table 10, p. 15, row 49; `ORC-IKOF4DUXD5` |  |
| Entropy; _printed: °S298_ | 22.1 J/mol-atom/K | 298.15 | Mn2O3; _alloy: O 0.6_ | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 50; `ORC-WAGRU7YP6H` |  |
| Entropy; _printed: °S298_ | 22.42 J/mol-atom/K | 298.15 | Mn2O3; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 10, p. 15, row 52; `ORC-WX4UUAND7C` |  |
| Entropy; _printed: °S298_ | 22.1143 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 44; `ORC-5PYJFWGPSE` |  |
| Entropy; _printed: °S298_ | 21.37 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | experimental | [2] Kjellqvist 2010; _cites Millar 1928_ | Table 1, p. 5, row 16; `ORC-7LBOS3ZMGS` |  |
| Entropy; _printed: °S298_ | 23.6729 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [2] Kjellqvist 2010 | Table 1, p. 5, row 22; `ORC-BRW76CTYCW` |  |
| Entropy; _printed: °S298_ | 23.8714 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | experimental | [2] Kjellqvist 2010; _cites Chhor 1986_ [doi](https://doi.org/10.1016/0021-9614%2886%2990047-9) | Table 1, p. 5, row 18; `ORC-C672B4OYB3` |  |
| Entropy; _printed: °S298_ | 22.25 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 39; `ORC-CEYWPMLC6P` |  |
| Entropy; _printed: °S298_ | 23.4429 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | experimental | [2] Kjellqvist 2010; _cites Robie 1985_ [doi](https://doi.org/10.1016/0021-9614%2885%2990069-2) | Table 1, p. 5, row 17; `ORC-DIT7OPGPC6` |  |
| Entropy; _printed: °S298_ | 22.01 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 45; `ORC-DM7E3HDNGP` |  |
| Entropy; _printed: °S298_ | 23.8 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites ONeill 1993_ [doi](https://doi.org/10.1007/bf01046534) | Table 10, p. 15, row 40; `ORC-FFOSIAETFS` |  |
| Entropy; _printed: °S298_ | 23.8714 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Chhor 1986_ [doi](https://doi.org/10.1016/0021-9614%2886%2990047-9) | Table 10, p. 15, row 43; `ORC-GKINJ5SLJY` |  |
| Entropy; _printed: °S298_ | 23.4429 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Robie 1985_ [doi](https://doi.org/10.1016/0021-9614%2885%2990069-2) | Table 10, p. 15, row 42; `ORC-J47JSGX2M5` |  |
| Entropy; _printed: °S298_ | 22.01 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | experimental | [2] Kjellqvist 2010; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 1, p. 5, row 20; `ORC-NEDTVO5RID` |  |
| Entropy; _printed: °S298_ | 21.37 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003; _cites Millar 1928_ | Table 10, p. 15, row 41; `ORC-PZTGROHNZU` |  |
| Entropy; _printed: °S298_ | 22.25 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | unspecified | [2] Kjellqvist 2010; _cites Pankratz 1982_ | Table 1, p. 5, row 14; `ORC-SQDZI3DMCG` |  |
| Entropy; _printed: °S298_ | 24.0486 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [2] Kjellqvist 2010; _cites Grundy 2003_ | Table 1, p. 5, row 21; `ORC-UPYDEKH2IK` |  |
| Entropy; _printed: °S298_ | 22.1143 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | unspecified | [2] Kjellqvist 2010; _cites Kubaschewski 1993_ | Table 1, p. 5, row 19; `ORC-XBHRV2JLSL` |  |
| Entropy; _printed: °S298_ | 23.8 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [2] Kjellqvist 2010; _cites ONeill 1993_ [doi](https://doi.org/10.1007/bf01046533) | Table 1, p. 5, row 15; `ORC-YAR6VE2A2F` |  |
| Entropy; _printed: °S298_ | 24.0486 J/mol-atom/K | 298.15 | Mn3O4; _alloy: O 0.571429_ | model | [1] Grundy 2003 | Table 10, p. 15, row 46; `ORC-YZ52JW2TFN` |  |
| Entropy; _printed: °S298_ | 17.5833 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Robie 1985_ [doi](https://doi.org/10.1016/0021-9614%2885%2990069-2) | Table 10, p. 15, row 56; `ORC-BQSQWYOT66` |  |
| Entropy; _printed: °S298_ | 17.6967 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 59; `ORC-CJ6BBSLPMF` |  |
| Entropy; _printed: °S298_ | 18.0867 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Moore 1943_ [doi](https://doi.org/10.1021/ja01245a015) | Table 10, p. 15, row 54; `ORC-HUWQPWDLLC` |  |
| Entropy; _printed: °S298_ | 17.9833 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003 | Table 10, p. 15, row 60; `ORC-HYIQOMGMWN` |  |
| Entropy; _printed: °S298_ | 19.44 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Millar 1928_ | Table 10, p. 15, row 55; `ORC-PFKGFZSO7F` |  |
| Entropy; _printed: °S298_ | 17.7233 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Kelley 1943_ [doi](https://doi.org/10.1021/ja01245a015) | Table 10, p. 15, row 58; `ORC-SK3JRX6PZV` |  |
| Entropy; _printed: °S298_ | 17.6967 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 53; `ORC-UXJMRJLSCM` |  |
| Entropy; _printed: °S298_ | 17.7 J/mol-atom/K | 298.15 | MnO2; _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 57; `ORC-YHG5OFEIVJ` |  |
| Entropy; _printed: °S298_ | 19.44 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Millar 1928_ | Table 10, p. 15, row 25; `ORC-4NKQPCL3FW` |  |
| Entropy; _printed: °S298_ | 17.7 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Kubaschewski 1993_ | Table 10, p. 15, row 27; `ORC-5U7QW4PSJM` |  |
| Entropy; _printed: °S298_ | 17.6967 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Zordan 1968_ [doi](https://doi.org/10.1021/cr60256a003) | Table 10, p. 15, row 29; `ORC-DKVX2QJLYX` |  |
| Entropy; _printed: °S298_ | 17.7233 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Kelley 1943_ [doi](https://doi.org/10.1021/ja01245a015) | Table 10, p. 15, row 28; `ORC-EMX7EPEWWM` |  |
| Entropy; _printed: °S298_ | 17.5833 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Robie 1985_ [doi](https://doi.org/10.1016/0021-9614%2885%2990069-2) | Table 10, p. 15, row 26; `ORC-JK3M2X6JX4` |  |
| Entropy; _printed: °S298_ | 18.0867 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Moore 1943_ [doi](https://doi.org/10.1021/ja01245a015) | Table 10, p. 15, row 24; `ORC-OQ5OBL6UOL` |  |
| Entropy; _printed: °S298_ | 17.6967 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003; _cites Pankratz 1982_ | Table 10, p. 15, row 23; `ORC-VTVUTKHFNL` |  |
| Entropy; _printed: °S298_ | 17.9833 J/mol-atom/K | 298.15 | Pyrolusite (MnO2); _alloy: O 0.666667_ | model | [1] Grundy 2003 | Table 10, p. 15, row 30; `ORC-ZLVUUANV7N` |  |

### Model expression (113)

Table: Model expression, Mn–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 92.63 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Charette 1968_ [doi](https://doi.org/10.1149/1.2411434) | Table 8, p. 11, row 28; `ORC-44L3GERLK4.5f85f3` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -114139 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Charette 1968_ [doi](https://doi.org/10.1149/1.2411434) | Table 8, p. 11, row 28; `ORC-44L3GERLK4.d848fa` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 96.73 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Schmahl 1963_ [doi](https://doi.org/10.1002/srin.196304016) | Table 8, p. 11, row 27; `ORC-4B2KQOYR5C.89ed62` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -1119770 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Schmahl 1963_ [doi](https://doi.org/10.1002/srin.196304016) | Table 8, p. 11, row 27; `ORC-4B2KQOYR5C.a25160` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 120.8 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 30; `ORC-6M5KNRSGU6.1c2183` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -155690 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 30; `ORC-6M5KNRSGU6.7084b5` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -104252 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Vlasov 1958_ | Table 8, p. 11, row 19; `ORC-7LXVMSZREZ.82d5a7` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 80.73 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Vlasov 1958_ | Table 8, p. 11, row 19; `ORC-7LXVMSZREZ.e1c8b5` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 69.25 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Klingsberg 1960_ | Table 8, p. 11, row 26; `ORC-BZ3NIMNNZX.36d139` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -64756 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Klingsberg 1960_ | Table 8, p. 11, row 26; `ORC-BZ3NIMNNZX.8167f9` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 84.74 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Ingraham 1966_ [doi](https://doi.org/10.1179/cmq.1966.5.2.109) | Table 8, p. 11, row 23; `ORC-CBENG57NZT.56b83c` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -105600 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Ingraham 1966_ [doi](https://doi.org/10.1179/cmq.1966.5.2.109) | Table 8, p. 11, row 23; `ORC-CBENG57NZT.c0b223` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -90311 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Huebner 1970_ | Table 8, p. 11, row 17; `ORC-DY76QOD4SQ.0cb30d` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 72.11 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Huebner 1970_ | Table 8, p. 11, row 17; `ORC-DY76QOD4SQ.d2518b` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 52.53 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Meyer 1908_ [doi](https://doi.org/10.1002/zaac.19080570105) | Table 8, p. 11, row 20; `ORC-HAZ44M7NHT.8dddb9` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -71513 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Meyer 1908_ [doi](https://doi.org/10.1002/zaac.19080570105) | Table 8, p. 11, row 20; `ORC-HAZ44M7NHT.a00158` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 68.97 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Otto 2003_ | Table 8, p. 11, row 25; `ORC-JLKDQJUE46.cf051d` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -86401 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Otto 2003_ | Table 8, p. 11, row 25; `ORC-JLKDQJUE46.d30db2` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 289 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 29; `ORC-KAQEGYA53D.a65d6b` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -140000 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 29; `ORC-KAQEGYA53D.abfb55` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T ln(T)_ | -24.8 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 29; `ORC-KAQEGYA53D.f9bb5f` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -87423 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Hahn 1960_ [doi](https://doi.org/10.2475/ajs.258.1.66) | Table 8, p. 11, row 18; `ORC-LQW6EW2POI.de4f61` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 70.54 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Hahn 1960_ [doi](https://doi.org/10.2475/ajs.258.1.66) | Table 8, p. 11, row 18; `ORC-LQW6EW2POI.f4ec4b` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -97719 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Shenouda 1967_ [doi](https://doi.org/10.1002/jctb.5010170905) | Table 8, p. 11, row 22; `ORC-NLWOAPWKAX.88a1b1` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 78.88 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Shenouda 1967_ [doi](https://doi.org/10.1002/jctb.5010170905) | Table 8, p. 11, row 22; `ORC-NLWOAPWKAX.dc2da2` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 71.54 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Kim 1966_ | Table 8, p. 11, row 21; `ORC-WL5OKOWISK.0877e5` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -95305 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Kim 1966_ | Table 8, p. 11, row 21; `ORC-WL5OKOWISK.c5d4af` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 84.47 J/mol/K |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Hochgeschwender 1967_ [doi](https://doi.org/10.1179/cmq.1967.6.1.71) | Table 8, p. 11, row 24; `ORC-ZTREHNK4J4.ebe9c1` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -105768 J/mol |  | Mn2O3 + α-Mn3O4; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Hochgeschwender 1967_ [doi](https://doi.org/10.1179/cmq.1967.6.1.71) | Table 8, p. 11, row 24; `ORC-ZTREHNK4J4.f6ae07` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -124740 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Meyer 1908_ [doi](https://doi.org/10.1002/zaac.19080570105) | Table 9, p. 11, row 15; `ORC-3K74EHFATY.848408` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 148.91 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Meyer 1908_ [doi](https://doi.org/10.1002/zaac.19080570105) | Table 9, p. 11, row 15; `ORC-3K74EHFATY.bcb8de` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 106.63 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Otto 1965_ [doi](https://doi.org/10.1149/1.2423551) | Table 9, p. 11, row 11; `ORC-5KXQ5JSDNE.c34830` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -77583 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Otto 1965_ [doi](https://doi.org/10.1149/1.2423551) | Table 9, p. 11, row 11; `ORC-5KXQ5JSDNE.f733e8` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 112.51 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Hochgeschwender 1967_ [doi](https://doi.org/10.1179/cmq.1967.6.1.71) | Table 9, p. 11, row 14; `ORC-DHSFDCME3A.08a39c` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -91933 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Hochgeschwender 1967_ [doi](https://doi.org/10.1179/cmq.1967.6.1.71) | Table 9, p. 11, row 14; `ORC-DHSFDCME3A.a11128` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -66236 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Vlasov 1958_ | Table 9, p. 11, row 10; `ORC-K3YDDP3OV7.1114ae` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 82.61 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Vlasov 1958_ | Table 9, p. 11, row 10; `ORC-K3YDDP3OV7.79b88f` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -224.87 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Klingsberg 1960_ | Table 9, p. 11, row 16; `ORC-MBI3TOJ3FR.ef582f` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 46.76 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Klingsberg 1960_ | Table 9, p. 11, row 16; `ORC-MBI3TOJ3FR.fe3876` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -76338 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 9, p. 11, row 18; `ORC-PPFGZJ2VDI.6d14f4` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 103.63 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 9, p. 11, row 18; `ORC-PPFGZJ2VDI.6f4bf1` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -49862 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Askenasy 1910_ | Table 9, p. 11, row 13; `ORC-RTOVQV4VOD.9f1adc` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 62.24 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Askenasy 1910_ | Table 9, p. 11, row 13; `ORC-RTOVQV4VOD.ae7430` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -45055 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Kim 1966_ | Table 9, p. 11, row 12; `ORC-WWULX6IWSS.3b31ab` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 49.56 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | experimental | [1] Grundy 2003; _cites Kim 1966_ | Table 9, p. 11, row 12; `ORC-WWULX6IWSS.64ba55` |  |
| gibbs energy expression term; _printed: Δ°G(T) T ln(T) coefficient_ | 2.11 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 9, p. 11, row 17; `ORC-ZKRPD3Z3OX.2c30e5` |  |
| gibbs energy expression term; _printed: Δ°G(T) T coefficient_ | 94.4 J/mol/K |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 9, p. 11, row 17; `ORC-ZKRPD3Z3OX.737df3` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant_ | -80000 J/mol |  | Mn2O3 + α-MnO2; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 9, p. 11, row 17; `ORC-ZKRPD3Z3OX.93a04c` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 306 J/mol/K |  | Mn2O3 + β-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 31; `ORC-54XEVCH7PY.7652e5` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -174000 J/mol |  | Mn2O3 + β-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 31; `ORC-54XEVCH7PY.ee1e2b` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T ln(T)_ | -23.8 J/mol/K |  | Mn2O3 + β-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 31; `ORC-54XEVCH7PY.f02649` |  |
| gibbs energy expression term; _printed: Δ°G(T) coefficient of T_ | 77.823 J/mol/K |  | Mn2O3 + β-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 32; `ORC-V3ATLV32BF.66f4a0` |  |
| gibbs energy expression term; _printed: Δ°G(T) constant A_ | -94568 J/mol |  | Mn2O3 + β-Mn3O4; _alloy: O 0.6_ | model | [1] Grundy 2003 | Table 8, p. 11, row 32; `ORC-V3ATLV32BF.6b32d8` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 110.05 J/(mol K) |  | MnO + α-, β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Fender 1970_ | Table 7, p. 11, row 13; `ORC-C4L3OUD42H.6f4361` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -221609 J/mol |  | MnO + α-, β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Fender 1970_ | Table 7, p. 11, row 13; `ORC-C4L3OUD42H.712072` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -240533 J/mol |  | MnO + α-, β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Tromel 1976_ | Table 7, p. 11, row 10; `ORC-MNXOM3UEAT.66b123` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 123.59 J/(mol K) |  | MnO + α-, β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Tromel 1976_ | Table 7, p. 11, row 10; `ORC-MNXOM3UEAT.f07ee0` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -245694 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Huebner 1970_ | Table 7, p. 11, row 4; `ORC-B73MPFHYZ2.8527d7` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 129.68 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Huebner 1970_ | Table 7, p. 11, row 4; `ORC-B73MPFHYZ2.c819c6` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | -151.43 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Kim 1966_ | Table 7, p. 11, row 1; `ORC-BLOMIONMEF.706d5a` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -241735 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Kim 1966_ | Table 7, p. 11, row 1; `ORC-BLOMIONMEF.f22de5` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 111.4 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites ONeill 1993_ [doi](https://doi.org/10.1007/bf01046534) | Table 7, p. 11, row 8; `ORC-DPZSD2SRWS.1740ba` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -222827 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites ONeill 1993_ [doi](https://doi.org/10.1007/bf01046534) | Table 7, p. 11, row 8; `ORC-DPZSD2SRWS.b6ca27` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 109.94 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Schwerdtfeger 1967_ | Table 7, p. 11, row 6; `ORC-DZ32GFD2ZT.cdc25f` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -222259 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Schwerdtfeger 1967_ | Table 7, p. 11, row 6; `ORC-DZ32GFD2ZT.d090a5` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -245604 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Chou 1978_ | Table 7, p. 11, row 9; `ORC-F74X5D5IBA.182493` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 130.48 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Chou 1978_ | Table 7, p. 11, row 9; `ORC-F74X5D5IBA.ac88f5` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -224450 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Charette 1968_ [doi](https://doi.org/10.1149/1.2411434) | Table 7, p. 11, row 12; `ORC-I3UEBOFFTX.29a345` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T (printed without T)\]_ | 112.35 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Charette 1968_ [doi](https://doi.org/10.1149/1.2411434) | Table 7, p. 11, row 12; `ORC-I3UEBOFFTX.d91859` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -223681 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Charette 1968_ [doi](https://doi.org/10.1149/1.2411434) | Table 7, p. 11, row 11; `ORC-MME75SM54M.57d47c` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 111.9 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Charette 1968_ [doi](https://doi.org/10.1149/1.2411434) | Table 7, p. 11, row 11; `ORC-MME75SM54M.b29d21` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 107.36 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Schwerdtfeger 1967_ | Table 7, p. 11, row 7; `ORC-SUCCIGYD55.d9caf4` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -219419 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Schwerdtfeger 1967_ | Table 7, p. 11, row 7; `ORC-SUCCIGYD55.ddab0f` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T ln(T)\]_ | 7.82 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 14; `ORC-YMGIXAOF7S.1fc858` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -214000 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 14; `ORC-YMGIXAOF7S.236768` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 48.8 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 14; `ORC-YMGIXAOF7S.b25c5d` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -222470 J/mol |  | MnO + α-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 15; `ORC-ZOU24W44Z6.9d4397` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 111.1 J/(mol K) |  | MnO + α-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 15; `ORC-ZOU24W44Z6.a63f76` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 117.2 J/(mol K) |  | MnO + β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Schmahl 1969_ [doi](https://doi.org/10.1002/srin.196904332) | Table 7, p. 11, row 2; `ORC-2AF6PDLOGU.5c2838` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -229774 J/mol |  | MnO + β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Schmahl 1969_ [doi](https://doi.org/10.1002/srin.196904332) | Table 7, p. 11, row 2; `ORC-2AF6PDLOGU.9ceae1` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 137.82 J/(mol K) |  | MnO + β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Hahn 1960_ [doi](https://doi.org/10.2475/ajs.258.1.66) | Table 7, p. 11, row 3; `ORC-C2LDI3IY4A.50aa48` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -266649 J/mol |  | MnO + β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Hahn 1960_ [doi](https://doi.org/10.2475/ajs.258.1.66) | Table 7, p. 11, row 3; `ORC-C2LDI3IY4A.804abf` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 117.77 J/(mol K) |  | MnO + β-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 17; `ORC-G3PO6IBOHC.8af9fa` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -231960 J/mol |  | MnO + β-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 17; `ORC-G3PO6IBOHC.dec537` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | 73.66 J/(mol K) |  | MnO + β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Hed 1967_ [doi](https://doi.org/10.1149/1.2426584) | Table 7, p. 11, row 5; `ORC-YE7MVSQJ63.44f42c` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -159463 J/mol |  | MnO + β-Mn3O4; _alloy: O 0.5_ | experimental | [1] Grundy 2003; _cites Hed 1967_ [doi](https://doi.org/10.1149/1.2426584) | Table 7, p. 11, row 5; `ORC-YE7MVSQJ63.dcc2ac` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T ln(T)\]_ | 110.2 J/(mol K) |  | MnO + β-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 16; `ORC-ZB3R6QBCIZ.13b3b2` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[a\]_ | -54008 J/mol |  | MnO + β-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 16; `ORC-ZB3R6QBCIZ.18080d` |  |
| gibbs energy expression term; _printed: Δ°G(T) \[T\]_ | -807.1 J/(mol K) |  | MnO + β-Mn3O4; _alloy: O 0.5_ | model | [1] Grundy 2003 | Table 7, p. 11, row 16; `ORC-ZB3R6QBCIZ.73d406` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 72.33 J/mol/K |  | α-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 14; `ORC-LAWWSGEUC5.e38e33` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -385510 J/mol |  | α-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 14; `ORC-LAWWSGEUC5.fdfebe` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -386000 J/mol |  | α-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 13; `ORC-Z5V53QHJBB.4a9166` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of Tln(T))_ | -0.559 J/mol/K |  | α-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 13; `ORC-Z5V53QHJBB.ca6f0c` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 77.3 J/mol/K |  | α-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 13; `ORC-Z5V53QHJBB.e95734` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -391657 J/mol |  | β-, γ-, δ-Mn + MnO; _alloy: O 0_ | experimental | [1] Grundy 2003; _cites Alcock 1967_ [doi](https://doi.org/10.1016/0013-4686%2867%2985035-7) | Table 6, p. 10, row 12; `ORC-NPJTAQF5YL.2041fb` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 78.06 J/mol/K |  | β-, γ-, δ-Mn + MnO; _alloy: O 0_ | experimental | [1] Grundy 2003; _cites Alcock 1967_ [doi](https://doi.org/10.1016/0013-4686%2867%2985035-7) | Table 6, p. 10, row 12; `ORC-NPJTAQF5YL.652e26` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 76.26 J/mol/K |  | β-, γ-, δ-Mn + MnO; _alloy: O 0_ | experimental | [1] Grundy 2003; _cites Alcock 1967_ [doi](https://doi.org/10.1016/0013-4686%2867%2985035-7) | Table 6, p. 10, row 11; `ORC-RVRGPGPOQB.6ffcbf` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -391538 J/mol |  | β-, γ-, δ-Mn + MnO; _alloy: O 0_ | experimental | [1] Grundy 2003; _cites Alcock 1967_ [doi](https://doi.org/10.1016/0013-4686%2867%2985035-7) | Table 6, p. 10, row 11; `ORC-RVRGPGPOQB.c1c924` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 75.345 J/mol/K |  | β-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 16; `ORC-D4GQ67FU2Y.a30646` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -387830 J/mol |  | β-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 16; `ORC-D4GQ67FU2Y.f276af` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of Tln(T))_ | 1.74 J/mol/K |  | β-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 15; `ORC-ONHBSRDW6S.dc324b` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 61.3 J/mol/K |  | β-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 15; `ORC-ONHBSRDW6S.eac067` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -386000 J/mol |  | β-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 15; `ORC-ONHBSRDW6S.eb808d` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -386000 J/mol |  | γ-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 17; `ORC-T4LU53O274.1f9379` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 50.7 J/mol/K |  | γ-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 17; `ORC-T4LU53O274.3a6cff` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of Tln(T))_ | 3.21 J/mol/K |  | γ-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 17; `ORC-T4LU53O274.7fbf3a` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -390140 J/mol |  | γ-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 18; `ORC-TYZMMQMBSR.548639` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 77.048 J/mol/K |  | γ-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 18; `ORC-TYZMMQMBSR.7dda32` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 79.023 J/mol/K |  | δ-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 20; `ORC-3NWUF4IYCB.6a483d` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -392940 J/mol |  | δ-Mn + MnO; _alloy: O 0_ | unspecified | [1] Grundy 2003 | Table 6, p. 10, row 20; `ORC-3NWUF4IYCB.aeb7e3` |  |
| gibbs energy expression term; _printed: Δ°G(T) (constant term)_ | -386000 J/mol |  | δ-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 19; `ORC-LPHBH37AQX.2d05f2` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of Tln(T))_ | 4.55 J/mol/K |  | δ-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 19; `ORC-LPHBH37AQX.693012` |  |
| gibbs energy expression term; _printed: Δ°G(T) (coefficient of T)_ | 40.9 J/mol/K |  | δ-Mn + MnO; _alloy: O 0_ | model | [1] Grundy 2003 | Table 6, p. 10, row 19; `ORC-LPHBH37AQX.c7f0cd` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Assessment of the Mn-O system, JPE 24, 21-39 (2003). [doi:10.1007/s11669-003-0004-6](https://doi.org/10.1007/s11669-003-0004-6)
2. Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Mn-O System, J. Phase Equilib. Diffus. 31, 113-134 (2010). [doi:10.1007/s11669-009-9643-6](https://doi.org/10.1007/s11669-009-9643-6)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
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
