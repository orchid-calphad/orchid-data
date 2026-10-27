# Mg–Nd phases

> Mg–Nd system: 11 phases (tier A 6, tier C 4, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-ND.html · Markdown: https://data.orchid-project.org/phases/pages/MG-ND.md

11 phases (tier A 6, tier C 4, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-ND) · [full JSON](https://data.orchid-project.org/phases/systems/MG-ND.json) · [Mg–Nd system page](https://data.orchid-project.org/systems/MG-ND.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-ND.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Nd system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-nd-bcc-a2); _phase:mg-nd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 7 calculated diagram(s): 816.55–2499.34 K, x(Nd) 0.67009–1 | 15 | 9 |
| [B2_BCC](#phase-mg-nd-bcc-b2); _phase:mg-nd:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1289.06 K, x(Nd) 0.45149–1 | 8 | 4 |
| [MG2M_C15](#phase-mg-nd-c15-mg2m); _phase:mg-nd:c15-mg2m_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 932.13–1028.31 K, x(Nd) 0.33333–0.33333 | 18 | 7 |
| [MG3M_D03](#phase-mg-nd-d03-mg3m); _phase:mg-nd:d03-mg3m_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–1059.11 K, x(Nd) 0.19478–0.25 | 20 | 7 |
| [DHCP](#phase-mg-nd-dhcp-a3); _phase:mg-nd:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1284.25 K, x(Nd) 0.91156–1 | 6 | 7 |
| [FCC_A1](#phase-mg-nd-fcc-a1); _phase:mg-nd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [HCP_A3](#phase-mg-nd-hcp-a3); _phase:mg-nd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–932.95 K, x(Nd) 0–0.00949 | 6 | 7 |
| [LIQUID](#phase-mg-nd-liquid); _phase:mg-nd:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 817.44–2500 K, x(Nd) 0–1 | 33 | 7 |
| [MG41M5](#phase-mg-nd-mg41m5); _phase:mg-nd:mg41m5_ | Ce5Mg41 · tI92 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–833.27 K, x(Nd) 0.1087–0.1087 | 8 | 5 |
| [MG41ND5](#phase-mg-nd-mg41nd5); _phase:mg-nd:mg41nd5_ | Ce5Mg41 · tI92 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–832.46 K, x(Nd) 0.10135–0.1087 | 4 | 2 |
| [MGND_B2](#phase-mg-nd-mgnd-b2); _phase:mg-nd:mgnd-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1078.25 K, x(Nd) 0.48371–0.5 | 0 | 3 |

## BCC_A2 (Mg–Nd)

- Id: `phase:mg-nd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 7 calculated diagram(s): 816.55–2499.34 K, x(Nd) 0.67009–1
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:bcc-a2)

Names (14): _corpus: _corpus:phase:mg-nd:bcc-a2  
_paper: _paper:10.1016/j.calphad.2010.07.010:bcc_A2, paper:10.1016/j.jallcom.2010.07.056:BCC_A2, paper:10.1016/s1003-6326(07)60051-x:BCC_A2, paper:10.1016/s1003-6326(07)60051-x:BCC_B2  
_tdb: _tdb:MgNd-05Gor-RK.tdb:BCC_A2, tdb:MgNd-05Gor-ass.tdb:BCC_A2, tdb:MgNd-06Guo.tdb:BCC_A2, tdb:MgNd-07Men.tdb:A2_BCC, tdb:MgNd-07Men.tdb:BCC_A2, tdb:MgNd-08Guo.tdb:BCC_A2, tdb:MgNd-10Niu.tdb:BCC_A2, tdb:MgNd-11Qi.tdb:A2_BCC, tdb:MgNd-11Qi.tdb:BCC_A2  


### TDB models of BCC_A2 (9): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): BCC_A2, type code %B, sha256 `f7a30de1313053e0…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : MG ND% : VA% : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): BCC_A2, type code %B, sha256 `78190c1f09693a34…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : MG ND% : VA% : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): BCC_A2, type code %B, sha256 `40b7e9ee569d905d…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : MG ND% : VA% : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): A2_BCC, type code %B, sha256 `e6ae632117b97396…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : MG ND : VA% : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): BCC_A2, type code %B, sha256 `e6ae632117b97396…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MG ND% : VA% : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): BCC_A2, type code %B, sha256 `cf2db92d7efdb61e…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MG ND% : VA% : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): BCC_A2, type code %B, sha256 `875ad4d46a8d6b2b…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MG ND% : VA% : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): A2_BCC, type code %B, sha256 `60cd25bc6483030f…`

~~~~text
42: PHASE A2_BCC %B 2 1 3 !
43: CONST A2_BCC : MG ND : VA% : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): BCC_A2, type code %B, sha256 `60cd25bc6483030f…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : MG ND% : VA% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_
- [doi:10.1016/s1003-6326(07)60051-x](https://doi.org/10.1016/s1003-6326%2807%2960051-x) Fan-gui MENG, Hua-shan LIU, Li-bin LIU, Zhan-peng JIN, Thermodynamic optimization of Mg-Nd system, Transactions of Nonferrous Metals Society of China 17, 77-81 (2007).  
_reports values for this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## B2_BCC (Mg–Nd)

- Id: `phase:mg-nd:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: MgNd-07Men.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: MgNd-08Guo.tdb: ordered phase with disordered part BCC_A2 (order/disorder model)
- Caveat: MgNd-10Niu.tdb: ordered phase with disordered part BCC_A2 (order/disorder model)
- Caveat: MgNd-11Qi.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in MgNd-07Men.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgNd-08Guo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgNd-10Niu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgNd-11Qi.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1289.06 K, x(Nd) 0.45149–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:bcc-b2)

Names (7): _corpus: _corpus:phase:mg-nd:bcc-b2, corpus:phase:mg-nd:b2-bcc  
_paper: _paper:10.1016/j.jallcom.2010.07.056:B2  
_tdb: _tdb:MgNd-07Men.tdb:B2_BCC, tdb:MgNd-08Guo.tdb:B2_BCC, tdb:MgNd-10Niu.tdb:B2_BCC, tdb:MgNd-11Qi.tdb:B2_BCC  


### TDB models of B2_BCC (4): PHASE and CONSTITUENT statements as written

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): B2_BCC, type code %BO, sha256 `e6ae632117b97396…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : MG% ND : MG ND% : VA : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): B2_BCC, type code %BO, sha256 `cf2db92d7efdb61e…`

~~~~text
35: PHASE B2_BCC %BO 3 0.5 0.5 3 !
36: CONST B2_BCC : MG% ND : MG ND% : VA : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): B2_BCC, type code %BO, sha256 `875ad4d46a8d6b2b…`

~~~~text
36: PHASE B2_BCC %BO 3 0.5 0.5 3 !
37: CONST B2_BCC : MG% ND : MG ND% : VA : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): B2_BCC, type code %BO, sha256 `60cd25bc6483030f…`

~~~~text
47: PHASE B2_BCC %BO 3 0.5 0.5 3 !
48: CONST B2_BCC : MG% ND : MG ND% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## MG2M_C15 (Mg–Nd)

- Id: `phase:mg-nd:c15-mg2m`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MG2M); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.6667, Nd 0.3333
- Stability: stable in 7 of 7 calculated diagram(s): 932.13–1028.31 K, x(Nd) 0.33333–0.33333
- Literature: 18 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:c15-mg2m)

Names (12): _corpus: _corpus:phase:mg-nd:c15-mg2m, corpus:phase:mg-nd:mg2m-c15  
_paper: _paper:10.1016/j.calphad.2010.07.010:Mg2Nd, paper:10.1016/j.jallcom.2010.07.056:Mg2Nd, paper:10.1016/s1003-6326(07)60051-x:Mg2Nd  
_tdb: _tdb:MgNd-05Gor-RK.tdb:MG2M_C15, tdb:MgNd-05Gor-ass.tdb:MG2M_C15, tdb:MgNd-06Guo.tdb:MG2M_C15, tdb:MgNd-07Men.tdb:MG2M_C15, tdb:MgNd-08Guo.tdb:MG2M_C15, tdb:MgNd-10Niu.tdb:MG2M_C15, tdb:MgNd-11Qi.tdb:MG2M_C15  


### TDB models of MG2M_C15 (7): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): MG2M_C15, type code %, sha256 `f7a30de1313053e0…`

~~~~text
64: PHASE MG2M_C15 % 2 2 1 !
65: CONST MG2M_C15 : MG : ND : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): MG2M_C15, type code %, sha256 `78190c1f09693a34…`

~~~~text
68: PHASE MG2M_C15 % 2 2 1 !
69: CONST MG2M_C15 : MG : ND : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): MG2M_C15, type code %, sha256 `40b7e9ee569d905d…`

~~~~text
54: PHASE MG2M_C15 % 2 2 1 !
55: CONST MG2M_C15 : MG : ND : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): MG2M_C15, type code %, sha256 `e6ae632117b97396…`

~~~~text
70: PHASE MG2M_C15 % 2 2 1 !
71: CONST MG2M_C15 : MG : ND : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): MG2M_C15, type code %, sha256 `cf2db92d7efdb61e…`

~~~~text
50: PHASE MG2M_C15 % 2 2 1 !
51: CONST MG2M_C15 : MG : ND : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): MG2M_C15, type code %, sha256 `875ad4d46a8d6b2b…`

~~~~text
51: PHASE MG2M_C15 % 2 2 1 !
52: CONST MG2M_C15 : MG : ND : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): MG2M_C15, type code %, sha256 `60cd25bc6483030f…`

~~~~text
72: PHASE MG2M_C15 % 2 2 1 !
73: CONST MG2M_C15 : MG : ND : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_
- [doi:10.1016/s1003-6326(07)60051-x](https://doi.org/10.1016/s1003-6326%2807%2960051-x) Fan-gui MENG, Hua-shan LIU, Li-bin LIU, Zhan-peng JIN, Thermodynamic optimization of Mg-Nd system, Transactions of Nonferrous Metals Society of China 17, 77-81 (2007).  
_reports values for this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## MG3M_D03 (Mg–Nd)

- Id: `phase:mg-nd:d03-mg3m`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MG3M); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 7 of 7 calculated diagram(s): 300–1059.11 K, x(Nd) 0.19478–0.25
- Literature: 20 values (20 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:d03-mg3m)

Names (12): _corpus: _corpus:phase:mg-nd:d03-mg3m, corpus:phase:mg-nd:mg3m-d03  
_paper: _paper:10.1016/j.calphad.2010.07.010:Mg3Nd, paper:10.1016/j.jallcom.2010.07.056:Mg3Nd, paper:10.1016/s1003-6326(07)60051-x:Mg3Nd  
_tdb: _tdb:MgNd-05Gor-RK.tdb:MG3M_D03, tdb:MgNd-05Gor-ass.tdb:MG3M_D03, tdb:MgNd-06Guo.tdb:MG3M_D03, tdb:MgNd-07Men.tdb:MG3M_D03, tdb:MgNd-08Guo.tdb:MG3M_D03, tdb:MgNd-10Niu.tdb:MG3M_D03, tdb:MgNd-11Qi.tdb:MG3M_D03  


### TDB models of MG3M_D03 (7): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): MG3M_D03, type code %, sha256 `f7a30de1313053e0…`

~~~~text
59: PHASE MG3M_D03 % 2 3 1 !
60: CONST MG3M_D03 : MG : ND : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): MG3M_D03, type code %, sha256 `78190c1f09693a34…`

~~~~text
63: PHASE MG3M_D03 % 2 3 1 !
64: CONST MG3M_D03 : MG : ND : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): MG3M_D03, type code %, sha256 `40b7e9ee569d905d…`

~~~~text
49: PHASE MG3M_D03 % 2 3 1 !
50: CONST MG3M_D03 : MG : MG ND% : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): MG3M_D03, type code %, sha256 `e6ae632117b97396…`

~~~~text
65: PHASE MG3M_D03 % 2 3 1 !
66: CONST MG3M_D03 : MG : ND : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): MG3M_D03, type code %, sha256 `cf2db92d7efdb61e…`

~~~~text
55: PHASE MG3M_D03 % 2 3 1 !
56: CONST MG3M_D03 : MG : MG ND% : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): MG3M_D03, type code %, sha256 `875ad4d46a8d6b2b…`

~~~~text
56: PHASE MG3M_D03 % 2 3 1 !
57: CONST MG3M_D03 : MG : MG ND% : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): MG3M_D03, type code %, sha256 `60cd25bc6483030f…`

~~~~text
67: PHASE MG3M_D03 % 2 3 1 !
68: CONST MG3M_D03 : MG : MG ND% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_
- [doi:10.1016/s1003-6326(07)60051-x](https://doi.org/10.1016/s1003-6326%2807%2960051-x) Fan-gui MENG, Hua-shan LIU, Li-bin LIU, Zhan-peng JIN, Thermodynamic optimization of Mg-Nd system, Transactions of Nonferrous Metals Society of China 17, 77-81 (2007).  
_reports values for this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## DHCP (Mg–Nd)

- Id: `phase:mg-nd:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–1284.25 K, x(Nd) 0.91156–1
- Literature: 6 values (6 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:dhcp-a3)

Names (12): _corpus: _corpus:phase:mg-nd:dhcp-a3, corpus:phase:mg-nd:dhcp  
_paper: _paper:10.1016/j.calphad.2010.07.010:dhcp, paper:10.1016/j.jallcom.2010.07.056:DHCP, paper:10.1016/s1003-6326(07)60051-x:dHCP  
_tdb: _tdb:MgNd-05Gor-RK.tdb:DHCP, tdb:MgNd-05Gor-ass.tdb:DHCP, tdb:MgNd-06Guo.tdb:DHCP, tdb:MgNd-07Men.tdb:DHCP, tdb:MgNd-08Guo.tdb:DHCP, tdb:MgNd-10Niu.tdb:DHCP, tdb:MgNd-11Qi.tdb:DHCP  


### TDB models of DHCP (7): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): DHCP, type code %A, sha256 `f7a30de1313053e0…`

~~~~text
49: PHASE DHCP %A 2 1 0.5 !
50: CONST DHCP : MG ND% : VA% : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): DHCP, type code %A, sha256 `78190c1f09693a34…`

~~~~text
53: PHASE DHCP %A 2 1 0.5 !
54: CONST DHCP : MG ND% : VA% : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): DHCP, type code %A, sha256 `40b7e9ee569d905d…`

~~~~text
39: PHASE DHCP %A 2 1 0.5 !
40: CONST DHCP : MG ND% : VA% : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): DHCP, type code %A, sha256 `e6ae632117b97396…`

~~~~text
55: PHASE DHCP %A 2 1 0.5 !
56: CONST DHCP : MG ND% : VA% : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): DHCP, type code %A, sha256 `cf2db92d7efdb61e…`

