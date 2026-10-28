# Sb–Tb phases

> Sb–Tb system: 11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SB-TB.html · Markdown: https://data.orchid-project.org/phases/pages/SB-TB.md

11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SB-TB) · [full JSON](https://data.orchid-project.org/phases/systems/SB-TB.json) · [Sb–Tb system page](https://data.orchid-project.org/systems/SB-TB.html) · [Markdown](https://data.orchid-project.org/phases/pages/SB-TB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sb–Tb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-sb-tb-a7-rhombohedral); _phase:sb-tb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Tb) 0–0 | 2 | 1 |
| [BCC_A2](#phase-sb-tb-bcc-a2); _phase:sb-tb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1538.23–1631.99 K, x(Tb) 0.99049–1 | 2 | 1 |
| [FCC_A1](#phase-sb-tb-fcc-a1); _phase:sb-tb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-sb-tb-hcp-a3); _phase:sb-tb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1627 K, x(Tb) 0.98309–1 | 4 | 1 |
| [LIQUID](#phase-sb-tb-liquid); _phase:sb-tb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 896.54–2500 K, x(Tb) 0–1 | 13 | 1 |
| [SB2TB](#phase-sb-tb-sb2tb); _phase:sb-tb:sb2tb_ | Sb2Sm · oC24 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1013.13 K, x(Tb) 0.33333–0.33333 | 4 | 1 |
| [SB3TB4_BETA](#phase-sb-tb-sb3tb4-beta); _phase:sb-tb:sb3tb4-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1873–2043.2 K, x(Tb) 0.57143–0.57143 | 4 | 1 |
| [SB3TB4_D73](#phase-sb-tb-sb3tb4-d73); _phase:sb-tb:sb3tb4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1873 K, x(Tb) 0.57143–0.57143 | 0 | 1 |
| [SB3TB5_D88](#phase-sb-tb-sb3tb5-d88); _phase:sb-tb:sb3tb5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1923.05 K, x(Tb) 0.625–0.625 | 4 | 1 |
| [SBTB_B1](#phase-sb-tb-sbtb-b1); _phase:sb-tb:sbtb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2133 K, x(Tb) 0.5–0.5 | 4 | 1 |
| [SBTB_BETA](#phase-sb-tb-sbtb-beta); _phase:sb-tb:sbtb-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2133–2433 K, x(Tb) 0.5–0.5 | 0 | 1 |

## RHOMBOHEDRAL_A7 (Sb–Tb)

- Id: `phase:sb-tb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Tb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:sb-tb:a7-rhombohedral  
_paper: _paper:10.1016/j.calphad.2012.01.002:(Sb)  
_tdb: _tdb:SbTb-12Gao.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `59da5731b61eb820…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Sb–Tb)

- Id: `phase:sb-tb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1538.23–1631.99 K, x(Tb) 0.99049–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:bcc-a2)

Names (3): _corpus: _corpus:phase:sb-tb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2012.01.002:(β-Tb)  
_tdb: _tdb:SbTb-12Gao.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): BCC_A2, type code %B, sha256 `59da5731b61eb820…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : SB TB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Sb–Tb)

- Id: `phase:sb-tb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:fcc-a1)

Names (2): _corpus: _corpus:phase:sb-tb:fcc-a1  
_tdb: _tdb:SbTb-12Gao.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): FCC_A1, type code %A, sha256 `59da5731b61eb820…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase_

## HCP_A3 (Sb–Tb)

- Id: `phase:sb-tb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1627 K, x(Tb) 0.98309–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:hcp-a3)

Names (3): _corpus: _corpus:phase:sb-tb:hcp-a3  
_paper: _paper:10.1016/j.calphad.2012.01.002:(α-Tb)  
_tdb: _tdb:SbTb-12Gao.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): HCP_A3, type code %A, sha256 `59da5731b61eb820…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SB TB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Sb–Tb)

- Id: `phase:sb-tb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 896.54–2500 K, x(Tb) 0–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:liquid)

Names (4): _corpus: _corpus:phase:sb-tb:liquid  
_paper: _paper:10.1016/j.calphad.2012.01.002:L, paper:10.1016/j.calphad.2012.01.002:liquid  
_tdb: _tdb:SbTb-12Gao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): LIQUID, type code %, sha256 `59da5731b61eb820…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SB TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## SB2TB (Sb–Tb)

- Id: `phase:sb-tb:sb2tb`; status `assigned`
- Structure: Sb2Sm · oC24 · Cmce (64); type `st:sb2sm-oc24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sb 0.6667, Tb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1013.13 K, x(Tb) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:sb2tb)

Names (3): _corpus: _corpus:phase:sb-tb:sb2tb  
_paper: _paper:10.1016/j.calphad.2012.01.002:Sb2Tb  
_tdb: _tdb:SbTb-12Gao.tdb:SB2TB  


### TDB models of SB2TB (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): SB2TB, type code %, sha256 `59da5731b61eb820…`

~~~~text
45: PHASE SB2TB % 2 2 1 !
46: CONST SB2TB : SB : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## SB3TB4_BETA (Sb–Tb)

- Id: `phase:sb-tb:sb3tb4-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (sgte_mmc2): (beta-Sb3Tb4) — Hallstedt 2025 mmc2 row for SB3TB4_BETA: Sb3Tb4-beta
- Stoichiometry: Sb 0.4286, Tb 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 1873–2043.2 K, x(Tb) 0.57143–0.57143
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:sb3tb4-beta)

Names (3): _corpus: _corpus:phase:sb-tb:sb3tb4-beta  
_paper: _paper:10.1016/j.calphad.2012.01.002:(β-Sb3Tb4)  
_tdb: _tdb:SbTb-12Gao.tdb:SB3TB4_BETA  


### TDB models of SB3TB4_BETA (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): SB3TB4_BETA, type code %, sha256 `59da5731b61eb820…`

~~~~text
65: PHASE SB3TB4_BETA % 2 3 4 !
66: CONST SB3TB4_BETA : SB : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## SB3TB4_D73 (Sb–Tb)

- Id: `phase:sb-tb:sb3tb4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.4286, Tb 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1873 K, x(Tb) 0.57143–0.57143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:sb3tb4-d73)

Names (2): _corpus: _corpus:phase:sb-tb:sb3tb4-d73  
_tdb: _tdb:SbTb-12Gao.tdb:SB3TB4_D73  


### TDB models of SB3TB4_D73 (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): SB3TB4_D73, type code %, sha256 `59da5731b61eb820…`

~~~~text
60: PHASE SB3TB4_D73 % 2 3 4 !
61: CONST SB3TB4_D73 : SB : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase_

## SB3TB5_D88 (Sb–Tb)

- Id: `phase:sb-tb:sb3tb5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.3750, Tb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1923.05 K, x(Tb) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:sb3tb5-d88)

Names (3): _corpus: _corpus:phase:sb-tb:sb3tb5-d88  
_paper: _paper:10.1016/j.calphad.2012.01.002:Sb3Tb5  
_tdb: _tdb:SbTb-12Gao.tdb:SB3TB5_D88  


### TDB models of SB3TB5_D88 (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): SB3TB5_D88, type code %, sha256 `59da5731b61eb820…`

~~~~text
70: PHASE SB3TB5_D88 % 2 3 5 !
71: CONST SB3TB5_D88 : SB : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## SBTB_B1 (Sb–Tb)

- Id: `phase:sb-tb:sbtb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.5000, Tb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2133 K, x(Tb) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:sbtb-b1)

Names (3): _corpus: _corpus:phase:sb-tb:sbtb-b1  
_paper: _paper:10.1016/j.calphad.2012.01.002:(α-SbTb)  
_tdb: _tdb:SbTb-12Gao.tdb:SBTB_B1  


### TDB models of SBTB_B1 (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): SBTB_B1, type code %, sha256 `59da5731b61eb820…`

~~~~text
50: PHASE SBTB_B1 % 2 1 1 !
51: CONST SBTB_B1 : SB : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## SBTB_BETA (Sb–Tb)

- Id: `phase:sb-tb:sbtb-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Fm-3m (225) — on-hull MP TbSb at x(TB)=0.5000
- Candidate (dft_oqmd): P-3m1 (164) — on-hull OQMD Sb1 Tb1 at x(TB)=0.5000
- Candidate (sgte_mmc2): (beta-SbTb) — Hallstedt 2025 mmc2 row for SBTB_BETA: SbTb-beta
- Stoichiometry: Sb 0.5000, Tb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 2133–2433 K, x(Tb) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tb:sbtb-beta)

Names (2): _corpus: _corpus:phase:sb-tb:sbtb-beta  
_tdb: _tdb:SbTb-12Gao.tdb:SBTB_BETA  


### TDB models of SBTB_BETA (1): PHASE and CONSTITUENT statements as written

[SbTb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTb-12Gao.tdb): SBTB_BETA, type code %, sha256 `59da5731b61eb820…`

~~~~text
55: PHASE SBTB_BETA % 2 1 1 !
56: CONST SBTB_BETA : SB : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
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
