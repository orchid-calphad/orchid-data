# Cu–Pu phases

> Cu–Pu system: 12 phases (tier A 4, tier C 2, liquid 1, needs_review 5); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-PU.html · Markdown: https://data.orchid-project.org/phases/pages/CU-PU.md

12 phases (tier A 4, tier C 2, liquid 1, needs_review 5); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-PU) · [full JSON](https://data.orchid-project.org/phases/systems/CU-PU.json) · [Cu–Pu system page](https://data.orchid-project.org/systems/CU-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Pu system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-cu-pu-a6-tetragonal); _phase:cu-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 700.79–755.67 K, x(Pu) 0.99888–1 | 4 | 1 |
| [BCC_A2](#phase-cu-pu-bcc-a2); _phase:cu-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 720–3999.25 K, x(Pu) 0.94026–1 | 4 | 1 |
| [CU17PU4](#phase-cu-pu-cu17pu4); _phase:cu-pu:cu17pu4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1228.87 K, x(Pu) 0.19048–0.19048 | 4 | 1 |
| [CU2PU](#phase-cu-pu-cu2pu); _phase:cu-pu:cu2pu_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1133.59 K, x(Pu) 0.33333–0.33333 | 8 | 1 |
| [CU4PU](#phase-cu-pu-cu4pu); _phase:cu-pu:cu4pu_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1173.87 K, x(Pu) 0.2–0.2 | 4 | 1 |
| [CU6PU](#phase-cu-pu-cu6pu); _phase:cu-pu:cu6pu_ | CeCu6 · oP28 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1203.82 K, x(Pu) 0.14286–0.14286 | 4 | 1 |
| [FCC_A1](#phase-cu-pu-fcc-a1); _phase:cu-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1443.38 K, x(Pu) 0–1 | 3 | 1 |
| [HCP_A3](#phase-cu-pu-hcp-a3); _phase:cu-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cu-pu-liquid); _phase:cu-pu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 899.88–4000 K, x(Pu) 0–1 | 10 | 1 |
| [ALPHA_PU](#phase-cu-pu-pu-alpha); _phase:cu-pu:pu-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1 | 0 | 1 |
| [BETA_PU](#phase-cu-pu-pu-beta); _phase:cu-pu:pu-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1 | 0 | 1 |
| [GAMMA_PU](#phase-cu-pu-pu-gamma); _phase:cu-pu:pu-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 487.9–593.06 K, x(Pu) 1–1 | 0 | 1 |

## TETRAGONAL_A6 (Cu–Pu)

- Id: `phase:cu-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 700.79–755.67 K, x(Pu) 0.99888–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:a6-tetragonal)

Names (4): _corpus: _corpus:phase:cu-pu:a6-tetragonal, corpus:phase:cu-pu:tetragonal-a6  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:δ'Pu  
_tdb: _tdb:CuPu-09Wan.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): TETRAGONAL_A6, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
41: PHASE TETRAGONAL_A6 % 1 1 !
42: CONST TETRAGONAL_A6 : CU PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Cu–Pu)

- Id: `phase:cu-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 720–3999.25 K, x(Pu) 0.94026–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-pu:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:εPu  
_tdb: _tdb:CuPu-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): BCC_A2, type code %B, sha256 `6d0db724a0d0d814…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CU PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## CU17PU4 (Cu–Pu)

- Id: `phase:cu-pu:cu17pu4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu17Pu4) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu17Pu4) — Hallstedt 2025 mmc2 row for CU17PU4: Cu17Pu4
- Stoichiometry: Cu 0.8095, Pu 0.1905
- Stability: stable in 1 of 1 calculated diagram(s): 300–1228.87 K, x(Pu) 0.19048–0.19048
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:cu17pu4)

Names (3): _corpus: _corpus:phase:cu-pu:cu17pu4  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:Cu17Pu4  
_tdb: _tdb:CuPu-09Wan.tdb:CU17PU4  


### TDB models of CU17PU4 (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): CU17PU4, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
66: PHASE CU17PU4 % 2 17 4 !
67: CONST CU17PU4 : CU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## CU2PU (Cu–Pu)

- Id: `phase:cu-pu:cu2pu`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Pu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1133.59 K, x(Pu) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:cu2pu)

Names (3): _corpus: _corpus:phase:cu-pu:cu2pu  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:Cu2Pu  
_tdb: _tdb:CuPu-09Wan.tdb:CU2PU  


### TDB models of CU2PU (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): CU2PU, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
76: PHASE CU2PU % 2 2 1 !
77: CONST CU2PU : CU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## CU4PU (Cu–Pu)

- Id: `phase:cu-pu:cu4pu`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu4Pu) · oP20 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu4Pu) · oP20 — Hallstedt 2025 mmc2 row for CU4PU: Cu4Pu
- Stoichiometry: Cu 0.8000, Pu 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1173.87 K, x(Pu) 0.2–0.2
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:cu4pu)

Names (3): _corpus: _corpus:phase:cu-pu:cu4pu  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:Cu4Pu  
_tdb: _tdb:CuPu-09Wan.tdb:CU4PU  


### TDB models of CU4PU (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): CU4PU, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
71: PHASE CU4PU % 2 4 1 !
72: CONST CU4PU : CU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## CU6PU (Cu–Pu)

- Id: `phase:cu-pu:cu6pu`; status `assigned`
- Structure: CeCu6 · oP28 · Pnma (62); type `st:cecu6-op28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.8571, Pu 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–1203.82 K, x(Pu) 0.14286–0.14286
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:cu6pu)

Names (3): _corpus: _corpus:phase:cu-pu:cu6pu  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:Cu6Pu  
_tdb: _tdb:CuPu-09Wan.tdb:CU6PU  


### TDB models of CU6PU (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): CU6PU, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
61: PHASE CU6PU % 2 6 1 !
62: CONST CU6PU : CU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cu–Pu)

- Id: `phase:cu-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1443.38 K, x(Pu) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-pu:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:(Cu), paper:10.1016/j.jnucmat.2009.04.017:δPu  
_tdb: _tdb:CuPu-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): FCC_A1, type code %A, sha256 `6d0db724a0d0d814…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CU% PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Cu–Pu)

- Id: `phase:cu-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-pu:hcp-a3  
_tdb: _tdb:CuPu-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): HCP_A3, type code %A, sha256 `6d0db724a0d0d814…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase_

## LIQUID (Cu–Pu)

- Id: `phase:cu-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 899.88–4000 K, x(Pu) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:liquid)

