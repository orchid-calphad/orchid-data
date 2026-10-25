# Sb–Yb phases

> Sb–Yb system: 12 phases (tier A 8, tier C 3, liquid 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SB-YB.html · Markdown: https://data.orchid-project.org/phases/pages/SB-YB.md

12 phases (tier A 8, tier C 3, liquid 1); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SB-YB) · [full JSON](https://data.orchid-project.org/phases/systems/SB-YB.json) · [Sb–Yb system page](https://data.orchid-project.org/systems/SB-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/SB-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sb–Yb system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-sb-yb-a7-rhombohedral); _phase:sb-yb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–906.36 K, x(Yb) 0–0.00863 | 4 | 2 |
| [BCC_A2](#phase-sb-yb-bcc-a2); _phase:sb-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300.51–2499.98 K, x(Yb) 0.99125–1 | 5 | 2 |
| [FCC_A1](#phase-sb-yb-fcc-a1); _phase:sb-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1038.15 K, x(Yb) 0.99336–1 | 0 | 2 |
| [HCP_A3](#phase-sb-yb-hcp-a3); _phase:sb-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-sb-yb-liquid); _phase:sb-yb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 885.12–2500 K, x(Yb) 0–1 | 32 | 2 |
| [SB10YB11](#phase-sb-yb-sb10yb11); _phase:sb-yb:sb10yb11_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1678.22 K, x(Yb) 0.52381–0.52381 | 8 | 2 |
| [SB11YB16](#phase-sb-yb-sb11yb16); _phase:sb-yb:sb11yb16_ | Ca16Sb11 · . · tP56 · P-42_1m (113) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1877.56 K, x(Yb) 0.59259–0.59259 | 3 | 1 |
| [SB2YB_C49](#phase-sb-yb-sb2yb-c49); _phase:sb-yb:sb2yb-c49_ | ZrSi2 · C49 · oC12 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1077.97 K, x(Yb) 0.33333–0.33333 | 9 | 2 |
| [SB3YB4_D73](#phase-sb-yb-sb3yb4-d73); _phase:sb-yb:sb3yb4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1953.22 K, x(Yb) 0.57143–0.57143 | 12 | 2 |
| [SB3YB5_HT](#phase-sb-yb-sb3yb5); _phase:sb-yb:sb3yb5_ | Sb3Yb5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1553.22–1813.03 K, x(Yb) 0.625–0.625 | 4 | 1 |
| [SB3YB5_D88](#phase-sb-yb-sb3yb5-d88); _phase:sb-yb:sb3yb5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1811.98 K, x(Yb) 0.625–0.625 | 9 | 2 |
| [SBYB_B1](#phase-sb-yb-sbyb-b1); _phase:sb-yb:sbyb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1348.34 K, x(Yb) 0.5–0.5 | 9 | 2 |

## RHOMBOHEDRAL_A7 (Sb–Yb)

- Id: `phase:sb-yb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–906.36 K, x(Yb) 0–0.00863
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:sb-yb:a7-rhombohedral, corpus:phase:sb-yb:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2012.02.004:(Sb), paper:10.1016/j.calphad.2023.102541:Rhombohedral  
_tdb: _tdb:SbYb-12Liu.tdb:RHOMBOHEDRAL_A7, tdb:SbYb-23Paz.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : SB% YB : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : SB% YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Sb–Yb)

- Id: `phase:sb-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.51–2499.98 K, x(Yb) 0.99125–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:bcc-a2)

Names (5): _corpus: _corpus:phase:sb-yb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2012.02.004:(γYb), paper:10.1016/j.calphad.2023.102541:BCC_A2  
_tdb: _tdb:SbYb-12Liu.tdb:BCC_A2, tdb:SbYb-23Paz.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): BCC_A2, type code %B, sha256 `9665ec0dd33d9b48…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SB YB% : VA : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): BCC_A2, type code %B, sha256 `8bf0a94cd3195ef3…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : SB YB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Sb–Yb)

- Id: `phase:sb-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1038.15 K, x(Yb) 0.99336–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:sb-yb:fcc-a1  
_tdb: _tdb:SbYb-12Liu.tdb:FCC_A1, tdb:SbYb-23Paz.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): FCC_A1, type code %A, sha256 `9665ec0dd33d9b48…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SB YB% : VA : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): FCC_A1, type code %A, sha256 `8bf0a94cd3195ef3…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : SB YB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase_

## HCP_A3 (Sb–Yb)

- Id: `phase:sb-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:hcp-a3)

Names (3): _corpus: _corpus:phase:sb-yb:hcp-a3  
_tdb: _tdb:SbYb-12Liu.tdb:HCP_A3, tdb:SbYb-23Paz.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): HCP_A3, type code %A, sha256 `9665ec0dd33d9b48…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SB YB : VA : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): HCP_A3, type code %A, sha256 `8bf0a94cd3195ef3…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : SB YB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase_

## LIQUID (Sb–Yb)

- Id: `phase:sb-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 885.12–2500 K, x(Yb) 0–1
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:liquid)

Names (6): _corpus: _corpus:phase:sb-yb:liquid  
_paper: _paper:10.1016/j.calphad.2012.02.004:L, paper:10.1016/j.calphad.2023.102541:Liquid, paper:10.1016/j.calphad.2023.102541:liquid  
_tdb: _tdb:SbYb-12Liu.tdb:LIQUID, tdb:SbYb-23Paz.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): LIQUID, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SB YB : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): LIQUID, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : SB SB3YB4 YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50048a030](https://doi.org/10.1021/ic50048a030) Raymond E. Bodnar, Hugo Steinfink, Phase equilibriums and crystal chemistry of the intermediate phases in the ytterbium-antimony system, Inorg. Chem. 6, 327-330 (1967).  
_cited as the source of values for this phase_

## SB10YB11 (Sb–Yb)

- Id: `phase:sb-yb:sb10yb11`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sb 0.4762, Yb 0.5238
- Stability: stable in 2 of 2 calculated diagram(s): 300–1678.22 K, x(Yb) 0.52381–0.52381
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:sb10yb11)

Names (5): _corpus: _corpus:phase:sb-yb:sb10yb11  
_paper: _paper:10.1016/j.calphad.2012.02.004:Sb10Yb11, paper:10.1016/j.calphad.2023.102541:Yb11Sb10  
_tdb: _tdb:SbYb-12Liu.tdb:SB10YB11, tdb:SbYb-23Paz.tdb:SB10YB11  


### TDB models of SB10YB11 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): SB10YB11, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
56: PHASE SB10YB11 % 2 10 11 !
57: CONST SB10YB11 : SB : YB : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): SB10YB11, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
66: PHASE SB10YB11 % 2 10 11 !
67: CONST SB10YB11 : SB : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50048a030](https://doi.org/10.1021/ic50048a030) Raymond E. Bodnar, Hugo Steinfink, Phase equilibriums and crystal chemistry of the intermediate phases in the ytterbium-antimony system, Inorg. Chem. 6, 327-330 (1967).  
_cited as the source of values for this phase_

## SB11YB16 (Sb–Yb)

- Id: `phase:sb-yb:sb11yb16`; status `assigned`
- Structure: Ca16Sb11 · . · tP56 · P-42_1m (113); type `st:ca16sb11-tp56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sb 0.4074, Yb 0.5926
- Stability: stable in 1 of 1 calculated diagram(s): 300–1877.56 K, x(Yb) 0.59259–0.59259
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:sb11yb16)

Names (3): _corpus: _corpus:phase:sb-yb:sb11yb16  
_paper: _paper:10.1016/j.calphad.2023.102541:Yb16Sb11  
_tdb: _tdb:SbYb-23Paz.tdb:SB11YB16  


### TDB models of SB11YB16 (1): PHASE and CONSTITUENT statements as written

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): SB11YB16, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
76: PHASE SB11YB16 % 2 11 16 !
77: CONST SB11YB16 : SB : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_

## SB2YB_C49 (Sb–Yb)

- Id: `phase:sb-yb:sb2yb-c49`; status `assigned`
- Structure: ZrSi2 · C49 · oC12 · Cmcm (63); type `st:c49-zrsi2-oc12`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.6667, Yb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1077.97 K, x(Yb) 0.33333–0.33333
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:sb2yb-c49)

Names (5): _corpus: _corpus:phase:sb-yb:sb2yb-c49  
_paper: _paper:10.1016/j.calphad.2012.02.004:Sb2Yb, paper:10.1016/j.calphad.2023.102541:YbSb2  
_tdb: _tdb:SbYb-12Liu.tdb:SB2YB_C49, tdb:SbYb-23Paz.tdb:SB2YB_C49  


### TDB models of SB2YB_C49 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): SB2YB_C49, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
46: PHASE SB2YB_C49 % 2 2 1 !
47: CONST SB2YB_C49 : SB : YB : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): SB2YB_C49, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
56: PHASE SB2YB_C49 % 2 2 1 !
57: CONST SB2YB_C49 : SB : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50048a030](https://doi.org/10.1021/ic50048a030) Raymond E. Bodnar, Hugo Steinfink, Phase equilibriums and crystal chemistry of the intermediate phases in the ytterbium-antimony system, Inorg. Chem. 6, 327-330 (1967).  
_cited as the source of values for this phase_

## SB3YB4_D73 (Sb–Yb)

- Id: `phase:sb-yb:sb3yb4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.4286, Yb 0.5714
- Stability: stable in 2 of 2 calculated diagram(s): 300–1953.22 K, x(Yb) 0.57143–0.57143
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:sb3yb4-d73)

Names (5): _corpus: _corpus:phase:sb-yb:sb3yb4-d73  
_paper: _paper:10.1016/j.calphad.2012.02.004:Sb3Yb4, paper:10.1016/j.calphad.2023.102541:Yb4Sb3  
_tdb: _tdb:SbYb-12Liu.tdb:SB3YB4_D73, tdb:SbYb-23Paz.tdb:SB3YB4_D73  


### TDB models of SB3YB4_D73 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): SB3YB4_D73, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
61: PHASE SB3YB4_D73 % 2 3 4 !
62: CONST SB3YB4_D73 : SB : YB : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): SB3YB4_D73, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
71: PHASE SB3YB4_D73 % 2 3 4 !
72: CONST SB3YB4_D73 : SB : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50048a030](https://doi.org/10.1021/ic50048a030) Raymond E. Bodnar, Hugo Steinfink, Phase equilibriums and crystal chemistry of the intermediate phases in the ytterbium-antimony system, Inorg. Chem. 6, 327-330 (1967).  
_cited as the source of values for this phase_

## SB3YB5_HT (Sb–Yb)

- Id: `phase:sb-yb:sb3yb5`; status `assigned`
- Structure: Sb3Yb5 · oP32 · Pnma (62); type `st:sb3yb5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sb 0.3750, Yb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1553.22–1813.03 K, x(Yb) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:sb3yb5)

