# Al–Li phases

> Al–Li system: 12 phases (tier A 6, tier C 2, liquid 1, needs_review 3); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-LI.html · Markdown: https://data.orchid-project.org/phases/pages/AL-LI.md

12 phases (tier A 6, tier C 2, liquid 1, needs_review 3); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-LI) · [full JSON](https://data.orchid-project.org/phases/systems/AL-LI.json) · [Al–Li system page](https://data.orchid-project.org/systems/AL-LI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-LI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Li system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2LI3](#phase-al-li-al2li3); _phase:al-li:al2li3_ | Al2Li3 · hR5 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–793.67 K, x(Li) 0.6–0.6 | 14 | 8 |
| [AL4LI9](#phase-al-li-al4li9); _phase:al-li:al4li9_ | Al4Li9 · mC26 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–609.6 K, x(Li) 0.69231–0.69231 | 12 | 8 |
| [ALLI_B32](#phase-al-li-alli-b32); _phase:al-li:alli-b32_ | NaTl · B32 · cF16 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–977.6 K, x(Li) 0.46269–0.55521 | 0 | 2 |
| [ALLI2](#phase-al-li-alli2); _phase:al-li:alli2_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–610.14 K, x(Li) 0.64–0.65936 | 4 | 4 |
| [BCC_4SL](#phase-al-li-bcc-4sl); _phase:al-li:bcc-4sl_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–974.56 K, x(Li) 0.44522–1 | 19 | 5 |
| [BCC_A2](#phase-al-li-bcc-a2); _phase:al-li:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 12 calculated diagram(s): 300–772.87 K, x(Li) 0.99413–1 | 5 | 14 |
| [B32_BCC](#phase-al-li-bcc-b32); _phase:al-li:bcc-b32_ | NaTl · B32 · cF16 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–975.08 K, x(Li) 0.4646–1 | 0 | 1 |
| [FCC_4SL](#phase-al-li-fcc-4sl); _phase:al-li:fcc-4sl_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–933.51 K, x(Li) 0–0.13814 | 0 | 6 |
| [FCC_A1](#phase-al-li-fcc-a1); _phase:al-li:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 7 of 12 calculated diagram(s): 300–934.11 K, x(Li) 0–0.15499 | 8 | 14 |
| [L12_FCC](#phase-al-li-fcc-l12); _phase:al-li:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–933.58 K, x(Li) 0–0.15499 | 0 | 1 |
| [HCP_A3](#phase-al-li-hcp-a3); _phase:al-li:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 8 |
| [LIQUID](#phase-al-li-liquid); _phase:al-li:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 447.76–2500 K, x(Li) 0–1 | 33 | 8 |

## AL2LI3 (Al–Li)

- Id: `phase:al-li:al2li3`; status `assigned`
- Structure: Al2Li3 · hR5 · R-3m (166); type `st:al2li3-hr5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Li 0.6000
- Stability: stable in 7 of 7 calculated diagram(s): 300–793.67 K, x(Li) 0.6–0.6
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:al2li3)

Names (11): _corpus: _corpus:phase:al-li:al2li3  
_paper: _paper:10.1007/s11669-020-00827-z:Al2Li3, paper:10.1016/s0364-5916(98)00037-6:Al2Li3  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:AL2LI3, tdb:AlLi-07Hal.tdb:AL2LI3, tdb:AlLi-11Guo.tdb:AL2LI3, tdb:AlLi-20Lon.tdb:AL2LI3, tdb:AlLi-23Cui-reg2.tdb:AL2LI3, tdb:AlLi-23Cui-reg3.tdb:AL2LI3, tdb:AlLi-24Liu.tdb:AL2LI3, tdb:AlLi-89Sau-LB.tdb:AL2LI3  


### TDB models of AL2LI3 (8): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): AL2LI3, type code %, sha256 `e5680b08c1df1ba6…`

~~~~text
65: PHASE AL2LI3 % 2 2 3 !
66: CONST AL2LI3 : AL : LI : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): AL2LI3, type code %, sha256 `78495fabf676b01c…`

~~~~text
64: PHASE AL2LI3 % 2 2 3 !
65: CONST AL2LI3 : AL : LI : !
~~~~

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): AL2LI3, type code %, sha256 `382ed9c65e84687b…`

~~~~text
53: PHASE AL2LI3 % 2 2 3 !
54: CONST AL2LI3 : AL : LI : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): AL2LI3, type code %, sha256 `936c9bbf5ba6a805…`

~~~~text
66: PHASE AL2LI3 % 2 2 3 !
67: CONST AL2LI3 : AL : LI : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): AL2LI3, type code %, sha256 `14bb1a0a18b09f82…`

~~~~text
69: PHASE AL2LI3 % 2 2 3 !
70: CONST AL2LI3 : AL : LI : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): AL2LI3, type code %, sha256 `e05d559facd6eb60…`

~~~~text
69: PHASE AL2LI3 % 2 2 3 !
70: CONST AL2LI3 : AL : LI : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): AL2LI3, type code %, sha256 `32893aa7d9de4856…`

~~~~text
64: PHASE AL2LI3 % 2 2 3 !
65: CONST AL2LI3 : AL : LI : !
~~~~

[AlLi-89Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-89Sau-LB.tdb): AL2LI3, type code %, sha256 `2ee512366f415a06…`

~~~~text
46: PHASE AL2LI3 % 2 2 3 !
47: CONST AL2LI3 : AL : LI : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.11.006](https://doi.org/10.1016/j.calphad.2010.11.006) Cuiping Guo, Yu Liang, Changrong Li, Zhenmin Du, Thermodynamic description of the Al–Li–Zn system, Calphad 35, 54-65 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-801209](https://doi.org/10.1515/ijmr-1989-801209) N. Saunders, Z. Metallkd., 80, 894-903 (1989)  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1007/bf02647619](https://doi.org/10.1007/bf02647619) R. J. Pulham, P. Hubberstey, P. Hemptenmacher, Solutions of aluminum in liquid lithium: contribution to the Li-Al phase diagram, JPE 15, 587-590 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2010.08.029](https://doi.org/10.1016/j.jssc.2010.08.029) Kati Puhakainen, Magnus Boström, Thomas L. Groy, Ulrich Häussermann, A new phase in the system lithium–aluminum: Characterization of orthorhombic Li2Al, Journal of Solid State Chemistry 183, 2528-2533 (2010).  
_cited as the source of values for this phase_

## AL4LI9 (Al–Li)

- Id: `phase:al-li:al4li9`; status `assigned`
- Structure: Al4Li9 · mC26 · C2/m (12); type `st:al4li9-mc26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.3077, Li 0.6923
- Stability: stable in 7 of 7 calculated diagram(s): 300–609.6 K, x(Li) 0.69231–0.69231
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:al4li9)

Names (11): _corpus: _corpus:phase:al-li:al4li9  
_paper: _paper:10.1007/s11669-020-00827-z:Al4Li9, paper:10.1016/s0364-5916(98)00037-6:Al4Li9  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:AL4LI9, tdb:AlLi-07Hal.tdb:AL4LI9, tdb:AlLi-11Guo.tdb:AL4LI9, tdb:AlLi-20Lon.tdb:AL4LI9, tdb:AlLi-23Cui-reg2.tdb:AL4LI9, tdb:AlLi-23Cui-reg3.tdb:AL4LI9, tdb:AlLi-24Liu.tdb:AL4LI9, tdb:AlLi-89Sau-LB.tdb:AL4LI9  


### TDB models of AL4LI9 (8): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): AL4LI9, type code %, sha256 `e5680b08c1df1ba6…`

~~~~text
70: PHASE AL4LI9 % 2 4 9 !
71: CONST AL4LI9 : AL : LI : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): AL4LI9, type code %, sha256 `78495fabf676b01c…`

~~~~text
69: PHASE AL4LI9 % 2 4 9 !
70: CONST AL4LI9 : AL : LI : !
~~~~

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): AL4LI9, type code %, sha256 `382ed9c65e84687b…`

~~~~text
58: PHASE AL4LI9 % 2 4 9 !
59: CONST AL4LI9 : AL : LI : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): AL4LI9, type code %, sha256 `936c9bbf5ba6a805…`

~~~~text
76: PHASE AL4LI9 % 2 4 9 !
77: CONST AL4LI9 : AL : LI : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): AL4LI9, type code %, sha256 `14bb1a0a18b09f82…`

~~~~text
79: PHASE AL4LI9 % 2 4 9 !
80: CONST AL4LI9 : AL : LI : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): AL4LI9, type code %, sha256 `e05d559facd6eb60…`

~~~~text
79: PHASE AL4LI9 % 2 4 9 !
80: CONST AL4LI9 : AL : LI : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): AL4LI9, type code %, sha256 `32893aa7d9de4856…`

~~~~text
74: PHASE AL4LI9 % 2 4 9 !
75: CONST AL4LI9 : AL : LI : !
~~~~

[AlLi-89Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-89Sau-LB.tdb): AL4LI9, type code %, sha256 `2ee512366f415a06…`

~~~~text
51: PHASE AL4LI9 % 2 4 9 !
52: CONST AL4LI9 : AL : LI : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.11.006](https://doi.org/10.1016/j.calphad.2010.11.006) Cuiping Guo, Yu Liang, Changrong Li, Zhenmin Du, Thermodynamic description of the Al–Li–Zn system, Calphad 35, 54-65 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-801209](https://doi.org/10.1515/ijmr-1989-801209) N. Saunders, Z. Metallkd., 80, 894-903 (1989)  
_assessment that models this phase_
- [doi:10.1007/bf02647619](https://doi.org/10.1007/bf02647619) R. J. Pulham, P. Hubberstey, P. Hemptenmacher, Solutions of aluminum in liquid lithium: contribution to the Li-Al phase diagram, JPE 15, 587-590 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1016/j.jssc.2010.08.029](https://doi.org/10.1016/j.jssc.2010.08.029) Kati Puhakainen, Magnus Boström, Thomas L. Groy, Ulrich Häussermann, A new phase in the system lithium–aluminum: Characterization of orthorhombic Li2Al, Journal of Solid State Chemistry 183, 2528-2533 (2010).  
_cited as the source of values for this phase_

## ALLI_B32 (Al–Li)

- Id: `phase:al-li:alli-b32`; status `assigned`
- Structure: NaTl · B32 · cF16 · Fd-3m (227); type `st:b32-natl-cf16`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–977.6 K, x(Li) 0.46269–0.55521
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:alli-b32)

Names (3): _corpus: _corpus:phase:al-li:alli-b32  
_tdb: _tdb:AlLi-24Liu.tdb:ALLI_B32, tdb:AlLi-89Sau-LB.tdb:ALLI_B32  


### TDB models of ALLI_B32 (2): PHASE and CONSTITUENT statements as written

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): ALLI_B32, type code %, sha256 `32893aa7d9de4856…`

~~~~text
79: PHASE ALLI_B32 % 2 1 1 !
80: CONST ALLI_B32 : AL% LI : LI% VA : !
~~~~

[AlLi-89Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-89Sau-LB.tdb): ALLI_B32, type code %, sha256 `2ee512366f415a06…`

~~~~text
56: PHASE ALLI_B32 % 2 1 1 !
57: CONST ALLI_B32 : AL% LI : LI% VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-801209](https://doi.org/10.1515/ijmr-1989-801209) N. Saunders, Z. Metallkd., 80, 894-903 (1989)  
_assessment that models this phase_

## ALLI2 (Al–Li)

- Id: `phase:al-li:alli2`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): GaLi2 · oC12 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): GaLi2 · oC12 · Cmcm (63) — Hallstedt 2025 mmc2 row for ALLI2: AlLi2
- Candidate (tdb_comment): GaLi2 · oC12 · Cmcm — AlLi-20Lon.tdb: 'Prototype GaLi2 (oC12, Cmcm)'
- Candidate (tdb_comment): GaLi2 · oC12 · Cmcm — AlLi-23Cui-reg2.tdb: 'Prototype GaLi2 (oC12, Cmcm)'
- Candidate (tdb_comment): GaLi2 · oC12 · Cmcm — AlLi-23Cui-reg3.tdb: 'Prototype GaLi2 (oC12, Cmcm)'
- Candidate (tdb_comment): GaLi2 · oC12 · Cmcm — AlLi-24Liu.tdb: 'Prototype GaLi2 (oC12, Cmcm)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–610.14 K, x(Li) 0.64–0.65936
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:alli2)

Names (6): _corpus: _corpus:phase:al-li:alli2  
_paper: _paper:10.1007/s11669-020-00827-z:AlLi2  
_tdb: _tdb:AlLi-20Lon.tdb:ALLI2, tdb:AlLi-23Cui-reg2.tdb:ALLI2, tdb:AlLi-23Cui-reg3.tdb:ALLI2, tdb:AlLi-24Liu.tdb:ALLI2  


### TDB models of ALLI2 (4): PHASE and CONSTITUENT statements as written

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): ALLI2, type code %, sha256 `936c9bbf5ba6a805…`

