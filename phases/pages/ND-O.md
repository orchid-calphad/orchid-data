# Nd–O phases

> Nd–O system: 10 phases (tier A 4, tier C 3, liquid 1, gas 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ND-O.html · Markdown: https://data.orchid-project.org/phases/pages/ND-O.md

10 phases (tier A 4, tier C 3, liquid 1, gas 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ND-O) · [full JSON](https://data.orchid-project.org/phases/systems/ND-O.json) · [Nd–O system page](https://data.orchid-project.org/systems/ND-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/ND-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nd–O system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nd-o-bcc-a2); _phase:nd-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1128–1305.26 K, x(O) 0–0.01477 | 0 | 2 |
| [A_R2O3_D52](#phase-nd-o-d52-a-r2o3); _phase:nd-o:d52-a-r2o3_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2172.76 K, x(O) 0.6–0.6 | 0 | 2 |
| [DHCP](#phase-nd-o-dhcp-a3); _phase:nd-o:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1135 K, x(O) 0–0.00786 | 0 | 2 |
| [FCC_A1](#phase-nd-o-fcc-a1); _phase:nd-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-nd-o-gas); _phase:nd-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 2485–2500 K, x(O) 1–1 | 0 | 1 |
| [H_R2O3](#phase-nd-o-h-r2o3); _phase:nd-o:h-r2o3_ | H-La2O3 · hP10 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-nd-o-hcp-a3); _phase:nd-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-nd-o-ion); _phase:nd-o:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1264–2500 K, x(O) 0–0.57992 | 0 | 2 |
| [O2GAS](#phase-nd-o-o2gas); _phase:nd-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 1–1 | 0 | 2 |
| [X_R2O3](#phase-nd-o-r2o3-x); _phase:nd-o:r2o3-x_ | Nd2O3 · cI26 · Im-3m (229) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 2475–2500 K, x(O) 0.6–0.6 | 0 | 2 |

## BCC_A2 (Nd–O)

- Id: `phase:nd-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1128–1305.26 K, x(O) 0–0.01477
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:bcc-a2)

Names (3): _corpus: _corpus:phase:nd-o:bcc-a2  
_tdb: _tdb:NdO-07Zin.tdb:BCC_A2, tdb:NdO-15Dot.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): BCC_A2, type code %B, sha256 `0671e946c589d9b9…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : ND : VA : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): BCC_A2, type code %B, sha256 `cbc54824da87bc68…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : ND : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## A_R2O3_D52 (Nd–O)

- Id: `phase:nd-o:d52-a-r2o3`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:A,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–2172.76 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:d52-a-r2o3)

Names (3): _corpus: _corpus:phase:nd-o:d52-a-r2o3  
_tdb: _tdb:NdO-07Zin.tdb:A_R2O3_D52, tdb:NdO-15Dot.tdb:A_R2O3_D52  


### TDB models of A_R2O3_D52 (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): A_R2O3_D52, type code %, sha256 `0671e946c589d9b9…`

~~~~text
57: PHASE A_R2O3_D52:I % 2 2 3 !
58: CONST A_R2O3_D52:I : ND+3 : O-2 : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): A_R2O3_D52, type code %, sha256 `cbc54824da87bc68…`

~~~~text
56: PHASE A_R2O3_D52:I % 2 2 3 !
57: CONST A_R2O3_D52:I : ND+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## DHCP (Nd–O)

- Id: `phase:nd-o:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1135 K, x(O) 0–0.00786
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:dhcp-a3)

Names (3): _corpus: _corpus:phase:nd-o:dhcp-a3  
_tdb: _tdb:NdO-07Zin.tdb:DHCP, tdb:NdO-15Dot.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): DHCP, type code %, sha256 `0671e946c589d9b9…`

~~~~text
52: PHASE DHCP % 1 1 !
53: CONST DHCP : ND : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): DHCP, type code %, sha256 `cbc54824da87bc68…`

~~~~text
51: PHASE DHCP % 2 1 0.5 !
52: CONST DHCP : ND : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## FCC_A1 (Nd–O)

- Id: `phase:nd-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Nd 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:fcc-a1)

Names (3): _corpus: _corpus:phase:nd-o:fcc-a1  
_tdb: _tdb:NdO-07Zin.tdb:FCC_A1, tdb:NdO-15Dot.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): FCC_A1, type code %A, sha256 `0671e946c589d9b9…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : ND : VA : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): FCC_A1, type code %A, sha256 `cbc54824da87bc68…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : ND : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## GAS (Nd–O)

- Id: `phase:nd-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2485–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:gas)

Names (2): _corpus: _corpus:phase:nd-o:gas  
_tdb: _tdb:NdO-15Dot.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): GAS, type code %, sha256 `cbc54824da87bc68…`

~~~~text
69: PHASE GAS:G % 1 1 !
70: CONST GAS:G : ND O O2% O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_

## H_R2O3 (Nd–O)

- Id: `phase:nd-o:h-r2o3`; status `assigned`
- Structure: H-La2O3 · hP10 · P6_3/mmc (194); type `st:h-la2o3-hp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:H,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:h-r2o3)

Names (3): _corpus: _corpus:phase:nd-o:h-r2o3  
_tdb: _tdb:NdO-07Zin.tdb:H_R2O3, tdb:NdO-15Dot.tdb:H_R2O3  


### TDB models of H_R2O3 (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): H_R2O3, type code %, sha256 `0671e946c589d9b9…`

~~~~text
62: PHASE H_R2O3:I % 2 2 3 !
63: CONST H_R2O3:I : ND+3 : O-2 : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): H_R2O3, type code %, sha256 `cbc54824da87bc68…`

~~~~text
61: PHASE H_R2O3:I % 2 2 3 !
62: CONST H_R2O3:I : ND+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## HCP_A3 (Nd–O)

- Id: `phase:nd-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Nd 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:hcp-a3)

