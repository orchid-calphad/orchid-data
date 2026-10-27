# Cr–O phases

> Cr–O system: 11 phases (tier A 6, tier C 1, liquid 2, gas 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-O.html · Markdown: https://data.orchid-project.org/phases/pages/CR-O.md

11 phases (tier A 6, tier C 1, liquid 2, gas 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-O) · [full JSON](https://data.orchid-project.org/phases/systems/CR-O.json) · [Cr–O system page](https://data.orchid-project.org/systems/CR-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–O system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-o-bcc-a2); _phase:cr-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2179.98 K, x(O) 0–0.00078 | 0 | 3 |
| [CR2O3_D51](#phase-cr-o-cr2o3-d51); _phase:cr-o:cr2o3-d51_ | alpha-Al2O3 · D5_1 · hR10 · R-3c (167) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2583.7 K, x(O) 0.59163–0.6 | 0 | 3 |
| [CR3O4_H11](#phase-cr-o-cr3o4-h11); _phase:cr-o:cr3o4-h11_ | Al2MgO4 · H1_1 · cF56 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1917.97–1973.2 K, x(O) 0.57143–0.57143 | 0 | 2 |
| [CRO_B1](#phase-cr-o-cro-b1); _phase:cr-o:cro-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-cr-o-fcc-a1); _phase:cr-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-cr-o-gas); _phase:cr-o:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300.1–3913.79 K, x(O) 0–1 | 0 | 3 |
| [SPINEL_H11](#phase-cr-o-h11-spinel); _phase:cr-o:h11-spinel_ | Al2MgO4 · H1_1 · cF56 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cr-o-hcp-a3); _phase:cr-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ION](#phase-cr-o-ion); _phase:cr-o:ion_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1911.97–3913.79 K, x(O) 0–0.6 | 0 | 3 |
| [LIQUID](#phase-cr-o-liquid); _phase:cr-o:liquid_ | liquid | liquid | not stable in 3 calculated diagram(s) | 2 | 3 |
| [O2GAS](#phase-cr-o-o2gas); _phase:cr-o:o2gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300–1115 K, x(O) 1–1 | 0 | 3 |

## BCC_A2 (Cr–O)

- Id: `phase:cr-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2179.98 K, x(O) 0–0.00078
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:bcc-a2)

Names (4): _corpus: _corpus:phase:cr-o:bcc-a2  
_tdb: _tdb:CrO-06Pov.tdb:BCC_A2, tdb:CrO-10Kje.tdb:BCC_A2, tdb:CrO-90Tay.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): BCC_A2, type code %B, sha256 `91b2e0d80ba0b62e…`

~~~~text
58: PHASE BCC_A2 %B 2 1 3 !
59: CONST BCC_A2 : CR : O VA% : !
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): BCC_A2, type code %B, sha256 `ee031ab4eb31aac1…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : CR : O VA : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): BCC_A2, type code %B, sha256 `d075f681078353be…`

~~~~text
55: PHASE BCC_A2 %B 2 1 3 !
56: CONST BCC_A2 : CR : O VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## CR2O3_D51 (Cr–O)

- Id: `phase:cr-o:cr2o3-d51`; status `assigned`
- Structure: alpha-Al2O3 · D5_1 · hR10 · R-3c (167); type `st:d5-1-alpha-al2o3-hr10`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2583.7 K, x(O) 0.59163–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:cr2o3-d51)

Names (4): _corpus: _corpus:phase:cr-o:cr2o3-d51  
_tdb: _tdb:CrO-06Pov.tdb:CR2O3_D51, tdb:CrO-10Kje.tdb:CR2O3_D51, tdb:CrO-90Tay.tdb:CR2O3_D51  


### TDB models of CR2O3_D51 (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): CR2O3_D51, type code %, sha256 `91b2e0d80ba0b62e…`

~~~~text
78: PHASE CR2O3_D51:I % 3 2 1 3 !
79: CONST CR2O3_D51:I : CR+2 CR+3% : CR+3 VA% : O-2 : !
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): CR2O3_D51, type code %A, sha256 `ee031ab4eb31aac1…`

~~~~text
60: PHASE CR2O3_D51:I %A 3 2 1 3 !
61: CONST CR2O3_D51:I : CR+2 CR+3% : CR+3 VA% : O-2 : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): CR2O3_D51, type code %A, sha256 `d075f681078353be…`

~~~~text
65: PHASE CR2O3_D51:I %A 3 2 1 3 !
66: CONST CR2O3_D51:I : CR+2 CR+3% : CR+3 VA% : O-2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## CR3O4_H11 (Cr–O)

- Id: `phase:cr-o:cr3o4-h11`; status `assigned`
- Structure: Al2MgO4 · H1_1 · cF56 · Fd-3m (227); type `st:h1-1-al2mgo4-cf56`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1917.97–1973.2 K, x(O) 0.57143–0.57143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:cr3o4-h11)

Names (3): _corpus: _corpus:phase:cr-o:cr3o4-h11  
_tdb: _tdb:CrO-06Pov.tdb:CR3O4_H11, tdb:CrO-90Tay.tdb:CR3O4_H11  


### TDB models of CR3O4_H11 (2): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): CR3O4_H11, type code %, sha256 `91b2e0d80ba0b62e…`

~~~~text
73: PHASE CR3O4_H11:I % 3 1 2 4 !
74: CONST CR3O4_H11:I : CR+2 : CR+3 : O-2 : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): CR3O4_H11, type code %, sha256 `d075f681078353be…`

~~~~text
70: PHASE CR3O4_H11:I % 3 2 1 4 !
71: CONST CR3O4_H11:I : CR+3 : CR+2 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## CRO_B1 (Cr–O)

- Id: `phase:cr-o:cro-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:cro-b1)

Names (2): _corpus: _corpus:phase:cr-o:cro-b1  
_tdb: _tdb:CrO-06Pov.tdb:CRO_B1  


### TDB models of CRO_B1 (1): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): CRO_B1, type code %, sha256 `91b2e0d80ba0b62e…`

~~~~text
68: PHASE CRO_B1:I % 2 1 1 !
69: CONST CRO_B1:I : CR+2 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_

## FCC_A1 (Cr–O)

- Id: `phase:cr-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cr 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:fcc-a1)

Names (4): _corpus: _corpus:phase:cr-o:fcc-a1  
_tdb: _tdb:CrO-06Pov.tdb:FCC_A1, tdb:CrO-10Kje.tdb:FCC_A1, tdb:CrO-90Tay.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): FCC_A1, type code %A, sha256 `91b2e0d80ba0b62e…`

