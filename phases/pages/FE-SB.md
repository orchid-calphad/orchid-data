# Fe–Sb phases

> Fe–Sb system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-SB.html · Markdown: https://data.orchid-project.org/phases/pages/FE-SB.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-SB) · [full JSON](https://data.orchid-project.org/phases/systems/FE-SB.json) · [Fe–Sb system page](https://data.orchid-project.org/systems/FE-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Sb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-fe-sb-a7-rhombohedral); _phase:fe-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 14 | 3 |
| [BCC_A2](#phase-fe-sb-bcc-a2); _phase:fe-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1820.95 K, x(Sb) 0–0.05903 | 19 | 3 |
| [FCC_A1](#phase-fe-sb-fcc-a1); _phase:fe-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1147.46–1670.46 K, x(Sb) 0–0.01169 | 5 | 3 |
| [FESB_B81](#phase-fe-sb-fesb-b81); _phase:fe-sb:fesb-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1307.8 K, x(Sb) 0.4032–0.49486 | 17 | 3 |
| [FESB2_C18](#phase-fe-sb-fesb2-c18); _phase:fe-sb:fesb2-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1021.34 K, x(Sb) 0.66667–0.66667 | 29 | 3 |
| [HCP_A3](#phase-fe-sb-hcp-a3); _phase:fe-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-fe-sb-liquid); _phase:fe-sb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 897.68–2500 K, x(Sb) 0–1 | 62 | 3 |

## RHOMBOHEDRAL_A7 (Fe–Sb)

- Id: `phase:fe-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sb:a7-rhombohedral)

Names (8): _corpus: _corpus:phase:fe-sb:a7-rhombohedral, corpus:phase:fe-sb:rhombohedral-a7  
_paper: _paper:10.1016/0364-5916(95)00001-u:α-Sb, paper:10.1016/j.calphad.2008.01.001:Sb, paper:10.1016/j.calphad.2014.05.005:Sb  
_tdb: _tdb:FeSb-08Boa.tdb:RHOMBOHEDRAL_A7, tdb:FeSb-14Li.tdb:RHOMBOHEDRAL_A7, tdb:FeSb-95Pei-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[FeSb-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-08Boa.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `67f3cb0310dccf1b…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[FeSb-14Li.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-14Li.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8512f95ce9460d49…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[FeSb-95Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-95Pei-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `75ce69413b04b2fe…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2014.05.005](https://doi.org/10.1016/j.calphad.2014.05.005) Changrong Li, Daiman Zhu, Yubi Zhang, Zhenmin Du, Cuiping Guo, Junqin Li et al., Thermodynamic assessment of the Co–Fe–Sb system, Calphad 47, 23-34 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00001-U](https://doi.org/10.1016/0364-5916%2895%2900001-U) B. Pei, B. Bjorkman, B. Sundman, B. Jansson, Calphad, 19, 1-15(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02597-2](https://doi.org/10.1016/s0925-8388%2896%2902597-2) Klaus W. Richter, Herbert Ipser, Reinvestigation of the binary Fe-Sb phase diagram, Journal of Alloys and Compounds 247, 247-249 (1997).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080580102](https://doi.org/10.1002/zaac.19080580102) N. S. Kurnakow, N. S. Konstantinow, Antimonide des Eisens und des Cadmiums, Z. Anorg. Chem. 58, 1-22 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_

## BCC_A2 (Fe–Sb)

- Id: `phase:fe-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1820.95 K, x(Sb) 0–0.05903
- Literature: 19 values (19 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sb:bcc-a2)

Names (7): _corpus: _corpus:phase:fe-sb:bcc-a2  
_paper: _paper:10.1016/0364-5916(95)00001-u:α-Fe, paper:10.1016/j.calphad.2008.01.001:αFe, paper:10.1016/j.calphad.2014.05.005:α(Fe)  
_tdb: _tdb:FeSb-08Boa.tdb:BCC_A2, tdb:FeSb-14Li.tdb:BCC_A2, tdb:FeSb-95Pei-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[FeSb-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-08Boa.tdb): BCC_A2, type code %B, sha256 `67f3cb0310dccf1b…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% SB : VA : !
~~~~

[FeSb-14Li.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-14Li.tdb): BCC_A2, type code %B, sha256 `8512f95ce9460d49…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% SB : VA : !
~~~~

[FeSb-95Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-95Pei-LB.tdb): BCC_A2, type code %B, sha256 `75ce69413b04b2fe…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% SB : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2014.05.005](https://doi.org/10.1016/j.calphad.2014.05.005) Changrong Li, Daiman Zhu, Yubi Zhang, Zhenmin Du, Cuiping Guo, Junqin Li et al., Thermodynamic assessment of the Co–Fe–Sb system, Calphad 47, 23-34 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00001-U](https://doi.org/10.1016/0364-5916%2895%2900001-U) B. Pei, B. Bjorkman, B. Sundman, B. Jansson, Calphad, 19, 1-15(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080580102](https://doi.org/10.1002/zaac.19080580102) N. S. Kurnakow, N. S. Konstantinow, Antimonide des Eisens und des Cadmiums, Z. Anorg. Chem. 58, 1-22 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02597-2](https://doi.org/10.1016/s0925-8388%2896%2902597-2) Klaus W. Richter, Herbert Ipser, Reinvestigation of the binary Fe-Sb phase diagram, Journal of Alloys and Compounds 247, 247-249 (1997).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Sb)

- Id: `phase:fe-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1147.46–1670.46 K, x(Sb) 0–0.01169
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sb:fcc-a1)

Names (5): _corpus: _corpus:phase:fe-sb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2014.05.005:γ(Fe)  
_tdb: _tdb:FeSb-08Boa.tdb:FCC_A1, tdb:FeSb-14Li.tdb:FCC_A1, tdb:FeSb-95Pei-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[FeSb-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-08Boa.tdb): FCC_A1, type code %A, sha256 `67f3cb0310dccf1b…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% SB : VA : !
~~~~

[FeSb-14Li.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-14Li.tdb): FCC_A1, type code %A, sha256 `8512f95ce9460d49…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% SB : VA : !
~~~~

[FeSb-95Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-95Pei-LB.tdb): FCC_A1, type code %A, sha256 `75ce69413b04b2fe…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.05.005](https://doi.org/10.1016/j.calphad.2014.05.005) Changrong Li, Daiman Zhu, Yubi Zhang, Zhenmin Du, Cuiping Guo, Junqin Li et al., Thermodynamic assessment of the Co–Fe–Sb system, Calphad 47, 23-34 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00001-U](https://doi.org/10.1016/0364-5916%2895%2900001-U) B. Pei, B. Bjorkman, B. Sundman, B. Jansson, Calphad, 19, 1-15(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase_

## FESB_B81 (Fe–Sb)

- Id: `phase:fe-sb:fesb-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1307.8 K, x(Sb) 0.4032–0.49486
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sb:fesb-b81)

Names (6): _corpus: _corpus:phase:fe-sb:fesb-b81  
_paper: _paper:10.1016/0364-5916(95)00001-u:ε-FeSb, paper:10.1016/j.calphad.2008.01.001:ε-FeSb  
_tdb: _tdb:FeSb-08Boa.tdb:FESB_B81, tdb:FeSb-14Li.tdb:FESB_B81, tdb:FeSb-95Pei-LB.tdb:FESB_B81  


### TDB models of FESB_B81 (3): PHASE and CONSTITUENT statements as written

[FeSb-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-08Boa.tdb): FESB_B81, type code %, sha256 `67f3cb0310dccf1b…`

~~~~text
49: PHASE FESB_B81 % 2 1 1  !
50: CONST FESB_B81 : FE : FE SB : !
~~~~

[FeSb-14Li.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-14Li.tdb): FESB_B81, type code %, sha256 `8512f95ce9460d49…`

~~~~text
49: PHASE FESB_B81 % 3 1 1 1  !
50: CONST FESB_B81 : FE% VA : FE VA% : SB : !
~~~~

[FeSb-95Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-95Pei-LB.tdb): FESB_B81, type code %, sha256 `75ce69413b04b2fe…`

~~~~text
50: PHASE FESB_B81 % 2 1 1  !
51: CONST FESB_B81 : FE : FE SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(95)00001-U](https://doi.org/10.1016/0364-5916%2895%2900001-U) B. Pei, B. Bjorkman, B. Sundman, B. Jansson, Calphad, 19, 1-15(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.05.005](https://doi.org/10.1016/j.calphad.2014.05.005) Changrong Li, Daiman Zhu, Yubi Zhang, Zhenmin Du, Cuiping Guo, Junqin Li et al., Thermodynamic assessment of the Co–Fe–Sb system, Calphad 47, 23-34 (2014).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(96)02597-2](https://doi.org/10.1016/s0925-8388%2896%2902597-2) Klaus W. Richter, Herbert Ipser, Reinvestigation of the binary Fe-Sb phase diagram, Journal of Alloys and Compounds 247, 247-249 (1997).  
_cited as the source of values for this phase_

## FESB2_C18 (Fe–Sb)

- Id: `phase:fe-sb:fesb2-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.3333, Sb 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1021.34 K, x(Sb) 0.66667–0.66667
- Literature: 29 values (29 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sb:fesb2-c18)

Names (7): _corpus: _corpus:phase:fe-sb:fesb2-c18  
_paper: _paper:10.1016/0364-5916(95)00001-u:FeSb2, paper:10.1016/j.calphad.2008.01.001:FeSb2, paper:10.1016/j.calphad.2014.05.005:ζ2FeSb2  
_tdb: _tdb:FeSb-08Boa.tdb:FESB2_C18, tdb:FeSb-14Li.tdb:FESB2_C18, tdb:FeSb-95Pei-LB.tdb:FESB2_C18  


### TDB models of FESB2_C18 (3): PHASE and CONSTITUENT statements as written

[FeSb-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-08Boa.tdb): FESB2_C18, type code %, sha256 `67f3cb0310dccf1b…`

~~~~text
54: PHASE FESB2_C18 % 2 1 2  !
55: CONST FESB2_C18 : FE : SB : !
~~~~

[FeSb-14Li.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-14Li.tdb): FESB2_C18, type code %, sha256 `8512f95ce9460d49…`

~~~~text
54: PHASE FESB2_C18 % 2 1 2  !
55: CONST FESB2_C18 : FE : SB : !
~~~~

[FeSb-95Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-95Pei-LB.tdb): FESB2_C18, type code %, sha256 `75ce69413b04b2fe…`

~~~~text
55: PHASE FESB2_C18 % 2 1 2  !
56: CONST FESB2_C18 : FE : SB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2014.05.005](https://doi.org/10.1016/j.calphad.2014.05.005) Changrong Li, Daiman Zhu, Yubi Zhang, Zhenmin Du, Cuiping Guo, Junqin Li et al., Thermodynamic assessment of the Co–Fe–Sb system, Calphad 47, 23-34 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00001-U](https://doi.org/10.1016/0364-5916%2895%2900001-U) B. Pei, B. Bjorkman, B. Sundman, B. Jansson, Calphad, 19, 1-15(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02597-2](https://doi.org/10.1016/s0925-8388%2896%2902597-2) Klaus W. Richter, Herbert Ipser, Reinvestigation of the binary Fe-Sb phase diagram, Journal of Alloys and Compounds 247, 247-249 (1997).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080580102](https://doi.org/10.1002/zaac.19080580102) N. S. Kurnakow, N. S. Konstantinow, Antimonide des Eisens und des Cadmiums, Z. Anorg. Chem. 58, 1-22 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Sb)

- Id: `phase:fe-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sb:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-sb:hcp-a3  
_tdb: _tdb:FeSb-08Boa.tdb:HCP_A3, tdb:FeSb-14Li.tdb:HCP_A3, tdb:FeSb-95Pei-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[FeSb-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-08Boa.tdb): HCP_A3, type code %A, sha256 `67f3cb0310dccf1b…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE SB : VA : !
~~~~

[FeSb-14Li.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-14Li.tdb): HCP_A3, type code %A, sha256 `8512f95ce9460d49…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE SB : VA : !
~~~~

[FeSb-95Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-95Pei-LB.tdb): HCP_A3, type code %A, sha256 `75ce69413b04b2fe…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(95)00001-U](https://doi.org/10.1016/0364-5916%2895%2900001-U) B. Pei, B. Bjorkman, B. Sundman, B. Jansson, Calphad, 19, 1-15(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.05.005](https://doi.org/10.1016/j.calphad.2014.05.005) Changrong Li, Daiman Zhu, Yubi Zhang, Zhenmin Du, Cuiping Guo, Junqin Li et al., Thermodynamic assessment of the Co–Fe–Sb system, Calphad 47, 23-34 (2014).  
_assessment that models this phase_

## LIQUID (Fe–Sb)

- Id: `phase:fe-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 897.68–2500 K, x(Sb) 0–1
- Literature: 62 values (62 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sb:liquid)

Names (8): _corpus: _corpus:phase:fe-sb:liquid  
_paper: _paper:10.1016/0364-5916(95)00001-u:L, paper:10.1016/j.calphad.2008.01.001:Liq, paper:10.1016/j.calphad.2008.01.001:liquid, paper:10.1016/j.calphad.2014.05.005:L  
_tdb: _tdb:FeSb-08Boa.tdb:LIQUID, tdb:FeSb-14Li.tdb:LIQUID, tdb:FeSb-95Pei-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[FeSb-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-08Boa.tdb): LIQUID, type code %, sha256 `67f3cb0310dccf1b…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE SB : !
~~~~

[FeSb-14Li.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-14Li.tdb): LIQUID, type code %, sha256 `8512f95ce9460d49…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE SB : !
~~~~

[FeSb-95Pei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSb-95Pei-LB.tdb): LIQUID, type code %, sha256 `75ce69413b04b2fe…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE SB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2014.05.005](https://doi.org/10.1016/j.calphad.2014.05.005) Changrong Li, Daiman Zhu, Yubi Zhang, Zhenmin Du, Cuiping Guo, Junqin Li et al., Thermodynamic assessment of the Co–Fe–Sb system, Calphad 47, 23-34 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00001-U](https://doi.org/10.1016/0364-5916%2895%2900001-U) B. Pei, B. Bjorkman, B. Sundman, B. Jansson, Calphad, 19, 1-15(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02597-2](https://doi.org/10.1016/s0925-8388%2896%2902597-2) Klaus W. Richter, Herbert Ipser, Reinvestigation of the binary Fe-Sb phase diagram, Journal of Alloys and Compounds 247, 247-249 (1997).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080580102](https://doi.org/10.1002/zaac.19080580102) N. S. Kurnakow, N. S. Konstantinow, Antimonide des Eisens und des Cadmiums, Z. Anorg. Chem. 58, 1-22 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
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
