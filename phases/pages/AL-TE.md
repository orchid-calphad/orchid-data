# Al–Te phases

> Al–Te system: 11 phases (tier A 4, tier C 3, liquid 2, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-TE.html · Markdown: https://data.orchid-project.org/phases/pages/AL-TE.md

11 phases (tier A 4, tier C 3, liquid 2, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-TE) · [full JSON](https://data.orchid-project.org/phases/systems/AL-TE.json) · [Al–Te system page](https://data.orchid-project.org/systems/AL-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Te system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-al-te-a8-hexagonal); _phase:al-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 4 | 2 |
| [AL2TE3](#phase-al-te-al2te3); _phase:al-te:al2te3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1167.29 K, x(Te) 0.6–0.6 | 5 | 1 |
| [AL2TE3_ALPHA](#phase-al-te-al2te3-alpha); _phase:al-te:al2te3-alpha_ | Al2Te3 · mP240 · P2_1 (4) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–993.15 K, x(Te) 0.6–0.6 | 4 | 1 |
| [AL2TE3_BETA](#phase-al-te-al2te3-beta); _phase:al-te:al2te3-beta_ | Al2Te3 · mP40 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 993.15–1165.36 K, x(Te) 0.6–0.6 | 2 | 1 |
| [AL2TE5](#phase-al-te-al2te5); _phase:al-te:al2te5_ | Al2Te5 · mC14 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 682.23–735.99 K, x(Te) 0.71429–0.71429 | 10 | 1 |
| [ALTE](#phase-al-te-alte); _phase:al-te:alte_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1128.7 K, x(Te) 0.5–0.5 | 7 | 1 |
| [BCC_A2](#phase-al-te-bcc-a2); _phase:al-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-al-te-fcc-a1); _phase:al-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–933.47 K, x(Te) 0–0 | 2 | 2 |
| [HCP_A3](#phase-al-te-hcp-a3); _phase:al-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-al-te-ion); _phase:al-te:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 567.29–2500 K, x(Te) 0–1 | 0 | 1 |
| [LIQUID](#phase-al-te-liquid); _phase:al-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 699.65–2500 K, x(Te) 0–1 | 12 | 1 |

## HEXAGONAL_A8 (Al–Te)

- Id: `phase:al-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:a8-hexagonal)

Names (5): _corpus: _corpus:phase:al-te:a8-hexagonal, corpus:phase:al-te:hexagonal-a8  
_paper: _paper:10.1007/s11669-019-00733-z:(Te)  
_tdb: _tdb:AlTe-19Shi.tdb:HEXAGONAL_A8, tdb:AlTe-93Oh.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): HEXAGONAL_A8, type code %, sha256 `c52e1bafcdb91f7e…`

~~~~text
48: PHASE HEXAGONAL_A8 % 1 1 !
49: CONST HEXAGONAL_A8 : TE : !
~~~~

[AlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-93Oh.tdb): HEXAGONAL_A8, type code %, sha256 `a95e02f39b2e3292…`

~~~~text
52: PHASE HEXAGONAL_A8 % 1 1 !
53: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_
- [doi:10.1515/znb-1988-0209](https://doi.org/10.1515/znb-1988-0209) Rüdiger Kniep, Peter Blees, Phasengleichgewichte und intermediäre Phasen im System Al–Te / Phase Relations and Intermediate Phases in the Al–Te System, Zeitschrift für Naturforschung B 43, 182-188 (1988).  
_cited as the source of values for this phase_

## AL2TE3 (Al–Te)

- Id: `phase:al-te:al2te3`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P2_1/c (14) — on-hull MP Al2Te3 at x(TE)=0.6000
- Candidate (dft_oqmd): P21/c (14) — on-hull OQMD Al2 Te3 at x(TE)=0.6000
- Candidate (tdb_comment): Al2Te3 · mP240 · P2_1 — AlTe-93Oh.tdb: 'Prototype Al2Te3 (mP240, P2_1)'
- Stoichiometry: Al 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1167.29 K, x(Te) 0.6–0.6
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:al2te3)

Names (3): _corpus: _corpus:phase:al-te:al2te3  
_paper: _paper:10.1007/s11669-019-00733-z:Al2Te3  
_tdb: _tdb:AlTe-93Oh.tdb:AL2TE3  


### TDB models of AL2TE3 (1): PHASE and CONSTITUENT statements as written

[AlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-93Oh.tdb): AL2TE3, type code %, sha256 `a95e02f39b2e3292…`

~~~~text
57: PHASE AL2TE3 % 2 2 3 !
58: CONST AL2TE3 : AL : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_
- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_reports values for this phase_

## AL2TE3_ALPHA (Al–Te)

- Id: `phase:al-te:al2te3-alpha`; status `assigned`
- Structure: Al2Te3 · mP240 · P2_1 (4); type `st:al2te3-mp240`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–993.15 K, x(Te) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:al2te3-alpha)

Names (3): _corpus: _corpus:phase:al-te:al2te3-alpha  
_paper: _paper:10.1007/s11669-019-00733-z:αAl2Te3  
_tdb: _tdb:AlTe-19Shi.tdb:AL2TE3_ALPHA  


### TDB models of AL2TE3_ALPHA (1): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): AL2TE3_ALPHA, type code %, sha256 `c52e1bafcdb91f7e…`

~~~~text
58: PHASE AL2TE3_ALPHA % 2 2 3 !
59: CONST AL2TE3_ALPHA : AL : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/znb-1988-0209](https://doi.org/10.1515/znb-1988-0209) Rüdiger Kniep, Peter Blees, Phasengleichgewichte und intermediäre Phasen im System Al–Te / Phase Relations and Intermediate Phases in the Al–Te System, Zeitschrift für Naturforschung B 43, 182-188 (1988).  
_cited as the source of values for this phase_

## AL2TE3_BETA (Al–Te)

- Id: `phase:al-te:al2te3-beta`; status `assigned`
- Structure: Al2Te3 · mP40 · P2_1/c (14); type `st:al2te3-mp40`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 993.15–1165.36 K, x(Te) 0.6–0.6
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:al2te3-beta)

Names (3): _corpus: _corpus:phase:al-te:al2te3-beta  
_paper: _paper:10.1007/s11669-019-00733-z:βAl2Te3  
_tdb: _tdb:AlTe-19Shi.tdb:AL2TE3_BETA  


### TDB models of AL2TE3_BETA (1): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): AL2TE3_BETA, type code %, sha256 `c52e1bafcdb91f7e…`

~~~~text
63: PHASE AL2TE3_BETA % 2 2 3 !
64: CONST AL2TE3_BETA : AL : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/znb-1988-0209](https://doi.org/10.1515/znb-1988-0209) Rüdiger Kniep, Peter Blees, Phasengleichgewichte und intermediäre Phasen im System Al–Te / Phase Relations and Intermediate Phases in the Al–Te System, Zeitschrift für Naturforschung B 43, 182-188 (1988).  
_cited as the source of values for this phase_

## AL2TE5 (Al–Te)

- Id: `phase:al-te:al2te5`; status `assigned`
- Structure: Al2Te5 · mC14 · C2/m (12); type `st:al2te5-mc14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.2857, Te 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 682.23–735.99 K, x(Te) 0.71429–0.71429
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:al2te5)

Names (3): _corpus: _corpus:phase:al-te:al2te5  
_paper: _paper:10.1007/s11669-019-00733-z:Al2Te5  
_tdb: _tdb:AlTe-19Shi.tdb:AL2TE5  


### TDB models of AL2TE5 (1): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): AL2TE5, type code %, sha256 `c52e1bafcdb91f7e…`

~~~~text
68: PHASE AL2TE5 % 2 2 5 !
69: CONST AL2TE5 : AL : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19966220611](https://doi.org/10.1002/zaac.19966220611) H. J. Deiseroth, P. Amann, H. Thurn, Die Pentatelluride M\<sub>2\</sub>Te\<sub>5\</sub> (M = Al, Ga, In): Polymorphie, Strukturbeziehungen und Homogenitätsbereiche, Zeitschrift anorg allge chemie 622, 985-993 (1996).  
_cited as the source of values for this phase_
- [doi:10.1515/znb-1988-0209](https://doi.org/10.1515/znb-1988-0209) Rüdiger Kniep, Peter Blees, Phasengleichgewichte und intermediäre Phasen im System Al–Te / Phase Relations and Intermediate Phases in the Al–Te System, Zeitschrift für Naturforschung B 43, 182-188 (1988).  
_cited as the source of values for this phase_

## ALTE (Al–Te)

- Id: `phase:al-te:alte`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Al1 Te1 at x(TE)=0.5000
- Candidate (literature_printed): (AlTe) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (AlTe) — Hallstedt 2025 mmc2 row for ALTE: AlTe
- Stoichiometry: Al 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1128.7 K, x(Te) 0.5–0.5
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:alte)

Names (3): _corpus: _corpus:phase:al-te:alte  
_paper: _paper:10.1007/s11669-019-00733-z:AlTe  
_tdb: _tdb:AlTe-19Shi.tdb:ALTE  


### TDB models of ALTE (1): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): ALTE, type code %, sha256 `c52e1bafcdb91f7e…`

~~~~text
53: PHASE ALTE % 2 1 1 !
54: CONST ALTE : AL : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/znb-1988-0209](https://doi.org/10.1515/znb-1988-0209) Rüdiger Kniep, Peter Blees, Phasengleichgewichte und intermediäre Phasen im System Al–Te / Phase Relations and Intermediate Phases in the Al–Te System, Zeitschrift für Naturforschung B 43, 182-188 (1988).  
_cited as the source of values for this phase_

## BCC_A2 (Al–Te)

- Id: `phase:al-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:bcc-a2)

Names (3): _corpus: _corpus:phase:al-te:bcc-a2  
_tdb: _tdb:AlTe-19Shi.tdb:BCC_A2, tdb:AlTe-93Oh.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): BCC_A2, type code %B, sha256 `c52e1bafcdb91f7e…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL : VA : !
~~~~

[AlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-93Oh.tdb): BCC_A2, type code %B, sha256 `a95e02f39b2e3292…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : AL : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## FCC_A1 (Al–Te)

- Id: `phase:al-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–933.47 K, x(Te) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:fcc-a1)

Names (4): _corpus: _corpus:phase:al-te:fcc-a1  
_paper: _paper:10.1007/s11669-019-00733-z:(Al)  
_tdb: _tdb:AlTe-19Shi.tdb:FCC_A1, tdb:AlTe-93Oh.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): FCC_A1, type code %A, sha256 `c52e1bafcdb91f7e…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL : VA : !
~~~~

[AlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-93Oh.tdb): FCC_A1, type code %A, sha256 `a95e02f39b2e3292…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AL : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_
- [doi:10.1515/znb-1988-0209](https://doi.org/10.1515/znb-1988-0209) Rüdiger Kniep, Peter Blees, Phasengleichgewichte und intermediäre Phasen im System Al–Te / Phase Relations and Intermediate Phases in the Al–Te System, Zeitschrift für Naturforschung B 43, 182-188 (1988).  
_cited as the source of values for this phase_

## HCP_A3 (Al–Te)

- Id: `phase:al-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:hcp-a3)

Names (3): _corpus: _corpus:phase:al-te:hcp-a3  
_tdb: _tdb:AlTe-19Shi.tdb:HCP_A3, tdb:AlTe-93Oh.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): HCP_A3, type code %A, sha256 `c52e1bafcdb91f7e…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AL : VA: !
~~~~

[AlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-93Oh.tdb): HCP_A3, type code %A, sha256 `a95e02f39b2e3292…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : AL : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## ION (Al–Te)

- Id: `phase:al-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 567.29–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:ion)

Names (2): _corpus: _corpus:phase:al-te:ion  
_tdb: _tdb:AlTe-93Oh.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[AlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-93Oh.tdb): ION, type code %, sha256 `a95e02f39b2e3292…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : AL+3 : TE-2 VA TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## LIQUID (Al–Te)

- Id: `phase:al-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 699.65–2500 K, x(Te) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-te:liquid)

Names (5): _corpus: _corpus:phase:al-te:liquid  
_paper: _paper:10.1007/s11669-019-00733-z:L, paper:10.1007/s11669-019-00733-z:L1, paper:10.1007/s11669-019-00733-z:L2  
_tdb: _tdb:AlTe-19Shi.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AlTe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb): LIQUID, type code %, sha256 `c52e1bafcdb91f7e…`

~~~~text
28: PHASE LIQUID % 1 1 !
29: CONST LIQUID :AL AL2TE3 TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/znb-1988-0209](https://doi.org/10.1515/znb-1988-0209) Rüdiger Kniep, Peter Blees, Phasengleichgewichte und intermediäre Phasen im System Al–Te / Phase Relations and Intermediate Phases in the Al–Te System, Zeitschrift für Naturforschung B 43, 182-188 (1988).  
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
