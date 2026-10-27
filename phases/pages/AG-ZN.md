# Ag–Zn phases

> Ag–Zn system: 7 phases (tier A 4, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/AG-ZN.md

7 phases (tier A 4, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/AG-ZN.json) · [Ag–Zn system page](https://data.orchid-project.org/systems/AG-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Zn system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG5ZN8_D82](#phase-ag-zn-ag5zn8-d82); _phase:ag-zn:ag5zn8-d82_ | Cu5Zn8 · D8_2 · cI52 · I-43m (217) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–934.53 K, x(Zn) 0.58099–0.65083 | 6 | 5 |
| [AGZN_BB](#phase-ag-zn-agzn-bb); _phase:ag-zn:agzn-bb_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–552.02 K, x(Zn) 0.31652–0.52303 | 4 | 5 |
| [BCC_A2](#phase-ag-zn-bcc-a2); _phase:ag-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 518.13–982.96 K, x(Zn) 0.36607–0.58648 | 8 | 5 |
| [FCC_A1](#phase-ag-zn-fcc-a1); _phase:ag-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1234.93 K, x(Zn) 0–0.40408 | 4 | 5 |
| [HCP_A3](#phase-ag-zn-hcp-a3); _phase:ag-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–711.89 K, x(Zn) 0.9568–1 | 2 | 5 |
| [HCP_IM_A3](#phase-ag-zn-hcp-a3-im); _phase:ag-zn:hcp-a3-im_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–918.44 K, x(Zn) 0.65568–0.92955 | 4 | 5 |
| [LIQUID](#phase-ag-zn-liquid); _phase:ag-zn:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 692.68–2500 K, x(Zn) 0–1 | 8 | 5 |

## AG5ZN8_D82 (Ag–Zn)

- Id: `phase:ag-zn:ag5zn8-d82`; status `assigned`
- Structure: Cu5Zn8 · D8_2 · cI52 · I-43m (217); type `st:d8-2-cu5zn8-ci52`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AgZn-02Fri-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AgZn-02Fri-SGSOL.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AgZn-98Gom.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AgZn-99Oht.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–934.53 K, x(Zn) 0.58099–0.65083
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zn:ag5zn8-d82)

Names (8): _corpus: _corpus:phase:ag-zn:ag5zn8-d82  
_paper: _paper:10.1016/s0364-5916(98)00024-8:γ  
_system_alias: _system_alias:ag-zn:gamma  
_tdb: _tdb:AgZn-02Fri-LB.tdb:AG5ZN8_D82, tdb:AgZn-02Fri-SGSOL.tdb:AG5ZN8_D82, tdb:AgZn-98Gom.tdb:AG5ZN8_D82, tdb:AgZn-99Lee.tdb:AG5ZN8_D82, tdb:AgZn-99Oht.tdb:AG5ZN8_D82  


### TDB models of AG5ZN8_D82 (5): PHASE and CONSTITUENT statements as written

[AgZn-02Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-LB.tdb): AG5ZN8_D82, type code %, sha256 `b8990d47caf560f9…`

~~~~text
59: PHASE AG5ZN8_D82 % 4 2 2 3 6 !
60: CONST AG5ZN8_D82 : AG ZN% : AG : AG ZN% : AG ZN : !
~~~~

[AgZn-02Fri-SGSOL.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-SGSOL.tdb): AG5ZN8_D82, type code %, sha256 `0a185d9fbbf51abd…`

~~~~text
62: PHASE AG5ZN8_D82 % 4 2 2 3 6 !
63: CONST AG5ZN8_D82 : AG ZN : AG ZN : AG : ZN : !
~~~~

[AgZn-98Gom.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-98Gom.tdb): AG5ZN8_D82, type code %, sha256 `1bf7d9cb7ceb2d6f…`

~~~~text
46: PHASE AG5ZN8_D82 % 4 2 2 3 6 !
47: CONST AG5ZN8_D82 : AG ZN% : AG : AG ZN% : AG ZN : !
~~~~

[AgZn-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Lee.tdb): AG5ZN8_D82, type code %, sha256 `8d7d465d8d2edd39…`

~~~~text
48: PHASE AG5ZN8_D82 % 1 1 !
49: CONST AG5ZN8_D82 : AG ZN : !
~~~~

[AgZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Oht.tdb): AG5ZN8_D82, type code %, sha256 `8ee75db6e0e24c48…`

~~~~text
50: PHASE AG5ZN8_D82 % 4 2 2 3 6 !
51: CONST AG5ZN8_D82 : AG ZN : AG ZN : AG : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00024-8](https://doi.org/10.1016/S0364-5916%2898%2900024-8) T. Gomez-Acebo, Calphad, 22, 203-20(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## AGZN_BB (Ag–Zn)

- Id: `phase:ag-zn:agzn-bb`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_B_b; site_ratios_contradict_B_b:AgZn-02Fri-LB.tdb; site_ratios_contradict_B_b:AgZn-02Fri-SGSOL.tdb; site_ratios_contradict_B_b:AgZn-98Gom.tdb
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Ag1 Zn1 at x(ZN)=0.5000
- Candidate (literature_printed): AgZn · hP9 — printed with a label mapped to this phase
- Candidate (name_token): AgZn · B_b · hP9 · P-3 (147) — Strukturbericht/word 'BB' in the TDB name
- Candidate (sgte_mmc2): AgZn · B_b · hP9 · P-3 (147) — Hallstedt 2025 mmc2 row for AGZN_BB: AgZn (zeta)
- Candidate (tdb_comment): AgZn · hP9 · P-3 — AgZn-02Fri-LB.tdb: 'Prototype AgZn (hP9, P-3), zeta'
- Candidate (tdb_comment): AgZn · hP9 · P-3 — AgZn-02Fri-SGSOL.tdb: 'Prototype AgZn (hP9, P-3), zeta'
- Candidate (tdb_comment): AgZn · hP9 · P-3 — AgZn-98Gom.tdb: 'Prototype AgZn (hP9, P-3), zeta'
- Candidate (tdb_comment): AgZn · hP9 · P-3 — AgZn-99Lee.tdb: 'Prototype AgZn (hP9, P-3), zeta'
- Stability: stable in 5 of 5 calculated diagram(s): 300–552.02 K, x(Zn) 0.31652–0.52303
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zn:agzn-bb)

Names (7): _corpus: _corpus:phase:ag-zn:agzn-bb  
_paper: _paper:10.1016/s0364-5916(98)00024-8:ζ  
_tdb: _tdb:AgZn-02Fri-LB.tdb:AGZN_BB, tdb:AgZn-02Fri-SGSOL.tdb:AGZN_BB, tdb:AgZn-98Gom.tdb:AGZN_BB, tdb:AgZn-99Lee.tdb:AGZN_BB, tdb:AgZn-99Oht.tdb:AGZN_BB  


### TDB models of AGZN_BB (5): PHASE and CONSTITUENT statements as written

[AgZn-02Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-LB.tdb): AGZN_BB, type code %, sha256 `b8990d47caf560f9…`

~~~~text
54: PHASE AGZN_BB % 2 1 2 !
55: CONST AGZN_BB : ZN : AG ZN : !
~~~~

[AgZn-02Fri-SGSOL.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-SGSOL.tdb): AGZN_BB, type code %, sha256 `0a185d9fbbf51abd…`

~~~~text
57: PHASE AGZN_BB % 2 1 2 !
58: CONST AGZN_BB : ZN : AG ZN : !
~~~~

[AgZn-98Gom.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-98Gom.tdb): AGZN_BB, type code %, sha256 `1bf7d9cb7ceb2d6f…`

~~~~text
41: PHASE AGZN_BB % 2 1 2 !
42: CONST AGZN_BB : ZN : AG ZN : !
~~~~

[AgZn-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Lee.tdb): AGZN_BB, type code %, sha256 `8d7d465d8d2edd39…`

~~~~text
43: PHASE AGZN_BB % 1 1 !
44: CONST AGZN_BB : AG ZN : !
~~~~

[AgZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Oht.tdb): AGZN_BB, type code %, sha256 `8ee75db6e0e24c48…`

~~~~text
45: PHASE AGZN_BB % 1 1 !
46: CONST AGZN_BB : AG ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00024-8](https://doi.org/10.1016/S0364-5916%2898%2900024-8) T. Gomez-Acebo, Calphad, 22, 203-20(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## BCC_A2 (Ag–Zn)

- Id: `phase:ag-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 518.13–982.96 K, x(Zn) 0.36607–0.58648
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zn:bcc-a2)

Names (8): _corpus: _corpus:phase:ag-zn:bcc-a2  
_paper: _paper:10.1016/s0364-5916(98)00024-8:β  
_system_alias: _system_alias:ag-zn:beta  
_tdb: _tdb:AgZn-02Fri-LB.tdb:BCC_A2, tdb:AgZn-02Fri-SGSOL.tdb:BCC_A2, tdb:AgZn-98Gom.tdb:BCC_A2, tdb:AgZn-99Lee.tdb:BCC_A2, tdb:AgZn-99Oht.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[AgZn-02Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-LB.tdb): BCC_A2, type code %B, sha256 `b8990d47caf560f9…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : AG ZN : VA : !
~~~~

[AgZn-02Fri-SGSOL.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-SGSOL.tdb): BCC_A2, type code %B, sha256 `0a185d9fbbf51abd…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : AG ZN : VA : !
~~~~

[AgZn-98Gom.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-98Gom.tdb): BCC_A2, type code %B, sha256 `1bf7d9cb7ceb2d6f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG ZN : VA : !
~~~~

[AgZn-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Lee.tdb): BCC_A2, type code %B, sha256 `8d7d465d8d2edd39…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG ZN : VA : !
~~~~

[AgZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Oht.tdb): BCC_A2, type code %B, sha256 `8ee75db6e0e24c48…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00024-8](https://doi.org/10.1016/S0364-5916%2898%2900024-8) T. Gomez-Acebo, Calphad, 22, 203-20(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## FCC_A1 (Ag–Zn)

- Id: `phase:ag-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1234.93 K, x(Zn) 0–0.40408
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zn:fcc-a1)

Names (8): _corpus: _corpus:phase:ag-zn:fcc-a1  
_paper: _paper:10.1016/s0364-5916(98)00024-8:α  
_system_alias: _system_alias:ag-zn:alpha  
_tdb: _tdb:AgZn-02Fri-LB.tdb:FCC_A1, tdb:AgZn-02Fri-SGSOL.tdb:FCC_A1, tdb:AgZn-98Gom.tdb:FCC_A1, tdb:AgZn-99Lee.tdb:FCC_A1, tdb:AgZn-99Oht.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[AgZn-02Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-LB.tdb): FCC_A1, type code %A, sha256 `b8990d47caf560f9…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : AG% ZN : VA : !
~~~~

[AgZn-02Fri-SGSOL.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-SGSOL.tdb): FCC_A1, type code %A, sha256 `0a185d9fbbf51abd…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : AG% ZN : VA : !
~~~~

[AgZn-98Gom.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-98Gom.tdb): FCC_A1, type code %A, sha256 `1bf7d9cb7ceb2d6f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% ZN : VA : !
~~~~

[AgZn-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Lee.tdb): FCC_A1, type code %A, sha256 `8d7d465d8d2edd39…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% ZN : VA : !
~~~~

[AgZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Oht.tdb): FCC_A1, type code %A, sha256 `8ee75db6e0e24c48…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00024-8](https://doi.org/10.1016/S0364-5916%2898%2900024-8) T. Gomez-Acebo, Calphad, 22, 203-20(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## HCP_A3 (Ag–Zn)

- Id: `phase:ag-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–711.89 K, x(Zn) 0.9568–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zn:hcp-a3)

Names (8): _corpus: _corpus:phase:ag-zn:hcp-a3  
_paper: _paper:10.1016/s0364-5916(98)00024-8:η  
_system_alias: _system_alias:ag-zn:eta  
_tdb: _tdb:AgZn-02Fri-LB.tdb:HCP_A3, tdb:AgZn-02Fri-SGSOL.tdb:HCP_A3, tdb:AgZn-98Gom.tdb:HCP_A3, tdb:AgZn-99Lee.tdb:HCP_A3, tdb:AgZn-99Oht.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[AgZn-02Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-LB.tdb): HCP_A3, type code %A, sha256 `b8990d47caf560f9…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : AG ZN% : VA : !
~~~~

[AgZn-02Fri-SGSOL.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-SGSOL.tdb): HCP_A3, type code %A, sha256 `0a185d9fbbf51abd…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : AG ZN% : VA : !
~~~~

[AgZn-98Gom.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-98Gom.tdb): HCP_A3, type code %A, sha256 `1bf7d9cb7ceb2d6f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG ZN : VA : !
~~~~

[AgZn-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Lee.tdb): HCP_A3, type code %A, sha256 `8d7d465d8d2edd39…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG ZN : VA : !
~~~~

[AgZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Oht.tdb): HCP_A3, type code %A, sha256 `8ee75db6e0e24c48…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG ZN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00024-8](https://doi.org/10.1016/S0364-5916%2898%2900024-8) T. Gomez-Acebo, Calphad, 22, 203-20(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## HCP_IM_A3 (Ag–Zn)

- Id: `phase:ag-zn:hcp-a3-im`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:IM); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 5 of 5 calculated diagram(s): 300–918.44 K, x(Zn) 0.65568–0.92955
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zn:hcp-a3-im)

Names (8): _corpus: _corpus:phase:ag-zn:hcp-a3-im  
_paper: _paper:10.1016/s0364-5916(98)00024-8:ε  
_system_alias: _system_alias:ag-zn:epsilon  
_tdb: _tdb:AgZn-02Fri-LB.tdb:HCP_IM_A3, tdb:AgZn-02Fri-SGSOL.tdb:HCP_IM_A3, tdb:AgZn-98Gom.tdb:HCP_IM_A3, tdb:AgZn-99Lee.tdb:HCP_IM_A3, tdb:AgZn-99Oht.tdb:HCP_IM_A3  


### TDB models of HCP_IM_A3 (5): PHASE and CONSTITUENT statements as written

[AgZn-02Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-LB.tdb): HCP_IM_A3, type code %, sha256 `b8990d47caf560f9…`

~~~~text
64: PHASE HCP_IM_A3 % 1 1 !
65: CONST HCP_IM_A3 : AG ZN : !
~~~~

[AgZn-02Fri-SGSOL.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-SGSOL.tdb): HCP_IM_A3, type code %, sha256 `0a185d9fbbf51abd…`

~~~~text
67: PHASE HCP_IM_A3 % 1 1 !
68: CONST HCP_IM_A3 : AG ZN : !
~~~~

[AgZn-98Gom.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-98Gom.tdb): HCP_IM_A3, type code %, sha256 `1bf7d9cb7ceb2d6f…`

~~~~text
51: PHASE HCP_IM_A3 % 1 1 !
52: CONST HCP_IM_A3 : AG ZN : !
~~~~

[AgZn-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Lee.tdb): HCP_IM_A3, type code %, sha256 `8d7d465d8d2edd39…`

~~~~text
53: PHASE HCP_IM_A3 % 1 1 !
54: CONST HCP_IM_A3 : AG ZN : !
~~~~

[AgZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Oht.tdb): HCP_IM_A3, type code %, sha256 `8ee75db6e0e24c48…`

~~~~text
55: PHASE HCP_IM_A3 % 1 1 !
56: CONST HCP_IM_A3 : AG ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00024-8](https://doi.org/10.1016/S0364-5916%2898%2900024-8) T. Gomez-Acebo, Calphad, 22, 203-20(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## LIQUID (Ag–Zn)

- Id: `phase:ag-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 692.68–2500 K, x(Zn) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zn:liquid)

Names (7): _corpus: _corpus:phase:ag-zn:liquid  
_paper: _paper:10.1016/s0364-5916(98)00024-8:L  
_tdb: _tdb:AgZn-02Fri-LB.tdb:LIQUID, tdb:AgZn-02Fri-SGSOL.tdb:LIQUID, tdb:AgZn-98Gom.tdb:LIQUID, tdb:AgZn-99Lee.tdb:LIQUID, tdb:AgZn-99Oht.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[AgZn-02Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-LB.tdb): LIQUID, type code %, sha256 `b8990d47caf560f9…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : AG ZN : !
~~~~

[AgZn-02Fri-SGSOL.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-02Fri-SGSOL.tdb): LIQUID, type code %, sha256 `0a185d9fbbf51abd…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : AG ZN : !
~~~~

[AgZn-98Gom.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-98Gom.tdb): LIQUID, type code %, sha256 `1bf7d9cb7ceb2d6f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG ZN : !
~~~~

[AgZn-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Lee.tdb): LIQUID, type code %, sha256 `8d7d465d8d2edd39…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG ZN : !
~~~~

[AgZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZn-99Oht.tdb): LIQUID, type code %, sha256 `8ee75db6e0e24c48…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00024-8](https://doi.org/10.1016/S0364-5916%2898%2900024-8) T. Gomez-Acebo, Calphad, 22, 203-20(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
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
