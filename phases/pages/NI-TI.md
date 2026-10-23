# Ni–Ti phases

> Ni–Ti system: 14 phases (tier A 7, tier C 3, liquid 1, needs_review 3); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-TI.html · Markdown: https://data.orchid-project.org/phases/pages/NI-TI.md

14 phases (tier A 7, tier C 3, liquid 1, needs_review 3); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-TI) · [full JSON](https://data.orchid-project.org/phases/systems/NI-TI.json) · [Ni–Ti system page](https://data.orchid-project.org/systems/NI-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Ti system (14)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_4SL](#phase-ni-ti-bcc-4sl); _phase:ni-ti:bcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2499.72 K, x(Ti) 0.4478–1 | 0 | 1 |
| [BCC_A2](#phase-ni-ti-bcc-a2); _phase:ni-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 13 of 22 calculated diagram(s): 1036.31–2499.91 K, x(Ti) 0.88033–1 | 8 | 22 |
| [B2_BCC](#phase-ni-ti-bcc-b2); _phase:ni-ti:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–2499.93 K, x(Ti) 0.42452–1 | 37 | 9 |
| [FCC_4SL](#phase-ni-ti-fcc-4sl); _phase:ni-ti:fcc-4sl_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1728.24 K, x(Ti) 0–0.15079 | 0 | 2 |
| [FCC_A1](#phase-ni-ti-fcc-a1); _phase:ni-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 13 of 15 calculated diagram(s): 300–1753.24 K, x(Ti) 0–0.15698 | 3 | 15 |
| [HCP_A3](#phase-ni-ti-hcp-a3); _phase:ni-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 13 of 13 calculated diagram(s): 300–1939.99 K, x(Ti) 0.9976–1 | 4 | 13 |
| [LIQUID](#phase-ni-ti-liquid); _phase:ni-ti:liquid_ | liquid | liquid | stable in 13 of 13 calculated diagram(s): 1212.05–2500 K, x(Ti) 0–1 | 34 | 13 |
| [NI3TI_D024](#phase-ni-ti-ni3ti-d024); _phase:ni-ti:ni3ti-d024_ | Ni3Ti · D0_24 · hP16 · P6_3/mmc (194) | tier A: standard phase name | stable in 13 of 13 calculated diagram(s): 300–2500 K, x(Ti) 0.0776–0.262 | 24 | 13 |
| [NI3TI2](#phase-ni-ti-ni3ti2); _phase:ni-ti:ni3ti2_ | Ni8Ti5 · hR52 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [NI4TI3](#phase-ni-ti-ni4ti3); _phase:ni-ti:ni4ti3_ | Pd4Pu3 · hR14 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [NITI_B19](#phase-ni-ti-niti-b19); _phase:ni-ti:niti-b19_ | AuCd · B19 · oP4 · Pmma (51) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–366.4 K, x(Ti) 0.5–0.50028 | 0 | 1 |
| [NITI_B19P](#phase-ni-ti-niti-b19p); _phase:ni-ti:niti-b19p_ | NiTi · B19' · mP4 · P2_1/m (11) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–351.3 K, x(Ti) 0.5–0.50001 | 0 | 2 |
| [NITI_B2](#phase-ni-ti-niti-b2); _phase:ni-ti:niti-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1584.59 K, x(Ti) 0.43263–0.53215 | 0 | 3 |
| [NITI2](#phase-ni-ti-niti2); _phase:ni-ti:niti2_ |  | needs_review | stable in 13 of 13 calculated diagram(s): 300–1287.9 K, x(Ti) 0.66667–0.66704 | 23 | 13 |

## BCC_4SL (Ni–Ti)

- Id: `phase:ni-ti:bcc-4sl`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:order_disorder_ambiguity; order_disorder_ambiguity:NiTi-14Hu.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:BCC_4SL; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Fd-3m (227) — on-hull MP Ti2Ni at x(TI)=0.6667
- Candidate (dft_mp): P2_1/m (11) — on-hull MP TiNi at x(TI)=0.5000
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Ni1 Ti1 at x(TI)=0.5000
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Ni1 Ti2 at x(TI)=0.6667
- Candidate (dft_oqmd): P42/mnm (136) — on-hull OQMD Ni4 Ti11 at x(TI)=0.7333
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for BCC_4SL: AlFe, AlMn, AlNi, NiTi
- Candidate (tdb_comment): CsCl · B2 · cP2, Pm-3m — NiTi-14Hu.tdb: 'Prototype CsCl (B2, cP2, Pm-3m), NaTl (B32, cF16, Fd-3m),'
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.72 K, x(Ti) 0.4478–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:bcc-4sl)

Names (2): _corpus: _corpus:phase:ni-ti:bcc-4sl  
_tdb: _tdb:NiTi-14Hu.tdb:BCC_4SL  


### TDB models of BCC_4SL (1): PHASE and CONSTITUENT statements as written

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): BCC_4SL, type code %BZ, sha256 `83c0ad45fde56b37…`

~~~~text
72: PHASE BCC_4SL:B %BZ 5 0.25 0.25 0.25 0.25 3 !
73: CONST BCC_4SL:B : NI TI : NI TI : NI TI : NI TI : VA :  !
~~~~

## BCC_A2 (Ni–Ti)

- Id: `phase:ni-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 13 of 22 calculated diagram(s): 1036.31–2499.91 K, x(Ti) 0.88033–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:bcc-a2)

Names (24): _corpus: _corpus:phase:ni-ti:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2014.08.200:(β-Ti)  
_tdb: _tdb:NiTi-04Tok.tdb:BCC_A2, tdb:NiTi-09Key.tdb:A2_BCC, tdb:NiTi-09Key.tdb:BCC_A2, tdb:NiTi-13Pov.tdb:A2_BCC, tdb:NiTi-13Pov.tdb:BCC_A2, tdb:NiTi-14Hu.tdb:A2_BCC, tdb:NiTi-14Hu.tdb:BCC_A2, tdb:NiTi-15San.tdb:A2_BCC, tdb:NiTi-15San.tdb:BCC_A2, tdb:NiTi-16Ber.tdb:BCC_A2, tdb:NiTi-18Hua.tdb:A2_BCC, tdb:NiTi-18Hua.tdb:BCC_A2, tdb:NiTi-21Jin.tdb:A2_BCC, tdb:NiTi-21Jin.tdb:BCC_A2, tdb:NiTi-22Sun.tdb:A2_BCC, tdb:NiTi-22Sun.tdb:BCC_A2, tdb:NiTi-92Sau.tdb:BCC_A2, tdb:NiTi-95Oh.tdb:BCC_A2, tdb:NiTi-96Bel-LB.tdb:A2_BCC, tdb:NiTi-96Bel-LB.tdb:BCC_A2, tdb:NiTi-99Tan.tdb:A2_BCC, tdb:NiTi-99Tan.tdb:BCC_A2  


### TDB models of BCC_A2 (22): PHASE and CONSTITUENT statements as written

[NiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-04Tok.tdb): BCC_A2, type code %B, sha256 `362b1ea505e0ce05…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): A2_BCC, type code %B, sha256 `5edb4535ec69baf2…`

~~~~text
57: PHASE A2_BCC %B 2 1 3 !
58: CONST A2_BCC : NI TI : VA : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): BCC_A2, type code %B, sha256 `5edb4535ec69baf2…`

~~~~text
52: PHASE BCC_A2 %B 2 1 3 !
53: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): A2_BCC, type code %B, sha256 `aba1407d528a3950…`

~~~~text
45: PHASE A2_BCC %B 2 1 3 !
46: CONST A2_BCC : NI TI : VA : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): BCC_A2, type code %B, sha256 `aba1407d528a3950…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): A2_BCC, type code %B, sha256 `83c0ad45fde56b37…`

~~~~text
66: PHASE A2_BCC %B 2 1 3 !
67: CONST A2_BCC : NI TI : VA : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): BCC_A2, type code %B, sha256 `83c0ad45fde56b37…`

~~~~text
61: PHASE BCC_A2 %B 2 1 3 !
62: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): A2_BCC, type code %B, sha256 `28f41732b6b51f8a…`

~~~~text
38: PHASE A2_BCC %B 2 1 3 !
39: CONST A2_BCC : NI TI VA : VA : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): BCC_A2, type code %B, sha256 `28f41732b6b51f8a…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI TI% VA : VA : !
~~~~

[NiTi-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-16Ber.tdb): BCC_A2, type code %B, sha256 `d2a92729bf95724c…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): A2_BCC, type code %B, sha256 `37a12353c6dda89d…`

~~~~text
41: PHASE A2_BCC %B 2 1 3 !
42: CONST A2_BCC : NI TI : VA : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): BCC_A2, type code %B, sha256 `37a12353c6dda89d…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): A2_BCC, type code %B, sha256 `07cb881c11a82ea1…`

~~~~text
39: PHASE A2_BCC %B 2 1 3 !
40: CONST A2_BCC : NI TI : VA : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): BCC_A2, type code %B, sha256 `07cb881c11a82ea1…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): A2_BCC, type code %B, sha256 `510a8484471c8fd2…`

~~~~text
43: PHASE A2_BCC %B 2 1 3 !
44: CONST A2_BCC : NI TI : VA : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): BCC_A2, type code %B, sha256 `510a8484471c8fd2…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-92Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-92Sau.tdb): BCC_A2, type code %B, sha256 `7cdd2f2d8f3af719…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-95Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-95Oh.tdb): BCC_A2, type code %B, sha256 `661c193a3a6c1514…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): A2_BCC, type code %B, sha256 `1dc4d56ca879ba45…`

~~~~text
47: PHASE A2_BCC %B 2 1 3 !
48: CONST A2_BCC : NI TI VA : VA : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): BCC_A2, type code %B, sha256 `1dc4d56ca879ba45…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : NI TI% : VA : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): A2_BCC, type code %B, sha256 `b49cb7d07c39c86a…`

~~~~text
47: PHASE A2_BCC %B 2 1 3 !
48: CONST A2_BCC : NI TI% VA : VA : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): BCC_A2, type code %B, sha256 `b49cb7d07c39c86a…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : NI TI% : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-018-0650-3](https://doi.org/10.1007/s11669-018-0650-3) Jinwan Huang, Yang Wang, Jingjing Wang, Xiao-Gang Lu, Lijun Zhang, Thermodynamic Assessments of the Ni-Cr-Ti System and Atomic Mobility of Its fcc Phase, J. Phase Equilib. Diffus. 39, 597-609 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102256](https://doi.org/10.1016/j.calphad.2021.102256) B. Jin, X. Lu, S. Liu, K. Xu, Y. Du, S. Zhang, M. Chu, Calphad, 73, 102256(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-871207](https://doi.org/10.1515/ijmr-1996-871207) P. Bellen, K.C. Hari Kumar, P. Wollants, Z. Metallkd., 87, 972-78(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## B2_BCC (Ni–Ti)

- Id: `phase:ni-ti:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: NiTi-09Key.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: NiTi-13Pov.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: NiTi-15San.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: NiTi-18Hua.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: NiTi-21Jin.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: NiTi-22Sun.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: NiTi-96Bel-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: NiTi-99Tan.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in NiTi-09Key.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-13Pov.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-15San.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-18Hua.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-21Jin.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-22Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-92Sau.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-96Bel-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-99Tan.tdb also describes the disordered state
- Stability: stable in 9 of 9 calculated diagram(s): 300–2499.93 K, x(Ti) 0.42452–1
- Literature: 37 values (37 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:bcc-b2)

Names (13): _corpus: _corpus:phase:ni-ti:bcc-b2, corpus:phase:ni-ti:b2-bcc  
_paper: _paper:10.1007/s11669-018-0650-3:NiTi, paper:10.1016/j.jallcom.2014.08.200:NiTi  
_tdb: _tdb:NiTi-09Key.tdb:B2_BCC, tdb:NiTi-13Pov.tdb:B2_BCC, tdb:NiTi-15San.tdb:B2_BCC, tdb:NiTi-18Hua.tdb:B2_BCC, tdb:NiTi-21Jin.tdb:B2_BCC, tdb:NiTi-22Sun.tdb:B2_BCC, tdb:NiTi-92Sau.tdb:B2_BCC, tdb:NiTi-96Bel-LB.tdb:B2_BCC, tdb:NiTi-99Tan.tdb:B2_BCC  


### TDB models of B2_BCC (9): PHASE and CONSTITUENT statements as written

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): B2_BCC, type code %BO, sha256 `5edb4535ec69baf2…`

~~~~text
62: PHASE B2_BCC %BO 3 0.5 0.5 3 !
63: CONST B2_BCC : NI% TI : NI TI% : VA : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): B2_BCC, type code %BO, sha256 `aba1407d528a3950…`

~~~~text
50: PHASE B2_BCC %BO 3 0.5 0.5 3 !
51: CONST B2_BCC : NI% TI : NI TI% : VA : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): B2_BCC, type code %BO, sha256 `28f41732b6b51f8a…`

~~~~text
43: PHASE B2_BCC %BO 3 0.5 0.5 3 !
44: CONST B2_BCC : NI% TI VA : NI TI% VA : VA : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): B2_BCC, type code %BO, sha256 `37a12353c6dda89d…`

~~~~text
46: PHASE B2_BCC %BO 3 0.5 0.5 3 !
47: CONST B2_BCC : NI% TI : NI TI% : VA : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): B2_BCC, type code %BO, sha256 `07cb881c11a82ea1…`

~~~~text
44: PHASE B2_BCC %BO 3 0.5 0.5 3 !
45: CONST B2_BCC : NI% TI : NI TI% : VA : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): B2_BCC, type code %BO, sha256 `510a8484471c8fd2…`

~~~~text
48: PHASE B2_BCC %BO 3 0.5 0.5 3 !
49: CONST B2_BCC : NI% TI : NI TI% : VA : !
~~~~

[NiTi-92Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-92Sau.tdb): B2_BCC, type code %B, sha256 `7cdd2f2d8f3af719…`

~~~~text
43: PHASE B2_BCC %B 3 1 1 6 !
44: CONST B2_BCC : NI% TI VA : NI TI% VA : VA : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): B2_BCC, type code %BO, sha256 `1dc4d56ca879ba45…`

~~~~text
52: PHASE B2_BCC %BO 3 0.5 0.5 3 !
53: CONST B2_BCC : NI% TI VA : NI TI% VA : VA : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): B2_BCC, type code %BO, sha256 `b49cb7d07c39c86a…`

~~~~text
52: PHASE B2_BCC %BO 3 0.5 0.5 3 !
53: CONST B2_BCC : NI% TI VA : NI TI% VA : VA : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-018-0650-3](https://doi.org/10.1007/s11669-018-0650-3) Jinwan Huang, Yang Wang, Jingjing Wang, Xiao-Gang Lu, Lijun Zhang, Thermodynamic Assessments of the Ni-Cr-Ti System and Atomic Mobility of Its fcc Phase, J. Phase Equilib. Diffus. 39, 597-609 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102256](https://doi.org/10.1016/j.calphad.2021.102256) B. Jin, X. Lu, S. Liu, K. Xu, Y. Du, S. Zhang, M. Chu, Calphad, 73, 102256(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-871207](https://doi.org/10.1515/ijmr-1996-871207) P. Bellen, K.C. Hari Kumar, P. Wollants, Z. Metallkd., 87, 972-78(1996).  
_assessment that models this phase_
- [doi:10.1103/physrevb.52.15176](https://doi.org/10.1103/physrevb.52.15176) A. Pasturel, C. Colinet, D. Nguyen Manh, A. T. Paxton, M. van Schilfgaarde, Electronic structure and phase stability study in the Ni-Ti system, Phys. Rev. B 52, 15176-15190 (1995).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02385723](https://doi.org/10.1007/bf02385723) H. C. Yi, J. J. Moore, Combustion synthesis of TiNi intermetallic compounds, J Mater Sci 24, 3449-3455 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)87031-1](https://doi.org/10.1016/0040-6031%2881%2987031-1) J.C. Gachon, M. Notin, J. Hertz, The enthalphy of mixing of the intermediate phases in the systems FeTi, CoTi, and NiTi by direct reaction calorimetry, Thermochimica Acta 48, 155-164 (1981).  
_cited as the source of values for this phase_

## FCC_4SL (Ni–Ti)

- Id: `phase:ni-ti:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:NiTi-09Key.tdb_model_is_partitioned; order_disorder_ambiguity:NiTi-14Hu.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — NiTi-09Key.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — NiTi-14Hu.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1728.24 K, x(Ti) 0–0.15079
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:fcc-4sl)

