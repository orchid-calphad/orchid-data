# Gd–O phases

> Gd–O system: 11 phases (tier A 3, tier C 5, liquid 1, gas 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-O.html · Markdown: https://data.orchid-project.org/phases/pages/GD-O.md

11 phases (tier A 3, tier C 5, liquid 1, gas 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-O) · [full JSON](https://data.orchid-project.org/phases/systems/GD-O.json) · [Gd–O system page](https://data.orchid-project.org/systems/GD-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–O system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [B_R2O3](#phase-gd-o-b-r2o3); _phase:gd-o:b-r2o3_ | B-Sm2O3 · mC30 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BCC_A2](#phase-gd-o-bcc-a2); _phase:gd-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 1586.12–2499.87 K, x(O) 0–0 | 0 | 2 |
| [A_R2O3_D52](#phase-gd-o-d52-a-r2o3); _phase:gd-o:d52-a-r2o3_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 0 | 2 |
| [C_R2O3_D53](#phase-gd-o-d53-c-r2o3); _phase:gd-o:d53-c-r2o3_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–535 K, x(O) 0.6–0.6 | 0 | 2 |
| [FCC_A1](#phase-gd-o-fcc-a1); _phase:gd-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-gd-o-gas); _phase:gd-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 2485–2500 K, x(O) 1–1 | 0 | 2 |
| [H_R2O3](#phase-gd-o-h-r2o3); _phase:gd-o:h-r2o3_ | H-La2O3 · hP10 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 2485–2500 K, x(O) 0.6–0.6 | 0 | 2 |
| [HCP_A3](#phase-gd-o-hcp-a3); _phase:gd-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–325 K, x(O) 0–0 | 0 | 2 |
| [ION](#phase-gd-o-ion); _phase:gd-o:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1586.12–2500 K, x(O) 0–0.56845 | 0 | 2 |
| [O2GAS](#phase-gd-o-o2gas); _phase:gd-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–535 K, x(O) 1–1 | 0 | 2 |
| [X_R2O3](#phase-gd-o-r2o3-x); _phase:gd-o:r2o3-x_ | Nd2O3 · cI26 · Im-3m (229) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 0 | 2 |

## B_R2O3 (Gd–O)

- Id: `phase:gd-o:b-r2o3`; status `assigned`
- Structure: B-Sm2O3 · mC30 · C2/m (12); type `st:b-sm2o3-mc30`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:B,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:b-r2o3)

Names (3): _corpus: _corpus:phase:gd-o:b-r2o3  
_tdb: _tdb:GdO-14McM.tdb:B_R2O3, tdb:GdO-23Nak.tdb:B_R2O3  


### TDB models of B_R2O3 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): B_R2O3, type code %, sha256 `b72717c7ab25c852…`

~~~~text
58: PHASE B_R2O3:I % 2 2 3 !
59: CONST B_R2O3:I : GD+3 : O-2 : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): B_R2O3, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
56: PHASE B_R2O3:I % 2 2 3 !
57: CONST B_R2O3:I : GD+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## BCC_A2 (Gd–O)

- Id: `phase:gd-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: stable in 1 of 2 calculated diagram(s): 1586.12–2499.87 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:bcc-a2)

Names (3): _corpus: _corpus:phase:gd-o:bcc-a2  
_tdb: _tdb:GdO-14McM.tdb:BCC_A2, tdb:GdO-23Nak.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): BCC_A2, type code %B, sha256 `b72717c7ab25c852…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : GD : VA : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): BCC_A2, type code %B, sha256 `bd0ea93f229ea2a2…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : GD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## A_R2O3_D52 (Gd–O)

- Id: `phase:gd-o:d52-a-r2o3`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:A,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:d52-a-r2o3)

Names (3): _corpus: _corpus:phase:gd-o:d52-a-r2o3  
_tdb: _tdb:GdO-14McM.tdb:A_R2O3_D52, tdb:GdO-23Nak.tdb:A_R2O3_D52  


### TDB models of A_R2O3_D52 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): A_R2O3_D52, type code %, sha256 `b72717c7ab25c852…`

~~~~text
53: PHASE A_R2O3_D52:I % 2 2 3 !
54: CONST A_R2O3_D52:I : GD+3 : O-2 : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): A_R2O3_D52, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
51: PHASE A_R2O3_D52:I % 2 2 3 !
52: CONST A_R2O3_D52:I : GD+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## C_R2O3_D53 (Gd–O)

- Id: `phase:gd-o:d53-c-r2o3`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:C,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–535 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:d53-c-r2o3)

Names (3): _corpus: _corpus:phase:gd-o:d53-c-r2o3  
_tdb: _tdb:GdO-14McM.tdb:C_R2O3_D53, tdb:GdO-23Nak.tdb:C_R2O3_D53  


### TDB models of C_R2O3_D53 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): C_R2O3_D53, type code %, sha256 `b72717c7ab25c852…`

~~~~text
63: PHASE C_R2O3_D53:I % 2 2 3 !
64: CONST C_R2O3_D53:I : GD+3 : O-2 : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): C_R2O3_D53, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
61: PHASE C_R2O3_D53:I % 2 2 3 !
62: CONST C_R2O3_D53:I : GD+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## FCC_A1 (Gd–O)

- Id: `phase:gd-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:fcc-a1)

Names (3): _corpus: _corpus:phase:gd-o:fcc-a1  
_tdb: _tdb:GdO-14McM.tdb:FCC_A1, tdb:GdO-23Nak.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): FCC_A1, type code %A, sha256 `b72717c7ab25c852…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : GD : VA : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): FCC_A1, type code %A, sha256 `bd0ea93f229ea2a2…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : GD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## GAS (Gd–O)

- Id: `phase:gd-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2485–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:gas)

Names (3): _corpus: _corpus:phase:gd-o:gas  
_tdb: _tdb:GdO-14McM.tdb:GAS, tdb:GdO-23Nak.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): GAS, type code %, sha256 `b72717c7ab25c852…`

~~~~text
76: PHASE GAS:G % 1 1 !
77: CONST GAS:G : GD GDO O O2% O3 : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): GAS, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
74: PHASE GAS:G % 1 1 !
75: CONST GAS:G : GD GDO O O2% O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## H_R2O3 (Gd–O)

- Id: `phase:gd-o:h-r2o3`; status `assigned`
- Structure: H-La2O3 · hP10 · P6_3/mmc (194); type `st:h-la2o3-hp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:H,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 2485–2500 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:h-r2o3)

Names (3): _corpus: _corpus:phase:gd-o:h-r2o3  
_tdb: _tdb:GdO-14McM.tdb:H_R2O3, tdb:GdO-23Nak.tdb:H_R2O3  


### TDB models of H_R2O3 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): H_R2O3, type code %, sha256 `b72717c7ab25c852…`

~~~~text
68: PHASE H_R2O3:I % 2 2 3 !
69: CONST H_R2O3:I : GD+3 : O-2 : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): H_R2O3, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
66: PHASE H_R2O3:I % 2 2 3 !
67: CONST H_R2O3:I : GD+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## HCP_A3 (Gd–O)

- Id: `phase:gd-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–325 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:hcp-a3)

Names (3): _corpus: _corpus:phase:gd-o:hcp-a3  
_tdb: _tdb:GdO-14McM.tdb:HCP_A3, tdb:GdO-23Nak.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): HCP_A3, type code %A, sha256 `b72717c7ab25c852…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : GD : VA : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): HCP_A3, type code %A, sha256 `bd0ea93f229ea2a2…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : GD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## ION (Gd–O)

- Id: `phase:gd-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1586.12–2500 K, x(O) 0–0.56845
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:ion)

Names (3): _corpus: _corpus:phase:gd-o:ion  
_tdb: _tdb:GdO-14McM.tdb:ION, tdb:GdO-23Nak.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): ION, type code %, sha256 `b72717c7ab25c852…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : GD+3 : O-2 VA : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): ION, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
31: PHASE ION:Y % 2 1 1 !
32: CONST ION:Y : GD+3 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## O2GAS (Gd–O)

- Id: `phase:gd-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–535 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:o2gas)

