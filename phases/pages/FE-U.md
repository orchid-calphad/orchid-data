# Fe–U phases

> Fe–U system: 8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-U.html · Markdown: https://data.orchid-project.org/phases/pages/FE-U.md

8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-U) · [full JSON](https://data.orchid-project.org/phases/systems/FE-U.json) · [Fe–U system page](https://data.orchid-project.org/systems/FE-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–U system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-fe-u-a20-orthorhombic); _phase:fe-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1047.02 K, x(U) 1–1 | 0 | 4 |
| [BCC_A2](#phase-fe-u-bcc-a2); _phase:fe-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2062.99 K, x(U) 0–1 | 6 | 4 |
| [FCC_A1](#phase-fe-u-fcc-a1); _phase:fe-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 529.81–1812.47 K, x(U) 0–0.00719 | 8 | 4 |
| [FE2U_C15](#phase-fe-u-fe2u-c15); _phase:fe-u:fe2u-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1560.9 K, x(U) 0.33333–0.33333 | 18 | 4 |
| [FEU6_D2C](#phase-fe-u-feu6-d2c); _phase:fe-u:feu6-d2c_ | MnU6 · D2_c · tI28 · I4/mcm (140) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–4000 K, x(U) 0.85714–0.85714 | 15 | 4 |
| [HCP_A3](#phase-fe-u-hcp-a3); _phase:fe-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-fe-u-liquid); _phase:fe-u:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 875.01–4000 K, x(U) 0–1 | 18 | 4 |
| [TETRAGONAL_U](#phase-fe-u-u-tetragonal); _phase:fe-u:u-tetragonal_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 938.79–1407.62 K, x(U) 0.99878–1 | 11 | 4 |

## ORTHORHOMBIC_A20 (Fe–U)

- Id: `phase:fe-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1047.02 K, x(U) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:a20-orthorhombic)

Names (5): _corpus: _corpus:phase:fe-u:a20-orthorhombic  
_tdb: _tdb:FeU-03Cha.tdb:ORTHORHOMBIC_A20, tdb:FeU-10Kur.tdb:ORTHORHOMBIC_A20, tdb:FeU-23Jia.tdb:ORTHORHOMBIC_A20, tdb:FeU-98Kur.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): ORTHORHOMBIC_A20, type code %, sha256 `2b3cb4ca0291ed3c…`

~~~~text
49: PHASE ORTHORHOMBIC_A20 % 1 1 !
50: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `bc15fcbedb33d3b6…`

~~~~text
48: PHASE ORTHORHOMBIC_A20 % 1 1 !
49: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): ORTHORHOMBIC_A20, type code %, sha256 `eb9a00d844e17ebb…`

~~~~text
42: PHASE ORTHORHOMBIC_A20 % 1 1 !
43: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `d4682ee275bf4ce8…`

~~~~text
49: PHASE ORTHORHOMBIC_A20 % 1 1 !
50: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase_

## BCC_A2 (Fe–U)

- Id: `phase:fe-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2062.99 K, x(U) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:bcc-a2)

Names (6): _corpus: _corpus:phase:fe-u:bcc-a2  
_paper: _paper:10.1361/105497103770330730:bcc - Fe  
_tdb: _tdb:FeU-03Cha.tdb:BCC_A2, tdb:FeU-10Kur.tdb:BCC_A2, tdb:FeU-23Jia.tdb:BCC_A2, tdb:FeU-98Kur.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): BCC_A2, type code %B, sha256 `2b3cb4ca0291ed3c…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE% U% : VA : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): BCC_A2, type code %B, sha256 `bc15fcbedb33d3b6…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE% U% : VA : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): BCC_A2, type code %B, sha256 `eb9a00d844e17ebb…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% U% : VA : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): BCC_A2, type code %B, sha256 `d4682ee275bf4ce8…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE% U% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1179/cmq.1966.5.4.355](https://doi.org/10.1179/cmq.1966.5.4.355) G.G. Michaud, A Study of the Iron-Rich Portion of the Fe-U Phase Diagram, Canadian Metallurgical Quarterly 5, 355-365 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(84)90046-1](https://doi.org/10.1016/0022-3115%2884%2990046-1) L.R. Chapman, C.E. Holcombe, Revision of the uranium-iron phase diagram, Journal of Nuclear Materials 126, 323-326 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(91)90531-b](https://doi.org/10.1016/0022-3115%2891%2990531-b) L. Leibowitz, R.A. Blomquist, Thermodynamics and phase equilibria of the iron—uranium system, Journal of Nuclear Materials 184, 47-52 (1991).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–U)

- Id: `phase:fe-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 529.81–1812.47 K, x(U) 0–0.00719
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:fcc-a1)

Names (6): _corpus: _corpus:phase:fe-u:fcc-a1  
_paper: _paper:10.1361/105497103770330730:fcc - Fe  
_tdb: _tdb:FeU-03Cha.tdb:FCC_A1, tdb:FeU-10Kur.tdb:FCC_A1, tdb:FeU-23Jia.tdb:FCC_A1, tdb:FeU-98Kur.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): FCC_A1, type code %A, sha256 `2b3cb4ca0291ed3c…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE : VA : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): FCC_A1, type code %A, sha256 `bc15fcbedb33d3b6…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE% U : VA : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): FCC_A1, type code %A, sha256 `eb9a00d844e17ebb…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% U : VA : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): FCC_A1, type code %A, sha256 `d4682ee275bf4ce8…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE% U : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(84)90046-1](https://doi.org/10.1016/0022-3115%2884%2990046-1) L.R. Chapman, C.E. Holcombe, Revision of the uranium-iron phase diagram, Journal of Nuclear Materials 126, 323-326 (1984).  
_cited as the source of values for this phase_
- [doi:10.1179/cmq.1966.5.4.355](https://doi.org/10.1179/cmq.1966.5.4.355) G.G. Michaud, A Study of the Iron-Rich Portion of the Fe-U Phase Diagram, Canadian Metallurgical Quarterly 5, 355-365 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(91)90531-b](https://doi.org/10.1016/0022-3115%2891%2990531-b) L. Leibowitz, R.A. Blomquist, Thermodynamics and phase equilibria of the iron—uranium system, Journal of Nuclear Materials 184, 47-52 (1991).  
_cited as the source of values for this phase_

## FE2U_C15 (Fe–U)

- Id: `phase:fe-u:fe2u-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.6667, U 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–1560.9 K, x(U) 0.33333–0.33333
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:fe2u-c15)

Names (6): _corpus: _corpus:phase:fe-u:fe2u-c15  
_paper: _paper:10.1361/105497103770330730:Fe2U  
_tdb: _tdb:FeU-03Cha.tdb:FE2U_C15, tdb:FeU-10Kur.tdb:FE2U_C15, tdb:FeU-23Jia.tdb:FE2U_C15, tdb:FeU-98Kur.tdb:FE2U_C15  


### TDB models of FE2U_C15 (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): FE2U_C15, type code %, sha256 `2b3cb4ca0291ed3c…`

~~~~text
59: PHASE FE2U_C15 % 2 2 1 !
60: CONST FE2U_C15 : FE : U : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): FE2U_C15, type code %, sha256 `bc15fcbedb33d3b6…`

