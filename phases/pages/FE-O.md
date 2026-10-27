# Fe–O phases

> Fe–O system: 10 phases (tier A 4, tier C 2, liquid 2, gas 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-O.html · Markdown: https://data.orchid-project.org/phases/pages/FE-O.md

10 phases (tier A 4, tier C 2, liquid 2, gas 2); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-O) · [full JSON](https://data.orchid-project.org/phases/systems/FE-O.json) · [Fe–O system page](https://data.orchid-project.org/systems/FE-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–O system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HALITE_B1](#phase-fe-o-b1-halite); _phase:fe-o:b1-halite_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 832.32–1695.47 K, x(O) 0.51203–0.54514 | 0 | 8 |
| [BCC_A2](#phase-fe-o-bcc-a2); _phase:fe-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1810.92 K, x(O) 0–0.00029 | 0 | 8 |
| [CORUNDUM_D51](#phase-fe-o-d51-corundum); _phase:fe-o:d51-corundum_ | alpha-Al2O3 · D5_1 · hR10 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1725.46 K, x(O) 0.6–0.6 | 0 | 8 |
| [FCC_A1](#phase-fe-o-fcc-a1); _phase:fe-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 838.66–1802.44 K, x(O) 0–0.0001 | 0 | 8 |
| [GAS](#phase-fe-o-gas); _phase:fe-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 1555.46–2500 K, x(O) 0.99965–1 | 0 | 8 |
| [SPINEL_H11](#phase-fe-o-h11-spinel); _phase:fe-o:h11-spinel_ | Al2MgO4 · H1_1 · cF56 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1869.74 K, x(O) 0.57089–0.57994 | 0 | 8 |
| [HCP_A3](#phase-fe-o-hcp-a3); _phase:fe-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 8 |
| [ION](#phase-fe-o-ion); _phase:fe-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1642.72–2500 K, x(O) 2e-05–0.58105 | 0 | 5 |
| [LIQUID](#phase-fe-o-liquid); _phase:fe-o:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1642.22–2500 K, x(O) 2e-05–0.58105 | 1 | 4 |
| [O2GAS](#phase-fe-o-o2gas); _phase:fe-o:o2gas_ | gas | gas | stable in 1 of 2 calculated diagram(s): 300–445 K, x(O) 1–1 | 0 | 8 |

## HALITE_B1 (Fe–O)

- Id: `phase:fe-o:b1-halite`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 832.32–1695.47 K, x(O) 0.51203–0.54514
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:b1-halite)

Names (9): _corpus: _corpus:phase:fe-o:b1-halite  
_tdb: _tdb:FeO-02Luo.tdb:HALITE_B1, tdb:FeO-09Pov.tdb:HALITE_B1, tdb:FeO-23Jia.tdb:HALITE_B1, tdb:FeO-91Sun-LB.tdb:HALITE_B1, tdb:FeO-91Sun-orig.tdb:HALITE_B1, tdb:FeO-93Tay.tdb:HALITE_B1, tdb:FeO-95Kow.tdb:HALITE_B1, tdb:FeO-96Sel.tdb:HALITE_B1  


### TDB models of HALITE_B1 (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): HALITE_B1, type code %, sha256 `444e225f4fad778c…`

~~~~text
66: PHASE HALITE_B1:I % 2 1 1 !
67: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): HALITE_B1, type code %, sha256 `e44f811ba37703b5…`

~~~~text
68: PHASE HALITE_B1:I % 2 1 1 !
69: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): HALITE_B1, type code %, sha256 `16bc7d5f6d3971df…`

~~~~text
65: PHASE HALITE_B1:I % 2 1 1 !
66: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): HALITE_B1, type code %, sha256 `0670fd1794f0d2b7…`

~~~~text
85: PHASE HALITE_B1:I % 2 1 1 !
86: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): HALITE_B1, type code %, sha256 `214f51010594d665…`

~~~~text
63: PHASE HALITE_B1:I % 2 1 1 !
64: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): HALITE_B1, type code %, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
63: PHASE HALITE_B1:I % 2 1 1 !
64: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): HALITE_B1, type code %, sha256 `4b25481824b6c677…`

~~~~text
66: PHASE HALITE_B1:I % 2 1 1 !
67: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): HALITE_B1, type code %, sha256 `35ab77bc661f3ab6…`

~~~~text
67: PHASE HALITE_B1:I % 2 1 1 !
68: CONST HALITE_B1:I : FE+2% FE+3 VA : O-2 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## BCC_A2 (Fe–O)

- Id: `phase:fe-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1810.92 K, x(O) 0–0.00029
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:bcc-a2)

Names (9): _corpus: _corpus:phase:fe-o:bcc-a2  
_tdb: _tdb:FeO-02Luo.tdb:BCC_A2, tdb:FeO-09Pov.tdb:BCC_A2, tdb:FeO-23Jia.tdb:BCC_A2, tdb:FeO-91Sun-LB.tdb:BCC_A2, tdb:FeO-91Sun-orig.tdb:BCC_A2, tdb:FeO-93Tay.tdb:BCC_A2, tdb:FeO-95Kow.tdb:BCC_A2, tdb:FeO-96Sel.tdb:BCC_A2  


### TDB models of BCC_A2 (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): BCC_A2, type code %B, sha256 `444e225f4fad778c…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : FE : O VA% : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): BCC_A2, type code %B, sha256 `e44f811ba37703b5…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : FE : O VA% : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): BCC_A2, type code %B, sha256 `16bc7d5f6d3971df…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : FE : O VA% : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): BCC_A2, type code %B, sha256 `0670fd1794f0d2b7…`

