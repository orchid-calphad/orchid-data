# B–Dy phases

> B–Dy system: 11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-DY.html · Markdown: https://data.orchid-project.org/phases/pages/B-DY.md

11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-DY) · [full JSON](https://data.orchid-project.org/phases/systems/B-DY.json) · [B–Dy system page](https://data.orchid-project.org/systems/B-DY.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-DY.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Dy system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-dy-b-alpha-rhombo); _phase:b-dy:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-dy-b-beta-rhombo); _phase:b-dy:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2349.42 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-dy-bcc-a2); _phase:b-dy:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1652.97–1680 K, x(B) 0–0.00044 | 2 | 1 |
| [DYB12_D2F](#phase-b-dy-dyb12-d2f); _phase:b-dy:dyb12-d2f_ | UB12 · D2_f · cF52 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2369.57 K, x(B) 0.92308–0.92308 | 7 | 1 |
| [DYB2_C32](#phase-b-dy-dyb2-c32); _phase:b-dy:dyb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2352.49 K, x(B) 0.66667–0.66667 | 6 | 1 |
| [DYB4_D1E](#phase-b-dy-dyb4-d1e); _phase:b-dy:dyb4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2754.79 K, x(B) 0.8–0.8 | 10 | 1 |
| [DYB6_D21](#phase-b-dy-dyb6-d21); _phase:b-dy:dyb6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2468.46 K, x(B) 0.85714–0.85714 | 7 | 1 |
| [DYB66](#phase-b-dy-dyb66); _phase:b-dy:dyb66_ | YB66 · cF1936 · Fm-3c (226) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 965.53–2365.39 K, x(B) 0.98507–0.98507 | 7 | 1 |
| [FCC_A1](#phase-b-dy-fcc-a1); _phase:b-dy:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-dy-hcp-a3); _phase:b-dy:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1677.97 K, x(B) 0–0.00052 | 5 | 1 |
| [LIQUID](#phase-b-dy-liquid); _phase:b-dy:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1607.59–4000 K, x(B) 0–1 | 24 | 1 |

## ALPHA_RHOMBO_B (B–Dy)

- Id: `phase:b-dy:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — DyB-20Li.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-dy:b-alpha-rhombo  
_tdb: _tdb:DyB-20Li.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): ALPHA_RHOMBO_B, type code %, sha256 `2b087d63468004bc…`

~~~~text
43: PHASE ALPHA_RHOMBO_B % 1 1 !
44: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Dy)

- Id: `phase:b-dy:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — DyB-20Li.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2349.42 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:b-beta-rhombo)

Names (3): _corpus: _corpus:phase:b-dy:b-beta-rhombo, corpus:phase:b-dy:beta-rhombo-b  
_tdb: _tdb:DyB-20Li.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): BETA_RHOMBO_B, type code %, sha256 `2b087d63468004bc…`

~~~~text
48: PHASE BETA_RHOMBO_B % 1 1 !
49: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_

## BCC_A2 (B–Dy)

- Id: `phase:b-dy:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1652.97–1680 K, x(B) 0–0.00044
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:bcc-a2)

Names (3): _corpus: _corpus:phase:b-dy:bcc-a2  
_paper: _paper:10.1016/j.calphad.2020.101740:β-Dy  
_tdb: _tdb:DyB-20Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): BCC_A2, type code %B, sha256 `2b087d63468004bc…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : B DY% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## DYB12_D2F (B–Dy)

- Id: `phase:b-dy:dyb12-d2f`; status `assigned`
- Structure: UB12 · D2_f · cF52 · Fm-3m (225); type `st:d2-f-ub12-cf52`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackujk and oqmd-28341, space group 225
- Stoichiometry: B 0.9231, Dy 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–2369.57 K, x(B) 0.92308–0.92308
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:dyb12-d2f)

Names (5): _corpus: _corpus:phase:b-dy:dyb12-d2f  
_mp: _mp:mp-aaackujk  
_oqmd: _oqmd:oqmd-28341  
_paper: _paper:10.1016/j.calphad.2020.101740:DyB12  
_tdb: _tdb:DyB-20Li.tdb:DYB12_D2F  


### TDB models of DYB12_D2F (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): DYB12_D2F, type code %, sha256 `2b087d63468004bc…`

~~~~text
68: PHASE DYB12_D2F % 2 1 12 !
69: CONST DYB12_D2F : DY : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## DYB2_C32 (B–Dy)

- Id: `phase:b-dy:dyb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadbd and oqmd-8332, space group 191
- Stoichiometry: B 0.6667, Dy 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2352.49 K, x(B) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:dyb2-c32)

Names (5): _corpus: _corpus:phase:b-dy:dyb2-c32  
_mp: _mp:mp-aaaaadbd  
_oqmd: _oqmd:oqmd-8332  
_paper: _paper:10.1016/j.calphad.2020.101740:DyB2  
_tdb: _tdb:DyB-20Li.tdb:DYB2_C32  


### TDB models of DYB2_C32 (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): DYB2_C32, type code %, sha256 `2b087d63468004bc…`

~~~~text
53: PHASE DYB2_C32 % 2 1 2 !
54: CONST DYB2_C32 : DY : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## DYB4_D1E (B–Dy)

- Id: `phase:b-dy:dyb4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaeap and oqmd-12458, space group 127
- Stoichiometry: B 0.8000, Dy 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2754.79 K, x(B) 0.8–0.8
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:dyb4-d1e)

Names (5): _corpus: _corpus:phase:b-dy:dyb4-d1e  
_mp: _mp:mp-aaaaaeap  
_oqmd: _oqmd:oqmd-12458  
_paper: _paper:10.1016/j.calphad.2020.101740:DyB4  
_tdb: _tdb:DyB-20Li.tdb:DYB4_D1E  


### TDB models of DYB4_D1E (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): DYB4_D1E, type code %, sha256 `2b087d63468004bc…`

~~~~text
58: PHASE DYB4_D1E % 2 1 4 !
59: CONST DYB4_D1E : DY : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## DYB6_D21 (B–Dy)

- Id: `phase:b-dy:dyb6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.8571, Dy 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–2468.46 K, x(B) 0.85714–0.85714
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:dyb6-d21)

Names (3): _corpus: _corpus:phase:b-dy:dyb6-d21  
_paper: _paper:10.1016/j.calphad.2020.101740:DyB6  
_tdb: _tdb:DyB-20Li.tdb:DYB6_D21  


### TDB models of DYB6_D21 (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): DYB6_D21, type code %, sha256 `2b087d63468004bc…`

~~~~text
63: PHASE DYB6_D21 % 2 1 6 !
64: CONST DYB6_D21 : DY : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## DYB66 (B–Dy)

- Id: `phase:b-dy:dyb66`; status `assigned`
- Structure: YB66 · cF1936 · Fm-3c (226); type `st:yb66-cf1936`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.9851, Dy 0.0149
- Stability: stable in 1 of 1 calculated diagram(s): 965.53–2365.39 K, x(B) 0.98507–0.98507
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:dyb66)

Names (3): _corpus: _corpus:phase:b-dy:dyb66  
_paper: _paper:10.1016/j.calphad.2020.101740:DyB66  
_tdb: _tdb:DyB-20Li.tdb:DYB66  


### TDB models of DYB66 (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): DYB66, type code %, sha256 `2b087d63468004bc…`

~~~~text
73: PHASE DYB66 % 2 1 66 !
74: CONST DYB66 : DY : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (B–Dy)

- Id: `phase:b-dy:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:fcc-a1)

Names (2): _corpus: _corpus:phase:b-dy:fcc-a1  
_tdb: _tdb:DyB-20Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): FCC_A1, type code %A, sha256 `2b087d63468004bc…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : B DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_

## HCP_A3 (B–Dy)

- Id: `phase:b-dy:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1677.97 K, x(B) 0–0.00052
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:hcp-a3)

Names (3): _corpus: _corpus:phase:b-dy:hcp-a3  
_paper: _paper:10.1016/j.calphad.2020.101740:α-Dy  
_tdb: _tdb:DyB-20Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): HCP_A3, type code %A, sha256 `2b087d63468004bc…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : B DY% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## LIQUID (B–Dy)

- Id: `phase:b-dy:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1607.59–4000 K, x(B) 0–1
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-dy:liquid)

Names (3): _corpus: _corpus:phase:b-dy:liquid  
_paper: _paper:10.1016/j.calphad.2020.101740:L  
_tdb: _tdb:DyB-20Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[DyB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/DyB-20Li.tdb): LIQUID, type code %, sha256 `2b087d63468004bc…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : B DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

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
