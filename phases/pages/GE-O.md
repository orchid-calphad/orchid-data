# Ge–O phases

> Ge–O system: 10 phases (tier A 5, liquid 2, gas 2, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-O.html · Markdown: https://data.orchid-project.org/phases/pages/GE-O.md

10 phases (tier A 5, liquid 2, gas 2, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-O) · [full JSON](https://data.orchid-project.org/phases/systems/GE-O.json) · [Ge–O system page](https://data.orchid-project.org/systems/GE-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–O system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-o-a4-diamond); _phase:ge-o:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(O) 0–0 | 0 | 2 |
| [BCC_A2](#phase-ge-o-bcc-a2); _phase:ge-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ge-o-fcc-a1); _phase:ge-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-ge-o-gas); _phase:ge-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 1–1 | 0 | 2 |
| [GEO2_HT](#phase-ge-o-geo2); _phase:ge-o:geo2_ |  | needs_review | stable in 1 of 2 calculated diagram(s): 1324.19–1389.19 K, x(O) 0.66667–0.66667 | 0 | 2 |
| [GEO2_C4](#phase-ge-o-geo2-c4); _phase:ge-o:geo2-c4_ | TiO2 · C4 · tP6 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–475 K, x(O) 0.66667–0.66667 | 0 | 2 |
| [HCP_A3](#phase-ge-o-hcp-a3); _phase:ge-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-ge-o-ion); _phase:ge-o:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1192.81–2500 K, x(O) 0–0.66667 | 0 | 2 |
| [LIQUID](#phase-ge-o-liquid); _phase:ge-o:liquid_ | liquid | liquid | not stable in 2 calculated diagram(s) | 0 | 2 |
| [O2GAS](#phase-ge-o-o2gas); _phase:ge-o:o2gas_ | gas | gas | not stable in 2 calculated diagram(s) | 0 | 2 |

## DIAMOND_A4 (Ge–O)

- Id: `phase:ge-o:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:a4-diamond)

Names (3): _corpus: _corpus:phase:ge-o:a4-diamond  
_tdb: _tdb:GeO-15Din.tdb:DIAMOND_A4, tdb:GeO-21Baj-3g.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): DIAMOND_A4, type code %, sha256 `004d6c7cf629014a…`

~~~~text
53: PHASE DIAMOND_A4 % 1 1 !
54: CONST DIAMOND_A4 : GE : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): DIAMOND_A4, type code %, sha256 `904325ae56bbb509…`

~~~~text
55: PHASE DIAMOND_A4 % 1 1 !
56: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## BCC_A2 (Ge–O)

- Id: `phase:ge-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:bcc-a2)

Names (3): _corpus: _corpus:phase:ge-o:bcc-a2  
_tdb: _tdb:GeO-15Din.tdb:BCC_A2, tdb:GeO-21Baj-3g.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): BCC_A2, type code %B, sha256 `004d6c7cf629014a…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : GE : O VA% : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): BCC_A2, type code %B, sha256 `904325ae56bbb509…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : GE : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## FCC_A1 (Ge–O)

- Id: `phase:ge-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:fcc-a1)

Names (3): _corpus: _corpus:phase:ge-o:fcc-a1  
_tdb: _tdb:GeO-15Din.tdb:FCC_A1, tdb:GeO-21Baj-3g.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): FCC_A1, type code %A, sha256 `004d6c7cf629014a…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : GE : O VA% : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): FCC_A1, type code %A, sha256 `904325ae56bbb509…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : GE : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## GAS (Ge–O)

- Id: `phase:ge-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:gas)

Names (3): _corpus: _corpus:phase:ge-o:gas  
_tdb: _tdb:GeO-15Din.tdb:GAS, tdb:GeO-21Baj-3g.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): GAS, type code %, sha256 `004d6c7cf629014a…`

~~~~text
69: PHASE GAS:G % 1 1 !
70: CONST GAS:G : O O2 O3 : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): GAS, type code %, sha256 `904325ae56bbb509…`

~~~~text
71: PHASE GAS:G % 1 1 !
72: CONST GAS:G : O O2 O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## GEO2_HT (Ge–O)

- Id: `phase:ge-o:geo2`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (tdb_comment): SiO2 · hP9 · P3_121 — GeO-15Din.tdb: 'Prototype SiO2 (hP9, P3_121), alpha-quartz'
- Candidate (tdb_comment): SiO2 · hP9 · P3_121 — GeO-21Baj-3g.tdb: 'Prototype SiO2 (hP9, P3_121), alpha-quartz'
- Stability: stable in 1 of 2 calculated diagram(s): 1324.19–1389.19 K, x(O) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:geo2)

Names (3): _corpus: _corpus:phase:ge-o:geo2  
_tdb: _tdb:GeO-15Din.tdb:GEO2_HT, tdb:GeO-21Baj-3g.tdb:GEO2_HT  


### TDB models of GEO2_HT (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): GEO2_HT, type code %, sha256 `004d6c7cf629014a…`

~~~~text
63: PHASE GEO2_HT % 2 1 2 !
64: CONST GEO2_HT : GE+4 : O-2 : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): GEO2_HT, type code %, sha256 `904325ae56bbb509…`

