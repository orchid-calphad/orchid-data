# Ca–O phases

> Ca–O system: 9 phases (tier A 4, liquid 2, gas 2, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-O.html · Markdown: https://data.orchid-project.org/phases/pages/CA-O.md

9 phases (tier A 4, liquid 2, gas 2, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-O) · [full JSON](https://data.orchid-project.org/phases/systems/CA-O.json) · [Ca–O system page](https://data.orchid-project.org/systems/CA-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–O system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [B1_OXIDE](#phase-ca-o-b1-oxide); _phase:ca-o:b1-oxide_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(O) 0.5–0.5 | 18 | 4 |
| [BCC_A2](#phase-ca-o-bcc-a2); _phase:ca-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 716.03–1168 K, x(O) 0–0 | 0 | 4 |
| [CAO2_C11A](#phase-ca-o-cao2-c11a); _phase:ca-o:cao2-c11a_ |  | needs_review | stable in 1 of 3 calculated diagram(s): 300–335 K, x(O) 0.66667–0.66667 | 0 | 3 |
| [FCC_A1](#phase-ca-o-fcc-a1); _phase:ca-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 4 calculated diagram(s): 300–716.03 K, x(O) 0–0 | 0 | 4 |
| [GAS](#phase-ca-o-gas); _phase:ca-o:gas_ | gas | gas | stable in 4 of 4 calculated diagram(s): 1347.5–2500 K, x(O) 0–1 | 0 | 4 |
| [HCP_A3](#phase-ca-o-hcp-a3); _phase:ca-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [ION](#phase-ca-o-ion); _phase:ca-o:ion_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1100–1809.06 K, x(O) 0–0.07372 | 0 | 4 |
| [LIQUID](#phase-ca-o-liquid); _phase:ca-o:liquid_ | liquid | liquid | not stable in 4 calculated diagram(s) | 18 | 4 |
| [O2GAS](#phase-ca-o-o2gas); _phase:ca-o:o2gas_ | gas | gas | stable in 4 of 4 calculated diagram(s): 300–1077.5 K, x(O) 1–1 | 0 | 4 |

## B1_OXIDE (Ca–O)

- Id: `phase:ca-o:b1-oxide`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(O) 0.5–0.5
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:b1-oxide)

Names (6): _corpus: _corpus:phase:ca-o:b1-oxide  
_paper: _paper:10.1016/j.jeurceramsoc.2018.06.015:CaO  
_tdb: _tdb:CaO-18Lia.tdb:B1_OXIDE, tdb:CaO-20Def-3g.tdb:B1_OXIDE, tdb:CaO-23Abd-3g.tdb:B1_OXIDE, tdb:CaO-96Sel.tdb:B1_OXIDE  


### TDB models of B1_OXIDE (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): B1_OXIDE, type code %, sha256 `78618178a1324682…`

~~~~text
59: PHASE B1_OXIDE:I % 2 1 1 !
60: CONST B1_OXIDE:I : CA+2 : O-2 : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): B1_OXIDE, type code %, sha256 `2df29e5f285a88c6…`

~~~~text
65: PHASE B1_OXIDE:I % 2 1 1 !
66: CONST B1_OXIDE:I : CA+2 : O-2 : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): B1_OXIDE, type code %, sha256 `c6509b3e8c06ae7f…`

~~~~text
67: PHASE B1_OXIDE:I % 2 1 1 !
68: CONST B1_OXIDE:I : CA+2 : O-2 : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): B1_OXIDE, type code %, sha256 `c26a22ca6d938a23…`

~~~~text
56: PHASE B1_OXIDE:I % 2 1 1 !
57: CONST B1_OXIDE:I : CA+2 : O-2 : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_
- [doi:10.1007/bf02880517](https://doi.org/10.1007/bf02880517) H.A. Wriedt, The Ca−O (Calcium-Oxygen) system, Bull. Alloy Phase Diagrams 6 (1985) 337–342, http://dx.doi.org/10.1007/BF02880517.  
_cited as the source of values for this phase_
- [doi:10.1351/pac198254030681](https://doi.org/10.1351/pac198254030681) J. Hlavac, Melting temperatures of refractory oxides: Part I, Pure and Applied Chemistry 54, 681-688 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/0016-7037(87)90009-3](https://doi.org/10.1016/0016-7037%2887%2990009-3) Milton Blander, Arthur D. Pelton, Thermodynamic analysis of binary liquid silicates and prediction of ternary solution properties by modified quasichemical equations, Geochimica et Cosmochimica Acta 51, 85-95 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0038-092x(65)90162-3](https://doi.org/10.1016/0038-092x%2865%2990162-3) Marc Foex, Measurement of the solidification points of several refractory oxides by means of a solar furnace, Solar Energy 9, 61-67 (1965).  
_cited as the source of values for this phase_
- [doi:10.1016/0038-092x(67)90022-9](https://doi.org/10.1016/0038-092x%2867%2990022-9) Tetsuo Noguchi, Masao Mizuno, William M. Conn, Fundamental research in refractory system with a solar furnace—ZrO2CaO system, Solar Energy 11, 145-152 (1967).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(89)90006-0](https://doi.org/10.1016/0364-5916%2889%2990006-0) M. Hillert, X. Wang, Thermodynamic calculation of the CaO–MgO system, Calphad 13 (1989) 267–271, http://dx.doi.org/10.1016/0364-5916(89)90006-0.  
_cited as the source of values for this phase_

## BCC_A2 (Ca–O)

- Id: `phase:ca-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 716.03–1168 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:bcc-a2)

Names (5): _corpus: _corpus:phase:ca-o:bcc-a2  
_tdb: _tdb:CaO-18Lia.tdb:BCC_A2, tdb:CaO-20Def-3g.tdb:BCC_A2, tdb:CaO-23Abd-3g.tdb:BCC_A2, tdb:CaO-96Sel.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): BCC_A2, type code %B, sha256 `78618178a1324682…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : CA% O : VA : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): BCC_A2, type code %B, sha256 `2df29e5f285a88c6…`

~~~~text
55: PHASE BCC_A2 %B 2 1 3 !
56: CONST BCC_A2 : CA% O : VA : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): BCC_A2, type code %B, sha256 `c6509b3e8c06ae7f…`

~~~~text
57: PHASE BCC_A2 %B 2 1 3 !
58: CONST BCC_A2 : CA% O : VA : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): BCC_A2, type code %B, sha256 `c26a22ca6d938a23…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : CA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_

## CAO2_C11A (Ca–O)

- Id: `phase:ca-o:cao2-c11a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_C11_a; site_ratios_contradict_C11_a:CaO-18Lia.tdb; site_ratios_contradict_C11_a:CaO-20Def-3g.tdb; site_ratios_contradict_C11_a:CaO-23Abd-3g.tdb
- Candidate (name_token): CaC2 · C11_a · tI6 · I4/mmm (139) — Strukturbericht/word 'C11A' in the TDB name
- Candidate (sgte_mmc2): CaC2 · C11_a · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for CAO2_C11A: CaO2 (peroxide)
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — CaO-18Lia.tdb: 'Prototype CaC2 (tI6, I4/mmm), C11_a, barium peroxide'
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — CaO-20Def-3g.tdb: 'Prototype CaC2 (tI6, I4/mmm), C11_a, barium peroxide'
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — CaO-23Abd-3g.tdb: 'Prototype CaC2 (tI6, I4/mmm), C11_a, barium peroxide'
- Stability: stable in 1 of 3 calculated diagram(s): 300–335 K, x(O) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:cao2-c11a)

Names (4): _corpus: _corpus:phase:ca-o:cao2-c11a  
_tdb: _tdb:CaO-18Lia.tdb:CAO2_C11A, tdb:CaO-20Def-3g.tdb:CAO2_C11A, tdb:CaO-23Abd-3g.tdb:CAO2_C11A  


### TDB models of CAO2_C11A (3): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): CAO2_C11A, type code %, sha256 `78618178a1324682…`

~~~~text
64: PHASE CAO2_C11A:I % 2 1 1 !
65: CONST CAO2_C11A:I : CA+2 : O2-2 : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): CAO2_C11A, type code %, sha256 `2df29e5f285a88c6…`

~~~~text
70: PHASE CAO2_C11A:I % 2 1 1 !
71: CONST CAO2_C11A:I : CA+2 : O2-2 : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): CAO2_C11A, type code %, sha256 `c6509b3e8c06ae7f…`

~~~~text
72: PHASE CAO2_C11A:I % 2 1 1 !
73: CONST CAO2_C11A:I : CA+2 : O2-2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_

## FCC_A1 (Ca–O)

- Id: `phase:ca-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 4 calculated diagram(s): 300–716.03 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:fcc-a1)

Names (5): _corpus: _corpus:phase:ca-o:fcc-a1  
_tdb: _tdb:CaO-18Lia.tdb:FCC_A1, tdb:CaO-20Def-3g.tdb:FCC_A1, tdb:CaO-23Abd-3g.tdb:FCC_A1, tdb:CaO-96Sel.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): FCC_A1, type code %A, sha256 `78618178a1324682…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : CA% O : VA : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): FCC_A1, type code %A, sha256 `2df29e5f285a88c6…`

~~~~text
50: PHASE FCC_A1 %A 2 1 1 !
51: CONST FCC_A1 : CA% O : VA : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): FCC_A1, type code %A, sha256 `c6509b3e8c06ae7f…`

