# Fe–Si phases

> Fe–Si system: 12 phases (tier A 5, tier C 3, liquid 1, needs_review 3); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-SI.html · Markdown: https://data.orchid-project.org/phases/pages/FE-SI.md

12 phases (tier A 5, tier C 3, liquid 1, needs_review 3); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-SI) · [full JSON](https://data.orchid-project.org/phases/systems/FE-SI.json) · [Fe–Si system page](https://data.orchid-project.org/systems/FE-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Si system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-fe-si-a4-diamond); _phase:fe-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.97 K, x(Si) 1–1 | 4 | 5 |
| [MSI_B20](#phase-fe-si-b20-msi); _phase:fe-si:b20-msi_ | FeSi · B20 · cP8 · P2_13 (198) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1683.86 K, x(Si) 0.48824–0.5122 | 12 | 5 |
| [BCC_4SL](#phase-fe-si-bcc-4sl); _phase:fe-si:bcc-4sl_ |  | needs_review | no calculated diagram | 0 | 2 |
| [BCC_A2](#phase-fe-si-bcc-a2); _phase:fe-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1800 K, x(Si) 0–0.19 | 4 | 10 |
| [B2_BCC](#phase-fe-si-bcc-b2); _phase:fe-si:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1823.25 K, x(Si) 0–0.31807 | 6 | 5 |
| [M5SI3_D88](#phase-fe-si-d88-m5si3); _phase:fe-si:d88-m5si3_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 1070–1364.45 K, x(Si) 0.375–0.375 | 3 | 5 |
| [FCC_A1](#phase-fe-si-fcc-a1); _phase:fe-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1179.97–1696.48 K, x(Si) 0–0.03391 | 0 | 5 |
| [FE2SI](#phase-fe-si-fe2si); _phase:fe-si:fe2si_ | AlNi2 · hP6 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 1315.83–1487.53 K, x(Si) 0.33333–0.3392 | 11 | 5 |
| [FESI2_H](#phase-fe-si-fesi2-h); _phase:fe-si:fesi2-h_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 1209.55–1487 K, x(Si) 0.69809–0.71468 | 11 | 5 |
| [FESI2_L](#phase-fe-si-fesi2-l); _phase:fe-si:fesi2-l_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1275.67 K, x(Si) 0.66667–0.66667 | 2 | 5 |
| [HCP_A3](#phase-fe-si-hcp-a3); _phase:fe-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-fe-si-liquid); _phase:fe-si:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1470.59–2500 K, x(Si) 0–1 | 21 | 5 |

## DIAMOND_A4 (Fe–Si)

- Id: `phase:fe-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.97 K, x(Si) 1–1
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:a4-diamond)

Names (9): _corpus: _corpus:phase:fe-si:a4-diamond, corpus:phase:fe-si:diamond-a4  
_paper: _paper:10.1016/j.calphad.2013.07.007:(Si), paper:10.1016/s0364-5916(98)00037-6:(Si)  
_tdb: _tdb:FeSi-12Ohn.tdb:DIAMOND_A4, tdb:FeSi-14Yua.tdb:DIAMOND_A4, tdb:FeSi-17Cui.tdb:DIAMOND_A4, tdb:FeSi-23Wit.tdb:DIAMOND_A4, tdb:FeSi-91Lac-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): DIAMOND_A4, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
62: PHASE DIAMOND_A4 % 1 1 !
63: CONST DIAMOND_A4 : SI : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): DIAMOND_A4, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
55: PHASE DIAMOND_A4 % 1 1 !
56: CONST DIAMOND_A4 : SI : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): DIAMOND_A4, type code %, sha256 `93d3ce80d5ece2c2…`

~~~~text
64: PHASE DIAMOND_A4 % 1 1 !
65: CONST DIAMOND_A4 : FE SI% : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): DIAMOND_A4, type code %, sha256 `1860578382796878…`

~~~~text
62: PHASE DIAMOND_A4 % 1 1 !
63: CONST DIAMOND_A4 : FE SI% : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): DIAMOND_A4, type code %, sha256 `b0825ae47e316513…`

~~~~text
59: PHASE DIAMOND_A4 % 1 1 !
60: CONST DIAMOND_A4 : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## MSI_B20 (Fe–Si)

- Id: `phase:fe-si:b20-msi`; status `assigned`
- Structure: FeSi · B20 · cP8 · P2_13 (198); type `st:b20-fesi-cp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MSI); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in FeSi-23Wit.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1683.86 K, x(Si) 0.48824–0.5122
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:b20-msi)

Names (9): _corpus: _corpus:phase:fe-si:b20-msi, corpus:phase:fe-si:msi-b20  
_paper: _paper:10.1016/j.calphad.2013.07.007:FeSi, paper:10.1016/s0364-5916(98)00037-6:FeSi  
_tdb: _tdb:FeSi-12Ohn.tdb:MSI_B20, tdb:FeSi-14Yua.tdb:MSI_B20, tdb:FeSi-17Cui.tdb:MSI_B20, tdb:FeSi-23Wit.tdb:MSI_B20, tdb:FeSi-91Lac-LB.tdb:MSI_B20  


### TDB models of MSI_B20 (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): MSI_B20, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
77: PHASE MSI_B20 % 2 1 1 !
78: CONST MSI_B20 : FE : SI : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): MSI_B20, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
70: PHASE MSI_B20 % 2 1 1 !
71: CONST MSI_B20 : FE : SI : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): MSI_B20, type code %, sha256 `93d3ce80d5ece2c2…`

~~~~text
79: PHASE MSI_B20 % 2 1 1 !
80: CONST MSI_B20 : FE : SI : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): MSI_B20, type code %, sha256 `1860578382796878…`

~~~~text
77: PHASE MSI_B20 % 2 1 1 !
78: CONST MSI_B20 : FE% SI : FE SI% : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): MSI_B20, type code %, sha256 `b0825ae47e316513…`

~~~~text
79: PHASE MSI_B20 % 2 1 1 !
80: CONST MSI_B20 : FE : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## BCC_4SL (Fe–Si)

- Id: `phase:fe-si:bcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:FeSi-12Ohn.tdb_model_is_partitioned; order_disorder_ambiguity:FeSi-17Cui.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Candidate (tdb_comment): CsCl · B2 · cP2, Pm-3m — FeSi-12Ohn.tdb: 'Prototype CsCl (B2, cP2, Pm-3m), NaTl (B32, cF16, Fd-3m),'
- Candidate (tdb_comment): CsCl · B2 · cP2, Pm-3m — FeSi-17Cui.tdb: 'Prototype CsCl (B2, cP2, Pm-3m), NaTl (B32, cF16, Fd-3m),'
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:bcc-4sl)

Names (3): _corpus: _corpus:phase:fe-si:bcc-4sl  
_tdb: _tdb:FeSi-12Ohn.tdb:BCC_4SL, tdb:FeSi-17Cui.tdb:BCC_4SL  


### TDB models of BCC_4SL (2): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): BCC_4SL, type code %BZ, sha256 `e67d734746ab4b1c…`

~~~~text
52: PHASE BCC_4SL %BZ 5 0.25 0.25 0.25 0.25 1 !
53: CONST BCC_4SL : FE SI : FE SI : FE SI : FE SI : VA : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): BCC_4SL, type code %BZ, sha256 `93d3ce80d5ece2c2…`

~~~~text
54: PHASE BCC_4SL %BZ 5 0.25 0.25 0.25 0.25 1 !
55: CONST BCC_4SL : FE SI : FE SI : FE SI : FE SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_

## BCC_A2 (Fe–Si)

- Id: `phase:fe-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1800 K, x(Si) 0–0.19
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:bcc-a2)

Names (13): _corpus: _corpus:phase:fe-si:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.07.007:BCC_B2, paper:10.2355/isijinternational.52.540:A2 (B2)  
_tdb: _tdb:FeSi-12Ohn.tdb:A2_BCC, tdb:FeSi-12Ohn.tdb:BCC_A2, tdb:FeSi-14Yua.tdb:A2_BCC, tdb:FeSi-14Yua.tdb:BCC_A2, tdb:FeSi-17Cui.tdb:A2_BCC, tdb:FeSi-17Cui.tdb:BCC_A2, tdb:FeSi-23Wit.tdb:A2_BCC, tdb:FeSi-23Wit.tdb:BCC_A2, tdb:FeSi-91Lac-LB.tdb:A2_BCC, tdb:FeSi-91Lac-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (10): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): A2_BCC, type code %B, sha256 `e67d734746ab4b1c…`

~~~~text
41: PHASE A2_BCC %B 2 1 3 !
42: CONST A2_BCC : FE SI : VA : !
~~~~

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): BCC_A2, type code %B, sha256 `e67d734746ab4b1c…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE SI : VA : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): A2_BCC, type code %B, sha256 `b45ac7c1e94df438…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : FE SI : VA : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): BCC_A2, type code %B, sha256 `b45ac7c1e94df438…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE SI : VA : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): A2_BCC, type code %B, sha256 `93d3ce80d5ece2c2…`

~~~~text
43: PHASE A2_BCC %B 2 1 3 !
44: CONST A2_BCC : FE SI : VA : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): BCC_A2, type code %B, sha256 `93d3ce80d5ece2c2…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE SI : VA : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): A2_BCC, type code %B, sha256 `1860578382796878…`