~~~~text
68: PHASE BCC_A2 %B 2 1 3 !
69: CONST BCC_A2 : FE : O VA% : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): BCC_A2, type code %B, sha256 `214f51010594d665…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : FE O : VA : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): BCC_A2, type code %B, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : FE O : VA : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): BCC_A2, type code %B, sha256 `4b25481824b6c677…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : FE : O VA% : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): BCC_A2, type code %B, sha256 `35ab77bc661f3ab6…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : FE O : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## CORUNDUM_D51 (Fe–O)

- Id: `phase:fe-o:d51-corundum`; status `assigned`
- Structure: alpha-Al2O3 · D5_1 · hR10 · R-3c (167); type `st:d5-1-alpha-al2o3-hr10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:CORUNDUM); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–1725.46 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:d51-corundum)

Names (10): _corpus: _corpus:phase:fe-o:d51-corundum, corpus:phase:fe-o:corundum-d51  
_tdb: _tdb:FeO-02Luo.tdb:CORUNDUM_D51, tdb:FeO-09Pov.tdb:CORUNDUM_D51, tdb:FeO-23Jia.tdb:CORUNDUM_D51, tdb:FeO-91Sun-LB.tdb:CORUNDUM_D51, tdb:FeO-91Sun-orig.tdb:CORUNDUM_D51, tdb:FeO-93Tay.tdb:CORUNDUM_D51, tdb:FeO-95Kow.tdb:CORUNDUM_D51, tdb:FeO-96Sel.tdb:CORUNDUM_D51  


### TDB models of CORUNDUM_D51 (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): CORUNDUM_D51, type code %A, sha256 `444e225f4fad778c…`

~~~~text
60: PHASE CORUNDUM_D51:I %A 2 2 3 !
61: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): CORUNDUM_D51, type code %A, sha256 `e44f811ba37703b5…`

~~~~text
62: PHASE CORUNDUM_D51:I %A 2 2 3 !
63: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): CORUNDUM_D51, type code %A, sha256 `16bc7d5f6d3971df…`

~~~~text
59: PHASE CORUNDUM_D51:I %A 2 2 3 !
60: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): CORUNDUM_D51, type code %A, sha256 `0670fd1794f0d2b7…`

~~~~text
79: PHASE CORUNDUM_D51:I %A 2 2 3 !
80: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): CORUNDUM_D51, type code %A, sha256 `214f51010594d665…`

~~~~text
57: PHASE CORUNDUM_D51:I %A 2 2 3 !
58: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): CORUNDUM_D51, type code %A, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
57: PHASE CORUNDUM_D51:I %A 2 2 3 !
58: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): CORUNDUM_D51, type code %A, sha256 `4b25481824b6c677…`

~~~~text
60: PHASE CORUNDUM_D51:I %A 2 2 3 !
61: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): CORUNDUM_D51, type code %A, sha256 `35ab77bc661f3ab6…`

