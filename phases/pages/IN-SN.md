# In–Sn phases

> In–Sn system: 9 phases (tier A 7, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-SN.html · Markdown: https://data.orchid-project.org/phases/pages/IN-SN.md

9 phases (tier A 7, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-SN) · [full JSON](https://data.orchid-project.org/phases/systems/IN-SN.json) · [In–Sn system page](https://data.orchid-project.org/systems/IN-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Sn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-in-sn-a4-diamond); _phase:in-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [BCT_A5](#phase-in-sn-a5-bct); _phase:in-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 299.64–750.08 K, x(Sn) 0.70959–1 | 2 | 5 |
| [TETRAGONAL_A6](#phase-in-sn-a6-tetragonal); _phase:in-sn:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–429.75 K, x(Sn) 0–0.12654 | 2 | 5 |
| [BCC_A2](#phase-in-sn-bcc-a2); _phase:in-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-in-sn-fcc-a1); _phase:in-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-in-sn-hcp-a3); _phase:in-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [INSN_AF](#phase-in-sn-insn-af); _phase:in-sn:insn-af_ | HgSn12 · A_f · hP1 · P6/mmm (191) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 299.64–2500 K, x(Sn) 0–0.98093 | 4 | 5 |
| [LIQUID](#phase-in-sn-liquid); _phase:in-sn:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 391.1–2500 K, x(Sn) 0–1 | 6 | 5 |
| [TET_ALPHA1_A6](#phase-in-sn-tet-a6-alpha1); _phase:in-sn:tet-a6-alpha1_ | In · A6 · tI2 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–415.1 K, x(Sn) 0.12157–0.45149 | 4 | 5 |

## DIAMOND_A4 (In–Sn)

- Id: `phase:in-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:a4-diamond)

Names (5): _corpus: _corpus:phase:in-sn:a4-diamond  
_tdb: _tdb:InSn-03Moe.tdb:DIAMOND_A4, tdb:InSn-04Dav.tdb:DIAMOND_A4, tdb:InSn-96Lee.tdb:DIAMOND_A4, tdb:InSn-99Ans-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): DIAMOND_A4, type code %, sha256 `abc7f5fc726c8aa0…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): DIAMOND_A4, type code %, sha256 `1f3503fa95e0ad09…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SN : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): DIAMOND_A4, type code %, sha256 `eee2852c48eaf14e…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : SN : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): DIAMOND_A4, type code %, sha256 `0680f4def3b7ba99…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## BCT_A5 (In–Sn)

- Id: `phase:in-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 299.64–750.08 K, x(Sn) 0.70959–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:a5-bct)

Names (8): _corpus: _corpus:phase:in-sn:a5-bct, corpus:phase:in-sn:bct-a5  
_paper: _paper:10.1016/j.tca.2003.10.020:(βSn)  
_tdb: _tdb:InSn-03Moe.tdb:BCT_A5, tdb:InSn-04Dav.tdb:BCT_A5, tdb:InSn-96Lee.tdb:BCT_A5, tdb:InSn-98Kor.tdb:BCT_A5, tdb:InSn-99Ans-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): BCT_A5, type code %, sha256 `abc7f5fc726c8aa0…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : IN SN% : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): BCT_A5, type code %, sha256 `1f3503fa95e0ad09…`

~~~~text
53: PHASE BCT_A5 % 1 1 !
54: CONST BCT_A5 : IN SN% : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): BCT_A5, type code %, sha256 `eee2852c48eaf14e…`

~~~~text
44: PHASE BCT_A5 % 1 1 !
45: CONST BCT_A5 : IN SN% : !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): BCT_A5, type code %, sha256 `bb53889282aa9f06…`

~~~~text
42: PHASE BCT_A5 % 1 1 !
43: CONST BCT_A5 : IN SN% : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): BCT_A5, type code %, sha256 `0680f4def3b7ba99…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : IN SN% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## TETRAGONAL_A6 (In–Sn)

- Id: `phase:in-sn:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–429.75 K, x(Sn) 0–0.12654
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:a6-tetragonal)

Names (8): _corpus: _corpus:phase:in-sn:a6-tetragonal, corpus:phase:in-sn:tetragonal-a6  
_paper: _paper:10.1016/j.tca.2003.10.020:(In)  
_tdb: _tdb:InSn-03Moe.tdb:TETRAGONAL_A6, tdb:InSn-04Dav.tdb:TETRAGONAL_A6, tdb:InSn-96Lee.tdb:TETRAGONAL_A6, tdb:InSn-98Kor.tdb:TETRAGONAL_A6, tdb:InSn-99Ans-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): TETRAGONAL_A6, type code %, sha256 `abc7f5fc726c8aa0…`

~~~~text
54: PHASE TETRAGONAL_A6 % 1 1 !
55: CONST TETRAGONAL_A6 : IN% SN : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): TETRAGONAL_A6, type code %, sha256 `1f3503fa95e0ad09…`

~~~~text
58: PHASE TETRAGONAL_A6 % 1 1 !
59: CONST TETRAGONAL_A6 : IN% SN : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): TETRAGONAL_A6, type code %, sha256 `eee2852c48eaf14e…`

~~~~text
49: PHASE TETRAGONAL_A6 % 1 1 !
50: CONST TETRAGONAL_A6 : IN% SN : !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): TETRAGONAL_A6, type code %, sha256 `bb53889282aa9f06…`

~~~~text
47: PHASE TETRAGONAL_A6 % 1 1 !
48: CONST TETRAGONAL_A6 : IN% SN : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): TETRAGONAL_A6, type code %, sha256 `0680f4def3b7ba99…`

~~~~text
51: PHASE TETRAGONAL_A6 % 1 1 !
52: CONST TETRAGONAL_A6 : IN% SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## BCC_A2 (In–Sn)

- Id: `phase:in-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:bcc-a2)

Names (6): _corpus: _corpus:phase:in-sn:bcc-a2  
_tdb: _tdb:InSn-03Moe.tdb:BCC_A2, tdb:InSn-04Dav.tdb:BCC_A2, tdb:InSn-96Lee.tdb:BCC_A2, tdb:InSn-98Kor.tdb:BCC_A2, tdb:InSn-99Ans-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): BCC_A2, type code %B, sha256 `abc7f5fc726c8aa0…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : IN SN : VA : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): BCC_A2, type code %B, sha256 `1f3503fa95e0ad09…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : IN SN : VA : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): BCC_A2, type code %B, sha256 `eee2852c48eaf14e…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : IN SN : VA : !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): BCC_A2, type code %B, sha256 `bb53889282aa9f06…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : IN SN : VA : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): BCC_A2, type code %B, sha256 `0680f4def3b7ba99…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : IN SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## FCC_A1 (In–Sn)

- Id: `phase:in-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:fcc-a1)