Names (3): _corpus: _corpus:phase:ni-ti:fcc-4sl  
_tdb: _tdb:NiTi-09Key.tdb:FCC_4SL, tdb:NiTi-14Hu.tdb:FCC_4SL  


### TDB models of FCC_4SL (2): PHASE and CONSTITUENT statements as written

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): FCC_4SL, type code %AY, sha256 `5edb4535ec69baf2…`

~~~~text
47: PHASE FCC_4SL %AY 5 0.25 0.25 0.25 0.25 1 !
48: CONST FCC_4SL : NI TI : NI TI : NI TI : NI TI : VA :  !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): FCC_4SL, type code %AY, sha256 `83c0ad45fde56b37…`

~~~~text
56: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
57: CONST FCC_4SL:F : NI TI : NI TI : NI TI : NI TI : VA :  !
~~~~

## FCC_A1 (Ni–Ti)

- Id: `phase:ni-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 13 of 15 calculated diagram(s): 300–1753.24 K, x(Ti) 0–0.15698
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:fcc-a1)

Names (18): _corpus: _corpus:phase:ni-ti:fcc-a1  
_paper: _paper:10.1007/s11669-018-0650-3:fcc, paper:10.1016/j.jallcom.2014.08.200:(γ-Ni)  
_tdb: _tdb:NiTi-04Tok.tdb:FCC_A1, tdb:NiTi-09Key.tdb:A1_FCC, tdb:NiTi-09Key.tdb:FCC_A1, tdb:NiTi-13Pov.tdb:FCC_A1, tdb:NiTi-14Hu.tdb:A1_FCC, tdb:NiTi-14Hu.tdb:FCC_A1, tdb:NiTi-15San.tdb:FCC_A1, tdb:NiTi-16Ber.tdb:FCC_A1, tdb:NiTi-18Hua.tdb:FCC_A1, tdb:NiTi-21Jin.tdb:FCC_A1, tdb:NiTi-22Sun.tdb:FCC_A1, tdb:NiTi-92Sau.tdb:FCC_A1, tdb:NiTi-95Oh.tdb:FCC_A1, tdb:NiTi-96Bel-LB.tdb:FCC_A1, tdb:NiTi-99Tan.tdb:FCC_A1  


### TDB models of FCC_A1 (15): PHASE and CONSTITUENT statements as written

[NiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-04Tok.tdb): FCC_A1, type code %A, sha256 `362b1ea505e0ce05…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): A1_FCC, type code %A, sha256 `5edb4535ec69baf2…`

