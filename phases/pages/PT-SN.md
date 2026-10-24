# Pt–Sn phases

> Pt–Sn system: 11 phases (tier A 9, tier B 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PT-SN.html · Markdown: https://data.orchid-project.org/phases/pages/PT-SN.md

11 phases (tier A 9, tier B 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PT-SN) · [full JSON](https://data.orchid-project.org/phases/systems/PT-SN.json) · [Pt–Sn system page](https://data.orchid-project.org/systems/PT-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/PT-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pt–Sn system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-pt-sn-a4-diamond); _phase:pt-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 1 | 4 |
| [BCT_A5](#phase-pt-sn-a5-bct); _phase:pt-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 13 | 4 |
| [BCC_A2](#phase-pt-sn-bcc-a2); _phase:pt-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-pt-sn-fcc-a1); _phase:pt-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2048.86 K, x(Sn) 0–0.12769 | 11 | 4 |
| [HCP_A3](#phase-pt-sn-hcp-a3); _phase:pt-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-pt-sn-liquid); _phase:pt-sn:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 504.27–2500 K, x(Sn) 0–1 | 99 | 4 |
| [PT2SN3](#phase-pt-sn-pt2sn3); _phase:pt-sn:pt2sn3_ | Pt2Sn3 · hP10 · P6_3/mmc (194) | tier B: DFT-supported (unique MP + OQMD match) | stable in 4 of 4 calculated diagram(s): 300–1176.06 K, x(Sn) 0.6–0.6 | 36 | 4 |
| [PT3SN_L12](#phase-pt-sn-pt3sn-l12); _phase:pt-sn:pt3sn-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1684.88 K, x(Sn) 0.25–0.25 | 41 | 4 |
| [PTSN_B81](#phase-pt-sn-ptsn-b81); _phase:pt-sn:ptsn-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1553.29 K, x(Sn) 0.5–0.5 | 46 | 4 |
| [PTSN2_C1](#phase-pt-sn-ptsn2-c1); _phase:pt-sn:ptsn2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1021.21 K, x(Sn) 0.66667–0.66667 | 33 | 4 |
| [PTSN4_D1C](#phase-pt-sn-ptsn4-d1c); _phase:pt-sn:ptsn4-d1c_ | PtSn4 · D1_c · oC20 · Ccce (68) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–814.06 K, x(Sn) 0.8–0.8 | 41 | 4 |

## DIAMOND_A4 (Pt–Sn)

- Id: `phase:pt-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:a4-diamond)

Names (7): _corpus: _corpus:phase:pt-sn:a4-diamond, corpus:phase:pt-sn:diamond-a4  
_paper: _paper:10.1016/j.jallcom.2020.157064:(α\_Sn)  
_tdb: _tdb:PtSn-01Su.tdb:DIAMOND_A4, tdb:PtSn-08Gro.tdb:DIAMOND_A4, tdb:PtSn-21Cui.tdb:DIAMOND_A4, tdb:PtSn-22Hu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): DIAMOND_A4, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): DIAMOND_A4, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): DIAMOND_A4, type code %, sha256 `8a3b41718a07411c…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): DIAMOND_A4, type code %, sha256 `6450b475af9188aa…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## BCT_A5 (Pt–Sn)

- Id: `phase:pt-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 13 values (13 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:a5-bct)

Names (9): _corpus: _corpus:phase:pt-sn:a5-bct, corpus:phase:pt-sn:bct-a5  
_paper: _paper:10.1016/j.jallcom.2006.11.027:β-Sn, paper:10.1016/j.jallcom.2020.157064:(β\_Sn), paper:10.1016/s0925-8388(01)01201-4:βSn (bct)  
_tdb: _tdb:PtSn-01Su.tdb:BCT_A5, tdb:PtSn-08Gro.tdb:BCT_A5, tdb:PtSn-21Cui.tdb:BCT_A5, tdb:PtSn-22Hu.tdb:BCT_A5  


### TDB models of BCT_A5 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): BCT_A5, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
52: PHASE BCT_A5 % 1 1 !
53: CONST BCT_A5 : SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): BCT_A5, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
52: PHASE BCT_A5 % 1 1 !
53: CONST BCT_A5 : SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): BCT_A5, type code %, sha256 `8a3b41718a07411c…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): BCT_A5, type code %, sha256 `6450b475af9188aa…`

~~~~text
54: PHASE BCT_A5 % 1 1 !
55: CONST BCT_A5 : SN : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_

## BCC_A2 (Pt–Sn)

- Id: `phase:pt-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:bcc-a2)

Names (5): _corpus: _corpus:phase:pt-sn:bcc-a2  
_tdb: _tdb:PtSn-01Su.tdb:BCC_A2, tdb:PtSn-08Gro.tdb:BCC_A2, tdb:PtSn-21Cui.tdb:BCC_A2, tdb:PtSn-22Hu.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): BCC_A2, type code %B, sha256 `eb26f28e6b499db9…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : PT SN  : VA : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): BCC_A2, type code %B, sha256 `7e5e91d53d76607b…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : PT SN  : VA : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): BCC_A2, type code %B, sha256 `8a3b41718a07411c…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : PT SN  : VA : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): BCC_A2, type code %B, sha256 `6450b475af9188aa…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : PT SN  : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase_

## FCC_A1 (Pt–Sn)

- Id: `phase:pt-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2048.86 K, x(Sn) 0–0.12769
- Literature: 11 values (11 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:fcc-a1)

Names (8): _corpus: _corpus:phase:pt-sn:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2006.11.027:(Pt), paper:10.1016/j.jallcom.2020.157064:(Pt), paper:10.1016/s0925-8388(01)01201-4:Pt (f.c.c.)  
_tdb: _tdb:PtSn-01Su.tdb:FCC_A1, tdb:PtSn-08Gro.tdb:FCC_A1, tdb:PtSn-21Cui.tdb:FCC_A1, tdb:PtSn-22Hu.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): FCC_A1, type code %A, sha256 `eb26f28e6b499db9…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : PT% SN : VA : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): FCC_A1, type code %A, sha256 `7e5e91d53d76607b…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : PT% SN : VA : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): FCC_A1, type code %A, sha256 `8a3b41718a07411c…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : PT% SN : VA : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): FCC_A1, type code %A, sha256 `6450b475af9188aa…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : PT% SN : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_

## HCP_A3 (Pt–Sn)

- Id: `phase:pt-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:hcp-a3)

Names (5): _corpus: _corpus:phase:pt-sn:hcp-a3  
_tdb: _tdb:PtSn-01Su.tdb:HCP_A3, tdb:PtSn-08Gro.tdb:HCP_A3, tdb:PtSn-21Cui.tdb:HCP_A3, tdb:PtSn-22Hu.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): HCP_A3, type code %A, sha256 `eb26f28e6b499db9…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : PT SN : VA: !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): HCP_A3, type code %A, sha256 `7e5e91d53d76607b…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : PT SN : VA: !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): HCP_A3, type code %A, sha256 `8a3b41718a07411c…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : PT SN : VA: !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): HCP_A3, type code %A, sha256 `6450b475af9188aa…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : PT SN : VA: !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase_

