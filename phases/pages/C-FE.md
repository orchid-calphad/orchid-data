# C–Fe phases

> C–Fe system: 12 phases (tier A 6, tier C 1, liquid 1, needs_review 2, unresolved_no_candidates 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-FE.html · Markdown: https://data.orchid-project.org/phases/pages/C-FE.md

12 phases (tier A 6, tier C 1, liquid 1, needs_review 2, unresolved_no_candidates 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-FE) · [full JSON](https://data.orchid-project.org/phases/systems/C-FE.json) · [C–Fe system page](https://data.orchid-project.org/systems/C-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Fe system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-fe-a4-diamond); _phase:c-fe:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 9 calculated diagram(s) | 0 | 9 |
| [GRAPHITE_A9](#phase-c-fe-a9-graphite); _phase:c-fe:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–2500 K, x(C) 1–1 | 0 | 9 |
| [BCC_A2](#phase-c-fe-bcc-a2); _phase:c-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–2499.69 K, x(C) 0–0.00626 | 4 | 9 |
| [BCC_ALT](#phase-c-fe-bcc-alt); _phase:c-fe:bcc-alt_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300.82–2345.95 K, x(C) 0–0.00308 | 0 | 1 |
| [BCT_Z1](#phase-c-fe-bct-z1); _phase:c-fe:bct-z1_ |  | unresolved_no_candidates | stable in 1 of 1 calculated diagram(s): 300–1800 K, x(C) 0.5–0.5 | 0 | 1 |
| [BCT_Z2](#phase-c-fe-bct-z2); _phase:c-fe:bct-z2_ |  | unresolved_no_candidates | stable in 1 of 1 calculated diagram(s): 300.4–2499.12 K, x(C) 0–0.00626 | 0 | 1 |
| [CEMENTITE_D011](#phase-c-fe-cementite-d011); _phase:c-fe:cementite-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 2 of 9 calculated diagram(s): 1010–1416.1 K, x(C) 0.25–0.25 | 0 | 9 |
| [M2C_ETA](#phase-c-fe-eta-m2c); _phase:c-fe:eta-m2c_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-c-fe-fcc-a1); _phase:c-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 1009.04–1768.83 K, x(C) 0–0.08879 | 3 | 9 |
| [HCP_A3](#phase-c-fe-hcp-a3); _phase:c-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 8 calculated diagram(s) | 0 | 8 |
| [LIQUID](#phase-c-fe-liquid); _phase:c-fe:liquid_ | liquid | liquid | stable in 9 of 9 calculated diagram(s): 1415.24–2500 K, x(C) 0–0.27456 | 5 | 9 |
| [M5C2](#phase-c-fe-m5c2); _phase:c-fe:m5c2_ | Mn5C2 · mC28 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |

## DIAMOND_A4 (C–Fe)

- Id: `phase:c-fe:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 9 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:a4-diamond)

Names (10): _corpus: _corpus:phase:c-fe:a4-diamond  
_tdb: _tdb:FeC-10Hal.tdb:DIAMOND_A4, tdb:FeC-14Nar-3g.tdb:DIAMOND_A4, tdb:FeC-16Goh.tdb:DIAMOND_A4, tdb:FeC-19Che.tdb:DIAMOND_A4, tdb:FeC-19Mie.tdb:DIAMOND_A4, tdb:FeC-20Sae.tdb:DIAMOND_A4, tdb:FeC-23Jac.tdb:DIAMOND_A4, tdb:FeC-24Eno.tdb:DIAMOND_A4, tdb:FeC-85Gus-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (9): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): DIAMOND_A4, type code %, sha256 `7b87dfe21503206d…`

~~~~text
72: PHASE DIAMOND_A4 % 1 1 !
73: CONST DIAMOND_A4 : C : !
~~~~

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): DIAMOND_A4, type code %, sha256 `2ac51900c8c0ad3b…`

~~~~text
56: PHASE DIAMOND_A4 % 1 1 !
57: CONST DIAMOND_A4 : C : !
~~~~

[FeC-16Goh.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-16Goh.tdb): DIAMOND_A4, type code %, sha256 `f7f205bbf9b6e594…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : C : !
~~~~

[FeC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Che.tdb): DIAMOND_A4, type code %, sha256 `fe32281d077aba24…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : C : !
~~~~

[FeC-19Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Mie.tdb): DIAMOND_A4, type code %, sha256 `a128011207de397a…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : C : !
~~~~

[FeC-20Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-20Sae.tdb): DIAMOND_A4, type code %, sha256 `36e4397833b59ef8…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : C : !
~~~~

[FeC-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-23Jac.tdb): DIAMOND_A4, type code %, sha256 `c7f5cd4fc7acc9e5…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

[FeC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-24Eno.tdb): DIAMOND_A4, type code %, sha256 `6287b7852f6f5d4b…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : C : !
~~~~

[FeC-85Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-85Gus-LB.tdb): DIAMOND_A4, type code %, sha256 `9997883ee0500523…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : C : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.10.014](https://doi.org/10.1016/j.calphad.2015.10.014) H. Göhring, A. Leineweber, E.J. Mittemeijer, A thermodynamic model for non-stoichiometric cementite; the Fe–C phase diagram, Calphad 52, 38-46 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.ISIJINT-2019-274](https://doi.org/10.2355/isijinternational.ISIJINT-2019-274) M. Saeki, T. Yamashita, H. Ohtani, ISIJ Int., 60, 745-55(2020).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Fe)

- Id: `phase:c-fe:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 9 of 9 calculated diagram(s): 300–2500 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:a9-graphite)

Names (10): _corpus: _corpus:phase:c-fe:a9-graphite  
_tdb: _tdb:FeC-10Hal.tdb:GRAPHITE_A9, tdb:FeC-14Nar-3g.tdb:GRAPHITE_A9, tdb:FeC-16Goh.tdb:GRAPHITE_A9, tdb:FeC-19Che.tdb:GRAPHITE_A9, tdb:FeC-19Mie.tdb:GRAPHITE_A9, tdb:FeC-20Sae.tdb:GRAPHITE_A9, tdb:FeC-23Jac.tdb:GRAPHITE_A9, tdb:FeC-24Eno.tdb:GRAPHITE_A9, tdb:FeC-85Gus-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (9): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): GRAPHITE_A9, type code %, sha256 `7b87dfe21503206d…`

~~~~text
77: PHASE GRAPHITE_A9 % 1 1 !
78: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): GRAPHITE_A9, type code %, sha256 `2ac51900c8c0ad3b…`

~~~~text
61: PHASE GRAPHITE_A9 % 1 1 !
62: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-16Goh.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-16Goh.tdb): GRAPHITE_A9, type code %, sha256 `f7f205bbf9b6e594…`

~~~~text
52: PHASE GRAPHITE_A9 % 1 1 !
53: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Che.tdb): GRAPHITE_A9, type code %, sha256 `fe32281d077aba24…`

~~~~text
53: PHASE GRAPHITE_A9 % 1 1 !
54: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-19Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Mie.tdb): GRAPHITE_A9, type code %, sha256 `a128011207de397a…`

~~~~text
53: PHASE GRAPHITE_A9 % 1 1 !
54: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-20Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-20Sae.tdb): GRAPHITE_A9, type code %, sha256 `36e4397833b59ef8…`

~~~~text
53: PHASE GRAPHITE_A9 % 1 1 !
54: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-23Jac.tdb): GRAPHITE_A9, type code %, sha256 `c7f5cd4fc7acc9e5…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-24Eno.tdb): GRAPHITE_A9, type code %, sha256 `6287b7852f6f5d4b…`

~~~~text
51: PHASE GRAPHITE_A9 % 1 1 !
52: CONST GRAPHITE_A9 : C : !
~~~~

[FeC-85Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-85Gus-LB.tdb): GRAPHITE_A9, type code %, sha256 `9997883ee0500523…`

~~~~text
49: PHASE GRAPHITE_A9 % 1 1 !
50: CONST GRAPHITE_A9 : C : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.10.014](https://doi.org/10.1016/j.calphad.2015.10.014) H. Göhring, A. Leineweber, E.J. Mittemeijer, A thermodynamic model for non-stoichiometric cementite; the Fe–C phase diagram, Calphad 52, 38-46 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.ISIJINT-2019-274](https://doi.org/10.2355/isijinternational.ISIJINT-2019-274) M. Saeki, T. Yamashita, H. Ohtani, ISIJ Int., 60, 745-55(2020).  
_assessment that models this phase_

## BCC_A2 (C–Fe)

- Id: `phase:c-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 300–2499.69 K, x(C) 0–0.00626
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:bcc-a2)

Names (11): _corpus: _corpus:phase:c-fe:bcc-a2  
_paper: _paper:10.1007/bf02649916:α  
_tdb: _tdb:FeC-10Hal.tdb:BCC_A2, tdb:FeC-14Nar-3g.tdb:BCC_A2, tdb:FeC-16Goh.tdb:BCC_A2, tdb:FeC-19Che.tdb:BCC_A2, tdb:FeC-19Mie.tdb:BCC_A2, tdb:FeC-20Sae.tdb:BCC_A2, tdb:FeC-23Jac.tdb:BCC_A2, tdb:FeC-24Eno.tdb:BCC_A2, tdb:FeC-85Gus-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (9): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): BCC_A2, type code %B, sha256 `7b87dfe21503206d…`

~~~~text
57: PHASE BCC_A2 %B 2 1 3 !
58: CONST BCC_A2 : FE : C VA% : !
~~~~

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): BCC_A2, type code %B, sha256 `2ac51900c8c0ad3b…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : FE : C VA% : !
~~~~

[FeC-16Goh.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-16Goh.tdb): BCC_A2, type code %B, sha256 `f7f205bbf9b6e594…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : FE : C VA% : !
~~~~

[FeC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Che.tdb): BCC_A2, type code %B, sha256 `fe32281d077aba24…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE : C VA% : !
~~~~

[FeC-19Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Mie.tdb): BCC_A2, type code %B, sha256 `a128011207de397a…`

~~~~text
38: PHASE BCC_A2 %B 1 1 !
39: CONST BCC_A2 : FE% C : !
~~~~

[FeC-20Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-20Sae.tdb): BCC_A2, type code %B, sha256 `36e4397833b59ef8…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE : C VA% : !
~~~~

[FeC-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-23Jac.tdb): BCC_A2, type code %B, sha256 `c7f5cd4fc7acc9e5…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE : C VA% : !
~~~~

[FeC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-24Eno.tdb): BCC_A2, type code %B, sha256 `6287b7852f6f5d4b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE : C VA% : !
~~~~

[FeC-85Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-85Gus-LB.tdb): BCC_A2, type code %B, sha256 `9997883ee0500523…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE : C VA% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.10.014](https://doi.org/10.1016/j.calphad.2015.10.014) H. Göhring, A. Leineweber, E.J. Mittemeijer, A thermodynamic model for non-stoichiometric cementite; the Fe–C phase diagram, Calphad 52, 38-46 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.ISIJINT-2019-274](https://doi.org/10.2355/isijinternational.ISIJINT-2019-274) M. Saeki, T. Yamashita, H. Ohtani, ISIJ Int., 60, 745-55(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02649916](https://doi.org/10.1007/bf02649916) K. C. Hari Kumar, V. Raghavan, A Thermodynamic Analysis of the Al-C-Fe System, JPE 12, 275-286 (1991).  
_reports values for this phase_

## BCC_ALT (C–Fe)

- Id: `phase:c-fe:bcc-alt`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:ALT
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Stability: stable in 1 of 1 calculated diagram(s): 300.82–2345.95 K, x(C) 0–0.00308
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:bcc-alt)

Names (2): _corpus: _corpus:phase:c-fe:bcc-alt  
_tdb: _tdb:FeC-10Hal.tdb:BCC_ALT  


### TDB models of BCC_ALT (1): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): BCC_ALT, type code %B, sha256 `7b87dfe21503206d…`

~~~~text
62: PHASE BCC_ALT %B 2 1 1 !
63: CONST BCC_ALT : FE : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_

## BCT_Z1 (C–Fe)

- Id: `phase:c-fe:bct-z1`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:BCT,Z1; no_structure_token
- Stability: stable in 1 of 1 calculated diagram(s): 300–1800 K, x(C) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:bct-z1)

Names (2): _corpus: _corpus:phase:c-fe:bct-z1  
_tdb: _tdb:FeC-14Nar-3g.tdb:BCT_Z1  


### TDB models of BCT_Z1 (1): PHASE and CONSTITUENT statements as written

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): BCT_Z1, type code %B, sha256 `2ac51900c8c0ad3b…`

~~~~text
46: PHASE BCT_Z1 %B 3 1 1 2 !
47: CONST BCT_Z1 : FE : C VA% : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_

## BCT_Z2 (C–Fe)

- Id: `phase:c-fe:bct-z2`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:BCT,Z2; no_structure_token
- Stability: stable in 1 of 1 calculated diagram(s): 300.4–2499.12 K, x(C) 0–0.00626
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:bct-z2)

Names (2): _corpus: _corpus:phase:c-fe:bct-z2  
_tdb: _tdb:FeC-14Nar-3g.tdb:BCT_Z2  


### TDB models of BCT_Z2 (1): PHASE and CONSTITUENT statements as written

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): BCT_Z2, type code %B, sha256 `2ac51900c8c0ad3b…`

~~~~text
51: PHASE BCT_Z2 %B 3 1 0.125 2.875 !
52: CONST BCT_Z2 : FE : C% VA : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_

## CEMENTITE_D011 (C–Fe)

- Id: `phase:c-fe:cementite-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 9 calculated diagram(s): 1010–1416.1 K, x(C) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:cementite-d011)

Names (10): _corpus: _corpus:phase:c-fe:cementite-d011  
_tdb: _tdb:FeC-10Hal.tdb:CEMENTITE_D011, tdb:FeC-14Nar-3g.tdb:CEMENTITE_D011, tdb:FeC-16Goh.tdb:CEMENTITE_D011, tdb:FeC-19Che.tdb:CEMENTITE_D011, tdb:FeC-19Mie.tdb:CEMENTITE_D011, tdb:FeC-20Sae.tdb:CEMENTITE_D011, tdb:FeC-23Jac.tdb:CEMENTITE_D011, tdb:FeC-24Eno.tdb:CEMENTITE_D011, tdb:FeC-85Gus-LB.tdb:CEMENTITE_D011  


### TDB models of CEMENTITE_D011 (9): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): CEMENTITE_D011, type code %A, sha256 `7b87dfe21503206d…`

~~~~text
82: PHASE CEMENTITE_D011 %A 2 3 1 !
83: CONST CEMENTITE_D011 : FE : C : !
~~~~

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): CEMENTITE_D011, type code %A, sha256 `2ac51900c8c0ad3b…`

~~~~text
66: PHASE CEMENTITE_D011 %A 2 3 1 !
67: CONST CEMENTITE_D011 : FE : C : !
~~~~

[FeC-16Goh.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-16Goh.tdb): CEMENTITE_D011, type code %A, sha256 `f7f205bbf9b6e594…`

~~~~text
57: PHASE CEMENTITE_D011 %A 2 3 1 !
58: CONST CEMENTITE_D011 : FE : C VA : !
~~~~

[FeC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Che.tdb): CEMENTITE_D011, type code %A, sha256 `fe32281d077aba24…`

~~~~text
58: PHASE CEMENTITE_D011 %A 2 3 1 !
59: CONST CEMENTITE_D011 : FE : C VA : !
~~~~

[FeC-19Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Mie.tdb): CEMENTITE_D011, type code %, sha256 `a128011207de397a…`

~~~~text
58: PHASE CEMENTITE_D011 % 2 3 1 !
59: CONST CEMENTITE_D011 : FE : C : !
~~~~

[FeC-20Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-20Sae.tdb): CEMENTITE_D011, type code %, sha256 `36e4397833b59ef8…`

~~~~text
58: PHASE CEMENTITE_D011 % 2 3 1 !
59: CONST CEMENTITE_D011 : FE : C : !
~~~~

[FeC-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-23Jac.tdb): CEMENTITE_D011, type code %, sha256 `c7f5cd4fc7acc9e5…`

~~~~text
55: PHASE CEMENTITE_D011 % 2 3 1 !
56: CONST CEMENTITE_D011 : FE : C : !
~~~~

[FeC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-24Eno.tdb): CEMENTITE_D011, type code %A, sha256 `6287b7852f6f5d4b…`

~~~~text
56: PHASE CEMENTITE_D011 %A 2 3 1 !
57: CONST CEMENTITE_D011 : FE : C : !
~~~~

[FeC-85Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-85Gus-LB.tdb): CEMENTITE_D011, type code %, sha256 `9997883ee0500523…`

~~~~text
54: PHASE CEMENTITE_D011 % 2 3 1 !
55: CONST CEMENTITE_D011 : FE : C : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.10.014](https://doi.org/10.1016/j.calphad.2015.10.014) H. Göhring, A. Leineweber, E.J. Mittemeijer, A thermodynamic model for non-stoichiometric cementite; the Fe–C phase diagram, Calphad 52, 38-46 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.ISIJINT-2019-274](https://doi.org/10.2355/isijinternational.ISIJINT-2019-274) M. Saeki, T. Yamashita, H. Ohtani, ISIJ Int., 60, 745-55(2020).  
_assessment that models this phase_

## M2C_ETA (C–Fe)

- Id: `phase:c-fe:eta-m2c`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:M2C; no_structure_token
- Candidate (tdb_comment): Fe2C-eta · oP6 · Pnnm — FeC-14Nar-3g.tdb: 'Prototype Fe2C-eta (oP6, Pnnm)'
- Stoichiometry: C 0.3333, Fe 0.6667
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:eta-m2c)

Names (2): _corpus: _corpus:phase:c-fe:eta-m2c  
_tdb: _tdb:FeC-14Nar-3g.tdb:M2C_ETA  


### TDB models of M2C_ETA (1): PHASE and CONSTITUENT statements as written

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): M2C_ETA, type code %A, sha256 `2ac51900c8c0ad3b…`

~~~~text
76: PHASE M2C_ETA %A 2 2 1 !
77: CONST M2C_ETA : FE : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_

## FCC_A1 (C–Fe)

- Id: `phase:c-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 1009.04–1768.83 K, x(C) 0–0.08879
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:fcc-a1)

Names (11): _corpus: _corpus:phase:c-fe:fcc-a1  
_paper: _paper:10.1007/bf02649916:γ  
_tdb: _tdb:FeC-10Hal.tdb:FCC_A1, tdb:FeC-14Nar-3g.tdb:FCC_A1, tdb:FeC-16Goh.tdb:FCC_A1, tdb:FeC-19Che.tdb:FCC_A1, tdb:FeC-19Mie.tdb:FCC_A1, tdb:FeC-20Sae.tdb:FCC_A1, tdb:FeC-23Jac.tdb:FCC_A1, tdb:FeC-24Eno.tdb:FCC_A1, tdb:FeC-85Gus-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (9): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): FCC_A1, type code %A, sha256 `7b87dfe21503206d…`

~~~~text
52: PHASE FCC_A1 %A 2 1 1 !
53: CONST FCC_A1 : FE : C VA% : !
~~~~

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): FCC_A1, type code %A, sha256 `2ac51900c8c0ad3b…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : FE : C VA% : !
~~~~

[FeC-16Goh.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-16Goh.tdb): FCC_A1, type code %A, sha256 `f7f205bbf9b6e594…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : FE : C VA% : !
~~~~

[FeC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Che.tdb): FCC_A1, type code %A, sha256 `fe32281d077aba24…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE : C VA% : !
~~~~

[FeC-19Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Mie.tdb): FCC_A1, type code %A, sha256 `a128011207de397a…`

~~~~text
33: PHASE FCC_A1 %A 1 1 !
34: CONST FCC_A1 : FE% C : !
~~~~

[FeC-20Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-20Sae.tdb): FCC_A1, type code %A, sha256 `36e4397833b59ef8…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE : C VA% : !
~~~~

[FeC-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-23Jac.tdb): FCC_A1, type code %A, sha256 `c7f5cd4fc7acc9e5…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE : C VA% : !
~~~~

[FeC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-24Eno.tdb): FCC_A1, type code %A, sha256 `6287b7852f6f5d4b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE : C VA% : !
~~~~

[FeC-85Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-85Gus-LB.tdb): FCC_A1, type code %A, sha256 `9997883ee0500523…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE : C VA% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.10.014](https://doi.org/10.1016/j.calphad.2015.10.014) H. Göhring, A. Leineweber, E.J. Mittemeijer, A thermodynamic model for non-stoichiometric cementite; the Fe–C phase diagram, Calphad 52, 38-46 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.ISIJINT-2019-274](https://doi.org/10.2355/isijinternational.ISIJINT-2019-274) M. Saeki, T. Yamashita, H. Ohtani, ISIJ Int., 60, 745-55(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02649916](https://doi.org/10.1007/bf02649916) K. C. Hari Kumar, V. Raghavan, A Thermodynamic Analysis of the Al-C-Fe System, JPE 12, 275-286 (1991).  
_reports values for this phase_

## HCP_A3 (C–Fe)

- Id: `phase:c-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 8 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:hcp-a3)

Names (9): _corpus: _corpus:phase:c-fe:hcp-a3  
_tdb: _tdb:FeC-10Hal.tdb:HCP_A3, tdb:FeC-16Goh.tdb:HCP_A3, tdb:FeC-19Che.tdb:HCP_A3, tdb:FeC-19Mie.tdb:HCP_A3, tdb:FeC-20Sae.tdb:HCP_A3, tdb:FeC-23Jac.tdb:HCP_A3, tdb:FeC-24Eno.tdb:HCP_A3, tdb:FeC-85Gus-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (8): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): HCP_A3, type code %, sha256 `7b87dfe21503206d…`

~~~~text
67: PHASE HCP_A3 % 2 1 0.5 !
68: CONST HCP_A3 : FE : C VA% : !
~~~~

[FeC-16Goh.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-16Goh.tdb): HCP_A3, type code %, sha256 `f7f205bbf9b6e594…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : FE : C VA% : !
~~~~

[FeC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Che.tdb): HCP_A3, type code %, sha256 `fe32281d077aba24…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : FE : C VA% : !
~~~~

[FeC-19Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Mie.tdb): HCP_A3, type code %, sha256 `a128011207de397a…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : FE : C VA% : !
~~~~

[FeC-20Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-20Sae.tdb): HCP_A3, type code %, sha256 `36e4397833b59ef8…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : FE : C VA% : !
~~~~

[FeC-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-23Jac.tdb): HCP_A3, type code %, sha256 `c7f5cd4fc7acc9e5…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : FE : C VA% : !
~~~~

[FeC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-24Eno.tdb): HCP_A3, type code %, sha256 `6287b7852f6f5d4b…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : FE : C VA% : !
~~~~

[FeC-85Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-85Gus-LB.tdb): HCP_A3, type code %, sha256 `9997883ee0500523…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : FE : C VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.10.014](https://doi.org/10.1016/j.calphad.2015.10.014) H. Göhring, A. Leineweber, E.J. Mittemeijer, A thermodynamic model for non-stoichiometric cementite; the Fe–C phase diagram, Calphad 52, 38-46 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.ISIJINT-2019-274](https://doi.org/10.2355/isijinternational.ISIJINT-2019-274) M. Saeki, T. Yamashita, H. Ohtani, ISIJ Int., 60, 745-55(2020).  
_assessment that models this phase_

## LIQUID (C–Fe)

- Id: `phase:c-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 1415.24–2500 K, x(C) 0–0.27456
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:liquid)

