# As–Fe phases

> As–Fe system: 10 phases (tier A 7, liquid 2, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-FE.html · Markdown: https://data.orchid-project.org/phases/pages/AS-FE.md

10 phases (tier A 7, liquid 2, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-FE) · [full JSON](https://data.orchid-project.org/phases/systems/AS-FE.json) · [As–Fe system page](https://data.orchid-project.org/systems/AS-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AS-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–Fe system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-as-fe-a7-rhombohedral); _phase:as-fe:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1095.45 K, x(As) 1–1 | 0 | 2 |
| [BCC_A2](#phase-as-fe-bcc-a2); _phase:as-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.68 K, x(As) 0–0.09849 | 0 | 2 |
| [FCC_A1](#phase-as-fe-fcc-a1); _phase:as-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 301.21–1789.82 K, x(As) 0–0.01503 | 0 | 2 |
| [FE2AS_C38](#phase-as-fe-fe2as-c38); _phase:as-fe:fe2as-c38_ | Cu2Sb · C38 · tP6 · P4/nmm (129) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1202.46 K, x(As) 0.33333–0.33333 | 0 | 2 |
| [FE3AS2](#phase-as-fe-fe3as2); _phase:as-fe:fe3as2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1096.12–1249.91 K, x(As) 0.39708–0.42149 | 0 | 2 |
| [FEAS_B31](#phase-as-fe-feas-b31); _phase:as-fe:feas-b31_ | MnP · B31 · oP8 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1315.16 K, x(As) 0.5–0.5 | 0 | 2 |
| [FEAS2_C18](#phase-as-fe-feas2-c18); _phase:as-fe:feas2-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1293.72 K, x(As) 0.66667–0.66667 | 0 | 2 |
| [HCP_A3](#phase-as-fe-hcp-a3); _phase:as-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-as-fe-ion); _phase:as-fe:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1077.52–2500 K, x(As) 0–1 | 0 | 1 |
| [LIQUID](#phase-as-fe-liquid); _phase:as-fe:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1075.45–2500 K, x(As) 0–1 | 0 | 1 |

## RHOMBOHEDRAL_A7 (As–Fe)

- Id: `phase:as-fe:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1095.45 K, x(As) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:as-fe:a7-rhombohedral  
_tdb: _tdb:FeAs-08Ohn.tdb:RHOMBOHEDRAL_A7, tdb:FeAs-94Pei-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `ed9f68c0b96e5b34…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `24c905685b77bd98…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## BCC_A2 (As–Fe)

- Id: `phase:as-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.68 K, x(As) 0–0.09849
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:bcc-a2)

Names (3): _corpus: _corpus:phase:as-fe:bcc-a2  
_tdb: _tdb:FeAs-08Ohn.tdb:BCC_A2, tdb:FeAs-94Pei-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): BCC_A2, type code %B, sha256 `ed9f68c0b96e5b34…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AS FE% : VA : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): BCC_A2, type code %B, sha256 `24c905685b77bd98…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AS FE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## FCC_A1 (As–Fe)

- Id: `phase:as-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 301.21–1789.82 K, x(As) 0–0.01503
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:fcc-a1)

Names (3): _corpus: _corpus:phase:as-fe:fcc-a1  
_tdb: _tdb:FeAs-08Ohn.tdb:FCC_A1, tdb:FeAs-94Pei-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): FCC_A1, type code %A, sha256 `ed9f68c0b96e5b34…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AS FE% : VA : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): FCC_A1, type code %A, sha256 `24c905685b77bd98…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AS FE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## FE2AS_C38 (As–Fe)

- Id: `phase:as-fe:fe2as-c38`; status `assigned`
- Structure: Cu2Sb · C38 · tP6 · P4/nmm (129); type `st:c38-cu2sb-tp6`; tier A: standard phase name; confidence high
- Stoichiometry: As 0.3333, Fe 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1202.46 K, x(As) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:fe2as-c38)

Names (3): _corpus: _corpus:phase:as-fe:fe2as-c38  
_tdb: _tdb:FeAs-08Ohn.tdb:FE2AS_C38, tdb:FeAs-94Pei-LB.tdb:FE2AS_C38  


### TDB models of FE2AS_C38 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): FE2AS_C38, type code %, sha256 `ed9f68c0b96e5b34…`

~~~~text
51: PHASE FE2AS_C38 % 2 2 1 !
52: CONST FE2AS_C38 : FE : AS : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): FE2AS_C38, type code %, sha256 `24c905685b77bd98…`

~~~~text
53: PHASE FE2AS_C38 % 2 2 1 !
54: CONST FE2AS_C38 : FE : AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## FE3AS2 (As–Fe)

- Id: `phase:as-fe:fe3as2`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Fe3As2) — Hallstedt 2025 mmc2 row for FE3AS2: Fe3As2
- Stability: stable in 2 of 2 calculated diagram(s): 1096.12–1249.91 K, x(As) 0.39708–0.42149
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:fe3as2)

Names (3): _corpus: _corpus:phase:as-fe:fe3as2  
_tdb: _tdb:FeAs-08Ohn.tdb:FE3AS2, tdb:FeAs-94Pei-LB.tdb:FE3AS2  


### TDB models of FE3AS2 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): FE3AS2, type code %, sha256 `ed9f68c0b96e5b34…`

~~~~text
56: PHASE FE3AS2 % 2 1 0.75 !
57: CONST FE3AS2 : FE : AS VA : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): FE3AS2, type code %, sha256 `24c905685b77bd98…`

~~~~text
58: PHASE FE3AS2 % 2 1 0.75 !
59: CONST FE3AS2 : FE : AS VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## FEAS_B31 (As–Fe)

- Id: `phase:as-fe:feas-b31`; status `assigned`
- Structure: MnP · B31 · oP8 · Pnma (62); type `st:b31-mnp-op8`; tier A: standard phase name; confidence high
- Stoichiometry: As 0.5000, Fe 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1315.16 K, x(As) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:feas-b31)

Names (3): _corpus: _corpus:phase:as-fe:feas-b31  
_tdb: _tdb:FeAs-08Ohn.tdb:FEAS_B31, tdb:FeAs-94Pei-LB.tdb:FEAS_B31  


### TDB models of FEAS_B31 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): FEAS_B31, type code %, sha256 `ed9f68c0b96e5b34…`

~~~~text
61: PHASE FEAS_B31 % 2 1 1 !
62: CONST FEAS_B31 : FE : AS : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): FEAS_B31, type code %, sha256 `24c905685b77bd98…`

~~~~text
63: PHASE FEAS_B31 % 2 1 1 !
64: CONST FEAS_B31 : FE : AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## FEAS2_C18 (As–Fe)

- Id: `phase:as-fe:feas2-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Stoichiometry: As 0.6667, Fe 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1293.72 K, x(As) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:feas2-c18)

Names (3): _corpus: _corpus:phase:as-fe:feas2-c18  
_tdb: _tdb:FeAs-08Ohn.tdb:FEAS2_C18, tdb:FeAs-94Pei-LB.tdb:FEAS2_C18  


### TDB models of FEAS2_C18 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): FEAS2_C18, type code %, sha256 `ed9f68c0b96e5b34…`

~~~~text
66: PHASE FEAS2_C18 % 2 1 2 !
67: CONST FEAS2_C18 : FE : AS : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): FEAS2_C18, type code %, sha256 `24c905685b77bd98…`

~~~~text
68: PHASE FEAS2_C18 % 2 1 2 !
69: CONST FEAS2_C18 : FE : AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## HCP_A3 (As–Fe)

- Id: `phase:as-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:hcp-a3)

Names (3): _corpus: _corpus:phase:as-fe:hcp-a3  
_tdb: _tdb:FeAs-08Ohn.tdb:HCP_A3, tdb:FeAs-94Pei-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): HCP_A3, type code %A, sha256 `ed9f68c0b96e5b34…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AS FE : VA : !
~~~~

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): HCP_A3, type code %A, sha256 `24c905685b77bd98…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AS FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## ION (As–Fe)

- Id: `phase:as-fe:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1077.52–2500 K, x(As) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:ion)

Names (2): _corpus: _corpus:phase:as-fe:ion  
_tdb: _tdb:FeAs-94Pei-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[FeAs-94Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-94Pei-LB.tdb): ION, type code %, sha256 `24c905685b77bd98…`

~~~~text
28: PHASE ION:Y % 2 1 1 !
29: CONST ION:Y : FE+2 : AS-3 AS VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1994-850304](https://doi.org/10.1515/ijmr-1994-850304) B. Pei, B. Bjoerkman, B. Jansson, B. Sundman, Z. Metallkd., 85, 171-77(1994).  
_assessment that models this phase_

## LIQUID (As–Fe)

- Id: `phase:as-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1075.45–2500 K, x(As) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-fe:liquid)

Names (2): _corpus: _corpus:phase:as-fe:liquid  
_tdb: _tdb:FeAs-08Ohn.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[FeAs-08Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeAs-08Ohn.tdb): LIQUID, type code %, sha256 `ed9f68c0b96e5b34…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AS FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jcrysgro.2008.02.017](https://doi.org/10.1016/j.jcrysgro.2008.02.017) Munekazu Ohno, Kanji Yoh, Thermodynamic modeling of the system As–Fe combined with first-principles total energy calculations, Journal of Crystal Growth 310, 2751-2759 (2008).  
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
