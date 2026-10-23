# Co–Hf phases

> Co–Hf system: 11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-HF.html · Markdown: https://data.orchid-project.org/phases/pages/CO-HF.md

11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-HF) · [full JSON](https://data.orchid-project.org/phases/systems/CO-HF.json) · [Co–Hf system page](https://data.orchid-project.org/systems/CO-HF.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-HF.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Hf system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-hf-bcc-a2); _phase:co-hf:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 5 calculated diagram(s): 1480–3999.74 K, x(Hf) 0.84811–1 | 7 | 5 |
| [B2_BCC](#phase-co-hf-bcc-b2); _phase:co-hf:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3531.03 K, x(Hf) 0.48209–1 | 8 | 2 |
| [C15_LAVES](#phase-co-hf-c15-laves); _phase:co-hf:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1895.96 K, x(Hf) 0.25028–0.34687 | 20 | 2 |
| [CO11HF2](#phase-co-hf-co11hf2); _phase:co-hf:co11hf2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 928.48–1545.8 K, x(Hf) 0.15385–0.15385 | 9 | 2 |
| [CO23HF6_D8A](#phase-co-hf-co23hf6-d8a); _phase:co-hf:co23hf6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1600 K, x(Hf) 0.2069–0.2069 | 11 | 2 |
| [CO2HF_C15](#phase-co-hf-co2hf-c15); _phase:co-hf:co2hf-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2065.65 K, x(Hf) 0.33333–0.33333 | 0 | 1 |
| [COHF_B2](#phase-co-hf-cohf-b2); _phase:co-hf:cohf-b2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2028.18 K, x(Hf) 0.5–0.5 | 0 | 1 |
| [COHF2](#phase-co-hf-cohf2); _phase:co-hf:cohf2_ | NiTi2 · cF96 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1699.29 K, x(Hf) 0.65937–0.68042 | 18 | 3 |
| [FCC_A1](#phase-co-hf-fcc-a1); _phase:co-hf:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 694.96–1773.17 K, x(Hf) 0–0.01466 | 8 | 3 |
| [HCP_A3](#phase-co-hf-hcp-a3); _phase:co-hf:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2500.33 K, x(Hf) 0–1 | 2 | 3 |
| [LIQUID](#phase-co-hf-liquid); _phase:co-hf:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1516.31–4000 K, x(Hf) 0–1 | 25 | 3 |

## BCC_A2 (Co–Hf)

- Id: `phase:co-hf:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 5 calculated diagram(s): 1480–3999.74 K, x(Hf) 0.84811–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:bcc-a2)

Names (8): _corpus: _corpus:phase:co-hf:bcc-a2  
_paper: _paper:10.1016/j.tca.2015.04.004:(βHf), paper:10.1016/j.tca.2015.04.004:(εCo)  
_tdb: _tdb:CoHf-06Bra.tdb:BCC_A2, tdb:CoHf-15Lu.tdb:A2_BCC, tdb:CoHf-15Lu.tdb:BCC_A2, tdb:CoHf-18Hua.tdb:A2_BCC, tdb:CoHf-18Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[CoHf-06Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-06Bra.tdb): BCC_A2, type code %B, sha256 `046d63a555f58b79…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CO HF% : VA : !
~~~~

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): A2_BCC, type code %B, sha256 `dffa8495cab9319c…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : CO HF VA : VA : !
~~~~

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): BCC_A2, type code %B, sha256 `dffa8495cab9319c…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CO HF% : VA : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): A2_BCC, type code %B, sha256 `065a8d8f49f9e2c1…`

~~~~text
37: PHASE A2_BCC %B 2 1 3 !
38: CONST A2_BCC : CO HF VA : VA : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): BCC_A2, type code %B, sha256 `065a8d8f49f9e2c1…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO HF% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1361/154770306X109746](https://doi.org/10.1361/154770306X109746) J. Bratberg, B. Jansson, J. Phase Equilib. Diffus., 27, 213-19(2006).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_

## B2_BCC (Co–Hf)

- Id: `phase:co-hf:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: CoHf-15Lu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CoHf-18Hua.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in CoHf-15Lu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoHf-18Hua.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–3531.03 K, x(Hf) 0.48209–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:bcc-b2)

Names (5): _corpus: _corpus:phase:co-hf:bcc-b2, corpus:phase:co-hf:b2-bcc  
_paper: _paper:10.1016/j.tca.2015.04.004:CoHf  
_tdb: _tdb:CoHf-15Lu.tdb:B2_BCC, tdb:CoHf-18Hua.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): B2_BCC, type code %BO, sha256 `dffa8495cab9319c…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : CO% HF VA : CO HF% VA : VA : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): B2_BCC, type code %BO, sha256 `065a8d8f49f9e2c1…`

~~~~text
42: PHASE B2_BCC %BO 3 0.5 0.5 3 !
43: CONST B2_BCC : CO% HF VA : CO HF% VA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_

## C15_LAVES (Co–Hf)

- Id: `phase:co-hf:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoHf-15Lu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoHf-18Hua.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1895.96 K, x(Hf) 0.25028–0.34687
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:c15-laves)

Names (4): _corpus: _corpus:phase:co-hf:c15-laves  
_paper: _paper:10.1016/j.tca.2015.04.004:Co2Hf  
_tdb: _tdb:CoHf-15Lu.tdb:C15_LAVES, tdb:CoHf-18Hua.tdb:C15_LAVES  


### TDB models of C15_LAVES (2): PHASE and CONSTITUENT statements as written

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): C15_LAVES, type code %, sha256 `dffa8495cab9319c…`

~~~~text
65: PHASE C15_LAVES % 2 2 1 !
66: CONST C15_LAVES : CO% HF : CO HF% : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): C15_LAVES, type code %, sha256 `065a8d8f49f9e2c1…`

~~~~text
62: PHASE C15_LAVES % 2 2 1 !
63: CONST C15_LAVES : CO% HF : CO HF% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90111-x](https://doi.org/10.1016/0022-5088%2878%2990111-x) K.H.J. Buschow, J.H. Wernick, G.Y. Chin, Note on the Hf-Co phase diagram, Journal of the Less Common Metals 59, 61-67 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_

## CO11HF2 (Co–Hf)

- Id: `phase:co-hf:co11hf2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Co11Hf2) · oP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Co11Hf2) · Pban (50) — Hallstedt 2025 mmc2 row for CO11HF2: Co11Hf2
- Stoichiometry: Co 0.8462, Hf 0.1538
- Stability: stable in 2 of 2 calculated diagram(s): 928.48–1545.8 K, x(Hf) 0.15385–0.15385
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:co11hf2)

Names (4): _corpus: _corpus:phase:co-hf:co11hf2  
_paper: _paper:10.1016/j.tca.2015.04.004:Co11Hf2  
_tdb: _tdb:CoHf-15Lu.tdb:CO11HF2, tdb:CoHf-18Hua.tdb:CO11HF2  


### TDB models of CO11HF2 (2): PHASE and CONSTITUENT statements as written

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): CO11HF2, type code %, sha256 `dffa8495cab9319c…`

~~~~text
55: PHASE CO11HF2 % 2 11 2 !
56: CONST CO11HF2 : CO : HF : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): CO11HF2, type code %, sha256 `065a8d8f49f9e2c1…`

~~~~text
52: PHASE CO11HF2 % 2 11 2 !
53: CONST CO11HF2 : CO : HF : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90111-x](https://doi.org/10.1016/0022-5088%2878%2990111-x) K.H.J. Buschow, J.H. Wernick, G.Y. Chin, Note on the Hf-Co phase diagram, Journal of the Less Common Metals 59, 61-67 (1978).  
_cited as the source of values for this phase_

## CO23HF6_D8A (Co–Hf)

- Id: `phase:co-hf:co23hf6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacpwmt and oqmd-29361, space group 225
- Stoichiometry: Co 0.7931, Hf 0.2069
- Stability: stable in 2 of 2 calculated diagram(s): 300–1600 K, x(Hf) 0.2069–0.2069
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:co23hf6-d8a)

Names (6): _corpus: _corpus:phase:co-hf:co23hf6-d8a  
_mp: _mp:mp-aaacpwmt  
_oqmd: _oqmd:oqmd-29361  
_paper: _paper:10.1016/j.tca.2015.04.004:Co23Hf6  
_tdb: _tdb:CoHf-15Lu.tdb:CO23HF6_D8A, tdb:CoHf-18Hua.tdb:CO23HF6_D8A  


### TDB models of CO23HF6_D8A (2): PHASE and CONSTITUENT statements as written

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): CO23HF6_D8A, type code %, sha256 `dffa8495cab9319c…`

~~~~text
60: PHASE CO23HF6_D8A % 2 23 6 !
61: CONST CO23HF6_D8A : CO : HF : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): CO23HF6_D8A, type code %, sha256 `065a8d8f49f9e2c1…`

