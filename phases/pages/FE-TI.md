# Fe–Ti phases

> Fe–Ti system: 10 phases (tier A 7, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-TI.html · Markdown: https://data.orchid-project.org/phases/pages/FE-TI.md

10 phases (tier A 7, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-TI) · [full JSON](https://data.orchid-project.org/phases/systems/FE-TI.json) · [Fe–Ti system page](https://data.orchid-project.org/systems/FE-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Ti system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_4SL](#phase-fe-ti-bcc-4sl); _phase:fe-ti:bcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1780 K, x(Ti) 0.04–0.96 | 12 | 1 |
| [BCC_A2](#phase-fe-ti-bcc-a2); _phase:fe-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 15 of 25 calculated diagram(s): 300–2499.94 K, x(Ti) 0–1 | 182 | 25 |
| [B2_BCC](#phase-fe-ti-bcc-b2); _phase:fe-ti:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 7 of 8 calculated diagram(s): 300–2499.76 K, x(Ti) 0–1 | 63 | 8 |
| [C14_LAVES](#phase-fe-ti-c14-laves); _phase:fe-ti:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 14 of 15 calculated diagram(s): 300–1735.31 K, x(Ti) 0.2589–0.4128 | 107 | 15 |
| [FCC_4SL](#phase-fe-ti-fcc-4sl); _phase:fe-ti:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1172.46–1686.08 K, x(Ti) 0–0.00879 | 0 | 1 |
| [FCC_A1](#phase-fe-ti-fcc-a1); _phase:fe-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 15 of 17 calculated diagram(s): 939.83–1804.83 K, x(Ti) 0–0.01013 | 0 | 17 |
| [FE2TI_C14](#phase-fe-ti-fe2ti-c14); _phase:fe-ti:fe2ti-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1699.74 K, x(Ti) 0.26027–0.49993 | 41 | 3 |
| [FETI_B2](#phase-fe-ti-feti-b2); _phase:fe-ti:feti-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1608.99 K, x(Ti) 0.49594–0.52103 | 99 | 7 |
| [HCP_A3](#phase-fe-ti-hcp-a3); _phase:fe-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 15 of 16 calculated diagram(s): 300–1939.99 K, x(Ti) 0.99925–1 | 30 | 16 |
| [LIQUID](#phase-fe-ti-liquid); _phase:fe-ti:liquid_ | liquid | liquid | stable in 15 of 16 calculated diagram(s): 1335.77–2500 K, x(Ti) 0–1 | 256 | 16 |

## BCC_4SL (Fe–Ti)

- Id: `phase:fe-ti:bcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:FeTi-24Lia.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Pm-3m (221) — on-hull MP TiFe at x(TI)=0.5000
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP TiFe2 at x(TI)=0.3333
- Candidate (dft_oqmd): Cmmm (65) — on-hull OQMD Fe1 Ti1 at x(TI)=0.5000
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Fe1 Ti2 at x(TI)=0.6667
- Candidate (dft_oqmd): Fd-3m (227) — on-hull OQMD Fe2 Ti1 at x(TI)=0.3333
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Candidate (tdb_comment): CsCl · B2 · cP2, Pm-3m — FeTi-24Lia.tdb: 'Prototype CsCl (B2, cP2, Pm-3m), NaTl (B32, cF16, Fd-3m),'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1780 K, x(Ti) 0.04–0.96
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:bcc-4sl)

Names (4): _corpus: _corpus:phase:fe-ti:bcc-4sl  
_paper: _paper:10.1007/s11669-024-01124-9:BCC_4SL, paper:10.1007/s11669-024-01124-9:TiFe_B2  
_tdb: _tdb:FeTi-24Lia.tdb:BCC_4SL  


### TDB models of BCC_4SL (1): PHASE and CONSTITUENT statements as written

[FeTi-24Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-24Lia.tdb): BCC_4SL, type code %BO, sha256 `0a498e0d238a414e…`

~~~~text
54: PHASE BCC_4SL:B %BO 5 0.25 0.25 0.25 0.25 3 !
55: CONST BCC_4SL:B : FE TI VA : FE TI VA : FE TI VA : FE TI VA : VA% :  !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01124-9](https://doi.org/10.1007/s11669-024-01124-9) Zhi Liang, Ursula Kattner, Kamal Choudharry, Francesca Tavazza, Carelyn Campbell, Thermodynamic Assessments of Ti-Al, Ti-Fe, and Ti-Al-Fe Systems with Four-Sublattice Description of Ordered Body-Centered Cubic Phase and Density Functional Theory Data, J. Phase Equilib. Diffus. 45, 732-756 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2012.02.002](https://doi.org/10.1016/j.commatsci.2012.02.002) Stefano Curtarolo, Wahyu Setyawan, Shidong Wang, Junkai Xue, Kesong Yang, Richard H. Taylor et al., AFLOWLIB.ORG: A distributed materials properties repository from high-throughput ab initio calculations, Computational Materials Science 58, 227-235 (2012).  
_cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2014.05.014](https://doi.org/10.1016/j.commatsci.2014.05.014) Richard H. Taylor, Frisco Rose, Cormac Toher, Ohad Levy, Kesong Yang, Marco Buongiorno Nardelli et al., A RESTful API for exchanging materials data in the AFLOWLIB.org consortium, Computational Materials Science 93, 178-192 (2014).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2008.10.003](https://doi.org/10.1016/j.calphad.2008.10.003) Jozefien De Keyzer, Gabriele Cacciamani, Nathalie Dupin, Patrick Wollants, Thermodynamic modeling and optimization of the Fe–Ni–Ti system, Calphad 33, 109-123 (2009).  
_cited as the source of values for this phase_

## BCC_A2 (Fe–Ti)

- Id: `phase:fe-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 15 of 25 calculated diagram(s): 300–2499.94 K, x(Ti) 0–1
- Literature: 182 values (182 accepted) from 8 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:bcc-a2)

Names (42): _corpus: _corpus:phase:fe-ti:bcc-a2  
_paper: _paper:10.1007/s11663-998-0113-z:Bcc, paper:10.1007/s11663-998-0113-z:Bcc(Fe), paper:10.1007/s11663-998-0113-z:Bcc(Ti), paper:10.1007/s11669-024-01124-9:β-Fe, paper:10.1007/s11669-024-01124-9:β-Ti, paper:10.1016/0364-5916(94)90028-0:α, paper:10.1016/0364-5916(94)90028-0:ε, paper:10.1016/j.intermet.2020.106978:α-Fe, paper:10.1016/j.intermet.2020.106978:β-Ti, paper:10.1016/j.jallcom.2019.05.341:A2, paper:10.1016/j.matchemphys.2011.07.071:αFe, paper:10.1016/j.matchemphys.2011.07.071:βTi, paper:10.1016/s0364-5916(98)00037-6:bcc-A2, paper:10.1361/105497198770341923:bcc, paper:10.1361/105497198770341923:bcc(Fe), paper:10.1361/105497198770341923:bcc(Ti)  
_tdb: _tdb:FeTi-09Key.tdb:A2_BCC, tdb:FeTi-09Key.tdb:BCC_A2, tdb:FeTi-11Wan.tdb:BCC_A2, tdb:FeTi-12Bo.tdb:A2_BCC, tdb:FeTi-12Bo.tdb:BCC_A2, tdb:FeTi-12Guo.tdb:A2_BCC, tdb:FeTi-12Guo.tdb:BCC_A2, tdb:FeTi-19Wit.tdb:A2_BCC, tdb:FeTi-19Wit.tdb:BCC_A2, tdb:FeTi-21San.tdb:A2_BCC, tdb:FeTi-21San.tdb:BCC_A2, tdb:FeTi-21Zha.tdb:A2_BCC, tdb:FeTi-21Zha.tdb:BCC_A2, tdb:FeTi-22Kri.tdb:BCC_A2, tdb:FeTi-23Wal-3g.tdb:A2_BCC, tdb:FeTi-23Wal-3g.tdb:BCC_A2, tdb:FeTi-24Lia.tdb:A2_BCC, tdb:FeTi-24Lia.tdb:BCC_A2, tdb:FeTi-89Bal.tdb:BCC_A2, tdb:FeTi-94Har.tdb:BCC_A2, tdb:FeTi-98Dum.tdb:BCC_A2, tdb:FeTi-98Har-LB.tdb:A2_BCC, tdb:FeTi-98Har-LB.tdb:BCC_A2, tdb:FeTi-98Jon.tdb:BCC_A2, tdb:FeTi-98Ran.tdb:BCC_A2  


### TDB models of BCC_A2 (25): PHASE and CONSTITUENT statements as written

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): A2_BCC, type code %B, sha256 `1ea2428706857b8b…`

~~~~text
55: PHASE A2_BCC %B 2 1 3 !
56: CONST A2_BCC : FE TI : VA : !
~~~~

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): BCC_A2, type code %B, sha256 `1ea2428706857b8b…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-11Wan.tdb): BCC_A2, type code %B, sha256 `29487a21dbf9915b…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): A2_BCC, type code %B, sha256 `183add95bfc32e46…`

~~~~text
50: PHASE A2_BCC %B 2 1 3 !
51: CONST A2_BCC : FE TI : VA : !
~~~~

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): BCC_A2, type code %B, sha256 `183add95bfc32e46…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Guo.tdb): A2_BCC, type code %B, sha256 `47ca15461ab905b4…`

~~~~text
38: PHASE A2_BCC %B 2 1 3 !
39: CONST A2_BCC : FE TI : VA : !
~~~~

[FeTi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Guo.tdb): BCC_A2, type code %B, sha256 `47ca15461ab905b4…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-19Wit.tdb): A2_BCC, type code %B, sha256 `20ca15b772842baa…`

~~~~text
44: PHASE A2_BCC %B 2 1 3 !
45: CONST A2_BCC : FE TI : VA : !
~~~~

[FeTi-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-19Wit.tdb): BCC_A2, type code %B, sha256 `20ca15b772842baa…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): A2_BCC, type code %B, sha256 `34a1c0676e8eed2a…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : FE TI : VA : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): BCC_A2, type code %B, sha256 `34a1c0676e8eed2a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21Zha.tdb): A2_BCC, type code %B, sha256 `de527885390e9a9d…`

~~~~text
43: PHASE A2_BCC %B 2 1 3 !
44: CONST A2_BCC : FE TI : VA : !
~~~~

[FeTi-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21Zha.tdb): BCC_A2, type code %B, sha256 `de527885390e9a9d…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-22Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-22Kri.tdb): BCC_A2, type code %B, sha256 `7d978f1075f96b7f…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-23Wal-3g.tdb): A2_BCC, type code %B, sha256 `eb27ebd8890d3aea…`

~~~~text
49: PHASE A2_BCC %B 2 1 3 !
50: CONST A2_BCC : FE TI : VA : !
~~~~

[FeTi-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-23Wal-3g.tdb): BCC_A2, type code %B, sha256 `eb27ebd8890d3aea…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-24Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-24Lia.tdb): A2_BCC, type code %B, sha256 `0a498e0d238a414e…`

~~~~text
48: PHASE A2_BCC %B 2 1 3 !
49: CONST A2_BCC : FE TI VA : VA : !
~~~~

[FeTi-24Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-24Lia.tdb): BCC_A2, type code %B, sha256 `0a498e0d238a414e…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : FE% TI% VA : VA : !
~~~~

[FeTi-89Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-89Bal.tdb): BCC_A2, type code %B, sha256 `960a05a577d637ea…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-94Har.tdb): BCC_A2, type code %B, sha256 `89d365c4c3215e59…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-98Dum.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Dum.tdb): BCC_A2, type code %B, sha256 `16241d492de1e8a2…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-98Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Har-LB.tdb): A2_BCC, type code %B, sha256 `8b57368794e5504f…`

