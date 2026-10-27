# Ag–Pu phases

> Ag–Pu system: 10 phases (tier A 4, tier C 1, liquid 1, needs_review 4); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-PU.html · Markdown: https://data.orchid-project.org/phases/pages/AG-PU.md

10 phases (tier A 4, tier C 1, liquid 1, needs_review 4); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-PU) · [full JSON](https://data.orchid-project.org/phases/systems/AG-PU.json) · [Ag–Pu system page](https://data.orchid-project.org/systems/AG-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Pu system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-ag-pu-a6-tetragonal); _phase:ag-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 611.42–910.67 K, x(Pu) 1–1 | 4 | 1 |
| [AG2PU](#phase-ag-pu-ag2pu); _phase:ag-pu:ag2pu_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1092.7 K, x(Pu) 0.33333–0.33333 | 17 | 1 |
| [AG51PU14](#phase-ag-pu-ag51pu14); _phase:ag-pu:ag51pu14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1250 K, x(Pu) 0.21538–0.21538 | 7 | 1 |
| [BCC_A2](#phase-ag-pu-bcc-a2); _phase:ag-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 755.67–3999.25 K, x(Pu) 0.42–1 | 4 | 1 |
| [FCC_A1](#phase-ag-pu-fcc-a1); _phase:ag-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1266.15 K, x(Pu) 0–1 | 4 | 1 |
| [HCP_A3](#phase-ag-pu-hcp-a3); _phase:ag-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-pu-liquid); _phase:ag-pu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 909.75–4000 K, x(Pu) 0–1 | 10 | 1 |
| [ALPHA_PU](#phase-ag-pu-pu-alpha); _phase:ag-pu:pu-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1 | 2 | 1 |
| [BETA_PU](#phase-ag-pu-pu-beta); _phase:ag-pu:pu-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1 | 4 | 1 |
| [GAMMA_PU](#phase-ag-pu-pu-gamma); _phase:ag-pu:pu-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 487.9–608.06 K, x(Pu) 1–1 | 4 | 1 |

## TETRAGONAL_A6 (Ag–Pu)

- Id: `phase:ag-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 611.42–910.67 K, x(Pu) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:a6-tetragonal)

Names (4): _corpus: _corpus:phase:ag-pu:a6-tetragonal, corpus:phase:ag-pu:tetragonal-a6  
_paper: _paper:10.1007/s11669-020-00813-5:(δ'Pu)  
_tdb: _tdb:AgPu-20Zho.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): TETRAGONAL_A6, type code %, sha256 `3a0aa8760514e86a…`

~~~~text
55: PHASE TETRAGONAL_A6 % 1 1 !
56: CONST TETRAGONAL_A6 : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## AG2PU (Ag–Pu)

- Id: `phase:ag-pu:ag2pu`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Ag2Pu) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ag2Pu) — Hallstedt 2025 mmc2 row for AG2PU: Ag2Pu
- Stoichiometry: Ag 0.6667, Pu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1092.7 K, x(Pu) 0.33333–0.33333
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:ag2pu)

Names (3): _corpus: _corpus:phase:ag-pu:ag2pu  
_paper: _paper:10.1007/s11669-020-00813-5:Ag2Pu  
_tdb: _tdb:AgPu-20Zho.tdb:AG2PU  


### TDB models of AG2PU (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): AG2PU, type code %, sha256 `3a0aa8760514e86a…`

~~~~text
80: PHASE AG2PU % 2 2 1 !
81: CONST AG2PU : AG : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## AG51PU14 (Ag–Pu)

- Id: `phase:ag-pu:ag51pu14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.7846, Pu 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–1250 K, x(Pu) 0.21538–0.21538
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:ag51pu14)

Names (3): _corpus: _corpus:phase:ag-pu:ag51pu14  
_paper: _paper:10.1007/s11669-020-00813-5:Ag51Pu14  
_tdb: _tdb:AgPu-20Zho.tdb:AG51PU14  


### TDB models of AG51PU14 (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): AG51PU14, type code %, sha256 `3a0aa8760514e86a…`

~~~~text
75: PHASE AG51PU14 % 2 51 14 !
76: CONST AG51PU14 : AG : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Pu)

- Id: `phase:ag-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 755.67–3999.25 K, x(Pu) 0.42–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-pu:bcc-a2  
_paper: _paper:10.1007/s11669-020-00813-5:(εPu)  
_tdb: _tdb:AgPu-20Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): BCC_A2, type code %B, sha256 `3a0aa8760514e86a…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : AG PU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Pu)

- Id: `phase:ag-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1266.15 K, x(Pu) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-pu:fcc-a1  
_paper: _paper:10.1007/s11669-020-00813-5:(Ag), paper:10.1007/s11669-020-00813-5:(δPu)  
_tdb: _tdb:AgPu-20Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): FCC_A1, type code %A, sha256 `3a0aa8760514e86a…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : AG% PU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Pu)

- Id: `phase:ag-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-pu:hcp-a3  
_tdb: _tdb:AgPu-20Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): HCP_A3, type code %A, sha256 `3a0aa8760514e86a…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : AG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase_

## LIQUID (Ag–Pu)

- Id: `phase:ag-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 909.75–4000 K, x(Pu) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:liquid)

Names (4): _corpus: _corpus:phase:ag-pu:liquid  
_paper: _paper:10.1007/s11669-020-00813-5:Liquid#1, paper:10.1007/s11669-020-00813-5:Liquid#2  
_tdb: _tdb:AgPu-20Zho.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): LIQUID, type code %, sha256 `3a0aa8760514e86a…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : AG PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## ALPHA_PU (Ag–Pu)

- Id: `phase:ag-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): alpha-Pu · mP16 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — AgPu-20Zho.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:pu-alpha)

Names (4): _corpus: _corpus:phase:ag-pu:pu-alpha, corpus:phase:ag-pu:alpha-pu  
_paper: _paper:10.1007/s11669-020-00813-5:(αPu)  
_tdb: _tdb:AgPu-20Zho.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): ALPHA_PU, type code %, sha256 `3a0aa8760514e86a…`

~~~~text
60: PHASE ALPHA_PU % 1 1 !
61: CONST ALPHA_PU : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## BETA_PU (Ag–Pu)

- Id: `phase:ag-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): beta-Pu · mC34 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — AgPu-20Zho.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:pu-beta)

Names (4): _corpus: _corpus:phase:ag-pu:pu-beta, corpus:phase:ag-pu:beta-pu  
_paper: _paper:10.1007/s11669-020-00813-5:(βPu)  
_tdb: _tdb:AgPu-20Zho.tdb:BETA_PU  


### TDB models of BETA_PU (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): BETA_PU, type code %, sha256 `3a0aa8760514e86a…`

~~~~text
65: PHASE BETA_PU % 1 1 !
66: CONST BETA_PU : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## GAMMA_PU (Ag–Pu)

- Id: `phase:ag-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): gamma-Pu · oF8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — AgPu-20Zho.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 487.9–608.06 K, x(Pu) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-pu:pu-gamma)

Names (3): _corpus: _corpus:phase:ag-pu:pu-gamma  
_paper: _paper:10.1007/s11669-020-00813-5:(γPu)  
_tdb: _tdb:AgPu-20Zho.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (1): PHASE and CONSTITUENT statements as written

[AgPu-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb): GAMMA_PU, type code %, sha256 `3a0aa8760514e86a…`

~~~~text
70: PHASE GAMMA_PU % 1 1 !
71: CONST GAMMA_PU : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2172/4104255](https://doi.org/10.2172/4104255) California Univ., Livermore. Lawrence Radiation Lab., D Wood, E Cramer, P Wallace, INVESTIGATION OF THE PLUTONIUM--SILVER SYSTEM., (1970).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
