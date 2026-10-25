# Mg–Si phases

> Mg–Si system: 6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-SI.html · Markdown: https://data.orchid-project.org/phases/pages/MG-SI.md

6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-SI) · [full JSON](https://data.orchid-project.org/phases/systems/MG-SI.json) · [Mg–Si system page](https://data.orchid-project.org/systems/MG-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Si system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-mg-si-a4-diamond); _phase:mg-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2499.44 K, x(Si) 0.99974–1 | 21 | 7 |
| [BCC_A2](#phase-mg-si-bcc-a2); _phase:mg-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [FCC_A1](#phase-mg-si-fcc-a1); _phase:mg-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [HCP_A3](#phase-mg-si-hcp-a3); _phase:mg-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–930.75 K, x(Si) 0–6e-05 | 31 | 7 |
| [LIQUID](#phase-mg-si-liquid); _phase:mg-si:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 910.24–2500 K, x(Si) 0–1 | 105 | 7 |
| [MG2SI_C1](#phase-mg-si-mg2si-c1); _phase:mg-si:mg2si-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1360.67 K, x(Si) 0.33333–0.33333 | 124 | 7 |

## DIAMOND_A4 (Mg–Si)

- Id: `phase:mg-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–2499.44 K, x(Si) 0.99974–1
- Literature: 21 values (21 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-si:a4-diamond)

Names (12): _corpus: _corpus:phase:mg-si:a4-diamond, corpus:phase:mg-si:diamond-a4  
_paper: _paper:10.1016/j.calphad.2009.08.004:Si-diamond, paper:10.1016/j.calphad.2012.02.001:Si (dia), paper:10.1361/105497100770339914:(Si)  
_tdb: _tdb:MgSi-00Yan-LB.tdb:DIAMOND_A4, tdb:MgSi-04Kev.tdb:DIAMOND_A4, tdb:MgSi-09Yua.tdb:DIAMOND_A4, tdb:MgSi-12Sch.tdb:DIAMOND_A4, tdb:MgSi-16Lia.tdb:DIAMOND_A4, tdb:MgSi-86Lud.tdb:DIAMOND_A4, tdb:MgSi-97Feu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (7): PHASE and CONSTITUENT statements as written

[MgSi-00Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-00Yan-LB.tdb): DIAMOND_A4, type code %, sha256 `7347483183dd69b2…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

[MgSi-04Kev.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-04Kev.tdb): DIAMOND_A4, type code %, sha256 `8a16b2608533d041…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[MgSi-09Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-09Yua.tdb): DIAMOND_A4, type code %, sha256 `d51ae3480eef32b8…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SI : !
~~~~

[MgSi-12Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-12Sch.tdb): DIAMOND_A4, type code %, sha256 `fb5bcd7ddaaab551…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[MgSi-16Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-16Lia.tdb): DIAMOND_A4, type code %, sha256 `01f8dc8d22e0e37f…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : MG SI% : !
~~~~

[MgSi-86Lud.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-86Lud.tdb): DIAMOND_A4, type code %, sha256 `9be7ae691d0061a0…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SI : !
~~~~

[MgSi-97Feu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-97Feu.tdb): DIAMOND_A4, type code %, sha256 `ebffb15d1bb1ae71…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1361/105497100770339914](https://doi.org/10.1361/105497100770339914) Xin-Yan Yan, Y. A. Chang, F. Zhang, A thermodynamic analysis of the Mg-Si system, JPE 21, 379-384 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.001](https://doi.org/10.1016/j.calphad.2012.02.001) Michael Schick, Bengt Hallstedt, Albert Glensk, Blazej Grabowski, Tilmann Hickel, Milan Hampl et al., Combined ab initio, experimental, and CALPHAD approach for an improved thermodynamic evaluation of the Mg–Si system, Calphad 37, 77-86 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.004](https://doi.org/10.1016/j.calphad.2009.08.004) Xiaoming Yuan, Weihua Sun, Yong Du, Dongdong Zhao, Huaming Yang, Thermodynamic modeling of the Mg–Si system with the Kaptay equation for the excess Gibbs energy of the liquid phase, Calphad 33, 673-678 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Godecke, H.L. Lukas, F. Sommer, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2016.06.003](https://doi.org/10.1016/j.calphad.2016.06.003) S.-M. Liang, P. Wang, R. Schmid-Fetzer, Calphad, 54, 82-96(2016).  
_assessment that models this phase_
- [doi:10.1361/15477030418569](https://doi.org/10.1361/15477030418569) D. Kevorkov, R. Schmid-Fetzer, F. Zhang, Phase Equilibria and Thermodynamics of the Mg-Si-Li System and Remodeling of the Mg-Si System, Journal of Phase Equilibria &amp; Diffusion 25, 140-151 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-770503](https://doi.org/10.1515/ijmr-1986-770503) D. Luedecke, Z. Metallkd., 77, 278-83(1986).  
_assessment that models this phase_
- [doi:10.1002/zaac.19090610105](https://doi.org/10.1002/zaac.19090610105) R. Vogel, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXX. Über Magnesium‐Siliciumlegierungen, Z. Anorg. Chem. 61, 46-53 (1909).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19261510102](https://doi.org/10.1002/zaac.19261510102) Lothar Wöhler, O. Schliephake, Die Silicide des Calciums und Magnesiums, Z. Anorg. Allg. Chem. 151, 1-20 (1926).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(81)90016-x](https://doi.org/10.1016/0364-5916%2881%2990016-x) P. Dorner, H. Krieg, H.L. Lukas, R. Muller, and G. Petzow: CALPHAD, 1981, vol. 1, pp. 41-55.  
_cited as the source of values for this phase_

## BCC_A2 (Mg–Si)

- Id: `phase:mg-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-si:bcc-a2)

Names (8): _corpus: _corpus:phase:mg-si:bcc-a2  
_tdb: _tdb:MgSi-00Yan-LB.tdb:BCC_A2, tdb:MgSi-04Kev.tdb:BCC_A2, tdb:MgSi-09Yua.tdb:BCC_A2, tdb:MgSi-12Sch.tdb:BCC_A2, tdb:MgSi-16Lia.tdb:BCC_A2, tdb:MgSi-86Lud.tdb:BCC_A2, tdb:MgSi-97Feu.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[MgSi-00Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-00Yan-LB.tdb): BCC_A2, type code %B, sha256 `7347483183dd69b2…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MG SI : VA : !
~~~~

[MgSi-04Kev.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-04Kev.tdb): BCC_A2, type code %B, sha256 `8a16b2608533d041…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MG SI : VA : !
~~~~

[MgSi-09Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-09Yua.tdb): BCC_A2, type code %B, sha256 `d51ae3480eef32b8…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : MG SI : VA : !
~~~~

[MgSi-12Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-12Sch.tdb): BCC_A2, type code %B, sha256 `fb5bcd7ddaaab551…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MG SI : VA : !
~~~~

[MgSi-16Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-16Lia.tdb): BCC_A2, type code %B, sha256 `01f8dc8d22e0e37f…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : MG SI : VA : !
~~~~

[MgSi-86Lud.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-86Lud.tdb): BCC_A2, type code %B, sha256 `9be7ae691d0061a0…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : MG SI : VA : !
~~~~

[MgSi-97Feu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-97Feu.tdb): BCC_A2, type code %B, sha256 `ebffb15d1bb1ae71…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MG SI : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2009.08.004](https://doi.org/10.1016/j.calphad.2009.08.004) Xiaoming Yuan, Weihua Sun, Yong Du, Dongdong Zhao, Huaming Yang, Thermodynamic modeling of the Mg–Si system with the Kaptay equation for the excess Gibbs energy of the liquid phase, Calphad 33, 673-678 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.02.001](https://doi.org/10.1016/j.calphad.2012.02.001) Michael Schick, Bengt Hallstedt, Albert Glensk, Blazej Grabowski, Tilmann Hickel, Milan Hampl et al., Combined ab initio, experimental, and CALPHAD approach for an improved thermodynamic evaluation of the Mg–Si system, Calphad 37, 77-86 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.003](https://doi.org/10.1016/j.calphad.2016.06.003) S.-M. Liang, P. Wang, R. Schmid-Fetzer, Calphad, 54, 82-96(2016).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Godecke, H.L. Lukas, F. Sommer, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase_
- [doi:10.1361/105497100770339914](https://doi.org/10.1361/105497100770339914) Xin-Yan Yan, Y. A. Chang, F. Zhang, A thermodynamic analysis of the Mg-Si system, JPE 21, 379-384 (2000).  
_assessment that models this phase_
- [doi:10.1361/15477030418569](https://doi.org/10.1361/15477030418569) D. Kevorkov, R. Schmid-Fetzer, F. Zhang, Phase Equilibria and Thermodynamics of the Mg-Si-Li System and Remodeling of the Mg-Si System, Journal of Phase Equilibria &amp; Diffusion 25, 140-151 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-770503](https://doi.org/10.1515/ijmr-1986-770503) D. Luedecke, Z. Metallkd., 77, 278-83(1986).  
_assessment that models this phase_

## FCC_A1 (Mg–Si)

- Id: `phase:mg-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-si:fcc-a1)

Names (8): _corpus: _corpus:phase:mg-si:fcc-a1  
_tdb: _tdb:MgSi-00Yan-LB.tdb:FCC_A1, tdb:MgSi-04Kev.tdb:FCC_A1, tdb:MgSi-09Yua.tdb:FCC_A1, tdb:MgSi-12Sch.tdb:FCC_A1, tdb:MgSi-16Lia.tdb:FCC_A1, tdb:MgSi-86Lud.tdb:FCC_A1, tdb:MgSi-97Feu.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[MgSi-00Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-00Yan-LB.tdb): FCC_A1, type code %A, sha256 `7347483183dd69b2…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MG SI : VA : !
~~~~

[MgSi-04Kev.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-04Kev.tdb): FCC_A1, type code %A, sha256 `8a16b2608533d041…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MG SI : VA : !
~~~~

[MgSi-09Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-09Yua.tdb): FCC_A1, type code %A, sha256 `d51ae3480eef32b8…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MG SI : VA : !
~~~~

[MgSi-12Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-12Sch.tdb): FCC_A1, type code %A, sha256 `fb5bcd7ddaaab551…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MG SI : VA : !
~~~~

[MgSi-16Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-16Lia.tdb): FCC_A1, type code %A, sha256 `01f8dc8d22e0e37f…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : MG SI : VA : !
~~~~

[MgSi-86Lud.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-86Lud.tdb): FCC_A1, type code %A, sha256 `9be7ae691d0061a0…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : MG SI : VA : !
~~~~

[MgSi-97Feu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-97Feu.tdb): FCC_A1, type code %A, sha256 `ebffb15d1bb1ae71…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MG SI : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2009.08.004](https://doi.org/10.1016/j.calphad.2009.08.004) Xiaoming Yuan, Weihua Sun, Yong Du, Dongdong Zhao, Huaming Yang, Thermodynamic modeling of the Mg–Si system with the Kaptay equation for the excess Gibbs energy of the liquid phase, Calphad 33, 673-678 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.02.001](https://doi.org/10.1016/j.calphad.2012.02.001) Michael Schick, Bengt Hallstedt, Albert Glensk, Blazej Grabowski, Tilmann Hickel, Milan Hampl et al., Combined ab initio, experimental, and CALPHAD approach for an improved thermodynamic evaluation of the Mg–Si system, Calphad 37, 77-86 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.003](https://doi.org/10.1016/j.calphad.2016.06.003) S.-M. Liang, P. Wang, R. Schmid-Fetzer, Calphad, 54, 82-96(2016).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Godecke, H.L. Lukas, F. Sommer, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase_
- [doi:10.1361/105497100770339914](https://doi.org/10.1361/105497100770339914) Xin-Yan Yan, Y. A. Chang, F. Zhang, A thermodynamic analysis of the Mg-Si system, JPE 21, 379-384 (2000).  
_assessment that models this phase_
- [doi:10.1361/15477030418569](https://doi.org/10.1361/15477030418569) D. Kevorkov, R. Schmid-Fetzer, F. Zhang, Phase Equilibria and Thermodynamics of the Mg-Si-Li System and Remodeling of the Mg-Si System, Journal of Phase Equilibria &amp; Diffusion 25, 140-151 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-770503](https://doi.org/10.1515/ijmr-1986-770503) D. Luedecke, Z. Metallkd., 77, 278-83(1986).  
_assessment that models this phase_

## HCP_A3 (Mg–Si)

- Id: `phase:mg-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–930.75 K, x(Si) 0–6e-05
- Literature: 31 values (30 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-si:hcp-a3)

Names (11): _corpus: _corpus:phase:mg-si:hcp-a3  
_paper: _paper:10.1016/j.calphad.2009.08.004:(Mg)-hcp, paper:10.1016/j.calphad.2012.02.001:Mg (hcp), paper:10.1361/105497100770339914:(Mg)  
_tdb: _tdb:MgSi-00Yan-LB.tdb:HCP_A3, tdb:MgSi-04Kev.tdb:HCP_A3, tdb:MgSi-09Yua.tdb:HCP_A3, tdb:MgSi-12Sch.tdb:HCP_A3, tdb:MgSi-16Lia.tdb:HCP_A3, tdb:MgSi-86Lud.tdb:HCP_A3, tdb:MgSi-97Feu.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[MgSi-00Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-00Yan-LB.tdb): HCP_A3, type code %, sha256 `7347483183dd69b2…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : MG% SI : VA : !
~~~~

[MgSi-04Kev.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-04Kev.tdb): HCP_A3, type code %, sha256 `8a16b2608533d041…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : MG% SI : VA : !
~~~~

[MgSi-09Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-09Yua.tdb): HCP_A3, type code %, sha256 `d51ae3480eef32b8…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : MG% SI : VA : !
~~~~

[MgSi-12Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-12Sch.tdb): HCP_A3, type code %, sha256 `fb5bcd7ddaaab551…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : MG% SI : VA : !
~~~~

[MgSi-16Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-16Lia.tdb): HCP_A3, type code %, sha256 `01f8dc8d22e0e37f…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : MG% SI : VA : !
~~~~

[MgSi-86Lud.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-86Lud.tdb): HCP_A3, type code %, sha256 `9be7ae691d0061a0…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : MG% SI : VA : !
~~~~

[MgSi-97Feu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-97Feu.tdb): HCP_A3, type code %, sha256 `ebffb15d1bb1ae71…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : MG% SI : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1361/105497100770339914](https://doi.org/10.1361/105497100770339914) Xin-Yan Yan, Y. A. Chang, F. Zhang, A thermodynamic analysis of the Mg-Si system, JPE 21, 379-384 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.004](https://doi.org/10.1016/j.calphad.2009.08.004) Xiaoming Yuan, Weihua Sun, Yong Du, Dongdong Zhao, Huaming Yang, Thermodynamic modeling of the Mg–Si system with the Kaptay equation for the excess Gibbs energy of the liquid phase, Calphad 33, 673-678 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.001](https://doi.org/10.1016/j.calphad.2012.02.001) Michael Schick, Bengt Hallstedt, Albert Glensk, Blazej Grabowski, Tilmann Hickel, Milan Hampl et al., Combined ab initio, experimental, and CALPHAD approach for an improved thermodynamic evaluation of the Mg–Si system, Calphad 37, 77-86 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Godecke, H.L. Lukas, F. Sommer, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2016.06.003](https://doi.org/10.1016/j.calphad.2016.06.003) S.-M. Liang, P. Wang, R. Schmid-Fetzer, Calphad, 54, 82-96(2016).  
_assessment that models this phase_
- [doi:10.1361/15477030418569](https://doi.org/10.1361/15477030418569) D. Kevorkov, R. Schmid-Fetzer, F. Zhang, Phase Equilibria and Thermodynamics of the Mg-Si-Li System and Remodeling of the Mg-Si System, Journal of Phase Equilibria &amp; Diffusion 25, 140-151 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-770503](https://doi.org/10.1515/ijmr-1986-770503) D. Luedecke, Z. Metallkd., 77, 278-83(1986).  
_assessment that models this phase_
- [doi:10.1002/zaac.19090610105](https://doi.org/10.1002/zaac.19090610105) R. Vogel, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXX. Über Magnesium‐Siliciumlegierungen, Z. Anorg. Chem. 61, 46-53 (1909).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19261510102](https://doi.org/10.1002/zaac.19261510102) Lothar Wöhler, O. Schliephake, Die Silicide des Calciums und Magnesiums, Z. Anorg. Allg. Chem. 151, 1-20 (1926).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(81)90016-x](https://doi.org/10.1016/0364-5916%2881%2990016-x) P. Dorner, H. Krieg, H.L. Lukas, R. Muller, and G. Petzow: CALPHAD, 1981, vol. 1, pp. 41-55.  
_cited as the source of values for this phase_

## LIQUID (Mg–Si)

- Id: `phase:mg-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 910.24–2500 K, x(Si) 0–1
- Literature: 105 values (103 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-si:liquid)

Names (15): _corpus: _corpus:phase:mg-si:liquid  
_paper: _paper:10.1016/j.calphad.2009.08.004:L, paper:10.1016/j.calphad.2012.02.001:L, paper:10.1016/j.calphad.2012.02.001:Liquid, paper:10.1016/j.calphad.2012.02.001:liquid, paper:10.1016/s0925-8388(96)02655-2:liquid, paper:10.1361/105497100770339914:L, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:MgSi-00Yan-LB.tdb:LIQUID, tdb:MgSi-04Kev.tdb:LIQUID, tdb:MgSi-09Yua.tdb:LIQUID, tdb:MgSi-12Sch.tdb:LIQUID, tdb:MgSi-16Lia.tdb:LIQUID, tdb:MgSi-86Lud.tdb:LIQUID, tdb:MgSi-97Feu.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[MgSi-00Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-00Yan-LB.tdb): LIQUID, type code %, sha256 `7347483183dd69b2…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MG SI : !
~~~~

[MgSi-04Kev.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-04Kev.tdb): LIQUID, type code %, sha256 `8a16b2608533d041…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MG SI : !
~~~~

[MgSi-09Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-09Yua.tdb): LIQUID, type code %, sha256 `d51ae3480eef32b8…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : MG SI : !
~~~~

[MgSi-12Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-12Sch.tdb): LIQUID, type code %, sha256 `fb5bcd7ddaaab551…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MG SI : !
~~~~

[MgSi-16Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-16Lia.tdb): LIQUID, type code %, sha256 `01f8dc8d22e0e37f…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : MG SI : !
~~~~

[MgSi-86Lud.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-86Lud.tdb): LIQUID, type code %, sha256 `9be7ae691d0061a0…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : MG SI : !
~~~~

[MgSi-97Feu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-97Feu.tdb): LIQUID, type code %, sha256 `ebffb15d1bb1ae71…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MG SI : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1361/105497100770339914](https://doi.org/10.1361/105497100770339914) Xin-Yan Yan, Y. A. Chang, F. Zhang, A thermodynamic analysis of the Mg-Si system, JPE 21, 379-384 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Godecke, H.L. Lukas, F. Sommer, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.001](https://doi.org/10.1016/j.calphad.2012.02.001) Michael Schick, Bengt Hallstedt, Albert Glensk, Blazej Grabowski, Tilmann Hickel, Milan Hampl et al., Combined ab initio, experimental, and CALPHAD approach for an improved thermodynamic evaluation of the Mg–Si system, Calphad 37, 77-86 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.004](https://doi.org/10.1016/j.calphad.2009.08.004) Xiaoming Yuan, Weihua Sun, Yong Du, Dongdong Zhao, Huaming Yang, Thermodynamic modeling of the Mg–Si system with the Kaptay equation for the excess Gibbs energy of the liquid phase, Calphad 33, 673-678 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.06.003](https://doi.org/10.1016/j.calphad.2016.06.003) S.-M. Liang, P. Wang, R. Schmid-Fetzer, Calphad, 54, 82-96(2016).  
_assessment that models this phase_
- [doi:10.1361/15477030418569](https://doi.org/10.1361/15477030418569) D. Kevorkov, R. Schmid-Fetzer, F. Zhang, Phase Equilibria and Thermodynamics of the Mg-Si-Li System and Remodeling of the Mg-Si System, Journal of Phase Equilibria &amp; Diffusion 25, 140-151 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-770503](https://doi.org/10.1515/ijmr-1986-770503) D. Luedecke, Z. Metallkd., 77, 278-83(1986).  
_assessment that models this phase_
- [doi:10.1002/zaac.19090610105](https://doi.org/10.1002/zaac.19090610105) R. Vogel, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXX. Über Magnesium‐Siliciumlegierungen, Z. Anorg. Chem. 61, 46-53 (1909).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19261510102](https://doi.org/10.1002/zaac.19261510102) Lothar Wöhler, O. Schliephake, Die Silicide des Calciums und Magnesiums, Z. Anorg. Allg. Chem. 151, 1-20 (1926).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(81)90016-x](https://doi.org/10.1016/0364-5916%2881%2990016-x) P. Dorner, H. Krieg, H.L. Lukas, R. Muller, and G. Petzow: CALPHAD, 1981, vol. 1, pp. 41-55.  
_cited as the source of values for this phase_

## MG2SI_C1 (Mg–Si)

- Id: `phase:mg-si:mg2si-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacap and oqmd-17649, space group 225
- Stoichiometry: Mg 0.6667, Si 0.3333
- Stability: stable in 7 of 7 calculated diagram(s): 300–1360.67 K, x(Si) 0.33333–0.33333
- Literature: 124 values (122 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-si:mg2si-c1)

Names (13): _corpus: _corpus:phase:mg-si:mg2si-c1  
_mp: _mp:mp-aaaaacap  
_oqmd: _oqmd:oqmd-17649  
_paper: _paper:10.1016/j.calphad.2009.08.004:Mg2Si, paper:10.1016/j.calphad.2012.02.001:Mg2Si, paper:10.1361/105497100770339914:Mg2Si  
_tdb: _tdb:MgSi-00Yan-LB.tdb:MG2SI_C1, tdb:MgSi-04Kev.tdb:MG2SI_C1, tdb:MgSi-09Yua.tdb:MG2SI_C1, tdb:MgSi-12Sch.tdb:MG2SI_C1, tdb:MgSi-16Lia.tdb:MG2SI_C1, tdb:MgSi-86Lud.tdb:MG2SI_C1, tdb:MgSi-97Feu.tdb:MG2SI_C1  


### TDB models of MG2SI_C1 (7): PHASE and CONSTITUENT statements as written

[MgSi-00Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-00Yan-LB.tdb): MG2SI_C1, type code %, sha256 `7347483183dd69b2…`

~~~~text
51: PHASE MG2SI_C1 % 2 2 1 !
52: CONST MG2SI_C1 : MG : SI : !
~~~~

[MgSi-04Kev.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-04Kev.tdb): MG2SI_C1, type code %, sha256 `8a16b2608533d041…`

~~~~text
46: PHASE MG2SI_C1 % 2 2 1 !
47: CONST MG2SI_C1 : MG : SI : !
~~~~

[MgSi-09Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-09Yua.tdb): MG2SI_C1, type code %, sha256 `d51ae3480eef32b8…`

~~~~text
52: PHASE MG2SI_C1 % 2 2 1 !
53: CONST MG2SI_C1 : MG : SI : !
~~~~

[MgSi-12Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-12Sch.tdb): MG2SI_C1, type code %, sha256 `fb5bcd7ddaaab551…`

~~~~text
46: PHASE MG2SI_C1 % 2 2 1 !
47: CONST MG2SI_C1 : MG : SI : !
~~~~

[MgSi-16Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-16Lia.tdb): MG2SI_C1, type code %, sha256 `01f8dc8d22e0e37f…`

~~~~text
47: PHASE MG2SI_C1 % 2 2 1 !
48: CONST MG2SI_C1 : MG : SI : !
~~~~

[MgSi-86Lud.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-86Lud.tdb): MG2SI_C1, type code %, sha256 `9be7ae691d0061a0…`

~~~~text
54: PHASE MG2SI_C1 % 2 0.66666667 0.33333333 !
55: CONST MG2SI_C1 : MG : SI : !
~~~~

[MgSi-97Feu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSi-97Feu.tdb): MG2SI_C1, type code %, sha256 `ebffb15d1bb1ae71…`

~~~~text
51: PHASE MG2SI_C1 % 2 2 1 !
52: CONST MG2SI_C1 : MG : SI : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1016/j.calphad.2012.02.001](https://doi.org/10.1016/j.calphad.2012.02.001) Michael Schick, Bengt Hallstedt, Albert Glensk, Blazej Grabowski, Tilmann Hickel, Milan Hampl et al., Combined ab initio, experimental, and CALPHAD approach for an improved thermodynamic evaluation of the Mg–Si system, Calphad 37, 77-86 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339914](https://doi.org/10.1361/105497100770339914) Xin-Yan Yan, Y. A. Chang, F. Zhang, A thermodynamic analysis of the Mg-Si system, JPE 21, 379-384 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.004](https://doi.org/10.1016/j.calphad.2009.08.004) Xiaoming Yuan, Weihua Sun, Yong Du, Dongdong Zhao, Huaming Yang, Thermodynamic modeling of the Mg–Si system with the Kaptay equation for the excess Gibbs energy of the liquid phase, Calphad 33, 673-678 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Godecke, H.L. Lukas, F. Sommer, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2016.06.003](https://doi.org/10.1016/j.calphad.2016.06.003) S.-M. Liang, P. Wang, R. Schmid-Fetzer, Calphad, 54, 82-96(2016).  
_assessment that models this phase_
- [doi:10.1361/15477030418569](https://doi.org/10.1361/15477030418569) D. Kevorkov, R. Schmid-Fetzer, F. Zhang, Phase Equilibria and Thermodynamics of the Mg-Si-Li System and Remodeling of the Mg-Si System, Journal of Phase Equilibria &amp; Diffusion 25, 140-151 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-770503](https://doi.org/10.1515/ijmr-1986-770503) D. Luedecke, Z. Metallkd., 77, 278-83(1986).  
_assessment that models this phase_
- [doi:10.1002/zaac.19090610105](https://doi.org/10.1002/zaac.19090610105) R. Vogel, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXX. Über Magnesium‐Siliciumlegierungen, Z. Anorg. Chem. 61, 46-53 (1909).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19261510102](https://doi.org/10.1002/zaac.19261510102) Lothar Wöhler, O. Schliephake, Die Silicide des Calciums und Magnesiums, Z. Anorg. Allg. Chem. 151, 1-20 (1926).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(81)90016-x](https://doi.org/10.1016/0364-5916%2881%2990016-x) P. Dorner, H. Krieg, H.L. Lukas, R. Muller, and G. Petzow: CALPHAD, 1981, vol. 1, pp. 41-55.  
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