~~~~text
45: PHASE DHCP %A 2 1 0.5 !
46: CONST DHCP : MG ND% : VA% : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): DHCP, type code %A, sha256 `875ad4d46a8d6b2b…`

~~~~text
46: PHASE DHCP %A 2 1 0.5 !
47: CONST DHCP : MG ND% : VA% : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): DHCP, type code %A, sha256 `60cd25bc6483030f…`

~~~~text
57: PHASE DHCP %A 2 1 0.5 !
58: CONST DHCP : MG ND% : VA% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_
- [doi:10.1016/s1003-6326(07)60051-x](https://doi.org/10.1016/s1003-6326%2807%2960051-x) Fan-gui MENG, Hua-shan LIU, Li-bin LIU, Zhan-peng JIN, Thermodynamic optimization of Mg-Nd system, Transactions of Nonferrous Metals Society of China 17, 77-81 (2007).  
_reports values for this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## FCC_A1 (Mg–Nd)

- Id: `phase:mg-nd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:fcc-a1)

Names (8): _corpus: _corpus:phase:mg-nd:fcc-a1  
_tdb: _tdb:MgNd-05Gor-RK.tdb:FCC_A1, tdb:MgNd-05Gor-ass.tdb:FCC_A1, tdb:MgNd-06Guo.tdb:FCC_A1, tdb:MgNd-07Men.tdb:FCC_A1, tdb:MgNd-08Guo.tdb:FCC_A1, tdb:MgNd-10Niu.tdb:FCC_A1, tdb:MgNd-11Qi.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): FCC_A1, type code %A, sha256 `f7a30de1313053e0…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : MG ND : VA% : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): FCC_A1, type code %A, sha256 `78190c1f09693a34…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : MG ND : VA% : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): FCC_A1, type code %A, sha256 `40b7e9ee569d905d…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : MG ND : VA% : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): FCC_A1, type code %A, sha256 `e6ae632117b97396…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MG ND : VA% : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): FCC_A1, type code %A, sha256 `cf2db92d7efdb61e…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MG ND : VA% : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): FCC_A1, type code %A, sha256 `875ad4d46a8d6b2b…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MG ND : VA% : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): FCC_A1, type code %A, sha256 `60cd25bc6483030f…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MG ND : VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_

