# Al–Ho phases

> Al–Ho system: 9 phases (tier A 5, tier B 1, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-HO.html · Markdown: https://data.orchid-project.org/phases/pages/AL-HO.md

9 phases (tier A 5, tier B 1, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-HO) · [full JSON](https://data.orchid-project.org/phases/systems/AL-HO.json) · [Al–Ho system page](https://data.orchid-project.org/systems/AL-HO.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-HO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Ho system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2HO3](#phase-al-ho-al2ho3); _phase:al-ho:al2ho3_ | Al2Gd3 · tP20 · P4_2nm (102) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1294.89 K, x(Ho) 0.6–0.6 | 0 | 2 |
| [AL3HO](#phase-al-ho-al3ho); _phase:al-ho:al3ho_ | Al3Ho · hR20 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1365.56 K, x(Ho) 0.25–0.25 | 0 | 2 |
| [ALHO](#phase-al-ho-alho); _phase:al-ho:alho_ | AlDy · oP16 · Pbcm (57) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–1396.15 K, x(Ho) 0.5–0.5 | 0 | 2 |
| [ALHO2_C37](#phase-al-ho-alho2-c37); _phase:al-ho:alho2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1301.15 K, x(Ho) 0.66667–0.66667 | 0 | 2 |
| [BCC_A2](#phase-al-ho-bcc-a2); _phase:al-ho:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [C15_LAVES](#phase-al-ho-c15-laves); _phase:al-ho:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1801.83 K, x(Ho) 0.32173–0.35505 | 0 | 2 |
| [FCC_A1](#phase-al-ho-fcc-a1); _phase:al-ho:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–937.78 K, x(Ho) 0–0 | 0 | 2 |
| [HCP_A3](#phase-al-ho-hcp-a3); _phase:al-ho:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.8 K, x(Ho) 0.99602–1 | 0 | 2 |
| [LIQUID](#phase-al-ho-liquid); _phase:al-ho:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 902.16–2500 K, x(Ho) 0–1 | 0 | 2 |

## AL2HO3 (Al–Ho)

- Id: `phase:al-ho:al2ho3`; status `assigned`
- Structure: Al2Gd3 · tP20 · P4_2nm (102); type `st:al2gd3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Ho 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1294.89 K, x(Ho) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:al2ho3)

Names (3): _corpus: _corpus:phase:al-ho:al2ho3  
_tdb: _tdb:AlHo-03Cac-LB.tdb:AL2HO3, tdb:AlHo-13Tok.tdb:AL2HO3  


### TDB models of AL2HO3 (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): AL2HO3, type code %, sha256 `1af1b05d2b3627b3…`

~~~~text
61: PHASE AL2HO3 % 2 2 3 !
62: CONST AL2HO3 : AL : HO : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): AL2HO3, type code %, sha256 `c966c95b19c63dec…`

~~~~text
61: PHASE AL2HO3 % 2 2 3 !
62: CONST AL2HO3 : AL : HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## AL3HO (Al–Ho)

- Id: `phase:al-ho:al3ho`; status `assigned`
- Structure: Al3Ho · hR20 · R-3m (166); type `st:al3ho-hr20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_0_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.7500, Ho 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1365.56 K, x(Ho) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:al3ho)

Names (3): _corpus: _corpus:phase:al-ho:al3ho  
_tdb: _tdb:AlHo-03Cac-LB.tdb:AL3HO, tdb:AlHo-13Tok.tdb:AL3HO  


### TDB models of AL3HO (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): AL3HO, type code %, sha256 `1af1b05d2b3627b3…`

~~~~text
46: PHASE AL3HO % 2 3 1 !
47: CONST AL3HO : AL : HO : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): AL3HO, type code %, sha256 `c966c95b19c63dec…`

~~~~text
46: PHASE AL3HO % 2 3 1 !
47: CONST AL3HO : AL : HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## ALHO (Al–Ho)

- Id: `phase:al-ho:alho`; status `assigned`
- Structure: AlDy · oP16 · Pbcm (57); type `st:aldy-op16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.5000, Ho 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1396.15 K, x(Ho) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:alho)

Names (5): _corpus: _corpus:phase:al-ho:alho  
_mp: _mp:mp-aaacpqam  
_oqmd: _oqmd:oqmd-690043  
_tdb: _tdb:AlHo-03Cac-LB.tdb:ALHO, tdb:AlHo-13Tok.tdb:ALHO  


### TDB models of ALHO (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): ALHO, type code %, sha256 `1af1b05d2b3627b3…`

~~~~text
56: PHASE ALHO % 2 1 1 !
57: CONST ALHO : AL : HO : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): ALHO, type code %, sha256 `c966c95b19c63dec…`

~~~~text
56: PHASE ALHO % 2 1 1 !
57: CONST ALHO : AL : HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## ALHO2_C37 (Al–Ho)

- Id: `phase:al-ho:alho2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaayks and oqmd-10475, space group 62
- Stoichiometry: Al 0.3333, Ho 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1301.15 K, x(Ho) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:alho2-c37)

Names (5): _corpus: _corpus:phase:al-ho:alho2-c37  
_mp: _mp:mp-aaaaayks  
_oqmd: _oqmd:oqmd-10475  
_tdb: _tdb:AlHo-03Cac-LB.tdb:ALHO2_C37, tdb:AlHo-13Tok.tdb:ALHO2_C37  


### TDB models of ALHO2_C37 (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): ALHO2_C37, type code %, sha256 `1af1b05d2b3627b3…`

~~~~text
66: PHASE ALHO2_C37 % 2 1 2 !
67: CONST ALHO2_C37 : AL : HO : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): ALHO2_C37, type code %, sha256 `c966c95b19c63dec…`

~~~~text
66: PHASE ALHO2_C37 % 2 1 2 !
67: CONST ALHO2_C37 : AL : HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## BCC_A2 (Al–Ho)

- Id: `phase:al-ho:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:bcc-a2)

Names (3): _corpus: _corpus:phase:al-ho:bcc-a2  
_tdb: _tdb:AlHo-03Cac-LB.tdb:BCC_A2, tdb:AlHo-13Tok.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): BCC_A2, type code %B, sha256 `1af1b05d2b3627b3…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL HO : VA : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): BCC_A2, type code %B, sha256 `c966c95b19c63dec…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL HO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## C15_LAVES (Al–Ho)

- Id: `phase:al-ho:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlHo-03Cac-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlHo-13Tok.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1801.83 K, x(Ho) 0.32173–0.35505
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:c15-laves)

Names (3): _corpus: _corpus:phase:al-ho:c15-laves  
_tdb: _tdb:AlHo-03Cac-LB.tdb:C15_LAVES, tdb:AlHo-13Tok.tdb:C15_LAVES  


### TDB models of C15_LAVES (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): C15_LAVES, type code %, sha256 `1af1b05d2b3627b3…`

~~~~text
51: PHASE C15_LAVES % 2 2 1 !
52: CONST C15_LAVES : AL% HO : AL HO% : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): C15_LAVES, type code %, sha256 `c966c95b19c63dec…`

~~~~text
51: PHASE C15_LAVES % 2 2 1 !
52: CONST C15_LAVES : AL% HO : AL HO% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## FCC_A1 (Al–Ho)

- Id: `phase:al-ho:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–937.78 K, x(Ho) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:fcc-a1)

Names (3): _corpus: _corpus:phase:al-ho:fcc-a1  
_tdb: _tdb:AlHo-03Cac-LB.tdb:FCC_A1, tdb:AlHo-13Tok.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): FCC_A1, type code %A, sha256 `1af1b05d2b3627b3…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% HO : VA : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): FCC_A1, type code %A, sha256 `c966c95b19c63dec…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% HO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## HCP_A3 (Al–Ho)

- Id: `phase:al-ho:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.8 K, x(Ho) 0.99602–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:hcp-a3)

Names (3): _corpus: _corpus:phase:al-ho:hcp-a3  
_tdb: _tdb:AlHo-03Cac-LB.tdb:HCP_A3, tdb:AlHo-13Tok.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): HCP_A3, type code %A, sha256 `1af1b05d2b3627b3…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL HO% : VA : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): HCP_A3, type code %A, sha256 `c966c95b19c63dec…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL HO% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## LIQUID (Al–Ho)

- Id: `phase:al-ho:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 902.16–2500 K, x(Ho) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ho:liquid)

Names (3): _corpus: _corpus:phase:al-ho:liquid  
_tdb: _tdb:AlHo-03Cac-LB.tdb:LIQUID, tdb:AlHo-13Tok.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AlHo-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-03Cac-LB.tdb): LIQUID, type code %, sha256 `1af1b05d2b3627b3…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL HO : !
~~~~

[AlHo-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHo-13Tok.tdb): LIQUID, type code %, sha256 `c966c95b19c63dec…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

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
