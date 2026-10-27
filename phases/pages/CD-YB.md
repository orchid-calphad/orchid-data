# Cd–Yb phases

> Cd–Yb system: 11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-YB.html · Markdown: https://data.orchid-project.org/phases/pages/CD-YB.md

11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-YB) · [full JSON](https://data.orchid-project.org/phases/systems/CD-YB.json) · [Cd–Yb system page](https://data.orchid-project.org/systems/CD-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Yb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-yb-bcc-a2); _phase:cd-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 975–2500 K, x(Yb) 0.97886–1 | 3 | 1 |
| [CD2YB_HT](#phase-cd-yb-cd2yb); _phase:cd-yb:cd2yb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 967.03–976.2 K, x(Yb) 0.33333–0.33333 | 0 | 1 |
| [CD2YB_C14](#phase-cd-yb-cd2yb-c14); _phase:cd-yb:cd2yb-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–967.03 K, x(Yb) 0.33333–0.33333 | 0 | 1 |
| [CD51YB14](#phase-cd-yb-cd51yb14); _phase:cd-yb:cd51yb14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–927.69 K, x(Yb) 0.21538–0.21538 | 6 | 1 |
| [CD57YB10](#phase-cd-yb-cd57yb10); _phase:cd-yb:cd57yb10_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–908.69 K, x(Yb) 0.14925–0.14925 | 6 | 1 |
| [CD6YB](#phase-cd-yb-cd6yb); _phase:cd-yb:cd6yb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–901.58 K, x(Yb) 0.14286–0.14286 | 4 | 1 |
| [CD8YB3](#phase-cd-yb-cd8yb3); _phase:cd-yb:cd8yb3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–926.95 K, x(Yb) 0.27273–0.27273 | 4 | 1 |
| [CDYB_B2](#phase-cd-yb-cdyb-b2); _phase:cd-yb:cdyb-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1070.02 K, x(Yb) 0.5–0.5 | 7 | 1 |
| [FCC_A1](#phase-cd-yb-fcc-a1); _phase:cd-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1033 K, x(Yb) 0.97611–1 | 5 | 1 |
| [HCP_A3](#phase-cd-yb-hcp-a3); _phase:cd-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–594.43 K, x(Yb) 0–0 | 2 | 1 |
| [LIQUID](#phase-cd-yb-liquid); _phase:cd-yb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 569.43–2500 K, x(Yb) 0–1 | 26 | 1 |

## BCC_A2 (Cd–Yb)

- Id: `phase:cd-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 975–2500 K, x(Yb) 0.97886–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:bcc-a2)

Names (3): _corpus: _corpus:phase:cd-yb:bcc-a2  
_paper: _paper:10.1007/s11669-017-0588-x:(γYb)  
_tdb: _tdb:CdYb-17Kal.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): BCC_A2, type code %B, sha256 `7753beb8aad6591a…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CD YB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02890551](https://doi.org/10.1007/bf02890551) K.A. Gschneidner and J.F.W. Calderwood, The Cd - Yb (Cadmium-Ytterbium) System, J. Phase Equilib., 1988, 9(2), p 141143  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_

## CD2YB_HT (Cd–Yb)

- Id: `phase:cd-yb:cd2yb`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): Imma (74) — on-hull OQMD Cd2 Yb1 at x(YB)=0.3333
- Candidate (sgte_mmc2): (Cd2Yb) — Hallstedt 2025 mmc2 row for CD2YB_HT: Cd2Yb
- Stoichiometry: Cd 0.6667, Yb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 967.03–976.2 K, x(Yb) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:cd2yb)

Names (3): _corpus: _corpus:phase:cd-yb:cd2yb, corpus:phase:cd-yb:cd2yb-ht  
_tdb: _tdb:CdYb-17Kal.tdb:CD2YB_HT  


### TDB models of CD2YB_HT (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): CD2YB_HT, type code %, sha256 `7753beb8aad6591a…`

~~~~text
69: PHASE CD2YB_HT % 2 2 1 !
70: CONST CD2YB_HT : CD : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase_

## CD2YB_C14 (Cd–Yb)

- Id: `phase:cd-yb:cd2yb-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.6667, Yb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–967.03 K, x(Yb) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:cd2yb-c14)

Names (2): _corpus: _corpus:phase:cd-yb:cd2yb-c14  
_tdb: _tdb:CdYb-17Kal.tdb:CD2YB_C14  


### TDB models of CD2YB_C14 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): CD2YB_C14, type code %, sha256 `7753beb8aad6591a…`

~~~~text
64: PHASE CD2YB_C14 % 2 2 1 !
65: CONST CD2YB_C14 : CD : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase_

## CD51YB14 (Cd–Yb)

- Id: `phase:cd-yb:cd51yb14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.7846, Yb 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–927.69 K, x(Yb) 0.21538–0.21538
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:cd51yb14)

Names (3): _corpus: _corpus:phase:cd-yb:cd51yb14  
_paper: _paper:10.1007/s11669-017-0588-x:Yb14Cd51  
_tdb: _tdb:CdYb-17Kal.tdb:CD51YB14  


### TDB models of CD51YB14 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): CD51YB14, type code %, sha256 `7753beb8aad6591a…`

~~~~text
54: PHASE CD51YB14 % 2 51 14 !
55: CONST CD51YB14 : CD : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_

## CD57YB10 (Cd–Yb)

- Id: `phase:cd-yb:cd57yb10`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cd5.7Yb) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cd5.7Yb) — Hallstedt 2025 mmc2 row for CD57YB10: Cd5.7Yb
- Stoichiometry: Cd 0.8507, Yb 0.1493
- Stability: stable in 1 of 1 calculated diagram(s): 300–908.69 K, x(Yb) 0.14925–0.14925
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:cd57yb10)

Names (3): _corpus: _corpus:phase:cd-yb:cd57yb10  
_paper: _paper:10.1007/s11669-017-0588-x:YbCd5,7  
_tdb: _tdb:CdYb-17Kal.tdb:CD57YB10  


### TDB models of CD57YB10 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): CD57YB10, type code %, sha256 `7753beb8aad6591a…`

~~~~text
49: PHASE CD57YB10 % 2 5.7 1 !
50: CONST CD57YB10 : CD : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_

## CD6YB (Cd–Yb)

- Id: `phase:cd-yb:cd6yb`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Cd6Y · cI184 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Cd6Y · cI184 · Im-3 (204) — Hallstedt 2025 mmc2 row for CD6YB: Cd6Yb (alt. Cd6Yb)
- Candidate (sgte_mmc2): Cd6Yb · cI168 · I23 (197) — Hallstedt 2025 mmc2 row for CD6YB: Cd6Yb (alt. Cd6Y)
- Candidate (tdb_comment): Cd6Y · cI184 · Im-3 — CdYb-17Kal.tdb: 'Prototype Cd6Y (cI184, Im-3) and/or Cd6Yb (cI168, I23)'
- Stoichiometry: Cd 0.8571, Yb 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–901.58 K, x(Yb) 0.14286–0.14286
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:cd6yb)

Names (3): _corpus: _corpus:phase:cd-yb:cd6yb  
_paper: _paper:10.1007/s11669-017-0588-x:YbCd6  
_tdb: _tdb:CdYb-17Kal.tdb:CD6YB  


### TDB models of CD6YB (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): CD6YB, type code %, sha256 `7753beb8aad6591a…`

~~~~text
44: PHASE CD6YB % 2 6 1 !
45: CONST CD6YB : CD : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_

## CD8YB3 (Cd–Yb)

- Id: `phase:cd-yb:cd8yb3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cd8Yb3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cd8Yb3) — Hallstedt 2025 mmc2 row for CD8YB3: Cd8Yb3
- Stoichiometry: Cd 0.7273, Yb 0.2727
- Stability: stable in 1 of 1 calculated diagram(s): 300–926.95 K, x(Yb) 0.27273–0.27273
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:cd8yb3)

Names (3): _corpus: _corpus:phase:cd-yb:cd8yb3  
_paper: _paper:10.1007/s11669-017-0588-x:Yb3Cd8  
_tdb: _tdb:CdYb-17Kal.tdb:CD8YB3  


### TDB models of CD8YB3 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): CD8YB3, type code %, sha256 `7753beb8aad6591a…`

~~~~text
59: PHASE CD8YB3 % 2 8 3 !
60: CONST CD8YB3 : CD : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_

## CDYB_B2 (Cd–Yb)

- Id: `phase:cd-yb:cdyb-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.5000, Yb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1070.02 K, x(Yb) 0.5–0.5
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:cdyb-b2)

Names (3): _corpus: _corpus:phase:cd-yb:cdyb-b2  
_paper: _paper:10.1007/s11669-017-0588-x:YbCd  
_tdb: _tdb:CdYb-17Kal.tdb:CDYB_B2  


### TDB models of CDYB_B2 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): CDYB_B2, type code %, sha256 `7753beb8aad6591a…`

~~~~text
74: PHASE CDYB_B2 % 2 1 1 !
75: CONST CDYB_B2 : CD : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02890551](https://doi.org/10.1007/bf02890551) K.A. Gschneidner and J.F.W. Calderwood, The Cd - Yb (Cadmium-Ytterbium) System, J. Phase Equilib., 1988, 9(2), p 141143  
_cited as the source of values for this phase_

## FCC_A1 (Cd–Yb)

- Id: `phase:cd-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1033 K, x(Yb) 0.97611–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:cd-yb:fcc-a1  
_paper: _paper:10.1007/s11669-017-0588-x:(βYb)  
_tdb: _tdb:CdYb-17Kal.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): FCC_A1, type code %A, sha256 `7753beb8aad6591a…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CD YB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02890551](https://doi.org/10.1007/bf02890551) K.A. Gschneidner and J.F.W. Calderwood, The Cd - Yb (Cadmium-Ytterbium) System, J. Phase Equilib., 1988, 9(2), p 141143  
_cited as the source of values for this phase_

## HCP_A3 (Cd–Yb)

- Id: `phase:cd-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–594.43 K, x(Yb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:hcp-a3)

Names (3): _corpus: _corpus:phase:cd-yb:hcp-a3  
_paper: _paper:10.1007/s11669-017-0588-x:(Cd)  
_tdb: _tdb:CdYb-17Kal.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): HCP_A3, type code %A, sha256 `7753beb8aad6591a…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CD YB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_

## LIQUID (Cd–Yb)

- Id: `phase:cd-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 569.43–2500 K, x(Yb) 0–1
- Literature: 26 values (26 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-yb:liquid)

Names (3): _corpus: _corpus:phase:cd-yb:liquid  
_paper: _paper:10.1007/s11669-017-0588-x:L  
_tdb: _tdb:CdYb-17Kal.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/CdYb-17Kal.tdb): LIQUID, type code %, sha256 `7753beb8aad6591a…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CD YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90179-2](https://doi.org/10.1016/0022-5088%2871%2990179-2) A. Palenzona, The ytterbium-cadmium system, Journal of the Less Common Metals 25, 367-372 (1971).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02890551](https://doi.org/10.1007/bf02890551) K.A. Gschneidner and J.F.W. Calderwood, The Cd - Yb (Cadmium-Ytterbium) System, J. Phase Equilib., 1988, 9(2), p 141143  
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
