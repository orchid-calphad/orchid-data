# C–Cr phases

> C–Cr system: 9 phases (tier A 6, tier C 2, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-CR.html · Markdown: https://data.orchid-project.org/phases/pages/C-CR.md

9 phases (tier A 6, tier C 2, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-CR) · [full JSON](https://data.orchid-project.org/phases/systems/C-CR.json) · [C–Cr system page](https://data.orchid-project.org/systems/C-CR.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-CR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Cr system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-cr-a4-diamond); _phase:c-cr:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [GRAPHITE_A9](#phase-c-cr-a9-graphite); _phase:c-cr:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 1–1 | 6 | 5 |
| [BCC_A2](#phase-c-cr-bcc-a2); _phase:c-cr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–3999.96 K, x(C) 0–0.00424 | 8 | 5 |
| [CR3C2_D510](#phase-c-cr-cr3c2-d510); _phase:c-cr:cr3c2-d510_ | Cr3C2 · D5_10 · oP20 · Pnma (62) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2140 K, x(C) 0.4–0.4 | 30 | 5 |
| [M7C3_D101](#phase-c-cr-d101-m7c3); _phase:c-cr:d101-m7c3_ | Cr7C3 · D10_1 · oP40 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–2054.69 K, x(C) 0.3–0.3 | 37 | 5 |
| [M23C6_D84](#phase-c-cr-d84-m23c6); _phase:c-cr:d84-m23c6_ | Cr23C6 · D8_4 · cF116 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–1889.69 K, x(C) 0.2069–0.2069 | 30 | 5 |
| [FCC_A1](#phase-c-cr-fcc-a1); _phase:c-cr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-c-cr-hcp-a3); _phase:c-cr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-c-cr-liquid); _phase:c-cr:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1799.28–4000 K, x(C) 0–0.62699 | 40 | 5 |

## DIAMOND_A4 (C–Cr)

- Id: `phase:c-cr:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:a4-diamond)

Names (6): _corpus: _corpus:phase:c-cr:a4-diamond  
_tdb: _tdb:CrC-04Ten.tdb:DIAMOND_A4, tdb:CrC-12Khv.tdb:DIAMOND_A4, tdb:CrC-87And-LB.tdb:DIAMOND_A4, tdb:CrC-90Kaj.tdb:DIAMOND_A4, tdb:CrC-92Lee.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): DIAMOND_A4, type code %, sha256 `c8336d57da4b1288…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : C : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): DIAMOND_A4, type code %, sha256 `ff1bea928fc2df4e…`

~~~~text
56: PHASE DIAMOND_A4 % 1 1 !
57: CONST DIAMOND_A4 : C : !
~~~~

[CrC-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-87And-LB.tdb): DIAMOND_A4, type code %, sha256 `6b5822923c2c9b71…`

~~~~text
35: PHASE DIAMOND_A4 % 1 1 !
36: CONST DIAMOND_A4 : C : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): DIAMOND_A4, type code %, sha256 `066ecf8dc98a16b2…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : C : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): DIAMOND_A4, type code %, sha256 `39d71e278a93190b…`

~~~~text
60: PHASE DIAMOND_A4 % 1 1 !
61: CONST DIAMOND_A4 : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90045-9](https://doi.org/10.1016/0364-5916%2887%2990045-9) Jan-Olof Andersson, Thermodynamic properties of Cr-C, Calphad 11, 271-276 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Cr)

- Id: `phase:c-cr:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:a9-graphite)

Names (8): _corpus: _corpus:phase:c-cr:a9-graphite  
_paper: _paper:10.1007/bf02646072:graphite, paper:10.1016/0364-5916(87)90045-9:Graphite  
_tdb: _tdb:CrC-04Ten.tdb:GRAPHITE_A9, tdb:CrC-12Khv.tdb:GRAPHITE_A9, tdb:CrC-87And-LB.tdb:GRAPHITE_A9, tdb:CrC-90Kaj.tdb:GRAPHITE_A9, tdb:CrC-92Lee.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (5): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): GRAPHITE_A9, type code %, sha256 `c8336d57da4b1288…`

~~~~text
54: PHASE GRAPHITE_A9 % 1 1 !
55: CONST GRAPHITE_A9 : C : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): GRAPHITE_A9, type code %, sha256 `ff1bea928fc2df4e…`

~~~~text
61: PHASE GRAPHITE_A9 % 1 1 !
62: CONST GRAPHITE_A9 : C : !
~~~~

[CrC-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-87And-LB.tdb): GRAPHITE_A9, type code %, sha256 `6b5822923c2c9b71…`

~~~~text
40: PHASE GRAPHITE_A9 % 1 1 !
41: CONST GRAPHITE_A9 : C : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): GRAPHITE_A9, type code %, sha256 `066ecf8dc98a16b2…`

~~~~text
57: PHASE GRAPHITE_A9 % 1 1 !
58: CONST GRAPHITE_A9 : C : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): GRAPHITE_A9, type code %, sha256 `39d71e278a93190b…`