~~~~text
58: PHASE FE2U_C15 % 2 2 1 !
59: CONST FE2U_C15 : FE : U : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): FE2U_C15, type code %, sha256 `eb9a00d844e17ebb…`

~~~~text
52: PHASE FE2U_C15 % 2 2 1 !
53: CONST FE2U_C15 : FE : U : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): FE2U_C15, type code %, sha256 `d4682ee275bf4ce8…`

~~~~text
59: PHASE FE2U_C15 % 2 2 1 !
60: CONST FE2U_C15 : FE : U : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(84)90046-1](https://doi.org/10.1016/0022-3115%2884%2990046-1) L.R. Chapman, C.E. Holcombe, Revision of the uranium-iron phase diagram, Journal of Nuclear Materials 126, 323-326 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(91)90531-b](https://doi.org/10.1016/0022-3115%2891%2990531-b) L. Leibowitz, R.A. Blomquist, Thermodynamics and phase equilibria of the iron—uranium system, Journal of Nuclear Materials 184, 47-52 (1991).  
_cited as the source of values for this phase_
- [doi:10.1179/cmq.1966.5.4.355](https://doi.org/10.1179/cmq.1966.5.4.355) G.G. Michaud, A Study of the Iron-Rich Portion of the Fe-U Phase Diagram, Canadian Metallurgical Quarterly 5, 355-365 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(95)00164-6](https://doi.org/10.1016/0022-3115%2895%2900164-6) M.P. Antony, R. Babu, C.K. Mathews, U.V. Varada Raju, Erratum to “enthalpies of formation of UNi5 UNI2 and UFe2 by solution calorimetry” \[Journal of Nuclear Materials 223 (1995) 213\], Journal of Nuclear Materials 228, 154 (1996).  
_cited as the source of values for this phase_

## FEU6_D2C (Fe–U)

- Id: `phase:fe-u:feu6-d2c`; status `assigned`
- Structure: MnU6 · D2_c · tI28 · I4/mcm (140); type `st:d2-c-mnu6-ti28`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.1429, U 0.8571
- Stability: stable in 4 of 4 calculated diagram(s): 300–4000 K, x(U) 0.85714–0.85714
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:feu6-d2c)

Names (6): _corpus: _corpus:phase:fe-u:feu6-d2c  
_paper: _paper:10.1361/105497103770330730:FeU6  
_tdb: _tdb:FeU-03Cha.tdb:FEU6_D2C, tdb:FeU-10Kur.tdb:FEU6_D2C, tdb:FeU-23Jia.tdb:FEU6_D2C, tdb:FeU-98Kur.tdb:FEU6_D2C  


### TDB models of FEU6_D2C (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): FEU6_D2C, type code %, sha256 `2b3cb4ca0291ed3c…`

~~~~text
64: PHASE FEU6_D2C % 2 1 6 !
65: CONST FEU6_D2C : FE : U : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): FEU6_D2C, type code %, sha256 `bc15fcbedb33d3b6…`

