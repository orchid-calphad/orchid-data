# Sb–Se phases

> Sb–Se system: 8 phases (tier A 6, liquid 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SB-SE.html · Markdown: https://data.orchid-project.org/phases/pages/SB-SE.md

8 phases (tier A 6, liquid 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SB-SE) · [full JSON](https://data.orchid-project.org/phases/systems/SB-SE.json) · [Sb–Se system page](https://data.orchid-project.org/systems/SB-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/SB-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sb–Se system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-sb-se-a7-rhombohedral); _phase:sb-se:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Se) 0–0 | 0 | 3 |
| [HEXAGONAL_A8](#phase-sb-se-a8-hexagonal); _phase:sb-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–494 K, x(Se) 1–1 | 0 | 3 |
| [BCC_A2](#phase-sb-se-bcc-a2); _phase:sb-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-sb-se-fcc-a1); _phase:sb-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-sb-se-hcp-a3); _phase:sb-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ION](#phase-sb-se-ion); _phase:sb-se:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 486.45–2500 K, x(Se) 0–1 | 0 | 1 |
| [LIQUID](#phase-sb-se-liquid); _phase:sb-se:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 493.18–2500 K, x(Se) 0–1 | 0 | 3 |
| [SB2SE3_D58](#phase-sb-se-sb2se3-d58); _phase:sb-se:sb2se3-d58_ | Sb2S3 · D5_8 · oP20 · Pnma (62) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–893.15 K, x(Se) 0.6–0.6 | 0 | 3 |

## RHOMBOHEDRAL_A7 (Sb–Se)

- Id: `phase:sb-se:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Se) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:sb-se:a7-rhombohedral  
_tdb: _tdb:SbSe-21Gie.tdb:RHOMBOHEDRAL_A7, tdb:SbSe-23Liu.tdb:RHOMBOHEDRAL_A7, tdb:SbSe-89Gho.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[SbSe-21Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-21Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9ada23085074f680…`

~~~~text
52: PHASE RHOMBOHEDRAL_A7 % 1 1 !
53: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[SbSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-23Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `482b80658bf0ab4a…`

~~~~text
53: PHASE RHOMBOHEDRAL_A7 % 1 1 !
54: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `3d9847ebb3a99376…`

~~~~text
56: PHASE RHOMBOHEDRAL_A7 % 1 1 !
57: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102257](https://doi.org/10.1016/j.calphad.2021.102257) W. Gierlotka, I. Lin, S. Chen, W. Gasior, A. Debski, Calphad, 73, 102257(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
_assessment that models this phase_

## HEXAGONAL_A8 (Sb–Se)

- Id: `phase:sb-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:a8-hexagonal)

Names (4): _corpus: _corpus:phase:sb-se:a8-hexagonal  
_tdb: _tdb:SbSe-21Gie.tdb:HEXAGONAL_A8, tdb:SbSe-23Liu.tdb:HEXAGONAL_A8, tdb:SbSe-89Gho.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (3): PHASE and CONSTITUENT statements as written

[SbSe-21Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-21Gie.tdb): HEXAGONAL_A8, type code %, sha256 `9ada23085074f680…`

~~~~text
57: PHASE HEXAGONAL_A8 % 1 1 !
58: CONST HEXAGONAL_A8 : SE : !
~~~~

[SbSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-23Liu.tdb): HEXAGONAL_A8, type code %, sha256 `482b80658bf0ab4a…`

~~~~text
58: PHASE HEXAGONAL_A8 % 1 1 !
59: CONST HEXAGONAL_A8 : SE : !
~~~~

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): HEXAGONAL_A8, type code %, sha256 `3d9847ebb3a99376…`

~~~~text
61: PHASE HEXAGONAL_A8 % 1 1 !
62: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102257](https://doi.org/10.1016/j.calphad.2021.102257) W. Gierlotka, I. Lin, S. Chen, W. Gasior, A. Debski, Calphad, 73, 102257(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
_assessment that models this phase_

## BCC_A2 (Sb–Se)

- Id: `phase:sb-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:bcc-a2)

Names (4): _corpus: _corpus:phase:sb-se:bcc-a2  
_tdb: _tdb:SbSe-21Gie.tdb:BCC_A2, tdb:SbSe-23Liu.tdb:BCC_A2, tdb:SbSe-89Gho.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[SbSe-21Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-21Gie.tdb): BCC_A2, type code %B, sha256 `9ada23085074f680…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : SB : VA : !
~~~~

[SbSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-23Liu.tdb): BCC_A2, type code %B, sha256 `482b80658bf0ab4a…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : SB : VA : !
~~~~

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): BCC_A2, type code %B, sha256 `3d9847ebb3a99376…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102257](https://doi.org/10.1016/j.calphad.2021.102257) W. Gierlotka, I. Lin, S. Chen, W. Gasior, A. Debski, Calphad, 73, 102257(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
_assessment that models this phase_

## FCC_A1 (Sb–Se)

- Id: `phase:sb-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:fcc-a1)

Names (4): _corpus: _corpus:phase:sb-se:fcc-a1  
_tdb: _tdb:SbSe-21Gie.tdb:FCC_A1, tdb:SbSe-23Liu.tdb:FCC_A1, tdb:SbSe-89Gho.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[SbSe-21Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-21Gie.tdb): FCC_A1, type code %A, sha256 `9ada23085074f680…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : SB : VA : !
~~~~

[SbSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-23Liu.tdb): FCC_A1, type code %A, sha256 `482b80658bf0ab4a…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : SB : VA : !
~~~~

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): FCC_A1, type code %A, sha256 `3d9847ebb3a99376…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102257](https://doi.org/10.1016/j.calphad.2021.102257) W. Gierlotka, I. Lin, S. Chen, W. Gasior, A. Debski, Calphad, 73, 102257(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
_assessment that models this phase_

## HCP_A3 (Sb–Se)

- Id: `phase:sb-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:hcp-a3)

Names (4): _corpus: _corpus:phase:sb-se:hcp-a3  
_tdb: _tdb:SbSe-21Gie.tdb:HCP_A3, tdb:SbSe-23Liu.tdb:HCP_A3, tdb:SbSe-89Gho.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[SbSe-21Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-21Gie.tdb): HCP_A3, type code %A, sha256 `9ada23085074f680…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : SB : VA: !
~~~~

[SbSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-23Liu.tdb): HCP_A3, type code %A, sha256 `482b80658bf0ab4a…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : SB : VA: !
~~~~

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): HCP_A3, type code %A, sha256 `3d9847ebb3a99376…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : SB : VA: !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102257](https://doi.org/10.1016/j.calphad.2021.102257) W. Gierlotka, I. Lin, S. Chen, W. Gasior, A. Debski, Calphad, 73, 102257(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
_assessment that models this phase_

## ION (Sb–Se)

- Id: `phase:sb-se:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 486.45–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:ion)