## LIQUID (Pt–Sn)

- Id: `phase:pt-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 504.27–2500 K, x(Sn) 0–1
- Literature: 99 values (99 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:liquid)

Names (9): _corpus: _corpus:phase:pt-sn:liquid  
_paper: _paper:10.1016/j.jallcom.2006.11.027:Liq, paper:10.1016/j.jallcom.2020.157064:Liquid, paper:10.1016/j.jallcom.2020.157064:liquid, paper:10.1016/s0925-8388(01)01201-4:Liq.  
_tdb: _tdb:PtSn-01Su.tdb:LIQUID, tdb:PtSn-08Gro.tdb:LIQUID, tdb:PtSn-21Cui.tdb:LIQUID, tdb:PtSn-22Hu.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): LIQUID, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : PT SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): LIQUID, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : PT PTSN SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): LIQUID, type code %, sha256 `8a3b41718a07411c…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : PT SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): LIQUID, type code %, sha256 `6450b475af9188aa…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : PT PTSN SN : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_

## PT2SN3 (Pt–Sn)

- Id: `phase:pt-sn:pt2sn3`; status `assigned`
- Structure: Pt2Sn3 · hP10 · P6_3/mmc (194); type `st:pt2sn3-hp10`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Pt 0.4000, Sn 0.6000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1176.06 K, x(Sn) 0.6–0.6
- Literature: 36 values (36 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:pt2sn3)

Names (11): _corpus: _corpus:phase:pt-sn:pt2sn3  
_mp: _mp:mp-aaaabtqk  
_oqmd: _oqmd:oqmd-18003  
_paper: _paper:10.1016/j.jallcom.2006.11.027:Pt2Sn3, paper:10.1016/j.jallcom.2020.157064:Pt2Sn3, paper:10.1016/s0925-8388(01)01201-4:Pt2Sn3, paper:10.1088/2053-1591/ac475f:Pt2Sn3  
_tdb: _tdb:PtSn-01Su.tdb:PT2SN3, tdb:PtSn-08Gro.tdb:PT2SN3, tdb:PtSn-21Cui.tdb:PT2SN3, tdb:PtSn-22Hu.tdb:PT2SN3  


### TDB models of PT2SN3 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): PT2SN3, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
67: PHASE PT2SN3 %  2 2 3 !
68: CONST PT2SN3 : PT : SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): PT2SN3, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
67: PHASE PT2SN3 %  2 2 3 !
68: CONST PT2SN3 : PT : SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): PT2SN3, type code %, sha256 `8a3b41718a07411c…`

~~~~text
66: PHASE PT2SN3 %  2 2 3 !
67: CONST PT2SN3 : PT : SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): PT2SN3, type code %, sha256 `6450b475af9188aa…`

~~~~text
69: PHASE PT2SN3 %  2 2 3 !
70: CONST PT2SN3 : PT : SN : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1088/2053-1591/ac475f](https://doi.org/10.1088/2053-1591/ac475f) Jieqiong Hu, Ming Xie, Yongtai Chen, Jiheng Fang, Qiao Zhang, Thermodynamic reassessment of Au–Pt–Sn system, Mater. Res. Express 9, 016507 (2022).  
_reports values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(70)90094-9](https://doi.org/10.1016/0022-5088%2870%2990094-9) J.S. Charlton, M. Cordey-Hayes, I.R. Harris, A study of the 119Sn mössbauer isomer shifts in some platinum-tin and gold-tin alloys, Journal of the Less Common Metals 20, 105-112 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2009.04.044](https://doi.org/10.1016/j.commatsci.2009.04.044) Wei Zhou, Lijuan Liu, Baoling Li, Ping Wu, Qinggong Song, Structural, elastic and electronic properties of intermetallics in the Pt–Sn system: A density functional investigation, Computational Materials Science 46, 921-931 (2009).  
_cited as the source of values for this phase_

## PT3SN_L12 (Pt–Sn)

- Id: `phase:pt-sn:pt3sn-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pt 0.7500, Sn 0.2500
- Stability: stable in 4 of 4 calculated diagram(s): 300–1684.88 K, x(Sn) 0.25–0.25
- Literature: 41 values (41 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:pt3sn-l12)

