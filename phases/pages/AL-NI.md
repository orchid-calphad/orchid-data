# Al–Ni phases

> Al–Ni system: 12 phases (tier A 7, tier B 2, liquid 1, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-NI.html · Markdown: https://data.orchid-project.org/phases/pages/AL-NI.md

12 phases (tier A 7, tier B 2, liquid 1, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-NI) · [full JSON](https://data.orchid-project.org/phases/systems/AL-NI.json) · [Al–Ni system page](https://data.orchid-project.org/systems/AL-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Ni system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL3NI_D011](#phase-al-ni-al3ni-d011); _phase:al-ni:al3ni-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 13 of 13 calculated diagram(s): 300–1137.04 K, x(Ni) 0.25–0.25 | 34 | 13 |
| [AL3NI2_D513](#phase-al-ni-al3ni2-d513); _phase:al-ni:al3ni2-d513_ | Ni2Al3 · D5_13 · hP5 · P-3m1 (164) | tier A: standard phase name | stable in 13 of 13 calculated diagram(s): 300–1563.52 K, x(Ni) 0.29517–0.4136 | 28 | 13 |
| [AL3NI5](#phase-al-ni-al3ni5); _phase:al-ni:al3ni5_ | Ga3Pt5 · oC16 · Cmmm (65) | tier B: DFT-supported (unique MP + OQMD match) | stable in 12 of 12 calculated diagram(s): 300–1024.89 K, x(Ni) 0.625–0.625 | 14 | 12 |
| [AL4NI3](#phase-al-ni-al4ni3); _phase:al-ni:al4ni3_ | Ga4Ni3 · cI112 · Ia-3d (230) | tier B: DFT-supported (unique MP + OQMD match) | stable in 4 of 4 calculated diagram(s): 300–975.24 K, x(Ni) 0.42857–0.42857 | 2 | 4 |
| [ALNI3_L12](#phase-al-ni-alni3-l12); _phase:al-ni:alni3-l12_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1643.07 K, x(Ni) 0.76–0.76 | 15 | 1 |
| [BCC_A2](#phase-al-ni-bcc-a2); _phase:al-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 18 calculated diagram(s): 300–1916.22 K, x(Ni) 0.41534–0.65223 | 16 | 18 |
| [B2_BCC](#phase-al-ni-bcc-b2); _phase:al-ni:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 12 of 12 calculated diagram(s): 300–1952.88 K, x(Ni) 0.40974–0.7244 | 36 | 12 |
| [FCC_4SL](#phase-al-ni-fcc-4sl); _phase:al-ni:fcc-4sl_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1731.78 K, x(Ni) 0–1 | 15 | 4 |
| [FCC_A1](#phase-al-ni-fcc-a1); _phase:al-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 12 of 22 calculated diagram(s): 300–1734.62 K, x(Ni) 0–1 | 25 | 22 |
| [L12_FCC](#phase-al-ni-fcc-l12); _phase:al-ni:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 300–1728.42 K, x(Ni) 0–1 | 15 | 8 |
| [HCP_A3](#phase-al-ni-hcp-a3); _phase:al-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 13 calculated diagram(s) | 0 | 13 |
| [LIQUID](#phase-al-ni-liquid); _phase:al-ni:liquid_ | liquid | liquid | stable in 13 of 13 calculated diagram(s): 908.3–2500 K, x(Ni) 0–1 | 80 | 13 |

## AL3NI_D011 (Al–Ni)

- Id: `phase:al-ni:al3ni-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabjkld and oqmd-10517, space group 62
- Stoichiometry: Al 0.7500, Ni 0.2500
- Stability: stable in 13 of 13 calculated diagram(s): 300–1137.04 K, x(Ni) 0.25–0.25
- Literature: 34 values (34 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:al3ni-d011)

Names (20): _corpus: _corpus:phase:al-ni:al3ni-d011  
_mp: _mp:mp-aaabjkld  
_oqmd: _oqmd:oqmd-10517  
_paper: _paper:10.1016/j.calphad.2005.02.002:γ1, paper:10.1016/j.intermet.2022.107647:Al3Ni, paper:10.1016/j.tca.2010.10.005:Al3Ni, paper:10.1016/s0966-9795(97)00099-x:Al3Ni  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:AL3NI_D011, tdb:AlNi-01Dup-4sl.tdb:AL3NI_D011, tdb:AlNi-01Dup-LB.tdb:AL3NI_D011, tdb:AlNi-01Dup-orig.tdb:AL3NI_D011, tdb:AlNi-03Sun.tdb:AL3NI_D011, tdb:AlNi-04Oht.tdb:AL3NI_D011, tdb:AlNi-05Mie.tdb:AL3NI_D011, tdb:AlNi-11Che.tdb:AL3NI_D011, tdb:AlNi-14Zhu.tdb:AL3NI_D011, tdb:AlNi-22Yan.tdb:AL3NI_D011, tdb:AlNi-88Ans.tdb:AL3NI_D011, tdb:AlNi-97Ans.tdb:AL3NI_D011, tdb:AlNi-98Hua.tdb:AL3NI_D011  


### TDB models of AL3NI_D011 (13): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): AL3NI_D011, type code %, sha256 `67b462ac7c6861a8…`

~~~~text
70: PHASE AL3NI_D011 % 2 0.75 0.25 !
71: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): AL3NI_D011, type code %, sha256 `de7e77f0f98a25d4…`

~~~~text
76: PHASE AL3NI_D011 % 2 3 1 !
77: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): AL3NI_D011, type code %, sha256 `f92c4694c34add59…`

~~~~text
71: PHASE AL3NI_D011 % 2 0.75 0.25 !
72: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): AL3NI_D011, type code %, sha256 `e936330672baf793…`

~~~~text
66: PHASE AL3NI_D011 % 2 0.75 0.25 !
67: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): AL3NI_D011, type code %, sha256 `b61858b6243ad431…`

~~~~text
78: PHASE AL3NI_D011 % 2 3 1 !
79: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): AL3NI_D011, type code %, sha256 `7532c7378b636d77…`

~~~~text
53: PHASE AL3NI_D011 % 2 3 1 !
54: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): AL3NI_D011, type code %, sha256 `3b6faf924a8dca5b…`

~~~~text
45: PHASE AL3NI_D011 % 2 3 1 !
46: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): AL3NI_D011, type code %, sha256 `38cb761434c46112…`

~~~~text
60: PHASE AL3NI_D011 % 2 3 1 !
61: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): AL3NI_D011, type code %, sha256 `7b8304cf5f0be6a0…`

~~~~text
62: PHASE AL3NI_D011 % 2 3 1 !
63: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): AL3NI_D011, type code %, sha256 `e71d9e3cf85a2ad2…`

~~~~text
66: PHASE AL3NI_D011 % 2 3 1 !
67: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-88Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-88Ans.tdb): AL3NI_D011, type code %, sha256 `e3328a93ebedd45d…`

~~~~text
47: PHASE AL3NI_D011 % 2 0.75 0.25 !
48: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): AL3NI_D011, type code %, sha256 `476040576afa2e82…`

~~~~text
62: PHASE AL3NI_D011 % 2 0.75 0.25 !
63: CONST AL3NI_D011 : AL : NI : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): AL3NI_D011, type code %, sha256 `41ccf30b100f6f25…`

~~~~text
67: PHASE AL3NI_D011 % 2 3 1 !
68: CONST AL3NI_D011 : AL : NI : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(88)90152-6](https://doi.org/10.1016/0001-6160%2888%2990152-6) I. Ansara, B. Sundman, P. Willemin, Thermodynamic modeling of ordered phases in the NiAl system, Acta Metallurgica 36, 977-982 (1988).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1007/bf02667823](https://doi.org/10.1007/bf02667823) H. Okamoto, Al-Ni (aluminum-nickel), JPE 14, 257-259 (1993).  
_cited as the source of values for this phase_

## AL3NI2_D513 (Al–Ni)

- Id: `phase:al-ni:al3ni2-d513`; status `assigned`
- Structure: Ni2Al3 · D5_13 · hP5 · P-3m1 (164); type `st:d5-13-ni2al3-hp5`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlNi-88Ans.tdb also describes the disordered state
- Stability: stable in 13 of 13 calculated diagram(s): 300–1563.52 K, x(Ni) 0.29517–0.4136
- Literature: 28 values (28 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:al3ni2-d513)

Names (18): _corpus: _corpus:phase:al-ni:al3ni2-d513  
_paper: _paper:10.1016/j.calphad.2005.02.002:γ2, paper:10.1016/j.intermet.2022.107647:Al3Ni2, paper:10.1016/j.tca.2010.10.005:Al3Ni2, paper:10.1016/s0966-9795(97)00099-x:Al3Ni2  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:AL3NI2_D513, tdb:AlNi-01Dup-4sl.tdb:AL3NI2_D513, tdb:AlNi-01Dup-LB.tdb:AL3NI2_D513, tdb:AlNi-01Dup-orig.tdb:AL3NI2_D513, tdb:AlNi-03Sun.tdb:AL3NI2_D513, tdb:AlNi-04Oht.tdb:AL3NI2_D513, tdb:AlNi-05Mie.tdb:AL3NI2_D513, tdb:AlNi-11Che.tdb:AL3NI2_D513, tdb:AlNi-14Zhu.tdb:AL3NI2_D513, tdb:AlNi-22Yan.tdb:AL3NI2_D513, tdb:AlNi-88Ans.tdb:AL3NI2_D513, tdb:AlNi-97Ans.tdb:AL3NI2_D513, tdb:AlNi-98Hua.tdb:AL3NI2_D513  


### TDB models of AL3NI2_D513 (13): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): AL3NI2_D513, type code %, sha256 `67b462ac7c6861a8…`

~~~~text
75: PHASE AL3NI2_D513 % 3 3 2 1 !
76: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): AL3NI2_D513, type code %, sha256 `de7e77f0f98a25d4…`

~~~~text
81: PHASE AL3NI2_D513 % 3 3 2 1 !
82: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): AL3NI2_D513, type code %, sha256 `f92c4694c34add59…`

~~~~text
76: PHASE AL3NI2_D513 % 3 3 2 1 !
77: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): AL3NI2_D513, type code %, sha256 `e936330672baf793…`

~~~~text
71: PHASE AL3NI2_D513 % 3 3 2 1 !
72: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): AL3NI2_D513, type code %, sha256 `b61858b6243ad431…`

~~~~text
83: PHASE AL3NI2_D513 % 3 3 2 1 !
84: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): AL3NI2_D513, type code %, sha256 `7532c7378b636d77…`

~~~~text
58: PHASE AL3NI2_D513 % 2 2 3 !
59: CONST AL3NI2_D513 : AL NI% : AL : !
~~~~

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): AL3NI2_D513, type code %, sha256 `3b6faf924a8dca5b…`

~~~~text
50: PHASE AL3NI2_D513 % 2 3 2 !
51: CONST AL3NI2_D513 : AL : NI : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): AL3NI2_D513, type code %, sha256 `38cb761434c46112…`

~~~~text
65: PHASE AL3NI2_D513 % 3 3 2 1 !
66: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): AL3NI2_D513, type code %, sha256 `7b8304cf5f0be6a0…`

~~~~text
67: PHASE AL3NI2_D513 % 3 3 2 1 !
68: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): AL3NI2_D513, type code %, sha256 `e71d9e3cf85a2ad2…`

~~~~text
71: PHASE AL3NI2_D513 % 3 3 2 1 !
72: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-88Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-88Ans.tdb): AL3NI2_D513, type code %, sha256 `e3328a93ebedd45d…`

~~~~text
53: PHASE AL3NI2_D513 % 2 0.6 0.4 !
54: CONST AL3NI2_D513 : AL NI% : AL% NI : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): AL3NI2_D513, type code %, sha256 `476040576afa2e82…`

~~~~text
67: PHASE AL3NI2_D513 % 3 3 2 1 !
68: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): AL3NI2_D513, type code %, sha256 `41ccf30b100f6f25…`

~~~~text
72: PHASE AL3NI2_D513 % 3 3 2 1 !
73: CONST AL3NI2_D513 : AL : AL NI% : NI VA% : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(88)90152-6](https://doi.org/10.1016/0001-6160%2888%2990152-6) I. Ansara, B. Sundman, P. Willemin, Thermodynamic modeling of ordered phases in the NiAl system, Acta Metallurgica 36, 977-982 (1988).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1007/bf02667823](https://doi.org/10.1007/bf02667823) H. Okamoto, Al-Ni (aluminum-nickel), JPE 14, 257-259 (1993).  
_cited as the source of values for this phase_

## AL3NI5 (Al–Ni)

- Id: `phase:al-ni:al3ni5`; status `assigned`
- Structure: Ga3Pt5 · oC16 · Cmmm (65); type `st:ga3pt5-oc16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.3750, Ni 0.6250
- Stability: stable in 12 of 12 calculated diagram(s): 300–1024.89 K, x(Ni) 0.625–0.625
- Literature: 14 values (14 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:al3ni5)

Names (20): _corpus: _corpus:phase:al-ni:al3ni5  
_mp: _mp:mp-aaaaayle  
_oqmd: _oqmd:oqmd-10518  
_paper: _paper:10.1016/j.calphad.2005.02.002:γ3, paper:10.1016/j.intermet.2022.107647:Al3Ni5, paper:10.1016/j.tca.2010.10.005:Al3Ni5, paper:10.1016/s0966-9795(97)00099-x:Al3Ni5, paper:10.1361/105497199770340743:Al3Ni5  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:AL3NI5, tdb:AlNi-01Dup-4sl.tdb:AL3NI5, tdb:AlNi-01Dup-LB.tdb:AL3NI5, tdb:AlNi-01Dup-orig.tdb:AL3NI5, tdb:AlNi-03Sun.tdb:AL3NI5, tdb:AlNi-04Oht.tdb:AL3NI5, tdb:AlNi-05Mie.tdb:AL3NI5, tdb:AlNi-11Che.tdb:AL3NI5, tdb:AlNi-14Zhu.tdb:AL3NI5, tdb:AlNi-22Yan.tdb:AL3NI5, tdb:AlNi-97Ans.tdb:AL3NI5, tdb:AlNi-98Hua.tdb:AL3NI5  


### TDB models of AL3NI5 (12): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): AL3NI5, type code %, sha256 `67b462ac7c6861a8…`

~~~~text
85: PHASE AL3NI5 % 2 0.375 0.625 !
86: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): AL3NI5, type code %, sha256 `de7e77f0f98a25d4…`

~~~~text
91: PHASE AL3NI5 % 2 3 5 !
92: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): AL3NI5, type code %, sha256 `f92c4694c34add59…`

~~~~text
86: PHASE AL3NI5 % 2 0.375 0.625 !
87: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): AL3NI5, type code %, sha256 `e936330672baf793…`

~~~~text
76: PHASE AL3NI5 % 2 0.375 0.625 !
77: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): AL3NI5, type code %, sha256 `b61858b6243ad431…`

~~~~text
88: PHASE AL3NI5 % 2 3 5 !
89: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): AL3NI5, type code %, sha256 `7532c7378b636d77…`

~~~~text
63: PHASE AL3NI5 % 2 3 5 !
64: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): AL3NI5, type code %, sha256 `3b6faf924a8dca5b…`

~~~~text
55: PHASE AL3NI5 % 2 3 5 !
56: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): AL3NI5, type code %, sha256 `38cb761434c46112…`

~~~~text
70: PHASE AL3NI5 % 2 0.375 0.625 !
71: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): AL3NI5, type code %, sha256 `7b8304cf5f0be6a0…`

~~~~text
72: PHASE AL3NI5 % 2 3 5 !
73: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): AL3NI5, type code %, sha256 `e71d9e3cf85a2ad2…`

~~~~text
81: PHASE AL3NI5 % 2 3 5 !
82: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): AL3NI5, type code %, sha256 `476040576afa2e82…`

~~~~text
72: PHASE AL3NI5 % 2 0.375 0.625 !
73: CONST AL3NI5 : AL : NI : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): AL3NI5, type code %, sha256 `41ccf30b100f6f25…`

~~~~text
77: PHASE AL3NI5 % 2 3 5 !
78: CONST AL3NI5 : AL : NI : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1016/0026-0800(84)90004-1](https://doi.org/10.1016/0026-0800%2884%2990004-1) I.M. Robertson, C.M. Wayman, Ni5Al3 and the nickel-aluminum binary phase diagram, Metallography 17, 43-55 (1984).  
_cited as the source of values for this phase_
- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_reports values for this phase_

## AL4NI3 (Al–Ni)

- Id: `phase:al-ni:al4ni3`; status `assigned`
- Structure: Ga4Ni3 · cI112 · Ia-3d (230); type `st:ga4ni3-ci112`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.5714, Ni 0.4286
- Stability: stable in 4 of 4 calculated diagram(s): 300–975.24 K, x(Ni) 0.42857–0.42857
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:al4ni3)

Names (8): _corpus: _corpus:phase:al-ni:al4ni3  
_mp: _mp:mp-aaaaaylf  
_oqmd: _oqmd:oqmd-10519  
_paper: _paper:10.1016/j.intermet.2022.107647:Al4Ni3  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:AL4NI3, tdb:AlNi-01Dup-4sl.tdb:AL4NI3, tdb:AlNi-01Dup-LB.tdb:AL4NI3, tdb:AlNi-22Yan.tdb:AL4NI3  


### TDB models of AL4NI3 (4): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): AL4NI3, type code %, sha256 `67b462ac7c6861a8…`

~~~~text
80: PHASE AL4NI3 % 2 4 3 !
81: CONST AL4NI3 : AL : NI : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): AL4NI3, type code %, sha256 `de7e77f0f98a25d4…`

