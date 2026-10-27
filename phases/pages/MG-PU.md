# Mg–Pu phases

> Mg–Pu system: 11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-PU.html · Markdown: https://data.orchid-project.org/phases/pages/MG-PU.md

11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-PU) · [full JSON](https://data.orchid-project.org/phases/systems/MG-PU.json) · [Mg–Pu system page](https://data.orchid-project.org/systems/MG-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Pu system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-mg-pu-a6-tetragonal); _phase:mg-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 730.29–756.52 K, x(Pu) 0.99959–1 | 0 | 1 |
| [BCC_A2](#phase-mg-pu-bcc-a2); _phase:mg-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 755.26–913 K, x(Pu) 0.99965–1 | 4 | 1 |
| [FCC_A1](#phase-mg-pu-fcc-a1); _phase:mg-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 593.02–755.26 K, x(Pu) 0.99981–1 | 4 | 1 |
| [HCP_A3](#phase-mg-pu-hcp-a3); _phase:mg-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–926 K, x(Pu) 0–0.03635 | 4 | 1 |
| [LIQUID](#phase-mg-pu-liquid); _phase:mg-pu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 833.35–4000 K, x(Pu) 0–1 | 5 | 1 |
| [MG2PU_C1](#phase-mg-pu-mg2pu-c1); _phase:mg-pu:mg2pu-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–503.66 K, x(Pu) 0.33333–0.33333 | 2 | 1 |
| [MG4PU](#phase-mg-pu-mg4pu); _phase:mg-pu:mg4pu_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–684.36 K, x(Pu) 0.2–0.2 | 4 | 1 |
| [MG6PU](#phase-mg-pu-mg6pu); _phase:mg-pu:mg6pu_ | Cu · A1 · cF4 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–709.95 K, x(Pu) 0.14286–0.14286 | 4 | 1 |
| [ALPHA_PU](#phase-mg-pu-pu-alpha); _phase:mg-pu:pu-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 0.99998–1 | 0 | 1 |
| [BETA_PU](#phase-mg-pu-pu-beta); _phase:mg-pu:pu-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1 | 0 | 1 |
| [GAMMA_PU](#phase-mg-pu-pu-gamma); _phase:mg-pu:pu-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 487.9–728.06 K, x(Pu) 0.99999–1 | 2 | 1 |

## TETRAGONAL_A6 (Mg–Pu)

- Id: `phase:mg-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 730.29–756.52 K, x(Pu) 0.99959–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:a6-tetragonal)

Names (2): _corpus: _corpus:phase:mg-pu:a6-tetragonal  
_tdb: _tdb:MgPu-09Wan.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): TETRAGONAL_A6, type code %, sha256 `43f00c0b4df80622…`

~~~~text
44: PHASE TETRAGONAL_A6 % 1 1 !
45: CONST TETRAGONAL_A6 : MG PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase_

## BCC_A2 (Mg–Pu)

- Id: `phase:mg-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 755.26–913 K, x(Pu) 0.99965–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:bcc-a2)

Names (3): _corpus: _corpus:phase:mg-pu:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:εPu  
_tdb: _tdb:MgPu-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): BCC_A2, type code %B, sha256 `43f00c0b4df80622…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MG PU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
_cited as the source of values for this phase_

## FCC_A1 (Mg–Pu)

- Id: `phase:mg-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 593.02–755.26 K, x(Pu) 0.99981–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:fcc-a1)

Names (3): _corpus: _corpus:phase:mg-pu:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:δPu  
_tdb: _tdb:MgPu-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): FCC_A1, type code %A, sha256 `43f00c0b4df80622…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MG PU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
_cited as the source of values for this phase_

## HCP_A3 (Mg–Pu)

- Id: `phase:mg-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–926 K, x(Pu) 0–0.03635
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:hcp-a3)

Names (3): _corpus: _corpus:phase:mg-pu:hcp-a3  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:(Mg)  
_tdb: _tdb:MgPu-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): HCP_A3, type code %A, sha256 `43f00c0b4df80622…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MG% PU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
_cited as the source of values for this phase_

## LIQUID (Mg–Pu)

- Id: `phase:mg-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 833.35–4000 K, x(Pu) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:liquid)

Names (4): _corpus: _corpus:phase:mg-pu:liquid  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:L1, paper:10.1016/j.jnucmat.2009.04.017:L2  
_tdb: _tdb:MgPu-09Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): LIQUID, type code %, sha256 `43f00c0b4df80622…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MG PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
_cited as the source of values for this phase_

## MG2PU_C1 (Mg–Pu)

- Id: `phase:mg-pu:mg2pu-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.6667, Pu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–503.66 K, x(Pu) 0.33333–0.33333
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:mg2pu-c1)

Names (3): _corpus: _corpus:phase:mg-pu:mg2pu-c1  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:Mg2Pu  
_tdb: _tdb:MgPu-09Wan.tdb:MG2PU_C1  


### TDB models of MG2PU_C1 (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): MG2PU_C1, type code %, sha256 `43f00c0b4df80622…`

~~~~text
74: PHASE MG2PU_C1 % 2 2 1 !
75: CONST MG2PU_C1 : MG : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
_cited as the source of values for this phase_

## MG4PU (Mg–Pu)

- Id: `phase:mg-pu:mg4pu`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Mg4Pu) · h\*\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Mg4Pu) — Hallstedt 2025 mmc2 row for MG4PU: Mg4Pu
- Stoichiometry: Mg 0.8000, Pu 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–684.36 K, x(Pu) 0.2–0.2
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:mg4pu)

