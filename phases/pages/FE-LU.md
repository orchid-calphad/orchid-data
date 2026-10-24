# Fe–Lu phases

> Fe–Lu system: 10 phases (tier A 5, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-LU.html · Markdown: https://data.orchid-project.org/phases/pages/FE-LU.md

10 phases (tier A 5, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-LU) · [full JSON](https://data.orchid-project.org/phases/systems/FE-LU.json) · [Fe–Lu system page](https://data.orchid-project.org/systems/FE-LU.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-LU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Lu system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-lu-bcc-a2); _phase:fe-lu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1822.47 K, x(Lu) 0–0 | 5 | 2 |
| [FCC_A1](#phase-fe-lu-fcc-a1); _phase:fe-lu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1184.81–1667.47 K, x(Lu) 0–0 | 4 | 2 |
| [FE17LU2](#phase-fe-lu-fe17lu2); _phase:fe-lu:fe17lu2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1590.27 K, x(Lu) 0.10526–0.10526 | 12 | 1 |
| [FE17LU2_HT](#phase-fe-lu-fe17lu2-ht); _phase:fe-lu:fe17lu2-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1190.62–1593.22 K, x(Lu) 0.08224–0.10076 | 9 | 1 |
| [FE17LU2_LT](#phase-fe-lu-fe17lu2-lt); _phase:fe-lu:fe17lu2-lt_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 360.42–1192.32 K, x(Lu) 0.08975–0.10526 | 12 | 1 |
| [FE23LU6_D8A](#phase-fe-lu-fe23lu6-d8a); _phase:fe-lu:fe23lu6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1560.91 K, x(Lu) 0.2069–0.2069 | 5 | 2 |
| [FE2LU_C15](#phase-fe-lu-fe2lu-c15); _phase:fe-lu:fe2lu-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1619.28 K, x(Lu) 0.33333–0.33333 | 8 | 2 |
| [FE3LU](#phase-fe-lu-fe3lu); _phase:fe-lu:fe3lu_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1581.75 K, x(Lu) 0.25–0.25 | 22 | 2 |
| [HCP_A3](#phase-fe-lu-hcp-a3); _phase:fe-lu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.64 K, x(Lu) 0.99739–1 | 2 | 2 |
| [LIQUID](#phase-fe-lu-liquid); _phase:fe-lu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1237.63–2500 K, x(Lu) 0–1 | 22 | 2 |

## BCC_A2 (Fe–Lu)

- Id: `phase:fe-lu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1822.47 K, x(Lu) 0–0
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-lu:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.01.003:δFe  
_tdb: _tdb:FeLu-14Kar.tdb:BCC_A2, tdb:FeLu-23Ye.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): BCC_A2, type code %B, sha256 `93d8c09f43286312…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE : VA : !
~~~~

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): BCC_A2, type code %B, sha256 `2a24b752097da078…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Fe–Lu)

- Id: `phase:fe-lu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 1184.81–1667.47 K, x(Lu) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-lu:fcc-a1  
_paper: _paper:10.1016/j.calphad.2014.01.003:γFe  
_tdb: _tdb:FeLu-14Kar.tdb:FCC_A1, tdb:FeLu-23Ye.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): FCC_A1, type code %A, sha256 `93d8c09f43286312…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE : VA : !
~~~~

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): FCC_A1, type code %A, sha256 `2a24b752097da078…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_

## FE17LU2 (Fe–Lu)

- Id: `phase:fe-lu:fe17lu2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — FeLu-23Ye.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc)'
- Stoichiometry: Fe 0.8947, Lu 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 300–1590.27 K, x(Lu) 0.10526–0.10526
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:fe17lu2)

Names (3): _corpus: _corpus:phase:fe-lu:fe17lu2  
_paper: _paper:10.20517/jmi.2023.08:Fe17Lu2  
_tdb: _tdb:FeLu-23Ye.tdb:FE17LU2  


### TDB models of FE17LU2 (1): PHASE and CONSTITUENT statements as written

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): FE17LU2, type code %A, sha256 `2a24b752097da078…`

~~~~text
44: PHASE FE17LU2 %A 2 17 2 !
45: CONST FE17LU2 : FE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_

## FE17LU2_HT (Fe–Lu)

- Id: `phase:fe-lu:fe17lu2-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Fe17Lu2-ht) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Fe17Lu2-ht) — Hallstedt 2025 mmc2 row for FE17LU2_HT: Fe17Lu2 (high T)
- Stability: stable in 1 of 1 calculated diagram(s): 1190.62–1593.22 K, x(Lu) 0.08224–0.10076
- Literature: 9 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:fe17lu2-ht)

Names (4): _corpus: _corpus:phase:fe-lu:fe17lu2-ht  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe17Lu2_HT, paper:10.1016/j.calphad.2014.01.003:αFe17Lu2_HT  
_tdb: _tdb:FeLu-14Kar.tdb:FE17LU2_HT  


### TDB models of FE17LU2_HT (1): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): FE17LU2_HT, type code %, sha256 `93d8c09f43286312…`

~~~~text
53: PHASE FE17LU2_HT % 2 17 2 !
54: CONST FE17LU2_HT : FE : FE LU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_

## FE17LU2_LT (Fe–Lu)

- Id: `phase:fe-lu:fe17lu2-lt`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 360.42–1192.32 K, x(Lu) 0.08975–0.10526
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:fe17lu2-lt)

Names (3): _corpus: _corpus:phase:fe-lu:fe17lu2-lt  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe17Lu2_LT  
_tdb: _tdb:FeLu-14Kar.tdb:FE17LU2_LT  


### TDB models of FE17LU2_LT (1): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): FE17LU2_LT, type code %A, sha256 `93d8c09f43286312…`

~~~~text
48: PHASE FE17LU2_LT %A 2 17 2 !
49: CONST FE17LU2_LT : FE : FE LU% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## FE23LU6_D8A (Fe–Lu)

- Id: `phase:fe-lu:fe23lu6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.7931, Lu 0.2069
- Stability: stable in 2 of 2 calculated diagram(s): 300–1560.91 K, x(Lu) 0.2069–0.2069
- Literature: 5 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:fe23lu6-d8a)

Names (4): _corpus: _corpus:phase:fe-lu:fe23lu6-d8a  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe23Lu6  
_tdb: _tdb:FeLu-14Kar.tdb:FE23LU6_D8A, tdb:FeLu-23Ye.tdb:FE23LU6_D8A  


### TDB models of FE23LU6_D8A (2): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): FE23LU6_D8A, type code %A, sha256 `93d8c09f43286312…`

~~~~text
58: PHASE FE23LU6_D8A %A 2 23 6 !
59: CONST FE23LU6_D8A : FE : LU : !
~~~~

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): FE23LU6_D8A, type code %A, sha256 `2a24b752097da078…`

~~~~text
49: PHASE FE23LU6_D8A %A 2 23 6 !
50: CONST FE23LU6_D8A : FE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_

## FE2LU_C15 (Fe–Lu)

- Id: `phase:fe-lu:fe2lu-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadqt and oqmd-30221, space group 227
- Stoichiometry: Fe 0.6667, Lu 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1619.28 K, x(Lu) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:fe2lu-c15)

Names (6): _corpus: _corpus:phase:fe-lu:fe2lu-c15  
_mp: _mp:mp-aaaaadqt  
_oqmd: _oqmd:oqmd-30221  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe2Lu  
_tdb: _tdb:FeLu-14Kar.tdb:FE2LU_C15, tdb:FeLu-23Ye.tdb:FE2LU_C15  


### TDB models of FE2LU_C15 (2): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): FE2LU_C15, type code %A, sha256 `93d8c09f43286312…`

~~~~text
68: PHASE FE2LU_C15 %A 2 2 1 !
69: CONST FE2LU_C15 : FE : LU : !
~~~~

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): FE2LU_C15, type code %A, sha256 `2a24b752097da078…`

~~~~text
59: PHASE FE2LU_C15 %A 2 2 1 !
60: CONST FE2LU_C15 : FE : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_

## FE3LU (Fe–Lu)

- Id: `phase:fe-lu:fe3lu`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7500, Lu 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1581.75 K, x(Lu) 0.25–0.25
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:fe3lu)

Names (5): _corpus: _corpus:phase:fe-lu:fe3lu  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe3Lu, paper:10.20517/jmi.2023.08:Fe3Lu  
_tdb: _tdb:FeLu-14Kar.tdb:FE3LU, tdb:FeLu-23Ye.tdb:FE3LU  


### TDB models of FE3LU (2): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): FE3LU, type code %A, sha256 `93d8c09f43286312…`

~~~~text
63: PHASE FE3LU %A 2 3 1 !
64: CONST FE3LU : FE : LU : !
~~~~

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): FE3LU, type code %A, sha256 `2a24b752097da078…`

~~~~text
54: PHASE FE3LU %A 2 3 1 !
55: CONST FE3LU : FE : LU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Lu)

