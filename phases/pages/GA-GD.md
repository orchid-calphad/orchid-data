# Ga–Gd phases

> Ga–Gd system: 10 phases (tier A 6, tier B 1, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-GD.html · Markdown: https://data.orchid-project.org/phases/pages/GA-GD.md

10 phases (tier A 6, tier B 1, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-GD) · [full JSON](https://data.orchid-project.org/phases/systems/GA-GD.json) · [Ga–Gd system page](https://data.orchid-project.org/systems/GA-GD.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-GD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Gd system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-gd-a11-orthorhombic); _phase:ga-gd:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–302.91 K, x(Gd) 0–0 | 10 | 3 |
| [BCC_A2](#phase-ga-gd-bcc-a2); _phase:ga-gd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1508.05–2499.87 K, x(Gd) 0.99999–1 | 8 | 3 |
| [FCC_A1](#phase-ga-gd-fcc-a1); _phase:ga-gd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GA2GD_C32](#phase-ga-gd-ga2gd-c32); _phase:ga-gd:ga2gd-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1681.61 K, x(Gd) 0.1949–0.33346 | 27 | 3 |
| [GA2GD3](#phase-ga-gd-ga2gd3); _phase:ga-gd:ga2gd3_ | Ga2Gd3 · tI80 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1380.29 K, x(Gd) 0.6–0.6 | 18 | 3 |
| [GA3GD5](#phase-ga-gd-ga3gd5); _phase:ga-gd:ga3gd5_ | Ba5Si3 · tP32 · P4/ncc (130) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1363.62 K, x(Gd) 0.625–0.625 | 18 | 3 |
| [GA6GD](#phase-ga-gd-ga6gd); _phase:ga-gd:ga6gd_ | Ga6Pu · tP14 · P4/nbm (125) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–678.55 K, x(Gd) 0.14286–0.14286 | 16 | 3 |
| [GAGD_B33](#phase-ga-gd-gagd-b33); _phase:ga-gd:gagd-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1466.07 K, x(Gd) 0.5–0.5 | 18 | 3 |
| [HCP_A3](#phase-ga-gd-hcp-a3); _phase:ga-gd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1583.06 K, x(Gd) 0.99998–1 | 13 | 3 |
| [LIQUID](#phase-ga-gd-liquid); _phase:ga-gd:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 302.91–2500 K, x(Gd) 0–1 | 60 | 3 |

## ORTHORHOMBIC_A11 (Ga–Gd)

- Id: `phase:ga-gd:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–302.91 K, x(Gd) 0–0
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:a11-orthorhombic)

Names (7): _corpus: _corpus:phase:ga-gd:a11-orthorhombic, corpus:phase:ga-gd:orthorhombic-a11  
_paper: _paper:10.1007/s00706-019-02420-8:orth., paper:10.1016/j.matpr.2019.07.598:(αGa)  
_tdb: _tdb:GaGd-19Liu.tdb:ORTHORHOMBIC_A11, tdb:GaGd-20Ait.tdb:ORTHORHOMBIC_A11, tdb:GaGd-23Tam.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): ORTHORHOMBIC_A11, type code %, sha256 `c20783412d926e19…`

~~~~text
45: PHASE ORTHORHOMBIC_A11 % 1 1 !
46: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): ORTHORHOMBIC_A11, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
49: PHASE ORTHORHOMBIC_A11 % 1 1 !
50: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): ORTHORHOMBIC_A11, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
41: PHASE ORTHORHOMBIC_A11 % 1 1 !
42: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90171-5](https://doi.org/10.1016/0022-5088%2881%2990171-5) Joshua Pelleg, L Zevin, The Gd-Ga system: Redetermination of the phase diagram on the gallium-rich side, Journal of the Less Common Metals 77, 197-203 (1981).  
_cited as the source of values for this phase_

## BCC_A2 (Ga–Gd)

- Id: `phase:ga-gd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1508.05–2499.87 K, x(Gd) 0.99999–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:bcc-a2)

Names (6): _corpus: _corpus:phase:ga-gd:bcc-a2  
_paper: _paper:10.1007/s00706-019-02420-8:bcc, paper:10.1016/j.matpr.2019.07.598:(βGd)  
_tdb: _tdb:GaGd-19Liu.tdb:BCC_A2, tdb:GaGd-20Ait.tdb:BCC_A2, tdb:GaGd-23Tam.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): BCC_A2, type code %B, sha256 `c20783412d926e19…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : GA GD% : VA : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): BCC_A2, type code %B, sha256 `c6bc03bf1e76ae90…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : GA GD% : VA : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): BCC_A2, type code %B, sha256 `87a4fc5f0d2a5c21…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GA GD% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_

## FCC_A1 (Ga–Gd)

- Id: `phase:ga-gd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:fcc-a1)

Names (4): _corpus: _corpus:phase:ga-gd:fcc-a1  
_tdb: _tdb:GaGd-19Liu.tdb:FCC_A1, tdb:GaGd-20Ait.tdb:FCC_A1, tdb:GaGd-23Tam.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): FCC_A1, type code %A, sha256 `c20783412d926e19…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : GA GD : VA : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): FCC_A1, type code %A, sha256 `c6bc03bf1e76ae90…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : GA GD : VA : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): FCC_A1, type code %A, sha256 `87a4fc5f0d2a5c21…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GA GD : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase_

## GA2GD_C32 (Ga–Gd)

- Id: `phase:ga-gd:ga2gd-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in GaGd-19Liu.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1681.61 K, x(Gd) 0.1949–0.33346
- Literature: 27 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:ga2gd-c32)

Names (6): _corpus: _corpus:phase:ga-gd:ga2gd-c32  
_paper: _paper:10.1007/s00706-019-02420-8:Ga2Gd, paper:10.1016/j.matpr.2019.07.598:Ga2Gd  
_tdb: _tdb:GaGd-19Liu.tdb:GA2GD_C32, tdb:GaGd-20Ait.tdb:GA2GD_C32, tdb:GaGd-23Tam.tdb:GA2GD_C32  


### TDB models of GA2GD_C32 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): GA2GD_C32, type code %, sha256 `c20783412d926e19…`

~~~~text
55: PHASE GA2GD_C32 % 2 2 1 !
56: CONST GA2GD_C32 : GA% GD : GA GD% : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): GA2GD_C32, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
59: PHASE GA2GD_C32 % 2 2 1 !
60: CONST GA2GD_C32 : GA : GA GD% : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): GA2GD_C32, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
51: PHASE GA2GD_C32 % 2 2 1 !
52: CONST GA2GD_C32 : GA : GA GD% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90277-0](https://doi.org/10.1016/0022-5088%2876%2990277-0) K.H.J. Buschow, W.W.v.d. Hoogenhof, Magnetic properties and phase relationships of gadolinium-gallium compounds, Journal of the Less Common Metals 45, 309-313 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90171-5](https://doi.org/10.1016/0022-5088%2881%2990171-5) Joshua Pelleg, L Zevin, The Gd-Ga system: Redetermination of the phase diagram on the gallium-rich side, Journal of the Less Common Metals 77, 197-203 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(01)00913-6](https://doi.org/10.1016/s0925-8388%2801%2900913-6) S.V Meschel, O.J Kleppa, Standard enthalpies of formation of some lanthanide gallides by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 319, 204-209 (2001).  
_cited as the source of values for this phase_

## GA2GD3 (Ga–Gd)

- Id: `phase:ga-gd:ga2gd3`; status `assigned`
- Structure: Ga2Gd3 · tI80 · I4/mcm (140); type `st:ga2gd3-ti80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.4000, Gd 0.6000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1380.29 K, x(Gd) 0.6–0.6
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:ga2gd3)

Names (6): _corpus: _corpus:phase:ga-gd:ga2gd3  
_paper: _paper:10.1007/s00706-019-02420-8:Ga2Gd3, paper:10.1016/j.matpr.2019.07.598:Ga2Gd3  
_tdb: _tdb:GaGd-19Liu.tdb:GA2GD3, tdb:GaGd-20Ait.tdb:GA2GD3, tdb:GaGd-23Tam.tdb:GA2GD3  


### TDB models of GA2GD3 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): GA2GD3, type code %, sha256 `c20783412d926e19…`

~~~~text
65: PHASE GA2GD3 % 2 2 3 !
66: CONST GA2GD3 : GA : GD : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): GA2GD3, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
69: PHASE GA2GD3 % 2 2 3 !
70: CONST GA2GD3 : GA : GD : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): GA2GD3, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
61: PHASE GA2GD3 % 2 2 3 !
62: CONST GA2GD3 : GA : GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90277-0](https://doi.org/10.1016/0022-5088%2876%2990277-0) K.H.J. Buschow, W.W.v.d. Hoogenhof, Magnetic properties and phase relationships of gadolinium-gallium compounds, Journal of the Less Common Metals 45, 309-313 (1976).  
_cited as the source of values for this phase_

## GA3GD5 (Ga–Gd)

- Id: `phase:ga-gd:ga3gd5`; status `assigned`
- Structure: Ba5Si3 · tP32 · P4/ncc (130); type `st:ba5si3-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.3750, Gd 0.6250
- Stability: stable in 3 of 3 calculated diagram(s): 300–1363.62 K, x(Gd) 0.625–0.625
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:ga3gd5)

