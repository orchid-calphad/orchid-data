# As–Cu phases

> As–Cu system: 12 phases (tier A 6, liquid 2, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-CU.html · Markdown: https://data.orchid-project.org/phases/pages/AS-CU.md

12 phases (tier A 6, liquid 2, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-CU) · [full JSON](https://data.orchid-project.org/phases/systems/AS-CU.json) · [Markdown](https://data.orchid-project.org/phases/pages/AS-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–Cu system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-as-cu-a7-rhombohedral); _phase:as-cu:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1090 K, x(As) 1–1 | 0 | 2 |
| [BCC_A2](#phase-as-cu-bcc-a2); _phase:as-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [CU12AS5_D03](#phase-as-cu-cu12as5-d03); _phase:as-cu:cu12as5-d03_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 573.12–982.59 K, x(As) 0.29412–0.29412 | 0 | 1 |
| [CU3AS](#phase-as-cu-cu3as); _phase:as-cu:cu3as_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1073.82 K, x(As) 0.25178–0.27711 | 0 | 1 |
| [CU3AS_D06](#phase-as-cu-cu3as-d06); _phase:as-cu:cu3as-d06_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1102.22 K, x(As) 0.25294–0.27659 | 0 | 1 |
| [CU7AS_A3](#phase-as-cu-cu7as-a3); _phase:as-cu:cu7as-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–620.29 K, x(As) 0.125–0.125 | 0 | 1 |
| [CU7AS3_D03](#phase-as-cu-cu7as3-d03); _phase:as-cu:cu7as3-d03_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 615.39–966.31 K, x(As) 0.3–0.3 | 0 | 1 |
| [CU8AS_A3](#phase-as-cu-cu8as-a3); _phase:as-cu:cu8as-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–597.77 K, x(As) 0.11111–0.11111 | 0 | 1 |
| [FCC_A1](#phase-as-cu-fcc-a1); _phase:as-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.02 K, x(As) 0–0.06812 | 0 | 2 |
| [HCP_A3](#phase-as-cu-hcp-a3); _phase:as-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-as-cu-ion); _phase:as-cu:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 872.04–2500 K, x(As) 0–0.99827 | 0 | 1 |
| [LIQUID](#phase-as-cu-liquid); _phase:as-cu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 802.79–2500 K, x(As) 0–1 | 0 | 2 |

## RHOMBOHEDRAL_A7 (As–Cu)

- Id: `phase:as-cu:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1090 K, x(As) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:as-cu:a7-rhombohedral  
_tdb: _tdb:CuAs-01Uhl.tdb:RHOMBOHEDRAL_A7, tdb:CuAs-94Pei-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `37d4768fa49739e5…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8227f3feed69881f…`

~~~~text
63: PHASE RHOMBOHEDRAL_A7 % 1 1 !
64: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## BCC_A2 (As–Cu)

- Id: `phase:as-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:bcc-a2)

Names (3): _corpus: _corpus:phase:as-cu:bcc-a2  
_tdb: _tdb:CuAs-01Uhl.tdb:BCC_A2, tdb:CuAs-94Pei-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): BCC_A2, type code %B, sha256 `37d4768fa49739e5…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AS CU : VA : !
~~~~

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): BCC_A2, type code %B, sha256 `8227f3feed69881f…`

~~~~text
53: PHASE BCC_A2 %B 2 1 3 !
54: CONST BCC_A2 : AS CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## CU12AS5_D03 (As–Cu)

- Id: `phase:as-cu:cu12as5-d03`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D0_3; stoichiometry_contradicts_D0_3:CuAs-94Pei-LB.tdb
- Candidate (name_token): BiF3 · D0_3 · cF16 · Fm-3m (225) — Strukturbericht/word 'D03' in the TDB name
- Candidate (sgte_mmc2): BiF3 · D0_3 · cF16 · Fm-3m (225) — Hallstedt 2025 mmc2 row for CU12AS5_D03: Cu12As5
- Candidate (tdb_comment): BiF3 · cF16 · Fm-3m — CuAs-94Pei-LB.tdb: 'Prototype BiF3 (cF16, Fm-3m)'
- Stoichiometry: As 0.2941, Cu 0.7059
- Stability: stable in 1 of 1 calculated diagram(s): 573.12–982.59 K, x(As) 0.29412–0.29412
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:cu12as5-d03)

Names (2): _corpus: _corpus:phase:as-cu:cu12as5-d03  
_tdb: _tdb:CuAs-94Pei-LB.tdb:CU12AS5_D03  


### TDB models of CU12AS5_D03 (1): PHASE and CONSTITUENT statements as written

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): CU12AS5_D03, type code %, sha256 `8227f3feed69881f…`

~~~~text
78: PHASE CU12AS5_D03 % 2 12 5 !
79: CONST CU12AS5_D03 : CU : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## CU3AS (As–Cu)

- Id: `phase:as-cu:cu3as`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): HoH3 · hP24 · P-3c1 (165) — Hallstedt 2025 mmc2 row for CU3AS: Cu3As
- Candidate (tdb_comment): HoH3 · hP24 · P-3c1 — CuAs-01Uhl.tdb: 'Prototype HoH3 (hP24, P-3c1), prototype Cu3As suggested in LB binary'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1073.82 K, x(As) 0.25178–0.27711
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:cu3as)

Names (2): _corpus: _corpus:phase:as-cu:cu3as  
_tdb: _tdb:CuAs-01Uhl.tdb:CU3AS  


### TDB models of CU3AS (1): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): CU3AS, type code %, sha256 `37d4768fa49739e5…`

~~~~text
57: PHASE CU3AS % 2 3 1.15 !
58: CONST CU3AS : CU : AS% CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## CU3AS_D06 (As–Cu)

- Id: `phase:as-cu:cu3as-d06`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:D06; no_structure_token
- Candidate (tdb_comment): HoH3 · hP24 · P-3c1 — CuAs-94Pei-LB.tdb: 'Prototype HoH3 (hP24, P-3c1), prototype Cu3As suggested in LB binary'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1102.22 K, x(As) 0.25294–0.27659
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:cu3as-d06)

Names (2): _corpus: _corpus:phase:as-cu:cu3as-d06  
_tdb: _tdb:CuAs-94Pei-LB.tdb:CU3AS_D06  


### TDB models of CU3AS_D06 (1): PHASE and CONSTITUENT statements as written

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): CU3AS_D06, type code %, sha256 `8227f3feed69881f…`

~~~~text
73: PHASE CU3AS_D06 % 2 3 1 !
74: CONST CU3AS_D06 : CU VA : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## CU7AS_A3 (As–Cu)

- Id: `phase:as-cu:cu7as-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: As 0.1250, Cu 0.8750
- Stability: stable in 1 of 1 calculated diagram(s): 300–620.29 K, x(As) 0.125–0.125
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:cu7as-a3)

Names (2): _corpus: _corpus:phase:as-cu:cu7as-a3  
_tdb: _tdb:CuAs-01Uhl.tdb:CU7AS_A3  


### TDB models of CU7AS_A3 (1): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): CU7AS_A3, type code %, sha256 `37d4768fa49739e5…`

~~~~text
52: PHASE CU7AS_A3 % 2 7 1 !
53: CONST CU7AS_A3 : CU : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## CU7AS3_D03 (As–Cu)

- Id: `phase:as-cu:cu7as3-d03`; status `needs_review`
- No structure assigned. Why: stoichiometry_contradicts_D0_3:CuAs-01Uhl.tdb
- Candidate (name_token): BiF3 · D0_3 · cF16 · Fm-3m (225) — Strukturbericht/word 'D03' in the TDB name
- Candidate (tdb_comment): BiF3 · cF16 · Fm-3m — CuAs-01Uhl.tdb: 'Prototype BiF3 (cF16, Fm-3m)'
- Stoichiometry: As 0.3000, Cu 0.7000
- Stability: stable in 1 of 1 calculated diagram(s): 615.39–966.31 K, x(As) 0.3–0.3
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:cu7as3-d03)

Names (2): _corpus: _corpus:phase:as-cu:cu7as3-d03  
_tdb: _tdb:CuAs-01Uhl.tdb:CU7AS3_D03  


### TDB models of CU7AS3_D03 (1): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): CU7AS3_D03, type code %, sha256 `37d4768fa49739e5…`

~~~~text
62: PHASE CU7AS3_D03 % 2 7 3 !
63: CONST CU7AS3_D03 : CU : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## CU8AS_A3 (As–Cu)

- Id: `phase:as-cu:cu8as-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: As 0.1111, Cu 0.8889
- Stability: stable in 1 of 1 calculated diagram(s): 300–597.77 K, x(As) 0.11111–0.11111
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:cu8as-a3)

Names (2): _corpus: _corpus:phase:as-cu:cu8as-a3  
_tdb: _tdb:CuAs-94Pei-LB.tdb:CU8AS_A3  


### TDB models of CU8AS_A3 (1): PHASE and CONSTITUENT statements as written

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): CU8AS_A3, type code %, sha256 `8227f3feed69881f…`

~~~~text
68: PHASE CU8AS_A3 % 2 8 1 !
69: CONST CU8AS_A3 : CU : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## FCC_A1 (As–Cu)

- Id: `phase:as-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.02 K, x(As) 0–0.06812
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:fcc-a1)

Names (3): _corpus: _corpus:phase:as-cu:fcc-a1  
_tdb: _tdb:CuAs-01Uhl.tdb:FCC_A1, tdb:CuAs-94Pei-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): FCC_A1, type code %A, sha256 `37d4768fa49739e5…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AS CU : VA : !
~~~~

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): FCC_A1, type code %A, sha256 `8227f3feed69881f…`

~~~~text
48: PHASE FCC_A1 %A 2 1 1 !
49: CONST FCC_A1 : AS CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## HCP_A3 (As–Cu)

- Id: `phase:as-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:as-cu:hcp-a3  
_tdb: _tdb:CuAs-01Uhl.tdb:HCP_A3, tdb:CuAs-94Pei-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): HCP_A3, type code %A, sha256 `37d4768fa49739e5…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AS CU : VA : !
~~~~

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): HCP_A3, type code %A, sha256 `8227f3feed69881f…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : AS CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## ION (As–Cu)

- Id: `phase:as-cu:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 872.04–2500 K, x(As) 0–0.99827
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:ion)

Names (2): _corpus: _corpus:phase:as-cu:ion  
_tdb: _tdb:CuAs-94Pei-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): ION, type code %, sha256 `8227f3feed69881f…`

~~~~text
43: PHASE ION:Y % 2 1 1 !
44: CONST ION:Y : CU+1 : AS-3 VA AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
_assessment that models this phase_

## LIQUID (As–Cu)

- Id: `phase:as-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 802.79–2500 K, x(As) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-cu:liquid)

Names (3): _corpus: _corpus:phase:as-cu:liquid  
_tdb: _tdb:CuAs-01Uhl.tdb:LIQUID, tdb:CuAs-94Pei-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-01Uhl.tdb): LIQUID, type code %, sha256 `37d4768fa49739e5…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AS CU : !
~~~~

[CuAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuAs-94Pei-LB.tdb): LIQUID, type code %, sha256 `8227f3feed69881f…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : CU AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850305](https://doi.org/10.1515/ijmr-1994-850305) B. Pei, B. Bjorkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 178-84(1994).  
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