~~~~text
71: PHASE ALLI2 % 2 0.36 0.64 !
72: CONST ALLI2 : AL% LI : LI : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): ALLI2, type code %, sha256 `14bb1a0a18b09f82…`

~~~~text
74: PHASE ALLI2 % 2 0.36 0.64 !
75: CONST ALLI2 : AL% LI : LI : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): ALLI2, type code %, sha256 `e05d559facd6eb60…`

~~~~text
74: PHASE ALLI2 % 2 0.36 0.64 !
75: CONST ALLI2 : AL% LI : LI : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): ALLI2, type code %, sha256 `32893aa7d9de4856…`

~~~~text
69: PHASE ALLI2 % 2 0.36 0.64 !
70: CONST ALLI2 : AL : LI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2010.08.029](https://doi.org/10.1016/j.jssc.2010.08.029) Kati Puhakainen, Magnus Boström, Thomas L. Groy, Ulrich Häussermann, A new phase in the system lithium–aluminum: Characterization of orthorhombic Li2Al, Journal of Solid State Chemistry 183, 2528-2533 (2010).  
_cited as the source of values for this phase_

## BCC_4SL (Al–Li)

- Id: `phase:al-li:bcc-4sl`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:order_disorder_ambiguity; order_disorder_ambiguity:AlLi-07Hal-condensed.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-07Hal.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-20Lon.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-23Cui-reg2.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-23Cui-reg3.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:BCC_4SL; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Cmcm (63) — on-hull MP Li2Al at x(LI)=0.6667
- Candidate (dft_mp): R-3m (166) — on-hull MP Li3Al2 at x(LI)=0.6000
- Candidate (dft_mp): Fd-3m (227) — on-hull MP LiAl at x(LI)=0.5000
- Candidate (dft_oqmd): Fd-3m (227) — on-hull OQMD Al1 Li1 at x(LI)=0.5000
- Candidate (dft_oqmd): R-3m (166) — on-hull OQMD Al2 Li3 at x(LI)=0.6000
- Candidate (dft_oqmd): P-3m1 (164) — on-hull OQMD Al4 Li5 at x(LI)=0.5556
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Al4 Li9 at x(LI)=0.6923
- Candidate (literature_printed): NaTl · cF16 — printed with a label mapped to this phase
- Stability: stable in 4 of 4 calculated diagram(s): 300–974.56 K, x(Li) 0.44522–1
- Literature: 19 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:bcc-4sl)

