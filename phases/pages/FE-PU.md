# Fe–Pu phases

> Fe–Pu system: 10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-PU.html · Markdown: https://data.orchid-project.org/phases/pages/FE-PU.md

10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-PU) · [full JSON](https://data.orchid-project.org/phases/systems/FE-PU.json) · [Fe–Pu system page](https://data.orchid-project.org/systems/FE-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Pu system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-fe-pu-a6-tetragonal); _phase:fe-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 617.4–907.61 K, x(Pu) 1–1 | 0 | 2 |
| [BCC_A2](#phase-fe-pu-bcc-a2); _phase:fe-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.25 K, x(Pu) 0–1 | 0 | 2 |
| [FCC_A1](#phase-fe-pu-fcc-a1); _phase:fe-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 581.18–1690.33 K, x(Pu) 0–1 | 0 | 2 |
| [FE2PU_C15](#phase-fe-pu-fe2pu-c15); _phase:fe-pu:fe2pu-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1512.98 K, x(Pu) 0.32714–0.33375 | 0 | 2 |
| [FEPU6_D2C](#phase-fe-pu-fepu6-d2c); _phase:fe-pu:fepu6-d2c_ | MnU6 · D2_c · tI28 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–700.61 K, x(Pu) 0.85276–0.85714 | 0 | 2 |
| [HCP_A3](#phase-fe-pu-hcp-a3); _phase:fe-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-fe-pu-liquid); _phase:fe-pu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 666.74–4000 K, x(Pu) 0–1 | 0 | 2 |
| [ALPHA_PU](#phase-fe-pu-pu-alpha); _phase:fe-pu:pu-alpha_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–397.62 K, x(Pu) 1–1 | 0 | 2 |
| [BETA_PU](#phase-fe-pu-pu-beta); _phase:fe-pu:pu-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1 | 0 | 2 |
| [GAMMA_PU](#phase-fe-pu-pu-gamma); _phase:fe-pu:pu-gamma_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 487.9–607.92 K, x(Pu) 1–1 | 0 | 2 |

## TETRAGONAL_A6 (Fe–Pu)

- Id: `phase:fe-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 617.4–907.61 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:a6-tetragonal)

Names (3): _corpus: _corpus:phase:fe-pu:a6-tetragonal  
_tdb: _tdb:FePu-01Kur.tdb:TETRAGONAL_A6, tdb:FePu-04Tur.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): TETRAGONAL_A6, type code %, sha256 `a1185b9017b19c8f…`

~~~~text
41: PHASE TETRAGONAL_A6 % 1 1 !
42: CONST TETRAGONAL_A6 : PU : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): TETRAGONAL_A6, type code %, sha256 `212316a67a63edf4…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## BCC_A2 (Fe–Pu)

- Id: `phase:fe-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.25 K, x(Pu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:bcc-a2)

Names (3): _corpus: _corpus:phase:fe-pu:bcc-a2  
_tdb: _tdb:FePu-01Kur.tdb:BCC_A2, tdb:FePu-04Tur.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): BCC_A2, type code %B, sha256 `a1185b9017b19c8f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : FE% PU% : VA : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): BCC_A2, type code %B, sha256 `212316a67a63edf4…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## FCC_A1 (Fe–Pu)

- Id: `phase:fe-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 581.18–1690.33 K, x(Pu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:fcc-a1)

Names (3): _corpus: _corpus:phase:fe-pu:fcc-a1  
_tdb: _tdb:FePu-01Kur.tdb:FCC_A1, tdb:FePu-04Tur.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): FCC_A1, type code %A, sha256 `a1185b9017b19c8f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : FE% PU : VA : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): FCC_A1, type code %A, sha256 `212316a67a63edf4…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% PU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## FE2PU_C15 (Fe–Pu)

- Id: `phase:fe-pu:fe2pu-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FePu-04Tur.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1512.98 K, x(Pu) 0.32714–0.33375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:fe2pu-c15)

Names (3): _corpus: _corpus:phase:fe-pu:fe2pu-c15  
_tdb: _tdb:FePu-01Kur.tdb:FE2PU_C15, tdb:FePu-04Tur.tdb:FE2PU_C15  


### TDB models of FE2PU_C15 (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): FE2PU_C15, type code %, sha256 `a1185b9017b19c8f…`

~~~~text
61: PHASE FE2PU_C15 % 2 2 1 !
62: CONST FE2PU_C15 : FE : PU : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): FE2PU_C15, type code %, sha256 `212316a67a63edf4…`

~~~~text
60: PHASE FE2PU_C15 % 2 2 1 !
61: CONST FE2PU_C15 : FE% PU : FE PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## FEPU6_D2C (Fe–Pu)

- Id: `phase:fe-pu:fepu6-d2c`; status `assigned`
- Structure: MnU6 · D2_c · tI28 · I4/mcm (140); type `st:d2-c-mnu6-ti28`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FePu-04Tur.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–700.61 K, x(Pu) 0.85276–0.85714
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:fepu6-d2c)

Names (3): _corpus: _corpus:phase:fe-pu:fepu6-d2c  
_tdb: _tdb:FePu-01Kur.tdb:FEPU6_D2C, tdb:FePu-04Tur.tdb:FEPU6_D2C  


### TDB models of FEPU6_D2C (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): FEPU6_D2C, type code %, sha256 `a1185b9017b19c8f…`

~~~~text
66: PHASE FEPU6_D2C % 2 1 6 !
67: CONST FEPU6_D2C : FE : PU : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): FEPU6_D2C, type code %, sha256 `212316a67a63edf4…`

~~~~text
65: PHASE FEPU6_D2C % 2 1 6 !
66: CONST FEPU6_D2C : FE% PU : FE PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## HCP_A3 (Fe–Pu)

- Id: `phase:fe-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:hcp-a3)

Names (3): _corpus: _corpus:phase:fe-pu:hcp-a3  
_tdb: _tdb:FePu-01Kur.tdb:HCP_A3, tdb:FePu-04Tur.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): HCP_A3, type code %A, sha256 `a1185b9017b19c8f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : FE : VA : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): HCP_A3, type code %A, sha256 `212316a67a63edf4…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## LIQUID (Fe–Pu)

- Id: `phase:fe-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 666.74–4000 K, x(Pu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:liquid)

Names (3): _corpus: _corpus:phase:fe-pu:liquid  
_tdb: _tdb:FePu-01Kur.tdb:LIQUID, tdb:FePu-04Tur.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): LIQUID, type code %, sha256 `a1185b9017b19c8f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : FE PU : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): LIQUID, type code %, sha256 `212316a67a63edf4…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## ALPHA_PU (Fe–Pu)

- Id: `phase:fe-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — FePu-01Kur.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — FePu-04Tur.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–397.62 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:pu-alpha)

Names (3): _corpus: _corpus:phase:fe-pu:pu-alpha  
_tdb: _tdb:FePu-01Kur.tdb:ALPHA_PU, tdb:FePu-04Tur.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): ALPHA_PU, type code %, sha256 `a1185b9017b19c8f…`

~~~~text
46: PHASE ALPHA_PU % 1 1 !
47: CONST ALPHA_PU : PU : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): ALPHA_PU, type code %, sha256 `212316a67a63edf4…`

~~~~text
45: PHASE ALPHA_PU % 1 1 !
46: CONST ALPHA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## BETA_PU (Fe–Pu)

- Id: `phase:fe-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — FePu-01Kur.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — FePu-04Tur.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:pu-beta)

Names (3): _corpus: _corpus:phase:fe-pu:pu-beta  
_tdb: _tdb:FePu-01Kur.tdb:BETA_PU, tdb:FePu-04Tur.tdb:BETA_PU  


### TDB models of BETA_PU (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): BETA_PU, type code %, sha256 `a1185b9017b19c8f…`

~~~~text
51: PHASE BETA_PU % 1 1 !
52: CONST BETA_PU : PU : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): BETA_PU, type code %, sha256 `212316a67a63edf4…`

~~~~text
50: PHASE BETA_PU % 1 1 !
51: CONST BETA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

## GAMMA_PU (Fe–Pu)

- Id: `phase:fe-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — FePu-01Kur.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — FePu-04Tur.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 487.9–607.92 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pu:pu-gamma)

Names (3): _corpus: _corpus:phase:fe-pu:pu-gamma  
_tdb: _tdb:FePu-01Kur.tdb:GAMMA_PU, tdb:FePu-04Tur.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (2): PHASE and CONSTITUENT statements as written

[FePu-01Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-01Kur.tdb): GAMMA_PU, type code %, sha256 `a1185b9017b19c8f…`

~~~~text
56: PHASE GAMMA_PU % 1 1 !
57: CONST GAMMA_PU : PU : !
~~~~

[FePu-04Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/FePu-04Tur.tdb): GAMMA_PU, type code %, sha256 `212316a67a63edf4…`

~~~~text
55: PHASE GAMMA_PU % 1 1 !
56: CONST GAMMA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(01)00473-1](https://doi.org/10.1016/S0022-3115%2801%2900473-1) M. Kurata, K. Nakamura, T. Ogata, J. Nucl. Mater., 294, 123-29(2001).  
_assessment that models this phase_

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