~~~~text
46: PHASE A2_BCC %B 2 1 3 !
47: CONST A2_BCC : FE TI VA : VA : !
~~~~

[FeTi-98Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Har-LB.tdb): BCC_A2, type code %B, sha256 `8b57368794e5504f…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-98Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Jon.tdb): BCC_A2, type code %B, sha256 `d6efa66564a03f46…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% TI% : VA : !
~~~~

[FeTi-98Ran.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Ran.tdb): BCC_A2, type code %B, sha256 `72430ad2c2591dea…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% TI% : VA : !
~~~~

Example references (10 of 17; assessments first): 

- [doi:10.1361/105497198770341923](https://doi.org/10.1361/105497198770341923) L. F. S. Dumitrescu, M. Hillert, N. Sounders, Comparison of Fe-Ti assessments, JPE 19, 441-448 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11663-998-0113-z](https://doi.org/10.1007/s11663-998-0113-z) Stefan Jonsson, Assessment of the Fe-Ti system, Metall Mater Trans B 29, 361-370 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90028-0](https://doi.org/10.1016/0364-5916%2894%2990028-0) K.C.Hari Kumar, P. Wollaiits, L. Delaey, Thermodynamic reassessment and calculation of FeTi phase diagram, Calphad 18, 223-234 (1994).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2011.07.071](https://doi.org/10.1016/j.matchemphys.2011.07.071) C.P. Wang, J.P. Zheng, Y. Yu, H.F. Hu, X.J. Liu, Experimental investigation and thermodynamic calculation of the phase equilibria in the Fe–Nb–Ti ternary system, Materials Chemistry and Physics 130, 806-814 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2020.106978](https://doi.org/10.1016/j.intermet.2020.106978) K. Santhy, K.C. Hari Kumar, Thermodynamic modelling of magnetic laves phase in Fe–Ti system using first principle method, Intermetallics 128, 106978 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S1003-6326(11)61450-7](https://doi.org/10.1016/S1003-6326%2811%2961450-7) H. Bo, J. Wang, L. Duarte, C. Leinenbach, L. Liu, H. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 22, 2204-11(2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-024-01124-9](https://doi.org/10.1007/s11669-024-01124-9) Zhi Liang, Ursula Kattner, Kamal Choudharry, Francesca Tavazza, Carelyn Campbell, Thermodynamic Assessments of Ti-Al, Ti-Fe, and Ti-Al-Fe Systems with Four-Sublattice Description of Ordered Body-Centered Cubic Phase and Density Functional Theory Data, J. Phase Equilib. Diffus. 45, 732-756 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00889-7](https://doi.org/10.1007/s11669-021-00889-7) G. Zhang, W. Zheng, Z. Zhao, Y. He, Z. Zheng, D. Tang, J. Phase Equilib. Diffus., 42, 363-72(2021).  
_assessment that models this phase_

## B2_BCC (Fe–Ti)

- Id: `phase:fe-ti:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: FeTi-09Key.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeTi-12Bo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeTi-12Guo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeTi-19Wit.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeTi-21San.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeTi-21Zha.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeTi-23Wal-3g.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeTi-98Har-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in FeTi-09Key.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-12Bo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-12Guo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-19Wit.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-21San.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-21Zha.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-23Wal-3g.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-98Har-LB.tdb also describes the disordered state
- Stability: stable in 7 of 8 calculated diagram(s): 300–2499.76 K, x(Ti) 0–1
- Literature: 63 values (63 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:bcc-b2)