~~~~text
61: PHASE CORUNDUM_D51:I %A 2 2 3 !
62: CONST CORUNDUM_D51:I : FE+3 : O-2 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## FCC_A1 (Fe–O)

- Id: `phase:fe-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 838.66–1802.44 K, x(O) 0–0.0001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:fcc-a1)

Names (9): _corpus: _corpus:phase:fe-o:fcc-a1  
_tdb: _tdb:FeO-02Luo.tdb:FCC_A1, tdb:FeO-09Pov.tdb:FCC_A1, tdb:FeO-23Jia.tdb:FCC_A1, tdb:FeO-91Sun-LB.tdb:FCC_A1, tdb:FeO-91Sun-orig.tdb:FCC_A1, tdb:FeO-93Tay.tdb:FCC_A1, tdb:FeO-95Kow.tdb:FCC_A1, tdb:FeO-96Sel.tdb:FCC_A1  


### TDB models of FCC_A1 (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): FCC_A1, type code %A, sha256 `444e225f4fad778c…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : FE : O VA% : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): FCC_A1, type code %A, sha256 `e44f811ba37703b5…`

~~~~text
46: PHASE FCC_A1 %A 2 1 1 !
47: CONST FCC_A1 : FE : O VA% : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): FCC_A1, type code %A, sha256 `16bc7d5f6d3971df…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : FE : O VA% : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): FCC_A1, type code %A, sha256 `0670fd1794f0d2b7…`

~~~~text
63: PHASE FCC_A1 %A 2 1 1 !
64: CONST FCC_A1 : FE : O VA% : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): FCC_A1, type code %A, sha256 `214f51010594d665…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : FE O : VA : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): FCC_A1, type code %A, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : FE O : VA : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): FCC_A1, type code %A, sha256 `4b25481824b6c677…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : FE : O VA% : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): FCC_A1, type code %A, sha256 `35ab77bc661f3ab6…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : FE O : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## GAS (Fe–O)

- Id: `phase:fe-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1555.46–2500 K, x(O) 0.99965–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:gas)

Names (9): _corpus: _corpus:phase:fe-o:gas  
_tdb: _tdb:FeO-02Luo.tdb:GAS, tdb:FeO-09Pov.tdb:GAS, tdb:FeO-23Jia.tdb:GAS, tdb:FeO-91Sun-LB.tdb:GAS, tdb:FeO-91Sun-orig.tdb:GAS, tdb:FeO-93Tay.tdb:GAS, tdb:FeO-95Kow.tdb:GAS, tdb:FeO-96Sel.tdb:GAS  


### TDB models of GAS (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): GAS, type code %, sha256 `444e225f4fad778c…`

~~~~text
75: PHASE GAS:G % 1 1 !
76: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): GAS, type code %, sha256 `e44f811ba37703b5…`

~~~~text
77: PHASE GAS:G % 1 1 !
78: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): GAS, type code %, sha256 `16bc7d5f6d3971df…`

~~~~text
74: PHASE GAS:G % 1 1 !
75: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): GAS, type code %, sha256 `0670fd1794f0d2b7…`

~~~~text
94: PHASE GAS:G % 1 1 !
95: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): GAS, type code %, sha256 `214f51010594d665…`

~~~~text
72: PHASE GAS:G % 1 1 !
73: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): GAS, type code %, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
72: PHASE GAS:G % 1 1 !
73: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): GAS, type code %, sha256 `4b25481824b6c677…`

~~~~text
75: PHASE GAS:G % 1 1 !
76: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): GAS, type code %, sha256 `35ab77bc661f3ab6…`

~~~~text
76: PHASE GAS:G % 1 1 !
77: CONST GAS:G : FE FE2 FEO FEO2 O O2% O3 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## SPINEL_H11 (Fe–O)

- Id: `phase:fe-o:h11-spinel`; status `assigned`
- Structure: Al2MgO4 · H1_1 · cF56 · Fd-3m (227); type `st:h1-1-al2mgo4-cf56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:SPINEL); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in FeO-02Luo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeO-09Pov.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeO-23Jia.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeO-91Sun-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeO-91Sun-orig.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeO-93Tay.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeO-95Kow.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeO-96Sel.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1869.74 K, x(O) 0.57089–0.57994
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:h11-spinel)

