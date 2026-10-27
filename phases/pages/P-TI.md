# P–Ti phases

> P–Ti system: 13 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/P-TI.html · Markdown: https://data.orchid-project.org/phases/pages/P-TI.md

13 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=P-TI) · [full JSON](https://data.orchid-project.org/phases/systems/P-TI.json) · [Markdown](https://data.orchid-project.org/phases/pages/P-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the P–Ti system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-p-ti-bcc-a2); _phase:p-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1154.99–2499.94 K, x(P) 0–0.00321 | 0 | 1 |
| [M2P_C22](#phase-p-ti-c22-m2p); _phase:p-ti:c22-m2p_ | Fe2P · C22 · hP9 · P-62m (189) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2192.61 K, x(P) 0.33333–0.33333 | 0 | 1 |
| [FCC_A1](#phase-p-ti-fcc-a1); _phase:p-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-p-ti-hcp-a3); _phase:p-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1939.99 K, x(P) 0–0 | 0 | 1 |
| [LIQUID](#phase-p-ti-liquid); _phase:p-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 852.3–2500 K, x(P) 0–1 | 0 | 1 |
| [RED_P](#phase-p-ti-p-red); _phase:p-ti:p-red_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–852.3 K, x(P) 1–1 | 0 | 1 |
| [WHITE_P](#phase-p-ti-p-white); _phase:p-ti:p-white_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [TI3P](#phase-p-ti-ti3p); _phase:p-ti:ti3p_ | Ti3P · tP32 · P4_2/n (86) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2036.93 K, x(P) 0.25–0.25 | 0 | 1 |
| [TI4P3_D73](#phase-p-ti-ti4p3-d73); _phase:p-ti:ti4p3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 600.91–2333.53 K, x(P) 0.42857–0.42857 | 0 | 1 |
| [TI5P3_ALPHA](#phase-p-ti-ti5p3-alpha); _phase:p-ti:ti5p3-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2105.93 K, x(P) 0.37–0.37 | 0 | 1 |
| [TI5P3_D88](#phase-p-ti-ti5p3-d88); _phase:p-ti:ti5p3-d88_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2360.75 K, x(P) 0.36129–0.39 | 0 | 1 |
| [TIP_BI](#phase-p-ti-tip-bi); _phase:p-ti:tip-bi_ | TiAs · B_i · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2268.81 K, x(P) 0.48437–0.5 | 0 | 1 |
| [TIP2_C37](#phase-p-ti-tip2-c37); _phase:p-ti:tip2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1856.49 K, x(P) 0.66667–0.66667 | 0 | 1 |

## BCC_A2 (P–Ti)

- Id: `phase:p-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1154.99–2499.94 K, x(P) 0–0.00321
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:bcc-a2)

Names (2): _corpus: _corpus:phase:p-ti:bcc-a2  
_tdb: _tdb:TiP-06Oht.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): BCC_A2, type code %B, sha256 `e79ac2694bb46a76…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : P TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## M2P_C22 (P–Ti)

- Id: `phase:p-ti:c22-m2p`; status `assigned`
- Structure: Fe2P · C22 · hP9 · P-62m (189); type `st:c22-fe2p-hp9`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M2P); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: P 0.3333, Ti 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–2192.61 K, x(P) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:c22-m2p)

Names (2): _corpus: _corpus:phase:p-ti:c22-m2p  
_tdb: _tdb:TiP-06Oht.tdb:M2P_C22  


### TDB models of M2P_C22 (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): M2P_C22, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
60: PHASE M2P_C22 % 2 2 1 !
61: CONST M2P_C22 : TI : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## FCC_A1 (P–Ti)

- Id: `phase:p-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:fcc-a1)

Names (2): _corpus: _corpus:phase:p-ti:fcc-a1  
_tdb: _tdb:TiP-06Oht.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): FCC_A1, type code %A, sha256 `e79ac2694bb46a76…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : P TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## HCP_A3 (P–Ti)

- Id: `phase:p-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ti 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1939.99 K, x(P) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:hcp-a3)

Names (2): _corpus: _corpus:phase:p-ti:hcp-a3  
_tdb: _tdb:TiP-06Oht.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): HCP_A3, type code %A, sha256 `e79ac2694bb46a76…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## LIQUID (P–Ti)

- Id: `phase:p-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 852.3–2500 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:liquid)

Names (2): _corpus: _corpus:phase:p-ti:liquid  
_tdb: _tdb:TiP-06Oht.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): LIQUID, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : P TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## RED_P (P–Ti)

- Id: `phase:p-ti:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–852.3 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:p-red)

Names (2): _corpus: _corpus:phase:p-ti:p-red  
_tdb: _tdb:TiP-06Oht.tdb:RED_P  


### TDB models of RED_P (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): RED_P, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
50: PHASE RED_P % 1 1 !
51: CONST RED_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## WHITE_P (P–Ti)

- Id: `phase:p-ti:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:p-white)

Names (2): _corpus: _corpus:phase:p-ti:p-white  
_tdb: _tdb:TiP-06Oht.tdb:WHITE_P  


### TDB models of WHITE_P (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): WHITE_P, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
45: PHASE WHITE_P % 1 1 !
46: CONST WHITE_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## TI3P (P–Ti)

- Id: `phase:p-ti:ti3p`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: P 0.2500, Ti 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–2036.93 K, x(P) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:ti3p)

Names (4): _corpus: _corpus:phase:p-ti:ti3p  
_mp: _mp:mp-aaaabueo  
_oqmd: _oqmd:oqmd-7984  
_tdb: _tdb:TiP-06Oht.tdb:TI3P  


### TDB models of TI3P (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): TI3P, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
55: PHASE TI3P % 2 3 1 !
56: CONST TI3P : TI : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## TI4P3_D73 (P–Ti)

- Id: `phase:p-ti:ti4p3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: P 0.4286, Ti 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 600.91–2333.53 K, x(P) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:ti4p3-d73)

Names (2): _corpus: _corpus:phase:p-ti:ti4p3-d73  
_tdb: _tdb:TiP-06Oht.tdb:TI4P3_D73  


### TDB models of TI4P3_D73 (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): TI4P3_D73, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
75: PHASE TI4P3_D73 % 2 4 3 !
76: CONST TI4P3_D73 : TI : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## TI5P3_ALPHA (P–Ti)

- Id: `phase:p-ti:ti5p3-alpha`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): Sb3Yb5 · oP32 · Pnma (62) — Hallstedt 2025 mmc2 row for TI5P3_ALPHA: Ti5P3 (Ti1.7P)
- Candidate (tdb_comment): Sb3Yb5 · oP32 · Pnma — TiP-06Oht.tdb: 'Prototype Sb3Yb5 (oP32, Pnma), Ti1.7P'
- Stoichiometry: P 0.3700, Ti 0.6300
- Stability: stable in 1 of 1 calculated diagram(s): 300–2105.93 K, x(P) 0.37–0.37
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:ti5p3-alpha)

Names (2): _corpus: _corpus:phase:p-ti:ti5p3-alpha  
_tdb: _tdb:TiP-06Oht.tdb:TI5P3_ALPHA  


### TDB models of TI5P3_ALPHA (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): TI5P3_ALPHA, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
65: PHASE TI5P3_ALPHA % 2 0.63 0.37 !
66: CONST TI5P3_ALPHA : TI : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## TI5P3_D88 (P–Ti)

- Id: `phase:p-ti:ti5p3-d88`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_D8_8; site_ratios_contradict_D8_8:TiP-06Oht.tdb
- Candidate (name_token): Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) — Strukturbericht/word 'D88' in the TDB name
- Candidate (sgte_mmc2): Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) — Hallstedt 2025 mmc2 row for TI5P3_D88: Ti5P3
- Candidate (tdb_comment): Mn5Si3 · hP16 · P6_3/mcm — TiP-06Oht.tdb: 'Prototype Mn5Si3 (hP16, P6_3/mcm)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–2360.75 K, x(P) 0.36129–0.39
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:ti5p3-d88)

Names (2): _corpus: _corpus:phase:p-ti:ti5p3-d88  
_tdb: _tdb:TiP-06Oht.tdb:TI5P3_D88  


### TDB models of TI5P3_D88 (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): TI5P3_D88, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
70: PHASE TI5P3_D88 % 2 0.61 0.39 !
71: CONST TI5P3_D88 : TI : P% TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## TIP_BI (P–Ti)

- Id: `phase:p-ti:tip-bi`; status `assigned`
- Structure: TiAs · B_i · hP8 · P6_3/mmc (194); type `st:b-i-tias-hp8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2268.81 K, x(P) 0.48437–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:tip-bi)

Names (2): _corpus: _corpus:phase:p-ti:tip-bi  
_tdb: _tdb:TiP-06Oht.tdb:TIP_BI  


### TDB models of TIP_BI (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): TIP_BI, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
80: PHASE TIP_BI % 2 1 1 !
81: CONST TIP_BI : TI : P% TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## TIP2_C37 (P–Ti)

- Id: `phase:p-ti:tip2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabebv and oqmd-4606, space group 62
- Stoichiometry: P 0.6667, Ti 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1856.49 K, x(P) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-ti:tip2-c37)

Names (4): _corpus: _corpus:phase:p-ti:tip2-c37  
_mp: _mp:mp-aaaabebv  
_oqmd: _oqmd:oqmd-4606  
_tdb: _tdb:TiP-06Oht.tdb:TIP2_C37  


### TDB models of TIP2_C37 (1): PHASE and CONSTITUENT statements as written

[TiP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiP-06Oht.tdb): TIP2_C37, type code %, sha256 `e79ac2694bb46a76…`

~~~~text
85: PHASE TIP2_C37 % 2 1 2 !
86: CONST TIP2_C37 : TI : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
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
