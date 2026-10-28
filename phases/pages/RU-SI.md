# Ru–Si phases

> Ru–Si system: 10 phases (tier A 5, tier C 1, liquid 1, needs_review 2, unresolved_no_candidates 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RU-SI.html · Markdown: https://data.orchid-project.org/phases/pages/RU-SI.md

10 phases (tier A 5, tier C 1, liquid 1, needs_review 2, unresolved_no_candidates 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RU-SI) · [full JSON](https://data.orchid-project.org/phases/systems/RU-SI.json) · [Ru–Si system page](https://data.orchid-project.org/systems/RU-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/RU-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ru–Si system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ru-si-a4-diamond); _phase:ru-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.61 K, x(Si) 0.98397–1 | 7 | 4 |
| [BCC_A2](#phase-ru-si-bcc-a2); _phase:ru-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-ru-si-fcc-a1); _phase:ru-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-ru-si-hcp-a3); _phase:ru-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2627.41 K, x(Si) 0–0.05336 | 15 | 4 |
| [LIQUID](#phase-ru-si-liquid); _phase:ru-si:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1561.64–4000 K, x(Si) 0–1 | 50 | 4 |
| [RU2SI_C37](#phase-ru-si-ru2si-c37); _phase:ru-si:ru2si-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1506.67–1822.42 K, x(Si) 0.33333–0.33333 | 21 | 4 |
| [RU2SI3](#phase-ru-si-ru2si3); _phase:ru-si:ru2si3_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1985.87 K, x(Si) 0.6–0.6 | 32 | 4 |
| [RU4SI3](#phase-ru-si-ru4si3); _phase:ru-si:ru4si3_ | Ru4Si3 · oP28 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1948.13 K, x(Si) 0.42857–0.42857 | 26 | 4 |
| [RU5SI3](#phase-ru-si-ru5si3); _phase:ru-si:ru5si3_ |  | unresolved_no_candidates | stable in 1 of 1 calculated diagram(s): 1603.09–1822.74 K, x(Si) 0.375–0.375 | 0 | 1 |
| [RUSI](#phase-ru-si-rusi); _phase:ru-si:rusi_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–2103.4 K, x(Si) 0.5–0.5 | 41 | 4 |

## DIAMOND_A4 (Ru–Si)

- Id: `phase:ru-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.61 K, x(Si) 0.98397–1
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:a4-diamond)

Names (8): _corpus: _corpus:phase:ru-si:a4-diamond, corpus:phase:ru-si:diamond-a4  
_paper: _paper:10.1016/j.jallcom.2009.01.079:Diamond (Si), paper:10.1016/s0925-8388(01)00931-8:Diamond  
_tdb: _tdb:RuSi-01Du-LB.tdb:DIAMOND_A4, tdb:RuSi-01Liu.tdb:DIAMOND_A4, tdb:RuSi-09Lon.tdb:DIAMOND_A4, tdb:RuSi-95Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): DIAMOND_A4, type code %, sha256 `52402724aa676957…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): DIAMOND_A4, type code %, sha256 `a229255af0c2e5ae…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): DIAMOND_A4, type code %, sha256 `6b726c2f0814471a…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SI : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): DIAMOND_A4, type code %, sha256 `fac3db235d64c253…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : RU SI% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(98)00911-6](https://doi.org/10.1016/s0925-8388%2898%2900911-6) L. Perring, F. Bussy, J.C. Gachon, P. Feschotte, The Ruthenium–Silicon system, Journal of Alloys and Compounds 284, 198-205 (1999).  
_cited as the source of values for this phase_

## BCC_A2 (Ru–Si)

- Id: `phase:ru-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:bcc-a2)

Names (5): _corpus: _corpus:phase:ru-si:bcc-a2  
_tdb: _tdb:RuSi-01Du-LB.tdb:BCC_A2, tdb:RuSi-01Liu.tdb:BCC_A2, tdb:RuSi-09Lon.tdb:BCC_A2, tdb:RuSi-95Che.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): BCC_A2, type code %B, sha256 `52402724aa676957…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : RU SI : VA : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): BCC_A2, type code %B, sha256 `a229255af0c2e5ae…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : RU SI : VA : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): BCC_A2, type code %B, sha256 `6b726c2f0814471a…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : RU SI : VA : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): BCC_A2, type code %B, sha256 `fac3db235d64c253…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : RU SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_

## FCC_A1 (Ru–Si)

- Id: `phase:ru-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:fcc-a1)

Names (5): _corpus: _corpus:phase:ru-si:fcc-a1  
_tdb: _tdb:RuSi-01Du-LB.tdb:FCC_A1, tdb:RuSi-01Liu.tdb:FCC_A1, tdb:RuSi-09Lon.tdb:FCC_A1, tdb:RuSi-95Che.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): FCC_A1, type code %A, sha256 `52402724aa676957…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : RU SI : VA : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): FCC_A1, type code %A, sha256 `a229255af0c2e5ae…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : RU SI : VA : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): FCC_A1, type code %A, sha256 `6b726c2f0814471a…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : RU SI : VA : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): FCC_A1, type code %A, sha256 `fac3db235d64c253…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : RU SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_

## HCP_A3 (Ru–Si)

- Id: `phase:ru-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2627.41 K, x(Si) 0–0.05336
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:hcp-a3)

Names (7): _corpus: _corpus:phase:ru-si:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.01.079:Hcp (Ru), paper:10.1016/s0925-8388(01)00931-8:(Ru)  
_tdb: _tdb:RuSi-01Du-LB.tdb:HCP_A3, tdb:RuSi-01Liu.tdb:HCP_A3, tdb:RuSi-09Lon.tdb:HCP_A3, tdb:RuSi-95Che.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): HCP_A3, type code %, sha256 `52402724aa676957…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : RU% SI : VA : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): HCP_A3, type code %, sha256 `a229255af0c2e5ae…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : RU% SI : VA : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): HCP_A3, type code %, sha256 `6b726c2f0814471a…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : RU% SI : VA : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): HCP_A3, type code %, sha256 `fac3db235d64c253…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : RU% SI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(98)00911-6](https://doi.org/10.1016/s0925-8388%2898%2900911-6) L. Perring, F. Bussy, J.C. Gachon, P. Feschotte, The Ruthenium–Silicon system, Journal of Alloys and Compounds 284, 198-205 (1999).  
_cited as the source of values for this phase_

## LIQUID (Ru–Si)

- Id: `phase:ru-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1561.64–4000 K, x(Si) 0–1
- Literature: 50 values (50 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:liquid)

Names (7): _corpus: _corpus:phase:ru-si:liquid  
_paper: _paper:10.1016/j.jallcom.2009.01.079:L, paper:10.1016/s0925-8388(01)00931-8:liquid  
_tdb: _tdb:RuSi-01Du-LB.tdb:LIQUID, tdb:RuSi-01Liu.tdb:LIQUID, tdb:RuSi-09Lon.tdb:LIQUID, tdb:RuSi-95Che.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): LIQUID, type code %, sha256 `52402724aa676957…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : RU SI : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): LIQUID, type code %, sha256 `a229255af0c2e5ae…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : RU SI : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): LIQUID, type code %, sha256 `6b726c2f0814471a…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : RU SI : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): LIQUID, type code %, sha256 `fac3db235d64c253…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : RU SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(98)00911-6](https://doi.org/10.1016/s0925-8388%2898%2900911-6) L. Perring, F. Bussy, J.C. Gachon, P. Feschotte, The Ruthenium–Silicon system, Journal of Alloys and Compounds 284, 198-205 (1999).  
_cited as the source of values for this phase_

## RU2SI_C37 (Ru–Si)

- Id: `phase:ru-si:ru2si-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: Ru 0.6667, Si 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 1506.67–1822.42 K, x(Si) 0.33333–0.33333
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:ru2si-c37)