~~~~text
53: PHASE FCC_A1 %A 2 1 1 !
54: CONST FCC_A1 : CR : VA : !
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): FCC_A1, type code %A, sha256 `ee031ab4eb31aac1…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : CR : VA : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): FCC_A1, type code %A, sha256 `d075f681078353be…`

~~~~text
50: PHASE FCC_A1 %A 2 1 1 !
51: CONST FCC_A1 : CR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## GAS (Cr–O)

- Id: `phase:cr-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300.1–3913.79 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:gas)

Names (4): _corpus: _corpus:phase:cr-o:gas  
_tdb: _tdb:CrO-06Pov.tdb:GAS, tdb:CrO-10Kje.tdb:GAS, tdb:CrO-90Tay.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): GAS, type code %, sha256 `91b2e0d80ba0b62e…`

~~~~text
84: PHASE GAS:G % 1 1 !
85: CONST GAS:G : CR CR2 CR2O CRO CR2O2 CR2O3 CRO2 CRO3 O O2 O3 : !
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): GAS, type code %, sha256 `ee031ab4eb31aac1…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : CR CR2 CR2O CRO CR2O2 CR2O3 CRO2 CRO3 O O2 O3 : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): GAS, type code %, sha256 `d075f681078353be…`

~~~~text
76: PHASE GAS:G % 1 1 !
77: CONST GAS:G : CR CR2 CR2O CRO CR2O2 CR2O3 CRO2 CRO3 O O2 O3 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## SPINEL_H11 (Cr–O)

- Id: `phase:cr-o:h11-spinel`; status `assigned`
- Structure: Al2MgO4 · H1_1 · cF56 · Fd-3m (227); type `st:h1-1-al2mgo4-cf56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:SPINEL); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:h11-spinel)

Names (2): _corpus: _corpus:phase:cr-o:h11-spinel  
_tdb: _tdb:CrO-10Kje.tdb:SPINEL_H11  


### TDB models of SPINEL_H11 (1): PHASE and CONSTITUENT statements as written

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): SPINEL_H11, type code %A, sha256 `ee031ab4eb31aac1…`