Names (9): _corpus: _corpus:phase:pt-sn:pt3sn-l12  
_paper: _paper:10.1016/j.jallcom.2006.11.027:Pt3Sn, paper:10.1016/j.jallcom.2020.157064:Pt3Sn, paper:10.1016/s0925-8388(01)01201-4:Pt3Sn, paper:10.1088/2053-1591/ac475f:Pt3Sn  
_tdb: _tdb:PtSn-01Su.tdb:PT3SN_L12, tdb:PtSn-08Gro.tdb:PT3SN_L12, tdb:PtSn-21Cui.tdb:PT3SN_L12, tdb:PtSn-22Hu.tdb:PT3SN_L12  


### TDB models of PT3SN_L12 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): PT3SN_L12, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
57: PHASE PT3SN_L12 %  2 3 1 !
58: CONST PT3SN_L12 : PT : SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): PT3SN_L12, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
57: PHASE PT3SN_L12 %  2 3 1 !
58: CONST PT3SN_L12 : PT : SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): PT3SN_L12, type code %, sha256 `8a3b41718a07411c…`

~~~~text
56: PHASE PT3SN_L12 %  2 3 1 !
57: CONST PT3SN_L12 : PT : SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): PT3SN_L12, type code %, sha256 `6450b475af9188aa…`

