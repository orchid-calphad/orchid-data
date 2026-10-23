# Au–Tm phases

> Au–Tm system: 11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-TM.html · Markdown: https://data.orchid-project.org/phases/pages/AU-TM.md

11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-TM) · [full JSON](https://data.orchid-project.org/phases/systems/AU-TM.json) · [Au–Tm system page](https://data.orchid-project.org/systems/AU-TM.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-TM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Tm system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU10TM7](#phase-au-tm-au10tm7); _phase:au-tm:au10tm7_ | Au10Gd7 · tI136 · I4_1/acd (142) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1625.81 K, x(Tm) 0.41176–0.41176 | 4 | 1 |
| [AU2TM_C11B](#phase-au-tm-au2tm-c11b); _phase:au-tm:au2tm-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1689.8 K, x(Tm) 0.33333–0.33333 | 6 | 1 |
| [AU3TM_D0A](#phase-au-tm-au3tm-d0a); _phase:au-tm:au3tm-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1561.89 K, x(Tm) 0.25–0.25 | 6 | 1 |
| [AU4TM_D1A](#phase-au-tm-au4tm-d1a); _phase:au-tm:au4tm-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1309.39 K, x(Tm) 0.2–0.2 | 4 | 1 |
| [AUTM_B2](#phase-au-tm-autm-b2); _phase:au-tm:autm-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1903.63–1991.13 K, x(Tm) 0.5–0.5 | 4 | 1 |
| [AUTM_B33](#phase-au-tm-autm-b33); _phase:au-tm:autm-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1903.63 K, x(Tm) 0.5–0.5 | 6 | 1 |
| [AUTM2_C37](#phase-au-tm-autm2-c37); _phase:au-tm:autm2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1438.39 K, x(Tm) 0.66667–0.66667 | 4 | 1 |
| [BCC_A2](#phase-au-tm-bcc-a2); _phase:au-tm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-au-tm-fcc-a1); _phase:au-tm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1348.01 K, x(Tm) 0–0.07418 | 2 | 1 |
| [HCP_A3](#phase-au-tm-hcp-a3); _phase:au-tm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.37 K, x(Tm) 0.99459–1 | 2 | 1 |
| [LIQUID](#phase-au-tm-liquid); _phase:au-tm:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1113.01–2500 K, x(Tm) 0–1 | 20 | 1 |

## AU10TM7 (Au–Tm)

- Id: `phase:au-tm:au10tm7`; status `assigned`
- Structure: Au10Gd7 · tI136 · I4_1/acd (142); type `st:au10gd7-ti136`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.5882, Tm 0.4118
- Stability: stable in 1 of 1 calculated diagram(s): 300–1625.81 K, x(Tm) 0.41176–0.41176
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:au10tm7)

Names (3): _corpus: _corpus:phase:au-tm:au10tm7  
_paper: _paper:10.1016/j.calphad.2012.02.002:Au10Tm7  
_tdb: _tdb:AuTm-12Don.tdb:AU10TM7  


### TDB models of AU10TM7 (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): AU10TM7, type code %, sha256 `97665efb6ffc621e…`

~~~~text
59: PHASE AU10TM7 % 2 10 7 !
60: CONST AU10TM7 : AU : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AU2TM_C11B (Au–Tm)

- Id: `phase:au-tm:au2tm-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.6667, Tm 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1689.8 K, x(Tm) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:au2tm-c11b)

Names (3): _corpus: _corpus:phase:au-tm:au2tm-c11b  
_paper: _paper:10.1016/j.calphad.2012.02.002:Au2Tm  
_tdb: _tdb:AuTm-12Don.tdb:AU2TM_C11B  


### TDB models of AU2TM_C11B (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): AU2TM_C11B, type code %, sha256 `97665efb6ffc621e…`

~~~~text
54: PHASE AU2TM_C11B % 2 2 1 !
55: CONST AU2TM_C11B : AU : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AU3TM_D0A (Au–Tm)

- Id: `phase:au-tm:au3tm-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgipr and oqmd-28227, space group 59
- Stoichiometry: Au 0.7500, Tm 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1561.89 K, x(Tm) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:au3tm-d0a)

Names (5): _corpus: _corpus:phase:au-tm:au3tm-d0a  
_mp: _mp:mp-aaabgipr  
_oqmd: _oqmd:oqmd-28227  
_paper: _paper:10.1016/j.calphad.2012.02.002:Au3Tm  
_tdb: _tdb:AuTm-12Don.tdb:AU3TM_D0A  


### TDB models of AU3TM_D0A (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): AU3TM_D0A, type code %, sha256 `97665efb6ffc621e…`

~~~~text
49: PHASE AU3TM_D0A % 2 3 1 !
50: CONST AU3TM_D0A : AU : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AU4TM_D1A (Au–Tm)

- Id: `phase:au-tm:au4tm-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaciuki and oqmd-28228, space group 87
- Stoichiometry: Au 0.8000, Tm 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1309.39 K, x(Tm) 0.2–0.2
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:au4tm-d1a)

Names (5): _corpus: _corpus:phase:au-tm:au4tm-d1a  
_mp: _mp:mp-aaaciuki  
_oqmd: _oqmd:oqmd-28228  
_paper: _paper:10.1016/j.calphad.2012.02.002:Au4Tm  
_tdb: _tdb:AuTm-12Don.tdb:AU4TM_D1A  


### TDB models of AU4TM_D1A (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): AU4TM_D1A, type code %, sha256 `97665efb6ffc621e…`

~~~~text
44: PHASE AU4TM_D1A % 2 4 1 !
45: CONST AU4TM_D1A : AU : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AUTM_B2 (Au–Tm)

- Id: `phase:au-tm:autm-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.5000, Tm 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 1903.63–1991.13 K, x(Tm) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:autm-b2)

Names (3): _corpus: _corpus:phase:au-tm:autm-b2  
_paper: _paper:10.1016/j.calphad.2012.02.002:βAuTm  
_tdb: _tdb:AuTm-12Don.tdb:AUTM_B2  


### TDB models of AUTM_B2 (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): AUTM_B2, type code %, sha256 `97665efb6ffc621e…`

~~~~text
69: PHASE AUTM_B2 % 2 1 1 !
70: CONST AUTM_B2 : AU : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AUTM_B33 (Au–Tm)

- Id: `phase:au-tm:autm-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.5000, Tm 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1903.63 K, x(Tm) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:autm-b33)

Names (3): _corpus: _corpus:phase:au-tm:autm-b33  
_paper: _paper:10.1016/j.calphad.2012.02.002:αAuTm  
_tdb: _tdb:AuTm-12Don.tdb:AUTM_B33  


### TDB models of AUTM_B33 (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): AUTM_B33, type code %, sha256 `97665efb6ffc621e…`

~~~~text
64: PHASE AUTM_B33 % 2 1 1 !
65: CONST AUTM_B33 : AU : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AUTM2_C37 (Au–Tm)

- Id: `phase:au-tm:autm2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackivy and oqmd-1800555, space group 62
- Stoichiometry: Au 0.3333, Tm 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1438.39 K, x(Tm) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:autm2-c37)

Names (5): _corpus: _corpus:phase:au-tm:autm2-c37  
_mp: _mp:mp-aaackivy  
_oqmd: _oqmd:oqmd-1800555  
_paper: _paper:10.1016/j.calphad.2012.02.002:AuTm2  
_tdb: _tdb:AuTm-12Don.tdb:AUTM2_C37  


### TDB models of AUTM2_C37 (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): AUTM2_C37, type code %, sha256 `97665efb6ffc621e…`

~~~~text
74: PHASE AUTM2_C37 % 2 1 2 !
75: CONST AUTM2_C37 : AU : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Tm)

- Id: `phase:au-tm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:bcc-a2)

Names (2): _corpus: _corpus:phase:au-tm:bcc-a2  
_tdb: _tdb:AuTm-12Don.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): BCC_A2, type code %B, sha256 `97665efb6ffc621e…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AU TM : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase_

## FCC_A1 (Au–Tm)

- Id: `phase:au-tm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1348.01 K, x(Tm) 0–0.07418
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:fcc-a1)

Names (3): _corpus: _corpus:phase:au-tm:fcc-a1  
_paper: _paper:10.1016/j.calphad.2012.02.002:Au(fcc)  
_tdb: _tdb:AuTm-12Don.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): FCC_A1, type code %A, sha256 `97665efb6ffc621e…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AU% TM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Tm)

- Id: `phase:au-tm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.37 K, x(Tm) 0.99459–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:hcp-a3)

Names (3): _corpus: _corpus:phase:au-tm:hcp-a3  
_paper: _paper:10.1016/j.calphad.2012.02.002:Tm(hcp)  
_tdb: _tdb:AuTm-12Don.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): HCP_A3, type code %A, sha256 `97665efb6ffc621e…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AU TM% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## LIQUID (Au–Tm)

- Id: `phase:au-tm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1113.01–2500 K, x(Tm) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-tm:liquid)

Names (3): _corpus: _corpus:phase:au-tm:liquid  
_paper: _paper:10.1016/j.calphad.2012.02.002:L  
_tdb: _tdb:AuTm-12Don.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuTm-12Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTm-12Don.tdb): LIQUID, type code %, sha256 `97665efb6ffc621e…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AU TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.002](https://doi.org/10.1016/j.calphad.2012.02.002) H.Q. Dong, X.M. Tao, T. Laurila, M. Paulasto-Kröckel, Thermodynamic assessment of Au–Ho and Au–Tm binary systems, Calphad 37, 87-93 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

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