Names (8): _corpus: _corpus:phase:al-li:bcc-4sl  
_paper: _paper:10.1007/s11669-020-00827-z:AlLi, paper:10.1016/s0364-5916(98)00037-6:AlLi  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:BCC_4SL, tdb:AlLi-07Hal.tdb:BCC_4SL, tdb:AlLi-20Lon.tdb:BCC_4SL, tdb:AlLi-23Cui-reg2.tdb:BCC_4SL, tdb:AlLi-23Cui-reg3.tdb:BCC_4SL  


### TDB models of BCC_4SL (5): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): BCC_4SL, type code %BO, sha256 `e5680b08c1df1ba6…`

~~~~text
55: PHASE BCC_4SL:B %BO 5 0.25 0.25 0.25 0.25 3 !
56: CONST BCC_4SL:B : AL% LI : AL LI% : AL LI% : AL% LI : VA : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): BCC_4SL, type code %DO, sha256 `78495fabf676b01c…`

~~~~text
54: PHASE BCC_4SL %DO 5 0.25 0.25 0.25 0.25 3 !
55: CONST BCC_4SL : AL% LI : AL LI% : AL LI% : AL% LI : VA : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): BCC_4SL, type code %BO, sha256 `936c9bbf5ba6a805…`

~~~~text
56: PHASE BCC_4SL:B %BO 5 0.25 0.25 0.25 0.25 3 !
57: CONST BCC_4SL:B : AL% LI : AL LI% : AL LI% : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): BCC_4SL, type code %BO, sha256 `14bb1a0a18b09f82…`