Names (6): _corpus: _corpus:phase:in-sn:fcc-a1  
_tdb: _tdb:InSn-03Moe.tdb:FCC_A1, tdb:InSn-04Dav.tdb:FCC_A1, tdb:InSn-96Lee.tdb:FCC_A1, tdb:InSn-98Kor.tdb:FCC_A1, tdb:InSn-99Ans-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): FCC_A1, type code %A, sha256 `abc7f5fc726c8aa0…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : IN SN : VA : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): FCC_A1, type code %A, sha256 `1f3503fa95e0ad09…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : IN SN : VA : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): FCC_A1, type code %A, sha256 `eee2852c48eaf14e…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : IN SN : VA : !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): FCC_A1, type code %A, sha256 `bb53889282aa9f06…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : IN SN : VA : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): FCC_A1, type code %A, sha256 `0680f4def3b7ba99…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : IN SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## HCP_A3 (In–Sn)

- Id: `phase:in-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:hcp-a3)

Names (6): _corpus: _corpus:phase:in-sn:hcp-a3  
_tdb: _tdb:InSn-03Moe.tdb:HCP_A3, tdb:InSn-04Dav.tdb:HCP_A3, tdb:InSn-96Lee.tdb:HCP_A3, tdb:InSn-98Kor.tdb:HCP_A3, tdb:InSn-99Ans-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): HCP_A3, type code %A, sha256 `abc7f5fc726c8aa0…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : IN SN : VA: !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): HCP_A3, type code %A, sha256 `1f3503fa95e0ad09…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : IN SN : VA: !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): HCP_A3, type code %A, sha256 `eee2852c48eaf14e…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : IN SN : VA: !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): HCP_A3, type code %A, sha256 `bb53889282aa9f06…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : IN SN : VA: !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): HCP_A3, type code %A, sha256 `0680f4def3b7ba99…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : IN SN : VA: !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## INSN_AF (In–Sn)

- Id: `phase:in-sn:insn-af`; status `assigned`
- Structure: HgSn12 · A_f · hP1 · P6/mmm (191); type `st:a-f-hgsn12-hp1`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 299.64–2500 K, x(Sn) 0–0.98093
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:insn-af)

Names (7): _corpus: _corpus:phase:in-sn:insn-af  
_paper: _paper:10.1016/j.tca.2003.10.020:γ  
_tdb: _tdb:InSn-03Moe.tdb:INSN_AF, tdb:InSn-04Dav.tdb:INSN_AF, tdb:InSn-96Lee.tdb:INSN_AF, tdb:InSn-98Kor.tdb:INSN_AF, tdb:InSn-99Ans-LB.tdb:INSN_AF  


### TDB models of INSN_AF (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): INSN_AF, type code %, sha256 `abc7f5fc726c8aa0…`

~~~~text
64: PHASE INSN_AF % 1 1 !
65: CONST INSN_AF : IN SN : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): INSN_AF, type code %, sha256 `1f3503fa95e0ad09…`

~~~~text
68: PHASE INSN_AF % 1 1 !
69: CONST INSN_AF : IN SN : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): INSN_AF, type code %, sha256 `eee2852c48eaf14e…`

~~~~text
59: PHASE INSN_AF % 1 1 !
60: CONST INSN_AF : IN SN : !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): INSN_AF, type code %, sha256 `bb53889282aa9f06…`

~~~~text
57: PHASE INSN_AF % 1 1 !
58: CONST INSN_AF : IN SN : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): INSN_AF, type code %, sha256 `0680f4def3b7ba99…`

~~~~text
61: PHASE INSN_AF % 1 1 !
62: CONST INSN_AF : IN SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## LIQUID (In–Sn)

- Id: `phase:in-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 391.1–2500 K, x(Sn) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:liquid)

