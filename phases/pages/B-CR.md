# B–Cr phases

> B–Cr system: 12 phases (tier A 6, tier C 1, liquid 1, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-CR.html · Markdown: https://data.orchid-project.org/phases/pages/B-CR.md

12 phases (tier A 6, tier C 1, liquid 1, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-CR) · [full JSON](https://data.orchid-project.org/phases/systems/B-CR.json) · [B–Cr system page](https://data.orchid-project.org/systems/B-CR.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-CR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Cr system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-cr-b-alpha-rhombo); _phase:b-cr:b-alpha-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 3 |
| [BETA_RHOMBO_B](#phase-b-cr-b-beta-rhombo); _phase:b-cr:b-beta-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 1388–2348 K, x(B) 1–1 | 6 | 3 |
| [MB_B33](#phase-b-cr-b33-mb); _phase:b-cr:b33-mb_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–2373.36 K, x(B) 0.5–0.5 | 10 | 3 |
| [BCC_A2](#phase-b-cr-bcc-a2); _phase:b-cr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.86 K, x(B) 0–0.01722 | 4 | 3 |
| [MB2_C32](#phase-b-cr-c32-mb2); _phase:b-cr:c32-mb2_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–2480.05 K, x(B) 0.66481–0.66667 | 8 | 3 |
| [CR2B_CB](#phase-b-cr-cr2b-cb); _phase:b-cr:cr2b-cb_ | CuMg2 · C_b · oF48 · Fddd (70) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2149.2 K, x(B) 0.33333–0.33333 | 8 | 3 |
| [CR3B4_D7B](#phase-b-cr-cr3b4-d7b); _phase:b-cr:cr3b4-d7b_ | Ta3B4 · D7_b · oI14 · Immm (71) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2356.29 K, x(B) 0.57143–0.57143 | 8 | 3 |
| [CR5B3_D8L](#phase-b-cr-cr5b3-d8l); _phase:b-cr:cr5b3-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2186.75 K, x(B) 0.375–0.375 | 8 | 3 |
| [CRB4](#phase-b-cr-crb4); _phase:b-cr:crb4_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1818.3 K, x(B) 0.8–0.8 | 2 | 3 |
| [FCC_A1](#phase-b-cr-fcc-a1); _phase:b-cr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-b-cr-hcp-a3); _phase:b-cr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-b-cr-liquid); _phase:b-cr:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1878.38–4000 K, x(B) 0–1 | 20 | 3 |

## ALPHA_RHOMBO_B (B–Cr)

- Id: `phase:b-cr:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — CrB-02Cam.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — CrB-08Yam.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — CrB-91Pan-LB.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:b-alpha-rhombo)

Names (4): _corpus: _corpus:phase:b-cr:b-alpha-rhombo  
_tdb: _tdb:CrB-02Cam.tdb:ALPHA_RHOMBO_B, tdb:CrB-08Yam.tdb:ALPHA_RHOMBO_B, tdb:CrB-91Pan-LB.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): ALPHA_RHOMBO_B, type code %, sha256 `e712fc05d415dc32…`

~~~~text
42: PHASE ALPHA_RHOMBO_B % 1 1 !
43: CONST ALPHA_RHOMBO_B : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): ALPHA_RHOMBO_B, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
57: PHASE ALPHA_RHOMBO_B % 1 1 !
58: CONST ALPHA_RHOMBO_B : B : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): ALPHA_RHOMBO_B, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
41: PHASE ALPHA_RHOMBO_B % 1 1 !
42: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Cr)

- Id: `phase:b-cr:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CrB-02Cam.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CrB-08Yam.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CrB-91Pan-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 1388–2348 K, x(B) 1–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:b-beta-rhombo)

Names (6): _corpus: _corpus:phase:b-cr:b-beta-rhombo, corpus:phase:b-cr:beta-rhombo-b  
_paper: _paper:10.1016/s0364-5916(02)00058-5:β(B)  
_tdb: _tdb:CrB-02Cam.tdb:BETA_RHOMBO_B, tdb:CrB-08Yam.tdb:BETA_RHOMBO_B, tdb:CrB-91Pan-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): BETA_RHOMBO_B, type code %, sha256 `e712fc05d415dc32…`

~~~~text
47: PHASE BETA_RHOMBO_B % 1 1 !
48: CONST BETA_RHOMBO_B : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): BETA_RHOMBO_B, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
62: PHASE BETA_RHOMBO_B % 1 1 !
63: CONST BETA_RHOMBO_B : B : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
46: PHASE BETA_RHOMBO_B % 1 1 !
47: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## MB_B33 (B–Cr)

- Id: `phase:b-cr:b33-mb`; status `needs_review`
- No structure assigned. Why: assessment_declared_conflicts_with_dft; name_has_descriptive_tokens:MB; no_structure_token; structure_token_is_also_a_formula
- Candidate (dft_mp): I4_1/amd (141) — on-hull MP CrB at x(CR)=0.5000
- Candidate (dft_oqmd): I41/amd (141) — on-hull OQMD B1 Cr1 at x(CR)=0.5000
- Candidate (literature_printed): CrB · oC8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): CrB · B33 · oC8 · Cmcm (63) — Hallstedt 2025 mmc2 row for MB_B33: CrB, beta-MoB, VB (also B_f)
- Candidate (tdb_comment): CrB · oC8 · Cmcm — CrB-02Cam.tdb: 'Prototype CrB (oC8, Cmcm)'
- Candidate (tdb_comment): CrB · oC8 · Cmcm — CrB-08Yam.tdb: 'Prototype CrB (oC8, Cmcm)'
- Candidate (tdb_comment): CrB · oC8 · Cmcm — CrB-91Pan-LB.tdb: 'Prototype CrB (oC8, Cmcm)'
- Stoichiometry: B 0.5000, Cr 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2373.36 K, x(B) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:b33-mb)

Names (6): _corpus: _corpus:phase:b-cr:b33-mb, corpus:phase:b-cr:mb-b33  
_paper: _paper:10.1016/s0364-5916(02)00058-5:CrB  
_tdb: _tdb:CrB-02Cam.tdb:MB_B33, tdb:CrB-08Yam.tdb:MB_B33, tdb:CrB-91Pan-LB.tdb:MB_B33  


### TDB models of MB_B33 (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): MB_B33, type code %, sha256 `e712fc05d415dc32…`

~~~~text
62: PHASE MB_B33 % 2 1 1 !
63: CONST MB_B33 : CR : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): MB_B33, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
77: PHASE MB_B33 % 2 1 1 !
78: CONST MB_B33 : CR : B : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): MB_B33, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
61: PHASE MB_B33 % 2 1 1 !
62: CONST MB_B33 : CR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## BCC_A2 (B–Cr)

- Id: `phase:b-cr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.86 K, x(B) 0–0.01722
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:bcc-a2)

Names (5): _corpus: _corpus:phase:b-cr:bcc-a2  
_paper: _paper:10.1016/s0364-5916(02)00058-5:BCC(Cr)  
_tdb: _tdb:CrB-02Cam.tdb:BCC_A2, tdb:CrB-08Yam.tdb:BCC_A2, tdb:CrB-91Pan-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): BCC_A2, type code %B, sha256 `e712fc05d415dc32…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR% : B VA% : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): BCC_A2, type code %B, sha256 `8f5a8bb878cae5a8…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : B CR% : VA : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): BCC_A2, type code %B, sha256 `f54a6c7ef2cf6747…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR% : B VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## MB2_C32 (B–Cr)

- Id: `phase:b-cr:c32-mb2`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MB2); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 300–2480.05 K, x(B) 0.66481–0.66667
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:c32-mb2)

Names (6): _corpus: _corpus:phase:b-cr:c32-mb2, corpus:phase:b-cr:mb2-c32  
_paper: _paper:10.1016/s0364-5916(02)00058-5:CrB2  
_tdb: _tdb:CrB-02Cam.tdb:MB2_C32, tdb:CrB-08Yam.tdb:MB2_C32, tdb:CrB-91Pan-LB.tdb:MB2_C32  


### TDB models of MB2_C32 (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): MB2_C32, type code %, sha256 `e712fc05d415dc32…`

~~~~text
72: PHASE MB2_C32 % 2 1 2 !
73: CONST MB2_C32 : CR : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): MB2_C32, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
87: PHASE MB2_C32 % 2 1 2 !
88: CONST MB2_C32 : CR VA : B VA : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): MB2_C32, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
71: PHASE MB2_C32 % 2 1 2 !
72: CONST MB2_C32 : CR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## CR2B_CB (B–Cr)

