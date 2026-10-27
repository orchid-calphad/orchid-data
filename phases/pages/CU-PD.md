# Cu–Pd phases

> Cu–Pd system: 10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-PD.html · Markdown: https://data.orchid-project.org/phases/pages/CU-PD.md

10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-PD) · [full JSON](https://data.orchid-project.org/phases/systems/CU-PD.json) · [Cu–Pd system page](https://data.orchid-project.org/systems/CU-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Pd system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-pd-bcc-a2); _phase:cu-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [B2_BCC](#phase-cu-pd-bcc-b2); _phase:cu-pd:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 300–865 K, x(Pd) 0.30064–0.49997 | 4 | 2 |
| [D1_LPS](#phase-cu-pd-d1-lps); _phase:cu-pd:d1-lps_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1670–1710 K, x(Pd) 0.97–0.97 | 0 | 1 |
| [D2_LPS](#phase-cu-pd-d2-lps); _phase:cu-pd:d2-lps_ | Cu3Pd · oP320 · Pnnm (58) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1720 K, x(Pd) 0–0.97 | 4 | 1 |
| [FCC_2](#phase-cu-pd-fcc-2); _phase:cu-pd:fcc-2_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_3](#phase-cu-pd-fcc-3); _phase:cu-pd:fcc-3_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-cu-pd-fcc-a1); _phase:cu-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 300–2499.25 K, x(Pd) 0–1 | 10 | 3 |
| [L12_FCC](#phase-cu-pd-fcc-l12); _phase:cu-pd:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1828 K, x(Pd) 0–1 | 4 | 1 |
| [HCP_A3](#phase-cu-pd-hcp-a3); _phase:cu-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cu-pd-liquid); _phase:cu-pd:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1357.77–2500 K, x(Pd) 0–1 | 1 | 2 |

## BCC_A2 (Cu–Pd)

- Id: `phase:cu-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-pd:bcc-a2  
_tdb: _tdb:CuPd-07Hua.tdb:BCC_A2, tdb:CuPd-08Li.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuPd-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-07Hua.tdb): BCC_A2, type code %B, sha256 `06510f59b44887a3…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CU PD : VA : !
~~~~

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): BCC_A2, type code %B, sha256 `9f6569339cd316e7…`

~~~~text
64: PHASE BCC_A2 %B 2 1 3 !
65: CONST BCC_A2 : CU PD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase_

## B2_BCC (Cu–Pd)

- Id: `phase:cu-pd:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CuPd-07Hua.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CuPd-08Li.tdb also describes the disordered state
- Stability: stable in 1 of 2 calculated diagram(s): 300–865 K, x(Pd) 0.30064–0.49997
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:bcc-b2)

Names (5): _corpus: _corpus:phase:cu-pd:bcc-b2, corpus:phase:cu-pd:b2-bcc  
_paper: _paper:10.1016/j.calphad.2008.04.004:CuPd  
_tdb: _tdb:CuPd-07Hua.tdb:B2_BCC, tdb:CuPd-08Li.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[CuPd-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-07Hua.tdb): B2_BCC, type code %B, sha256 `06510f59b44887a3…`

~~~~text
41: PHASE B2_BCC %B 3 0.5 0.5 1 !
42: CONST B2_BCC : CU% PD : CU PD% : VA : !
~~~~

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): B2_BCC, type code %, sha256 `9f6569339cd316e7…`

~~~~text
69: PHASE B2_BCC % 2 1 1 !
70: CONST B2_BCC : CU% PD : CU PD% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1007/bf02663663](https://doi.org/10.1007/bf02663663) P Huang, S Menon, D de Fontaine, On the Cu-Pd phase diagram, JPE 12, 3-5 (1991).  
_cited as the source of values for this phase_

## D1_LPS (Cu–Pd)

- Id: `phase:cu-pd:d1-lps`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_name; sgte_mmc2_row_disagrees_with_name:D1_LPS; unrecognised_name_tokens:LPS
- Candidate (name_token): NH3 · D1 · cP16 · P2_13 (198) — Strukturbericht/word 'D1' in the TDB name
- Candidate (sgte_mmc2): Cu3Pd · tP28 · P4/mmm (123) — Hallstedt 2025 mmc2 row for D1_LPS: Cu3Pd (1D-LPS)
- Candidate (tdb_comment): Cu3Pd · tP28 · P4/mmm — CuPd-08Li.tdb: 'Prototype Cu3Pd (tP28, P4/mmm), 1D-LPS'
- Stability: stable in 1 of 1 calculated diagram(s): 1670–1710 K, x(Pd) 0.97–0.97
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:d1-lps)

Names (2): _corpus: _corpus:phase:cu-pd:d1-lps  
_tdb: _tdb:CuPd-08Li.tdb:D1_LPS  


### TDB models of D1_LPS (1): PHASE and CONSTITUENT statements as written

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): D1_LPS, type code %AU, sha256 `9f6569339cd316e7…`

~~~~text
49: PHASE D1_LPS %AU 3 0.75 0.25 1 !
50: CONST D1_LPS : CU% PD : CU PD% : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase_

## D2_LPS (Cu–Pd)

- Id: `phase:cu-pd:d2-lps`; status `assigned`
- Structure: Cu3Pd · oP320 · Pnnm (58); type `st:cu3pd-op320`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:D2,LPS, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1720 K, x(Pd) 0–0.97
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:d2-lps)

Names (3): _corpus: _corpus:phase:cu-pd:d2-lps  
_paper: _paper:10.1016/j.calphad.2008.04.004:2D-LPS  
_tdb: _tdb:CuPd-08Li.tdb:D2_LPS  


### TDB models of D2_LPS (1): PHASE and CONSTITUENT statements as written

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): D2_LPS, type code %AV, sha256 `9f6569339cd316e7…`

~~~~text
59: PHASE D2_LPS %AV 3 0.75 0.25 1 !
60: CONST D2_LPS : CU% PD : CU PD% : VA :  !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02663663](https://doi.org/10.1007/bf02663663) P Huang, S Menon, D de Fontaine, On the Cu-Pd phase diagram, JPE 12, 3-5 (1991).  
_cited as the source of values for this phase_

## FCC_2 (Cu–Pd)

- Id: `phase:cu-pd:fcc-2`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:2
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:fcc-2)

Names (2): _corpus: _corpus:phase:cu-pd:fcc-2  
_tdb: _tdb:CuPd-08Li.tdb:FCC_2  


### TDB models of FCC_2 (1): PHASE and CONSTITUENT statements as written

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): FCC_2, type code %A, sha256 `9f6569339cd316e7…`

~~~~text
44: PHASE FCC_2 %A 2 1 1 !
45: CONST FCC_2 : CU% PD% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase_

## FCC_3 (Cu–Pd)

- Id: `phase:cu-pd:fcc-3`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:3
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:fcc-3)

Names (2): _corpus: _corpus:phase:cu-pd:fcc-3  
_tdb: _tdb:CuPd-08Li.tdb:FCC_3  


### TDB models of FCC_3 (1): PHASE and CONSTITUENT statements as written

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): FCC_3, type code %A, sha256 `9f6569339cd316e7…`

~~~~text
54: PHASE FCC_3 %A 2 1 1 !
55: CONST FCC_3 : CU% PD% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase_

## FCC_A1 (Cu–Pd)

- Id: `phase:cu-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–2499.25 K, x(Pd) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:fcc-a1)

Names (5): _corpus: _corpus:phase:cu-pd:fcc-a1  
_paper: _paper:10.1016/j.calphad.2008.04.004:fcc  
_tdb: _tdb:CuPd-07Hua.tdb:FCC_A1, tdb:CuPd-08Li.tdb:A1_FCC, tdb:CuPd-08Li.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CuPd-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-07Hua.tdb): FCC_A1, type code %A, sha256 `06510f59b44887a3…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CU% PD% : VA : !
~~~~

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): A1_FCC, type code %A, sha256 `9f6569339cd316e7…`

~~~~text
34: PHASE A1_FCC %A 2 1 1 !
35: CONST A1_FCC : CU% PD% : VA : !
~~~~

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): FCC_A1, type code %A, sha256 `9f6569339cd316e7…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CU% PD% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1007/bf02663663](https://doi.org/10.1007/bf02663663) P Huang, S Menon, D de Fontaine, On the Cu-Pd phase diagram, JPE 12, 3-5 (1991).  
_cited as the source of values for this phase_

## L12_FCC (Cu–Pd)

- Id: `phase:cu-pd:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: CuPd-08Li.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in CuPd-08Li.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1828 K, x(Pd) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:fcc-l12)

Names (4): _corpus: _corpus:phase:cu-pd:fcc-l12, corpus:phase:cu-pd:l12-fcc  
_paper: _paper:10.1016/j.calphad.2008.04.004:Cu3Pd  
_tdb: _tdb:CuPd-08Li.tdb:L12_FCC  


### TDB models of L12_FCC (1): PHASE and CONSTITUENT statements as written

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): L12_FCC, type code %AY, sha256 `9f6569339cd316e7…`

~~~~text
39: PHASE L12_FCC %AY 3 0.75 0.25 1 !
40: CONST L12_FCC : CU% PD : CU PD% : VA :  !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02663663](https://doi.org/10.1007/bf02663663) P Huang, S Menon, D de Fontaine, On the Cu-Pd phase diagram, JPE 12, 3-5 (1991).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Pd)

- Id: `phase:cu-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:hcp-a3)

Names (3): _corpus: _corpus:phase:cu-pd:hcp-a3  
_tdb: _tdb:CuPd-07Hua.tdb:HCP_A3, tdb:CuPd-08Li.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuPd-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-07Hua.tdb): HCP_A3, type code %A, sha256 `06510f59b44887a3…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : CU PD : VA : !
~~~~

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): HCP_A3, type code %A, sha256 `9f6569339cd316e7…`

~~~~text
74: PHASE HCP_A3 %A 2 1 0.5 !
75: CONST HCP_A3 : CU PD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
_assessment that models this phase_

## LIQUID (Cu–Pd)

- Id: `phase:cu-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1357.77–2500 K, x(Pd) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pd:liquid)

Names (4): _corpus: _corpus:phase:cu-pd:liquid  
_paper: _paper:10.1016/j.calphad.2007.02.002:liquid  
_tdb: _tdb:CuPd-07Hua.tdb:LIQUID, tdb:CuPd-08Li.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuPd-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-07Hua.tdb): LIQUID, type code %, sha256 `06510f59b44887a3…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CU PD : !
~~~~

[CuPd-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb): LIQUID, type code %, sha256 `9f6569339cd316e7…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CU PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008).  
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
