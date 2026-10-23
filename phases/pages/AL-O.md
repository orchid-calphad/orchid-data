# Al–O phases

> Al–O system: 9 phases (tier A 3, tier C 1, liquid 2, gas 2, unresolved_no_candidates 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-O.html · Markdown: https://data.orchid-project.org/phases/pages/AL-O.md

9 phases (tier A 3, tier C 1, liquid 2, gas 2, unresolved_no_candidates 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-O) · [full JSON](https://data.orchid-project.org/phases/systems/AL-O.json) · [Al–O system page](https://data.orchid-project.org/systems/AL-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–O system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-al-o-bcc-a2); _phase:al-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [CORUNDUM_D51](#phase-al-o-d51-corundum); _phase:al-o:d51-corundum_ | alpha-Al2O3 · D5_1 · hR10 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–2327 K, x(O) 0.6–0.6 | 0 | 3 |
| [DILUTE](#phase-al-o-dilute); _phase:al-o:dilute_ |  | unresolved_no_candidates | stable in 2 of 2 calculated diagram(s): 2054.81–2500 K, x(O) 0–0.00071 | 0 | 2 |
| [FCC_A1](#phase-al-o-fcc-a1); _phase:al-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–345 K, x(O) 0–0 | 0 | 3 |
| [GAS](#phase-al-o-gas); _phase:al-o:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 2213.75–2500 K, x(O) 0.30484–1 | 0 | 3 |
| [HCP_A3](#phase-al-o-hcp-a3); _phase:al-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ION](#phase-al-o-ion); _phase:al-o:ion_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 2054.81–2500 K, x(O) 0–0.6 | 0 | 3 |
| [LIQUID](#phase-al-o-liquid); _phase:al-o:liquid_ | liquid | liquid | not stable in 3 calculated diagram(s) | 0 | 3 |
| [O2GAS](#phase-al-o-o2gas); _phase:al-o:o2gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300–825 K, x(O) 1–1 | 0 | 3 |

## BCC_A2 (Al–O)

- Id: `phase:al-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:bcc-a2)

Names (4): _corpus: _corpus:phase:al-o:bcc-a2  
_tdb: _tdb:AlO-23Li.tdb:BCC_A2, tdb:AlO-92Tay.tdb:BCC_A2, tdb:AlO-93Hal-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): BCC_A2, type code %B, sha256 `b626da52ef13746e…`

~~~~text
52: PHASE BCC_A2 %B 2 1 3 !
53: CONST BCC_A2 : AL : VA : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): BCC_A2, type code %B, sha256 `f56b31da71628e62…`

~~~~text
53: PHASE BCC_A2 %B 2 1 3 !
54: CONST BCC_A2 : AL : VA : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): BCC_A2, type code %B, sha256 `3893b53d655fc07c…`

~~~~text
61: PHASE BCC_A2 %B 2 1 3 !
62: CONST BCC_A2 : AL : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## CORUNDUM_D51 (Al–O)

- Id: `phase:al-o:d51-corundum`; status `assigned`
- Structure: alpha-Al2O3 · D5_1 · hR10 · R-3c (167); type `st:d5-1-alpha-al2o3-hr10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:CORUNDUM); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 300–2327 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:d51-corundum)

Names (4): _corpus: _corpus:phase:al-o:d51-corundum  
_tdb: _tdb:AlO-23Li.tdb:CORUNDUM_D51, tdb:AlO-92Tay.tdb:CORUNDUM_D51, tdb:AlO-93Hal-LB.tdb:CORUNDUM_D51  


### TDB models of CORUNDUM_D51 (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): CORUNDUM_D51, type code %A, sha256 `b626da52ef13746e…`

~~~~text
62: PHASE CORUNDUM_D51:I %A 2 2 3 !
63: CONST CORUNDUM_D51:I : AL+3 : O-2 : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): CORUNDUM_D51, type code %A, sha256 `f56b31da71628e62…`

~~~~text
63: PHASE CORUNDUM_D51:I %A 2 2 3 !
64: CONST CORUNDUM_D51:I : AL+3 : O-2 : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): CORUNDUM_D51, type code %A, sha256 `3893b53d655fc07c…`

~~~~text
71: PHASE CORUNDUM_D51:I %A 2 2 3 !
72: CONST CORUNDUM_D51:I : AL+3 : O-2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## DILUTE (Al–O)

- Id: `phase:al-o:dilute`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:DILUTE; no_structure_token
- Stability: stable in 2 of 2 calculated diagram(s): 2054.81–2500 K, x(O) 0–0.00071
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:dilute)

Names (3): _corpus: _corpus:phase:al-o:dilute  
_tdb: _tdb:AlO-92Tay.tdb:DILUTE, tdb:AlO-93Hal-LB.tdb:DILUTE  


### TDB models of DILUTE (2): PHASE and CONSTITUENT statements as written

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): DILUTE, type code %, sha256 `f56b31da71628e62…`

~~~~text
43: PHASE DILUTE % 1 1 !
44: CONST DILUTE : AL O : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): DILUTE, type code %, sha256 `3893b53d655fc07c…`

~~~~text
51: PHASE DILUTE % 1 1 !
52: CONST DILUTE : AL O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_

## FCC_A1 (Al–O)

- Id: `phase:al-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–345 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:fcc-a1)

Names (4): _corpus: _corpus:phase:al-o:fcc-a1  
_tdb: _tdb:AlO-23Li.tdb:FCC_A1, tdb:AlO-92Tay.tdb:FCC_A1, tdb:AlO-93Hal-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): FCC_A1, type code %A, sha256 `b626da52ef13746e…`

~~~~text
47: PHASE FCC_A1 %A 2 1 1 !
48: CONST FCC_A1 : AL : VA : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): FCC_A1, type code %A, sha256 `f56b31da71628e62…`

~~~~text
48: PHASE FCC_A1 %A 2 1 1 !
49: CONST FCC_A1 : AL : VA : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): FCC_A1, type code %A, sha256 `3893b53d655fc07c…`

~~~~text
56: PHASE FCC_A1 %A 2 1 1 !
57: CONST FCC_A1 : AL : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## GAS (Al–O)

- Id: `phase:al-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2213.75–2500 K, x(O) 0.30484–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:gas)

