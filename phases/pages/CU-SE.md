# Cu–Se phases

> Cu–Se system: 12 phases (tier A 6, tier B 1, liquid 1, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-SE.html · Markdown: https://data.orchid-project.org/phases/pages/CU-SE.md

12 phases (tier A 6, tier B 1, liquid 1, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-SE) · [full JSON](https://data.orchid-project.org/phases/systems/CU-SE.json) · [Cu–Se system page](https://data.orchid-project.org/systems/CU-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Se system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-cu-se-a8-hexagonal); _phase:cu-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–494 K, x(Se) 1–1 | 0 | 2 |
| [BCC_A2](#phase-cu-se-bcc-a2); _phase:cu-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [CU2SE_ALPHA](#phase-cu-se-cu2se-alpha); _phase:cu-se:cu2se-alpha_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–396 K, x(Se) 0.33333–0.33333 | 0 | 2 |
| [CU2SE_BETA](#phase-cu-se-cu2se-beta); _phase:cu-se:cu2se-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 377.74–1433.74 K, x(Se) 0.33333–0.36305 | 0 | 2 |
| [CU3SE2](#phase-cu-se-cu3se2); _phase:cu-se:cu3se2_ | Cu3Se2 · tP10 · P-42_1m (113) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–390.33 K, x(Se) 0.4–0.4 | 2 | 2 |
| [CUSE_ALPHA](#phase-cu-se-cuse-alpha); _phase:cu-se:cuse-alpha_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–328.45 K, x(Se) 0.5–0.5 | 0 | 2 |
| [CUSE_B18](#phase-cu-se-cuse-b18); _phase:cu-se:cuse-b18_ | CuS · B18 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 409.15–652.72 K, x(Se) 0.5–0.5 | 0 | 2 |
| [CUSE_BETA](#phase-cu-se-cuse-beta); _phase:cu-se:cuse-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 326.81–410.42 K, x(Se) 0.5–0.5 | 0 | 2 |
| [CUSE2_C18](#phase-cu-se-cuse2-c18); _phase:cu-se:cuse2-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–610.5 K, x(Se) 0.66667–0.66667 | 0 | 2 |
| [FCC_A1](#phase-cu-se-fcc-a1); _phase:cu-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1357.77 K, x(Se) 0–0 | 0 | 2 |
| [HCP_A3](#phase-cu-se-hcp-a3); _phase:cu-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cu-se-liquid); _phase:cu-se:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 494–2500 K, x(Se) 0–1 | 0 | 2 |

## HEXAGONAL_A8 (Cu–Se)

- Id: `phase:cu-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:a8-hexagonal)

Names (3): _corpus: _corpus:phase:cu-se:a8-hexagonal  
_tdb: _tdb:CuSe-08Du.tdb:HEXAGONAL_A8, tdb:CuSe-23Liu.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): HEXAGONAL_A8, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
48: PHASE HEXAGONAL_A8 % 1 1 !
49: CONST HEXAGONAL_A8 : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): HEXAGONAL_A8, type code %, sha256 `c43a98dbd0136561…`

~~~~text
52: PHASE HEXAGONAL_A8 % 1 1 !
53: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## BCC_A2 (Cu–Se)

- Id: `phase:cu-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-se:bcc-a2  
_tdb: _tdb:CuSe-08Du.tdb:BCC_A2, tdb:CuSe-23Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): BCC_A2, type code %B, sha256 `47155ae6b8c026d3…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CU : VA : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): BCC_A2, type code %B, sha256 `c43a98dbd0136561…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## CU2SE_ALPHA (Cu–Se)

- Id: `phase:cu-se:cu2se-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): Cu2Se-alpha · mC144 · C2/c (15) — Hallstedt 2025 mmc2 row for CU2SE_ALPHA: Cu2Se-alpha
- Candidate (tdb_comment): Cu2Se-alpha · mC144 · C2/c, 15 — CuSe-08Du.tdb: 'Prototype Cu2Se-alpha (mC144, C2/c, 15)'
- Candidate (tdb_comment): Cu2Se-alpha · mC144 · C2/c — CuSe-23Liu.tdb: 'Prototype Cu2Se-alpha (mC144, C2/c)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–396 K, x(Se) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:cu2se-alpha)

Names (3): _corpus: _corpus:phase:cu-se:cu2se-alpha  
_tdb: _tdb:CuSe-08Du.tdb:CU2SE_ALPHA, tdb:CuSe-23Liu.tdb:CU2SE_ALPHA  


### TDB models of CU2SE_ALPHA (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): CU2SE_ALPHA, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
53: PHASE CU2SE_ALPHA % 2 2 1 !
54: CONST CU2SE_ALPHA : CU% SE : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): CU2SE_ALPHA, type code %, sha256 `c43a98dbd0136561…`

~~~~text
57: PHASE CU2SE_ALPHA % 2 2 1 !
58: CONST CU2SE_ALPHA : CU% SE : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## CU2SE_BETA (Cu–Se)

- Id: `phase:cu-se:cu2se-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): Cu2Se-beta · cF44 · Fm-3m (225) — Hallstedt 2025 mmc2 row for CU2SE_BETA: Cu2Se-beta (berzelianite)
- Candidate (tdb_comment): Cu2Se-beta · cF44 · Fm-3m — CuSe-08Du.tdb: 'Prototype Cu2Se-beta (cF44, Fm-3m), berzelianite'
- Candidate (tdb_comment): Cu2Se-beta · cF44 · Fm-3m — CuSe-23Liu.tdb: 'Prototype Cu2Se-beta (cF44, Fm-3m), berzelianite'
- Stability: stable in 2 of 2 calculated diagram(s): 377.74–1433.74 K, x(Se) 0.33333–0.36305
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:cu2se-beta)

Names (3): _corpus: _corpus:phase:cu-se:cu2se-beta  
_tdb: _tdb:CuSe-08Du.tdb:CU2SE_BETA, tdb:CuSe-23Liu.tdb:CU2SE_BETA  


### TDB models of CU2SE_BETA (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): CU2SE_BETA, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
58: PHASE CU2SE_BETA % 2 2 1 !
59: CONST CU2SE_BETA : CU% SE : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): CU2SE_BETA, type code %, sha256 `c43a98dbd0136561…`

~~~~text
62: PHASE CU2SE_BETA % 2 2 1 !
63: CONST CU2SE_BETA : CU% SE : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## CU3SE2 (Cu–Se)

- Id: `phase:cu-se:cu3se2`; status `assigned`
- Structure: Cu3Se2 · tP10 · P-42_1m (113); type `st:cu3se2-tp10`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cu 0.6000, Se 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–390.33 K, x(Se) 0.4–0.4
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:cu3se2)

Names (6): _corpus: _corpus:phase:cu-se:cu3se2  
_mp: _mp:mp-aaaabepn  
_oqmd: _oqmd:oqmd-1659  
_paper: _paper:10.1007/s11669-023-01074-8:Cu3Se2  
_tdb: _tdb:CuSe-08Du.tdb:CU3SE2, tdb:CuSe-23Liu.tdb:CU3SE2  


### TDB models of CU3SE2 (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): CU3SE2, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
63: PHASE CU3SE2 % 2 3 2 !
64: CONST CU3SE2 : CU : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): CU3SE2, type code %, sha256 `c43a98dbd0136561…`

~~~~text
67: PHASE CU3SE2 % 2 3 2 !
68: CONST CU3SE2 : CU : SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_
- [doi:10.1139/v75-122](https://doi.org/10.1139/v75-122) Ritchie MacLaren Murray, Robert Donald Heyding, The Copper–Selenium System at Temperatures to 850 K and Pressures To 50 Kbar, Can. J. Chem. 53, 878-887 (1975).  
_cited as the source of values for this phase_

## CUSE_ALPHA (Cu–Se)

- Id: `phase:cu-se:cuse-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Cmcm (63) — on-hull MP CuSe at x(SE)=0.5000
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Cu1 Se1 at x(SE)=0.5000
- Candidate (sgte_mmc2): CuSe-alpha · hP26 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CUSE_ALPHA: CuSe-alpha (klockmannite)
- Candidate (tdb_comment): CuSe-alpha · hP26 · P6_3/mmc — CuSe-08Du.tdb: 'Prototype CuSe-alpha (hP26, P6_3/mmc), klockmannite'
- Candidate (tdb_comment): CuSe-alpha · hP26 · P6_3/mmc — CuSe-23Liu.tdb: 'Prototype CuSe-alpha (hP26, P6_3/mmc), klockmannite'
- Stoichiometry: Cu 0.5000, Se 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–328.45 K, x(Se) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:cuse-alpha)

Names (3): _corpus: _corpus:phase:cu-se:cuse-alpha  
_tdb: _tdb:CuSe-08Du.tdb:CUSE_ALPHA, tdb:CuSe-23Liu.tdb:CUSE_ALPHA  


### TDB models of CUSE_ALPHA (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): CUSE_ALPHA, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
68: PHASE CUSE_ALPHA % 2 1 1 !
69: CONST CUSE_ALPHA : CU : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): CUSE_ALPHA, type code %, sha256 `c43a98dbd0136561…`

~~~~text
72: PHASE CUSE_ALPHA % 2 1 1 !
73: CONST CUSE_ALPHA : CU : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## CUSE_B18 (Cu–Se)

- Id: `phase:cu-se:cuse-b18`; status `assigned`
- Structure: CuS · B18 · hP12 · P6_3/mmc (194); type `st:b18-cus-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.5000, Se 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 409.15–652.72 K, x(Se) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:cuse-b18)

Names (3): _corpus: _corpus:phase:cu-se:cuse-b18  
_tdb: _tdb:CuSe-08Du.tdb:CUSE_B18, tdb:CuSe-23Liu.tdb:CUSE_B18  


### TDB models of CUSE_B18 (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): CUSE_B18, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
78: PHASE CUSE_B18 % 2 1 1 !
79: CONST CUSE_B18 : CU : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): CUSE_B18, type code %, sha256 `c43a98dbd0136561…`

~~~~text
82: PHASE CUSE_B18 % 2 1 1 !
83: CONST CUSE_B18 : CU : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## CUSE_BETA (Cu–Se)

- Id: `phase:cu-se:cuse-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Cmcm (63) — on-hull MP CuSe at x(SE)=0.5000
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Cu1 Se1 at x(SE)=0.5000
- Candidate (sgte_mmc2): CuS (alpha?) · oC24 · Cmcm (63) — Hallstedt 2025 mmc2 row for CUSE_BETA: CuSe-beta
- Candidate (tdb_comment): CuS · oC24 · Cmcm, 63 — CuSe-08Du.tdb: 'Prototype CuS (oC24, Cmcm, 63)'
- Candidate (tdb_comment): CuS · oC24 · Cmcm — CuSe-23Liu.tdb: 'Prototype CuS (oC24, Cmcm)'
- Stoichiometry: Cu 0.5000, Se 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 326.81–410.42 K, x(Se) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:cuse-beta)

Names (3): _corpus: _corpus:phase:cu-se:cuse-beta  
_tdb: _tdb:CuSe-08Du.tdb:CUSE_BETA, tdb:CuSe-23Liu.tdb:CUSE_BETA  


### TDB models of CUSE_BETA (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): CUSE_BETA, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
73: PHASE CUSE_BETA % 2 1 1 !
74: CONST CUSE_BETA : CU : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): CUSE_BETA, type code %, sha256 `c43a98dbd0136561…`

~~~~text
77: PHASE CUSE_BETA % 2 1 1 !
78: CONST CUSE_BETA : CU : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## CUSE2_C18 (Cu–Se)

- Id: `phase:cu-se:cuse2-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacyy and oqmd-1660, space group 58
- Stoichiometry: Cu 0.3333, Se 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–610.5 K, x(Se) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:cuse2-c18)

Names (5): _corpus: _corpus:phase:cu-se:cuse2-c18  
_mp: _mp:mp-aaaaacyy  
_oqmd: _oqmd:oqmd-1660  
_tdb: _tdb:CuSe-08Du.tdb:CUSE2_C18, tdb:CuSe-23Liu.tdb:CUSE2_C18  


### TDB models of CUSE2_C18 (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): CUSE2_C18, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
83: PHASE CUSE2_C18 % 2 1 2 !
84: CONST CUSE2_C18 : CU : SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): CUSE2_C18, type code %, sha256 `c43a98dbd0136561…`

~~~~text
87: PHASE CUSE2_C18 % 2 1 2 !
88: CONST CUSE2_C18 : CU : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## FCC_A1 (Cu–Se)

- Id: `phase:cu-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1357.77 K, x(Se) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-se:fcc-a1  
_tdb: _tdb:CuSe-08Du.tdb:FCC_A1, tdb:CuSe-23Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): FCC_A1, type code %A, sha256 `47155ae6b8c026d3…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CU : VA : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): FCC_A1, type code %A, sha256 `c43a98dbd0136561…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## HCP_A3 (Cu–Se)

- Id: `phase:cu-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:hcp-a3)

Names (3): _corpus: _corpus:phase:cu-se:hcp-a3  
_tdb: _tdb:CuSe-08Du.tdb:HCP_A3, tdb:CuSe-23Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): HCP_A3, type code %A, sha256 `47155ae6b8c026d3…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CU : VA : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): HCP_A3, type code %A, sha256 `c43a98dbd0136561…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
_assessment that models this phase_

## LIQUID (Cu–Se)

- Id: `phase:cu-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 494–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-se:liquid)

Names (3): _corpus: _corpus:phase:cu-se:liquid  
_tdb: _tdb:CuSe-08Du.tdb:LIQUID, tdb:CuSe-23Liu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuSe-08Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-08Du.tdb): LIQUID, type code %, sha256 `47155ae6b8c026d3…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CU CU2SE SE : !
~~~~

[CuSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSe-23Liu.tdb): LIQUID, type code %, sha256 `c43a98dbd0136561…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : CU CU2SE SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.3139/146.101636](https://doi.org/10.3139/146.101636) Z. Du, C. Guo, M. Tao, C. Li, Int. J. Mater. Res., 99, 294-300(2008).  
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
