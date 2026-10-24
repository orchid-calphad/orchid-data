# Na–O phases

> Na–O system: 12 phases (tier A 5, liquid 1, gas 2, needs_review 4); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NA-O.html · Markdown: https://data.orchid-project.org/phases/pages/NA-O.md

12 phases (tier A 5, liquid 1, gas 2, needs_review 4); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NA-O) · [full JSON](https://data.orchid-project.org/phases/systems/NA-O.json) · [Na–O system page](https://data.orchid-project.org/systems/NA-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/NA-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Na–O system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-na-o-bcc-a2); _phase:na-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0–0 | 4 | 1 |
| [FCC_A1](#phase-na-o-fcc-a1); _phase:na-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-na-o-gas); _phase:na-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1006.07–2111.07 K, x(O) 0.39956–1 | 0 | 1 |
| [HCP_A3](#phase-na-o-hcp-a3); _phase:na-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-na-o-ion); _phase:na-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1006.07–2111.07 K, x(O) 0.3426–0.49063 | 0 | 1 |
| [NA2O_C1](#phase-na-o-na2o-c1); _phase:na-o:na2o-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0.33333–0.33333 | 8 | 1 |
| [NA2O_II](#phase-na-o-na2o-ii); _phase:na-o:na2o-ii_ |  | needs_review | not stable in 1 calculated diagram(s) | 4 | 1 |
| [NA2O_III](#phase-na-o-na2o-iii); _phase:na-o:na2o-iii_ |  | needs_review | not stable in 1 calculated diagram(s) | 6 | 1 |
| [NA2O2_I](#phase-na-o-na2o2-i); _phase:na-o:na2o2-i_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–422.5 K, x(O) 0.5–0.5 | 4 | 1 |
| [NA2O2_II](#phase-na-o-na2o2-ii); _phase:na-o:na2o2-ii_ |  | needs_review | not stable in 1 calculated diagram(s) | 6 | 1 |
| [NAO2_B1](#phase-na-o-nao2-b1); _phase:na-o:nao2-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [O2GAS](#phase-na-o-o2gas); _phase:na-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–422.5 K, x(O) 1–1 | 0 | 1 |

## BCC_A2 (Na–O)

- Id: `phase:na-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0–0
- Literature: 4 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:bcc-a2)

Names (3): _corpus: _corpus:phase:na-o:bcc-a2  
_paper: _paper:10.1016/j.jct.2017.04.003:β-Na  
_tdb: _tdb:NaO-17Smi.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): BCC_A2, type code %B, sha256 `4ebf441b547a4b28…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : NA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874915](https://doi.org/10.1007/bf02874915) H. A. Wriedt, The Na−O (Sodium-Oxygen) System, Bulletin of Alloy Phase Diagrams 8, 234-246 (1987).  
_cited as the source of values for this phase_

## FCC_A1 (Na–O)

- Id: `phase:na-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:fcc-a1)

Names (2): _corpus: _corpus:phase:na-o:fcc-a1  
_tdb: _tdb:NaO-17Smi.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): FCC_A1, type code %A, sha256 `4ebf441b547a4b28…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase_

## GAS (Na–O)

- Id: `phase:na-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1006.07–2111.07 K, x(O) 0.39956–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:gas)

Names (2): _corpus: _corpus:phase:na-o:gas  
_tdb: _tdb:NaO-17Smi.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): GAS, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
88: PHASE GAS:G % 1 1 !
89: CONST GAS:G : NA NA2 NA2O NA2O2 O O2 O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase_

## HCP_A3 (Na–O)

- Id: `phase:na-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:hcp-a3)

Names (2): _corpus: _corpus:phase:na-o:hcp-a3  
_tdb: _tdb:NaO-17Smi.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): HCP_A3, type code %A, sha256 `4ebf441b547a4b28…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase_

## ION (Na–O)

- Id: `phase:na-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1006.07–2111.07 K, x(O) 0.3426–0.49063
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:ion)

Names (2): _corpus: _corpus:phase:na-o:ion  
_tdb: _tdb:NaO-17Smi.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): ION, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : NA+1 : O-2 VA NA2O2 O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase_

## NA2O_C1 (Na–O)

- Id: `phase:na-o:na2o-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0.33333–0.33333
- Literature: 8 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:na2o-c1)

Names (5): _corpus: _corpus:phase:na-o:na2o-c1  
_paper: _paper:10.1016/j.jct.2017.04.003:Na2O-I, paper:10.1016/j.jct.2017.04.003:Na2O-I(cr), paper:10.1016/j.jct.2017.04.003:Na2OI  
_tdb: _tdb:NaO-17Smi.tdb:NA2O_C1  


### TDB models of NA2O_C1 (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): NA2O_C1, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
57: PHASE NA2O_C1 % 2 2 1 !
58: CONST NA2O_C1 : NA+1 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874915](https://doi.org/10.1007/bf02874915) H. A. Wriedt, The Na−O (Sodium-Oxygen) System, Bulletin of Alloy Phase Diagrams 8, 234-246 (1987).  
_cited as the source of values for this phase_

## NA2O_II (Na–O)

- Id: `phase:na-o:na2o-ii`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:II; no_structure_token
- Candidate (sgte_mmc2): (Na2O-II) — Hallstedt 2025 mmc2 row for NA2O_II: Na2O-II
- Stability: not stable in 1 calculated diagram(s)
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:na2o-ii)

Names (3): _corpus: _corpus:phase:na-o:na2o-ii  
_paper: _paper:10.1016/j.jct.2017.04.003:Na2O-II  
_tdb: _tdb:NaO-17Smi.tdb:NA2O_II  


### TDB models of NA2O_II (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): NA2O_II, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
62: PHASE NA2O_II % 2 2 1 !
63: CONST NA2O_II : NA+1 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase; reports values for this phase_

## NA2O_III (Na–O)

- Id: `phase:na-o:na2o-iii`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:III; no_structure_token
- Candidate (sgte_mmc2): (Na2O-III) — Hallstedt 2025 mmc2 row for NA2O_III: Na2O-III
- Stability: not stable in 1 calculated diagram(s)
- Literature: 6 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:na2o-iii)

Names (3): _corpus: _corpus:phase:na-o:na2o-iii  
_paper: _paper:10.1016/j.jct.2017.04.003:Na2O-III  
_tdb: _tdb:NaO-17Smi.tdb:NA2O_III  


### TDB models of NA2O_III (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): NA2O_III, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
67: PHASE NA2O_III % 2 2 1 !
68: CONST NA2O_III : NA+1 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874915](https://doi.org/10.1007/bf02874915) H. A. Wriedt, The Na−O (Sodium-Oxygen) System, Bulletin of Alloy Phase Diagrams 8, 234-246 (1987).  
_cited as the source of values for this phase_

## NA2O2_I (Na–O)

- Id: `phase:na-o:na2o2-i`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:I; no_structure_token
- Candidate (dft_mp): P-62m (189) — on-hull MP Na2O2 at x(O)=0.5000
- Candidate (dft_oqmd): P-62m (189) — on-hull OQMD Na1 O1 at x(O)=0.5000
- Candidate (sgte_mmc2): Na2O2 · hP12 · P-62m (189) — Hallstedt 2025 mmc2 row for NA2O2_I: Na2O2-I
- Candidate (tdb_comment): Na2O2 · hP12 · P-62m — NaO-17Smi.tdb: 'Prototype Na2O2 (hP12, P-62m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–422.5 K, x(O) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:na2o2-i)

Names (4): _corpus: _corpus:phase:na-o:na2o2-i  
_paper: _paper:10.1016/j.jct.2017.04.003:Na2O2-I, paper:10.1016/j.jct.2017.04.003:Na2O2-I(cr)  
_tdb: _tdb:NaO-17Smi.tdb:NA2O2_I  


### TDB models of NA2O2_I (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): NA2O2_I, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
72: PHASE NA2O2_I % 2 2 1 !
73: CONST NA2O2_I : NA+1 : O2-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase; reports values for this phase_

## NA2O2_II (Na–O)

- Id: `phase:na-o:na2o2-ii`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:II; no_structure_token
- Candidate (sgte_mmc2): (Na2O2-II) — Hallstedt 2025 mmc2 row for NA2O2_II: Na2O2-II
- Stability: not stable in 1 calculated diagram(s)
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:na2o2-ii)

Names (4): _corpus: _corpus:phase:na-o:na2o2-ii  
_paper: _paper:10.1016/j.jct.2017.04.003:Na2O2 II, paper:10.1016/j.jct.2017.04.003:Na2O2-II  
_tdb: _tdb:NaO-17Smi.tdb:NA2O2_II  


### TDB models of NA2O2_II (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): NA2O2_II, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
77: PHASE NA2O2_II % 2 2 1 !
78: CONST NA2O2_II : NA+1 : O2-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase; reports values for this phase_

## NAO2_B1 (Na–O)

- Id: `phase:na-o:nao2-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:nao2-b1)

Names (2): _corpus: _corpus:phase:na-o:nao2-b1  
_tdb: _tdb:NaO-17Smi.tdb:NAO2_B1  


### TDB models of NAO2_B1 (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): NAO2_B1, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
82: PHASE NAO2_B1 % 1 1 !
83: CONST NAO2_B1 : NAO2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase_

## O2GAS (Na–O)

- Id: `phase:na-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–422.5 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-o:o2gas)

Names (2): _corpus: _corpus:phase:na-o:o2gas  
_tdb: _tdb:NaO-17Smi.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[NaO-17Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb): O2GAS, type code %, sha256 `4ebf441b547a4b28…`

~~~~text
85: PHASE O2GAS % 1 1 !
86: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017).  
_assessment that models this phase_

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