Names (3): _corpus: _corpus:phase:nd-o:hcp-a3  
_tdb: _tdb:NdO-07Zin.tdb:HCP_A3, tdb:NdO-15Dot.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): HCP_A3, type code %A, sha256 `0671e946c589d9b9…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : ND : VA : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): HCP_A3, type code %A, sha256 `cbc54824da87bc68…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : ND : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## ION (Nd–O)

- Id: `phase:nd-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1264–2500 K, x(O) 0–0.57992
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:ion)

Names (3): _corpus: _corpus:phase:nd-o:ion  
_tdb: _tdb:NdO-07Zin.tdb:ION, tdb:NdO-15Dot.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): ION, type code %, sha256 `0671e946c589d9b9…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : ND+3 : O-2 VA : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): ION, type code %, sha256 `cbc54824da87bc68…`

~~~~text
31: PHASE ION:Y % 2 1 1 !
32: CONST ION:Y : ND+3 : O-2 VA O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## O2GAS (Nd–O)

- Id: `phase:nd-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:o2gas)

Names (3): _corpus: _corpus:phase:nd-o:o2gas  
_tdb: _tdb:NdO-07Zin.tdb:O2GAS, tdb:NdO-15Dot.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): O2GAS, type code %, sha256 `0671e946c589d9b9…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): O2GAS, type code %, sha256 `cbc54824da87bc68…`

~~~~text
72: PHASE O2GAS % 1 1 !
73: CONST O2GAS : O2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## X_R2O3 (Nd–O)

- Id: `phase:nd-o:r2o3-x`; status `assigned`
- Structure: Nd2O3 · cI26 · Im-3m (229); type `st:nd2o3-ci26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:R2O3,X, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 2475–2500 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-o:r2o3-x)

Names (3): _corpus: _corpus:phase:nd-o:r2o3-x  
_tdb: _tdb:NdO-07Zin.tdb:X_R2O3, tdb:NdO-15Dot.tdb:X_R2O3  


### TDB models of X_R2O3 (2): PHASE and CONSTITUENT statements as written

[NdO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb): X_R2O3, type code %, sha256 `0671e946c589d9b9…`

~~~~text
67: PHASE X_R2O3:I % 2 2 3 !
68: CONST X_R2O3:I : ND+3 : O-2 : !
~~~~

[NdO-15Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb): X_R2O3, type code %, sha256 `cbc54824da87bc68…`

~~~~text
66: PHASE X_R2O3:I % 2 2 3 !
67: CONST X_R2O3:I : ND+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) Giannina Dottavio, Yves Pontillon, Lionel Desgranges, Christine Guéneau, Renaud C. Belin, Characterising the U–Nd–O miscibility gap by an experimental and a theoretical approach, Journal of Nuclear Materials 458, 394-405 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

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
