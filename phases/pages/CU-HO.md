# Cu–Ho phases

> Cu–Ho system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-HO.html · Markdown: https://data.orchid-project.org/phases/pages/CU-HO.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-HO) · [full JSON](https://data.orchid-project.org/phases/systems/CU-HO.json) · [Cu–Ho system page](https://data.orchid-project.org/systems/CU-HO.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-HO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Ho system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-ho-bcc-a2); _phase:cu-ho:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 1700.91–2499.66 K, x(Ho) 0.99955–1 | 0 | 2 |
| [CU2HO](#phase-cu-ho-cu2ho); _phase:cu-ho:cu2ho_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1161.14 K, x(Ho) 0.33333–0.33333 | 6 | 2 |
| [CU5HO_C15B](#phase-cu-ho-cu5ho-c15b); _phase:cu-ho:cu5ho-c15b_ | AuBe5 · C15_b · cF24 · F-43m (216) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1242.86 K, x(Ho) 0.16667–0.16667 | 5 | 2 |
| [CU5HO_D2D](#phase-cu-ho-cu5ho-d2d); _phase:cu-ho:cu5ho-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1242.86–1259.36 K, x(Ho) 0.16667–0.16667 | 4 | 2 |
| [CU7HO2](#phase-cu-ho-cu7ho2); _phase:cu-ho:cu7ho2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1143.81–1206.65 K, x(Ho) 0.22222–0.22222 | 4 | 2 |
| [CU9HO2](#phase-cu-ho-cu9ho2); _phase:cu-ho:cu9ho2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1262.98 K, x(Ho) 0.18182–0.18182 | 10 | 2 |
| [CUHO_B2](#phase-cu-ho-cuho-b2); _phase:cu-ho:cuho-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1285.55 K, x(Ho) 0.5–0.5 | 6 | 2 |
| [FCC_A1](#phase-cu-ho-fcc-a1); _phase:cu-ho:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1374.2 K, x(Ho) 0–0 | 3 | 2 |
| [HCP_A3](#phase-cu-ho-hcp-a3); _phase:cu-ho:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.14 K, x(Ho) 0.99953–1 | 2 | 2 |
| [LIQUID](#phase-cu-ho-liquid); _phase:cu-ho:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1103.13–2500 K, x(Ho) 0–1 | 21 | 2 |

## BCC_A2 (Cu–Ho)

- Id: `phase:cu-ho:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 1700.91–2499.66 K, x(Ho) 0.99955–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-ho:bcc-a2  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:BCC_A2, tdb:CuHo-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): BCC_A2, type code %B, sha256 `b376cb3e339bac72…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CU HO : VA : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): BCC_A2, type code %B, sha256 `7fa1a2bcc060b66d…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CU HO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase_

## CU2HO (Cu–Ho)

- Id: `phase:cu-ho:cu2ho`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Ho 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1161.14 K, x(Ho) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:cu2ho)

Names (4): _corpus: _corpus:phase:cu-ho:cu2ho  
_paper: _paper:10.1016/j.jallcom.2009.08.042:Cu2Ho  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:CU2HO, tdb:CuHo-09Wan.tdb:CU2HO  


### TDB models of CU2HO (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): CU2HO, type code %, sha256 `b376cb3e339bac72…`

~~~~text
66: PHASE CU2HO % 2 2 1 !
67: CONST CU2HO : CU : HO : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): CU2HO, type code %, sha256 `7fa1a2bcc060b66d…`

~~~~text
66: PHASE CU2HO % 2 2 1 !
67: CONST CU2HO : CU : HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## CU5HO_C15B (Cu–Ho)

- Id: `phase:cu-ho:cu5ho-c15b`; status `assigned`
- Structure: AuBe5 · C15_b · cF24 · F-43m (216); type `st:c15-b-aube5-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.8333, Ho 0.1667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1242.86 K, x(Ho) 0.16667–0.16667
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:cu5ho-c15b)

Names (5): _corpus: _corpus:phase:cu-ho:cu5ho-c15b  
_paper: _paper:10.1016/j.jallcom.2009.08.042:Cu5Ho, paper:10.1016/j.jallcom.2009.08.042:αCu5Ho  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:CU5HO_C15B, tdb:CuHo-09Wan.tdb:CU5HO_C15B  


### TDB models of CU5HO_C15B (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): CU5HO_C15B, type code %, sha256 `b376cb3e339bac72…`

~~~~text
46: PHASE CU5HO_C15B % 2 5 1 !
47: CONST CU5HO_C15B : CU : HO : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): CU5HO_C15B, type code %, sha256 `7fa1a2bcc060b66d…`

~~~~text
46: PHASE CU5HO_C15B % 2 5 1 !
47: CONST CU5HO_C15B : CU : HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## CU5HO_D2D (Cu–Ho)

- Id: `phase:cu-ho:cu5ho-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.8333, Ho 0.1667
- Stability: stable in 2 of 2 calculated diagram(s): 1242.86–1259.36 K, x(Ho) 0.16667–0.16667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:cu5ho-d2d)

Names (4): _corpus: _corpus:phase:cu-ho:cu5ho-d2d  
_paper: _paper:10.1016/j.jallcom.2009.08.042:βCu5Ho  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:CU5HO_D2D, tdb:CuHo-09Wan.tdb:CU5HO_D2D  


### TDB models of CU5HO_D2D (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): CU5HO_D2D, type code %, sha256 `b376cb3e339bac72…`

~~~~text
51: PHASE CU5HO_D2D % 2 5 1 !
52: CONST CU5HO_D2D : CU : HO : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): CU5HO_D2D, type code %, sha256 `7fa1a2bcc060b66d…`

~~~~text
51: PHASE CU5HO_D2D % 2 5 1 !
52: CONST CU5HO_D2D : CU : HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## CU7HO2 (Cu–Ho)

- Id: `phase:cu-ho:cu7ho2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu7Ho2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu7Ho2) — Hallstedt 2025 mmc2 row for CU7HO2: Cu7Ho2
- Stoichiometry: Cu 0.7778, Ho 0.2222
- Stability: stable in 2 of 2 calculated diagram(s): 1143.81–1206.65 K, x(Ho) 0.22222–0.22222
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:cu7ho2)

Names (4): _corpus: _corpus:phase:cu-ho:cu7ho2  
_paper: _paper:10.1016/j.jallcom.2009.08.042:Cu7Ho2  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:CU7HO2, tdb:CuHo-09Wan.tdb:CU7HO2  


### TDB models of CU7HO2 (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): CU7HO2, type code %, sha256 `b376cb3e339bac72…`

~~~~text
61: PHASE CU7HO2 % 2 7 2 !
62: CONST CU7HO2 : CU : HO : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): CU7HO2, type code %, sha256 `7fa1a2bcc060b66d…`

~~~~text
61: PHASE CU7HO2 % 2 7 2 !
62: CONST CU7HO2 : CU : HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## CU9HO2 (Cu–Ho)

- Id: `phase:cu-ho:cu9ho2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu9Ho2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu9Ho2) — Hallstedt 2025 mmc2 row for CU9HO2: Cu9Ho2
- Stoichiometry: Cu 0.8182, Ho 0.1818
- Stability: stable in 2 of 2 calculated diagram(s): 300–1262.98 K, x(Ho) 0.18182–0.18182
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:cu9ho2)

Names (4): _corpus: _corpus:phase:cu-ho:cu9ho2  
_paper: _paper:10.1016/j.jallcom.2009.08.042:Cu9Ho2  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:CU9HO2, tdb:CuHo-09Wan.tdb:CU9HO2  


### TDB models of CU9HO2 (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): CU9HO2, type code %, sha256 `b376cb3e339bac72…`

~~~~text
56: PHASE CU9HO2 % 2 9 2 !
57: CONST CU9HO2 : CU : HO : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): CU9HO2, type code %, sha256 `7fa1a2bcc060b66d…`

~~~~text
56: PHASE CU9HO2 % 2 9 2 !
57: CONST CU9HO2 : CU : HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## CUHO_B2 (Cu–Ho)

- Id: `phase:cu-ho:cuho-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.5000, Ho 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1285.55 K, x(Ho) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:cuho-b2)

Names (4): _corpus: _corpus:phase:cu-ho:cuho-b2  
_paper: _paper:10.1016/j.jallcom.2009.08.042:CuHo  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:CUHO_B2, tdb:CuHo-09Wan.tdb:CUHO_B2  


### TDB models of CUHO_B2 (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): CUHO_B2, type code %, sha256 `b376cb3e339bac72…`

~~~~text
71: PHASE CUHO_B2 % 2 1 1 !
72: CONST CUHO_B2 : CU : HO : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): CUHO_B2, type code %, sha256 `7fa1a2bcc060b66d…`

~~~~text
71: PHASE CUHO_B2 % 2 1 1 !
72: CONST CUHO_B2 : CU : HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cu–Ho)

