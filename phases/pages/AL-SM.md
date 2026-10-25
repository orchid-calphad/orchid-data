# Al–Sm phases

> Al–Sm system: 13 phases (tier A 9, tier C 2, liquid 1, needs_review 1); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-SM.html · Markdown: https://data.orchid-project.org/phases/pages/AL-SM.md

13 phases (tier A 9, tier C 2, liquid 1, needs_review 1); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-SM) · [full JSON](https://data.orchid-project.org/phases/systems/AL-SM.json) · [Al–Sm system page](https://data.orchid-project.org/systems/AL-SM.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-SM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Sm system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL11SM3_LT](#phase-al-sm-al11sm3); _phase:al-sm:al11sm3_ | Al11La3 · oI28 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 3 calculated diagram(s): 300–1346.78 K, x(Sm) 0.21429–0.21429 | 6 | 3 |
| [AL11SM3_D13](#phase-al-sm-al11sm3-d13); _phase:al-sm:al11sm3-d13_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1337.85–1653.03 K, x(Sm) 0.21429–0.21429 | 0 | 2 |
| [AL2SM_C15](#phase-al-sm-al2sm-c15); _phase:al-sm:al2sm-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1758 K, x(Sm) 0.33333–0.33333 | 14 | 3 |
| [AL3SM_D019](#phase-al-sm-al3sm-d019); _phase:al-sm:al3sm-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1408.51 K, x(Sm) 0.25–0.25 | 0 | 3 |
| [AL4SM_D13](#phase-al-sm-al4sm-d13); _phase:al-sm:al4sm-d13_ | Al4Ba · D1_3 · tI10 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1330–1654.47 K, x(Sm) 0.2–0.2 | 0 | 1 |
| [AL4SM_D1B](#phase-al-sm-al4sm-d1b); _phase:al-sm:al4sm-d1b_ | Al4U · D1_b · oI20 · Imma (74) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 3 | 1 |
| [ALSM](#phase-al-sm-alsm); _phase:al-sm:alsm_ | AlDy · oP16 · Pbcm (57) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1236.44 K, x(Sm) 0.5–0.5 | 5 | 3 |
| [ALSM2_C37](#phase-al-sm-alsm2-c37); _phase:al-sm:alsm2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1134.93 K, x(Sm) 0.66667–0.66667 | 9 | 3 |
| [BCC_A2](#phase-al-sm-bcc-a2); _phase:al-sm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 973.36–2499.27 K, x(Sm) 0.89027–1 | 7 | 3 |
| [FCC_A1](#phase-al-sm-fcc-a1); _phase:al-sm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–947.78 K, x(Sm) 0–0 | 6 | 3 |
| [HCP_A3](#phase-al-sm-hcp-a3); _phase:al-sm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300.49–1382.31 K, x(Sm) 0.99998–1 | 0 | 3 |
| [LIQUID](#phase-al-sm-liquid); _phase:al-sm:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 893.81–2500 K, x(Sm) 0–1 | 37 | 3 |
| [RHOMB_C19](#phase-al-sm-rhomb-c19); _phase:al-sm:rhomb-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1187.99 K, x(Sm) 0.96244–1 | 3 | 3 |

## AL11SM3_LT (Al–Sm)

- Id: `phase:al-sm:al11sm3`; status `assigned`
- Structure: Al11La3 · oI28 · Immm (71); type `st:al11la3-oi28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.7857, Sm 0.2143
- Stability: stable in 2 of 3 calculated diagram(s): 300–1346.78 K, x(Sm) 0.21429–0.21429
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:al11sm3)

Names (5): _corpus: _corpus:phase:al-sm:al11sm3  
_paper: _paper:10.1007/s11661-007-9445-6:α  
_tdb: _tdb:AlSm-08Jia.tdb:AL11SM3_LT, tdb:AlSm-08Zho.tdb:AL11SM3, tdb:AlSm-98Sac.tdb:AL11SM3_LT  


### TDB models of AL11SM3_LT (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): AL11SM3_LT, type code %, sha256 `b393d63733d46908…`

~~~~text
55: PHASE AL11SM3_LT % 2 11 3 !
56: CONST AL11SM3_LT : AL : SM : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): AL11SM3, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
61: PHASE AL11SM3 % 2 11 3 !
62: CONST AL11SM3 : AL : SM : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): AL11SM3_LT, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
53: PHASE AL11SM3_LT % 2 11 3 !
54: CONST AL11SM3_LT : AL : SM : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_
- [doi:10.1016/0167-577x(95)00066-6](https://doi.org/10.1016/0167-577x%2895%2900066-6) J.Q. Guo, K. Ohtera, K. Kita, J. Nagahora, N.S. Kazama, Crystallization behavior of Al100 − xSmx (x = 8–14 at%) amorphous alloys, Materials Letters 24, 133-138 (1995).  
_cited as the source of values for this phase_

## AL11SM3_D13 (Al–Sm)

- Id: `phase:al-sm:al11sm3-d13`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D1_3; stoichiometry_contradicts_D1_3:AlSm-08Jia.tdb; stoichiometry_contradicts_D1_3:AlSm-98Sac.tdb
- Candidate (name_token): Al4Ba · D1_3 · tI10 · I4/mmm (139) — Strukturbericht/word 'D13' in the TDB name
- Candidate (sgte_mmc2): Al4Ba · D1_3 · tI10 · I4/mmm (139) — Hallstedt 2025 mmc2 row for AL11SM3_D13: Al11Sm3
- Candidate (tdb_comment): Al4Ba · tI10 · I4/mmm — AlSm-08Jia.tdb: 'Prototype Al4Ba (tI10, I4/mmm)'
- Candidate (tdb_comment): Al4Ba · tI10 · I4/mmm — AlSm-98Sac.tdb: 'Prototype Al4Ba (tI10, I4/mmm)'
- Stoichiometry: Al 0.7857, Sm 0.2143
- Stability: stable in 2 of 2 calculated diagram(s): 1337.85–1653.03 K, x(Sm) 0.21429–0.21429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:al11sm3-d13)

Names (3): _corpus: _corpus:phase:al-sm:al11sm3-d13  
_tdb: _tdb:AlSm-08Jia.tdb:AL11SM3_D13, tdb:AlSm-98Sac.tdb:AL11SM3_D13  


### TDB models of AL11SM3_D13 (2): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): AL11SM3_D13, type code %, sha256 `b393d63733d46908…`

~~~~text
60: PHASE AL11SM3_D13 % 2 11 3 !
61: CONST AL11SM3_D13 : AL : SM : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): AL11SM3_D13, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
58: PHASE AL11SM3_D13 % 2 11 3 !
59: CONST AL11SM3_D13 : AL : SM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase_

## AL2SM_C15 (Al–Sm)

- Id: `phase:al-sm:al2sm-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadms and oqmd-10582, space group 227
- Stoichiometry: Al 0.6667, Sm 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1758 K, x(Sm) 0.33333–0.33333
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:al2sm-c15)

Names (7): _corpus: _corpus:phase:al-sm:al2sm-c15  
_mp: _mp:mp-aaaaadms  
_oqmd: _oqmd:oqmd-10582  
_paper: _paper:10.1007/s11661-007-9445-6:σ  
_tdb: _tdb:AlSm-08Jia.tdb:AL2SM_C15, tdb:AlSm-08Zho.tdb:AL2SM_C15, tdb:AlSm-98Sac.tdb:AL2SM_C15  


### TDB models of AL2SM_C15 (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): AL2SM_C15, type code %, sha256 `b393d63733d46908…`

~~~~text
70: PHASE AL2SM_C15 % 2 2 1 !
71: CONST AL2SM_C15 : AL : SM : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): AL2SM_C15, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
71: PHASE AL2SM_C15 % 2 2 1 !
72: CONST AL2SM_C15 : AL : SM : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): AL2SM_C15, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
68: PHASE AL2SM_C15 % 2 2 1 !
69: CONST AL2SM_C15 : AL : SM : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(67)90116-6](https://doi.org/10.1016/0022-5088%2867%2990116-6) F Casteels, The aluminium-rich parts of the aluminium-samarium and aluminium-dysprosium systems, Journal of the Less Common Metals 12, 210-220 (1967).  
_cited as the source of values for this phase_

## AL3SM_D019 (Al–Sm)

- Id: `phase:al-sm:al3sm-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabxjvq and oqmd-321863, space group 194
- Stoichiometry: Al 0.7500, Sm 0.2500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1408.51 K, x(Sm) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:al3sm-d019)

Names (6): _corpus: _corpus:phase:al-sm:al3sm-d019  
_mp: _mp:mp-aaabxjvq  
_oqmd: _oqmd:oqmd-321863  
_tdb: _tdb:AlSm-08Jia.tdb:AL3SM_D019, tdb:AlSm-08Zho.tdb:AL3SM_D019, tdb:AlSm-98Sac.tdb:AL3SM_D019  


### TDB models of AL3SM_D019 (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): AL3SM_D019, type code %, sha256 `b393d63733d46908…`

~~~~text
65: PHASE AL3SM_D019 % 2 3 1 !
66: CONST AL3SM_D019 : AL : SM : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): AL3SM_D019, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
66: PHASE AL3SM_D019 % 2 3 1 !
67: CONST AL3SM_D019 : AL : SM : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): AL3SM_D019, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
63: PHASE AL3SM_D019 % 2 3 1 !
64: CONST AL3SM_D019 : AL : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase_

## AL4SM_D13 (Al–Sm)

- Id: `phase:al-sm:al4sm-d13`; status `assigned`
- Structure: Al4Ba · D1_3 · tI10 · I4/mmm (139); type `st:d1-3-al4ba-ti10`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.8000, Sm 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 1330–1654.47 K, x(Sm) 0.2–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:al4sm-d13)

Names (2): _corpus: _corpus:phase:al-sm:al4sm-d13  
_tdb: _tdb:AlSm-08Zho.tdb:AL4SM_D13  


### TDB models of AL4SM_D13 (1): PHASE and CONSTITUENT statements as written

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): AL4SM_D13, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
51: PHASE AL4SM_D13 % 2 4 1 !
52: CONST AL4SM_D13 : AL : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase_

## AL4SM_D1B (Al–Sm)

- Id: `phase:al-sm:al4sm-d1b`; status `assigned`
- Structure: Al4U · D1_b · oI20 · Imma (74); type `st:d1-b-al4u-oi20`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.8000, Sm 0.2000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:al4sm-d1b)

Names (3): _corpus: _corpus:phase:al-sm:al4sm-d1b  
_paper: _paper:10.1007/s11661-007-9445-6:γ  
_tdb: _tdb:AlSm-08Zho.tdb:AL4SM_D1B  


### TDB models of AL4SM_D1B (1): PHASE and CONSTITUENT statements as written

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): AL4SM_D1B, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
56: PHASE AL4SM_D1B % 2 4 1 !
57: CONST AL4SM_D1B : AL : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0167-577x(95)00066-6](https://doi.org/10.1016/0167-577x%2895%2900066-6) J.Q. Guo, K. Ohtera, K. Kita, J. Nagahora, N.S. Kazama, Crystallization behavior of Al100 − xSmx (x = 8–14 at%) amorphous alloys, Materials Letters 24, 133-138 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/s0921-5093(00)01537-9](https://doi.org/10.1016/s0921-5093%2800%2901537-9) P. Rizzi, M. Baricco, S. Borace, L. Battezzati, Phase selection in Al–TM–RE alloys: nanocrystalline Al versus intermetallics, Materials Science and Engineering: A 304-306, 574-578 (2001).  
_cited as the source of values for this phase_

## ALSM (Al–Sm)

- Id: `phase:al-sm:alsm`; status `assigned`
- Structure: AlDy · oP16 · Pbcm (57); type `st:aldy-op16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.5000, Sm 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1236.44 K, x(Sm) 0.5–0.5
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:alsm)

Names (5): _corpus: _corpus:phase:al-sm:alsm  
_paper: _paper:10.1007/s11661-007-9445-6:θ  
_tdb: _tdb:AlSm-08Jia.tdb:ALSM, tdb:AlSm-08Zho.tdb:ALSM, tdb:AlSm-98Sac.tdb:ALSM  


### TDB models of ALSM (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): ALSM, type code %, sha256 `b393d63733d46908…`

~~~~text
75: PHASE ALSM % 2 1 1 !
76: CONST ALSM : AL : SM : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): ALSM, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
76: PHASE ALSM % 2 1 1 !
77: CONST ALSM : AL : SM : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): ALSM, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
73: PHASE ALSM % 2 1 1 !
74: CONST ALSM : AL : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_

## ALSM2_C37 (Al–Sm)

- Id: `phase:al-sm:alsm2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.3333, Sm 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1134.93 K, x(Sm) 0.66667–0.66667
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:alsm2-c37)

Names (5): _corpus: _corpus:phase:al-sm:alsm2-c37  
_paper: _paper:10.1007/s11661-007-9445-6:χ  
_tdb: _tdb:AlSm-08Jia.tdb:ALSM2_C37, tdb:AlSm-08Zho.tdb:ALSM2_C37, tdb:AlSm-98Sac.tdb:ALSM2_C37  


### TDB models of ALSM2_C37 (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): ALSM2_C37, type code %, sha256 `b393d63733d46908…`

~~~~text
80: PHASE ALSM2_C37 % 2 1 2 !
81: CONST ALSM2_C37 : AL : SM : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): ALSM2_C37, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
81: PHASE ALSM2_C37 % 2 1 2 !
82: CONST ALSM2_C37 : AL : SM : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): ALSM2_C37, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
78: PHASE ALSM2_C37 % 2 1 2 !
79: CONST ALSM2_C37 : AL : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_

## BCC_A2 (Al–Sm)

- Id: `phase:al-sm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 973.36–2499.27 K, x(Sm) 0.89027–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:bcc-a2)

Names (5): _corpus: _corpus:phase:al-sm:bcc-a2  
_paper: _paper:10.1007/s11661-007-9445-6:bcc  
_tdb: _tdb:AlSm-08Jia.tdb:BCC_A2, tdb:AlSm-08Zho.tdb:BCC_A2, tdb:AlSm-98Sac.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): BCC_A2, type code %B, sha256 `b393d63733d46908…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : AL SM% : VA : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): BCC_A2, type code %B, sha256 `2da381cdcf96b97e…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AL SM% : VA : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): BCC_A2, type code %B, sha256 `dbfe39f86fc8f00a…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL SM% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_

## FCC_A1 (Al–Sm)

- Id: `phase:al-sm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–947.78 K, x(Sm) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:fcc-a1)

Names (5): _corpus: _corpus:phase:al-sm:fcc-a1  
_paper: _paper:10.1007/s11661-007-9445-6:fcc  
_tdb: _tdb:AlSm-08Jia.tdb:FCC_A1, tdb:AlSm-08Zho.tdb:FCC_A1, tdb:AlSm-98Sac.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): FCC_A1, type code %A, sha256 `b393d63733d46908…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : AL : VA : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): FCC_A1, type code %A, sha256 `2da381cdcf96b97e…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AL% SM : VA : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): FCC_A1, type code %A, sha256 `dbfe39f86fc8f00a…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(67)90116-6](https://doi.org/10.1016/0022-5088%2867%2990116-6) F Casteels, The aluminium-rich parts of the aluminium-samarium and aluminium-dysprosium systems, Journal of the Less Common Metals 12, 210-220 (1967).  
_cited as the source of values for this phase_
- [doi:10.1016/0167-577x(95)00066-6](https://doi.org/10.1016/0167-577x%2895%2900066-6) J.Q. Guo, K. Ohtera, K. Kita, J. Nagahora, N.S. Kazama, Crystallization behavior of Al100 − xSmx (x = 8–14 at%) amorphous alloys, Materials Letters 24, 133-138 (1995).  
_cited as the source of values for this phase_

## HCP_A3 (Al–Sm)

- Id: `phase:al-sm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300.49–1382.31 K, x(Sm) 0.99998–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:hcp-a3)

