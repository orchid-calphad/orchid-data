# Co–Ti phases

> Co–Ti system: 9 phases (tier A 7, tier C 1, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-TI.html · Markdown: https://data.orchid-project.org/phases/pages/CO-TI.md

9 phases (tier A 7, tier C 1, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-TI) · [full JSON](https://data.orchid-project.org/phases/systems/CO-TI.json) · [Co–Ti system page](https://data.orchid-project.org/systems/CO-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Ti system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-ti-bcc-a2); _phase:co-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 1050–1920 K, x(Ti) 0.89–0.96 | 18 | 12 |
| [B2_BCC](#phase-co-ti-bcc-b2); _phase:co-ti:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2499.95 K, x(Ti) 0.41482–1 | 50 | 6 |
| [C15_LAVES](#phase-co-ti-c15-laves); _phase:co-ti:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1524.39 K, x(Ti) 0.31983–0.34062 | 33 | 6 |
| [C36_LAVES](#phase-co-ti-c36-laves); _phase:co-ti:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1550 K, x(Ti) 0.28715–0.3333 | 36 | 6 |
| [COTI2](#phase-co-ti-coti2); _phase:co-ti:coti2_ | NiTi2 · cF96 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 6 of 6 calculated diagram(s): 300–1340 K, x(Ti) 0.66667–0.66667 | 47 | 6 |
| [FCC_A1](#phase-co-ti-fcc-a1); _phase:co-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 593.41–1885.95 K, x(Ti) 0–0.15423 | 37 | 12 |
| [L12_FCC](#phase-co-ti-fcc-l12); _phase:co-ti:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1885.95 K, x(Ti) 0–0.25 | 55 | 6 |
| [HCP_A3](#phase-co-ti-hcp-a3); _phase:co-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1163.96 K, x(Ti) 0–1 | 17 | 6 |
| [LIQUID](#phase-co-ti-liquid); _phase:co-ti:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1282.88–2500 K, x(Ti) 0–1 | 120 | 6 |

## BCC_A2 (Co–Ti)

- Id: `phase:co-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1050–1920 K, x(Ti) 0.89–0.96
- Literature: 18 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:bcc-a2)

Names (17): _corpus: _corpus:phase:co-ti:bcc-a2  
_paper: _paper:10.1007/s11661-001-0193-8:A2, paper:10.1016/j.jct.2019.105995:A2, paper:10.1016/j.jct.2019.105995:A2(βTi), paper:10.1016/s0966-9795(99)00098-9:A2  
_tdb: _tdb:CoTi-00Cac.tdb:A2_BCC, tdb:CoTi-00Cac.tdb:BCC_A2, tdb:CoTi-01Dav-LB.tdb:A2_BCC, tdb:CoTi-01Dav-LB.tdb:BCC_A2, tdb:CoTi-18Zho.tdb:A2_BCC, tdb:CoTi-18Zho.tdb:BCC_A2, tdb:CoTi-20Wu.tdb:A2_BCC, tdb:CoTi-20Wu.tdb:BCC_A2, tdb:CoTi-22Yan.tdb:A2_BCC, tdb:CoTi-22Yan.tdb:BCC_A2, tdb:CoTi-24Tur.tdb:A2_BCC, tdb:CoTi-24Tur.tdb:BCC_A2  


### TDB models of BCC_A2 (12): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): A2_BCC, type code %B, sha256 `6fb1ebbac943b8ac…`

~~~~text
45: PHASE A2_BCC %B 2 1 3 !
46: CONST A2_BCC : CO TI VA : VA : !
~~~~

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): BCC_A2, type code %B, sha256 `6fb1ebbac943b8ac…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CO TI% : VA : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): A2_BCC, type code %B, sha256 `b8589e70960bb053…`

~~~~text
46: PHASE A2_BCC %B 2 1 3 !
47: CONST A2_BCC : CO TI VA : VA : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): BCC_A2, type code %B, sha256 `b8589e70960bb053…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CO TI% : VA : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): A2_BCC, type code %B, sha256 `647d0f8bf6e642c1…`

~~~~text
46: PHASE A2_BCC %B 2 1 3 !
47: CONST A2_BCC : CO TI VA : VA : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): BCC_A2, type code %B, sha256 `647d0f8bf6e642c1…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CO TI% : VA : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): A2_BCC, type code %B, sha256 `c8f2189ee1f4e5d7…`

~~~~text
47: PHASE A2_BCC %B 2 1 3 !
48: CONST A2_BCC : CO TI VA : VA : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): BCC_A2, type code %B, sha256 `c8f2189ee1f4e5d7…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : CO TI% : VA : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): A2_BCC, type code %B, sha256 `18ac015ba2b74def…`

~~~~text
48: PHASE A2_BCC %B 2 1 3 !
49: CONST A2_BCC : CO TI VA : VA : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): BCC_A2, type code %B, sha256 `18ac015ba2b74def…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : CO TI% : VA : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): A2_BCC, type code %B, sha256 `8e8ceb6778fdc32a…`

~~~~text
62: PHASE A2_BCC %B 2 1 3 !
63: CONST A2_BCC : CO TI VA : VA : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): BCC_A2, type code %B, sha256 `8e8ceb6778fdc32a…`

~~~~text
57: PHASE BCC_A2 %B 2 1 3 !
58: CONST BCC_A2 : CO TI% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_

## B2_BCC (Co–Ti)

- Id: `phase:co-ti:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: CoTi-00Cac.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CoTi-01Dav-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CoTi-18Zho.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CoTi-20Wu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CoTi-22Yan.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CoTi-24Tur.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in CoTi-00Cac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-01Dav-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-18Zho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-20Wu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-22Yan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-24Tur.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–2499.95 K, x(Ti) 0.41482–1
- Literature: 50 values (50 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:bcc-b2)

Names (13): _corpus: _corpus:phase:co-ti:bcc-b2, corpus:phase:co-ti:b2-bcc  
_paper: _paper:10.1007/s11661-001-0193-8:B2, paper:10.1007/s11669-024-01094-y:CoTi, paper:10.1007/s42243-021-00736-6:CoTi, paper:10.1016/j.jct.2019.105995:B2, paper:10.1016/s0966-9795(99)00098-9:B2  
_tdb: _tdb:CoTi-00Cac.tdb:B2_BCC, tdb:CoTi-01Dav-LB.tdb:B2_BCC, tdb:CoTi-18Zho.tdb:B2_BCC, tdb:CoTi-20Wu.tdb:B2_BCC, tdb:CoTi-22Yan.tdb:B2_BCC, tdb:CoTi-24Tur.tdb:B2_BCC  


### TDB models of B2_BCC (6): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): B2_BCC, type code %BO, sha256 `6fb1ebbac943b8ac…`

~~~~text
50: PHASE B2_BCC %BO 3 0.5 0.5 3 !
51: CONST B2_BCC : CO% TI VA : CO TI% VA : VA : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): B2_BCC, type code %BO, sha256 `b8589e70960bb053…`

~~~~text
51: PHASE B2_BCC %BO 3 0.5 0.5 3 !
52: CONST B2_BCC : CO% TI VA : CO TI% VA : VA : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): B2_BCC, type code %BO, sha256 `647d0f8bf6e642c1…`

~~~~text
51: PHASE B2_BCC %BO 3 0.5 0.5 3 !
52: CONST B2_BCC : CO% TI VA : CO TI% VA : VA : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): B2_BCC, type code %BO, sha256 `c8f2189ee1f4e5d7…`

~~~~text
52: PHASE B2_BCC %BO 3 0.5 0.5 3 !
53: CONST B2_BCC : CO% TI VA : CO TI% VA : VA : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): B2_BCC, type code %BO, sha256 `18ac015ba2b74def…`

~~~~text
53: PHASE B2_BCC %BO 3 0.5 0.5 3 !
54: CONST B2_BCC : CO% TI VA : CO TI% VA : VA : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): B2_BCC, type code %BO, sha256 `8e8ceb6778fdc32a…`

~~~~text
67: PHASE B2_BCC %BO 3 0.5 0.5 3 !
68: CONST B2_BCC : CO% TI VA : CO TI% VA : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2019.101681](https://doi.org/10.1016/j.calphad.2019.101681) F. Stein, M. Merali, and P. Watermeyer, The Co-Ti System Revisited: About the Cubic-to-Hexagonal Laves Phase Transformation and Other Controversial Features of the Phase Diagram, Calphad, 2019, 67(2), 101681.  
_cited as the source of values for this phase_

## C15_LAVES (Co–Ti)

- Id: `phase:co-ti:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoTi-00Cac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-01Dav-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-18Zho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-20Wu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-22Yan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-24Tur.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–1524.39 K, x(Ti) 0.31983–0.34062
- Literature: 33 values (33 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:c15-laves)

Names (11): _corpus: _corpus:phase:co-ti:c15-laves  
_paper: _paper:10.1007/s11661-001-0193-8:C15, paper:10.1007/s11669-024-01094-y:C15, paper:10.1016/j.jct.2019.105995:C15, paper:10.1016/s0966-9795(99)00098-9:C15  
_tdb: _tdb:CoTi-00Cac.tdb:C15_LAVES, tdb:CoTi-01Dav-LB.tdb:C15_LAVES, tdb:CoTi-18Zho.tdb:C15_LAVES, tdb:CoTi-20Wu.tdb:C15_LAVES, tdb:CoTi-22Yan.tdb:C15_LAVES, tdb:CoTi-24Tur.tdb:C15_LAVES  


### TDB models of C15_LAVES (6): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): C15_LAVES, type code %, sha256 `6fb1ebbac943b8ac…`

~~~~text
65: PHASE C15_LAVES % 2 2 1 !
66: CONST C15_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): C15_LAVES, type code %, sha256 `b8589e70960bb053…`

~~~~text
66: PHASE C15_LAVES % 2 2 1 !
67: CONST C15_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): C15_LAVES, type code %, sha256 `647d0f8bf6e642c1…`

~~~~text
66: PHASE C15_LAVES % 2 2 1 !
67: CONST C15_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): C15_LAVES, type code %, sha256 `c8f2189ee1f4e5d7…`

~~~~text
67: PHASE C15_LAVES % 2 2 1 !
68: CONST C15_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): C15_LAVES, type code %, sha256 `18ac015ba2b74def…`

