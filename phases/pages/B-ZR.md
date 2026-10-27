# B–Zr phases

> B–Zr system: 10 phases (tier A 5, tier C 3, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/B-ZR.md

10 phases (tier A 5, tier C 3, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/B-ZR.json) · [B–Zr system page](https://data.orchid-project.org/systems/B-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Zr system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-zr-b-beta-rhombo); _phase:b-zr:b-beta-rhombo_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–3999.22 K, x(B) 0.97882–1 | 10 | 5 |
| [BCC_A2](#phase-b-zr-bcc-a2); _phase:b-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 1138.77–3999.1 K, x(B) 0–0.01085 | 11 | 5 |
| [MB2_C32](#phase-b-zr-c32-mb2); _phase:b-zr:c32-mb2_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–3517.94 K, x(B) 0.66637–0.6745 | 22 | 4 |
| [FCC_A1](#phase-b-zr-fcc-a1); _phase:b-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-b-zr-hcp-a3); _phase:b-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2123.99 K, x(B) 0–0.01109 | 0 | 5 |
| [LIQUID](#phase-b-zr-liquid); _phase:b-zr:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1934.13–4000 K, x(B) 0–1 | 24 | 5 |
| [ZRB](#phase-b-zr-zrb); _phase:b-zr:zrb_ | FeB · B27 · oP8 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1523.36 K, x(B) 0.5–0.5 | 7 | 3 |
| [ZRB_B1](#phase-b-zr-zrb-b1); _phase:b-zr:zrb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1521.96 K, x(B) 0.5–0.5 | 2 | 1 |
| [ZRB12_D2F](#phase-b-zr-zrb12-d2f); _phase:b-zr:zrb12-d2f_ | UB12 · D2_f · cF52 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 1972.97–2363.33 K, x(B) 0.92308–0.92308 | 18 | 5 |
| [ZRB2_C32](#phase-b-zr-zrb2-c32); _phase:b-zr:zrb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3503.49 K, x(B) 0.66667–0.66667 | 10 | 1 |

## BETA_RHOMBO_B (B–Zr)

- Id: `phase:b-zr:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ZrB-08Tok.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ZrB-09Che.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ZrB-11Cac.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ZrB-19Pan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ZrB-98Dus-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 5 of 5 calculated diagram(s): 300–3999.22 K, x(B) 0.97882–1
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:b-beta-rhombo)

Names (11): _corpus: _corpus:phase:b-zr:b-beta-rhombo, corpus:phase:b-zr:beta-rhombo-b  
_paper: _paper:10.1007/s11669-019-00728-w:(βB), paper:10.1007/s11669-019-00728-w:β-B, paper:10.1016/j.calphad.2011.10.003:B, paper:10.1016/j.jallcom.2008.01.061:β-B  
_tdb: _tdb:ZrB-08Tok.tdb:BETA_RHOMBO_B, tdb:ZrB-09Che.tdb:BETA_RHOMBO_B, tdb:ZrB-11Cac.tdb:BETA_RHOMBO_B, tdb:ZrB-19Pan.tdb:BETA_RHOMBO_B, tdb:ZrB-98Dus-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (5): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): BETA_RHOMBO_B, type code %, sha256 `242f40ef15d7797c…`

~~~~text
50: PHASE BETA_RHOMBO_B % 1 1 !
51: CONST BETA_RHOMBO_B : B : !
~~~~

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): BETA_RHOMBO_B, type code %, sha256 `8aa5d97abe833f81…`

~~~~text
44: PHASE BETA_RHOMBO_B % 2 93 12 !
45: CONST BETA_RHOMBO_B : B : B% ZR : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): BETA_RHOMBO_B, type code %, sha256 `17839f62b1d76015…`

~~~~text
47: PHASE BETA_RHOMBO_B % 1 1 !
48: CONST BETA_RHOMBO_B : B : !
~~~~

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): BETA_RHOMBO_B, type code %, sha256 `4c066caf80ae004c…`

~~~~text
53: PHASE BETA_RHOMBO_B % 2 93 12 !
54: CONST BETA_RHOMBO_B : B : B% ZR : !
~~~~

[ZrB-98Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-98Dus-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `c388186725057c68…`

~~~~text
42: PHASE BETA_RHOMBO_B % 1 1 !
43: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase_

## BCC_A2 (B–Zr)

- Id: `phase:b-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1138.77–3999.1 K, x(B) 0–0.01085
- Literature: 11 values (11 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:bcc-a2)

Names (9): _corpus: _corpus:phase:b-zr:bcc-a2  
_paper: _paper:10.1007/s11669-019-00728-w:(βZr), paper:10.1016/j.calphad.2011.10.003:bcc-Zr, paper:10.1016/j.jallcom.2008.01.061:bcc-Zr  
_tdb: _tdb:ZrB-08Tok.tdb:BCC_A2, tdb:ZrB-09Che.tdb:BCC_A2, tdb:ZrB-11Cac.tdb:BCC_A2, tdb:ZrB-19Pan.tdb:BCC_A2, tdb:ZrB-98Dus-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): BCC_A2, type code %B, sha256 `242f40ef15d7797c…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : ZR% B : VA : !
~~~~

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): BCC_A2, type code %B, sha256 `8aa5d97abe833f81…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : ZR : B VA% : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): BCC_A2, type code %B, sha256 `17839f62b1d76015…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : ZR : B VA% : !
~~~~

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): BCC_A2, type code %B, sha256 `4c066caf80ae004c…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : ZR : B VA% : !
~~~~

[ZrB-98Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-98Dus-LB.tdb): BCC_A2, type code %B, sha256 `c388186725057c68…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : ZR : B VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase_

## MB2_C32 (B–Zr)

- Id: `phase:b-zr:c32-mb2`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MB2); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 4 of 4 calculated diagram(s): 300–3517.94 K, x(B) 0.66637–0.6745
- Literature: 22 values (22 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:c32-mb2)

Names (9): _corpus: _corpus:phase:b-zr:c32-mb2, corpus:phase:b-zr:mb2-c32  
_paper: _paper:10.1016/j.calphad.2011.10.003:ZrB2, paper:10.1016/j.jallcom.2008.01.061:ZrB2, paper:10.2320/matertrans.mb200809:ZrB2  
_tdb: _tdb:ZrB-08Tok.tdb:MB2_C32, tdb:ZrB-09Che.tdb:MB2_C32, tdb:ZrB-11Cac.tdb:MB2_C32, tdb:ZrB-98Dus-LB.tdb:MB2_C32  


### TDB models of MB2_C32 (4): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): MB2_C32, type code %, sha256 `242f40ef15d7797c…`

~~~~text
60: PHASE MB2_C32 % 2 1 2 !
61: CONST MB2_C32 : VA ZR% : B% VA : !
~~~~

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): MB2_C32, type code %, sha256 `8aa5d97abe833f81…`

~~~~text
54: PHASE MB2_C32 % 2 1 2 !
55: CONST MB2_C32 : ZR : B : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): MB2_C32, type code %, sha256 `17839f62b1d76015…`

~~~~text
57: PHASE MB2_C32 % 2 1 2 !
58: CONST MB2_C32 : VA ZR% : B : !
~~~~

[ZrB-98Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-98Dus-LB.tdb): MB2_C32, type code %, sha256 `c388186725057c68…`

~~~~text
47: PHASE MB2_C32 % 2 1 2 !
48: CONST MB2_C32 : ZR : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j100792a052](https://doi.org/10.1021/j100792a052) Elmer J. Huber, Earl L. Head, Charles E. Holley, The Heats of Formation of Zirconium Diboride and Dioxide \<sup>1\</sup>, J. Phys. Chem. 68, 3040-3042 (1964).  
_cited as the source of values for this phase_
- [doi:10.1021/je60032a044](https://doi.org/10.1021/je60032a044) Gerald K. Johnson, Elliott Greenberg, John L. Margrave, Ward N. Hubbard, Fluorine bomb calorimetry. Enthalpies of formation of the diborides of ziconium and hafnium, J. Chem. Eng. Data 12, 137-141 (1967).  
_cited as the source of values for this phase_

## FCC_A1 (B–Zr)

- Id: `phase:b-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:fcc-a1)

Names (6): _corpus: _corpus:phase:b-zr:fcc-a1  
_tdb: _tdb:ZrB-08Tok.tdb:FCC_A1, tdb:ZrB-09Che.tdb:FCC_A1, tdb:ZrB-11Cac.tdb:FCC_A1, tdb:ZrB-19Pan.tdb:FCC_A1, tdb:ZrB-98Dus-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): FCC_A1, type code %A, sha256 `242f40ef15d7797c…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : ZR B : VA : !
~~~~

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): FCC_A1, type code %A, sha256 `8aa5d97abe833f81…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : ZR : B VA% : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): FCC_A1, type code %A, sha256 `17839f62b1d76015…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : ZR : B VA% : !
~~~~

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): FCC_A1, type code %A, sha256 `4c066caf80ae004c…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : ZR : B VA% : !
~~~~

[ZrB-98Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-98Dus-LB.tdb): FCC_A1, type code %A, sha256 `c388186725057c68…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : ZR : B VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase_

## HCP_A3 (B–Zr)

- Id: `phase:b-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2123.99 K, x(B) 0–0.01109
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:hcp-a3)

Names (6): _corpus: _corpus:phase:b-zr:hcp-a3  
_tdb: _tdb:ZrB-08Tok.tdb:HCP_A3, tdb:ZrB-09Che.tdb:HCP_A3, tdb:ZrB-11Cac.tdb:HCP_A3, tdb:ZrB-19Pan.tdb:HCP_A3, tdb:ZrB-98Dus-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): HCP_A3, type code %A, sha256 `242f40ef15d7797c…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : ZR% B : VA : !
~~~~

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): HCP_A3, type code %A, sha256 `8aa5d97abe833f81…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : ZR : B VA% : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): HCP_A3, type code %A, sha256 `17839f62b1d76015…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : ZR : B VA% : !
~~~~

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): HCP_A3, type code %A, sha256 `4c066caf80ae004c…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : ZR : B VA% : !
~~~~

[ZrB-98Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-98Dus-LB.tdb): HCP_A3, type code %A, sha256 `c388186725057c68…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : ZR : B VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase_

## LIQUID (B–Zr)

- Id: `phase:b-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1934.13–4000 K, x(B) 0–1
- Literature: 24 values (24 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:liquid)

Names (9): _corpus: _corpus:phase:b-zr:liquid  
_paper: _paper:10.1007/s11669-019-00728-w:L, paper:10.1016/j.calphad.2011.10.003:L, paper:10.1016/j.jallcom.2008.01.061:L  
_tdb: _tdb:ZrB-08Tok.tdb:LIQUID, tdb:ZrB-09Che.tdb:LIQUID, tdb:ZrB-11Cac.tdb:LIQUID, tdb:ZrB-19Pan.tdb:LIQUID, tdb:ZrB-98Dus-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): LIQUID, type code %, sha256 `242f40ef15d7797c…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : B ZR : !
~~~~

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): LIQUID, type code %, sha256 `8aa5d97abe833f81…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B ZR : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): LIQUID, type code %, sha256 `17839f62b1d76015…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : B ZR : !
~~~~

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): LIQUID, type code %, sha256 `4c066caf80ae004c…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : B ZR : !
~~~~