Names (11): _corpus: _corpus:phase:c-fe:liquid  
_paper: _paper:10.1007/bf02649916:L  
_tdb: _tdb:FeC-10Hal.tdb:LIQUID, tdb:FeC-14Nar-3g.tdb:LIQUID, tdb:FeC-16Goh.tdb:LIQUID, tdb:FeC-19Che.tdb:LIQUID, tdb:FeC-19Mie.tdb:LIQUID, tdb:FeC-20Sae.tdb:LIQUID, tdb:FeC-23Jac.tdb:LIQUID, tdb:FeC-24Eno.tdb:LIQUID, tdb:FeC-85Gus-LB.tdb:LIQUID  


### TDB models of LIQUID (9): PHASE and CONSTITUENT statements as written

[FeC-10Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-10Hal.tdb): LIQUID, type code %, sha256 `7b87dfe21503206d…`

~~~~text
47: PHASE LIQUID:L % 1 1 !
48: CONST LIQUID:L : C FE : !
~~~~

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): LIQUID, type code %, sha256 `2ac51900c8c0ad3b…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : C FE : !
~~~~

[FeC-16Goh.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-16Goh.tdb): LIQUID, type code %, sha256 `f7f205bbf9b6e594…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : C FE : !
~~~~

[FeC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Che.tdb): LIQUID, type code %, sha256 `fe32281d077aba24…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : C FE : !
~~~~

[FeC-19Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-19Mie.tdb): LIQUID, type code %, sha256 `a128011207de397a…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : C FE : !
~~~~