~~~~text
42: PHASE A1_FCC %A 2 1 1 !
43: CONST A1_FCC : NI% TI : VA : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): FCC_A1, type code %A, sha256 `5edb4535ec69baf2…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): FCC_A1, type code %A, sha256 `aba1407d528a3950…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): A1_FCC, type code %A, sha256 `83c0ad45fde56b37…`

~~~~text
51: PHASE A1_FCC %A 2 1 1 !
52: CONST A1_FCC : NI% TI : VA : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): FCC_A1, type code %A, sha256 `83c0ad45fde56b37…`

~~~~text
46: PHASE FCC_A1 %A 2 1 1 !
47: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): FCC_A1, type code %A, sha256 `28f41732b6b51f8a…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-16Ber.tdb): FCC_A1, type code %A, sha256 `d2a92729bf95724c…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): FCC_A1, type code %A, sha256 `37a12353c6dda89d…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): FCC_A1, type code %A, sha256 `07cb881c11a82ea1…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): FCC_A1, type code %A, sha256 `510a8484471c8fd2…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-92Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-92Sau.tdb): FCC_A1, type code %A, sha256 `7cdd2f2d8f3af719…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-95Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-95Oh.tdb): FCC_A1, type code %A, sha256 `661c193a3a6c1514…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): FCC_A1, type code %A, sha256 `1dc4d56ca879ba45…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : NI% TI : VA : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): FCC_A1, type code %A, sha256 `b49cb7d07c39c86a…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : NI% TI : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-018-0650-3](https://doi.org/10.1007/s11669-018-0650-3) Jinwan Huang, Yang Wang, Jingjing Wang, Xiao-Gang Lu, Lijun Zhang, Thermodynamic Assessments of the Ni-Cr-Ti System and Atomic Mobility of Its fcc Phase, J. Phase Equilib. Diffus. 39, 597-609 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102256](https://doi.org/10.1016/j.calphad.2021.102256) B. Jin, X. Lu, S. Liu, K. Xu, Y. Du, S. Zhang, M. Chu, Calphad, 73, 102256(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-871207](https://doi.org/10.1515/ijmr-1996-871207) P. Bellen, K.C. Hari Kumar, P. Wollants, Z. Metallkd., 87, 972-78(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## HCP_A3 (Ni–Ti)

- Id: `phase:ni-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 13 of 13 calculated diagram(s): 300–1939.99 K, x(Ti) 0.9976–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:hcp-a3)