Names (4): _corpus: _corpus:phase:sb-yb:sb3yb5, corpus:phase:sb-yb:sb3yb5-ht  
_paper: _paper:10.1016/j.calphad.2012.02.004:βSb3Yb5  
_tdb: _tdb:SbYb-12Liu.tdb:SB3YB5_HT  


### TDB models of SB3YB5_HT (1): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): SB3YB5_HT, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
71: PHASE SB3YB5_HT % 2 3 5 !
72: CONST SB3YB5_HT : SB : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_

## SB3YB5_D88 (Sb–Yb)

- Id: `phase:sb-yb:sb3yb5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.3750, Yb 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–1811.98 K, x(Yb) 0.625–0.625
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:sb3yb5-d88)

Names (5): _corpus: _corpus:phase:sb-yb:sb3yb5-d88  
_paper: _paper:10.1016/j.calphad.2012.02.004:αSb3Yb5, paper:10.1016/j.calphad.2023.102541:Yb5Sb3  
_tdb: _tdb:SbYb-12Liu.tdb:SB3YB5_D88, tdb:SbYb-23Paz.tdb:SB3YB5_D88  


### TDB models of SB3YB5_D88 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): SB3YB5_D88, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
66: PHASE SB3YB5_D88 % 2 3 5 !
67: CONST SB3YB5_D88 : SB : YB : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): SB3YB5_D88, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
81: PHASE SB3YB5_D88 % 2 3 5 !
82: CONST SB3YB5_D88 : SB : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_

## SBYB_B1 (Sb–Yb)

- Id: `phase:sb-yb:sbyb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.5000, Yb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1348.34 K, x(Yb) 0.5–0.5
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-yb:sbyb-b1)

