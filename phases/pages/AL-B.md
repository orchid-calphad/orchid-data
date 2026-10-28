# Al–B phases

> Al–B system: 9 phases (tier A 4, tier C 2, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-B.html · Markdown: https://data.orchid-project.org/phases/pages/AL-B.md

9 phases (tier A 4, tier C 2, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-B) · [full JSON](https://data.orchid-project.org/phases/systems/AL-B.json) · [Al–B system page](https://data.orchid-project.org/systems/AL-B.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-B.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–B system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2B3](#phase-al-b-al2b3); _phase:al-b:al2b3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–775.32 K, x(B) 0.6–0.6 | 3 | 1 |
| [ALB12_ALPHA](#phase-al-b-alb12-alpha); _phase:al-b:alb12-alpha_ | alpha-AlB12 · tP216 · P4_12_12 (92) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–2367.09 K, x(B) 0.92308–0.92308 | 10 | 5 |
| [ALB12_BETA](#phase-al-b-alb12-beta); _phase:al-b:alb12-beta_ | beta-AlB12 · oP384 · P2_12_12_1 (19) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1826.25–2448.45 K, x(B) 0.92308–0.92308 | 0 | 1 |
| [ALB2_C32](#phase-al-b-alb2-c32); _phase:al-b:alb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1303.12 K, x(B) 0.66667–0.66667 | 13 | 5 |
| [BETA_RHOMBO_B](#phase-al-b-b-beta-rhombo); _phase:al-b:b-beta-rhombo_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–3999.88 K, x(B) 0.97485–1 | 4 | 5 |
| [BCC_A2](#phase-al-b-bcc-a2); _phase:al-b:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-al-b-fcc-a1); _phase:al-b:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–935.04 K, x(B) 0–0.0031 | 10 | 5 |
| [HCP_A3](#phase-al-b-hcp-a3); _phase:al-b:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-al-b-liquid); _phase:al-b:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 932.64–4000 K, x(B) 0–1 | 18 | 5 |

## AL2B3 (Al–B)

- Id: `phase:al-b:al2b3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Al2B3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Al2B3) — Hallstedt 2025 mmc2 row for AL2B3: Al2B3
- Stoichiometry: Al 0.4000, B 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–775.32 K, x(B) 0.6–0.6
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:al2b3)

Names (3): _corpus: _corpus:phase:al-b:al2b3  
_paper: _paper:10.1361/105497199770340743:Al2B3  
_tdb: _tdb:AlB-99Cam.tdb:AL2B3  


### TDB models of AL2B3 (1): PHASE and CONSTITUENT statements as written

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): AL2B3, type code %, sha256 `4d78ca2cbf5a4096…`

~~~~text
50: PHASE AL2B3 % 2 2 3 !
51: CONST AL2B3 : AL : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0956-7151(92)90080-x](https://doi.org/10.1016/0956-7151%2892%2990080-x) R.G. Vardiman, Microstructures in aluminum ion implanted with boron and heat treated, Acta Metallurgica et Materialia 40, 1029-1035 (1992).  
_cited as the source of values for this phase_

## ALB12_ALPHA (Al–B)

- Id: `phase:al-b:alb12-alpha`; status `assigned`
- Structure: alpha-AlB12 · tP216 · P4_12_12 (92); type `st:alpha-alb12-tp216`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.0769, B 0.9231
- Stability: stable in 5 of 5 calculated diagram(s): 300–2367.09 K, x(B) 0.92308–0.92308
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:alb12-alpha)

Names (9): _corpus: _corpus:phase:al-b:alb12-alpha  
_paper: _paper:10.1016/j.jallcom.2004.04.100:AlB12, paper:10.1361/105497199770340743:AlB12, paper:sha256-85fd53a1a176b694:AlB12-L  
_tdb: _tdb:AlB-01Luk-LB.tdb:ALB12_ALPHA, tdb:AlB-04Mir.tdb:ALB12_ALPHA, tdb:AlB-15Wan.tdb:ALB12_ALPHA, tdb:AlB-98Luk.tdb:ALB12_ALPHA, tdb:AlB-99Cam.tdb:ALB12_ALPHA  


### TDB models of ALB12_ALPHA (5): PHASE and CONSTITUENT statements as written

[AlB-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-01Luk-LB.tdb): ALB12_ALPHA, type code %, sha256 `642c909d17cc2a6b…`

~~~~text
61: PHASE ALB12_ALPHA % 2 1 12 !
62: CONST ALB12_ALPHA : AL : B : !
~~~~

[AlB-04Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-04Mir.tdb): ALB12_ALPHA, type code %, sha256 `47801a2129a7f1f2…`

~~~~text
60: PHASE AlB12_ALPHA % 2 1 12 !
61: CONST AlB12_ALPHA : AL : B : !
~~~~

[AlB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-15Wan.tdb): ALB12_ALPHA, type code %, sha256 `45a52a0572a39025…`

~~~~text
57: PHASE AlB12_ALPHA % 2 1 12 !
58: CONST AlB12_ALPHA : AL : B : !
~~~~

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): ALB12_ALPHA, type code %, sha256 `564969ba25933e9f…`

~~~~text
57: PHASE AlB12_ALPHA % 2 1 12 !
58: CONST AlB12_ALPHA : AL : B : !
~~~~

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): ALB12_ALPHA, type code %, sha256 `4d78ca2cbf5a4096…`

~~~~text
60: PHASE AlB12_ALPHA % 2 1 12 !
61: CONST AlB12_ALPHA : AL : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.100](https://doi.org/10.1016/j.jallcom.2004.04.100) Djordje Mirković, Joachim Gröbner, Rainer Schmid-Fetzer, Olga Fabrichnaya, Hans Leo Lukas, Experimental study and thermodynamic re-assessment of the Al–B system, Journal of Alloys and Compounds 384, 168-174 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1007/bf02649415](https://doi.org/10.1007/bf02649415) H. Duschanek, P. Rogl, The Al-B (aluminum-boron) system, JPE 15, 543-552 (1994).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645112](https://doi.org/10.1007/bf02645112) Geoffrey K. Sigworth, The Grain Refining of Aluminum and Phase Relationships in the Al-Ti-B System, Metall Trans A 15, 277-282 (1984).  
_cited as the source of values for this phase_

## ALB12_BETA (Al–B)

- Id: `phase:al-b:alb12-beta`; status `assigned`
- Structure: beta-AlB12 · oP384 · P2_12_12_1 (19); type `st:beta-alb12-op384`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.0769, B 0.9231
- Stability: stable in 1 of 1 calculated diagram(s): 1826.25–2448.45 K, x(B) 0.92308–0.92308
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:alb12-beta)

Names (2): _corpus: _corpus:phase:al-b:alb12-beta  
_tdb: _tdb:AlB-98Luk.tdb:ALB12_BETA  


### TDB models of ALB12_BETA (1): PHASE and CONSTITUENT statements as written

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): ALB12_BETA, type code %, sha256 `564969ba25933e9f…`

~~~~text
62: PHASE AlB12_BETA % 2 1 12 !
63: CONST AlB12_BETA : AL : B : !
~~~~

## ALB2_C32 (Al–B)

- Id: `phase:al-b:alb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.3333, B 0.6667
- Stability: stable in 5 of 5 calculated diagram(s): 300–1303.12 K, x(B) 0.66667–0.66667
- Literature: 13 values (13 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:alb2-c32)

Names (9): _corpus: _corpus:phase:al-b:alb2-c32  
_paper: _paper:10.1016/j.jallcom.2004.04.100:AlB2, paper:10.1361/105497199770340743:AlB2, paper:sha256-85fd53a1a176b694:AlB2  
_tdb: _tdb:AlB-01Luk-LB.tdb:ALB2_C32, tdb:AlB-04Mir.tdb:ALB2_C32, tdb:AlB-15Wan.tdb:ALB2_C32, tdb:AlB-98Luk.tdb:ALB2_C32, tdb:AlB-99Cam.tdb:ALB2_C32  


### TDB models of ALB2_C32 (5): PHASE and CONSTITUENT statements as written

[AlB-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-01Luk-LB.tdb): ALB2_C32, type code %, sha256 `642c909d17cc2a6b…`

~~~~text
56: PHASE ALB2_C32 % 2 1 2 !
57: CONST ALB2_C32 : AL : B : !
~~~~

[AlB-04Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-04Mir.tdb): ALB2_C32, type code %, sha256 `47801a2129a7f1f2…`

~~~~text
55: PHASE ALB2_C32 % 2 1 2 !
56: CONST ALB2_C32 : AL : B : !
~~~~

[AlB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-15Wan.tdb): ALB2_C32, type code %, sha256 `45a52a0572a39025…`

~~~~text
52: PHASE ALB2_C32 % 2 1 2 !
53: CONST ALB2_C32 : AL : B : !
~~~~

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): ALB2_C32, type code %, sha256 `564969ba25933e9f…`

~~~~text
52: PHASE ALB2_C32 % 2 1 2 !
53: CONST ALB2_C32 : AL : B : !
~~~~

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): ALB2_C32, type code %, sha256 `4d78ca2cbf5a4096…`

~~~~text
55: PHASE ALB2_C32 % 2 1 2 !
56: CONST ALB2_C32 : AL : B : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.100](https://doi.org/10.1016/j.jallcom.2004.04.100) Djordje Mirković, Joachim Gröbner, Rainer Schmid-Fetzer, Olga Fabrichnaya, Hans Leo Lukas, Experimental study and thermodynamic re-assessment of the Al–B system, Journal of Alloys and Compounds 384, 168-174 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1007/bf02645112](https://doi.org/10.1007/bf02645112) Geoffrey K. Sigworth, The Grain Refining of Aluminum and Phase Relationships in the Al-Ti-B System, Metall Trans A 15, 277-282 (1984).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02649415](https://doi.org/10.1007/bf02649415) H. Duschanek, P. Rogl, The Al-B (aluminum-boron) system, JPE 15, 543-552 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/0956-7151(92)90080-x](https://doi.org/10.1016/0956-7151%2892%2990080-x) R.G. Vardiman, Microstructures in aluminum ion implanted with boron and heat treated, Acta Metallurgica et Materialia 40, 1029-1035 (1992).  
_cited as the source of values for this phase_

## BETA_RHOMBO_B (Al–B)

- Id: `phase:al-b:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AlB-01Luk-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AlB-04Mir.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AlB-15Wan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AlB-98Luk.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AlB-99Cam.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 5 of 5 calculated diagram(s): 300–3999.88 K, x(B) 0.97485–1
- Literature: 4 values (4 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:b-beta-rhombo)

Names (10): _corpus: _corpus:phase:al-b:b-beta-rhombo, corpus:phase:al-b:beta-rhombo-b  
_paper: _paper:10.1016/j.jallcom.2004.04.100:β-B, paper:10.1361/105497199770340743:β, paper:sha256-85fd53a1a176b694:β-rhombo-B  
_tdb: _tdb:AlB-01Luk-LB.tdb:BETA_RHOMBO_B, tdb:AlB-04Mir.tdb:BETA_RHOMBO_B, tdb:AlB-15Wan.tdb:BETA_RHOMBO_B, tdb:AlB-98Luk.tdb:BETA_RHOMBO_B, tdb:AlB-99Cam.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (5): PHASE and CONSTITUENT statements as written

[AlB-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-01Luk-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `642c909d17cc2a6b…`

~~~~text
51: PHASE BETA_RHOMBO_B % 2 93 12 !
52: CONST BETA_RHOMBO_B : B : B : !
~~~~

[AlB-04Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-04Mir.tdb): BETA_RHOMBO_B, type code %, sha256 `47801a2129a7f1f2…`

~~~~text
50: PHASE BETA_RHOMBO_B % 2 93 12 !
51: CONST BETA_RHOMBO_B : B : B : !
~~~~

[AlB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-15Wan.tdb): BETA_RHOMBO_B, type code %, sha256 `45a52a0572a39025…`

~~~~text
47: PHASE BETA_RHOMBO_B % 1 1 !
48: CONST BETA_RHOMBO_B : B : !
~~~~

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): BETA_RHOMBO_B, type code %, sha256 `564969ba25933e9f…`

~~~~text
47: PHASE BETA_RHOMBO_B % 2 93 12 !
48: CONST BETA_RHOMBO_B : B : B : !
~~~~

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): BETA_RHOMBO_B, type code %, sha256 `4d78ca2cbf5a4096…`

~~~~text
45: PHASE BETA_RHOMBO_B % 1 1 !
46: CONST BETA_RHOMBO_B : AL B% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.100](https://doi.org/10.1016/j.jallcom.2004.04.100) Djordje Mirković, Joachim Gröbner, Rainer Schmid-Fetzer, Olga Fabrichnaya, Hans Leo Lukas, Experimental study and thermodynamic re-assessment of the Al–B system, Journal of Alloys and Compounds 384, 168-174 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1007/bf02649415](https://doi.org/10.1007/bf02649415) H. Duschanek, P. Rogl, The Al-B (aluminum-boron) system, JPE 15, 543-552 (1994).  
_cited as the source of values for this phase_

## BCC_A2 (Al–B)

- Id: `phase:al-b:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:bcc-a2)

Names (6): _corpus: _corpus:phase:al-b:bcc-a2  
_tdb: _tdb:AlB-01Luk-LB.tdb:BCC_A2, tdb:AlB-04Mir.tdb:BCC_A2, tdb:AlB-15Wan.tdb:BCC_A2, tdb:AlB-98Luk.tdb:BCC_A2, tdb:AlB-99Cam.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[AlB-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-01Luk-LB.tdb): BCC_A2, type code %B, sha256 `642c909d17cc2a6b…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : AL : B VA% : !
~~~~

[AlB-04Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-04Mir.tdb): BCC_A2, type code %B, sha256 `47801a2129a7f1f2…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : AL : B VA% : !
~~~~

[AlB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-15Wan.tdb): BCC_A2, type code %B, sha256 `45a52a0572a39025…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL% B : VA : !
~~~~

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): BCC_A2, type code %B, sha256 `564969ba25933e9f…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL B : VA : !
~~~~

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): BCC_A2, type code %B, sha256 `4d78ca2cbf5a4096…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL : B VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.100](https://doi.org/10.1016/j.jallcom.2004.04.100) Djordje Mirković, Joachim Gröbner, Rainer Schmid-Fetzer, Olga Fabrichnaya, Hans Leo Lukas, Experimental study and thermodynamic re-assessment of the Al–B system, Journal of Alloys and Compounds 384, 168-174 (2004).  
_assessment that models this phase_
- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase_

## FCC_A1 (Al–B)

- Id: `phase:al-b:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–935.04 K, x(B) 0–0.0031
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:fcc-a1)

Names (9): _corpus: _corpus:phase:al-b:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2004.04.100:fcc, paper:10.1361/105497199770340743:Al, paper:sha256-85fd53a1a176b694:fcc-Al  
_tdb: _tdb:AlB-01Luk-LB.tdb:FCC_A1, tdb:AlB-04Mir.tdb:FCC_A1, tdb:AlB-15Wan.tdb:FCC_A1, tdb:AlB-98Luk.tdb:FCC_A1, tdb:AlB-99Cam.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[AlB-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-01Luk-LB.tdb): FCC_A1, type code %A, sha256 `642c909d17cc2a6b…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AL : B VA% : !
~~~~

[AlB-04Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-04Mir.tdb): FCC_A1, type code %A, sha256 `47801a2129a7f1f2…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : AL : B VA% : !
~~~~

[AlB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-15Wan.tdb): FCC_A1, type code %A, sha256 `45a52a0572a39025…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% B : VA : !
~~~~

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): FCC_A1, type code %A, sha256 `564969ba25933e9f…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% B : VA : !
~~~~

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): FCC_A1, type code %A, sha256 `4d78ca2cbf5a4096…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL : B VA% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.100](https://doi.org/10.1016/j.jallcom.2004.04.100) Djordje Mirković, Joachim Gröbner, Rainer Schmid-Fetzer, Olga Fabrichnaya, Hans Leo Lukas, Experimental study and thermodynamic re-assessment of the Al–B system, Journal of Alloys and Compounds 384, 168-174 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1007/bf02645112](https://doi.org/10.1007/bf02645112) Geoffrey K. Sigworth, The Grain Refining of Aluminum and Phase Relationships in the Al-Ti-B System, Metall Trans A 15, 277-282 (1984).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02841717](https://doi.org/10.1007/bf02841717) O.N. Carlson, The Al-B System, Bull. Alloy Phase Diagrams, Vol 11, 1990, p 560-566 496  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0956-7151(92)90080-x](https://doi.org/10.1016/0956-7151%2892%2990080-x) R.G. Vardiman, Microstructures in aluminum ion implanted with boron and heat treated, Acta Metallurgica et Materialia 40, 1029-1035 (1992).  
_cited as the source of values for this phase_

## HCP_A3 (Al–B)

- Id: `phase:al-b:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:hcp-a3)

Names (6): _corpus: _corpus:phase:al-b:hcp-a3  
_tdb: _tdb:AlB-01Luk-LB.tdb:HCP_A3, tdb:AlB-04Mir.tdb:HCP_A3, tdb:AlB-15Wan.tdb:HCP_A3, tdb:AlB-98Luk.tdb:HCP_A3, tdb:AlB-99Cam.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[AlB-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-01Luk-LB.tdb): HCP_A3, type code %A, sha256 `642c909d17cc2a6b…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : AL : B VA% : !
~~~~

[AlB-04Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-04Mir.tdb): HCP_A3, type code %A, sha256 `47801a2129a7f1f2…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : AL : B VA% : !
~~~~

[AlB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-15Wan.tdb): HCP_A3, type code %A, sha256 `45a52a0572a39025…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL% B : VA : !
~~~~

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): HCP_A3, type code %A, sha256 `564969ba25933e9f…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL B : VA : !
~~~~

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): HCP_A3, type code %A, sha256 `4d78ca2cbf5a4096…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL : B VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.100](https://doi.org/10.1016/j.jallcom.2004.04.100) Djordje Mirković, Joachim Gröbner, Rainer Schmid-Fetzer, Olga Fabrichnaya, Hans Leo Lukas, Experimental study and thermodynamic re-assessment of the Al–B system, Journal of Alloys and Compounds 384, 168-174 (2004).  
_assessment that models this phase_
- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase_

## LIQUID (Al–B)

- Id: `phase:al-b:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 932.64–4000 K, x(B) 0–1
- Literature: 18 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-b:liquid)

