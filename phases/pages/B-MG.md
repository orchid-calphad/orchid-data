# B–Mg phases

> B–Mg system: 10 phases (tier A 3, tier B 1, tier C 3, liquid 1, gas 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-MG.html · Markdown: https://data.orchid-project.org/phases/pages/B-MG.md

10 phases (tier A 3, tier B 1, tier C 3, liquid 1, gas 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-MG) · [full JSON](https://data.orchid-project.org/phases/systems/B-MG.json) · [B–Mg system page](https://data.orchid-project.org/systems/B-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Mg system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-mg-b-beta-rhombo); _phase:b-mg:b-beta-rhombo_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2351.38 K, x(B) 1–1 | 0 | 2 |
| [BCC_A2](#phase-b-mg-bcc-a2); _phase:b-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [MB2_C32](#phase-b-mg-c32-mb2); _phase:b-mg:c32-mb2_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1979.09 K, x(B) 0.66667–0.66667 | 27 | 2 |
| [FCC_A1](#phase-b-mg-fcc-a1); _phase:b-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-b-mg-gas); _phase:b-mg:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 1367.63–4000 K, x(B) 0–0.52475 | 4 | 2 |
| [HCP_A3](#phase-b-mg-hcp-a3); _phase:b-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1468 K, x(B) 0–0 | 1 | 2 |
| [LIQUID](#phase-b-mg-liquid); _phase:b-mg:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 922.85–4000 K, x(B) 0–1 | 4 | 2 |
| [MGB20](#phase-b-mg-mgb20); _phase:b-mg:mgb20_ | ScB28 · hR119 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2465.49 K, x(B) 0.95238–0.95238 | 12 | 1 |
| [MGB4](#phase-b-mg-mgb4); _phase:b-mg:mgb4_ | MgB4 · oP20 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2281.82 K, x(B) 0.8–0.8 | 27 | 2 |
| [MGB7](#phase-b-mg-mgb7); _phase:b-mg:mgb7_ | MgB7 · oI64 · Imma (74) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–2424.01 K, x(B) 0.875–0.875 | 18 | 2 |

## BETA_RHOMBO_B (B–Mg)

- Id: `phase:b-mg:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — MgB-01Liu-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — MgB-05Bal.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2351.38 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:b-beta-rhombo)

Names (4): _corpus: _corpus:phase:b-mg:b-beta-rhombo, corpus:phase:b-mg:beta-rhombo-b  
_tdb: _tdb:MgB-01Liu-LB.tdb:BETA_RHOMBO_B, tdb:MgB-05Bal.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `8309e62bcb5a44e3…`

~~~~text
47: PHASE BETA_RHOMBO_B % 1 1 !
48: CONST BETA_RHOMBO_B : B : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): BETA_RHOMBO_B, type code %, sha256 `560f62e9d31af938…`

~~~~text
49: PHASE BETA_RHOMBO_B % 1 1 !
50: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase_

## BCC_A2 (B–Mg)

- Id: `phase:b-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:bcc-a2)

Names (3): _corpus: _corpus:phase:b-mg:bcc-a2  
_tdb: _tdb:MgB-01Liu-LB.tdb:BCC_A2, tdb:MgB-05Bal.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): BCC_A2, type code %B, sha256 `8309e62bcb5a44e3…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : MG : VA : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): BCC_A2, type code %B, sha256 `560f62e9d31af938…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase_

## MB2_C32 (B–Mg)

- Id: `phase:b-mg:c32-mb2`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaaabdj and oqmd-98302, space group 191
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MB2); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.6667, Mg 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1979.09 K, x(B) 0.66667–0.66667
- Literature: 27 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:c32-mb2)

Names (8): _corpus: _corpus:phase:b-mg:c32-mb2, corpus:phase:b-mg:mb2-c32  
_mp: _mp:mp-aaaaabdj  
_oqmd: _oqmd:oqmd-98302  
_paper: _paper:10.1016/j.jpcs.2004.06.063:MgB2, paper:10.1016/s0364-5916(01)00050-5:MgB2  
_tdb: _tdb:MgB-01Liu-LB.tdb:MB2_C32, tdb:MgB-05Bal.tdb:MB2_C32  


### TDB models of MB2_C32 (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): MB2_C32, type code %, sha256 `8309e62bcb5a44e3…`

~~~~text
52: PHASE MB2_C32 % 2 1 2 !
53: CONST MB2_C32 : MG : B : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): MB2_C32, type code %, sha256 `560f62e9d31af938…`

~~~~text
54: PHASE MB2_C32 % 2 1 2 !
55: CONST MB2_C32 : MG : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90021-5](https://doi.org/10.1016/0364-5916%2885%2990021-5) Bo Sundman, Bo Jansson, Jan-Olof Andersson, The Thermo-Calc databank system, Calphad 9, 153-190 (1985).  
_cited as the source of values for this phase_

## FCC_A1 (B–Mg)

- Id: `phase:b-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:fcc-a1)

Names (3): _corpus: _corpus:phase:b-mg:fcc-a1  
_tdb: _tdb:MgB-01Liu-LB.tdb:FCC_A1, tdb:MgB-05Bal.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): FCC_A1, type code %A, sha256 `8309e62bcb5a44e3…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MG : VA : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): FCC_A1, type code %A, sha256 `560f62e9d31af938…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase_

## GAS (B–Mg)

- Id: `phase:b-mg:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1367.63–4000 K, x(B) 0–0.52475
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:gas)

Names (4): _corpus: _corpus:phase:b-mg:gas  
_paper: _paper:10.1016/s0364-5916(01)00050-5:gas  
_tdb: _tdb:MgB-01Liu-LB.tdb:GAS, tdb:MgB-05Bal.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): GAS, type code %, sha256 `8309e62bcb5a44e3…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : B B2 MG MG2 : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): GAS, type code %, sha256 `560f62e9d31af938…`

~~~~text
72: PHASE GAS:G % 1 1 !
73: CONST GAS:G : B B2 MG MG2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase_

## HCP_A3 (B–Mg)

- Id: `phase:b-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1468 K, x(B) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:hcp-a3)

