# Mg–Sm phases

> Mg–Sm system: 11 phases (tier A 8, tier C 2, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-SM.html · Markdown: https://data.orchid-project.org/phases/pages/MG-SM.md

11 phases (tier A 8, tier C 2, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-SM) · [full JSON](https://data.orchid-project.org/phases/systems/MG-SM.json) · [Mg–Sm system page](https://data.orchid-project.org/systems/MG-SM.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-SM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Sm system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-sm-bcc-a2); _phase:mg-sm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 852.98–2499.38 K, x(Sm) 0.65113–1 | 9 | 4 |
| [B2_BCC](#phase-mg-sm-bcc-b2); _phase:mg-sm:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.38 K, x(Sm) 0.49923–1 | 0 | 1 |
| [FCC_A1](#phase-mg-sm-fcc-a1); _phase:mg-sm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-mg-sm-hcp-a3); _phase:mg-sm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1340 K, x(Sm) 0–1 | 12 | 3 |
| [LIQUID](#phase-mg-sm-liquid); _phase:mg-sm:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 806.12–2500 K, x(Sm) 0–1 | 46 | 3 |
| [MG2SM_C15](#phase-mg-sm-mg2sm-c15); _phase:mg-sm:mg2sm-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1022.35 K, x(Sm) 0.33333–0.34357 | 19 | 3 |
| [MG3SM_D03](#phase-mg-sm-mg3sm-d03); _phase:mg-sm:mg3sm-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–982.7 K, x(Sm) 0.21593–0.25 | 18 | 3 |
| [MG41SM5](#phase-mg-sm-mg41sm5); _phase:mg-sm:mg41sm5_ | Ce5Mg41 · tI92 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–839.93 K, x(Sm) 0.1087–0.1087 | 14 | 3 |
| [MG5SM](#phase-mg-sm-mg5sm); _phase:mg-sm:mg5sm_ | Cd45Sm11 · cF448 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–860.33 K, x(Sm) 0.16667–0.16667 | 13 | 3 |
| [MGSM_B2](#phase-mg-sm-mgsm-b2); _phase:mg-sm:mgsm-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1345 K, x(Sm) 0.45449–1 | 28 | 2 |
| [RHOMB_C19](#phase-mg-sm-rhomb-c19); _phase:mg-sm:rhomb-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1192.36 K, x(Sm) 0.9504–1 | 2 | 3 |

## BCC_A2 (Mg–Sm)

- Id: `phase:mg-sm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 852.98–2499.38 K, x(Sm) 0.65113–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:bcc-a2)

Names (7): _corpus: _corpus:phase:mg-sm:bcc-a2  
_paper: _paper:10.1007/s11669-024-01111-0:γ-Sm, paper:10.1016/j.jallcom.2007.05.035:Bcc(Sm)  
_tdb: _tdb:MgSm-08Jia.tdb:BCC_A2, tdb:MgSm-10Guo.tdb:A2_BCC, tdb:MgSm-10Guo.tdb:BCC_A2, tdb:MgSm-24Jia.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): BCC_A2, type code %B, sha256 `95e32e81e730e1ee…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MG SM : VA : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): A2_BCC, type code %B, sha256 `74f15429343690e9…`

~~~~text
35: PHASE A2_BCC %B 2 1 3 !
36: CONST A2_BCC : MG SM : VA : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): BCC_A2, type code %B, sha256 `74f15429343690e9…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MG SM : VA : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): BCC_A2, type code %B, sha256 `5a4755c28397807e…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : MG SM : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90169-0](https://doi.org/10.1016/0022-5088%2889%2990169-0) A. Saccone, S. Delfino, G. Borzone, R. Ferro, The samarium-magnesium system: A phase diagram, Journal of the Less Common Metals 154, 47-60 (1989).  
_cited as the source of values for this phase_

## B2_BCC (Mg–Sm)

- Id: `phase:mg-sm:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: MgSm-10Guo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in MgSm-10Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.38 K, x(Sm) 0.49923–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:bcc-b2)

Names (2): _corpus: _corpus:phase:mg-sm:bcc-b2  
_tdb: _tdb:MgSm-10Guo.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): B2_BCC, type code %O, sha256 `74f15429343690e9…`

~~~~text
40: PHASE B2_BCC %O 3 0.5 0.5 3 !
41: CONST B2_BCC : MG% SM : MG SM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_

## FCC_A1 (Mg–Sm)

- Id: `phase:mg-sm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:fcc-a1)

Names (4): _corpus: _corpus:phase:mg-sm:fcc-a1  
_tdb: _tdb:MgSm-08Jia.tdb:FCC_A1, tdb:MgSm-10Guo.tdb:FCC_A1, tdb:MgSm-24Jia.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): FCC_A1, type code %A, sha256 `95e32e81e730e1ee…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MG : VA : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): FCC_A1, type code %A, sha256 `74f15429343690e9…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MG SM : VA : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): FCC_A1, type code %A, sha256 `5a4755c28397807e…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_

## HCP_A3 (Mg–Sm)

- Id: `phase:mg-sm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1340 K, x(Sm) 0–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:hcp-a3)

Names (8): _corpus: _corpus:phase:mg-sm:hcp-a3  
_paper: _paper:10.1007/s11669-024-01111-0:Mg, paper:10.1007/s11669-024-01111-0:β-Sm, paper:10.1016/j.jallcom.2007.05.035:Hcp, paper:10.1016/j.jallcom.2007.05.035:Hcp(Sm)  
_tdb: _tdb:MgSm-08Jia.tdb:HCP_A3, tdb:MgSm-10Guo.tdb:HCP_A3, tdb:MgSm-24Jia.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): HCP_A3, type code %A, sha256 `95e32e81e730e1ee…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MG SM : VA : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): HCP_A3, type code %A, sha256 `74f15429343690e9…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : MG SM : VA : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): HCP_A3, type code %A, sha256 `5a4755c28397807e…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : MG SM : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90169-0](https://doi.org/10.1016/0022-5088%2889%2990169-0) A. Saccone, S. Delfino, G. Borzone, R. Ferro, The samarium-magnesium system: A phase diagram, Journal of the Less Common Metals 154, 47-60 (1989).  
_cited as the source of values for this phase_

## LIQUID (Mg–Sm)

- Id: `phase:mg-sm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 806.12–2500 K, x(Sm) 0–1
- Literature: 46 values (43 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:liquid)

Names (6): _corpus: _corpus:phase:mg-sm:liquid  
_paper: _paper:10.1007/s11669-024-01111-0:L, paper:10.1016/j.jallcom.2007.05.035:L  
_tdb: _tdb:MgSm-08Jia.tdb:LIQUID, tdb:MgSm-10Guo.tdb:LIQUID, tdb:MgSm-24Jia.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): LIQUID, type code %, sha256 `95e32e81e730e1ee…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MG SM : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): LIQUID, type code %, sha256 `74f15429343690e9…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MG SM : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): LIQUID, type code %, sha256 `5a4755c28397807e…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : MG SM : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90169-0](https://doi.org/10.1016/0022-5088%2889%2990169-0) A. Saccone, S. Delfino, G. Borzone, R. Ferro, The samarium-magnesium system: A phase diagram, Journal of the Less Common Metals 154, 47-60 (1989).  
_cited as the source of values for this phase_

## MG2SM_C15 (Mg–Sm)

- Id: `phase:mg-sm:mg2sm-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgSm-24Jia.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1022.35 K, x(Sm) 0.33333–0.34357
- Literature: 19 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:mg2sm-c15)