~~~~text
86: PHASE AL4NI3 % 2 4 3 !
87: CONST AL4NI3 : AL : NI : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): AL4NI3, type code %, sha256 `f92c4694c34add59…`

~~~~text
81: PHASE AL4NI3 % 2 4 3 !
82: CONST AL4NI3 : AL : NI : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): AL4NI3, type code %, sha256 `e71d9e3cf85a2ad2…`

~~~~text
76: PHASE AL4NI3 % 2 4 3 !
77: CONST AL4NI3 : AL : NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase_

## ALNI3_L12 (Al–Ni)

- Id: `phase:al-ni:alni3-l12`; status `needs_review`
- No structure assigned. Why: stoichiometry_contradicts_L1_2:AlNi-05Mie.tdb
- Candidate (name_token): AuCu3 · L1_2 · cP4 · Pm-3m (221) — Strukturbericht/word 'L12' in the TDB name
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m — AlNi-05Mie.tdb: 'Prototype AuCu3 (cP4, Pm-3m)'
- Stoichiometry: Al 0.2400, Ni 0.7600
- Stability: stable in 1 of 1 calculated diagram(s): 300–1643.07 K, x(Ni) 0.76–0.76
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:alni3-l12)

Names (3): _corpus: _corpus:phase:al-ni:alni3-l12  
_paper: _paper:10.1016/j.calphad.2005.02.002:γ′  
_tdb: _tdb:AlNi-05Mie.tdb:ALNI3_L12  