Names (7): _corpus: _corpus:phase:in-sn:liquid  
_paper: _paper:10.1016/j.tca.2003.10.020:L  
_tdb: _tdb:InSn-03Moe.tdb:LIQUID, tdb:InSn-04Dav.tdb:LIQUID, tdb:InSn-96Lee.tdb:LIQUID, tdb:InSn-98Kor.tdb:LIQUID, tdb:InSn-99Ans-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): LIQUID, type code %, sha256 `abc7f5fc726c8aa0…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : IN SN : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): LIQUID, type code %, sha256 `1f3503fa95e0ad09…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : IN SN : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): LIQUID, type code %, sha256 `eee2852c48eaf14e…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : IN SN : !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): LIQUID, type code %, sha256 `bb53889282aa9f06…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : IN SN : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): LIQUID, type code %, sha256 `0680f4def3b7ba99…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : IN SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
_assessment that models this phase_

## TET_ALPHA1_A6 (In–Sn)

- Id: `phase:in-sn:tet-a6-alpha1`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:ALPHA1); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 5 of 5 calculated diagram(s): 300–415.1 K, x(Sn) 0.12157–0.45149
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sn:tet-a6-alpha1)

Names (8): _corpus: _corpus:phase:in-sn:tet-a6-alpha1, corpus:phase:in-sn:tet-alpha1-a6  
_paper: _paper:10.1016/j.tca.2003.10.020:β  
_tdb: _tdb:InSn-03Moe.tdb:TET_ALPHA1_A6, tdb:InSn-04Dav.tdb:TET_ALPHA1_A6, tdb:InSn-96Lee.tdb:TET_ALPHA1_A6, tdb:InSn-98Kor.tdb:TET_ALPHA1_A6, tdb:InSn-99Ans-LB.tdb:TET_ALPHA1_A6  


### TDB models of TET_ALPHA1_A6 (5): PHASE and CONSTITUENT statements as written

[InSn-03Moe.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-03Moe.tdb): TET_ALPHA1_A6, type code %, sha256 `abc7f5fc726c8aa0…`

~~~~text
59: PHASE TET_ALPHA1_A6 % 1 1 !
60: CONST TET_ALPHA1_A6 : IN SN : !
~~~~

[InSn-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-04Dav.tdb): TET_ALPHA1_A6, type code %, sha256 `1f3503fa95e0ad09…`

~~~~text
63: PHASE TET_ALPHA1_A6 % 1 1 !
64: CONST TET_ALPHA1_A6 : IN SN : !
~~~~

[InSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-96Lee.tdb): TET_ALPHA1_A6, type code %, sha256 `eee2852c48eaf14e…`

~~~~text
54: PHASE TET_ALPHA1_A6 % 1 1 !
55: CONST TET_ALPHA1_A6 : IN SN : !
~~~~

[InSn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-98Kor.tdb): TET_ALPHA1_A6, type code %, sha256 `bb53889282aa9f06…`

~~~~text
52: PHASE TET_ALPHA1_A6 % 1 1 !
53: CONST TET_ALPHA1_A6 : IN SN : !
~~~~

[InSn-99Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSn-99Ans-LB.tdb): TET_ALPHA1_A6, type code %, sha256 `0680f4def3b7ba99…`

~~~~text
56: PHASE TET_ALPHA1_A6 % 1 1 !
57: CONST TET_ALPHA1_A6 : IN SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00325-6](https://doi.org/10.1016/S0925-8388%2803%2900325-6) N. Moelans, K.C. Hari Kumar, P. Wollants, J. Alloys Compd., 360, 98-106(2003).  
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
