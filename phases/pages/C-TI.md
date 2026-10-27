# C–Ti phases

> C–Ti system: 6 phases (tier A 4, liquid 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-TI.html · Markdown: https://data.orchid-project.org/phases/pages/C-TI.md

6 phases (tier A 4, liquid 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-TI) · [full JSON](https://data.orchid-project.org/phases/systems/C-TI.json) · [C–Ti system page](https://data.orchid-project.org/systems/C-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Ti system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-ti-a4-diamond); _phase:c-ti:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [GRAPHITE_A9](#phase-c-ti-a9-graphite); _phase:c-ti:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 5 |
| [BCC_A2](#phase-c-ti-bcc-a2); _phase:c-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 1129.99–1955.98 K, x(C) 0–0.03018 | 9 | 5 |
| [FCC_A1](#phase-c-ti-fcc-a1); _phase:c-ti:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 5 of 5 calculated diagram(s): 300–3368.23 K, x(C) 0.31029–0.5 | 31 | 5 |
| [HCP_A3](#phase-c-ti-hcp-a3); _phase:c-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1220 K, x(C) 0–0.02091 | 4 | 5 |
| [LIQUID](#phase-c-ti-liquid); _phase:c-ti:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1910–4000 K, x(C) 0–0.80493 | 11 | 5 |

## DIAMOND_A4 (C–Ti)

- Id: `phase:c-ti:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ti:a4-diamond)

Names (6): _corpus: _corpus:phase:c-ti:a4-diamond  
_tdb: _tdb:TiC-03Fri.tdb:DIAMOND_A4, tdb:TiC-95Dus.tdb:DIAMOND_A4, tdb:TiC-96Jon.tdb:DIAMOND_A4, tdb:TiC-96Sei.tdb:DIAMOND_A4, tdb:TiC-99Dum-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[TiC-03Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-03Fri.tdb): DIAMOND_A4, type code %, sha256 `9f4e6802632c842e…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : C : !
~~~~

[TiC-95Dus.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-95Dus.tdb): DIAMOND_A4, type code %, sha256 `d36ce7591c7cc1de…`

~~~~text
50: PHASE DIAMOND_A4 % 1 1 !
51: CONST DIAMOND_A4 : C : !
~~~~

[TiC-96Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Jon.tdb): DIAMOND_A4, type code %, sha256 `45f9b1014632354b…`

~~~~text
50: PHASE DIAMOND_A4 % 1 1 !
51: CONST DIAMOND_A4 : C : !
~~~~

[TiC-96Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Sei.tdb): DIAMOND_A4, type code %, sha256 `5ad19b550fd4faa8…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : C : !
~~~~

[TiC-99Dum-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-99Dum-LB.tdb): DIAMOND_A4, type code %, sha256 `b270107d3fa5a3dd…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646248](https://doi.org/10.1007/BF02646248) H. Duschanek, P. Rogl, H.L. Lukas, J. Phase Equilib., 16, 46-60(1995).  
_assessment that models this phase_
- [doi:10.1007/BF02648366](https://doi.org/10.1007/BF02648366) H.J. Seifert, H.L. Lukas, G. Petzow, J. Phase Equilib., 17, 24-35(1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.01.004](https://doi.org/10.1016/j.calphad.2004.01.004) Karin Frisk, A revised thermodynamic description of the Ti–C system, Calphad 27, 367-373 (2003).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870904](https://doi.org/10.1515/ijmr-1996-870904) S. Jonsson, Z. Metallkd., 87, 703-12(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900712](https://doi.org/10.1515/ijmr-1999-900712) L.F.S. Dumitrescu, M. Hillert, B. Sundman, Z. Metallkd., 90, 534-41(1999).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Ti)

- Id: `phase:c-ti:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ti:a9-graphite)

Names (7): _corpus: _corpus:phase:c-ti:a9-graphite, corpus:phase:c-ti:graphite-a9  
_tdb: _tdb:TiC-03Fri.tdb:GRAPHITE_A9, tdb:TiC-95Dus.tdb:GRAPHITE_A9, tdb:TiC-96Jon.tdb:GRAPHITE_A9, tdb:TiC-96Sei.tdb:GRAPHITE_A9, tdb:TiC-99Dum-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (5): PHASE and CONSTITUENT statements as written

[TiC-03Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-03Fri.tdb): GRAPHITE_A9, type code %, sha256 `9f4e6802632c842e…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : C : !
~~~~

[TiC-95Dus.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-95Dus.tdb): GRAPHITE_A9, type code %, sha256 `d36ce7591c7cc1de…`

~~~~text
55: PHASE GRAPHITE_A9 % 1 1 !
56: CONST GRAPHITE_A9 : C : !
~~~~

[TiC-96Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Jon.tdb): GRAPHITE_A9, type code %, sha256 `45f9b1014632354b…`

~~~~text
55: PHASE GRAPHITE_A9 % 1 1 !
56: CONST GRAPHITE_A9 : C : !
~~~~

[TiC-96Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Sei.tdb): GRAPHITE_A9, type code %, sha256 `5ad19b550fd4faa8…`

~~~~text
47: PHASE GRAPHITE_A9 % 1 1 !
48: CONST GRAPHITE_A9 : C : !
~~~~

[TiC-99Dum-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-99Dum-LB.tdb): GRAPHITE_A9, type code %, sha256 `b270107d3fa5a3dd…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02646248](https://doi.org/10.1007/BF02646248) H. Duschanek, P. Rogl, H.L. Lukas, J. Phase Equilib., 16, 46-60(1995).  
_assessment that models this phase_
- [doi:10.1007/BF02648366](https://doi.org/10.1007/BF02648366) H.J. Seifert, H.L. Lukas, G. Petzow, J. Phase Equilib., 17, 24-35(1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.01.004](https://doi.org/10.1016/j.calphad.2004.01.004) Karin Frisk, A revised thermodynamic description of the Ti–C system, Calphad 27, 367-373 (2003).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870904](https://doi.org/10.1515/ijmr-1996-870904) S. Jonsson, Z. Metallkd., 87, 703-12(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900712](https://doi.org/10.1515/ijmr-1999-900712) L.F.S. Dumitrescu, M. Hillert, B. Sundman, Z. Metallkd., 90, 534-41(1999).  
_assessment that models this phase_

## BCC_A2 (C–Ti)

- Id: `phase:c-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1129.99–1955.98 K, x(C) 0–0.03018
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ti:bcc-a2)

Names (9): _corpus: _corpus:phase:c-ti:bcc-a2  
_paper: _paper:10.1007/bf02646248:βTi, paper:10.1007/bf02648366:βTi, paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:TiC-03Fri.tdb:BCC_A2, tdb:TiC-95Dus.tdb:BCC_A2, tdb:TiC-96Jon.tdb:BCC_A2, tdb:TiC-96Sei.tdb:BCC_A2, tdb:TiC-99Dum-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[TiC-03Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-03Fri.tdb): BCC_A2, type code %B, sha256 `9f4e6802632c842e…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : TI% : C VA% : !
~~~~

[TiC-95Dus.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-95Dus.tdb): BCC_A2, type code %B, sha256 `d36ce7591c7cc1de…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : TI% : C VA% : !
~~~~

[TiC-96Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Jon.tdb): BCC_A2, type code %B, sha256 `45f9b1014632354b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : TI% : C VA% : !
~~~~

[TiC-96Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Sei.tdb): BCC_A2, type code %B, sha256 `5ad19b550fd4faa8…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : TI% : C VA% : !
~~~~

[TiC-99Dum-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-99Dum-LB.tdb): BCC_A2, type code %B, sha256 `b270107d3fa5a3dd…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : TI% : C VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02648366](https://doi.org/10.1007/BF02648366) H.J. Seifert, H.L. Lukas, G. Petzow, J. Phase Equilib., 17, 24-35(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02646248](https://doi.org/10.1007/BF02646248) H. Duschanek, P. Rogl, H.L. Lukas, J. Phase Equilib., 16, 46-60(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.01.004](https://doi.org/10.1016/j.calphad.2004.01.004) Karin Frisk, A revised thermodynamic description of the Ti–C system, Calphad 27, 367-373 (2003).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870904](https://doi.org/10.1515/ijmr-1996-870904) S. Jonsson, Z. Metallkd., 87, 703-12(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900712](https://doi.org/10.1515/ijmr-1999-900712) L.F.S. Dumitrescu, M. Hillert, B. Sundman, Z. Metallkd., 90, 534-41(1999).  
_assessment that models this phase_
- [doi:10.21236/ada470307](https://doi.org/10.21236/ada470307) Erwin Rudy, Austin Y. Chang, Stefan Windisch, Ternary Phase Equilibria in Transition Metal-Boron-Carbon-Silicon Systems. Part 1. Related Binary Systems. Volume 1. Mo-C System, (1965).  
_cited as the source of values for this phase_

## FCC_A1 (C–Ti)

- Id: `phase:c-ti:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–3368.23 K, x(C) 0.31029–0.5
- Literature: 31 values (31 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ti:fcc-a1)

Names (11): _corpus: _corpus:phase:c-ti:fcc-a1  
_paper: _paper:10.1007/bf02648366:TiC, paper:10.1016/j.calphad.2004.01.004:TiC, paper:10.2355/isijinternational.isijint-2019-274:TiC, paper:sha256-85fd53a1a176b694:fcc-A1, paper:sha256-85fd53a1a176b694:fcc-A1\*  
_tdb: _tdb:TiC-03Fri.tdb:FCC_A1, tdb:TiC-95Dus.tdb:FCC_A1, tdb:TiC-96Jon.tdb:FCC_A1, tdb:TiC-96Sei.tdb:FCC_A1, tdb:TiC-99Dum-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[TiC-03Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-03Fri.tdb): FCC_A1, type code %A, sha256 `9f4e6802632c842e…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : TI : C VA% : !
~~~~

[TiC-95Dus.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-95Dus.tdb): FCC_A1, type code %A, sha256 `d36ce7591c7cc1de…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : TI : C VA% : !
~~~~

[TiC-96Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Jon.tdb): FCC_A1, type code %A, sha256 `45f9b1014632354b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : TI : C VA% : !
~~~~

[TiC-96Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Sei.tdb): FCC_A1, type code %A, sha256 `5ad19b550fd4faa8…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : TI : C VA% : !
~~~~

[TiC-99Dum-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-99Dum-LB.tdb): FCC_A1, type code %A, sha256 `b270107d3fa5a3dd…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : TI : C VA% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/BF02648366](https://doi.org/10.1007/BF02648366) H.J. Seifert, H.L. Lukas, G. Petzow, J. Phase Equilib., 17, 24-35(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.01.004](https://doi.org/10.1016/j.calphad.2004.01.004) Karin Frisk, A revised thermodynamic description of the Ti–C system, Calphad 27, 367-373 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02646248](https://doi.org/10.1007/BF02646248) H. Duschanek, P. Rogl, H.L. Lukas, J. Phase Equilib., 16, 46-60(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870904](https://doi.org/10.1515/ijmr-1996-870904) S. Jonsson, Z. Metallkd., 87, 703-12(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900712](https://doi.org/10.1515/ijmr-1999-900712) L.F.S. Dumitrescu, M. Hillert, B. Sundman, Z. Metallkd., 90, 534-41(1999).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.isijint-2019-274](https://doi.org/10.2355/isijinternational.isijint-2019-274) Michitoshi Saeki, Takako Yamashita, Hiroshi Ohtani, Thermodynamic Study on Solubility Products of Ti&lt;sub&gt;4&lt;/sub&gt;C&lt;sub&gt;2&lt;/sub&gt;S&lt;sub&gt;2&lt;/sub&gt; in Fe Using First-Principles Calculations, ISIJ Int. 60, 745-755 (2020).  
_reports values for this phase_
- [doi:10.21236/ada470307](https://doi.org/10.21236/ada470307) Erwin Rudy, Austin Y. Chang, Stefan Windisch, Ternary Phase Equilibria in Transition Metal-Boron-Carbon-Silicon Systems. Part 1. Related Binary Systems. Volume 1. Mo-C System, (1965).  
_cited as the source of values for this phase_

## HCP_A3 (C–Ti)

- Id: `phase:c-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1220 K, x(C) 0–0.02091
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ti:hcp-a3)

Names (8): _corpus: _corpus:phase:c-ti:hcp-a3  
_paper: _paper:10.1007/bf02648366:αTi, paper:sha256-85fd53a1a176b694:hcp-A3  
_tdb: _tdb:TiC-03Fri.tdb:HCP_A3, tdb:TiC-95Dus.tdb:HCP_A3, tdb:TiC-96Jon.tdb:HCP_A3, tdb:TiC-96Sei.tdb:HCP_A3, tdb:TiC-99Dum-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[TiC-03Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-03Fri.tdb): HCP_A3, type code %A, sha256 `9f4e6802632c842e…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : TI% : C VA% : !
~~~~

[TiC-95Dus.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-95Dus.tdb): HCP_A3, type code %A, sha256 `d36ce7591c7cc1de…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : TI% : C VA% : !
~~~~

[TiC-96Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Jon.tdb): HCP_A3, type code %A, sha256 `45f9b1014632354b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : TI% : C VA% : !
~~~~

[TiC-96Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Sei.tdb): HCP_A3, type code %A, sha256 `5ad19b550fd4faa8…`

~~~~text
37: PHASE HCP_A3 %A 2 1 1 !
38: CONST HCP_A3 : TI% : C VA% : !
~~~~

[TiC-99Dum-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-99Dum-LB.tdb): HCP_A3, type code %A, sha256 `b270107d3fa5a3dd…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : TI% : C VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02648366](https://doi.org/10.1007/BF02648366) H.J. Seifert, H.L. Lukas, G. Petzow, J. Phase Equilib., 17, 24-35(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02646248](https://doi.org/10.1007/BF02646248) H. Duschanek, P. Rogl, H.L. Lukas, J. Phase Equilib., 16, 46-60(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.01.004](https://doi.org/10.1016/j.calphad.2004.01.004) Karin Frisk, A revised thermodynamic description of the Ti–C system, Calphad 27, 367-373 (2003).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870904](https://doi.org/10.1515/ijmr-1996-870904) S. Jonsson, Z. Metallkd., 87, 703-12(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900712](https://doi.org/10.1515/ijmr-1999-900712) L.F.S. Dumitrescu, M. Hillert, B. Sundman, Z. Metallkd., 90, 534-41(1999).  
_assessment that models this phase_

## LIQUID (C–Ti)

- Id: `phase:c-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1910–4000 K, x(C) 0–0.80493
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ti:liquid)

Names (9): _corpus: _corpus:phase:c-ti:liquid  
_paper: _paper:10.1007/bf02648366:L, paper:10.1007/bf02648366:liquid, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:TiC-03Fri.tdb:LIQUID, tdb:TiC-95Dus.tdb:LIQUID, tdb:TiC-96Jon.tdb:LIQUID, tdb:TiC-96Sei.tdb:LIQUID, tdb:TiC-99Dum-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[TiC-03Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-03Fri.tdb): LIQUID, type code %, sha256 `9f4e6802632c842e…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : C TI : !
~~~~

[TiC-95Dus.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-95Dus.tdb): LIQUID, type code %, sha256 `d36ce7591c7cc1de…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : C TI : !
~~~~

[TiC-96Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Jon.tdb): LIQUID, type code %, sha256 `45f9b1014632354b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : C TI : !
~~~~

[TiC-96Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-96Sei.tdb): LIQUID, type code %, sha256 `5ad19b550fd4faa8…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : C TI : !
~~~~

[TiC-99Dum-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiC-99Dum-LB.tdb): LIQUID, type code %, sha256 `b270107d3fa5a3dd…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : C TI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02648366](https://doi.org/10.1007/BF02648366) H.J. Seifert, H.L. Lukas, G. Petzow, J. Phase Equilib., 17, 24-35(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02646248](https://doi.org/10.1007/BF02646248) H. Duschanek, P. Rogl, H.L. Lukas, J. Phase Equilib., 16, 46-60(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.01.004](https://doi.org/10.1016/j.calphad.2004.01.004) Karin Frisk, A revised thermodynamic description of the Ti–C system, Calphad 27, 367-373 (2003).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870904](https://doi.org/10.1515/ijmr-1996-870904) S. Jonsson, Z. Metallkd., 87, 703-12(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900712](https://doi.org/10.1515/ijmr-1999-900712) L.F.S. Dumitrescu, M. Hillert, B. Sundman, Z. Metallkd., 90, 534-41(1999).  
_assessment that models this phase_
- [doi:10.21236/ada470307](https://doi.org/10.21236/ada470307) Erwin Rudy, Austin Y. Chang, Stefan Windisch, Ternary Phase Equilibria in Transition Metal-Boron-Carbon-Silicon Systems. Part 1. Related Binary Systems. Volume 1. Mo-C System, (1965).  
_cited as the source of values for this phase_

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