~~~~text
57: PHASE CO23HF6_D8A % 2 23 6 !
58: CONST CO23HF6_D8A : CO : HF : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90111-x](https://doi.org/10.1016/0022-5088%2878%2990111-x) K.H.J. Buschow, J.H. Wernick, G.Y. Chin, Note on the Hf-Co phase diagram, Journal of the Less Common Metals 59, 61-67 (1978).  
_cited as the source of values for this phase_

## CO2HF_C15 (Co–Hf)

- Id: `phase:co-hf:co2hf-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.6667, Hf 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2065.65 K, x(Hf) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:co2hf-c15)

Names (2): _corpus: _corpus:phase:co-hf:co2hf-c15  
_tdb: _tdb:CoHf-06Bra.tdb:CO2HF_C15  


### TDB models of CO2HF_C15 (1): PHASE and CONSTITUENT statements as written

[CoHf-06Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-06Bra.tdb): CO2HF_C15, type code %, sha256 `046d63a555f58b79…`

~~~~text
44: PHASE CO2HF_C15 % 2 2 1 !
45: CONST CO2HF_C15 : CO : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/154770306X109746](https://doi.org/10.1361/154770306X109746) J. Bratberg, B. Jansson, J. Phase Equilib. Diffus., 27, 213-19(2006).  
_assessment that models this phase_

## COHF_B2 (Co–Hf)

- Id: `phase:co-hf:cohf-b2`; status `needs_review`
- No structure assigned. Why: name_suggests_B2_but_dft_space_group_63
- Candidate (dft_mp): Cmcm (63) — on-hull MP HfCo at x(HF)=0.5000
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Co1 Hf1 at x(HF)=0.5000
- Candidate (name_token): CsCl · B2 · cP2 · Pm-3m (221) — Strukturbericht/word 'B2' in the TDB name
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — CoHf-06Bra.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Stoichiometry: Co 0.5000, Hf 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2028.18 K, x(Hf) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:cohf-b2)

Names (2): _corpus: _corpus:phase:co-hf:cohf-b2  
_tdb: _tdb:CoHf-06Bra.tdb:COHF_B2  


### TDB models of COHF_B2 (1): PHASE and CONSTITUENT statements as written

[CoHf-06Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-06Bra.tdb): COHF_B2, type code %, sha256 `046d63a555f58b79…`

~~~~text
49: PHASE COHF_B2 % 2 1 1 !
50: CONST COHF_B2 : CO : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/154770306X109746](https://doi.org/10.1361/154770306X109746) J. Bratberg, B. Jansson, J. Phase Equilib. Diffus., 27, 213-19(2006).  
_assessment that models this phase_

## COHF2 (Co–Hf)

- Id: `phase:co-hf:cohf2`; status `assigned`
- Structure: NiTi2 · cF96 · Fd-3m (227); type `st:niti2-cf96`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 300–1699.29 K, x(Hf) 0.65937–0.68042
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:cohf2)

Names (5): _corpus: _corpus:phase:co-hf:cohf2  
_paper: _paper:10.1016/j.tca.2015.04.004:CoHf2  
_tdb: _tdb:CoHf-06Bra.tdb:COHF2, tdb:CoHf-15Lu.tdb:COHF2, tdb:CoHf-18Hua.tdb:COHF2  


### TDB models of COHF2 (3): PHASE and CONSTITUENT statements as written

[CoHf-06Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-06Bra.tdb): COHF2, type code %, sha256 `046d63a555f58b79…`

~~~~text
54: PHASE COHF2 % 2 1 2 !
55: CONST COHF2 : CO : HF : !
~~~~

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): COHF2, type code %, sha256 `dffa8495cab9319c…`

~~~~text
70: PHASE COHF2 % 2 1 2 !
71: CONST COHF2 : CO% HF : CO HF% : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): COHF2, type code %, sha256 `065a8d8f49f9e2c1…`

~~~~text
67: PHASE COHF2 % 2 1 2 !
68: CONST COHF2 : CO% HF : CO HF% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1361/154770306X109746](https://doi.org/10.1361/154770306X109746) J. Bratberg, B. Jansson, J. Phase Equilib. Diffus., 27, 213-19(2006).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_

## FCC_A1 (Co–Hf)

- Id: `phase:co-hf:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 694.96–1773.17 K, x(Hf) 0–0.01466
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:fcc-a1)

