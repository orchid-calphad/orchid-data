# Pb–Te phases

> Pb–Te system: 7 phases (tier A 5, liquid 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-TE.html · Markdown: https://data.orchid-project.org/phases/pages/PB-TE.md

7 phases (tier A 5, liquid 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-TE) · [full JSON](https://data.orchid-project.org/phases/systems/PB-TE.json) · [Pb–Te system page](https://data.orchid-project.org/systems/PB-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Te system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-pb-te-a8-hexagonal); _phase:pb-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 8 | 5 |
| [BCC_A2](#phase-pb-te-bcc-a2); _phase:pb-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-pb-te-fcc-a1); _phase:pb-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–667.36 K, x(Te) 0–0 | 4 | 5 |
| [HCP_A3](#phase-pb-te-hcp-a3); _phase:pb-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [ION](#phase-pb-te-ion); _phase:pb-te:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 600.06–2500 K, x(Te) 0–1 | 1 | 1 |
| [LIQUID](#phase-pb-te-liquid); _phase:pb-te:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 599.8–2500 K, x(Te) 0–1 | 17 | 4 |
| [PBTE_B1](#phase-pb-te-pbte-b1); _phase:pb-te:pbte-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1213.89 K, x(Te) 0.49994–0.50024 | 31 | 5 |

## HEXAGONAL_A8 (Pb–Te)

- Id: `phase:pb-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 8 values (8 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-te:a8-hexagonal)

Names (10): _corpus: _corpus:phase:pb-te:a8-hexagonal, corpus:phase:pb-te:hexagonal-a8  
_paper: _paper:10.1007/s11664-009-0875-3:hex, paper:10.1016/0364-5916(86)90015-5:(Te), paper:10.1016/j.jallcom.2008.12.083:HEXAGONAL_A8  
_tdb: _tdb:PbTe-09Gie.tdb:HEXAGONAL_A8, tdb:PbTe-09Liu.tdb:HEXAGONAL_A8, tdb:PbTe-10Gie.tdb:HEXAGONAL_A8, tdb:PbTe-15Baj.tdb:HEXAGONAL_A8, tdb:PbTe-86Kat.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (5): PHASE and CONSTITUENT statements as written

[PbTe-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Gie.tdb): HEXAGONAL_A8, type code %, sha256 `1d05106b6376c8f0…`

~~~~text
51: PHASE HEXAGONAL_A8 % 1 1 !
52: CONST HEXAGONAL_A8 : TE : !
~~~~

[PbTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Liu.tdb): HEXAGONAL_A8, type code %, sha256 `edccadcbcc684b2c…`

~~~~text
48: PHASE HEXAGONAL_A8 % 1 1 !
49: CONST HEXAGONAL_A8 : TE : !
~~~~

[PbTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-10Gie.tdb): HEXAGONAL_A8, type code %, sha256 `ffb7d7dfb04a30b6…`

~~~~text
48: PHASE HEXAGONAL_A8 % 1 1 !
49: CONST HEXAGONAL_A8 : TE : !
~~~~

[PbTe-15Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-15Baj.tdb): HEXAGONAL_A8, type code %, sha256 `e1bad0890740970f…`

~~~~text
49: PHASE HEXAGONAL_A8 % 1 1 !
50: CONST HEXAGONAL_A8 : TE : !
~~~~

[PbTe-86Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-86Kat.tdb): HEXAGONAL_A8, type code %, sha256 `c309772d299befd6…`

~~~~text
52: PHASE HEXAGONAL_A8 % 1 1 !
53: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(86)90015-5](https://doi.org/10.1016/0364-5916%2886%2990015-5) U. Kattner, H.L. Lukas, G. Petzow, Optimization and calculation of the PB — TE system, Calphad 10, 103-116 (1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.12.083](https://doi.org/10.1016/j.jallcom.2008.12.083) Wojciech Gierlotka, Joanna Łapsa, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Pb–Te system using ionic liquid model, Journal of Alloys and Compounds 479, 152-156 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9791-8](https://doi.org/10.1007/s11669-010-9791-8) W. Gierlotka, J. Lapsa, K. Fitzner, J. Phase Equilib. Diffus., 31, 509-17(2010).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2015.03.034](https://doi.org/10.1016/j.actamat.2015.03.034) Saurabh Bajaj, Gregory S. Pomrehn, Jeff W. Doak, Wojciech Gierlotka, Hsin-jay Wu, Sinn-Wen Chen et al., Ab initio study of intrinsic point defects in PbTe: an insight into phase stability, Acta Materialia 92, 72-80 (2015).  
_assessment that models this phase_
- [doi:10.1007/bf00809938](https://doi.org/10.1007/bf00809938) T. Leo Ngai, D. Marshall, R. C. Sharma, Y. A. Chang, Thermodynamic properties and phase equilibria of the lead-tellurium binary system, Monatsh Chem 118, 277-300 (1987).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1965-561207](https://doi.org/10.1515/ijmr-1965-561207) Walter Lugscheider, Horst Ebel, Gerhard Langer, Thermoanalytische und röntgenographische Untersuchungen im System Blei-Tellur, International Journal of Materials Research 56, 851-852 (1965).  
_cited as the source of values for this phase_

## BCC_A2 (Pb–Te)

- Id: `phase:pb-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-te:bcc-a2)

Names (6): _corpus: _corpus:phase:pb-te:bcc-a2  
_tdb: _tdb:PbTe-09Gie.tdb:BCC_A2, tdb:PbTe-09Liu.tdb:BCC_A2, tdb:PbTe-10Gie.tdb:BCC_A2, tdb:PbTe-15Baj.tdb:BCC_A2, tdb:PbTe-86Kat.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[PbTe-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Gie.tdb): BCC_A2, type code %B, sha256 `1d05106b6376c8f0…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : PB : VA : !
~~~~

[PbTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Liu.tdb): BCC_A2, type code %B, sha256 `edccadcbcc684b2c…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PB : VA : !
~~~~

[PbTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-10Gie.tdb): BCC_A2, type code %B, sha256 `ffb7d7dfb04a30b6…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PB : VA : !
~~~~

[PbTe-15Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-15Baj.tdb): BCC_A2, type code %B, sha256 `e1bad0890740970f…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : PB : VA : !
~~~~

[PbTe-86Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-86Kat.tdb): BCC_A2, type code %B, sha256 `c309772d299befd6…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : PB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11669-010-9791-8](https://doi.org/10.1007/s11669-010-9791-8) W. Gierlotka, J. Lapsa, K. Fitzner, J. Phase Equilib. Diffus., 31, 509-17(2010).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(86)90015-5](https://doi.org/10.1016/0364-5916%2886%2990015-5) U. Kattner, H.L. Lukas, G. Petzow, Optimization and calculation of the PB — TE system, Calphad 10, 103-116 (1986).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2015.03.034](https://doi.org/10.1016/j.actamat.2015.03.034) Saurabh Bajaj, Gregory S. Pomrehn, Jeff W. Doak, Wojciech Gierlotka, Hsin-jay Wu, Sinn-Wen Chen et al., Ab initio study of intrinsic point defects in PbTe: an insight into phase stability, Acta Materialia 92, 72-80 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.12.083](https://doi.org/10.1016/j.jallcom.2008.12.083) Wojciech Gierlotka, Joanna Łapsa, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Pb–Te system using ionic liquid model, Journal of Alloys and Compounds 479, 152-156 (2009).  
_assessment that models this phase_

## FCC_A1 (Pb–Te)

- Id: `phase:pb-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–667.36 K, x(Te) 0–0
- Literature: 4 values (4 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-te:fcc-a1)

Names (9): _corpus: _corpus:phase:pb-te:fcc-a1  
_paper: _paper:10.1007/s11664-009-0875-3:Pb, paper:10.1016/0364-5916(86)90015-5:(Pb), paper:10.1016/j.jallcom.2008.12.083:FCC_A1  
_tdb: _tdb:PbTe-09Gie.tdb:FCC_A1, tdb:PbTe-09Liu.tdb:FCC_A1, tdb:PbTe-10Gie.tdb:FCC_A1, tdb:PbTe-15Baj.tdb:FCC_A1, tdb:PbTe-86Kat.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[PbTe-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Gie.tdb): FCC_A1, type code %A, sha256 `1d05106b6376c8f0…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : PB : VA : !
~~~~

[PbTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Liu.tdb): FCC_A1, type code %A, sha256 `edccadcbcc684b2c…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PB : VA : !
~~~~

[PbTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-10Gie.tdb): FCC_A1, type code %A, sha256 `ffb7d7dfb04a30b6…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PB : VA : !
~~~~

[PbTe-15Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-15Baj.tdb): FCC_A1, type code %A, sha256 `e1bad0890740970f…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : PB : VA : !
~~~~

[PbTe-86Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-86Kat.tdb): FCC_A1, type code %A, sha256 `c309772d299befd6…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : PB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(86)90015-5](https://doi.org/10.1016/0364-5916%2886%2990015-5) U. Kattner, H.L. Lukas, G. Petzow, Optimization and calculation of the PB — TE system, Calphad 10, 103-116 (1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.12.083](https://doi.org/10.1016/j.jallcom.2008.12.083) Wojciech Gierlotka, Joanna Łapsa, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Pb–Te system using ionic liquid model, Journal of Alloys and Compounds 479, 152-156 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9791-8](https://doi.org/10.1007/s11669-010-9791-8) W. Gierlotka, J. Lapsa, K. Fitzner, J. Phase Equilib. Diffus., 31, 509-17(2010).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2015.03.034](https://doi.org/10.1016/j.actamat.2015.03.034) Saurabh Bajaj, Gregory S. Pomrehn, Jeff W. Doak, Wojciech Gierlotka, Hsin-jay Wu, Sinn-Wen Chen et al., Ab initio study of intrinsic point defects in PbTe: an insight into phase stability, Acta Materialia 92, 72-80 (2015).  
_assessment that models this phase_

## HCP_A3 (Pb–Te)

- Id: `phase:pb-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-te:hcp-a3)

Names (6): _corpus: _corpus:phase:pb-te:hcp-a3  
_tdb: _tdb:PbTe-09Gie.tdb:HCP_A3, tdb:PbTe-09Liu.tdb:HCP_A3, tdb:PbTe-10Gie.tdb:HCP_A3, tdb:PbTe-15Baj.tdb:HCP_A3, tdb:PbTe-86Kat.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[PbTe-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Gie.tdb): HCP_A3, type code %A, sha256 `1d05106b6376c8f0…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : PB : VA: !
~~~~

[PbTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Liu.tdb): HCP_A3, type code %A, sha256 `edccadcbcc684b2c…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PB : VA: !
~~~~

[PbTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-10Gie.tdb): HCP_A3, type code %A, sha256 `ffb7d7dfb04a30b6…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PB : VA: !
~~~~

[PbTe-15Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-15Baj.tdb): HCP_A3, type code %A, sha256 `e1bad0890740970f…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : PB : VA: !
~~~~

[PbTe-86Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-86Kat.tdb): HCP_A3, type code %A, sha256 `c309772d299befd6…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : PB : VA: !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11669-010-9791-8](https://doi.org/10.1007/s11669-010-9791-8) W. Gierlotka, J. Lapsa, K. Fitzner, J. Phase Equilib. Diffus., 31, 509-17(2010).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(86)90015-5](https://doi.org/10.1016/0364-5916%2886%2990015-5) U. Kattner, H.L. Lukas, G. Petzow, Optimization and calculation of the PB — TE system, Calphad 10, 103-116 (1986).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2015.03.034](https://doi.org/10.1016/j.actamat.2015.03.034) Saurabh Bajaj, Gregory S. Pomrehn, Jeff W. Doak, Wojciech Gierlotka, Hsin-jay Wu, Sinn-Wen Chen et al., Ab initio study of intrinsic point defects in PbTe: an insight into phase stability, Acta Materialia 92, 72-80 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.12.083](https://doi.org/10.1016/j.jallcom.2008.12.083) Wojciech Gierlotka, Joanna Łapsa, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Pb–Te system using ionic liquid model, Journal of Alloys and Compounds 479, 152-156 (2009).  
_assessment that models this phase_

## ION (Pb–Te)

- Id: `phase:pb-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 600.06–2500 K, x(Te) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-te:ion)

Names (3): _corpus: _corpus:phase:pb-te:ion  
_paper: _paper:10.1016/j.jallcom.2008.12.083:L  
_tdb: _tdb:PbTe-09Gie.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[PbTe-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Gie.tdb): ION, type code %, sha256 `1d05106b6376c8f0…`

~~~~text
31: PHASE ION:Y % 2 1 1 !
32: CONST ION:Y : PB+2 : TE-2 VA TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.12.083](https://doi.org/10.1016/j.jallcom.2008.12.083) Wojciech Gierlotka, Joanna Łapsa, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Pb–Te system using ionic liquid model, Journal of Alloys and Compounds 479, 152-156 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Pb–Te)

- Id: `phase:pb-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 599.8–2500 K, x(Te) 0–1
- Literature: 17 values (17 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-te:liquid)

Names (8): _corpus: _corpus:phase:pb-te:liquid  
_paper: _paper:10.1007/s11664-009-0875-3:L, paper:10.1016/0364-5916(86)90015-5:L, paper:10.1016/j.jallcom.2008.12.083:L  
_tdb: _tdb:PbTe-09Liu.tdb:LIQUID, tdb:PbTe-10Gie.tdb:LIQUID, tdb:PbTe-15Baj.tdb:LIQUID, tdb:PbTe-86Kat.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[PbTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Liu.tdb): LIQUID, type code %, sha256 `edccadcbcc684b2c…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PB PBTE TE : !
~~~~

[PbTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-10Gie.tdb): LIQUID, type code %, sha256 `ffb7d7dfb04a30b6…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PB PBTE TE : !
~~~~

[PbTe-15Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-15Baj.tdb): LIQUID, type code %, sha256 `e1bad0890740970f…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : PB PBTE TE : !
~~~~

[PbTe-86Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-86Kat.tdb): LIQUID, type code %, sha256 `c309772d299befd6…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : PB PBTE TE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(86)90015-5](https://doi.org/10.1016/0364-5916%2886%2990015-5) U. Kattner, H.L. Lukas, G. Petzow, Optimization and calculation of the PB — TE system, Calphad 10, 103-116 (1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9791-8](https://doi.org/10.1007/s11669-010-9791-8) W. Gierlotka, J. Lapsa, K. Fitzner, J. Phase Equilib. Diffus., 31, 509-17(2010).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2015.03.034](https://doi.org/10.1016/j.actamat.2015.03.034) Saurabh Bajaj, Gregory S. Pomrehn, Jeff W. Doak, Wojciech Gierlotka, Hsin-jay Wu, Sinn-Wen Chen et al., Ab initio study of intrinsic point defects in PbTe: an insight into phase stability, Acta Materialia 92, 72-80 (2015).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1965-561207](https://doi.org/10.1515/ijmr-1965-561207) Walter Lugscheider, Horst Ebel, Gerhard Langer, Thermoanalytische und röntgenographische Untersuchungen im System Blei-Tellur, International Journal of Materials Research 56, 851-852 (1965).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00809938](https://doi.org/10.1007/bf00809938) T. Leo Ngai, D. Marshall, R. C. Sharma, Y. A. Chang, Thermodynamic properties and phase equilibria of the lead-tellurium binary system, Monatsh Chem 118, 277-300 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.12.083](https://doi.org/10.1016/j.jallcom.2008.12.083) Wojciech Gierlotka, Joanna Łapsa, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Pb–Te system using ionic liquid model, Journal of Alloys and Compounds 479, 152-156 (2009).  
_reports values for this phase_

## PBTE_B1 (Pb–Te)

- Id: `phase:pb-te:pbte-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PbTe-09Gie.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1213.89 K, x(Te) 0.49994–0.50024
- Literature: 31 values (31 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-te:pbte-b1)

Names (10): _corpus: _corpus:phase:pb-te:pbte-b1  
_paper: _paper:10.1007/s11664-009-0875-3:PbTe, paper:10.1016/0364-5916(86)90015-5:PbTe, paper:10.1016/j.actamat.2015.03.034:PbTe, paper:10.1016/j.jallcom.2008.12.083:PbTe  
_tdb: _tdb:PbTe-09Gie.tdb:PBTE_B1, tdb:PbTe-09Liu.tdb:PBTE_B1, tdb:PbTe-10Gie.tdb:PBTE_B1, tdb:PbTe-15Baj.tdb:PBTE_B1, tdb:PbTe-86Kat.tdb:PBTE_B1  


### TDB models of PBTE_B1 (5): PHASE and CONSTITUENT statements as written

[PbTe-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Gie.tdb): PBTE_B1, type code %, sha256 `1d05106b6376c8f0…`

~~~~text
56: PHASE PBTE_B1 % 2 1 1 !
57: CONST PBTE_B1 : PB% TE : PB TE% : !
~~~~

[PbTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-09Liu.tdb): PBTE_B1, type code %, sha256 `edccadcbcc684b2c…`

~~~~text
53: PHASE PBTE_B1 % 2 1 1 !
54: CONST PBTE_B1 : PB : TE : !
~~~~

[PbTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-10Gie.tdb): PBTE_B1, type code %, sha256 `ffb7d7dfb04a30b6…`

~~~~text
53: PHASE PBTE_B1 % 2 1 1 !
54: CONST PBTE_B1 : PB : TE : !
~~~~

[PbTe-15Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-15Baj.tdb): PBTE_B1, type code %, sha256 `e1bad0890740970f…`

~~~~text
54: PHASE PBTE_B1 % 2 1 1 !
55: CONST PBTE_B1 : PB% VA : TE% VA : !
~~~~

[PbTe-86Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/PbTe-86Kat.tdb): PBTE_B1, type code %, sha256 `c309772d299befd6…`

~~~~text
57: PHASE PBTE_B1 % 2 1 1 !
58: CONST PBTE_B1 : PB% VA : PB TE% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2015.03.034](https://doi.org/10.1016/j.actamat.2015.03.034) Saurabh Bajaj, Gregory S. Pomrehn, Jeff W. Doak, Wojciech Gierlotka, Hsin-jay Wu, Sinn-Wen Chen et al., Ab initio study of intrinsic point defects in PbTe: an insight into phase stability, Acta Materialia 92, 72-80 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(86)90015-5](https://doi.org/10.1016/0364-5916%2886%2990015-5) U. Kattner, H.L. Lukas, G. Petzow, Optimization and calculation of the PB — TE system, Calphad 10, 103-116 (1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.12.083](https://doi.org/10.1016/j.jallcom.2008.12.083) Wojciech Gierlotka, Joanna Łapsa, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Pb–Te system using ionic liquid model, Journal of Alloys and Compounds 479, 152-156 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9791-8](https://doi.org/10.1007/s11669-010-9791-8) W. Gierlotka, J. Lapsa, K. Fitzner, J. Phase Equilib. Diffus., 31, 509-17(2010).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1965-561207](https://doi.org/10.1515/ijmr-1965-561207) Walter Lugscheider, Horst Ebel, Gerhard Langer, Thermoanalytische und röntgenographische Untersuchungen im System Blei-Tellur, International Journal of Materials Research 56, 851-852 (1965).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00809938](https://doi.org/10.1007/bf00809938) T. Leo Ngai, D. Marshall, R. C. Sharma, Y. A. Chang, Thermodynamic properties and phase equilibria of the lead-tellurium binary system, Monatsh Chem 118, 277-300 (1987).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
