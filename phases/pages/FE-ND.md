# Fe–Nd phases

> Fe–Nd system: 7 phases (tier A 4, tier C 2, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-ND.html · Markdown: https://data.orchid-project.org/phases/pages/FE-ND.md

7 phases (tier A 4, tier C 2, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-ND) · [full JSON](https://data.orchid-project.org/phases/systems/FE-ND.json) · [Fe–Nd system page](https://data.orchid-project.org/systems/FE-ND.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-ND.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Nd system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-nd-bcc-a2); _phase:fe-nd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2498.99 K, x(Nd) 0–1 | 0 | 3 |
| [DHCP](#phase-fe-nd-dhcp-a3); _phase:fe-nd:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1283 K, x(Nd) 0.99589–1 | 0 | 3 |
| [FCC_A1](#phase-fe-nd-fcc-a1); _phase:fe-nd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1132.83–1670.86 K, x(Nd) 0–0.01579 | 0 | 3 |
| [FE17ND2](#phase-fe-nd-fe17nd2); _phase:fe-nd:fe17nd2_ | Th2Zn17 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1490 K, x(Nd) 0.10526–0.10526 | 0 | 3 |
| [FE17ND5](#phase-fe-nd-fe17nd5); _phase:fe-nd:fe17nd5_ | Fe17Nd5 · hP264 · P6_3/mcm (193) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1071.03 K, x(Nd) 0.22727–0.22727 | 0 | 3 |
| [HCP_A3](#phase-fe-nd-hcp-a3); _phase:fe-nd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-fe-nd-liquid); _phase:fe-nd:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 952.68–2500 K, x(Nd) 0–1 | 0 | 3 |

## BCC_A2 (Fe–Nd)

- Id: `phase:fe-nd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2498.99 K, x(Nd) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nd:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-nd:bcc-a2  
_tdb: _tdb:FeNd-16Che.tdb:BCC_A2, tdb:FeNd-16Wan.tdb:BCC_A2, tdb:FeNd-95Hal-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[FeNd-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Che.tdb): BCC_A2, type code %B, sha256 `e50d3fee1b48c398…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% ND% : VA : !
~~~~

[FeNd-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Wan.tdb): BCC_A2, type code %B, sha256 `fa02ac1db21fdc42…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% ND% : VA : !
~~~~

[FeNd-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-95Hal-LB.tdb): BCC_A2, type code %B, sha256 `ab4a9e90b16a414a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% ND% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## DHCP (Fe–Nd)

- Id: `phase:fe-nd:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1283 K, x(Nd) 0.99589–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nd:dhcp-a3)

Names (4): _corpus: _corpus:phase:fe-nd:dhcp-a3  
_tdb: _tdb:FeNd-16Che.tdb:DHCP, tdb:FeNd-16Wan.tdb:DHCP, tdb:FeNd-95Hal-LB.tdb:DHCP  


### TDB models of DHCP (3): PHASE and CONSTITUENT statements as written

[FeNd-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Che.tdb): DHCP, type code %, sha256 `e50d3fee1b48c398…`

~~~~text
45: PHASE DHCP % 1 1 !
46: CONST DHCP : ND : !
~~~~

[FeNd-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Wan.tdb): DHCP, type code %, sha256 `fa02ac1db21fdc42…`

~~~~text
45: PHASE DHCP % 1 1 !
46: CONST DHCP : FE ND% : !
~~~~

[FeNd-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-95Hal-LB.tdb): DHCP, type code %, sha256 `ab4a9e90b16a414a…`

~~~~text
40: PHASE DHCP % 1 1 !
41: CONST DHCP : ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## FCC_A1 (Fe–Nd)

- Id: `phase:fe-nd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1132.83–1670.86 K, x(Nd) 0–0.01579
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nd:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-nd:fcc-a1  
_tdb: _tdb:FeNd-16Che.tdb:FCC_A1, tdb:FeNd-16Wan.tdb:FCC_A1, tdb:FeNd-95Hal-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[FeNd-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Che.tdb): FCC_A1, type code %A, sha256 `e50d3fee1b48c398…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% ND : VA : !
~~~~

[FeNd-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Wan.tdb): FCC_A1, type code %A, sha256 `fa02ac1db21fdc42…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% ND : VA : !
~~~~

[FeNd-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-95Hal-LB.tdb): FCC_A1, type code %A, sha256 `ab4a9e90b16a414a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% ND : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## FE17ND2 (Fe–Nd)

- Id: `phase:fe-nd:fe17nd2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.8947, Nd 0.1053
- Stability: stable in 3 of 3 calculated diagram(s): 300–1490 K, x(Nd) 0.10526–0.10526
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nd:fe17nd2)

Names (4): _corpus: _corpus:phase:fe-nd:fe17nd2  
_tdb: _tdb:FeNd-16Che.tdb:FE17ND2, tdb:FeNd-16Wan.tdb:FE17ND2, tdb:FeNd-95Hal-LB.tdb:FE17ND2  


### TDB models of FE17ND2 (3): PHASE and CONSTITUENT statements as written

[FeNd-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Che.tdb): FE17ND2, type code %A, sha256 `e50d3fee1b48c398…`

~~~~text
50: PHASE FE17ND2 %A 2 17 2 !
51: CONST FE17ND2 : FE : ND : !
~~~~

[FeNd-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Wan.tdb): FE17ND2, type code %A, sha256 `fa02ac1db21fdc42…`

~~~~text
50: PHASE FE17ND2 %A 2 17 2 !
51: CONST FE17ND2 : FE : ND : !
~~~~

[FeNd-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-95Hal-LB.tdb): FE17ND2, type code %A, sha256 `ab4a9e90b16a414a…`

~~~~text
45: PHASE FE17ND2 %A 2 17 2 !
46: CONST FE17ND2 : FE : ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## FE17ND5 (Fe–Nd)

- Id: `phase:fe-nd:fe17nd5`; status `assigned`
- Structure: Fe17Nd5 · hP264 · P6_3/mcm (193); type `st:fe17nd5-hp264`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7727, Nd 0.2273
- Stability: stable in 3 of 3 calculated diagram(s): 300–1071.03 K, x(Nd) 0.22727–0.22727
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nd:fe17nd5)

Names (4): _corpus: _corpus:phase:fe-nd:fe17nd5  
_tdb: _tdb:FeNd-16Che.tdb:FE17ND5, tdb:FeNd-16Wan.tdb:FE17ND5, tdb:FeNd-95Hal-LB.tdb:FE17ND5  


### TDB models of FE17ND5 (3): PHASE and CONSTITUENT statements as written

[FeNd-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Che.tdb): FE17ND5, type code %A, sha256 `e50d3fee1b48c398…`

~~~~text
55: PHASE FE17ND5 %A 2 17 5 !
56: CONST FE17ND5 : FE : ND : !
~~~~

[FeNd-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Wan.tdb): FE17ND5, type code %A, sha256 `fa02ac1db21fdc42…`

~~~~text
55: PHASE FE17ND5 %A 2 17 5 !
56: CONST FE17ND5 : FE : ND : !
~~~~

[FeNd-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-95Hal-LB.tdb): FE17ND5, type code %A, sha256 `ab4a9e90b16a414a…`

~~~~text
50: PHASE FE17ND5 %A 2 17 5 !
51: CONST FE17ND5 : FE : ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## HCP_A3 (Fe–Nd)

- Id: `phase:fe-nd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nd:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-nd:hcp-a3  
_tdb: _tdb:FeNd-16Che.tdb:HCP_A3, tdb:FeNd-16Wan.tdb:HCP_A3, tdb:FeNd-95Hal-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[FeNd-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Che.tdb): HCP_A3, type code %A, sha256 `e50d3fee1b48c398…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE ND : VA : !
~~~~

[FeNd-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Wan.tdb): HCP_A3, type code %A, sha256 `fa02ac1db21fdc42…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE ND : VA : !
~~~~

[FeNd-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-95Hal-LB.tdb): HCP_A3, type code %A, sha256 `ab4a9e90b16a414a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE ND : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## LIQUID (Fe–Nd)

- Id: `phase:fe-nd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 952.68–2500 K, x(Nd) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nd:liquid)

Names (4): _corpus: _corpus:phase:fe-nd:liquid  
_tdb: _tdb:FeNd-16Che.tdb:LIQUID, tdb:FeNd-16Wan.tdb:LIQUID, tdb:FeNd-95Hal-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[FeNd-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Che.tdb): LIQUID, type code %, sha256 `e50d3fee1b48c398…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE ND : !
~~~~

[FeNd-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-16Wan.tdb): LIQUID, type code %, sha256 `fa02ac1db21fdc42…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE ND : !
~~~~

[FeNd-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNd-95Hal-LB.tdb): LIQUID, type code %, sha256 `ab4a9e90b16a414a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2015333](https://doi.org/10.2320/matertrans.M2015333) W. Wang, T. Liu, H. Song, S. Xue, W. Zhang, H. Zhang, L. Zhang, Y. Jia, N. Wang, X. Cheng, C. Zeng, Mater. Trans. (JIM), 57, 103-11(2016).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