~~~~text
59: PHASE BCC_4SL:B %BO 5 0.25 0.25 0.25 0.25 3 !
60: CONST BCC_4SL:B : AL% LI : AL LI% : AL LI% : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): BCC_4SL, type code %BO, sha256 `e05d559facd6eb60…`

~~~~text
59: PHASE BCC_4SL:B %BO 5 0.25 0.25 0.25 0.25 3 !
60: CONST BCC_4SL:B : AL% LI : AL LI% : AL LI% : AL% LI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## BCC_A2 (Al–Li)

- Id: `phase:al-li:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 12 calculated diagram(s): 300–772.87 K, x(Li) 0.99413–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:bcc-a2)

Names (17): _corpus: _corpus:phase:al-li:bcc-a2  
_paper: _paper:10.1007/s11669-020-00827-z:bcc(Li), paper:10.1016/s0364-5916(98)00037-6:bcc-A2  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:A2_BCC, tdb:AlLi-07Hal-condensed.tdb:BCC_A2, tdb:AlLi-07Hal.tdb:A2_BCC, tdb:AlLi-07Hal.tdb:BCC_A2, tdb:AlLi-11Guo.tdb:A2_BCC, tdb:AlLi-11Guo.tdb:BCC_A2, tdb:AlLi-20Lon.tdb:A2_BCC, tdb:AlLi-20Lon.tdb:BCC_A2, tdb:AlLi-23Cui-reg2.tdb:A2_BCC, tdb:AlLi-23Cui-reg2.tdb:BCC_A2, tdb:AlLi-23Cui-reg3.tdb:A2_BCC, tdb:AlLi-23Cui-reg3.tdb:BCC_A2, tdb:AlLi-24Liu.tdb:BCC_A2, tdb:AlLi-89Sau-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (14): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): A2_BCC, type code %B, sha256 `e5680b08c1df1ba6…`

~~~~text
49: PHASE A2_BCC %B 2 1 3 !
50: CONST A2_BCC : AL LI% : VA : !
~~~~

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): BCC_A2, type code %B, sha256 `e5680b08c1df1ba6…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : AL LI% : VA : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): A2_BCC, type code %, sha256 `78495fabf676b01c…`