Names (13): _corpus: _corpus:phase:fe-ti:bcc-b2, corpus:phase:fe-ti:b2-bcc  
_paper: _paper:10.1016/j.intermet.2020.106978:FeTi, paper:10.1016/j.jallcom.2019.05.341:B2, paper:10.1016/s1003-6326(11)61450-7:FeTi  
_tdb: _tdb:FeTi-09Key.tdb:B2_BCC, tdb:FeTi-12Bo.tdb:B2_BCC, tdb:FeTi-12Guo.tdb:B2_BCC, tdb:FeTi-19Wit.tdb:B2_BCC, tdb:FeTi-21San.tdb:B2_BCC, tdb:FeTi-21Zha.tdb:B2_BCC, tdb:FeTi-23Wal-3g.tdb:B2_BCC, tdb:FeTi-98Har-LB.tdb:B2_BCC  


### TDB models of B2_BCC (8): PHASE and CONSTITUENT statements as written

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): B2_BCC, type code %BO, sha256 `1ea2428706857b8b…`

~~~~text
60: PHASE B2_BCC %BO 3 0.5 0.5 3 !
61: CONST B2_BCC : FE% TI : FE TI% : VA : !
~~~~

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): B2_BCC, type code %BO, sha256 `183add95bfc32e46…`

~~~~text
55: PHASE B2_BCC %BO 3 0.5 0.5 3 !
56: CONST B2_BCC : FE% TI : FE TI% : VA : !
~~~~

[FeTi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Guo.tdb): B2_BCC, type code %BO, sha256 `47ca15461ab905b4…`

~~~~text
43: PHASE B2_BCC %BO 3 0.5 0.5 3 !
44: CONST B2_BCC : FE% TI : FE TI% : VA : !
~~~~

[FeTi-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-19Wit.tdb): B2_BCC, type code %BO, sha256 `20ca15b772842baa…`

~~~~text
49: PHASE B2_BCC %BO 3 0.5 0.5 3 !
50: CONST B2_BCC : FE% TI : FE TI% : VA : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): B2_BCC, type code %BO, sha256 `34a1c0676e8eed2a…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : FE% TI : FE TI% : VA : !
~~~~

[FeTi-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21Zha.tdb): B2_BCC, type code %BO, sha256 `de527885390e9a9d…`

~~~~text
48: PHASE B2_BCC %BO 3 0.5 0.5 3 !
49: CONST B2_BCC : FE% TI : FE TI% : VA : !
~~~~

[FeTi-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-23Wal-3g.tdb): B2_BCC, type code %BO, sha256 `eb27ebd8890d3aea…`

~~~~text
54: PHASE B2_BCC %BO 3 0.5 0.5 3 !
55: CONST B2_BCC : FE% TI : FE TI% : VA : !
~~~~

[FeTi-98Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Har-LB.tdb): B2_BCC, type code %BO, sha256 `8b57368794e5504f…`

~~~~text
51: PHASE B2_BCC %BO 3 0.5 0.5 3 !
52: CONST B2_BCC : FE% TI VA : FE TI% VA : VA : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2020.106978](https://doi.org/10.1016/j.intermet.2020.106978) K. Santhy, K.C. Hari Kumar, Thermodynamic modelling of magnetic laves phase in Fe–Ti system using first principle method, Intermetallics 128, 106978 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)61450-7](https://doi.org/10.1016/S1003-6326%2811%2961450-7) H. Bo, J. Wang, L. Duarte, C. Leinenbach, L. Liu, H. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 22, 2204-11(2012).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-021-00889-7](https://doi.org/10.1007/s11669-021-00889-7) G. Zhang, W. Zheng, Z. Zhao, Y. He, Z. Zheng, D. Tang, J. Phase Equilib. Diffus., 42, 363-72(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_
- [doi:10.1007/bf02868286](https://doi.org/10.1007/bf02868286) J.L. Murray, The FeTi (IroneTitanium) system, Bull. Alloy Phase Diagr. 2 (1981) 320e334.  
_cited as the source of values for this phase_
- [doi:10.1007/s11663-998-0113-z](https://doi.org/10.1007/s11663-998-0113-z) Stefan Jonsson, Assessment of the Fe-Ti system, Metall Mater Trans B 29, 361-370 (1998).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(94)90028-0](https://doi.org/10.1016/0364-5916%2894%2990028-0) K.C.Hari Kumar, P. Wollaiits, L. Delaey, Thermodynamic reassessment and calculation of FeTi phase diagram, Calphad 18, 223-234 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/j.matchemphys.2011.07.071](https://doi.org/10.1016/j.matchemphys.2011.07.071) C.P. Wang, J.P. Zheng, Y. Yu, H.F. Hu, X.J. Liu, Experimental investigation and thermodynamic calculation of the phase equilibria in the Fe–Nb–Ti ternary system, Materials Chemistry and Physics 130, 806-814 (2011).  
_cited as the source of values for this phase_

## C14_LAVES (Fe–Ti)

- Id: `phase:fe-ti:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeTi-09Key.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-11Wan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-12Bo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-12Guo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-19Wit.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-21San.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-21Zha.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-22Kri.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-23Wal-3g.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-24Lia.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-98Dum.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-98Har-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-98Jon.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-98Ran.tdb also describes the disordered state
- Stability: stable in 14 of 15 calculated diagram(s): 300–1735.31 K, x(Ti) 0.2589–0.4128
- Literature: 107 values (107 accepted) from 6 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:c14-laves)

