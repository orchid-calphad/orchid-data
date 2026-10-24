# Ba–Pb phases

> Ba–Pb system: 11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-PB.html · Markdown: https://data.orchid-project.org/phases/pages/BA-PB.md

11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-PB) · [full JSON](https://data.orchid-project.org/phases/systems/BA-PB.json) · [Ba–Pb system page](https://data.orchid-project.org/systems/BA-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–Pb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BA17PB23](#phase-ba-pb-ba17pb23); _phase:ba-pb:ba17pb23_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1110.87 K, x(Pb) 0.575–0.575 | 8 | 1 |
| [BA2PB_C37](#phase-ba-pb-ba2pb-c37); _phase:ba-pb:ba2pb-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1184.64 K, x(Pb) 0.33333–0.33333 | 8 | 1 |
| [BA3PB5_HT](#phase-ba-pb-ba3pb5-ht); _phase:ba-pb:ba3pb5-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 977.58–986.14 K, x(Pb) 0.625–0.625 | 11 | 1 |
| [BA3PB5_LT](#phase-ba-pb-ba3pb5-lt); _phase:ba-pb:ba3pb5-lt_ | Pd5Pu3 · oC32 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–977.58 K, x(Pb) 0.625–0.625 | 13 | 1 |
| [BA5PB3_D8L](#phase-ba-pb-ba5pb3-d8l); _phase:ba-pb:ba5pb3-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1243.81 K, x(Pb) 0.375–0.375 | 12 | 1 |
| [BAPB_B33](#phase-ba-pb-bapb-b33); _phase:ba-pb:bapb-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1126.91 K, x(Pb) 0.5–0.5 | 12 | 1 |
| [BAPB3](#phase-ba-pb-bapb3); _phase:ba-pb:bapb3_ | BaPb3 · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–870.28 K, x(Pb) 0.75–0.75 | 11 | 1 |
| [BCC_A2](#phase-ba-pb-bcc-a2); _phase:ba-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1004 K, x(Pb) 0–0.00133 | 3 | 1 |
| [FCC_A1](#phase-ba-pb-fcc-a1); _phase:ba-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–601.61 K, x(Pb) 0.99184–1 | 2 | 1 |
| [HCP_A3](#phase-ba-pb-hcp-a3); _phase:ba-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ba-pb-liquid); _phase:ba-pb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 563.12–2500 K, x(Pb) 0–1 | 43 | 1 |

## BA17PB23 (Ba–Pb)

- Id: `phase:ba-pb:ba17pb23`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Ba17Pb23) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ba17Pb23) — Hallstedt 2025 mmc2 row for BA17PB23: Ba17Pb23
- Stoichiometry: Ba 0.4250, Pb 0.5750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1110.87 K, x(Pb) 0.575–0.575
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:ba17pb23)

Names (3): _corpus: _corpus:phase:ba-pb:ba17pb23  
_paper: _paper:10.1016/j.calphad.2007.04.003:Ba0.425Pb0.575  
_tdb: _tdb:BaPb-07Idb.tdb:BA17PB23  


### TDB models of BA17PB23 (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BA17PB23, type code %, sha256 `faf589a587c1792e…`

~~~~text
68: PHASE BA17PB23 % 2 17 23 !
69: CONST BA17PB23 : BA : PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_

## BA2PB_C37 (Ba–Pb)

- Id: `phase:ba-pb:ba2pb-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabfle and oqmd-10855, space group 62
- Stoichiometry: Ba 0.6667, Pb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1184.64 K, x(Pb) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:ba2pb-c37)

Names (5): _corpus: _corpus:phase:ba-pb:ba2pb-c37  
_mp: _mp:mp-aaaabfle  
_oqmd: _oqmd:oqmd-10855  
_paper: _paper:10.1016/j.calphad.2007.04.003:Ba2Pb  
_tdb: _tdb:BaPb-07Idb.tdb:BA2PB_C37  


### TDB models of BA2PB_C37 (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BA2PB_C37, type code %, sha256 `faf589a587c1792e…`

~~~~text
53: PHASE BA2PB_C37 % 2 2 1 !
54: CONST BA2PB_C37 : BA : PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## BA3PB5_HT (Ba–Pb)

- Id: `phase:ba-pb:ba3pb5-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Cmcm (63) — on-hull MP Ba3Pb5 at x(PB)=0.6250
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Ba3 Pb5 at x(PB)=0.6250
- Candidate (literature_printed): (Ba3Pb5) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ba3Pb5) — Hallstedt 2025 mmc2 row for BA3PB5_HT: Ba3Pb5 (high T)
- Stoichiometry: Ba 0.3750, Pb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 977.58–986.14 K, x(Pb) 0.625–0.625
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:ba3pb5-ht)

Names (3): _corpus: _corpus:phase:ba-pb:ba3pb5-ht  
_paper: _paper:10.1016/j.calphad.2007.04.003:βBa3Pb5  
_tdb: _tdb:BaPb-07Idb.tdb:BA3PB5_HT  


### TDB models of BA3PB5_HT (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BA3PB5_HT, type code %, sha256 `faf589a587c1792e…`

~~~~text
78: PHASE BA3PB5_HT % 2 3 5 !
79: CONST BA3PB5_HT : BA : PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## BA3PB5_LT (Ba–Pb)

- Id: `phase:ba-pb:ba3pb5-lt`; status `assigned`
- Structure: Pd5Pu3 · oC32 · Cmcm (63); type `st:pd5pu3-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ba 0.3750, Pb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–977.58 K, x(Pb) 0.625–0.625
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:ba3pb5-lt)

Names (3): _corpus: _corpus:phase:ba-pb:ba3pb5-lt  
_paper: _paper:10.1016/j.calphad.2007.04.003:αBa3Pb5  
_tdb: _tdb:BaPb-07Idb.tdb:BA3PB5_LT  


### TDB models of BA3PB5_LT (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BA3PB5_LT, type code %, sha256 `faf589a587c1792e…`

~~~~text
73: PHASE BA3PB5_LT % 2 3 5 !
74: CONST BA3PB5_LT : BA : PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## BA5PB3_D8L (Ba–Pb)

- Id: `phase:ba-pb:ba5pb3-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Ba 0.6250, Pb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1243.81 K, x(Pb) 0.375–0.375
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:ba5pb3-d8l)

Names (3): _corpus: _corpus:phase:ba-pb:ba5pb3-d8l  
_paper: _paper:10.1016/j.calphad.2007.04.003:Ba5Pb3  
_tdb: _tdb:BaPb-07Idb.tdb:BA5PB3_D8L  


### TDB models of BA5PB3_D8L (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BA5PB3_D8L, type code %, sha256 `faf589a587c1792e…`

~~~~text
58: PHASE BA5PB3_D8L % 2 5 3 !
59: CONST BA5PB3_D8L : BA : PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## BAPB_B33 (Ba–Pb)

- Id: `phase:ba-pb:bapb-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdum and oqmd-10853, space group 63
- Stoichiometry: Ba 0.5000, Pb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1126.91 K, x(Pb) 0.5–0.5
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:bapb-b33)

Names (5): _corpus: _corpus:phase:ba-pb:bapb-b33  
_mp: _mp:mp-aaaabdum  
_oqmd: _oqmd:oqmd-10853  
_paper: _paper:10.1016/j.calphad.2007.04.003:BaPb  
_tdb: _tdb:BaPb-07Idb.tdb:BAPB_B33  


### TDB models of BAPB_B33 (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BAPB_B33, type code %, sha256 `faf589a587c1792e…`

~~~~text
63: PHASE BAPB_B33 % 2 1 1 !
64: CONST BAPB_B33 : BA : PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## BAPB3 (Ba–Pb)

- Id: `phase:ba-pb:bapb3`; status `assigned`
- Structure: BaPb3 · hR12 · R-3m (166); type `st:bapb3-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ba 0.2500, Pb 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–870.28 K, x(Pb) 0.75–0.75
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:bapb3)

Names (3): _corpus: _corpus:phase:ba-pb:bapb3  
_paper: _paper:10.1016/j.calphad.2007.04.003:BaPb3  
_tdb: _tdb:BaPb-07Idb.tdb:BAPB3  


### TDB models of BAPB3 (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BAPB3, type code %, sha256 `faf589a587c1792e…`

~~~~text
83: PHASE BAPB3 % 2 1 3 !
84: CONST BAPB3 : BA : PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## BCC_A2 (Ba–Pb)

- Id: `phase:ba-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1004 K, x(Pb) 0–0.00133
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:bcc-a2)

Names (3): _corpus: _corpus:phase:ba-pb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2007.04.003:(Ba)  
_tdb: _tdb:BaPb-07Idb.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): BCC_A2, type code %B, sha256 `faf589a587c1792e…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : BA% PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ba–Pb)

- Id: `phase:ba-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–601.61 K, x(Pb) 0.99184–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:fcc-a1)

Names (3): _corpus: _corpus:phase:ba-pb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2007.04.003:(Pb)  
_tdb: _tdb:BaPb-07Idb.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): FCC_A1, type code %A, sha256 `faf589a587c1792e…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : BA PB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## HCP_A3 (Ba–Pb)

- Id: `phase:ba-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:hcp-a3)

Names (2): _corpus: _corpus:phase:ba-pb:hcp-a3  
_tdb: _tdb:BaPb-07Idb.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): HCP_A3, type code %A, sha256 `faf589a587c1792e…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : BA PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase_

## LIQUID (Ba–Pb)

- Id: `phase:ba-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 563.12–2500 K, x(Pb) 0–1
- Literature: 43 values (43 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-pb:liquid)

Names (3): _corpus: _corpus:phase:ba-pb:liquid  
_paper: _paper:10.1016/j.calphad.2007.04.003:Liq  
_tdb: _tdb:BaPb-07Idb.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BaPb-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb): LIQUID, type code %, sha256 `faf589a587c1792e…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : BA BAPB PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(77)90003-0](https://doi.org/10.1016/0022-5088%2877%2990003-0) Giacomo Bruzzone, Enrico Franceschi, Equilibrium phase diagram and crystal structures of the intermediate phases of the Ba-Pb binary system, Journal of the Less Common Metals 52, 211-216 (1977).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