~~~~text
52: PHASE FCC_A1 %A 2 1 1 !
53: CONST FCC_A1 : CA% O : VA : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): FCC_A1, type code %A, sha256 `c26a22ca6d938a23…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : CA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_

## GAS (Ca–O)

- Id: `phase:ca-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1347.5–2500 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:gas)

Names (5): _corpus: _corpus:phase:ca-o:gas  
_tdb: _tdb:CaO-18Lia.tdb:GAS, tdb:CaO-20Def-3g.tdb:GAS, tdb:CaO-23Abd-3g.tdb:GAS, tdb:CaO-96Sel.tdb:GAS  


### TDB models of GAS (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): GAS, type code %, sha256 `78618178a1324682…`

~~~~text
67: PHASE GAS:G % 1 1 !
68: CONST GAS:G : CA CA2 CAO O O2% O3 : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): GAS, type code %, sha256 `2df29e5f285a88c6…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : CA CA2 CAO O O2% O3 : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): GAS, type code %, sha256 `c6509b3e8c06ae7f…`

~~~~text
75: PHASE GAS:G % 1 1 !
76: CONST GAS:G : CA CA2 CAO O O2% O3 : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): GAS, type code %, sha256 `c26a22ca6d938a23…`

~~~~text
59: PHASE GAS:G % 1 1 !
60: CONST GAS:G : CA CA2 CAO O O2% O3 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_

## HCP_A3 (Ca–O)

- Id: `phase:ca-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:hcp-a3)

