# Fe–Ta phases

> Fe–Ta system: 7 phases (tier A 5, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-TA.html · Markdown: https://data.orchid-project.org/phases/pages/FE-TA.md

7 phases (tier A 5, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-TA) · [full JSON](https://data.orchid-project.org/phases/systems/FE-TA.json) · [Fe–Ta system page](https://data.orchid-project.org/systems/FE-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Ta system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-ta-bcc-a2); _phase:fe-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.95 K, x(Ta) 0–1 | 118 | 3 |
| [C14_LAVES](#phase-fe-ta-c14-laves); _phase:fe-ta:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2136.48 K, x(Ta) 0.26945–0.42799 | 31 | 3 |
| [MU_D85](#phase-fe-ta-d85-mu); _phase:fe-ta:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2064.99 K, x(Ta) 0.46154–0.61526 | 49 | 3 |
| [FCC_A1](#phase-fe-ta-fcc-a1); _phase:fe-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 777.33–1742.46 K, x(Ta) 0–0.01061 | 38 | 3 |
| [FE2TA3](#phase-fe-ta-fe2ta3); _phase:fe-ta:fe2ta3_ |  | needs_review | not stable in 1 calculated diagram(s) | 3 | 1 |
| [HCP_A3](#phase-fe-ta-hcp-a3); _phase:fe-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-fe-ta-liquid); _phase:fe-ta:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1716.11–4000 K, x(Ta) 0–1 | 58 | 3 |

## BCC_A2 (Fe–Ta)

- Id: `phase:fe-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.95 K, x(Ta) 0–1
- Literature: 118 values (118 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ta:bcc-a2)

Names (17): _corpus: _corpus:phase:fe-ta:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.12.006:(Ta), paper:10.1016/j.calphad.2014.12.006:(αFe), paper:10.1016/j.calphad.2014.12.006:Laves phase (ε), paper:10.1016/j.calphad.2014.12.006:ε, paper:10.1016/j.intermet.2011.03.018:α, paper:10.1016/j.intermet.2011.03.018:β, paper:10.1016/j.intermet.2011.03.018:δ, paper:10.1016/j.intermet.2011.03.018:λ, ε, TaFe2, paper:10.1016/s0022-3115(03)00196-x:bcc, paper:10.1016/s0022-3115(03)00196-x:α, paper:10.1016/s0022-3115(03)00196-x:δ, paper:10.1016/s0022-3115(03)00196-x:ε, paper:10.1016/s0022-3115(03)00196-x:ε ↔ Liq.  
_tdb: _tdb:FeTa-03Dan.tdb:BCC_A2, tdb:FeTa-11Wit.tdb:BCC_A2, tdb:FeTa-15Raj.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[FeTa-03Dan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-03Dan.tdb): BCC_A2, type code %B, sha256 `e83eaadd3887295a…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% TA% : VA : !
~~~~

[FeTa-11Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-11Wit.tdb): BCC_A2, type code %B, sha256 `9f4e7036b7ede195…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE% TA% : VA : !
~~~~

[FeTa-15Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-15Raj.tdb): BCC_A2, type code %B, sha256 `04b06f96f96efcaa…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% TA% : VA : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1016/j.intermet.2011.03.018](https://doi.org/10.1016/j.intermet.2011.03.018) V.T. Witusiewicz, A.A. Bondar, U. Hecht, V.M. Voblikov, O.S. Fomichov, V.M. Petyukh et al., Experimental study and thermodynamic re-assessment of the binary Fe–Ta system, Intermetallics 19, 1059-1075 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.12.006](https://doi.org/10.1016/j.calphad.2014.12.006) V.B. Rajkumar, K.C. Hari Kumar, Gibbs energy modeling of Fe–Ta system by Calphad method assisted by experiments and ab initio calculations, Calphad 48, 157-165 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0022-3115(03)00196-X](https://doi.org/10.1016/S0022-3115%2803%2900196-X) A. Danon, C. Servant, J. Nucl. Mater., 321, 8-18(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)90747-1](https://doi.org/10.1016/0925-8388%2894%2990747-1) S. Srikanth, A. Petric, Optimization and calculation of the FeTa phase diagram, Journal of Alloys and Compounds 203, 281-288 (1994).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.197001633](https://doi.org/10.1002/srin.197001633) Wilhelm Anton Fischer, Klaus Lorenz, Heinz Fabritius, Dieter Schlegel, Untersuchung der α/γ‐Umwandlung in hochreinen Zweistofflegierungen des Eisens mit Molybdän, Vanadin, Wolfram, Niob, Tantal, Zirkon und Kobalt, Steel Research Intl 41, 489-498 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/s0921-5093(02)00632-9](https://doi.org/10.1016/s0921-5093%2802%2900632-9) A Danon, C Servant, A Alamo, J.C Brachet, Heterogeneous austenite grain growth in 9Cr martensitic steels: influence of the heating rate and the austenitization temperature, Materials Science and Engineering: A 348, 122-132 (2003).  
_cited as the source of values for this phase_
- [doi:10.2355/isijinternational.29.843](https://doi.org/10.2355/isijinternational.29.843) Eiji Ichise, Ken-ichi Horikawa, Thermodynamic study of Fe-Ta and Fe-Nb alloys by means of the Knudsen cell mass spectrometry., ISIJ International 29, 843-851 (1989).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02664849](https://doi.org/10.1007/bf02664849) G. C. Coelho, J. G. Costa Neto, S. Gama, C. A. Ribeiro, Experimental study of the iron-tantalum equilibrium diagram, JPE 16, 121-128 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(70)90137-2](https://doi.org/10.1016/0022-5088%2870%2990137-2) G.B. Barbi, Determination of thermodynamic stability of the Fe2Ta intermetallic phase by non-stationary e.m.f. measurements on solid galvanic chains, Journal of the Less Common Metals 22, 487-494 (1970).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19352230405](https://doi.org/10.1002/zaac.19352230405) Werner Jellinghaus, Zur Kenntnis des Zweistoffsystems Eisen‐Tantal, Z. Anorg. Allg. Chem. 223, 362-364 (1935).  
_cited as the source of values for this phase_

## C14_LAVES (Fe–Ta)

- Id: `phase:fe-ta:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeTa-03Dan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTa-11Wit.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTa-15Raj.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–2136.48 K, x(Ta) 0.26945–0.42799
- Literature: 31 values (31 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ta:c14-laves)

Names (5): _corpus: _corpus:phase:fe-ta:c14-laves  
_paper: _paper:10.1016/j.intermet.2011.03.018:λ  
_tdb: _tdb:FeTa-03Dan.tdb:C14_LAVES, tdb:FeTa-11Wit.tdb:C14_LAVES, tdb:FeTa-15Raj.tdb:C14_LAVES  


### TDB models of C14_LAVES (3): PHASE and CONSTITUENT statements as written

[FeTa-03Dan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-03Dan.tdb): C14_LAVES, type code %, sha256 `e83eaadd3887295a…`

~~~~text
43: PHASE C14_LAVES % 2 2 1 !
44: CONST C14_LAVES : FE% TA : FE TA% : !
~~~~

[FeTa-11Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-11Wit.tdb): C14_LAVES, type code %, sha256 `9f4e7036b7ede195…`

~~~~text
48: PHASE C14_LAVES % 2 2 1 !
49: CONST C14_LAVES : FE% TA : FE TA% : !
~~~~

[FeTa-15Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-15Raj.tdb): C14_LAVES, type code %, sha256 `04b06f96f96efcaa…`

~~~~text
43: PHASE C14_LAVES % 2 2 1 !
44: CONST C14_LAVES : FE% TA : FE TA% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.intermet.2011.03.018](https://doi.org/10.1016/j.intermet.2011.03.018) V.T. Witusiewicz, A.A. Bondar, U. Hecht, V.M. Voblikov, O.S. Fomichov, V.M. Petyukh et al., Experimental study and thermodynamic re-assessment of the binary Fe–Ta system, Intermetallics 19, 1059-1075 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.12.006](https://doi.org/10.1016/j.calphad.2014.12.006) V.B. Rajkumar, K.C. Hari Kumar, Gibbs energy modeling of Fe–Ta system by Calphad method assisted by experiments and ab initio calculations, Calphad 48, 157-165 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(03)00196-X](https://doi.org/10.1016/S0022-3115%2803%2900196-X) A. Danon, C. Servant, J. Nucl. Mater., 321, 8-18(2003).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90747-1](https://doi.org/10.1016/0925-8388%2894%2990747-1) S. Srikanth, A. Petric, Optimization and calculation of the FeTa phase diagram, Journal of Alloys and Compounds 203, 281-288 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0921-5093(02)00632-9](https://doi.org/10.1016/s0921-5093%2802%2900632-9) A Danon, C Servant, A Alamo, J.C Brachet, Heterogeneous austenite grain growth in 9Cr martensitic steels: influence of the heating rate and the austenitization temperature, Materials Science and Engineering: A 348, 122-132 (2003).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.197001633](https://doi.org/10.1002/srin.197001633) Wilhelm Anton Fischer, Klaus Lorenz, Heinz Fabritius, Dieter Schlegel, Untersuchung der α/γ‐Umwandlung in hochreinen Zweistofflegierungen des Eisens mit Molybdän, Vanadin, Wolfram, Niob, Tantal, Zirkon und Kobalt, Steel Research Intl 41, 489-498 (1970).  
_cited as the source of values for this phase_
- [doi:10.2355/isijinternational.29.843](https://doi.org/10.2355/isijinternational.29.843) Eiji Ichise, Ken-ichi Horikawa, Thermodynamic study of Fe-Ta and Fe-Nb alloys by means of the Knudsen cell mass spectrometry., ISIJ International 29, 843-851 (1989).  
_cited as the source of values for this phase_

## MU_D85 (Fe–Ta)

- Id: `phase:fe-ta:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeTa-03Dan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTa-11Wit.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTa-15Raj.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–2064.99 K, x(Ta) 0.46154–0.61526
- Literature: 49 values (49 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ta:d85-mu)

Names (11): _corpus: _corpus:phase:fe-ta:d85-mu, corpus:phase:fe-ta:mu-d85  
_paper: _paper:10.1016/j.calphad.2014.12.006:Mu phase (μ), paper:10.1016/j.calphad.2014.12.006:μ, paper:10.1016/j.intermet.2011.03.018:μ, paper:10.1016/j.intermet.2011.03.018:μ, TaFe, Ta6Fe7, paper:10.1016/s0022-3115(03)00196-x:μ, paper:10.1016/s0022-3115(03)00196-x:μ ↔ Liq.  
_tdb: _tdb:FeTa-03Dan.tdb:MU_D85, tdb:FeTa-11Wit.tdb:MU_D85, tdb:FeTa-15Raj.tdb:MU_D85  


### TDB models of MU_D85 (3): PHASE and CONSTITUENT statements as written

[FeTa-03Dan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-03Dan.tdb): MU_D85, type code %, sha256 `e83eaadd3887295a…`

~~~~text
48: PHASE MU_D85 % 3 7 2 4 !
49: CONST MU_D85 : FE% TA : TA : FE TA% : !
~~~~

[FeTa-11Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-11Wit.tdb): MU_D85, type code %, sha256 `9f4e7036b7ede195…`

~~~~text
53: PHASE MU_D85 % 3 7 2 4 !
54: CONST MU_D85 : FE% TA : TA : FE TA% : !
~~~~

[FeTa-15Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-15Raj.tdb): MU_D85, type code %, sha256 `04b06f96f96efcaa…`

~~~~text
48: PHASE MU_D85 % 4 1 4 2 6 !
49: CONST MU_D85 : FE% TA : TA : FE TA% : FE% TA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.intermet.2011.03.018](https://doi.org/10.1016/j.intermet.2011.03.018) V.T. Witusiewicz, A.A. Bondar, U. Hecht, V.M. Voblikov, O.S. Fomichov, V.M. Petyukh et al., Experimental study and thermodynamic re-assessment of the binary Fe–Ta system, Intermetallics 19, 1059-1075 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.12.006](https://doi.org/10.1016/j.calphad.2014.12.006) V.B. Rajkumar, K.C. Hari Kumar, Gibbs energy modeling of Fe–Ta system by Calphad method assisted by experiments and ab initio calculations, Calphad 48, 157-165 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0022-3115(03)00196-X](https://doi.org/10.1016/S0022-3115%2803%2900196-X) A. Danon, C. Servant, J. Nucl. Mater., 321, 8-18(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)90747-1](https://doi.org/10.1016/0925-8388%2894%2990747-1) S. Srikanth, A. Petric, Optimization and calculation of the FeTa phase diagram, Journal of Alloys and Compounds 203, 281-288 (1994).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02664849](https://doi.org/10.1007/bf02664849) G. C. Coelho, J. G. Costa Neto, S. Gama, C. A. Ribeiro, Experimental study of the iron-tantalum equilibrium diagram, JPE 16, 121-128 (1995).  
_cited as the source of values for this phase_
- [doi:10.1002/pssb.19680270149](https://doi.org/10.1002/pssb.19680270149) K. Wetzig, Some Investigations Concerning the Position and the Melting Point of TaFe Lamellas in the System TaFe‐TaFe\<sub>2\</sub>, Physica Status Solidi (b) 27 (1968).  
_cited as the source of values for this phase_
- [doi:10.1016/s0921-5093(02)00632-9](https://doi.org/10.1016/s0921-5093%2802%2900632-9) A Danon, C Servant, A Alamo, J.C Brachet, Heterogeneous austenite grain growth in 9Cr martensitic steels: influence of the heating rate and the austenitization temperature, Materials Science and Engineering: A 348, 122-132 (2003).  
_cited as the source of values for this phase_
- [doi:10.2355/isijinternational.29.843](https://doi.org/10.2355/isijinternational.29.843) Eiji Ichise, Ken-ichi Horikawa, Thermodynamic study of Fe-Ta and Fe-Nb alloys by means of the Knudsen cell mass spectrometry., ISIJ International 29, 843-851 (1989).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Ta)

- Id: `phase:fe-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 777.33–1742.46 K, x(Ta) 0–0.01061
- Literature: 38 values (38 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ta:fcc-a1)

Names (7): _corpus: _corpus:phase:fe-ta:fcc-a1  
_paper: _paper:10.1016/j.calphad.2014.12.006:(γFe), paper:10.1016/j.intermet.2011.03.018:γ, paper:10.1016/s0022-3115(03)00196-x:γ  
_tdb: _tdb:FeTa-03Dan.tdb:FCC_A1, tdb:FeTa-11Wit.tdb:FCC_A1, tdb:FeTa-15Raj.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[FeTa-03Dan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-03Dan.tdb): FCC_A1, type code %A, sha256 `e83eaadd3887295a…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% TA : VA : !
~~~~

[FeTa-11Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-11Wit.tdb): FCC_A1, type code %A, sha256 `9f4e7036b7ede195…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE% TA : VA : !
~~~~

[FeTa-15Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-15Raj.tdb): FCC_A1, type code %A, sha256 `04b06f96f96efcaa…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% TA : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.intermet.2011.03.018](https://doi.org/10.1016/j.intermet.2011.03.018) V.T. Witusiewicz, A.A. Bondar, U. Hecht, V.M. Voblikov, O.S. Fomichov, V.M. Petyukh et al., Experimental study and thermodynamic re-assessment of the binary Fe–Ta system, Intermetallics 19, 1059-1075 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0022-3115(03)00196-X](https://doi.org/10.1016/S0022-3115%2803%2900196-X) A. Danon, C. Servant, J. Nucl. Mater., 321, 8-18(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.12.006](https://doi.org/10.1016/j.calphad.2014.12.006) V.B. Rajkumar, K.C. Hari Kumar, Gibbs energy modeling of Fe–Ta system by Calphad method assisted by experiments and ab initio calculations, Calphad 48, 157-165 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.197001633](https://doi.org/10.1002/srin.197001633) Wilhelm Anton Fischer, Klaus Lorenz, Heinz Fabritius, Dieter Schlegel, Untersuchung der α/γ‐Umwandlung in hochreinen Zweistofflegierungen des Eisens mit Molybdän, Vanadin, Wolfram, Niob, Tantal, Zirkon und Kobalt, Steel Research Intl 41, 489-498 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90747-1](https://doi.org/10.1016/0925-8388%2894%2990747-1) S. Srikanth, A. Petric, Optimization and calculation of the FeTa phase diagram, Journal of Alloys and Compounds 203, 281-288 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0921-5093(02)00632-9](https://doi.org/10.1016/s0921-5093%2802%2900632-9) A Danon, C Servant, A Alamo, J.C Brachet, Heterogeneous austenite grain growth in 9Cr martensitic steels: influence of the heating rate and the austenitization temperature, Materials Science and Engineering: A 348, 122-132 (2003).  
_cited as the source of values for this phase_

## FE2TA3 (Fe–Ta)

- Id: `phase:fe-ta:fe2ta3`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Fe2Ta3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Fe2Ta3) — Hallstedt 2025 mmc2 row for FE2TA3: Fe2Ta3 (metastable)
- Stability: not stable in 1 calculated diagram(s)
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ta:fe2ta3)

Names (3): _corpus: _corpus:phase:fe-ta:fe2ta3  
_paper: _paper:10.1016/j.intermet.2011.03.018:Ta3Fe2  
_tdb: _tdb:FeTa-11Wit.tdb:FE2TA3  


### TDB models of FE2TA3 (1): PHASE and CONSTITUENT statements as written

[FeTa-11Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-11Wit.tdb): FE2TA3, type code %, sha256 `9f4e7036b7ede195…`

~~~~text
58: PHASE FE2TA3 % 2 2 3 !
59: CONST FE2TA3 : FE% TA : FE TA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2011.03.018](https://doi.org/10.1016/j.intermet.2011.03.018) V.T. Witusiewicz, A.A. Bondar, U. Hecht, V.M. Voblikov, O.S. Fomichov, V.M. Petyukh et al., Experimental study and thermodynamic re-assessment of the binary Fe–Ta system, Intermetallics 19, 1059-1075 (2011).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Fe–Ta)

- Id: `phase:fe-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ta:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-ta:hcp-a3  
_tdb: _tdb:FeTa-03Dan.tdb:HCP_A3, tdb:FeTa-11Wit.tdb:HCP_A3, tdb:FeTa-15Raj.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[FeTa-03Dan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-03Dan.tdb): HCP_A3, type code %A, sha256 `e83eaadd3887295a…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE TA : VA : !
~~~~

[FeTa-11Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-11Wit.tdb): HCP_A3, type code %A, sha256 `9f4e7036b7ede195…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : FE TA : VA : !
~~~~

[FeTa-15Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-15Raj.tdb): HCP_A3, type code %A, sha256 `04b06f96f96efcaa…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE TA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.12.006](https://doi.org/10.1016/j.calphad.2014.12.006) V.B. Rajkumar, K.C. Hari Kumar, Gibbs energy modeling of Fe–Ta system by Calphad method assisted by experiments and ab initio calculations, Calphad 48, 157-165 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2011.03.018](https://doi.org/10.1016/j.intermet.2011.03.018) V.T. Witusiewicz, A.A. Bondar, U. Hecht, V.M. Voblikov, O.S. Fomichov, V.M. Petyukh et al., Experimental study and thermodynamic re-assessment of the binary Fe–Ta system, Intermetallics 19, 1059-1075 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(03)00196-X](https://doi.org/10.1016/S0022-3115%2803%2900196-X) A. Danon, C. Servant, J. Nucl. Mater., 321, 8-18(2003).  
_assessment that models this phase_

## LIQUID (Fe–Ta)

- Id: `phase:fe-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1716.11–4000 K, x(Ta) 0–1
- Literature: 58 values (58 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ta:liquid)

Names (8): _corpus: _corpus:phase:fe-ta:liquid  
_paper: _paper:10.1016/j.calphad.2014.12.006:L, paper:10.1016/j.intermet.2011.03.018:L, paper:10.1016/s0022-3115(03)00196-x:L, paper:10.1016/s0022-3115(03)00196-x:Liq.  
_tdb: _tdb:FeTa-03Dan.tdb:LIQUID, tdb:FeTa-11Wit.tdb:LIQUID, tdb:FeTa-15Raj.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[FeTa-03Dan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-03Dan.tdb): LIQUID, type code %, sha256 `e83eaadd3887295a…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE TA : !
~~~~

[FeTa-11Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-11Wit.tdb): LIQUID, type code %, sha256 `9f4e7036b7ede195…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE TA : !
~~~~

[FeTa-15Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTa-15Raj.tdb): LIQUID, type code %, sha256 `04b06f96f96efcaa…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE TA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.intermet.2011.03.018](https://doi.org/10.1016/j.intermet.2011.03.018) V.T. Witusiewicz, A.A. Bondar, U. Hecht, V.M. Voblikov, O.S. Fomichov, V.M. Petyukh et al., Experimental study and thermodynamic re-assessment of the binary Fe–Ta system, Intermetallics 19, 1059-1075 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0022-3115(03)00196-X](https://doi.org/10.1016/S0022-3115%2803%2900196-X) A. Danon, C. Servant, J. Nucl. Mater., 321, 8-18(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.12.006](https://doi.org/10.1016/j.calphad.2014.12.006) V.B. Rajkumar, K.C. Hari Kumar, Gibbs energy modeling of Fe–Ta system by Calphad method assisted by experiments and ab initio calculations, Calphad 48, 157-165 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)90747-1](https://doi.org/10.1016/0925-8388%2894%2990747-1) S. Srikanth, A. Petric, Optimization and calculation of the FeTa phase diagram, Journal of Alloys and Compounds 203, 281-288 (1994).  
_cited as the source of values for this phase_
- [doi:10.2355/isijinternational.29.843](https://doi.org/10.2355/isijinternational.29.843) Eiji Ichise, Ken-ichi Horikawa, Thermodynamic study of Fe-Ta and Fe-Nb alloys by means of the Knudsen cell mass spectrometry., ISIJ International 29, 843-851 (1989).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02664849](https://doi.org/10.1007/bf02664849) G. C. Coelho, J. G. Costa Neto, S. Gama, C. A. Ribeiro, Experimental study of the iron-tantalum equilibrium diagram, JPE 16, 121-128 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/s0921-5093(02)00632-9](https://doi.org/10.1016/s0921-5093%2802%2900632-9) A Danon, C Servant, A Alamo, J.C Brachet, Heterogeneous austenite grain growth in 9Cr martensitic steels: influence of the heating rate and the austenitization temperature, Materials Science and Engineering: A 348, 122-132 (2003).  
_cited as the source of values for this phase_
- [doi:10.1002/pssb.19680270149](https://doi.org/10.1002/pssb.19680270149) K. Wetzig, Some Investigations Concerning the Position and the Melting Point of TaFe Lamellas in the System TaFe‐TaFe\<sub>2\</sub>, Physica Status Solidi (b) 27 (1968).  
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
