# Cu–In phases

> Cu–In system: 12 phases (tier A 5, tier B 1, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-IN.html · Markdown: https://data.orchid-project.org/phases/pages/CU-IN.md

12 phases (tier A 5, tier B 1, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-IN) · [full JSON](https://data.orchid-project.org/phases/systems/CU-IN.json) · [Cu–In system page](https://data.orchid-project.org/systems/CU-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–In system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-cu-in-a6-tetragonal); _phase:cu-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–429.75 K, x(In) 1–1 | 20 | 5 |
| [BCC_A2](#phase-cu-in-bcc-a2); _phase:cu-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 5 calculated diagram(s): 840.77–984.32 K, x(In) 0.18704–0.24672 | 18 | 5 |
| [CU11IN9](#phase-cu-in-cu11in9); _phase:cu-in:cu11in9_ | AlCu(r) · mC20 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–610 K, x(In) 0.45–0.45 | 7 | 5 |
| [CU2IN_LT](#phase-cu-in-cu2in); _phase:cu-in:cu2in_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–939.33 K, x(In) 0.33333–0.36 | 7 | 4 |
| [CU2IN_B82](#phase-cu-in-cu2in-b82); _phase:cu-in:cu2in-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 334.9–942.76 K, x(In) 0.3266–0.40007 | 0 | 4 |
| [CU4IN](#phase-cu-in-cu4in); _phase:cu-in:cu4in_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 864.81–983.67 K, x(In) 0.2–0.2 | 0 | 1 |
| [CU7IN3](#phase-cu-in-cu7in3); _phase:cu-in:cu7in3_ | Cu7In3 · aP40 · P-1 (2) | tier B: DFT-supported (unique MP + OQMD match) | stable in 5 of 5 calculated diagram(s): 300–955.77 K, x(In) 0.3–0.3 | 9 | 5 |
| [CU9IN4_D83](#phase-cu-in-cu9in4-d83); _phase:cu-in:cu9in4-d83_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 886.25–961.64 K, x(In) 0.27969–0.33886 | 10 | 4 |
| [CUIN2](#phase-cu-in-cuin2); _phase:cu-in:cuin2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–380.76 K, x(In) 0.667–0.667 | 0 | 1 |
| [FCC_A1](#phase-cu-in-fcc-a1); _phase:cu-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1359.77 K, x(In) 0–0.10397 | 4 | 5 |
| [HCP_A3](#phase-cu-in-hcp-a3); _phase:cu-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-cu-in-liquid); _phase:cu-in:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 425.92–2500 K, x(In) 0–1 | 12 | 5 |

## TETRAGONAL_A6 (Cu–In)

- Id: `phase:cu-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–429.75 K, x(In) 1–1
- Literature: 20 values (20 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:a6-tetragonal)

Names (12): _corpus: _corpus:phase:cu-in:a6-tetragonal, corpus:phase:cu-in:tetragonal-a6  
_paper: _paper:10.1007/bf02652158:(In), paper:10.1007/bf02652158:δ, paper:10.1007/bf02652158:δ2, paper:10.1361/105497102770331163:δ, paper:10.1361/105497102770331352:δ  
_tdb: _tdb:CuIn-02Her.tdb:TETRAGONAL_A6, tdb:CuIn-02Liu-LB.tdb:TETRAGONAL_A6, tdb:CuIn-02Liu-orig.tdb:TETRAGONAL_A6, tdb:CuIn-24Cha.tdb:TETRAGONAL_A6, tdb:CuIn-93Kao.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (5): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): TETRAGONAL_A6, type code %, sha256 `939f507801d25dfe…`

~~~~text
45: PHASE TETRAGONAL_A6 % 1 1 !
46: CONST TETRAGONAL_A6 : IN : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): TETRAGONAL_A6, type code %, sha256 `bfea037b638c1645…`

~~~~text
58: PHASE TETRAGONAL_A6 % 1 1 !
59: CONST TETRAGONAL_A6 : IN : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): TETRAGONAL_A6, type code %, sha256 `d4b7857edb2a6ed4…`

~~~~text
48: PHASE TETRAGONAL_A6 % 1 1 !
49: CONST TETRAGONAL_A6 : IN : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): TETRAGONAL_A6, type code %, sha256 `afb9d98766f375ca…`

~~~~text
45: PHASE TETRAGONAL_A6 % 1 1 !
46: CONST TETRAGONAL_A6 : IN : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): TETRAGONAL_A6, type code %, sha256 `d051d27676496f92…`

~~~~text
60: PHASE TETRAGONAL_A6 % 1 1 !
61: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1021/j150541a005](https://doi.org/10.1021/j150541a005) O. J. Kleppa, Heat of Formation of Solid and Liquid Binary Alloys of Copper with Cadmium, Indium, Tin and Antimony at 450°, J. Phys. Chem. 60, 852-858 (1956).  
_cited as the source of values for this phase_

## BCC_A2 (Cu–In)

- Id: `phase:cu-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 5 calculated diagram(s): 840.77–984.32 K, x(In) 0.18704–0.24672
- Literature: 18 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:bcc-a2)

Names (9): _corpus: _corpus:phase:cu-in:bcc-a2  
_paper: _paper:10.1007/bf02652158:β, paper:10.1361/105497102770331163:β, paper:10.1361/105497102770331352:β  
_tdb: _tdb:CuIn-02Her.tdb:BCC_A2, tdb:CuIn-02Liu-LB.tdb:BCC_A2, tdb:CuIn-02Liu-orig.tdb:BCC_A2, tdb:CuIn-24Cha.tdb:BCC_A2, tdb:CuIn-93Kao.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): BCC_A2, type code %B, sha256 `939f507801d25dfe…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU IN : VA : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): BCC_A2, type code %B, sha256 `bfea037b638c1645…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : CU IN : VA : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): BCC_A2, type code %B, sha256 `d4b7857edb2a6ed4…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CU IN : VA : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): BCC_A2, type code %B, sha256 `afb9d98766f375ca…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU IN : VA : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): BCC_A2, type code %B, sha256 `d051d27676496f92…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : CU IN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_

## CU11IN9 (Cu–In)

- Id: `phase:cu-in:cu11in9`; status `assigned`
- Structure: AlCu(r) · mC20 · C2/m (12); type `st:alcu-r-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.5500, In 0.4500
- Stability: stable in 5 of 5 calculated diagram(s): 300–610 K, x(In) 0.45–0.45
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:cu11in9)

Names (7): _corpus: _corpus:phase:cu-in:cu11in9  
_paper: _paper:10.1007/bf02652158:Cu11In9  
_tdb: _tdb:CuIn-02Her.tdb:CU11IN9, tdb:CuIn-02Liu-LB.tdb:CU11IN9, tdb:CuIn-02Liu-orig.tdb:CU11IN9, tdb:CuIn-24Cha.tdb:CU11IN9, tdb:CuIn-93Kao.tdb:CU11IN9  


### TDB models of CU11IN9 (5): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): CU11IN9, type code %, sha256 `939f507801d25dfe…`

~~~~text
66: PHASE CU11IN9 % 2 11 9 !
67: CONST CU11IN9 : CU : IN : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): CU11IN9, type code %, sha256 `bfea037b638c1645…`

~~~~text
89: PHASE CU11IN9 % 2 0.55 0.45 !
90: CONST CU11IN9 : CU : IN : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): CU11IN9, type code %, sha256 `d4b7857edb2a6ed4…`

~~~~text
74: PHASE CU11IN9 % 2 0.55 0.45 !
75: CONST CU11IN9 : CU : IN : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): CU11IN9, type code %, sha256 `afb9d98766f375ca…`

~~~~text
71: PHASE CU11IN9 % 2 0.55 0.45 !
72: CONST CU11IN9 : CU : IN : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): CU11IN9, type code %, sha256 `d051d27676496f92…`

~~~~text
82: PHASE CU11IN9 % 2 11 9 !
83: CONST CU11IN9 : CU : IN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase_

## CU2IN_LT (Cu–In)

- Id: `phase:cu-in:cu2in`; status `needs_review`
- No structure assigned. Why: models_disagree_on_composition; no_structure_token
- Candidate (sgte_mmc2): (Cu2In) — Hallstedt 2025 mmc2 row for CU2IN_LT: Cu2In-lt
- Candidate (tdb_comment): InNi2 · hP6 · P6_3/mmc — CuIn-93Kao.tdb: 'Prototype InNi2 (hP6, P6_3/mmc), NiAs-type suggested in LB binary, Cu2In-ht'
- Stability: stable in 4 of 4 calculated diagram(s): 300–939.33 K, x(In) 0.33333–0.36
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:cu2in)

Names (7): _corpus: _corpus:phase:cu-in:cu2in  
_paper: _paper:10.1007/bf02652158:η, paper:10.1007/bf02652158:ηCu2In  
_tdb: _tdb:CuIn-02Liu-LB.tdb:CU2IN_LT, tdb:CuIn-02Liu-orig.tdb:CU2IN_LT, tdb:CuIn-24Cha.tdb:CU2IN_LT, tdb:CuIn-93Kao.tdb:CU2IN  


### TDB models of CU2IN_LT (4): PHASE and CONSTITUENT statements as written

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): CU2IN_LT, type code %, sha256 `bfea037b638c1645…`

~~~~text
84: PHASE CU2IN_LT % 2 0.64 0.36 !
85: CONST CU2IN_LT : CU : IN : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): CU2IN_LT, type code %, sha256 `d4b7857edb2a6ed4…`