- Id: `phase:b-cr:cr2b-cb`; status `assigned`
- Structure: CuMg2 · C_b · oF48 · Fddd (70); type `st:c-b-cumg2-of48`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgkiy and oqmd-28322, space group 70
- Stoichiometry: B 0.3333, Cr 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–2149.2 K, x(B) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:cr2b-cb)

Names (7): _corpus: _corpus:phase:b-cr:cr2b-cb  
_mp: _mp:mp-aaabgkiy  
_oqmd: _oqmd:oqmd-28322  
_paper: _paper:10.1016/s0364-5916(02)00058-5:Cr2B  
_tdb: _tdb:CrB-02Cam.tdb:CR2B_CB, tdb:CrB-08Yam.tdb:CR2B_CB, tdb:CrB-91Pan-LB.tdb:CR2B_CB  


### TDB models of CR2B_CB (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): CR2B_CB, type code %, sha256 `e712fc05d415dc32…`

~~~~text
52: PHASE CR2B_CB % 2 2 1 !
53: CONST CR2B_CB : CR : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): CR2B_CB, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
67: PHASE CR2B_CB % 2 2 1 !
68: CONST CR2B_CB : CR : B : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): CR2B_CB, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
51: PHASE CR2B_CB % 2 2 1 !
52: CONST CR2B_CB : CR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## CR3B4_D7B (B–Cr)

