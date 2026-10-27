# Sb–Sn phases

> Sb–Sn system: 10 phases (tier A 6, liquid 1, needs_review 3); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SB-SN.html · Markdown: https://data.orchid-project.org/phases/pages/SB-SN.md

10 phases (tier A 6, liquid 1, needs_review 3); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SB-SN) · [full JSON](https://data.orchid-project.org/phases/systems/SB-SN.json) · [Sb–Sn system page](https://data.orchid-project.org/systems/SB-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SB-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sb–Sn system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sb-sn-a4-diamond); _phase:sb-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [BCT_A5](#phase-sb-sn-a5-bct); _phase:sb-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–532.43 K, x(Sn) 0.88303–1 | 17 | 7 |
| [RHOMBOHEDRAL_A7](#phase-sb-sn-a7-rhombohedral); _phase:sb-sn:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–903.78 K, x(Sn) 0–0.15923 | 20 | 7 |
| [BCC_A2](#phase-sb-sn-bcc-a2); _phase:sb-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [FCC_A1](#phase-sb-sn-fcc-a1); _phase:sb-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [HCP_A3](#phase-sb-sn-hcp-a3); _phase:sb-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [LIQUID](#phase-sb-sn-liquid); _phase:sb-sn:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 505.08–2500 K, x(Sn) 0–1 | 46 | 7 |
| [SB2SN3](#phase-sb-sn-sb2sn3); _phase:sb-sn:sb2sn3_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 500–602.33 K, x(Sn) 0.6–0.6 | 13 | 4 |
| [SB3SN4](#phase-sb-sn-sb3sn4); _phase:sb-sn:sb3sn4_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–600 K, x(Sn) 0.57–0.57143 | 17 | 4 |
| [SBSN](#phase-sb-sn-sbsn); _phase:sb-sn:sbsn_ |  | needs_review | stable in 7 of 7 calculated diagram(s): 300–700.01 K, x(Sn) 0.32549–0.5697 | 32 | 7 |

## DIAMOND_A4 (Sb–Sn)

- Id: `phase:sb-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:a4-diamond)

Names (8): _corpus: _corpus:phase:sb-sn:a4-diamond  
_tdb: _tdb:SbSn-07Kro.tdb:DIAMOND_A4, tdb:SbSn-08Che.tdb:DIAMOND_A4, tdb:SbSn-19Lys.tdb:DIAMOND_A4, tdb:SbSn-20Gie.tdb:DIAMOND_A4, tdb:SbSn-21Zha.tdb:DIAMOND_A4, tdb:SbSn-86Jon.tdb:DIAMOND_A4, tdb:SbSn-96Oh-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): DIAMOND_A4, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): DIAMOND_A4, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SN : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): DIAMOND_A4, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SN : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): DIAMOND_A4, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): DIAMOND_A4, type code %, sha256 `d50a6f4312522c24…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SN : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): DIAMOND_A4, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
53: PHASE DIAMOND_A4 % 1 1 !
54: CONST DIAMOND_A4 : SN : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): DIAMOND_A4, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
54: PHASE DIAMOND_A4 % 1 1 !
55: CONST DIAMOND_A4 : SN : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_

## BCT_A5 (Sb–Sn)

- Id: `phase:sb-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–532.43 K, x(Sn) 0.88303–1
- Literature: 17 values (17 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:a5-bct)

Names (12): _corpus: _corpus:phase:sb-sn:a5-bct, corpus:phase:sb-sn:bct-a5  
_paper: _paper:10.1007/s10853-019-03934-6:BCT_A5, paper:10.1007/s11664-008-0464-x:Sn, paper:10.1016/j.jallcom.2016.11.003:(βSn)  
_tdb: _tdb:SbSn-07Kro.tdb:BCT_A5, tdb:SbSn-08Che.tdb:BCT_A5, tdb:SbSn-19Lys.tdb:BCT_A5, tdb:SbSn-20Gie.tdb:BCT_A5, tdb:SbSn-21Zha.tdb:BCT_A5, tdb:SbSn-86Jon.tdb:BCT_A5, tdb:SbSn-96Oh-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): BCT_A5, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : SB SN% : !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): BCT_A5, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
52: PHASE BCT_A5 % 1 1 !
53: CONST BCT_A5 : SB SN% : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): BCT_A5, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
53: PHASE BCT_A5 % 1 1 !
54: CONST BCT_A5 : SB SN% : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): BCT_A5, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : SB SN% : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): BCT_A5, type code %, sha256 `d50a6f4312522c24…`

~~~~text
52: PHASE BCT_A5 % 1 1 !
53: CONST BCT_A5 : SB SN% : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): BCT_A5, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
58: PHASE BCT_A5 % 1 1 !
59: CONST BCT_A5 : SB SN% : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): BCT_A5, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
59: PHASE BCT_A5 % 1 1 !
60: CONST BCT_A5 : SB SN% : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_reports values for this phase_
- [doi:10.1016/0021-9614(85)90113-2](https://doi.org/10.1016/0021-9614%2885%2990113-2) M Iwase, S Sugino, E Ichise, Y Waseda, Application of Na+-ion-conducting β-Al2O3 to thermodynamic studies of liquid sodium-based alloys: {xNa+(1−x)Cd}, {xNa+(1−x)In}, and {xNa+(1−x)Sn}, The Journal of Chemical Thermodynamics 17, 601-609 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0956-716x(90)90513-g](https://doi.org/10.1016/0956-716x%2890%2990513-g) W.P. Allen, J.H. Perepezko, Constitution of the tin-antimony system, Scripta Metallurgica et Materialia 24, 2215-2220 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01243-3](https://doi.org/10.1016/s0925-8388%2800%2901243-3) V. Vassiliev, Y. Feutelais, M. Sghaier, B. Legendre, Thermodynamic investigation in In–Sb, Sb–Sn and In–Sb–Sn liquid systems, Journal of Alloys and Compounds 314, 198-205 (2001).  
_cited as the source of values for this phase_

## RHOMBOHEDRAL_A7 (Sb–Sn)

- Id: `phase:sb-sn:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–903.78 K, x(Sn) 0–0.15923
- Literature: 20 values (20 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:a7-rhombohedral)

Names (12): _corpus: _corpus:phase:sb-sn:a7-rhombohedral, corpus:phase:sb-sn:rhombohedral-a7  
_paper: _paper:10.1007/s10853-019-03934-6:Rhombohedral_A7, paper:10.1007/s11664-008-0464-x:Sb, paper:10.1016/j.jallcom.2016.11.003:(αSb)  
_tdb: _tdb:SbSn-07Kro.tdb:RHOMBOHEDRAL_A7, tdb:SbSn-08Che.tdb:RHOMBOHEDRAL_A7, tdb:SbSn-19Lys.tdb:RHOMBOHEDRAL_A7, tdb:SbSn-20Gie.tdb:RHOMBOHEDRAL_A7, tdb:SbSn-21Zha.tdb:RHOMBOHEDRAL_A7, tdb:SbSn-86Jon.tdb:RHOMBOHEDRAL_A7, tdb:SbSn-96Oh-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
55: PHASE RHOMBOHEDRAL_A7 % 1 1 !
56: CONST RHOMBOHEDRAL_A7 : SB% SN : !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
57: PHASE RHOMBOHEDRAL_A7 % 1 1 !
58: CONST RHOMBOHEDRAL_A7 : SB% SN : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
58: PHASE RHOMBOHEDRAL_A7 % 1 1 !
59: CONST RHOMBOHEDRAL_A7 : SB% SN : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
55: PHASE RHOMBOHEDRAL_A7 % 1 1 !
56: CONST RHOMBOHEDRAL_A7 : SB% SN : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `d50a6f4312522c24…`

~~~~text
57: PHASE RHOMBOHEDRAL_A7 % 1 1 !
58: CONST RHOMBOHEDRAL_A7 : SB% SN : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
63: PHASE RHOMBOHEDRAL_A7 % 1 1 !
64: CONST RHOMBOHEDRAL_A7 : SB% SN : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
64: PHASE RHOMBOHEDRAL_A7 % 1 1 !
65: CONST RHOMBOHEDRAL_A7 : SB% SN : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_reports values for this phase_
- [doi:10.1016/s0925-8388(00)01243-3](https://doi.org/10.1016/s0925-8388%2800%2901243-3) V. Vassiliev, Y. Feutelais, M. Sghaier, B. Legendre, Thermodynamic investigation in In–Sb, Sb–Sn and In–Sb–Sn liquid systems, Journal of Alloys and Compounds 314, 198-205 (2001).  
_cited as the source of values for this phase_

## BCC_A2 (Sb–Sn)

- Id: `phase:sb-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:bcc-a2)

Names (8): _corpus: _corpus:phase:sb-sn:bcc-a2  
_tdb: _tdb:SbSn-07Kro.tdb:BCC_A2, tdb:SbSn-08Che.tdb:BCC_A2, tdb:SbSn-19Lys.tdb:BCC_A2, tdb:SbSn-20Gie.tdb:BCC_A2, tdb:SbSn-21Zha.tdb:BCC_A2, tdb:SbSn-86Jon.tdb:BCC_A2, tdb:SbSn-96Oh-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): BCC_A2, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
35: PHASE BCC_A2 % 2 1 3 !
36: CONST BCC_A2 : SB SN : VA : !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): BCC_A2, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
37: PHASE BCC_A2 % 2 1 3 !
38: CONST BCC_A2 : SB SN : VA : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): BCC_A2, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
38: PHASE BCC_A2 % 2 1 3 !
39: CONST BCC_A2 : SB SN : VA : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): BCC_A2, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
35: PHASE BCC_A2 % 2 1 3 !
36: CONST BCC_A2 : SB SN : VA : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): BCC_A2, type code %, sha256 `d50a6f4312522c24…`

~~~~text
37: PHASE BCC_A2 % 2 1 3 !
38: CONST BCC_A2 : SB SN : VA : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): BCC_A2, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
43: PHASE BCC_A2 % 2 1 3 !
44: CONST BCC_A2 : SB SN : VA : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): BCC_A2, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
44: PHASE BCC_A2 % 2 1 3 !
45: CONST BCC_A2 : SB SN : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_

## FCC_A1 (Sb–Sn)

- Id: `phase:sb-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:fcc-a1)

Names (8): _corpus: _corpus:phase:sb-sn:fcc-a1  
_tdb: _tdb:SbSn-07Kro.tdb:FCC_A1, tdb:SbSn-08Che.tdb:FCC_A1, tdb:SbSn-19Lys.tdb:FCC_A1, tdb:SbSn-20Gie.tdb:FCC_A1, tdb:SbSn-21Zha.tdb:FCC_A1, tdb:SbSn-86Jon.tdb:FCC_A1, tdb:SbSn-96Oh-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): FCC_A1, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
30: PHASE FCC_A1 % 2 1 1 !
31: CONST FCC_A1 : SB SN : VA : !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): FCC_A1, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
32: PHASE FCC_A1 % 2 1 1 !
33: CONST FCC_A1 : SB SN : VA : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): FCC_A1, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
33: PHASE FCC_A1 % 2 1 1 !
34: CONST FCC_A1 : SB SN : VA : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): FCC_A1, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
30: PHASE FCC_A1 % 2 1 1 !
31: CONST FCC_A1 : SB SN : VA : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): FCC_A1, type code %, sha256 `d50a6f4312522c24…`