Names (22): _corpus: _corpus:phase:fe-ti:c14-laves  
_paper: _paper:10.1007/s11663-998-0113-z:Fe2Ti, paper:10.1007/s11669-024-01124-9:C14, paper:10.1016/j.jallcom.2019.05.341:C14, paper:10.1016/j.matchemphys.2011.07.071:Fe2Ti, paper:10.1016/s0364-5916(98)00037-6:Laves-C14, paper:10.1361/105497198770341923:Fe2Ti  
_tdb: _tdb:FeTi-09Key.tdb:C14_LAVES, tdb:FeTi-11Wan.tdb:C14_LAVES, tdb:FeTi-12Bo.tdb:C14_LAVES, tdb:FeTi-12Guo.tdb:C14_LAVES, tdb:FeTi-19Wit.tdb:C14_LAVES, tdb:FeTi-21San.tdb:C14_LAVES, tdb:FeTi-21Zha.tdb:C14_LAVES, tdb:FeTi-22Kri.tdb:C14_LAVES, tdb:FeTi-23Wal-3g.tdb:C14_LAVES, tdb:FeTi-24Lia.tdb:C14_LAVES, tdb:FeTi-89Bal.tdb:C14_LAVES, tdb:FeTi-98Dum.tdb:C14_LAVES, tdb:FeTi-98Har-LB.tdb:C14_LAVES, tdb:FeTi-98Jon.tdb:C14_LAVES, tdb:FeTi-98Ran.tdb:C14_LAVES  


### TDB models of C14_LAVES (15): PHASE and CONSTITUENT statements as written

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): C14_LAVES, type code %, sha256 `1ea2428706857b8b…`

~~~~text
70: PHASE C14_LAVES % 3 2 3 1 !
71: CONST C14_LAVES : FE TI% : FE% TI : FE% TI : !
~~~~

[FeTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-11Wan.tdb): C14_LAVES, type code %, sha256 `29487a21dbf9915b…`

~~~~text
48: PHASE C14_LAVES % 2 2 1 !
49: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): C14_LAVES, type code %, sha256 `183add95bfc32e46…`

~~~~text
65: PHASE C14_LAVES % 2 2 1 !
66: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Guo.tdb): C14_LAVES, type code %, sha256 `47ca15461ab905b4…`

~~~~text
53: PHASE C14_LAVES % 2 2 1 !
54: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-19Wit.tdb): C14_LAVES, type code %, sha256 `20ca15b772842baa…`

~~~~text
59: PHASE C14_LAVES % 2 2 1 !
60: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): C14_LAVES, type code %A, sha256 `34a1c0676e8eed2a…`

~~~~text
55: PHASE C14_LAVES %A 2 2 1 !
56: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21Zha.tdb): C14_LAVES, type code %, sha256 `de527885390e9a9d…`

~~~~text
58: PHASE C14_LAVES % 2 2 1 !
59: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-22Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-22Kri.tdb): C14_LAVES, type code %, sha256 `7d978f1075f96b7f…`

~~~~text
47: PHASE C14_LAVES % 2 2 1 !
48: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-23Wal-3g.tdb): C14_LAVES, type code %A, sha256 `eb27ebd8890d3aea…`

~~~~text
64: PHASE C14_LAVES %A 3 0.16667 0.33333 0.5 !
65: CONST C14_LAVES : FE% TI : FE TI% : FE% TI : !
~~~~

[FeTi-24Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-24Lia.tdb): C14_LAVES, type code %A, sha256 `0a498e0d238a414e…`

~~~~text
64: PHASE C14_LAVES %A 3 1 1.5 0.5 !
65: CONST C14_LAVES : FE TI% : FE% TI : FE% TI : !
~~~~

[FeTi-89Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-89Bal.tdb): C14_LAVES, type code %, sha256 `960a05a577d637ea…`

~~~~text
52: PHASE C14_LAVES % 2 2 1 !
53: CONST C14_LAVES : FE : TI : !
~~~~

[FeTi-98Dum.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Dum.tdb): C14_LAVES, type code %, sha256 `16241d492de1e8a2…`

~~~~text
53: PHASE C14_LAVES % 2 2 1 !
54: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-98Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Har-LB.tdb): C14_LAVES, type code %, sha256 `8b57368794e5504f…`

~~~~text
61: PHASE C14_LAVES % 2 2 1 !
62: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

[FeTi-98Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Jon.tdb): C14_LAVES, type code %, sha256 `d6efa66564a03f46…`

~~~~text
50: PHASE C14_LAVES % 3 2 4 6 !
51: CONST C14_LAVES : FE% TI : FE TI% : FE : !
~~~~

[FeTi-98Ran.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Ran.tdb): C14_LAVES, type code %, sha256 `72430ad2c2591dea…`

~~~~text
47: PHASE C14_LAVES % 2 2 1 !
48: CONST C14_LAVES : FE% TI : FE TI% : !
~~~~

Example references (10 of 19; assessments first): 

