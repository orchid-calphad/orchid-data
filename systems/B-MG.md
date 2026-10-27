# B–Mg system

> B–Mg system: 93 accepted literature values (formation 70, phase transition 17, invariant reaction 6) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/B-MG.html · Markdown: https://data.orchid-project.org/systems/B-MG.md

93 accepted literature values from 2 paper(s) (experimental 56, model 37); 0 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/B-MG.json) · [CSV](https://data.orchid-project.org/systems/B-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#B-MG) · [phases (10)](https://data.orchid-project.org/phases/pages/B-MG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/B-MG.html) · [Markdown](https://data.orchid-project.org/systems/B-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 56 |
| model | 37 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 17 |
| formation | 70 |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/B/B-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/B/B-MG.json) · [CALPHAD hull MgB-01Liu-LB](https://data.orchid-project.org/hulls/calphad-sgte/B/B-MG--MgB-01Liu-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the B–Mg system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2423.15 | Gas+Liquid=MgB7 | MgB7: B 0.875, Mg 0.125; gas: B 1.000e-5; liq: B 0.991 | model | [1] Liu 2001 | Table 4, p. 4, row 1; `ORC-CUO65K6ZCK` |  |
| 2344.15 | Liquid=MgB7+β-rho | MgB7: B 0.875, Mg 0.125; β-rho: B 1; liq: B 0.996 | model | [1] Liu 2001 | Table 4, p. 4, row 2; `ORC-MX46FKHWGX` |  |
| 2008.15 | Gas+MgB7=MgB4 | MgB7: B 0.875, Mg 0.125; MgB4: B 0.8, Mg 0.2; gas: B 0 | model | [1] Liu 2001 | Table 4, p. 4, row 3; `ORC-X2UR6INRG3` |  |
| 1818.15 | Gas+MgB4=MgB2 | MgB4: B 0.8, Mg 0.2; MgB2: B 0.666667, Mg 0.333333; gas: B 0 | model | [1] Liu 2001 | Table 4, p. 4, row 4; `ORC-JED333DEWR` |  |
| 1367.15 | Gas+MgB2=Liquid | MgB2: B 0.666667, Mg 0.333333; gas: B 0; liq: B 0.01 | model | [1] Liu 2001 | Table 4, p. 4, row 5; `ORC-IZVODMZNRX` |  |
| 923.15 | Liquid=hcp+MgB2 | hcp: B 0; MgB2: B 0.666667, Mg 0.333333; liq: B 2.000e-4 | model | [1] Liu 2001 | Table 4, p. 4, row 6; `ORC-XH3WYO37II` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, B–Mg system (53)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Mg2B | [Mg2B](https://data.orchid-project.org/compounds/Mg2B.html) | -14.23 kJ/mol-atom ± 0.84 | 298.15 | experimental |  | 24.127 (oqmd-751629) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 11; `ORC-N2BPBLFSN3` |  |
| Mg4B |  | -19.53 kJ/mol-atom ± 1.39 | 298.15 | experimental |  |  | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 12; `ORC-TDP6IBGSN3` |  |
| MgB12 |  | -15.8 per mol-atom | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 20; `ORC-U4PKO6VDC3.e32d7d` |  |
| MgB12 |  | -10.1 per mol-atom | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 21; `ORC-KSZLEEN43W.59e8ac` |  |
| MgB12 | [MgB12](https://data.orchid-project.org/compounds/MgB12.html) | -10.07 kJ/mol-atom ± 0.9 | 298.15 | experimental |  | -0.392 (oqmd-1454219) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 10; `ORC-7PI7ACDB6X` |  |
| MgB2 |  | -41.1 per mol-atom ± 2.2 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 1; `ORC-ICOXV56CAA.5c1af0` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -41.1 kJ/mol-atom ± 2.2 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 1; `ORC-ICOXV56CAA.e54032` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -35.9 kJ/mol-atom | 298.15 | model | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 2; `ORC-2IFABLSXTP.0fc294` |  |
| MgB2 |  | -35.9 per mol-atom | 298.15 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 2; `ORC-2IFABLSXTP.68025c` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -26.66 kJ/mol-atom ± 10 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 1; `ORC-W2FCXHRFOP` |  |
| MgB2 |  | -26.6 per mol-atom ± 10 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 4; `ORC-YXEY33NPZK.25a37b` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -26.6 kJ/mol-atom ± 10 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 4; `ORC-YXEY33NPZK.6db522` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -24 kJ/mol-atom | 298.15 | model | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 3; `ORC-E6JIMEMUCO.4cfe01` |  |
| MgB2 |  | -24 per mol-atom | 298.15 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 3; `ORC-E6JIMEMUCO.5486b7` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -18.6 kJ/mol-atom | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 6; `ORC-WKL7IRXHLB.101474` |  |
| MgB2 |  | -18.6 per mol-atom | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 6; `ORC-WKL7IRXHLB.56a394` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -18.55 kJ/mol-atom ± 1.12 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 7; `ORC-ITEAB5IK2I` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -17.2 kJ/mol-atom ± 1.4 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [2] Balducci 2005 | Table 2, p. 4, row 5; `ORC-ERT3NO6RZ2.960926` |  |
| MgB2 |  | -17.2 per mol-atom ± 1.4 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 5; `ORC-ERT3NO6RZ2.bf8224` |  |
| MgB2 | [MgB2](https://data.orchid-project.org/compounds/MgB2.html) | -17.17 kJ/mol-atom ± 1.39 | 298.15 | experimental | -12.577 (mp-aaaaabdj) | -13.509 (oqmd-98302) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 4; `ORC-P2QKYSNQY6` |  |
| MgB20 |  | -15.8 kJ/mol-atom | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 20; `ORC-U4PKO6VDC3.44736a` |  |
| MgB20 |  | -10.1 kJ/mol-atom | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 21; `ORC-KSZLEEN43W.55841f` |  |
| MgB20 |  | -8.5 kJ/mol-atom ± 0.6 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 18; `ORC-3F6HNE63V7.beec38` |  |
| MgB20 |  | -8.5 per mol-atom ± 0.6 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 18; `ORC-3F6HNE63V7.f04d86` |  |
| MgB20 |  | -7.8 kJ/mol-atom | 298.15 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 19; `ORC-QPHLWARFMZ.626188` |  |
| MgB20 |  | -7.8 per mol-atom | 298.15 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 19; `ORC-QPHLWARFMZ.8b80cd` |  |
| MgB4 |  | -29.9 per mol-atom ± 2 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 7; `ORC-BBS5QJWESM.81953b` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -29.9 kJ/mol-atom ± 2 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 7; `ORC-BBS5QJWESM.c4284a` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -25.5 kJ/mol-atom | 298.15 | model | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 8; `ORC-T733N4EIL3.24deaa` |  |
| MgB4 |  | -25.5 per mol-atom | 298.15 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 8; `ORC-T733N4EIL3.49ce03` |  |
| MgB4 |  | -18.4 per mol-atom | 298.15 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 9; `ORC-ZDO3KQSJW5.7929a6` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -18.4 kJ/mol-atom | 298.15 | model | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 9; `ORC-ZDO3KQSJW5.f14655` |  |
| MgB4 |  | -17.6 per mol-atom ± 3.8 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 10; `ORC-YXGP7HACWX.5e50aa` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -17.6 kJ/mol-atom ± 3.8 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 10; `ORC-YXGP7HACWX.bd63e9` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -17.57 kJ/mol-atom ± 3.85 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 2; `ORC-X2SXXKZOB3` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -14.73 kJ/mol-atom ± 0.5 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 8; `ORC-R6NR5W7CED` |  |
| MgB4 |  | -14.7 per mol-atom | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 12; `ORC-UI3WEXKPCB.6c3cc9` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -14.7 kJ/mol-atom | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 12; `ORC-UI3WEXKPCB.ac1885` |  |
| MgB4 |  | -14.4 per mol-atom ± 0.8 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 11; `ORC-GVFN7QIKSZ.95264b` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -14.4 kJ/mol-atom ± 0.8 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [2] Balducci 2005 | Table 2, p. 4, row 11; `ORC-GVFN7QIKSZ.96de4b` |  |
| MgB4 | [MgB4](https://data.orchid-project.org/compounds/MgB4.html) | -14.39 kJ/mol-atom ± 0.75 | 298.15 | experimental | -13.395 (mp-aaaaaaob) | -13.876 (oqmd-4315) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 5; `ORC-VCABWHTXUT` |  |
| MgB6 |  | -15.5 per mol-atom ± 2.1 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 15; `ORC-G5XQAHUA2A.963f3e` |  |
| MgB6 |  | -13.4 per mol-atom | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 17; `ORC-KRQXJTFGPA.b008fc` |  |
| MgB6 |  | -13.4 per mol-atom ± 0.6 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 16; `ORC-NNE6I23M5C.9c392a` |  |
| MgB6 | [MgB6](https://data.orchid-project.org/compounds/MgB6.html) | -13.39 kJ/mol-atom ± 0.6 | 298.15 | experimental |  | 0.227 (oqmd-1454656) | [1] Liu 2001; _cites Jansson 1984_ | Table 2, p. 2, row 6; `ORC-3LPA54QJQD` |  |
| MgB6 | [MgB6](https://data.orchid-project.org/compounds/MgB6.html) | -13.39 kJ/mol-atom ± 0.3 | 298.15 | experimental |  | 0.227 (oqmd-1454656) | [1] Liu 2001; _cites Sundman 1985_ [doi](https://doi.org/10.1016/0364-5916%2885%2990021-5) | Table 2, p. 2, row 9; `ORC-KIP2CJSBMK` |  |
| MgB7 |  | -20.3 per mol-atom ± 1.5 | 298.15 | experimental |  |  | [2] Balducci 2005 | Table 2, p. 4, row 13; `ORC-P6MTDZ2R6C.cdf675` |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -20.3 kJ/mol-atom ± 1.5 | 298.15 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 13; `ORC-P6MTDZ2R6C.d17661` |  |
| MgB7 |  | -18.9 per mol-atom | 298.15 | model |  |  | [2] Balducci 2005 | Table 2, p. 4, row 14; `ORC-6QSEGQVYRF.1bc541` |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -18.9 kJ/mol-atom | 298.15 | model | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 14; `ORC-6QSEGQVYRF.a2be47` |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -15.5 kJ/mol-atom ± 2.1 | 298.15 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 15; `ORC-G5XQAHUA2A.b69905` |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -13.4 kJ/mol-atom | 298.15 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 17; `ORC-KRQXJTFGPA.f6e9e4` |  |
| MgB7 | [MgB7](https://data.orchid-project.org/compounds/MgB7.html) | -13.4 kJ/mol-atom ± 0.6 | 298.15 | experimental | -12.598 (mp-aaacdrdz) | -13.076 (oqmd-23820) | [2] Balducci 2005 | Table 2, p. 4, row 16; `ORC-NNE6I23M5C.137242` |  |

## Other properties

### Phase transition (17)

Table: Phase transition, B–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1818 K | 1818 | other: MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 4, p. 5, row 17; `ORC-JJZRRHVNDH` |  |
| Phase transition | 1818.15 K | 1818.15 | other | model | [1] Liu 2001 | p. 2; `ORC-QH6KBJN3XU.393f92` | “Based on the limited experimental data in the literature\[9, 10, 13\], the suggestion by Spear\[6\], and the thermodynamic data of MgB2 and MgB4 in the JANAF table and by SGTE\[18\], the decomposition temperatures of the three intermediate compounds are estimated to be 1545, 1735, and 2150 °C for MgB2, MgB4, and MgB7, respectively.” |
| Phase transition | 1823 K | 1823 | other: MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 4, p. 5, row 18; `ORC-5BL5EKDQ2R` |  |
| Phase transition | 1888 K | 1888 | other: MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 15; `ORC-ZFCZFYOXN7` |  |
| Phase transition | 1941 K | 1941 | other: MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 19; `ORC-Y6RBWFGXFK` |  |
| Phase transition | 1980 K | 1980 | other: MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 4, p. 5, row 16; `ORC-HCANQWCFRZ` |  |
| Phase transition | 2008 K | 2008 | other: MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 4, p. 5, row 21; `ORC-LGWRNWKKUO` |  |
| Phase transition | 2008.15 K | 2008.15 | other | model | [1] Liu 2001 | p. 2; `ORC-QH6KBJN3XU.73c116` | “Based on the limited experimental data in the literature\[9, 10, 13\], the suggestion by Spear\[6\], and the thermodynamic data of MgB2 and MgB4 in the JANAF table and by SGTE\[18\], the decomposition temperatures of the three intermediate compounds are estimated to be 1545, 1735, and 2150 °C for MgB2, MgB4, and MgB7, respectively.” |
| Phase transition | 2073 K | 2073 | other: MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 4, p. 5, row 22; `ORC-3J73Z65XKI` |  |
| Phase transition | 2282 K | 2282 | other: MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 4, p. 5, row 20; `ORC-22UP76QFRA` |  |
| Phase transition | 2318 K | 2318 | other: MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 23; `ORC-MBHAKOKLNE` |  |
| Phase transition | 2415 K | 2415 | other: MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 4, p. 5, row 24; `ORC-VM4OA7QXAH` |  |
| Phase transition | 2423 K | 2423 | other: MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 4, p. 5, row 25; `ORC-VYWLBCFOWA` |  |
| Phase transition | 2423.15 K | 2423.15 | other | model | [1] Liu 2001 | p. 2; `ORC-QH6KBJN3XU.2413ec` | “Based on the limited experimental data in the literature\[9, 10, 13\], the suggestion by Spear\[6\], and the thermodynamic data of MgB2 and MgB4 in the JANAF table and by SGTE\[18\], the decomposition temperatures of the three intermediate compounds are estimated to be 1545, 1735, and 2150 °C for MgB2, MgB4, and MgB7, respectively.” |
| Phase transition | 2464 K | 2464 | other: MgB20; _alloy: Mg 0.047619_ | model | [2] Balducci 2005 | Table 4, p. 5, row 27; `ORC-W7JR6U7KI2` |  |
| Phase transition | 2700 K | 2700 | other: MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 28; `ORC-24UMVVYEFE` |  |
| Phase transition | 2759 K | 2759 | other: MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 4, p. 5, row 26; `ORC-7PFPEOY6JG` |  |

### Formation (17)

Table: Formation, B–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔfS0298_ | -2.8 per mol-atom ± 0.1 | 298.15 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 4; `ORC-7JARYD2GDO.437e76` |  |
| Entropy of formation; _printed: ΔfS0298_ | -2.86 J/mol-atom/K | 298.15 | MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 3, p. 4, row 2; `ORC-CDBCAK65MM.38bbe3` |  |
| Entropy of formation; _printed: ΔfS0298_ | -4.25 per mol-atom ± 0.5 | 298.15 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 1; `ORC-MVKY3RMSTR.97302a` |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.343 J/mol-atom/K | 298.15 | MgB2; _alloy: Mg 0.333333_ | model | [2] Balducci 2005 | Table 3, p. 4, row 3; `ORC-OLQRBC4EVL.5e34a8` |  |
| Entropy of formation; _printed: ΔfS0298_ | -2.82 J/mol-atom/K | 298.15 | MgB2; _alloy: Mg 0.333333_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 5; `ORC-UF3FNGGTZP.0edffa` |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.03 per mol-atom ± 0.01 | 298.15 | MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 15; `ORC-6XQ6CRLVRT.86e8f1` |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.04 J/mol-atom/K | 298.15 | MgB20; _alloy: Mg 0.047619_ | model | [2] Balducci 2005 | Table 3, p. 4, row 16; `ORC-DEX7CPGC7S.045670` |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.47 per mol-atom ± 0.1 | 298.15 | MgB20; _alloy: Mg 0.047619_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 17; `ORC-ZRJNIMZSJH.5cdadd` |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.655 J/mol-atom/K | 298.15 | MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 3, p. 4, row 8; `ORC-BNYQZOHJAG.0134b4` |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.18 J/mol-atom/K | 298.15 | MgB4; _alloy: Mg 0.2_ | model | [2] Balducci 2005 | Table 3, p. 4, row 7; `ORC-FGMCYNYI3R.1b40e0` |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.32 J/mol-atom/K | 298.15 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005; _cites Pan 1989_ [doi](https://doi.org/10.1007/bf02057252) | Table 3, p. 4, row 10; `ORC-SIAI5CTOVN.43e53d` |  |
| Entropy of formation; _printed: ΔfS0298_ | -3.04 per mol-atom ± 0.5 | 298.15 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 6; `ORC-TKTYVPIWIP.62a63c` |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.84 per mol-atom ± 0.1 | 298.15 | MgB4; _alloy: Mg 0.2_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 9; `ORC-ZNETWPDODA.9374aa` |  |
| Entropy of formation; _printed: ΔfS0298_ | -0.1 J/mol-atom/K | 298.15 | MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 3, p. 4, row 13; `ORC-H65ITY2A2I.0d2abb` |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.02 J/mol-atom/K | 298.15 | MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005; _cites Pan 1989_ [doi](https://doi.org/10.1007/bf02057252) | Table 3, p. 4, row 14; `ORC-OAFWHKLTDT.1e2438` |  |
| Entropy of formation; _printed: ΔfS0298_ | 0.94 per mol-atom ± 0.5 | 298.15 | MgB7; _alloy: Mg 0.125_ | experimental | [2] Balducci 2005 | Table 3, p. 4, row 11; `ORC-WOF23P2X7S.046ce6` |  |
| Entropy of formation; _printed: ΔfS0298_ | -1.21 J/mol-atom/K | 298.15 | MgB7; _alloy: Mg 0.125_ | model | [2] Balducci 2005 | Table 3, p. 4, row 12; `ORC-WQU35CG3FF.3838fa` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zi-Kui Liu, Yu Zhong, D.G. Schlom, X.X. Xi, Qi Li, Computational thermodynamic modeling of the Mg-B system, Calphad 25, 299-303 (2001). [doi:10.1016/s0364-5916(01)00050-5](https://doi.org/10.1016/s0364-5916%2801%2900050-5)
2. G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005). [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

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