Names (4): _corpus: _corpus:phase:al-o:gas  
_tdb: _tdb:AlO-23Li.tdb:GAS, tdb:AlO-92Tay.tdb:GAS, tdb:AlO-93Hal-LB.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): GAS, type code %, sha256 `b626da52ef13746e…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : AL% AL2 ALO ALO2 AL2O% AL2O2 AL2O3 O O2% O3 : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): GAS, type code %, sha256 `f56b31da71628e62…`

~~~~text
66: PHASE GAS:G % 1 1 !
67: CONST GAS:G : AL% AL2 ALO ALO2 AL2O% AL2O2 AL2O3 O O2% O3 : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): GAS, type code %, sha256 `3893b53d655fc07c…`

~~~~text
74: PHASE GAS:G % 1 1 !
75: CONST GAS:G : AL% AL2 ALO ALO2 AL2O% AL2O2 AL2O3 O O2% O3 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## HCP_A3 (Al–O)

- Id: `phase:al-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:hcp-a3)

Names (4): _corpus: _corpus:phase:al-o:hcp-a3  
_tdb: _tdb:AlO-23Li.tdb:HCP_A3, tdb:AlO-92Tay.tdb:HCP_A3, tdb:AlO-93Hal-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): HCP_A3, type code %A, sha256 `b626da52ef13746e…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : AL : VA : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): HCP_A3, type code %A, sha256 `f56b31da71628e62…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : AL : VA : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): HCP_A3, type code %A, sha256 `3893b53d655fc07c…`

~~~~text
66: PHASE HCP_A3 %A 2 1 0.5 !
67: CONST HCP_A3 : AL : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## ION (Al–O)

- Id: `phase:al-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2054.81–2500 K, x(O) 0–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:ion)

Names (4): _corpus: _corpus:phase:al-o:ion  
_tdb: _tdb:AlO-23Li.tdb:ION, tdb:AlO-92Tay.tdb:ION, tdb:AlO-93Hal-LB.tdb:ION  


### TDB models of ION (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): ION, type code %, sha256 `b626da52ef13746e…`

~~~~text
39: PHASE ION:Y % 2 1 1 !
40: CONST ION:Y : AL+3 : O-2 VA : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): ION, type code %, sha256 `f56b31da71628e62…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : AL+3 : O-2 VA : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): ION, type code %, sha256 `3893b53d655fc07c…`

~~~~text
45: PHASE ION:Y % 2 1 1 !
46: CONST ION:Y : AL+3 : O-2 VA ALO3/2% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## LIQUID (Al–O)

- Id: `phase:al-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:liquid)

Names (4): _corpus: _corpus:phase:al-o:liquid  
_tdb: _tdb:AlO-23Li.tdb:LIQUID, tdb:AlO-92Tay.tdb:LIQUID, tdb:AlO-93Hal-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): LIQUID, type code %, sha256 `b626da52ef13746e…`

~~~~text
42: PHASE LIQUID:L % 1 1 !
43: CONST LIQUID:L : AL : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): LIQUID, type code %, sha256 `f56b31da71628e62…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : AL ALO3/2 : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): LIQUID, type code %, sha256 `3893b53d655fc07c…`

~~~~text
48: PHASE LIQUID:L % 1 1 !
49: CONST LIQUID:L : AL ALO3/2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## O2GAS (Al–O)

- Id: `phase:al-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–825 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-o:o2gas)

Names (4): _corpus: _corpus:phase:al-o:o2gas  
_tdb: _tdb:AlO-23Li.tdb:O2GAS, tdb:AlO-92Tay.tdb:O2GAS, tdb:AlO-93Hal-LB.tdb:O2GAS  


### TDB models of O2GAS (3): PHASE and CONSTITUENT statements as written

[AlO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb): O2GAS, type code %, sha256 `b626da52ef13746e…`

~~~~text
68: PHASE O2GAS % 1 1 !
69: CONST O2GAS : O2 : !
~~~~

[AlO-92Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb): O2GAS, type code %, sha256 `f56b31da71628e62…`

~~~~text
69: PHASE O2GAS % 1 1 !
70: CONST O2GAS : O2 : !
~~~~

[AlO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb): O2GAS, type code %, sha256 `3893b53d655fc07c…`

~~~~text
77: PHASE O2GAS % 1 1 !
78: CONST O2GAS : O2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
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
