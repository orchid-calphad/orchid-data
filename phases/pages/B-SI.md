# B–Si phases

> B–Si system: 7 phases (tier A 1, tier C 1, liquid 1, needs_review 4); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-SI.html · Markdown: https://data.orchid-project.org/phases/pages/B-SI.md

7 phases (tier A 1, tier C 1, liquid 1, needs_review 4); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-SI) · [full JSON](https://data.orchid-project.org/phases/systems/B-SI.json) · [B–Si system page](https://data.orchid-project.org/systems/B-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Si system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-b-si-a4-diamond); _phase:b-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1687 K, x(B) 0–0.02376 | 16 | 4 |
| [ALPHA_RHOMBO_B](#phase-b-si-b-alpha-rhombo); _phase:b-si:b-alpha-rhombo_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2310.04 K, x(B) 0.94061–1 | 0 | 2 |
| [BETA_RHOMBO_B](#phase-b-si-b-beta-rhombo); _phase:b-si:b-beta-rhombo_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–2349 K, x(B) 0.96838–1 | 5 | 4 |
| [LIQUID](#phase-b-si-liquid); _phase:b-si:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1635.39–4000 K, x(B) 0–1 | 21 | 4 |
| [SIB24](#phase-b-si-sib24); _phase:b-si:sib24_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–2305.08 K, x(B) 0.94185–0.97581 | 10 | 3 |
| [SIB3_D1G](#phase-b-si-sib3-d1g); _phase:b-si:sib3-d1g_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1560 K, x(B) 0.7299–0.75 | 7 | 4 |
| [SIB6](#phase-b-si-sib6); _phase:b-si:sib6_ | SiB6 · oP280 · Pnnm (58) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–2129.74 K, x(B) 0.85438–0.86312 | 26 | 4 |

## DIAMOND_A4 (B–Si)

- Id: `phase:b-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1687 K, x(B) 0–0.02376
- Literature: 16 values (16 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-si:a4-diamond)

Names (9): _corpus: _corpus:phase:b-si:a4-diamond, corpus:phase:b-si:diamond-a4  
_paper: _paper:10.1016/j.jallcom.2009.03.044:(Si), paper:10.1361/105497101770338798:(Si), paper:sha256-85fd53a1a176b694:diamond  
_tdb: _tdb:SiB-01Tok.tdb:DIAMOND_A4, tdb:SiB-03Tok.tdb:DIAMOND_A4, tdb:SiB-09Che.tdb:DIAMOND_A4, tdb:SiB-95Lim-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-01Tok.tdb): DIAMOND_A4, type code %, sha256 `d151ee95b11739ec…`

~~~~text
27: PHASE DIAMOND_A4 % 1 1 !
28: CONST DIAMOND_A4 : B SI : !
~~~~

[SiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-03Tok.tdb): DIAMOND_A4, type code %, sha256 `200e70443756318e…`

~~~~text
29: PHASE DIAMOND_A4 % 1 1 !
30: CONST DIAMOND_A4 : B SI : !
~~~~

[SiB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-09Che.tdb): DIAMOND_A4, type code %, sha256 `306d09e27c26972d…`

~~~~text
27: PHASE DIAMOND_A4 % 1 1 !
28: CONST DIAMOND_A4 : B SI : !
~~~~

[SiB-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-95Lim-LB.tdb): DIAMOND_A4, type code %, sha256 `2706dcc211c225ff…`

~~~~text
32: PHASE DIAMOND_A4 % 1 1 !
33: CONST DIAMOND_A4 : B SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.044](https://doi.org/10.1016/j.jallcom.2009.03.044) H.M. Chen, H.Y. Qi, F. Zheng, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the B–C–Si system, Journal of Alloys and Compounds 481, 182-189 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.-K. Lim, H.L. Lukas, "Hochleistungskeramik, Herstellung, Aufbau und Eigenschaften", G. Petzow, J. Tobolski, R. Telle (Eds.), VCH, Weinheim, 1995, pp. 605-16.  
_assessment that models this phase_
- [doi:10.1007/bf02872900](https://doi.org/10.1007/bf02872900) R. W. Olesinski, G. J. Abbaschian, The B−Si (Boron-Silicon) system, Bulletin of Alloy Phase Diagrams 5, 478-484 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90225-3](https://doi.org/10.1016/0022-5088%2881%2990225-3) B Armas, G Male, D Salanoubat, C Chatillon, M Allibert, Determination of the boron-rich side of the BSi phase diagram, Journal of the Less Common Metals 82, 245-254 (1981).  
_cited as the source of values for this phase_

## ALPHA_RHOMBO_B (B–Si)

- Id: `phase:b-si:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — SiB-09Che.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — SiB-95Lim-LB.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–2310.04 K, x(B) 0.94061–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-si:b-alpha-rhombo)

Names (4): _corpus: _corpus:phase:b-si:b-alpha-rhombo, corpus:phase:b-si:alpha-rhombo-b  
_tdb: _tdb:SiB-09Che.tdb:ALPHA_RHOMBO_B, tdb:SiB-95Lim-LB.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[SiB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-09Che.tdb): ALPHA_RHOMBO_B, type code %, sha256 `306d09e27c26972d…`

~~~~text
37: PHASE ALPHA_RHOMBO_B % 1 1 !
38: CONST ALPHA_RHOMBO_B : B : !
~~~~

[SiB-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-95Lim-LB.tdb): ALPHA_RHOMBO_B, type code %, sha256 `2706dcc211c225ff…`

~~~~text
42: PHASE ALPHA_RHOMBO_B % 3 61 1 8 !
43: CONST ALPHA_RHOMBO_B : B : SI : B SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.-K. Lim, H.L. Lukas, "Hochleistungskeramik, Herstellung, Aufbau und Eigenschaften", G. Petzow, J. Tobolski, R. Telle (Eds.), VCH, Weinheim, 1995, pp. 605-16.  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.03.044](https://doi.org/10.1016/j.jallcom.2009.03.044) H.M. Chen, H.Y. Qi, F. Zheng, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the B–C–Si system, Journal of Alloys and Compounds 481, 182-189 (2009).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Si)

- Id: `phase:b-si:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — SiB-01Tok.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — SiB-03Tok.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — SiB-09Che.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — SiB-95Lim-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–2349 K, x(B) 0.96838–1
- Literature: 5 values (5 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-si:b-beta-rhombo)

Names (9): _corpus: _corpus:phase:b-si:b-beta-rhombo, corpus:phase:b-si:beta-rhombo-b  
_paper: _paper:10.1016/j.jallcom.2009.03.044:(B), paper:10.1361/105497101770338798:(B), paper:sha256-85fd53a1a176b694:β-rhombo-B  
_tdb: _tdb:SiB-01Tok.tdb:BETA_RHOMBO_B, tdb:SiB-03Tok.tdb:BETA_RHOMBO_B, tdb:SiB-09Che.tdb:BETA_RHOMBO_B, tdb:SiB-95Lim-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (4): PHASE and CONSTITUENT statements as written

[SiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-01Tok.tdb): BETA_RHOMBO_B, type code %, sha256 `d151ee95b11739ec…`

~~~~text
32: PHASE BETA_RHOMBO_B % 1 1 !
33: CONST BETA_RHOMBO_B : B SI : !
~~~~

[SiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-03Tok.tdb): BETA_RHOMBO_B, type code %, sha256 `200e70443756318e…`

~~~~text
34: PHASE BETA_RHOMBO_B % 1 1 !
35: CONST BETA_RHOMBO_B : B SI : !
~~~~

[SiB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-09Che.tdb): BETA_RHOMBO_B, type code %, sha256 `306d09e27c26972d…`

~~~~text
32: PHASE BETA_RHOMBO_B % 2 93 12 !
33: CONST BETA_RHOMBO_B : B : B SI : !
~~~~

[SiB-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-95Lim-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `2706dcc211c225ff…`

~~~~text
37: PHASE BETA_RHOMBO_B % 2 93 12 !
38: CONST BETA_RHOMBO_B : B : B SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.044](https://doi.org/10.1016/j.jallcom.2009.03.044) H.M. Chen, H.Y. Qi, F. Zheng, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the B–C–Si system, Journal of Alloys and Compounds 481, 182-189 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.-K. Lim, H.L. Lukas, "Hochleistungskeramik, Herstellung, Aufbau und Eigenschaften", G. Petzow, J. Tobolski, R. Telle (Eds.), VCH, Weinheim, 1995, pp. 605-16.  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.1007/bf02872900](https://doi.org/10.1007/bf02872900) R. W. Olesinski, G. J. Abbaschian, The B−Si (Boron-Silicon) system, Bulletin of Alloy Phase Diagrams 5, 478-484 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90225-3](https://doi.org/10.1016/0022-5088%2881%2990225-3) B Armas, G Male, D Salanoubat, C Chatillon, M Allibert, Determination of the boron-rich side of the BSi phase diagram, Journal of the Less Common Metals 82, 245-254 (1981).  
_cited as the source of values for this phase_

## LIQUID (B–Si)

- Id: `phase:b-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1635.39–4000 K, x(B) 0–1
- Literature: 21 values (21 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-si:liquid)

Names (8): _corpus: _corpus:phase:b-si:liquid  
_paper: _paper:10.1016/j.jallcom.2009.03.044:L, paper:10.1361/105497101770338798:L, paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:SiB-01Tok.tdb:LIQUID, tdb:SiB-03Tok.tdb:LIQUID, tdb:SiB-09Che.tdb:LIQUID, tdb:SiB-95Lim-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-01Tok.tdb): LIQUID, type code %, sha256 `d151ee95b11739ec…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : B SI : !
~~~~

[SiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-03Tok.tdb): LIQUID, type code %, sha256 `200e70443756318e…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B SI : !
~~~~

[SiB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-09Che.tdb): LIQUID, type code %, sha256 `306d09e27c26972d…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : B SI : !
~~~~

[SiB-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-95Lim-LB.tdb): LIQUID, type code %, sha256 `2706dcc211c225ff…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : B SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.044](https://doi.org/10.1016/j.jallcom.2009.03.044) H.M. Chen, H.Y. Qi, F. Zheng, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the B–C–Si system, Journal of Alloys and Compounds 481, 182-189 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.-K. Lim, H.L. Lukas, "Hochleistungskeramik, Herstellung, Aufbau und Eigenschaften", G. Petzow, J. Tobolski, R. Telle (Eds.), VCH, Weinheim, 1995, pp. 605-16.  
_assessment that models this phase_
- [doi:10.1007/bf02872900](https://doi.org/10.1007/bf02872900) R. W. Olesinski, G. J. Abbaschian, The B−Si (Boron-Silicon) system, Bulletin of Alloy Phase Diagrams 5, 478-484 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90225-3](https://doi.org/10.1016/0022-5088%2881%2990225-3) B Armas, G Male, D Salanoubat, C Chatillon, M Allibert, Determination of the boron-rich side of the BSi phase diagram, Journal of the Less Common Metals 82, 245-254 (1981).  
_cited as the source of values for this phase_

## SIB24 (B–Si)

- Id: `phase:b-si:sib24`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (SiB24) · hR\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (SiB24) · R-3m (166) — Hallstedt 2025 mmc2 row for SIB24: SiB24
- Stability: stable in 3 of 3 calculated diagram(s): 300–2305.08 K, x(B) 0.94185–0.97581
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-si:sib24)

Names (7): _corpus: _corpus:phase:b-si:sib24  
_paper: _paper:10.1016/j.jallcom.2009.03.044:SiBn, paper:10.1361/105497101770338798:SiBn, paper:sha256-85fd53a1a176b694:BnSi  
_tdb: _tdb:SiB-01Tok.tdb:SIB24, tdb:SiB-03Tok.tdb:SIB24, tdb:SiB-09Che.tdb:SIB24  


### TDB models of SIB24 (3): PHASE and CONSTITUENT statements as written

[SiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-01Tok.tdb): SIB24, type code %, sha256 `d151ee95b11739ec…`

~~~~text
47: PHASE SIB24 % 2 0.041 0.959 !
48: CONST SIB24 : SI : B : !
~~~~

[SiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-03Tok.tdb): SIB24, type code %, sha256 `200e70443756318e…`

~~~~text
49: PHASE SIB24 % 2 0.041 0.959 !
50: CONST SIB24 : SI : B : !
~~~~

[SiB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-09Che.tdb): SIB24, type code %, sha256 `306d09e27c26972d…`

~~~~text
52: PHASE SIB24 % 3 61 1 8 !
53: CONST SIB24 : B : SI : B SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.044](https://doi.org/10.1016/j.jallcom.2009.03.044) H.M. Chen, H.Y. Qi, F. Zheng, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the B–C–Si system, Journal of Alloys and Compounds 481, 182-189 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.1007/bf02872900](https://doi.org/10.1007/bf02872900) R. W. Olesinski, G. J. Abbaschian, The B−Si (Boron-Silicon) system, Bulletin of Alloy Phase Diagrams 5, 478-484 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90225-3](https://doi.org/10.1016/0022-5088%2881%2990225-3) B Armas, G Male, D Salanoubat, C Chatillon, M Allibert, Determination of the boron-rich side of the BSi phase diagram, Journal of the Less Common Metals 82, 245-254 (1981).  
_cited as the source of values for this phase_

## SIB3_D1G (B–Si)

- Id: `phase:b-si:sib3-d1g`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D1_g; stoichiometry_contradicts_D1_g:SiB-01Tok.tdb; stoichiometry_contradicts_D1_g:SiB-03Tok.tdb; stoichiometry_contradicts_D1_g:SiB-09Che.tdb
- Candidate (literature_printed): B13C2 · hR15 — printed with a label mapped to this phase
- Candidate (name_token): B13C2 · D1_g · hR15 · R-3m (166) — Strukturbericht/word 'D1G' in the TDB name
- Candidate (sgte_mmc2): B13C2 · D1_g · hR15 · R-3m (166) — Hallstedt 2025 mmc2 row for SIB3_D1G: SiB3
- Candidate (tdb_comment): B13C2 · hR15 · R-3m — SiB-01Tok.tdb: 'Prototype B13C2 (hR15, R-3m)'
- Candidate (tdb_comment): B13C2 · hR15 · R-3m — SiB-03Tok.tdb: 'Prototype B13C2 (hR15, R-3m)'
- Candidate (tdb_comment): B13C2 · hR15 · R-3m — SiB-09Che.tdb: 'Prototype B13C2 (hR15, R-3m)'
- Candidate (tdb_comment): B13C2 · hR15 · R-3m — SiB-95Lim-LB.tdb: 'Prototype B13C2 (hR15, R-3m)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–1560 K, x(B) 0.7299–0.75
- Literature: 7 values (7 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-si:sib3-d1g)

Names (8): _corpus: _corpus:phase:b-si:sib3-d1g  
_paper: _paper:10.1016/j.jallcom.2009.03.044:SiB3, paper:10.1361/105497101770338798:SiB3, paper:sha256-85fd53a1a176b694:B3Si  
_tdb: _tdb:SiB-01Tok.tdb:SIB3_D1G, tdb:SiB-03Tok.tdb:SIB3_D1G, tdb:SiB-09Che.tdb:SIB3_D1G, tdb:SiB-95Lim-LB.tdb:SIB3_D1G  


### TDB models of SIB3_D1G (4): PHASE and CONSTITUENT statements as written

[SiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-01Tok.tdb): SIB3_D1G, type code %, sha256 `d151ee95b11739ec…`

~~~~text
37: PHASE SIB3_D1G % 2 1 3 !
38: CONST SIB3_D1G : SI : B : !
~~~~

[SiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-03Tok.tdb): SIB3_D1G, type code %, sha256 `200e70443756318e…`

~~~~text
39: PHASE SIB3_D1G % 2 1 3 !
40: CONST SIB3_D1G : SI : B : !
~~~~

[SiB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-09Che.tdb): SIB3_D1G, type code %, sha256 `306d09e27c26972d…`

~~~~text
42: PHASE SIB3_D1G % 2 1 3 !
43: CONST SIB3_D1G : SI : B : !
~~~~

[SiB-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-95Lim-LB.tdb): SIB3_D1G, type code %, sha256 `2706dcc211c225ff…`

~~~~text
47: PHASE SIB3_D1G % 3 6 2 6 !
48: CONST SIB3_D1G : B : SI : B SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.044](https://doi.org/10.1016/j.jallcom.2009.03.044) H.M. Chen, H.Y. Qi, F. Zheng, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the B–C–Si system, Journal of Alloys and Compounds 481, 182-189 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.-K. Lim, H.L. Lukas, "Hochleistungskeramik, Herstellung, Aufbau und Eigenschaften", G. Petzow, J. Tobolski, R. Telle (Eds.), VCH, Weinheim, 1995, pp. 605-16.  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.1007/bf02872900](https://doi.org/10.1007/bf02872900) R. W. Olesinski, G. J. Abbaschian, The B−Si (Boron-Silicon) system, Bulletin of Alloy Phase Diagrams 5, 478-484 (1984).  
_cited as the source of values for this phase_

## SIB6 (B–Si)

- Id: `phase:b-si:sib6`; status `assigned`
- Structure: SiB6 · oP280 · Pnnm (58); type `st:sib6-op280`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 4 of 4 calculated diagram(s): 300–2129.74 K, x(B) 0.85438–0.86312
- Literature: 26 values (26 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-si:sib6)

Names (8): _corpus: _corpus:phase:b-si:sib6  
_paper: _paper:10.1016/j.jallcom.2009.03.044:SiB6, paper:10.1361/105497101770338798:SiB6, paper:sha256-85fd53a1a176b694:B6Si  
_tdb: _tdb:SiB-01Tok.tdb:SIB6, tdb:SiB-03Tok.tdb:SIB6, tdb:SiB-09Che.tdb:SIB6, tdb:SiB-95Lim-LB.tdb:SIB6  


### TDB models of SIB6 (4): PHASE and CONSTITUENT statements as written

[SiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-01Tok.tdb): SIB6, type code %, sha256 `d151ee95b11739ec…`

~~~~text
42: PHASE SIB6 % 2 1 6 !
43: CONST SIB6 : SI : B : !
~~~~

[SiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-03Tok.tdb): SIB6, type code %, sha256 `200e70443756318e…`

~~~~text
44: PHASE SIB6 % 2 1 6 !
45: CONST SIB6 : SI : B : !
~~~~

[SiB-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-09Che.tdb): SIB6, type code %, sha256 `306d09e27c26972d…`

~~~~text
47: PHASE SIB6 % 2 1 6 !
48: CONST SIB6 : SI : B : !
~~~~

[SiB-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiB-95Lim-LB.tdb): SIB6, type code %, sha256 `2706dcc211c225ff…`

~~~~text
52: PHASE SIB6 % 3 210 23 48 !
53: CONST SIB6 : B : SI : B SI : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.044](https://doi.org/10.1016/j.jallcom.2009.03.044) H.M. Chen, H.Y. Qi, F. Zheng, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the B–C–Si system, Journal of Alloys and Compounds 481, 182-189 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.-K. Lim, H.L. Lukas, "Hochleistungskeramik, Herstellung, Aufbau und Eigenschaften", G. Petzow, J. Tobolski, R. Telle (Eds.), VCH, Weinheim, 1995, pp. 605-16.  
_assessment that models this phase_
- [doi:10.1007/bf02872900](https://doi.org/10.1007/bf02872900) R. W. Olesinski, G. J. Abbaschian, The B−Si (Boron-Silicon) system, Bulletin of Alloy Phase Diagrams 5, 478-484 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90225-3](https://doi.org/10.1016/0022-5088%2881%2990225-3) B Armas, G Male, D Salanoubat, C Chatillon, M Allibert, Determination of the boron-rich side of the BSi phase diagram, Journal of the Less Common Metals 82, 245-254 (1981).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1015457114818](https://doi.org/10.1023/a:1015457114818) A. I. Zaitsev, Thermodynamic Properties and Phase Equilibria in the Si-B System, Russian Journal of General Chemistry 72, 183-192 (2002).  
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