- Id: `phase:cu-ho:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1374.2 K, x(Ho) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-ho:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.08.042:(Cu)  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:FCC_A1, tdb:CuHo-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): FCC_A1, type code %A, sha256 `b376cb3e339bac72…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CU% HO : VA : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): FCC_A1, type code %A, sha256 `7fa1a2bcc060b66d…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CU% HO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Cu–Ho)

- Id: `phase:cu-ho:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.14 K, x(Ho) 0.99953–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-ho:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.08.042:(Ho)  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:HCP_A3, tdb:CuHo-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): HCP_A3, type code %A, sha256 `b376cb3e339bac72…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CU HO% : VA : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): HCP_A3, type code %A, sha256 `7fa1a2bcc060b66d…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CU HO% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Cu–Ho)

- Id: `phase:cu-ho:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1103.13–2500 K, x(Ho) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ho:liquid)

Names (4): _corpus: _corpus:phase:cu-ho:liquid  
_paper: _paper:10.1016/j.jallcom.2009.08.042:L  
_tdb: _tdb:CuHo-09Wan-newHo.tdb:LIQUID, tdb:CuHo-09Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuHo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan-newHo.tdb): LIQUID, type code %, sha256 `b376cb3e339bac72…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CU HO : !
~~~~

[CuHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHo-09Wan.tdb): LIQUID, type code %, sha256 `7fa1a2bcc060b66d…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CU HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

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