Names (5): _corpus: _corpus:phase:co-hf:fcc-a1  
_paper: _paper:10.1016/j.tca.2015.04.004:(αCo)  
_tdb: _tdb:CoHf-06Bra.tdb:FCC_A1, tdb:CoHf-15Lu.tdb:FCC_A1, tdb:CoHf-18Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CoHf-06Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-06Bra.tdb): FCC_A1, type code %A, sha256 `046d63a555f58b79…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CO% HF : VA : !
~~~~

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): FCC_A1, type code %A, sha256 `dffa8495cab9319c…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CO% HF : VA : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): FCC_A1, type code %A, sha256 `065a8d8f49f9e2c1…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% HF : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1361/154770306X109746](https://doi.org/10.1361/154770306X109746) J. Bratberg, B. Jansson, J. Phase Equilib. Diffus., 27, 213-19(2006).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90111-x](https://doi.org/10.1016/0022-5088%2878%2990111-x) K.H.J. Buschow, J.H. Wernick, G.Y. Chin, Note on the Hf-Co phase diagram, Journal of the Less Common Metals 59, 61-67 (1978).  
_cited as the source of values for this phase_

## HCP_A3 (Co–Hf)

- Id: `phase:co-hf:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2500.33 K, x(Hf) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:hcp-a3)