[ZrB-98Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-98Dus-LB.tdb): LIQUID, type code %, sha256 `c388186725057c68…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : B ZR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase_

## ZRB (B–Zr)

- Id: `phase:b-zr:zrb`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5000, Zr 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1523.36 K, x(B) 0.5–0.5
- Literature: 7 values (7 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:zrb)

Names (8): _corpus: _corpus:phase:b-zr:zrb  
_paper: _paper:10.1007/s11669-019-00728-w:ZrB, paper:10.1016/j.calphad.2011.10.003:ZrB, paper:10.2320/matertrans.mb200809:ZrB(FeB-type), paper:10.2320/matertrans.mb200809:ZrB(NaCl-type)  
_tdb: _tdb:ZrB-08Tok.tdb:ZRB, tdb:ZrB-11Cac.tdb:ZRB, tdb:ZrB-19Pan.tdb:ZRB  


### TDB models of ZRB (3): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): ZRB, type code %, sha256 `242f40ef15d7797c…`

~~~~text
55: PHASE ZRB % 2 1 1 !
56: CONST ZRB : ZR : B : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): ZRB, type code %, sha256 `17839f62b1d76015…`

~~~~text
52: PHASE ZRB % 2 1 1 !
53: CONST ZRB : ZR : B : !
~~~~

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): ZRB, type code %, sha256 `4c066caf80ae004c…`

~~~~text
58: PHASE ZRB % 2 1 1 !
59: CONST ZRB : ZR : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(88)90021-1](https://doi.org/10.1016/0364-5916%2888%2990021-1) P. Rogl and P. E. Potter: Calphad 12 (1988) 191–204.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_cited as the source of values for this phase_

## ZRB_B1 (B–Zr)

- Id: `phase:b-zr:zrb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5000, Zr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1521.96 K, x(B) 0.5–0.5
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:zrb-b1)