~~~~text
63: PHASE FEU6_D2C % 2 1 6 !
64: CONST FEU6_D2C : FE : U : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): FEU6_D2C, type code %, sha256 `eb9a00d844e17ebb…`

~~~~text
57: PHASE FEU6_D2C % 2 1 6 !
58: CONST FEU6_D2C : FE : U : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): FEU6_D2C, type code %, sha256 `d4682ee275bf4ce8…`

~~~~text
64: PHASE FEU6_D2C % 2 1 6 !
65: CONST FEU6_D2C : FE : U : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(84)90046-1](https://doi.org/10.1016/0022-3115%2884%2990046-1) L.R. Chapman, C.E. Holcombe, Revision of the uranium-iron phase diagram, Journal of Nuclear Materials 126, 323-326 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(91)90531-b](https://doi.org/10.1016/0022-3115%2891%2990531-b) L. Leibowitz, R.A. Blomquist, Thermodynamics and phase equilibria of the iron—uranium system, Journal of Nuclear Materials 184, 47-52 (1991).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–U)

- Id: `phase:fe-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:hcp-a3)

Names (5): _corpus: _corpus:phase:fe-u:hcp-a3  
_tdb: _tdb:FeU-03Cha.tdb:HCP_A3, tdb:FeU-10Kur.tdb:HCP_A3, tdb:FeU-23Jia.tdb:HCP_A3, tdb:FeU-98Kur.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): HCP_A3, type code %A, sha256 `2b3cb4ca0291ed3c…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : FE : VA : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): HCP_A3, type code %A, sha256 `bc15fcbedb33d3b6…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : FE U : VA : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): HCP_A3, type code %A, sha256 `eb9a00d844e17ebb…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE U : VA : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): HCP_A3, type code %A, sha256 `d4682ee275bf4ce8…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : FE U : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase_

## LIQUID (Fe–U)

- Id: `phase:fe-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 875.01–4000 K, x(U) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:liquid)