- [doi:10.1361/105497198770341923](https://doi.org/10.1361/105497198770341923) L. F. S. Dumitrescu, M. Hillert, N. Sounders, Comparison of Fe-Ti assessments, JPE 19, 441-448 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11663-998-0113-z](https://doi.org/10.1007/s11663-998-0113-z) Stefan Jonsson, Assessment of the Fe-Ti system, Metall Mater Trans B 29, 361-370 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2011.07.071](https://doi.org/10.1016/j.matchemphys.2011.07.071) C.P. Wang, J.P. Zheng, Y. Yu, H.F. Hu, X.J. Liu, Experimental investigation and thermodynamic calculation of the phase equilibria in the Fe–Nb–Ti ternary system, Materials Chemistry and Physics 130, 806-814 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S1003-6326(11)61450-7](https://doi.org/10.1016/S1003-6326%2811%2961450-7) H. Bo, J. Wang, L. Duarte, C. Leinenbach, L. Liu, H. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 22, 2204-11(2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-024-01124-9](https://doi.org/10.1007/s11669-024-01124-9) Zhi Liang, Ursula Kattner, Kamal Choudharry, Francesca Tavazza, Carelyn Campbell, Thermodynamic Assessments of Ti-Al, Ti-Fe, and Ti-Al-Fe Systems with Four-Sublattice Description of Ordered Body-Centered Cubic Phase and Density Functional Theory Data, J. Phase Equilib. Diffus. 45, 732-756 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00889-7](https://doi.org/10.1007/s11669-021-00889-7) G. Zhang, W. Zheng, Z. Zhao, Y. He, Z. Zheng, D. Tang, J. Phase Equilib. Diffus., 42, 363-72(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102383](https://doi.org/10.1016/j.calphad.2021.102383) M.J. Kriegel, M.H. Wetzel, O. Fabrichnaya, D. Rafaja, Calphad, 76, 102383(2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_

## FCC_4SL (Fe–Ti)

- Id: `phase:fe-ti:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:FeTi-09Key.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — FeTi-09Key.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Stability: stable in 1 of 1 calculated diagram(s): 1172.46–1686.08 K, x(Ti) 0–0.00879
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:fcc-4sl)

Names (2): _corpus: _corpus:phase:fe-ti:fcc-4sl  
_tdb: _tdb:FeTi-09Key.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): FCC_4SL, type code %AY, sha256 `1ea2428706857b8b…`

~~~~text
45: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
46: CONST FCC_4SL:F : FE TI : FE TI : FE TI : FE TI : VA :  !
~~~~

## FCC_A1 (Fe–Ti)

- Id: `phase:fe-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 15 of 17 calculated diagram(s): 939.83–1804.83 K, x(Ti) 0–0.01013
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:fcc-a1)

Names (18): _corpus: _corpus:phase:fe-ti:fcc-a1  
_tdb: _tdb:FeTi-09Key.tdb:A1_FCC, tdb:FeTi-09Key.tdb:FCC_A1, tdb:FeTi-11Wan.tdb:FCC_A1, tdb:FeTi-12Bo.tdb:FCC_A1, tdb:FeTi-12Guo.tdb:FCC_A1, tdb:FeTi-19Wit.tdb:FCC_A1, tdb:FeTi-21San.tdb:FCC_A1, tdb:FeTi-21Zha.tdb:FCC_A1, tdb:FeTi-22Kri.tdb:FCC_A1, tdb:FeTi-23Wal-3g.tdb:FCC_A1, tdb:FeTi-24Lia.tdb:FCC_A1, tdb:FeTi-89Bal.tdb:FCC_A1, tdb:FeTi-94Har.tdb:FCC_A1, tdb:FeTi-98Dum.tdb:FCC_A1, tdb:FeTi-98Har-LB.tdb:FCC_A1, tdb:FeTi-98Jon.tdb:FCC_A1, tdb:FeTi-98Ran.tdb:FCC_A1  


### TDB models of FCC_A1 (17): PHASE and CONSTITUENT statements as written

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): A1_FCC, type code %A, sha256 `1ea2428706857b8b…`

