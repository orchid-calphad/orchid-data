# Fe–Zn phases

> Fe–Zn system: 8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/FE-ZN.md

8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/FE-ZN.json) · [Fe–Zn system page](https://data.orchid-project.org/systems/FE-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Zn system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-zn-bcc-a2); _phase:fe-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1841.7 K, x(Zn) 0–0.46428 | 14 | 5 |
| [FCC_A1](#phase-fe-zn-fcc-a1); _phase:fe-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 1084.45–1701.07 K, x(Zn) 0–0.40105 | 0 | 5 |
| [FE3ZN7_D82](#phase-fe-zn-fe3zn7-d82); _phase:fe-zn:fe3zn7-d82_ | Cu5Zn8 · D8_2 · cI52 · I-43m (217) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1056.68 K, x(Zn) 0.66339–0.81554 | 44 | 5 |
| [FEZN10](#phase-fe-zn-fezn10); _phase:fe-zn:fezn10_ | FeZn10 · hP632 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–945.49 K, x(Zn) 0.85904–0.92268 | 56 | 5 |
| [FEZN13](#phase-fe-zn-fezn13); _phase:fe-zn:fezn13_ | CoZn13 · mC28 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–805.07 K, x(Zn) 0.92788–0.94125 | 45 | 5 |
| [FEZN4](#phase-fe-zn-fezn4); _phase:fe-zn:fezn4_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–824.1 K, x(Zn) 0.74689–0.84076 | 21 | 5 |
| [HCP_A3](#phase-fe-zn-hcp-a3); _phase:fe-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–692.98 K, x(Zn) 0.99932–1 | 15 | 5 |
| [LIQUID](#phase-fe-zn-liquid); _phase:fe-zn:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 300.36–2500 K, x(Zn) 0–1 | 58 | 5 |

## BCC_A2 (Fe–Zn)

- Id: `phase:fe-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1841.7 K, x(Zn) 0–0.46428
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:bcc-a2)

Names (9): _corpus: _corpus:phase:fe-zn:bcc-a2  
_paper: _paper:10.1016/j.calphad.2009.01.002:(αFe), paper:10.1016/s0925-8388(01)01273-7:α-Fe(b.c.c.), paper:10.2298/jmmb1101001t:(αFe)  
_tdb: _tdb:FeZn-00Reu-LB.tdb:BCC_A2, tdb:FeZn-01Su.tdb:BCC_A2, tdb:FeZn-05Su.tdb:BCC_A2, tdb:FeZn-09Xio.tdb:BCC_A2, tdb:FeZn-11Tan.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): BCC_A2, type code %B, sha256 `d4504e582665577a…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : FE% ZN : VA : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): BCC_A2, type code %B, sha256 `7ec69901e59741d2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% ZN : VA : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): BCC_A2, type code %B, sha256 `7315dc671e2b7ec8…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% ZN : VA : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): BCC_A2, type code %B, sha256 `adfbe318ba501357…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% ZN : VA : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): BCC_A2, type code %B, sha256 `fd6a097e34a77fe3…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% ZN : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1980-710303](https://doi.org/10.1515/ijmr-1980-710303) P.J. Gellings, G. Gierman, D. Koster, J. Kuit, Z. Metallkd., 71 (1980) 150.  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Zn)

- Id: `phase:fe-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1084.45–1701.07 K, x(Zn) 0–0.40105
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:fcc-a1)

Names (6): _corpus: _corpus:phase:fe-zn:fcc-a1  
_tdb: _tdb:FeZn-00Reu-LB.tdb:FCC_A1, tdb:FeZn-01Su.tdb:FCC_A1, tdb:FeZn-05Su.tdb:FCC_A1, tdb:FeZn-09Xio.tdb:FCC_A1, tdb:FeZn-11Tan.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): FCC_A1, type code %A, sha256 `d4504e582665577a…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : FE% ZN : VA : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): FCC_A1, type code %A, sha256 `7ec69901e59741d2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% ZN : VA : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): FCC_A1, type code %A, sha256 `7315dc671e2b7ec8…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% ZN : VA : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): FCC_A1, type code %A, sha256 `adfbe318ba501357…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% ZN : VA : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): FCC_A1, type code %A, sha256 `fd6a097e34a77fe3…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% ZN : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase_

## FE3ZN7_D82 (Fe–Zn)

- Id: `phase:fe-zn:fe3zn7-d82`; status `assigned`
- Structure: Cu5Zn8 · D8_2 · cI52 · I-43m (217); type `st:d8-2-cu5zn8-ci52`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeZn-00Reu-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeZn-09Xio.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeZn-11Tan.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1056.68 K, x(Zn) 0.66339–0.81554
- Literature: 44 values (44 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:fe3zn7-d82)

Names (10): _corpus: _corpus:phase:fe-zn:fe3zn7-d82  
_paper: _paper:10.1016/j.calphad.2009.01.002:Γ, paper:10.1016/s0925-8388(01)01273-7:Γ, paper:10.2298/jmmb1101001t:Γ  
_system_alias: _system_alias:fe-zn:Gamma  
_tdb: _tdb:FeZn-00Reu-LB.tdb:FE3ZN7_D82, tdb:FeZn-01Su.tdb:FE3ZN7_D82, tdb:FeZn-05Su.tdb:FE3ZN7_D82, tdb:FeZn-09Xio.tdb:FE3ZN7_D82, tdb:FeZn-11Tan.tdb:FE3ZN7_D82  


### TDB models of FE3ZN7_D82 (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): FE3ZN7_D82, type code %, sha256 `d4504e582665577a…`

~~~~text
42: PHASE FE3ZN7_D82 % 2 0.3 0.7 !
43: CONST FE3ZN7_D82 : FE% ZN : FE ZN% : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): FE3ZN7_D82, type code %, sha256 `7ec69901e59741d2…`

~~~~text
46: PHASE FE3ZN7_D82 % 2 10 16 !
47: CONST FE3ZN7_D82 : FE ZN : ZN : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): FE3ZN7_D82, type code %, sha256 `7315dc671e2b7ec8…`

~~~~text
46: PHASE FE3ZN7_D82 % 2 10 16 !
47: CONST FE3ZN7_D82 : FE ZN : ZN : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): FE3ZN7_D82, type code %, sha256 `adfbe318ba501357…`

~~~~text
45: PHASE FE3ZN7_D82 % 4 0.154 0.154 0.231 0.461 !
46: CONST FE3ZN7_D82 : FE ZN : FE ZN : FE ZN : ZN : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): FE3ZN7_D82, type code %, sha256 `fd6a097e34a77fe3…`