Names (9): _corpus: _corpus:phase:fe-o:h11-spinel  
_tdb: _tdb:FeO-02Luo.tdb:SPINEL_H11, tdb:FeO-09Pov.tdb:SPINEL_H11, tdb:FeO-23Jia.tdb:SPINEL_H11, tdb:FeO-91Sun-LB.tdb:SPINEL_H11, tdb:FeO-91Sun-orig.tdb:SPINEL_H11, tdb:FeO-93Tay.tdb:SPINEL_H11, tdb:FeO-95Kow.tdb:SPINEL_H11, tdb:FeO-96Sel.tdb:SPINEL_H11  


### TDB models of SPINEL_H11 (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): SPINEL_H11, type code %A, sha256 `444e225f4fad778c…`

~~~~text
72: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
73: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): SPINEL_H11, type code %A, sha256 `e44f811ba37703b5…`

~~~~text
74: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
75: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): SPINEL_H11, type code %A, sha256 `16bc7d5f6d3971df…`

~~~~text
71: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
72: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): SPINEL_H11, type code %A, sha256 `0670fd1794f0d2b7…`

~~~~text
91: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
92: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): SPINEL_H11, type code %A, sha256 `214f51010594d665…`

~~~~text
69: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
70: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): SPINEL_H11, type code %A, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
69: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
70: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): SPINEL_H11, type code %A, sha256 `4b25481824b6c677…`

~~~~text
72: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
73: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): SPINEL_H11, type code %A, sha256 `35ab77bc661f3ab6…`

~~~~text
73: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
74: CONST SPINEL_H11:I : FE+2% FE+3 : FE+2 FE+3% VA : FE+2 VA% : O-2 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## HCP_A3 (Fe–O)

- Id: `phase:fe-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:hcp-a3)

Names (9): _corpus: _corpus:phase:fe-o:hcp-a3  
_tdb: _tdb:FeO-02Luo.tdb:HCP_A3, tdb:FeO-09Pov.tdb:HCP_A3, tdb:FeO-23Jia.tdb:HCP_A3, tdb:FeO-91Sun-LB.tdb:HCP_A3, tdb:FeO-91Sun-orig.tdb:HCP_A3, tdb:FeO-93Tay.tdb:HCP_A3, tdb:FeO-95Kow.tdb:HCP_A3, tdb:FeO-96Sel.tdb:HCP_A3  


### TDB models of HCP_A3 (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): HCP_A3, type code %A, sha256 `444e225f4fad778c…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : FE : VA : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): HCP_A3, type code %A, sha256 `e44f811ba37703b5…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : FE : VA : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): HCP_A3, type code %A, sha256 `16bc7d5f6d3971df…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : FE : VA : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): HCP_A3, type code %A, sha256 `0670fd1794f0d2b7…`

~~~~text
73: PHASE HCP_A3 %A 2 1 0.5 !
74: CONST HCP_A3 : FE : VA : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): HCP_A3, type code %A, sha256 `214f51010594d665…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : FE : VA : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): HCP_A3, type code %A, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : FE : VA : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): HCP_A3, type code %A, sha256 `4b25481824b6c677…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : FE : VA : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): HCP_A3, type code %A, sha256 `35ab77bc661f3ab6…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : FE : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## ION (Fe–O)

- Id: `phase:fe-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1642.72–2500 K, x(O) 2e-05–0.58105
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:ion)

Names (6): _corpus: _corpus:phase:fe-o:ion  
_tdb: _tdb:FeO-09Pov.tdb:ION, tdb:FeO-91Sun-LB.tdb:ION, tdb:FeO-91Sun-orig.tdb:ION, tdb:FeO-93Tay.tdb:ION, tdb:FeO-96Sel.tdb:ION  


### TDB models of ION (5): PHASE and CONSTITUENT statements as written

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): ION, type code %, sha256 `e44f811ba37703b5…`

~~~~text
41: PHASE ION:Y % 2 1 1 !
42: CONST ION:Y : FE+2 FE+3 : O-2 VA : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): ION, type code %, sha256 `0670fd1794f0d2b7…`