## HCP_A3 (Mg–Nd)

- Id: `phase:mg-nd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–932.95 K, x(Nd) 0–0.00949
- Literature: 6 values (6 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:hcp-a3)

Names (11): _corpus: _corpus:phase:mg-nd:hcp-a3  
_paper: _paper:10.1016/j.calphad.2010.07.010:hcp_A3, paper:10.1016/j.jallcom.2010.07.056:HCP_A3, paper:10.1016/s1003-6326(07)60051-x:HCP_A3  
_tdb: _tdb:MgNd-05Gor-RK.tdb:HCP_A3, tdb:MgNd-05Gor-ass.tdb:HCP_A3, tdb:MgNd-06Guo.tdb:HCP_A3, tdb:MgNd-07Men.tdb:HCP_A3, tdb:MgNd-08Guo.tdb:HCP_A3, tdb:MgNd-10Niu.tdb:HCP_A3, tdb:MgNd-11Qi.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): HCP_A3, type code %A, sha256 `f7a30de1313053e0…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : MG% ND : VA% : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): HCP_A3, type code %A, sha256 `78190c1f09693a34…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : MG% ND : VA% : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): HCP_A3, type code %A, sha256 `40b7e9ee569d905d…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : MG% ND : VA% : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): HCP_A3, type code %A, sha256 `e6ae632117b97396…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : MG% ND : VA% : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): HCP_A3, type code %A, sha256 `cf2db92d7efdb61e…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MG% ND : VA% : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): HCP_A3, type code %A, sha256 `875ad4d46a8d6b2b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : MG% ND : VA% : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): HCP_A3, type code %A, sha256 `60cd25bc6483030f…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : MG% ND : VA% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_
- [doi:10.1016/s1003-6326(07)60051-x](https://doi.org/10.1016/s1003-6326%2807%2960051-x) Fan-gui MENG, Hua-shan LIU, Li-bin LIU, Zhan-peng JIN, Thermodynamic optimization of Mg-Nd system, Transactions of Nonferrous Metals Society of China 17, 77-81 (2007).  
_reports values for this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## LIQUID (Mg–Nd)

- Id: `phase:mg-nd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 817.44–2500 K, x(Nd) 0–1
- Literature: 33 values (33 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:liquid)

Names (12): _corpus: _corpus:phase:mg-nd:liquid  
_paper: _paper:10.1016/j.calphad.2010.07.010:Liquid, paper:10.1016/j.jallcom.2004.09.040:liquid, paper:10.1016/j.jallcom.2010.07.056:Liquid, paper:10.1016/s1003-6326(07)60051-x:L  
_tdb: _tdb:MgNd-05Gor-RK.tdb:LIQUID, tdb:MgNd-05Gor-ass.tdb:LIQUID, tdb:MgNd-06Guo.tdb:LIQUID, tdb:MgNd-07Men.tdb:LIQUID, tdb:MgNd-08Guo.tdb:LIQUID, tdb:MgNd-10Niu.tdb:LIQUID, tdb:MgNd-11Qi.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): LIQUID, type code %, sha256 `f7a30de1313053e0…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : MG ND : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): LIQUID, type code %, sha256 `78190c1f09693a34…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : MG MG3ND ND : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): LIQUID, type code %, sha256 `40b7e9ee569d905d…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : MG ND : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): LIQUID, type code %, sha256 `e6ae632117b97396…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MG ND : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): LIQUID, type code %, sha256 `cf2db92d7efdb61e…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MG ND : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): LIQUID, type code %, sha256 `875ad4d46a8d6b2b…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MG ND : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): LIQUID, type code %, sha256 `60cd25bc6483030f…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : MG ND : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_
- [doi:10.1016/s1003-6326(07)60051-x](https://doi.org/10.1016/s1003-6326%2807%2960051-x) Fan-gui MENG, Hua-shan LIU, Li-bin LIU, Zhan-peng JIN, Thermodynamic optimization of Mg-Nd system, Transactions of Nonferrous Metals Society of China 17, 77-81 (2007).  
_reports values for this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## MG41M5 (Mg–Nd)

- Id: `phase:mg-nd:mg41m5`; status `assigned`
- Structure: Ce5Mg41 · tI92 · I4/m (87); type `st:ce5mg41-ti92`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MG41M5, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.8913, Nd 0.1087
- Stability: stable in 5 of 5 calculated diagram(s): 300–833.27 K, x(Nd) 0.1087–0.1087
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:mg41m5)