Names (3): _corpus: _corpus:phase:b-zr:zrb-b1  
_paper: _paper:10.1016/j.jallcom.2008.01.061:ZrB  
_tdb: _tdb:ZrB-09Che.tdb:ZRB_B1  


### TDB models of ZRB_B1 (1): PHASE and CONSTITUENT statements as written

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): ZRB_B1, type code %, sha256 `8aa5d97abe833f81…`

~~~~text
49: PHASE ZRB_B1 % 2 1 1 !
50: CONST ZRB_B1 : ZR : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase; reports values for this phase_

## ZRB12_D2F (B–Zr)

- Id: `phase:b-zr:zrb12-d2f`; status `assigned`
- Structure: UB12 · D2_f · cF52 · Fm-3m (225); type `st:d2-f-ub12-cf52`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.9231, Zr 0.0769
- Stability: stable in 5 of 5 calculated diagram(s): 1972.97–2363.33 K, x(B) 0.92308–0.92308
- Literature: 18 values (18 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:zrb12-d2f)

Names (10): _corpus: _corpus:phase:b-zr:zrb12-d2f  
_paper: _paper:10.1007/s11669-019-00728-w:ZrB12, paper:10.1016/j.calphad.2011.10.003:ZrB12, paper:10.1016/j.jallcom.2008.01.061:ZrB12, paper:10.2320/matertrans.mb200809:ZrB12  
_tdb: _tdb:ZrB-08Tok.tdb:ZRB12_D2F, tdb:ZrB-09Che.tdb:ZRB12_D2F, tdb:ZrB-11Cac.tdb:ZRB12_D2F, tdb:ZrB-19Pan.tdb:ZRB12_D2F, tdb:ZrB-98Dus-LB.tdb:ZRB12_D2F  


