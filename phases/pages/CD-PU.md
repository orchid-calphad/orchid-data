# Cd–Pu phases

> Cd–Pu system: 12 phases (tier A 5, liquid 1, needs_review 5, unresolved_no_candidates 1); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-PU.html · Markdown: https://data.orchid-project.org/phases/pages/CD-PU.md

12 phases (tier A 5, liquid 1, needs_review 5, unresolved_no_candidates 1); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-PU) · [full JSON](https://data.orchid-project.org/phases/systems/CD-PU.json) · [Cd–Pu system page](https://data.orchid-project.org/systems/CD-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Pu system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-cd-pu-a6-tetragonal); _phase:cd-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 611.56–910.67 K, x(Pu) 1–1 | 0 | 1 |
| [BCC_A2](#phase-cd-pu-bcc-a2); _phase:cd-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 755.67–3999.93 K, x(Pu) 0.99999–1 | 0 | 1 |
| [CD11PU_D2E](#phase-cd-pu-cd11pu-d2e); _phase:cd-pu:cd11pu-d2e_ | BaHg11 · D2_e · cP36 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–683.14 K, x(Pu) 0.08333–0.08333 | 0 | 1 |
| [CD2PU](#phase-cd-pu-cd2pu); _phase:cd-pu:cd2pu_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1203.01 K, x(Pu) 0.33333–0.33333 | 2 | 1 |
| [CD4PU](#phase-cd-pu-cd4pu); _phase:cd-pu:cd4pu_ |  | unresolved_no_candidates | stable in 1 of 1 calculated diagram(s): 300–1074.68 K, x(Pu) 0.2–0.2 | 2 | 1 |
| [CD6PU](#phase-cd-pu-cd6pu); _phase:cd-pu:cd6pu_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1003.27 K, x(Pu) 0.14286–0.14286 | 2 | 1 |
| [FCC_A1](#phase-cd-pu-fcc-a1); _phase:cd-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 593.06–910 K, x(Pu) 0.41–1 | 0 | 1 |
| [HCP_A3](#phase-cd-pu-hcp-a3); _phase:cd-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–594.04 K, x(Pu) 0–0 | 0 | 1 |
| [LIQUID](#phase-cd-pu-liquid); _phase:cd-pu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 594.04–4000 K, x(Pu) 0–1 | 0 | 1 |
| [ALPHA_PU](#phase-cd-pu-pu-alpha); _phase:cd-pu:pu-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1 | 0 | 1 |
| [BETA_PU](#phase-cd-pu-pu-beta); _phase:cd-pu:pu-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1 | 0 | 1 |
| [GAMMA_PU](#phase-cd-pu-pu-gamma); _phase:cd-pu:pu-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 487.9–608.06 K, x(Pu) 1–1 | 0 | 1 |

## TETRAGONAL_A6 (Cd–Pu)

- Id: `phase:cd-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 611.56–910.67 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:a6-tetragonal)

Names (2): _corpus: _corpus:phase:cd-pu:a6-tetragonal  
_tdb: _tdb:CdPu-16Hua.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): TETRAGONAL_A6, type code %, sha256 `b0796d759bc2c895…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## BCC_A2 (Cd–Pu)

- Id: `phase:cd-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 755.67–3999.93 K, x(Pu) 0.99999–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-pu:bcc-a2  
_tdb: _tdb:CdPu-16Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): BCC_A2, type code %B, sha256 `b0796d759bc2c895…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CD PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## CD11PU_D2E (Cd–Pu)

- Id: `phase:cd-pu:cd11pu-d2e`; status `assigned`
- Structure: BaHg11 · D2_e · cP36 · Pm-3m (221); type `st:d2-e-bahg11-cp36`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.9167, Pu 0.0833
- Stability: stable in 1 of 1 calculated diagram(s): 300–683.14 K, x(Pu) 0.08333–0.08333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:cd11pu-d2e)

Names (2): _corpus: _corpus:phase:cd-pu:cd11pu-d2e  
_tdb: _tdb:CdPu-16Hua.tdb:CD11PU_D2E  


### TDB models of CD11PU_D2E (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): CD11PU_D2E, type code %, sha256 `b0796d759bc2c895…`

~~~~text
60: PHASE CD11PU_D2E % 2 11 1 !
61: CONST CD11PU_D2E : CD : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## CD2PU (Cd–Pu)

- Id: `phase:cd-pu:cd2pu`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): P6/mmm (191) — on-hull OQMD Cd2 Pu1 at x(PU)=0.3333
- Candidate (sgte_mmc2): (Cd2Pu) — Hallstedt 2025 mmc2 row for CD2PU: Cd2Pu
- Stoichiometry: Cd 0.6667, Pu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1203.01 K, x(Pu) 0.33333–0.33333
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:cd2pu)

Names (3): _corpus: _corpus:phase:cd-pu:cd2pu  
_paper: _paper:10.1361/105497101770338707:Cd2Pu  
_tdb: _tdb:CdPu-16Hua.tdb:CD2PU  


### TDB models of CD2PU (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): CD2PU, type code %, sha256 `b0796d759bc2c895…`

~~~~text
75: PHASE CD2PU % 2 2 1 !
76: CONST CD2PU : CD : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_
- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_reports values for this phase_

## CD4PU (Cd–Pu)

- Id: `phase:cd-pu:cd4pu`; status `unresolved_no_candidates`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Stoichiometry: Cd 0.8000, Pu 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1074.68 K, x(Pu) 0.2–0.2
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:cd4pu)

Names (3): _corpus: _corpus:phase:cd-pu:cd4pu  
_paper: _paper:10.1361/105497101770338707:Cd4Pu  
_tdb: _tdb:CdPu-16Hua.tdb:CD4PU  


### TDB models of CD4PU (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): CD4PU, type code %, sha256 `b0796d759bc2c895…`

~~~~text
70: PHASE CD4PU % 2 4 1 !
71: CONST CD4PU : CD : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_
- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_reports values for this phase_

## CD6PU (Cd–Pu)

- Id: `phase:cd-pu:cd6pu`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (sgte_mmc2): (Cd6Pu) — Hallstedt 2025 mmc2 row for CD6PU: Cd6Pu
- Candidate (sgte_mmc2): Cd6Y · cI184 · Im-3 (204) — Hallstedt 2025 mmc2 row for CD6PU: Cd6Pu
- Candidate (tdb_comment): Cd6Y · cI184 · Im-3 — CdPu-16Hua.tdb: 'Prototype Cd6Y (cI184, Im-3)'
- Stoichiometry: Cd 0.8571, Pu 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–1003.27 K, x(Pu) 0.14286–0.14286
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:cd6pu)

Names (3): _corpus: _corpus:phase:cd-pu:cd6pu  
_paper: _paper:10.1361/105497101770338707:Cd6Pu  
_tdb: _tdb:CdPu-16Hua.tdb:CD6PU  


### TDB models of CD6PU (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): CD6PU, type code %, sha256 `b0796d759bc2c895…`

~~~~text
65: PHASE CD6PU % 2 6 1 !
66: CONST CD6PU : CD : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_
- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_reports values for this phase_

## FCC_A1 (Cd–Pu)

- Id: `phase:cd-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 593.06–910 K, x(Pu) 0.41–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-pu:fcc-a1  
_tdb: _tdb:CdPu-16Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): FCC_A1, type code %A, sha256 `b0796d759bc2c895…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CD PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## HCP_A3 (Cd–Pu)

- Id: `phase:cd-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–594.04 K, x(Pu) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:hcp-a3)

Names (2): _corpus: _corpus:phase:cd-pu:hcp-a3  
_tdb: _tdb:CdPu-16Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): HCP_A3, type code %A, sha256 `b0796d759bc2c895…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## LIQUID (Cd–Pu)

- Id: `phase:cd-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 594.04–4000 K, x(Pu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:liquid)

Names (2): _corpus: _corpus:phase:cd-pu:liquid  
_tdb: _tdb:CdPu-16Hua.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): LIQUID, type code %, sha256 `b0796d759bc2c895…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CD PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## ALPHA_PU (Cd–Pu)

- Id: `phase:cd-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — CdPu-16Hua.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:pu-alpha)

Names (2): _corpus: _corpus:phase:cd-pu:pu-alpha  
_tdb: _tdb:CdPu-16Hua.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): ALPHA_PU, type code %, sha256 `b0796d759bc2c895…`

~~~~text
45: PHASE ALPHA_PU % 1 1 !
46: CONST ALPHA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## BETA_PU (Cd–Pu)

- Id: `phase:cd-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — CdPu-16Hua.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:pu-beta)

Names (2): _corpus: _corpus:phase:cd-pu:pu-beta  
_tdb: _tdb:CdPu-16Hua.tdb:BETA_PU  


### TDB models of BETA_PU (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): BETA_PU, type code %, sha256 `b0796d759bc2c895…`

~~~~text
50: PHASE BETA_PU % 1 1 !
51: CONST BETA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
_assessment that models this phase_

## GAMMA_PU (Cd–Pu)

- Id: `phase:cd-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — CdPu-16Hua.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 487.9–608.06 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pu:pu-gamma)

Names (2): _corpus: _corpus:phase:cd-pu:pu-gamma  
_tdb: _tdb:CdPu-16Hua.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (1): PHASE and CONSTITUENT statements as written

[CdPu-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPu-16Hua.tdb): GAMMA_PU, type code %, sha256 `b0796d759bc2c895…`

~~~~text
55: PHASE GAMMA_PU % 1 1 !
56: CONST GAMMA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.12.004](https://doi.org/10.1016/j.calphad.2015.12.004) Y.X. Huang, Y. Lu, Q. He, Y. Wang, W. Fang, X.J. Liu, J.P. Jia, C.P. Wang, Calphad, 52, 120-24(2016).  
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