Names (5): _corpus: _corpus:phase:ca-o:hcp-a3  
_tdb: _tdb:CaO-18Lia.tdb:HCP_A3, tdb:CaO-20Def-3g.tdb:HCP_A3, tdb:CaO-23Abd-3g.tdb:HCP_A3, tdb:CaO-96Sel.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): HCP_A3, type code %A, sha256 `78618178a1324682…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : CA O : VA : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): HCP_A3, type code %A, sha256 `2df29e5f285a88c6…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : CA O : VA : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): HCP_A3, type code %A, sha256 `c6509b3e8c06ae7f…`

~~~~text
62: PHASE HCP_A3 %A 2 1 0.5 !
63: CONST HCP_A3 : CA O : VA : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): HCP_A3, type code %A, sha256 `c26a22ca6d938a23…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : CA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_

## ION (Ca–O)

- Id: `phase:ca-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1100–1809.06 K, x(O) 0–0.07372
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:ion)

Names (5): _corpus: _corpus:phase:ca-o:ion  
_tdb: _tdb:CaO-18Lia.tdb:ION, tdb:CaO-20Def-3g.tdb:ION, tdb:CaO-23Abd-3g.tdb:ION, tdb:CaO-96Sel.tdb:ION  


### TDB models of ION (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): ION, type code %, sha256 `78618178a1324682…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : CA+2 : O-2 VA O : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): ION, type code %, sha256 `2df29e5f285a88c6…`

~~~~text
42: PHASE ION:Y % 2 1 1 !
43: CONST ION:Y : CA+2 : O-2 VA O : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): ION, type code %, sha256 `c6509b3e8c06ae7f…`

~~~~text
44: PHASE ION:Y % 2 1 1 !
45: CONST ION:Y : CA+2 : O-2 VA O : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): ION, type code %, sha256 `c26a22ca6d938a23…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : CA+2 : O-2 VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_

## LIQUID (Ca–O)

- Id: `phase:ca-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:liquid)

