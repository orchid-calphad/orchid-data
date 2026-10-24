# Co–Si phases

> Co–Si system: 10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-SI.html · Markdown: https://data.orchid-project.org/phases/pages/CO-SI.md

10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-SI) · [full JSON](https://data.orchid-project.org/phases/systems/CO-SI.json) · [Co–Si system page](https://data.orchid-project.org/systems/CO-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Si system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-co-si-a4-diamond); _phase:co-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 1–1 | 5 | 2 |
| [BCC_A2](#phase-co-si-bcc-a2); _phase:co-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [CO2SI_BETA](#phase-co-si-co2si-beta); _phase:co-si:co2si-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1512.3–1594.25 K, x(Si) 0.33337–0.34652 | 13 | 1 |
| [CO2SI_C37](#phase-co-si-co2si-c37); _phase:co-si:co2si-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1603.68 K, x(Si) 0.32229–0.33776 | 26 | 2 |
| [CO3SI_D019](#phase-co-si-co3si-d019); _phase:co-si:co3si-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1467.38–1500 K, x(Si) 0.25–0.25 | 17 | 2 |
| [COSI_B20](#phase-co-si-cosi-b20); _phase:co-si:cosi-b20_ | FeSi · B20 · cP8 · P2_13 (198) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1729.38 K, x(Si) 0.49115–0.51491 | 26 | 2 |
| [COSI2_C1](#phase-co-si-cosi2-c1); _phase:co-si:cosi2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1596.91 K, x(Si) 0.66667–0.66667 | 23 | 2 |
| [FCC_A1](#phase-co-si-fcc-a1); _phase:co-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 687.99–2500 K, x(Si) 0–0.74075 | 5 | 2 |
| [HCP_A3](#phase-co-si-hcp-a3); _phase:co-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1963.38 K, x(Si) 0–0.69033 | 6 | 2 |
| [LIQUID](#phase-co-si-liquid); _phase:co-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1475.55–2500 K, x(Si) 0–1 | 51 | 2 |

## DIAMOND_A4 (Co–Si)

- Id: `phase:co-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 1–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:a4-diamond)

Names (6): _corpus: _corpus:phase:co-si:a4-diamond, corpus:phase:co-si:diamond-a4  
_paper: _paper:10.1016/0364-5916(92)90003-g:Si, paper:10.1016/j.calphad.2006.06.001:(Si)  
_tdb: _tdb:CoSi-06Zha.tdb:DIAMOND_A4, tdb:CoSi-92Cho-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): DIAMOND_A4, type code %, sha256 `849716b03f938610…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): DIAMOND_A4, type code %, sha256 `9fb5aa520ab17aa5…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1937.1.3_135](https://doi.org/10.2320/jinstmet1937.1.3_135) Uichi Haschimoto, The Equilibrium Diagram of the Cobalt-Silicon system, J.Japan Inst.Metals 1, 135-143 (1937).  
_cited as the source of values for this phase_

## BCC_A2 (Co–Si)

- Id: `phase:co-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:bcc-a2)

Names (3): _corpus: _corpus:phase:co-si:bcc-a2  
_tdb: _tdb:CoSi-06Zha.tdb:BCC_A2, tdb:CoSi-92Cho-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): BCC_A2, type code %B, sha256 `849716b03f938610…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO SI : VA : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): BCC_A2, type code %B, sha256 `9fb5aa520ab17aa5…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CO SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase_

## CO2SI_BETA (Co–Si)

- Id: `phase:co-si:co2si-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Co2Si) — Hallstedt 2025 mmc2 row for CO2SI_BETA: beta-Co2Si
- Stability: stable in 1 of 1 calculated diagram(s): 1512.3–1594.25 K, x(Si) 0.33337–0.34652
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:co2si-beta)

Names (3): _corpus: _corpus:phase:co-si:co2si-beta  
_paper: _paper:10.1016/j.calphad.2006.06.001:βCo2Si  
_tdb: _tdb:CoSi-06Zha.tdb:CO2SI_BETA  


### TDB models of CO2SI_BETA (1): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): CO2SI_BETA, type code %, sha256 `849716b03f938610…`

~~~~text
58: PHASE CO2SI_BETA % 2 2 1 !
59: CONST CO2SI_BETA : CO% SI : CO SI% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.193400094](https://doi.org/10.1002/srin.193400094) Rudolf Vogel, Kurt Rosenthal, Das Zustandsschaubild Kobalt-Silizium, Archiv für das Eisenhüttenwesen 7, 689-691 (1934).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1937.1.3_135](https://doi.org/10.2320/jinstmet1937.1.3_135) Uichi Haschimoto, The Equilibrium Diagram of the Cobalt-Silicon system, J.Japan Inst.Metals 1, 135-143 (1937).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645074](https://doi.org/10.1007/bf02645074) K Ishida, T Nishizawa, M. E Schlesinger, The Co-Si (Cobalt-Silicon) system, JPE 12, 578-586 (1991).  
_cited as the source of values for this phase_

## CO2SI_C37 (Co–Si)

- Id: `phase:co-si:co2si-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoSi-06Zha.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1603.68 K, x(Si) 0.32229–0.33776
- Literature: 26 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:co2si-c37)

Names (5): _corpus: _corpus:phase:co-si:co2si-c37  
_paper: _paper:10.1016/0364-5916(92)90003-g:Co2Si, paper:10.1016/j.calphad.2006.06.001:αCo2Si  
_tdb: _tdb:CoSi-06Zha.tdb:CO2SI_C37, tdb:CoSi-92Cho-LB.tdb:CO2SI_C37  


### TDB models of CO2SI_C37 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): CO2SI_C37, type code %, sha256 `849716b03f938610…`

~~~~text
53: PHASE CO2SI_C37 % 2 2 1 !
54: CONST CO2SI_C37 : CO% SI : CO SI% : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): CO2SI_C37, type code %, sha256 `9fb5aa520ab17aa5…`

~~~~text
59: PHASE CO2SI_C37 % 2 2 1 !
60: CONST CO2SI_C37 : CO : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.193400094](https://doi.org/10.1002/srin.193400094) Rudolf Vogel, Kurt Rosenthal, Das Zustandsschaubild Kobalt-Silizium, Archiv für das Eisenhüttenwesen 7, 689-691 (1934).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1937.1.3_135](https://doi.org/10.2320/jinstmet1937.1.3_135) Uichi Haschimoto, The Equilibrium Diagram of the Cobalt-Silicon system, J.Japan Inst.Metals 1, 135-143 (1937).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645074](https://doi.org/10.1007/bf02645074) K Ishida, T Nishizawa, M. E Schlesinger, The Co-Si (Cobalt-Silicon) system, JPE 12, 578-586 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(72)90001-6](https://doi.org/10.1016/0001-6160%2872%2990001-6) J Van Den Boomgaard, F.M.A Carpay, The eutectoid Co3Si phase in the Co-Si system, Acta Metallurgica 20, 473-476 (1972).  
_cited as the source of values for this phase_

## CO3SI_D019 (Co–Si)

- Id: `phase:co-si:co3si-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.7500, Si 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 1467.38–1500 K, x(Si) 0.25–0.25
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:co3si-d019)

Names (5): _corpus: _corpus:phase:co-si:co3si-d019  
_paper: _paper:10.1016/0364-5916(92)90003-g:Co3Si, paper:10.1016/j.calphad.2006.06.001:αCo3Si  
_tdb: _tdb:CoSi-06Zha.tdb:CO3SI_D019, tdb:CoSi-92Cho-LB.tdb:CO3SI_D019  


### TDB models of CO3SI_D019 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): CO3SI_D019, type code %, sha256 `849716b03f938610…`

~~~~text
48: PHASE CO3SI_D019 % 2 3 1 !
49: CONST CO3SI_D019 : CO : SI : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): CO3SI_D019, type code %, sha256 `9fb5aa520ab17aa5…`

~~~~text
54: PHASE CO3SI_D019 % 2 3 1 !
55: CONST CO3SI_D019 : CO : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.193400094](https://doi.org/10.1002/srin.193400094) Rudolf Vogel, Kurt Rosenthal, Das Zustandsschaubild Kobalt-Silizium, Archiv für das Eisenhüttenwesen 7, 689-691 (1934).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(72)90001-6](https://doi.org/10.1016/0001-6160%2872%2990001-6) J Van Den Boomgaard, F.M.A Carpay, The eutectoid Co3Si phase in the Co-Si system, Acta Metallurgica 20, 473-476 (1972).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1937.1.3_135](https://doi.org/10.2320/jinstmet1937.1.3_135) Uichi Haschimoto, The Equilibrium Diagram of the Cobalt-Silicon system, J.Japan Inst.Metals 1, 135-143 (1937).  
_cited as the source of values for this phase_

## COSI_B20 (Co–Si)

- Id: `phase:co-si:cosi-b20`; status `assigned`
- Structure: FeSi · B20 · cP8 · P2_13 (198); type `st:b20-fesi-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoSi-06Zha.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1729.38 K, x(Si) 0.49115–0.51491
- Literature: 26 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:cosi-b20)

Names (5): _corpus: _corpus:phase:co-si:cosi-b20  
_paper: _paper:10.1016/0364-5916(92)90003-g:CoSi, paper:10.1016/j.calphad.2006.06.001:CoSi  
_tdb: _tdb:CoSi-06Zha.tdb:COSI_B20, tdb:CoSi-92Cho-LB.tdb:COSI_B20  


### TDB models of COSI_B20 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): COSI_B20, type code %, sha256 `849716b03f938610…`

~~~~text
63: PHASE COSI_B20 % 2 1 1 !
64: CONST COSI_B20 : CO% SI : CO SI% : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): COSI_B20, type code %, sha256 `9fb5aa520ab17aa5…`

~~~~text
64: PHASE COSI_B20 % 2 1 1 !
65: CONST COSI_B20 : CO : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1937.1.3_135](https://doi.org/10.2320/jinstmet1937.1.3_135) Uichi Haschimoto, The Equilibrium Diagram of the Cobalt-Silicon system, J.Japan Inst.Metals 1, 135-143 (1937).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193400094](https://doi.org/10.1002/srin.193400094) Rudolf Vogel, Kurt Rosenthal, Das Zustandsschaubild Kobalt-Silizium, Archiv für das Eisenhüttenwesen 7, 689-691 (1934).  
_cited as the source of values for this phase_

## COSI2_C1 (Co–Si)

- Id: `phase:co-si:cosi2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadnn and oqmd-5256, space group 225
- Stoichiometry: Co 0.3333, Si 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1596.91 K, x(Si) 0.66667–0.66667
- Literature: 23 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:cosi2-c1)

Names (7): _corpus: _corpus:phase:co-si:cosi2-c1  
_mp: _mp:mp-aaaaadnn  
_oqmd: _oqmd:oqmd-5256  
_paper: _paper:10.1016/0364-5916(92)90003-g:CoSi2, paper:10.1016/j.calphad.2006.06.001:CoSi2  
_tdb: _tdb:CoSi-06Zha.tdb:COSI2_C1, tdb:CoSi-92Cho-LB.tdb:COSI2_C1  


### TDB models of COSI2_C1 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): COSI2_C1, type code %, sha256 `849716b03f938610…`

~~~~text
68: PHASE COSI2_C1 % 2 1 2 !
69: CONST COSI2_C1 : CO : SI : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): COSI2_C1, type code %, sha256 `9fb5aa520ab17aa5…`

~~~~text
69: PHASE COSI2_C1 % 2 1 2 !
70: CONST COSI2_C1 : CO : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1937.1.3_135](https://doi.org/10.2320/jinstmet1937.1.3_135) Uichi Haschimoto, The Equilibrium Diagram of the Cobalt-Silicon system, J.Japan Inst.Metals 1, 135-143 (1937).  
_cited as the source of values for this phase_

## FCC_A1 (Co–Si)

- Id: `phase:co-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 687.99–2500 K, x(Si) 0–0.74075
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:fcc-a1)

Names (5): _corpus: _corpus:phase:co-si:fcc-a1  
_paper: _paper:10.1016/0364-5916(92)90003-g:α-Co, paper:10.1016/j.calphad.2006.06.001:(αCo)  
_tdb: _tdb:CoSi-06Zha.tdb:FCC_A1, tdb:CoSi-92Cho-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): FCC_A1, type code %A, sha256 `849716b03f938610…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO SI : VA : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): FCC_A1, type code %A, sha256 `9fb5aa520ab17aa5…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CO SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Co–Si)