~~~~text
65: PHASE GEO2_HT % 2 1 2 !
66: CONST GEO2_HT : GE+4 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## GEO2_C4 (Ge–O)

- Id: `phase:ge-o:geo2-c4`; status `assigned`
- Structure: TiO2 · C4 · tP6 · P4_2/mnm (136); type `st:c4-tio2-tp6`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–475 K, x(O) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:geo2-c4)

Names (3): _corpus: _corpus:phase:ge-o:geo2-c4  
_tdb: _tdb:GeO-15Din.tdb:GEO2_C4, tdb:GeO-21Baj-3g.tdb:GEO2_C4  


### TDB models of GEO2_C4 (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): GEO2_C4, type code %, sha256 `004d6c7cf629014a…`

~~~~text
58: PHASE GEO2_C4 % 2 1 2 !
59: CONST GEO2_C4 : GE+4 : O-2 : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): GEO2_C4, type code %, sha256 `904325ae56bbb509…`

~~~~text
60: PHASE GEO2_C4 % 2 1 2 !
61: CONST GEO2_C4 : GE+4 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## HCP_A3 (Ge–O)

- Id: `phase:ge-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:hcp-a3)

Names (3): _corpus: _corpus:phase:ge-o:hcp-a3  
_tdb: _tdb:GeO-15Din.tdb:HCP_A3, tdb:GeO-21Baj-3g.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): HCP_A3, type code %, sha256 `004d6c7cf629014a…`

~~~~text
48: PHASE HCP_A3 % 2 1 0.5 !
49: CONST HCP_A3 : GE : O VA% : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): HCP_A3, type code %, sha256 `904325ae56bbb509…`

~~~~text
50: PHASE HCP_A3 % 2 1 0.5 !
51: CONST HCP_A3 : GE : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## ION (Ge–O)

- Id: `phase:ge-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1192.81–2500 K, x(O) 0–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:ion)

Names (3): _corpus: _corpus:phase:ge-o:ion  
_tdb: _tdb:GeO-15Din.tdb:ION, tdb:GeO-21Baj-3g.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): ION, type code %, sha256 `004d6c7cf629014a…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : GE+4 : O-2 VA : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): ION, type code %, sha256 `904325ae56bbb509…`

~~~~text
35: PHASE ION:Y % 2 1 1 !
36: CONST ION:Y : GE+4 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## LIQUID (Ge–O)

- Id: `phase:ge-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:liquid)

Names (3): _corpus: _corpus:phase:ge-o:liquid  
_tdb: _tdb:GeO-15Din.tdb:LIQUID, tdb:GeO-21Baj-3g.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): LIQUID, type code %, sha256 `004d6c7cf629014a…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : GE : !
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): LIQUID, type code %, sha256 `904325ae56bbb509…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

## O2GAS (Ge–O)

- Id: `phase:ge-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-o:o2gas)

Names (3): _corpus: _corpus:phase:ge-o:o2gas  
_tdb: _tdb:GeO-15Din.tdb:O2GAS, tdb:GeO-21Baj-3g.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[GeO-15Din.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb): O2GAS, type code %, sha256 `004d6c7cf629014a…`

~~~~text
66: PHASE O2GAS % 1 1 !
67: CONST O2GAS : O2 :!
~~~~

[GeO-21Baj-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb): O2GAS, type code %, sha256 `904325ae56bbb509…`

~~~~text
68: PHASE O2GAS % 1 1 !
69: CONST O2GAS : O2 :!
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021).  
_assessment that models this phase_

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
