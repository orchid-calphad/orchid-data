# Bi–Ti phases

> Bi–Ti system: 11 phases (tier A 4, tier B 1, tier C 1, liquid 1, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-TI.html · Markdown: https://data.orchid-project.org/phases/pages/BI-TI.md

11 phases (tier A 4, tier B 1, tier C 1, liquid 1, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-TI) · [full JSON](https://data.orchid-project.org/phases/systems/BI-TI.json) · [Bi–Ti system page](https://data.orchid-project.org/systems/BI-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Ti system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-ti-a7-rhombohedral); _phase:bi-ti:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.54 K, x(Ti) 0–0 | 2 | 2 |
| [BCC_A2](#phase-bi-ti-bcc-a2); _phase:bi-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 992.62–2499.73 K, x(Ti) 0.89524–1 | 4 | 2 |
| [BI2TI](#phase-bi-ti-bi2ti); _phase:bi-ti:bi2ti_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–960.59 K, x(Ti) 0.33333–0.33333 | 4 | 2 |
| [BI2TI3](#phase-bi-ti-bi2ti3); _phase:bi-ti:bi2ti3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1249.02 K, x(Ti) 0.6–0.6 | 4 | 1 |
| [BI3TI2](#phase-bi-ti-bi3ti2); _phase:bi-ti:bi3ti2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1090.32 K, x(Ti) 0.4–0.4 | 0 | 1 |
| [BI9TI8](#phase-bi-ti-bi9ti8); _phase:bi-ti:bi9ti8_ | Sb9V8 · tP34 · P4/nmm (129) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–1270.95 K, x(Ti) 0.47059–0.47059 | 4 | 2 |
| [BITI2](#phase-bi-ti-biti2); _phase:bi-ti:biti2_ | BiTi2 · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1562.61 K, x(Ti) 0.66667–0.66667 | 3 | 2 |
| [BITI3](#phase-bi-ti-biti3); _phase:bi-ti:biti3_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1629.43 K, x(Ti) 0.75–0.75 | 5 | 2 |
| [FCC_A1](#phase-bi-ti-fcc-a1); _phase:bi-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-bi-ti-hcp-a3); _phase:bi-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1579.99 K, x(Ti) 0.99537–1 | 2 | 2 |
| [LIQUID](#phase-bi-ti-liquid); _phase:bi-ti:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 544.53–2500 K, x(Ti) 0–1 | 11 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Ti)

- Id: `phase:bi-ti:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.54 K, x(Ti) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:a7-rhombohedral)

Names (5): _corpus: _corpus:phase:bi-ti:a7-rhombohedral, corpus:phase:bi-ti:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2014.01.001:(Bi)  
_tdb: _tdb:BiTi-13Cao.tdb:RHOMBOHEDRAL_A7, tdb:BiTi-14Hua.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `00f08d653a2c924a…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6b2fb177d2031c50…`

~~~~text
55: PHASE RHOMBOHEDRAL_A7 % 1 1 !
56: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0243-0](https://doi.org/10.1007/s11669-013-0243-0) Sho Maruyama, Yuya Kado, Tetsuya Uda, Phase Diagram Investigations of the Bi-Ti System, J. Phase Equilib. Diffus. 34, 289-296 (2013).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Ti)

- Id: `phase:bi-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 992.62–2499.73 K, x(Ti) 0.89524–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:bcc-a2)

Names (4): _corpus: _corpus:phase:bi-ti:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.01.001:(βTi)  
_tdb: _tdb:BiTi-13Cao.tdb:BCC_A2, tdb:BiTi-14Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): BCC_A2, type code %B, sha256 `00f08d653a2c924a…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : BI TI% : VA : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): BCC_A2, type code %B, sha256 `6b2fb177d2031c50…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : BI TI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_

## BI2TI (Bi–Ti)

- Id: `phase:bi-ti:bi2ti`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): Fddd (70) — on-hull OQMD Bi2 Ti1 at x(TI)=0.3333
- Candidate (literature_printed): (Bi2Ti) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Bi2Ti) — Hallstedt 2025 mmc2 row for BI2TI: Bi2Ti
- Stoichiometry: Bi 0.6667, Ti 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–960.59 K, x(Ti) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:bi2ti)

Names (4): _corpus: _corpus:phase:bi-ti:bi2ti  
_paper: _paper:10.1016/j.calphad.2014.01.001:Bi2Ti  
_tdb: _tdb:BiTi-13Cao.tdb:BI2TI, tdb:BiTi-14Hua.tdb:BI2TI  


### TDB models of BI2TI (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): BI2TI, type code %, sha256 `00f08d653a2c924a…`

~~~~text
49: PHASE BI2TI % 2 2 1 !
50: CONST BI2TI : BI : TI : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): BI2TI, type code %, sha256 `6b2fb177d2031c50…`

~~~~text
60: PHASE BI2TI % 2 2 1 !
61: CONST BI2TI : BI : TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0243-0](https://doi.org/10.1007/s11669-013-0243-0) Sho Maruyama, Yuya Kado, Tetsuya Uda, Phase Diagram Investigations of the Bi-Ti System, J. Phase Equilib. Diffus. 34, 289-296 (2013).  
_cited as the source of values for this phase_

## BI2TI3 (Bi–Ti)

- Id: `phase:bi-ti:bi2ti3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Bi2Ti3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Bi2Ti3) — Hallstedt 2025 mmc2 row for BI2TI3: Bi2Ti3
- Stoichiometry: Bi 0.4000, Ti 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1249.02 K, x(Ti) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:bi2ti3)

Names (3): _corpus: _corpus:phase:bi-ti:bi2ti3  
_paper: _paper:10.1016/j.calphad.2014.01.001:Bi2Ti3  
_tdb: _tdb:BiTi-14Hua.tdb:BI2TI3  


### TDB models of BI2TI3 (1): PHASE and CONSTITUENT statements as written

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): BI2TI3, type code %, sha256 `6b2fb177d2031c50…`

~~~~text
70: PHASE BI2TI3 % 2 2 3 !
71: CONST BI2TI3 : BI : TI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-013-0243-0](https://doi.org/10.1007/s11669-013-0243-0) Sho Maruyama, Yuya Kado, Tetsuya Uda, Phase Diagram Investigations of the Bi-Ti System, J. Phase Equilib. Diffus. 34, 289-296 (2013).  
_cited as the source of values for this phase_

## BI3TI2 (Bi–Ti)

- Id: `phase:bi-ti:bi3ti2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Bi3Ti2) — Hallstedt 2025 mmc2 row for BI3TI2: Bi3Ti2
- Stoichiometry: Bi 0.6000, Ti 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1090.32 K, x(Ti) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:bi3ti2)

Names (2): _corpus: _corpus:phase:bi-ti:bi3ti2  
_tdb: _tdb:BiTi-13Cao.tdb:BI3TI2  


### TDB models of BI3TI2 (1): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): BI3TI2, type code %, sha256 `00f08d653a2c924a…`

~~~~text
54: PHASE BI3TI2 % 2 3 2 !
55: CONST BI3TI2 : BI : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_

## BI9TI8 (Bi–Ti)

- Id: `phase:bi-ti:bi9ti8`; status `assigned`
- Structure: Sb9V8 · tP34 · P4/nmm (129); type `st:sb9v8-tp34`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Bi 0.5294, Ti 0.4706
- Stability: stable in 2 of 2 calculated diagram(s): 300–1270.95 K, x(Ti) 0.47059–0.47059
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:bi9ti8)

Names (6): _corpus: _corpus:phase:bi-ti:bi9ti8  
_mp: _mp:mp-aaabkkvd  
_oqmd: _oqmd:oqmd-19247  
_paper: _paper:10.1016/j.calphad.2014.01.001:Bi9Ti8  
_tdb: _tdb:BiTi-13Cao.tdb:BI9TI8, tdb:BiTi-14Hua.tdb:BI9TI8  


### TDB models of BI9TI8 (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): BI9TI8, type code %, sha256 `00f08d653a2c924a…`

~~~~text
59: PHASE BI9TI8 % 2 9 8 !
60: CONST BI9TI8 : BI : TI : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): BI9TI8, type code %, sha256 `6b2fb177d2031c50…`

~~~~text
65: PHASE BI9TI8 % 2 9 8 !
66: CONST BI9TI8 : BI : TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0243-0](https://doi.org/10.1007/s11669-013-0243-0) Sho Maruyama, Yuya Kado, Tetsuya Uda, Phase Diagram Investigations of the Bi-Ti System, J. Phase Equilib. Diffus. 34, 289-296 (2013).  
_cited as the source of values for this phase_

## BITI2 (Bi–Ti)

- Id: `phase:bi-ti:biti2`; status `assigned`
- Structure: BiTi2 · tI12 · I4/mmm (139); type `st:biti2-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3333, Ti 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1562.61 K, x(Ti) 0.66667–0.66667
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:biti2)

Names (4): _corpus: _corpus:phase:bi-ti:biti2  
_paper: _paper:10.1016/j.calphad.2014.01.001:BiTi2  
_tdb: _tdb:BiTi-13Cao.tdb:BITI2, tdb:BiTi-14Hua.tdb:BITI2  


### TDB models of BITI2 (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): BITI2, type code %, sha256 `00f08d653a2c924a…`

~~~~text
64: PHASE BITI2 % 2 1 2 !
65: CONST BITI2 : BI : TI : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): BITI2, type code %, sha256 `6b2fb177d2031c50…`

~~~~text
75: PHASE BITI2 % 2 1 2 !
76: CONST BITI2 : BI : TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0243-0](https://doi.org/10.1007/s11669-013-0243-0) Sho Maruyama, Yuya Kado, Tetsuya Uda, Phase Diagram Investigations of the Bi-Ti System, J. Phase Equilib. Diffus. 34, 289-296 (2013).  
_cited as the source of values for this phase_

## BITI3 (Bi–Ti)

- Id: `phase:bi-ti:biti3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): Pm-3n (223) — on-hull OQMD Bi1 Ti3 at x(TI)=0.7500
- Candidate (literature_printed): (BiTi3) · t\*\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (BiTi3) — Hallstedt 2025 mmc2 row for BITI3: BiTi3
- Stoichiometry: Bi 0.2500, Ti 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1629.43 K, x(Ti) 0.75–0.75
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:biti3)