~~~~text
59: PHASE PT3SN_L12 %  2 3 1 !
60: CONST PT3SN_L12 : PT : SN : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_
- [doi:10.1088/2053-1591/ac475f](https://doi.org/10.1088/2053-1591/ac475f) Jieqiong Hu, Ming Xie, Yongtai Chen, Jiheng Fang, Qiao Zhang, Thermodynamic reassessment of Au–Pt–Sn system, Mater. Res. Express 9, 016507 (2022).  
_reports values for this phase_
- [doi:10.1007/bf00623719](https://doi.org/10.1007/bf00623719) Hermann Pfisterer, Konrad Schubert, Neue Phasen vom MnP (B 31)-Typ, Naturwissenschaften 37, 112-113 (1950).  
_cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2009.04.044](https://doi.org/10.1016/j.commatsci.2009.04.044) Wei Zhou, Lijuan Liu, Baoling Li, Ping Wu, Qinggong Song, Structural, elastic and electronic properties of intermetallics in the Pt–Sn system: A density functional investigation, Computational Materials Science 46, 921-931 (2009).  
_cited as the source of values for this phase_

## PTSN_B81 (Pt–Sn)

- Id: `phase:pt-sn:ptsn-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdjs and oqmd-7829, space group 194
- Stoichiometry: Pt 0.5000, Sn 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1553.29 K, x(Sn) 0.5–0.5
- Literature: 46 values (46 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:ptsn-b81)

Names (11): _corpus: _corpus:phase:pt-sn:ptsn-b81  
_mp: _mp:mp-aaaabdjs  
_oqmd: _oqmd:oqmd-7829  
_paper: _paper:10.1016/j.jallcom.2006.11.027:PtSn, paper:10.1016/j.jallcom.2020.157064:PtSn, paper:10.1016/s0925-8388(01)01201-4:PtSn, paper:10.1088/2053-1591/ac475f:PtSn  
_tdb: _tdb:PtSn-01Su.tdb:PTSN_B81, tdb:PtSn-08Gro.tdb:PTSN_B81, tdb:PtSn-21Cui.tdb:PTSN_B81, tdb:PtSn-22Hu.tdb:PTSN_B81  


### TDB models of PTSN_B81 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): PTSN_B81, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
62: PHASE PTSN_B81 %  2 1 1 !
63: CONST PTSN_B81 : PT : SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): PTSN_B81, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
62: PHASE PTSN_B81 %  2 1 1 !
63: CONST PTSN_B81 : PT : SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): PTSN_B81, type code %, sha256 `8a3b41718a07411c…`

~~~~text
61: PHASE PTSN_B81 %  2 1 1 !
62: CONST PTSN_B81 : PT : SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): PTSN_B81, type code %, sha256 `6450b475af9188aa…`

~~~~text
64: PHASE PTSN_B81 %  2 1 1 !
65: CONST PTSN_B81 : PT : SN : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(68)90141-0](https://doi.org/10.1016/0022-5088%2868%2990141-0) I.R. Harris, M. Norman, A.W. Bryant, A study of some palladium-indium, platinum-indium and platinum-tin alloys, Journal of the Less Common Metals 16, 427-440 (1968).  
_cited as the source of values for this phase_
- [doi:10.1088/2053-1591/ac475f](https://doi.org/10.1088/2053-1591/ac475f) Jieqiong Hu, Ming Xie, Yongtai Chen, Jiheng Fang, Qiao Zhang, Thermodynamic reassessment of Au–Pt–Sn system, Mater. Res. Express 9, 016507 (2022).  
_reports values for this phase_
- [doi:10.1016/j.calphad.2016.05.001](https://doi.org/10.1016/j.calphad.2016.05.001) C. Colinet, J.-C. Tedenac, Enthalpies of formation of TM-X compounds (X¼Al, Ga, Si, Ge, Sn). Comparison of ab-initio values and experimental data, Calphad 54 (2016) 16e34.  
_cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2009.04.044](https://doi.org/10.1016/j.commatsci.2009.04.044) Wei Zhou, Lijuan Liu, Baoling Li, Ping Wu, Qinggong Song, Structural, elastic and electronic properties of intermetallics in the Pt–Sn system: A density functional investigation, Computational Materials Science 46, 921-931 (2009).  
_cited as the source of values for this phase_

## PTSN2_C1 (Pt–Sn)

- Id: `phase:pt-sn:ptsn2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdnu and oqmd-18001, space group 225
- Stoichiometry: Pt 0.3333, Sn 0.6667
- Stability: stable in 4 of 4 calculated diagram(s): 300–1021.21 K, x(Sn) 0.66667–0.66667
- Literature: 33 values (33 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:ptsn2-c1)

Names (11): _corpus: _corpus:phase:pt-sn:ptsn2-c1  
_mp: _mp:mp-aaaabdnu  
_oqmd: _oqmd:oqmd-18001  
_paper: _paper:10.1016/j.jallcom.2006.11.027:PtSn2, paper:10.1016/j.jallcom.2020.157064:PtSn2, paper:10.1016/s0925-8388(01)01201-4:PtSn2, paper:10.1088/2053-1591/ac475f:PtSn2  
_tdb: _tdb:PtSn-01Su.tdb:PTSN2_C1, tdb:PtSn-08Gro.tdb:PTSN2_C1, tdb:PtSn-21Cui.tdb:PTSN2_C1, tdb:PtSn-22Hu.tdb:PTSN2_C1  


### TDB models of PTSN2_C1 (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): PTSN2_C1, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
72: PHASE PTSN2_C1 %  2 1 2 !
73: CONST PTSN2_C1 : PT : SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): PTSN2_C1, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
72: PHASE PTSN2_C1 %  2 1 2 !
73: CONST PTSN2_C1 : PT : SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): PTSN2_C1, type code %, sha256 `8a3b41718a07411c…`