Names (3): _corpus: _corpus:phase:cu-pu:liquid  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:L  
_tdb: _tdb:CuPu-09Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): LIQUID, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CU PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_

## ALPHA_PU (Cu–Pu)

- Id: `phase:cu-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — CuPu-09Wan.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:pu-alpha)

Names (2): _corpus: _corpus:phase:cu-pu:pu-alpha  
_tdb: _tdb:CuPu-09Wan.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): ALPHA_PU, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
46: PHASE ALPHA_PU % 1 1 !
47: CONST ALPHA_PU : CU PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase_

## BETA_PU (Cu–Pu)

- Id: `phase:cu-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — CuPu-09Wan.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stability: stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:pu-beta)

Names (2): _corpus: _corpus:phase:cu-pu:pu-beta  
_tdb: _tdb:CuPu-09Wan.tdb:BETA_PU  


### TDB models of BETA_PU (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): BETA_PU, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
51: PHASE BETA_PU % 1 1 !
52: CONST BETA_PU : CU PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase_

## GAMMA_PU (Cu–Pu)

- Id: `phase:cu-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — CuPu-09Wan.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stability: stable in 1 of 1 calculated diagram(s): 487.9–593.06 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pu:pu-gamma)

Names (2): _corpus: _corpus:phase:cu-pu:pu-gamma  
_tdb: _tdb:CuPu-09Wan.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (1): PHASE and CONSTITUENT statements as written

[CuPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPu-09Wan.tdb): GAMMA_PU, type code %, sha256 `6d0db724a0d0d814…`

~~~~text
56: PHASE GAMMA_PU % 1 1 !
57: CONST GAMMA_PU : CU PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
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