Names (15): _corpus: _corpus:phase:ni-ti:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2014.08.200:(α-Ti)  
_tdb: _tdb:NiTi-04Tok.tdb:HCP_A3, tdb:NiTi-09Key.tdb:HCP_A3, tdb:NiTi-13Pov.tdb:HCP_A3, tdb:NiTi-14Hu.tdb:HCP_A3, tdb:NiTi-15San.tdb:HCP_A3, tdb:NiTi-16Ber.tdb:HCP_A3, tdb:NiTi-18Hua.tdb:HCP_A3, tdb:NiTi-21Jin.tdb:HCP_A3, tdb:NiTi-22Sun.tdb:HCP_A3, tdb:NiTi-92Sau.tdb:HCP_A3, tdb:NiTi-95Oh.tdb:HCP_A3, tdb:NiTi-96Bel-LB.tdb:HCP_A3, tdb:NiTi-99Tan.tdb:HCP_A3  


### TDB models of HCP_A3 (13): PHASE and CONSTITUENT statements as written

[NiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-04Tok.tdb): HCP_A3, type code %A, sha256 `362b1ea505e0ce05…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): HCP_A3, type code %A, sha256 `5edb4535ec69baf2…`

~~~~text
67: PHASE HCP_A3 %A 2 1 0.5 !
68: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): HCP_A3, type code %A, sha256 `aba1407d528a3950…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): HCP_A3, type code %A, sha256 `83c0ad45fde56b37…`