Names (7): _corpus: _corpus:phase:ru-si:ru2si-c37  
_paper: _paper:10.1016/j.jallcom.2009.01.079:Ru2Si, paper:10.1016/s0925-8388(01)00931-8:Ru2Si  
_tdb: _tdb:RuSi-01Du-LB.tdb:RU2SI_C37, tdb:RuSi-01Liu.tdb:RU2SI_C37, tdb:RuSi-09Lon.tdb:RU2SI_C37, tdb:RuSi-95Che.tdb:RU2SI_C37  


### TDB models of RU2SI_C37 (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): RU2SI_C37, type code %, sha256 `52402724aa676957…`

~~~~text
48: PHASE RU2SI_C37 % 2 2 1 !
49: CONST RU2SI_C37 : RU : SI : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): RU2SI_C37, type code %, sha256 `a229255af0c2e5ae…`

~~~~text
51: PHASE RU2SI_C37 % 2 2 1 !
52: CONST RU2SI_C37 : RU : SI : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): RU2SI_C37, type code %, sha256 `6b726c2f0814471a…`

~~~~text
52: PHASE RU2SI_C37 % 2 2 1 !
53: CONST RU2SI_C37 : RU : SI : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): RU2SI_C37, type code %, sha256 `fac3db235d64c253…`

