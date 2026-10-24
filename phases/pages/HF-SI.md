# Hf–Si phases

> Hf–Si system: 11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-SI.html · Markdown: https://data.orchid-project.org/phases/pages/HF-SI.md

11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-SI) · [full JSON](https://data.orchid-project.org/phases/systems/HF-SI.json) · [Hf–Si system page](https://data.orchid-project.org/systems/HF-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Si system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-hf-si-a4-diamond); _phase:hf-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.18 K, x(Si) 1–1 | 4 | 3 |
| [BCC_A2](#phase-hf-si-bcc-a2); _phase:hf-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 2013.35–2548.99 K, x(Si) 0–0.00211 | 8 | 3 |
| [FCC_A1](#phase-hf-si-fcc-a1); _phase:hf-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-hf-si-hcp-a3); _phase:hf-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2016.03 K, x(Si) 0–0.00067 | 2 | 3 |
| [HF2SI_C16](#phase-hf-si-hf2si-c16); _phase:hf-si:hf2si-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2365.31 K, x(Si) 0.33333–0.33333 | 15 | 3 |
| [HF3SI2_D5A](#phase-hf-si-hf3si2-d5a); _phase:hf-si:hf3si2-d5a_ | Si2U3 · D5_a · tP10 · P4/mbm (127) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2752.96 K, x(Si) 0.4–0.4 | 16 | 3 |
| [HF5SI3_D88](#phase-hf-si-hf5si3-d88); _phase:hf-si:hf5si3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1816.93–2740.16 K, x(Si) 0.375–0.375 | 13 | 3 |
| [HF5SI4](#phase-hf-si-hf5si4); _phase:hf-si:hf5si4_ | Si4Zr5 · tP36 · P4_12_12 (92) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–2595.12 K, x(Si) 0.44444–0.44444 | 8 | 3 |
| [HFSI_B27](#phase-hf-si-hfsi-b27); _phase:hf-si:hfsi-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2416.93 K, x(Si) 0.5–0.5 | 8 | 3 |
| [HFSI2_C49](#phase-hf-si-hfsi2-c49); _phase:hf-si:hfsi2-c49_ | ZrSi2 · C49 · oC12 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1818.85 K, x(Si) 0.66667–0.66667 | 8 | 3 |
| [LIQUID](#phase-hf-si-liquid); _phase:hf-si:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1597.92–4000 K, x(Si) 0–1 | 33 | 3 |

## DIAMOND_A4 (Hf–Si)

- Id: `phase:hf-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.18 K, x(Si) 1–1
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:a4-diamond)

Names (7): _corpus: _corpus:phase:hf-si:a4-diamond, corpus:phase:hf-si:diamond-a4  
_paper: _paper:10.1016/s0966-9795(03)00021-9:(Si), paper:10.1361/105497100770340408:diamond_A4 (Si)  
_tdb: _tdb:HfSi-00Zha-LB.tdb:DIAMOND_A4, tdb:HfSi-03Yan.tdb:DIAMOND_A4, tdb:HfSi-19Hon.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): DIAMOND_A4, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): DIAMOND_A4, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): DIAMOND_A4, type code %, sha256 `6640e20000baa136…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## BCC_A2 (Hf–Si)

- Id: `phase:hf-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2013.35–2548.99 K, x(Si) 0–0.00211
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:bcc-a2)

Names (7): _corpus: _corpus:phase:hf-si:bcc-a2  
_paper: _paper:10.1016/s0966-9795(03)00021-9:bcc(Hf), paper:10.1361/105497100770340408:Bcc (Hf), paper:10.1361/105497100770340408:bcc (Hf)  
_tdb: _tdb:HfSi-00Zha-LB.tdb:BCC_A2, tdb:HfSi-03Yan.tdb:BCC_A2, tdb:HfSi-19Hon.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): BCC_A2, type code %B, sha256 `29edae6cd520ee5e…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : HF SI : VA : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): BCC_A2, type code %B, sha256 `4c947308a5e5f90e…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : HF SI : VA : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): BCC_A2, type code %B, sha256 `6640e20000baa136…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : HF SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## FCC_A1 (Hf–Si)

- Id: `phase:hf-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:fcc-a1)

Names (4): _corpus: _corpus:phase:hf-si:fcc-a1  
_tdb: _tdb:HfSi-00Zha-LB.tdb:FCC_A1, tdb:HfSi-03Yan.tdb:FCC_A1, tdb:HfSi-19Hon.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): FCC_A1, type code %A, sha256 `29edae6cd520ee5e…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : HF SI : VA : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): FCC_A1, type code %A, sha256 `4c947308a5e5f90e…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : HF SI : VA : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): FCC_A1, type code %A, sha256 `6640e20000baa136…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : HF SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase_

## HCP_A3 (Hf–Si)

- Id: `phase:hf-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2016.03 K, x(Si) 0–0.00067
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:hcp-a3)

Names (5): _corpus: _corpus:phase:hf-si:hcp-a3  
_paper: _paper:10.1361/105497100770340408:hcp (Hf)  
_tdb: _tdb:HfSi-00Zha-LB.tdb:HCP_A3, tdb:HfSi-03Yan.tdb:HCP_A3, tdb:HfSi-19Hon.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): HCP_A3, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : HF SI : VA : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): HCP_A3, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : HF SI : VA : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): HCP_A3, type code %, sha256 `6640e20000baa136…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : HF SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase_

## HF2SI_C16 (Hf–Si)

- Id: `phase:hf-si:hf2si-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaosg and oqmd-7793, space group 140
- Stoichiometry: Hf 0.6667, Si 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–2365.31 K, x(Si) 0.33333–0.33333
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:hf2si-c16)

Names (8): _corpus: _corpus:phase:hf-si:hf2si-c16  
_mp: _mp:mp-aaaaaosg  
_oqmd: _oqmd:oqmd-7793  
_paper: _paper:10.1016/s0966-9795(03)00021-9:Hf2Si, paper:10.1361/105497100770340408:Hf2Si  
_tdb: _tdb:HfSi-00Zha-LB.tdb:HF2SI_C16, tdb:HfSi-03Yan.tdb:HF2SI_C16, tdb:HfSi-19Hon.tdb:HF2SI_C16  


### TDB models of HF2SI_C16 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): HF2SI_C16, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
46: PHASE HF2SI_C16 % 2 2 1 !
47: CONST HF2SI_C16 : HF : SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): HF2SI_C16, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
48: PHASE HF2SI_C16 % 2 2 1 !
49: CONST HF2SI_C16 : HF : SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): HF2SI_C16, type code %, sha256 `6640e20000baa136…`

~~~~text
53: PHASE HF2SI_C16 % 2 2 1 !
54: CONST HF2SI_C16 : HF : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## HF3SI2_D5A (Hf–Si)

- Id: `phase:hf-si:hf3si2-d5a`; status `assigned`
- Structure: Si2U3 · D5_a · tP10 · P4/mbm (127); type `st:d5-a-si2u3-tp10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadcz and oqmd-647083, space group 127
- Stoichiometry: Hf 0.6000, Si 0.4000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2752.96 K, x(Si) 0.4–0.4
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:hf3si2-d5a)

Names (8): _corpus: _corpus:phase:hf-si:hf3si2-d5a  
_mp: _mp:mp-aaaaadcz  
_oqmd: _oqmd:oqmd-647083  
_paper: _paper:10.1016/s0966-9795(03)00021-9:Hf3Si2, paper:10.1361/105497100770340408:Hf3Si2  
_tdb: _tdb:HfSi-00Zha-LB.tdb:HF3SI2_D5A, tdb:HfSi-03Yan.tdb:HF3SI2_D5A, tdb:HfSi-19Hon.tdb:HF3SI2_D5A  


### TDB models of HF3SI2_D5A (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): HF3SI2_D5A, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
56: PHASE HF3SI2_D5A % 2 3 2 !
57: CONST HF3SI2_D5A : HF : SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): HF3SI2_D5A, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
58: PHASE HF3SI2_D5A % 2 3 2 !
59: CONST HF3SI2_D5A : HF : SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): HF3SI2_D5A, type code %, sha256 `6640e20000baa136…`

~~~~text
63: PHASE HF3SI2_D5A % 2 3 2 !
64: CONST HF3SI2_D5A : HF : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## HF5SI3_D88 (Hf–Si)

- Id: `phase:hf-si:hf5si3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Hf 0.6250, Si 0.3750
- Stability: stable in 3 of 3 calculated diagram(s): 1816.93–2740.16 K, x(Si) 0.375–0.375
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:hf5si3-d88)

Names (6): _corpus: _corpus:phase:hf-si:hf5si3-d88  
_paper: _paper:10.1016/s0966-9795(03)00021-9:Hf5Si3, paper:10.1361/105497100770340408:Hf5Si3  
_tdb: _tdb:HfSi-00Zha-LB.tdb:HF5SI3_D88, tdb:HfSi-03Yan.tdb:HF5SI3_D88, tdb:HfSi-19Hon.tdb:HF5SI3_D88  


### TDB models of HF5SI3_D88 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): HF5SI3_D88, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
51: PHASE HF5SI3_D88 % 2 5 3 !
52: CONST HF5SI3_D88 : HF : SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): HF5SI3_D88, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
53: PHASE HF5SI3_D88 % 2 5 3 !
54: CONST HF5SI3_D88 : HF : SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): HF5SI3_D88, type code %, sha256 `6640e20000baa136…`

~~~~text
58: PHASE HF5SI3_D88 % 2 5 3 !
59: CONST HF5SI3_D88 : HF : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## HF5SI4 (Hf–Si)

- Id: `phase:hf-si:hf5si4`; status `assigned`
- Structure: Si4Zr5 · tP36 · P4_12_12 (92); type `st:si4zr5-tp36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hf 0.5556, Si 0.4444
- Stability: stable in 3 of 3 calculated diagram(s): 300–2595.12 K, x(Si) 0.44444–0.44444
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:hf5si4)

Names (6): _corpus: _corpus:phase:hf-si:hf5si4  
_paper: _paper:10.1016/s0966-9795(03)00021-9:Hf5Si4, paper:10.1361/105497100770340408:Hf5Si4  
_tdb: _tdb:HfSi-00Zha-LB.tdb:HF5SI4, tdb:HfSi-03Yan.tdb:HF5SI4, tdb:HfSi-19Hon.tdb:HF5SI4  


### TDB models of HF5SI4 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): HF5SI4, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
61: PHASE HF5SI4 % 2 5 4 !
62: CONST HF5SI4 : HF : SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): HF5SI4, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
63: PHASE HF5SI4 % 2 5 4 !
64: CONST HF5SI4 : HF : SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): HF5SI4, type code %, sha256 `6640e20000baa136…`

~~~~text
68: PHASE HF5SI4 % 2 5 4 !
69: CONST HF5SI4 : HF : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## HFSI_B27 (Hf–Si)

- Id: `phase:hf-si:hfsi-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaboc and oqmd-647082, space group 62
- Stoichiometry: Hf 0.5000, Si 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2416.93 K, x(Si) 0.5–0.5
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:hfsi-b27)

Names (8): _corpus: _corpus:phase:hf-si:hfsi-b27  
_mp: _mp:mp-aaaaaboc  
_oqmd: _oqmd:oqmd-647082  
_paper: _paper:10.1016/s0966-9795(03)00021-9:HfSi, paper:10.1361/105497100770340408:HfSi  
_tdb: _tdb:HfSi-00Zha-LB.tdb:HFSI_B27, tdb:HfSi-03Yan.tdb:HFSI_B27, tdb:HfSi-19Hon.tdb:HFSI_B27  


### TDB models of HFSI_B27 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): HFSI_B27, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
66: PHASE HFSI_B27 % 2 1 1 !
67: CONST HFSI_B27 : HF : SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): HFSI_B27, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
68: PHASE HFSI_B27 % 2 1 1 !
69: CONST HFSI_B27 : HF : SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): HFSI_B27, type code %, sha256 `6640e20000baa136…`

~~~~text
73: PHASE HFSI_B27 % 2 1 1 !
74: CONST HFSI_B27 : HF : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## HFSI2_C49 (Hf–Si)

- Id: `phase:hf-si:hfsi2-c49`; status `assigned`
- Structure: ZrSi2 · C49 · oC12 · Cmcm (63); type `st:c49-zrsi2-oc12`; tier A: standard phase name; confidence high
- Stoichiometry: Hf 0.3333, Si 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1818.85 K, x(Si) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:hfsi2-c49)

Names (6): _corpus: _corpus:phase:hf-si:hfsi2-c49  
_paper: _paper:10.1016/s0966-9795(03)00021-9:HfSi2, paper:10.1361/105497100770340408:HfSi2  
_tdb: _tdb:HfSi-00Zha-LB.tdb:HFSI2_C49, tdb:HfSi-03Yan.tdb:HFSI2_C49, tdb:HfSi-19Hon.tdb:HFSI2_C49  


### TDB models of HFSI2_C49 (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): HFSI2_C49, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
71: PHASE HFSI2_C49 % 2 1 2 !
72: CONST HFSI2_C49 : HF : SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): HFSI2_C49, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
73: PHASE HFSI2_C49 % 2 1 2 !
74: CONST HFSI2_C49 : HF : SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): HFSI2_C49, type code %, sha256 `6640e20000baa136…`

~~~~text
78: PHASE HFSI2_C49 % 2 1 2 !
79: CONST HFSI2_C49 : HF : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
_assessment that models this phase_

## LIQUID (Hf–Si)

- Id: `phase:hf-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1597.92–4000 K, x(Si) 0–1
- Literature: 33 values (33 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-si:liquid)

Names (6): _corpus: _corpus:phase:hf-si:liquid  
_paper: _paper:10.1016/s0966-9795(03)00021-9:L, paper:10.1361/105497100770340408:L  
_tdb: _tdb:HfSi-00Zha-LB.tdb:LIQUID, tdb:HfSi-03Yan.tdb:LIQUID, tdb:HfSi-19Hon.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[HfSi-00Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-00Zha-LB.tdb): LIQUID, type code %, sha256 `29edae6cd520ee5e…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : HF SI : !
~~~~

[HfSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-03Yan.tdb): LIQUID, type code %, sha256 `4c947308a5e5f90e…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : HF SI : !
~~~~

[HfSi-19Hon.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSi-19Hon.tdb): LIQUID, type code %, sha256 `6640e20000baa136…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : HF SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770340408](https://doi.org/10.1361/105497100770340408) J. -C. Zhao, B. P. Bewlay, M. R. Jackson, Q. Chen, Hf-Si binary phase diagram determination and thermodynamic modeling, JPE 21, 40-45 (2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2018.11.007](https://doi.org/10.1016/j.actamat.2018.11.007) P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Acta Mater., 164, 636-47(2019).  
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