Names (4): _corpus: _corpus:phase:al-sm:hcp-a3  
_tdb: _tdb:AlSm-08Jia.tdb:HCP_A3, tdb:AlSm-08Zho.tdb:HCP_A3, tdb:AlSm-98Sac.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): HCP_A3, type code %A, sha256 `b393d63733d46908…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : AL SM : VA : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): HCP_A3, type code %A, sha256 `2da381cdcf96b97e…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AL SM : VA : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): HCP_A3, type code %A, sha256 `dbfe39f86fc8f00a…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AL SM : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase_

## LIQUID (Al–Sm)

- Id: `phase:al-sm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 893.81–2500 K, x(Sm) 0–1
- Literature: 37 values (37 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:liquid)

Names (7): _corpus: _corpus:phase:al-sm:liquid  
_paper: _paper:10.1007/s11661-007-9445-6:Liq, paper:10.1007/s11661-007-9445-6:liq, paper:10.1007/s11661-007-9445-6:liquid  
_tdb: _tdb:AlSm-08Jia.tdb:LIQUID, tdb:AlSm-08Zho.tdb:LIQUID, tdb:AlSm-98Sac.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): LIQUID, type code %, sha256 `b393d63733d46908…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : AL SM : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): LIQUID, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AL AL2SM SM : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): LIQUID, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL SM : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(67)90116-6](https://doi.org/10.1016/0022-5088%2867%2990116-6) F Casteels, The aluminium-rich parts of the aluminium-samarium and aluminium-dysprosium systems, Journal of the Less Common Metals 12, 210-220 (1967).  
_cited as the source of values for this phase_
- [doi:10.1016/0167-577x(95)00066-6](https://doi.org/10.1016/0167-577x%2895%2900066-6) J.Q. Guo, K. Ohtera, K. Kita, J. Nagahora, N.S. Kazama, Crystallization behavior of Al100 − xSmx (x = 8–14 at%) amorphous alloys, Materials Letters 24, 133-138 (1995).  
_cited as the source of values for this phase_

## RHOMB_C19 (Al–Sm)

- Id: `phase:al-sm:rhomb-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1187.99 K, x(Sm) 0.96244–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sm:rhomb-c19)

