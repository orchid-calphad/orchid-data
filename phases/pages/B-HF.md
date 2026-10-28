# B–Hf phases

> B–Hf system: 9 phases (tier A 4, tier C 3, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-HF.html · Markdown: https://data.orchid-project.org/phases/pages/B-HF.md

9 phases (tier A 4, tier C 3, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-HF) · [full JSON](https://data.orchid-project.org/phases/systems/B-HF.json) · [B–Hf system page](https://data.orchid-project.org/systems/B-HF.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-HF.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Hf system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-hf-b-beta-rhombo); _phase:b-hf:b-beta-rhombo_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–2490.94 K, x(B) 1–1 | 7 | 4 |
| [MB_B27](#phase-b-hf-b27-mb); _phase:b-hf:b27-mb_ | FeB · B27 · oP8 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–2380.45 K, x(B) 0.5–0.5 | 16 | 3 |
| [BCC_A2](#phase-b-hf-bcc-a2); _phase:b-hf:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 2016.03–3999.88 K, x(B) 0–0.04944 | 15 | 4 |
| [MB2_C32](#phase-b-hf-c32-mb2); _phase:b-hf:c32-mb2_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–3651.93 K, x(B) 0.66667–0.67697 | 27 | 3 |
| [FCC_A1](#phase-b-hf-fcc-a1); _phase:b-hf:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-b-hf-hcp-a3); _phase:b-hf:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2070 K, x(B) 0–0.02014 | 6 | 4 |
| [HFB_B27](#phase-b-hf-hfb-b27); _phase:b-hf:hfb-b27_ | FeB · B27 · oP8 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2373.37 K, x(B) 0.49967–0.5 | 6 | 1 |
| [HFB2_C32](#phase-b-hf-hfb2-c32); _phase:b-hf:hfb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3650.95 K, x(B) 0.66369–0.70713 | 6 | 1 |
| [LIQUID](#phase-b-hf-liquid); _phase:b-hf:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 2148.11–4000 K, x(B) 0–1 | 29 | 4 |

## BETA_RHOMBO_B (B–Hf)

- Id: `phase:b-hf:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — HfB-10Kau.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — HfB-11Cac.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — HfB-21Pan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — HfB-97Bit-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2490.94 K, x(B) 1–1
- Literature: 7 values (7 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:b-beta-rhombo)

Names (10): _corpus: _corpus:phase:b-hf:b-beta-rhombo, corpus:phase:b-hf:beta-rhombo-b  
_paper: _paper:10.1007/bf02646757:B, paper:10.1007/s11669-021-00928-3:(βB), paper:10.1016/j.calphad.2011.10.003:B, paper:sha256-85fd53a1a176b694:β-rhombo-B  
_tdb: _tdb:HfB-10Kau.tdb:BETA_RHOMBO_B, tdb:HfB-11Cac.tdb:BETA_RHOMBO_B, tdb:HfB-21Pan.tdb:BETA_RHOMBO_B, tdb:HfB-97Bit-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (4): PHASE and CONSTITUENT statements as written

[HfB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-10Kau.tdb): BETA_RHOMBO_B, type code %, sha256 `c2047bb2395431ba…`

~~~~text
52: PHASE BETA_RHOMBO_B % 2 93 12 !
53: CONST BETA_RHOMBO_B : B : B : !
~~~~

[HfB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-11Cac.tdb): BETA_RHOMBO_B, type code %, sha256 `5df78501ac600909…`

~~~~text
44: PHASE BETA_RHOMBO_B % 2 93 12 !
45: CONST BETA_RHOMBO_B : B : B : !
~~~~

[HfB-21Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-21Pan.tdb): BETA_RHOMBO_B, type code %, sha256 `af0cbca19fdb3a31…`

~~~~text
51: PHASE BETA_RHOMBO_B % 2 93 12 !
52: CONST BETA_RHOMBO_B : B : B : !
~~~~

[HfB-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-97Bit-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `be69f82e1247105b…`

~~~~text
46: PHASE BETA_RHOMBO_B % 2 93 12 !
47: CONST BETA_RHOMBO_B : B : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02646757](https://doi.org/10.1007/BF02646757) H. Bittermann, P. Rogl, J. Phase Equilib., 18, 24-47(1997).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00928-3](https://doi.org/10.1007/s11669-021-00928-3) Yafei Pan, Lei Huang, Jiuxing Zhang, Yong Du, Fenghua Luo, Shuyan Zhang, Thermodynamic Assessment of the Ternary B-Hf-Zr System with Refined B-Hf Description, J. Phase Equilib. Diffus. 42, 864-878 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) L. Kaufman, G. Cacciamani, M.L. Muolo, F. Valenza, A. Passerone, Calphad, 34, 2-5(2010).  
_assessment that models this phase_

## MB_B27 (B–Hf)

- Id: `phase:b-hf:b27-mb`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MB, no_structure_token, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5000, Hf 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2380.45 K, x(B) 0.5–0.5
- Literature: 16 values (16 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:b27-mb)

Names (8): _corpus: _corpus:phase:b-hf:b27-mb, corpus:phase:b-hf:mb-b27  
_paper: _paper:10.1007/bf02646757:HfB, paper:10.1016/j.calphad.2011.10.003:HfB, paper:sha256-85fd53a1a176b694:BHf  
_tdb: _tdb:HfB-10Kau.tdb:MB_B27, tdb:HfB-11Cac.tdb:MB_B27, tdb:HfB-97Bit-LB.tdb:MB_B27  


### TDB models of MB_B27 (3): PHASE and CONSTITUENT statements as written

[HfB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-10Kau.tdb): MB_B27, type code %, sha256 `c2047bb2395431ba…`

~~~~text
57: PHASE MB_B27 % 2 1 1 !
58: CONST MB_B27 : HF : B : !
~~~~

[HfB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-11Cac.tdb): MB_B27, type code %, sha256 `5df78501ac600909…`

~~~~text
49: PHASE MB_B27 % 2 1 1 !
50: CONST MB_B27 : HF : B : !
~~~~

[HfB-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-97Bit-LB.tdb): MB_B27, type code %, sha256 `be69f82e1247105b…`

~~~~text
51: PHASE MB_B27 % 2 1 1 !
52: CONST MB_B27 : HF : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646757](https://doi.org/10.1007/BF02646757) H. Bittermann, P. Rogl, J. Phase Equilib., 18, 24-47(1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) L. Kaufman, G. Cacciamani, M.L. Muolo, F. Valenza, A. Passerone, Calphad, 34, 2-5(2010).  
_assessment that models this phase_

## BCC_A2 (B–Hf)

- Id: `phase:b-hf:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 2016.03–3999.88 K, x(B) 0–0.04944
- Literature: 15 values (15 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:bcc-a2)

Names (9): _corpus: _corpus:phase:b-hf:bcc-a2  
_paper: _paper:10.1007/bf02646757:βHf, paper:10.1007/s11669-021-00928-3:(βHf), paper:10.1016/j.calphad.2011.10.003:bcc-Hf, paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:HfB-10Kau.tdb:BCC_A2, tdb:HfB-11Cac.tdb:BCC_A2, tdb:HfB-21Pan.tdb:BCC_A2, tdb:HfB-97Bit-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[HfB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-10Kau.tdb): BCC_A2, type code %B, sha256 `c2047bb2395431ba…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : B HF% : VA : !
~~~~

[HfB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-11Cac.tdb): BCC_A2, type code %B, sha256 `5df78501ac600909…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : HF% : B VA% : !
~~~~

[HfB-21Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-21Pan.tdb): BCC_A2, type code %B, sha256 `af0cbca19fdb3a31…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : HF% : B VA% : !
~~~~

[HfB-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-97Bit-LB.tdb): BCC_A2, type code %B, sha256 `be69f82e1247105b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : HF% : B VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646757](https://doi.org/10.1007/BF02646757) H. Bittermann, P. Rogl, J. Phase Equilib., 18, 24-47(1997).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00928-3](https://doi.org/10.1007/s11669-021-00928-3) Yafei Pan, Lei Huang, Jiuxing Zhang, Yong Du, Fenghua Luo, Shuyan Zhang, Thermodynamic Assessment of the Ternary B-Hf-Zr System with Refined B-Hf Description, J. Phase Equilib. Diffus. 42, 864-878 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) L. Kaufman, G. Cacciamani, M.L. Muolo, F. Valenza, A. Passerone, Calphad, 34, 2-5(2010).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## MB2_C32 (B–Hf)

- Id: `phase:b-hf:c32-mb2`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MB2); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 300–3651.93 K, x(B) 0.66667–0.67697
- Literature: 27 values (27 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:c32-mb2)

Names (8): _corpus: _corpus:phase:b-hf:c32-mb2, corpus:phase:b-hf:mb2-c32  
_paper: _paper:10.1007/bf02646757:HfB2, paper:10.1016/j.calphad.2011.10.003:HfB2, paper:sha256-85fd53a1a176b694:B2Hf  
_tdb: _tdb:HfB-10Kau.tdb:MB2_C32, tdb:HfB-11Cac.tdb:MB2_C32, tdb:HfB-97Bit-LB.tdb:MB2_C32  


### TDB models of MB2_C32 (3): PHASE and CONSTITUENT statements as written

[HfB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-10Kau.tdb): MB2_C32, type code %, sha256 `c2047bb2395431ba…`

~~~~text
62: PHASE MB2_C32 % 2 1 2 !
63: CONST MB2_C32 : HF : B : !
~~~~

[HfB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-11Cac.tdb): MB2_C32, type code %, sha256 `5df78501ac600909…`

~~~~text
54: PHASE MB2_C32 % 2 1 2 !
55: CONST MB2_C32 : HF% VA : B : !
~~~~

[HfB-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-97Bit-LB.tdb): MB2_C32, type code %, sha256 `be69f82e1247105b…`

~~~~text
56: PHASE MB2_C32 % 2 1 2 !
57: CONST MB2_C32 : HF : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02646757](https://doi.org/10.1007/BF02646757) H. Bittermann, P. Rogl, J. Phase Equilib., 18, 24-47(1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) L. Kaufman, G. Cacciamani, M.L. Muolo, F. Valenza, A. Passerone, Calphad, 34, 2-5(2010).  
_assessment that models this phase_
- [doi:10.1016/0021-9614(77)90048-9](https://doi.org/10.1016/0021-9614%2877%2990048-9) Edgar F Westrum, Goerge Feick, Heat capacities of HfB2.035 and HfC0.968 from 5 to 350 K, The Journal of Chemical Thermodynamics 9, 293-299 (1977).  
_cited as the source of values for this phase_

## FCC_A1 (B–Hf)

- Id: `phase:b-hf:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:fcc-a1)

Names (5): _corpus: _corpus:phase:b-hf:fcc-a1  
_tdb: _tdb:HfB-10Kau.tdb:FCC_A1, tdb:HfB-11Cac.tdb:FCC_A1, tdb:HfB-21Pan.tdb:FCC_A1, tdb:HfB-97Bit-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[HfB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-10Kau.tdb): FCC_A1, type code %A, sha256 `c2047bb2395431ba…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : HF B : VA : !
~~~~

[HfB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-11Cac.tdb): FCC_A1, type code %A, sha256 `5df78501ac600909…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : HF : B VA% : !
~~~~

[HfB-21Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-21Pan.tdb): FCC_A1, type code %A, sha256 `af0cbca19fdb3a31…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : HF : B VA% : !
~~~~

[HfB-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-97Bit-LB.tdb): FCC_A1, type code %A, sha256 `be69f82e1247105b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : HF : B VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02646757](https://doi.org/10.1007/BF02646757) H. Bittermann, P. Rogl, J. Phase Equilib., 18, 24-47(1997).  
_assessment that models this phase_
- [doi:10.1007/s11669-021-00928-3](https://doi.org/10.1007/s11669-021-00928-3) Yafei Pan, Lei Huang, Jiuxing Zhang, Yong Du, Fenghua Luo, Shuyan Zhang, Thermodynamic Assessment of the Ternary B-Hf-Zr System with Refined B-Hf Description, J. Phase Equilib. Diffus. 42, 864-878 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) L. Kaufman, G. Cacciamani, M.L. Muolo, F. Valenza, A. Passerone, Calphad, 34, 2-5(2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase_

## HCP_A3 (B–Hf)

- Id: `phase:b-hf:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2070 K, x(B) 0–0.02014
- Literature: 6 values (6 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:hcp-a3)

Names (9): _corpus: _corpus:phase:b-hf:hcp-a3  
_paper: _paper:10.1007/bf02646757:αHf, paper:10.1007/s11669-021-00928-3:(αHf), paper:10.1016/j.calphad.2011.10.003:hcp-Hf, paper:sha256-85fd53a1a176b694:hcp-A3  
_tdb: _tdb:HfB-10Kau.tdb:HCP_A3, tdb:HfB-11Cac.tdb:HCP_A3, tdb:HfB-21Pan.tdb:HCP_A3, tdb:HfB-97Bit-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[HfB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-10Kau.tdb): HCP_A3, type code %A, sha256 `c2047bb2395431ba…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : B HF% : VA : !
~~~~

[HfB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-11Cac.tdb): HCP_A3, type code %A, sha256 `5df78501ac600909…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : HF% : B VA% : !
~~~~

[HfB-21Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-21Pan.tdb): HCP_A3, type code %A, sha256 `af0cbca19fdb3a31…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : HF% : B VA% : !
~~~~

[HfB-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-97Bit-LB.tdb): HCP_A3, type code %A, sha256 `be69f82e1247105b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : HF% : B VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02646757](https://doi.org/10.1007/BF02646757) H. Bittermann, P. Rogl, J. Phase Equilib., 18, 24-47(1997).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00928-3](https://doi.org/10.1007/s11669-021-00928-3) Yafei Pan, Lei Huang, Jiuxing Zhang, Yong Du, Fenghua Luo, Shuyan Zhang, Thermodynamic Assessment of the Ternary B-Hf-Zr System with Refined B-Hf Description, J. Phase Equilib. Diffus. 42, 864-878 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) L. Kaufman, G. Cacciamani, M.L. Muolo, F. Valenza, A. Passerone, Calphad, 34, 2-5(2010).  
_assessment that models this phase_

## HFB_B27 (B–Hf)

- Id: `phase:b-hf:hfb-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–2373.37 K, x(B) 0.49967–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:hfb-b27)

Names (3): _corpus: _corpus:phase:b-hf:hfb-b27  
_paper: _paper:10.1007/s11669-021-00928-3:HfB  
_tdb: _tdb:HfB-21Pan.tdb:HFB_B27  


### TDB models of HFB_B27 (1): PHASE and CONSTITUENT statements as written

[HfB-21Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-21Pan.tdb): HFB_B27, type code %, sha256 `af0cbca19fdb3a31…`

~~~~text
56: PHASE HFB_B27 % 2 1 1 !
57: CONST HFB_B27 : HF : B% HF : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00928-3](https://doi.org/10.1007/s11669-021-00928-3) Yafei Pan, Lei Huang, Jiuxing Zhang, Yong Du, Fenghua Luo, Shuyan Zhang, Thermodynamic Assessment of the Ternary B-Hf-Zr System with Refined B-Hf Description, J. Phase Equilib. Diffus. 42, 864-878 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02646757](https://doi.org/10.1007/bf02646757) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the ternary system boron-hafnium-titanium (B-Hf-Ti), JPE 18, 24-47 (1997).  
_cited as the source of values for this phase_

## HFB2_C32 (B–Hf)

- Id: `phase:b-hf:hfb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfB-21Pan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–3650.95 K, x(B) 0.66369–0.70713
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:hfb2-c32)

Names (3): _corpus: _corpus:phase:b-hf:hfb2-c32  
_paper: _paper:10.1007/s11669-021-00928-3:HfB2  
_tdb: _tdb:HfB-21Pan.tdb:HFB2_C32  


### TDB models of HFB2_C32 (1): PHASE and CONSTITUENT statements as written

[HfB-21Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-21Pan.tdb): HFB2_C32, type code %, sha256 `af0cbca19fdb3a31…`

~~~~text
61: PHASE HFB2_C32 % 2 1 2 !
62: CONST HFB2_C32 : HF% B : HF B% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00928-3](https://doi.org/10.1007/s11669-021-00928-3) Yafei Pan, Lei Huang, Jiuxing Zhang, Yong Du, Fenghua Luo, Shuyan Zhang, Thermodynamic Assessment of the Ternary B-Hf-Zr System with Refined B-Hf Description, J. Phase Equilib. Diffus. 42, 864-878 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02646757](https://doi.org/10.1007/bf02646757) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the ternary system boron-hafnium-titanium (B-Hf-Ti), JPE 18, 24-47 (1997).  
_cited as the source of values for this phase_

## LIQUID (B–Hf)

- Id: `phase:b-hf:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 2148.11–4000 K, x(B) 0–1
- Literature: 29 values (29 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-hf:liquid)

Names (9): _corpus: _corpus:phase:b-hf:liquid  
_paper: _paper:10.1007/bf02646757:L, paper:10.1007/s11669-021-00928-3:L, paper:10.1016/j.calphad.2011.10.003:L, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:HfB-10Kau.tdb:LIQUID, tdb:HfB-11Cac.tdb:LIQUID, tdb:HfB-21Pan.tdb:LIQUID, tdb:HfB-97Bit-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[HfB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-10Kau.tdb): LIQUID, type code %, sha256 `c2047bb2395431ba…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : B HF : !
~~~~

[HfB-11Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-11Cac.tdb): LIQUID, type code %, sha256 `5df78501ac600909…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B HF : !
~~~~

[HfB-21Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-21Pan.tdb): LIQUID, type code %, sha256 `af0cbca19fdb3a31…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : B HF : !
~~~~

[HfB-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfB-97Bit-LB.tdb): LIQUID, type code %, sha256 `be69f82e1247105b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : B HF : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646757](https://doi.org/10.1007/BF02646757) H. Bittermann, P. Rogl, J. Phase Equilib., 18, 24-47(1997).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00928-3](https://doi.org/10.1007/s11669-021-00928-3) Yafei Pan, Lei Huang, Jiuxing Zhang, Yong Du, Fenghua Luo, Shuyan Zhang, Thermodynamic Assessment of the Ternary B-Hf-Zr System with Refined B-Hf Description, J. Phase Equilib. Diffus. 42, 864-878 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) L. Kaufman, G. Cacciamani, M.L. Muolo, F. Valenza, A. Passerone, Calphad, 34, 2-5(2010).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
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