### TDB models of ALNI3_L12 (1): PHASE and CONSTITUENT statements as written

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): ALNI3_L12, type code %, sha256 `3b6faf924a8dca5b…`

~~~~text
60: PHASE ALNI3_L12 % 2 0.24 0.76 !
61: CONST ALNI3_L12 : AL : NI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667823](https://doi.org/10.1007/bf02667823) H. Okamoto, Al-Ni (aluminum-nickel), JPE 14, 257-259 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02652-7](https://doi.org/10.1016/s0925-8388%2896%2902652-7) Ibrahim Ansara, Nathalie Dupin, Hans Leo Lukas, Bo Sundman, Thermodynamic assessment of the Al-Ni system, Journal of Alloys and Compounds 247, 20-30 (1997).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663666](https://doi.org/10.1007/bf02663666) J. D. Verhoeven, J. H. Lee, F.C Laabs, L. L. Jones, The phase equilibria of N3Al evaluated by directional solidification and diffusion couple experiments, JPE 12, 15-23 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-0248(88)90163-7](https://doi.org/10.1016/0022-0248%2888%2990163-7) F.J. Bremer, M. Beyss, E. Karthaus, A. Hellwig, T. Schober, J.-M. Welter et al., Experimental analysis of the Ni-Al phase diagram, Journal of Crystal Growth 87, 185-192 (1988).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-1987-1117](https://doi.org/10.1515/zna-1987-1117) K. Hilpert, D. Kobertz, V. Venugopal, M. Miller, H. Gerads, F. J. Bremer et al., Phase Diagram Studies on the Al- Ni System, Zeitschrift für Naturforschung A 42, 1327-1332 (1987).  
_cited as the source of values for this phase_

## BCC_A2 (Al–Ni)

- Id: `phase:al-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 18 calculated diagram(s): 300–1916.22 K, x(Ni) 0.41534–0.65223
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:bcc-a2)

Names (21): _corpus: _corpus:phase:al-ni:bcc-a2  
_paper: _paper:10.1016/j.calphad.2005.02.002:Bcc, paper:10.1016/j.calphad.2005.02.002:bcc  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:A2_BCC, tdb:AlNi-01Dup-4sl-old.tdb:BCC_A2, tdb:AlNi-01Dup-4sl.tdb:A2_BCC, tdb:AlNi-01Dup-4sl.tdb:BCC_A2, tdb:AlNi-01Dup-LB.tdb:A2_BCC, tdb:AlNi-01Dup-LB.tdb:BCC_A2, tdb:AlNi-01Dup-orig.tdb:A2_BCC, tdb:AlNi-01Dup-orig.tdb:BCC_A2, tdb:AlNi-03Sun.tdb:A2_BCC, tdb:AlNi-03Sun.tdb:BCC_A2, tdb:AlNi-04Oht.tdb:BCC_A2, tdb:AlNi-05Mie.tdb:BCC_A2, tdb:AlNi-11Che.tdb:BCC_A2, tdb:AlNi-14Zhu.tdb:BCC_A2, tdb:AlNi-22Yan.tdb:A2_BCC, tdb:AlNi-22Yan.tdb:BCC_A2, tdb:AlNi-97Ans.tdb:BCC_A2, tdb:AlNi-98Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (18): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): A2_BCC, type code %B, sha256 `67b462ac7c6861a8…`

~~~~text
55: PHASE A2_BCC %B 2 1 3 !
56: CONST A2_BCC : AL NI VA : VA : !
~~~~

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): BCC_A2, type code %B, sha256 `67b462ac7c6861a8…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): A2_BCC, type code %B, sha256 `de7e77f0f98a25d4…`

