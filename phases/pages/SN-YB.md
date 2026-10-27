# Sn–Yb phases

> Sn–Yb system: 13 phases (tier A 10, tier C 2, liquid 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SN-YB.html · Markdown: https://data.orchid-project.org/phases/pages/SN-YB.md

13 phases (tier A 10, tier C 2, liquid 1); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SN-YB) · [full JSON](https://data.orchid-project.org/phases/systems/SN-YB.json) · [Sn–Yb system page](https://data.orchid-project.org/systems/SN-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/SN-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sn–Yb system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sn-yb-a4-diamond); _phase:sn-yb:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BCT_A5](#phase-sn-yb-a5-bct); _phase:sn-yb:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Yb) 0–0 | 5 | 2 |
| [BCC_A2](#phase-sn-yb-bcc-a2); _phase:sn-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1033–2499.48 K, x(Yb) 1–1 | 6 | 2 |
| [FCC_A1](#phase-sn-yb-fcc-a1); _phase:sn-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2498.93 K, x(Yb) 1–1 | 0 | 2 |
| [HCP_A3](#phase-sn-yb-hcp-a3); _phase:sn-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-sn-yb-liquid); _phase:sn-yb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 505.07–2500 K, x(Yb) 0–1 | 51 | 2 |
| [SN3YB_L12](#phase-sn-yb-sn3yb-l12); _phase:sn-yb:sn3yb-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1104.72 K, x(Yb) 0.25–0.25 | 16 | 2 |
| [SN3YB5_D88](#phase-sn-yb-sn3yb5-d88); _phase:sn-yb:sn3yb5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1369.67 K, x(Yb) 0.625–0.625 | 2 | 2 |
| [SN3YB5_D8L](#phase-sn-yb-sn3yb5-d8l); _phase:sn-yb:sn3yb5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1360–1584.59 K, x(Yb) 0.625–0.625 | 6 | 2 |
| [SN4YB5](#phase-sn-yb-sn4yb5); _phase:sn-yb:sn4yb5_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1432.5 K, x(Yb) 0.55556–0.55556 | 12 | 2 |
| [SN5YB3](#phase-sn-yb-sn5yb3); _phase:sn-yb:sn5yb3_ | Pd5Pu3 · oC32 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1060.47 K, x(Yb) 0.375–0.375 | 11 | 2 |
| [SNYB_L10](#phase-sn-yb-snyb-l10); _phase:sn-yb:snyb-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1311.14 K, x(Yb) 0.5–0.5 | 11 | 2 |
| [SNYB2_B82](#phase-sn-yb-snyb2-b82); _phase:sn-yb:snyb2-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1661.04 K, x(Yb) 0.66667–0.66667 | 18 | 2 |

## DIAMOND_A4 (Sn–Yb)

- Id: `phase:sn-yb:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:a4-diamond)

Names (3): _corpus: _corpus:phase:sn-yb:a4-diamond  
_tdb: _tdb:SnYb-11Idb.tdb:DIAMOND_A4, tdb:SnYb-17Kal.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): DIAMOND_A4, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): DIAMOND_A4, type code %, sha256 `715f12293802d1e0…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase_

## BCT_A5 (Sn–Yb)

- Id: `phase:sn-yb:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Yb) 0–0
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:a5-bct)

Names (6): _corpus: _corpus:phase:sn-yb:a5-bct, corpus:phase:sn-yb:bct-a5  
_paper: _paper:10.1007/s10973-010-1082-4:βSn, paper:10.1007/s11669-017-0588-x:Sn(bct)  
_tdb: _tdb:SnYb-11Idb.tdb:BCT_A5, tdb:SnYb-17Kal.tdb:BCT_A5  


### TDB models of BCT_A5 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): BCT_A5, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : SN : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): BCT_A5, type code %, sha256 `715f12293802d1e0…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90221-6](https://doi.org/10.1016/0022-5088%2876%2990221-6) A. Palenzona, S. Cirafici, The ytterbium-tin system, Journal of the Less Common Metals 46, 321-326 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_

## BCC_A2 (Sn–Yb)

- Id: `phase:sn-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1033–2499.48 K, x(Yb) 1–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:bcc-a2)

Names (5): _corpus: _corpus:phase:sn-yb:bcc-a2  
_paper: _paper:10.1007/s10973-010-1082-4:γYb, paper:10.1007/s11669-017-0588-x:γYb(bcc)  
_tdb: _tdb:SnYb-11Idb.tdb:BCC_A2, tdb:SnYb-17Kal.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): BCC_A2, type code %B, sha256 `ecc0e580cfd5693c…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : SN YB% : VA : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): BCC_A2, type code %B, sha256 `715f12293802d1e0…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SN YB% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_

## FCC_A1 (Sn–Yb)

- Id: `phase:sn-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2498.93 K, x(Yb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:sn-yb:fcc-a1  
_tdb: _tdb:SnYb-11Idb.tdb:FCC_A1, tdb:SnYb-17Kal.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): FCC_A1, type code %A, sha256 `ecc0e580cfd5693c…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : SN YB% : VA : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): FCC_A1, type code %A, sha256 `715f12293802d1e0…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SN YB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase_

## HCP_A3 (Sn–Yb)

- Id: `phase:sn-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:hcp-a3)

Names (3): _corpus: _corpus:phase:sn-yb:hcp-a3  
_tdb: _tdb:SnYb-11Idb.tdb:HCP_A3, tdb:SnYb-17Kal.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): HCP_A3, type code %A, sha256 `ecc0e580cfd5693c…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : SN YB : VA : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): HCP_A3, type code %A, sha256 `715f12293802d1e0…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SN YB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase_

## LIQUID (Sn–Yb)

- Id: `phase:sn-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 505.07–2500 K, x(Yb) 0–1
- Literature: 51 values (51 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:liquid)

Names (5): _corpus: _corpus:phase:sn-yb:liquid  
_paper: _paper:10.1007/s10973-010-1082-4:L, paper:10.1007/s11669-017-0588-x:L  
_tdb: _tdb:SnYb-11Idb.tdb:LIQUID, tdb:SnYb-17Kal.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): LIQUID, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : SN YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): LIQUID, type code %, sha256 `715f12293802d1e0…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SN YB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90221-6](https://doi.org/10.1016/0022-5088%2876%2990221-6) A. Palenzona, S. Cirafici, The ytterbium-tin system, Journal of the Less Common Metals 46, 321-326 (1976).  
_cited as the source of values for this phase_

## SN3YB_L12 (Sn–Yb)

- Id: `phase:sn-yb:sn3yb-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 0.7500, Yb 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1104.72 K, x(Yb) 0.25–0.25
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:sn3yb-l12)

Names (5): _corpus: _corpus:phase:sn-yb:sn3yb-l12  
_paper: _paper:10.1007/s10973-010-1082-4:YbSn3, paper:10.1007/s11669-017-0588-x:YbSn3  
_tdb: _tdb:SnYb-11Idb.tdb:SN3YB_L12, tdb:SnYb-17Kal.tdb:SN3YB_L12  


### TDB models of SN3YB_L12 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): SN3YB_L12, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
55: PHASE SN3YB_L12 % 2 3 1 !
56: CONST SN3YB_L12 : SN : YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): SN3YB_L12, type code %, sha256 `715f12293802d1e0…`

~~~~text
54: PHASE SN3YB_L12 % 2 3 1 !
55: CONST SN3YB_L12 : SN : YB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90221-6](https://doi.org/10.1016/0022-5088%2876%2990221-6) A. Palenzona, S. Cirafici, The ytterbium-tin system, Journal of the Less Common Metals 46, 321-326 (1976).  
_cited as the source of values for this phase_

## SN3YB5_D88 (Sn–Yb)

- Id: `phase:sn-yb:sn3yb5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 0.3750, Yb 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–1369.67 K, x(Yb) 0.625–0.625
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:sn3yb5-d88)

Names (4): _corpus: _corpus:phase:sn-yb:sn3yb5-d88  
_paper: _paper:10.1007/s10973-010-1082-4:αYb5Sn3  
_tdb: _tdb:SnYb-11Idb.tdb:SN3YB5_D88, tdb:SnYb-17Kal.tdb:SN3YB5_D88  


### TDB models of SN3YB5_D88 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): SN3YB5_D88, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
75: PHASE SN3YB5_D88 % 2 3 5 !
76: CONST SN3YB5_D88 : SN : YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): SN3YB5_D88, type code %, sha256 `715f12293802d1e0…`

~~~~text
74: PHASE SN3YB5_D88 % 2 3 5 !
75: CONST SN3YB5_D88 : SN : YB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_

## SN3YB5_D8L (Sn–Yb)

- Id: `phase:sn-yb:sn3yb5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 0.3750, Yb 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 1360–1584.59 K, x(Yb) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:sn3yb5-d8l)

Names (4): _corpus: _corpus:phase:sn-yb:sn3yb5-d8l  
_paper: _paper:10.1007/s10973-010-1082-4:βYb5Sn3  
_tdb: _tdb:SnYb-11Idb.tdb:SN3YB5_D8L, tdb:SnYb-17Kal.tdb:SN3YB5_D8L  


### TDB models of SN3YB5_D8L (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): SN3YB5_D8L, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
80: PHASE SN3YB5_D8L % 2 3 5 !
81: CONST SN3YB5_D8L : SN : YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): SN3YB5_D8L, type code %, sha256 `715f12293802d1e0…`

~~~~text
79: PHASE SN3YB5_D8L % 2 3 5 !
80: CONST SN3YB5_D8L : SN : YB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_

## SN4YB5 (Sn–Yb)

- Id: `phase:sn-yb:sn4yb5`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.4444, Yb 0.5556
- Stability: stable in 2 of 2 calculated diagram(s): 300–1432.5 K, x(Yb) 0.55556–0.55556
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:sn4yb5)

Names (5): _corpus: _corpus:phase:sn-yb:sn4yb5  
_paper: _paper:10.1007/s10973-010-1082-4:Yb5Sn4, paper:10.1007/s11669-017-0588-x:Yb5Sn4  
_tdb: _tdb:SnYb-11Idb.tdb:SN4YB5, tdb:SnYb-17Kal.tdb:SN4YB5  


### TDB models of SN4YB5 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): SN4YB5, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
70: PHASE SN4YB5 % 2 4 5 !
71: CONST SN4YB5 : SN : YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): SN4YB5, type code %, sha256 `715f12293802d1e0…`

~~~~text
69: PHASE SN4YB5 % 2 4 5 !
70: CONST SN4YB5 : SN : YB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90221-6](https://doi.org/10.1016/0022-5088%2876%2990221-6) A. Palenzona, S. Cirafici, The ytterbium-tin system, Journal of the Less Common Metals 46, 321-326 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_

## SN5YB3 (Sn–Yb)

- Id: `phase:sn-yb:sn5yb3`; status `assigned`
- Structure: Pd5Pu3 · oC32 · Cmcm (63); type `st:pd5pu3-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.6250, Yb 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–1060.47 K, x(Yb) 0.375–0.375
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:sn5yb3)

Names (5): _corpus: _corpus:phase:sn-yb:sn5yb3  
_paper: _paper:10.1007/s10973-010-1082-4:Yb3Sn5, paper:10.1007/s11669-017-0588-x:Yb3Sn5  
_tdb: _tdb:SnYb-11Idb.tdb:SN5YB3, tdb:SnYb-17Kal.tdb:SN5YB3  


### TDB models of SN5YB3 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): SN5YB3, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
60: PHASE SN5YB3 % 2 5 3 !
61: CONST SN5YB3 : SN : YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): SN5YB3, type code %, sha256 `715f12293802d1e0…`

~~~~text
59: PHASE SN5YB3 % 2 5 3 !
60: CONST SN5YB3 : SN : YB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90221-6](https://doi.org/10.1016/0022-5088%2876%2990221-6) A. Palenzona, S. Cirafici, The ytterbium-tin system, Journal of the Less Common Metals 46, 321-326 (1976).  
_cited as the source of values for this phase_

## SNYB_L10 (Sn–Yb)

- Id: `phase:sn-yb:snyb-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 0.5000, Yb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1311.14 K, x(Yb) 0.5–0.5
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:snyb-l10)