Names (7): _corpus: _corpus:phase:fe-u:liquid  
_paper: _paper:10.1361/105497103770330730:L, paper:10.1361/105497103770330730:liquid  
_tdb: _tdb:FeU-03Cha.tdb:LIQUID, tdb:FeU-10Kur.tdb:LIQUID, tdb:FeU-23Jia.tdb:LIQUID, tdb:FeU-98Kur.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): LIQUID, type code %, sha256 `2b3cb4ca0291ed3c…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : FE U : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): LIQUID, type code %, sha256 `bc15fcbedb33d3b6…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE U : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): LIQUID, type code %, sha256 `eb9a00d844e17ebb…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE U : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): LIQUID, type code %, sha256 `d4682ee275bf4ce8…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : FE U : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(84)90046-1](https://doi.org/10.1016/0022-3115%2884%2990046-1) L.R. Chapman, C.E. Holcombe, Revision of the uranium-iron phase diagram, Journal of Nuclear Materials 126, 323-326 (1984).  
_cited as the source of values for this phase_
- [doi:10.1179/cmq.1966.5.4.355](https://doi.org/10.1179/cmq.1966.5.4.355) G.G. Michaud, A Study of the Iron-Rich Portion of the Fe-U Phase Diagram, Canadian Metallurgical Quarterly 5, 355-365 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(91)90531-b](https://doi.org/10.1016/0022-3115%2891%2990531-b) L. Leibowitz, R.A. Blomquist, Thermodynamics and phase equilibria of the iron—uranium system, Journal of Nuclear Materials 184, 47-52 (1991).  
_cited as the source of values for this phase_

## TETRAGONAL_U (Fe–U)

- Id: `phase:fe-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — FeU-03Cha.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — FeU-10Kur.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — FeU-23Jia.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — FeU-98Kur.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 4 of 4 calculated diagram(s): 938.79–1407.62 K, x(U) 0.99878–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-u:u-tetragonal)

Names (10): _corpus: _corpus:phase:fe-u:u-tetragonal, corpus:phase:fe-u:tetragonal-u  
_paper: _paper:10.1361/105497103770330730:bcc - U, paper:10.1361/105497103770330730:bcc-U, paper:10.1361/105497103770330730:tetragonal - U, paper:10.1361/105497103770330730:tetragonal-U  
_tdb: _tdb:FeU-03Cha.tdb:TETRAGONAL_U, tdb:FeU-10Kur.tdb:TETRAGONAL_U, tdb:FeU-23Jia.tdb:TETRAGONAL_U, tdb:FeU-98Kur.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (4): PHASE and CONSTITUENT statements as written

[FeU-03Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-03Cha.tdb): TETRAGONAL_U, type code %, sha256 `2b3cb4ca0291ed3c…`

~~~~text
54: PHASE TETRAGONAL_U % 1 1 !
55: CONST TETRAGONAL_U : FE U% : !
~~~~

[FeU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-10Kur.tdb): TETRAGONAL_U, type code %, sha256 `bc15fcbedb33d3b6…`

~~~~text
53: PHASE TETRAGONAL_U % 1 1 !
54: CONST TETRAGONAL_U : U : !
~~~~

[FeU-23Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-23Jia.tdb): TETRAGONAL_U, type code %, sha256 `eb9a00d844e17ebb…`

~~~~text
47: PHASE TETRAGONAL_U % 1 1 !
48: CONST TETRAGONAL_U : U : !
~~~~

[FeU-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FeU-98Kur.tdb): TETRAGONAL_U, type code %, sha256 `d4682ee275bf4ce8…`

~~~~text
54: PHASE TETRAGONAL_U % 1 1 !
55: CONST TETRAGONAL_U : U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497103770330730](https://doi.org/10.1361/105497103770330730) S. Chatain, C. Guéneau, D. Labroche, O. Dugne, J. Rogez, Thermodynamic assessment of the Fe-U binary system, JPE 24, 122-131 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2022.154180](https://doi.org/10.1016/j.jnucmat.2022.154180) Yueshan Jiang, Yanlin He, Weisen Zheng, Jianlei Zhang, Dekui Zhang, Xiaogang Lu, Thermodynamic analysis for molten corium stratification with U-Zr-O-Fe database, Journal of Nuclear Materials 574, 154180 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(84)90046-1](https://doi.org/10.1016/0022-3115%2884%2990046-1) L.R. Chapman, C.E. Holcombe, Revision of the uranium-iron phase diagram, Journal of Nuclear Materials 126, 323-326 (1984).  
_cited as the source of values for this phase_

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