~~~~text
47: PHASE A2_BCC %B 2 1 3 !
48: CONST A2_BCC : FE SI : VA : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): BCC_A2, type code %B, sha256 `1860578382796878…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : FE SI : VA : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): A2_BCC, type code %B, sha256 `b0825ae47e316513…`

~~~~text
44: PHASE A2_BCC %B 2 1 3 !
45: CONST A2_BCC : FE SI : VA : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): BCC_A2, type code %B, sha256 `b0825ae47e316513…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_

## B2_BCC (Fe–Si)

- Id: `phase:fe-si:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: FeSi-12Ohn.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeSi-14Yua.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeSi-17Cui.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeSi-23Wit.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeSi-91Lac-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in FeSi-12Ohn.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeSi-14Yua.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeSi-17Cui.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeSi-23Wit.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeSi-91Lac-LB.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1823.25 K, x(Si) 0–0.31807
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:bcc-b2)

Names (8): _corpus: _corpus:phase:fe-si:bcc-b2  
_paper: _paper:10.1016/s0364-5916(98)00037-6:bcc-B2, paper:10.2355/isijinternational.52.540:B2  
_tdb: _tdb:FeSi-12Ohn.tdb:B2_BCC, tdb:FeSi-14Yua.tdb:B2_BCC, tdb:FeSi-17Cui.tdb:B2_BCC, tdb:FeSi-23Wit.tdb:B2_BCC, tdb:FeSi-91Lac-LB.tdb:B2_BCC  


### TDB models of B2_BCC (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): B2_BCC, type code %BO, sha256 `e67d734746ab4b1c…`

~~~~text
46: PHASE B2_BCC %BO 3 0.5 0.5 3 !
47: CONST B2_BCC : FE% SI : FE SI% : VA : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): B2_BCC, type code %BO, sha256 `b45ac7c1e94df438…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : FE% SI : FE SI% : VA : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): B2_BCC, type code %BO, sha256 `93d3ce80d5ece2c2…`