~~~~text
54: PHASE RU2SI_C37 % 2 2 1 !
55: CONST RU2SI_C37 : RU : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(98)00911-6](https://doi.org/10.1016/s0925-8388%2898%2900911-6) L. Perring, F. Bussy, J.C. Gachon, P. Feschotte, The Ruthenium–Silicon system, Journal of Alloys and Compounds 284, 198-205 (1999).  
_cited as the source of values for this phase_

## RU2SI3 (Ru–Si)

- Id: `phase:ru-si:ru2si3`; status `needs_review`
- No structure assigned. Why: no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Pbcn (60) — on-hull MP Si3Ru2 at x(SI)=0.6000
- Candidate (dft_oqmd): Pbcn (60) — on-hull OQMD Ru2 Si3 at x(SI)=0.6000
- Candidate (sgte_mmc2): Ge3Ru2 · oP40 · Pbcn (60) — Hallstedt 2025 mmc2 row for RU2SI3: alpha-Ru2Si3 (see also Ru2Si3)
- Candidate (sgte_mmc2): (Ru2Si3) · tI80 · P-4c2 (116) — Hallstedt 2025 mmc2 row for RU2SI3: beta-Ru2Si3 (see also Ge3Ru2)
- Candidate (tdb_comment): Ge3Ru2 · oP40 · Pbcn — RuSi-01Du-LB.tdb: 'Prototype Ge3Ru2 (oP40, Pbcn), alpha-Ru2Si3'
- Candidate (tdb_comment): Ge3Ru2 · oP40 · Pbcn — RuSi-01Liu.tdb: 'Prototype Ge3Ru2 (oP40, Pbcn), alpha-Ru2Si3'
- Candidate (tdb_comment): Ge3Ru2 · oP40 · Pbcn — RuSi-09Lon.tdb: 'Prototype Ge3Ru2 (oP40, Pbcn), alpha-Ru2Si3'
- Candidate (tdb_comment): Ge3Ru2 · oP40 · Pbcn — RuSi-95Che.tdb: 'Prototype Ge3Ru2 (oP40, Pbcn), alpha-Ru2Si3'
- Stoichiometry: Ru 0.4000, Si 0.6000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1985.87 K, x(Si) 0.6–0.6
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:ru2si3)

Names (7): _corpus: _corpus:phase:ru-si:ru2si3  
_paper: _paper:10.1016/j.jallcom.2009.01.079:Ru2Si3, paper:10.1016/s0925-8388(01)00931-8:Ru2Si3  
_tdb: _tdb:RuSi-01Du-LB.tdb:RU2SI3, tdb:RuSi-01Liu.tdb:RU2SI3, tdb:RuSi-09Lon.tdb:RU2SI3, tdb:RuSi-95Che.tdb:RU2SI3  


### TDB models of RU2SI3 (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): RU2SI3, type code %, sha256 `52402724aa676957…`

~~~~text
65: PHASE RU2SI3 % 2 2 3 !
66: CONST RU2SI3 : RU : SI : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): RU2SI3, type code %, sha256 `a229255af0c2e5ae…`

~~~~text
68: PHASE RU2SI3 % 2 2 3 !
69: CONST RU2SI3 : RU : SI : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): RU2SI3, type code %, sha256 `6b726c2f0814471a…`

~~~~text
69: PHASE RU2SI3 % 2 2 3 !
70: CONST RU2SI3 : RU : SI : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): RU2SI3, type code %, sha256 `fac3db235d64c253…`

