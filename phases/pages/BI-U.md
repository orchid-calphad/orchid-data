# Bi–U phases

> Bi–U system: 10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-U.html · Markdown: https://data.orchid-project.org/phases/pages/BI-U.md

10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-U) · [full JSON](https://data.orchid-project.org/phases/systems/BI-U.json) · [Bi–U system page](https://data.orchid-project.org/systems/BI-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–U system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-bi-u-a20-orthorhombic); _phase:bi-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–942.03 K, x(U) 1–1 | 0 | 2 |
| [RHOMBOHEDRAL_A7](#phase-bi-u-a7-rhombohedral); _phase:bi-u:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(U) 0–0 | 2 | 2 |
| [BCC_A2](#phase-bi-u-bcc-a2); _phase:bi-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1048.99–3999.24 K, x(U) 0.99998–1 | 4 | 2 |
| [BI2U](#phase-bi-u-bi2u); _phase:bi-u:bi2u_ | UAs2 · tP6 · P4/nmm (129) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1281.52 K, x(U) 0.33333–0.33333 | 76 | 2 |
| [BI4U3_D73](#phase-bi-u-bi4u3-d73); _phase:bi-u:bi4u3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1424.47 K, x(U) 0.42857–0.42857 | 4 | 2 |
| [BIU_B1](#phase-bi-u-biu-b1); _phase:bi-u:biu-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1674.42 K, x(U) 0.5–0.5 | 10 | 2 |
| [FCC_A1](#phase-bi-u-fcc-a1); _phase:bi-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-bi-u-hcp-a3); _phase:bi-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-bi-u-liquid); _phase:bi-u:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 542.38–4000 K, x(U) 0–1 | 11 | 2 |
| [TETRAGONAL_U](#phase-bi-u-u-tetragonal); _phase:bi-u:u-tetragonal_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300.78–1403.99 K, x(U) 1–1 | 0 | 2 |

## ORTHORHOMBIC_A20 (Bi–U)

- Id: `phase:bi-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–942.03 K, x(U) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:a20-orthorhombic)

Names (4): _corpus: _corpus:phase:bi-u:a20-orthorhombic, corpus:phase:bi-u:orthorhombic-a20  
_tdb: _tdb:BiU-11Wan.tdb:ORTHORHOMBIC_A20, tdb:BiU-21Aga.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): ORTHORHOMBIC_A20, type code %, sha256 `7dd97a31494481fb…`

~~~~text
47: PHASE ORTHORHOMBIC_A20 % 1 1 !
48: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): ORTHORHOMBIC_A20, type code %, sha256 `54437879543405d4…`

~~~~text
52: PHASE ORTHORHOMBIC_A20 % 1 1 !
53: CONST ORTHORHOMBIC_A20 : BI U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (Bi–U)

- Id: `phase:bi-u:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(U) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:a7-rhombohedral)

Names (5): _corpus: _corpus:phase:bi-u:a7-rhombohedral, corpus:phase:bi-u:rhombohedral-a7  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:Bi  
_tdb: _tdb:BiU-11Wan.tdb:RHOMBOHEDRAL_A7, tdb:BiU-21Aga.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `7dd97a31494481fb…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `54437879543405d4…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : BI% U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## BCC_A2 (Bi–U)

- Id: `phase:bi-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1048.99–3999.24 K, x(U) 0.99998–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:bcc-a2)

Names (4): _corpus: _corpus:phase:bi-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:γU  
_tdb: _tdb:BiU-11Wan.tdb:BCC_A2, tdb:BiU-21Aga.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): BCC_A2, type code %B, sha256 `7dd97a31494481fb…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : BI U% : VA : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): BCC_A2, type code %B, sha256 `54437879543405d4…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : BI U% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## BI2U (Bi–U)

- Id: `phase:bi-u:bi2u`; status `assigned`
- Structure: UAs2 · tP6 · P4/nmm (129); type `st:uas2-tp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.6667, U 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1281.52 K, x(U) 0.33333–0.33333
- Literature: 76 values (76 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:bi2u)

Names (5): _corpus: _corpus:phase:bi-u:bi2u  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:UBi2, paper:10.1016/j.tca.2021.178913:Bi2U(s)  
_tdb: _tdb:BiU-11Wan.tdb:BI2U, tdb:BiU-21Aga.tdb:BI2U  


### TDB models of BI2U (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): BI2U, type code %, sha256 `7dd97a31494481fb…`

~~~~text
57: PHASE BI2U % 2 2 1 !
58: CONST BI2U : BI : U : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): BI2U, type code %, sha256 `54437879543405d4…`

~~~~text
62: PHASE BI2U % 2 2 1 !
63: CONST BI2U : BI : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_

## BI4U3_D73 (Bi–U)

- Id: `phase:bi-u:bi4u3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5714, U 0.4286
- Stability: stable in 2 of 2 calculated diagram(s): 300–1424.47 K, x(U) 0.42857–0.42857
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:bi4u3-d73)

Names (4): _corpus: _corpus:phase:bi-u:bi4u3-d73  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:U3Bi4  
_tdb: _tdb:BiU-11Wan.tdb:BI4U3_D73, tdb:BiU-21Aga.tdb:BI4U3_D73  


### TDB models of BI4U3_D73 (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): BI4U3_D73, type code %, sha256 `7dd97a31494481fb…`

~~~~text
62: PHASE BI4U3_D73 % 2 4 3 !
63: CONST BI4U3_D73 : BI : U : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): BI4U3_D73, type code %, sha256 `54437879543405d4…`

~~~~text
67: PHASE BI4U3_D73 % 2 4 3 !
68: CONST BI4U3_D73 : BI : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## BIU_B1 (Bi–U)

- Id: `phase:bi-u:biu-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, U 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1674.42 K, x(U) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:biu-b1)

Names (4): _corpus: _corpus:phase:bi-u:biu-b1  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:UBi  
_tdb: _tdb:BiU-11Wan.tdb:BIU_B1, tdb:BiU-21Aga.tdb:BIU_B1  


### TDB models of BIU_B1 (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): BIU_B1, type code %, sha256 `7dd97a31494481fb…`

~~~~text
67: PHASE BIU_B1 % 2 1 1 !
68: CONST BIU_B1 : BI : U : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): BIU_B1, type code %, sha256 `54437879543405d4…`

~~~~text
72: PHASE BIU_B1 % 2 1 1 !
73: CONST BIU_B1 : BI : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## FCC_A1 (Bi–U)

- Id: `phase:bi-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-u:fcc-a1  
_tdb: _tdb:BiU-11Wan.tdb:FCC_A1, tdb:BiU-21Aga.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): FCC_A1, type code %A, sha256 `7dd97a31494481fb…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BI U : VA : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): FCC_A1, type code %A, sha256 `54437879543405d4…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : BI U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## HCP_A3 (Bi–U)

- Id: `phase:bi-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-u:hcp-a3  
_tdb: _tdb:BiU-11Wan.tdb:HCP_A3, tdb:BiU-21Aga.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): HCP_A3, type code %A, sha256 `7dd97a31494481fb…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : BI U : VA: !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): HCP_A3, type code %A, sha256 `54437879543405d4…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : BI U : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## LIQUID (Bi–U)

- Id: `phase:bi-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 542.38–4000 K, x(U) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:liquid)

Names (5): _corpus: _corpus:phase:bi-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:L, paper:10.1016/j.jnucmat.2011.02.021:L2  
_tdb: _tdb:BiU-11Wan.tdb:LIQUID, tdb:BiU-21Aga.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): LIQUID, type code %, sha256 `7dd97a31494481fb…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BI U : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): LIQUID, type code %, sha256 `54437879543405d4…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : BI U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## TETRAGONAL_U (Bi–U)

- Id: `phase:bi-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — BiU-11Wan.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — BiU-21Aga.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 2 of 2 calculated diagram(s): 300.78–1403.99 K, x(U) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-u:u-tetragonal)

Names (4): _corpus: _corpus:phase:bi-u:u-tetragonal, corpus:phase:bi-u:tetragonal-u  
_tdb: _tdb:BiU-11Wan.tdb:TETRAGONAL_U, tdb:BiU-21Aga.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (2): PHASE and CONSTITUENT statements as written

[BiU-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-11Wan.tdb): TETRAGONAL_U, type code %, sha256 `7dd97a31494481fb…`

~~~~text
52: PHASE TETRAGONAL_U % 1 1 !
53: CONST TETRAGONAL_U : U : !
~~~~

[BiU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiU-21Aga.tdb): TETRAGONAL_U, type code %, sha256 `54437879543405d4…`

~~~~text
57: PHASE TETRAGONAL_U % 1 1 !
58: CONST TETRAGONAL_U : BI U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
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