Names (5): _corpus: _corpus:phase:al-sm:rhomb-c19  
_paper: _paper:10.1007/s11661-007-9445-6:rho  
_tdb: _tdb:AlSm-08Jia.tdb:RHOMB_C19, tdb:AlSm-08Zho.tdb:RHOMB_C19, tdb:AlSm-98Sac.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (3): PHASE and CONSTITUENT statements as written

[AlSm-08Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Jia.tdb): RHOMB_C19, type code %, sha256 `b393d63733d46908…`

~~~~text
50: PHASE RHOMB_C19 % 1 1 !
51: CONST RHOMB_C19 : AL SM% : !
~~~~

[AlSm-08Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-08Zho.tdb): RHOMB_C19, type code %, sha256 `2da381cdcf96b97e…`

~~~~text
46: PHASE RHOMB_C19 % 1 1 !
47: CONST RHOMB_C19 : AL SM% : !
~~~~

[AlSm-98Sac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSm-98Sac.tdb): RHOMB_C19, type code %, sha256 `dbfe39f86fc8f00a…`

~~~~text
48: PHASE RHOMB_C19 % 1 1 !
49: CONST RHOMB_C19 : AL SM% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11661-007-9445-6](https://doi.org/10.1007/s11661-007-9445-6) S.H. Zhou, R.E. Napolitano, Modeling of Thermodynamic Properties and Phase Equilibria for the Al-Sm Binary System, Metall Mater Trans A 39, 502-512 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00066-6](https://doi.org/10.1016/S0966-9795%2897%2900066-6) A. Saccone, G. Cacciamani, D. Maccio, G. Borzone, R. Ferro, Intermetallics, 6, 201-15(1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.05.035](https://doi.org/10.1016/j.jallcom.2007.05.035) B.R. Jia, L.B. Liu, D.Q. Yi, Z.P. Jin, J.F. Nie, Thermodynamic assessment of the Al–Mg–Sm system, Journal of Alloys and Compounds 459, 267-273 (2008).  
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