Names (6): _corpus: _corpus:phase:mg-sm:mg2sm-c15  
_paper: _paper:10.1007/s11669-024-01111-0:Mg2Sm, paper:10.1016/j.jallcom.2007.05.035:Mg2Sm  
_tdb: _tdb:MgSm-08Jia.tdb:MG2SM_C15, tdb:MgSm-10Guo.tdb:MG2SM_C15, tdb:MgSm-24Jia.tdb:MG2SM_C15  


### TDB models of MG2SM_C15 (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): MG2SM_C15, type code %, sha256 `95e32e81e730e1ee…`

~~~~text
65: PHASE MG2SM_C15 % 2 2 1 !
66: CONST MG2SM_C15 : MG : SM : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): MG2SM_C15, type code %, sha256 `74f15429343690e9…`

~~~~text
70: PHASE MG2SM_C15 % 2 2 1 !
71: CONST MG2SM_C15 : MG : SM : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): MG2SM_C15, type code %, sha256 `5a4755c28397807e…`

~~~~text
68: PHASE MG2SM_C15 % 2 2 1 !
69: CONST MG2SM_C15 : MG% SM : MG SM% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90169-0](https://doi.org/10.1016/0022-5088%2889%2990169-0) A. Saccone, S. Delfino, G. Borzone, R. Ferro, The samarium-magnesium system: A phase diagram, Journal of the Less Common Metals 154, 47-60 (1989).  
_cited as the source of values for this phase_

## MG3SM_D03 (Mg–Sm)

- Id: `phase:mg-sm:mg3sm-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–982.7 K, x(Sm) 0.21593–0.25
- Literature: 18 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:mg3sm-d03)

Names (6): _corpus: _corpus:phase:mg-sm:mg3sm-d03  
_paper: _paper:10.1007/s11669-024-01111-0:Mg3Sm, paper:10.1016/j.jallcom.2007.05.035:Mg3Sm  
_tdb: _tdb:MgSm-08Jia.tdb:MG3SM_D03, tdb:MgSm-10Guo.tdb:MG3SM_D03, tdb:MgSm-24Jia.tdb:MG3SM_D03  


### TDB models of MG3SM_D03 (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): MG3SM_D03, type code %, sha256 `95e32e81e730e1ee…`

~~~~text
60: PHASE MG3SM_D03 % 2 3 1 !
61: CONST MG3SM_D03 : MG : SM : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): MG3SM_D03, type code %, sha256 `74f15429343690e9…`

~~~~text
65: PHASE MG3SM_D03 % 2 3 1 !
66: CONST MG3SM_D03 : MG : SM : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): MG3SM_D03, type code %, sha256 `5a4755c28397807e…`

~~~~text
63: PHASE MG3SM_D03 % 2 3 1 !
64: CONST MG3SM_D03 : MG : MG SM% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90169-0](https://doi.org/10.1016/0022-5088%2889%2990169-0) A. Saccone, S. Delfino, G. Borzone, R. Ferro, The samarium-magnesium system: A phase diagram, Journal of the Less Common Metals 154, 47-60 (1989).  
_cited as the source of values for this phase_

## MG41SM5 (Mg–Sm)

- Id: `phase:mg-sm:mg41sm5`; status `assigned`
- Structure: Ce5Mg41 · tI92 · I4/m (87); type `st:ce5mg41-ti92`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.8913, Sm 0.1087
- Stability: stable in 3 of 3 calculated diagram(s): 300–839.93 K, x(Sm) 0.1087–0.1087
- Literature: 14 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:mg41sm5)

Names (6): _corpus: _corpus:phase:mg-sm:mg41sm5  
_paper: _paper:10.1007/s11669-024-01111-0:Mg41Sm5, paper:10.1016/j.jallcom.2007.05.035:Mg41Sm5  
_tdb: _tdb:MgSm-08Jia.tdb:MG41SM5, tdb:MgSm-10Guo.tdb:MG41SM5, tdb:MgSm-24Jia.tdb:MG41SM5  


### TDB models of MG41SM5 (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): MG41SM5, type code %, sha256 `95e32e81e730e1ee…`

~~~~text
50: PHASE MG41SM5 % 2 41 5 !
51: CONST MG41SM5 : MG : SM : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): MG41SM5, type code %, sha256 `74f15429343690e9…`

~~~~text
55: PHASE MG41SM5 % 2 41 5 !
56: CONST MG41SM5 : MG : SM : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): MG41SM5, type code %, sha256 `5a4755c28397807e…`

~~~~text
53: PHASE MG41SM5 % 2 41 5 !
54: CONST MG41SM5 : MG : SM : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90169-0](https://doi.org/10.1016/0022-5088%2889%2990169-0) A. Saccone, S. Delfino, G. Borzone, R. Ferro, The samarium-magnesium system: A phase diagram, Journal of the Less Common Metals 154, 47-60 (1989).  
_cited as the source of values for this phase_

## MG5SM (Mg–Sm)

- Id: `phase:mg-sm:mg5sm`; status `assigned`
- Structure: Cd45Sm11 · cF448 · F-43m (216); type `st:cd45sm11-cf448`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.8333, Sm 0.1667
- Stability: stable in 3 of 3 calculated diagram(s): 300–860.33 K, x(Sm) 0.16667–0.16667
- Literature: 13 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:mg5sm)

Names (6): _corpus: _corpus:phase:mg-sm:mg5sm  
_paper: _paper:10.1007/s11669-024-01111-0:Mg5Sm, paper:10.1016/j.jallcom.2007.05.035:Mg5Sm  
_tdb: _tdb:MgSm-08Jia.tdb:MG5SM, tdb:MgSm-10Guo.tdb:MG5SM, tdb:MgSm-24Jia.tdb:MG5SM  


### TDB models of MG5SM (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): MG5SM, type code %, sha256 `95e32e81e730e1ee…`

~~~~text
55: PHASE MG5SM % 2 5 1 !
56: CONST MG5SM : MG : SM : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): MG5SM, type code %, sha256 `74f15429343690e9…`

~~~~text
60: PHASE MG5SM % 2 5 1 !
61: CONST MG5SM : MG : SM : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): MG5SM, type code %, sha256 `5a4755c28397807e…`

~~~~text
58: PHASE MG5SM % 2 5 1 !
59: CONST MG5SM : MG : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
_assessment that models this phase_

## MGSM_B2 (Mg–Sm)

- Id: `phase:mg-sm:mgsm-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgSm-24Jia.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1345 K, x(Sm) 0.45449–1
- Literature: 28 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:mgsm-b2)