- Id: `phase:b-cr:cr3b4-d7b`; status `assigned`
- Structure: Ta3B4 · D7_b · oI14 · Immm (71); type `st:d7-b-ta3b4-oi14`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.5714, Cr 0.4286
- Stability: stable in 3 of 3 calculated diagram(s): 300–2356.29 K, x(B) 0.57143–0.57143
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:cr3b4-d7b)

Names (5): _corpus: _corpus:phase:b-cr:cr3b4-d7b  
_paper: _paper:10.1016/s0364-5916(02)00058-5:Cr3B4  
_tdb: _tdb:CrB-02Cam.tdb:CR3B4_D7B, tdb:CrB-08Yam.tdb:CR3B4_D7B, tdb:CrB-91Pan-LB.tdb:CR3B4_D7B  


### TDB models of CR3B4_D7B (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): CR3B4_D7B, type code %, sha256 `e712fc05d415dc32…`

~~~~text
67: PHASE CR3B4_D7B % 2 3 4 !
68: CONST CR3B4_D7B : CR : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): CR3B4_D7B, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
82: PHASE CR3B4_D7B % 2 3 4 !
83: CONST CR3B4_D7B : CR : B : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): CR3B4_D7B, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
66: PHASE CR3B4_D7B % 2 3 4 !
67: CONST CR3B4_D7B : CR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## CR5B3_D8L (B–Cr)