Names (2): _corpus: _corpus:phase:sb-se:ion  
_tdb: _tdb:SbSe-89Gho.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): ION, type code %, sha256 `3d9847ebb3a99376…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : SB+3 : SE-2 VA SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
_assessment that models this phase_

## LIQUID (Sb–Se)

- Id: `phase:sb-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 493.18–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:liquid)

Names (4): _corpus: _corpus:phase:sb-se:liquid  
_tdb: _tdb:SbSe-21Gie.tdb:LIQUID, tdb:SbSe-23Liu.tdb:LIQUID, tdb:SbSe-89Gho.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[SbSe-21Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-21Gie.tdb): LIQUID, type code %, sha256 `9ada23085074f680…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : SB SB2SE3 SE : !
~~~~

[SbSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-23Liu.tdb): LIQUID, type code %, sha256 `482b80658bf0ab4a…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : SB SB2SE3 SE : !
~~~~

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): LIQUID, type code %, sha256 `3d9847ebb3a99376…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : SB SB2SE3 SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102257](https://doi.org/10.1016/j.calphad.2021.102257) W. Gierlotka, I. Lin, S. Chen, W. Gasior, A. Debski, Calphad, 73, 102257(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
_assessment that models this phase_

## SB2SE3_D58 (Sb–Se)

- Id: `phase:sb-se:sb2se3-d58`; status `assigned`
- Structure: Sb2S3 · D5_8 · oP20 · Pnma (62); type `st:d5-8-sb2s3-op20`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.4000, Se 0.6000
- Stability: stable in 3 of 3 calculated diagram(s): 300–893.15 K, x(Se) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-se:sb2se3-d58)

Names (4): _corpus: _corpus:phase:sb-se:sb2se3-d58  
_tdb: _tdb:SbSe-21Gie.tdb:SB2SE3_D58, tdb:SbSe-23Liu.tdb:SB2SE3_D58, tdb:SbSe-89Gho.tdb:SB2SE3_D58  


### TDB models of SB2SE3_D58 (3): PHASE and CONSTITUENT statements as written

[SbSe-21Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-21Gie.tdb): SB2SE3_D58, type code %, sha256 `9ada23085074f680…`

~~~~text
62: PHASE SB2SE3_D58 % 2 2 3 !
63: CONST SB2SE3_D58 : SB : SE : !
~~~~

[SbSe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-23Liu.tdb): SB2SE3_D58, type code %, sha256 `482b80658bf0ab4a…`

~~~~text
63: PHASE SB2SE3_D58 % 2 2 3 !
64: CONST SB2SE3_D58 : SB : SE : !
~~~~

[SbSe-89Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSe-89Gho.tdb): SB2SE3_D58, type code %, sha256 `3d9847ebb3a99376…`

~~~~text
66: PHASE SB2SE3_D58 % 2 2 3 !
67: CONST SB2SE3_D58 : SB : SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102257](https://doi.org/10.1016/j.calphad.2021.102257) W. Gierlotka, I. Lin, S. Chen, W. Gasior, A. Debski, Calphad, 73, 102257(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1989-800911](https://doi.org/10.1515/ijmr-1989-800911) G. Ghosh, H.L. Lukas, L. Delaey, Z. Metallkd., 80, 663-68(1989).  
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