~~~~text
77: PHASE HCP_A3 %A 2 1 0.5 !
78: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): HCP_A3, type code %A, sha256 `28f41732b6b51f8a…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-16Ber.tdb): HCP_A3, type code %A, sha256 `d2a92729bf95724c…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): HCP_A3, type code %A, sha256 `37a12353c6dda89d…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): HCP_A3, type code %A, sha256 `07cb881c11a82ea1…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): HCP_A3, type code %A, sha256 `510a8484471c8fd2…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-92Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-92Sau.tdb): HCP_A3, type code %A, sha256 `7cdd2f2d8f3af719…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-95Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-95Oh.tdb): HCP_A3, type code %A, sha256 `661c193a3a6c1514…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): HCP_A3, type code %A, sha256 `1dc4d56ca879ba45…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : NI TI% : VA : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): HCP_A3, type code %A, sha256 `b49cb7d07c39c86a…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : NI TI% : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-018-0650-3](https://doi.org/10.1007/s11669-018-0650-3) Jinwan Huang, Yang Wang, Jingjing Wang, Xiao-Gang Lu, Lijun Zhang, Thermodynamic Assessments of the Ni-Cr-Ti System and Atomic Mobility of Its fcc Phase, J. Phase Equilib. Diffus. 39, 597-609 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102256](https://doi.org/10.1016/j.calphad.2021.102256) B. Jin, X. Lu, S. Liu, K. Xu, Y. Du, S. Zhang, M. Chu, Calphad, 73, 102256(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-871207](https://doi.org/10.1515/ijmr-1996-871207) P. Bellen, K.C. Hari Kumar, P. Wollants, Z. Metallkd., 87, 972-78(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## LIQUID (Ni–Ti)

- Id: `phase:ni-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 13 of 13 calculated diagram(s): 1212.05–2500 K, x(Ti) 0–1
- Literature: 34 values (34 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:liquid)

Names (18): _corpus: _corpus:phase:ni-ti:liquid  
_paper: _paper:10.1007/s11669-018-0650-3:L, paper:10.1016/j.calphad.2011.10.003:L, paper:10.1016/j.jallcom.2014.08.200:L, paper:10.1016/s1359-6454(99)00193-7:liquid  
_tdb: _tdb:NiTi-04Tok.tdb:LIQUID, tdb:NiTi-09Key.tdb:LIQUID, tdb:NiTi-13Pov.tdb:LIQUID, tdb:NiTi-14Hu.tdb:LIQUID, tdb:NiTi-15San.tdb:LIQUID, tdb:NiTi-16Ber.tdb:LIQUID, tdb:NiTi-18Hua.tdb:LIQUID, tdb:NiTi-21Jin.tdb:LIQUID, tdb:NiTi-22Sun.tdb:LIQUID, tdb:NiTi-92Sau.tdb:LIQUID, tdb:NiTi-95Oh.tdb:LIQUID, tdb:NiTi-96Bel-LB.tdb:LIQUID, tdb:NiTi-99Tan.tdb:LIQUID  


### TDB models of LIQUID (13): PHASE and CONSTITUENT statements as written

[NiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-04Tok.tdb): LIQUID, type code %, sha256 `362b1ea505e0ce05…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): LIQUID, type code %, sha256 `5edb4535ec69baf2…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): LIQUID, type code %, sha256 `aba1407d528a3950…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): LIQUID, type code %, sha256 `83c0ad45fde56b37…`

~~~~text
41: PHASE LIQUID:L % 1 1 !
42: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): LIQUID, type code %, sha256 `28f41732b6b51f8a…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-16Ber.tdb): LIQUID, type code %, sha256 `d2a92729bf95724c…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): LIQUID, type code %, sha256 `37a12353c6dda89d…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): LIQUID, type code %, sha256 `07cb881c11a82ea1…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): LIQUID, type code %, sha256 `510a8484471c8fd2…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-92Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-92Sau.tdb): LIQUID, type code %, sha256 `7cdd2f2d8f3af719…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-95Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-95Oh.tdb): LIQUID, type code %, sha256 `661c193a3a6c1514…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): LIQUID, type code %, sha256 `1dc4d56ca879ba45…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : NI TI : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): LIQUID, type code %, sha256 `b49cb7d07c39c86a…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : NI TI : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-018-0650-3](https://doi.org/10.1007/s11669-018-0650-3) Jinwan Huang, Yang Wang, Jingjing Wang, Xiao-Gang Lu, Lijun Zhang, Thermodynamic Assessments of the Ni-Cr-Ti System and Atomic Mobility of Its fcc Phase, J. Phase Equilib. Diffus. 39, 597-609 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102256](https://doi.org/10.1016/j.calphad.2021.102256) B. Jin, X. Lu, S. Liu, K. Xu, Y. Du, S. Zhang, M. Chu, Calphad, 73, 102256(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-871207](https://doi.org/10.1515/ijmr-1996-871207) P. Bellen, K.C. Hari Kumar, P. Wollants, Z. Metallkd., 87, 972-78(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_reports values for this phase_

## NI3TI_D024 (Ni–Ti)

- Id: `phase:ni-ti:ni3ti-d024`; status `assigned`
- Structure: Ni3Ti · D0_24 · hP16 · P6_3/mmc (194); type `st:d0-24-ni3ti-hp16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NiTi-04Tok.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-09Key.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-13Pov.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-14Hu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-15San.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-16Ber.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-18Hua.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-21Jin.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-22Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-92Sau.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiTi-99Tan.tdb also describes the disordered state
- Stability: stable in 13 of 13 calculated diagram(s): 300–2500 K, x(Ti) 0.0776–0.262
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:ni3ti-d024)

Names (16): _corpus: _corpus:phase:ni-ti:ni3ti-d024  
_paper: _paper:10.1007/s11669-018-0650-3:Ni3Ti, paper:10.1016/j.jallcom.2014.08.200:Ni3Ti  
_tdb: _tdb:NiTi-04Tok.tdb:NI3TI_D024, tdb:NiTi-09Key.tdb:NI3TI_D024, tdb:NiTi-13Pov.tdb:NI3TI_D024, tdb:NiTi-14Hu.tdb:NI3TI_D024, tdb:NiTi-15San.tdb:NI3TI_D024, tdb:NiTi-16Ber.tdb:NI3TI_D024, tdb:NiTi-18Hua.tdb:NI3TI_D024, tdb:NiTi-21Jin.tdb:NI3TI_D024, tdb:NiTi-22Sun.tdb:NI3TI_D024, tdb:NiTi-92Sau.tdb:NI3TI_D024, tdb:NiTi-95Oh.tdb:NI3TI_D024, tdb:NiTi-96Bel-LB.tdb:NI3TI_D024, tdb:NiTi-99Tan.tdb:NI3TI_D024  


### TDB models of NI3TI_D024 (13): PHASE and CONSTITUENT statements as written

[NiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-04Tok.tdb): NI3TI_D024, type code %, sha256 `362b1ea505e0ce05…`

~~~~text
48: PHASE NI3TI_D024 % 2 0.75 0.25 !
49: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): NI3TI_D024, type code %, sha256 `5edb4535ec69baf2…`

~~~~text
72: PHASE NI3TI_D024 % 2 3 1 !
73: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): NI3TI_D024, type code %, sha256 `aba1407d528a3950…`

~~~~text
60: PHASE NI3TI_D024 % 2 3 1 !
61: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): NI3TI_D024, type code %, sha256 `83c0ad45fde56b37…`

~~~~text
82: PHASE NI3TI_D024 % 2 3 1 !
83: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): NI3TI_D024, type code %, sha256 `28f41732b6b51f8a…`

~~~~text
53: PHASE NI3TI_D024 % 2 3 1 !
54: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-16Ber.tdb): NI3TI_D024, type code %, sha256 `d2a92729bf95724c…`

~~~~text
43: PHASE NI3TI_D024 % 2 0.75 0.25 !
44: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): NI3TI_D024, type code %, sha256 `37a12353c6dda89d…`

~~~~text
56: PHASE NI3TI_D024 % 2 3 1 !
57: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): NI3TI_D024, type code %, sha256 `07cb881c11a82ea1…`

~~~~text
54: PHASE NI3TI_D024 % 2 3 1 !
55: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): NI3TI_D024, type code %, sha256 `510a8484471c8fd2…`

~~~~text
58: PHASE NI3TI_D024 % 2 3 1 !
59: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-92Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-92Sau.tdb): NI3TI_D024, type code %, sha256 `7cdd2f2d8f3af719…`

~~~~text
53: PHASE NI3TI_D024 % 2 3 1 !
54: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

[NiTi-95Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-95Oh.tdb): NI3TI_D024, type code %, sha256 `661c193a3a6c1514…`

~~~~text
53: PHASE NI3TI_D024 % 2 0.75 0.25 !
54: CONST NI3TI_D024 : NI : TI : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): NI3TI_D024, type code %, sha256 `1dc4d56ca879ba45…`

~~~~text
62: PHASE NI3TI_D024 % 2 0.75 0.25 !
63: CONST NI3TI_D024 : NI% : NI TI% : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): NI3TI_D024, type code %, sha256 `b49cb7d07c39c86a…`

~~~~text
62: PHASE NI3TI_D024 % 2 3 1 !
63: CONST NI3TI_D024 : NI% TI : NI TI% : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-018-0650-3](https://doi.org/10.1007/s11669-018-0650-3) Jinwan Huang, Yang Wang, Jingjing Wang, Xiao-Gang Lu, Lijun Zhang, Thermodynamic Assessments of the Ni-Cr-Ti System and Atomic Mobility of Its fcc Phase, J. Phase Equilib. Diffus. 39, 597-609 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102256](https://doi.org/10.1016/j.calphad.2021.102256) B. Jin, X. Lu, S. Liu, K. Xu, Y. Du, S. Zhang, M. Chu, Calphad, 73, 102256(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-871207](https://doi.org/10.1515/ijmr-1996-871207) P. Bellen, K.C. Hari Kumar, P. Wollants, Z. Metallkd., 87, 972-78(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_
- [doi:10.1103/physrevb.52.15176](https://doi.org/10.1103/physrevb.52.15176) A. Pasturel, C. Colinet, D. Nguyen Manh, A. T. Paxton, M. van Schilfgaarde, Electronic structure and phase stability study in the Ni-Ti system, Phys. Rev. B 52, 15176-15190 (1995).  
_cited as the source of values for this phase_

## NI3TI2 (Ni–Ti)

- Id: `phase:ni-ti:ni3ti2`; status `assigned`
- Structure: Ni8Ti5 · hR52 · R-3m (166); type `st:ni8ti5-hr52`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.6000, Ti 0.4000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:ni3ti2)

Names (2): _corpus: _corpus:phase:ni-ti:ni3ti2  
_tdb: _tdb:NiTi-13Pov.tdb:NI3TI2  


### TDB models of NI3TI2 (1): PHASE and CONSTITUENT statements as written

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): NI3TI2, type code %, sha256 `aba1407d528a3950…`

~~~~text
65: PHASE NI3TI2 % 2 3 2 !
66: CONST NI3TI2 : NI : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_

## NI4TI3 (Ni–Ti)

- Id: `phase:ni-ti:ni4ti3`; status `assigned`
- Structure: Pd4Pu3 · hR14 · R-3 (148); type `st:pd4pu3-hr14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.5714, Ti 0.4286
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:ni4ti3)

