# Nb–Zn phases

> Nb–Zn system: 10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/NB-ZN.md

10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/NB-ZN.json) · [Nb–Zn system page](https://data.orchid-project.org/systems/NB-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Zn system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-zn-bcc-a2); _phase:nb-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2768.73 K, x(Zn) 0–0.00095 | 2 | 1 |
| [FCC_A1](#phase-nb-zn-fcc-a1); _phase:nb-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-nb-zn-hcp-a3); _phase:nb-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–692.73 K, x(Zn) 0.9999–1 | 2 | 1 |
| [LIQUID](#phase-nb-zn-liquid); _phase:nb-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300.23–4000 K, x(Zn) 0–1 | 14 | 1 |
| [NB2ZN3_D85](#phase-nb-zn-nb2zn3-d85); _phase:nb-zn:nb2zn3-d85_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1387.75 K, x(Zn) 0.6–0.6 | 4 | 1 |
| [NBZN](#phase-nb-zn-nbzn); _phase:nb-zn:nbzn_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1393.73 K, x(Zn) 0.5–0.5 | 4 | 1 |
| [NBZN15](#phase-nb-zn-nbzn15); _phase:nb-zn:nbzn15_ | TiZn16 · oC68 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–701.54 K, x(Zn) 0.9375–0.9375 | 10 | 1 |
| [NBZN2_C36](#phase-nb-zn-nbzn2-c36); _phase:nb-zn:nbzn2-c36_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1328.33 K, x(Zn) 0.66667–0.66667 | 10 | 1 |
| [NBZN3_L12](#phase-nb-zn-nbzn3-l12); _phase:nb-zn:nbzn3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1307.05 K, x(Zn) 0.75–0.75 | 8 | 1 |
| [NBZN7](#phase-nb-zn-nbzn7); _phase:nb-zn:nbzn7_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–750.27 K, x(Zn) 0.875–0.875 | 4 | 1 |

## BCC_A2 (Nb–Zn)

- Id: `phase:nb-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2768.73 K, x(Zn) 0–0.00095
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:bcc-a2)

Names (3): _corpus: _corpus:phase:nb-zn:bcc-a2  
_paper: _paper:10.1007/s11669-016-0457-z:(Nb)  
_tdb: _tdb:NbZn-16Lon.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): BCC_A2, type code %B, sha256 `4ba787a0409d8de0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NB% ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Nb–Zn)

- Id: `phase:nb-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:fcc-a1)

Names (2): _corpus: _corpus:phase:nb-zn:fcc-a1  
_tdb: _tdb:NbZn-16Lon.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): FCC_A1, type code %A, sha256 `4ba787a0409d8de0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NB ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase_

## HCP_A3 (Nb–Zn)

- Id: `phase:nb-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–692.73 K, x(Zn) 0.9999–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:hcp-a3)

Names (3): _corpus: _corpus:phase:nb-zn:hcp-a3  
_paper: _paper:10.1007/s11669-016-0457-z:(Zn)  
_tdb: _tdb:NbZn-16Lon.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): HCP_A3, type code %A, sha256 `4ba787a0409d8de0…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NB ZN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Nb–Zn)

- Id: `phase:nb-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.23–4000 K, x(Zn) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:liquid)

Names (3): _corpus: _corpus:phase:nb-zn:liquid  
_paper: _paper:10.1007/s11669-016-0457-z:L  
_tdb: _tdb:NbZn-16Lon.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): LIQUID, type code %, sha256 `4ba787a0409d8de0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NB ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_

## NB2ZN3_D85 (Nb–Zn)

- Id: `phase:nb-zn:nb2zn3-d85`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D8_5; stoichiometry_contradicts_D8_5:NbZn-16Lon.tdb
- Candidate (literature_printed): Fe7W6 · hR13 — printed with a label mapped to this phase
- Candidate (name_token): Fe7W6 · D8_5 · hR13 · R-3m (166) — Strukturbericht/word 'D85' in the TDB name
- Candidate (sgte_mmc2): Fe7W6 · D8_5 · hR13 · R-3m (166) — Hallstedt 2025 mmc2 row for NB2ZN3_D85: Nb2Zn3
- Candidate (tdb_comment):  — NbZn-16Lon.tdb: 'Prototype Fe7W6 (hR13)'
- Stoichiometry: Nb 0.4000, Zn 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1387.75 K, x(Zn) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:nb2zn3-d85)

Names (3): _corpus: _corpus:phase:nb-zn:nb2zn3-d85  
_paper: _paper:10.1007/s11669-016-0457-z:NbZn1.5  
_tdb: _tdb:NbZn-16Lon.tdb:NB2ZN3_D85  


### TDB models of NB2ZN3_D85 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): NB2ZN3_D85, type code %, sha256 `4ba787a0409d8de0…`

~~~~text
46: PHASE NB2ZN3_D85 % 2 2 3 !
47: CONST NB2ZN3_D85 : NB : ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_

## NBZN (Nb–Zn)

- Id: `phase:nb-zn:nbzn`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (NbZn) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (NbZn) — Hallstedt 2025 mmc2 row for NBZN: NbZn
- Stoichiometry: Nb 0.5000, Zn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1393.73 K, x(Zn) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:nbzn)

Names (3): _corpus: _corpus:phase:nb-zn:nbzn  
_paper: _paper:10.1007/s11669-016-0457-z:NbZn  
_tdb: _tdb:NbZn-16Lon.tdb:NBZN  


### TDB models of NBZN (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): NBZN, type code %, sha256 `4ba787a0409d8de0…`

~~~~text
41: PHASE NBZN % 2 1 1 !
42: CONST NBZN : NB : ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_

## NBZN15 (Nb–Zn)

- Id: `phase:nb-zn:nbzn15`; status `assigned`
- Structure: TiZn16 · oC68 · Cmcm (63); type `st:tizn16-oc68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Nb 0.0625, Zn 0.9375
- Stability: stable in 1 of 1 calculated diagram(s): 300–701.54 K, x(Zn) 0.9375–0.9375
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:nbzn15)

Names (3): _corpus: _corpus:phase:nb-zn:nbzn15  
_paper: _paper:10.1007/s11669-016-0457-z:NbZn15  
_tdb: _tdb:NbZn-16Lon.tdb:NBZN15  


### TDB models of NBZN15 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): NBZN15, type code %, sha256 `4ba787a0409d8de0…`

~~~~text
66: PHASE NBZN15 % 2 1 15 !
67: CONST NBZN15 : NB : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.8091](https://doi.org/10.1006/jssc.1998.8091) Tono Nasch, Wolfgang Jeitschko, Niobium and Molybdenum Compounds with High Zinc Content: NbZn3, NbZn16, and MoZn20.44, Journal of Solid State Chemistry 143, 95-103 (1999).  
_cited as the source of values for this phase_

## NBZN2_C36 (Nb–Zn)

- Id: `phase:nb-zn:nbzn2-c36`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtoo and oqmd-17758, space group 194
- Stoichiometry: Nb 0.3333, Zn 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1328.33 K, x(Zn) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:nbzn2-c36)

Names (5): _corpus: _corpus:phase:nb-zn:nbzn2-c36  
_mp: _mp:mp-aaaabtoo  
_oqmd: _oqmd:oqmd-17758  
_paper: _paper:10.1007/s11669-016-0457-z:NbZn2  
_tdb: _tdb:NbZn-16Lon.tdb:NBZN2_C36  


### TDB models of NBZN2_C36 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): NBZN2_C36, type code %, sha256 `4ba787a0409d8de0…`

~~~~text
51: PHASE NBZN2_C36 % 2 1 2 !
52: CONST NBZN2_C36 : NB : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1107/s0365110x61003764](https://doi.org/10.1107/s0365110x61003764) C. L. Vold, The crystal structure of NbZn\<sub>2\</sub>, Acta Cryst 14, 1289-1290 (1961).  
_cited as the source of values for this phase_

## NBZN3_L12 (Nb–Zn)

- Id: `phase:nb-zn:nbzn3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabkr and oqmd-17759, space group 221
- Stoichiometry: Nb 0.2500, Zn 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1307.05 K, x(Zn) 0.75–0.75
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:nbzn3-l12)

Names (5): _corpus: _corpus:phase:nb-zn:nbzn3-l12  
_mp: _mp:mp-aaaaabkr  
_oqmd: _oqmd:oqmd-17759  
_paper: _paper:10.1007/s11669-016-0457-z:NbZn3  
_tdb: _tdb:NbZn-16Lon.tdb:NBZN3_L12  


### TDB models of NBZN3_L12 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): NBZN3_L12, type code %, sha256 `4ba787a0409d8de0…`

~~~~text
56: PHASE NBZN3_L12 % 2 1 3 !
57: CONST NBZN3_L12 : NB : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.8091](https://doi.org/10.1006/jssc.1998.8091) Tono Nasch, Wolfgang Jeitschko, Niobium and Molybdenum Compounds with High Zinc Content: NbZn3, NbZn16, and MoZn20.44, Journal of Solid State Chemistry 143, 95-103 (1999).  
_cited as the source of values for this phase_

## NBZN7 (Nb–Zn)

- Id: `phase:nb-zn:nbzn7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (NbZn7) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (NbZn7) — Hallstedt 2025 mmc2 row for NBZN7: NbZn7
- Stoichiometry: Nb 0.1250, Zn 0.8750
- Stability: stable in 1 of 1 calculated diagram(s): 300–750.27 K, x(Zn) 0.875–0.875
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zn:nbzn7)

Names (3): _corpus: _corpus:phase:nb-zn:nbzn7  
_paper: _paper:10.1007/s11669-016-0457-z:NbZn7  
_tdb: _tdb:NbZn-16Lon.tdb:NBZN7  


### TDB models of NBZN7 (1): PHASE and CONSTITUENT statements as written

[NbZn-16Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZn-16Lon.tdb): NBZN7, type code %, sha256 `4ba787a0409d8de0…`

~~~~text
61: PHASE NBZN7 % 2 1 7 !
62: CONST NBZN7 : NB : ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0457-z](https://doi.org/10.1007/s11669-016-0457-z) Zhaohui Long, Jin Gong, Jing Ding, Chihua Tang, Zhi Li, Fucheng Yin, Thermodynamic Assessment of Zn-Fe-Nb Ternary System, J. Phase Equilib. Diffus. 37, 293-300 (2016).  
_assessment that models this phase; reports values for this phase_

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