Names (3): _corpus: _corpus:phase:mg-pu:mg4pu  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:Mg4Pu  
_tdb: _tdb:MgPu-09Wan.tdb:MG4PU  


### TDB models of MG4PU (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): MG4PU, type code %, sha256 `43f00c0b4df80622…`

~~~~text
69: PHASE MG4PU % 2 4 1 !
70: CONST MG4PU : MG : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
_cited as the source of values for this phase_

## MG6PU (Mg–Pu)

- Id: `phase:mg-pu:mg6pu`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.8571, Pu 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–709.95 K, x(Pu) 0.14286–0.14286
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:mg6pu)

Names (3): _corpus: _corpus:phase:mg-pu:mg6pu  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:Mg6Pu  
_tdb: _tdb:MgPu-09Wan.tdb:MG6PU  


### TDB models of MG6PU (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): MG6PU, type code %, sha256 `43f00c0b4df80622…`

~~~~text
64: PHASE MG6PU % 2 6 1 !
65: CONST MG6PU : MG : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
_cited as the source of values for this phase_

## ALPHA_PU (Mg–Pu)

- Id: `phase:mg-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — MgPu-09Wan.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 0.99998–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:pu-alpha)

Names (2): _corpus: _corpus:phase:mg-pu:pu-alpha  
_tdb: _tdb:MgPu-09Wan.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): ALPHA_PU, type code %, sha256 `43f00c0b4df80622…`

~~~~text
49: PHASE ALPHA_PU % 1 1 !
50: CONST ALPHA_PU : MG PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase_

## BETA_PU (Mg–Pu)

- Id: `phase:mg-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — MgPu-09Wan.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stability: stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:pu-beta)

Names (2): _corpus: _corpus:phase:mg-pu:pu-beta  
_tdb: _tdb:MgPu-09Wan.tdb:BETA_PU  


### TDB models of BETA_PU (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): BETA_PU, type code %, sha256 `43f00c0b4df80622…`

~~~~text
54: PHASE BETA_PU % 1 1 !
55: CONST BETA_PU : MG PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase_

## GAMMA_PU (Mg–Pu)

- Id: `phase:mg-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): gamma-Pu · oF8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — MgPu-09Wan.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stability: stable in 1 of 1 calculated diagram(s): 487.9–728.06 K, x(Pu) 0.99999–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pu:pu-gamma)

Names (4): _corpus: _corpus:phase:mg-pu:pu-gamma, corpus:phase:mg-pu:gamma-pu  
_paper: _paper:10.1016/j.jnucmat.2009.04.017:γPu  
_tdb: _tdb:MgPu-09Wan.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (1): PHASE and CONSTITUENT statements as written

[MgPu-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPu-09Wan.tdb): GAMMA_PU, type code %, sha256 `43f00c0b4df80622…`

~~~~text
59: PHASE GAMMA_PU % 1 1 !
60: CONST GAMMA_PU : MG PU% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2009.04.017](https://doi.org/10.1016/j.jnucmat.2009.04.017) C.P. Wang, W. Fang, Z.S. Li, X.J. Liu, Thermodynamic modeling of the Mg–Pu and Cu–Pu systems, Journal of Nuclear Materials 392, 525-530 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90474-1](https://doi.org/10.1016/0022-3115%2889%2990474-1) K.M. Axler, E.M. Foltyn, D.E. Peterson, R.I. Sheldon, W.B. Hutchinson, The plutonium-magnesium system, Journal of Nuclear Materials 161, 132-139 (1989).  
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