- Id: `phase:co-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1963.38 K, x(Si) 0–0.69033
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:hcp-a3)

Names (4): _corpus: _corpus:phase:co-si:hcp-a3  
_paper: _paper:10.1016/0364-5916(92)90003-g:ε-Co  
_tdb: _tdb:CoSi-06Zha.tdb:HCP_A3, tdb:CoSi-92Cho-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): HCP_A3, type code %A, sha256 `849716b03f938610…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO SI : VA : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): HCP_A3, type code %A, sha256 `9fb5aa520ab17aa5…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CO SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase_

## LIQUID (Co–Si)

- Id: `phase:co-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1475.55–2500 K, x(Si) 0–1
- Literature: 51 values (51 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-si:liquid)

Names (5): _corpus: _corpus:phase:co-si:liquid  
_paper: _paper:10.1016/0364-5916(92)90003-g:L, paper:10.1016/j.calphad.2006.06.001:L  
_tdb: _tdb:CoSi-06Zha.tdb:LIQUID, tdb:CoSi-92Cho-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CoSi-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-06Zha.tdb): LIQUID, type code %, sha256 `849716b03f938610…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO SI : !
~~~~

[CoSi-92Cho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSi-92Cho-LB.tdb): LIQUID, type code %, sha256 `9fb5aa520ab17aa5…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CO SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2006.06.001](https://doi.org/10.1016/j.calphad.2006.06.001) Lijun Zhang, Yong Du, Honghui Xu, Zhu Pan, Experimental investigation and thermodynamic description of the Co–Si system, Calphad 30, 470-481 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90003-G](https://doi.org/10.1016/0364-5916%2892%2990003-G) S.-D. Choi, Calphad, 16, 151-59(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1937.1.3_135](https://doi.org/10.2320/jinstmet1937.1.3_135) Uichi Haschimoto, The Equilibrium Diagram of the Cobalt-Silicon system, J.Japan Inst.Metals 1, 135-143 (1937).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193400094](https://doi.org/10.1002/srin.193400094) Rudolf Vogel, Kurt Rosenthal, Das Zustandsschaubild Kobalt-Silizium, Archiv für das Eisenhüttenwesen 7, 689-691 (1934).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645074](https://doi.org/10.1007/bf02645074) K Ishida, T Nishizawa, M. E Schlesinger, The Co-Si (Cobalt-Silicon) system, JPE 12, 578-586 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(72)90001-6](https://doi.org/10.1016/0001-6160%2872%2990001-6) J Van Den Boomgaard, F.M.A Carpay, The eutectoid Co3Si phase in the Co-Si system, Acta Metallurgica 20, 473-476 (1972).  
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