Names (5): _corpus: _corpus:phase:sn-yb:snyb-l10  
_paper: _paper:10.1007/s10973-010-1082-4:YbSn, paper:10.1007/s11669-017-0588-x:YbSn  
_tdb: _tdb:SnYb-11Idb.tdb:SNYB_L10, tdb:SnYb-17Kal.tdb:SNYB_L10  


### TDB models of SNYB_L10 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): SNYB_L10, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
65: PHASE SNYB_L10 % 2 1 1 !
66: CONST SNYB_L10 : SN : YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): SNYB_L10, type code %, sha256 `715f12293802d1e0…`

~~~~text
64: PHASE SNYB_L10 % 2 1 1 !
65: CONST SNYB_L10 : SN : YB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90221-6](https://doi.org/10.1016/0022-5088%2876%2990221-6) A. Palenzona, S. Cirafici, The ytterbium-tin system, Journal of the Less Common Metals 46, 321-326 (1976).  
_cited as the source of values for this phase_

## SNYB2_B82 (Sn–Yb)

- Id: `phase:sn-yb:snyb2-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 0.3333, Yb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1661.04 K, x(Yb) 0.66667–0.66667
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-yb:snyb2-b82)

Names (5): _corpus: _corpus:phase:sn-yb:snyb2-b82  
_paper: _paper:10.1007/s10973-010-1082-4:Yb2Sn, paper:10.1007/s11669-017-0588-x:Yb2Sn  
_tdb: _tdb:SnYb-11Idb.tdb:SNYB2_B82, tdb:SnYb-17Kal.tdb:SNYB2_B82  


### TDB models of SNYB2_B82 (2): PHASE and CONSTITUENT statements as written

[SnYb-11Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-11Idb.tdb): SNYB2_B82, type code %, sha256 `ecc0e580cfd5693c…`

~~~~text
85: PHASE SNYB2_B82 % 2 1 2 !
86: CONST SNYB2_B82 : SN : YB : !
~~~~

[SnYb-17Kal.tdb](https://orchid-project.org/data/databases/sgte-binary/SnYb-17Kal.tdb): SNYB2_B82, type code %, sha256 `715f12293802d1e0…`

~~~~text
84: PHASE SNYB2_B82 % 2 1 2 !
85: CONST SNYB2_B82 : SN : YB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-017-0588-x](https://doi.org/10.1007/s11669-017-0588-x) F. Kali-Ali, Y. Djaballah, S. Triaa, Ş. Uğur, A. Belgacem-Bouzida, M. Drir et al., Ab-Initio Calculations and Thermodynamic Description of the Yb-Cd and Yb-Sn Systems, J. Phase Equilib. Diffus. 38, 665-675 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-010-1082-4](https://doi.org/10.1007/s10973-010-1082-4) Mohamed Idbenali, Colette Servant, Thermodynamic optimization of the Yb–Sn system, J Therm Anal Calorim 103, 131-135 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02645976](https://doi.org/10.1007/bf02645976) A. Palenzona and S. Cirafici, The Sn-Yb (Tin-Ytterbium) System, J. Phase Equilib., 1991, 12(4), p 482-485  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00929-3](https://doi.org/10.1016/s0925-8388%2898%2900929-3) P Manfrinetti, D Mazzone, A Palenzona, An up-dating of the Yb–Sn phase diagram, Journal of Alloys and Compounds 284, L1-L3 (1999).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90221-6](https://doi.org/10.1016/0022-5088%2876%2990221-6) A. Palenzona, S. Cirafici, The ytterbium-tin system, Journal of the Less Common Metals 46, 321-326 (1976).  
_cited as the source of values for this phase_

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
