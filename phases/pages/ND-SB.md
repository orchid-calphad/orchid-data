# Nd–Sb phases

> Nd–Sb system: 11 phases (tier A 8, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ND-SB.html · Markdown: https://data.orchid-project.org/phases/pages/ND-SB.md

11 phases (tier A 8, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ND-SB) · [full JSON](https://data.orchid-project.org/phases/systems/ND-SB.json) · [Nd–Sb system page](https://data.orchid-project.org/systems/ND-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/ND-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nd–Sb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-nd-sb-a7-rhombohedral); _phase:nd-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.47 K, x(Sb) 1–1 | 0 | 2 |
| [BCC_A2](#phase-nd-sb-bcc-a2); _phase:nd-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1112.5–1302.9 K, x(Sb) 0–0.01259 | 0 | 2 |
| [DHCP](#phase-nd-sb-dhcp-a3); _phase:nd-sb:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1242.99 K, x(Sb) 0–8e-05 | 0 | 2 |
| [FCC_A1](#phase-nd-sb-fcc-a1); _phase:nd-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-nd-sb-hcp-a3); _phase:nd-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-nd-sb-liquid); _phase:nd-sb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 873.22–2500 K, x(Sb) 0–1 | 0 | 2 |
| [ND2SB](#phase-nd-sb-nd2sb); _phase:nd-sb:nd2sb_ | La2Sb · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1432.11 K, x(Sb) 0.33333–0.33333 | 0 | 2 |
| [ND4SB3_D73](#phase-nd-sb-nd4sb3-d73); _phase:nd-sb:nd4sb3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2073.1 K, x(Sb) 0.42857–0.42857 | 0 | 2 |
| [ND5SB3_D88](#phase-nd-sb-nd5sb3-d88); _phase:nd-sb:nd5sb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1962.94 K, x(Sb) 0.375–0.375 | 0 | 2 |
| [NDSB_B1](#phase-nd-sb-ndsb-b1); _phase:nd-sb:ndsb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2347.96 K, x(Sb) 0.5–0.5 | 0 | 2 |
| [NDSB2](#phase-nd-sb-ndsb2); _phase:nd-sb:ndsb2_ | Sb2Sm · oC24 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1922.96 K, x(Sb) 0.66667–0.66667 | 0 | 2 |

## RHOMBOHEDRAL_A7 (Nd–Sb)

- Id: `phase:nd-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.47 K, x(Sb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:nd-sb:a7-rhombohedral  
_tdb: _tdb:NdSb-16Wan.tdb:RHOMBOHEDRAL_A7, tdb:NdSb-92Cac-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `d8f37ff02b888b96…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : ND SB% : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `e0bd292dd8aa41ad…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## BCC_A2 (Nd–Sb)

- Id: `phase:nd-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1112.5–1302.9 K, x(Sb) 0–0.01259
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:bcc-a2)

Names (3): _corpus: _corpus:phase:nd-sb:bcc-a2  
_tdb: _tdb:NdSb-16Wan.tdb:BCC_A2, tdb:NdSb-92Cac-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): BCC_A2, type code %B, sha256 `d8f37ff02b888b96…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : ND% SB : VA : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): BCC_A2, type code %B, sha256 `e0bd292dd8aa41ad…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : ND% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## DHCP (Nd–Sb)

- Id: `phase:nd-sb:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1242.99 K, x(Sb) 0–8e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:dhcp-a3)

Names (3): _corpus: _corpus:phase:nd-sb:dhcp-a3  
_tdb: _tdb:NdSb-16Wan.tdb:DHCP, tdb:NdSb-92Cac-LB.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): DHCP, type code %A, sha256 `d8f37ff02b888b96…`

~~~~text
40: PHASE DHCP %A 1 1 !
41: CONST DHCP : ND% SB : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): DHCP, type code %A, sha256 `e0bd292dd8aa41ad…`

~~~~text
40: PHASE DHCP %A 1 1 !
41: CONST DHCP : ND : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## FCC_A1 (Nd–Sb)

- Id: `phase:nd-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:fcc-a1)

Names (3): _corpus: _corpus:phase:nd-sb:fcc-a1  
_tdb: _tdb:NdSb-16Wan.tdb:FCC_A1, tdb:NdSb-92Cac-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): FCC_A1, type code %A, sha256 `d8f37ff02b888b96…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : ND SB : VA : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): FCC_A1, type code %A, sha256 `e0bd292dd8aa41ad…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : ND SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## HCP_A3 (Nd–Sb)

- Id: `phase:nd-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:nd-sb:hcp-a3  
_tdb: _tdb:NdSb-16Wan.tdb:HCP_A3, tdb:NdSb-92Cac-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): HCP_A3, type code %A, sha256 `d8f37ff02b888b96…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : ND SB : VA : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): HCP_A3, type code %A, sha256 `e0bd292dd8aa41ad…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : ND SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## LIQUID (Nd–Sb)

- Id: `phase:nd-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 873.22–2500 K, x(Sb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:liquid)

Names (3): _corpus: _corpus:phase:nd-sb:liquid  
_tdb: _tdb:NdSb-16Wan.tdb:LIQUID, tdb:NdSb-92Cac-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): LIQUID, type code %, sha256 `d8f37ff02b888b96…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : ND SB : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): LIQUID, type code %, sha256 `e0bd292dd8aa41ad…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : ND SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## ND2SB (Nd–Sb)

- Id: `phase:nd-sb:nd2sb`; status `assigned`
- Structure: La2Sb · tI12 · I4/mmm (139); type `st:la2sb-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Nd 0.6667, Sb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1432.11 K, x(Sb) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:nd2sb)

Names (3): _corpus: _corpus:phase:nd-sb:nd2sb  
_tdb: _tdb:NdSb-16Wan.tdb:ND2SB, tdb:NdSb-92Cac-LB.tdb:ND2SB  


### TDB models of ND2SB (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): ND2SB, type code %, sha256 `d8f37ff02b888b96…`

~~~~text
50: PHASE ND2SB % 2 2 1 !
51: CONST ND2SB : ND : SB : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): ND2SB, type code %, sha256 `e0bd292dd8aa41ad…`

~~~~text
50: PHASE ND2SB % 2 2 1 !
51: CONST ND2SB : ND : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## ND4SB3_D73 (Nd–Sb)

- Id: `phase:nd-sb:nd4sb3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Nd 0.5714, Sb 0.4286
- Stability: stable in 2 of 2 calculated diagram(s): 300–2073.1 K, x(Sb) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:nd4sb3-d73)

Names (3): _corpus: _corpus:phase:nd-sb:nd4sb3-d73  
_tdb: _tdb:NdSb-16Wan.tdb:ND4SB3_D73, tdb:NdSb-92Cac-LB.tdb:ND4SB3_D73  


### TDB models of ND4SB3_D73 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): ND4SB3_D73, type code %, sha256 `d8f37ff02b888b96…`

~~~~text
60: PHASE ND4SB3_D73 % 2 4 3 !
61: CONST ND4SB3_D73 : ND : SB : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): ND4SB3_D73, type code %, sha256 `e0bd292dd8aa41ad…`

~~~~text
60: PHASE ND4SB3_D73 % 2 4 3 !
61: CONST ND4SB3_D73 : ND : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## ND5SB3_D88 (Nd–Sb)

- Id: `phase:nd-sb:nd5sb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacpqoh and oqmd-30814, space group 193
- Stoichiometry: Nd 0.6250, Sb 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–1962.94 K, x(Sb) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:nd5sb3-d88)

Names (5): _corpus: _corpus:phase:nd-sb:nd5sb3-d88  
_mp: _mp:mp-aaacpqoh  
_oqmd: _oqmd:oqmd-30814  
_tdb: _tdb:NdSb-16Wan.tdb:ND5SB3_D88, tdb:NdSb-92Cac-LB.tdb:ND5SB3_D88  


### TDB models of ND5SB3_D88 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): ND5SB3_D88, type code %, sha256 `d8f37ff02b888b96…`

~~~~text
55: PHASE ND5SB3_D88 % 2 5 3 !
56: CONST ND5SB3_D88 : ND : SB : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): ND5SB3_D88, type code %, sha256 `e0bd292dd8aa41ad…`

~~~~text
55: PHASE ND5SB3_D88 % 2 5 3 !
56: CONST ND5SB3_D88 : ND : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## NDSB_B1 (Nd–Sb)

- Id: `phase:nd-sb:ndsb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacja and oqmd-646231, space group 225
- Stoichiometry: Nd 0.5000, Sb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2347.96 K, x(Sb) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:ndsb-b1)

Names (5): _corpus: _corpus:phase:nd-sb:ndsb-b1  
_mp: _mp:mp-aaaaacja  
_oqmd: _oqmd:oqmd-646231  
_tdb: _tdb:NdSb-16Wan.tdb:NDSB_B1, tdb:NdSb-92Cac-LB.tdb:NDSB_B1  


### TDB models of NDSB_B1 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): NDSB_B1, type code %, sha256 `d8f37ff02b888b96…`

~~~~text
65: PHASE NDSB_B1 % 2 1 1 !
66: CONST NDSB_B1 : ND : SB : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): NDSB_B1, type code %, sha256 `e0bd292dd8aa41ad…`

~~~~text
65: PHASE NDSB_B1 % 2 1 1 !
66: CONST NDSB_B1 : ND : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## NDSB2 (Nd–Sb)

- Id: `phase:nd-sb:ndsb2`; status `assigned`
- Structure: Sb2Sm · oC24 · Cmce (64); type `st:sb2sm-oc24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_64_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Nd 0.3333, Sb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1922.96 K, x(Sb) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-sb:ndsb2)

Names (3): _corpus: _corpus:phase:nd-sb:ndsb2  
_tdb: _tdb:NdSb-16Wan.tdb:NDSB2, tdb:NdSb-92Cac-LB.tdb:NDSB2  


### TDB models of NDSB2 (2): PHASE and CONSTITUENT statements as written

[NdSb-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-16Wan.tdb): NDSB2, type code %, sha256 `d8f37ff02b888b96…`

~~~~text
70: PHASE NDSB2 % 2 1 2 !
71: CONST NDSB2 : ND : SB : !
~~~~

[NdSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdSb-92Cac-LB.tdb): NDSB2, type code %, sha256 `e0bd292dd8aa41ad…`

~~~~text
70: PHASE NDSB2 % 2 1 2 !
71: CONST NDSB2 : ND : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

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