~~~~text
65: PHASE GRAPHITE_A9 % 1 1 !
66: CONST GRAPHITE_A9 : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90045-9](https://doi.org/10.1016/0364-5916%2887%2990045-9) Jan-Olof Andersson, Thermodynamic properties of Cr-C, Calphad 11, 271-276 (1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase_

## BCC_A2 (C–Cr)

- Id: `phase:c-cr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–3999.96 K, x(C) 0–0.00424
- Literature: 8 values (8 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:bcc-a2)

Names (9): _corpus: _corpus:phase:c-cr:bcc-a2  
_paper: _paper:10.1007/bf02646072:Cr, paper:10.1016/0364-5916(87)90045-9:Bcc, paper:10.1016/j.calphad.2012.09.002:Cr  
_tdb: _tdb:CrC-04Ten.tdb:BCC_A2, tdb:CrC-12Khv.tdb:BCC_A2, tdb:CrC-87And-LB.tdb:BCC_A2, tdb:CrC-90Kaj.tdb:BCC_A2, tdb:CrC-92Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): BCC_A2, type code %B, sha256 `c8336d57da4b1288…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CR : C VA% : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): BCC_A2, type code %B, sha256 `ff1bea928fc2df4e…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : CR : C VA% : !
~~~~

[CrC-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-87And-LB.tdb): BCC_A2, type code %B, sha256 `6b5822923c2c9b71…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR : C VA% : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): BCC_A2, type code %B, sha256 `066ecf8dc98a16b2…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : CR : C VA% : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): BCC_A2, type code %B, sha256 `39d71e278a93190b…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : CR : C VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90045-9](https://doi.org/10.1016/0364-5916%2887%2990045-9) Jan-Olof Andersson, Thermodynamic properties of Cr-C, Calphad 11, 271-276 (1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_

## CR3C2_D510 (C–Cr)

- Id: `phase:c-cr:cr3c2-d510`; status `assigned`
- Structure: Cr3C2 · D5_10 · oP20 · Pnma (62); type `st:d5-10-cr3c2-op20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabezh and oqmd-2975, space group 62
- Stoichiometry: C 0.4000, Cr 0.6000
- Stability: stable in 5 of 5 calculated diagram(s): 300–2140 K, x(C) 0.4–0.4
- Literature: 30 values (28 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:cr3c2-d510)

Names (12): _corpus: _corpus:phase:c-cr:cr3c2-d510  
_mp: _mp:mp-aaaabezh  
_oqmd: _oqmd:oqmd-2975  
_paper: _paper:10.1007/bf02646072:Cr3C2, paper:10.1016/0364-5916(87)90045-9:Cr3C2, paper:10.1016/0364-5916(92)90002-f:Cr3C2, paper:10.1016/j.calphad.2012.09.002:Cr3C2  
_tdb: _tdb:CrC-04Ten.tdb:CR3C2_D510, tdb:CrC-12Khv.tdb:CR3C2_D510, tdb:CrC-87And-LB.tdb:CR3C2_D510, tdb:CrC-90Kaj.tdb:CR3C2_D510, tdb:CrC-92Lee.tdb:CR3C2_D510  


### TDB models of CR3C2_D510 (5): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): CR3C2_D510, type code %, sha256 `c8336d57da4b1288…`

~~~~text
69: PHASE CR3C2_D510 % 2 3 2 !
70: CONST CR3C2_D510 : CR : C : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): CR3C2_D510, type code %, sha256 `ff1bea928fc2df4e…`

~~~~text
76: PHASE CR3C2_D510 % 2 3 2 !
77: CONST CR3C2_D510 : CR : C : !
~~~~

[CrC-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-87And-LB.tdb): CR3C2_D510, type code %, sha256 `6b5822923c2c9b71…`

~~~~text
55: PHASE CR3C2_D510 % 2 3 2 !
56: CONST CR3C2_D510 : CR : C : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): CR3C2_D510, type code %, sha256 `066ecf8dc98a16b2…`

~~~~text
72: PHASE CR3C2_D510 % 2 3 2 !
73: CONST CR3C2_D510 : CR : C : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): CR3C2_D510, type code %, sha256 `39d71e278a93190b…`

~~~~text
80: PHASE CR3C2_D510 % 2 3 2 !
81: CONST CR3C2_D510 : CR : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90045-9](https://doi.org/10.1016/0364-5916%2887%2990045-9) Jan-Olof Andersson, Thermodynamic properties of Cr-C, Calphad 11, 271-276 (1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_

## M7C3_D101 (C–Cr)

- Id: `phase:c-cr:d101-m7c3`; status `assigned`
- Structure: Cr7C3 · D10_1 · oP40 · Pnma (62); type `st:d10-1-cr7c3-op40`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M7C3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.3000, Cr 0.7000
- Stability: stable in 5 of 5 calculated diagram(s): 300–2054.69 K, x(C) 0.3–0.3
- Literature: 37 values (36 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:d101-m7c3)

Names (11): _corpus: _corpus:phase:c-cr:d101-m7c3, corpus:phase:c-cr:m7c3-d101  
_paper: _paper:10.1007/bf02646072:Cr7C3, paper:10.1016/0364-5916(87)90045-9:Cr7C3, paper:10.1016/0364-5916(92)90002-f:Cr7C3, paper:10.1016/j.calphad.2012.09.002:Cr7C3  
_tdb: _tdb:CrC-04Ten.tdb:M7C3_D101, tdb:CrC-12Khv.tdb:M7C3_D101, tdb:CrC-87And-LB.tdb:M7C3_D101, tdb:CrC-90Kaj.tdb:M7C3_D101, tdb:CrC-92Lee.tdb:M7C3_D101  


### TDB models of M7C3_D101 (5): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): M7C3_D101, type code %, sha256 `c8336d57da4b1288…`

~~~~text
64: PHASE M7C3_D101 % 2 7 3 !
65: CONST M7C3_D101 : CR : C : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): M7C3_D101, type code %, sha256 `ff1bea928fc2df4e…`

~~~~text
71: PHASE M7C3_D101 % 2 7 3 !
72: CONST M7C3_D101 : CR : C : !
~~~~

[CrC-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-87And-LB.tdb): M7C3_D101, type code %, sha256 `6b5822923c2c9b71…`

~~~~text
50: PHASE M7C3_D101 % 2 7 3 !
51: CONST M7C3_D101 : CR : C : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): M7C3_D101, type code %, sha256 `066ecf8dc98a16b2…`

~~~~text
67: PHASE M7C3_D101 % 2 7 3 !
68: CONST M7C3_D101 : CR : C : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): M7C3_D101, type code %, sha256 `39d71e278a93190b…`

~~~~text
75: PHASE M7C3_D101 % 2 7 3 !
76: CONST M7C3_D101 : CR : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90045-9](https://doi.org/10.1016/0364-5916%2887%2990045-9) Jan-Olof Andersson, Thermodynamic properties of Cr-C, Calphad 11, 271-276 (1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_

## M23C6_D84 (C–Cr)

- Id: `phase:c-cr:d84-m23c6`; status `assigned`
- Structure: Cr23C6 · D8_4 · cF116 · Fm-3m (225); type `st:d8-4-cr23c6-cf116`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaaabbv and oqmd-2311, space group 225
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M23C6); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.2069, Cr 0.7931
- Stability: stable in 5 of 5 calculated diagram(s): 300–1889.69 K, x(C) 0.2069–0.2069
- Literature: 30 values (28 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:d84-m23c6)

Names (13): _corpus: _corpus:phase:c-cr:d84-m23c6, corpus:phase:c-cr:m23c6-d84  
_mp: _mp:mp-aaaaabbv  
_oqmd: _oqmd:oqmd-2311  
_paper: _paper:10.1007/bf02646072:Cr23C6, paper:10.1016/0364-5916(87)90045-9:Cr23C6, paper:10.1016/0364-5916(92)90002-f:Cr23C6, paper:10.1016/j.calphad.2012.09.002:Cr23C6  
_tdb: _tdb:CrC-04Ten.tdb:M23C6_D84, tdb:CrC-12Khv.tdb:M23C6_D84, tdb:CrC-87And-LB.tdb:M23C6_D84, tdb:CrC-90Kaj.tdb:M23C6_D84, tdb:CrC-92Lee.tdb:M23C6_D84  


### TDB models of M23C6_D84 (5): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): M23C6_D84, type code %, sha256 `c8336d57da4b1288…`

~~~~text
59: PHASE M23C6_D84 % 3 20 3 6 !
60: CONST M23C6_D84 : CR : CR : C : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): M23C6_D84, type code %, sha256 `ff1bea928fc2df4e…`

~~~~text
66: PHASE M23C6_D84 % 3 20 3 6 !
67: CONST M23C6_D84 : CR : CR : C : !
~~~~

[CrC-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-87And-LB.tdb): M23C6_D84, type code %, sha256 `6b5822923c2c9b71…`

~~~~text
45: PHASE M23C6_D84 % 3 20 3 6 !
46: CONST M23C6_D84 : CR : CR : C : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): M23C6_D84, type code %, sha256 `066ecf8dc98a16b2…`

~~~~text
62: PHASE M23C6_D84 % 3 20 3 6 !
63: CONST M23C6_D84 : CR : CR : C : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): M23C6_D84, type code %, sha256 `39d71e278a93190b…`

~~~~text
70: PHASE M23C6_D84 % 3 20 3 6 !
71: CONST M23C6_D84 : CR : CR : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90045-9](https://doi.org/10.1016/0364-5916%2887%2990045-9) Jan-Olof Andersson, Thermodynamic properties of Cr-C, Calphad 11, 271-276 (1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_

## FCC_A1 (C–Cr)

- Id: `phase:c-cr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:fcc-a1)