Names (6): _corpus: _corpus:phase:ca-o:liquid  
_paper: _paper:10.1016/j.jeurceramsoc.2018.06.015:liquid  
_tdb: _tdb:CaO-18Lia.tdb:LIQUID, tdb:CaO-20Def-3g.tdb:LIQUID, tdb:CaO-23Abd-3g.tdb:LIQUID, tdb:CaO-96Sel.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): LIQUID, type code %, sha256 `78618178a1324682…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : CA CAO O : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): LIQUID, type code %, sha256 `2df29e5f285a88c6…`

~~~~text
45: PHASE LIQUID:L % 1 1 !
46: CONST LIQUID:L : CA CAO O : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): LIQUID, type code %, sha256 `c6509b3e8c06ae7f…`

~~~~text
47: PHASE LIQUID:L % 1 1 !
48: CONST LIQUID:L : CA CAO O : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): LIQUID, type code %, sha256 `c26a22ca6d938a23…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : CA : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_
- [doi:10.1007/bf02880517](https://doi.org/10.1007/bf02880517) H.A. Wriedt, The Ca−O (Calcium-Oxygen) system, Bull. Alloy Phase Diagrams 6 (1985) 337–342, http://dx.doi.org/10.1007/BF02880517.  
_cited as the source of values for this phase_
- [doi:10.1351/pac198254030681](https://doi.org/10.1351/pac198254030681) J. Hlavac, Melting temperatures of refractory oxides: Part I, Pure and Applied Chemistry 54, 681-688 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/0016-7037(87)90009-3](https://doi.org/10.1016/0016-7037%2887%2990009-3) Milton Blander, Arthur D. Pelton, Thermodynamic analysis of binary liquid silicates and prediction of ternary solution properties by modified quasichemical equations, Geochimica et Cosmochimica Acta 51, 85-95 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0038-092x(65)90162-3](https://doi.org/10.1016/0038-092x%2865%2990162-3) Marc Foex, Measurement of the solidification points of several refractory oxides by means of a solar furnace, Solar Energy 9, 61-67 (1965).  
_cited as the source of values for this phase_
- [doi:10.1016/0038-092x(67)90022-9](https://doi.org/10.1016/0038-092x%2867%2990022-9) Tetsuo Noguchi, Masao Mizuno, William M. Conn, Fundamental research in refractory system with a solar furnace—ZrO2CaO system, Solar Energy 11, 145-152 (1967).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(89)90006-0](https://doi.org/10.1016/0364-5916%2889%2990006-0) M. Hillert, X. Wang, Thermodynamic calculation of the CaO–MgO system, Calphad 13 (1989) 267–271, http://dx.doi.org/10.1016/0364-5916(89)90006-0.  
_cited as the source of values for this phase_

## O2GAS (Ca–O)

- Id: `phase:ca-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1077.5 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-o:o2gas)

Names (5): _corpus: _corpus:phase:ca-o:o2gas  
_tdb: _tdb:CaO-18Lia.tdb:O2GAS, tdb:CaO-20Def-3g.tdb:O2GAS, tdb:CaO-23Abd-3g.tdb:O2GAS, tdb:CaO-96Sel.tdb:O2GAS  


### TDB models of O2GAS (4): PHASE and CONSTITUENT statements as written

[CaO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-18Lia.tdb): O2GAS, type code %, sha256 `78618178a1324682…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 : !
~~~~

[CaO-20Def-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-20Def-3g.tdb): O2GAS, type code %, sha256 `2df29e5f285a88c6…`

~~~~text
76: PHASE O2GAS % 1 1 !
77: CONST O2GAS : O2 : !
~~~~

[CaO-23Abd-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-23Abd-3g.tdb): O2GAS, type code %, sha256 `c6509b3e8c06ae7f…`

~~~~text
78: PHASE O2GAS % 1 1 !
79: CONST O2GAS : O2 : !
~~~~

[CaO-96Sel.tdb](https://orchid-project.org/data/databases/sgte-binary/CaO-96Sel.tdb): O2GAS, type code %, sha256 `c26a22ca6d938a23…`

~~~~text
62: PHASE O2GAS % 1 1 !
63: CONST O2GAS : O2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2020.101764](https://doi.org/10.1016/j.calphad.2020.101764) Guillaume Deffrennes, Noël Jakse, Cecilia M.S. Alvares, Ioana Nuta, Alain Pasturel, Alexandra Khvan et al., Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO2, Calphad 69, 101764 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.cemconres.2023.107309](https://doi.org/10.1016/j.cemconres.2023.107309) Wahab Abdul, Chancel Mawalala, Alexander Pisch, Marcus Nigel Bannerman, CaO-SiO2 assessment using 3rd generation CALPHAD models, Cement and Concrete Research 173, 107309 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00039-9](https://doi.org/10.1016/S0364-5916%2896%2900039-9) M. Selleby, B. Sundman, Calphad, 20, 391-92(1996).  
_assessment that models this phase_

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