~~~~text
32: PHASE FCC_A1 % 2 1 1 !
33: CONST FCC_A1 : SB SN : VA : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): FCC_A1, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
38: PHASE FCC_A1 % 2 1 1 !
39: CONST FCC_A1 : SB SN : VA : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): FCC_A1, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
39: PHASE FCC_A1 % 2 1 1 !
40: CONST FCC_A1 : SB SN : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_

## HCP_A3 (Sb–Sn)

- Id: `phase:sb-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:hcp-a3)

Names (8): _corpus: _corpus:phase:sb-sn:hcp-a3  
_tdb: _tdb:SbSn-07Kro.tdb:HCP_A3, tdb:SbSn-08Che.tdb:HCP_A3, tdb:SbSn-19Lys.tdb:HCP_A3, tdb:SbSn-20Gie.tdb:HCP_A3, tdb:SbSn-21Zha.tdb:HCP_A3, tdb:SbSn-86Jon.tdb:HCP_A3, tdb:SbSn-96Oh-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): HCP_A3, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : SB SN : VA: !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): HCP_A3, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : SB SN : VA: !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): HCP_A3, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : SB SN : VA: !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): HCP_A3, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : SB SN : VA: !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): HCP_A3, type code %, sha256 `d50a6f4312522c24…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : SB SN : VA: !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): HCP_A3, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
48: PHASE HCP_A3 % 2 1 0.5 !
49: CONST HCP_A3 : SB SN : VA: !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): HCP_A3, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
49: PHASE HCP_A3 % 2 1 0.5 !
50: CONST HCP_A3 : SB SN : VA: !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_