Names (8): _corpus: _corpus:phase:mg-nd:mg41m5  
_paper: _paper:10.1016/j.calphad.2010.07.010:Mg41Nd5, paper:10.1016/s1003-6326(07)60051-x:Mg41Nd5  
_tdb: _tdb:MgNd-05Gor-RK.tdb:MG41M5, tdb:MgNd-05Gor-ass.tdb:MG41M5, tdb:MgNd-07Men.tdb:MG41M5, tdb:MgNd-08Guo.tdb:MG41M5, tdb:MgNd-10Niu.tdb:MG41M5  


### TDB models of MG41M5 (5): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): MG41M5, type code %, sha256 `f7a30de1313053e0…`

~~~~text
54: PHASE MG41M5 % 2 41 5 !
55: CONST MG41M5 : MG : ND : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): MG41M5, type code %, sha256 `78190c1f09693a34…`

~~~~text
58: PHASE MG41M5 % 2 41 5 !
59: CONST MG41M5 : MG : ND : !
~~~~

[MgNd-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-07Men.tdb): MG41M5, type code %, sha256 `e6ae632117b97396…`

~~~~text
60: PHASE MG41M5 % 2 41 5 !
61: CONST MG41M5 : MG : ND : !
~~~~

[MgNd-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-08Guo.tdb): MG41M5, type code %, sha256 `cf2db92d7efdb61e…`