~~~~text
48: PHASE B2_BCC %BO 3 0.5 0.5 3 !
49: CONST B2_BCC : FE% SI : FE SI% : VA : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): B2_BCC, type code %BO, sha256 `1860578382796878…`

~~~~text
52: PHASE B2_BCC %BO 3 0.5 0.5 3 !
53: CONST B2_BCC : FE% SI : FE SI% : VA : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): B2_BCC, type code %BO, sha256 `b0825ae47e316513…`

~~~~text
49: PHASE B2_BCC %BO 3 0.5 0.5 3 !
50: CONST B2_BCC : FE% SI : FE SI% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## M5SI3_D88 (Fe–Si)

- Id: `phase:fe-si:d88-m5si3`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M5SI3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.6250, Si 0.3750
- Stability: stable in 3 of 3 calculated diagram(s): 1070–1364.45 K, x(Si) 0.375–0.375
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:d88-m5si3)

Names (7): _corpus: _corpus:phase:fe-si:d88-m5si3  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Fe5Si3  
_tdb: _tdb:FeSi-12Ohn.tdb:M5SI3_D88, tdb:FeSi-14Yua.tdb:M5SI3_D88, tdb:FeSi-17Cui.tdb:M5SI3_D88, tdb:FeSi-23Wit.tdb:M5SI3_D88, tdb:FeSi-91Lac-LB.tdb:M5SI3_D88  


