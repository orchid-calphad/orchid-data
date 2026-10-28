# Ge–Lu phases

> Ge–Lu system: 12 phases (tier A 5, tier C 2, liquid 1, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-LU.html · Markdown: https://data.orchid-project.org/phases/pages/GE-LU.md

12 phases (tier A 5, tier C 2, liquid 1, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-LU) · [full JSON](https://data.orchid-project.org/phases/systems/GE-LU.json) · [Ge–Lu system page](https://data.orchid-project.org/systems/GE-LU.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-LU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Lu system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-lu-a4-diamond); _phase:ge-lu:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Lu) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ge-lu-bcc-a2); _phase:ge-lu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ge-lu-fcc-a1); _phase:ge-lu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GE10LU11](#phase-ge-lu-ge10lu11); _phase:ge-lu:ge10lu11_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1983.62 K, x(Lu) 0.52381–0.52381 | 0 | 1 |
| [GE2LU_C49](#phase-ge-lu-ge2lu-c49); _phase:ge-lu:ge2lu-c49_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1332.43 K, x(Lu) 0.358–0.358 | 0 | 1 |
| [GE3LU2_ALPHA](#phase-ge-lu-ge3lu2-alpha); _phase:ge-lu:ge3lu2-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1313.04 K, x(Lu) 0.4–0.4 | 0 | 1 |
| [GE3LU2_C32](#phase-ge-lu-ge3lu2-c32); _phase:ge-lu:ge3lu2-c32_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1313.04–1610 K, x(Lu) 0.4–0.4 | 0 | 1 |
| [GE3LU5_D88](#phase-ge-lu-ge3lu5-d88); _phase:ge-lu:ge3lu5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2316.79 K, x(Lu) 0.625–0.625 | 0 | 1 |
| [GE4LU5](#phase-ge-lu-ge4lu5); _phase:ge-lu:ge4lu5_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1937.72–2208.64 K, x(Lu) 0.55556–0.55556 | 0 | 1 |
| [GE5LU4](#phase-ge-lu-ge5lu4); _phase:ge-lu:ge5lu4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1582.95 K, x(Lu) 0.44444–0.44444 | 0 | 1 |
| [HCP_A3](#phase-ge-lu-hcp-a3); _phase:ge-lu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.75 K, x(Lu) 1–1 | 0 | 1 |
| [LIQUID](#phase-ge-lu-liquid); _phase:ge-lu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1135.25–2500 K, x(Lu) 0–1 | 0 | 1 |

## DIAMOND_A4 (Ge–Lu)

- Id: `phase:ge-lu:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Lu) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:a4-diamond)

Names (2): _corpus: _corpus:phase:ge-lu:a4-diamond  
_tdb: _tdb:GeLu-18Ach.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): DIAMOND_A4, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## BCC_A2 (Ge–Lu)

- Id: `phase:ge-lu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-lu:bcc-a2  
_tdb: _tdb:GeLu-18Ach.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): BCC_A2, type code %B, sha256 `77ad7160d0fe8a37…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## FCC_A1 (Ge–Lu)

- Id: `phase:ge-lu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-lu:fcc-a1  
_tdb: _tdb:GeLu-18Ach.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): FCC_A1, type code %A, sha256 `77ad7160d0fe8a37…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## GE10LU11 (Ge–Lu)

- Id: `phase:ge-lu:ge10lu11`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.4762, Lu 0.5238
- Stability: stable in 1 of 1 calculated diagram(s): 300–1983.62 K, x(Lu) 0.52381–0.52381
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:ge10lu11)

Names (2): _corpus: _corpus:phase:ge-lu:ge10lu11  
_tdb: _tdb:GeLu-18Ach.tdb:GE10LU11  


### TDB models of GE10LU11 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): GE10LU11, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
72: PHASE GE10LU11 % 2 10 11 !
73: CONST GE10LU11 : GE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## GE2LU_C49 (Ge–Lu)

- Id: `phase:ge-lu:ge2lu-c49`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C49; stoichiometry_contradicts_C49:GeLu-18Ach.tdb
- Candidate (name_token): ZrSi2 · C49 · oC12 · Cmcm (63) — Strukturbericht/word 'C49' in the TDB name
- Candidate (sgte_mmc2): ZrSi2 · C49 · oC12 · Cmcm (63) — Hallstedt 2025 mmc2 row for GE2LU_C49: Ge2Lu
- Candidate (tdb_comment): Si2Zr · oC12 · Cmcm — GeLu-18Ach.tdb: 'Prototype Si2Zr (oC12, Cmcm)'
- Stoichiometry: Ge 0.6420, Lu 0.3580
- Stability: stable in 1 of 1 calculated diagram(s): 300–1332.43 K, x(Lu) 0.358–0.358
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:ge2lu-c49)

Names (2): _corpus: _corpus:phase:ge-lu:ge2lu-c49  
_tdb: _tdb:GeLu-18Ach.tdb:GE2LU_C49  


### TDB models of GE2LU_C49 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): GE2LU_C49, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
52: PHASE GE2LU_C49 % 2 0.642 0.358 !
53: CONST GE2LU_C49 : GE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## GE3LU2_ALPHA (Ge–Lu)

- Id: `phase:ge-lu:ge3lu2-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Ge3Lu2-LT) — Hallstedt 2025 mmc2 row for GE3LU2_ALPHA: Ge3Lu2 (low T)
- Stoichiometry: Ge 0.6000, Lu 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1313.04 K, x(Lu) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:ge3lu2-alpha)

Names (2): _corpus: _corpus:phase:ge-lu:ge3lu2-alpha  
_tdb: _tdb:GeLu-18Ach.tdb:GE3LU2_ALPHA  


### TDB models of GE3LU2_ALPHA (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): GE3LU2_ALPHA, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
57: PHASE GE3LU2_ALPHA % 2 3 2 !
58: CONST GE3LU2_ALPHA : GE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## GE3LU2_C32 (Ge–Lu)

- Id: `phase:ge-lu:ge3lu2-c32`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C32; stoichiometry_contradicts_C32:GeLu-18Ach.tdb
- Candidate (name_token): AlB2 · C32 · hP3 · P6/mmm (191) — Strukturbericht/word 'C32' in the TDB name
- Candidate (sgte_mmc2): AlB2 · C32 · hP3 · P6/mmm (191) — Hallstedt 2025 mmc2 row for GE3LU2_C32: Ge3Lu2 (high T)
- Candidate (tdb_comment): AlB2 · hP3 · P6/mmm — GeLu-18Ach.tdb: 'Prototype AlB2 (hP3, P6/mmm)'
- Stoichiometry: Ge 0.6000, Lu 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 1313.04–1610 K, x(Lu) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:ge3lu2-c32)

Names (2): _corpus: _corpus:phase:ge-lu:ge3lu2-c32  
_tdb: _tdb:GeLu-18Ach.tdb:GE3LU2_C32  


### TDB models of GE3LU2_C32 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): GE3LU2_C32, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
62: PHASE GE3LU2_C32 % 2 3 2 !
63: CONST GE3LU2_C32 : GE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## GE3LU5_D88 (Ge–Lu)

- Id: `phase:ge-lu:ge3lu5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackycb and oqmd-30459, space group 193
- Stoichiometry: Ge 0.3750, Lu 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–2316.79 K, x(Lu) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:ge3lu5-d88)

Names (4): _corpus: _corpus:phase:ge-lu:ge3lu5-d88  
_mp: _mp:mp-aaackycb  
_oqmd: _oqmd:oqmd-30459  
_tdb: _tdb:GeLu-18Ach.tdb:GE3LU5_D88  


### TDB models of GE3LU5_D88 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): GE3LU5_D88, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
82: PHASE GE3LU5_D88 % 2 3 5 !
83: CONST GE3LU5_D88 : GE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## GE4LU5 (Ge–Lu)

- Id: `phase:ge-lu:ge4lu5`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.4444, Lu 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 1937.72–2208.64 K, x(Lu) 0.55556–0.55556
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:ge4lu5)

Names (2): _corpus: _corpus:phase:ge-lu:ge4lu5  
_tdb: _tdb:GeLu-18Ach.tdb:GE4LU5  


### TDB models of GE4LU5 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): GE4LU5, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
77: PHASE GE4LU5 % 2 4 5 !
78: CONST GE4LU5 : GE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## GE5LU4 (Ge–Lu)

- Id: `phase:ge-lu:ge5lu4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Ge5Lu4) — Hallstedt 2025 mmc2 row for GE5LU4: Ge5Lu4
- Stoichiometry: Ge 0.5556, Lu 0.4444
- Stability: stable in 1 of 1 calculated diagram(s): 300–1582.95 K, x(Lu) 0.44444–0.44444
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:ge5lu4)

Names (2): _corpus: _corpus:phase:ge-lu:ge5lu4  
_tdb: _tdb:GeLu-18Ach.tdb:GE5LU4  


### TDB models of GE5LU4 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): GE5LU4, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
67: PHASE GE5LU4 % 2 5 4 !
68: CONST GE5LU4 : GE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## HCP_A3 (Ge–Lu)

- Id: `phase:ge-lu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.75 K, x(Lu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-lu:hcp-a3  
_tdb: _tdb:GeLu-18Ach.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): HCP_A3, type code %A, sha256 `77ad7160d0fe8a37…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : GE LU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

## LIQUID (Ge–Lu)

- Id: `phase:ge-lu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1135.25–2500 K, x(Lu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-lu:liquid)

Names (2): _corpus: _corpus:phase:ge-lu:liquid  
_tdb: _tdb:GeLu-18Ach.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeLu-18Ach.tdb](https://orchid-project.org/data/databases/sgte-binary/GeLu-18Ach.tdb): LIQUID, type code %, sha256 `77ad7160d0fe8a37…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : GE LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.05.001](https://doi.org/10.1016/j.calphad.2018.05.001) K. Achgar, N. Selhaoui, A. Iddaoudi, R. Tamim, H. Azza, L. Bouirden, Calphad, 62, 18-29(2018).  
_assessment that models this phase_

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