Names (6): _corpus: _corpus:phase:ga-gd:ga3gd5  
_paper: _paper:10.1007/s00706-019-02420-8:Ga3Gd5, paper:10.1016/j.matpr.2019.07.598:Ga3Gd5  
_tdb: _tdb:GaGd-19Liu.tdb:GA3GD5, tdb:GaGd-20Ait.tdb:GA3GD5, tdb:GaGd-23Tam.tdb:GA3GD5  


### TDB models of GA3GD5 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): GA3GD5, type code %, sha256 `c20783412d926e19…`

~~~~text
70: PHASE GA3GD5 % 2 3 5 !
71: CONST GA3GD5 : GA : GD : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): GA3GD5, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
74: PHASE GA3GD5 % 2 3 5 !
75: CONST GA3GD5 : GA : GD : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): GA3GD5, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
66: PHASE GA3GD5 % 2 3 5 !
67: CONST GA3GD5 : GA : GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90277-0](https://doi.org/10.1016/0022-5088%2876%2990277-0) K.H.J. Buschow, W.W.v.d. Hoogenhof, Magnetic properties and phase relationships of gadolinium-gallium compounds, Journal of the Less Common Metals 45, 309-313 (1976).  
_cited as the source of values for this phase_

## GA6GD (Ga–Gd)

- Id: `phase:ga-gd:ga6gd`; status `assigned`
- Structure: Ga6Pu · tP14 · P4/nbm (125); type `st:ga6pu-tp14`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ga 0.8571, Gd 0.1429
- Stability: stable in 3 of 3 calculated diagram(s): 300–678.55 K, x(Gd) 0.14286–0.14286
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:ga6gd)

