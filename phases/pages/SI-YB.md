# Si–Yb phases

> Si–Yb system: 11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-YB.html · Markdown: https://data.orchid-project.org/phases/pages/SI-YB.md

11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-YB) · [full JSON](https://data.orchid-project.org/phases/systems/SI-YB.json) · [Si–Yb system page](https://data.orchid-project.org/systems/SI-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–Yb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-yb-a4-diamond); _phase:si-yb:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1689.32 K, x(Yb) 0–0 | 7 | 1 |
| [BCC_A2](#phase-si-yb-bcc-a2); _phase:si-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1033–2499.95 K, x(Yb) 1–1 | 4 | 1 |
| [FCC_A1](#phase-si-yb-fcc-a1); _phase:si-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1033 K, x(Yb) 1–1 | 0 | 1 |
| [HCP_A3](#phase-si-yb-hcp-a3); _phase:si-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-si-yb-liquid); _phase:si-yb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1096.2–2500 K, x(Yb) 0–1 | 48 | 1 |
| [SI11YB8](#phase-si-yb-si11yb8); _phase:si-yb:si11yb8_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1257.13 K, x(Yb) 0.42105–0.42105 | 6 | 1 |
| [SI2YB_C32](#phase-si-yb-si2yb-c32); _phase:si-yb:si2yb-c32_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1034.45–1676.97 K, x(Yb) 0.36496–0.36496 | 16 | 1 |
| [SI3YB5_D88](#phase-si-yb-si3yb5-d88); _phase:si-yb:si3yb5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1890.67 K, x(Yb) 0.625–0.625 | 4 | 1 |
| [SI4YB5](#phase-si-yb-si4yb5); _phase:si-yb:si4yb5_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1939.13 K, x(Yb) 0.55556–0.55556 | 4 | 1 |
| [SI5YB3](#phase-si-yb-si5yb3); _phase:si-yb:si5yb3_ | Pd5Th3 · hP8 · P-62m (189) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1241.98 K, x(Yb) 0.375–0.375 | 7 | 1 |
| [SIYB_B27](#phase-si-yb-siyb-b27); _phase:si-yb:siyb-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1960.77 K, x(Yb) 0.5–0.5 | 10 | 1 |

## DIAMOND_A4 (Si–Yb)

- Id: `phase:si-yb:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1689.32 K, x(Yb) 0–0
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:a4-diamond)

Names (4): _corpus: _corpus:phase:si-yb:a4-diamond, corpus:phase:si-yb:diamond-a4  
_paper: _paper:10.1016/j.calphad.2005.06.004:Si  
_tdb: _tdb:SiYb-05Bru.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): DIAMOND_A4, type code %, sha256 `69e87e54956cef3f…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.2001.9390](https://doi.org/10.1006/jssc.2001.9390) A. Grytsiv, D. Kaczorowski, A. Leithe-Jasper, V.H. Tran, A. Pikul, P. Rogl et al., On the System Silicon–Ytterbium: Constitution, Crystal Chemistry, and Physical Properties, Journal of Solid State Chemistry 163, 178-185 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(03)00152-3](https://doi.org/10.1016/s0966-9795%2803%2900152-3) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona, Thermochemistry of ytterbium silicides, Intermetallics 11, 1153-1159 (2003).  
_cited as the source of values for this phase_

## BCC_A2 (Si–Yb)

- Id: `phase:si-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1033–2499.95 K, x(Yb) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:bcc-a2)

Names (3): _corpus: _corpus:phase:si-yb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2005.06.004:Yb(bcc)  
_tdb: _tdb:SiYb-05Bru.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): BCC_A2, type code %B, sha256 `69e87e54956cef3f…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : SI YB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Si–Yb)

- Id: `phase:si-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1033 K, x(Yb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:fcc-a1)

Names (2): _corpus: _corpus:phase:si-yb:fcc-a1  
_tdb: _tdb:SiYb-05Bru.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): FCC_A1, type code %A, sha256 `69e87e54956cef3f…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : SI YB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase_

## HCP_A3 (Si–Yb)

- Id: `phase:si-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:hcp-a3)

Names (2): _corpus: _corpus:phase:si-yb:hcp-a3  
_tdb: _tdb:SiYb-05Bru.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): HCP_A3, type code %A, sha256 `69e87e54956cef3f…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 :  SI YB : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase_

## LIQUID (Si–Yb)

- Id: `phase:si-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1096.2–2500 K, x(Yb) 0–1
- Literature: 48 values (48 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:liquid)

Names (5): _corpus: _corpus:phase:si-yb:liquid  
_paper: _paper:10.1016/j.calphad.2005.06.004:L, paper:10.1016/j.calphad.2005.06.004:liquid, paper:10.1016/j.calphad.2005.06.004:liquid solution  
_tdb: _tdb:SiYb-05Bru.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): LIQUID, type code %, sha256 `69e87e54956cef3f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : SI YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.2001.9390](https://doi.org/10.1006/jssc.2001.9390) A. Grytsiv, D. Kaczorowski, A. Leithe-Jasper, V.H. Tran, A. Pikul, P. Rogl et al., On the System Silicon–Ytterbium: Constitution, Crystal Chemistry, and Physical Properties, Journal of Solid State Chemistry 163, 178-185 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/j.optmat.2004.08.040](https://doi.org/10.1016/j.optmat.2004.08.040) Zhengxin Liu, Masato Osamura, Teruhisa Ootsuka, Shinan Wang, Yasuhiro Fukuzawa, Yasuhito Suzuki et al., Doping of β-FeSi2 films with boron and arsenic by sputtering and its application for optoelectronic devices, Optical Materials 27, 942-947 (2005).  
_cited as the source of values for this phase_

## SI11YB8 (Si–Yb)

- Id: `phase:si-yb:si11yb8`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): Si11Yb8 · oI38 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Si11Yb8 · oI38 — Hallstedt 2025 mmc2 row for SI11YB8: Si11Yb8
- Candidate (tdb_comment):  — SiYb-05Bru.tdb: 'Prototype Si11Yb8 (oI38)'
- Stoichiometry: Si 0.5789, Yb 0.4211
- Stability: stable in 1 of 1 calculated diagram(s): 300–1257.13 K, x(Yb) 0.42105–0.42105
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:si11yb8)

Names (3): _corpus: _corpus:phase:si-yb:si11yb8  
_paper: _paper:10.1016/j.calphad.2005.06.004:Yb8Si11  
_tdb: _tdb:SiYb-05Bru.tdb:SI11YB8  


### TDB models of SI11YB8 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): SI11YB8, type code %, sha256 `69e87e54956cef3f…`

~~~~text
65: PHASE SI11YB8 % 2 11 8 !
66: CONST SI11YB8 : SI : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(03)00152-3](https://doi.org/10.1016/s0966-9795%2803%2900152-3) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona, Thermochemistry of ytterbium silicides, Intermetallics 11, 1153-1159 (2003).  
_cited as the source of values for this phase_

## SI2YB_C32 (Si–Yb)

- Id: `phase:si-yb:si2yb-c32`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C32; stoichiometry_contradicts_C32:SiYb-05Bru.tdb
- Candidate (literature_printed): AlB2 · hP3 — printed with a label mapped to this phase
- Candidate (name_token): AlB2 · C32 · hP3 · P6/mmm (191) — Strukturbericht/word 'C32' in the TDB name
- Candidate (sgte_mmc2): AlB2 · C32 · hP3 · P6/mmm (191) — Hallstedt 2025 mmc2 row for SI2YB_C32: Si1.74Yb
- Candidate (tdb_comment): AlB2 · hP3 · P6/mmm — SiYb-05Bru.tdb: 'Prototype AlB2 (hP3, P6/mmm), Si1.74Yb'
- Stoichiometry: Si 0.6350, Yb 0.3650
- Stability: stable in 1 of 1 calculated diagram(s): 1034.45–1676.97 K, x(Yb) 0.36496–0.36496
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:si2yb-c32)

Names (3): _corpus: _corpus:phase:si-yb:si2yb-c32  
_paper: _paper:10.1016/j.calphad.2005.06.004:YbSi1.74  
_tdb: _tdb:SiYb-05Bru.tdb:SI2YB_C32  


### TDB models of SI2YB_C32 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): SI2YB_C32, type code %, sha256 `69e87e54956cef3f…`

~~~~text
75: PHASE SI2YB_C32 % 2 1.74 1 !
76: CONST SI2YB_C32 : SI : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.2001.9390](https://doi.org/10.1006/jssc.2001.9390) A. Grytsiv, D. Kaczorowski, A. Leithe-Jasper, V.H. Tran, A. Pikul, P. Rogl et al., On the System Silicon–Ytterbium: Constitution, Crystal Chemistry, and Physical Properties, Journal of Solid State Chemistry 163, 178-185 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(03)00152-3](https://doi.org/10.1016/s0966-9795%2803%2900152-3) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona, Thermochemistry of ytterbium silicides, Intermetallics 11, 1153-1159 (2003).  
_cited as the source of values for this phase_

## SI3YB5_D88 (Si–Yb)

- Id: `phase:si-yb:si3yb5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.3750, Yb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1890.67 K, x(Yb) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:si3yb5-d88)

Names (3): _corpus: _corpus:phase:si-yb:si3yb5-d88  
_paper: _paper:10.1016/j.calphad.2005.06.004:Yb5Si3  
_tdb: _tdb:SiYb-05Bru.tdb:SI3YB5_D88  


### TDB models of SI3YB5_D88 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): SI3YB5_D88, type code %, sha256 `69e87e54956cef3f…`

~~~~text
50: PHASE SI3YB5_D88 % 2 3 5 !
51: CONST SI3YB5_D88 : SI : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_

## SI4YB5 (Si–Yb)

- Id: `phase:si-yb:si4yb5`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Si 0.4444, Yb 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–1939.13 K, x(Yb) 0.55556–0.55556
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:si4yb5)

Names (3): _corpus: _corpus:phase:si-yb:si4yb5  
_paper: _paper:10.1016/j.calphad.2005.06.004:Yb5Si4  
_tdb: _tdb:SiYb-05Bru.tdb:SI4YB5  


### TDB models of SI4YB5 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): SI4YB5, type code %, sha256 `69e87e54956cef3f…`

~~~~text
55: PHASE SI4YB5 % 2 4 5 !
56: CONST SI4YB5 : SI : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_

## SI5YB3 (Si–Yb)

- Id: `phase:si-yb:si5yb3`; status `assigned`
- Structure: Pd5Th3 · hP8 · P-62m (189); type `st:pd5th3-hp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Si 0.6250, Yb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1241.98 K, x(Yb) 0.375–0.375
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:si5yb3)

Names (3): _corpus: _corpus:phase:si-yb:si5yb3  
_paper: _paper:10.1016/j.calphad.2005.06.004:Yb3Si5  
_tdb: _tdb:SiYb-05Bru.tdb:SI5YB3  


### TDB models of SI5YB3 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): SI5YB3, type code %, sha256 `69e87e54956cef3f…`

~~~~text
70: PHASE SI5YB3 % 2 5 3 !
71: CONST SI5YB3 : SI : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(03)00152-3](https://doi.org/10.1016/s0966-9795%2803%2900152-3) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona, Thermochemistry of ytterbium silicides, Intermetallics 11, 1153-1159 (2003).  
_cited as the source of values for this phase_
- [doi:10.1006/jssc.2001.9390](https://doi.org/10.1006/jssc.2001.9390) A. Grytsiv, D. Kaczorowski, A. Leithe-Jasper, V.H. Tran, A. Pikul, P. Rogl et al., On the System Silicon–Ytterbium: Constitution, Crystal Chemistry, and Physical Properties, Journal of Solid State Chemistry 163, 178-185 (2002).  
_cited as the source of values for this phase_

## SIYB_B27 (Si–Yb)

- Id: `phase:si-yb:siyb-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.5000, Yb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1960.77 K, x(Yb) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-yb:siyb-b27)

Names (3): _corpus: _corpus:phase:si-yb:siyb-b27  
_paper: _paper:10.1016/j.calphad.2005.06.004:YbSi  
_tdb: _tdb:SiYb-05Bru.tdb:SIYB_B27  


### TDB models of SIYB_B27 (1): PHASE and CONSTITUENT statements as written

[SiYb-05Bru.tdb](https://orchid-project.org/data/databases/sgte-binary/SiYb-05Bru.tdb): SIYB_B27, type code %, sha256 `69e87e54956cef3f…`

~~~~text
60: PHASE SIYB_B27 % 2 1 1 !
61: CONST SIYB_B27 : SI : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.06.004](https://doi.org/10.1016/j.calphad.2005.06.004) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, Thermodynamic assessment of the Yb–Si system, Calphad 29, 254-261 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.2001.9390](https://doi.org/10.1006/jssc.2001.9390) A. Grytsiv, D. Kaczorowski, A. Leithe-Jasper, V.H. Tran, A. Pikul, P. Rogl et al., On the System Silicon–Ytterbium: Constitution, Crystal Chemistry, and Physical Properties, Journal of Solid State Chemistry 163, 178-185 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(03)00152-3](https://doi.org/10.1016/s0966-9795%2803%2900152-3) S. Brutti, G. Balducci, A. Ciccioli, G. Gigli, P. Manfrinetti, A. Palenzona, Thermochemistry of ytterbium silicides, Intermetallics 11, 1153-1159 (2003).  
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