~~~~text
48: PHASE A2_BCC % 2 1 3 !
49: CONST A2_BCC : AL LI% : VA : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): BCC_A2, type code %, sha256 `78495fabf676b01c…`

~~~~text
43: PHASE BCC_A2 % 2 1 3 !
44: CONST BCC_A2 : AL LI% : VA : !
~~~~

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): A2_BCC, type code %B, sha256 `382ed9c65e84687b…`

~~~~text
38: PHASE A2_BCC %B 2 1 3 !
39: CONST A2_BCC : AL LI% : VA : !
~~~~

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): BCC_A2, type code %B, sha256 `382ed9c65e84687b…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL LI% : VA : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): A2_BCC, type code %B, sha256 `936c9bbf5ba6a805…`

~~~~text
50: PHASE A2_BCC %B 2 1 3 !
51: CONST A2_BCC : AL LI% : VA : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): BCC_A2, type code %B, sha256 `936c9bbf5ba6a805…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : AL LI% : VA : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): A2_BCC, type code %B, sha256 `14bb1a0a18b09f82…`

~~~~text
53: PHASE A2_BCC %B 2 1 3 !
54: CONST A2_BCC : AL LI% : VA : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): BCC_A2, type code %B, sha256 `14bb1a0a18b09f82…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : AL LI% : VA : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): A2_BCC, type code %B, sha256 `e05d559facd6eb60…`

~~~~text
53: PHASE A2_BCC %B 2 1 3 !
54: CONST A2_BCC : AL LI% : VA : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): BCC_A2, type code %B, sha256 `e05d559facd6eb60…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : AL LI% : VA : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): BCC_A2, type code %B, sha256 `32893aa7d9de4856…`

~~~~text
54: PHASE BCC_A2 %B 2 1 3 !
55: CONST BCC_A2 : AL LI% : VA : !
~~~~