~~~~text
67: PHASE SPINEL_H11:I %A 4 1 2 2 4 !
68: CONST SPINEL_H11:I : CR+2 CR+3 : CR+3 VA : CR+2 VA : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_

## HCP_A3 (Cr–O)

- Id: `phase:cr-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cr 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:hcp-a3)

Names (4): _corpus: _corpus:phase:cr-o:hcp-a3  
_tdb: _tdb:CrO-06Pov.tdb:HCP_A3, tdb:CrO-10Kje.tdb:HCP_A3, tdb:CrO-90Tay.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): HCP_A3, type code %A, sha256 `91b2e0d80ba0b62e…`

~~~~text
63: PHASE HCP_A3 %A 2 1 0.5 !
64: CONST HCP_A3 : CR : VA : !
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): HCP_A3, type code %A, sha256 `ee031ab4eb31aac1…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : CR : VA : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): HCP_A3, type code %A, sha256 `d075f681078353be…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : CR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## ION (Cr–O)

- Id: `phase:cr-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1911.97–3913.79 K, x(O) 0–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:ion)

Names (4): _corpus: _corpus:phase:cr-o:ion  
_tdb: _tdb:CrO-06Pov.tdb:ION, tdb:CrO-10Kje.tdb:ION, tdb:CrO-90Tay.tdb:ION  


### TDB models of ION (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): ION, type code %, sha256 `91b2e0d80ba0b62e…`

~~~~text
48: PHASE ION:Y % 2 1 1 !
49: CONST ION:Y : CR+2 CR+3 : O-2 VA : !
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): ION, type code %, sha256 `ee031ab4eb31aac1…`

~~~~text
40: PHASE ION:Y % 2 1 1 !
41: CONST ION:Y : CR+2 : O-2 VA CRO1.5 : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): ION, type code %, sha256 `d075f681078353be…`

~~~~text
45: PHASE ION:Y % 2 1 1 !
46: CONST ION:Y : CR+3 : O-2 VA O : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## LIQUID (Cr–O)

- Id: `phase:cr-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Cr 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:liquid)

Names (5): _corpus: _corpus:phase:cr-o:liquid  
_paper: _paper:10.1361/154770306x116289:liquid  
_tdb: _tdb:CrO-06Pov.tdb:LIQUID, tdb:CrO-10Kje.tdb:LIQUID, tdb:CrO-90Tay.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): LIQUID, type code %, sha256 `91b2e0d80ba0b62e…`

~~~~text
45: PHASE LIQUID:L % 1 1 !
46: CONST LIQUID:L : CR : !
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): LIQUID, type code %, sha256 `ee031ab4eb31aac1…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : CR : !
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): LIQUID, type code %, sha256 `d075f681078353be…`

~~~~text
42: PHASE LIQUID:L % 1 1 !
43: CONST LIQUID:L : CR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## O2GAS (Cr–O)

- Id: `phase:cr-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1115 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-o:o2gas)

Names (4): _corpus: _corpus:phase:cr-o:o2gas  
_tdb: _tdb:CrO-06Pov.tdb:O2GAS, tdb:CrO-10Kje.tdb:O2GAS, tdb:CrO-90Tay.tdb:O2GAS  


### TDB models of O2GAS (3): PHASE and CONSTITUENT statements as written

[CrO-06Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-06Pov.tdb): O2GAS, type code %, sha256 `91b2e0d80ba0b62e…`

~~~~text
81: PHASE O2GAS % 1 1 !
82: CONST O2GAS : O2 :!
~~~~

[CrO-10Kje.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-10Kje.tdb): O2GAS, type code %, sha256 `ee031ab4eb31aac1…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 :!
~~~~

[CrO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/CrO-90Tay.tdb): O2GAS, type code %, sha256 `d075f681078353be…`

~~~~text
73: PHASE O2GAS % 1 1 !
74: CONST O2GAS : O2 :!
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.04.252](https://doi.org/10.1016/j.jallcom.2010.04.252) Lina Kjellqvist, Malin Selleby, Thermodynamic assessment of the Cr–Mn–O system, Journal of Alloys and Compounds 507, 84-92 (2010).  
_assessment that models this phase_
- [doi:10.1361/154770306X116289](https://doi.org/10.1361/154770306X116289) E. Povoden, A.N. Grundy, L.J. Gauckler, J. Phase Equilib. Diffus., 27, 353-62(2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
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
