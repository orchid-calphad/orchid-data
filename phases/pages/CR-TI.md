# Cr–Ti phases

> Cr–Ti system: 10 phases (tier A 9, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-TI.html · Markdown: https://data.orchid-project.org/phases/pages/CR-TI.md

10 phases (tier A 9, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-TI) · [full JSON](https://data.orchid-project.org/phases/systems/CR-TI.json) · [Cr–Ti system page](https://data.orchid-project.org/systems/CR-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Ti system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-ti-bcc-a2); _phase:cr-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 300–3999.73 K, x(Ti) 0–1 | 106 | 8 |
| [C14_LAVES](#phase-cr-ti-c14-laves); _phase:cr-ti:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 760–1648.88 K, x(Ti) 0.08–0.36776 | 44 | 8 |
| [C15_LAVES](#phase-cr-ti-c15-laves); _phase:cr-ti:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 300–1500 K, x(Ti) 0.03–0.3941 | 42 | 8 |
| [C36_LAVES](#phase-cr-ti-c36-laves); _phase:cr-ti:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 930–1560 K, x(Ti) 0.05–0.36967 | 35 | 7 |
| [CR2TI_C14](#phase-cr-ti-cr2ti-c14); _phase:cr-ti:cr2ti-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CR2TI_C15](#phase-cr-ti-cr2ti-c15); _phase:cr-ti:cr2ti-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1206.37 K, x(Ti) 0.33333–0.35227 | 0 | 1 |
| [CR2TI_C36](#phase-cr-ti-cr2ti-c36); _phase:cr-ti:cr2ti-c36_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1300–1530 K | 0 | 1 |
| [FCC_A1](#phase-cr-ti-fcc-a1); _phase:cr-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 8 calculated diagram(s) | 0 | 8 |
| [HCP_A3](#phase-cr-ti-hcp-a3); _phase:cr-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 300–2169.99 K, x(Ti) 0.11–1 | 17 | 8 |
| [LIQUID](#phase-cr-ti-liquid); _phase:cr-ti:liquid_ | liquid | liquid | stable in 8 of 8 calculated diagram(s): 1676.96–4000 K, x(Ti) 0–1 | 16 | 8 |

## BCC_A2 (Cr–Ti)

- Id: `phase:cr-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 8 of 8 calculated diagram(s): 300–3999.73 K, x(Ti) 0–1
- Literature: 106 values (106 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:bcc-a2)

Names (15): _corpus: _corpus:phase:cr-ti:bcc-a2  
_paper: _paper:10.1007/s11669-024-01090-2:bcc, paper:10.1007/s11669-024-01090-2:bcc (Cr-rich), paper:10.1007/s11669-024-01090-2:bcc (Ti-rich), paper:10.1361/105497102770331569:(Cr), paper:10.1361/105497102770331569:(βTi), paper:10.1361/105497102770331569:β(Cr,Ti)  
_tdb: _tdb:CrTi-00Zhu.tdb:BCC_A2, tdb:CrTi-02Gho.tdb:BCC_A2, tdb:CrTi-10Pav-3SL.tdb:BCC_A2, tdb:CrTi-10Pav.tdb:BCC_A2, tdb:CrTi-22Sun.tdb:BCC_A2, tdb:CrTi-24Flo.tdb:BCC_A2, tdb:CrTi-98Sau-LB.tdb:BCC_A2, tdb:CrTi-99Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (8): PHASE and CONSTITUENT statements as written

[CrTi-00Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-00Zhu.tdb): BCC_A2, type code %B, sha256 `8e0045194fc6bbe4…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CR% TI% : VA : !
~~~~

[CrTi-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-02Gho.tdb): BCC_A2, type code %B, sha256 `cfa98d3054ed1a83…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% TI% : VA : !
~~~~

[CrTi-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav-3SL.tdb): BCC_A2, type code %B, sha256 `7566666f3d21bb88…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CR% TI% : VA : !
~~~~

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): BCC_A2, type code %B, sha256 `72d079567c30caf6…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : CR% TI% : VA : !
~~~~

[CrTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-22Sun.tdb): BCC_A2, type code %B, sha256 `636c20714b97be05…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CR% TI% : VA : !
~~~~

[CrTi-24Flo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-24Flo.tdb): BCC_A2, type code %B, sha256 `aade304e745bf1bd…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR% TI% : VA : !
~~~~

[CrTi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-98Sau-LB.tdb): BCC_A2, type code %B, sha256 `ba7af58faf26ef72…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% TI% : VA : !
~~~~

[CrTi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-99Lee.tdb): BCC_A2, type code %B, sha256 `6210a5bfed1fb282…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR% TI% : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s11669-024-01090-2](https://doi.org/10.1007/s11669-024-01090-2) Agustin Flores, Sylvie Chatain, Paul Fossati, Frank Stein, Jean-Marc Joubert, Experimental Investigation and Thermodynamic Assessment of the Cr–Ti System, J. Phase Equilib. Diffus. 45, 417-432 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910203](https://doi.org/10.1515/ijmr-2000-910203) W. Zhuang, J. Shen, Y. Liu, L. Ling, S. Shang, Y. Du, J.C. Schuster, Z. Metallkd., 91, 121-27(2000).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2011.03.031](https://doi.org/10.1016/j.intermet.2011.03.031) D.M. Cupid, M.J. Kriegel, O. Fabrichnaya, F. Ebrahimi, and H.J. Seifert, Thermodynamic Assessment of the Cr–Ti and first Assessment of the Al–Cr–Ti Systems, Intermetallics, 2011, 19(8), p 1222-1235. https://doi.org/10.1016/j.intermet.2011.03.031  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2010.06.117](https://doi.org/10.1016/j.jallcom.2010.06.117) Wolfgang Baumann, Andreas Leineweber, Solid solubility by anti-site atoms in the C36-TiCr2 Laves phase revealed by single-crystal X-ray diffractometry, Journal of Alloys and Compounds 505, 492-496 (2010).  
_cited as the source of values for this phase_
- [doi:10.1063/1.106450](https://doi.org/10.1063/1.106450) K. Ohsaka, E. H. Trinh, J. C. Holzer, W. L. Johnson, Gibbs free energy difference between the undercooled liquid and the β phase of a Ti-Cr alloy, Applied Physics Letters 60, 1079-1081 (1992).  
_cited as the source of values for this phase_

## C14_LAVES (Cr–Ti)

- Id: `phase:cr-ti:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTi-00Zhu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-02Gho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-10Pav-3SL.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-10Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-22Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-24Flo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-98Sau-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-99Lee.tdb also describes the disordered state
- Stability: stable in 8 of 8 calculated diagram(s): 760–1648.88 K, x(Ti) 0.08–0.36776
- Literature: 44 values (44 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:c14-laves)

Names (12): _corpus: _corpus:phase:cr-ti:c14-laves  
_paper: _paper:10.1007/s11669-024-01090-2:C14, paper:10.1361/105497102770331569:β-Cr2Ti, paper:10.1361/105497102770331569:γ-Cr2Ti  
_tdb: _tdb:CrTi-00Zhu.tdb:C14_LAVES, tdb:CrTi-02Gho.tdb:C14_LAVES, tdb:CrTi-10Pav-3SL.tdb:C14_LAVES, tdb:CrTi-10Pav.tdb:C14_LAVES, tdb:CrTi-22Sun.tdb:C14_LAVES, tdb:CrTi-24Flo.tdb:C14_LAVES, tdb:CrTi-98Sau-LB.tdb:C14_LAVES, tdb:CrTi-99Lee.tdb:C14_LAVES  


### TDB models of C14_LAVES (8): PHASE and CONSTITUENT statements as written

[CrTi-00Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-00Zhu.tdb): C14_LAVES, type code %, sha256 `8e0045194fc6bbe4…`

~~~~text
51: PHASE C14_LAVES % 3 2 4 6 !
52: CONST C14_LAVES : CR : CR TI : CR TI : !
~~~~

[CrTi-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-02Gho.tdb): C14_LAVES, type code %, sha256 `cfa98d3054ed1a83…`

~~~~text
40: PHASE C14_LAVES % 2 2 1 !
41: CONST C14_LAVES : CR TI : CR TI : !
~~~~

[CrTi-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav-3SL.tdb): C14_LAVES, type code %, sha256 `7566666f3d21bb88…`

~~~~text
43: PHASE C14_LAVES % 3 2 4 6 !
44: CONST C14_LAVES : CR : CR TI : CR TI : !
~~~~

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): C14_LAVES, type code %, sha256 `72d079567c30caf6…`

~~~~text
71: PHASE C14_LAVES % 2 2 1 !
72: CONST C14_LAVES : CR TI : CR TI : !
~~~~

[CrTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-22Sun.tdb): C14_LAVES, type code %, sha256 `636c20714b97be05…`

~~~~text
47: PHASE C14_LAVES % 2 2 1 !
48: CONST C14_LAVES : CR TI : CR TI : !
~~~~

[CrTi-24Flo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-24Flo.tdb): C14_LAVES, type code %, sha256 `aade304e745bf1bd…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : CR TI : CR TI : !
~~~~

[CrTi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-98Sau-LB.tdb): C14_LAVES, type code %, sha256 `ba7af58faf26ef72…`

~~~~text
44: PHASE C14_LAVES % 2 2 1 !
45: CONST C14_LAVES : CR TI : CR TI : !
~~~~

[CrTi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-99Lee.tdb): C14_LAVES, type code %, sha256 `6210a5bfed1fb282…`

~~~~text
41: PHASE C14_LAVES % 2 2 1 !
42: CONST C14_LAVES : CR TI : CR TI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01090-2](https://doi.org/10.1007/s11669-024-01090-2) Agustin Flores, Sylvie Chatain, Paul Fossati, Frank Stein, Jean-Marc Joubert, Experimental Investigation and Thermodynamic Assessment of the Cr–Ti System, J. Phase Equilib. Diffus. 45, 417-432 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910203](https://doi.org/10.1515/ijmr-2000-910203) W. Zhuang, J. Shen, Y. Liu, L. Ling, S. Shang, Y. Du, J.C. Schuster, Z. Metallkd., 91, 121-27(2000).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2011.03.031](https://doi.org/10.1016/j.intermet.2011.03.031) D.M. Cupid, M.J. Kriegel, O. Fabrichnaya, F. Ebrahimi, and H.J. Seifert, Thermodynamic Assessment of the Cr–Ti and first Assessment of the Al–Cr–Ti Systems, Intermetallics, 2011, 19(8), p 1222-1235. https://doi.org/10.1016/j.intermet.2011.03.031  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2010.06.117](https://doi.org/10.1016/j.jallcom.2010.06.117) Wolfgang Baumann, Andreas Leineweber, Solid solubility by anti-site atoms in the C36-TiCr2 Laves phase revealed by single-crystal X-ray diffractometry, Journal of Alloys and Compounds 505, 492-496 (2010).  
_cited as the source of values for this phase_

## C15_LAVES (Cr–Ti)

- Id: `phase:cr-ti:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTi-00Zhu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-02Gho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-10Pav-3SL.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-10Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-22Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-24Flo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-98Sau-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-99Lee.tdb also describes the disordered state
- Stability: stable in 8 of 8 calculated diagram(s): 300–1500 K, x(Ti) 0.03–0.3941
- Literature: 42 values (42 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:c15-laves)

Names (11): _corpus: _corpus:phase:cr-ti:c15-laves  
_paper: _paper:10.1007/s11669-024-01090-2:C15, paper:10.1361/105497102770331569:α-Cr2Ti  
_tdb: _tdb:CrTi-00Zhu.tdb:C15_LAVES, tdb:CrTi-02Gho.tdb:C15_LAVES, tdb:CrTi-10Pav-3SL.tdb:C15_LAVES, tdb:CrTi-10Pav.tdb:C15_LAVES, tdb:CrTi-22Sun.tdb:C15_LAVES, tdb:CrTi-24Flo.tdb:C15_LAVES, tdb:CrTi-98Sau-LB.tdb:C15_LAVES, tdb:CrTi-99Lee.tdb:C15_LAVES  


### TDB models of C15_LAVES (8): PHASE and CONSTITUENT statements as written

[CrTi-00Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-00Zhu.tdb): C15_LAVES, type code %, sha256 `8e0045194fc6bbe4…`

~~~~text
56: PHASE C15_LAVES % 2 2 1 !
57: CONST C15_LAVES : CR TI : CR TI : !
~~~~

[CrTi-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-02Gho.tdb): C15_LAVES, type code %, sha256 `cfa98d3054ed1a83…`

~~~~text
45: PHASE C15_LAVES % 2 2 1 !
46: CONST C15_LAVES : CR TI : CR TI : !
~~~~

[CrTi-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav-3SL.tdb): C15_LAVES, type code %, sha256 `7566666f3d21bb88…`

~~~~text
48: PHASE C15_LAVES % 2 2 1 !
49: CONST C15_LAVES : CR TI : CR TI : !
~~~~

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): C15_LAVES, type code %, sha256 `72d079567c30caf6…`

~~~~text
76: PHASE C15_LAVES % 2 2 1 !
77: CONST C15_LAVES : CR TI : CR TI : !
~~~~

[CrTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-22Sun.tdb): C15_LAVES, type code %, sha256 `636c20714b97be05…`

~~~~text
52: PHASE C15_LAVES % 2 2 1 !
53: CONST C15_LAVES : CR TI : CR TI : !
~~~~

[CrTi-24Flo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-24Flo.tdb): C15_LAVES, type code %, sha256 `aade304e745bf1bd…`

~~~~text
47: PHASE C15_LAVES % 2 2 1 !
48: CONST C15_LAVES : CR TI : CR TI : !
~~~~

[CrTi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-98Sau-LB.tdb): C15_LAVES, type code %, sha256 `ba7af58faf26ef72…`

~~~~text
49: PHASE C15_LAVES % 2 2 1 !
50: CONST C15_LAVES : CR TI : CR TI : !
~~~~

[CrTi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-99Lee.tdb): C15_LAVES, type code %, sha256 `6210a5bfed1fb282…`

~~~~text
46: PHASE C15_LAVES % 2 2 1 !
47: CONST C15_LAVES : CR TI : CR TI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01090-2](https://doi.org/10.1007/s11669-024-01090-2) Agustin Flores, Sylvie Chatain, Paul Fossati, Frank Stein, Jean-Marc Joubert, Experimental Investigation and Thermodynamic Assessment of the Cr–Ti System, J. Phase Equilib. Diffus. 45, 417-432 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910203](https://doi.org/10.1515/ijmr-2000-910203) W. Zhuang, J. Shen, Y. Liu, L. Ling, S. Shang, Y. Du, J.C. Schuster, Z. Metallkd., 91, 121-27(2000).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2011.03.031](https://doi.org/10.1016/j.intermet.2011.03.031) D.M. Cupid, M.J. Kriegel, O. Fabrichnaya, F. Ebrahimi, and H.J. Seifert, Thermodynamic Assessment of the Cr–Ti and first Assessment of the Al–Cr–Ti Systems, Intermetallics, 2011, 19(8), p 1222-1235. https://doi.org/10.1016/j.intermet.2011.03.031  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2010.06.117](https://doi.org/10.1016/j.jallcom.2010.06.117) Wolfgang Baumann, Andreas Leineweber, Solid solubility by anti-site atoms in the C36-TiCr2 Laves phase revealed by single-crystal X-ray diffractometry, Journal of Alloys and Compounds 505, 492-496 (2010).  
_cited as the source of values for this phase_

## C36_LAVES (Cr–Ti)

- Id: `phase:cr-ti:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTi-00Zhu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-02Gho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-10Pav-3SL.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-10Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-22Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-24Flo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTi-99Lee.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 930–1560 K, x(Ti) 0.05–0.36967
- Literature: 35 values (35 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:c36-laves)

Names (9): _corpus: _corpus:phase:cr-ti:c36-laves  
_paper: _paper:10.1007/s11669-024-01090-2:C36  
_tdb: _tdb:CrTi-00Zhu.tdb:C36_LAVES, tdb:CrTi-02Gho.tdb:C36_LAVES, tdb:CrTi-10Pav-3SL.tdb:C36_LAVES, tdb:CrTi-10Pav.tdb:C36_LAVES, tdb:CrTi-22Sun.tdb:C36_LAVES, tdb:CrTi-24Flo.tdb:C36_LAVES, tdb:CrTi-99Lee.tdb:C36_LAVES  


### TDB models of C36_LAVES (7): PHASE and CONSTITUENT statements as written

[CrTi-00Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-00Zhu.tdb): C36_LAVES, type code %, sha256 `8e0045194fc6bbe4…`

~~~~text
61: PHASE C36_LAVES % 3 2 4 6 !
62: CONST C36_LAVES : CR : CR TI : CR TI : !
~~~~

[CrTi-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-02Gho.tdb): C36_LAVES, type code %, sha256 `cfa98d3054ed1a83…`

~~~~text
50: PHASE C36_LAVES % 2 2 1 !
51: CONST C36_LAVES : CR TI : CR TI : !
~~~~

[CrTi-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav-3SL.tdb): C36_LAVES, type code %, sha256 `7566666f3d21bb88…`

~~~~text
53: PHASE C36_LAVES % 3 2 4 6 !
54: CONST C36_LAVES : CR : CR TI : CR TI : !
~~~~

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): C36_LAVES, type code %, sha256 `72d079567c30caf6…`

~~~~text
81: PHASE C36_LAVES % 2 2 1 !
82: CONST C36_LAVES : CR TI : CR TI : !
~~~~

[CrTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-22Sun.tdb): C36_LAVES, type code %, sha256 `636c20714b97be05…`

~~~~text
57: PHASE C36_LAVES % 2 2 1 !
58: CONST C36_LAVES : CR TI : CR TI : !
~~~~

[CrTi-24Flo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-24Flo.tdb): C36_LAVES, type code %, sha256 `aade304e745bf1bd…`

~~~~text
52: PHASE C36_LAVES % 2 2 1 !
53: CONST C36_LAVES : CR TI : CR TI : !
~~~~

[CrTi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-99Lee.tdb): C36_LAVES, type code %, sha256 `6210a5bfed1fb282…`

~~~~text
51: PHASE C36_LAVES % 2 2 1 !
52: CONST C36_LAVES : CR TI : CR TI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01090-2](https://doi.org/10.1007/s11669-024-01090-2) Agustin Flores, Sylvie Chatain, Paul Fossati, Frank Stein, Jean-Marc Joubert, Experimental Investigation and Thermodynamic Assessment of the Cr–Ti System, J. Phase Equilib. Diffus. 45, 417-432 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910203](https://doi.org/10.1515/ijmr-2000-910203) W. Zhuang, J. Shen, Y. Liu, L. Ling, S. Shang, Y. Du, J.C. Schuster, Z. Metallkd., 91, 121-27(2000).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2011.03.031](https://doi.org/10.1016/j.intermet.2011.03.031) D.M. Cupid, M.J. Kriegel, O. Fabrichnaya, F. Ebrahimi, and H.J. Seifert, Thermodynamic Assessment of the Cr–Ti and first Assessment of the Al–Cr–Ti Systems, Intermetallics, 2011, 19(8), p 1222-1235. https://doi.org/10.1016/j.intermet.2011.03.031  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2010.06.117](https://doi.org/10.1016/j.jallcom.2010.06.117) Wolfgang Baumann, Andreas Leineweber, Solid solubility by anti-site atoms in the C36-TiCr2 Laves phase revealed by single-crystal X-ray diffractometry, Journal of Alloys and Compounds 505, 492-496 (2010).  
_cited as the source of values for this phase_

## CR2TI_C14 (Cr–Ti)

- Id: `phase:cr-ti:cr2ti-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTi-10Pav.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:cr2ti-c14)

Names (2): _corpus: _corpus:phase:cr-ti:cr2ti-c14  
_tdb: _tdb:CrTi-10Pav.tdb:CR2TI_C14  


### TDB models of CR2TI_C14 (1): PHASE and CONSTITUENT statements as written

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): CR2TI_C14, type code %, sha256 `72d079567c30caf6…`

~~~~text
56: PHASE CR2TI_C14 % 2 2 1 !
57: CONST CR2TI_C14 : CR TI : CR TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## CR2TI_C15 (Cr–Ti)

- Id: `phase:cr-ti:cr2ti-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTi-10Pav.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1206.37 K, x(Ti) 0.33333–0.35227
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:cr2ti-c15)

Names (2): _corpus: _corpus:phase:cr-ti:cr2ti-c15  
_tdb: _tdb:CrTi-10Pav.tdb:CR2TI_C15  


### TDB models of CR2TI_C15 (1): PHASE and CONSTITUENT statements as written

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): CR2TI_C15, type code %, sha256 `72d079567c30caf6…`

~~~~text
61: PHASE CR2TI_C15 % 2 2 1 !
62: CONST CR2TI_C15 : CR TI : CR TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## CR2TI_C36 (Cr–Ti)

- Id: `phase:cr-ti:cr2ti-c36`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTi-10Pav.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1300–1530 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:cr2ti-c36)

Names (2): _corpus: _corpus:phase:cr-ti:cr2ti-c36  
_tdb: _tdb:CrTi-10Pav.tdb:CR2TI_C36  


### TDB models of CR2TI_C36 (1): PHASE and CONSTITUENT statements as written

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): CR2TI_C36, type code %, sha256 `72d079567c30caf6…`

~~~~text
66: PHASE CR2TI_C36 % 2 2 1 !
67: CONST CR2TI_C36 : CR TI : CR TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## FCC_A1 (Cr–Ti)

- Id: `phase:cr-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 8 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:fcc-a1)

Names (9): _corpus: _corpus:phase:cr-ti:fcc-a1  
_tdb: _tdb:CrTi-00Zhu.tdb:FCC_A1, tdb:CrTi-02Gho.tdb:FCC_A1, tdb:CrTi-10Pav-3SL.tdb:FCC_A1, tdb:CrTi-10Pav.tdb:FCC_A1, tdb:CrTi-22Sun.tdb:FCC_A1, tdb:CrTi-24Flo.tdb:FCC_A1, tdb:CrTi-98Sau-LB.tdb:FCC_A1, tdb:CrTi-99Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (8): PHASE and CONSTITUENT statements as written

[CrTi-00Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-00Zhu.tdb): FCC_A1, type code %A, sha256 `8e0045194fc6bbe4…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : CR TI : VA : !
~~~~

[CrTi-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-02Gho.tdb): FCC_A1, type code %A, sha256 `cfa98d3054ed1a83…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR TI : VA : !
~~~~

[CrTi-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav-3SL.tdb): FCC_A1, type code %A, sha256 `7566666f3d21bb88…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CR TI : VA : !
~~~~

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): FCC_A1, type code %A, sha256 `72d079567c30caf6…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : CR TI : VA : !
~~~~

[CrTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-22Sun.tdb): FCC_A1, type code %A, sha256 `636c20714b97be05…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CR TI : VA : !
~~~~

[CrTi-24Flo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-24Flo.tdb): FCC_A1, type code %A, sha256 `aade304e745bf1bd…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR TI : VA : !
~~~~

[CrTi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-98Sau-LB.tdb): FCC_A1, type code %A, sha256 `ba7af58faf26ef72…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR TI : VA : !
~~~~

[CrTi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-99Lee.tdb): FCC_A1, type code %A, sha256 `6210a5bfed1fb282…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR TI : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-024-01090-2](https://doi.org/10.1007/s11669-024-01090-2) Agustin Flores, Sylvie Chatain, Paul Fossati, Frank Stein, Jean-Marc Joubert, Experimental Investigation and Thermodynamic Assessment of the Cr–Ti System, J. Phase Equilib. Diffus. 45, 417-432 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910203](https://doi.org/10.1515/ijmr-2000-910203) W. Zhuang, J. Shen, Y. Liu, L. Ling, S. Shang, Y. Du, J.C. Schuster, Z. Metallkd., 91, 121-27(2000).  
_assessment that models this phase_

## HCP_A3 (Cr–Ti)

- Id: `phase:cr-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 8 of 8 calculated diagram(s): 300–2169.99 K, x(Ti) 0.11–1
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:hcp-a3)

Names (11): _corpus: _corpus:phase:cr-ti:hcp-a3  
_paper: _paper:10.1007/s11669-024-01090-2:hcp, paper:10.1361/105497102770331569:(αTi)  
_tdb: _tdb:CrTi-00Zhu.tdb:HCP_A3, tdb:CrTi-02Gho.tdb:HCP_A3, tdb:CrTi-10Pav-3SL.tdb:HCP_A3, tdb:CrTi-10Pav.tdb:HCP_A3, tdb:CrTi-22Sun.tdb:HCP_A3, tdb:CrTi-24Flo.tdb:HCP_A3, tdb:CrTi-98Sau-LB.tdb:HCP_A3, tdb:CrTi-99Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (8): PHASE and CONSTITUENT statements as written

[CrTi-00Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-00Zhu.tdb): HCP_A3, type code %A, sha256 `8e0045194fc6bbe4…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : CR TI% : VA : !
~~~~

[CrTi-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-02Gho.tdb): HCP_A3, type code %A, sha256 `cfa98d3054ed1a83…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR TI% : VA : !
~~~~

[CrTi-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav-3SL.tdb): HCP_A3, type code %A, sha256 `7566666f3d21bb88…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CR TI% : VA : !
~~~~

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): HCP_A3, type code %A, sha256 `72d079567c30caf6…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : CR TI% : VA : !
~~~~

[CrTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-22Sun.tdb): HCP_A3, type code %A, sha256 `636c20714b97be05…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CR TI% : VA : !
~~~~

[CrTi-24Flo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-24Flo.tdb): HCP_A3, type code %A, sha256 `aade304e745bf1bd…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CR TI% : VA : !
~~~~

[CrTi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-98Sau-LB.tdb): HCP_A3, type code %A, sha256 `ba7af58faf26ef72…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CR TI% : VA : !
~~~~

[CrTi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-99Lee.tdb): HCP_A3, type code %A, sha256 `6210a5bfed1fb282…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR TI% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-024-01090-2](https://doi.org/10.1007/s11669-024-01090-2) Agustin Flores, Sylvie Chatain, Paul Fossati, Frank Stein, Jean-Marc Joubert, Experimental Investigation and Thermodynamic Assessment of the Cr–Ti System, J. Phase Equilib. Diffus. 45, 417-432 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910203](https://doi.org/10.1515/ijmr-2000-910203) W. Zhuang, J. Shen, Y. Liu, L. Ling, S. Shang, Y. Du, J.C. Schuster, Z. Metallkd., 91, 121-27(2000).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2011.03.031](https://doi.org/10.1016/j.intermet.2011.03.031) D.M. Cupid, M.J. Kriegel, O. Fabrichnaya, F. Ebrahimi, and H.J. Seifert, Thermodynamic Assessment of the Cr–Ti and first Assessment of the Al–Cr–Ti Systems, Intermetallics, 2011, 19(8), p 1222-1235. https://doi.org/10.1016/j.intermet.2011.03.031  
_cited as the source of values for this phase_

## LIQUID (Cr–Ti)

- Id: `phase:cr-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 8 of 8 calculated diagram(s): 1676.96–4000 K, x(Ti) 0–1
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ti:liquid)

Names (12): _corpus: _corpus:phase:cr-ti:liquid  
_paper: _paper:10.1007/s11669-024-01090-2:Liquid, paper:10.1007/s11669-024-01090-2:liquid, paper:10.1361/105497102770331569:L  
_tdb: _tdb:CrTi-00Zhu.tdb:LIQUID, tdb:CrTi-02Gho.tdb:LIQUID, tdb:CrTi-10Pav-3SL.tdb:LIQUID, tdb:CrTi-10Pav.tdb:LIQUID, tdb:CrTi-22Sun.tdb:LIQUID, tdb:CrTi-24Flo.tdb:LIQUID, tdb:CrTi-98Sau-LB.tdb:LIQUID, tdb:CrTi-99Lee.tdb:LIQUID  


### TDB models of LIQUID (8): PHASE and CONSTITUENT statements as written

[CrTi-00Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-00Zhu.tdb): LIQUID, type code %, sha256 `8e0045194fc6bbe4…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : CR TI : !
~~~~

[CrTi-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-02Gho.tdb): LIQUID, type code %, sha256 `cfa98d3054ed1a83…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR TI : !
~~~~

[CrTi-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav-3SL.tdb): LIQUID, type code %, sha256 `7566666f3d21bb88…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CR TI : !
~~~~

[CrTi-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-10Pav.tdb): LIQUID, type code %, sha256 `72d079567c30caf6…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : CR TI : !
~~~~

[CrTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-22Sun.tdb): LIQUID, type code %, sha256 `636c20714b97be05…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CR TI : !
~~~~

[CrTi-24Flo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-24Flo.tdb): LIQUID, type code %, sha256 `aade304e745bf1bd…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CR TI : !
~~~~

[CrTi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-98Sau-LB.tdb): LIQUID, type code %, sha256 `ba7af58faf26ef72…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR TI : !
~~~~

[CrTi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTi-99Lee.tdb): LIQUID, type code %, sha256 `6210a5bfed1fb282…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR TI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01090-2](https://doi.org/10.1007/s11669-024-01090-2) Agustin Flores, Sylvie Chatain, Paul Fossati, Frank Stein, Jean-Marc Joubert, Experimental Investigation and Thermodynamic Assessment of the Cr–Ti System, J. Phase Equilib. Diffus. 45, 417-432 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910203](https://doi.org/10.1515/ijmr-2000-910203) W. Zhuang, J. Shen, Y. Liu, L. Ling, S. Shang, Y. Du, J.C. Schuster, Z. Metallkd., 91, 121-27(2000).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2011.03.031](https://doi.org/10.1016/j.intermet.2011.03.031) D.M. Cupid, M.J. Kriegel, O. Fabrichnaya, F. Ebrahimi, and H.J. Seifert, Thermodynamic Assessment of the Cr–Ti and first Assessment of the Al–Cr–Ti Systems, Intermetallics, 2011, 19(8), p 1222-1235. https://doi.org/10.1016/j.intermet.2011.03.031  
_cited as the source of values for this phase_
- [doi:10.1063/1.106450](https://doi.org/10.1063/1.106450) K. Ohsaka, E. H. Trinh, J. C. Holzer, W. L. Johnson, Gibbs free energy difference between the undercooled liquid and the β phase of a Ti-Cr alloy, Applied Physics Letters 60, 1079-1081 (1992).  
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