~~~~text
69: PHASE CU2IN_LT % 2 0.64 0.36 !
70: CONST CU2IN_LT : CU : IN : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): CU2IN_LT, type code %, sha256 `afb9d98766f375ca…`

~~~~text
66: PHASE CU2IN_LT % 2 0.64 0.36 !
67: CONST CU2IN_LT : CU : IN : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): CU2IN, type code %, sha256 `d051d27676496f92…`

~~~~text
77: PHASE CU2IN % 2 2 1 !
78: CONST CU2IN : CU : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase_

## CU2IN_B82 (Cu–In)

- Id: `phase:cu-in:cu2in-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CuIn-02Her.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 334.9–942.76 K, x(In) 0.3266–0.40007
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:cu2in-b82)

Names (5): _corpus: _corpus:phase:cu-in:cu2in-b82  
_tdb: _tdb:CuIn-02Her.tdb:CU2IN_B82, tdb:CuIn-02Liu-LB.tdb:CU2IN_B82, tdb:CuIn-02Liu-orig.tdb:CU2IN_B82, tdb:CuIn-24Cha.tdb:CU2IN_B82  


### TDB models of CU2IN_B82 (4): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): CU2IN_B82, type code %, sha256 `939f507801d25dfe…`

~~~~text
61: PHASE CU2IN_B82 % 2 6 4 !
62: CONST CU2IN_B82 : CU IN : CU IN : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): CU2IN_B82, type code %, sha256 `bfea037b638c1645…`

~~~~text
74: PHASE CU2IN_B82 % 3 1 1 1 !
75: CONST CU2IN_B82 : CU : CU VA : IN : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): CU2IN_B82, type code %, sha256 `d4b7857edb2a6ed4…`

~~~~text
64: PHASE CU2IN_B82 % 3 0.545 0.122 0.333 !
65: CONST CU2IN_B82 : CU : CU IN : IN : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): CU2IN_B82, type code %, sha256 `afb9d98766f375ca…`

~~~~text
61: PHASE CU2IN_B82 % 3 0.545 0.122 0.333 !
62: CONST CU2IN_B82 : CU : CU IN : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase_

## CU4IN (Cu–In)

- Id: `phase:cu-in:cu4in`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Candidate (tdb_comment): W · cI2 · Im-3m — CuIn-93Kao.tdb: 'Prototype W (cI2, Im-3m), bcc!!, beta'
- Stoichiometry: Cu 0.8000, In 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 864.81–983.67 K, x(In) 0.2–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:cu4in)

Names (2): _corpus: _corpus:phase:cu-in:cu4in  
_tdb: _tdb:CuIn-93Kao.tdb:CU4IN  


### TDB models of CU4IN (1): PHASE and CONSTITUENT statements as written

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): CU4IN, type code %, sha256 `d051d27676496f92…`

~~~~text
65: PHASE CU4IN % 2 4 1 !
66: CONST CU4IN : CU : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase_

## CU7IN3 (Cu–In)

- Id: `phase:cu-in:cu7in3`; status `assigned`
- Structure: Cu7In3 · aP40 · P-1 (2); type `st:cu7in3-ap40`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cu 0.7000, In 0.3000
- Stability: stable in 5 of 5 calculated diagram(s): 300–955.77 K, x(In) 0.3–0.3
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:cu7in3)

Names (10): _corpus: _corpus:phase:cu-in:cu7in3  
_mp: _mp:mp-aaaabgnp  
_oqmd: _oqmd:oqmd-2051515  
_paper: _paper:10.1007/bf02652158:γ, paper:10.1007/bf02652158:δCu7In3  
_tdb: _tdb:CuIn-02Her.tdb:CU7IN3, tdb:CuIn-02Liu-LB.tdb:CU7IN3, tdb:CuIn-02Liu-orig.tdb:CU7IN3, tdb:CuIn-24Cha.tdb:CU7IN3, tdb:CuIn-93Kao.tdb:CU7IN3  


### TDB models of CU7IN3 (5): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): CU7IN3, type code %, sha256 `939f507801d25dfe…`

~~~~text
55: PHASE CU7IN3 % 2 7 3 !
56: CONST CU7IN3 : CU : IN : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): CU7IN3, type code %, sha256 `bfea037b638c1645…`

~~~~text
68: PHASE CU7IN3 % 2 0.7 0.3 !
69: CONST CU7IN3 : CU : IN : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): CU7IN3, type code %, sha256 `d4b7857edb2a6ed4…`

~~~~text
58: PHASE CU7IN3 % 2 0.7 0.3 !
59: CONST CU7IN3 : CU : IN : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): CU7IN3, type code %, sha256 `afb9d98766f375ca…`

~~~~text
55: PHASE CU7IN3 % 2 0.7 0.3 !
56: CONST CU7IN3 : CU : IN : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): CU7IN3, type code %, sha256 `d051d27676496f92…`

~~~~text
70: PHASE CU7IN3 % 2 7 3 !
71: CONST CU7IN3 : CU : IN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase_

## CU9IN4_D83 (Cu–In)

- Id: `phase:cu-in:cu9in4-d83`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_D8_3; site_ratios_contradict_D8_3:CuIn-02Her.tdb
- Candidate (dft_mp): P-1 (2) — on-hull MP In3Cu7 at x(IN)=0.3000
- Candidate (dft_oqmd): P-1 (2) — on-hull OQMD Cu7 In3 at x(IN)=0.3000
- Candidate (name_token): Al4Cu9 · D8_3 · cP52 · P-43m (215) — Strukturbericht/word 'D83' in the TDB name
- Candidate (sgte_mmc2): Al4Cu9 · D8_3 · cP52 · P-43m (215) — Hallstedt 2025 mmc2 row for CU9IN4_D83: Cu9In4 (gamma)
- Candidate (sgte_mmc2): Al4Cu9 · D8_3 · cP52 · P-43m (215) — Hallstedt 2025 mmc2 row for CU9IN4_D83: Cu9In4 (gamma) (= 17:3:6)
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — CuIn-02Her.tdb: 'Prototype Al4Cu9 (cP52, P-43m), gamma-CuIn'
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — CuIn-02Liu-LB.tdb: 'Prototype Al4Cu9 (cP52, P-43m), gamma-CuIn'
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — CuIn-02Liu-orig.tdb: 'Prototype Al4Cu9 (cP52, P-43m), gamma-CuIn'
- Stability: stable in 4 of 4 calculated diagram(s): 886.25–961.64 K, x(In) 0.27969–0.33886
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:cu9in4-d83)

Names (7): _corpus: _corpus:phase:cu-in:cu9in4-d83  
_paper: _paper:10.1361/105497102770331163:γ, paper:10.1361/105497102770331352:γ  
_tdb: _tdb:CuIn-02Her.tdb:CU9IN4_D83, tdb:CuIn-02Liu-LB.tdb:CU9IN4_D83, tdb:CuIn-02Liu-orig.tdb:CU9IN4_D83, tdb:CuIn-24Cha.tdb:CU9IN4_D83  


### TDB models of CU9IN4_D83 (4): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): CU9IN4_D83, type code %, sha256 `939f507801d25dfe…`

~~~~text
50: PHASE CU9IN4_D83 % 2 3 1 !
51: CONST CU9IN4_D83 : CU IN : IN : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): CU9IN4_D83, type code %, sha256 `bfea037b638c1645…`

~~~~text
63: PHASE CU9IN4_D83 % 3 0.654 0.115 0.231 !
64: CONST CU9IN4_D83 : CU : CU IN : IN : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): CU9IN4_D83, type code %, sha256 `d4b7857edb2a6ed4…`

~~~~text
53: PHASE CU9IN4_D83 % 3 0.654 0.115 0.231 !
54: CONST CU9IN4_D83 : CU : CU IN : IN : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): CU9IN4_D83, type code %, sha256 `afb9d98766f375ca…`

~~~~text
50: PHASE CU9IN4_D83 % 3 0.654 0.115 0.231 !
51: CONST CU9IN4_D83 : CU : CU IN : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_

## CUIN2 (Cu–In)

- Id: `phase:cu-in:cuin2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (CuIn2) — Hallstedt 2025 mmc2 row for CUIN2: CuIn2
- Stoichiometry: Cu 0.3330, In 0.6670
- Stability: stable in 1 of 1 calculated diagram(s): 300–380.76 K, x(In) 0.667–0.667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:cuin2)

