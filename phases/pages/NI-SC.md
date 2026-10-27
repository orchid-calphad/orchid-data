# Ni–Sc phases

> Ni–Sc system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-SC.html · Markdown: https://data.orchid-project.org/phases/pages/NI-SC.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-SC) · [full JSON](https://data.orchid-project.org/phases/systems/NI-SC.json) · [Ni–Sc system page](https://data.orchid-project.org/systems/NI-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Sc system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ni-sc-bcc-a2); _phase:ni-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1160–2499.14 K, x(Sc) 0.93989–1 | 13 | 4 |
| [B2_BCC](#phase-ni-sc-bcc-b2); _phase:ni-sc:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2161.01 K, x(Sc) 0.49991–1 | 8 | 1 |
| [C15_LAVES](#phase-ni-sc-c15-laves); _phase:ni-sc:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1581.16 K, x(Sc) 0.27895–0.3499 | 31 | 3 |
| [FCC_A1](#phase-ni-sc-fcc-a1); _phase:ni-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1770.42 K, x(Sc) 0–0.00706 | 15 | 3 |
| [HCP_A3](#phase-ni-sc-hcp-a3); _phase:ni-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1882.97 K, x(Sc) 0.98992–1 | 22 | 3 |
| [LIQUID](#phase-ni-sc-liquid); _phase:ni-sc:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1112.71–2500 K, x(Sc) 0–1 | 110 | 3 |
| [NI5SC_D2D](#phase-ni-sc-ni5sc-d2d); _phase:ni-sc:ni5sc-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1455.72 K, x(Sc) 0.16667–0.16667 | 26 | 3 |
| [NI7SC2](#phase-ni-sc-ni7sc2); _phase:ni-sc:ni7sc2_ | Ce2Ni7 · hP36 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1564.33 K, x(Sc) 0.22222–0.22222 | 34 | 3 |
| [NISC_B2](#phase-ni-sc-nisc-b2); _phase:ni-sc:nisc-b2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1542.73 K, x(Sc) 0.53–0.53 | 20 | 2 |
| [NISC2](#phase-ni-sc-nisc2); _phase:ni-sc:nisc2_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1270 K, x(Sc) 0.72–0.72 | 27 | 3 |

## BCC_A2 (Ni–Sc)

- Id: `phase:ni-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1160–2499.14 K, x(Sc) 0.93989–1
- Literature: 13 values (13 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:bcc-a2)

Names (8): _corpus: _corpus:phase:ni-sc:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.07.003:BCC_A2, paper:10.1016/j.calphad.2014.11.005:Bcc_A2, paper:10.1016/j.tca.2014.04.006:(βSc)  
_tdb: _tdb:NiSc-13Kar.tdb:BCC_A2, tdb:NiSc-14Cao.tdb:A2_BCC, tdb:NiSc-14Cao.tdb:BCC_A2, tdb:NiSc-15Zhu.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): BCC_A2, type code %B, sha256 `49e8d54d4d81024b…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : NI SC% : VA : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): A2_BCC, type code %B, sha256 `ff80233bcc4a5f5d…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : NI SC : VA : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): BCC_A2, type code %B, sha256 `ff80233bcc4a5f5d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NI SC% : VA : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): BCC_A2, type code %B, sha256 `93e76d916a3807e7…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : NI SC% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## B2_BCC (Ni–Sc)

- Id: `phase:ni-sc:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: NiSc-14Cao.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in NiSc-14Cao.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2161.01 K, x(Sc) 0.49991–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:bcc-b2)

Names (4): _corpus: _corpus:phase:ni-sc:bcc-b2, corpus:phase:ni-sc:b2-bcc  
_paper: _paper:10.1016/j.tca.2014.04.006:ScNi  
_tdb: _tdb:NiSc-14Cao.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): B2_BCC, type code %BO, sha256 `ff80233bcc4a5f5d…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : NI SC : NI SC : VA :  !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## C15_LAVES (Ni–Sc)

- Id: `phase:ni-sc:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NiSc-13Kar.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSc-14Cao.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSc-15Zhu.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1581.16 K, x(Sc) 0.27895–0.3499
- Literature: 31 values (31 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:c15-laves)

Names (7): _corpus: _corpus:phase:ni-sc:c15-laves  
_paper: _paper:10.1016/j.calphad.2013.07.003:Ni2Sc, paper:10.1016/j.calphad.2014.11.005:(ScNi2), paper:10.1016/j.tca.2014.04.006:ScNi2  
_tdb: _tdb:NiSc-13Kar.tdb:C15_LAVES, tdb:NiSc-14Cao.tdb:C15_LAVES, tdb:NiSc-15Zhu.tdb:C15_LAVES  


### TDB models of C15_LAVES (3): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): C15_LAVES, type code %, sha256 `49e8d54d4d81024b…`

~~~~text
61: PHASE C15_LAVES % 2 2 1 !
62: CONST C15_LAVES : NI% SC : NI SC% : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): C15_LAVES, type code %, sha256 `ff80233bcc4a5f5d…`

~~~~text
65: PHASE C15_LAVES % 2 2 1 !
66: CONST C15_LAVES : NI% SC : NI SC% : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): C15_LAVES, type code %, sha256 `93e76d916a3807e7…`

~~~~text
59: PHASE C15_LAVES % 2 2 1 !
60: CONST C15_LAVES : NI% SC : NI SC% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## FCC_A1 (Ni–Sc)

- Id: `phase:ni-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1770.42 K, x(Sc) 0–0.00706
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:fcc-a1)

Names (7): _corpus: _corpus:phase:ni-sc:fcc-a1  
_paper: _paper:10.1016/j.calphad.2013.07.003:FCC_A1, paper:10.1016/j.calphad.2014.11.005:Fcc_A1, paper:10.1016/j.tca.2014.04.006:(Ni)  
_tdb: _tdb:NiSc-13Kar.tdb:FCC_A1, tdb:NiSc-14Cao.tdb:FCC_A1, tdb:NiSc-15Zhu.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): FCC_A1, type code %A, sha256 `49e8d54d4d81024b…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : NI% SC : VA : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): FCC_A1, type code %A, sha256 `ff80233bcc4a5f5d…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NI% SC : VA : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): FCC_A1, type code %A, sha256 `93e76d916a3807e7…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : NI% SC : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## HCP_A3 (Ni–Sc)

- Id: `phase:ni-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1882.97 K, x(Sc) 0.98992–1
- Literature: 22 values (22 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:hcp-a3)

Names (7): _corpus: _corpus:phase:ni-sc:hcp-a3  
_paper: _paper:10.1016/j.calphad.2013.07.003:HCP_A3, paper:10.1016/j.calphad.2014.11.005:Hcp_A3, paper:10.1016/j.tca.2014.04.006:(αSc)  
_tdb: _tdb:NiSc-13Kar.tdb:HCP_A3, tdb:NiSc-14Cao.tdb:HCP_A3, tdb:NiSc-15Zhu.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): HCP_A3, type code %A, sha256 `49e8d54d4d81024b…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : NI SC% : VA : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): HCP_A3, type code %A, sha256 `ff80233bcc4a5f5d…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : NI SC% : VA : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): HCP_A3, type code %A, sha256 `93e76d916a3807e7…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : NI SC% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## LIQUID (Ni–Sc)

- Id: `phase:ni-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1112.71–2500 K, x(Sc) 0–1
- Literature: 110 values (110 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:liquid)

Names (8): _corpus: _corpus:phase:ni-sc:liquid  
_paper: _paper:10.1016/j.calphad.2013.07.003:L, paper:10.1016/j.calphad.2014.11.005:Liq, paper:10.1016/j.tca.2014.04.006:Liquid, paper:10.1016/j.tca.2014.04.006:liquid  
_tdb: _tdb:NiSc-13Kar.tdb:LIQUID, tdb:NiSc-14Cao.tdb:LIQUID, tdb:NiSc-15Zhu.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): LIQUID, type code %, sha256 `49e8d54d4d81024b…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : NI SC : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): LIQUID, type code %, sha256 `ff80233bcc4a5f5d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : NI SC : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): LIQUID, type code %, sha256 `93e76d916a3807e7…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : NI NISC SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## NI5SC_D2D (Ni–Sc)