~~~~text
71: PHASE PTSN2_C1 %  2 1 2 !
72: CONST PTSN2_C1 : PT : SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): PTSN2_C1, type code %, sha256 `6450b475af9188aa…`

~~~~text
74: PHASE PTSN2_C1 %  2 1 2 !
75: CONST PTSN2_C1 : PT : SN : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_
- [doi:10.1088/2053-1591/ac475f](https://doi.org/10.1088/2053-1591/ac475f) Jieqiong Hu, Ming Xie, Yongtai Chen, Jiheng Fang, Qiao Zhang, Thermodynamic reassessment of Au–Pt–Sn system, Mater. Res. Express 9, 016507 (2022).  
_reports values for this phase_
- [doi:10.1016/0022-5088(68)90141-0](https://doi.org/10.1016/0022-5088%2868%2990141-0) I.R. Harris, M. Norman, A.W. Bryant, A study of some palladium-indium, platinum-indium and platinum-tin alloys, Journal of the Less Common Metals 16, 427-440 (1968).  
_cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2009.04.044](https://doi.org/10.1016/j.commatsci.2009.04.044) Wei Zhou, Lijuan Liu, Baoling Li, Ping Wu, Qinggong Song, Structural, elastic and electronic properties of intermetallics in the Pt–Sn system: A density functional investigation, Computational Materials Science 46, 921-931 (2009).  
_cited as the source of values for this phase_

## PTSN4_D1C (Pt–Sn)

- Id: `phase:pt-sn:ptsn4-d1c`; status `assigned`
- Structure: PtSn4 · D1_c · oC20 · Ccce (68); type `st:d1-c-ptsn4-oc20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabeos and oqmd-647912, space group 68
- Stoichiometry: Pt 0.2000, Sn 0.8000
- Stability: stable in 4 of 4 calculated diagram(s): 300–814.06 K, x(Sn) 0.8–0.8
- Literature: 41 values (41 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sn:ptsn4-d1c)

Names (11): _corpus: _corpus:phase:pt-sn:ptsn4-d1c  
_mp: _mp:mp-aaaabeos  
_oqmd: _oqmd:oqmd-647912  
_paper: _paper:10.1016/j.jallcom.2006.11.027:PtSn4, paper:10.1016/j.jallcom.2020.157064:PtSn4, paper:10.1016/s0925-8388(01)01201-4:PtSn4, paper:10.1088/2053-1591/ac475f:PtSn4  
_tdb: _tdb:PtSn-01Su.tdb:PTSN4_D1C, tdb:PtSn-08Gro.tdb:PTSN4_D1C, tdb:PtSn-21Cui.tdb:PTSN4_D1C, tdb:PtSn-22Hu.tdb:PTSN4_D1C  


### TDB models of PTSN4_D1C (4): PHASE and CONSTITUENT statements as written

[PtSn-01Su.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-01Su.tdb): PTSN4_D1C, type code %, sha256 `eb26f28e6b499db9…`

~~~~text
77: PHASE PTSN4_D1C %  2 1 4 !
78: CONST PTSN4_D1C : PT : SN : !
~~~~

[PtSn-08Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-08Gro.tdb): PTSN4_D1C, type code %, sha256 `7e5e91d53d76607b…`

~~~~text
77: PHASE PTSN4_D1C %  2 1 4 !
78: CONST PTSN4_D1C : PT : SN : !
~~~~

[PtSn-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-21Cui.tdb): PTSN4_D1C, type code %, sha256 `8a3b41718a07411c…`

~~~~text
76: PHASE PTSN4_D1C %  2 1 4 !
77: CONST PTSN4_D1C : PT : SN : !
~~~~

[PtSn-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSn-22Hu.tdb): PTSN4_D1C, type code %, sha256 `6450b475af9188aa…`

~~~~text
79: PHASE PTSN4_D1C %  2 1 4 !
80: CONST PTSN4_D1C : PT : SN : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2020.157064](https://doi.org/10.1016/j.jallcom.2020.157064) Senlin Cui, Matthew Lynn, Ralph E. Napolitano, Experimental investigation and thermodynamic modeling of the binary Pt–Sn system, Journal of Alloys and Compounds 854, 157064 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(01)01201-4](https://doi.org/10.1016/S0925-8388%2801%2901201-4) X. Su, F. Yin, M. Huang, Z. Li, C. Chen, J. Alloys Compd., 325, 109-12(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.11.027](https://doi.org/10.1016/j.jallcom.2006.11.027) Vincent Grolier, Rainer Schmid-Fetzer, Thermodynamic analysis of the Pt–Sn system, Journal of Alloys and Compounds 450, 264-271 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(00)01042-2](https://doi.org/10.1016/s0925-8388%2800%2901042-2) Bernd Künnen, Dirk Niepmann, Wolfgang Jeitschko, Structure refinements and some properties of the transition metal stannides Os3Sn7, Ir5Sn7, Ni0.402(4)Pd0.598Sn4, α-PdSn2 and PtSn4, Journal of Alloys and Compounds 309, 1-9 (2000).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070540130](https://doi.org/10.1002/zaac.19070540130) Fr. Doerinckel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen über einige Platinlegierungen, Z. Anorg. Chem. 54, 333-366 (1907).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90837-0](https://doi.org/10.1016/0925-8388%2894%2990837-0) Ph. Durussel, R. Massara, P. Feschotte, Le système binaire PtSn, Journal of Alloys and Compounds 215, 175-179 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00682-3](https://doi.org/10.1016/s0925-8388%2898%2900682-3) P Anres, M Gaune-Escard, J.P Bros, E Hayer, Enthalpy of formation of the (Pt–Sn) system, Journal of Alloys and Compounds 280, 158-167 (1998).  
_cited as the source of values for this phase_
- [doi:10.1088/2053-1591/ac475f](https://doi.org/10.1088/2053-1591/ac475f) Jieqiong Hu, Ming Xie, Yongtai Chen, Jiheng Fang, Qiao Zhang, Thermodynamic reassessment of Au–Pt–Sn system, Mater. Res. Express 9, 016507 (2022).  
_reports values for this phase_
- [doi:10.1016/j.commatsci.2009.04.044](https://doi.org/10.1016/j.commatsci.2009.04.044) Wei Zhou, Lijuan Liu, Baoling Li, Ping Wu, Qinggong Song, Structural, elastic and electronic properties of intermetallics in the Pt–Sn system: A density functional investigation, Computational Materials Science 46, 921-931 (2009).  
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