Names (2): _corpus: _corpus:phase:cu-in:cuin2  
_tdb: _tdb:CuIn-24Cha.tdb:CUIN2  


### TDB models of CUIN2 (1): PHASE and CONSTITUENT statements as written

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): CUIN2, type code %, sha256 `afb9d98766f375ca…`

~~~~text
76: PHASE CUIN2 % 2 0.333 0.667 !
77: CONST CUIN2 : CU : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_

## FCC_A1 (Cu–In)

- Id: `phase:cu-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1359.77 K, x(In) 0–0.10397
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:fcc-a1)

Names (7): _corpus: _corpus:phase:cu-in:fcc-a1  
_paper: _paper:10.1007/bf02652158:α  
_tdb: _tdb:CuIn-02Her.tdb:FCC_A1, tdb:CuIn-02Liu-LB.tdb:FCC_A1, tdb:CuIn-02Liu-orig.tdb:FCC_A1, tdb:CuIn-24Cha.tdb:FCC_A1, tdb:CuIn-93Kao.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): FCC_A1, type code %A, sha256 `939f507801d25dfe…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU% IN : VA : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): FCC_A1, type code %A, sha256 `bfea037b638c1645…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : CU% IN : VA : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): FCC_A1, type code %A, sha256 `d4b7857edb2a6ed4…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CU% IN : VA : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): FCC_A1, type code %A, sha256 `afb9d98766f375ca…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU% IN : VA : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): FCC_A1, type code %A, sha256 `d051d27676496f92…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : CU% IN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase_