### TDB models of M5SI3_D88 (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): M5SI3_D88, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
72: PHASE M5SI3_D88 % 2 5 3 !
73: CONST M5SI3_D88 : FE : SI : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): M5SI3_D88, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
65: PHASE M5SI3_D88 % 2 5 3 !
66: CONST M5SI3_D88 : FE : SI : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): M5SI3_D88, type code %A, sha256 `93d3ce80d5ece2c2…`

~~~~text
74: PHASE M5SI3_D88 %A 2 5 3 !
75: CONST M5SI3_D88 : FE : SI : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): M5SI3_D88, type code %A, sha256 `1860578382796878…`

~~~~text
72: PHASE M5SI3_D88 %A 2 5 3 !
73: CONST M5SI3_D88 : FE : SI : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): M5SI3_D88, type code %, sha256 `b0825ae47e316513…`

~~~~text
84: PHASE M5SI3_D88 % 2 5 3 !
85: CONST M5SI3_D88 : FE : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## FCC_A1 (Fe–Si)

- Id: `phase:fe-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1179.97–1696.48 K, x(Si) 0–0.03391
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:fcc-a1)

Names (6): _corpus: _corpus:phase:fe-si:fcc-a1  
_tdb: _tdb:FeSi-12Ohn.tdb:FCC_A1, tdb:FeSi-14Yua.tdb:FCC_A1, tdb:FeSi-17Cui.tdb:FCC_A1, tdb:FeSi-23Wit.tdb:FCC_A1, tdb:FeSi-91Lac-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): FCC_A1, type code %A, sha256 `e67d734746ab4b1c…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE SI : VA : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): FCC_A1, type code %A, sha256 `b45ac7c1e94df438…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE SI : VA : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): FCC_A1, type code %A, sha256 `93d3ce80d5ece2c2…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE SI : VA : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): FCC_A1, type code %A, sha256 `1860578382796878…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : FE SI : VA : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): FCC_A1, type code %A, sha256 `b0825ae47e316513…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_

## FE2SI (Fe–Si)

