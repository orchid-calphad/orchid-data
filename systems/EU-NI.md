# Eu–Ni system

> Eu–Ni system: 55 accepted literature values (invariant reaction 27, formation 19, heat capacity / entropy / enthalpy 9) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/EU-NI.html · Markdown: https://data.orchid-project.org/systems/EU-NI.md

55 accepted literature values from 1 paper(s) (experimental 18, model 37); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/EU-NI.json) · [CSV](https://data.orchid-project.org/systems/EU-NI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#EU-NI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#EU-NI/EuNi-16Kar.json) · [phases (8)](https://data.orchid-project.org/phases/pages/EU-NI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/EU-NI.html) · [Markdown](https://data.orchid-project.org/systems/EU-NI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 18 |
| model | 37 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 27 |
| formation | 19 |
| heat capacity / entropy / enthalpy | 9 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| EuNi-16Kar.tdb | S. Kardellass, C. Servant, N. Selhaoui, J. Thermal Anal. Calorim., 125, 255-69(2016). [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) | `921469b7e3cef2ddddb778c160b323be6584d59358b5d6482b057201f326c468` | [viewer](https://orchid-project.org/phase-diagrams/#EU-NI/EuNi-16Kar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/EuNi-16Kar.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| EuNi-16Kar.tdb | 1557.87 | EUNI5_D2D (x(Ni) 0.83333) + LIQUID (x(Ni) 0.91559) + FCC_A1 (x(Ni) 1) |
| EuNi-16Kar.tdb | 1557.87 | EUNI5_D2D (x(Ni) 0.83333) + LIQUID (x(Ni) 0.91567) + FCC_A1 (x(Ni) 1) |
| EuNi-16Kar.tdb | 1463.99 | EUNI5_D2D (x(Ni) 0.83333) + EU2NI17 (x(Ni) 0.89474) + FCC_A1 (x(Ni) 1) |
| EuNi-16Kar.tdb | 1365.51 | LIQUID#2 (x(Ni) 0.13752) + LIQUID (x(Ni) 0.37891) + EUNI (x(Ni) 0.5) |
| EuNi-16Kar.tdb | 1353.33 | LIQUID (x(Ni) 0.66392) + EUNI2_C36 (x(Ni) 0.66667) + EUNI5_D2D (x(Ni) 0.83333) |
| EuNi-16Kar.tdb | 1353.32 | LIQUID (x(Ni) 0.66365) + EUNI2_C36 (x(Ni) 0.66667) + EUNI5_D2D (x(Ni) 0.83333) |
| EuNi-16Kar.tdb | 1328.66 | EUNI (x(Ni) 0.5) + LIQUID (x(Ni) 0.60675) + EUNI2_C36 (x(Ni) 0.66667) |
| EuNi-16Kar.tdb | 1328.66 | EUNI (x(Ni) 0.5) + LIQUID (x(Ni) 0.60655) + EUNI2_C36 (x(Ni) 0.66667) |
| EuNi-16Kar.tdb | 1044.97 | BCC_A2 (x(Ni) 3.000e-5) + LIQUID (x(Ni) 0.03775) + EUNI (x(Ni) 0.5) |
| EuNi-16Kar.tdb | 1044.97 | BCC_A2 (x(Ni) 3.000e-5) + LIQUID (x(Ni) 0.03764) + EUNI (x(Ni) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/EU/EU-NI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/EU/EU-NI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Eu–Ni system (27)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1993.15 | monotectic: Top of the monotectic domain | L: Eu 0.745; Liq: Eu 0.745 | model | [1] Kardellass 2016 | Table 8, p. 13, row 24; `ORC-RZOKIGX3YF` |  |
| 1983.15 | monotectic: Top of the monotectic domain | L: Eu 0.74; Liq: Eu 0.74 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 23; `ORC-IZOHSXKVNO` |  |
| 1713.15 | congruent melting: Liq -> Ni5Eu | Ni5Eu: Eu 0.166667, Ni 0.833333 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 8; `ORC-ZCG34AZUYB` |  |
| 1670.15 | congruent melting: Liq -> Ni5Eu | L: Eu 0.166; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.166 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 9; `ORC-FZOF2BRP7P` |  |
| 1666.15 | congruent melting: Liq -> Ni5Eu | Ni5Eu: Eu 0.166667, Ni 0.833333 | model | [1] Kardellass 2016 | Table 8, p. 13, row 10; `ORC-AAT3JUB2C4` |  |
| 1593.95 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.0827; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.0827 | model | [1] Kardellass 2016 | Table 8, p. 13, row 4; `ORC-4ECPHMTY4D` |  |
| 1589.45 | peritectic: Liq + Ni5Eu -> Ni17Eu2 | L: Eu 0.0827; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni17Eu2: Eu 0.105263, Ni 0.894737; Liq: Eu 0.0827 | model | [1] Kardellass 2016 | Table 8, p. 13, row 7; `ORC-YPA6MZYSNT` |  |
| 1543.15 | peritectic: Liq + Ni5Eu -> Ni17Eu2 | L: Eu 0.078; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni17Eu2: Eu 0.105263, Ni 0.894737; Liq: Eu 0.078 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 5; `ORC-UJY5YKOBEV` |  |
| 1543.15 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.078; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.078 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 3; `ORC-X6DTTIFSCR` |  |
| 1510.15 | peritectic: Liq + Ni5Eu -> Ni17Eu2 | L: Eu 0.0788; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni17Eu2: Eu 0.105263, Ni 0.894737; Liq: Eu 0.0788 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 6; `ORC-72NTS5V2OI` |  |
| 1473.15 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.05; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.05 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 1; `ORC-3NJTUBL65X` |  |
| 1473.15 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.073; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.073 | model | [1] Kardellass 2016; _cites Tung 1989_ [doi](https://doi.org/10.1007/bf02881420) | Table 8, p. 13, row 2; `ORC-HUCPU26WI6` |  |
| 1391.75 | congruent melting: Liq -> NiEu | L: Eu 0.5; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.5 | model | [1] Kardellass 2016 | Table 8, p. 13, row 16; `ORC-3GVCZ3M2JR` |  |
| 1371.15 | eutectic: Liq1# -> Liq2# + NiEu | Liq1#: Eu 0.6; Liq2#: Eu 0.851; NiEu: Eu 0.5, Ni 0.5 | model | [1] Kardellass 2016 | Table 8, p. 13, row 22; `ORC-H5DEKRXERA` |  |
| 1365.55 | eutectic: Liq1# -> Liq2# + NiEu | Liq1#: Eu 0.505; Liq2#: Eu 0.948; NiEu: Eu 0.5, Ni 0.5 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 21; `ORC-4HYNNUPRZJ` |  |
| 1365.55 | peritectic: Liq + Ni5Eu -> Ni2Eu | L: Eu 0.347; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni2Eu: Eu 0.333333, Ni 0.666667; Liq: Eu 0.347 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 12; `ORC-JZA77ZU3Z4` |  |
| 1365.55 | congruent melting: Liq -> NiEu | L: Eu 0.5; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.5 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 15; `ORC-QYFVFVVZYX` |  |
| 1365.55 | congruent melting: Liq -> NiEu | L: Eu 0.5; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.5 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 14; `ORC-XLIZ42L2TG` |  |
| 1358.15 | peritectic: Liq + Ni5Eu -> Ni2Eu | L: Eu 0.341; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni2Eu: Eu 0.333333, Ni 0.666667; Liq: Eu 0.341 | model | [1] Kardellass 2016 | Table 8, p. 13, row 13; `ORC-3WDZJW3X5L` |  |
| 1342.65 | peritectic: Liq + Ni5Eu -> Ni2Eu | L: Eu 0.366; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni2Eu: Eu 0.333333, Ni 0.666667; Liq: Eu 0.366 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 11; `ORC-GIODDFBPVN` |  |
| 1335.05 | eutectic: Ni2Eu + NiEu -> Liq | Ni2Eu: Eu 0.333333, Ni 0.666667; NiEu: Eu 0.5, Ni 0.5; L: Eu 0.41; Liq: Eu 0.41 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 18; `ORC-KF2J6DSERT` |  |
| 1330.15 | eutectic: Ni2Eu + NiEu -> Liq | Ni2Eu: Eu 0.333333, Ni 0.666667; NiEu: Eu 0.5, Ni 0.5; L: Eu 0.396; Liq: Eu 0.396 | model | [1] Kardellass 2016 | Table 8, p. 13, row 19; `ORC-47RTFF2UR2` |  |
| 1312.15 | eutectic: Liq1# -> Liq2# + NiEu | Liq1#: Eu 0.581; Liq2#: Eu 0.934; NiEu: Eu 0.5, Ni 0.5 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 20; `ORC-XVYXJOCQDZ` |  |
| 1281.15 | eutectic: Ni2Eu + NiEu -> Liq | Ni2Eu: Eu 0.333333, Ni 0.666667; NiEu: Eu 0.5, Ni 0.5; L: Eu 0.415; Liq: Eu 0.415 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 17; `ORC-XIXH2ZBXEW` |  |
| 1083.15 | eutectic: Liq -> NiEu + fcc_A1 | L: Eu 0.997; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.997 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 25; `ORC-QQZYKSBMIO` |  |
| 1083.15 | eutectic: Liq -> NiEu + fcc_A1 | L: Eu 0.997; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.997 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 26; `ORC-S4GLOYVWBD` |  |
| 1023.15 | eutectic: Liq -> NiEu + fcc_A1 | L: Eu 0.954; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.954 | model | [1] Kardellass 2016 | Table 8, p. 13, row 27; `ORC-CLW4Y5L2AF` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Eu–Ni system (14)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ni17Eu2 |  | -48 kJ/mol (basis unstated) ± 4 | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Cignini 2003_ [doi](https://doi.org/10.1016/s0966-9795%2803%2900155-9) | Table 7, p. 13, row 3; `ORC-MQJOYXSXAF.a82c93` |  |
| Ni17Eu2 |  | -9.9 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 2; `ORC-OFQIU3EJTQ.af7938` |  |
| Ni17Eu2 | [Eu2Ni17](https://data.orchid-project.org/compounds/Eu2Ni17.html) | -9 kJ/mol-atom | 298.15 | model | -6.408 (mp-aaacqixi) | -12.136 (oqmd-30108) | [1] Kardellass 2016 | Table 4, p. 7, row 3; `ORC-EVU6QOBHFX.35987c` |  |
| Ni17Eu2 |  | -9 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 1; `ORC-UXZ7KE63PM.75b93e` |  |
| Ni2Eu |  | -16.36 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 6; `ORC-A6KOMUBVA5.1ef03e` |  |
| Ni2Eu | [EuNi2](https://data.orchid-project.org/compounds/EuNi2.html) | -16.36 kJ/mol-atom | 298.15 | model |  | -37.69 (oqmd-1591127) | [1] Kardellass 2016 | Table 4, p. 7, row 10; `ORC-K4PJKKIDRN.1a10a1` |  |
| Ni2Eu |  | -16.22 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 8; `ORC-4F2EYUKZH7.66f9d0` |  |
| Ni2Eu |  | -15.6 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 7; `ORC-OFI7V7CDNZ.5d72fe` |  |
| Ni5Eu |  | -15.6 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 5; `ORC-ALJUMA5B62.aa752a` |  |
| Ni5Eu | [EuNi5](https://data.orchid-project.org/compounds/EuNi5.html) | -14.47 kJ/mol-atom | 298.15 | model | -12.017 (mp-aaaabhad) | -21.135 (oqmd-30109) | [1] Kardellass 2016 | Table 4, p. 7, row 6; `ORC-7VZKE7XNKM.5d2b1f` |  |
| Ni5Eu |  | -14.47 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 4; `ORC-AYACNSRBQF.74c238` |  |
| NiEu |  | -16.22 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 8; `ORC-4F2EYUKZH7.7b0842` |  |
| NiEu | [EuNi](https://data.orchid-project.org/compounds/EuNi.html) | -16.22 kJ/mol-atom | 298.15 | model |  | -30.347 (oqmd-1366256) | [1] Kardellass 2016 | Table 4, p. 7, row 14; `ORC-MGFXQXSL57.d2f173` |  |
| NiEu |  | -13 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 9; `ORC-5MJRSHIRLY.2364d5` |  |

## Other properties

### Formation (5)

Table: Formation, Eu–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropies of formation_ | 2 J/mol (basis unstated)/K ± 0.2 | 298.15 | Ni17Eu2; _alloy: Ni 0.894737_ | experimental | [1] Kardellass 2016; _cites Cignini 2003_ [doi](https://doi.org/10.1016/s0966-9795%2803%2900155-9) | Table 7, p. 13, row 3; `ORC-MQJOYXSXAF.b54a5c` |  |
| Entropy of formation; _printed: Entropies of formation_ | -0.1 J/mol (basis unstated)/K | 298.15 | Ni17Eu2; _alloy: Ni 0.894737_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 2; `ORC-OFQIU3EJTQ.b9704b` |  |
| Entropy of formation; _printed: Entropies of formation_ | -0.2 J/mol (basis unstated)/K | 298.15 | Ni2Eu; _alloy: Ni 0.666667_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 7; `ORC-OFI7V7CDNZ.1b3a5c` |  |
| Entropy of formation; _printed: Entropies of formation_ | -0.1 J/mol (basis unstated)/K | 298.15 | Ni5Eu; _alloy: Ni 0.833333_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 5; `ORC-ALJUMA5B62.57896c` |  |
| Entropy of formation; _printed: Entropies of formation_ | -2 J/mol (basis unstated)/K | 298.15 | NiEu; _alloy: Ni 0.5_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 9; `ORC-5MJRSHIRLY.6ed7d7` |  |

### Heat capacity / entropy / enthalpy (9)

Table: Heat capacity / entropy / enthalpy, Eu–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Entropies of formation_ | 37.79 J/mol (basis unstated)/K |  | Ni17Eu2; _alloy: Ni 0.894737_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 1; `ORC-UXZ7KE63PM.045e19` |  |
| Entropy; _printed: Entropies of formation_ | 57.74 J/mol (basis unstated)/K |  | Ni2Eu; _alloy: Eu 0.333333, Ni 0.666667_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 8; `ORC-4F2EYUKZH7.91623b` |  |
| Entropy; _printed: Entropies of formation_ | 49.55 J/mol (basis unstated)/K |  | Ni2Eu; _alloy: Ni 0.666667_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 6; `ORC-A6KOMUBVA5.327710` |  |
| Entropy; _printed: Entropies of formation_ | 41.19 J/mol (basis unstated)/K |  | Ni5Eu; _alloy: Ni 0.833333_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 4; `ORC-AYACNSRBQF.6b17b6` |  |
| Entropy; _printed: Entropies of formation_ | 57.74 J/mol (basis unstated)/K |  | NiEu; _alloy: Ni 0.5_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 8; `ORC-4F2EYUKZH7.9ea394` |  |
| Entropy; _printed: Entropies of formation_ | 37.78 J/mol-atom/K | 298.15 | Ni17Eu2; _alloy: Ni 0.894737_ | model | [1] Kardellass 2016 | Table 4, p. 7, row 3; `ORC-EVU6QOBHFX.0bc32a` |  |
| Entropy; _printed: Entropies of formation_ | 49.55 J/mol-atom/K | 298.15 | Ni2Eu; _alloy: Ni 0.666667_ | model | [1] Kardellass 2016 | Table 4, p. 7, row 10; `ORC-K4PJKKIDRN.8f1322` |  |
| Entropy; _printed: Entropies of formation_ | 41.19 J/mol-atom/K | 298.15 | Ni5Eu; _alloy: Ni 0.833333_ | model | [1] Kardellass 2016 | Table 4, p. 7, row 6; `ORC-7VZKE7XNKM.6fbc38` |  |
| Entropy; _printed: Entropies of formation_ | 57.74 J/mol-atom/K | 298.15 | NiEu; _alloy: Ni 0.5_ | model | [1] Kardellass 2016 | Table 4, p. 7, row 14; `ORC-MGFXQXSL57.c2a181` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016). [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