Names (4): _corpus: _corpus:phase:bi-ti:biti3  
_paper: _paper:10.1016/j.calphad.2014.01.001:BiTi3  
_tdb: _tdb:BiTi-13Cao.tdb:BITI3, tdb:BiTi-14Hua.tdb:BITI3  


### TDB models of BITI3 (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): BITI3, type code %, sha256 `00f08d653a2c924a…`

~~~~text
69: PHASE BITI3 % 2 1 3 !
70: CONST BITI3 : BI : TI : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): BITI3, type code %, sha256 `6b2fb177d2031c50…`

~~~~text
80: PHASE BITI3 % 2 1 3 !
81: CONST BITI3 : BI : TI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_

## FCC_A1 (Bi–Ti)

- Id: `phase:bi-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-ti:fcc-a1  
_tdb: _tdb:BiTi-13Cao.tdb:FCC_A1, tdb:BiTi-14Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): FCC_A1, type code %A, sha256 `00f08d653a2c924a…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : BI TI : VA : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): FCC_A1, type code %A, sha256 `6b2fb177d2031c50…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : BI TI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_

## HCP_A3 (Bi–Ti)

- Id: `phase:bi-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1579.99 K, x(Ti) 0.99537–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:hcp-a3)

Names (4): _corpus: _corpus:phase:bi-ti:hcp-a3  
_paper: _paper:10.1016/j.calphad.2014.01.001:(αTi)  
_tdb: _tdb:BiTi-13Cao.tdb:HCP_A3, tdb:BiTi-14Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): HCP_A3, type code %A, sha256 `00f08d653a2c924a…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : BI TI% : VA: !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): HCP_A3, type code %A, sha256 `6b2fb177d2031c50…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : BI TI% : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_

## LIQUID (Bi–Ti)

- Id: `phase:bi-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 544.53–2500 K, x(Ti) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ti:liquid)

Names (4): _corpus: _corpus:phase:bi-ti:liquid  
_paper: _paper:10.1016/j.calphad.2014.01.001:L  
_tdb: _tdb:BiTi-13Cao.tdb:LIQUID, tdb:BiTi-14Hua.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiTi-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-13Cao.tdb): LIQUID, type code %, sha256 `00f08d653a2c924a…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : BI TI : !
~~~~

[BiTi-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTi-14Hua.tdb): LIQUID, type code %, sha256 `6b2fb177d2031c50…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : BI TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.01.001](https://doi.org/10.1016/j.calphad.2014.01.001) L.H. Huang, Q. Chen, Y. He, X.M. Tao, G.M. Cai, H.S. Liu et al., Thermodynamic modeling of Fe–Ti–Bi system assisted with key experiments, Calphad 46, 34-41 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0243-0](https://doi.org/10.1007/s11669-013-0243-0) Sho Maruyama, Yuya Kado, Tetsuya Uda, Phase Diagram Investigations of the Bi-Ti System, J. Phase Equilib. Diffus. 34, 289-296 (2013).  
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