[FeC-20Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-20Sae.tdb): LIQUID, type code %, sha256 `36e4397833b59ef8…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : C FE : !
~~~~

[FeC-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-23Jac.tdb): LIQUID, type code %, sha256 `c7f5cd4fc7acc9e5…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C FE : !
~~~~

[FeC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-24Eno.tdb): LIQUID, type code %, sha256 `6287b7852f6f5d4b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : C FE : !
~~~~

[FeC-85Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-85Gus-LB.tdb): LIQUID, type code %, sha256 `9997883ee0500523…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : C FE : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.01.004](https://doi.org/10.1016/j.calphad.2010.01.004) Bengt Hallstedt, Dejan Djurovic, Jörg von Appen, Richard Dronskowski, Alexey Dick, Fritz Körmann et al., Thermodynamic properties of cementite (), Calphad 34, 129-133 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.10.014](https://doi.org/10.1016/j.calphad.2015.10.014) H. Göhring, A. Leineweber, E.J. Mittemeijer, A thermodynamic model for non-stoichiometric cementite; the Fe–C phase diagram, Calphad 52, 38-46 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.ISIJINT-2019-274](https://doi.org/10.2355/isijinternational.ISIJINT-2019-274) M. Saeki, T. Yamashita, H. Ohtani, ISIJ Int., 60, 745-55(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02649916](https://doi.org/10.1007/bf02649916) K. C. Hari Kumar, V. Raghavan, A Thermodynamic Analysis of the Al-C-Fe System, JPE 12, 275-286 (1991).  
_reports values for this phase_

## M5C2 (C–Fe)

- Id: `phase:c-fe:m5c2`; status `assigned`
- Structure: Mn5C2 · mC28 · C2/c (15); type `st:mn5c2-mc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:M5C2, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.2857, Fe 0.7143
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-fe:m5c2)

Names (2): _corpus: _corpus:phase:c-fe:m5c2  
_tdb: _tdb:FeC-14Nar-3g.tdb:M5C2  


### TDB models of M5C2 (1): PHASE and CONSTITUENT statements as written

[FeC-14Nar-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeC-14Nar-3g.tdb): M5C2, type code %A, sha256 `2ac51900c8c0ad3b…`

~~~~text
71: PHASE M5C2 %A 2 5 2 !
72: CONST M5C2 : FE : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.03.004](https://doi.org/10.1016/j.calphad.2014.03.004) Reza Naraghi, Malin Selleby, John Ågren, Thermodynamics of stable and metastable structures in Fe–C system, Calphad 46, 148-158 (2014).  
_assessment that models this phase_

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