~~~~text
40: PHASE A1_FCC %A 2 1 1 !
41: CONST A1_FCC : FE% TI : VA : !
~~~~

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): FCC_A1, type code %A, sha256 `1ea2428706857b8b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-11Wan.tdb): FCC_A1, type code %A, sha256 `29487a21dbf9915b…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): FCC_A1, type code %A, sha256 `183add95bfc32e46…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Guo.tdb): FCC_A1, type code %A, sha256 `47ca15461ab905b4…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-19Wit.tdb): FCC_A1, type code %A, sha256 `20ca15b772842baa…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): FCC_A1, type code %A, sha256 `34a1c0676e8eed2a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21Zha.tdb): FCC_A1, type code %A, sha256 `de527885390e9a9d…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-22Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-22Kri.tdb): FCC_A1, type code %A, sha256 `7d978f1075f96b7f…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-23Wal-3g.tdb): FCC_A1, type code %A, sha256 `eb27ebd8890d3aea…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-24Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-24Lia.tdb): FCC_A1, type code %A, sha256 `0a498e0d238a414e…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-89Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-89Bal.tdb): FCC_A1, type code %A, sha256 `960a05a577d637ea…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-94Har.tdb): FCC_A1, type code %A, sha256 `89d365c4c3215e59…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-98Dum.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Dum.tdb): FCC_A1, type code %A, sha256 `16241d492de1e8a2…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-98Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Har-LB.tdb): FCC_A1, type code %A, sha256 `8b57368794e5504f…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-98Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Jon.tdb): FCC_A1, type code %A, sha256 `d6efa66564a03f46…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% TI : VA : !
~~~~

[FeTi-98Ran.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Ran.tdb): FCC_A1, type code %A, sha256 `72430ad2c2591dea…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% TI : VA : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s11663-998-0113-z](https://doi.org/10.1007/s11663-998-0113-z) Stefan Jonsson, Assessment of the Fe-Ti system, Metall Mater Trans B 29, 361-370 (1998).  
_assessment that models this phase_
- [doi:10.1007/s11669-021-00889-7](https://doi.org/10.1007/s11669-021-00889-7) G. Zhang, W. Zheng, Z. Zhao, Y. He, Z. Zheng, D. Tang, J. Phase Equilib. Diffus., 42, 363-72(2021).  
_assessment that models this phase_
- [doi:10.1007/s11669-024-01124-9](https://doi.org/10.1007/s11669-024-01124-9) Zhi Liang, Ursula Kattner, Kamal Choudharry, Francesca Tavazza, Carelyn Campbell, Thermodynamic Assessments of Ti-Al, Ti-Fe, and Ti-Al-Fe Systems with Four-Sublattice Description of Ordered Body-Centered Cubic Phase and Density Functional Theory Data, J. Phase Equilib. Diffus. 45, 732-756 (2024).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90028-0](https://doi.org/10.1016/0364-5916%2894%2990028-0) K.C.Hari Kumar, P. Wollaiits, L. Delaey, Thermodynamic reassessment and calculation of FeTi phase diagram, Calphad 18, 223-234 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102383](https://doi.org/10.1016/j.calphad.2021.102383) M.J. Kriegel, M.H. Wetzel, O. Fabrichnaya, D. Rafaja, Calphad, 76, 102383(2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2020.106978](https://doi.org/10.1016/j.intermet.2020.106978) K. Santhy, K.C. Hari Kumar, Thermodynamic modelling of magnetic laves phase in Fe–Ti system using first principle method, Intermetallics 128, 106978 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.matchemphys.2011.07.071](https://doi.org/10.1016/j.matchemphys.2011.07.071) C.P. Wang, J.P. Zheng, Y. Yu, H.F. Hu, X.J. Liu, Experimental investigation and thermodynamic calculation of the phase equilibria in the Fe–Nb–Ti ternary system, Materials Chemistry and Physics 130, 806-814 (2011).  
_assessment that models this phase_

## FE2TI_C14 (Fe–Ti)

- Id: `phase:fe-ti:fe2ti-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeTi-12Bo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-21San.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1699.74 K, x(Ti) 0.26027–0.49993
- Literature: 41 values (41 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:fe2ti-c14)

Names (7): _corpus: _corpus:phase:fe-ti:fe2ti-c14  
_paper: _paper:10.1016/0364-5916(94)90028-0:λ, paper:10.1016/j.intermet.2020.106978:Fe2Ti, paper:10.1016/s1003-6326(11)61450-7:Fe2Ti  
_tdb: _tdb:FeTi-12Bo.tdb:FE2TI_C14, tdb:FeTi-21San.tdb:FE2TI_C14, tdb:FeTi-94Har.tdb:FE2TI_C14  


### TDB models of FE2TI_C14 (3): PHASE and CONSTITUENT statements as written

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): FE2TI_C14, type code %, sha256 `183add95bfc32e46…`

~~~~text
70: PHASE FE2TI_C14 % 2 2 1 !
71: CONST FE2TI_C14 : FE% TI : FE TI% : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): FE2TI_C14, type code %A, sha256 `34a1c0676e8eed2a…`

~~~~text
60: PHASE FE2TI_C14 %A 3 0.5 1 1.5 !
61: CONST FE2TI_C14 : FE% TI : FE TI% : FE : !
~~~~

[FeTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-94Har.tdb): FE2TI_C14, type code %, sha256 `89d365c4c3215e59…`

~~~~text
40: PHASE FE2TI_C14 % 3 2 4 6 !
41: CONST FE2TI_C14 : FE% VA : FE TI% : FE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(94)90028-0](https://doi.org/10.1016/0364-5916%2894%2990028-0) K.C.Hari Kumar, P. Wollaiits, L. Delaey, Thermodynamic reassessment and calculation of FeTi phase diagram, Calphad 18, 223-234 (1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)61450-7](https://doi.org/10.1016/S1003-6326%2811%2961450-7) H. Bo, J. Wang, L. Duarte, C. Leinenbach, L. Liu, H. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 22, 2204-11(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2020.106978](https://doi.org/10.1016/j.intermet.2020.106978) K. Santhy, K.C. Hari Kumar, Thermodynamic modelling of magnetic laves phase in Fe–Ti system using first principle method, Intermetallics 128, 106978 (2021).  
_assessment that models this phase; reports values for this phase_

## FETI_B2 (Fe–Ti)

- Id: `phase:fe-ti:feti-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeTi-11Wan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeTi-22Kri.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 300–1608.99 K, x(Ti) 0.49594–0.52103
- Literature: 99 values (99 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:feti-b2)

Names (13): _corpus: _corpus:phase:fe-ti:feti-b2  
_paper: _paper:10.1007/s11663-998-0113-z:FeTi, paper:10.1016/0364-5916(94)90028-0:FeTi, paper:10.1016/j.matchemphys.2011.07.071:FeTi, paper:10.1016/s0364-5916(98)00037-6:FeTi\*, paper:10.1361/105497198770341923:FeTi  
_tdb: _tdb:FeTi-11Wan.tdb:FETI_B2, tdb:FeTi-22Kri.tdb:FETI_B2, tdb:FeTi-89Bal.tdb:FETI_B2, tdb:FeTi-94Har.tdb:FETI_B2, tdb:FeTi-98Dum.tdb:FETI_B2, tdb:FeTi-98Jon.tdb:FETI_B2, tdb:FeTi-98Ran.tdb:FETI_B2  


### TDB models of FETI_B2 (7): PHASE and CONSTITUENT statements as written

[FeTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-11Wan.tdb): FETI_B2, type code %B, sha256 `29487a21dbf9915b…`

~~~~text
53: PHASE FETI_B2 %B 3 0.5 0.5 3 !
54: CONST FETI_B2 : FE% TI : FE TI% : VA : !
~~~~

[FeTi-22Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-22Kri.tdb): FETI_B2, type code %, sha256 `7d978f1075f96b7f…`

~~~~text
52: PHASE FETI_B2 % 2 1 1 !
53: CONST FETI_B2 : FE% TI : FE TI% : !
~~~~

[FeTi-89Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-89Bal.tdb): FETI_B2, type code %, sha256 `960a05a577d637ea…`

~~~~text
47: PHASE FETI_B2 % 2 1 1 !
48: CONST FETI_B2 : FE : TI : !
~~~~

[FeTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-94Har.tdb): FETI_B2, type code %, sha256 `89d365c4c3215e59…`

~~~~text
45: PHASE FETI_B2 % 2 1 1 !
46: CONST FETI_B2 : FE : TI : !
~~~~

[FeTi-98Dum.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Dum.tdb): FETI_B2, type code %, sha256 `16241d492de1e8a2…`

~~~~text
48: PHASE FETI_B2 % 2 1 1 !
49: CONST FETI_B2 : FE : TI : !
~~~~

[FeTi-98Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Jon.tdb): FETI_B2, type code %, sha256 `d6efa66564a03f46…`

~~~~text
45: PHASE FETI_B2 % 2 1 1 !
46: CONST FETI_B2 : FE : TI : !
~~~~

[FeTi-98Ran.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Ran.tdb): FETI_B2, type code %, sha256 `72430ad2c2591dea…`

~~~~text
42: PHASE FETI_B2 % 2 1 1 !
43: CONST FETI_B2 : FE : TI : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1361/105497198770341923](https://doi.org/10.1361/105497198770341923) L. F. S. Dumitrescu, M. Hillert, N. Sounders, Comparison of Fe-Ti assessments, JPE 19, 441-448 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90028-0](https://doi.org/10.1016/0364-5916%2894%2990028-0) K.C.Hari Kumar, P. Wollaiits, L. Delaey, Thermodynamic reassessment and calculation of FeTi phase diagram, Calphad 18, 223-234 (1994).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11663-998-0113-z](https://doi.org/10.1007/s11663-998-0113-z) Stefan Jonsson, Assessment of the Fe-Ti system, Metall Mater Trans B 29, 361-370 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2011.07.071](https://doi.org/10.1016/j.matchemphys.2011.07.071) C.P. Wang, J.P. Zheng, Y. Yu, H.F. Hu, X.J. Liu, Experimental investigation and thermodynamic calculation of the phase equilibria in the Fe–Nb–Ti ternary system, Materials Chemistry and Physics 130, 806-814 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102383](https://doi.org/10.1016/j.calphad.2021.102383) M.J. Kriegel, M.H. Wetzel, O. Fabrichnaya, D. Rafaja, Calphad, 76, 102383(2022).  
_assessment that models this phase_
- [doi:10.1007/bf02868286](https://doi.org/10.1007/bf02868286) J.L. Murray, The FeTi (IroneTitanium) system, Bull. Alloy Phase Diagr. 2 (1981) 320e334.  
_cited as the source of values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1016/0001-6160(55)90038-9](https://doi.org/10.1016/0001-6160%2855%2990038-9) O Kubaschewski, W.A Dench, The heats of formation in the systems titanium-aluminium and titanium-iron, Acta Metallurgica 3, 339-346 (1955).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)87031-1](https://doi.org/10.1016/0040-6031%2881%2987031-1) J.C. Gachon, M. Notin, J. Hertz, The enthalphy of mixing of the intermediate phases in the systems FeTi, CoTi, and NiTi by direct reaction calorimetry, Thermochimica Acta 48, 155-164 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(83)90024-x](https://doi.org/10.1016/0364-5916%2883%2990024-x) J.C. Gachon, Enthalpies of formation of binary phases in the systems FeTi, FeZr, CoTi, CoZr, NiTi, and NiZr, by direct reaction calorimetry, Calphad (1983).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Ti)

- Id: `phase:fe-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 15 of 16 calculated diagram(s): 300–1939.99 K, x(Ti) 0.99925–1
- Literature: 30 values (30 accepted) from 8 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:hcp-a3)

Names (25): _corpus: _corpus:phase:fe-ti:hcp-a3  
_paper: _paper:10.1007/s11663-998-0113-z:Hcp(Ti), paper:10.1007/s11669-024-01124-9:α-Ti, paper:10.1016/j.intermet.2020.106978:α-Ti, paper:10.1016/j.jallcom.2019.05.341:A3, paper:10.1016/j.matchemphys.2011.07.071:αTi, paper:10.1016/s0364-5916(98)00037-6:hcp-A3, paper:10.1016/s1003-6326(11)61450-7:HCP_Ti, paper:10.1361/105497198770341923:cph(Ti)  
_tdb: _tdb:FeTi-09Key.tdb:HCP_A3, tdb:FeTi-11Wan.tdb:HCP_A3, tdb:FeTi-12Bo.tdb:HCP_A3, tdb:FeTi-12Guo.tdb:HCP_A3, tdb:FeTi-19Wit.tdb:HCP_A3, tdb:FeTi-21San.tdb:HCP_A3, tdb:FeTi-21Zha.tdb:HCP_A3, tdb:FeTi-22Kri.tdb:HCP_A3, tdb:FeTi-23Wal-3g.tdb:HCP_A3, tdb:FeTi-24Lia.tdb:HCP_A3, tdb:FeTi-89Bal.tdb:HCP_A3, tdb:FeTi-94Har.tdb:HCP_A3, tdb:FeTi-98Dum.tdb:HCP_A3, tdb:FeTi-98Har-LB.tdb:HCP_A3, tdb:FeTi-98Jon.tdb:HCP_A3, tdb:FeTi-98Ran.tdb:HCP_A3  


### TDB models of HCP_A3 (16): PHASE and CONSTITUENT statements as written

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): HCP_A3, type code %A, sha256 `1ea2428706857b8b…`

~~~~text
65: PHASE HCP_A3 %A 2 1 0.5 !
66: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-11Wan.tdb): HCP_A3, type code %A, sha256 `29487a21dbf9915b…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): HCP_A3, type code %A, sha256 `183add95bfc32e46…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Guo.tdb): HCP_A3, type code %A, sha256 `47ca15461ab905b4…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-19Wit.tdb): HCP_A3, type code %A, sha256 `20ca15b772842baa…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): HCP_A3, type code %A, sha256 `34a1c0676e8eed2a…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21Zha.tdb): HCP_A3, type code %A, sha256 `de527885390e9a9d…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-22Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-22Kri.tdb): HCP_A3, type code %A, sha256 `7d978f1075f96b7f…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-23Wal-3g.tdb): HCP_A3, type code %A, sha256 `eb27ebd8890d3aea…`

