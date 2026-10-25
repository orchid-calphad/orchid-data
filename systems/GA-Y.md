# Ga–Y system

> Ga–Y system: 51 accepted literature values (formation 23, invariant reaction 19, phase transition 6, mixing / partial 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-Y.html · Markdown: https://data.orchid-project.org/systems/GA-Y.md

51 accepted literature values from 1 paper(s) (experimental 23, model 28); 1 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-Y.json) · [CSV](https://data.orchid-project.org/systems/GA-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-Y/GaY-13Idb.json) · [phases (10)](https://data.orchid-project.org/phases/pages/GA-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-Y.html) · [Markdown](https://data.orchid-project.org/systems/GA-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 23 |
| model | 28 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 19 |
| phase transition | 6 |
| formation | 23 |
| mixing / partial | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaY-13Idb.tdb | M. Idbenali, C. Servant, J. Therm. Anal. Calorim., 112, 245-53(2013). [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) | `cbddd22351605c045afe0d705d5ffd6c73c043a0c067ec7e6ee22e023b3785de` | [viewer](https://orchid-project.org/phase-diagrams/#GA-Y/GaY-13Idb.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaY-13Idb.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaY-13Idb.tdb | 1557.13 | GAY_B33 (x(Y) 0.5) + LIQUID (x(Y) 0.58341) + GA3Y5_D88 (x(Y) 0.625) |
| GaY-13Idb.tdb | 1557.13 | GAY_B33 (x(Y) 0.5) + LIQUID (x(Y) 0.58338) + GA3Y5_D88 (x(Y) 0.625) |
| GaY-13Idb.tdb | 1543.04 | GA2Y_C32 (x(Y) 0.33333) + LIQUID (x(Y) 0.40866) + GAY_B33 (x(Y) 0.5) |
| GaY-13Idb.tdb | 1543.04 | GA2Y_C32 (x(Y) 0.33333) + LIQUID (x(Y) 0.40867) + GAY_B33 (x(Y) 0.5) |
| GaY-13Idb.tdb | 1272.72 | GAY_B33 (x(Y) 0.5) + GA3Y5_D88 (x(Y) 0.625) + GA3Y5_MT (x(Y) 0.625) |
| GaY-13Idb.tdb | 1073.42 | GAY_B33 (x(Y) 0.5) + GA3Y5_LT (x(Y) 0.625) + GA3Y5_MT (x(Y) 0.625) |
| GaY-13Idb.tdb | 1073.42 | GA3Y5_MT (x(Y) 0.625) + GA3Y5_LT (x(Y) 0.625) + HCP_A3 (x(Y) 1) |
| GaY-13Idb.tdb | 302.32 | ORTHORHOMBIC_A11 (x(Y) 0) + LIQUID (x(Y) 0.0054) + GA2Y_C32 (x(Y) 0.33333) |
| GaY-13Idb.tdb | 302.32 | ORTHORHOMBIC_A11 (x(Y) 0) + LIQUID (x(Y) 0.00538) + GA2Y_C32 (x(Y) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ga–Y system (19)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1752 | α(Y) -> β(Y) + Liq | L: Y 0.9786 | model | [1] Idbenali 2013 | Table 4, p. 5, row 27; `ORC-4MRUWGNJBJ` |  |
| 1751 | α(Y) -> β(Y) + Liq | L: Y 0.982 | model | [1] Idbenali 2013 | Table 4, p. 5, row 26; `ORC-D4SP4OTABZ` |  |
| 1751 | α(Y) -> β(Y) + Liq | L: Y 0.963 | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 25; `ORC-EG4HYQZ6B3` |  |
| 1568 | H_Ga3Y5 -> Liq + GaY | H_Ga3Y5: Y 0.625; L: Y 0.58; GaY: Y 0.5 | model | [1] Idbenali 2013 | Table 4, p. 5, row 14; `ORC-NZTWO7ITPO` |  |
| 1568 | H_Ga3Y5 -> Liq + GaY | H_Ga3Y5: Y 0.625; L: Y 0.5937; GaY: Y 0.5 | model | [1] Idbenali 2013 | Table 4, p. 5, row 15; `ORC-SZU2BT3FYR` |  |
| 1568 | H_Ga3Y5 -> Liq + GaY | H_Ga3Y5: Y 0.625; L: Y 0.625; GaY: Y 0.5 | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 13; `ORC-UQDDTCLCKV` |  |
| 1559 | eutectic: Liq -> Ga2Y + GaY | L: Y 0.4053; Ga2Y: Y 0.333333; GaY: Y 0.5 | model | [1] Idbenali 2013 | Table 4, p. 5, row 9; `ORC-FVEBUUG4BT` |  |
| 1544 | eutectic: Liq -> Ga2Y + GaY | L: Y 0.46; Ga2Y: Y 0.333333; GaY: Y 0.5 | model | [1] Idbenali 2013 | Table 4, p. 5, row 8; `ORC-HI63GB6JLU` |  |
| 1543 | eutectic: Liq -> Ga2Y + GaY | L: Y 0.43; Ga2Y: Y 0.333333; GaY: Y 0.5 | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 7; `ORC-IQ6QPENUUA` |  |
| 1286 | eutectic: Liq -> H_Ga3Y5 + α(Y) | L: Y 0.8; H_Ga3Y5: Y 0.625 | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 16; `ORC-ECQBHX2HWL` |  |
| 1283 | eutectic: Liq -> H_Ga3Y5 + α(Y) | L: Y 0.815; H_Ga3Y5: Y 0.625 | model | [1] Idbenali 2013 | Table 4, p. 5, row 17; `ORC-4Z6AFCLTWW` |  |
| 1283 | eutectic: Liq -> H_Ga3Y5 + α(Y) | L: Y 0.7747; H_Ga3Y5: Y 0.625 | model | [1] Idbenali 2013 | Table 4, p. 5, row 18; `ORC-A2OUVDOUAT` |  |
| 1273 | H_Ga3Y5 -> M_Ga3Y5 + α(Y) | H_Ga3Y5: Y 0.625; M_Ga3Y5: Y 0.615 | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 19; `ORC-AHZC3T4NQO` |  |
| 1273 | H_Ga3Y5 -> M_Ga3Y5 + α(Y) | H_Ga3Y5: Y 0.625; M_Ga3Y5: Y 0.625 | model | [1] Idbenali 2013 | Table 4, p. 5, row 21; `ORC-IHIZBNKPIO` |  |
| 1073 | M_Ga3Y5 -> L_Ga3Y5 + α(Y) | M_Ga3Y5: Y 0.625; L_Ga3Y5: Y 0.625 | model | [1] Idbenali 2013 | Table 4, p. 5, row 24; `ORC-2VVZRAUSQW` |  |
| 1073 | M_Ga3Y5 -> L_Ga3Y5 + α(Y) | M_Ga3Y5: Y 0.625; L_Ga3Y5: Y 0.625 | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 22; `ORC-5SQRLD6MPY` |  |
| 303 | (Ga) -> Liq + Ga2Y | (Ga): Y 0; L: Y 1.000e-4; Ga2Y: Y 0.333333 | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 1; `ORC-RD7RVLAA3Q` |  |
| 302 | (Ga) -> Liq + Ga2Y | (Ga): Y 0; L: Y 0.0057; Ga2Y: Y 0.333333 | model | [1] Idbenali 2013 | Table 4, p. 5, row 2; `ORC-EWFLVC2F6G` |  |
| 300.7 | (Ga) -> Liq + Ga2Y | (Ga): Y 0; L: Y 0.0235; Ga2Y: Y 0.333333 | model | [1] Idbenali 2013 | Table 4, p. 5, row 3; `ORC-AXWIA3KMI2` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ga–Y system (23)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -74.6 kJ/mol-atom ± 1.5 | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Meschel 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900599-x) | Table 5, p. 7, row 11; `ORC-D62AZ3EOOF` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -73.49 kJ/mol-atom | 298.15 | model | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013 | Table 5, p. 7, row 4; `ORC-HGBUPAPL5B` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -73.47 kJ/mol-atom | 298.15 | model | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013 | Table 5, p. 7, row 3; `ORC-T3KIGB7X3X` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -72.1 kJ/mol-atom ± 1.3 | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Meschel 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900599-x) | Table 5, p. 7, row 9; `ORC-AK4MEPFDCO` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -70.9 kJ/mol-atom ± 1.5 | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Yamshchikov 1979_ | Table 5, p. 7, row 12; `ORC-XQVVHXIE2P` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -69 kJ/mol-atom | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Merker 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990065-c) | Table 5, p. 7, row 8; `ORC-EMXATGHEVS` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -68.4 kJ/mol-atom ± 1.3 | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Yamshchikov 1979_ | Table 5, p. 7, row 10; `ORC-L5OSCQ3MBA` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -68.1 kJ/mol-atom ± 2.3 | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Meschel 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900599-x) | Table 5, p. 7, row 7; `ORC-5K3AIJTOR3` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -65 kJ/mol-atom | 298.15 | model | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites de Boer FR 1988_ | Table 5, p. 7, row 5; `ORC-2X4VVWDTWE` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -64.4 kJ/mol-atom ± 2.5 | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Babu 2000_ [doi](https://doi.org/10.1016/s0925-8388%2800%2901132-4) | Table 5, p. 7, row 6; `ORC-3AMEIA2A2X` |  |
| Ga2Y | [Ga2Y](https://data.orchid-project.org/compounds/Ga2Y.html) | -61.8 kJ/mol-atom ± 2.8 | 298.15 | experimental | -64.044 (mp-aaaaacvq) | -63.776 (oqmd-30368) | [1] Idbenali 2013; _cites Babu 2000_ [doi](https://doi.org/10.1016/s0925-8388%2800%2901132-4) | Table 5, p. 7, row 2; `ORC-HNUQ7TBIW2.63f956` |  |
| Ga3Y5 | [Ga3Y5](https://data.orchid-project.org/compounds/Ga3Y5.html) | -64 kJ/mol-atom | 298.15 | model | -50.575 (mp-aaabmgma) | -50.713 (oqmd-18353) | [1] Idbenali 2013 | Table 5, p. 7, row 21; `ORC-GIT22H6OAM` |  |
| Ga3Y5 | [Ga3Y5](https://data.orchid-project.org/compounds/Ga3Y5.html) | -63.99 kJ/mol-atom | 298.15 | model | -50.575 (mp-aaabmgma) | -50.713 (oqmd-18353) | [1] Idbenali 2013 | Table 5, p. 7, row 20; `ORC-ZNJGLQGMYJ` |  |
| Ga3Y5 | [Ga3Y5](https://data.orchid-project.org/compounds/Ga3Y5.html) | -61 kJ/mol-atom | 298.15 | model | -50.575 (mp-aaabmgma) | -50.713 (oqmd-18353) | [1] Idbenali 2013; _cites de Boer FR 1988_ | Table 5, p. 7, row 22; `ORC-EEM6AJQFIL` |  |
| Ga3Y5 | [Ga3Y5](https://data.orchid-project.org/compounds/Ga3Y5.html) | -59.6 kJ/mol-atom ± 3.6 | 298.15 | experimental | -50.575 (mp-aaabmgma) | -50.713 (oqmd-18353) | [1] Idbenali 2013; _cites Babu 2000_ [doi](https://doi.org/10.1016/s0925-8388%2800%2901132-4) | Table 5, p. 7, row 23; `ORC-KW3VBQ6QZL` |  |
| Ga3Y5 | [Ga3Y5](https://data.orchid-project.org/compounds/Ga3Y5.html) | -57 kJ/mol-atom | 298.15 | experimental | -50.575 (mp-aaabmgma) | -50.713 (oqmd-18353) | [1] Idbenali 2013; _cites Merker 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990065-c) | Table 5, p. 7, row 19; `ORC-FQDLRJYDWH` |  |
| Ga6Y | [Ga6Y](https://data.orchid-project.org/compounds/Ga6Y.html) | -35 kJ/mol-atom | 298.15 | model | -29.959 (mp-aaaabtkb) | -30.859 (oqmd-17313) | [1] Idbenali 2013 | Table 5, p. 7, row 1; `ORC-FYWH2NPMWI` |  |
| GaY | [GaY](https://data.orchid-project.org/compounds/GaY.html) | -75.2 kJ/mol-atom | 298.15 | model | -64.449 (mp-aaaaaqxg) | -64.338 (oqmd-30366) | [1] Idbenali 2013 | Table 5, p. 7, row 14; `ORC-CD4LXZ4CMM` |  |
| GaY | [GaY](https://data.orchid-project.org/compounds/GaY.html) | -75.19 kJ/mol-atom | 298.15 | model | -64.449 (mp-aaaaaqxg) | -64.338 (oqmd-30366) | [1] Idbenali 2013 | Table 5, p. 7, row 15; `ORC-AONFJJ2L4W` |  |
| GaY | [GaY](https://data.orchid-project.org/compounds/GaY.html) | -73 kJ/mol-atom | 298.15 | model | -64.449 (mp-aaaaaqxg) | -64.338 (oqmd-30366) | [1] Idbenali 2013; _cites de Boer FR 1988_ | Table 5, p. 7, row 16; `ORC-KP454ZSCIO` |  |
| GaY | [GaY](https://data.orchid-project.org/compounds/GaY.html) | -71.4 kJ/mol-atom ± 1.7 | 298.15 | experimental | -64.449 (mp-aaaaaqxg) | -64.338 (oqmd-30366) | [1] Idbenali 2013; _cites Meschel 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900599-x) | Table 5, p. 7, row 17; `ORC-UM363FP6O2` |  |
| GaY | [GaY](https://data.orchid-project.org/compounds/GaY.html) | -71 kJ/mol-atom | 298.15 | experimental | -64.449 (mp-aaaaaqxg) | -64.338 (oqmd-30366) | [1] Idbenali 2013; _cites Merker 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990065-c) | Table 5, p. 7, row 18; `ORC-PITICB4H36` |  |
| GaY | [GaY](https://data.orchid-project.org/compounds/GaY.html) | -68.9 kJ/mol-atom ± 2.8 | 298.15 | experimental | -64.449 (mp-aaaaaqxg) | -64.338 (oqmd-30366) | [1] Idbenali 2013; _cites Babu 2000_ [doi](https://doi.org/10.1016/s0925-8388%2800%2901132-4) | Table 5, p. 7, row 13; `ORC-3KBBK4PM37` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Ga–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1615 K | 1615 | Liq -> Ga2Y; _Ga2Y: Y 0.3367_ | model | [1] Idbenali 2013 | Table 4, p. 5, row 6; `ORC-6H52MIEBYC` |  |
| Phase transition | 1623 K | 1623 | Liq -> Ga2Y; _Ga2Y: Y 0.3333_ | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 4; `ORC-HNCCST2TG4` |  |
| Phase transition | 1624 K | 1624 | Liq -> Ga2Y; _Ga2Y: Y 0.332_ | model | [1] Idbenali 2013 | Table 4, p. 5, row 5; `ORC-CQE33SS5KK` |  |
| Phase transition | 1658 K | 1658 | Liq -> GaY; _GaY: Y 0.5_ | experimental | [1] Idbenali 2013; _cites Yatsenko 1979_ [doi](https://doi.org/10.1016/0022-5088%2879%2990170-x) | Table 4, p. 5, row 10; `ORC-IK5YTX22FW` |  |
| Phase transition | 1666 K | 1666 | Liq -> GaY; _GaY: Y 0.5_ | model | [1] Idbenali 2013 | Table 4, p. 5, row 12; `ORC-3GURFDLFLU` |  |
| Phase transition | 1672 K | 1672 | Liq -> GaY; _GaY: Y 0.5_ | model | [1] Idbenali 2013 | Table 4, p. 5, row 11; `ORC-3GNQ6TNQY2` |  |

### Mixing / partial (3)

Table: Mixing / partial, Ga–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Partial enthalpy; _printed: partial enthalpy of liquid Y in liquid Ga_ | -180.25 unspecified | 14 |  | model | [1] Idbenali 2013; _cites de Boer FR 1988_ | p. 8; `ORC-VBJYFKJOYL.6c4773` | “liquid Y in liquid Ga (R-K equation) at 1,750 K (-181 kJ mol-1 at.-1) is in good agreement with the data (-181.63 ± 7.93 kJ mol-1 at.-1) by \[6\] or (-184.4 ± 5.3 kJ mol-1 at.-1) by \[24\] at 1,099 K or the predicted value (-180.25 kJ mol-1 at.-1) by \[27\] at 14 K (Table 5).” |
| Partial enthalpy; _printed: partial enthalpy of liquid Y in liquid Ga_ | -184.4 unspecified ± 5.3 | 1099 |  | experimental | [1] Idbenali 2013; _cites Babu 2000_ [doi](https://doi.org/10.1016/s0925-8388%2800%2901132-4) | p. 8; `ORC-VBJYFKJOYL.cce770` | “liquid Y in liquid Ga (R-K equation) at 1,750 K (-181 kJ mol-1 at.-1) is in good agreement with the data (-181.63 ± 7.93 kJ mol-1 at.-1) by \[6\] or (-184.4 ± 5.3 kJ mol-1 at.-1) by \[24\] at 1,099 K or the predicted value (-180.25 kJ mol-1 at.-1) by \[27\] at 14 K (Table 5).” |
| Partial enthalpy; _printed: partial enthalpy of liquid Y in liquid Ga_ | -181 kJ/mol-atom | 1750 |  | model | [1] Idbenali 2013 | p. 8; `ORC-VBJYFKJOYL.c2281a` | “liquid Y in liquid Ga (R-K equation) at 1,750 K (-181 kJ mol-1 at.-1) is in good agreement with the data (-181.63 ± 7.93 kJ mol-1 at.-1) by \[6\] or (-184.4 ± 5.3 kJ mol-1 at.-1) by \[24\] at 1,099 K or the predicted value (-180.25 kJ mol-1 at.-1) by \[27\] at 14 K (Table 5).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013). [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