~~~~text
68: PHASE C15_LAVES % 2 2 1 !
69: CONST C15_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): C15_LAVES, type code %, sha256 `8e8ceb6778fdc32a…`

~~~~text
82: PHASE C15_LAVES % 2 2 1 !
83: CONST C15_LAVES : CO% TI : CO TI% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2019.101681](https://doi.org/10.1016/j.calphad.2019.101681) F. Stein, M. Merali, and P. Watermeyer, The Co-Ti System Revisited: About the Cubic-to-Hexagonal Laves Phase Transformation and Other Controversial Features of the Phase Diagram, Calphad, 2019, 67(2), 101681.  
_cited as the source of values for this phase_

## C36_LAVES (Co–Ti)

- Id: `phase:co-ti:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoTi-00Cac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-01Dav-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-18Zho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-20Wu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-22Yan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-24Tur.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–1550 K, x(Ti) 0.28715–0.3333
- Literature: 36 values (36 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:c36-laves)

Names (11): _corpus: _corpus:phase:co-ti:c36-laves  
_paper: _paper:10.1007/s11661-001-0193-8:C36, paper:10.1007/s11669-024-01094-y:C36, paper:10.1016/j.jct.2019.105995:C36, paper:10.1016/s0966-9795(99)00098-9:C36  
_tdb: _tdb:CoTi-00Cac.tdb:C36_LAVES, tdb:CoTi-01Dav-LB.tdb:C36_LAVES, tdb:CoTi-18Zho.tdb:C36_LAVES, tdb:CoTi-20Wu.tdb:C36_LAVES, tdb:CoTi-22Yan.tdb:C36_LAVES, tdb:CoTi-24Tur.tdb:C36_LAVES  


### TDB models of C36_LAVES (6): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): C36_LAVES, type code %, sha256 `6fb1ebbac943b8ac…`

~~~~text
60: PHASE C36_LAVES % 2 2 1 !
61: CONST C36_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): C36_LAVES, type code %, sha256 `b8589e70960bb053…`

~~~~text
61: PHASE C36_LAVES % 2 2 1 !
62: CONST C36_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): C36_LAVES, type code %, sha256 `647d0f8bf6e642c1…`

~~~~text
61: PHASE C36_LAVES % 2 2 1 !
62: CONST C36_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): C36_LAVES, type code %, sha256 `c8f2189ee1f4e5d7…`

~~~~text
62: PHASE C36_LAVES % 2 2 1 !
63: CONST C36_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): C36_LAVES, type code %, sha256 `18ac015ba2b74def…`

~~~~text
63: PHASE C36_LAVES % 2 2 1 !
64: CONST C36_LAVES : CO% TI : CO TI% : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): C36_LAVES, type code %, sha256 `8e8ceb6778fdc32a…`

~~~~text
77: PHASE C36_LAVES % 2 2 1 !
78: CONST C36_LAVES : CO% TI : CO TI% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2019.101681](https://doi.org/10.1016/j.calphad.2019.101681) F. Stein, M. Merali, and P. Watermeyer, The Co-Ti System Revisited: About the Cubic-to-Hexagonal Laves Phase Transformation and Other Controversial Features of the Phase Diagram, Calphad, 2019, 67(2), 101681.  
_cited as the source of values for this phase_

## COTI2 (Co–Ti)

- Id: `phase:co-ti:coti2`; status `assigned`
- Structure: NiTi2 · cF96 · Fd-3m (227); type `st:niti2-cf96`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.3333, Ti 0.6667
- Stability: stable in 6 of 6 calculated diagram(s): 300–1340 K, x(Ti) 0.66667–0.66667
- Literature: 47 values (47 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:coti2)

Names (13): _corpus: _corpus:phase:co-ti:coti2  
_paper: _paper:10.1007/s11661-001-0193-8:CoTi2, paper:10.1007/s11669-024-01094-y:CoTi2, paper:10.1007/s42243-021-00736-6:CoTi2, paper:10.1016/j.jct.2019.105995:CoTi2, paper:10.1016/j.jct.2019.105995:E93, paper:10.1016/s0966-9795(99)00098-9:CoTi2  
_tdb: _tdb:CoTi-00Cac.tdb:COTI2, tdb:CoTi-01Dav-LB.tdb:COTI2, tdb:CoTi-18Zho.tdb:COTI2, tdb:CoTi-20Wu.tdb:COTI2, tdb:CoTi-22Yan.tdb:COTI2, tdb:CoTi-24Tur.tdb:COTI2  


### TDB models of COTI2 (6): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): COTI2, type code %, sha256 `6fb1ebbac943b8ac…`

~~~~text
70: PHASE COTI2 % 2 1 2 !
71: CONST COTI2 : CO : TI : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): COTI2, type code %, sha256 `b8589e70960bb053…`

~~~~text
71: PHASE COTI2 % 2 1 2 !
72: CONST COTI2 : CO : TI : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): COTI2, type code %, sha256 `647d0f8bf6e642c1…`

~~~~text
71: PHASE COTI2 % 2 1 2 !
72: CONST COTI2 : CO : TI : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): COTI2, type code %, sha256 `c8f2189ee1f4e5d7…`

~~~~text
72: PHASE COTI2 % 2 1 2 !
73: CONST COTI2 : CO : TI : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): COTI2, type code %, sha256 `18ac015ba2b74def…`

~~~~text
73: PHASE COTI2 % 2 1 2 !
74: CONST COTI2 : CO : TI : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): COTI2, type code %, sha256 `8e8ceb6778fdc32a…`

~~~~text
87: PHASE COTI2 % 2 1 2 !
88: CONST COTI2 : CO : TI : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_

## FCC_A1 (Co–Ti)

- Id: `phase:co-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 593.41–1885.95 K, x(Ti) 0–0.15423
- Literature: 37 values (37 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:fcc-a1)

Names (20): _corpus: _corpus:phase:co-ti:fcc-a1  
_paper: _paper:10.1007/s11661-001-0193-8:A1, paper:10.1007/s11669-024-01094-y:(αCo), paper:10.1007/s11669-024-01094-y:(αCo)para, paper:10.1007/s42243-021-00736-6:α-Co, paper:10.1016/j.jct.2019.105995:A1, paper:10.1016/j.jct.2019.105995:A1(αCo), paper:10.1016/s0966-9795(99)00098-9:A1  
_tdb: _tdb:CoTi-00Cac.tdb:A1_FCC, tdb:CoTi-00Cac.tdb:FCC_A1, tdb:CoTi-01Dav-LB.tdb:A1_FCC, tdb:CoTi-01Dav-LB.tdb:FCC_A1, tdb:CoTi-18Zho.tdb:A1_FCC, tdb:CoTi-18Zho.tdb:FCC_A1, tdb:CoTi-20Wu.tdb:A1_FCC, tdb:CoTi-20Wu.tdb:FCC_A1, tdb:CoTi-22Yan.tdb:A1_FCC, tdb:CoTi-22Yan.tdb:FCC_A1, tdb:CoTi-24Tur.tdb:A1_FCC, tdb:CoTi-24Tur.tdb:FCC_A1  


### TDB models of FCC_A1 (12): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): A1_FCC, type code %A, sha256 `6fb1ebbac943b8ac…`

~~~~text
30: PHASE A1_FCC %A 2 1 1 !
31: CONST A1_FCC : CO% TI : VA : !
~~~~

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): FCC_A1, type code %A, sha256 `6fb1ebbac943b8ac…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% TI : VA : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): A1_FCC, type code %A, sha256 `b8589e70960bb053…`

~~~~text
31: PHASE A1_FCC %A 2 1 1 !
32: CONST A1_FCC : CO% TI : VA : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): FCC_A1, type code %A, sha256 `b8589e70960bb053…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CO% TI : VA : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): A1_FCC, type code %A, sha256 `647d0f8bf6e642c1…`