[AlLi-89Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-89Sau-LB.tdb): BCC_A2, type code %B, sha256 `2ee512366f415a06…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AL LI% : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.11.006](https://doi.org/10.1016/j.calphad.2010.11.006) Cuiping Guo, Yu Liang, Changrong Li, Zhenmin Du, Thermodynamic description of the Al–Li–Zn system, Calphad 35, 54-65 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-801209](https://doi.org/10.1515/ijmr-1989-801209) N. Saunders, Z. Metallkd., 80, 894-903 (1989)  
_assessment that models this phase_
- [doi:10.1007/bf02647619](https://doi.org/10.1007/bf02647619) R. J. Pulham, P. Hubberstey, P. Hemptenmacher, Solutions of aluminum in liquid lithium: contribution to the Li-Al phase diagram, JPE 15, 587-590 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## B32_BCC (Al–Li)

- Id: `phase:al-li:bcc-b32`; status `assigned`
- Structure: NaTl · B32 · cF16 · Fd-3m (227); type `st:b32-natl-cf16`; tier A: standard phase name; confidence high
- Caveat: AlLi-11Guo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in AlLi-11Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–975.08 K, x(Li) 0.4646–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:bcc-b32)

Names (2): _corpus: _corpus:phase:al-li:bcc-b32  
_tdb: _tdb:AlLi-11Guo.tdb:B32_BCC  


### TDB models of B32_BCC (1): PHASE and CONSTITUENT statements as written

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): B32_BCC, type code %BO, sha256 `382ed9c65e84687b…`

~~~~text
43: PHASE B32_BCC %BO 3 0.5 0.5 3 !
44: CONST B32_BCC : AL% LI : AL LI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.11.006](https://doi.org/10.1016/j.calphad.2010.11.006) Cuiping Guo, Yu Liang, Changrong Li, Zhenmin Du, Thermodynamic description of the Al–Li–Zn system, Calphad 35, 54-65 (2011).  
_assessment that models this phase_

## FCC_4SL (Al–Li)

- Id: `phase:al-li:fcc-4sl`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:order_disorder_ambiguity; order_disorder_ambiguity:AlLi-07Hal-condensed.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-07Hal.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-20Lon.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-23Cui-reg2.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-23Cui-reg3.tdb_model_is_partitioned; order_disorder_ambiguity:AlLi-24Liu.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; unrecognised_name_tokens:4SL
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (sgte_mmc2): AuCu3 · L1_2 · cP4 · Pm-3m (221) — Hallstedt 2025 mmc2 row for FCC_4SL: Ag3Mg, Al3Li, AlNi3, AlPt3, Au3Cu, AuCu3, Co3Pt, CoPt3, Cr3Pt, CrPt3, Cu3Pt, FeNi3, Fe3Pt, FePt3, MnNi3, Ni3Pt, NiPt3, Ni3Si (beta-1)
- Candidate (tdb_comment): AuCu · L1_0 · tP4, P4/mmm — AlLi-07Hal-condensed.tdb: 'Prototype AuCu (L1_0, tP4, P4/mmm) and AuCu3 (L1_2, cP4, Pm-3m)'
- Candidate (tdb_comment): AuCu · L1_0 · tP4, P4/mmm — AlLi-07Hal.tdb: 'Prototype AuCu (L1_0, tP4, P4/mmm) and AuCu3 (L1_2, cP4, Pm-3m)'
- Candidate (tdb_comment): AuCu · L1_0 · tP4, P4/mmm — AlLi-20Lon.tdb: 'Prototype AuCu (L1_0, tP4, P4/mmm) and AuCu3 (L1_2, cP4, Pm-3m)'
- Candidate (tdb_comment): AuCu · L1_0 · tP4, P4/mmm — AlLi-23Cui-reg2.tdb: 'Prototype AuCu (L1_0, tP4, P4/mmm) and AuCu3 (L1_2, cP4, Pm-3m)'
- Candidate (tdb_comment): AuCu · L1_0 · tP4, P4/mmm — AlLi-23Cui-reg3.tdb: 'Prototype AuCu (L1_0, tP4, P4/mmm) and AuCu3 (L1_2, cP4, Pm-3m)'
- Candidate (tdb_comment): AuCu · L1_0 · tP4, P4/mmm — AlLi-24Liu.tdb: 'Prototype AuCu (L1_0, tP4, P4/mmm) and AuCu3 (L1_2, cP4, Pm-3m)'
- Stability: stable in 5 of 5 calculated diagram(s): 300–933.51 K, x(Li) 0–0.13814
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:fcc-4sl)

Names (7): _corpus: _corpus:phase:al-li:fcc-4sl  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:FCC_4SL, tdb:AlLi-07Hal.tdb:FCC_4SL, tdb:AlLi-20Lon.tdb:FCC_4SL, tdb:AlLi-23Cui-reg2.tdb:FCC_4SL, tdb:AlLi-23Cui-reg3.tdb:FCC_4SL, tdb:AlLi-24Liu.tdb:FCC_4SL  


### TDB models of FCC_4SL (6): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): FCC_4SL, type code %AY, sha256 `e5680b08c1df1ba6…`

~~~~text
39: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
40: CONST FCC_4SL:F : AL% LI : AL% LI : AL% LI : AL% LI : VA : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): FCC_4SL, type code %CY, sha256 `78495fabf676b01c…`

~~~~text
38: PHASE FCC_4SL %CY 5 0.25 0.25 0.25 0.25 1 !
39: CONST FCC_4SL : AL% LI : AL% LI : AL% LI : AL% LI : VA : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): FCC_4SL, type code %AY, sha256 `936c9bbf5ba6a805…`

~~~~text
40: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
41: CONST FCC_4SL:F : AL% LI : AL% LI : AL% LI : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): FCC_4SL, type code %AY, sha256 `14bb1a0a18b09f82…`

~~~~text
43: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
44: CONST FCC_4SL:F : AL% LI : AL% LI : AL% LI : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): FCC_4SL, type code %AY, sha256 `e05d559facd6eb60…`

~~~~text
43: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
44: CONST FCC_4SL:F : AL% LI : AL% LI : AL% LI : AL% LI : VA : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): FCC_4SL, type code %AY, sha256 `32893aa7d9de4856…`

~~~~text
44: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
45: CONST FCC_4SL:F : AL% LI : AL% LI : AL% LI : AL% LI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase_

## FCC_A1 (Al–Li)

- Id: `phase:al-li:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 12 calculated diagram(s): 300–934.11 K, x(Li) 0–0.15499
- Literature: 8 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:fcc-a1)

Names (17): _corpus: _corpus:phase:al-li:fcc-a1  
_paper: _paper:10.1007/s11669-020-00827-z:fcc(Al), paper:10.1016/s0364-5916(98)00037-6:fcc-A1  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:A1_FCC, tdb:AlLi-07Hal-condensed.tdb:FCC_A1, tdb:AlLi-07Hal.tdb:A1_FCC, tdb:AlLi-07Hal.tdb:FCC_A1, tdb:AlLi-11Guo.tdb:FCC_A1, tdb:AlLi-20Lon.tdb:A1_FCC, tdb:AlLi-20Lon.tdb:FCC_A1, tdb:AlLi-23Cui-reg2.tdb:A1_FCC, tdb:AlLi-23Cui-reg2.tdb:FCC_A1, tdb:AlLi-23Cui-reg3.tdb:A1_FCC, tdb:AlLi-23Cui-reg3.tdb:FCC_A1, tdb:AlLi-24Liu.tdb:A1_FCC, tdb:AlLi-24Liu.tdb:FCC_A1, tdb:AlLi-89Sau-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (14): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): A1_FCC, type code %A, sha256 `e5680b08c1df1ba6…`