~~~~text
46: PHASE FE3ZN7_D82 % 4 0.154 0.154 0.231 0.461 !
47: CONST FE3ZN7_D82 : FE ZN : FE ZN : FE ZN : ZN : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1980-710303](https://doi.org/10.1515/ijmr-1980-710303) P.J. Gellings, G. Gierman, D. Koster, J. Kuit, Z. Metallkd., 71 (1980) 150.  
_cited as the source of values for this phase_
- [doi:10.1006/jssc.2000.8626](https://doi.org/10.1006/jssc.2000.8626) Claude H.E. Belin, Renaud C.H. Belin, Synthesis and Crystal Structure Determinations in the Γ and δ Phase Domains of the Iron–Zinc System: Electronic and Bonding Analysis of Fe13Zn39 and FeZn10, a Subtle Deviation from the Hume–Rothery Standard?, Journal of Solid State Chemistry 151, 85-95 (2000).  
_cited as the source of values for this phase_

## FEZN10 (Fe–Zn)

- Id: `phase:fe-zn:fezn10`; status `assigned`
- Structure: FeZn10 · hP632 · P6_3/mmc (194); type `st:fezn10-hp632`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 5 of 5 calculated diagram(s): 300–945.49 K, x(Zn) 0.85904–0.92268
- Literature: 56 values (56 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:fezn10)

Names (11): _corpus: _corpus:phase:fe-zn:fezn10  
_paper: _paper:10.1016/j.calphad.2009.01.002:δ, paper:10.1016/s0925-8388(01)01273-7:δ, paper:10.1361/105497100770339905:δ1, paper:10.2298/jmmb1101001t:δ  
_system_alias: _system_alias:fe-zn:delta  
_tdb: _tdb:FeZn-00Reu-LB.tdb:FEZN10, tdb:FeZn-01Su.tdb:FEZN10, tdb:FeZn-05Su.tdb:FEZN10, tdb:FeZn-09Xio.tdb:FEZN10, tdb:FeZn-11Tan.tdb:FEZN10  


### TDB models of FEZN10 (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): FEZN10, type code %, sha256 `d4504e582665577a…`

~~~~text
52: PHASE FEZN10 % 2 0.125 0.875 !
53: CONST FEZN10 : FE% ZN : FE ZN% : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): FEZN10, type code %, sha256 `7ec69901e59741d2…`

~~~~text
56: PHASE FEZN10 % 3 2 4 20 !
57: CONST FEZN10 : FE : FE ZN : ZN : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): FEZN10, type code %, sha256 `7315dc671e2b7ec8…`