~~~~text
31: PHASE A1_FCC %A 2 1 1 !
32: CONST A1_FCC : CO% TI : VA : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): FCC_A1, type code %A, sha256 `647d0f8bf6e642c1…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CO% TI : VA : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): A1_FCC, type code %A, sha256 `c8f2189ee1f4e5d7…`

~~~~text
32: PHASE A1_FCC %A 2 1 1 !
33: CONST A1_FCC : CO% TI : VA : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): FCC_A1, type code %A, sha256 `c8f2189ee1f4e5d7…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% TI : VA : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): A1_FCC, type code %A, sha256 `18ac015ba2b74def…`

~~~~text
33: PHASE A1_FCC %A 2 1 1 !
34: CONST A1_FCC : CO% TI : VA : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): FCC_A1, type code %A, sha256 `18ac015ba2b74def…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% TI : VA : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): A1_FCC, type code %A, sha256 `8e8ceb6778fdc32a…`

~~~~text
47: PHASE A1_FCC %A 2 1 1 !
48: CONST A1_FCC : CO% TI : VA : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): FCC_A1, type code %A, sha256 `8e8ceb6778fdc32a…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : CO% TI : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2019.101681](https://doi.org/10.1016/j.calphad.2019.101681) F. Stein, M. Merali, and P. Watermeyer, The Co-Ti System Revisited: About the Cubic-to-Hexagonal Laves Phase Transformation and Other Controversial Features of the Phase Diagram, Calphad, 2019, 67(2), 101681.  
_cited as the source of values for this phase_

## L12_FCC (Co–Ti)

- Id: `phase:co-ti:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: CoTi-00Cac.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: CoTi-01Dav-LB.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: CoTi-18Zho.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: CoTi-20Wu.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: CoTi-22Yan.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: CoTi-24Tur.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in CoTi-00Cac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-01Dav-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-18Zho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-20Wu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-22Yan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoTi-24Tur.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–1885.95 K, x(Ti) 0–0.25
- Literature: 55 values (55 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:fcc-l12)

Names (13): _corpus: _corpus:phase:co-ti:fcc-l12, corpus:phase:co-ti:l12-fcc  
_paper: _paper:10.1007/s11661-001-0193-8:L12, paper:10.1007/s11669-024-01094-y:Co3Ti, paper:10.1007/s42243-021-00736-6:Co3Ti, paper:10.1016/j.jct.2019.105995:L12, paper:10.1016/s0966-9795(99)00098-9:L12  
_tdb: _tdb:CoTi-00Cac.tdb:L12_FCC, tdb:CoTi-01Dav-LB.tdb:L12_FCC, tdb:CoTi-18Zho.tdb:L12_FCC, tdb:CoTi-20Wu.tdb:L12_FCC, tdb:CoTi-22Yan.tdb:L12_FCC, tdb:CoTi-24Tur.tdb:L12_FCC  


### TDB models of L12_FCC (6): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): L12_FCC, type code %AY, sha256 `6fb1ebbac943b8ac…`

~~~~text
35: PHASE L12_FCC %AY 3 0.75 0.25 1 !
36: CONST L12_FCC : CO% TI : CO TI% : VA :  !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): L12_FCC, type code %AY, sha256 `b8589e70960bb053…`

~~~~text
36: PHASE L12_FCC %AY 3 0.75 0.25 1 !
37: CONST L12_FCC : CO% TI : CO TI% : VA :  !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): L12_FCC, type code %AY, sha256 `647d0f8bf6e642c1…`

~~~~text
36: PHASE L12_FCC %AY 3 0.75 0.25 1 !
37: CONST L12_FCC : CO% TI : CO TI% : VA :  !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): L12_FCC, type code %AY, sha256 `c8f2189ee1f4e5d7…`

~~~~text
37: PHASE L12_FCC %AY 3 0.75 0.25 1 !
38: CONST L12_FCC : CO% TI : CO TI% : VA :  !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): L12_FCC, type code %AY, sha256 `18ac015ba2b74def…`

~~~~text
38: PHASE L12_FCC %AY 3 0.75 0.25 1 !
39: CONST L12_FCC : CO% TI : CO TI% : VA :  !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): L12_FCC, type code %AY, sha256 `8e8ceb6778fdc32a…`

~~~~text
52: PHASE L12_FCC %AY 3 0.75 0.25 1 !
53: CONST L12_FCC : CO% TI : CO TI% : VA :  !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2019.101681](https://doi.org/10.1016/j.calphad.2019.101681) F. Stein, M. Merali, and P. Watermeyer, The Co-Ti System Revisited: About the Cubic-to-Hexagonal Laves Phase Transformation and Other Controversial Features of the Phase Diagram, Calphad, 2019, 67(2), 101681.  
_cited as the source of values for this phase_

## HCP_A3 (Co–Ti)

- Id: `phase:co-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1163.96 K, x(Ti) 0–1
- Literature: 17 values (17 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:hcp-a3)

Names (13): _corpus: _corpus:phase:co-ti:hcp-a3  
_paper: _paper:10.1007/s11661-001-0193-8:A3, paper:10.1007/s11669-024-01094-y:(εCo), paper:10.1007/s42243-021-00736-6:α-Ti, paper:10.1016/j.jct.2019.105995:A3, paper:10.1016/j.jct.2019.105995:A3(αTi), paper:10.1016/s0966-9795(99)00098-9:A3  
_tdb: _tdb:CoTi-00Cac.tdb:HCP_A3, tdb:CoTi-01Dav-LB.tdb:HCP_A3, tdb:CoTi-18Zho.tdb:HCP_A3, tdb:CoTi-20Wu.tdb:HCP_A3, tdb:CoTi-22Yan.tdb:HCP_A3, tdb:CoTi-24Tur.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): HCP_A3, type code %A, sha256 `6fb1ebbac943b8ac…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : CO% TI% : VA : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): HCP_A3, type code %A, sha256 `b8589e70960bb053…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : CO% TI% : VA : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): HCP_A3, type code %A, sha256 `647d0f8bf6e642c1…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : CO% TI% : VA : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): HCP_A3, type code %A, sha256 `c8f2189ee1f4e5d7…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : CO% TI% : VA : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): HCP_A3, type code %A, sha256 `18ac015ba2b74def…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : CO% TI% : VA : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): HCP_A3, type code %A, sha256 `8e8ceb6778fdc32a…`

~~~~text
72: PHASE HCP_A3 %A 2 1 0.5 !
73: CONST HCP_A3 : CO% TI% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_

## LIQUID (Co–Ti)

- Id: `phase:co-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1282.88–2500 K, x(Ti) 0–1
- Literature: 120 values (120 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ti:liquid)