- Id: `phase:ni-sc:ni5sc-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 0.8333, Sc 0.1667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1455.72 K, x(Sc) 0.16667–0.16667
- Literature: 26 values (26 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:ni5sc-d2d)

Names (7): _corpus: _corpus:phase:ni-sc:ni5sc-d2d  
_paper: _paper:10.1016/j.calphad.2013.07.003:Ni5Sc, paper:10.1016/j.calphad.2014.11.005:ScNi5, paper:10.1016/j.tca.2014.04.006:ScNi5  
_tdb: _tdb:NiSc-13Kar.tdb:NI5SC_D2D, tdb:NiSc-14Cao.tdb:NI5SC_D2D, tdb:NiSc-15Zhu.tdb:NI5SC_D2D  


### TDB models of NI5SC_D2D (3): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): NI5SC_D2D, type code %, sha256 `49e8d54d4d81024b…`

~~~~text
51: PHASE NI5SC_D2D % 2 5 1 !
52: CONST NI5SC_D2D : NI : SC : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): NI5SC_D2D, type code %, sha256 `ff80233bcc4a5f5d…`

~~~~text
55: PHASE NI5SC_D2D % 2 5 1 !
56: CONST NI5SC_D2D : NI : SC : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): NI5SC_D2D, type code %, sha256 `93e76d916a3807e7…`

~~~~text
49: PHASE NI5SC_D2D % 2 5 1 !
50: CONST NI5SC_D2D : NI : SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## NI7SC2 (Ni–Sc)

- Id: `phase:ni-sc:ni7sc2`; status `assigned`
- Structure: Ce2Ni7 · hP36 · P6_3/mmc (194); type `st:ce2ni7-hp36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.7778, Sc 0.2222
- Stability: stable in 3 of 3 calculated diagram(s): 300–1564.33 K, x(Sc) 0.22222–0.22222
- Literature: 34 values (34 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:ni7sc2)

