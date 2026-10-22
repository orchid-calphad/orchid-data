# Eu–Ni system

> Eu–Ni system: 47 accepted literature values (invariant reaction 27, formation 20) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/EU-NI.html · Markdown: https://data.orchid-project.org/systems/EU-NI.md

47 accepted literature values from 1 paper(s) (experimental 18, model 29); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/EU-NI.json) · [CSV](https://data.orchid-project.org/systems/EU-NI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#EU-NI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#EU-NI/EuNi-16Kar.json) · [Markdown](https://data.orchid-project.org/systems/EU-NI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 18 |
| model | 29 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 27 |
| formation | 20 |

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
| 1993.15 | monotectic: Top of the monotectic domain | L: Eu 0.745; Liq: Eu 0.745 | model | [1] Kardellass 2016 | Table 8, p. 13, row 24 |  |
| 1983.15 | monotectic: Top of the monotectic domain | L: Eu 0.74; Liq: Eu 0.74 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 23 |  |
| 1713.15 | congruent melting: Liq -> Ni5Eu | Ni5Eu: Eu 0.166667, Ni 0.833333 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 8 |  |
| 1670.15 | congruent melting: Liq -> Ni5Eu | L: Eu 0.166; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.166 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 9 |  |
| 1666.15 | congruent melting: Liq -> Ni5Eu | Ni5Eu: Eu 0.166667, Ni 0.833333 | model | [1] Kardellass 2016 | Table 8, p. 13, row 10 |  |
| 1593.95 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.0827; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.0827 | model | [1] Kardellass 2016 | Table 8, p. 13, row 4 |  |
| 1589.45 | peritectic: Liq + Ni5Eu -> Ni17Eu2 | L: Eu 0.0827; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni17Eu2: Eu 0.105263, Ni 0.894737; Liq: Eu 0.0827 | model | [1] Kardellass 2016 | Table 8, p. 13, row 7 |  |
| 1543.15 | peritectic: Liq + Ni5Eu -> Ni17Eu2 | L: Eu 0.078; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni17Eu2: Eu 0.105263, Ni 0.894737; Liq: Eu 0.078 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 5 |  |
| 1543.15 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.078; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.078 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 3 |  |
| 1510.15 | peritectic: Liq + Ni5Eu -> Ni17Eu2 | L: Eu 0.0788; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni17Eu2: Eu 0.105263, Ni 0.894737; Liq: Eu 0.0788 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 6 |  |
| 1473.15 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.05; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.05 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 1 |  |
| 1473.15 | eutectic: Liq -> fcc_A1 + Ni5Eu | L: Eu 0.073; Ni5Eu: Eu 0.166667, Ni 0.833333; Liq: Eu 0.073 | model | [1] Kardellass 2016; _cites Tung 1989_ [doi](https://doi.org/10.1007/bf02881420) | Table 8, p. 13, row 2 |  |
| 1391.75 | congruent melting: Liq -> NiEu | L: Eu 0.5; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.5 | model | [1] Kardellass 2016 | Table 8, p. 13, row 16 |  |
| 1371.15 | eutectic: Liq1# -> Liq2# + NiEu | Liq1#: Eu 0.6; Liq2#: Eu 0.851; NiEu: Eu 0.5, Ni 0.5 | model | [1] Kardellass 2016 | Table 8, p. 13, row 22 |  |
| 1365.55 | eutectic: Liq1# -> Liq2# + NiEu | Liq1#: Eu 0.505; Liq2#: Eu 0.948; NiEu: Eu 0.5, Ni 0.5 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 21 |  |
| 1365.55 | peritectic: Liq + Ni5Eu -> Ni2Eu | L: Eu 0.347; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni2Eu: Eu 0.333333, Ni 0.666667; Liq: Eu 0.347 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 12 |  |
| 1365.55 | congruent melting: Liq -> NiEu | L: Eu 0.5; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.5 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 15 |  |
| 1365.55 | congruent melting: Liq -> NiEu | L: Eu 0.5; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.5 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 14 |  |
| 1358.15 | peritectic: Liq + Ni5Eu -> Ni2Eu | L: Eu 0.341; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni2Eu: Eu 0.333333, Ni 0.666667; Liq: Eu 0.341 | model | [1] Kardellass 2016 | Table 8, p. 13, row 13 |  |
| 1342.65 | peritectic: Liq + Ni5Eu -> Ni2Eu | L: Eu 0.366; Ni5Eu: Eu 0.166667, Ni 0.833333; Ni2Eu: Eu 0.333333, Ni 0.666667; Liq: Eu 0.366 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 11 |  |
| 1335.05 | eutectic: Ni2Eu + NiEu -> Liq | Ni2Eu: Eu 0.333333, Ni 0.666667; NiEu: Eu 0.5, Ni 0.5; L: Eu 0.41; Liq: Eu 0.41 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 18 |  |
| 1330.15 | eutectic: Ni2Eu + NiEu -> Liq | Ni2Eu: Eu 0.333333, Ni 0.666667; NiEu: Eu 0.5, Ni 0.5; L: Eu 0.396; Liq: Eu 0.396 | model | [1] Kardellass 2016 | Table 8, p. 13, row 19 |  |
| 1312.15 | eutectic: Liq1# -> Liq2# + NiEu | Liq1#: Eu 0.581; Liq2#: Eu 0.934; NiEu: Eu 0.5, Ni 0.5 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 20 |  |
| 1281.15 | eutectic: Ni2Eu + NiEu -> Liq | Ni2Eu: Eu 0.333333, Ni 0.666667; NiEu: Eu 0.5, Ni 0.5; L: Eu 0.415; Liq: Eu 0.415 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 17 |  |
| 1083.15 | eutectic: Liq -> NiEu + fcc_A1 | L: Eu 0.997; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.997 | experimental | [1] Kardellass 2016; _cites Savitskii 1967_ [doi](https://doi.org/10.1007/bf00819832) | Table 8, p. 13, row 25 |  |
| 1083.15 | eutectic: Liq -> NiEu + fcc_A1 | L: Eu 0.997; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.997 | model | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 8, p. 13, row 26 |  |
| 1023.15 | eutectic: Liq -> NiEu + fcc_A1 | L: Eu 0.954; NiEu: Eu 0.5, Ni 0.5; Liq: Eu 0.954 | model | [1] Kardellass 2016 | Table 8, p. 13, row 27 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Eu–Ni system (10)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ni17Eu2 |  | -48 kJ/mol (basis unstated) ± 4 | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Cignini 2003_ [doi](https://doi.org/10.1016/s0966-9795%2803%2900155-9) | Table 7, p. 13, row 3 |  |
| Ni17Eu2 |  | -9.9 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 2 |  |
| Ni17Eu2 |  | -9 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 1 |  |
| Ni2Eu |  | -16.36 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 6 |  |
| Ni2Eu |  | -16.22 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 8 |  |
| Ni2Eu |  | -15.6 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 7 |  |
| Ni5Eu |  | -15.6 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 5 |  |
| Ni5Eu |  | -14.47 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 4 |  |
| NiEu |  | -16.22 kJ/mol (basis unstated) |  | model |  |  | [1] Kardellass 2016 | Table 7, p. 13, row 8 |  |
| NiEu |  | -13 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 9 |  |

## Other properties

### Formation (10)

Table: Formation, Eu–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropies of formation_ | 37.79 J/mol (basis unstated)/K |  | Ni17Eu2; _alloy: Ni 0.894737_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 1 |  |
| Entropy of formation; _printed: Entropies of formation_ | 57.74 J/mol (basis unstated)/K |  | Ni2Eu; _alloy: Ni 0.5_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 8 |  |
| Entropy of formation; _printed: Entropies of formation_ | 49.55 J/mol (basis unstated)/K |  | Ni2Eu; _alloy: Ni 0.666667_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 6 |  |
| Entropy of formation; _printed: Entropies of formation_ | 41.19 J/mol (basis unstated)/K |  | Ni5Eu; _alloy: Ni 0.833333_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 4 |  |
| Entropy of formation; _printed: Entropies of formation_ | 57.74 J/mol (basis unstated)/K |  | NiEu; _alloy: Ni 0.5_ | model | [1] Kardellass 2016 | Table 7, p. 13, row 8 |  |
| Entropy of formation; _printed: Entropies of formation_ | 2 J/mol (basis unstated)/K ± 0.2 | 298.15 | Ni17Eu2; _alloy: Ni 0.894737_ | experimental | [1] Kardellass 2016; _cites Cignini 2003_ [doi](https://doi.org/10.1016/s0966-9795%2803%2900155-9) | Table 7, p. 13, row 3 |  |
| Entropy of formation; _printed: Entropies of formation_ | -0.1 J/mol (basis unstated)/K | 298.15 | Ni17Eu2; _alloy: Ni 0.894737_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 2 |  |
| Entropy of formation; _printed: Entropies of formation_ | -0.2 J/mol (basis unstated)/K | 298.15 | Ni2Eu; _alloy: Ni 0.666667_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 7 |  |
| Entropy of formation; _printed: Entropies of formation_ | -0.1 J/mol (basis unstated)/K | 298.15 | Ni5Eu; _alloy: Ni 0.833333_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 5 |  |
| Entropy of formation; _printed: Entropies of formation_ | -2 J/mol (basis unstated)/K | 298.15 | NiEu; _alloy: Ni 0.5_ | experimental | [1] Kardellass 2016; _cites Berezutskii 2014_ [doi](https://doi.org/10.1134/s0036024414090064) | Table 7, p. 13, row 9 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016). [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