~~~~text
61: PHASE A2_BCC %B 2 1 3 !
62: CONST A2_BCC : AL NI VA : VA : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): BCC_A2, type code %B, sha256 `de7e77f0f98a25d4…`

~~~~text
56: PHASE BCC_A2 %B 2 1 3 !
57: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): A2_BCC, type code %B, sha256 `f92c4694c34add59…`

~~~~text
56: PHASE A2_BCC %B 2 1 3 !
57: CONST A2_BCC : AL NI VA : VA : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): BCC_A2, type code %B, sha256 `f92c4694c34add59…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): A2_BCC, type code %B, sha256 `e936330672baf793…`

~~~~text
51: PHASE A2_BCC %B 2 1 3 !
52: CONST A2_BCC : AL NI VA : VA : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): BCC_A2, type code %B, sha256 `e936330672baf793…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): A2_BCC, type code %B, sha256 `b61858b6243ad431…`

~~~~text
63: PHASE A2_BCC %B 2 1 3 !
64: CONST A2_BCC : AL NI VA : VA : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): BCC_A2, type code %B, sha256 `b61858b6243ad431…`

~~~~text
58: PHASE BCC_A2 %B 2 1 3 !
59: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): BCC_A2, type code %B, sha256 `7532c7378b636d77…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): BCC_A2, type code %B, sha256 `3b6faf924a8dca5b…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): BCC_A2, type code %B, sha256 `38cb761434c46112…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): BCC_A2, type code %B, sha256 `7b8304cf5f0be6a0…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): A2_BCC, type code %B, sha256 `e71d9e3cf85a2ad2…`

~~~~text
51: PHASE A2_BCC %B 2 1 3 !
52: CONST A2_BCC : AL NI VA : VA : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): BCC_A2, type code %B, sha256 `e71d9e3cf85a2ad2…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : AL NI VA : VA : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): BCC_A2, type code %B, sha256 `476040576afa2e82…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : AL NI : VA : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): BCC_A2, type code %B, sha256 `41ccf30b100f6f25…`