~~~~text
56: PHASE FEZN10 % 3 2 4 20 !
57: CONST FEZN10 : FE : FE ZN : ZN : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): FEZN10, type code %, sha256 `adfbe318ba501357…`

~~~~text
55: PHASE FEZN10 % 3 0.058 0.18 0.762 !
56: CONST FEZN10 : FE : FE ZN : ZN : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): FEZN10, type code %, sha256 `fd6a097e34a77fe3…`

~~~~text
56: PHASE FEZN10 % 3 0.058 0.18 0.762 !
57: CONST FEZN10 : FE : FE ZN : ZN : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1006/jssc.2000.8626](https://doi.org/10.1006/jssc.2000.8626) Claude H.E. Belin, Renaud C.H. Belin, Synthesis and Crystal Structure Determinations in the Γ and δ Phase Domains of the Iron–Zinc System: Electronic and Bonding Analysis of Fe13Zn39 and FeZn10, a Subtle Deviation from the Hume–Rothery Standard?, Journal of Solid State Chemistry 151, 85-95 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1980-710303](https://doi.org/10.1515/ijmr-1980-710303) P.J. Gellings, G. Gierman, D. Koster, J. Kuit, Z. Metallkd., 71 (1980) 150.  
_cited as the source of values for this phase_
- [doi:10.1002/srin.198004874](https://doi.org/10.1002/srin.198004874) Peter Reutner, Hans-Jürgen Engeil, Elektrochemische Untersuchungen über die Thermodynamik der intermetallischen Phasen des Systems Esen-Znk, Archiv für das Eisenhüttenwesen 51, 457-462 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(88)87199-5](https://doi.org/10.1016/0040-6031%2888%2987199-5) Stephan Petersen, Philip J. Spencer, Klaus Hack, A thermodynamic evaluation of the iron-zinc system, Thermochimica Acta 129, 77-87 (1988).  
_cited as the source of values for this phase_

## FEZN13 (Fe–Zn)

- Id: `phase:fe-zn:fezn13`; status `assigned`
- Structure: CoZn13 · mC28 · C2/m (12); type `st:cozn13-mc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 5 of 5 calculated diagram(s): 300–805.07 K, x(Zn) 0.92788–0.94125
- Literature: 45 values (45 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:fezn13)

Names (11): _corpus: _corpus:phase:fe-zn:fezn13  
_paper: _paper:10.1016/j.calphad.2009.01.002:ζ, paper:10.1016/s0925-8388(01)01273-7:ζ, paper:10.1361/105497100770339905:ζ, paper:10.2298/jmmb1101001t:ζ  
_system_alias: _system_alias:fe-zn:zeta  
_tdb: _tdb:FeZn-00Reu-LB.tdb:FEZN13, tdb:FeZn-01Su.tdb:FEZN13, tdb:FeZn-05Su.tdb:FEZN13, tdb:FeZn-09Xio.tdb:FEZN13, tdb:FeZn-11Tan.tdb:FEZN13  


### TDB models of FEZN13 (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): FEZN13, type code %, sha256 `d4504e582665577a…`

~~~~text
57: PHASE FEZN13 % 2 0.072 0.928 !
58: CONST FEZN13 : FE% ZN : FE ZN% : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): FEZN13, type code %, sha256 `7ec69901e59741d2…`

~~~~text
61: PHASE FEZN13 % 2 1 13 !
62: CONST FEZN13 : FE : ZN : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): FEZN13, type code %, sha256 `7315dc671e2b7ec8…`

~~~~text
61: PHASE FEZN13 % 2 1 13 !
62: CONST FEZN13 : FE : ZN : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): FEZN13, type code %, sha256 `adfbe318ba501357…`

~~~~text
60: PHASE FEZN13 % 3 0.072 0.856 0.072 !
61: CONST FEZN13 : FE VA : ZN : ZN VA : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): FEZN13, type code %, sha256 `fd6a097e34a77fe3…`

~~~~text
61: PHASE FEZN13 % 3 0.072 0.856 0.072 !
62: CONST FEZN13 : FE VA : ZN : ZN VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1007/bf02830333](https://doi.org/10.1007/bf02830333) Oswald N. C. Uwakweh, Zhentong Liu, Aszetta Jordan, Bryan Chakoumakos, Stephen Spooner, Philip Maziasz, Neutron diffraction and phase evolution of the mechanically alloyed intermetallic compound ζ-FeZn13, Metall Mater Trans A 31, 2739-2745 (2000).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.198004874](https://doi.org/10.1002/srin.198004874) Peter Reutner, Hans-Jürgen Engeil, Elektrochemische Untersuchungen über die Thermodynamik der intermetallischen Phasen des Systems Esen-Znk, Archiv für das Eisenhüttenwesen 51, 457-462 (1980).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1980-710303](https://doi.org/10.1515/ijmr-1980-710303) P.J. Gellings, G. Gierman, D. Koster, J. Kuit, Z. Metallkd., 71 (1980) 150.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(88)87199-5](https://doi.org/10.1016/0040-6031%2888%2987199-5) Stephan Petersen, Philip J. Spencer, Klaus Hack, A thermodynamic evaluation of the iron-zinc system, Thermochimica Acta 129, 77-87 (1988).  
_cited as the source of values for this phase_

## FEZN4 (Fe–Zn)

- Id: `phase:fe-zn:fezn4`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): Fe11Zn40 · cF408 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Fe11Zn40 · cF408 · F-43m (216) — Hallstedt 2025 mmc2 row for FEZN4: FeZn4 (Gamma_1)
- Candidate (tdb_comment): Fe11Zn40 · cF408 · F-43m — FeZn-00Reu-LB.tdb: 'Prototype Fe11Zn40 (cF408, F-43m), Gamma_1'
- Candidate (tdb_comment): Fe11Zn40 · cF408 · F-43m — FeZn-01Su.tdb: 'Prototype Fe11Zn40 (cF408, F-43m), Gamma_1'
- Candidate (tdb_comment): Fe11Zn40 · cF408 · F-43m — FeZn-05Su.tdb: 'Prototype Fe11Zn40 (cF408, F-43m), Gamma_1'
- Candidate (tdb_comment): Fe11Zn40 · cF408 · F-43m — FeZn-09Xio.tdb: 'Prototype Fe11Zn40 (cF408, F-43m), Gamma_1'
- Candidate (tdb_comment): Fe11Zn40 · cF408 · F-43m — FeZn-11Tan.tdb: 'Prototype Fe11Zn40 (cF408, F-43m), Gamma_1'
- Stability: stable in 5 of 5 calculated diagram(s): 300–824.1 K, x(Zn) 0.74689–0.84076
- Literature: 21 values (21 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:fezn4)

Names (11): _corpus: _corpus:phase:fe-zn:fezn4  
_paper: _paper:10.1016/j.calphad.2009.01.002:Γ1, paper:10.1016/s0925-8388(01)01273-7:Γ1, paper:10.1361/105497100770339905:Γ1, paper:10.2298/jmmb1101001t:Γ1  
_system_alias: _system_alias:fe-zn:Gamma1  
_tdb: _tdb:FeZn-00Reu-LB.tdb:FEZN4, tdb:FeZn-01Su.tdb:FEZN4, tdb:FeZn-05Su.tdb:FEZN4, tdb:FeZn-09Xio.tdb:FEZN4, tdb:FeZn-11Tan.tdb:FEZN4  


### TDB models of FEZN4 (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): FEZN4, type code %, sha256 `d4504e582665577a…`

~~~~text
47: PHASE FEZN4 % 2 0.25 0.75 !
48: CONST FEZN4 : FE% ZN : FE ZN% : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): FEZN4, type code %, sha256 `7ec69901e59741d2…`

~~~~text
51: PHASE FEZN4 % 2 14 12 !
52: CONST FEZN4 : FE ZN : ZN : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): FEZN4, type code %, sha256 `7315dc671e2b7ec8…`

~~~~text
51: PHASE FEZN4 % 2 14 12 !
52: CONST FEZN4 : FE ZN : ZN : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): FEZN4, type code %, sha256 `adfbe318ba501357…`

~~~~text
50: PHASE FEZN4 % 3 0.137 0.118 0.745 !
51: CONST FEZN4 : FE : FE ZN : ZN : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): FEZN4, type code %, sha256 `fd6a097e34a77fe3…`

~~~~text
51: PHASE FEZN4 % 3 0.137 0.118 0.745 !
52: CONST FEZN4 : FE : FE ZN : ZN : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1002/srin.198004874](https://doi.org/10.1002/srin.198004874) Peter Reutner, Hans-Jürgen Engeil, Elektrochemische Untersuchungen über die Thermodynamik der intermetallischen Phasen des Systems Esen-Znk, Archiv für das Eisenhüttenwesen 51, 457-462 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(88)87199-5](https://doi.org/10.1016/0040-6031%2888%2987199-5) Stephan Petersen, Philip J. Spencer, Klaus Hack, A thermodynamic evaluation of the iron-zinc system, Thermochimica Acta 129, 77-87 (1988).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1980-710303](https://doi.org/10.1515/ijmr-1980-710303) P.J. Gellings, G. Gierman, D. Koster, J. Kuit, Z. Metallkd., 71 (1980) 150.  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Zn)

- Id: `phase:fe-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–692.98 K, x(Zn) 0.99932–1
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:hcp-a3)

Names (9): _corpus: _corpus:phase:fe-zn:hcp-a3  
_paper: _paper:10.1016/j.calphad.2009.01.002:(Zn), paper:10.1016/s0925-8388(01)01273-7:Zn(h.c.p.), paper:10.2298/jmmb1101001t:(Zn)  
_tdb: _tdb:FeZn-00Reu-LB.tdb:HCP_A3, tdb:FeZn-01Su.tdb:HCP_A3, tdb:FeZn-05Su.tdb:HCP_A3, tdb:FeZn-09Xio.tdb:HCP_A3, tdb:FeZn-11Tan.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): HCP_A3, type code %, sha256 `d4504e582665577a…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : FE ZN : VA : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): HCP_A3, type code %, sha256 `7ec69901e59741d2…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : FE ZN : VA : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): HCP_A3, type code %, sha256 `7315dc671e2b7ec8…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : FE ZN : VA : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): HCP_A3, type code %, sha256 `adfbe318ba501357…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : FE ZN : VA : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): HCP_A3, type code %, sha256 `fd6a097e34a77fe3…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : FE ZN : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1980-710303](https://doi.org/10.1515/ijmr-1980-710303) P.J. Gellings, G. Gierman, D. Koster, J. Kuit, Z. Metallkd., 71 (1980) 150.  
_cited as the source of values for this phase_

## LIQUID (Fe–Zn)

- Id: `phase:fe-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300.36–2500 K, x(Zn) 0–1
- Literature: 58 values (58 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-zn:liquid)