~~~~text
60: PHASE MG41M5 % 2 41 5 !
61: CONST MG41M5 : MG : ND : !
~~~~

[MgNd-10Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-10Niu.tdb): MG41M5, type code %, sha256 `875ad4d46a8d6b2b…`

~~~~text
61: PHASE MG41M5 % 2 41 5 !
62: CONST MG41M5 : MG : ND : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2010.07.010](https://doi.org/10.1016/j.calphad.2010.07.010) Chunju Niu, Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic description on the miscibility gap of the Mg-based solid solution in the Mg–Zn, Mg–Nd and Mg–Zn–Nd systems, Calphad 34, 428-433 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.1016/s1003-6326(07)60051-x](https://doi.org/10.1016/s1003-6326%2807%2960051-x) Fan-gui MENG, Hua-shan LIU, Li-bin LIU, Zhan-peng JIN, Thermodynamic optimization of Mg-Nd system, Transactions of Nonferrous Metals Society of China 17, 77-81 (2007).  
_reports values for this phase_

## MG41ND5 (Mg–Nd)

- Id: `phase:mg-nd:mg41nd5`; status `assigned`
- Structure: Ce5Mg41 · tI92 · I4/m (87); type `st:ce5mg41-ti92`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–832.46 K, x(Nd) 0.10135–0.1087
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:mg41nd5)

