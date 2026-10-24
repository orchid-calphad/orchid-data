# Au–Er phases

> Au–Er system: 11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-ER.html · Markdown: https://data.orchid-project.org/phases/pages/AU-ER.md

11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-ER) · [full JSON](https://data.orchid-project.org/phases/systems/AU-ER.json) · [Au–Er system page](https://data.orchid-project.org/systems/AU-ER.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-ER.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Er system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU10ER7](#phase-au-er-au10er7); _phase:au-er:au10er7_ | Au10Gd7 · tI136 · I4_1/acd (142) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1635.32 K, x(Er) 0.41176–0.41176 | 8 | 1 |
| [AU2ER_C11B](#phase-au-er-au2er-c11b); _phase:au-er:au2er-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1637.54 K, x(Er) 0.33333–0.33333 | 7 | 1 |
| [AU3ER_D0A](#phase-au-er-au3er-d0a); _phase:au-er:au3er-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1552.54 K, x(Er) 0.25–0.25 | 6 | 1 |
| [AU4ER_D1A](#phase-au-er-au4er-d1a); _phase:au-er:au4er-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1273.86 K, x(Er) 0.2–0.2 | 5 | 1 |
| [AUER_B2](#phase-au-er-auer-b2); _phase:au-er:auer-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1890.97–1978.47 K, x(Er) 0.5–0.5 | 4 | 1 |
| [AUER_B33](#phase-au-er-auer-b33); _phase:au-er:auer-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1890.97 K, x(Er) 0.5–0.5 | 7 | 1 |
| [AUER2_C37](#phase-au-er-auer2-c37); _phase:au-er:auer2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1386.71 K, x(Er) 0.66667–0.66667 | 4 | 1 |
| [BCC_A2](#phase-au-er-bcc-a2); _phase:au-er:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-au-er-fcc-a1); _phase:au-er:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1345.32 K, x(Er) 0–0.07195 | 3 | 1 |
| [HCP_A3](#phase-au-er-hcp-a3); _phase:au-er:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.43 K, x(Er) 0.99288–1 | 2 | 1 |
| [LIQUID](#phase-au-er-liquid); _phase:au-er:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1077.82–2500 K, x(Er) 0–1 | 23 | 1 |

## AU10ER7 (Au–Er)

- Id: `phase:au-er:au10er7`; status `assigned`
- Structure: Au10Gd7 · tI136 · I4_1/acd (142); type `st:au10gd7-ti136`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.5882, Er 0.4118
- Stability: stable in 1 of 1 calculated diagram(s): 300–1635.32 K, x(Er) 0.41176–0.41176
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:au10er7)

Names (3): _corpus: _corpus:phase:au-er:au10er7  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au10Er7  
_tdb: _tdb:AuEr-11Don.tdb:AU10ER7  


### TDB models of AU10ER7 (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): AU10ER7, type code %, sha256 `f614597f077a07e2…`

~~~~text
56: PHASE AU10ER7 % 2 10 7 !
57: CONST AU10ER7 : AU : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AU2ER_C11B (Au–Er)

- Id: `phase:au-er:au2er-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.6667, Er 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1637.54 K, x(Er) 0.33333–0.33333
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:au2er-c11b)

Names (3): _corpus: _corpus:phase:au-er:au2er-c11b  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au2Er  
_tdb: _tdb:AuEr-11Don.tdb:AU2ER_C11B  


### TDB models of AU2ER_C11B (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): AU2ER_C11B, type code %, sha256 `f614597f077a07e2…`

~~~~text
51: PHASE AU2ER_C11B % 2 2 1 !
52: CONST AU2ER_C11B : AU : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AU3ER_D0A (Au–Er)

- Id: `phase:au-er:au3er-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacjmto and oqmd-28151, space group 59
- Stoichiometry: Au 0.7500, Er 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1552.54 K, x(Er) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:au3er-d0a)

Names (5): _corpus: _corpus:phase:au-er:au3er-d0a  
_mp: _mp:mp-aaacjmto  
_oqmd: _oqmd:oqmd-28151  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au3Er  
_tdb: _tdb:AuEr-11Don.tdb:AU3ER_D0A  


### TDB models of AU3ER_D0A (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): AU3ER_D0A, type code %, sha256 `f614597f077a07e2…`

~~~~text
46: PHASE AU3ER_D0A % 2 3 1 !
47: CONST AU3ER_D0A : AU : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AU4ER_D1A (Au–Er)

- Id: `phase:au-er:au4er-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacixsh and oqmd-28152, space group 87
- Stoichiometry: Au 0.8000, Er 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1273.86 K, x(Er) 0.2–0.2
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:au4er-d1a)

Names (5): _corpus: _corpus:phase:au-er:au4er-d1a  
_mp: _mp:mp-aaacixsh  
_oqmd: _oqmd:oqmd-28152  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au4Er  
_tdb: _tdb:AuEr-11Don.tdb:AU4ER_D1A  


### TDB models of AU4ER_D1A (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): AU4ER_D1A, type code %, sha256 `f614597f077a07e2…`

~~~~text
41: PHASE AU4ER_D1A % 2 4 1 !
42: CONST AU4ER_D1A : AU : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AUER_B2 (Au–Er)

- Id: `phase:au-er:auer-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.5000, Er 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 1890.97–1978.47 K, x(Er) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:auer-b2)

Names (3): _corpus: _corpus:phase:au-er:auer-b2  
_paper: _paper:10.1016/j.jallcom.2011.01.072:βAuEr  
_tdb: _tdb:AuEr-11Don.tdb:AUER_B2  


### TDB models of AUER_B2 (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): AUER_B2, type code %, sha256 `f614597f077a07e2…`

~~~~text
66: PHASE AUER_B2 % 2 1 1 !
67: CONST AUER_B2 : AU : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AUER_B33 (Au–Er)

- Id: `phase:au-er:auer-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.5000, Er 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1890.97 K, x(Er) 0.5–0.5
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:auer-b33)

Names (3): _corpus: _corpus:phase:au-er:auer-b33  
_paper: _paper:10.1016/j.jallcom.2011.01.072:αAuEr  
_tdb: _tdb:AuEr-11Don.tdb:AUER_B33  


### TDB models of AUER_B33 (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): AUER_B33, type code %, sha256 `f614597f077a07e2…`

~~~~text
61: PHASE AUER_B33 % 2 1 1 !
62: CONST AUER_B33 : AU : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## AUER2_C37 (Au–Er)

- Id: `phase:au-er:auer2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacktqa and oqmd-1436040, space group 62
- Stoichiometry: Au 0.3333, Er 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1386.71 K, x(Er) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:auer2-c37)

Names (5): _corpus: _corpus:phase:au-er:auer2-c37  
_mp: _mp:mp-aaacktqa  
_oqmd: _oqmd:oqmd-1436040  
_paper: _paper:10.1016/j.jallcom.2011.01.072:AuEr2  
_tdb: _tdb:AuEr-11Don.tdb:AUER2_C37  


### TDB models of AUER2_C37 (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): AUER2_C37, type code %, sha256 `f614597f077a07e2…`

~~~~text
71: PHASE AUER2_C37 % 2 1 2 !
72: CONST AUER2_C37 : AU : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Er)

- Id: `phase:au-er:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:bcc-a2)

Names (2): _corpus: _corpus:phase:au-er:bcc-a2  
_tdb: _tdb:AuEr-11Don.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): BCC_A2, type code %B, sha256 `f614597f077a07e2…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AU ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase_

## FCC_A1 (Au–Er)

- Id: `phase:au-er:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1345.32 K, x(Er) 0–0.07195
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:fcc-a1)

Names (3): _corpus: _corpus:phase:au-er:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au(fcc)  
_tdb: _tdb:AuEr-11Don.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): FCC_A1, type code %A, sha256 `f614597f077a07e2…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AU% ER : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Er)

- Id: `phase:au-er:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.43 K, x(Er) 0.99288–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:hcp-a3)

Names (3): _corpus: _corpus:phase:au-er:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Er(hcp)  
_tdb: _tdb:AuEr-11Don.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): HCP_A3, type code %A, sha256 `f614597f077a07e2…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AU ER : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(02)00093-6](https://doi.org/10.1016/s0966-9795%2802%2900093-6) A. Saccone, D. Macciò, S. Delfino, R. Ferro, Alloying behavior of the rare earth metals with gold: the Ho–Au, Er–Au and Tm–Au systems, Intermetallics 10, 903-913 (2002).  
_cited as the source of values for this phase_

## LIQUID (Au–Er)

- Id: `phase:au-er:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1077.82–2500 K, x(Er) 0–1
- Literature: 23 values (23 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-er:liquid)

Names (3): _corpus: _corpus:phase:au-er:liquid  
_paper: _paper:10.1016/j.jallcom.2011.01.072:L  
_tdb: _tdb:AuEr-11Don.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuEr-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb): LIQUID, type code %, sha256 `f614597f077a07e2…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AU ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
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