## LIQUID (Sb–Sn)

- Id: `phase:sb-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 505.08–2500 K, x(Sn) 0–1
- Literature: 46 values (46 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:liquid)

Names (12): _corpus: _corpus:phase:sb-sn:liquid  
_paper: _paper:10.1007/s10853-019-03934-6:L, paper:10.1007/s11664-008-0464-x:L, paper:10.1007/s11664-008-0464-x:Liquid, paper:10.1016/j.jallcom.2016.11.003:L  
_tdb: _tdb:SbSn-07Kro.tdb:LIQUID, tdb:SbSn-08Che.tdb:LIQUID, tdb:SbSn-19Lys.tdb:LIQUID, tdb:SbSn-20Gie.tdb:LIQUID, tdb:SbSn-21Zha.tdb:LIQUID, tdb:SbSn-86Jon.tdb:LIQUID, tdb:SbSn-96Oh-LB.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): LIQUID, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : SB SN : !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): LIQUID, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : SB SN : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): LIQUID, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : SB SN : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): LIQUID, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : SB SN : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): LIQUID, type code %, sha256 `d50a6f4312522c24…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : SB SN : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): LIQUID, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : SB SN : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): LIQUID, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : SB SN : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_reports values for this phase_
- [doi:10.1016/s0925-8388(00)01243-3](https://doi.org/10.1016/s0925-8388%2800%2901243-3) V. Vassiliev, Y. Feutelais, M. Sghaier, B. Legendre, Thermodynamic investigation in In–Sb, Sb–Sn and In–Sb–Sn liquid systems, Journal of Alloys and Compounds 314, 198-205 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/0021-9614(85)90113-2](https://doi.org/10.1016/0021-9614%2885%2990113-2) M Iwase, S Sugino, E Ichise, Y Waseda, Application of Na+-ion-conducting β-Al2O3 to thermodynamic studies of liquid sodium-based alloys: {xNa+(1−x)Cd}, {xNa+(1−x)In}, and {xNa+(1−x)Sn}, The Journal of Chemical Thermodynamics 17, 601-609 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0956-716x(90)90513-g](https://doi.org/10.1016/0956-716x%2890%2990513-g) W.P. Allen, J.H. Perepezko, Constitution of the tin-antimony system, Scripta Metallurgica et Materialia 24, 2215-2220 (1990).  
_cited as the source of values for this phase_

## SB2SN3 (Sb–Sn)

- Id: `phase:sb-sn:sb2sn3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Sb2Sn3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Sb2Sn3) — Hallstedt 2025 mmc2 row for SB2SN3: Sb2Sn3
- Stoichiometry: Sb 0.4000, Sn 0.6000
- Stability: stable in 4 of 4 calculated diagram(s): 500–602.33 K, x(Sn) 0.6–0.6
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:sb2sn3)

Names (6): _corpus: _corpus:phase:sb-sn:sb2sn3  
_paper: _paper:10.1016/j.jallcom.2016.11.003:Sb2Sn3  
_tdb: _tdb:SbSn-07Kro.tdb:SB2SN3, tdb:SbSn-19Lys.tdb:SB2SN3, tdb:SbSn-86Jon.tdb:SB2SN3, tdb:SbSn-96Oh-LB.tdb:SB2SN3  


### TDB models of SB2SN3 (4): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): SB2SN3, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
65: PHASE SB2SN3 % 2 2 3 !
66: CONST SB2SN3 : SB : SN : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): SB2SN3, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
73: PHASE SB2SN3 % 2 2 3 !
74: CONST SB2SN3 : SB : SN : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): SB2SN3, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
73: PHASE SB2SN3 % 2 2 3 !
74: CONST SB2SN3 : SB : SN : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): SB2SN3, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
74: PHASE SB2SN3 % 2 2 3 !
75: CONST SB2SN3 : SB : SN : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_reports values for this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_cited as the source of values for this phase_
- [doi:10.1016/0021-9614(85)90113-2](https://doi.org/10.1016/0021-9614%2885%2990113-2) M Iwase, S Sugino, E Ichise, Y Waseda, Application of Na+-ion-conducting β-Al2O3 to thermodynamic studies of liquid sodium-based alloys: {xNa+(1−x)Cd}, {xNa+(1−x)In}, and {xNa+(1−x)Sn}, The Journal of Chemical Thermodynamics 17, 601-609 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0956-716x(90)90513-g](https://doi.org/10.1016/0956-716x%2890%2990513-g) W.P. Allen, J.H. Perepezko, Constitution of the tin-antimony system, Scripta Metallurgica et Materialia 24, 2215-2220 (1990).  
_cited as the source of values for this phase_

## SB3SN4 (Sb–Sn)

- Id: `phase:sb-sn:sb3sn4`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; no_structure_token
- Candidate (dft_oqmd): R-3m (166) — on-hull OQMD Sb3 Sn4 at x(SN)=0.5714
- Candidate (literature_printed): Sb3Sn4 · hR7 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Sb3Sn4 · hR7 · R-3m (166) — Hallstedt 2025 mmc2 row for SB3SN4: Sb3Sn4
- Candidate (tdb_comment): Sb3Sn4 · hR7 · R-3m — SbSn-08Che.tdb: 'Prototype Sb3Sn4 (hR7, R-3m)'
- Candidate (tdb_comment): Sb3Sn4 · hR7 · R-3m — SbSn-19Lys.tdb: 'Prototype Sb3Sn4 (hR7, R-3m)'
- Candidate (tdb_comment): Sb3Sn4 · hR7 · R-3m — SbSn-20Gie.tdb: 'Prototype Sb3Sn4 (hR7, R-3m)'
- Candidate (tdb_comment): Sb3Sn4 · hR7 · R-3m — SbSn-21Zha.tdb: 'Prototype Sb3Sn4 (hR7, R-3m)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–600 K, x(Sn) 0.57–0.57143
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:sb3sn4)

Names (7): _corpus: _corpus:phase:sb-sn:sb3sn4  
_paper: _paper:10.1007/s10853-019-03934-6:Sb3Sn4, paper:10.1007/s11664-008-0464-x:Sn3Sb2  
_tdb: _tdb:SbSn-08Che.tdb:SB3SN4, tdb:SbSn-19Lys.tdb:SB3SN4, tdb:SbSn-20Gie.tdb:SB3SN4, tdb:SbSn-21Zha.tdb:SB3SN4  


### TDB models of SB3SN4 (4): PHASE and CONSTITUENT statements as written

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): SB3SN4, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
67: PHASE SB3SN4 % 2 0.43 0.57 !
68: CONST SB3SN4 : SB : SN : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): SB3SN4, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
68: PHASE SB3SN4 % 2 3 4 !
69: CONST SB3SN4 : SB : SN : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): SB3SN4, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
65: PHASE SB3SN4 % 2 3 4 !
66: CONST SB3SN4 : SB : SN : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): SB3SN4, type code %, sha256 `d50a6f4312522c24…`

~~~~text
67: PHASE SB3SN4 % 2 3 4 !
68: CONST SB3SN4 : SB : SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(00)01243-3](https://doi.org/10.1016/s0925-8388%2800%2901243-3) V. Vassiliev, Y. Feutelais, M. Sghaier, B. Legendre, Thermodynamic investigation in In–Sb, Sb–Sn and In–Sb–Sn liquid systems, Journal of Alloys and Compounds 314, 198-205 (2001).  
_cited as the source of values for this phase_

## SBSN (Sb–Sn)

- Id: `phase:sb-sn:sbsn`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): Fm-3m (225) — on-hull MP SnSb at x(SN)=0.5000
- Candidate (literature_printed): SbSn · hR1 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): SbSn · hR1 · R-3m (166) — Hallstedt 2025 mmc2 row for SBSN: SbSn
- Candidate (tdb_comment): SbSn · hR1 · R-3m — SbSn-07Kro.tdb: 'Prototype SbSn (hR1, R-3m)'
- Candidate (tdb_comment): SbSn · hR1 · R-3m — SbSn-08Che.tdb: 'Prototype SbSn (hR1, R-3m)'
- Candidate (tdb_comment): SbSn · hR1 · R-3m — SbSn-19Lys.tdb: 'Prototype SbSn (hR1, R-3m)'
- Candidate (tdb_comment): SbSn · hR1 · R-3m — SbSn-20Gie.tdb: 'Prototype SbSn (hR1, R-3m)'
- Candidate (tdb_comment): SbSn · hR1 · R-3m — SbSn-21Zha.tdb: 'Prototype SbSn (hR1, R-3m)'
- Stability: stable in 7 of 7 calculated diagram(s): 300–700.01 K, x(Sn) 0.32549–0.5697
- Literature: 32 values (32 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-sn:sbsn)

Names (12): _corpus: _corpus:phase:sb-sn:sbsn  
_paper: _paper:10.1007/s10853-019-03934-6:SbSn, paper:10.1007/s11664-008-0464-x:β-SnSb, paper:10.1016/j.jallcom.2016.11.003:SbSn, paper:10.1179/mst.1986.2.9.913:SbSn  
_tdb: _tdb:SbSn-07Kro.tdb:SBSN, tdb:SbSn-08Che.tdb:SBSN, tdb:SbSn-19Lys.tdb:SBSN, tdb:SbSn-20Gie.tdb:SBSN, tdb:SbSn-21Zha.tdb:SBSN, tdb:SbSn-86Jon.tdb:SBSN, tdb:SbSn-96Oh-LB.tdb:SBSN  


### TDB models of SBSN (7): PHASE and CONSTITUENT statements as written

[SbSn-07Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-07Kro.tdb): SBSN, type code %, sha256 `4362fd5505bf6c6e…`

~~~~text
60: PHASE SBSN % 2 1 1 !
61: CONST SBSN : SB% SN : SB SN% : !
~~~~

[SbSn-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-08Che.tdb): SBSN, type code %, sha256 `8dbc58c45ff8a178…`

~~~~text
62: PHASE SBSN % 2 1 1 !
63: CONST SBSN : SB% SN : SB SN% : !
~~~~

[SbSn-19Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-19Lys.tdb): SBSN, type code %, sha256 `444c2c01cb612eb3…`

~~~~text
63: PHASE SBSN % 2 1 1 !
64: CONST SBSN : SB% SN : SB SN% : !
~~~~

[SbSn-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-20Gie.tdb): SBSN, type code %, sha256 `6e68652e3e5cdb6f…`

~~~~text
60: PHASE SBSN % 2 3 4 !
61: CONST SBSN : SB : SB SN% : !
~~~~

[SbSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-21Zha.tdb): SBSN, type code %, sha256 `d50a6f4312522c24…`

~~~~text
62: PHASE SBSN % 2 3 4 !
63: CONST SBSN : SB : SB SN% VA : !
~~~~

[SbSn-86Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-86Jon.tdb): SBSN, type code %, sha256 `ae5b45b1dfceacbc…`

~~~~text
68: PHASE SBSN % 2 0.5 0.5 !
69: CONST SBSN : SB% SN : SB SN% : !
~~~~

[SbSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSn-96Oh-LB.tdb): SBSN, type code %, sha256 `a2ded9c80655a44b…`

~~~~text
69: PHASE SBSN % 2 1 1 !
70: CONST SBSN : SB% SN : SB SN% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10853-019-03934-6](https://doi.org/10.1007/s10853-019-03934-6) Wojciech Gierlotka, On the binary Sb–Sn system: ab initio calculation and thermodynamic remodeling, J Mater Sci 55, 347-357 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-008-0464-x](https://doi.org/10.1007/s11664-008-0464-x) Sinn-Wen Chen, Chih-Chi Chen, Wojcieh Gierlotka, An-Ren Zi, Po-Yin Chen, Hsin-Jay Wu, Phase Equilibria of the Sn-Sb Binary System, Journal of Elec Materi 37, 992-1002 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1179/mst.1986.2.9.913](https://doi.org/10.1179/mst.1986.2.9.913) B. Jönsson, J. Ågren, Thermodynamic assessment of Sb–Sn system, Materials Science and Technology 2, 913-916 (1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.10.223](https://doi.org/10.1016/j.jallcom.2018.10.223) V.A. Lysenko, Thermodynamic reassessment of the Sb-Sn and In-Sb-Sn systems, Journal of Alloys and Compounds 776, 850-857 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_reports values for this phase_
- [doi:10.1016/s0925-8388(00)01243-3](https://doi.org/10.1016/s0925-8388%2800%2901243-3) V. Vassiliev, Y. Feutelais, M. Sghaier, B. Legendre, Thermodynamic investigation in In–Sb, Sb–Sn and In–Sb–Sn liquid systems, Journal of Alloys and Compounds 314, 198-205 (2001).  
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