Names (2): _corpus: _corpus:phase:ni-ti:ni4ti3  
_tdb: _tdb:NiTi-13Pov.tdb:NI4TI3  


### TDB models of NI4TI3 (1): PHASE and CONSTITUENT statements as written

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): NI4TI3, type code %, sha256 `aba1407d528a3950…`

~~~~text
70: PHASE NI4TI3 % 2 4 3 !
71: CONST NI4TI3 : NI : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_

## NITI_B19 (Ni–Ti)

- Id: `phase:ni-ti:niti-b19`; status `assigned`
- Structure: AuCd · B19 · oP4 · Pmma (51); type `st:b19-aucd-op4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–366.4 K, x(Ti) 0.5–0.50028
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:niti-b19)

Names (2): _corpus: _corpus:phase:ni-ti:niti-b19  
_tdb: _tdb:NiTi-99Tan.tdb:NITI_B19  


### TDB models of NITI_B19 (1): PHASE and CONSTITUENT statements as written

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): NITI_B19, type code %B, sha256 `b49cb7d07c39c86a…`

~~~~text
68: PHASE NITI_B19 %B 2 0.5 0.5 !
69: CONST NITI_B19 : NI% VA : NI TI% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase_

## NITI_B19P (Ni–Ti)

- Id: `phase:ni-ti:niti-b19p`; status `assigned`
- Structure: NiTi · B19' · mP4 · P2_1/m (11); type `st:b19-niti-mp4`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:B19P, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–351.3 K, x(Ti) 0.5–0.50001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:niti-b19p)

Names (3): _corpus: _corpus:phase:ni-ti:niti-b19p  
_tdb: _tdb:NiTi-13Pov.tdb:NITI_B19P, tdb:NiTi-22Sun.tdb:NITI_B19P  


### TDB models of NITI_B19P (2): PHASE and CONSTITUENT statements as written

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): NITI_B19P, type code %, sha256 `aba1407d528a3950…`

~~~~text
76: PHASE NITI_B19P % 2 0.5 0.5 !
77: CONST NITI_B19P : NI% VA : NI TI% : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): NITI_B19P, type code %, sha256 `510a8484471c8fd2…`

~~~~text
64: PHASE NITI_B19P % 2 0.5 0.5 !
65: CONST NITI_B19P : NI% VA : NI TI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_

## NITI_B2 (Ni–Ti)

- Id: `phase:ni-ti:niti-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1584.59 K, x(Ti) 0.43263–0.53215
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:niti-b2)

Names (4): _corpus: _corpus:phase:ni-ti:niti-b2  
_tdb: _tdb:NiTi-04Tok.tdb:NITI_B2, tdb:NiTi-16Ber.tdb:NITI_B2, tdb:NiTi-95Oh.tdb:NITI_B2  


### TDB models of NITI_B2 (3): PHASE and CONSTITUENT statements as written

[NiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-04Tok.tdb): NITI_B2, type code %B, sha256 `362b1ea505e0ce05…`

~~~~text
53: PHASE NITI_B2 %B 3 0.5 0.5 3 !
54: CONST NITI_B2 : NI% VA : NI TI% : VA : !
~~~~

[NiTi-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-16Ber.tdb): NITI_B2, type code %B, sha256 `d2a92729bf95724c…`

~~~~text
48: PHASE NITI_B2 %B 3 0.5 0.5 3 !
49: CONST NITI_B2 : NI% VA : NI TI% : VA : !
~~~~

[NiTi-95Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-95Oh.tdb): NITI_B2, type code %B, sha256 `661c193a3a6c1514…`

~~~~text
58: PHASE NITI_B2 %B 3 0.5 0.5 3 !
59: CONST NITI_B2 : NI% VA : NI TI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## NITI2 (Ni–Ti)