- Id: `phase:b-cr:cr5b3-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaxcr and oqmd-5250, space group 140
- Stoichiometry: B 0.3750, Cr 0.6250
- Stability: stable in 3 of 3 calculated diagram(s): 300–2186.75 K, x(B) 0.375–0.375
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:cr5b3-d8l)

Names (7): _corpus: _corpus:phase:b-cr:cr5b3-d8l  
_mp: _mp:mp-aaaaaxcr  
_oqmd: _oqmd:oqmd-5250  
_paper: _paper:10.1016/s0364-5916(02)00058-5:Cr5B3  
_tdb: _tdb:CrB-02Cam.tdb:CR5B3_D8L, tdb:CrB-08Yam.tdb:CR5B3_D8L, tdb:CrB-91Pan-LB.tdb:CR5B3_D8L  


### TDB models of CR5B3_D8L (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): CR5B3_D8L, type code %, sha256 `e712fc05d415dc32…`

~~~~text
57: PHASE CR5B3_D8L % 2 5 3 !
58: CONST CR5B3_D8L : CR : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): CR5B3_D8L, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
72: PHASE CR5B3_D8L % 2 5 3 !
73: CONST CR5B3_D8L : CR : B : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): CR5B3_D8L, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
56: PHASE CR5B3_D8L % 2 5 3 !
57: CONST CR5B3_D8L : CR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## CRB4 (B–Cr)

- Id: `phase:b-cr:crb4`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_dft; dft_space_group_58_matches_0_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft
- Candidate (dft_mp): Pnnm (58) — on-hull MP CrB4 at x(CR)=0.2000
- Candidate (dft_oqmd): Pnnm (58) — on-hull OQMD B4 Cr1 at x(CR)=0.2000
- Candidate (literature_printed): CrB4 · oI10 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): CrB4 · oI10 · Immm (71) — Hallstedt 2025 mmc2 row for CRB4: CrB4
- Candidate (tdb_comment): CrB4 · oI10 · Immm — CrB-02Cam.tdb: 'Prototype CrB4 (oI10, Immm)'
- Candidate (tdb_comment): CrB4 · oI10 · Immm — CrB-08Yam.tdb: 'Prototype CrB4 (oI10, Immm)'
- Candidate (tdb_comment): CrB4 · oI10 · Immm — CrB-91Pan-LB.tdb: 'Prototype CrB4 (oI10, Immm)'
- Stoichiometry: B 0.8000, Cr 0.2000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1818.3 K, x(B) 0.8–0.8
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:crb4)

Names (5): _corpus: _corpus:phase:b-cr:crb4  
_paper: _paper:10.1016/s0364-5916(02)00058-5:CrB4  
_tdb: _tdb:CrB-02Cam.tdb:CRB4, tdb:CrB-08Yam.tdb:CRB4, tdb:CrB-91Pan-LB.tdb:CRB4  


### TDB models of CRB4 (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): CRB4, type code %, sha256 `e712fc05d415dc32…`

~~~~text
77: PHASE CRB4 % 2 1 4 !
78: CONST CRB4 : CR : B : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): CRB4, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
92: PHASE CRB4 % 2 1 4 !
93: CONST CRB4 : CR : B : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): CRB4, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
76: PHASE CRB4 % 2 1 4 !
77: CONST CRB4 : CR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## FCC_A1 (B–Cr)

- Id: `phase:b-cr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:fcc-a1)

Names (4): _corpus: _corpus:phase:b-cr:fcc-a1  
_tdb: _tdb:CrB-02Cam.tdb:FCC_A1, tdb:CrB-08Yam.tdb:FCC_A1, tdb:CrB-91Pan-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): FCC_A1, type code %A, sha256 `e712fc05d415dc32…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR : B VA% : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): FCC_A1, type code %A, sha256 `8f5a8bb878cae5a8…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : B CR : VA : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): FCC_A1, type code %A, sha256 `f54a6c7ef2cf6747…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR : B VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## HCP_A3 (B–Cr)

- Id: `phase:b-cr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:hcp-a3)

Names (4): _corpus: _corpus:phase:b-cr:hcp-a3  
_tdb: _tdb:CrB-02Cam.tdb:HCP_A3, tdb:CrB-08Yam.tdb:HCP_A3, tdb:CrB-91Pan-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): HCP_A3, type code %A, sha256 `e712fc05d415dc32…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CR : B VA% : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): HCP_A3, type code %A, sha256 `8f5a8bb878cae5a8…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : B CR : VA : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): HCP_A3, type code %A, sha256 `f54a6c7ef2cf6747…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR : B VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
_assessment that models this phase_

## LIQUID (B–Cr)

- Id: `phase:b-cr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1878.38–4000 K, x(B) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cr:liquid)

Names (5): _corpus: _corpus:phase:b-cr:liquid  
_paper: _paper:10.1016/s0364-5916(02)00058-5:L  
_tdb: _tdb:CrB-02Cam.tdb:LIQUID, tdb:CrB-08Yam.tdb:LIQUID, tdb:CrB-91Pan-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CrB-02Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-02Cam.tdb): LIQUID, type code %, sha256 `e712fc05d415dc32…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : B CR : !
~~~~

[CrB-08Yam.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-08Yam.tdb): LIQUID, type code %, sha256 `8f5a8bb878cae5a8…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : B CR : !
~~~~

[CrB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrB-91Pan-LB.tdb): LIQUID, type code %, sha256 `f54a6c7ef2cf6747…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : B CR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(02)00058-5](https://doi.org/10.1016/S0364-5916%2802%2900058-5) C.E. Campbell, U.R. Kattner, Calphad, 26, 477-90(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2008.27.4.269](https://doi.org/10.1515/HTMP.2008.27.4.269) K. Yamada, H. Ohtani, M. Hasebe, High Temp. Mater. Processes., 27, 269-83(2008).  
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