- Id: `phase:fe-lu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.64 K, x(Lu) 0.99739–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-lu:hcp-a3  
_paper: _paper:10.1016/j.calphad.2014.01.003:(Lu)  
_tdb: _tdb:FeLu-14Kar.tdb:HCP_A3, tdb:FeLu-23Ye.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): HCP_A3, type code %A, sha256 `93d8c09f43286312…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : FE LU% : VA : !
~~~~

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): HCP_A3, type code %A, sha256 `2a24b752097da078…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE LU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Fe–Lu)

- Id: `phase:fe-lu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1237.63–2500 K, x(Lu) 0–1
- Literature: 22 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-lu:liquid)

Names (6): _corpus: _corpus:phase:fe-lu:liquid  
_paper: _paper:10.1016/j.calphad.2014.01.003:L, paper:10.1016/j.calphad.2014.01.003:Liq, paper:10.20517/jmi.2023.08:L  
_tdb: _tdb:FeLu-14Kar.tdb:LIQUID, tdb:FeLu-23Ye.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FeLu-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-14Kar.tdb): LIQUID, type code %, sha256 `93d8c09f43286312…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE LU : !
~~~~

[FeLu-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLu-23Ye.tdb): LIQUID, type code %, sha256 `2a24b752097da078…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE LU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_

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