- Id: `phase:ni-ti:niti2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): NiTi2 · cF96 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): NiTi2 · cF96 · Fd-3m (227) — Hallstedt 2025 mmc2 row for NITI2: NiTi2
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiTi-04Tok.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiTi-09Key.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiTi-13Pov.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiTi-14Hu.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiTi-15San.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Candidate (tdb_comment): NiTi2 · cF96 · Fd-3m — NiTi-16Ber.tdb: 'Prototype NiTi2 (cF96, Fd-3m)'
- Stability: stable in 13 of 13 calculated diagram(s): 300–1287.9 K, x(Ti) 0.66667–0.66704
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ti:niti2)

Names (16): _corpus: _corpus:phase:ni-ti:niti2  
_paper: _paper:10.1007/s11669-018-0650-3:NiTi2, paper:10.1016/j.jallcom.2014.08.200:NiTi2  
_tdb: _tdb:NiTi-04Tok.tdb:NITI2, tdb:NiTi-09Key.tdb:NITI2, tdb:NiTi-13Pov.tdb:NITI2, tdb:NiTi-14Hu.tdb:NITI2, tdb:NiTi-15San.tdb:NITI2, tdb:NiTi-16Ber.tdb:NITI2, tdb:NiTi-18Hua.tdb:NITI2, tdb:NiTi-21Jin.tdb:NITI2, tdb:NiTi-22Sun.tdb:NITI2, tdb:NiTi-92Sau.tdb:NITI2, tdb:NiTi-95Oh.tdb:NITI2, tdb:NiTi-96Bel-LB.tdb:NITI2, tdb:NiTi-99Tan.tdb:NITI2  


### TDB models of NITI2 (13): PHASE and CONSTITUENT statements as written

[NiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-04Tok.tdb): NITI2, type code %, sha256 `362b1ea505e0ce05…`

~~~~text
58: PHASE NITI2 % 2 0.333 0.667 !
59: CONST NITI2 : NI : TI : !
~~~~

[NiTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-09Key.tdb): NITI2, type code %, sha256 `5edb4535ec69baf2…`

~~~~text
77: PHASE NITI2 % 2 1 2 !
78: CONST NITI2 : NI% TI : NI TI% : !
~~~~

[NiTi-13Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-13Pov.tdb): NITI2, type code %, sha256 `aba1407d528a3950…`

~~~~text
81: PHASE NITI2 % 2 1 2 !
82: CONST NITI2 : NI% TI : NI TI% : !
~~~~

[NiTi-14Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-14Hu.tdb): NITI2, type code %, sha256 `83c0ad45fde56b37…`

~~~~text
87: PHASE NITI2 % 2 1 2 !
88: CONST NITI2 : NI% TI : NI TI% : !
~~~~

[NiTi-15San.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-15San.tdb): NITI2, type code %, sha256 `28f41732b6b51f8a…`

~~~~text
58: PHASE NITI2 % 2 1 2 !
59: CONST NITI2 : NI : TI : !
~~~~

[NiTi-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-16Ber.tdb): NITI2, type code %, sha256 `d2a92729bf95724c…`

~~~~text
53: PHASE NITI2 % 2 0.333 0.667 !
54: CONST NITI2 : NI : TI : !
~~~~

[NiTi-18Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-18Hua.tdb): NITI2, type code %, sha256 `37a12353c6dda89d…`

~~~~text
61: PHASE NITI2 % 2 1 2 !
62: CONST NITI2 : NI% TI : NI TI% : !
~~~~

[NiTi-21Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-21Jin.tdb): NITI2, type code %, sha256 `07cb881c11a82ea1…`

~~~~text
59: PHASE NITI2 % 2 1 2 !
60: CONST NITI2 : NI : TI : !
~~~~

[NiTi-22Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-22Sun.tdb): NITI2, type code %, sha256 `510a8484471c8fd2…`

~~~~text
69: PHASE NITI2 % 2 1 2 !
70: CONST NITI2 : NI% TI : NI TI% : !
~~~~

[NiTi-92Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-92Sau.tdb): NITI2, type code %, sha256 `7cdd2f2d8f3af719…`

~~~~text
58: PHASE NITI2 % 2 1 2 !
59: CONST NITI2 : NI : TI : !
~~~~

[NiTi-95Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-95Oh.tdb): NITI2, type code %, sha256 `661c193a3a6c1514…`

~~~~text
63: PHASE NITI2 % 2 0.33333 0.66667 !
64: CONST NITI2 : NI : TI : !
~~~~

[NiTi-96Bel-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-96Bel-LB.tdb): NITI2, type code %, sha256 `1dc4d56ca879ba45…`

~~~~text
67: PHASE NITI2 % 2 1 2 !
68: CONST NITI2 : NI% TI : NI TI% : !
~~~~

[NiTi-99Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTi-99Tan.tdb): NITI2, type code %, sha256 `b49cb7d07c39c86a…`

~~~~text
73: PHASE NITI2 % 2 1 2 !
74: CONST NITI2 : NI : TI : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-018-0650-3](https://doi.org/10.1007/s11669-018-0650-3) Jinwan Huang, Yang Wang, Jingjing Wang, Xiao-Gang Lu, Lijun Zhang, Thermodynamic Assessments of the Ni-Cr-Ti System and Atomic Mobility of Its fcc Phase, J. Phase Equilib. Diffus. 39, 597-609 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.004](https://doi.org/10.1016/j.calphad.2013.02.004) E. Povoden-Karadeniz, D.C. Cirstea, P. Lang, T. Wojcik, E. Kozeschnik, Thermodynamics of Ti–Ni shape memory alloys, Calphad 41, 128-139 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102256](https://doi.org/10.1016/j.calphad.2021.102256) B. Jin, X. Lu, S. Liu, K. Xu, Y. Du, S. Zhang, M. Chu, Calphad, 73, 102256(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102505](https://doi.org/10.1016/j.calphad.2022.102505) H. Sun, Y. Zhang, Q. Pan, Y. Liu, W. Zheng, and X.-G. Lu, Thermodynamic Modeling of the Ni-Ti-Cr System and the B2/ B190 Martensitic Transformation, Calphad, 2022, 79, 102505. https://doi.org/10.1016/j.calphad.2022.102505  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(99)00193-7](https://doi.org/10.1016/S1359-6454%2899%2900193-7) W. Tang, B. Sundman, R. Sandstrom, C. Qiu, Acta Mater., 47, 3457-68(1999).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-871207](https://doi.org/10.1515/ijmr-1996-871207) P. Bellen, K.C. Hari Kumar, P. Wollants, Z. Metallkd., 87, 972-78(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_
- [doi:10.1103/physrevb.52.15176](https://doi.org/10.1103/physrevb.52.15176) A. Pasturel, C. Colinet, D. Nguyen Manh, A. T. Paxton, M. van Schilfgaarde, Electronic structure and phase stability study in the Ni-Ti system, Phys. Rev. B 52, 15176-15190 (1995).  
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