Names (5): _corpus: _corpus:phase:c-cr:fcc-a1  
_tdb: _tdb:CrC-04Ten.tdb:FCC_A1, tdb:CrC-12Khv.tdb:FCC_A1, tdb:CrC-90Kaj.tdb:FCC_A1, tdb:CrC-92Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): FCC_A1, type code %A, sha256 `c8336d57da4b1288…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CR : C VA% : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): FCC_A1, type code %A, sha256 `ff1bea928fc2df4e…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : CR : C VA% : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): FCC_A1, type code %A, sha256 `066ecf8dc98a16b2…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : CR : C VA% : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): FCC_A1, type code %A, sha256 `39d71e278a93190b…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : CR : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase_

## HCP_A3 (C–Cr)

- Id: `phase:c-cr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:hcp-a3)

Names (5): _corpus: _corpus:phase:c-cr:hcp-a3  
_tdb: _tdb:CrC-04Ten.tdb:HCP_A3, tdb:CrC-12Khv.tdb:HCP_A3, tdb:CrC-90Kaj.tdb:HCP_A3, tdb:CrC-92Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): HCP_A3, type code %A, sha256 `c8336d57da4b1288…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CR : C VA% : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): HCP_A3, type code %A, sha256 `ff1bea928fc2df4e…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : CR : C VA% : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): HCP_A3, type code %A, sha256 `066ecf8dc98a16b2…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CR : VA : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): HCP_A3, type code %A, sha256 `39d71e278a93190b…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : CR : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase_

## LIQUID (C–Cr)

- Id: `phase:c-cr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1799.28–4000 K, x(C) 0–0.62699
- Literature: 40 values (40 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cr:liquid)