Names (7): _corpus: _corpus:phase:ni-sc:ni7sc2  
_paper: _paper:10.1016/j.calphad.2013.07.003:Ni7Sc2, paper:10.1016/j.calphad.2014.11.005:Sc2Ni7, paper:10.1016/j.tca.2014.04.006:Sc2Ni7  
_tdb: _tdb:NiSc-13Kar.tdb:NI7SC2, tdb:NiSc-14Cao.tdb:NI7SC2, tdb:NiSc-15Zhu.tdb:NI7SC2  


### TDB models of NI7SC2 (3): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): NI7SC2, type code %, sha256 `49e8d54d4d81024b…`

~~~~text
56: PHASE NI7SC2 % 2 7 2 !
57: CONST NI7SC2 : NI : SC : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): NI7SC2, type code %, sha256 `ff80233bcc4a5f5d…`

~~~~text
60: PHASE NI7SC2 % 2 7 2 !
61: CONST NI7SC2 : NI : SC : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): NI7SC2, type code %, sha256 `93e76d916a3807e7…`

~~~~text
54: PHASE NI7SC2 % 2 7 2 !
55: CONST NI7SC2 : NI : SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## NISC_B2 (Ni–Sc)

- Id: `phase:ni-sc:nisc-b2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_B2; stoichiometry_contradicts_B2:NiSc-13Kar.tdb; stoichiometry_contradicts_B2:NiSc-15Zhu.tdb
- Candidate (literature_printed): CsCl · cP2 — printed with a label mapped to this phase
- Candidate (name_token): CsCl · B2 · cP2 · Pm-3m (221) — Strukturbericht/word 'B2' in the TDB name
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for NISC_B2: NiSc
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — NiSc-13Kar.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — NiSc-15Zhu.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Stoichiometry: Ni 0.4700, Sc 0.5300
- Stability: stable in 2 of 2 calculated diagram(s): 300–1542.73 K, x(Sc) 0.53–0.53
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:nisc-b2)

Names (5): _corpus: _corpus:phase:ni-sc:nisc-b2  
_paper: _paper:10.1016/j.calphad.2013.07.003:NiSc, paper:10.1016/j.calphad.2014.11.005:ScNi  
_tdb: _tdb:NiSc-13Kar.tdb:NISC_B2, tdb:NiSc-15Zhu.tdb:NISC_B2  


### TDB models of NISC_B2 (2): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): NISC_B2, type code %, sha256 `49e8d54d4d81024b…`

~~~~text
66: PHASE NISC_B2 % 2 0.47 0.53 !
67: CONST NISC_B2 : NI : SC : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): NISC_B2, type code %, sha256 `93e76d916a3807e7…`

~~~~text
64: PHASE NISC_B2 % 2 0.47 0.53 !
65: CONST NISC_B2 : NI : SC : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
_cited as the source of values for this phase_

## NISC2 (Ni–Sc)

- Id: `phase:ni-sc:nisc2`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (literature_printed): NiTi2 · cF96 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): NiTi2 · cF96 · Fd-3m (227) — Hallstedt 2025 mmc2 row for NISC2: NiSc2
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiSc-13Kar.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiSc-14Cao.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiSc-15Zhu.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Stoichiometry: Ni 0.2800, Sc 0.7200
- Stability: stable in 3 of 3 calculated diagram(s): 300–1270 K, x(Sc) 0.72–0.72
- Literature: 27 values (27 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sc:nisc2)

Names (7): _corpus: _corpus:phase:ni-sc:nisc2  
_paper: _paper:10.1016/j.calphad.2013.07.003:NiSc2, paper:10.1016/j.calphad.2014.11.005:Sc2Ni, paper:10.1016/j.tca.2014.04.006:Sc2Ni  
_tdb: _tdb:NiSc-13Kar.tdb:NISC2, tdb:NiSc-14Cao.tdb:NISC2, tdb:NiSc-15Zhu.tdb:NISC2  


### TDB models of NISC2 (3): PHASE and CONSTITUENT statements as written

[NiSc-13Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-13Kar.tdb): NISC2, type code %, sha256 `49e8d54d4d81024b…`

~~~~text
71: PHASE NISC2 % 2 7 18 !
72: CONST NISC2 : NI : SC : !
~~~~

[NiSc-14Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-14Cao.tdb): NISC2, type code %, sha256 `ff80233bcc4a5f5d…`

~~~~text
70: PHASE NISC2 % 2 7 18 !
71: CONST NISC2 : NI : SC : !
~~~~

[NiSc-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSc-15Zhu.tdb): NISC2, type code %, sha256 `93e76d916a3807e7…`

~~~~text
69: PHASE NISC2 % 2 7 18 !
70: CONST NISC2 : NI : SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.07.003](https://doi.org/10.1016/j.calphad.2013.07.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, Thermodynamic description of the Ni–Sc system, Calphad 42, 59-65 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.11.005](https://doi.org/10.1016/j.calphad.2014.11.005) Daiman Zhu, Changrong Li, Cuiping Guo, Zhenmin Du, Junqin Li, Thermodynamic assessment of the Ni–Sc binary system, Calphad 48, 106-112 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.04.006](https://doi.org/10.1016/j.tca.2014.04.006) Zhaoping Cao, Shuhong Liu, Xu Fang, Kaiming Cheng, Qiannan Gao, Yong Du et al., Experimental investigation and thermodynamic analysis of the Sc–Ni system supplemented with first-principles calculations, Thermochimica Acta 586, 30-39 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(97)00467-2](https://doi.org/10.1016/s0925-8388%2897%2900467-2) E.L. Semenova, N.Yu. Rusetskaya, The ScNi system, Journal of Alloys and Compounds 262-263, 258-262 (1997).  
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