~~~~text
55: PHASE ION:Y % 2 1 1 !
56: CONST ION:Y : FE+2 : O-2 VA FEO1.5% : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): ION, type code %, sha256 `214f51010594d665…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : FE+2 FE+3 : O-2 VA : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): ION, type code %, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : FE+2 FE+3 : O-2 VA : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): ION, type code %, sha256 `35ab77bc661f3ab6…`

~~~~text
40: PHASE ION:Y % 2 1 1 !
41: CONST ION:Y : FE+2 : O-2 VA FEO1.5 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## LIQUID (Fe–O)

- Id: `phase:fe-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1642.22–2500 K, x(O) 2e-05–0.58105
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:liquid)

Names (6): _corpus: _corpus:phase:fe-o:liquid  
_paper: _paper:10.1007/bf02645709:liquid  
_tdb: _tdb:FeO-02Luo.tdb:LIQUID, tdb:FeO-23Jia.tdb:LIQUID, tdb:FeO-91Sun-LB.tdb:LIQUID, tdb:FeO-95Kow.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): LIQUID, type code %, sha256 `444e225f4fad778c…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : FE FEO FEO1.5 : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): LIQUID, type code %, sha256 `16bc7d5f6d3971df…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : FE FEO FEO1.5 : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): LIQUID, type code %, sha256 `0670fd1794f0d2b7…`

~~~~text
58: PHASE LIQUID:L % 1 1 !
59: CONST LIQUID:L : FE FEO FEO1.5 : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): LIQUID, type code %, sha256 `4b25481824b6c677…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : FE FEO FEO1.5 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_

## O2GAS (Fe–O)

- Id: `phase:fe-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–445 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-o:o2gas)

Names (9): _corpus: _corpus:phase:fe-o:o2gas  
_tdb: _tdb:FeO-02Luo.tdb:O2GAS, tdb:FeO-09Pov.tdb:O2GAS, tdb:FeO-23Jia.tdb:O2GAS, tdb:FeO-91Sun-LB.tdb:O2GAS, tdb:FeO-91Sun-orig.tdb:O2GAS, tdb:FeO-93Tay.tdb:O2GAS, tdb:FeO-95Kow.tdb:O2GAS, tdb:FeO-96Sel.tdb:O2GAS  


### TDB models of O2GAS (8): PHASE and CONSTITUENT statements as written

[FeO-02Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-02Luo.tdb): O2GAS, type code %, sha256 `444e225f4fad778c…`

~~~~text
78: PHASE O2GAS % 1 1 !
79: CONST O2GAS : O2 : !
~~~~

[FeO-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-09Pov.tdb): O2GAS, type code %, sha256 `e44f811ba37703b5…`

~~~~text
80: PHASE O2GAS % 1 1 !
81: CONST O2GAS : O2 : !
~~~~

[FeO-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-23Jia.tdb): O2GAS, type code %, sha256 `16bc7d5f6d3971df…`

~~~~text
77: PHASE O2GAS % 1 1 !
78: CONST O2GAS : O2 : !
~~~~

[FeO-91Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-LB.tdb): O2GAS, type code %, sha256 `0670fd1794f0d2b7…`

~~~~text
97: PHASE O2GAS % 1 1 !
98: CONST O2GAS : O2 : !
~~~~

[FeO-91Sun-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-91Sun-orig.tdb): O2GAS, type code %, sha256 `214f51010594d665…`

~~~~text
75: PHASE O2GAS % 1 1 !
76: CONST O2GAS : O2 : !
~~~~

[FeO-93Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-93Tay.tdb): O2GAS, type code %, sha256 `b5fe5c3fdd6ae4b4…`

~~~~text
75: PHASE O2GAS % 1 1 !
76: CONST O2GAS : O2 : !
~~~~

[FeO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-95Kow.tdb): O2GAS, type code %, sha256 `4b25481824b6c677…`

~~~~text
78: PHASE O2GAS % 1 1 !
79: CONST O2GAS : O2 : !
~~~~

[FeO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/FeO-96Sel.tdb): O2GAS, type code %, sha256 `35ab77bc661f3ab6…`

~~~~text
79: PHASE O2GAS % 1 1 !
80: CONST O2GAS : O2 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02645709](https://doi.org/10.1007/BF02645709) B. Sundman, J. Phase Equilib., 12, 127-40(1991).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 381-92(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-840511](https://doi.org/10.1515/ijmr-1993-840511) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 84, 335-45(1993).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
