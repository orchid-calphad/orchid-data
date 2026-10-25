# Re–Zr phases

> Re–Zr system: 8 phases (tier A 5, tier C 2, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RE-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/RE-ZR.md

8 phases (tier A 5, tier C 2, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RE-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/RE-ZR.json) · [Re–Zr system page](https://data.orchid-project.org/systems/RE-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/RE-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Re–Zr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-re-zr-bcc-a2); _phase:re-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1016.28–2282.85 K, x(Zr) 0.89715–1 | 17 | 2 |
| [C14_LAVES](#phase-re-zr-c14-laves); _phase:re-zr:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3263.91 K, x(Zr) 0.29852–0.36282 | 37 | 2 |
| [FCC_A1](#phase-re-zr-fcc-a1); _phase:re-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-re-zr-hcp-a3); _phase:re-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3542.25 K, x(Zr) 0–1 | 18 | 2 |
| [LIQUID](#phase-re-zr-liquid); _phase:re-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1821.17–4000 K, x(Zr) 0–1 | 47 | 2 |
| [RE24ZR5_A12](#phase-re-zr-re24zr5-a12); _phase:re-zr:re24zr5-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3122.98 K, x(Zr) 0.1699–0.1727 | 18 | 2 |
| [RE25ZR21](#phase-re-zr-re25zr21); _phase:re-zr:re25zr21_ | Re25Zr21 · hR92 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1933.91 K, x(Zr) 0.45652–0.45801 | 24 | 1 |
| [REZR2](#phase-re-zr-rezr2); _phase:re-zr:rezr2_ | Re25Zr21 · hR92 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1913 K, x(Zr) 0.66667–0.66667 | 11 | 1 |

## BCC_A2 (Re–Zr)

- Id: `phase:re-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1016.28–2282.85 K, x(Zr) 0.89715–1
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:bcc-a2)

Names (5): _corpus: _corpus:phase:re-zr:bcc-a2  
_paper: _paper:10.1007/s00706-013-1040-5:bcc, paper:10.1016/j.ijrmhm.2023.106259:bcc (Zr)  
_tdb: _tdb:ReZr-13Liu.tdb:BCC_A2, tdb:ReZr-23Che.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ReZr-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb): BCC_A2, type code %B, sha256 `1fcf6a3bca904b49…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : RE ZR% : VA : !
~~~~

[ReZr-23Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb): BCC_A2, type code %B, sha256 `644674a05faf287f…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : RE ZR% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf01479962](https://doi.org/10.1007/bf01479962) E. M. Savitskii, M. A. Tylkina, I. A. Tsyganova, Phase diagram of the zirconium-rhenium system, The Soviet Journal of Atomic Energy 7, 724-727 (1961).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(79)90119-4](https://doi.org/10.1016/0036-9748%2879%2990119-4) S.P. Garg, R.J. Ackermann, Zr-Re phase diagram between 1866 to 1913 K, Scripta Metallurgica 13, 611-613 (1979).  
_cited as the source of values for this phase_

## C14_LAVES (Re–Zr)

- Id: `phase:re-zr:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in ReZr-13Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in ReZr-23Che.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–3263.91 K, x(Zr) 0.29852–0.36282
- Literature: 37 values (37 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:c14-laves)

Names (5): _corpus: _corpus:phase:re-zr:c14-laves  
_paper: _paper:10.1007/s00706-013-1040-5:Re2Zr, paper:10.1016/j.ijrmhm.2023.106259:Re2Zr  
_tdb: _tdb:ReZr-13Liu.tdb:C14_LAVES, tdb:ReZr-23Che.tdb:C14_LAVES  


### TDB models of C14_LAVES (2): PHASE and CONSTITUENT statements as written

[ReZr-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb): C14_LAVES, type code %, sha256 `1fcf6a3bca904b49…`

~~~~text
55: PHASE C14_LAVES % 2 2 1 !
56: CONST C14_LAVES : RE% ZR : RE ZR% : !
~~~~

[ReZr-23Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb): C14_LAVES, type code %, sha256 `644674a05faf287f…`

~~~~text
56: PHASE C14_LAVES % 2 2 1 !
57: CONST C14_LAVES : RE% ZR : RE ZR% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf01479962](https://doi.org/10.1007/bf01479962) E. M. Savitskii, M. A. Tylkina, I. A. Tsyganova, Phase diagram of the zirconium-rhenium system, The Soviet Journal of Atomic Energy 7, 724-727 (1961).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(79)90119-4](https://doi.org/10.1016/0036-9748%2879%2990119-4) S.P. Garg, R.J. Ackermann, Zr-Re phase diagram between 1866 to 1913 K, Scripta Metallurgica 13, 611-613 (1979).  
_cited as the source of values for this phase_

## FCC_A1 (Re–Zr)

- Id: `phase:re-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:re-zr:fcc-a1  
_tdb: _tdb:ReZr-13Liu.tdb:FCC_A1, tdb:ReZr-23Che.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ReZr-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb): FCC_A1, type code %A, sha256 `1fcf6a3bca904b49…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : RE ZR : VA : !
~~~~

[ReZr-23Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb): FCC_A1, type code %A, sha256 `644674a05faf287f…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : RE ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_assessment that models this phase_

## HCP_A3 (Re–Zr)

- Id: `phase:re-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3542.25 K, x(Zr) 0–1
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:hcp-a3)

Names (7): _corpus: _corpus:phase:re-zr:hcp-a3  
_paper: _paper:10.1007/s00706-013-1040-5:hcp(Re), paper:10.1007/s00706-013-1040-5:hcp(Zr), paper:10.1016/j.ijrmhm.2023.106259:hcp (Re), paper:10.1016/j.ijrmhm.2023.106259:hcp (Zr)  
_tdb: _tdb:ReZr-13Liu.tdb:HCP_A3, tdb:ReZr-23Che.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ReZr-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb): HCP_A3, type code %A, sha256 `1fcf6a3bca904b49…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : RE% ZR% : VA : !
~~~~

[ReZr-23Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb): HCP_A3, type code %A, sha256 `644674a05faf287f…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : RE% ZR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## LIQUID (Re–Zr)

- Id: `phase:re-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1821.17–4000 K, x(Zr) 0–1
- Literature: 47 values (43 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:liquid)

Names (7): _corpus: _corpus:phase:re-zr:liquid  
_paper: _paper:10.1007/s00706-013-1040-5:liq., paper:10.1007/s00706-013-1040-5:liquid, paper:10.1016/j.ijrmhm.2023.106259:Liquid, paper:10.1016/j.ijrmhm.2023.106259:liquid  
_tdb: _tdb:ReZr-13Liu.tdb:LIQUID, tdb:ReZr-23Che.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ReZr-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb): LIQUID, type code %, sha256 `1fcf6a3bca904b49…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : RE ZR : !
~~~~

[ReZr-23Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb): LIQUID, type code %, sha256 `644674a05faf287f…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : RE ZR : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.matchar.2020.110285](https://doi.org/10.1016/j.matchar.2020.110285) Hui-zhong Li, Lei Yang, Yan Wang, Gang Tan, Shi-chang Qiao, Zheng-qin Huang et al., Thermal deformation and dynamic recrystallization of a novel HEXed P/M nickel-based superalloy, Materials Characterization 163, 110285 (2020).  
_cited as the source of values for this phase_
- [doi:10.1007/bf01479962](https://doi.org/10.1007/bf01479962) E. M. Savitskii, M. A. Tylkina, I. A. Tsyganova, Phase diagram of the zirconium-rhenium system, The Soviet Journal of Atomic Energy 7, 724-727 (1961).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102438](https://doi.org/10.1016/j.calphad.2022.102438) C. Zhang, Y. Wan, X. Liang, M. Rong, G. Ma, L. Li, C. Hu, C. Tang, Melting and phase diagram of Au–Co alloy at nanoscale by thermodynamic modeling and key experiments, Calphad 78 (2022), 102438.  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(79)90119-4](https://doi.org/10.1016/0036-9748%2879%2990119-4) S.P. Garg, R.J. Ackermann, Zr-Re phase diagram between 1866 to 1913 K, Scripta Metallurgica 13, 611-613 (1979).  
_cited as the source of values for this phase_
- [doi:10.1080/09506608.2018.1516713](https://doi.org/10.1080/09506608.2018.1516713) R. Darolia, Development of strong, oxidation and corrosion resistant nickel-based superalloys: critical review of challenges, progress and prospects, Int. Mater. Rev. 64 (6) (2019) 355–380.  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2014.02.010](https://doi.org/10.1016/j.actamat.2014.02.010) Jean-Marc Joubert, Jean-Claude Crivello, Mohamed Andasmas, Pierre Joubert, Phase stability in the ternary Re–W–Zr system, Acta Materialia 70, 56-65 (2014).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2015.04.009](https://doi.org/10.1016/j.calphad.2015.04.009) O. Senkov, J. Miller, D. Miracle, C. Woodward, Accelerated exploration of multiprincipal element alloys for structural applications, Calphad 50 (2015) 32–48. Fig. 9. Calculate the mixing enthalpies of bcc at 298 K and compared with the literature \[21\].  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2020.155195](https://doi.org/10.1016/j.jallcom.2020.155195) Jianbo Zhang, Chongji Wu, Yuanyi Peng, Xingchuan Xia, Jingan Li, Jian Ding et al., Hot compression deformation behavior and processing maps of ATI 718Plus superalloy, Journal of Alloys and Compounds 835, 155195 (2020).  
_cited as the source of values for this phase_

## RE24ZR5_A12 (Re–Zr)

- Id: `phase:re-zr:re24zr5-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3122.98 K, x(Zr) 0.1699–0.1727
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:re24zr5-a12)

Names (6): _corpus: _corpus:phase:re-zr:re24zr5-a12  
_paper: _paper:10.1007/s00706-013-1040-5:Re24Zr5, paper:10.1016/j.ijrmhm.2023.106259:Re24Zr5, paper:10.1016/j.ijrmhm.2023.106259:Re24Zr5 + (Re)  
_tdb: _tdb:ReZr-13Liu.tdb:RE24ZR5_A12, tdb:ReZr-23Che.tdb:RE24ZR5_A12  


### TDB models of RE24ZR5_A12 (2): PHASE and CONSTITUENT statements as written

[ReZr-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb): RE24ZR5_A12, type code %, sha256 `1fcf6a3bca904b49…`

~~~~text
50: PHASE RE24ZR5_A12 % 2 24 5 !
51: CONST RE24ZR5_A12 : RE% ZR : RE ZR% : !
~~~~

[ReZr-23Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb): RE24ZR5_A12, type code %, sha256 `644674a05faf287f…`

~~~~text
51: PHASE RE24ZR5_A12 % 2 24 5 !
52: CONST RE24ZR5_A12 : RE% ZR : RE ZR% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## RE25ZR21 (Re–Zr)

- Id: `phase:re-zr:re25zr21`; status `assigned`
- Structure: Re25Zr21 · hR92 · R-3c (167); type `st:re25zr21-hr92`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1933.91 K, x(Zr) 0.45652–0.45801
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:re25zr21)

Names (4): _corpus: _corpus:phase:re-zr:re25zr21  
_paper: _paper:10.1016/j.ijrmhm.2023.106259:Re25Zr21, paper:10.1016/j.ijrmhm.2023.106259:Re25Zr21 + bcc (Zr)  
_tdb: _tdb:ReZr-23Che.tdb:RE25ZR21  


### TDB models of RE25ZR21 (1): PHASE and CONSTITUENT statements as written

[ReZr-23Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb): RE25ZR21, type code %, sha256 `644674a05faf287f…`

~~~~text
61: PHASE RE25ZR21 % 2 25 21 !
62: CONST RE25ZR21 : RE% ZR : RE ZR% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf01479962](https://doi.org/10.1007/bf01479962) E. M. Savitskii, M. A. Tylkina, I. A. Tsyganova, Phase diagram of the zirconium-rhenium system, The Soviet Journal of Atomic Energy 7, 724-727 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_cited as the source of values for this phase_

## REZR2 (Re–Zr)

- Id: `phase:re-zr:rezr2`; status `assigned`
- Structure: Re25Zr21 · hR92 · R-3c (167); type `st:re25zr21-hr92`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Re 0.3333, Zr 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1913 K, x(Zr) 0.66667–0.66667
- Literature: 11 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-zr:rezr2)

Names (4): _corpus: _corpus:phase:re-zr:rezr2  
_paper: _paper:10.1007/s00706-013-1040-5:ReZr2, paper:10.1016/j.ijrmhm.2023.106259:ReZr2  
_tdb: _tdb:ReZr-13Liu.tdb:REZR2  


### TDB models of REZR2 (1): PHASE and CONSTITUENT statements as written

[ReZr-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb): REZR2, type code %, sha256 `1fcf6a3bca904b49…`

~~~~text
60: PHASE REZR2 % 2 1 2 !
61: CONST REZR2 : RE : ZR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf01479962](https://doi.org/10.1007/bf01479962) E. M. Savitskii, M. A. Tylkina, I. A. Tsyganova, Phase diagram of the zirconium-rhenium system, The Soviet Journal of Atomic Energy 7, 724-727 (1961).  
_cited as the source of values for this phase_
- [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023).  
_reports values for this phase_
- [doi:10.1016/0036-9748(79)90119-4](https://doi.org/10.1016/0036-9748%2879%2990119-4) S.P. Garg, R.J. Ackermann, Zr-Re phase diagram between 1866 to 1913 K, Scripta Metallurgica 13, 611-613 (1979).  
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