Names (14): _corpus: _corpus:phase:co-ti:liquid  
_paper: _paper:10.1007/s11661-001-0193-8:L, paper:10.1007/s11661-001-0193-8:liquid, paper:10.1007/s11669-024-01094-y:L, paper:10.1007/s42243-021-00736-6:liquid, paper:10.1016/j.jct.2019.105995:L, paper:10.1016/j.jct.2019.105995:liquid, paper:10.1016/s0966-9795(99)00098-9:Liquid  
_tdb: _tdb:CoTi-00Cac.tdb:LIQUID, tdb:CoTi-01Dav-LB.tdb:LIQUID, tdb:CoTi-18Zho.tdb:LIQUID, tdb:CoTi-20Wu.tdb:LIQUID, tdb:CoTi-22Yan.tdb:LIQUID, tdb:CoTi-24Tur.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[CoTi-00Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-00Cac.tdb): LIQUID, type code %, sha256 `6fb1ebbac943b8ac…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO TI : !
~~~~

[CoTi-01Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-01Dav-LB.tdb): LIQUID, type code %, sha256 `b8589e70960bb053…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CO TI : !
~~~~

[CoTi-18Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-18Zho.tdb): LIQUID, type code %, sha256 `647d0f8bf6e642c1…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CO TI : !
~~~~

[CoTi-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-20Wu.tdb): LIQUID, type code %, sha256 `c8f2189ee1f4e5d7…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO TI : !
~~~~

