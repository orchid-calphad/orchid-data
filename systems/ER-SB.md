# Er–Sb system

> Er–Sb system: 42 accepted literature values (invariant reaction 28, formation 11, phase transition 2, mixing / partial 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-SB.html · Markdown: https://data.orchid-project.org/systems/ER-SB.md

42 accepted literature values from 2 paper(s) (experimental 23, model 19); 1 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-SB.json) · [CSV](https://data.orchid-project.org/systems/ER-SB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-SB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-SB/ErSb-11Wan.json) · [phases (9)](https://data.orchid-project.org/phases/pages/ER-SB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ER-SB.html) · [Markdown](https://data.orchid-project.org/systems/ER-SB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 23 |
| model | 19 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 28 |
| phase transition | 2 |
| formation | 11 |
| mixing / partial | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErSb-11Wan.tdb | S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Calphad, 35, 473-78(2011). [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) | `af95d657f5e4a5775ccaee480cccada64894a655e89a7dd5aaa766df11e8c052` | [viewer](https://orchid-project.org/phase-diagrams/#ER-SB/ErSb-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErSb-11Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErSb-11Wan.tdb | 2083.22 | ERSB_B1 (x(Sb) 0.5) + ERSB_BETA (x(Sb) 0.5) + LIQUID (x(Sb) 0.66398) |
| ErSb-11Wan.tdb | 2083.22 | LIQUID (x(Sb) 0.35043) + ERSB_B1 (x(Sb) 0.5) + ERSB_BETA (x(Sb) 0.5) |
| ErSb-11Wan.tdb | 1912.92 | LIQUID (x(Sb) 0.29909) + ER5SB3 (x(Sb) 0.375) + ERSB_B1 (x(Sb) 0.5) |
| ErSb-11Wan.tdb | 1912.92 | LIQUID (x(Sb) 0.29919) + ER5SB3 (x(Sb) 0.375) + ERSB_B1 (x(Sb) 0.5) |
| ErSb-11Wan.tdb | 1801.99 | HCP_A3 (x(Sb) 0) + LIQUID (x(Sb) 0) + ERSB_B1 (x(Sb) 0.5) |
| ErSb-11Wan.tdb | 1443.29 | HCP_A3 (x(Sb) 0.01399) + LIQUID (x(Sb) 0.13214) + ER5SB3 (x(Sb) 0.375) |
| ErSb-11Wan.tdb | 1443.29 | HCP_A3 (x(Sb) 0.01397) + LIQUID (x(Sb) 0.13208) + ER5SB3 (x(Sb) 0.375) |
| ErSb-11Wan.tdb | 922.25 | ERSB_B1 (x(Sb) 0.5) + ERSB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.98661) |
| ErSb-11Wan.tdb | 922.25 | ERSB_B1 (x(Sb) 0.5) + ERSB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.9866) |
| ErSb-11Wan.tdb | 900.1 | ERSB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.98957) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| ErSb-11Wan.tdb | 900.1 | ERSB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.98958) + RHOMBOHEDRAL_A7 (x(Sb) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-SB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–Sb system (28)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2313.15 | congruent melting: L -> βErSb | L: Sb 0.5; βErSb: Sb 0.5 | model | [1] Wang 2011 | Table 1, p. 3, row 8; `ORC-2KEF3XWDAL` |  |
| 2313.15 | congruent melting: L -> βErSb | L: Sb 0.5; βErSb: Sb 0.5 | experimental | [1] Wang 2011; _cites Abdusalyamova 1993_ [doi](https://doi.org/10.1016/0925-8388%2893%2990504-g) | Table 1, p. 3, row 7; `ORC-HXRTN6NP2R` |  |
| 2313 | congruent melting: liq. -> βErSb | liq.: Er 0.5, Sb 0.5; βErSb: Er 0.5, Sb 0.5 | model | [2] Wang 2011 | Table 4, p. 9, row 5; `ORC-EMUW26U7OW` |  |
| 2313 | congruent melting: liq. -> βErSb | liq.: Er 0.5, Sb 0.5; βErSb: Er 0.5, Sb 0.5 | experimental | [2] Wang 2011; _cites Abdusalyamova 2002_ [doi](https://doi.org/10.1515/zna-2002-9-1017) | Table 4, p. 9, row 6; `ORC-J6BW23EQHK` |  |
| 2083.25 | polymorphic: αErSb -> βErSb | αErSb: Er 0.5, Sb 0.5; βErSb: Sb 0.5 | model | [1] Wang 2011 | Table 1, p. 3, row 6; `ORC-XUL3IJZAYN` |  |
| 2083.15 | polymorphic: αErSb -> βErSb | αErSb: Er 0.5, Sb 0.5; βErSb: Sb 0.5 | experimental | [1] Wang 2011; _cites Abdusalyamova 1993_ [doi](https://doi.org/10.1016/0925-8388%2893%2990504-g) | Table 1, p. 3, row 5; `ORC-TZGKTMDGEO` |  |
| 2083 | polymorphic: αErSb -> βErSb | αErSb: Er 0.5, Sb 0.5; βErSb: Er 0.5, Sb 0.5 | experimental | [2] Wang 2011; _cites Abdusalyamova 2002_ [doi](https://doi.org/10.1515/zna-2002-9-1017) | Table 4, p. 9, row 12; `ORC-2L6YOMHJHR` |  |
| 2083 | polymorphic: αErSb -> βErSb | αErSb: Er 0.5, Sb 0.5; βErSb: Er 0.5, Sb 0.5 | model | [2] Wang 2011 | Table 4, p. 9, row 11; `ORC-YU6WNUIJKW` |  |
| 1913.15 | peritectic: L + αErSb -> Er5Sb3 | αErSb: Sb 0.5; Er5Sb3: Sb 0.375 | experimental | [1] Wang 2011; _cites Abdusalyamova 1993_ [doi](https://doi.org/10.1016/0925-8388%2893%2990504-g) | Table 1, p. 3, row 3; `ORC-HOKARMQTUY` |  |
| 1913.15 | peritectic |  | experimental | [1] Wang 2011; _cites Abdusalyamova 1993_ [doi](https://doi.org/10.1016/0925-8388%2893%2990504-g) | p. 1; `ORC-PVYOTEU74C.fa1ca3` | “Later, based on thermal, microstructural, and X-ray diffraction analysis, Abdusalyamova \[6\] investigated the phase diagram in the Er-Sb system, and reported three stoichiometric compounds: Er5 Sb3 (peritectic formation at 1640 °C), ErSb (melting point 2040 °C), and ErSb2 (peritectic formation at 650 °C).” |
| 1913 | liq. + αErSb -> Er5Sb3 | liq.: Sb 0.3005; αErSb: Er 0.5, Sb 0.5; Er5Sb3: Er 0.625, Sb 0.375 | model | [2] Wang 2011 | Table 4, p. 9, row 3; `ORC-UFUJFNKFLB` |  |
| 1913 | liq. + αErSb -> Er5Sb3 | αErSb: Er 0.5, Sb 0.5; Er5Sb3: Er 0.625, Sb 0.375 | experimental | [2] Wang 2011; _cites Abdusalyamova 2002_ [doi](https://doi.org/10.1515/zna-2002-9-1017) | Table 4, p. 9, row 4; `ORC-V7XJI2YTN2` |  |
| 1912.95 | peritectic: L + αErSb -> Er5Sb3 | L: Sb 0.299; αErSb: Sb 0.5; Er5Sb3: Sb 0.375 | model | [1] Wang 2011 | Table 1, p. 3, row 4; `ORC-3F45TCMV66` |  |
| 1443.25 | eutectic: L -> (Er) + Er5Sb3 | L: Sb 0.132; (Er): Sb 0.014; Er5Sb3: Sb 0.25 | model | [1] Wang 2011 | Table 1, p. 3, row 2; `ORC-GZFZB2TAH3` |  |
| 1443.15 | eutectic: L -> (Er) + Er5Sb3 | L: Sb 0.155; Er5Sb3: Sb 0.25 | experimental | [1] Wang 2011; _cites Abdusalyamova 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900581-2) | Table 1, p. 3, row 1; `ORC-75XUOE7TMB` |  |
| 1443 | eutectic: liq. -> hcp + Er5Sb3 | liq.: Sb 0.1396; hcp: Sb 0.0242; Er5Sb3: Er 0.625, Sb 0.375 | model | [2] Wang 2011 | Table 4, p. 9, row 1; `ORC-PDNKOC3A55` |  |
| 1443 | eutectic: liq. -> hcp + Er5Sb3 | liq.: Sb 0.155; Er5Sb3: Er 0.625, Sb 0.375 | experimental | [2] Wang 2011; _cites Abdusalyamova 2002_ [doi](https://doi.org/10.1515/zna-2002-9-1017) | Table 4, p. 9, row 2; `ORC-X4RA3F3KG4` |  |
| 923.15 | peritectic: L + αErSb -> ErSb2 | αErSb: Sb 0.5; ErSb2: Sb 0.667 | experimental | [1] Wang 2011; _cites Abdusalyamova 1988_ | Table 1, p. 3, row 9; `ORC-4HYAUTCGEQ` |  |
| 923.15 | peritectic: L + αErSb -> ErSb2 | L: Sb 0.987; αErSb: Sb 0.5; ErSb2: Sb 0.667 | model | [1] Wang 2011 | Table 1, p. 3, row 10; `ORC-GOODFMQHGN` |  |
| 923.15 | peritectic |  | experimental | [1] Wang 2011; _cites Abdusalyamova 1993_ [doi](https://doi.org/10.1016/0925-8388%2893%2990504-g) | p. 1; `ORC-PVYOTEU74C.63730c` | “Later, based on thermal, microstructural, and X-ray diffraction analysis, Abdusalyamova \[6\] investigated the phase diagram in the Er-Sb system, and reported three stoichiometric compounds: Er5 Sb3 (peritectic formation at 1640 °C), ErSb (melting point 2040 °C), and ErSb2 (peritectic formation at 650 °C).” |
| 923 | liq. + αErSb -> ErSb2 | liq.: Sb 0.9627; αErSb: Er 0.5, Sb 0.5; ErSb2: Er 0.333333, Sb 0.666667 | model | [2] Wang 2011 | Table 4, p. 9, row 7; `ORC-SFJ3WDHJQO` |  |
| 923 | liq. + αErSb -> ErSb2 | liq.: Sb 0.976; αErSb: Er 0.5, Sb 0.5; ErSb2: Er 0.333333, Sb 0.666667 | experimental | [2] Wang 2011; _cites Abdusalyamova 2002_ [doi](https://doi.org/10.1515/zna-2002-9-1017) | Table 4, p. 9, row 8; `ORC-YFWGEMIKZ7` |  |
| 903.15 | eutectic: L -> ErSb2 + (Sb) | ErSb2: Sb 0.667; (Sb): Sb 1 | experimental | [1] Wang 2011; _cites Okamoto 1995_ [doi](https://doi.org/10.1007/bf02667317) | Table 1, p. 3, row 11; `ORC-H3FTBNGCQD` |  |
| 900.15 | eutectic: L -> ErSb2 + (Sb) | L: Sb 0.99; ErSb2: Sb 0.667; (Sb): Sb 1 | model | [1] Wang 2011 | Table 1, p. 3, row 14; `ORC-H5P4CFEK5V` |  |
| 898.15 | eutectic: L -> ErSb2 + (Sb) | L: Sb 0.99; ErSb2: Sb 0.667; (Sb): Sb 1 | experimental | [1] Wang 2011; _cites Abdusalyamova 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900581-2) | Table 1, p. 3, row 12; `ORC-ZVVLCOCCMD` |  |
| 893.15 | eutectic: L -> ErSb2 + (Sb) | L: Sb 0.994; ErSb2: Sb 0.667; (Sb): Sb 1 | experimental | [1] Wang 2011; _cites Abdusalyamova 2002_ [doi](https://doi.org/10.1515/zna-2002-9-1016) | Table 1, p. 3, row 13; `ORC-PNWIVDPJG5` |  |
| 893 | eutectic: liq. -> ErSb2 + rhom | liq.: Sb 0.9728; ErSb2: Er 0.333333, Sb 0.666667 | model | [2] Wang 2011 | Table 4, p. 9, row 9; `ORC-6WWBWJL7ZT` |  |
| 893 | eutectic: liq. -> ErSb2 + rhom | liq.: Sb 0.994; ErSb2: Er 0.333333, Sb 0.666667 | experimental | [2] Wang 2011; _cites Abdusalyamova 2002_ [doi](https://doi.org/10.1515/zna-2002-9-1017) | Table 4, p. 9, row 10; `ORC-ZUNVDGCBMW` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Er–Sb system (6)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Er5Sb3 | [Er5Sb3](https://data.orchid-project.org/compounds/Er5Sb3.html) | -83.05 kJ/mol-atom |  | model | -92.052 (mp-aaaaatem) | -85.758 (oqmd-99705) | [1] Wang 2011 | Table 3, p. 3, row 1; `ORC-IRWEXAI545` |  |
| ErSb2 | [ErSb2](https://data.orchid-project.org/compounds/ErSb2.html) | -75.6 kJ/mol-atom | 298.15 | experimental | -30.891 (mp-aaacfydz) | -67.126 (oqmd-1436071) | [1] Wang 2011; _cites Goryacheva 1981_ | Table 3, p. 3, row 5; `ORC-Q7C5BLWXKK` |  |
| ErSb2 | [ErSb2](https://data.orchid-project.org/compounds/ErSb2.html) | -75.142 kJ/mol-atom |  | model | -30.891 (mp-aaacfydz) | -67.126 (oqmd-1436071) | [1] Wang 2011 | Table 3, p. 3, row 6; `ORC-FX42G73YLD` |  |
| αErSb | [ErSb](https://data.orchid-project.org/compounds/ErSb.html) | -113.4 kJ/mol-atom | 298.15 | experimental | -114.05 (mp-aaaaadgh) | -105.779 (oqmd-8168) | [1] Wang 2011; _cites Goryacheva 1981_ | Table 3, p. 3, row 2; `ORC-4I5O2VKX3R` |  |
| αErSb | [ErSb](https://data.orchid-project.org/compounds/ErSb.html) | -111.583 kJ/mol-atom |  | model | -114.05 (mp-aaaaadgh) | -105.779 (oqmd-8168) | [1] Wang 2011 | Table 3, p. 3, row 4; `ORC-NQDLQWNQXF` |  |
| αErSb | [ErSb](https://data.orchid-project.org/compounds/ErSb.html) | -109 kJ/mol-atom | 298.15 | experimental | -114.05 (mp-aaaaadgh) | -105.779 (oqmd-8168) | [1] Wang 2011; _cites Pratt 1970_ | Table 3, p. 3, row 3; `ORC-7UHU6X4NLH` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Er–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 923.15 K | 923.15 | ErSb2 | experimental | [1] Wang 2011; _cites Abdusalyamova 1988_ | p. 1; `ORC-WA3GXQM5KW` | “Abdusalyamova et al. \[5\] were the first to report incongruent melting of the ErSb2 phase at 650 °C by means of differential thermal analysis (DTA).” |
| Phase transition | 2313.15 K | 2313.15 | ErSb | experimental | [1] Wang 2011; _cites Abdusalyamova 1993_ [doi](https://doi.org/10.1016/0925-8388%2893%2990504-g) | p. 1; `ORC-PVYOTEU74C.1eae94` | “Later, based on thermal, microstructural, and X-ray diffraction analysis, Abdusalyamova \[6\] investigated the phase diagram in the Er-Sb system, and reported three stoichiometric compounds: Er5 Sb3 (peritectic formation at 1640 °C), ErSb (melting point 2040 °C), and ErSb2 (peritectic formation at 650 °C).” |

### Formation (5)

Table: Formation, Er–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: standard entropies of formation_ | -1.23 J/mol-atom/K |  | Er5Sb3; _alloy: Sb 0.375_ | model | [1] Wang 2011 | Table 4, p. 3, row 1; `ORC-C3VRV5QQ7B` |  |
| Entropy of formation; _printed: standard entropies of formation_ | -5.507 J/mol-atom/K |  | ErSb2; _alloy: Sb 0.666667_ | model | [1] Wang 2011 | Table 4, p. 3, row 5; `ORC-GOWQRYVJRI` |  |
| Entropy of formation; _printed: standard entropies of formation_ | -7.314 J/mol-atom/K |  | αErSb; _alloy: Sb 0.5_ | model | [1] Wang 2011 | Table 4, p. 3, row 3; `ORC-O22WIKYCQV` |  |
| Entropy of formation; _printed: standard entropies of formation_ | -5 J/mol-atom/K | 298.15 | ErSb2; _alloy: Sb 0.666667_ | experimental | [1] Wang 2011; _cites Goryacheva 1981_ | Table 4, p. 3, row 4; `ORC-Q4JVICUL3R` |  |
| Entropy of formation; _printed: standard entropies of formation_ | -7.6 J/mol-atom/K | 298.15 | αErSb; _alloy: Sb 0.5_ | experimental | [1] Wang 2011; _cites Goryacheva 1981_ | Table 4, p. 3, row 2; `ORC-GCVPTSJRV4` |  |

### Mixing / partial (1)

Table: Mixing / partial, Er–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpies of mixing_ | -52.936 kJ/mol (basis unstated) | 2373.15 |  | model | [1] Wang 2011 | p. 4; `ORC-4WML3AHSVB` | “Fig. 6 shows the calculated enthalpies of mixing of the liquid phase at 2100 °C with reference states of pure Er (liquid) and Sb (liquid) in the Er-Sb binary system. The calculated value at 50 at% Sb is -52.936 kJ/mol, which is very close to the value of -53 kJ/mol predicted by Colinet et al. \[12\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011). [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001)
2. Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011). [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001)

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