~~~~text
52: PHASE BCC_A2 %B 2 1 3 !
53: CONST BCC_A2 : AL NI : VA : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1007/bf02667823](https://doi.org/10.1007/bf02667823) H. Okamoto, Al-Ni (aluminum-nickel), JPE 14, 257-259 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663666](https://doi.org/10.1007/bf02663666) J. D. Verhoeven, J. H. Lee, F.C Laabs, L. L. Jones, The phase equilibria of N3Al evaluated by directional solidification and diffusion couple experiments, JPE 12, 15-23 (1991).  
_cited as the source of values for this phase_

## B2_BCC (Al–Ni)

- Id: `phase:al-ni:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: AlNi-01Dup-4sl-old.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: AlNi-01Dup-4sl.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: AlNi-01Dup-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: AlNi-01Dup-orig.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: AlNi-03Sun.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: AlNi-22Yan.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in AlNi-01Dup-4sl-old.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-01Dup-4sl.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-01Dup-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-01Dup-orig.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-03Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-04Oht.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-11Che.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-22Yan.tdb also describes the disordered state
- Stability: stable in 12 of 12 calculated diagram(s): 300–1952.88 K, x(Ni) 0.40974–0.7244
- Literature: 36 values (36 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:bcc-b2)

Names (17): _corpus: _corpus:phase:al-ni:bcc-b2, corpus:phase:al-ni:b2-bcc  
_paper: _paper:10.1016/j.intermet.2022.107647:B2, paper:10.1016/j.tca.2010.10.005:B2, paper:10.1016/s0966-9795(97)00099-x:B2  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:B2_BCC, tdb:AlNi-01Dup-4sl.tdb:B2_BCC, tdb:AlNi-01Dup-LB.tdb:B2_BCC, tdb:AlNi-01Dup-orig.tdb:B2_BCC, tdb:AlNi-03Sun.tdb:B2_BCC, tdb:AlNi-04Oht.tdb:B2_BCC, tdb:AlNi-11Che.tdb:B2_BCC, tdb:AlNi-14Zhu.tdb:B2_BCC, tdb:AlNi-22Yan.tdb:B2_BCC, tdb:AlNi-88Ans.tdb:B2_BCC, tdb:AlNi-97Ans.tdb:B2_BCC, tdb:AlNi-98Hua.tdb:B2_BCC  


### TDB models of B2_BCC (12): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): B2_BCC, type code %BO, sha256 `67b462ac7c6861a8…`

~~~~text
60: PHASE B2_BCC %BO 3 0.5 0.5 3 !
61: CONST B2_BCC : AL% NI VA : AL NI% VA : VA : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): B2_BCC, type code %BO, sha256 `de7e77f0f98a25d4…`

~~~~text
66: PHASE B2_BCC %BO 3 0.5 0.5 3 !
67: CONST B2_BCC : AL% NI VA : AL NI% VA : VA : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): B2_BCC, type code %BO, sha256 `f92c4694c34add59…`

~~~~text
61: PHASE B2_BCC %BO 3 0.5 0.5 3 !
62: CONST B2_BCC : AL% NI VA : AL NI% VA : VA : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): B2_BCC, type code %BO, sha256 `e936330672baf793…`

~~~~text
56: PHASE B2_BCC %BO 3 0.5 0.5 3 !
57: CONST B2_BCC : AL% NI VA : AL NI% VA : VA : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): B2_BCC, type code %BO, sha256 `b61858b6243ad431…`

~~~~text
68: PHASE B2_BCC %BO 3 0.5 0.5 3 !
69: CONST B2_BCC : AL% NI VA : AL NI% VA : VA : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): B2_BCC, type code %B, sha256 `7532c7378b636d77…`

~~~~text
43: PHASE B2_BCC %B 5 0.25 0.25 0.25 0.25 3 !
44: CONST B2_BCC : AL% NI : AL% NI : AL NI% : AL NI% : VA : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): B2_BCC, type code %B, sha256 `38cb761434c46112…`

~~~~text
50: PHASE B2_BCC %B 2 1 1 !
51: CONST B2_BCC : AL% NI VA : AL NI% VA : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): B2_BCC, type code %B, sha256 `7b8304cf5f0be6a0…`

~~~~text
52: PHASE B2_BCC %B 2 1 1 !
53: CONST B2_BCC : AL% NI : NI% VA : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): B2_BCC, type code %BO, sha256 `e71d9e3cf85a2ad2…`

~~~~text
56: PHASE B2_BCC %BO 3 0.5 0.5 3 !
57: CONST B2_BCC : AL% NI VA : AL NI% VA : VA : !
~~~~

[AlNi-88Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-88Ans.tdb): B2_BCC, type code %B, sha256 `e3328a93ebedd45d…`

~~~~text
37: PHASE B2_BCC %B 2 0.5 0.5 !
38: CONST B2_BCC : AL% NI : NI% VA : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): B2_BCC, type code %B, sha256 `476040576afa2e82…`

~~~~text
52: PHASE B2_BCC %B 2 1 1 !
53: CONST B2_BCC : AL% NI : NI% VA : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): B2_BCC, type code %B, sha256 `41ccf30b100f6f25…`

~~~~text
57: PHASE B2_BCC %B 2 1 1 !
58: CONST B2_BCC : AL% NI : NI% VA : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(88)90152-6](https://doi.org/10.1016/0001-6160%2888%2990152-6) I. Ansara, B. Sundman, P. Willemin, Thermodynamic modeling of ordered phases in the NiAl system, Acta Metallurgica 36, 977-982 (1988).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1007/bf02669138](https://doi.org/10.1007/bf02669138) J. D. Cotton, R. D. Noebe, M. J. Kaufman, Nial-rich portion of the NiAl-Cr pseudobinary eutectic system, JPE 14, 579-582 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0026-0800(84)90004-1](https://doi.org/10.1016/0026-0800%2884%2990004-1) I.M. Robertson, C.M. Wayman, Ni5Al3 and the nickel-aluminum binary phase diagram, Metallography 17, 43-55 (1984).  
_cited as the source of values for this phase_

## FCC_4SL (Al–Ni)

- Id: `phase:al-ni:fcc-4sl`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:order_disorder_ambiguity; order_disorder_ambiguity:AlNi-01Dup-4sl-old.tdb_model_is_partitioned; order_disorder_ambiguity:AlNi-01Dup-4sl.tdb_model_is_partitioned; order_disorder_ambiguity:AlNi-03Sun.tdb_model_is_partitioned; order_disorder_ambiguity:AlNi-22Yan.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Pnma (62) — on-hull MP Al3Ni at x(NI)=0.2500
- Candidate (dft_mp): P-3m1 (164) — on-hull MP Al3Ni2 at x(NI)=0.4000
- Candidate (dft_mp): Cmmm (65) — on-hull MP Al3Ni5 at x(NI)=0.6250
- Candidate (dft_mp): Ia-3d (230) — on-hull MP Al4Ni3 at x(NI)=0.4286
- Candidate (dft_mp): Pm-3m (221) — on-hull MP AlNi at x(NI)=0.5000
- Candidate (dft_mp): Pm-3m (221) — on-hull MP AlNi3 at x(NI)=0.7500
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Al1 Ni1 at x(NI)=0.5000
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Al3 Ni1 at x(NI)=0.2500
- Stability: stable in 4 of 4 calculated diagram(s): 300–1731.78 K, x(Ni) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:fcc-4sl)

Names (9): _corpus: _corpus:phase:al-ni:fcc-4sl  
_paper: _paper:10.1016/j.intermet.2022.107647:L10-Al2Ni2, paper:10.1016/j.intermet.2022.107647:L12, paper:10.1016/j.intermet.2022.107647:L12-Al3Ni, paper:10.1016/j.intermet.2022.107647:L12-AlNi3  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:FCC_4SL, tdb:AlNi-01Dup-4sl.tdb:FCC_4SL, tdb:AlNi-03Sun.tdb:FCC_4SL, tdb:AlNi-22Yan.tdb:FCC_4SL  


### TDB models of FCC_4SL (4): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): FCC_4SL, type code %AY, sha256 `67b462ac7c6861a8…`

~~~~text
45: PHASE FCC_4SL %AY 5 0.25 0.25 0.25 0.25 1 !
46: CONST FCC_4SL : AL NI% : AL NI% : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): FCC_4SL, type code %AY, sha256 `de7e77f0f98a25d4…`

~~~~text
51: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
52: CONST FCC_4SL:F : AL NI% : AL NI% : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): FCC_4SL, type code %AY, sha256 `b61858b6243ad431…`

~~~~text
53: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
54: CONST FCC_4SL:F : AL NI% : AL NI% : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): FCC_4SL, type code %AY, sha256 `e71d9e3cf85a2ad2…`

~~~~text
41: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
42: CONST FCC_4SL:F : AL NI% : AL NI% : AL NI% : AL% NI : VA :  !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1515/zna-1987-1117](https://doi.org/10.1515/zna-1987-1117) K. Hilpert, D. Kobertz, V. Venugopal, M. Miller, H. Gerads, F. J. Bremer et al., Phase Diagram Studies on the Al- Ni System, Zeitschrift für Naturforschung A 42, 1327-1332 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0026-0800(84)90004-1](https://doi.org/10.1016/0026-0800%2884%2990004-1) I.M. Robertson, C.M. Wayman, Ni5Al3 and the nickel-aluminum binary phase diagram, Metallography 17, 43-55 (1984).  
_cited as the source of values for this phase_

## FCC_A1 (Al–Ni)

- Id: `phase:al-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 12 of 22 calculated diagram(s): 300–1734.62 K, x(Ni) 0–1
- Literature: 25 values (25 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:fcc-a1)

Names (29): _corpus: _corpus:phase:al-ni:fcc-a1  
_paper: _paper:10.1016/j.calphad.2005.02.002:fcc, paper:10.1016/j.intermet.2022.107647:(Al), paper:10.1016/j.intermet.2022.107647:(Ni), paper:10.1016/j.tca.2010.10.005:(Al), paper:10.1016/j.tca.2010.10.005:(Ni), paper:10.1016/s0966-9795(97)00099-x:fcc  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:A1_FCC, tdb:AlNi-01Dup-4sl-old.tdb:FCC_A1, tdb:AlNi-01Dup-4sl.tdb:A1_FCC, tdb:AlNi-01Dup-4sl.tdb:FCC_A1, tdb:AlNi-01Dup-LB.tdb:A1_FCC, tdb:AlNi-01Dup-LB.tdb:FCC_A1, tdb:AlNi-01Dup-orig.tdb:A1_FCC, tdb:AlNi-01Dup-orig.tdb:FCC_A1, tdb:AlNi-03Sun.tdb:A1_FCC, tdb:AlNi-03Sun.tdb:FCC_A1, tdb:AlNi-04Oht.tdb:FCC_A1, tdb:AlNi-05Mie.tdb:FCC_A1, tdb:AlNi-11Che.tdb:A1_FCC, tdb:AlNi-11Che.tdb:FCC_A1, tdb:AlNi-14Zhu.tdb:A1_FCC, tdb:AlNi-14Zhu.tdb:FCC_A1, tdb:AlNi-22Yan.tdb:A1_FCC, tdb:AlNi-22Yan.tdb:FCC_A1, tdb:AlNi-97Ans.tdb:A1_FCC, tdb:AlNi-97Ans.tdb:FCC_A1, tdb:AlNi-98Hua.tdb:A1_FCC, tdb:AlNi-98Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (22): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): A1_FCC, type code %A, sha256 `67b462ac7c6861a8…`