Names (6): _corpus: _corpus:phase:mg-sm:mgsm-b2  
_paper: _paper:10.1007/s11669-024-01111-0:MgSm, paper:10.1016/j.jallcom.2007.05.035:MgSm, paper:10.1016/j.jallcom.2007.05.035:Mgm  
_tdb: _tdb:MgSm-08Jia.tdb:MGSM_B2, tdb:MgSm-24Jia.tdb:MGSM_B2  


### TDB models of MGSM_B2 (2): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): MGSM_B2, type code %, sha256 `95e32e81e730e1ee…`

~~~~text
70: PHASE MGSM_B2 % 2 1 1 !
71: CONST MGSM_B2 : MG : SM : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): MGSM_B2, type code %, sha256 `5a4755c28397807e…`

~~~~text
73: PHASE MGSM_B2 % 2 1 1 !
74: CONST MGSM_B2 : MG% SM : MG SM% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90169-0](https://doi.org/10.1016/0022-5088%2889%2990169-0) A. Saccone, S. Delfino, G. Borzone, R. Ferro, The samarium-magnesium system: A phase diagram, Journal of the Less Common Metals 154, 47-60 (1989).  
_cited as the source of values for this phase_

## RHOMB_C19 (Mg–Sm)

- Id: `phase:mg-sm:rhomb-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1192.36 K, x(Sm) 0.9504–1
- Literature: 2 values (2 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sm:rhomb-c19)

Names (6): _corpus: _corpus:phase:mg-sm:rhomb-c19  
_paper: _paper:10.1007/s11669-024-01111-0:α-Sm, paper:10.1016/j.jallcom.2007.05.035:Rhom(Sm)  
_tdb: _tdb:MgSm-08Jia.tdb:RHOMB_C19, tdb:MgSm-10Guo.tdb:RHOMB_C19, tdb:MgSm-24Jia.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (3): PHASE and CONSTITUENT statements as written

[MgSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-08Jia.tdb): RHOMB_C19, type code %, sha256 `95e32e81e730e1ee…`

~~~~text
45: PHASE RHOMB_C19 % 1 1 !
46: CONST RHOMB_C19 : MG SM : !
~~~~

[MgSm-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-10Guo.tdb): RHOMB_C19, type code %, sha256 `74f15429343690e9…`

~~~~text
50: PHASE RHOMB_C19 % 1 1 !
51: CONST RHOMB_C19 : MG SM : !
~~~~

[MgSm-24Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSm-24Jia.tdb): RHOMB_C19, type code %, sha256 `5a4755c28397807e…`

~~~~text
48: PHASE RHOMB_C19 % 1 1 !
49: CONST RHOMB_C19 : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01111-0](https://doi.org/10.1007/s11669-024-01111-0) Ruyi Jiang, Xiaofen Duan, Dashi Li, Cuiyun He, Re-investigation of the Phase Equilibria and Thermodynamic Assessment of the Mg-Sm Binary System, J. Phase Equilib. Diffus. 45, 520-536 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.12.006](https://doi.org/10.1016/j.calphad.2009.12.006) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Sm system, Calphad 34, 90-97 (2010).  
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