[CoTi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-22Yan.tdb): LIQUID, type code %, sha256 `18ac015ba2b74def…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO TI : !
~~~~

[CoTi-24Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTi-24Tur.tdb): LIQUID, type code %, sha256 `8e8ceb6778fdc32a…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : CO COTI COTI2 CO2TI TI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01094-y](https://doi.org/10.1007/s11669-024-01094-y) Mykhailo Turchanin, Pavlo Agraval, Anna Vodopyanova, Liya Dreval, Thermodynamic Assessment of the Co-Ti System, J. Phase Equilib. Diffus. 45, 434-446 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-021-00736-6](https://doi.org/10.1007/s42243-021-00736-6) Hua-kou Yang, Chen-yang Zhou, Hang Wang, Bin Yang, Phase equilibria in Ti-rich portion and thermodynamic re-optimization of Co–Ti system, J. Iron Steel Res. Int. 29, 914-924 (2022).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0193-8](https://doi.org/10.1007/s11661-001-0193-8) A. V. Davydov, U. R. Kattner, D. Josell, R. M. Waterstrat, W. J. Boettinger, J. E. Blendell et al., Determination of the CoTi congruent melting point and thermodynamic reassessment of the Co-Ti system, Metall Mater Trans A 32, 2175-2186 (2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jct.2019.105995](https://doi.org/10.1016/j.jct.2019.105995) Liying Wu, Yinping Zeng, Yafei Pan, Yong Du, Yingbiao Peng, Han Li et al., Thermodynamic description and simulation of solidification microstructure in the Co-Ti system, The Journal of Chemical Thermodynamics 142, 105995 (2020).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(99)00098-9](https://doi.org/10.1016/S0966-9795%2899%2900098-9) G. Cacciamani, R. Ferro, I. Ansara, N. Dupin, Intermetallics, 8, 213-22(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.011](https://doi.org/10.1016/j.calphad.2018.08.011) C. Zhou, C. Guo, C. Li, Z. Du, Calphad, 63, 61-76(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02873414](https://doi.org/10.1007/bf02873414) Joanne L. Murray, The Co−Ti (Cobalt−Titanium) system, Bulletin of Alloy Phase Diagrams 3 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2019.101681](https://doi.org/10.1016/j.calphad.2019.101681) F. Stein, M. Merali, and P. Watermeyer, The Co-Ti System Revisited: About the Cubic-to-Hexagonal Laves Phase Transformation and Other Controversial Features of the Phase Diagram, Calphad, 2019, 67(2), 101681.  
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