Names (9): _corpus: _corpus:phase:c-cr:liquid  
_paper: _paper:10.1007/bf02646072:L, paper:10.1016/0364-5916(87)90045-9:L, paper:10.1016/j.calphad.2012.09.002:L  
_tdb: _tdb:CrC-04Ten.tdb:LIQUID, tdb:CrC-12Khv.tdb:LIQUID, tdb:CrC-87And-LB.tdb:LIQUID, tdb:CrC-90Kaj.tdb:LIQUID, tdb:CrC-92Lee.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[CrC-04Ten.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-04Ten.tdb): LIQUID, type code %, sha256 `c8336d57da4b1288…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : C CR : !
~~~~

[CrC-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-12Khv.tdb): LIQUID, type code %, sha256 `ff1bea928fc2df4e…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : C CR : !
~~~~

[CrC-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-87And-LB.tdb): LIQUID, type code %, sha256 `6b5822923c2c9b71…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C CR : !
~~~~

[CrC-90Kaj.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-90Kaj.tdb): LIQUID, type code %, sha256 `066ecf8dc98a16b2…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : C CR : !
~~~~

[CrC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrC-92Lee.tdb): LIQUID, type code %, sha256 `39d71e278a93190b…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : C CR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646072](https://doi.org/10.1007/BF02646072) M. Kajihara, M. Hillert, Metall. Trans. A, 21A, 2777-87(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90045-9](https://doi.org/10.1016/0364-5916%2887%2990045-9) Jan-Olof Andersson, Thermodynamic properties of Cr-C, Calphad 11, 271-276 (1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.002](https://doi.org/10.1016/j.calphad.2012.09.002) A.V. Khvan, B. Hallstedt, K. Chang, Thermodynamic assessment of Cr–Nb–C and Mn–Nb–C systems, Calphad 39, 54-61 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0273-7](https://doi.org/10.1007/s11661-004-0273-7) L. D. Teng, K. G. Lu, R. E. Aune, S. Seetharaman, Thermodynamic investigations of Cr3C2 and reassessment of the Cr-C system, Metall Mater Trans A 35, 3673-3680 (2004).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
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
