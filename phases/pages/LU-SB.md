# Lu–Sb phases

> Lu–Sb system: 10 phases (tier A 5, tier C 2, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LU-SB.html · Markdown: https://data.orchid-project.org/phases/pages/LU-SB.md

10 phases (tier A 5, tier C 2, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LU-SB) · [full JSON](https://data.orchid-project.org/phases/systems/LU-SB.json) · [Lu–Sb system page](https://data.orchid-project.org/systems/LU-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/LU-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Lu–Sb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-lu-sb-a7-rhombohedral); _phase:lu-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 2 | 1 |
| [BCC_A2](#phase-lu-sb-bcc-a2); _phase:lu-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-lu-sb-fcc-a1); _phase:lu-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-lu-sb-hcp-a3); _phase:lu-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1957.83 K, x(Sb) 0–0.01948 | 2 | 1 |
| [LIQUID](#phase-lu-sb-liquid); _phase:lu-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 900.67–2500 K, x(Sb) 0–1 | 12 | 1 |
| [LU3SB](#phase-lu-sb-lu3sb); _phase:lu-sb:lu3sb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1563.16 K, x(Sb) 0.25–0.25 | 7 | 1 |
| [LU5SB3](#phase-lu-sb-lu5sb3); _phase:lu-sb:lu5sb3_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1843.43 K, x(Sb) 0.375–0.375 | 7 | 1 |
| [LUSB_B1](#phase-lu-sb-lusb-b1); _phase:lu-sb:lusb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2139.13 K, x(Sb) 0.5–0.5 | 10 | 1 |
| [LUSB_BETA](#phase-lu-sb-lusb-beta); _phase:lu-sb:lusb-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2139.13–2453.24 K, x(Sb) 0.5–0.5 | 4 | 1 |
| [LUSB2](#phase-lu-sb-lusb2); _phase:lu-sb:lusb2_ | HoSb2 · oC6 · C222 (21) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1202.47 K, x(Sb) 0.66667–0.66667 | 9 | 1 |

## RHOMBOHEDRAL_A7 (Lu–Sb)

- Id: `phase:lu-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:lu-sb:a7-rhombohedral, corpus:phase:lu-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2011.05.003:(Sb)  
_tdb: _tdb:LuSb-11Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `2d5ed9c2ebfd6144…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_

## BCC_A2 (Lu–Sb)

- Id: `phase:lu-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:bcc-a2)

Names (2): _corpus: _corpus:phase:lu-sb:bcc-a2  
_tdb: _tdb:LuSb-11Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): BCC_A2, type code %B, sha256 `2d5ed9c2ebfd6144…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase_

## FCC_A1 (Lu–Sb)

- Id: `phase:lu-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:lu-sb:fcc-a1  
_tdb: _tdb:LuSb-11Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): FCC_A1, type code %A, sha256 `2d5ed9c2ebfd6144…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase_

## HCP_A3 (Lu–Sb)

- Id: `phase:lu-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1957.83 K, x(Sb) 0–0.01948
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:lu-sb:hcp-a3  
_paper: _paper:10.1016/j.calphad.2011.05.003:(Lu)  
_tdb: _tdb:LuSb-11Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): HCP_A3, type code %A, sha256 `2d5ed9c2ebfd6144…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : LU% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_

## LIQUID (Lu–Sb)

- Id: `phase:lu-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 900.67–2500 K, x(Sb) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:liquid)

Names (3): _corpus: _corpus:phase:lu-sb:liquid  
_paper: _paper:10.1016/j.calphad.2011.05.003:L  
_tdb: _tdb:LuSb-11Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): LIQUID, type code %, sha256 `2d5ed9c2ebfd6144…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : LU SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_

## LU3SB (Lu–Sb)

- Id: `phase:lu-sb:lu3sb`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Lu3Sb) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Lu3Sb) — Hallstedt 2025 mmc2 row for LU3SB: Lu3Sb
- Stoichiometry: Lu 0.7500, Sb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1563.16 K, x(Sb) 0.25–0.25
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:lu3sb)

Names (3): _corpus: _corpus:phase:lu-sb:lu3sb  
_paper: _paper:10.1016/j.calphad.2011.05.003:Lu3Sb  
_tdb: _tdb:LuSb-11Wan.tdb:LU3SB  


### TDB models of LU3SB (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): LU3SB, type code %, sha256 `2d5ed9c2ebfd6144…`

~~~~text
45: PHASE LU3SB % 2 3 1 !
46: CONST LU3SB : LU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## LU5SB3 (Lu–Sb)

- Id: `phase:lu-sb:lu5sb3`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Lu 0.6250, Sb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1843.43 K, x(Sb) 0.375–0.375
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:lu5sb3)

Names (3): _corpus: _corpus:phase:lu-sb:lu5sb3  
_paper: _paper:10.1016/j.calphad.2011.05.003:Lu5Sb3  
_tdb: _tdb:LuSb-11Wan.tdb:LU5SB3  


### TDB models of LU5SB3 (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): LU5SB3, type code %, sha256 `2d5ed9c2ebfd6144…`

~~~~text
50: PHASE LU5SB3 % 2 5 3 !
51: CONST LU5SB3 : LU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## LUSB_B1 (Lu–Sb)

- Id: `phase:lu-sb:lusb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Lu 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2139.13 K, x(Sb) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:lusb-b1)

Names (3): _corpus: _corpus:phase:lu-sb:lusb-b1  
_paper: _paper:10.1016/j.calphad.2011.05.003:αLuSb  
_tdb: _tdb:LuSb-11Wan.tdb:LUSB_B1  


### TDB models of LUSB_B1 (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): LUSB_B1, type code %, sha256 `2d5ed9c2ebfd6144…`

~~~~text
55: PHASE LUSB_B1 % 2 1 1 !
56: CONST LUSB_B1 : LU : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(74)85109-9](https://doi.org/10.1016/0040-6031%2874%2985109-9) K.S. Chua, J.N. Pratt, A simple direct-reaction calorimeter and some observations on the heats of formation of IIIA-VB sodium chloride structures, Thermochimica Acta 8, 409-421 (1974).  
_cited as the source of values for this phase_

## LUSB_BETA (Lu–Sb)

- Id: `phase:lu-sb:lusb-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Fm-3m (225) — on-hull MP LuSb at x(SB)=0.5000
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD Lu1 Sb1 at x(SB)=0.5000
- Candidate (sgte_mmc2): (LuSb-beta) — Hallstedt 2025 mmc2 row for LUSB_BETA: LuSb-beta
- Stoichiometry: Lu 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 2139.13–2453.24 K, x(Sb) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:lusb-beta)

Names (3): _corpus: _corpus:phase:lu-sb:lusb-beta  
_paper: _paper:10.1016/j.calphad.2011.05.003:βLuSb  
_tdb: _tdb:LuSb-11Wan.tdb:LUSB_BETA  


### TDB models of LUSB_BETA (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): LUSB_BETA, type code %, sha256 `2d5ed9c2ebfd6144…`

~~~~text
60: PHASE LUSB_BETA % 2 1 1 !
61: CONST LUSB_BETA : LU : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_

## LUSB2 (Lu–Sb)

- Id: `phase:lu-sb:lusb2`; status `assigned`
- Structure: HoSb2 · oC6 · C222 (21); type `st:hosb2-oc6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Lu 0.3333, Sb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1202.47 K, x(Sb) 0.66667–0.66667
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-sb:lusb2)

Names (3): _corpus: _corpus:phase:lu-sb:lusb2  
_paper: _paper:10.1016/j.calphad.2011.05.003:LuSb2  
_tdb: _tdb:LuSb-11Wan.tdb:LUSB2  


### TDB models of LUSB2 (1): PHASE and CONSTITUENT statements as written

[LuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuSb-11Wan.tdb): LUSB2, type code %, sha256 `2d5ed9c2ebfd6144…`

~~~~text
65: PHASE LUSB2 % 2 1 2 !
66: CONST LUSB2 : LU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90004-4](https://doi.org/10.1016/0022-5088%2890%2990004-4) M.N. Abdusalyamova, N.D. Faslyeva, A.A. Eliseev, E.A. Shishkin, O.I. Rakhmatov, A.G. Chuiko et al., The Lu-Sb system, Journal of the Less Common Metals 166, 229-232 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

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