Names (9): _corpus: _corpus:phase:al-b:liquid  
_paper: _paper:10.1016/j.jallcom.2004.04.100:Liquid, paper:10.1361/105497199770340743:L, paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:AlB-01Luk-LB.tdb:LIQUID, tdb:AlB-04Mir.tdb:LIQUID, tdb:AlB-15Wan.tdb:LIQUID, tdb:AlB-98Luk.tdb:LIQUID, tdb:AlB-99Cam.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[AlB-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-01Luk-LB.tdb): LIQUID, type code %, sha256 `642c909d17cc2a6b…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : AL B : !
~~~~

[AlB-04Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-04Mir.tdb): LIQUID, type code %, sha256 `47801a2129a7f1f2…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : AL B : !
~~~~

[AlB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-15Wan.tdb): LIQUID, type code %, sha256 `45a52a0572a39025…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL B : !
~~~~

[AlB-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-98Luk.tdb): LIQUID, type code %, sha256 `564969ba25933e9f…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL B : !
~~~~

[AlB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlB-99Cam.tdb): LIQUID, type code %, sha256 `4d78ca2cbf5a4096…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL B : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.100](https://doi.org/10.1016/j.jallcom.2004.04.100) Djordje Mirković, Joachim Gröbner, Rainer Schmid-Fetzer, Olga Fabrichnaya, Hans Leo Lukas, Experimental study and thermodynamic re-assessment of the Al–B system, Journal of Alloys and Compounds 384, 168-174 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1007/bf02645112](https://doi.org/10.1007/bf02645112) Geoffrey K. Sigworth, The Grain Refining of Aluminum and Phase Relationships in the Al-Ti-B System, Metall Trans A 15, 277-282 (1984).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02649415](https://doi.org/10.1007/bf02649415) H. Duschanek, P. Rogl, The Al-B (aluminum-boron) system, JPE 15, 543-552 (1994).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02841717](https://doi.org/10.1007/bf02841717) O.N. Carlson, The Al-B System, Bull. Alloy Phase Diagrams, Vol 11, 1990, p 560-566 496  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
