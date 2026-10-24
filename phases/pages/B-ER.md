# B–Er phases

> B–Er system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-ER.html · Markdown: https://data.orchid-project.org/phases/pages/B-ER.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-ER) · [full JSON](https://data.orchid-project.org/phases/systems/B-ER.json) · [B–Er system page](https://data.orchid-project.org/systems/B-ER.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-ER.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Er system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-er-b-alpha-rhombo); _phase:b-er:b-alpha-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 3 |
| [BETA_RHOMBO_B](#phase-b-er-b-beta-rhombo); _phase:b-er:b-beta-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 1388–2365.95 K, x(B) 1–1 | 0 | 3 |
| [BCC_A2](#phase-b-er-bcc-a2); _phase:b-er:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ERB12_D2F](#phase-b-er-erb12-d2f); _phase:b-er:erb12-d2f_ | UB12 · D2_f · cF52 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2355.96 K, x(B) 0.92308–0.92308 | 4 | 3 |
| [ERB2_C32](#phase-b-er-erb2-c32); _phase:b-er:erb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2460 K, x(B) 0.66667–0.66667 | 4 | 3 |
| [ERB4_D1E](#phase-b-er-erb4-d1e); _phase:b-er:erb4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2633.53 K, x(B) 0.8–0.8 | 6 | 3 |
| [ERB66](#phase-b-er-erb66); _phase:b-er:erb66_ | YB66 · cF1936 · Fm-3c (226) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–2345.42 K, x(B) 0.98507–0.98507 | 4 | 3 |
| [FCC_A1](#phase-b-er-fcc-a1); _phase:b-er:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-b-er-hcp-a3); _phase:b-er:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.83 K, x(B) 0–0.00025 | 2 | 3 |
| [LIQUID](#phase-b-er-liquid); _phase:b-er:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1768.72–4000 K, x(B) 0–1 | 12 | 3 |

## ALPHA_RHOMBO_B (B–Er)

- Id: `phase:b-er:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — ErB-12Wan.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — ErB-15Wan.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — ErB-20Wei.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:b-alpha-rhombo)

Names (4): _corpus: _corpus:phase:b-er:b-alpha-rhombo  
_tdb: _tdb:ErB-12Wan.tdb:ALPHA_RHOMBO_B, tdb:ErB-15Wan.tdb:ALPHA_RHOMBO_B, tdb:ErB-20Wei.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): ALPHA_RHOMBO_B, type code %, sha256 `8f09916e3716a12b…`

~~~~text
45: PHASE ALPHA_RHOMBO_B % 1 1 !
46: CONST ALPHA_RHOMBO_B : B : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): ALPHA_RHOMBO_B, type code %, sha256 `0b206ab2f0b78176…`

~~~~text
42: PHASE ALPHA_RHOMBO_B % 1 1 !
43: CONST ALPHA_RHOMBO_B : B : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): ALPHA_RHOMBO_B, type code %, sha256 `dc59cadaaa23c3a1…`

~~~~text
35: PHASE ALPHA_RHOMBO_B % 1 1 !
36: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Er)

- Id: `phase:b-er:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ErB-12Wan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ErB-15Wan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ErB-20Wei.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 1388–2365.95 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:b-beta-rhombo)

Names (5): _corpus: _corpus:phase:b-er:b-beta-rhombo, corpus:phase:b-er:beta-rhombo-b  
_tdb: _tdb:ErB-12Wan.tdb:BETA_RHOMBO_B, tdb:ErB-15Wan.tdb:BETA_RHOMBO_B, tdb:ErB-20Wei.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): BETA_RHOMBO_B, type code %, sha256 `8f09916e3716a12b…`

~~~~text
50: PHASE BETA_RHOMBO_B % 1 1 !
51: CONST BETA_RHOMBO_B : B : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): BETA_RHOMBO_B, type code %, sha256 `0b206ab2f0b78176…`

~~~~text
47: PHASE BETA_RHOMBO_B % 1 1 !
48: CONST BETA_RHOMBO_B : B : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): BETA_RHOMBO_B, type code %, sha256 `dc59cadaaa23c3a1…`

~~~~text
40: PHASE BETA_RHOMBO_B % 1 1 !
41: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase_

## BCC_A2 (B–Er)

- Id: `phase:b-er:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:bcc-a2)

Names (4): _corpus: _corpus:phase:b-er:bcc-a2  
_tdb: _tdb:ErB-12Wan.tdb:BCC_A2, tdb:ErB-15Wan.tdb:BCC_A2, tdb:ErB-20Wei.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): BCC_A2, type code %B, sha256 `8f09916e3716a12b…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : B ER : VA : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): BCC_A2, type code %B, sha256 `0b206ab2f0b78176…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : B ER : VA : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): BCC_A2, type code %B, sha256 `dc59cadaaa23c3a1…`

~~~~text
25: PHASE BCC_A2 %B 2 1 3 !
26: CONST BCC_A2 : ER : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase_

## ERB12_D2F (B–Er)

- Id: `phase:b-er:erb12-d2f`; status `assigned`
- Structure: UB12 · D2_f · cF52 · Fm-3m (225); type `st:d2-f-ub12-cf52`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackwao and oqmd-28367, space group 225
- Stoichiometry: B 0.9231, Er 0.0769
- Stability: stable in 3 of 3 calculated diagram(s): 300–2355.96 K, x(B) 0.92308–0.92308
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:erb12-d2f)

Names (7): _corpus: _corpus:phase:b-er:erb12-d2f  
_mp: _mp:mp-aaackwao  
_oqmd: _oqmd:oqmd-28367  
_paper: _paper:10.1016/j.jallcom.2011.08.014:B12Er  
_tdb: _tdb:ErB-12Wan.tdb:ERB12_D2F, tdb:ErB-15Wan.tdb:ERB12_D2F, tdb:ErB-20Wei.tdb:ERB12_D2F  


### TDB models of ERB12_D2F (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): ERB12_D2F, type code %, sha256 `8f09916e3716a12b…`

~~~~text
65: PHASE ERB12_D2F % 2 1 12 !
66: CONST ERB12_D2F : ER : B : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): ERB12_D2F, type code %, sha256 `0b206ab2f0b78176…`

~~~~text
62: PHASE ERB12_D2F % 2 1 12 !
63: CONST ERB12_D2F : ER : B : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): ERB12_D2F, type code %, sha256 `dc59cadaaa23c3a1…`

~~~~text
55: PHASE ERB12_D2F % 2 1 12 !
56: CONST ERB12_D2F : ER : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02665558](https://doi.org/10.1007/bf02665558) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Er (boron-erbium) system, JPE 17, 326-329 (1996).  
_cited as the source of values for this phase_

## ERB2_C32 (B–Er)

- Id: `phase:b-er:erb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacqg and oqmd-647372, space group 191
- Stoichiometry: B 0.6667, Er 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–2460 K, x(B) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:erb2-c32)

Names (7): _corpus: _corpus:phase:b-er:erb2-c32  
_mp: _mp:mp-aaaaacqg  
_oqmd: _oqmd:oqmd-647372  
_paper: _paper:10.1016/j.jallcom.2011.08.014:B2Er  
_tdb: _tdb:ErB-12Wan.tdb:ERB2_C32, tdb:ErB-15Wan.tdb:ERB2_C32, tdb:ErB-20Wei.tdb:ERB2_C32  


### TDB models of ERB2_C32 (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): ERB2_C32, type code %, sha256 `8f09916e3716a12b…`

~~~~text
55: PHASE ERB2_C32 % 2 1 2 !
56: CONST ERB2_C32 : ER : B : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): ERB2_C32, type code %, sha256 `0b206ab2f0b78176…`