~~~~text
34: PHASE A1_FCC %A 2 1 1 !
35: CONST A1_FCC : AL% LI : VA : !
~~~~

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): FCC_A1, type code %A, sha256 `e5680b08c1df1ba6…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL% LI : VA : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): A1_FCC, type code %, sha256 `78495fabf676b01c…`

~~~~text
33: PHASE A1_FCC % 2 1 1 !
34: CONST A1_FCC : AL% LI : VA : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): FCC_A1, type code %, sha256 `78495fabf676b01c…`

~~~~text
28: PHASE FCC_A1 % 2 1 1 !
29: CONST FCC_A1 : AL% LI : VA : !
~~~~

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): FCC_A1, type code %A, sha256 `382ed9c65e84687b…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL% LI : VA : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): A1_FCC, type code %A, sha256 `936c9bbf5ba6a805…`

~~~~text
35: PHASE A1_FCC %A 2 1 1 !
36: CONST A1_FCC : AL% LI : VA : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): FCC_A1, type code %A, sha256 `936c9bbf5ba6a805…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): A1_FCC, type code %A, sha256 `14bb1a0a18b09f82…`

~~~~text
38: PHASE A1_FCC %A 2 1 1 !
39: CONST A1_FCC : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): FCC_A1, type code %A, sha256 `14bb1a0a18b09f82…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): A1_FCC, type code %A, sha256 `e05d559facd6eb60…`

~~~~text
38: PHASE A1_FCC %A 2 1 1 !
39: CONST A1_FCC : AL% LI : VA : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): FCC_A1, type code %A, sha256 `e05d559facd6eb60…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL% LI : VA : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): A1_FCC, type code %A, sha256 `32893aa7d9de4856…`

~~~~text
39: PHASE A1_FCC %A 2 1 1 !
40: CONST A1_FCC : AL% LI : VA : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): FCC_A1, type code %A, sha256 `32893aa7d9de4856…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AL% LI : VA : !
~~~~

[AlLi-89Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-89Sau-LB.tdb): FCC_A1, type code %A, sha256 `2ee512366f415a06…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AL% LI : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.11.006](https://doi.org/10.1016/j.calphad.2010.11.006) Cuiping Guo, Yu Liang, Changrong Li, Zhenmin Du, Thermodynamic description of the Al–Li–Zn system, Calphad 35, 54-65 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-801209](https://doi.org/10.1515/ijmr-1989-801209) N. Saunders, Z. Metallkd., 80, 894-903 (1989)  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## L12_FCC (Al–Li)

- Id: `phase:al-li:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: AlLi-24Liu.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in AlLi-24Liu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–933.58 K, x(Li) 0–0.15499
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:fcc-l12)

Names (2): _corpus: _corpus:phase:al-li:fcc-l12  
_tdb: _tdb:AlLi-24Liu.tdb:L12_FCC  


### TDB models of L12_FCC (1): PHASE and CONSTITUENT statements as written

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): L12_FCC, type code %AL, sha256 `32893aa7d9de4856…`

~~~~text
49: PHASE L12_FCC %AL 3 0.75 0.25 1 !
50: CONST L12_FCC : AL% LI : AL% LI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_

## HCP_A3 (Al–Li)

- Id: `phase:al-li:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:hcp-a3)

Names (9): _corpus: _corpus:phase:al-li:hcp-a3  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:HCP_A3, tdb:AlLi-07Hal.tdb:HCP_A3, tdb:AlLi-11Guo.tdb:HCP_A3, tdb:AlLi-20Lon.tdb:HCP_A3, tdb:AlLi-23Cui-reg2.tdb:HCP_A3, tdb:AlLi-23Cui-reg3.tdb:HCP_A3, tdb:AlLi-24Liu.tdb:HCP_A3, tdb:AlLi-89Sau-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (8): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): HCP_A3, type code %A, sha256 `e5680b08c1df1ba6…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : AL LI : VA : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): HCP_A3, type code %, sha256 `78495fabf676b01c…`