### TDB models of ZRB12_D2F (5): PHASE and CONSTITUENT statements as written

[ZrB-08Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-08Tok.tdb): ZRB12_D2F, type code %, sha256 `242f40ef15d7797c…`

~~~~text
65: PHASE ZRB12_D2F % 2 1 12 !
66: CONST ZRB12_D2F : ZR : B : !
~~~~

[ZrB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-09Che.tdb): ZRB12_D2F, type code %, sha256 `8aa5d97abe833f81…`

~~~~text
59: PHASE ZRB12_D2F % 2 1 12 !
60: CONST ZRB12_D2F : ZR : B : !
~~~~

[ZrB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-11Cac.tdb): ZRB12_D2F, type code %, sha256 `17839f62b1d76015…`

~~~~text
62: PHASE ZRB12_D2F % 2 1 12 !
63: CONST ZRB12_D2F : ZR : B : !
~~~~

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): ZRB12_D2F, type code %, sha256 `4c066caf80ae004c…`

~~~~text
68: PHASE ZRB12_D2F % 2 1 12 !
69: CONST ZRB12_D2F : ZR : B : !
~~~~

[ZrB-98Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-98Dus-LB.tdb): ZRB12_D2F, type code %, sha256 `c388186725057c68…`

~~~~text
52: PHASE ZRB12_D2F % 2 1 12 !
53: CONST ZRB12_D2F : ZR : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.MB200809](https://doi.org/10.2320/matertrans.MB200809) T. Tokunaga, K. Terashima, H. Ohtani, M. Hasebe, Mater. Trans. JIM, 49, 2534-40(2008).  
_assessment that models this phase; reports values for this phase_

## ZRB2_C32 (B–Zr)

- Id: `phase:b-zr:zrb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.6667, Zr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–3503.49 K, x(B) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-zr:zrb2-c32)

Names (3): _corpus: _corpus:phase:b-zr:zrb2-c32  
_paper: _paper:10.1007/s11669-019-00728-w:ZrB2  
_tdb: _tdb:ZrB-19Pan.tdb:ZRB2_C32  


### TDB models of ZRB2_C32 (1): PHASE and CONSTITUENT statements as written

[ZrB-19Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrB-19Pan.tdb): ZRB2_C32, type code %, sha256 `4c066caf80ae004c…`

~~~~text
63: PHASE ZRB2_C32 % 2 1 2 !
64: CONST ZRB2_C32 : ZR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00728-w](https://doi.org/10.1007/s11669-019-00728-w) Yafei Pan, Cong Zhang, Jiuxing Zhang, Lei Huang, Xinyu Yang, Yong Du et al., Thermodynamic Modeling of the B-Ti-Zr System Over the Whole Composition and Temperature Ranges, J. Phase Equilib. Diffus. 40, 364-374 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.01.061](https://doi.org/10.1016/j.jallcom.2008.01.061) H.M. Chen, F. Zheng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic assessment of B–Zr and Si–Zr binary systems, Journal of Alloys and Compounds 468, 209-216 (2009).  
_cited as the source of values for this phase_

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