Names (8): _corpus: _corpus:phase:ga-gd:ga6gd  
_mp: _mp:mp-aaackwju  
_oqmd: _oqmd:oqmd-1484077  
_paper: _paper:10.1007/s00706-019-02420-8:Ga6Gd, paper:10.1016/j.matpr.2019.07.598:Ga6Gd  
_tdb: _tdb:GaGd-19Liu.tdb:GA6GD, tdb:GaGd-20Ait.tdb:GA6GD, tdb:GaGd-23Tam.tdb:GA6GD  


### TDB models of GA6GD (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): GA6GD, type code %, sha256 `c20783412d926e19…`

~~~~text
50: PHASE GA6GD % 2 6 1 !
51: CONST GA6GD : GA : GD : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): GA6GD, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
54: PHASE GA6GD % 2 6 1 !
55: CONST GA6GD : GA : GD : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): GA6GD, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
46: PHASE GA6GD % 2 6 1 !
47: CONST GA6GD : GA : GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90171-5](https://doi.org/10.1016/0022-5088%2881%2990171-5) Joshua Pelleg, L Zevin, The Gd-Ga system: Redetermination of the phase diagram on the gallium-rich side, Journal of the Less Common Metals 77, 197-203 (1981).  
_cited as the source of values for this phase_

## GAGD_B33 (Ga–Gd)

- Id: `phase:ga-gd:gagd-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabecv and oqmd-19090, space group 63
- Stoichiometry: Ga 0.5000, Gd 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1466.07 K, x(Gd) 0.5–0.5
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:gagd-b33)

Names (8): _corpus: _corpus:phase:ga-gd:gagd-b33  
_mp: _mp:mp-aaaabecv  
_oqmd: _oqmd:oqmd-19090  
_paper: _paper:10.1007/s00706-019-02420-8:GaGd, paper:10.1016/j.matpr.2019.07.598:GaGd  
_tdb: _tdb:GaGd-19Liu.tdb:GAGD_B33, tdb:GaGd-20Ait.tdb:GAGD_B33, tdb:GaGd-23Tam.tdb:GAGD_B33  


### TDB models of GAGD_B33 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): GAGD_B33, type code %, sha256 `c20783412d926e19…`

~~~~text
60: PHASE GAGD_B33 % 2 1 1 !
61: CONST GAGD_B33 : GA : GD : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): GAGD_B33, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
64: PHASE GAGD_B33 % 2 1 1 !
65: CONST GAGD_B33 : GA : GD : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): GAGD_B33, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
56: PHASE GAGD_B33 % 2 1 1 !
57: CONST GAGD_B33 : GA : GD : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90277-0](https://doi.org/10.1016/0022-5088%2876%2990277-0) K.H.J. Buschow, W.W.v.d. Hoogenhof, Magnetic properties and phase relationships of gadolinium-gallium compounds, Journal of the Less Common Metals 45, 309-313 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90171-5](https://doi.org/10.1016/0022-5088%2881%2990171-5) Joshua Pelleg, L Zevin, The Gd-Ga system: Redetermination of the phase diagram on the gallium-rich side, Journal of the Less Common Metals 77, 197-203 (1981).  
_cited as the source of values for this phase_

## HCP_A3 (Ga–Gd)

- Id: `phase:ga-gd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1583.06 K, x(Gd) 0.99998–1
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:hcp-a3)