Names (4): _corpus: _corpus:phase:mg-nd:mg41nd5  
_paper: _paper:10.1016/j.jallcom.2010.07.056:Mg41Nd5  
_tdb: _tdb:MgNd-06Guo.tdb:MG41ND5, tdb:MgNd-11Qi.tdb:MG41ND5  


### TDB models of MG41ND5 (2): PHASE and CONSTITUENT statements as written

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): MG41ND5, type code %, sha256 `40b7e9ee569d905d…`

~~~~text
44: PHASE MG41ND5 % 2 41 5 !
45: CONST MG41ND5 : MG% ND : MG ND% : !
~~~~

[MgNd-11Qi.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-11Qi.tdb): MG41ND5, type code %, sha256 `60cd25bc6483030f…`

~~~~text
62: PHASE MG41ND5 % 2 41 5 !
63: CONST MG41ND5 : MG% ND : MG ND% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.07.056](https://doi.org/10.1016/j.jallcom.2010.07.056) H.Y. Qi, G.X. Huang, H. Bo, G.L. Xu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Mg–Nd–Zn ternary system, Journal of Alloys and Compounds 509, 3274-3281 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
_assessment that models this phase_
- [doi:10.1007/bf02647869](https://doi.org/10.1007/bf02647869) S. Delfino, A. Saccone, R. Ferro, Phase relationships in the neodymium-magnesium alloy system, Metall Trans A 21, 2109-2114 (1990).  
_cited as the source of values for this phase_

## MGND_B2 (Mg–Nd)

- Id: `phase:mg-nd:mgnd-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1078.25 K, x(Nd) 0.48371–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-nd:mgnd-b2)

Names (4): _corpus: _corpus:phase:mg-nd:mgnd-b2  
_tdb: _tdb:MgNd-05Gor-RK.tdb:MGND_B2, tdb:MgNd-05Gor-ass.tdb:MGND_B2, tdb:MgNd-06Guo.tdb:MGND_B2  


### TDB models of MGND_B2 (3): PHASE and CONSTITUENT statements as written

[MgNd-05Gor-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-RK.tdb): MGND_B2, type code %, sha256 `f7a30de1313053e0…`

~~~~text
69: PHASE MGND_B2 % 2 1 1 !
70: CONST MGND_B2 : MG : ND : !
~~~~

[MgNd-05Gor-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-05Gor-ass.tdb): MGND_B2, type code %, sha256 `78190c1f09693a34…`

~~~~text
73: PHASE MGND_B2 % 2 1 1 !
74: CONST MGND_B2 : MG : ND : !
~~~~

[MgNd-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNd-06Guo.tdb): MGND_B2, type code %, sha256 `40b7e9ee569d905d…`

~~~~text
59: PHASE MGND_B2 % 2 1 1 !
60: CONST MGND_B2 : MG : MG ND% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.09.040](https://doi.org/10.1016/j.jallcom.2004.09.040) S. Gorsse, C.R. Hutchinson, B. Chevalier, J.-F. Nie, A thermodynamic assessment of the Mg–Nd binary system using random solution and associate models for the liquid phase, Journal of Alloys and Compounds 392, 253-262 (2005).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0022](https://doi.org/10.3139/ijmr-2006-0022) C. Guo, Z. Du, Z. Metallkd., 97, 130-35(2006).  
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