- Id: `phase:fe-si:fe2si`; status `assigned`
- Structure: AlNi2 · hP6 · P-3m1 (164); type `st:alni2-hp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 1315.83–1487.53 K, x(Si) 0.33333–0.3392
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:fe2si)

Names (8): _corpus: _corpus:phase:fe-si:fe2si  
_paper: _paper:10.1016/j.calphad.2013.07.007:Fe2Si, paper:10.1016/s0364-5916(98)00037-6:Fe2Si  
_tdb: _tdb:FeSi-12Ohn.tdb:FE2SI, tdb:FeSi-14Yua.tdb:FE2SI, tdb:FeSi-17Cui.tdb:FE2SI, tdb:FeSi-23Wit.tdb:FE2SI, tdb:FeSi-91Lac-LB.tdb:FE2SI  


### TDB models of FE2SI (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): FE2SI, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
67: PHASE FE2SI % 2 2 1 !
68: CONST FE2SI : FE : SI : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): FE2SI, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
60: PHASE FE2SI % 2 0.666667 0.333333 !
61: CONST FE2SI : FE : SI : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): FE2SI, type code %, sha256 `93d3ce80d5ece2c2…`

~~~~text
69: PHASE FE2SI % 2 2 1 !
70: CONST FE2SI : FE : SI : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): FE2SI, type code %, sha256 `1860578382796878…`

~~~~text
67: PHASE FE2SI % 3 1 1 1 !
68: CONST FE2SI : FE : FE VA : SI VA : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): FE2SI, type code %, sha256 `b0825ae47e316513…`

~~~~text
64: PHASE FE2SI % 2 2 1 !
65: CONST FE2SI : FE : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## FESI2_H (Fe–Si)

- Id: `phase:fe-si:fesi2-h`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:H; no_structure_token
- Candidate (sgte_mmc2): FeSi2-h · oC48 · Cmce (64) — Hallstedt 2025 mmc2 row for FESI2_H: FeSi2-h
- Candidate (tdb_comment): FeSi2-h · oC48 · Cmca — FeSi-12Ohn.tdb: 'Prototype FeSi2-h (oC48, Cmca)'
- Candidate (tdb_comment): FeSi2-h · oC48 · Cmca — FeSi-14Yua.tdb: 'Prototype FeSi2-h (oC48, Cmca)'
- Candidate (tdb_comment): FeSi2-h · oC48 · Cmca — FeSi-17Cui.tdb: 'Prototype FeSi2-h (oC48, Cmca)'
- Candidate (tdb_comment): FeSi2-h · oC48 · Cmca — FeSi-23Wit.tdb: 'Prototype FeSi2-h (oC48, Cmca)'
- Candidate (tdb_comment): FeSi2-h · oC48 · Cmca — FeSi-91Lac-LB.tdb: 'Prototype FeSi2-h (oC48, Cmca)'
- Stability: stable in 3 of 3 calculated diagram(s): 1209.55–1487 K, x(Si) 0.69809–0.71468
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:fesi2-h)

Names (8): _corpus: _corpus:phase:fe-si:fesi2-h  
_paper: _paper:10.1016/j.calphad.2013.07.007:FeSi2_H, paper:10.1016/s0364-5916(98)00037-6:FeSi2-H  
_tdb: _tdb:FeSi-12Ohn.tdb:FESI2_H, tdb:FeSi-14Yua.tdb:FESI2_H, tdb:FeSi-17Cui.tdb:FESI2_H, tdb:FeSi-23Wit.tdb:FESI2_H, tdb:FeSi-91Lac-LB.tdb:FESI2_H  


### TDB models of FESI2_H (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): FESI2_H, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
87: PHASE FESI2_H % 2 0.3 0.7 !
88: CONST FESI2_H : FE : SI : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): FESI2_H, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
75: PHASE FESI2_H % 2 0.3 0.7 !
76: CONST FESI2_H : FE : SI : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): FESI2_H, type code %, sha256 `93d3ce80d5ece2c2…`

~~~~text
89: PHASE FESI2_H % 2 3 7 !
90: CONST FESI2_H : FE : SI : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): FESI2_H, type code %, sha256 `1860578382796878…`

~~~~text
87: PHASE FESI2_H % 2 3 7 !
88: CONST FESI2_H : FE% SI : FE SI% : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): FESI2_H, type code %, sha256 `b0825ae47e316513…`

~~~~text
69: PHASE FESI2_H % 2 0.3 0.7 !
70: CONST FESI2_H : FE : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## FESI2_L (Fe–Si)

- Id: `phase:fe-si:fesi2-l`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:L; no_structure_token
- Candidate (dft_mp): Cmce (64) — on-hull MP FeSi2 at x(SI)=0.6667
- Candidate (dft_oqmd): Cmca (64) — on-hull OQMD Fe1 Si2 at x(SI)=0.6667
- Candidate (sgte_mmc2): FeSi2-l · tP3 · P4/mmm (123) — Hallstedt 2025 mmc2 row for FESI2_L: FeSi2-l
- Candidate (tdb_comment): FeSi2-l · tP3 · P4/mmm — FeSi-12Ohn.tdb: 'Prototype FeSi2-l (tP3, P4/mmm)'
- Candidate (tdb_comment): FeSi2-l · tP3 · P4/mmm — FeSi-14Yua.tdb: 'Prototype FeSi2-l (tP3, P4/mmm)'
- Candidate (tdb_comment): FeSi2-l · tP3 · P4/mmm — FeSi-17Cui.tdb: 'Prototype FeSi2-l (tP3, P4/mmm)'
- Candidate (tdb_comment): FeSi2-l · tP3 · P4/mmm — FeSi-23Wit.tdb: 'Prototype FeSi2-l (tP3, P4/mmm)'
- Candidate (tdb_comment): FeSi2-l · tP3 · P4/mmm — FeSi-91Lac-LB.tdb: 'Prototype FeSi2-l (tP3, P4/mmm)'
- Stoichiometry: Fe 0.3333, Si 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1275.67 K, x(Si) 0.66667–0.66667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:fesi2-l)

Names (7): _corpus: _corpus:phase:fe-si:fesi2-l  
_paper: _paper:10.1016/s0364-5916(98)00037-6:FeSi2-L  
_tdb: _tdb:FeSi-12Ohn.tdb:FESI2_L, tdb:FeSi-14Yua.tdb:FESI2_L, tdb:FeSi-17Cui.tdb:FESI2_L, tdb:FeSi-23Wit.tdb:FESI2_L, tdb:FeSi-91Lac-LB.tdb:FESI2_L  


### TDB models of FESI2_L (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): FESI2_L, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
82: PHASE FESI2_L % 2 1 2 !
83: CONST FESI2_L : FE : SI : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): FESI2_L, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
80: PHASE FESI2_L % 2 0.333333 0.666667 !
81: CONST FESI2_L : FE : SI : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): FESI2_L, type code %, sha256 `93d3ce80d5ece2c2…`

~~~~text
84: PHASE FESI2_L % 2 1 2 !
85: CONST FESI2_L : FE : SI : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): FESI2_L, type code %, sha256 `1860578382796878…`

~~~~text
82: PHASE FESI2_L % 2 1 2 !
83: CONST FESI2_L : FE : SI : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): FESI2_L, type code %, sha256 `b0825ae47e316513…`

~~~~text
74: PHASE FESI2_L % 2 1 2 !
75: CONST FESI2_L : FE : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## HCP_A3 (Fe–Si)

- Id: `phase:fe-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:hcp-a3)