Names (3): _corpus: _corpus:phase:gd-o:o2gas  
_tdb: _tdb:GdO-14McM.tdb:O2GAS, tdb:GdO-23Nak.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): O2GAS, type code %, sha256 `b72717c7ab25c852…`

~~~~text
79: PHASE O2GAS % 1 1 !
80: CONST O2GAS : O2 : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): O2GAS, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
77: PHASE O2GAS % 1 1 !
78: CONST O2GAS : O2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
_assessment that models this phase_

## X_R2O3 (Gd–O)

- Id: `phase:gd-o:r2o3-x`; status `assigned`
- Structure: Nd2O3 · cI26 · Im-3m (229); type `st:nd2o3-ci26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:R2O3,X, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-o:r2o3-x)

Names (3): _corpus: _corpus:phase:gd-o:r2o3-x  
_tdb: _tdb:GdO-14McM.tdb:X_R2O3, tdb:GdO-23Nak.tdb:X_R2O3  


### TDB models of X_R2O3 (2): PHASE and CONSTITUENT statements as written

[GdO-14McM.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb): X_R2O3, type code %, sha256 `b72717c7ab25c852…`

~~~~text
73: PHASE X_R2O3:I % 2 2 3 !
74: CONST X_R2O3:I : GD+3 : O-2 : !
~~~~

[GdO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb): X_R2O3, type code %, sha256 `bd0ea93f229ea2a2…`

~~~~text
71: PHASE X_R2O3:I % 2 2 3 !
72: CONST X_R2O3:I : GD+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014).  
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