~~~~text
40: PHASE A1_FCC %A 2 1 1 !
41: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): FCC_A1, type code %A, sha256 `67b462ac7c6861a8…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): A1_FCC, type code %A, sha256 `de7e77f0f98a25d4…`

~~~~text
46: PHASE A1_FCC %A 2 1 1 !
47: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): FCC_A1, type code %A, sha256 `de7e77f0f98a25d4…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): A1_FCC, type code %A, sha256 `f92c4694c34add59…`

~~~~text
41: PHASE A1_FCC %A 2 1 1 !
42: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): FCC_A1, type code %A, sha256 `f92c4694c34add59…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): A1_FCC, type code %A, sha256 `e936330672baf793…`

~~~~text
36: PHASE A1_FCC %A 2 1 1 !
37: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): FCC_A1, type code %A, sha256 `e936330672baf793…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): A1_FCC, type code %A, sha256 `b61858b6243ad431…`

~~~~text
48: PHASE A1_FCC %A 2 1 1 !
49: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): FCC_A1, type code %A, sha256 `b61858b6243ad431…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): FCC_A1, type code %A, sha256 `7532c7378b636d77…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): FCC_A1, type code %A, sha256 `3b6faf924a8dca5b…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): A1_FCC, type code %A, sha256 `38cb761434c46112…`

~~~~text
35: PHASE A1_FCC %A 2 1 1 !
36: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): FCC_A1, type code %A, sha256 `38cb761434c46112…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): A1_FCC, type code %A, sha256 `7b8304cf5f0be6a0…`

~~~~text
37: PHASE A1_FCC %A 2 1 1 !
38: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): FCC_A1, type code %A, sha256 `7b8304cf5f0be6a0…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): A1_FCC, type code %A, sha256 `e71d9e3cf85a2ad2…`

~~~~text
36: PHASE A1_FCC %A 2 1 1 !
37: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): FCC_A1, type code %A, sha256 `e71d9e3cf85a2ad2…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): A1_FCC, type code %A, sha256 `476040576afa2e82…`

