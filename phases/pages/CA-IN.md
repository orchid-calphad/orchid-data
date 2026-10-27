# Ca–In phases

> Ca–In system: 10 phases (tier A 5, tier C 4, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-IN.html · Markdown: https://data.orchid-project.org/phases/pages/CA-IN.md

10 phases (tier A 5, tier C 4, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-IN) · [full JSON](https://data.orchid-project.org/phases/systems/CA-IN.json) · [Ca–In system page](https://data.orchid-project.org/systems/CA-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–In system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-ca-in-a6-tetragonal); _phase:ca-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–429.75 K, x(In) 1–1 | 2 | 2 |
| [BCC_A2](#phase-ca-in-bcc-a2); _phase:ca-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 716.03–1155 K, x(In) 0–0 | 1 | 3 |
| [B2_BCC](#phase-ca-in-bcc-b2); _phase:ca-in:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1164.08 K, x(In) 0–0.5 | 0 | 1 |
| [CA3IN](#phase-ca-in-ca3in); _phase:ca-in:ca3in_ | Ca8In3 · aP22 · P-1 (2) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1037.11 K, x(In) 0.25–0.25 | 4 | 1 |
| [CA8IN3](#phase-ca-in-ca8in3); _phase:ca-in:ca8in3_ | Ca8In3 · aP22 · P-1 (2) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1034.43 K, x(In) 0.27273–0.27273 | 14 | 1 |
| [CAIN](#phase-ca-in-cain); _phase:ca-in:cain_ | GaPu · tI16 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1167.58 K, x(In) 0.5–0.5 | 10 | 1 |
| [CAIN2](#phase-ca-in-cain2); _phase:ca-in:cain2_ | CaIn2 · hP6 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1110.32 K, x(In) 0.66667–0.66667 | 12 | 2 |
| [FCC_A1](#phase-ca-in-fcc-a1); _phase:ca-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–716.03 K, x(In) 0–0 | 0 | 2 |
| [HCP_A3](#phase-ca-in-hcp-a3); _phase:ca-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ca-in-liquid); _phase:ca-in:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 425.43–2500 K, x(In) 0–1 | 12 | 2 |

## TETRAGONAL_A6 (Ca–In)

- Id: `phase:ca-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–429.75 K, x(In) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:a6-tetragonal)

Names (5): _corpus: _corpus:phase:ca-in:a6-tetragonal, corpus:phase:ca-in:tetragonal-a6  
_paper: _paper:10.1007/s11669-013-0258-6:(In)  
_tdb: _tdb:CaIn-13Wan.tdb:TETRAGONAL_A6, tdb:CaIn-15Qin.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (2): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): TETRAGONAL_A6, type code %, sha256 `79293c7821a91f29…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : IN : !
~~~~

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): TETRAGONAL_A6, type code %, sha256 `09448428a82f51e5…`

~~~~text
55: PHASE TETRAGONAL_A6 % 1 1 !
56: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(64)90081-5](https://doi.org/10.1016/0022-5088%2864%2990081-5) G. Bruzzone, A.F. Ruggiero, The equilibrium diagram of the calcium-indium system, Journal of the Less Common Metals 7, 368-372 (1964).  
_cited as the source of values for this phase_

## BCC_A2 (Ca–In)

- Id: `phase:ca-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 716.03–1155 K, x(In) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:bcc-a2)

Names (5): _corpus: _corpus:phase:ca-in:bcc-a2  
_paper: _paper:10.1007/s11669-013-0258-6:(βCa)  
_tdb: _tdb:CaIn-13Wan.tdb:BCC_A2, tdb:CaIn-15Qin.tdb:A2_BCC, tdb:CaIn-15Qin.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): BCC_A2, type code %B, sha256 `79293c7821a91f29…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CA% IN : VA : !
~~~~

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): A2_BCC, type code %B, sha256 `09448428a82f51e5…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : CA% IN : VA : !
~~~~

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): BCC_A2, type code %B, sha256 `09448428a82f51e5…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CA% IN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## B2_BCC (Ca–In)

- Id: `phase:ca-in:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: CaIn-15Qin.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in CaIn-15Qin.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1164.08 K, x(In) 0–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:bcc-b2)

Names (2): _corpus: _corpus:phase:ca-in:bcc-b2  
_tdb: _tdb:CaIn-15Qin.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): B2_BCC, type code %BO, sha256 `09448428a82f51e5…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : CA% IN : CA IN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## CA3IN (Ca–In)

- Id: `phase:ca-in:ca3in`; status `assigned`
- Structure: Ca8In3 · aP22 · P-1 (2); type `st:ca8in3-ap22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.7500, In 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1037.11 K, x(In) 0.25–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:ca3in)

Names (3): _corpus: _corpus:phase:ca-in:ca3in  
_paper: _paper:10.1007/s11669-013-0258-6:Ca3In  
_tdb: _tdb:CaIn-13Wan.tdb:CA3IN  


### TDB models of CA3IN (1): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): CA3IN, type code %, sha256 `79293c7821a91f29…`

~~~~text
45: PHASE CA3IN % 2 3 1 !
46: CONST CA3IN : CA : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(64)90081-5](https://doi.org/10.1016/0022-5088%2864%2990081-5) G. Bruzzone, A.F. Ruggiero, The equilibrium diagram of the calcium-indium system, Journal of the Less Common Metals 7, 368-372 (1964).  
_cited as the source of values for this phase_

## CA8IN3 (Ca–In)

- Id: `phase:ca-in:ca8in3`; status `assigned`
- Structure: Ca8In3 · aP22 · P-1 (2); type `st:ca8in3-ap22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_2_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.7273, In 0.2727
- Stability: stable in 1 of 1 calculated diagram(s): 300–1034.43 K, x(In) 0.27273–0.27273
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:ca8in3)

Names (3): _corpus: _corpus:phase:ca-in:ca8in3  
_paper: _paper:10.1016/j.calphad.2014.10.008:Ca8In3  
_tdb: _tdb:CaIn-15Qin.tdb:CA8IN3  


### TDB models of CA8IN3 (1): PHASE and CONSTITUENT statements as written

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): CA8IN3, type code %, sha256 `09448428a82f51e5…`

~~~~text
60: PHASE CA8IN3 % 2 8 3 !
61: CONST CA8IN3 : CA : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1107/s0108270187010904](https://doi.org/10.1107/s0108270187010904) R. E. Marsh, K. M. Slagle, On the structure of Ca8In3, Acta Crystallogr C Cryst Struct Commun 44, 395-396 (1988).  
_cited as the source of values for this phase_

## CAIN (Ca–In)

- Id: `phase:ca-in:cain`; status `assigned`
- Structure: GaPu · tI16 · I4/mmm (139); type `st:gapu-ti16-2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.5000, In 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1167.58 K, x(In) 0.5–0.5
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:cain)

Names (4): _corpus: _corpus:phase:ca-in:cain  
_paper: _paper:10.1007/s11669-013-0258-6:CaIn, paper:10.1016/j.calphad.2014.10.008:CaIn  
_tdb: _tdb:CaIn-13Wan.tdb:CAIN  


### TDB models of CAIN (1): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): CAIN, type code %, sha256 `79293c7821a91f29…`

~~~~text
50: PHASE CAIN % 2 1 1 !
51: CONST CAIN : CA : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(64)90081-5](https://doi.org/10.1016/0022-5088%2864%2990081-5) G. Bruzzone, A.F. Ruggiero, The equilibrium diagram of the calcium-indium system, Journal of the Less Common Metals 7, 368-372 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_reports values for this phase_

## CAIN2 (Ca–In)

- Id: `phase:ca-in:cain2`; status `assigned`
- Structure: CaIn2 · hP6 · P6_3/mmc (194); type `st:cain2-hp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_194_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.3333, In 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1110.32 K, x(In) 0.66667–0.66667
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:cain2)

Names (5): _corpus: _corpus:phase:ca-in:cain2  
_paper: _paper:10.1007/s11669-013-0258-6:CaIn2, paper:10.1016/j.calphad.2014.10.008:CaIn2  
_tdb: _tdb:CaIn-13Wan.tdb:CAIN2, tdb:CaIn-15Qin.tdb:CAIN2  


### TDB models of CAIN2 (2): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): CAIN2, type code %, sha256 `79293c7821a91f29…`

~~~~text
55: PHASE CAIN2 % 2 1 2 !
56: CONST CAIN2 : CA : IN : !
~~~~

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): CAIN2, type code %, sha256 `09448428a82f51e5…`

~~~~text
65: PHASE CAIN2 % 2 1 2 !
66: CONST CAIN2 : CA : IN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(64)90081-5](https://doi.org/10.1016/0022-5088%2864%2990081-5) G. Bruzzone, A.F. Ruggiero, The equilibrium diagram of the calcium-indium system, Journal of the Less Common Metals 7, 368-372 (1964).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19643300315](https://doi.org/10.1002/zaac.19643300315) A. Iandelli, MX\<sub>2\</sub>‐Verbindungen der Erdalkali‐ und Seltenen Erdmetalle mit Gallium, Indium und Thallium, Zeitschrift anorg allge chemie 330, 221-232 (1964).  
_cited as the source of values for this phase_

## FCC_A1 (Ca–In)

- Id: `phase:ca-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–716.03 K, x(In) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:fcc-a1)

Names (3): _corpus: _corpus:phase:ca-in:fcc-a1  
_tdb: _tdb:CaIn-13Wan.tdb:FCC_A1, tdb:CaIn-15Qin.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): FCC_A1, type code %A, sha256 `79293c7821a91f29…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CA% IN : VA : !
~~~~

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): FCC_A1, type code %A, sha256 `09448428a82f51e5…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CA% IN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## HCP_A3 (Ca–In)

- Id: `phase:ca-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:hcp-a3)

Names (3): _corpus: _corpus:phase:ca-in:hcp-a3  
_tdb: _tdb:CaIn-13Wan.tdb:HCP_A3, tdb:CaIn-15Qin.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): HCP_A3, type code %A, sha256 `79293c7821a91f29…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CA IN : VA : !
~~~~

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): HCP_A3, type code %A, sha256 `09448428a82f51e5…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : CA IN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## LIQUID (Ca–In)

- Id: `phase:ca-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 425.43–2500 K, x(In) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-in:liquid)

Names (4): _corpus: _corpus:phase:ca-in:liquid  
_paper: _paper:10.1007/s11669-013-0258-6:L  
_tdb: _tdb:CaIn-13Wan.tdb:LIQUID, tdb:CaIn-15Qin.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CaIn-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-13Wan.tdb): LIQUID, type code %, sha256 `79293c7821a91f29…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CA IN : !
~~~~

[CaIn-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaIn-15Qin.tdb): LIQUID, type code %, sha256 `09448428a82f51e5…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CA IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-013-0258-6](https://doi.org/10.1007/s11669-013-0258-6) Lei Wang, Yajun Liu, Jing Liu, Thermodynamic Basis and Related Phase Equilibria for In-Na and In-Ca Binary Systems, J. Phase Equilib. Diffus. 34, 447-452 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(64)90081-5](https://doi.org/10.1016/0022-5088%2864%2990081-5) G. Bruzzone, A.F. Ruggiero, The equilibrium diagram of the calcium-indium system, Journal of the Less Common Metals 7, 368-372 (1964).  
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