~~~~text
52: PHASE ERB2_C32 % 2 1 2 !
53: CONST ERB2_C32 : ER : B : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): ERB2_C32, type code %, sha256 `dc59cadaaa23c3a1…`

~~~~text
45: PHASE ERB2_C32 % 2 1 2 !
46: CONST ERB2_C32 : ER : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02665558](https://doi.org/10.1007/bf02665558) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Er (boron-erbium) system, JPE 17, 326-329 (1996).  
_cited as the source of values for this phase_

## ERB4_D1E (B–Er)

- Id: `phase:b-er:erb4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaefn and oqmd-8336, space group 127
- Stoichiometry: B 0.8000, Er 0.2000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2633.53 K, x(B) 0.8–0.8
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:erb4-d1e)

Names (7): _corpus: _corpus:phase:b-er:erb4-d1e  
_mp: _mp:mp-aaaaaefn  
_oqmd: _oqmd:oqmd-8336  
_paper: _paper:10.1016/j.jallcom.2011.08.014:B4Er  
_tdb: _tdb:ErB-12Wan.tdb:ERB4_D1E, tdb:ErB-15Wan.tdb:ERB4_D1E, tdb:ErB-20Wei.tdb:ERB4_D1E  


### TDB models of ERB4_D1E (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): ERB4_D1E, type code %, sha256 `8f09916e3716a12b…`

~~~~text
60: PHASE ERB4_D1E % 2 1 4 !
61: CONST ERB4_D1E : ER : B : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): ERB4_D1E, type code %, sha256 `0b206ab2f0b78176…`

~~~~text
57: PHASE ERB4_D1E % 2 1 4 !
58: CONST ERB4_D1E : ER : B : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): ERB4_D1E, type code %, sha256 `dc59cadaaa23c3a1…`

~~~~text
50: PHASE ERB4_D1E % 2 1 4 !
51: CONST ERB4_D1E : ER : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02665558](https://doi.org/10.1007/bf02665558) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Er (boron-erbium) system, JPE 17, 326-329 (1996).  
_cited as the source of values for this phase_

## ERB66 (B–Er)

- Id: `phase:b-er:erb66`; status `assigned`
- Structure: YB66 · cF1936 · Fm-3c (226); type `st:yb66-cf1936`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.9851, Er 0.0149
- Stability: stable in 3 of 3 calculated diagram(s): 300–2345.42 K, x(B) 0.98507–0.98507
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:erb66)

Names (5): _corpus: _corpus:phase:b-er:erb66  
_paper: _paper:10.1016/j.jallcom.2011.08.014:B66Er  
_tdb: _tdb:ErB-12Wan.tdb:ERB66, tdb:ErB-15Wan.tdb:ERB66, tdb:ErB-20Wei.tdb:ERB66  


### TDB models of ERB66 (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): ERB66, type code %, sha256 `8f09916e3716a12b…`

~~~~text
70: PHASE ERB66 % 2 1 66 !
71: CONST ERB66 : ER : B : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): ERB66, type code %, sha256 `0b206ab2f0b78176…`

~~~~text
67: PHASE ERB66 % 2 1 66 !
68: CONST ERB66 : ER : B : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): ERB66, type code %, sha256 `dc59cadaaa23c3a1…`

~~~~text
60: PHASE ERB66 % 2 1 66 !
61: CONST ERB66 : ER : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02665558](https://doi.org/10.1007/bf02665558) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Er (boron-erbium) system, JPE 17, 326-329 (1996).  
_cited as the source of values for this phase_

## FCC_A1 (B–Er)

- Id: `phase:b-er:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: B 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:fcc-a1)