Names (4): _corpus: _corpus:phase:b-mg:hcp-a3  
_paper: _paper:10.1016/s0364-5916(01)00050-5:hcp  
_tdb: _tdb:MgB-01Liu-LB.tdb:HCP_A3, tdb:MgB-05Bal.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): HCP_A3, type code %A, sha256 `8309e62bcb5a44e3…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : MG% : VA : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): HCP_A3, type code %A, sha256 `560f62e9d31af938…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : MG% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase_

## LIQUID (B–Mg)

- Id: `phase:b-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 922.85–4000 K, x(B) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:liquid)

Names (4): _corpus: _corpus:phase:b-mg:liquid  
_paper: _paper:10.1016/s0364-5916(01)00050-5:liq  
_tdb: _tdb:MgB-01Liu-LB.tdb:LIQUID, tdb:MgB-05Bal.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): LIQUID, type code %, sha256 `8309e62bcb5a44e3…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : B MG : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): LIQUID, type code %, sha256 `560f62e9d31af938…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : B MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase_

## MGB20 (B–Mg)

- Id: `phase:b-mg:mgb20`; status `assigned`
- Structure: ScB28 · hR119 · R-3m (166); type `st:scb28-hr119`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.9524, Mg 0.0476
- Stability: stable in 1 of 1 calculated diagram(s): 300–2465.49 K, x(B) 0.95238–0.95238
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:mgb20)

Names (3): _corpus: _corpus:phase:b-mg:mgb20  
_paper: _paper:10.1016/j.jpcs.2004.06.063:MgB20  
_tdb: _tdb:MgB-05Bal.tdb:MGB20  


### TDB models of MGB20 (1): PHASE and CONSTITUENT statements as written

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): MGB20, type code %, sha256 `560f62e9d31af938…`

~~~~text
69: PHASE MGB20 % 2 1 20 !
70: CONST MGB20 : MG : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase; reports values for this phase_

## MGB4 (B–Mg)

- Id: `phase:b-mg:mgb4`; status `assigned`
- Structure: MgB4 · oP20 · Pnma (62); type `st:mgb4-op20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.8000, Mg 0.2000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2281.82 K, x(B) 0.8–0.8
- Literature: 27 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:mgb4)

