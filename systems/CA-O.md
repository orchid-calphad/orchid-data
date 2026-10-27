# Ca–O system

> Ca–O system: 61 accepted literature values (heat capacity / entropy / enthalpy 26, phase equilibrium 18, formation 14, invariant reaction 2) and 4 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-O.html · Markdown: https://data.orchid-project.org/systems/CA-O.md

61 accepted literature values from 2 paper(s) (experimental 11, model 44, DFT 6); 4 calculated phase diagram(s). 7 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-O.json) · [CSV](https://data.orchid-project.org/systems/CA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-O/CaO-18Lia.json) · [phases (9)](https://data.orchid-project.org/phases/pages/CA-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CA-O.html) · [Markdown](https://data.orchid-project.org/systems/CA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 44 |
| DFT | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 1 |
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

Table: Invariant reactions reported in the literature for the Ca–O system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1103.2 | eutectic: L -> β-Ca + CaO | L: O 0.0098 | model | [1] Deffrennes 2020 | Table 4, p. 21, row 2; `ORC-KDMSKZTUIC` |  |
| 1094.6 | eutectic: L -> β-Ca + CaO | L: O 0.017 | model | [1] Deffrennes 2020 | Table 4, p. 21, row 1; `ORC-LF5WICU4A5` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ca–O system (14)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -317.55 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [1] Deffrennes 2020; _cites Chase 1998_ | Table 3, p. 17, row 6; `ORC-FDK7VGPM2Z.234c60` |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -317.55 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 3; `ORC-YHMSI6IKE4.81e7a6` |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -317.3 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [1] Deffrennes 2020 | Table 3, p. 17, row 1; `ORC-N6RZ52LOV5.b9b0c1` |  |
| CaO(cr) |  | -317.3 kJ/mol-atom | 298.15 | DFT |  |  | [1] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 5; `ORC-WIQAAOJS7J.6edd6d` |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -317 kJ/mol-atom | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 2; `ORC-MOABLTWFHR.fd3a6b` |  |
| CaO(cr) | [CaO](https://data.orchid-project.org/compounds/CaO.html) | -317 kJ/mol-atom ± 0.75 | 298.15 | model | -318.981 (mp-aaaaadwf) | -308.324 (oqmd-1443085) | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 4; `ORC-XQRAM3624L` |  |
| CaO(liq-am) |  | -300.45 kJ/mol-atom | 298.15 | model |  |  | [1] Deffrennes 2020 | Table 3, p. 17, row 7; `ORC-S7YOHYNZRJ.30327b` |  |
| CaO(liq-am) |  | -282.8 kJ/mol-atom | 298.15 | model |  |  | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 8; `ORC-BWUGY4RCBI.19f6e9` |  |
| CaO(liq-am) |  | -278.65 kJ/mol-atom | 298.15 | model |  |  | [1] Deffrennes 2020; _cites Chase 1998_ | Table 3, p. 17, row 10; `ORC-2RQQARKD4D.a020f1` |  |
| CaO(liq-am) |  | -277.8 kJ/mol-atom | 298.15 | model |  |  | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 9; `ORC-SAKKEEI5SE.2d0105` |  |
| CaO2(cr) | [CaO2](https://data.orchid-project.org/compounds/CaO2.html) | -219.667 kJ/mol-atom | 298.15 | model | -212.9 (mp-aaabkddr) | -219.972 (oqmd-1367693) | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 13; `ORC-2XXL6EGLXQ.a44990` |  |
| CaO2(cr) | [CaO2](https://data.orchid-project.org/compounds/CaO2.html) | -217.567 kJ/mol-atom | 298.15 | model | -212.9 (mp-aaabkddr) | -219.972 (oqmd-1367693) | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 12; `ORC-IOMQXHHZHX.39b429` |  |
| CaO2(cr) |  | -216.033 kJ/mol-atom | 298.15 | DFT |  |  | [1] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 14; `ORC-32IJWP2DCH.19497d` |  |
| CaO2(cr) | [CaO2](https://data.orchid-project.org/compounds/CaO2.html) | -216.033 kJ/mol-atom | 298.15 | model | -212.9 (mp-aaabkddr) | -219.972 (oqmd-1367693) | [1] Deffrennes 2020 | Table 3, p. 17, row 11; `ORC-EONGZNVMF4.e5cd6e` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ca–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 3221.8 K | 3221.8 | congruent transformation | model | [2] Liang 2018 | p. 14; `ORC-3CYZ26RQQ3` | “However, in the binary Ca-O system the congruent melting point of CaO occurs at 3221.8 K.” |

### Phase equilibrium (18)

Table: Phase equilibrium, Ca–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 2843 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Kanolt 1913_ | Table 2, p. 5, row 1; `ORC-JTH2DUCWQU` |  |
| Phase composition |  | 2845 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [2] Liang 2018; _cites Factsage 2017_ | Table 2, p. 5, row 16; `ORC-TALCCE2VFA` |  |
| Phase composition |  | 2849 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Schumacher 1926_ [doi](https://doi.org/10.1021/ja01413a013) | Table 2, p. 5, row 2; `ORC-2QKP2SE3D3` |  |
| Phase composition |  | 2863 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Noguchi 1967_ [doi](https://doi.org/10.1016/0038-092x%2867%2990022-9) | Table 2, p. 5, row 6; `ORC-KVGJUYFZCT` |  |
| Phase composition |  | 2886 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [2] Liang 2018; _cites Hlavac 1982_ [doi](https://doi.org/10.1351/pac198254030681) | Table 2, p. 5, row 12; `ORC-4PKTBKLUO5` |  |
| Phase composition |  | 2886 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [2] Liang 2018; _cites Wriedt 1985_ [doi](https://doi.org/10.1007/bf02880517) | Table 2, p. 5, row 13; `ORC-GSCUINQ6J2` |  |
| Phase composition |  | 2890 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Panek 1979_ | Table 2, p. 5, row 9; `ORC-BWRY4NHF7I` |  |
| Phase composition |  | 2893 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites OlShanskil 1958_ | Table 2, p. 5, row 3; `ORC-BBLAGB7W5S` |  |
| Phase composition |  | 2898 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Doman 1963_ | Table 2, p. 5, row 4; `ORC-2AEEFYPT74` |  |
| Phase composition |  | 2900 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [2] Liang 2018; _cites Kubaschewski 1993_ | Table 2, p. 5, row 14; `ORC-CYC5AGHCVA` |  |
| Phase composition |  | 3172 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Yamada 1986_ [doi](https://doi.org/10.1111/j.1151-2916.1986.tb07350.x) | Table 2, p. 5, row 10; `ORC-JBWMFPXF4V` |  |
| Phase composition |  | 3172 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [2] Liang 2018; _cites SGTE 2013_ | Table 2, p. 5, row 17; `ORC-OANJNOVFFT` |  |
| Phase composition |  | 3173 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Traverse 1969_ | Table 2, p. 5, row 8; `ORC-OAZIQKIZCE` |  |
| Phase composition |  | 3183 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Foex 1965_ [doi](https://doi.org/10.1016/0038-092x%2865%2990162-3) | Table 2, p. 5, row 5; `ORC-UL465S5JRR` |  |
| Phase composition |  | 3200 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [2] Liang 2018; _cites Chase 1998_ | Table 2, p. 5, row 15; `ORC-OYDRQ7PHBU` |  |
| Phase composition |  | 3222 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | model | [2] Liang 2018 | Table 2, p. 5, row 18; `ORC-GEYDFCEQZG` |  |
| Phase composition |  | 3222 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Manara 2014_ | Table 2, p. 5, row 11; `ORC-VLFH7CZPDU` |  |
| Phase composition |  | 3223 | congruent melting: CaO; _liquid: O 0.5; CaO: O 0.5_ | experimental | [2] Liang 2018; _cites Foex 1968_ | Table 2, p. 5, row 7; `ORC-C6HW6G5FK3` |  |

### Heat capacity / entropy / enthalpy (26)

Table: Heat capacity / entropy / enthalpy, Ca–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S°_ | 19.105 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Chase 1998_ | Table 3, p. 17, row 6; `ORC-FDK7VGPM2Z.f0a714` |  |
| Entropy; _printed: S°_ | 19.05 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 2; `ORC-MOABLTWFHR.008a14` |  |
| Entropy; _printed: S°_ | 20.175 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020 | Table 3, p. 17, row 1; `ORC-N6RZ52LOV5.0e83c8` |  |
| Entropy; _printed: S°_ | 20.175 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | DFT | [1] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 5; `ORC-WIQAAOJS7J.0c35da` |  |
| Entropy; _printed: S°_ | 18.875 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 3; `ORC-YHMSI6IKE4.596c0f` |  |
| Entropy; _printed: S°_ | 31.16 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Chase 1998_ | Table 3, p. 17, row 10; `ORC-2RQQARKD4D.665e33` |  |
| Entropy; _printed: S°_ | 29.345 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 8; `ORC-BWUGY4RCBI.61b23b` |  |
| Entropy; _printed: S°_ | 20.175 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020 | Table 3, p. 17, row 7; `ORC-S7YOHYNZRJ.1c4369` |  |
| Entropy; _printed: S°_ | 32.845 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 9; `ORC-SAKKEEI5SE.3f9ad1` |  |
| Entropy; _printed: S°_ | 27.8933 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 13; `ORC-2XXL6EGLXQ.c1edf5` |  |
| Entropy; _printed: S°_ | 19.8667 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | DFT | [1] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 14; `ORC-32IJWP2DCH.ef3588` |  |
| Entropy; _printed: S°_ | 19.8667 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [1] Deffrennes 2020 | Table 3, p. 17, row 11; `ORC-EONGZNVMF4.0b9fce` |  |
| Entropy; _printed: S°_ | 27.8933 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 12; `ORC-IOMQXHHZHX.057938` |  |
| Heat capacity; _printed: Cp°_ | 21.06 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Chase 1998_ | Table 3, p. 17, row 6; `ORC-FDK7VGPM2Z.5cd21e` |  |
| Heat capacity; _printed: Cp°_ | 21.025 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 2; `ORC-MOABLTWFHR.66cf49` |  |
| Heat capacity; _printed: Cp°_ | 21.365 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020 | Table 3, p. 17, row 1; `ORC-N6RZ52LOV5.1da2a7` |  |
| Heat capacity; _printed: Cp°_ | 21.365 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | DFT | [1] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 5; `ORC-WIQAAOJS7J.2664ef` |  |
| Heat capacity; _printed: Cp°_ | 21.01 J/mol-atom/K | 298.15 | CaO(cr); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 3; `ORC-YHMSI6IKE4.236295` |  |
| Heat capacity; _printed: Cp°_ | 21.06 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Chase 1998_ | Table 3, p. 17, row 10; `ORC-2RQQARKD4D.13f70e` |  |
| Heat capacity; _printed: Cp°_ | 21.02 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 8; `ORC-BWUGY4RCBI.9258e5` |  |
| Heat capacity; _printed: Cp°_ | 21.365 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020 | Table 3, p. 17, row 7; `ORC-S7YOHYNZRJ.e6a53b` |  |
| Heat capacity; _printed: Cp°_ | 21.01 J/mol-atom/K | 298.15 | CaO(liq-am); _alloy: O 0.5_ | model | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 9; `ORC-SAKKEEI5SE.632f2b` |  |
| Heat capacity; _printed: Cp°_ | 27.6133 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [1] Deffrennes 2020; _cites Lindberg 2009_ [doi](https://doi.org/10.1016/j.jct.2009.04.018) | Table 3, p. 17, row 13; `ORC-2XXL6EGLXQ.cf9c28` |  |
| Heat capacity; _printed: Cp°_ | 20.5267 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | DFT | [1] Deffrennes 2020; _cites Pisch_ | Table 3, p. 17, row 14; `ORC-32IJWP2DCH.821da6` |  |
| Heat capacity; _printed: Cp°_ | 20.5433 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [1] Deffrennes 2020 | Table 3, p. 17, row 11; `ORC-EONGZNVMF4.321b1e` |  |
| Heat capacity; _printed: Cp°_ | 27.6133 J/mol-atom/K | 298.15 | CaO2(cr); _alloy: O 0.666667_ | model | [1] Deffrennes 2020; _cites Liang 2018_ [doi](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | Table 3, p. 17, row 12; `ORC-IOMQXHHZHX.013f5e` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020). [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764)
2. Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018). [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