Names (9): _corpus: _corpus:phase:fe-zn:liquid  
_paper: _paper:10.1016/j.calphad.2009.01.002:L, paper:10.1016/s0925-8388(01)01273-7:L, paper:10.2298/jmmb1101001t:L  
_tdb: _tdb:FeZn-00Reu-LB.tdb:LIQUID, tdb:FeZn-01Su.tdb:LIQUID, tdb:FeZn-05Su.tdb:LIQUID, tdb:FeZn-09Xio.tdb:LIQUID, tdb:FeZn-11Tan.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[FeZn-00Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-00Reu-LB.tdb): LIQUID, type code %, sha256 `d4504e582665577a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : FE ZN : !
~~~~

[FeZn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-01Su.tdb): LIQUID, type code %, sha256 `7ec69901e59741d2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE ZN : !
~~~~

[FeZn-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-05Su.tdb): LIQUID, type code %, sha256 `7315dc671e2b7ec8…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE ZN : !
~~~~

[FeZn-09Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-09Xio.tdb): LIQUID, type code %, sha256 `adfbe318ba501357…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE ZN : !
~~~~

[FeZn-11Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeZn-11Tan.tdb): LIQUID, type code %, sha256 `fd6a097e34a77fe3…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE ZN : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2009.01.002](https://doi.org/10.1016/j.calphad.2009.01.002) Wei Xiong, Yi Kong, Yong Du, Zi-Kui Liu, Malin Selleby, Wei-Hua Sun, Thermodynamic investigation of the galvanizing systems, I: Refinement of the thermodynamic description for the Fe–Zn system, Calphad 33, 433-440 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01273-7](https://doi.org/10.1016/S0925-8388%2801%2901273-7) X. Su, N.-Y. Tang, J.M. Toguri, J. Alloys Compd., 325, 129-36(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.2298/JMMB1101001T](https://doi.org/10.2298/JMMB1101001T) Y. Tang, X. Yuan, Y. Du, W. Xiong, J. Mining Metall. B, 47, 1-10(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.12.031](https://doi.org/10.1016/j.jallcom.2004.12.031) Xuping Su, Fucheng Yin, Zhi Li, Nai-Yong Tang, Manxiu Zhao, Thermodynamic calculation of the Fe–Zn–Si system, Journal of Alloys and Compounds 396, 156-163 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497100770339905](https://doi.org/10.1361/105497100770339905) G. Reumont, P. Perrot, J. M. Fiorani, J. Hertz, Thermodynamic assessment of the Fe-Zn system, JPE 21, 371-378 (2000).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1980-710303](https://doi.org/10.1515/ijmr-1980-710303) P.J. Gellings, G. Gierman, D. Koster, J. Kuit, Z. Metallkd., 71 (1980) 150.  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