Names (5): _corpus: _corpus:phase:b-mg:mgb4  
_paper: _paper:10.1016/j.jpcs.2004.06.063:MgB4, paper:10.1016/s0364-5916(01)00050-5:MgB4  
_tdb: _tdb:MgB-01Liu-LB.tdb:MGB4, tdb:MgB-05Bal.tdb:MGB4  


### TDB models of MGB4 (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): MGB4, type code %, sha256 `8309e62bcb5a44e3…`

~~~~text
57: PHASE MGB4 % 2 1 4 !
58: CONST MGB4 : MG : B : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): MGB4, type code %, sha256 `560f62e9d31af938…`

~~~~text
59: PHASE MGB4 % 2 1 4 !
60: CONST MGB4 : MG : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02057252](https://doi.org/10.1007/bf02057252) R. Pan, Manika Varma Nair, B. Wunderlich, On theC p toC v conversion of solid linear macromolecules II, Journal of Thermal Analysis 35, 955-966 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(85)90021-5](https://doi.org/10.1016/0364-5916%2885%2990021-5) Bo Sundman, Bo Jansson, Jan-Olof Andersson, The Thermo-Calc databank system, Calphad 9, 153-190 (1985).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1010188110516](https://doi.org/10.1023/a:1010188110516) M. Pyda, M. Bartkowiak, B. Wunderlich, Computation of Heat Capacities of Solids Using a General Tarasov Equation, Journal of Thermal Analysis and Calorimetry 52, 631-656 (1998).  
_cited as the source of values for this phase_

## MGB7 (B–Mg)

- Id: `phase:b-mg:mgb7`; status `assigned`
- Structure: MgB7 · oI64 · Imma (74); type `st:mgb7-oi64`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: B 0.8750, Mg 0.1250
- Stability: stable in 2 of 2 calculated diagram(s): 300–2424.01 K, x(B) 0.875–0.875
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-mg:mgb7)

Names (7): _corpus: _corpus:phase:b-mg:mgb7  
_mp: _mp:mp-aaacdrdz  
_oqmd: _oqmd:oqmd-23820  
_paper: _paper:10.1016/j.jpcs.2004.06.063:MgB7, paper:10.1016/s0364-5916(01)00050-5:MgB7  
_tdb: _tdb:MgB-01Liu-LB.tdb:MGB7, tdb:MgB-05Bal.tdb:MGB7  


### TDB models of MGB7 (2): PHASE and CONSTITUENT statements as written

[MgB-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-01Liu-LB.tdb): MGB7, type code %, sha256 `8309e62bcb5a44e3…`

~~~~text
62: PHASE MGB7 % 2 1 7 !
63: CONST MGB7 : MG : B : !
~~~~

[MgB-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgB-05Bal.tdb): MGB7, type code %, sha256 `560f62e9d31af938…`

~~~~text
64: PHASE MGB7 % 2 1 7 !
65: CONST MGB7 : MG : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jpcs.2004.06.063](https://doi.org/10.1016/j.jpcs.2004.06.063) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona et al., Thermodynamics of the intermediate phases in the Mg–B system, Journal of Physics and Chemistry of Solids 66, 292-297 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00050-5](https://doi.org/10.1016/S0364-5916%2801%2900050-5) Z.-K. Liu, Y. Zhong, D.G. Schlom, X.X. Xi, Q. Li, Calphad, 25, 299-303(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02057252](https://doi.org/10.1007/bf02057252) R. Pan, Manika Varma Nair, B. Wunderlich, On theC p toC v conversion of solid linear macromolecules II, Journal of Thermal Analysis 35, 955-966 (1989).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1010188110516](https://doi.org/10.1023/a:1010188110516) M. Pyda, M. Bartkowiak, B. Wunderlich, Computation of Heat Capacities of Solids Using a General Tarasov Equation, Journal of Thermal Analysis and Calorimetry 52, 631-656 (1998).  
_cited as the source of values for this phase_

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
