# Al–Dy phases

> Al–Dy system: 10 phases (tier A 6, tier B 1, tier C 2, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-DY.html · Markdown: https://data.orchid-project.org/phases/pages/AL-DY.md

10 phases (tier A 6, tier B 1, tier C 2, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-DY) · [full JSON](https://data.orchid-project.org/phases/systems/AL-DY.json) · [Al–Dy system page](https://data.orchid-project.org/systems/AL-DY.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-DY.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Dy system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2DY3](#phase-al-dy-al2dy3); _phase:al-dy:al2dy3_ | Al2Zr3 · tP20 · P4_2/mnm (136) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1303.92 K, x(Dy) 0.6–0.6 | 0 | 3 |
| [AL3DY_HT](#phase-al-dy-al3dy); _phase:al-dy:al3dy_ | Al3Ho · hR20 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 1070.13–1364.85 K, x(Dy) 0.25–0.25 | 0 | 3 |
| [AL3DY_D024](#phase-al-dy-al3dy-d024); _phase:al-dy:al3dy-d024_ | Ni3Ti · D0_24 · hP16 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1281.23 K, x(Dy) 0.25–0.25 | 0 | 3 |
| [ALDY](#phase-al-dy-aldy); _phase:al-dy:aldy_ | AlDy · oP16 · Pbcm (57) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–1396.2 K, x(Dy) 0.5–0.5 | 0 | 3 |
| [ALDY2_C37](#phase-al-dy-aldy2-c37); _phase:al-dy:aldy2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1262.9 K, x(Dy) 0.66667–0.66667 | 0 | 3 |
| [BCC_A2](#phase-al-dy-bcc-a2); _phase:al-dy:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1571.14–2335.11 K, x(Dy) 0.9827–1 | 0 | 3 |
| [C15_LAVES](#phase-al-dy-c15-laves); _phase:al-dy:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1774.34 K, x(Dy) 0.31807–0.40658 | 0 | 3 |
| [FCC_A1](#phase-al-dy-fcc-a1); _phase:al-dy:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–941.28 K, x(Dy) 0–0 | 0 | 3 |
| [HCP_A3](#phase-al-dy-hcp-a3); _phase:al-dy:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1679.11 K, x(Dy) 0.99858–1 | 0 | 3 |
| [LIQUID](#phase-al-dy-liquid); _phase:al-dy:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 902.68–2500 K, x(Dy) 0–1 | 0 | 3 |

## AL2DY3 (Al–Dy)

- Id: `phase:al-dy:al2dy3`; status `assigned`
- Structure: Al2Zr3 · tP20 · P4_2/mnm (136); type `st:al2zr3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Dy 0.6000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1303.92 K, x(Dy) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:al2dy3)

Names (4): _corpus: _corpus:phase:al-dy:al2dy3  
_tdb: _tdb:AlDy-03Cac-LB.tdb:AL2DY3, tdb:AlDy-14Bo.tdb:AL2DY3, tdb:AlDy-24Ma.tdb:AL2DY3  


### TDB models of AL2DY3 (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): AL2DY3, type code %, sha256 `fd5853d7b91ea722…`

~~~~text
63: PHASE AL2DY3 % 2 2 3 !
64: CONST AL2DY3 : AL : DY : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): AL2DY3, type code %, sha256 `839b27402dd36c7a…`

~~~~text
65: PHASE AL2DY3 % 2 2 3 !
66: CONST AL2DY3 : AL : DY : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): AL2DY3, type code %, sha256 `b49a8c269df92a80…`

~~~~text
65: PHASE AL2DY3 % 2 2 3 !
66: CONST AL2DY3 : AL : DY : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## AL3DY_HT (Al–Dy)

- Id: `phase:al-dy:al3dy`; status `assigned`
- Structure: Al3Ho · hR20 · R-3m (166); type `st:al3ho-hr20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.7500, Dy 0.2500
- Stability: stable in 3 of 3 calculated diagram(s): 1070.13–1364.85 K, x(Dy) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:al3dy)

Names (4): _corpus: _corpus:phase:al-dy:al3dy  
_tdb: _tdb:AlDy-03Cac-LB.tdb:AL3DY_HT, tdb:AlDy-14Bo.tdb:AL3DY_HT, tdb:AlDy-24Ma.tdb:AL3DY_HT  


### TDB models of AL3DY_HT (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): AL3DY_HT, type code %, sha256 `fd5853d7b91ea722…`

~~~~text
48: PHASE AL3DY_HT % 2 3 1 !
49: CONST AL3DY_HT : AL : DY : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): AL3DY_HT, type code %, sha256 `839b27402dd36c7a…`

~~~~text
50: PHASE AL3DY_HT % 2 3 1 !
51: CONST AL3DY_HT : AL : DY : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): AL3DY_HT, type code %, sha256 `b49a8c269df92a80…`

~~~~text
50: PHASE AL3DY_HT % 2 3 1 !
51: CONST AL3DY_HT : AL : DY : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## AL3DY_D024 (Al–Dy)

- Id: `phase:al-dy:al3dy-d024`; status `assigned`
- Structure: Ni3Ti · D0_24 · hP16 · P6_3/mmc (194); type `st:d0-24-ni3ti-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.7500, Dy 0.2500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1281.23 K, x(Dy) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:al3dy-d024)

Names (4): _corpus: _corpus:phase:al-dy:al3dy-d024  
_tdb: _tdb:AlDy-03Cac-LB.tdb:AL3DY_D024, tdb:AlDy-14Bo.tdb:AL3DY_D024, tdb:AlDy-24Ma.tdb:AL3DY_D024  


### TDB models of AL3DY_D024 (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): AL3DY_D024, type code %, sha256 `fd5853d7b91ea722…`

~~~~text
43: PHASE AL3DY_D024 % 2 3 1 !
44: CONST AL3DY_D024 : AL : DY : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): AL3DY_D024, type code %, sha256 `839b27402dd36c7a…`

~~~~text
45: PHASE AL3DY_D024 % 2 3 1 !
46: CONST AL3DY_D024 : AL : DY : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): AL3DY_D024, type code %, sha256 `b49a8c269df92a80…`

~~~~text
45: PHASE AL3DY_D024 % 2 3 1 !
46: CONST AL3DY_D024 : AL : DY : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## ALDY (Al–Dy)

- Id: `phase:al-dy:aldy`; status `assigned`
- Structure: AlDy · oP16 · Pbcm (57); type `st:aldy-op16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.5000, Dy 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1396.2 K, x(Dy) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:aldy)

Names (6): _corpus: _corpus:phase:al-dy:aldy  
_mp: _mp:mp-aaaaaaqr  
_oqmd: _oqmd:oqmd-10444  
_tdb: _tdb:AlDy-03Cac-LB.tdb:ALDY, tdb:AlDy-14Bo.tdb:ALDY, tdb:AlDy-24Ma.tdb:ALDY  


### TDB models of ALDY (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): ALDY, type code %, sha256 `fd5853d7b91ea722…`

~~~~text
58: PHASE ALDY % 2 1 1 !
59: CONST ALDY : AL : DY : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): ALDY, type code %, sha256 `839b27402dd36c7a…`

~~~~text
60: PHASE ALDY % 2 1 1 !
61: CONST ALDY : AL : DY : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): ALDY, type code %, sha256 `b49a8c269df92a80…`

~~~~text
60: PHASE ALDY % 2 1 1 !
61: CONST ALDY : AL : DY : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## ALDY2_C37 (Al–Dy)

- Id: `phase:al-dy:aldy2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacktgq and oqmd-1520772, space group 62
- Stoichiometry: Al 0.3333, Dy 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1262.9 K, x(Dy) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:aldy2-c37)

Names (6): _corpus: _corpus:phase:al-dy:aldy2-c37  
_mp: _mp:mp-aaacktgq  
_oqmd: _oqmd:oqmd-1520772  
_tdb: _tdb:AlDy-03Cac-LB.tdb:ALDY2_C37, tdb:AlDy-14Bo.tdb:ALDY2_C37, tdb:AlDy-24Ma.tdb:ALDY2_C37  


### TDB models of ALDY2_C37 (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): ALDY2_C37, type code %, sha256 `fd5853d7b91ea722…`

~~~~text
68: PHASE ALDY2_C37 % 2 1 2 !
69: CONST ALDY2_C37 : AL : DY : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): ALDY2_C37, type code %, sha256 `839b27402dd36c7a…`

~~~~text
70: PHASE ALDY2_C37 % 2 1 2 !
71: CONST ALDY2_C37 : AL : DY : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): ALDY2_C37, type code %, sha256 `b49a8c269df92a80…`

~~~~text
70: PHASE ALDY2_C37 % 2 1 2 !
71: CONST ALDY2_C37 : AL : DY : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## BCC_A2 (Al–Dy)

- Id: `phase:al-dy:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1571.14–2335.11 K, x(Dy) 0.9827–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:bcc-a2)

Names (4): _corpus: _corpus:phase:al-dy:bcc-a2  
_tdb: _tdb:AlDy-03Cac-LB.tdb:BCC_A2, tdb:AlDy-14Bo.tdb:BCC_A2, tdb:AlDy-24Ma.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): BCC_A2, type code %B, sha256 `fd5853d7b91ea722…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL DY% : VA : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): BCC_A2, type code %B, sha256 `839b27402dd36c7a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL DY% : VA : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): BCC_A2, type code %B, sha256 `b49a8c269df92a80…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL DY% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## C15_LAVES (Al–Dy)

- Id: `phase:al-dy:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlDy-03Cac-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlDy-14Bo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlDy-24Ma.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1774.34 K, x(Dy) 0.31807–0.40658
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:c15-laves)

Names (4): _corpus: _corpus:phase:al-dy:c15-laves  
_tdb: _tdb:AlDy-03Cac-LB.tdb:C15_LAVES, tdb:AlDy-14Bo.tdb:C15_LAVES, tdb:AlDy-24Ma.tdb:C15_LAVES  


### TDB models of C15_LAVES (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): C15_LAVES, type code %, sha256 `fd5853d7b91ea722…`

~~~~text
53: PHASE C15_LAVES % 2 2 1 !
54: CONST C15_LAVES : AL% DY : AL DY% : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): C15_LAVES, type code %, sha256 `839b27402dd36c7a…`