## HCP_A3 (Cu–In)

- Id: `phase:cu-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:hcp-a3)

Names (6): _corpus: _corpus:phase:cu-in:hcp-a3  
_tdb: _tdb:CuIn-02Her.tdb:HCP_A3, tdb:CuIn-02Liu-LB.tdb:HCP_A3, tdb:CuIn-02Liu-orig.tdb:HCP_A3, tdb:CuIn-24Cha.tdb:HCP_A3, tdb:CuIn-93Kao.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): HCP_A3, type code %A, sha256 `939f507801d25dfe…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU IN : VA : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): HCP_A3, type code %A, sha256 `bfea037b638c1645…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : CU IN : VA : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): HCP_A3, type code %A, sha256 `d4b7857edb2a6ed4…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CU IN : VA : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): HCP_A3, type code %A, sha256 `afb9d98766f375ca…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU IN : VA : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): HCP_A3, type code %A, sha256 `d051d27676496f92…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : CU IN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
_assessment that models this phase_

## LIQUID (Cu–In)

- Id: `phase:cu-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 425.92–2500 K, x(In) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-in:liquid)

Names (7): _corpus: _corpus:phase:cu-in:liquid  
_paper: _paper:10.1007/bf02652158:L  
_tdb: _tdb:CuIn-02Her.tdb:LIQUID, tdb:CuIn-02Liu-LB.tdb:LIQUID, tdb:CuIn-02Liu-orig.tdb:LIQUID, tdb:CuIn-24Cha.tdb:LIQUID, tdb:CuIn-93Kao.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[CuIn-02Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Her.tdb): LIQUID, type code %, sha256 `939f507801d25dfe…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU IN : !
~~~~