Names (7): _corpus: _corpus:phase:ga-gd:hcp-a3  
_paper: _paper:10.1007/s00706-019-02420-8:hcp, paper:10.1007/s00706-019-02420-8:hcp(Gd), paper:10.1016/j.matpr.2019.07.598:(αGd)  
_tdb: _tdb:GaGd-19Liu.tdb:HCP_A3, tdb:GaGd-20Ait.tdb:HCP_A3, tdb:GaGd-23Tam.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): HCP_A3, type code %, sha256 `c20783412d926e19…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : GA GD% : VA : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): HCP_A3, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : GA GD% : VA : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): HCP_A3, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : GA GD% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90277-0](https://doi.org/10.1016/0022-5088%2876%2990277-0) K.H.J. Buschow, W.W.v.d. Hoogenhof, Magnetic properties and phase relationships of gadolinium-gallium compounds, Journal of the Less Common Metals 45, 309-313 (1976).  
_cited as the source of values for this phase_

## LIQUID (Ga–Gd)

- Id: `phase:ga-gd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 302.91–2500 K, x(Gd) 0–1
- Literature: 60 values (60 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-gd:liquid)

Names (6): _corpus: _corpus:phase:ga-gd:liquid  
_paper: _paper:10.1007/s00706-019-02420-8:liq., paper:10.1016/j.matpr.2019.07.598:Liq  
_tdb: _tdb:GaGd-19Liu.tdb:LIQUID, tdb:GaGd-20Ait.tdb:LIQUID, tdb:GaGd-23Tam.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[GaGd-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-19Liu.tdb): LIQUID, type code %, sha256 `c20783412d926e19…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : GA GD : !
~~~~

[GaGd-20Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-20Ait.tdb): LIQUID, type code %, sha256 `c6bc03bf1e76ae90…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : GA GA2GD GD : !
~~~~

[GaGd-23Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/GaGd-23Tam.tdb): LIQUID, type code %, sha256 `87a4fc5f0d2a5c21…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GA GD : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s00706-019-02420-8](https://doi.org/10.1007/s00706-019-02420-8) Jinming Liu, Fei Li, Jinping Liu, Xu Zhang, Tahir Ahmad, Tongxiang Liang, Thermodynamic description of the Ce–Ga and Ga–Gd systems, Monatsh Chem 150, 1225-1233 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598) M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596) Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02841585](https://doi.org/10.1007/bf02841585) A. Palenzona, S. Clrafici, The Ga-Gd (Gallium-Gadolinium) system, Bulletin of Alloy Phase Diagrams 11, 67-72 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90277-0](https://doi.org/10.1016/0022-5088%2876%2990277-0) K.H.J. Buschow, W.W.v.d. Hoogenhof, Magnetic properties and phase relationships of gadolinium-gallium compounds, Journal of the Less Common Metals 45, 309-313 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90171-5](https://doi.org/10.1016/0022-5088%2881%2990171-5) Joshua Pelleg, L Zevin, The Gd-Ga system: Redetermination of the phase diagram on the gallium-rich side, Journal of the Less Common Metals 77, 197-203 (1981).  
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
