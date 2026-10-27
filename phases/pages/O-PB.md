# O–Pb phases

> O–Pb system: 13 phases (tier A 5, tier C 3, liquid 2, gas 2, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-PB.html · Markdown: https://data.orchid-project.org/phases/pages/O-PB.md

13 phases (tier A 5, tier C 3, liquid 2, gas 2, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-PB) · [full JSON](https://data.orchid-project.org/phases/systems/O-PB.json) · [O–Pb system page](https://data.orchid-project.org/systems/O-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Pb system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-pb-bcc-a2); _phase:o-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-o-pb-fcc-a1); _phase:o-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–515 K, x(O) 0–0 | 0 | 1 |
| [GAS](#phase-o-pb-gas); _phase:o-pb:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 930.04–2019.02 K, x(O) 1e-05–1 | 0 | 1 |
| [HCP_A3](#phase-o-pb-hcp-a3); _phase:o-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-o-pb-ion); _phase:o-pb:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1162.43–2019.02 K, x(O) 0–0.49856 | 0 | 1 |
| [LIQUID](#phase-o-pb-liquid); _phase:o-pb:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |
| [O2GAS](#phase-o-pb-o2gas); _phase:o-pb:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–315 K, x(O) 1–1 | 0 | 1 |
| [PB12O17](#phase-o-pb-pb12o17); _phase:o-pb:pb12o17_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–325 K, x(O) 0.58621–0.58621 | 13 | 1 |
| [PB12O19](#phase-o-pb-pb12o19); _phase:o-pb:pb12o19_ | (Pb12O19) · mP62 · Pc (7) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 18 | 1 |
| [PB3O4](#phase-o-pb-pb3o4); _phase:o-pb:pb3o4_ | Pb3O4-T · tP28 · P4_2/mbc (135) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–307 K, x(O) 0.57143–0.57143 | 0 | 1 |
| [PBO_B10](#phase-o-pb-pbo-b10); _phase:o-pb:pbo-b10_ | PbO-L · B10 · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–515 K, x(O) 0.5–0.5 | 0 | 1 |
| [PBO_M](#phase-o-pb-pbo-m); _phase:o-pb:pbo-m_ | PbO-M · oP8 · Pbcm (57) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 930.04–1152.54 K, x(O) 0.5–0.5 | 0 | 1 |
| [PBO2_C4](#phase-o-pb-pbo2-c4); _phase:o-pb:pbo2-c4_ | TiO2 · C4 · tP6 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–325 K, x(O) 0.66667–0.66667 | 10 | 1 |

## BCC_A2 (O–Pb)

- Id: `phase:o-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:bcc-a2)

Names (2): _corpus: _corpus:phase:o-pb:bcc-a2  
_tdb: _tdb:PbO-98Ris-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): BCC_A2, type code %B, sha256 `263b6f32a74f0f62…`

~~~~text
54: PHASE BCC_A2 %B 2 1 3 !
55: CONST BCC_A2 : PB : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## FCC_A1 (O–Pb)

- Id: `phase:o-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–515 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:fcc-a1)

Names (2): _corpus: _corpus:phase:o-pb:fcc-a1  
_tdb: _tdb:PbO-98Ris-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): FCC_A1, type code %A, sha256 `263b6f32a74f0f62…`

~~~~text
49: PHASE FCC_A1 %A 2 1 1 !
50: CONST FCC_A1 : PB% : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## GAS (O–Pb)

- Id: `phase:o-pb:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 930.04–2019.02 K, x(O) 1e-05–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:gas)

Names (2): _corpus: _corpus:phase:o-pb:gas  
_tdb: _tdb:PbO-98Ris-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): GAS, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
96: PHASE GAS:G % 1 1 !
97: CONST GAS:G : O O2% O3 PB PB2 PBO PB2O2 PB3O3 PB4O4 PB5O5 PB6O6 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## HCP_A3 (O–Pb)

- Id: `phase:o-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:hcp-a3)

Names (2): _corpus: _corpus:phase:o-pb:hcp-a3  
_tdb: _tdb:PbO-98Ris-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): HCP_A3, type code %A, sha256 `263b6f32a74f0f62…`

~~~~text
59: PHASE HCP_A3 %A 2 1 0.5 !
60: CONST HCP_A3 : PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## ION (O–Pb)

- Id: `phase:o-pb:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1162.43–2019.02 K, x(O) 0–0.49856
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:ion)

Names (2): _corpus: _corpus:phase:o-pb:ion  
_tdb: _tdb:PbO-98Ris-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): ION, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
41: PHASE ION:Y % 2 1 1 !
42: CONST ION:Y : PB+2 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## LIQUID (O–Pb)

- Id: `phase:o-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:liquid)

Names (2): _corpus: _corpus:phase:o-pb:liquid  
_tdb: _tdb:PbO-98Ris-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): LIQUID, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
44: PHASE LIQUID:L % 1 1 !
45: CONST LIQUID:L : PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## O2GAS (O–Pb)

- Id: `phase:o-pb:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–315 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:o2gas)

Names (2): _corpus: _corpus:phase:o-pb:o2gas  
_tdb: _tdb:PbO-98Ris-LB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): O2GAS, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
99: PHASE O2GAS % 1 1 !
100: CONST O2GAS : O2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## PB12O17 (O–Pb)

- Id: `phase:o-pb:pb12o17`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Pb12O17) · Pmc2_1 (26) — Hallstedt 2025 mmc2 row for PB12O17: Pb12O17
- Stability: stable in 1 of 1 calculated diagram(s): 300–325 K, x(O) 0.58621–0.58621
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:pb12o17)

Names (3): _corpus: _corpus:phase:o-pb:pb12o17  
_paper: _paper:10.1361/105497198770342238:Pb12O17  
_tdb: _tdb:PbO-98Ris-LB.tdb:PB12O17  


### TDB models of PB12O17 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): PB12O17, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
82: PHASE PB12O17:I % 3 7 5 17 !
83: CONST PB12O17:I : PB+2 : PB+4 : O-2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2424016](https://doi.org/10.1149/1.2424016) Earl M. Otto, Equilibrium Pressures of Oxygen over Oxides of Lead at Various Temperatures, J. Electrochem. Soc. 113, 525 (1966).  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1964.tb14404.x](https://doi.org/10.1111/j.1151-2916.1964.tb14404.x) WILLIAM B. WHITE, RUSTUM ROY, Phase Relations in the System Lead—Oxygen, Journal of the American Ceramic Society 47, 242-249 (1964).  
_cited as the source of values for this phase_

## PB12O19 (O–Pb)

- Id: `phase:o-pb:pb12o19`; status `assigned`
- Structure: (Pb12O19) · mP62 · Pc (7); type `st:pb12o19-mp62`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:pb12o19)

Names (3): _corpus: _corpus:phase:o-pb:pb12o19  
_paper: _paper:10.1361/105497198770342238:Pb12O19  
_tdb: _tdb:PbO-98Ris-LB.tdb:PB12O19  


### TDB models of PB12O19 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): PB12O19, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
87: PHASE PB12O19:I % 3 5 7 19 !
88: CONST PB12O19:I : PB+2 : PB+4 : O-2 : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2424016](https://doi.org/10.1149/1.2424016) Earl M. Otto, Equilibrium Pressures of Oxygen over Oxides of Lead at Various Temperatures, J. Electrochem. Soc. 113, 525 (1966).  
_cited as the source of values for this phase_
- [doi:10.1002/bbpc.19120181610](https://doi.org/10.1002/bbpc.19120181610) W. Hempel and C. Schubert,"On the Dissociation of Some Oxides, Carbonates, and Sulfides," Z, Elektrochem., 18, 729 (1912) in German.  
_cited as the source of values for this phase_
- [doi:10.1002/bbpc.19370430108](https://doi.org/10.1002/bbpc.19370430108) J. Krustinsons, "On the Termal Decomposition of Lead(4)-Oxides," Z Elektrochem., 40, 246-248 (1934); 43, 65-66 (1937) in German.  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1964.tb14404.x](https://doi.org/10.1111/j.1151-2916.1964.tb14404.x) WILLIAM B. WHITE, RUSTUM ROY, Phase Relations in the System Lead—Oxygen, Journal of the American Ceramic Society 47, 242-249 (1964).  
_cited as the source of values for this phase_

## PB3O4 (O–Pb)

- Id: `phase:o-pb:pb3o4`; status `assigned`
- Structure: Pb3O4-T · tP28 · P4_2/mbc (135); type `st:pb3o4-t-tp28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–307 K, x(O) 0.57143–0.57143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:pb3o4)

Names (2): _corpus: _corpus:phase:o-pb:pb3o4  
_tdb: _tdb:PbO-98Ris-LB.tdb:PB3O4  


### TDB models of PB3O4 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): PB3O4, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
77: PHASE PB3O4:I % 3 2 1 4 !
78: CONST PB3O4:I : PB+2 : PB+4 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## PBO_B10 (O–Pb)

- Id: `phase:o-pb:pbo-b10`; status `assigned`
- Structure: PbO-L · B10 · tP4 · P4/nmm (129); type `st:b10-pbo-l-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–515 K, x(O) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:pbo-b10)

Names (2): _corpus: _corpus:phase:o-pb:pbo-b10  
_tdb: _tdb:PbO-98Ris-LB.tdb:PBO_B10  


### TDB models of PBO_B10 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): PBO_B10, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
65: PHASE PBO_B10:I % 2 1 1 !
66: CONST PBO_B10:I : PB+2 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## PBO_M (O–Pb)

- Id: `phase:o-pb:pbo-m`; status `assigned`
- Structure: PbO-M · oP8 · Pbcm (57); type `st:pbo-m-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:M, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 930.04–1152.54 K, x(O) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:pbo-m)

Names (2): _corpus: _corpus:phase:o-pb:pbo-m  
_tdb: _tdb:PbO-98Ris-LB.tdb:PBO_M  


### TDB models of PBO_M (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): PBO_M, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
71: PHASE PBO_M:I % 2 1 1 !
72: CONST PBO_M:I : PB+2 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase_

## PBO2_C4 (O–Pb)

- Id: `phase:o-pb:pbo2-c4`; status `assigned`
- Structure: TiO2 · C4 · tP6 · P4_2/mnm (136); type `st:c4-tio2-tp6`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–325 K, x(O) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pb:pbo2-c4)

Names (3): _corpus: _corpus:phase:o-pb:pbo2-c4  
_paper: _paper:10.1361/105497198770342238:PbO2-I.  
_tdb: _tdb:PbO-98Ris-LB.tdb:PBO2_C4  


### TDB models of PBO2_C4 (1): PHASE and CONSTITUENT statements as written

[PbO-98Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbO-98Ris-LB.tdb): PBO2_C4, type code %, sha256 `263b6f32a74f0f62…`

~~~~text
93: PHASE PBO2_C4:I % 2 1 2 !
94: CONST PBO2_C4:I : PB+4 : O-2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497198770342238](https://doi.org/10.1361/105497198770342238) D. Risold, J. -I. Nagata, R. O. Suzuki, Thermodynamic description of the Pb-O system, JPE 19, 213-233 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0021-9614(70)90039-x](https://doi.org/10.1016/0021-9614%2870%2990039-x) L. Espada, G. Pilcher, H.A. Skinner, Hot-zone reaction calorimetry II. The enthalpies of formation of lead oxides, The Journal of Chemical Thermodynamics 2, 647-653 (1970).  
_cited as the source of values for this phase_
- [doi:10.1021/j100848a030](https://doi.org/10.1021/j100848a030) J. A. Duisman, William F. Giauque, Thermodynamics of the lead storage cell. The heat capacity and entropy of lead dioxide from 15 to 318.degree.K, J. Phys. Chem. 72, 562-573 (1968).  
_cited as the source of values for this phase_

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