Names (5): _corpus: _corpus:phase:sb-yb:sbyb-b1  
_paper: _paper:10.1016/j.calphad.2012.02.004:SbYb, paper:10.1016/j.calphad.2023.102541:YbSb  
_tdb: _tdb:SbYb-12Liu.tdb:SBYB_B1, tdb:SbYb-23Paz.tdb:SBYB_B1  


### TDB models of SBYB_B1 (2): PHASE and CONSTITUENT statements as written

[SbYb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-12Liu.tdb): SBYB_B1, type code %, sha256 `9665ec0dd33d9b48…`

~~~~text
51: PHASE SBYB_B1 % 2 1 1 !
52: CONST SBYB_B1 : SB : YB : !
~~~~

[SbYb-23Paz.tdb](https://orchid-project.org/data/databases/sgte-binary/SbYb-23Paz.tdb): SBYB_B1, type code %, sha256 `8bf0a94cd3195ef3…`

~~~~text
61: PHASE SBYB_B1 % 2 1 1 !
62: CONST SBYB_B1 : SB : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2023.102541](https://doi.org/10.1016/j.calphad.2023.102541) Jorge Paz Soldan Palma, XiaoYu Chong, Yi Wang, Shun-Li Shang, Zi-Kui Liu, Thermodynamic re-modeling of the Yb-Sb system aided by first-principles calculations, Calphad 81, 102541 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50048a030](https://doi.org/10.1021/ic50048a030) Raymond E. Bodnar, Hugo Steinfink, Phase equilibriums and crystal chemistry of the intermediate phases in the ytterbium-antimony system, Inorg. Chem. 6, 327-330 (1967).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