~~~~text
37: PHASE A1_FCC %A 2 1 1 !
38: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): FCC_A1, type code %A, sha256 `476040576afa2e82…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL NI : VA : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): A1_FCC, type code %A, sha256 `41ccf30b100f6f25…`

~~~~text
42: PHASE A1_FCC %A 2 1 1 !
43: CONST A1_FCC : AL NI : VA : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): FCC_A1, type code %A, sha256 `41ccf30b100f6f25…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AL NI : VA : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1515/zna-1987-1117](https://doi.org/10.1515/zna-1987-1117) K. Hilpert, D. Kobertz, V. Venugopal, M. Miller, H. Gerads, F. J. Bremer et al., Phase Diagram Studies on the Al- Ni System, Zeitschrift für Naturforschung A 42, 1327-1332 (1987).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667823](https://doi.org/10.1007/bf02667823) H. Okamoto, Al-Ni (aluminum-nickel), JPE 14, 257-259 (1993).  
_cited as the source of values for this phase_

## L12_FCC (Al–Ni)

- Id: `phase:al-ni:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: AlNi-01Dup-LB.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: AlNi-01Dup-orig.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: AlNi-11Che.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: AlNi-14Zhu.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: AlNi-97Ans.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: AlNi-98Hua.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in AlNi-01Dup-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-01Dup-orig.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-04Oht.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-11Che.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-14Zhu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-88Ans.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-97Ans.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlNi-98Hua.tdb also describes the disordered state
- Stability: stable in 8 of 8 calculated diagram(s): 300–1728.42 K, x(Ni) 0–1
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:fcc-l12)

Names (13): _corpus: _corpus:phase:al-ni:fcc-l12, corpus:phase:al-ni:l12-fcc  
_paper: _paper:10.1016/j.tca.2010.10.005:L12, paper:10.1016/s0966-9795(97)00099-x:L12, paper:10.1016/s0966-9795(97)00099-x:Ni3Al  
_tdb: _tdb:AlNi-01Dup-LB.tdb:L12_FCC, tdb:AlNi-01Dup-orig.tdb:L12_FCC, tdb:AlNi-04Oht.tdb:L12_FCC, tdb:AlNi-11Che.tdb:L12_FCC, tdb:AlNi-14Zhu.tdb:L12_FCC, tdb:AlNi-88Ans.tdb:L12_FCC, tdb:AlNi-97Ans.tdb:L12_FCC, tdb:AlNi-98Hua.tdb:L12_FCC  


### TDB models of L12_FCC (8): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): L12_FCC, type code %AY, sha256 `f92c4694c34add59…`

~~~~text
46: PHASE L12_FCC %AY 3 0.75 0.25 1 !
47: CONST L12_FCC : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): L12_FCC, type code %AY, sha256 `e936330672baf793…`

~~~~text
41: PHASE L12_FCC %AY 3 0.75 0.25 1 !
42: CONST L12_FCC : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): L12_FCC, type code %A, sha256 `7532c7378b636d77…`

~~~~text
33: PHASE L12_FCC %A 2 0.75 0.25 !
34: CONST L12_FCC : AL NI% : AL% NI : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): L12_FCC, type code %AY, sha256 `38cb761434c46112…`

~~~~text
40: PHASE L12_FCC %AY 3 0.75 0.25 1 !
41: CONST L12_FCC : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): L12_FCC, type code %AY, sha256 `7b8304cf5f0be6a0…`

~~~~text
42: PHASE L12_FCC %AY 3 0.75 0.25 1 !
43: CONST L12_FCC : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-88Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-88Ans.tdb): L12_FCC, type code %A, sha256 `e3328a93ebedd45d…`

~~~~text
32: PHASE L12_FCC %A 2 0.75 0.25 !
33: CONST L12_FCC : AL NI% : AL% NI : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): L12_FCC, type code %AY, sha256 `476040576afa2e82…`

~~~~text
42: PHASE L12_FCC %AY 3 0.75 0.25 1 !
43: CONST L12_FCC : AL NI% : AL% NI : VA :  !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): L12_FCC, type code %AY, sha256 `41ccf30b100f6f25…`

~~~~text
47: PHASE L12_FCC %AY 3 0.75 0.25 1 !
48: CONST L12_FCC : AL NI% : AL% NI : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(88)90152-6](https://doi.org/10.1016/0001-6160%2888%2990152-6) I. Ansara, B. Sundman, P. Willemin, Thermodynamic modeling of ordered phases in the NiAl system, Acta Metallurgica 36, 977-982 (1988).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1515/zna-1987-1117](https://doi.org/10.1515/zna-1987-1117) K. Hilpert, D. Kobertz, V. Venugopal, M. Miller, H. Gerads, F. J. Bremer et al., Phase Diagram Studies on the Al- Ni System, Zeitschrift für Naturforschung A 42, 1327-1332 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0026-0800(84)90004-1](https://doi.org/10.1016/0026-0800%2884%2990004-1) I.M. Robertson, C.M. Wayman, Ni5Al3 and the nickel-aluminum binary phase diagram, Metallography 17, 43-55 (1984).  
_cited as the source of values for this phase_

## HCP_A3 (Al–Ni)

- Id: `phase:al-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 13 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:hcp-a3)

Names (14): _corpus: _corpus:phase:al-ni:hcp-a3  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:HCP_A3, tdb:AlNi-01Dup-4sl.tdb:HCP_A3, tdb:AlNi-01Dup-LB.tdb:HCP_A3, tdb:AlNi-01Dup-orig.tdb:HCP_A3, tdb:AlNi-03Sun.tdb:HCP_A3, tdb:AlNi-04Oht.tdb:HCP_A3, tdb:AlNi-05Mie.tdb:HCP_A3, tdb:AlNi-11Che.tdb:HCP_A3, tdb:AlNi-14Zhu.tdb:HCP_A3, tdb:AlNi-22Yan.tdb:HCP_A3, tdb:AlNi-88Ans.tdb:HCP_A3, tdb:AlNi-97Ans.tdb:HCP_A3, tdb:AlNi-98Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (13): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): HCP_A3, type code %A, sha256 `67b462ac7c6861a8…`

~~~~text
65: PHASE HCP_A3 %A 2 1 0.5 !
66: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): HCP_A3, type code %A, sha256 `de7e77f0f98a25d4…`

~~~~text
71: PHASE HCP_A3 %A 2 1 0.5 !
72: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): HCP_A3, type code %A, sha256 `f92c4694c34add59…`

~~~~text
66: PHASE HCP_A3 %A 2 1 0.5 !
67: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): HCP_A3, type code %A, sha256 `e936330672baf793…`

~~~~text
61: PHASE HCP_A3 %A 2 1 0.5 !
62: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): HCP_A3, type code %A, sha256 `b61858b6243ad431…`