[CuIn-02Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-LB.tdb): LIQUID, type code %, sha256 `bfea037b638c1645…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : CU IN : !
~~~~

[CuIn-02Liu-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-02Liu-orig.tdb): LIQUID, type code %, sha256 `d4b7857edb2a6ed4…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CU IN : !
~~~~

[CuIn-24Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-24Cha.tdb): LIQUID, type code %, sha256 `afb9d98766f375ca…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU IN : !
~~~~

[CuIn-93Kao.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIn-93Kao.tdb): LIQUID, type code %, sha256 `d051d27676496f92…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : CU IN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02652158](https://doi.org/10.1007/BF02652158) C.R. Kao, A. Bolcavage, S.-L. Chen, S.W. Chen, Y.A. Chang, A.D. Romig, J. Phase Equilib., 14, 22-30(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102700](https://doi.org/10.1016/j.calphad.2024.102700) F.-L. Chang, Y.-H. Lin, H.-T. Hung, C.R. Kao, Calphad, 85, 102700(2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331163](https://doi.org/10.1361/105497102770331163) Jean Hertz, Khadija Aissaoui, Lahcen Bouirden, A thermodynamic optimization of the Cu-In system, JPE 23, 473-479 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497102770331352](https://doi.org/10.1361/105497102770331352) H. S. Liu, Y. Cui, K. Ishida, X. J. Liu, C. P. Wang, I. Ohnuma et al., Thermodynamic assessment of the Cu-In binary system, JPE 23, 409-415 (2002).  
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
