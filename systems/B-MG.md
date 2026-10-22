# B–Mg system

> B–Mg system: 111 accepted literature values (formation 87, phase transition 18, invariant reaction 6) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/B-MG.html · Markdown: https://data.orchid-project.org/systems/B-MG.md

111 accepted literature values from 2 paper(s) (experimental 66, model 45); 0 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/B-MG.json) · [CSV](https://data.orchid-project.org/systems/B-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#B-MG) · [Markdown](https://data.orchid-project.org/systems/B-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 66 |
| model | 45 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 18 |
| formation | 87 |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/B/B-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/B/B-MG.json) · [CALPHAD hull MgB-01Liu-LB](https://data.orchid-project.org/hulls/calphad-sgte/B/B-MG--MgB-01Liu-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the B–Mg system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2423.15 | Gas+Liquid=MgB7 | MgB7: B 0.875, Mg 0.125; gas: B 1.000e-5; liq: B 0.991 | model | [1] Liu 2001 | Table 4, p. 4, row 1 |  |
| 2344.15 | Liquid=MgB7+β-rho | MgB7: B 0.875, Mg 0.125; β-rho: B 1; liq: B 0.996 | model | [1] Liu 2001 | Table 4, p. 4, row 2 |  |
| 2008.15 | Gas+MgB7=MgB4 | MgB7: B 0.875, Mg 0.125; MgB4: B 0.8, Mg 0.2; gas: B 0 | model | [1] Liu 2001 | Table 4, p. 4, row 3 |  |
| 1818.15 | Gas+MgB4=MgB2 | MgB4: B 0.8, Mg 0.2; MgB2: B 0.666667, Mg 0.333333; gas: B 0 | model | [1] Liu 2001 | Table 4, p. 4, row 4 |  |
| 1367.15 | Gas+MgB2=Liquid | MgB2: B 0.666667, Mg 0.333333; gas: B 0; liq: B 0.01 | model | [1] Liu 2001 | Table 4, p. 4, row 5 |  |
| 923.15 | Liquid=hcp+MgB2 | hcp: B 0; MgB2: B 0.666667, Mg 0.333333; liq: B 2.000e-4 | model | [1] Liu 2001 | Table 4, p. 4, row 6 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, B–Mg system (53)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Mg2B | [Mg2B](https://data.orchid-project.org/compounds/Mg2B.html) | -0.01423 kJ/mol-atom ± 8.400e-4 | 298.15 | experimental |  | 24.127 (oqmd-751629) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 11 |  |
| Mg4B |  | -0.01953 kJ/mol-atom ± 0.00139 | 298.15 | experimental |  |  | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 12 |  |
| MgB12 |  | -15.8 per mol-atom | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 20 |  |
| MgB12 |  | -10.1 per mol-atom | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 21 |  |
| MgB12 | [MgB12](https://data.orchid-project.org/compounds/MgB12.html) | -0.01007 kJ/mol-atom ± 9.000e-4 | 298.15 | experimental |  | -0.392 (oqmd-1454219) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 10 |  |
| MgB2 |  | -41.1 per mol-atom ± 2.2 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 1 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -41.1 kJ/mol-atom ± 2.2 | 298 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 1 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -35.9 kJ/mol-atom | 298 | model | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 2 |  |
| MgB2 |  | -35.9 per mol-atom | 298 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 2 |  |
| MgB2 |  | -26.6 per mol-atom ± 10 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 4 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -26.6 kJ/mol-atom ± 10 | 298 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 4 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -24 kJ/mol-atom | 298 | model | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 3 |  |
| MgB2 |  | -24 per mol-atom | 298 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 3 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -18.6 kJ/mol-atom | 298 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 6 |  |
| MgB2 |  | -18.6 per mol-atom | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 6 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -17.2 kJ/mol-atom ± 1.4 | 298 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 5 |  |
| MgB2 |  | -17.2 per mol-atom ± 1.4 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 5 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -0.02666 kJ/mol-atom ± 0.01 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 1 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -0.01855 kJ/mol-atom ± 0.00112 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 7 |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -0.01717 kJ/mol-atom ± 0.00139 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 4 |  |
| MgB20 |  | -15.8 kJ/mol-atom | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 20 |  |
| MgB20 |  | -10.1 kJ/mol-atom | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 21 |  |
| MgB20 |  | -8.5 kJ/mol-atom ± 0.6 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 18 |  |
| MgB20 |  | -8.5 per mol-atom ± 0.6 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 18 |  |
| MgB20 |  | -7.8 kJ/mol-atom | 298 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 19 |  |
| MgB20 |  | -7.8 per mol-atom | 298 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 19 |  |
| MgB4 |  | -29.9 per mol-atom ± 2 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 7 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -29.9 kJ/mol-atom ± 2 | 298 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 7 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -25.5 kJ/mol-atom | 298 | model | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 8 |  |
| MgB4 |  | -25.5 per mol-atom | 298 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 8 |  |
| MgB4 |  | -18.4 per mol-atom | 298 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 9 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -18.4 kJ/mol-atom | 298 | model | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 9 |  |
| MgB4 |  | -17.6 per mol-atom ± 3.8 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 10 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -17.6 kJ/mol-atom ± 3.8 | 298 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 10 |  |
| MgB4 |  | -14.7 per mol-atom | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 12 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -14.7 kJ/mol-atom | 298 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 12 |  |
| MgB4 |  | -14.4 per mol-atom ± 0.8 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 11 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -14.4 kJ/mol-atom ± 0.8 | 298 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 11 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -0.01757 kJ/mol-atom ± 0.00385 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 2 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -0.01473 kJ/mol-atom ± 5.000e-4 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 8 |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -0.01439 kJ/mol-atom ± 7.500e-4 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 5 |  |
| MgB6 |  | -15.5 per mol-atom ± 2.1 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 15 |  |
| MgB6 |  | -13.4 per mol-atom | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 17 |  |
| MgB6 |  | -13.4 per mol-atom ± 0.6 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 16 |  |
| MgB6 | [MgB6](https://data.orchid-project.org/compounds/MgB6.html) | -0.01339 kJ/mol-atom ± 6.000e-4 | 298.15 | experimental |  | 0.227 (oqmd-1454656) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 6 |  |
| MgB6 | [MgB6](https://data.orchid-project.org/compounds/MgB6.html) | -0.01339 kJ/mol-atom ± 3.000e-4 | 298.15 | experimental |  | 0.227 (oqmd-1454656) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 9 |  |
| MgB7 |  | -20.3 per mol-atom ± 1.5 | 298 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 13 |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -20.3 kJ/mol-atom ± 1.5 | 298 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 13 |  |
| MgB7 |  | -18.9 per mol-atom | 298 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 14 |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -18.9 kJ/mol-atom | 298 | model | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 14 |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -15.5 kJ/mol-atom ± 2.1 | 298 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 15 |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -13.4 kJ/mol-atom | 298 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 17 |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -13.4 kJ/mol-atom ± 0.6 | 298 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 16 |  |

## Other properties

### Phase transition (18)

Table: Phase transition, B–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1818 K | 1818 | other: MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 4, p. 5, row 17 |  |
| Phase transition | 1818.15 K | 1818.15 | other | model | [1] Liu 2001 | p. 2 | “Based on the limited experimental data in the literature\[9, 10, 13\], the suggestion by Spear\[6\], and the thermodynamic data of MgB2 and MgB4 in the JANAF table and by SGTE\[18\], the decomposition temperatures of the three intermediate compounds are estimated to be 1545, 1735, and 2150 °C for MgB2, MgB4, and MgB7, respectively.” |
| Phase transition | 1823 K | 1823 | other: MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 4, p. 5, row 18 |  |
| Phase transition | 1888 K | 1888 | other: MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 15 |  |
| Phase transition | 1941 K | 1941 | other: MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 19 |  |
| Phase transition | 1980 K | 1980 | other: MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 4, p. 5, row 16 |  |
| Phase transition | 2008 K | 2008 | other: MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 4, p. 5, row 21 |  |
| Phase transition | 2008.15 K | 2008.15 | other | model | [1] Liu 2001 | p. 2 | “Based on the limited experimental data in the literature\[9, 10, 13\], the suggestion by Spear\[6\], and the thermodynamic data of MgB2 and MgB4 in the JANAF table and by SGTE\[18\], the decomposition temperatures of the three intermediate compounds are estimated to be 1545, 1735, and 2150 °C for MgB2, MgB4, and MgB7, respectively.” |
| Phase transition | 2073 K | 2073 | other: MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 4, p. 5, row 22 |  |
| Phase transition | 2282 K | 2282 | other: MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 4, p. 5, row 20 |  |
| Phase transition | 2318 K | 2318 | other: MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 23 |  |
| Phase transition | 2415 K | 2415 | other: MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 4, p. 5, row 24 |  |
| Phase transition | 2423 K | 2423 | other: MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 4, p. 5, row 25 |  |
| Phase transition | 2423.15 K | 2423.15 | other | model | [1] Liu 2001 | p. 2 | “Based on the limited experimental data in the literature\[9, 10, 13\], the suggestion by Spear\[6\], and the thermodynamic data of MgB2 and MgB4 in the JANAF table and by SGTE\[18\], the decomposition temperatures of the three intermediate compounds are estimated to be 1545, 1735, and 2150 °C for MgB2, MgB4, and MgB7, respectively.” |
| Phase transition | 2464 K | 2464 | other | model | [2] Balducci 2005 | p. 5 | “The new phase MgB20 is stable up to 2464 K: at that temperature it decomposes into a B-rich liquid phase and Mg (g) at 1 bar.” |
| Phase transition | 2464 K | 2464 | other: MgB20; _alloy: Mg 0.047619_ | model | [2] Balducci 2005 | Table 4, p. 5, row 27 |  |
| Phase transition | 2700 K | 2700 | other: MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 28 |  |
| Phase transition | 2759 K | 2759 | other: MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 26 |  |

### Formation (34)

Table: Formation, B–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔfS0298_ | -2.8 per mol-atom ± 0.1 | 298 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 4 |  |
| Entropy of formation; _printed: ΔfS0298_ | -2.8 per mol-atom ± 0.1 | 298 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 4 |  |
| Entropy of formation; _printed: ΔfS0298_ | -2.86 J/mol-atom/K | 298 | MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 3, p. 4, row 2 |  |
| Entropy of formation; _printed: ΔfS0298_ | -2.86 J/mol-atom/K | 298 | MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 3, p. 4, row 2 |  |
| Entropy of formation; _printed: ΔfS0298_ | -4.25 per mol-atom ± 0.5 | 298 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 1 |  |
| Entropy of formation; _printed: ΔfS0298_ | -4.25 per mol-atom ± 0.5 | 298 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 1 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.343 J/mol-atom/K | 298 | MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 3, p. 4, row 3 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.343 J/mol-atom/K | 298 | MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 3, p. 4, row 3 |  |
| Entropy of formation; _printed: ΔfS0298_ | -2.82 J/mol-atom/K | 298 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 5 |  |
| Entropy of formation; _printed: ΔfS0298_ | -2.82 J/mol-atom/K | 298 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 5 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.03 per mol-atom ± 0.01 | 298 | MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 15 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.03 per mol-atom ± 0.01 | 298 | MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 15 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.04 J/mol-atom/K | 298 | MgB20; _alloy: Mg 0.047619_ | model | [2] Balducci 2005 | Table 3, p. 4, row 16 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.04 J/mol-atom/K | 298 | MgB20; _alloy: Mg 0.047619_ | model | [2] Balducci 2005 | Table 3, p. 4, row 16 |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.47 per mol-atom ± 0.1 | 298 | MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 17 |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.47 per mol-atom ± 0.1 | 298 | MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 17 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.655 J/mol-atom/K | 298 | MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 3, p. 4, row 8 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.655 J/mol-atom/K | 298 | MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 3, p. 4, row 8 |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.18 J/mol-atom/K | 298 | MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 3, p. 4, row 7 |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.18 J/mol-atom/K | 298 | MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 3, p. 4, row 7 |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.32 J/mol-atom/K | 298 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005; _cites Pan 1989_ [doi](https://doi.org/10.1007/bf02057252) | Table 3, p. 4, row 10 |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.32 J/mol-atom/K | 298 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005; _cites Pan 1989_ [doi](https://doi.org/10.1007/bf02057252) | Table 3, p. 4, row 10 |  |
| Entropy of formation; _printed: ΔfS0298_ | -3.04 per mol-atom ± 0.5 | 298 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 6 |  |
| Entropy of formation; _printed: ΔfS0298_ | -3.04 per mol-atom ± 0.5 | 298 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 6 |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.84 per mol-atom ± 0.1 | 298 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 9 |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.84 per mol-atom ± 0.1 | 298 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 9 |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.1 J/mol-atom/K | 298 | MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 3, p. 4, row 13 |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.1 J/mol-atom/K | 298 | MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 3, p. 4, row 13 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.02 J/mol-atom/K | 298 | MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005; _cites Pan 1989_ [doi](https://doi.org/10.1007/bf02057252) | Table 3, p. 4, row 14 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.02 J/mol-atom/K | 298 | MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005; _cites Pan 1989_ [doi](https://doi.org/10.1007/bf02057252) | Table 3, p. 4, row 14 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.94 per mol-atom ± 0.5 | 298 | MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 11 |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.94 per mol-atom ± 0.5 | 298 | MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 11 |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.21 J/mol-atom/K | 298 | MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 3, p. 4, row 12 |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.21 J/mol-atom/K | 298 | MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 3, p. 4, row 12 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zi-Kui Liu, Yu Zhong, D.G. Schlom, X.X. Xi, Qi Li, Computational thermodynamic modeling of the Mg-B system, Calphad 25, 299-303 (2001). [doi:10.1016/s0364-5916(01)00050-5](https://doi.org/10.1016/s0364-5916%2801%2900050-5)
2. G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005). [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