~~~~text
59: PHASE HCP_A3 %A 2 1 0.5 !
60: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-24Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-24Lia.tdb): HCP_A3, type code %A, sha256 `0a498e0d238a414e…`

~~~~text
59: PHASE HCP_A3 %A 2 1 0.5 !
60: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-89Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-89Bal.tdb): HCP_A3, type code %A, sha256 `960a05a577d637ea…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-94Har.tdb): HCP_A3, type code %A, sha256 `89d365c4c3215e59…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-98Dum.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Dum.tdb): HCP_A3, type code %A, sha256 `16241d492de1e8a2…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-98Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Har-LB.tdb): HCP_A3, type code %A, sha256 `8b57368794e5504f…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-98Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Jon.tdb): HCP_A3, type code %A, sha256 `d6efa66564a03f46…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE TI% : VA : !
~~~~

[FeTi-98Ran.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Ran.tdb): HCP_A3, type code %A, sha256 `72430ad2c2591dea…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE TI% : VA : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770341923](https://doi.org/10.1361/105497198770341923) L. F. S. Dumitrescu, M. Hillert, N. Sounders, Comparison of Fe-Ti assessments, JPE 19, 441-448 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11663-998-0113-z](https://doi.org/10.1007/s11663-998-0113-z) Stefan Jonsson, Assessment of the Fe-Ti system, Metall Mater Trans B 29, 361-370 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2011.07.071](https://doi.org/10.1016/j.matchemphys.2011.07.071) C.P. Wang, J.P. Zheng, Y. Yu, H.F. Hu, X.J. Liu, Experimental investigation and thermodynamic calculation of the phase equilibria in the Fe–Nb–Ti ternary system, Materials Chemistry and Physics 130, 806-814 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)61450-7](https://doi.org/10.1016/S1003-6326%2811%2961450-7) H. Bo, J. Wang, L. Duarte, C. Leinenbach, L. Liu, H. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 22, 2204-11(2012).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90028-0](https://doi.org/10.1016/0364-5916%2894%2990028-0) K.C.Hari Kumar, P. Wollaiits, L. Delaey, Thermodynamic reassessment and calculation of FeTi phase diagram, Calphad 18, 223-234 (1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2020.106978](https://doi.org/10.1016/j.intermet.2020.106978) K. Santhy, K.C. Hari Kumar, Thermodynamic modelling of magnetic laves phase in Fe–Ti system using first principle method, Intermetallics 128, 106978 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01124-9](https://doi.org/10.1007/s11669-024-01124-9) Zhi Liang, Ursula Kattner, Kamal Choudharry, Francesca Tavazza, Carelyn Campbell, Thermodynamic Assessments of Ti-Al, Ti-Fe, and Ti-Al-Fe Systems with Four-Sublattice Description of Ordered Body-Centered Cubic Phase and Density Functional Theory Data, J. Phase Equilib. Diffus. 45, 732-756 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-021-00889-7](https://doi.org/10.1007/s11669-021-00889-7) G. Zhang, W. Zheng, Z. Zhao, Y. He, Z. Zheng, D. Tang, J. Phase Equilib. Diffus., 42, 363-72(2021).  
_assessment that models this phase_

## LIQUID (Fe–Ti)

- Id: `phase:fe-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 15 of 16 calculated diagram(s): 1335.77–2500 K, x(Ti) 0–1
- Literature: 256 values (256 accepted) from 9 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ti:liquid)

Names (28): _corpus: _corpus:phase:fe-ti:liquid  
_paper: _paper:10.1007/s11663-998-0113-z:L, paper:10.1007/s11669-024-01124-9:L, paper:10.1016/0364-5916(94)90028-0:Liquid, paper:10.1016/j.intermet.2020.106978:L, paper:10.1016/j.jallcom.2019.05.341:L, paper:10.1016/j.matchemphys.2011.07.071:L, paper:10.1016/s0364-5916(98)00037-6:L, paper:10.1016/s0364-5916(98)00037-6:Liquid, paper:10.1016/s1003-6326(11)61450-7:L, paper:10.1016/s1003-6326(11)61450-7:Liquid, paper:10.1361/105497198770341923:L  
_tdb: _tdb:FeTi-09Key.tdb:LIQUID, tdb:FeTi-11Wan.tdb:LIQUID, tdb:FeTi-12Bo.tdb:LIQUID, tdb:FeTi-12Guo.tdb:LIQUID, tdb:FeTi-19Wit.tdb:LIQUID, tdb:FeTi-21San.tdb:LIQUID, tdb:FeTi-21Zha.tdb:LIQUID, tdb:FeTi-22Kri.tdb:LIQUID, tdb:FeTi-23Wal-3g.tdb:LIQUID, tdb:FeTi-24Lia.tdb:LIQUID, tdb:FeTi-89Bal.tdb:LIQUID, tdb:FeTi-94Har.tdb:LIQUID, tdb:FeTi-98Dum.tdb:LIQUID, tdb:FeTi-98Har-LB.tdb:LIQUID, tdb:FeTi-98Jon.tdb:LIQUID, tdb:FeTi-98Ran.tdb:LIQUID  


### TDB models of LIQUID (16): PHASE and CONSTITUENT statements as written

[FeTi-09Key.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-09Key.tdb): LIQUID, type code %, sha256 `1ea2428706857b8b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-11Wan.tdb): LIQUID, type code %, sha256 `29487a21dbf9915b…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-12Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Bo.tdb): LIQUID, type code %, sha256 `183add95bfc32e46…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-12Guo.tdb): LIQUID, type code %, sha256 `47ca15461ab905b4…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-19Wit.tdb): LIQUID, type code %, sha256 `20ca15b772842baa…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-21San.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21San.tdb): LIQUID, type code %, sha256 `34a1c0676e8eed2a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-21Zha.tdb): LIQUID, type code %, sha256 `de527885390e9a9d…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-22Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-22Kri.tdb): LIQUID, type code %, sha256 `7d978f1075f96b7f…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-23Wal-3g.tdb): LIQUID, type code %, sha256 `eb27ebd8890d3aea…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-24Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-24Lia.tdb): LIQUID, type code %, sha256 `0a498e0d238a414e…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-89Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-89Bal.tdb): LIQUID, type code %, sha256 `960a05a577d637ea…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-94Har.tdb): LIQUID, type code %, sha256 `89d365c4c3215e59…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-98Dum.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Dum.tdb): LIQUID, type code %, sha256 `16241d492de1e8a2…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-98Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Har-LB.tdb): LIQUID, type code %, sha256 `8b57368794e5504f…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-98Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Jon.tdb): LIQUID, type code %, sha256 `d6efa66564a03f46…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE TI : !
~~~~

