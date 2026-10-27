# Cs–O phases

> Cs–O system: 15 phases (tier A 4, tier B 1, tier C 3, liquid 2, gas 2, needs_review 3); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CS-O.html · Markdown: https://data.orchid-project.org/phases/pages/CS-O.md

15 phases (tier A 4, tier B 1, tier C 3, liquid 2, gas 2, needs_review 3); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CS-O) · [full JSON](https://data.orchid-project.org/phases/systems/CS-O.json) · [Cs–O system page](https://data.orchid-project.org/systems/CS-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/CS-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cs–O system (15)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cs-o-bcc-a2); _phase:cs-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 299.47–301.59 K, x(O) 0–0 | 0 | 1 |
| [CS2O_C19](#phase-cs-o-cs2o-c19); _phase:cs-o:cs2o-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–375 K, x(O) 0.33333–0.33333 | 0 | 1 |
| [CS2O2](#phase-cs-o-cs2o2); _phase:cs-o:cs2o2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–335 K, x(O) 0.5–0.5 | 18 | 1 |
| [CS3O](#phase-cs-o-cs3o); _phase:cs-o:cs3o_ | Cs3O · hP8 · P6_3/mcm (193) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–430.17 K, x(O) 0.25–0.25 | 16 | 1 |
| [CS4O](#phase-cs-o-cs4o); _phase:cs-o:cs4o_ | Cs4O · oP60 · Pna2_1 (33) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–325.17 K, x(O) 0.2–0.2 | 7 | 1 |
| [CS7O](#phase-cs-o-cs7o); _phase:cs-o:cs7o_ | Cs7O · hP24 · P-6m2 (187) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 14 | 1 |
| [CS7O2](#phase-cs-o-cs7o2); _phase:cs-o:cs7o2_ | Cs11O3 · mP56 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 7 | 1 |
| [CSO2_C11A](#phase-cs-o-cso2-c11a); _phase:cs-o:cso2-c11a_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CSO3](#phase-cs-o-cso3); _phase:cs-o:cso3_ |  | needs_review | not stable in 1 calculated diagram(s) | 23 | 1 |
| [FCC_A1](#phase-cs-o-fcc-a1); _phase:cs-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-cs-o-gas); _phase:cs-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 557.05–1433.53 K, x(O) 0–1 | 0 | 1 |
| [HCP_A3](#phase-cs-o-hcp-a3); _phase:cs-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-cs-o-ion); _phase:cs-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 299.47–1433.53 K, x(O) 0–0.72819 | 0 | 1 |
| [LIQUID](#phase-cs-o-liquid); _phase:cs-o:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 2 | 1 |
| [O2GAS](#phase-cs-o-o2gas); _phase:cs-o:o2gas_ | gas | gas | not stable in 1 calculated diagram(s) | 0 | 1 |

## BCC_A2 (Cs–O)

- Id: `phase:cs-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cs 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 299.47–301.59 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:bcc-a2)

Names (2): _corpus: _corpus:phase:cs-o:bcc-a2  
_tdb: _tdb:CsO-15Gue.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): BCC_A2, type code %B, sha256 `5219d7e34c2f9d74…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : CS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase_

## CS2O_C19 (Cs–O)

- Id: `phase:cs-o:cs2o-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–375 K, x(O) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cs2o-c19)

Names (2): _corpus: _corpus:phase:cs-o:cs2o-c19  
_tdb: _tdb:CsO-15Gue.tdb:CS2O_C19  


### TDB models of CS2O_C19 (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CS2O_C19, type code %A, sha256 `5219d7e34c2f9d74…`

~~~~text
78: PHASE CS2O_C19:I %A 2 2 1 !
79: CONST CS2O_C19:I : CS+1 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase_

## CS2O2 (Cs–O)

- Id: `phase:cs-o:cs2o2`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): Immm (71) — on-hull MP Cs2O2 at x(O)=0.5000
- Candidate (dft_oqmd): Immm (71) — on-hull OQMD Cs1 O1 at x(O)=0.5000
- Candidate (sgte_mmc2): Rb2O2 · oI8 · Immm (71) — Hallstedt 2025 mmc2 row for CS2O2: Cs2O2
- Candidate (tdb_comment): Rb2O2 · oI8 · Immm — CsO-15Gue.tdb: 'Prototype Rb2O2 (oI8, Immm)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–335 K, x(O) 0.5–0.5
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cs2o2)

Names (3): _corpus: _corpus:phase:cs-o:cs2o2  
_paper: _paper:10.1016/j.calphad.2015.02.002:Cs2O2  
_tdb: _tdb:CsO-15Gue.tdb:CS2O2  


### TDB models of CS2O2 (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CS2O2, type code %A, sha256 `5219d7e34c2f9d74…`

~~~~text
83: PHASE CS2O2:I %A 2 2 1 !
84: CONST CS2O2:I : CS+1 : O2-2 : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(79)90163-6](https://doi.org/10.1016/0022-3115%2879%2990163-6) C.F Knights, B.A Phillips, The Cs-O system;Phase diagram and oxygen potentials, Journal of Nuclear Materials 84, 196-206 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1063/1.555706](https://doi.org/10.1063/1.555706) R. H. Lamoreaux, D. L. Hildenbrand, High Temperature Vaporization Behavior of Oxides. I. Alkali Metal Binary Oxides, Journal of Physical and Chemical Reference Data 13, 151-173 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/j.ces.2010.01.024](https://doi.org/10.1016/j.ces.2010.01.024) Anubhav Jain, S.-A. Seyed-Reihani, Christopher C. Fischer, David J. Couling, Gerbrand Ceder, William H. Green, Ab initio screening of metal sorbents for elemental mercury capture in syngas streams, Chemical Engineering Science 65, 3025-3033 (2010).  
_cited as the source of values for this phase_

## CS3O (Cs–O)

- Id: `phase:cs-o:cs3o`; status `assigned`
- Structure: Cs3O · hP8 · P6_3/mcm (193); type `st:cs3o-hp8`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cs 0.7500, O 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–430.17 K, x(O) 0.25–0.25
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cs3o)

Names (5): _corpus: _corpus:phase:cs-o:cs3o  
_mp: _mp:mp-aaabdavm  
_oqmd: _oqmd:oqmd-2013713  
_paper: _paper:10.1016/j.calphad.2015.02.002:Cs3O  
_tdb: _tdb:CsO-15Gue.tdb:CS3O  


### TDB models of CS3O (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CS3O, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
73: PHASE CS3O % 2 3 1 !
74: CONST CS3O : CS : O : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(79)90163-6](https://doi.org/10.1016/0022-3115%2879%2990163-6) C.F Knights, B.A Phillips, The Cs-O system;Phase diagram and oxygen potentials, Journal of Nuclear Materials 84, 196-206 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/j.ces.2010.01.024](https://doi.org/10.1016/j.ces.2010.01.024) Anubhav Jain, S.-A. Seyed-Reihani, Christopher C. Fischer, David J. Couling, Gerbrand Ceder, William H. Green, Ab initio screening of metal sorbents for elemental mercury capture in syngas streams, Chemical Engineering Science 65, 3025-3033 (2010).  
_cited as the source of values for this phase_

## CS4O (Cs–O)

- Id: `phase:cs-o:cs4o`; status `assigned`
- Structure: Cs4O · oP60 · Pna2_1 (33); type `st:cs4o-op60`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.8000, O 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–325.17 K, x(O) 0.2–0.2
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cs4o)

Names (3): _corpus: _corpus:phase:cs-o:cs4o  
_paper: _paper:10.1016/j.calphad.2015.02.002:Cs4O  
_tdb: _tdb:CsO-15Gue.tdb:CS4O  


### TDB models of CS4O (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CS4O, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
63: PHASE CS4O % 2 4 1 !
64: CONST CS4O : CS : O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(79)90163-6](https://doi.org/10.1016/0022-3115%2879%2990163-6) C.F Knights, B.A Phillips, The Cs-O system;Phase diagram and oxygen potentials, Journal of Nuclear Materials 84, 196-206 (1979).  
_cited as the source of values for this phase_

## CS7O (Cs–O)

- Id: `phase:cs-o:cs7o`; status `assigned`
- Structure: Cs7O · hP24 · P-6m2 (187); type `st:cs7o-hp24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.8750, O 0.1250
- Stability: not stable in 1 calculated diagram(s)
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cs7o)

Names (3): _corpus: _corpus:phase:cs-o:cs7o  
_paper: _paper:10.1016/j.calphad.2015.02.002:Cs7O  
_tdb: _tdb:CsO-15Gue.tdb:CS7O  


### TDB models of CS7O (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CS7O, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
58: PHASE CS7O % 2 7 1 !
59: CONST CS7O : CS : O : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19472550110](https://doi.org/10.1002/zaac.19472550110) G. Brauer, Untersuchungen über das System Cäsium‐Sauerstoff, Z. Anorg. Chem. 255, 101-124 (1947).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(79)90163-6](https://doi.org/10.1016/0022-3115%2879%2990163-6) C.F Knights, B.A Phillips, The Cs-O system;Phase diagram and oxygen potentials, Journal of Nuclear Materials 84, 196-206 (1979).  
_cited as the source of values for this phase_

## CS7O2 (Cs–O)

- Id: `phase:cs-o:cs7o2`; status `assigned`
- Structure: Cs11O3 · mP56 · P2_1/c (14); type `st:cs11o3-mp56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.7778, O 0.2222
- Stability: not stable in 1 calculated diagram(s)
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cs7o2)

Names (3): _corpus: _corpus:phase:cs-o:cs7o2  
_paper: _paper:10.1016/j.calphad.2015.02.002:Cs7O2  
_tdb: _tdb:CsO-15Gue.tdb:CS7O2  


### TDB models of CS7O2 (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CS7O2, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
68: PHASE CS7O2 % 2 7 2 !
69: CONST CS7O2 : CS : O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(79)90163-6](https://doi.org/10.1016/0022-3115%2879%2990163-6) C.F Knights, B.A Phillips, The Cs-O system;Phase diagram and oxygen potentials, Journal of Nuclear Materials 84, 196-206 (1979).  
_cited as the source of values for this phase_

## CSO2_C11A (Cs–O)

- Id: `phase:cs-o:cso2-c11a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_C11_a; site_ratios_contradict_C11_a:CsO-15Gue.tdb
- Candidate (name_token): CaC2 · C11_a · tI6 · I4/mmm (139) — Strukturbericht/word 'C11A' in the TDB name
- Candidate (sgte_mmc2): CaC2 · C11_a · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for CSO2_C11A: CsO2
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — CsO-15Gue.tdb: 'Prototype CaC2 (tI6, I4/mmm)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cso2-c11a)

Names (2): _corpus: _corpus:phase:cs-o:cso2-c11a  
_tdb: _tdb:CsO-15Gue.tdb:CSO2_C11A  


### TDB models of CSO2_C11A (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CSO2_C11A, type code %A, sha256 `5219d7e34c2f9d74…`

~~~~text
89: PHASE CSO2_C11A:I %A 2 1 1 !
90: CONST CSO2_C11A:I : CS+1 : O2-1 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase_

## CSO3 (Cs–O)

- Id: `phase:cs-o:cso3`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): RbO3 · mP16 · P2_1/c (14) — Hallstedt 2025 mmc2 row for CSO3: CsO3
- Candidate (tdb_comment): RbO3 · mP16 · P2_1/c — CsO-15Gue.tdb: 'Prototype RbO3 (mP16, P2_1/c)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 23 values (23 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:cso3)

Names (3): _corpus: _corpus:phase:cs-o:cso3  
_paper: _paper:10.1016/j.calphad.2015.02.002:CsO3  
_tdb: _tdb:CsO-15Gue.tdb:CSO3  


### TDB models of CSO3 (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): CSO3, type code %A, sha256 `5219d7e34c2f9d74…`

~~~~text
94: PHASE CSO3:I %A 2 1 1 !
95: CONST CSO3:I : CS+1 : O3-1 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(79)90163-6](https://doi.org/10.1016/0022-3115%2879%2990163-6) C.F Knights, B.A Phillips, The Cs-O system;Phase diagram and oxygen potentials, Journal of Nuclear Materials 84, 196-206 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/j.ces.2010.01.024](https://doi.org/10.1016/j.ces.2010.01.024) Anubhav Jain, S.-A. Seyed-Reihani, Christopher C. Fischer, David J. Couling, Gerbrand Ceder, William H. Green, Ab initio screening of metal sorbents for elemental mercury capture in syngas streams, Chemical Engineering Science 65, 3025-3033 (2010).  
_cited as the source of values for this phase_

## FCC_A1 (Cs–O)

- Id: `phase:cs-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cs 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:fcc-a1)

Names (2): _corpus: _corpus:phase:cs-o:fcc-a1  
_tdb: _tdb:CsO-15Gue.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): FCC_A1, type code %A, sha256 `5219d7e34c2f9d74…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : CS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase_

## GAS (Cs–O)

- Id: `phase:cs-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 557.05–1433.53 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:gas)

Names (2): _corpus: _corpus:phase:cs-o:gas  
_tdb: _tdb:CsO-15Gue.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): GAS, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
100: PHASE GAS:G % 1 1 !
101: CONST GAS:G : CS CS2 CS2O CSO CS2O2 O O2 O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase_

## HCP_A3 (Cs–O)

- Id: `phase:cs-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cs 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:hcp-a3)

Names (2): _corpus: _corpus:phase:cs-o:hcp-a3  
_tdb: _tdb:CsO-15Gue.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): HCP_A3, type code %A, sha256 `5219d7e34c2f9d74…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : CS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase_

## ION (Cs–O)

- Id: `phase:cs-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 299.47–1433.53 K, x(O) 0–0.72819
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:ion)

Names (2): _corpus: _corpus:phase:cs-o:ion  
_tdb: _tdb:CsO-15Gue.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): ION, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
38: PHASE ION:Y % 2 1 1 !
39: CONST ION:Y : CS+1 : O-2 VA CSO2 O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase_

## LIQUID (Cs–O)

- Id: `phase:cs-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Cs 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:liquid)

Names (3): _corpus: _corpus:phase:cs-o:liquid  
_paper: _paper:10.1016/j.calphad.2015.02.002:liquid  
_tdb: _tdb:CsO-15Gue.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): LIQUID, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : CS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(79)90163-6](https://doi.org/10.1016/0022-3115%2879%2990163-6) C.F Knights, B.A Phillips, The Cs-O system;Phase diagram and oxygen potentials, Journal of Nuclear Materials 84, 196-206 (1979).  
_cited as the source of values for this phase_

## O2GAS (Cs–O)

- Id: `phase:cs-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-o:o2gas)

Names (2): _corpus: _corpus:phase:cs-o:o2gas  
_tdb: _tdb:CsO-15Gue.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[CsO-15Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb): O2GAS, type code %, sha256 `5219d7e34c2f9d74…`

~~~~text
97: PHASE O2GAS % 1 1 !
98: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015).  
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
