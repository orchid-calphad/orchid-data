# Hg–Mg phases

> Hg–Mg system: 11 phases (tier A 8, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HG-MG.html · Markdown: https://data.orchid-project.org/phases/pages/HG-MG.md

11 phases (tier A 8, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HG-MG) · [full JSON](https://data.orchid-project.org/phases/systems/HG-MG.json) · [Hg–Mg system page](https://data.orchid-project.org/systems/HG-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/HG-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hg–Mg system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBO_A10](#phase-hg-mg-a10-rhombo); _phase:hg-mg:a10-rhombo_ | alpha-Hg · A10 · hR1 · R-3m (166) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 3 | 1 |
| [BCC_A2](#phase-hg-mg-bcc-a2); _phase:hg-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-hg-mg-fcc-a1); _phase:hg-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-hg-mg-hcp-a3); _phase:hg-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1258 K, x(Mg) 0.98164–1 | 4 | 1 |
| [HG2MG_C11B](#phase-hg-mg-hg2mg-c11b); _phase:hg-mg:hg2mg-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–441.1 K, x(Mg) 0.33333–0.33333 | 7 | 1 |
| [HG2MG5](#phase-hg-mg-hg2mg5); _phase:hg-mg:hg2mg5_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–794.16 K, x(Mg) 0.71429–0.71429 | 6 | 1 |
| [HG3MG5_D88](#phase-hg-mg-hg3mg5-d88); _phase:hg-mg:hg3mg5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–834 K, x(Mg) 0.625–0.625 | 9 | 1 |
| [HGMG_B2](#phase-hg-mg-hgmg-b2); _phase:hg-mg:hgmg-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–899.22 K, x(Mg) 0.5–0.5 | 11 | 1 |
| [HGMG2_C37](#phase-hg-mg-hgmg2-c37); _phase:hg-mg:hgmg2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–841.39 K, x(Mg) 0.66667–0.66667 | 10 | 1 |
| [HGMG3](#phase-hg-mg-hgmg3); _phase:hg-mg:hgmg3_ | HgMg3 · hR24 · R32 (155) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–780.47 K, x(Mg) 0.75–0.75 | 7 | 1 |
| [LIQUID](#phase-hg-mg-liquid); _phase:hg-mg:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Mg) 0–1 | 34 | 1 |

## RHOMBO_A10 (Hg–Mg)

- Id: `phase:hg-mg:a10-rhombo`; status `assigned`
- Structure: alpha-Hg · A10 · hR1 · R-3m (166); type `st:a10-alpha-hg-hr1`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:a10-rhombo)

Names (4): _corpus: _corpus:phase:hg-mg:a10-rhombo, corpus:phase:hg-mg:rhombo-a10  
_paper: _paper:10.1007/s11771-009-0005-7:Hg  
_tdb: _tdb:HgMg-09Fen.tdb:RHOMBO_A10  


### TDB models of RHOMBO_A10 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): RHOMBO_A10, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
49: PHASE RHOMBO_A10 % 1 1 !
50: CONST RHOMBO_A10 : HG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Hg–Mg)

- Id: `phase:hg-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:bcc-a2)

Names (2): _corpus: _corpus:phase:hg-mg:bcc-a2  
_tdb: _tdb:HgMg-09Fen.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): BCC_A2, type code %B, sha256 `ddfcb316b5d22cbe…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase_

## FCC_A1 (Hg–Mg)

- Id: `phase:hg-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:fcc-a1)

Names (2): _corpus: _corpus:phase:hg-mg:fcc-a1  
_tdb: _tdb:HgMg-09Fen.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): FCC_A1, type code %A, sha256 `ddfcb316b5d22cbe…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : HG MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase_

## HCP_A3 (Hg–Mg)

- Id: `phase:hg-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1258 K, x(Mg) 0.98164–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:hcp-a3)

Names (3): _corpus: _corpus:phase:hg-mg:hcp-a3  
_paper: _paper:10.1007/s11771-009-0005-7:(Mg)  
_tdb: _tdb:HgMg-09Fen.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): HCP_A3, type code %A, sha256 `ddfcb316b5d22cbe…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : HG MG% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## HG2MG_C11B (Hg–Mg)

- Id: `phase:hg-mg:hg2mg-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 0.6667, Mg 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–441.1 K, x(Mg) 0.33333–0.33333
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:hg2mg-c11b)

Names (3): _corpus: _corpus:phase:hg-mg:hg2mg-c11b  
_paper: _paper:10.1007/s11771-009-0005-7:MgHg2  
_tdb: _tdb:HgMg-09Fen.tdb:HG2MG_C11B  


### TDB models of HG2MG_C11B (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): HG2MG_C11B, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
54: PHASE HG2MG_C11B % 2 2 1 !
55: CONST HG2MG_C11B : HG : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## HG2MG5 (Hg–Mg)

- Id: `phase:hg-mg:hg2mg5`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Hg2Mg5) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Hg2Mg5) — Hallstedt 2025 mmc2 row for HG2MG5: Hg2Mg5
- Stoichiometry: Hg 0.2857, Mg 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–794.16 K, x(Mg) 0.71429–0.71429
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:hg2mg5)

Names (3): _corpus: _corpus:phase:hg-mg:hg2mg5  
_paper: _paper:10.1007/s11771-009-0005-7:Mg5Hg2  
_tdb: _tdb:HgMg-09Fen.tdb:HG2MG5  


### TDB models of HG2MG5 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): HG2MG5, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
74: PHASE HG2MG5 % 2 2 5 !
75: CONST HG2MG5 : HG : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## HG3MG5_D88 (Hg–Mg)

- Id: `phase:hg-mg:hg3mg5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqyz and oqmd-17412, space group 193
- Stoichiometry: Hg 0.3750, Mg 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–834 K, x(Mg) 0.625–0.625
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:hg3mg5-d88)

Names (5): _corpus: _corpus:phase:hg-mg:hg3mg5-d88  
_mp: _mp:mp-aaaaaqyz  
_oqmd: _oqmd:oqmd-17412  
_paper: _paper:10.1007/s11771-009-0005-7:Mg5Hg3  
_tdb: _tdb:HgMg-09Fen.tdb:HG3MG5_D88  


### TDB models of HG3MG5_D88 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): HG3MG5_D88, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
64: PHASE HG3MG5_D88 % 2 3 5 !
65: CONST HG3MG5_D88 : HG : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## HGMG_B2 (Hg–Mg)

- Id: `phase:hg-mg:hgmg-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 0.5000, Mg 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–899.22 K, x(Mg) 0.5–0.5
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:hgmg-b2)

Names (3): _corpus: _corpus:phase:hg-mg:hgmg-b2  
_paper: _paper:10.1007/s11771-009-0005-7:MgHg  
_tdb: _tdb:HgMg-09Fen.tdb:HGMG_B2  


### TDB models of HGMG_B2 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): HGMG_B2, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
59: PHASE HGMG_B2 % 2 1 1 !
60: CONST HGMG_B2 : HG : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## HGMG2_C37 (Hg–Mg)

- Id: `phase:hg-mg:hgmg2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 0.3333, Mg 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–841.39 K, x(Mg) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:hgmg2-c37)

Names (3): _corpus: _corpus:phase:hg-mg:hgmg2-c37  
_paper: _paper:10.1007/s11771-009-0005-7:Mg2Hg  
_tdb: _tdb:HgMg-09Fen.tdb:HGMG2_C37  


### TDB models of HGMG2_C37 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): HGMG2_C37, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
69: PHASE HGMG2_C37 % 2 1 2 !
70: CONST HGMG2_C37 : HG : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## HGMG3 (Hg–Mg)

- Id: `phase:hg-mg:hgmg3`; status `assigned`
- Structure: HgMg3 · hR24 · R32 (155); type `st:hgmg3-hr24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hg 0.2500, Mg 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–780.47 K, x(Mg) 0.75–0.75
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:hgmg3)

Names (3): _corpus: _corpus:phase:hg-mg:hgmg3  
_paper: _paper:10.1007/s11771-009-0005-7:Mg3Hg  
_tdb: _tdb:HgMg-09Fen.tdb:HGMG3  


### TDB models of HGMG3 (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): HGMG3, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
79: PHASE HGMG3 % 2 1 3 !
80: CONST HGMG3 : HG : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Hg–Mg)

- Id: `phase:hg-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Mg) 0–1
- Literature: 34 values (34 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-mg:liquid)

Names (3): _corpus: _corpus:phase:hg-mg:liquid  
_paper: _paper:10.1007/s11771-009-0005-7:L  
_tdb: _tdb:HgMg-09Fen.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HgMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/HgMg-09Fen.tdb): LIQUID, type code %, sha256 `ddfcb316b5d22cbe…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : HG MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