Names (5): _corpus: _corpus:phase:co-hf:hcp-a3  
_paper: _paper:10.1016/j.tca.2015.04.004:(αHf)  
_tdb: _tdb:CoHf-06Bra.tdb:HCP_A3, tdb:CoHf-15Lu.tdb:HCP_A3, tdb:CoHf-18Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CoHf-06Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-06Bra.tdb): HCP_A3, type code %A, sha256 `046d63a555f58b79…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CO% HF% : VA : !
~~~~

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): HCP_A3, type code %A, sha256 `dffa8495cab9319c…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : CO% HF% : VA : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): HCP_A3, type code %A, sha256 `065a8d8f49f9e2c1…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CO% HF% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1361/154770306X109746](https://doi.org/10.1361/154770306X109746) J. Bratberg, B. Jansson, J. Phase Equilib. Diffus., 27, 213-19(2006).  
_assessment that models this phase_

## LIQUID (Co–Hf)

- Id: `phase:co-hf:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1516.31–4000 K, x(Hf) 0–1
- Literature: 25 values (25 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-hf:liquid)

Names (5): _corpus: _corpus:phase:co-hf:liquid  
_paper: _paper:10.1016/j.tca.2015.04.004:Liquid  
_tdb: _tdb:CoHf-06Bra.tdb:LIQUID, tdb:CoHf-15Lu.tdb:LIQUID, tdb:CoHf-18Hua.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CoHf-06Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-06Bra.tdb): LIQUID, type code %, sha256 `046d63a555f58b79…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CO HF : !
~~~~

[CoHf-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-15Lu.tdb): LIQUID, type code %, sha256 `dffa8495cab9319c…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CO HF : !
~~~~

[CoHf-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoHf-18Hua.tdb): LIQUID, type code %, sha256 `065a8d8f49f9e2c1…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO HF : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2015.04.004](https://doi.org/10.1016/j.tca.2015.04.004) Xingxu Lu, Shuhong Liu, Kaiming Cheng, Ying Tang, Pengfei Ou, Philip Nash et al., Thermodynamic modeling of the Co–Hf system supported by key experiments and first-principles calculations, Thermochimica Acta 608, 49-58 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.002](https://doi.org/10.1016/j.calphad.2018.06.002) X.M. Huang, W.J. Zeng, J.L. Liu, G.M. Cai, S.H. Liu, H.S. Liu, Z.P. Jin, Calphad, 62, 128-40(2018).  
_assessment that models this phase_
- [doi:10.1361/154770306X109746](https://doi.org/10.1361/154770306X109746) J. Bratberg, B. Jansson, J. Phase Equilib. Diffus., 27, 213-19(2006).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.11.206](https://doi.org/10.1016/j.jallcom.2014.11.206) Xingxu Lu, Kaiming Cheng, Shuhong Liu, Kai Li, Feng Zheng, Yong Du, Experimental investigation of phase equilibria in the Co–Hf system, Journal of Alloys and Compounds 627, 251-260 (2015).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90111-x](https://doi.org/10.1016/0022-5088%2878%2990111-x) K.H.J. Buschow, J.H. Wernick, G.Y. Chin, Note on the Hf-Co phase diagram, Journal of the Less Common Metals 59, 61-67 (1978).  
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
