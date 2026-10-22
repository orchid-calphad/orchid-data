# Ca–O system

> Ca–O system: 67 accepted literature values (heat capacity / entropy / enthalpy 26, phase equilibrium 18, formation 14, phase transition 5) and 4 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-O.html · Markdown: https://data.orchid-project.org/systems/CA-O.md

67 accepted literature values from 2 paper(s) (experimental 12, model 49, DFT 6); 4 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-O.json) · [CSV](https://data.orchid-project.org/systems/CA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-O/CaO-18Lia.json) · [Markdown](https://data.orchid-project.org/systems/CA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 49 |
| DFT | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 5 |
| phase equilibrium | 18 |
| formation | 14 |
| heat capacity / entropy / enthalpy | 26 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaO-18Lia.tdb | S.-M. Liang, R. Schmid-Fetzer, J. Eur. Ceram. Soc., 38, 4768-85(2018). [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | `78618178a1324682abe5762bf34fd20689dfc6461c02571d1f63465f606dfcc1` | [viewer](https://orchid-project.org/phase-diagrams/#CA-O/CaO-18Lia.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaO-18Lia.json) |
| CaO-20Def-3g.tdb | G. Deffrennes, N. Jakse, C.M.S. Alvares, I. Nuta, A. Pasturel, A.V. Khvan, A. Pisch, Calphad, 69, 101764(2020). [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) | `2df29e5f285a88c61920a1de0346ed6dd875de0fc237350301d09f81ab4df153` | [viewer](https://orchid-project.org/phase-diagrams/#CA-O/CaO-20Def-3g.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaO-20Def-3g.json) |
| CaO-23Abd-3g.tdb | W. Abdul, C. Mawalala, A. Pisch, M.N. Bannerman, Cem. Concr. Res., 173, 107309(2023). [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) | `c6509b3e8c06ae7f3214e95a3bdd245dabd062bed11d4cb6bbf45398f8017220` | [viewer](https://orchid-project.org/phase-diagrams/#CA-O/CaO-23Abd-3g.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaO-23Abd-3g.json) |
| CaO-96Sel.tdb | M. Selleby, B. Sundman, Calphad, 20, 391-92(1996). [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) | `c26a22ca6d938a23c4deba75b8dd32e0968fb65a59ed515eb6d0dc508a66bcb7` | [viewer](https://orchid-project.org/phase-diagrams/#CA-O/CaO-96Sel.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaO-96Sel.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaO-23Abd-3g.tdb | 716.03 | BCC_A2 (x(O) 0) + FCC_A1 (x(O) 0) + B1_OXIDE (x(O) 0.5) |
| CaO-96Sel.tdb | 1111.39 | BCC_A2 (x(O) 0) + ION (x(O) 0.00299) + B1_OXIDE (x(O) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-O.json) · [CALPHAD hull CaO-20Def-3g](https://data.orchid-project.org/hulls/calphad-sgte/CA/CA-O--CaO-20Def-3g.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–O system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 3221.3 | eutectic: L = Gas + CaO(s) |  | model | [1] Liang 2018 | p. 14 | “With O-excess the invariant of eutectic type L (50.02 at.% O) = Gas (99.5 at.% O) + CaO(s) forms at 3221.3 K.” |
| 3217.4 | eutectic: L = Gas + CaO(s) |  | model | [1] Liang 2018 | p. 14 | “With Ca-excess in the liquid the invariant of eutectic type L (49.89 at.% O) = Gas (0.8 at.% O) + CaO(s) forms at 3217.4 K.” |
| 1103.2 | eutectic: L -> β-Ca + CaO | L: O 0.0098 | model | [2] Deffrennes 2020 | Table 4, p. 21, row 2 |  |
| 1094.6 | eutectic: L -> β-Ca + CaO | L: O 0.017 | model | [2] Deffrennes 2020 | Table 4, p. 21, row 1 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ca–O system (14)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -635.1 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020; _cites Chase 1963_ | Table 3, p. 17, row 6 |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -635.1 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 3 |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -634.6 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020 | Table 3, p. 17, row 1 |  |
| CaO(cr) |  | -634.6 kJ/mol-atom | 298.15 | DFT |  |  | [2] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 5 |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -634 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 2 |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -634 kJ/mol-atom ± 1.5 | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 4 |  |
| CaO(liq-am) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -600.9 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020 | Table 3, p. 17, row 7 |  |
| CaO(liq-am) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -565.6 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 8 |  |
| CaO(liq-am) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -557.3 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020; _cites Chase 1963_ | Table 3, p. 17, row 10 |  |
| CaO(liq-am) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -555.6 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 9 |  |
| CaO2(cr) | [CaO2](https://data.orchid-project.org/compounds/CaO2.html) | -659 kJ/mol-atom | 298.15 | model | -212.9 (mp-aaabkddr) | -219.972 (oqmd-1367693) | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 13 |  |
| CaO2(cr) | [CaO2](https://data.orchid-project.org/compounds/CaO2.html) | -652.7 kJ/mol-atom | 298.15 | model | -212.9 (mp-aaabkddr) | -219.972 (oqmd-1367693) | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 12 |  |
| CaO2(cr) |  | -648.1 kJ/mol-atom | 298.15 | DFT |  |  | [2] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 14 |  |
| CaO2(cr) | [CaO2](https://data.orchid-project.org/compounds/CaO2.html) | -648.1 kJ/mol-atom | 298.15 | model | -212.9 (mp-aaabkddr) | -219.972 (oqmd-1367693) | [2] Deffrennes 2020 | Table 3, p. 17, row 11 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Ca–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2845 K | 2845 |  | model | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | p. 17 | “Compared to previous modellings of the system, the description of Lindberg et al. \[17\] features a discontinuity in heat content at their selected melting point of 2845 K, and the one of Liang et al. \[18\] does not reproduce the very high temperature increase in heat content observed experimentally by Chekhovskoi et al. \[34\] and in molecular dynamics simulations conducted by Alvares et al. \[37\].” |
| Phase transition | 3217 K | 3217 | other | model | [1] Liang 2018 | p. 6 | “At 3217 K the three-phase equilibrium, Gas (0.8 at.% O) + L + CaO(s) is calculated in the binary Ca-O system at 1 bar.” |
| Phase transition | 3221.8 K | 3221.8 | congruent | model | [1] Liang 2018 | p. 14 | “However, in the binary Ca-O system the congruent melting point of CaO occurs at 3221.8 K.” |
| Phase transition | 3222 K | 3222 |  | model | [2] Deffrennes 2020 | p. 19 | “The heat capacity of liquid CaO modelled by Liang et al. \[18\] is in acceptable agreement with the one proposed in this work above the melting point of CaO selected at 3222 K in both assessments.” |
| Phase transition | 3222 K | 3222 |  | experimental | [2] Deffrennes 2020 | p. 12 | “To begin with, the heat capacity of the phase was described up to the compound's selected melting point of 3222 K using the DFT data from Alvares et al. \[37\] up to 1700 K and the heat content data obtained by the same authors by ab initio molecular dynamics.” |

### Phase equilibrium (18)

Table: Phase equilibrium, Ca–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 2843 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Kanolt 1913_ | Table 2, p. 5, row 1 |  |
| Phase composition |  | 2845 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [1] Liang 2018; _cites Factsage 2017_ | Table 2, p. 5, row 16 |  |
| Phase composition |  | 2849 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Schumacher 1926_ [doi](https://doi.org/10.1021/ja01413a013) | Table 2, p. 5, row 2 |  |
| Phase composition |  | 2863 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Noguchi 1967_ [doi](https://doi.org/10.1016/0038-092x%2867%2990022-9) | Table 2, p. 5, row 6 |  |
| Phase composition |  | 2886 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [1] Liang 2018; _cites Hlavac 1982_ [doi](https://doi.org/10.1351/pac198254030681) | Table 2, p. 5, row 12 |  |
| Phase composition |  | 2886 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [1] Liang 2018; _cites Wriedt 1985_ [doi](https://doi.org/10.1007/bf02880517) | Table 2, p. 5, row 13 |  |
| Phase composition |  | 2890 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Panek 1979_ | Table 2, p. 5, row 9 |  |
| Phase composition |  | 2893 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites OlShanskil 1958_ | Table 2, p. 5, row 3 |  |
| Phase composition |  | 2898 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Doman 1963_ | Table 2, p. 5, row 4 |  |
| Phase composition |  | 2900 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [1] Liang 2018; _cites Kubaschewski 1993_ | Table 2, p. 5, row 14 |  |
| Phase composition |  | 3172 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Yamada 1986_ [doi](https://doi.org/10.1111/j.1151-2916.1986.tb07350.x) | Table 2, p. 5, row 10 |  |
| Phase composition |  | 3172 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [1] Liang 2018; _cites SGTE 2013_ | Table 2, p. 5, row 17 |  |
| Phase composition |  | 3173 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Traverse 1969_ | Table 2, p. 5, row 8 |  |
| Phase composition |  | 3183 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Foex 1965_ [doi](https://doi.org/10.1016/0038-092x%2865%2990162-3) | Table 2, p. 5, row 5 |  |
| Phase composition |  | 3200 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [1] Liang 2018; _cites Chase 1998_ | Table 2, p. 5, row 15 |  |
| Phase composition |  | 3222 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [1] Liang 2018 | Table 2, p. 5, row 18 |  |
| Phase composition |  | 3222 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Manara 2013_ | Table 2, p. 5, row 11 |  |
| Phase composition |  | 3223 | congruent: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [1] Liang 2018; _cites Foex 1968_ | Table 2, p. 5, row 7 |  |

### Heat capacity / entropy / enthalpy (26)

Table: Heat capacity / entropy / enthalpy, Ca–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S°_ | 38.21 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Chase 1963_ | Table 3, p. 17, row 6 |  |
| Entropy; _printed: S°_ | 38.1 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 2 |  |
| Entropy; _printed: S°_ | 40.35 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020 | Table 3, p. 17, row 1 |  |
| Entropy; _printed: S°_ | 40.35 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | DFT | [2] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 5 |  |
| Entropy; _printed: S°_ | 37.75 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 3 |  |
| Entropy; _printed: S°_ | 62.32 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Chase 1963_ | Table 3, p. 17, row 10 |  |
| Entropy; _printed: S°_ | 58.69 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 8 |  |
| Entropy; _printed: S°_ | 40.35 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020 | Table 3, p. 17, row 7 |  |
| Entropy; _printed: S°_ | 65.69 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 9 |  |
| Entropy; _printed: S°_ | 83.68 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 13 |  |
| Entropy; _printed: S°_ | 59.6 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | DFT | [2] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 14 |  |
| Entropy; _printed: S°_ | 59.6 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [2] Deffrennes 2020 | Table 3, p. 17, row 11 |  |
| Entropy; _printed: S°_ | 83.68 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 12 |  |
| Heat capacity; _printed: Cp°_ | 42.12 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Chase 1963_ | Table 3, p. 17, row 6 |  |
| Heat capacity; _printed: Cp°_ | 42.05 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 2 |  |
| Heat capacity; _printed: Cp°_ | 42.73 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020 | Table 3, p. 17, row 1 |  |
| Heat capacity; _printed: Cp°_ | 42.73 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | DFT | [2] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 5 |  |
| Heat capacity; _printed: Cp°_ | 42.02 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 3 |  |
| Heat capacity; _printed: Cp°_ | 42.12 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Chase 1963_ | Table 3, p. 17, row 10 |  |
| Heat capacity; _printed: Cp°_ | 42.04 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 8 |  |
| Heat capacity; _printed: Cp°_ | 42.73 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020 | Table 3, p. 17, row 7 |  |
| Heat capacity; _printed: Cp°_ | 42.02 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 9 |  |
| Heat capacity; _printed: Cp°_ | 82.84 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [2] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 13 |  |
| Heat capacity; _printed: Cp°_ | 61.58 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | DFT | [2] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 14 |  |
| Heat capacity; _printed: Cp°_ | 61.63 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [2] Deffrennes 2020 | Table 3, p. 17, row 11 |  |
| Heat capacity; _printed: Cp°_ | 82.84 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [2] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 12 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018). [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015)
2. Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020). [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