[FeTi-98Ran.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTi-98Ran.tdb): LIQUID, type code %, sha256 `72430ad2c2591dea…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE TI : !
~~~~

Example references (10 of 17; assessments first): 

- [doi:10.1361/105497198770341923](https://doi.org/10.1361/105497198770341923) L. F. S. Dumitrescu, M. Hillert, N. Sounders, Comparison of Fe-Ti assessments, JPE 19, 441-448 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11663-998-0113-z](https://doi.org/10.1007/s11663-998-0113-z) Stefan Jonsson, Assessment of the Fe-Ti system, Metall Mater Trans B 29, 361-370 (1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90028-0](https://doi.org/10.1016/0364-5916%2894%2990028-0) K.C.Hari Kumar, P. Wollaiits, L. Delaey, Thermodynamic reassessment and calculation of FeTi phase diagram, Calphad 18, 223-234 (1994).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)61450-7](https://doi.org/10.1016/S1003-6326%2811%2961450-7) H. Bo, J. Wang, L. Duarte, C. Leinenbach, L. Liu, H. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 22, 2204-11(2012).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2011.07.071](https://doi.org/10.1016/j.matchemphys.2011.07.071) C.P. Wang, J.P. Zheng, Y. Yu, H.F. Hu, X.J. Liu, Experimental investigation and thermodynamic calculation of the phase equilibria in the Fe–Nb–Ti ternary system, Materials Chemistry and Physics 130, 806-814 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2020.106978](https://doi.org/10.1016/j.intermet.2020.106978) K. Santhy, K.C. Hari Kumar, Thermodynamic modelling of magnetic laves phase in Fe–Ti system using first principle method, Intermetallics 128, 106978 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01124-9](https://doi.org/10.1007/s11669-024-01124-9) Zhi Liang, Ursula Kattner, Kamal Choudharry, Francesca Tavazza, Carelyn Campbell, Thermodynamic Assessments of Ti-Al, Ti-Fe, and Ti-Al-Fe Systems with Four-Sublattice Description of Ordered Body-Centered Cubic Phase and Density Functional Theory Data, J. Phase Equilib. Diffus. 45, 732-756 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-021-00889-7](https://doi.org/10.1007/s11669-021-00889-7) G. Zhang, W. Zheng, Z. Zhao, Y. He, Z. Zheng, D. Tang, J. Phase Equilib. Diffus., 42, 363-72(2021).  
_assessment that models this phase_

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