Names (3): _corpus: _corpus:phase:b-er:fcc-a1  
_tdb: _tdb:ErB-12Wan.tdb:FCC_A1, tdb:ErB-15Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): FCC_A1, type code %A, sha256 `8f09916e3716a12b…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : B : VA : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): FCC_A1, type code %A, sha256 `0b206ab2f0b78176…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : B : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase_

## HCP_A3 (B–Er)

- Id: `phase:b-er:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.83 K, x(B) 0–0.00025
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:hcp-a3)

Names (5): _corpus: _corpus:phase:b-er:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2011.08.014:(Er)  
_tdb: _tdb:ErB-12Wan.tdb:HCP_A3, tdb:ErB-15Wan.tdb:HCP_A3, tdb:ErB-20Wei.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): HCP_A3, type code %A, sha256 `8f09916e3716a12b…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : B ER% : VA : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): HCP_A3, type code %A, sha256 `0b206ab2f0b78176…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : B ER% : VA : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): HCP_A3, type code %A, sha256 `dc59cadaaa23c3a1…`

~~~~text
30: PHASE HCP_A3 %A 2 1 0.5 !
31: CONST HCP_A3 : ER : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02665558](https://doi.org/10.1007/bf02665558) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Er (boron-erbium) system, JPE 17, 326-329 (1996).  
_cited as the source of values for this phase_

## LIQUID (B–Er)

- Id: `phase:b-er:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1768.72–4000 K, x(B) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-er:liquid)

Names (5): _corpus: _corpus:phase:b-er:liquid  
_paper: _paper:10.1016/j.jallcom.2011.08.014:L  
_tdb: _tdb:ErB-12Wan.tdb:LIQUID, tdb:ErB-15Wan.tdb:LIQUID, tdb:ErB-20Wei.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[ErB-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-12Wan.tdb): LIQUID, type code %, sha256 `8f09916e3716a12b…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : B ER : !
~~~~

[ErB-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-15Wan.tdb): LIQUID, type code %, sha256 `0b206ab2f0b78176…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : B ER : !
~~~~

[ErB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/ErB-20Wei.tdb): LIQUID, type code %, sha256 `dc59cadaaa23c3a1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : B ER : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.07.001](https://doi.org/10.1016/j.calphad.2015.07.001) W. Wang, Z. Fu, T. Liu, W. Zhang, Calphad, 51, 24-34(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02665558](https://doi.org/10.1007/bf02665558) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Er (boron-erbium) system, JPE 17, 326-329 (1996).  
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