~~~~text
76: PHASE RU2SI3 % 2 2 3 !
77: CONST RU2SI3 : RU : SI : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(98)00911-6](https://doi.org/10.1016/s0925-8388%2898%2900911-6) L. Perring, F. Bussy, J.C. Gachon, P. Feschotte, The Ruthenium–Silicon system, Journal of Alloys and Compounds 284, 198-205 (1999).  
_cited as the source of values for this phase_
- [doi:10.1016/s0040-6031(97)00041-5](https://doi.org/10.1016/s0040-6031%2897%2900041-5) L. Perring, P. Feschotte, J.C. Gachon, Enthalpies of formation of RuSi and RuSn compounds by direct reaction calorimetry, Thermochimica Acta 293, 101-108 (1997).  
_cited as the source of values for this phase_
- [doi:10.1002/bbpc.19981020925](https://doi.org/10.1002/bbpc.19981020925) L. Perring, F. Bussy, J. J. Kuntz, J. C. Gachon, IV. Progress in experimental methods: Thermodynamic investigations in the Si‐Ge‐rich part of the ruthenium‐silicon‐germanium system, Ber Bunsenges Phys Chem 102, 1211-1216 (1998).  
_cited as the source of values for this phase_
- [doi:10.1006/jssc.1997.7508](https://doi.org/10.1006/jssc.1997.7508) J.J. Kuntz, L. Perring, P. Feschotte, J.C. Gachon, Heat Capacity and Heat Content Measurements on Binary Compounds in the Ru–Si, Ru–Ge, and Ru–Sn Systems, Journal of Solid State Chemistry 133, 439-444 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00504-0](https://doi.org/10.1016/s0925-8388%2898%2900504-0) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of some 4d transition metal silicides by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 274, 193-200 (1998).  
_cited as the source of values for this phase_
- [doi:10.1063/1.331319](https://doi.org/10.1063/1.331319) C. S. Petersson, J. E. E. Baglin, J. J. Dempsey, F. M. d’Heurle, S. J. La Placa, Silicides of ruthenium and osmium: Thin film reactions, diffusion, nucleation, and stability, Journal of Applied Physics 53, 4866-4883 (1982).  
_cited as the source of values for this phase_

## RU4SI3 (Ru–Si)

- Id: `phase:ru-si:ru4si3`; status `assigned`
- Structure: Ru4Si3 · oP28 · Pnma (62); type `st:ru4si3-op28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.5714, Si 0.4286
- Stability: stable in 4 of 4 calculated diagram(s): 300–1948.13 K, x(Si) 0.42857–0.42857
- Literature: 26 values (26 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:ru4si3)

Names (7): _corpus: _corpus:phase:ru-si:ru4si3  
_paper: _paper:10.1016/j.jallcom.2009.01.079:Ru4Si3, paper:10.1016/s0925-8388(01)00931-8:Ru4Si3  
_tdb: _tdb:RuSi-01Du-LB.tdb:RU4SI3, tdb:RuSi-01Liu.tdb:RU4SI3, tdb:RuSi-09Lon.tdb:RU4SI3, tdb:RuSi-95Che.tdb:RU4SI3  


### TDB models of RU4SI3 (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): RU4SI3, type code %, sha256 `52402724aa676957…`

~~~~text
53: PHASE RU4SI3 % 2 4 3 !
54: CONST RU4SI3 : RU : SI : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): RU4SI3, type code %, sha256 `a229255af0c2e5ae…`

~~~~text
56: PHASE RU4SI3 % 2 4 3 !
57: CONST RU4SI3 : RU : SI : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): RU4SI3, type code %, sha256 `6b726c2f0814471a…`

~~~~text
57: PHASE RU4SI3 % 2 4 3 !
58: CONST RU4SI3 : RU : SI : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): RU4SI3, type code %, sha256 `fac3db235d64c253…`

~~~~text
64: PHASE RU4SI3 % 2 4 3 !
65: CONST RU4SI3 : RU : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(98)00911-6](https://doi.org/10.1016/s0925-8388%2898%2900911-6) L. Perring, F. Bussy, J.C. Gachon, P. Feschotte, The Ruthenium–Silicon system, Journal of Alloys and Compounds 284, 198-205 (1999).  
_cited as the source of values for this phase_
- [doi:10.1016/s0040-6031(97)00041-5](https://doi.org/10.1016/s0040-6031%2897%2900041-5) L. Perring, P. Feschotte, J.C. Gachon, Enthalpies of formation of RuSi and RuSn compounds by direct reaction calorimetry, Thermochimica Acta 293, 101-108 (1997).  
_cited as the source of values for this phase_

## RU5SI3 (Ru–Si)

- Id: `phase:ru-si:ru5si3`; status `unresolved_no_candidates`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Stoichiometry: Ru 0.6250, Si 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 1603.09–1822.74 K, x(Si) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:ru5si3)

Names (2): _corpus: _corpus:phase:ru-si:ru5si3  
_tdb: _tdb:RuSi-95Che.tdb:RU5SI3  


### TDB models of RU5SI3 (1): PHASE and CONSTITUENT statements as written

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): RU5SI3, type code %, sha256 `fac3db235d64c253…`

~~~~text
59: PHASE RU5SI3 % 2 5 3 !
60: CONST RU5SI3 : RU : SI : !
~~~~

## RUSI (Ru–Si)

- Id: `phase:ru-si:rusi`; status `needs_review`
- No structure assigned. Why: dft_space_group_198_matches_2_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P2_13 (198) — on-hull MP SiRu at x(SI)=0.5000
- Candidate (dft_oqmd): P213 (198) — on-hull OQMD Ru1 Si1 at x(SI)=0.5000
- Candidate (dft_space_group_and_stoichiometry): FeSi · B20 · cP8 · P2_13 (198) — space group 198 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): alpha-CO · B21 · cP8 · P2_13 (198) — space group 198 and stoichiometry match
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for RUSI: beta-RuSi (see also FeSi)
- Candidate (sgte_mmc2): FeSi · B20 · cP8 · P2_13 (198) — Hallstedt 2025 mmc2 row for RUSI: alpha-RuSi (see also CsCl)
- Candidate (tdb_comment): FeSi · cP8 · P2_13, B20 — RuSi-01Du-LB.tdb: 'Prototype FeSi (cP8, P2_13, B20), alpha-RuSi'
- Candidate (tdb_comment): FeSi · cP8 · P2_13, B20 — RuSi-01Liu.tdb: 'Prototype FeSi (cP8, P2_13, B20), alpha-RuSi'
- Stoichiometry: Ru 0.5000, Si 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2103.4 K, x(Si) 0.5–0.5
- Literature: 41 values (41 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-si:rusi)

Names (7): _corpus: _corpus:phase:ru-si:rusi  
_paper: _paper:10.1016/j.jallcom.2009.01.079:RuSi, paper:10.1016/s0925-8388(01)00931-8:RuSi  
_tdb: _tdb:RuSi-01Du-LB.tdb:RUSI, tdb:RuSi-01Liu.tdb:RUSI, tdb:RuSi-09Lon.tdb:RUSI, tdb:RuSi-95Che.tdb:RUSI  


### TDB models of RUSI (4): PHASE and CONSTITUENT statements as written

[RuSi-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Du-LB.tdb): RUSI, type code %, sha256 `52402724aa676957…`

~~~~text
59: PHASE RUSI % 2 1 1 !
60: CONST RUSI : RU : SI : !
~~~~

[RuSi-01Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-01Liu.tdb): RUSI, type code %, sha256 `a229255af0c2e5ae…`

~~~~text
62: PHASE RUSI % 2 1 1 !
63: CONST RUSI : RU : SI : !
~~~~

[RuSi-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-09Lon.tdb): RUSI, type code %, sha256 `6b726c2f0814471a…`

~~~~text
63: PHASE RUSI % 2 1 1 !
64: CONST RUSI : RU : SI : !
~~~~

[RuSi-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSi-95Che.tdb): RUSI, type code %, sha256 `fac3db235d64c253…`

~~~~text
70: PHASE RUSI % 2 1 1 !
71: CONST RUSI : RU : SI : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/ijmr-2001-0064](https://doi.org/10.3139/ijmr-2001-0064) Y. Du, K.H. Chen, J.C. Schuster, L. Perring, B.Y. Huang, Z.H. Yuan, J.C. Gachon, Z. Metallkd., 92, 323-27(2001).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(98)00911-6](https://doi.org/10.1016/s0925-8388%2898%2900911-6) L. Perring, F. Bussy, J.C. Gachon, P. Feschotte, The Ruthenium–Silicon system, Journal of Alloys and Compounds 284, 198-205 (1999).  
_cited as the source of values for this phase_
- [doi:10.1016/s0040-6031(97)00041-5](https://doi.org/10.1016/s0040-6031%2897%2900041-5) L. Perring, P. Feschotte, J.C. Gachon, Enthalpies of formation of RuSi and RuSn compounds by direct reaction calorimetry, Thermochimica Acta 293, 101-108 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00504-0](https://doi.org/10.1016/s0925-8388%2898%2900504-0) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of some 4d transition metal silicides by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 274, 193-200 (1998).  
_cited as the source of values for this phase_
- [doi:10.1006/jssc.1997.7508](https://doi.org/10.1006/jssc.1997.7508) J.J. Kuntz, L. Perring, P. Feschotte, J.C. Gachon, Heat Capacity and Heat Content Measurements on Binary Compounds in the Ru–Si, Ru–Ge, and Ru–Sn Systems, Journal of Solid State Chemistry 133, 439-444 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/0038-1101(78)90335-0](https://doi.org/10.1016/0038-1101%2878%2990335-0) R. Pretorius, J.M. Harris, M-A. Nicolet, Reaction of thin metal films with SiO2 substrates, Solid-State Electronics 21, 667-675 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(81)90013-4](https://doi.org/10.1016/0364-5916%2881%2990013-4) E.S. Machlin, Calphad 5 (1981) 1.  
_cited as the source of values for this phase_
- [doi:10.1063/1.331319](https://doi.org/10.1063/1.331319) C. S. Petersson, J. E. E. Baglin, J. J. Dempsey, F. M. d’Heurle, S. J. La Placa, Silicides of ruthenium and osmium: Thin film reactions, diffusion, nucleation, and stability, Journal of Applied Physics 53, 4866-4883 (1982).  
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