Names (6): _corpus: _corpus:phase:fe-si:hcp-a3  
_tdb: _tdb:FeSi-12Ohn.tdb:HCP_A3, tdb:FeSi-14Yua.tdb:HCP_A3, tdb:FeSi-17Cui.tdb:HCP_A3, tdb:FeSi-23Wit.tdb:HCP_A3, tdb:FeSi-91Lac-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): HCP_A3, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
57: PHASE HCP_A3 % 2 1 0.5 !
58: CONST HCP_A3 : FE SI : VA : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): HCP_A3, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
50: PHASE HCP_A3 % 2 1 0.5 !
51: CONST HCP_A3 : FE SI : VA : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): HCP_A3, type code %, sha256 `93d3ce80d5ece2c2…`

~~~~text
59: PHASE HCP_A3 % 2 1 0.5 !
60: CONST HCP_A3 : FE SI : VA : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): HCP_A3, type code %, sha256 `1860578382796878…`

~~~~text
57: PHASE HCP_A3 % 2 1 0.5 !
58: CONST HCP_A3 : FE SI : VA : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): HCP_A3, type code %, sha256 `b0825ae47e316513…`

~~~~text
54: PHASE HCP_A3 % 2 1 0.5 !
55: CONST HCP_A3 : FE SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_

## LIQUID (Fe–Si)

- Id: `phase:fe-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1470.59–2500 K, x(Si) 0–1
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-si:liquid)

Names (8): _corpus: _corpus:phase:fe-si:liquid  
_paper: _paper:10.1016/j.calphad.2013.07.007:L, paper:10.1016/s0364-5916(98)00037-6:Liquid  
_tdb: _tdb:FeSi-12Ohn.tdb:LIQUID, tdb:FeSi-14Yua.tdb:LIQUID, tdb:FeSi-17Cui.tdb:LIQUID, tdb:FeSi-23Wit.tdb:LIQUID, tdb:FeSi-91Lac-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[FeSi-12Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-12Ohn.tdb): LIQUID, type code %, sha256 `e67d734746ab4b1c…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE SI : !
~~~~

[FeSi-14Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-14Yua.tdb): LIQUID, type code %, sha256 `b45ac7c1e94df438…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE SI : !
~~~~

[FeSi-17Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-17Cui.tdb): LIQUID, type code %, sha256 `93d3ce80d5ece2c2…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE SI : !
~~~~

[FeSi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-23Wit.tdb): LIQUID, type code %, sha256 `1860578382796878…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : FE SI : !
~~~~

[FeSi-91Lac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSi-91Lac-LB.tdb): LIQUID, type code %, sha256 `b0825ae47e316513…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : FE SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2013.07.007](https://doi.org/10.1016/j.calphad.2013.07.007) Yuan Yuan, Fusheng Pan, Dajian Li, Andrew Watson, The re-assessment of the Mg–Zn and Fe–Si systems and their incorporation in thermodynamic descriptions of the Al–Mg–Zn and Fe–Si–Zn systems, Calphad 44, 54-61 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991). Liquid modified by J. Miettinen 1998.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.11.003](https://doi.org/10.1016/j.calphad.2016.11.003) S. Cui, I.-H. Jung, Calphad, 56, 108-25(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.52.540](https://doi.org/10.2355/isijinternational.52.540) Ikuo Ohnuma, Shinya Abe, Shota Shimenouchi, Toshihiro Omori, Ryosuke Kainuma, Kiyohito Ishida, Experimental and Thermodynamic Studies of the Fe–Si Binary System, ISIJ Int. 52, 540-548 (2012).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

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
