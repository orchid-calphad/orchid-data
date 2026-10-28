# Ca–Si phases

> Ca–Si system: 11 phases (tier A 8, tier C 2, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-SI.html · Markdown: https://data.orchid-project.org/phases/pages/CA-SI.md

11 phases (tier A 8, tier C 2, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-SI) · [full JSON](https://data.orchid-project.org/phases/systems/CA-SI.json) · [Ca–Si system page](https://data.orchid-project.org/systems/CA-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Si system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ca-si-a4-diamond); _phase:ca-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2498.95 K, x(Si) 1–1 | 3 | 2 |
| [BCC_A2](#phase-ca-si-bcc-a2); _phase:ca-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 716.03–1115 K, x(Si) 0–0 | 4 | 2 |
| [CA14SI19](#phase-ca-si-ca14si19); _phase:ca-si:ca14si19_ | Ca14Si19 · hR66 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1149.13–1356.72 K, x(Si) 0.57576–0.57576 | 11 | 1 |
| [CA2SI_C37](#phase-ca-si-ca2si-c37); _phase:ca-si:ca2si-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1576.82 K, x(Si) 0.33333–0.33333 | 18 | 2 |
| [CA3SI4](#phase-ca-si-ca3si4); _phase:ca-si:ca3si4_ | Ca3Si4 · hP42 · P6_3/m (176) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1206.52 K, x(Si) 0.57143–0.57143 | 6 | 1 |
| [CA5SI3_D8L](#phase-ca-si-ca5si3-d8l); _phase:ca-si:ca5si3-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1509.27 K, x(Si) 0.375–0.375 | 7 | 1 |
| [CASI_B33](#phase-ca-si-casi-b33); _phase:ca-si:casi-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1588.91 K, x(Si) 0.5–0.5 | 18 | 2 |
| [CASI2_C12](#phase-ca-si-casi2-c12); _phase:ca-si:casi2-c12_ | CaSi2 · C12 · hR6 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1303.36 K, x(Si) 0.66667–0.66667 | 18 | 2 |
| [FCC_A1](#phase-ca-si-fcc-a1); _phase:ca-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–716.03 K, x(Si) 0–0 | 1 | 2 |
| [HCP_A3](#phase-ca-si-hcp-a3); _phase:ca-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ca-si-liquid); _phase:ca-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1048.93–2500 K, x(Si) 0–1 | 22 | 2 |

## DIAMOND_A4 (Ca–Si)

- Id: `phase:ca-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2498.95 K, x(Si) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:a4-diamond)

Names (5): _corpus: _corpus:phase:ca-si:a4-diamond, corpus:phase:ca-si:diamond-a4  
_paper: _paper:10.1016/j.intermet.2003.07.001:(Si)  
_tdb: _tdb:CaSi-03Gro.tdb:DIAMOND_A4, tdb:CaSi-94Ang-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): DIAMOND_A4, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): DIAMOND_A4, type code %, sha256 `1769fd4ca474bf20…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_

## BCC_A2 (Ca–Si)

- Id: `phase:ca-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 716.03–1115 K, x(Si) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:bcc-a2)

Names (4): _corpus: _corpus:phase:ca-si:bcc-a2  
_paper: _paper:10.1016/j.intermet.2003.07.001:(βCa)  
_tdb: _tdb:CaSi-03Gro.tdb:BCC_A2, tdb:CaSi-94Ang-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): BCC_A2, type code %B, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CA% SI : VA : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): BCC_A2, type code %B, sha256 `1769fd4ca474bf20…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CA% SI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_

## CA14SI19 (Ca–Si)

- Id: `phase:ca-si:ca14si19`; status `assigned`
- Structure: Ca14Si19 · hR66 · R-3c (167); type `st:ca14si19-hr66`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.4242, Si 0.5758
- Stability: stable in 1 of 1 calculated diagram(s): 1149.13–1356.72 K, x(Si) 0.57576–0.57576
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:ca14si19)

Names (3): _corpus: _corpus:phase:ca-si:ca14si19  
_paper: _paper:10.1016/j.intermet.2003.07.001:Ca14Si19  
_tdb: _tdb:CaSi-03Gro.tdb:CA14SI19  


### TDB models of CA14SI19 (1): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): CA14SI19, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
68: PHASE CA14SI19 % 2 14 19 !
69: CONST CA14SI19 : CA : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
_cited as the source of values for this phase_

## CA2SI_C37 (Ca–Si)

- Id: `phase:ca-si:ca2si-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadsv and oqmd-4796, space group 62
- Stoichiometry: Ca 0.6667, Si 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1576.82 K, x(Si) 0.33333–0.33333
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:ca2si-c37)

Names (6): _corpus: _corpus:phase:ca-si:ca2si-c37  
_mp: _mp:mp-aaaaadsv  
_oqmd: _oqmd:oqmd-4796  
_paper: _paper:10.1016/j.intermet.2003.07.001:Ca2Si  
_tdb: _tdb:CaSi-03Gro.tdb:CA2SI_C37, tdb:CaSi-94Ang-LB.tdb:CA2SI_C37  


### TDB models of CA2SI_C37 (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): CA2SI_C37, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
48: PHASE CA2SI_C37 % 2 2 1 !
49: CONST CA2SI_C37 : CA : SI : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): CA2SI_C37, type code %, sha256 `1769fd4ca474bf20…`

~~~~text
53: PHASE CA2SI_C37 % 2 2 1 !
54: CONST CA2SI_C37 : CA : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_

## CA3SI4 (Ca–Si)

- Id: `phase:ca-si:ca3si4`; status `assigned`
- Structure: Ca3Si4 · hP42 · P6_3/m (176); type `st:ca3si4-hp42`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.4286, Si 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1206.52 K, x(Si) 0.57143–0.57143
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:ca3si4)

Names (3): _corpus: _corpus:phase:ca-si:ca3si4  
_paper: _paper:10.1016/j.intermet.2003.07.001:Ca3Si4  
_tdb: _tdb:CaSi-03Gro.tdb:CA3SI4  


### TDB models of CA3SI4 (1): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): CA3SI4, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
63: PHASE CA3SI4 % 2 3 4 !
64: CONST CA3SI4 : CA : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_

## CA5SI3_D8L (Ca–Si)

- Id: `phase:ca-si:ca5si3-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaben and oqmd-7693, space group 140
- Stoichiometry: Ca 0.6250, Si 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1509.27 K, x(Si) 0.375–0.375
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:ca5si3-d8l)

Names (5): _corpus: _corpus:phase:ca-si:ca5si3-d8l  
_mp: _mp:mp-aaaaaben  
_oqmd: _oqmd:oqmd-7693  
_paper: _paper:10.1016/j.intermet.2003.07.001:Ca5Si3  
_tdb: _tdb:CaSi-03Gro.tdb:CA5SI3_D8L  


### TDB models of CA5SI3_D8L (1): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): CA5SI3_D8L, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
53: PHASE CA5SI3_D8L % 2 5 3 !
54: CONST CA5SI3_D8L : CA : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
_cited as the source of values for this phase_

## CASI_B33 (Ca–Si)

- Id: `phase:ca-si:casi-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacid and oqmd-52884, space group 63
- Stoichiometry: Ca 0.5000, Si 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1588.91 K, x(Si) 0.5–0.5
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:casi-b33)

Names (6): _corpus: _corpus:phase:ca-si:casi-b33  
_mp: _mp:mp-aaaaacid  
_oqmd: _oqmd:oqmd-52884  
_paper: _paper:10.1016/j.intermet.2003.07.001:CaSi  
_tdb: _tdb:CaSi-03Gro.tdb:CASI_B33, tdb:CaSi-94Ang-LB.tdb:CASI_B33  


### TDB models of CASI_B33 (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): CASI_B33, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
58: PHASE CASI_B33 % 2 1 1 !
59: CONST CASI_B33 : CA : SI : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): CASI_B33, type code %, sha256 `1769fd4ca474bf20…`

~~~~text
58: PHASE CASI_B33 % 2 1 1 !
59: CONST CASI_B33 : CA : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02664227](https://doi.org/10.1007/bf02664227) J. R. Wynnyckyj, L. M. Pidgeon, Activities in the Ca-Si system, Metall Trans 2, 975-978 (1971).  
_cited as the source of values for this phase_

## CASI2_C12 (Ca–Si)

- Id: `phase:ca-si:casi2-c12`; status `assigned`
- Structure: CaSi2 · C12 · hR6 · R-3m (166); type `st:c12-casi2-hr6`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 0.3333, Si 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1303.36 K, x(Si) 0.66667–0.66667
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:casi2-c12)

Names (4): _corpus: _corpus:phase:ca-si:casi2-c12  
_paper: _paper:10.1016/j.intermet.2003.07.001:CaSi2  
_tdb: _tdb:CaSi-03Gro.tdb:CASI2_C12, tdb:CaSi-94Ang-LB.tdb:CASI2_C12  


### TDB models of CASI2_C12 (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): CASI2_C12, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
73: PHASE CASI2_C12 % 2 1 2 !
74: CONST CASI2_C12 : CA : SI : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): CASI2_C12, type code %, sha256 `1769fd4ca474bf20…`

~~~~text
63: PHASE CASI2_C12 % 2 1 2 !
64: CONST CASI2_C12 : CA : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02664227](https://doi.org/10.1007/bf02664227) J. R. Wynnyckyj, L. M. Pidgeon, Activities in the Ca-Si system, Metall Trans 2, 975-978 (1971).  
_cited as the source of values for this phase_

## FCC_A1 (Ca–Si)

- Id: `phase:ca-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–716.03 K, x(Si) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:fcc-a1)

Names (4): _corpus: _corpus:phase:ca-si:fcc-a1  
_paper: _paper:10.1016/j.intermet.2003.07.001:(αCa)  
_tdb: _tdb:CaSi-03Gro.tdb:FCC_A1, tdb:CaSi-94Ang-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): FCC_A1, type code %A, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CA% SI : VA : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): FCC_A1, type code %A, sha256 `1769fd4ca474bf20…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CA% SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase_

## HCP_A3 (Ca–Si)

- Id: `phase:ca-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:hcp-a3)

Names (3): _corpus: _corpus:phase:ca-si:hcp-a3  
_tdb: _tdb:CaSi-03Gro.tdb:HCP_A3, tdb:CaSi-94Ang-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): HCP_A3, type code %A, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CA SI : VA : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): HCP_A3, type code %A, sha256 `1769fd4ca474bf20…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CA SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase_

## LIQUID (Ca–Si)

- Id: `phase:ca-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1048.93–2500 K, x(Si) 0–1
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-si:liquid)

Names (4): _corpus: _corpus:phase:ca-si:liquid  
_paper: _paper:10.1016/j.intermet.2003.07.001:L  
_tdb: _tdb:CaSi-03Gro.tdb:LIQUID, tdb:CaSi-94Ang-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CaSi-03Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-03Gro.tdb): LIQUID, type code %, sha256 `ee18ca4a4c4fd9e2…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CA SI : !
~~~~

[CaSi-94Ang-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSi-94Ang-LB.tdb): LIQUID, type code %, sha256 `1769fd4ca474bf20…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CA SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2003.07.001](https://doi.org/10.1016/j.intermet.2003.07.001) Joachim Gröbner, Igor Chumak, Rainer Schmid-Fetzer, Experimental study of ternary Ca–Mg–Si phase equilibria and thermodynamic assessment of Ca–Si and Ca–Mg–Si systems, Intermetallics 11, 1065-1074 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90034-5](https://doi.org/10.1016/0364-5916%2894%2990034-5) J.C. Anglezio, C. Servant, I. Ansara, Contribution to the experimental and thermodynamic assessment of the AlCaFeSi system—I. AlCaFe, AlCaSi, AlFeSi and CaFeSi systems, Calphad 18, 273-309 (1994).  
_assessment that models this phase_
- [doi:10.1016/s0966-9795(99)00112-0](https://doi.org/10.1016/s0966-9795%2899%2900112-0) P. Manfrinetti, M.L. Fornasini, A. Palenzona, The phase diagram of the Ca–Si system, Intermetallics 8, 223-228 (2000).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.197503664](https://doi.org/10.1002/srin.197503664) Eberhard Schürmann, Peter Fünders, Hans Litterscheidt, Dampfdruck des Calciums über Calcium‐Silicium‐ und Calcium‐Aluminium‐Schmelzen sowie über Calcium‐Aluminium‐Silicium‐Legierungen, Steel Research Intl 46, 473-476 (1975).  
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