~~~~text
73: PHASE HCP_A3 %A 2 1 0.5 !
74: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): HCP_A3, type code %A, sha256 `7532c7378b636d77…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): HCP_A3, type code %A, sha256 `3b6faf924a8dca5b…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): HCP_A3, type code %A, sha256 `38cb761434c46112…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): HCP_A3, type code %A, sha256 `7b8304cf5f0be6a0…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): HCP_A3, type code %A, sha256 `e71d9e3cf85a2ad2…`

~~~~text
61: PHASE HCP_A3 %A 2 1 0.5 !
62: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-88Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-88Ans.tdb): HCP_A3, type code %A, sha256 `e3328a93ebedd45d…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): HCP_A3, type code %A, sha256 `476040576afa2e82…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : AL NI : VA : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): HCP_A3, type code %A, sha256 `41ccf30b100f6f25…`

~~~~text
62: PHASE HCP_A3 %A 2 1 0.5 !
63: CONST HCP_A3 : AL NI : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(88)90152-6](https://doi.org/10.1016/0001-6160%2888%2990152-6) I. Ansara, B. Sundman, P. Willemin, Thermodynamic modeling of ordered phases in the NiAl system, Acta Metallurgica 36, 977-982 (1988).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_

## LIQUID (Al–Ni)

- Id: `phase:al-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 13 of 13 calculated diagram(s): 908.3–2500 K, x(Ni) 0–1
- Literature: 80 values (80 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ni:liquid)

Names (19): _corpus: _corpus:phase:al-ni:liquid  
_paper: _paper:10.1016/j.calphad.2005.02.002:L, paper:10.1016/j.intermet.2022.107647:L, paper:10.1016/j.tca.2010.10.005:L, paper:10.1016/s0966-9795(97)00099-x:L, paper:10.1361/105497199770340743:L  
_tdb: _tdb:AlNi-01Dup-4sl-old.tdb:LIQUID, tdb:AlNi-01Dup-4sl.tdb:LIQUID, tdb:AlNi-01Dup-LB.tdb:LIQUID, tdb:AlNi-01Dup-orig.tdb:LIQUID, tdb:AlNi-03Sun.tdb:LIQUID, tdb:AlNi-04Oht.tdb:LIQUID, tdb:AlNi-05Mie.tdb:LIQUID, tdb:AlNi-11Che.tdb:LIQUID, tdb:AlNi-14Zhu.tdb:LIQUID, tdb:AlNi-22Yan.tdb:LIQUID, tdb:AlNi-88Ans.tdb:LIQUID, tdb:AlNi-97Ans.tdb:LIQUID, tdb:AlNi-98Hua.tdb:LIQUID  


### TDB models of LIQUID (13): PHASE and CONSTITUENT statements as written

[AlNi-01Dup-4sl-old.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl-old.tdb): LIQUID, type code %, sha256 `67b462ac7c6861a8…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-01Dup-4sl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-4sl.tdb): LIQUID, type code %, sha256 `de7e77f0f98a25d4…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-01Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-LB.tdb): LIQUID, type code %, sha256 `f92c4694c34add59…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-01Dup-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-01Dup-orig.tdb): LIQUID, type code %, sha256 `e936330672baf793…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-03Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-03Sun.tdb): LIQUID, type code %, sha256 `b61858b6243ad431…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-04Oht.tdb): LIQUID, type code %, sha256 `7532c7378b636d77…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-05Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-05Mie.tdb): LIQUID, type code %, sha256 `3b6faf924a8dca5b…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-11Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-11Che.tdb): LIQUID, type code %, sha256 `38cb761434c46112…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-14Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-14Zhu.tdb): LIQUID, type code %, sha256 `7b8304cf5f0be6a0…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-22Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-22Yan.tdb): LIQUID, type code %, sha256 `e71d9e3cf85a2ad2…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-88Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-88Ans.tdb): LIQUID, type code %, sha256 `e3328a93ebedd45d…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-97Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-97Ans.tdb): LIQUID, type code %, sha256 `476040576afa2e82…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL NI : !
~~~~

[AlNi-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlNi-98Hua.tdb): LIQUID, type code %, sha256 `41ccf30b100f6f25…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : AL NI : !
~~~~

Example references (10 of 15; assessments first): 

- [doi:10.1016/j.calphad.2005.02.002](https://doi.org/10.1016/j.calphad.2005.02.002) Jyrki Miettinen, Thermodynamic description of the Cu–Al–Ni system at the Cu–Ni side, Calphad 29, 40-48 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.10.005](https://doi.org/10.1016/j.tca.2010.10.005) H.-L. Chen, E. Doernberg, P. Svoboda, R. Schmid-Fetzer, Thermodynamics of the Al3Ni phase and revision of the Al–Ni system, Thermochimica Acta 512, 189-195 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2022.107647](https://doi.org/10.1016/j.intermet.2022.107647) Wei Yang, Peisheng Wang, Xiaozhong Huang, Shuyan Zhang, Thermodynamic analysis of the Al–Ni system, Intermetallics 149, 107647 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(97)00099-X](https://doi.org/10.1016/S0966-9795%2897%2900099-X) W. Huang, Y.A. Chang, Intermet., 6, 487-98(1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00049-9](https://doi.org/10.1016/S0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Calphad, 25, 279-98(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, H.L. Lukas, B. Sundman, J. Alloys Compd., 247, 20-30(1997).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-014-0327-5](https://doi.org/10.1007/s11669-014-0327-5) J. Zhu, M. S. Titus, T. M. Pollock, Experimental Investigation and Thermodynamic Modeling of the Co-Rich Region in the Co-Al-Ni-W Quaternary System, J. Phase Equilib. Diffus. 35, 595-611 (2014).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(88)90152-6](https://doi.org/10.1016/0001-6160%2888%2990152-6) I. Ansara, B. Sundman, P. Willemin, Thermodynamic modeling of ordered phases in the NiAl system, Acta Metallurgica 36, 977-982 (1988).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1489](https://doi.org/10.2320/matertrans.45.1489) Hiroshi Ohtani, Ying Chen, Mitsuhiro Hasebe, Phase Separation of the B2 Structure Accompanied by an Ordering in Co-Al and Ni-Al Binary Systems, Mater. Trans. 45, 1489-1498 (2004).  
_assessment that models this phase_
- [doi:10.1515/zna-1987-1117](https://doi.org/10.1515/zna-1987-1117) K. Hilpert, D. Kobertz, V. Venugopal, M. Miller, H. Gerads, F. J. Bremer et al., Phase Diagram Studies on the Al- Ni System, Zeitschrift für Naturforschung A 42, 1327-1332 (1987).  
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