~~~~text
55: PHASE C15_LAVES % 2 2 1 !
56: CONST C15_LAVES : AL% DY : AL DY% : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): C15_LAVES, type code %, sha256 `b49a8c269df92a80…`

~~~~text
55: PHASE C15_LAVES % 2 2 1 !
56: CONST C15_LAVES : AL% DY : AL DY% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## FCC_A1 (Al–Dy)

- Id: `phase:al-dy:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–941.28 K, x(Dy) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:fcc-a1)

Names (4): _corpus: _corpus:phase:al-dy:fcc-a1  
_tdb: _tdb:AlDy-03Cac-LB.tdb:FCC_A1, tdb:AlDy-14Bo.tdb:FCC_A1, tdb:AlDy-24Ma.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): FCC_A1, type code %A, sha256 `fd5853d7b91ea722…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL% DY : VA : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): FCC_A1, type code %A, sha256 `839b27402dd36c7a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% DY : VA : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): FCC_A1, type code %A, sha256 `b49a8c269df92a80…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% DY : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## HCP_A3 (Al–Dy)

- Id: `phase:al-dy:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1679.11 K, x(Dy) 0.99858–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:hcp-a3)

Names (4): _corpus: _corpus:phase:al-dy:hcp-a3  
_tdb: _tdb:AlDy-03Cac-LB.tdb:HCP_A3, tdb:AlDy-14Bo.tdb:HCP_A3, tdb:AlDy-24Ma.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): HCP_A3, type code %A, sha256 `fd5853d7b91ea722…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL DY% : VA : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): HCP_A3, type code %A, sha256 `839b27402dd36c7a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL DY% : VA : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): HCP_A3, type code %A, sha256 `b49a8c269df92a80…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL DY% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## LIQUID (Al–Dy)

- Id: `phase:al-dy:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 902.68–2500 K, x(Dy) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-dy:liquid)

Names (4): _corpus: _corpus:phase:al-dy:liquid  
_tdb: _tdb:AlDy-03Cac-LB.tdb:LIQUID, tdb:AlDy-14Bo.tdb:LIQUID, tdb:AlDy-24Ma.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlDy-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-03Cac-LB.tdb): LIQUID, type code %, sha256 `fd5853d7b91ea722…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL DY : !
~~~~

[AlDy-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-14Bo.tdb): LIQUID, type code %, sha256 `839b27402dd36c7a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL DY : !
~~~~

[AlDy-24Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/AlDy-24Ma.tdb): LIQUID, type code %, sha256 `b49a8c269df92a80…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL DY : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11434-014-0192-y](https://doi.org/10.1007/s11434-014-0192-y) H. Bo, L. Liu, X. Xiong, Z. Jin, Chin. Sci. Bull., 59, 1738-46(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102681](https://doi.org/10.1016/j.calphad.2024.102681) D. Ma, Y.T. Guo, Z. Li, J. Hu, F. Yin, Y. Liu, Y. Liu, Calphad, 85, 102681(2024).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
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
