# Cs–O system

> Cs–O system: 171 accepted literature values (crystal structure 68, heat capacity / entropy / enthalpy 54, formation 39, phase transition 9) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CS-O.html · Markdown: https://data.orchid-project.org/systems/CS-O.md

171 accepted literature values from 1 paper(s) (experimental 50, model 36, DFT 73, unspecified 12); 1 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CS-O.json) · [CSV](https://data.orchid-project.org/systems/CS-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CS-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CS-O/CsO-15Gue.json) · [phases (15)](https://data.orchid-project.org/phases/pages/CS-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CS-O.html) · [Markdown](https://data.orchid-project.org/systems/CS-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 50 |
| model | 36 |
| DFT | 73 |
| unspecified | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 9 |
| formation | 39 |
| heat capacity / entropy / enthalpy | 54 |
| crystal structure | 68 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CsO-15Gue.tdb | C. Gueneau, J.-L. Fleche, Calphad, 49, 67-78(2015). [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) | `5219d7e34c2f9d747da82c88e4744644fccf0b1155da2778af483725a55b4ebe` | [viewer](https://orchid-project.org/phase-diagrams/#CS-O/CsO-15Gue.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CsO-15Gue.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CsO-15Gue.tdb | 325.17 | ION (x(O) 0.19439) + CS4O (x(O) 0.2) + CS3O (x(O) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CS/CS-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CS/CS-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cs–O system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 262.7 | peritectic: Cs7O2 = Cs7O + Cs3O |  | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | p. 2; `ORC-4X3TF7HV74` | “Their observation of a transition at 262.7 K between 20 and 25 at% O implies that Cs7O2 decomposes by a peritectic reaction into Cs7O and Cs3O.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cs–O system (39)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Cs2O |  | -122.367 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 10; `ORC-FTGB7HG7ZE.9b3869` |  |
| Cs2O |  | -117.4 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 12; `ORC-BAOM3I77FZ.ef554b` |  |
| Cs2O |  | -116.933 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 11; `ORC-NT2QGLN5HK.e8dfa9` |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -116.133 kJ/mol-atom | 298.15 | experimental | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 18; `ORC-43ZXOO6TFO.5bfa0b` |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | unspecified | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 16; `ORC-2ISCIC7H7H.f0f769` |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | model | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015 | Table 5, p. 7, row 19; `ORC-55RRRCHTNI.a09d8d` |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | unspecified | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 14; `ORC-KXPDBPFE4W.ebb2e4` |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | model | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15; `ORC-QZUGH5QMOW.60d01e` |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | experimental | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Settle 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990179-7) | Table 5, p. 7, row 17; `ORC-VICVK7W5MI.4eb1cb` |  |
| Cs2O2 |  | -131.025 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 21; `ORC-QY5KKD4K23.6461e2` |  |
| Cs2O2 |  | -129.05 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 22; `ORC-LXSQ6CEKAC.47bf6a` |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -124.4 kJ/mol-atom | 298.15 | unspecified | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 25; `ORC-55ILDIWZLJ.c51754` |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -110 kJ/mol-atom | 298.15 | model | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24; `ORC-4VILVIHB5A.7adb97` |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -110 kJ/mol-atom | 298.15 | unspecified | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 23; `ORC-QDOOQ242QY.21c1ef` |  |
| Cs2O2 |  | -97.95 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 20; `ORC-UCYL5M5YMQ.b47829` |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -97.5 kJ/mol-atom | 298.15 | model | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015 | Table 5, p. 7, row 27; `ORC-LOSOBGLB6R.1b9c29` |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -96.625 kJ/mol-atom | 298.15 | experimental | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 26; `ORC-RAE3344I7N.9f6f6d` |  |
| Cs3O |  | -92.575 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 8; `ORC-ZF7CU7QGZE.7c760d` |  |
| Cs3O | [Cs3O](https://data.orchid-project.org/compounds/Cs3O.html) | -85.475 kJ/mol-atom | 298.15 | model | -89.555 (mp-aaabdavm) | -85.555 (oqmd-2013713) | [1] Guéneau 2015 | Table 5, p. 7, row 9; `ORC-OGL6BPJQE3.4f5cf9` |  |
| Cs3O |  | -74.125 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 7; `ORC-TSATJTWL4X.039973` |  |
| Cs4O |  | -67.84 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 4; `ORC-XIB343EK4O.ebb941` |  |
| Cs4O |  | -59.64 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 3; `ORC-IDEY4NU7GH.da045f` |  |
| Cs7O | [Cs7O](https://data.orchid-project.org/compounds/Cs7O.html) | -42.5625 kJ/mol-atom | 298.15 | model | -44.374 (mp-aaabfyzf) | -43.119 (oqmd-1632) | [1] Guéneau 2015 | Table 5, p. 7, row 2; `ORC-74PDWOUQ6D.cfe15c` |  |
| Cs7O |  | -37.475 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 1; `ORC-NGZLBXOCTJ.f74634` |  |
| Cs7O2 |  | -75.8111 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 6; `ORC-5JTV2YD5ZE.d14fb0` |  |
| Cs7O2 |  | -64 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 5; `ORC-SWEHTSC4LB.e1d05d` |  |
| CsO2 |  | -129.533 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 29; `ORC-63T6UUMOMP.41ed7e` |  |
| CsO2 |  | -117.067 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 30; `ORC-HSFBTMJG4X.cbe28d` |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -95.4 kJ/mol-atom | 298.15 | model | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32; `ORC-I3KHTYFGXV.668aa4` |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -95.4 kJ/mol-atom | 298.15 | unspecified | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 33; `ORC-SZXWPYYEN4.46a7ac` |  |
| CsO2 |  | -84.2667 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 28; `ORC-SVOB5GY4NR.a00d38` |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -80.4667 kJ/mol-atom | 298.15 | model | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015 | Table 5, p. 7, row 35; `ORC-7E7CJ5YOFI.290ec1` |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -78.3 kJ/mol-atom | 298.15 | experimental | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 34; `ORC-636TFSTTTX.9fd6f2` |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -77.7 kJ/mol-atom | 298.15 | unspecified | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 31; `ORC-YWJF45XPKP.be9b5b` |  |
| CsO3 |  | -71 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 36; `ORC-QEFWZ76HIE.df403f` |  |
| CsO3 | [CsO3](https://data.orchid-project.org/compounds/CsO3.html) | -68.15 kJ/mol-atom | 298.15 | model | -62.92 (mp-aaacprqh) | -84.786 (oqmd-6357) | [1] Guéneau 2015 | Table 5, p. 7, row 38; `ORC-WWB3YGRQ7H.7cd638` |  |
| CsO3 |  | -50.175 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 37; `ORC-WLXHDHAIDP.a4c280` |  |
| UNKNOWN |  | -682.3 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 6; `ORC-5JTV2YD5ZE.0e3914` |  |
| UNKNOWN |  | -576 kJ/mol (basis unstated) | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 5; `ORC-SWEHTSC4LB.872b13` |  |

## Other properties

### Phase transition (9)

Table: Phase transition, Cs–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 276 K | 276 | congruent transformation | experimental | [1] Guéneau 2015; _cites Brauer 1947_ [doi](https://doi.org/10.1002/zaac.19472550110) | p. 2; `ORC-B5SGBQWVUS.2fb522` | “In the Cs-Cs2O part, an eutectic reaction (liquid1⁄4 Cs bccþ Cs7O) was measured by Brauer \[10\] at 271 K and the compound Cs7O was found to melt congruently at 276 K.” |
| Phase transition | 326 K | 326 | Cs4O = liquid + Cs3O | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | p. 2; `ORC-CXQ3SVKDBS` | “Cs4O was found to decompose at 326 K into liquid and Cs3O.” |
| Phase transition | 343 K | 343 | other | experimental | [1] Guéneau 2015; _cites Cordfunke 1990_ | p. 2; `ORC-K3PHFC2Y6E.1aa8c7` | “The largest uncertainties were on both the melting point of Cs2O2 (863 K) and the decomposition of CsO3 (343 K), which were reported on the phase diagrams successively by Knights and Phillips \[11\], Cordfunke and Konings \[8\].” |
| Phase transition | 437 K | 437 | Cs3O = liquid + Cs2O | experimental | [1] Guéneau 2015 | p. 2; `ORC-M73HP4OOV6` | “And Cs3O was observed to decompose into liquid and Cs2O at 437 K.” |
| Phase transition | 705 K | 705 | CsO2 | experimental | [1] Guéneau 2015; _cites Blumenthal 1933_ | p. 2; `ORC-KM7ZYQFNR5.1d1eac` | “The melting point of CsO2 was estimated at 705 K by Blumenthal and Centerszwer \[12\] and later reported as 723 K by Vol'nov \[13\].” |
| Phase transition | 723 K | 723 | CsO2 | experimental | [1] Guéneau 2015; _cites Volnov 1967_ | p. 2; `ORC-KM7ZYQFNR5.fb7253` | “The melting point of CsO2 was estimated at 705 K by Blumenthal and Centerszwer \[12\] and later reported as 723 K by Vol'nov \[13\].” |
| Phase transition | 723 K | 723 | CsO2 | experimental | [1] Guéneau 2015; _cites Volnov 1967_ | p. 2; `ORC-NYL5LJSQBJ` | “CsO2 was observed to start to melt at 723 K in agreement with Vol'nov \[13\].” |
| Phase transition | 768 K | 768 | Cs2O | experimental | [1] Guéneau 2015; _cites Touzain 1976_ [doi](https://doi.org/10.1007/bf01909410) | p. 2; `ORC-NSOAQSEFZC` | “The melting point of Cs2O was found at 768 K by Touzain \[14\] using DTA.” |
| Phase transition | 863 K | 863 | Cs2O2 | experimental | [1] Guéneau 2015; _cites Cordfunke 1990_ | p. 2; `ORC-K3PHFC2Y6E.039518` | “The largest uncertainties were on both the melting point of Cs2O2 (863 K) and the decomposition of CsO3 (343 K), which were reported on the phase diagrams successively by Knights and Phillips \[11\], Cordfunke and Konings \[8\].” |

### Heat capacity / entropy / enthalpy (54)

Table: Heat capacity / entropy / enthalpy, Cs–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 16; `ORC-2ISCIC7H7H.fc2720` |  |
| Entropy; _printed: S0 298.15 K_ | 38.2 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 18; `ORC-43ZXOO6TFO.9a5ff5` |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 19; `ORC-55RRRCHTNI.4399ea` |  |
| Entropy; _printed: S0 298.15 K_ | 52.4333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 10; `ORC-FTGB7HG7ZE.3a3f9f` |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 14; `ORC-KXPDBPFE4W.bf77cc` |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Flotow 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990256-0) | Table 5, p. 7, row 13; `ORC-LF2XK4HKT2.58f977` |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15; `ORC-QZUGH5QMOW.12e4b1` |  |
| Entropy; _printed: S0 298.15 K_ | 48.9 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Settle 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990179-7) | Table 5, p. 7, row 17; `ORC-VICVK7W5MI.87e1e2` |  |
| Entropy; _printed: S0 298.15 K_ | 45 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24; `ORC-4VILVIHB5A.c22e72` |  |
| Entropy; _printed: S0 298.15 K_ | 36.075 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 25; `ORC-55ILDIWZLJ.380dd3` |  |
| Entropy; _printed: S0 298.15 K_ | 53.85 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 27; `ORC-LOSOBGLB6R.710382` |  |
| Entropy; _printed: S0 298.15 K_ | 43.4 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 23; `ORC-QDOOQ242QY.79478b` |  |
| Entropy; _printed: S0 298.15 K_ | 53.325 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 26; `ORC-RAE3344I7N.7e1d0f` |  |
| Entropy; _printed: S0 298.15 K_ | 40.925 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 20; `ORC-UCYL5M5YMQ.2be18e` |  |
| Entropy; _printed: S0 298.15 K_ | 65.45 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 9; `ORC-OGL6BPJQE3.b1a660` |  |
| Entropy; _printed: S0 298.15 K_ | 59.25 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 7; `ORC-TSATJTWL4X.de9739` |  |
| Entropy; _printed: S0 298.15 K_ | 60.86 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 3; `ORC-IDEY4NU7GH.6d36ca` |  |
| Entropy; _printed: S0 298.15 K_ | 72.84 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 4; `ORC-XIB343EK4O.441b7e` |  |
| Entropy; _printed: S0 298.15 K_ | 78.075 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 2; `ORC-74PDWOUQ6D.6cd4d8` |  |
| Entropy; _printed: S0 298.15 K_ | 77.1625 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 1; `ORC-NGZLBXOCTJ.89404d` |  |
| Entropy; _printed: S0 298.15 K_ | 69.0444 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 6; `ORC-5JTV2YD5ZE.0a54c3` |  |
| Entropy; _printed: S0 298.15 K_ | 60.5556 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5; `ORC-SWEHTSC4LB.6455b7` |  |
| Entropy; _printed: S0 298.15 K_ | 57.0667 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 34; `ORC-636TFSTTTX.fadc13` |  |
| Entropy; _printed: S0 298.15 K_ | 54.4 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 35; `ORC-7E7CJ5YOFI.262d70` |  |
| Entropy; _printed: S0 298.15 K_ | 47.3333 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32; `ORC-I3KHTYFGXV.dfb796` |  |
| Entropy; _printed: S0 298.15 K_ | 49.1667 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 28; `ORC-SVOB5GY4NR.a974c5` |  |
| Entropy; _printed: S0 298.15 K_ | 46.6 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 33; `ORC-SZXWPYYEN4.0c40e3` |  |
| Entropy; _printed: S0 298.15 K_ | 45.5 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 31; `ORC-YWJF45XPKP.46c247` |  |
| Entropy; _printed: S0 298.15 K_ | 36.175 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 36; `ORC-QEFWZ76HIE.a5828c` |  |
| Entropy; _printed: S0 298.15 K_ | 42.15 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 38; `ORC-WWB3YGRQ7H.c328a5` |  |
| Entropy; _printed: S0_ | 621.4 J/mol (basis unstated)/K | 298.15 | UNKNOWN | model | [1] Guéneau 2015 | Table 5, p. 7, row 6; `ORC-5JTV2YD5ZE.5baff2` |  |
| Entropy; _printed: S0_ | 545 J/mol (basis unstated)/K | 298.15 | UNKNOWN | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5; `ORC-SWEHTSC4LB.4963ce` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.2333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 19; `ORC-55RRRCHTNI.9b85fb` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 24.9333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 10; `ORC-FTGB7HG7ZE.e76623` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.3333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Flotow 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990256-0) | Table 5, p. 7, row 13; `ORC-LF2XK4HKT2.754378` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.3333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15; `ORC-QZUGH5QMOW.0132bb` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 23.75 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24; `ORC-4VILVIHB5A.90bdb7` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 23.375 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 27; `ORC-LOSOBGLB6R.e609e2` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 27.75 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 20; `ORC-UCYL5M5YMQ.7ecf28` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.675 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 9; `ORC-OGL6BPJQE3.e85834` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.7 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 7; `ORC-TSATJTWL4X.f55708` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 27.28 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 3; `ORC-IDEY4NU7GH.5fcb90` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.74 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 4; `ORC-XIB343EK4O.aff151` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.3 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 2; `ORC-74PDWOUQ6D.656ab0` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.3125 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 1; `ORC-NGZLBXOCTJ.51d7f5` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.6778 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 6; `ORC-5JTV2YD5ZE.92926b` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.6889 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5; `ORC-SWEHTSC4LB.f524bc` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 22.8167 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 35; `ORC-7E7CJ5YOFI.424614` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.3 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32; `ORC-I3KHTYFGXV.658f42` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 22.7333 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 28; `ORC-SVOB5GY4NR.1b1e5a` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 21.075 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 36; `ORC-QEFWZ76HIE.1459c2` |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 21.05 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 38; `ORC-WWB3YGRQ7H.eb34af` |  |
| Heat capacity; _printed: Cp0_ | 231.1 J/mol (basis unstated)/K | 298.15 | UNKNOWN | model | [1] Guéneau 2015 | Table 5, p. 7, row 6; `ORC-5JTV2YD5ZE.62559e` |  |
| Heat capacity; _printed: Cp0_ | 231.2 J/mol (basis unstated)/K | 298.15 | UNKNOWN | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5; `ORC-SWEHTSC4LB.f73a15` |  |

### Crystal structure (68)

Table: Crystal structure, Cs–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 17.88 Å |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6; `ORC-SFGE2KD3UF.afdb16` |  |
| Lattice a | 4.33 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 10; `ORC-AVYJPJTBJW.4fa99b` |  |
| Lattice a | 4.232 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 11; `ORC-IVMWQERCQY.964938` |  |
| Lattice a | 8.899 Å |  | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 8; `ORC-LI3V72VRVT.b85fb5` |  |
| Lattice a | 16.414 Å |  | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 2; `ORC-NLCV64A6NE.86d5c4` |  |
| Lattice a | 4.46 Å |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13; `ORC-RU4WU2KPH6.c0865d` |  |
| Lattice a | 9.031 Å |  | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 15; `ORC-K3Y3GW5UX7.60148f` |  |
| Lattice a | 6.836 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18; `ORC-4NWNQ4Q5Z2.87b48d` |  |
| Lattice a | 7.008 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17; `ORC-CRXYSV7HNB.1f348b` |  |
| Lattice a | 17.027 Å |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4; `ORC-UPX3Q4HYB2.6566cf` |  |
| Lattice a | 17.61 Å | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5; `ORC-PPDRWC6GG6.220d10` |  |
| Lattice a | 4.269 Å | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 9; `ORC-7CWATBOSWY.eaaae6` |  |
| Lattice a | 8.78 Å | 298.15 | Cs3O; _alloy: O 0.25_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 7; `ORC-33JCZL4AEZ.76c81e` |  |
| Lattice a | 16.393 Å | 298.15 | Cs7O; _alloy: O 0.125_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 1; `ORC-3FOKF5JVGB.97f6b1` |  |
| Lattice a | 4.322 Å | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12; `ORC-DNPONZO2B2.ffafd7` |  |
| Lattice a | 8.924 Å | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 14; `ORC-I27WS7JY3N.073974` |  |
| Lattice a | 6.709 Å | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16; `ORC-45ZWEMCXX6.d4f08f` |  |
| Lattice a | 16.833 Å | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3; `ORC-G3CIGRWYWI.9d0c3d` |  |
| Lattice b | 9.377 Å |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6; `ORC-SFGE2KD3UF.abe297` |  |
| Lattice b | 7.644 Å |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13; `ORC-RU4WU2KPH6.95193b` |  |
| Lattice b | 6.358 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18; `ORC-4NWNQ4Q5Z2.3e7e4a` |  |
| Lattice b | 6.556 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17; `ORC-CRXYSV7HNB.5d9810` |  |
| Lattice b | 20.882 Å |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4; `ORC-UPX3Q4HYB2.e16f4f` |  |
| Lattice b | 9.218 Å | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5; `ORC-PPDRWC6GG6.009374` |  |
| Lattice b | 7.517 Å | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12; `ORC-DNPONZO2B2.e8b0fc` |  |
| Lattice b | 6.244 Å | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16; `ORC-45ZWEMCXX6.c92e60` |  |
| Lattice b | 20.569 Å | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3; `ORC-G3CIGRWYWI.04bef1` |  |
| Lattice c | 24.466 Å |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6; `ORC-SFGE2KD3UF.b4ed44` |  |
| Lattice c | 22.491 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 10; `ORC-AVYJPJTBJW.3d334b` |  |
| Lattice c | 18.74 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 11; `ORC-IVMWQERCQY.49c7a8` |  |
| Lattice c | 7.627 Å |  | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 8; `ORC-LI3V72VRVT.83d8d8` |  |
| Lattice c | 9.357 Å |  | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 2; `ORC-NLCV64A6NE.ea7267` |  |
| Lattice c | 6.495 Å |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13; `ORC-RU4WU2KPH6.545894` |  |
| Lattice c | 14.906 Å |  | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 15; `ORC-K3Y3GW5UX7.da9dca` |  |
| Lattice c | 9.231 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18; `ORC-4NWNQ4Q5Z2.7e323a` |  |
| Lattice c | 9.42 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17; `ORC-CRXYSV7HNB.a9c12d` |  |
| Lattice c | 12.643 Å |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4; `ORC-UPX3Q4HYB2.7040b4` |  |
| Lattice c | 24.047 Å | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5; `ORC-PPDRWC6GG6.37316b` |  |
| Lattice c | 18.82 Å | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 9; `ORC-7CWATBOSWY.6a6dca` |  |
| Lattice c | 7.52 Å | 298.15 | Cs3O; _alloy: O 0.25_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 7; `ORC-33JCZL4AEZ.9bcd57` |  |
| Lattice c | 9.193 Å | 298.15 | Cs7O; _alloy: O 0.125_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 1; `ORC-3FOKF5JVGB.11bfc7` |  |
| Lattice c | 6.43 Å | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12; `ORC-DNPONZO2B2.375891` |  |
| Lattice c | 14.652 Å | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 14; `ORC-I27WS7JY3N.f92e9a` |  |
| Lattice c | 8.997 Å | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16; `ORC-45ZWEMCXX6.85884f` |  |
| Lattice c | 12.4 Å | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3; `ORC-G3CIGRWYWI.b910b3` |  |
| lattice beta | 100.29 not_printed |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6; `ORC-SFGE2KD3UF.d1b408` |  |
| lattice beta | 122.41 not_printed |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18; `ORC-4NWNQ4Q5Z2.41b7f3` |  |
| lattice beta | 123.61 not_printed |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17; `ORC-CRXYSV7HNB.873fb9` |  |
| lattice beta | 100.14 not_printed | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5; `ORC-PPDRWC6GG6.5f48f1` |  |
| lattice beta | 120.85 not_printed | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16; `ORC-45ZWEMCXX6.45fee7` |  |
| lattice v | 4035.98 Å³ |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6; `ORC-SFGE2KD3UF.d99a0e` |  |
| lattice v | 365.2 Å³ |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 10; `ORC-AVYJPJTBJW.c6b0bc` |  |
| lattice v | 290.57 Å³ |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 11; `ORC-IVMWQERCQY.668c87` |  |
| lattice v | 523.17 Å³ |  | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 8; `ORC-LI3V72VRVT.cca07a` |  |
| lattice v | 2183.46 Å³ |  | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 2; `ORC-NLCV64A6NE.39b8a7` |  |
| lattice v | 221.43 Å³ |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13; `ORC-RU4WU2KPH6.4258f8` |  |
| lattice v | 1215.72 Å³ |  | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 15; `ORC-K3Y3GW5UX7.bf2260` |  |
| lattice v | 338.7 Å³ |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18; `ORC-4NWNQ4Q5Z2.c37984` |  |
| lattice v | 360.51 Å³ |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17; `ORC-CRXYSV7HNB.7a0690` |  |
| lattice v | 4496.23 Å³ |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4; `ORC-UPX3Q4HYB2.31cc47` |  |
| lattice v | 3842.55 Å³ | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5; `ORC-PPDRWC6GG6.8146bd` |  |
| lattice v | 297.03 Å³ | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 9; `ORC-7CWATBOSWY.68550c` |  |
| lattice v | 502.04 Å³ | 298.15 | Cs3O; _alloy: O 0.25_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 7; `ORC-33JCZL4AEZ.a3f614` |  |
| lattice v | 2139.46 Å³ | 298.15 | Cs7O; _alloy: O 0.125_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 1; `ORC-3FOKF5JVGB.e3d4e9` |  |
| lattice v | 208.9 Å³ | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12; `ORC-DNPONZO2B2.2477ae` |  |
| lattice v | 1166.85 Å³ | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 14; `ORC-I27WS7JY3N.6d83dc` |  |
| lattice v | 323.56 Å³ | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16; `ORC-45ZWEMCXX6.1f2b39` |  |
| lattice v | 4293.35 Å³ | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3; `ORC-G3CIGRWYWI.1713f9` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015). [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002)

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