~~~~text
59: PHASE HCP_A3 % 2 1 0.5 !
60: CONST HCP_A3 : AL LI : VA : !
~~~~

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): HCP_A3, type code %A, sha256 `382ed9c65e84687b…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : AL LI : VA : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): HCP_A3, type code %A, sha256 `936c9bbf5ba6a805…`

~~~~text
61: PHASE HCP_A3 %A 2 1 0.5 !
62: CONST HCP_A3 : AL LI : VA : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): HCP_A3, type code %A, sha256 `14bb1a0a18b09f82…`

~~~~text
64: PHASE HCP_A3 %A 2 1 0.5 !
65: CONST HCP_A3 : AL LI : VA : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): HCP_A3, type code %A, sha256 `e05d559facd6eb60…`

~~~~text
64: PHASE HCP_A3 %A 2 1 0.5 !
65: CONST HCP_A3 : AL LI : VA : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): HCP_A3, type code %A, sha256 `32893aa7d9de4856…`

~~~~text
59: PHASE HCP_A3 %A 2 1 0.5 !
60: CONST HCP_A3 : AL LI : VA : !
~~~~

[AlLi-89Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-89Sau-LB.tdb): HCP_A3, type code %A, sha256 `2ee512366f415a06…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AL LI : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.11.006](https://doi.org/10.1016/j.calphad.2010.11.006) Cuiping Guo, Yu Liang, Changrong Li, Zhenmin Du, Thermodynamic description of the Al–Li–Zn system, Calphad 35, 54-65 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-801209](https://doi.org/10.1515/ijmr-1989-801209) N. Saunders, Z. Metallkd., 80, 894-903 (1989)  
_assessment that models this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase_

## LIQUID (Al–Li)

- Id: `phase:al-li:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 447.76–2500 K, x(Li) 0–1
- Literature: 33 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-li:liquid)

Names (11): _corpus: _corpus:phase:al-li:liquid  
_paper: _paper:10.1007/s11669-020-00827-z:L, paper:10.1016/s0364-5916(98)00037-6:Liquid  
_tdb: _tdb:AlLi-07Hal-condensed.tdb:LIQUID, tdb:AlLi-07Hal.tdb:LIQUID, tdb:AlLi-11Guo.tdb:LIQUID, tdb:AlLi-20Lon.tdb:LIQUID, tdb:AlLi-23Cui-reg2.tdb:LIQUID, tdb:AlLi-23Cui-reg3.tdb:LIQUID, tdb:AlLi-24Liu.tdb:LIQUID, tdb:AlLi-89Sau-LB.tdb:LIQUID  


### TDB models of LIQUID (8): PHASE and CONSTITUENT statements as written

[AlLi-07Hal-condensed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal-condensed.tdb): LIQUID, type code %, sha256 `e5680b08c1df1ba6…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL LI : !
~~~~

[AlLi-07Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-07Hal.tdb): LIQUID, type code %, sha256 `78495fabf676b01c…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL LI : !
~~~~

[AlLi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-11Guo.tdb): LIQUID, type code %, sha256 `382ed9c65e84687b…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL LI : !
~~~~

[AlLi-20Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-20Lon.tdb): LIQUID, type code %, sha256 `936c9bbf5ba6a805…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL LI : !
~~~~

[AlLi-23Cui-reg2.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg2.tdb): LIQUID, type code %, sha256 `14bb1a0a18b09f82…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL LI : !
~~~~

[AlLi-23Cui-reg3.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-23Cui-reg3.tdb): LIQUID, type code %, sha256 `e05d559facd6eb60…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL LI : !
~~~~

[AlLi-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-24Liu.tdb): LIQUID, type code %, sha256 `32893aa7d9de4856…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AL LI : !
~~~~

[AlLi-89Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlLi-89Sau-LB.tdb): LIQUID, type code %, sha256 `2ee512366f415a06…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AL LI : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z) Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101553](https://doi.org/10.3139/146.101553) Bengt Hallstedt, Olga Kim, Thermodynamic assessment of the Al–Li system, International Journal of Materials Research 98, 961-969 (2007).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.11.006](https://doi.org/10.1016/j.calphad.2010.11.006) Cuiping Guo, Yu Liang, Changrong Li, Zhenmin Du, Thermodynamic description of the Al–Li–Zn system, Calphad 35, 54-65 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102585](https://doi.org/10.1016/j.calphad.2023.102585) S. Cui, H. Ma, J. Wang, B. Hu, Calphad, 82, 102585(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102752](https://doi.org/10.1016/j.calphad.2024.102752) Y. Liu, S. Liu, Y. Du, Calphad, 87, 102752(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-801209](https://doi.org/10.1515/ijmr-1989-801209) N. Saunders, Z. Metallkd., 80, 894-903 (1989)  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1007/bf02647619](https://doi.org/10.1007/bf02647619) R. J. Pulham, P. Hubberstey, P. Hemptenmacher, Solutions of aluminum in liquid lithium: contribution to the Li-Al phase diagram, JPE 15, 587-590 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2010.08.029](https://doi.org/10.1016/j.jssc.2010.08.029) Kati Puhakainen, Magnus Boström, Thomas L. Groy, Ulrich Häussermann, A new phase in the system lithium–aluminum: Characterization of orthorhombic Li2Al, Journal of Solid State Chemistry 183, 2528-2533 (2010).  
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
