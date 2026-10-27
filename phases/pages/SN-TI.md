# Sn–Ti phases

> Sn–Ti system: 13 phases (tier A 8, tier C 4, liquid 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SN-TI.html · Markdown: https://data.orchid-project.org/phases/pages/SN-TI.md

13 phases (tier A 8, tier C 4, liquid 1); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SN-TI) · [full JSON](https://data.orchid-project.org/phases/systems/SN-TI.json) · [Sn–Ti system page](https://data.orchid-project.org/systems/SN-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/SN-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sn–Ti system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sn-ti-a4-diamond); _phase:sn-ti:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [BCT_A5](#phase-sn-ti-a5-bct); _phase:sn-ti:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 4 of 5 calculated diagram(s): 300–505.08 K, x(Ti) 0–0 | 4 | 5 |
| [BCC_A2](#phase-sn-ti-bcc-a2); _phase:sn-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 504.51–1954.88 K, x(Ti) 0.152–1 | 2 | 5 |
| [FCC_A1](#phase-sn-ti-fcc-a1); _phase:sn-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-sn-ti-hcp-a3); _phase:sn-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1339.99 K, x(Ti) 0.88438–1 | 11 | 5 |
| [LIQUID](#phase-sn-ti-liquid); _phase:sn-ti:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 504.81–2500 K, x(Ti) 0–1 | 30 | 5 |
| [SN3TI2](#phase-sn-ti-sn3ti2); _phase:sn-ti:sn3ti2_ | Sn3Ti2 · oC40 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1028.43 K, x(Ti) 0.4–0.4 | 6 | 4 |
| [SN3TI5_D88](#phase-sn-ti-sn3ti5-d88); _phase:sn-ti:sn3ti5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1790 K, x(Ti) 0.62458–0.625 | 6 | 5 |
| [SN5TI6](#phase-sn-ti-sn5ti6); _phase:sn-ti:sn5ti6_ | Sn5Ti6-beta · hP22 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1762.33 K, x(Ti) 0.54545–0.54545 | 11 | 4 |
| [SN5TI6_ALPHA](#phase-sn-ti-sn5ti6-alpha); _phase:sn-ti:sn5ti6-alpha_ | Sn5Ti6-alpha · oI44 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–952.02 K, x(Ti) 0.54545–0.54545 | 0 | 1 |
| [SN5TI6_BETA](#phase-sn-ti-sn5ti6-beta); _phase:sn-ti:sn5ti6-beta_ | Sn5Ti6-beta · hP22 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 952.02–1774.8 K, x(Ti) 0.54545–0.54545 | 0 | 1 |
| [SNTI2_B82](#phase-sn-ti-snti2-b82); _phase:sn-ti:snti2-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1835.88 K, x(Ti) 0.64488–0.67263 | 6 | 5 |
| [SNTI3_D019](#phase-sn-ti-snti3-d019); _phase:sn-ti:snti3-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2500 K, x(Ti) 0–0.78452 | 17 | 5 |

## DIAMOND_A4 (Sn–Ti)

- Id: `phase:sn-ti:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:a4-diamond)

Names (6): _corpus: _corpus:phase:sn-ti:a4-diamond  
_tdb: _tdb:SnTi-05Liu.tdb:DIAMOND_A4, tdb:SnTi-07Yin.tdb:DIAMOND_A4, tdb:SnTi-11Wan.tdb:DIAMOND_A4, tdb:SnTi-19Tan.tdb:DIAMOND_A4, tdb:SnTi-98Hay-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): DIAMOND_A4, type code %, sha256 `1a9211ad13916936…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): DIAMOND_A4, type code %, sha256 `b2dedaccad25576a…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): DIAMOND_A4, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): DIAMOND_A4, type code %, sha256 `a09a2a0493b90176…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): DIAMOND_A4, type code %, sha256 `1a838be0ab839173…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## BCT_A5 (Sn–Ti)

- Id: `phase:sn-ti:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 5 calculated diagram(s): 300–505.08 K, x(Ti) 0–0
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:a5-bct)

Names (9): _corpus: _corpus:phase:sn-ti:a5-bct, corpus:phase:sn-ti:bct-a5  
_paper: _paper:10.1016/j.calphad.2007.01.003:(Sn), paper:sha256-85fd53a1a176b694:bct-A5  
_tdb: _tdb:SnTi-05Liu.tdb:BCT_A5, tdb:SnTi-07Yin.tdb:BCT_A5, tdb:SnTi-11Wan.tdb:BCT_A5, tdb:SnTi-19Tan.tdb:BCT_A5, tdb:SnTi-98Hay-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): BCT_A5, type code %, sha256 `1a9211ad13916936…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : SN% TI : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): BCT_A5, type code %, sha256 `b2dedaccad25576a…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN% TI : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): BCT_A5, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : SN% TI : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): BCT_A5, type code %, sha256 `a09a2a0493b90176…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : SN% TI : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): BCT_A5, type code %, sha256 `1a838be0ab839173…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : SN% TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## BCC_A2 (Sn–Ti)

- Id: `phase:sn-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 504.51–1954.88 K, x(Ti) 0.152–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:bcc-a2)

Names (7): _corpus: _corpus:phase:sn-ti:bcc-a2  
_paper: _paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:SnTi-05Liu.tdb:BCC_A2, tdb:SnTi-07Yin.tdb:BCC_A2, tdb:SnTi-11Wan.tdb:BCC_A2, tdb:SnTi-19Tan.tdb:BCC_A2, tdb:SnTi-98Hay-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): BCC_A2, type code %, sha256 `1a9211ad13916936…`

~~~~text
33: PHASE BCC_A2 % 2 1 3 !
34: CONST BCC_A2 : SN TI% : VA : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): BCC_A2, type code %, sha256 `b2dedaccad25576a…`

~~~~text
34: PHASE BCC_A2 % 2 1 3 !
35: CONST BCC_A2 : SN TI% : VA : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): BCC_A2, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
33: PHASE BCC_A2 % 2 1 3 !
34: CONST BCC_A2 : SN TI% : VA : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): BCC_A2, type code %, sha256 `a09a2a0493b90176…`

~~~~text
32: PHASE BCC_A2 % 2 1 3 !
33: CONST BCC_A2 : SN TI% : VA : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): BCC_A2, type code %, sha256 `1a838be0ab839173…`

~~~~text
32: PHASE BCC_A2 % 2 1 3 !
33: CONST BCC_A2 : SN TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## FCC_A1 (Sn–Ti)

- Id: `phase:sn-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:fcc-a1)

Names (6): _corpus: _corpus:phase:sn-ti:fcc-a1  
_tdb: _tdb:SnTi-05Liu.tdb:FCC_A1, tdb:SnTi-07Yin.tdb:FCC_A1, tdb:SnTi-11Wan.tdb:FCC_A1, tdb:SnTi-19Tan.tdb:FCC_A1, tdb:SnTi-98Hay-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): FCC_A1, type code %, sha256 `1a9211ad13916936…`

~~~~text
28: PHASE FCC_A1 % 2 1 1 !
29: CONST FCC_A1 : SN TI : VA : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): FCC_A1, type code %, sha256 `b2dedaccad25576a…`

~~~~text
29: PHASE FCC_A1 % 2 1 1 !
30: CONST FCC_A1 : SN TI : VA : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): FCC_A1, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
28: PHASE FCC_A1 % 2 1 1 !
29: CONST FCC_A1 : SN TI : VA : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): FCC_A1, type code %, sha256 `a09a2a0493b90176…`

~~~~text
27: PHASE FCC_A1 % 2 1 1 !
28: CONST FCC_A1 : SN TI : VA : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): FCC_A1, type code %, sha256 `1a838be0ab839173…`

~~~~text
27: PHASE FCC_A1 % 2 1 1 !
28: CONST FCC_A1 : SN TI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## HCP_A3 (Sn–Ti)

- Id: `phase:sn-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1339.99 K, x(Ti) 0.88438–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:hcp-a3)

Names (8): _corpus: _corpus:phase:sn-ti:hcp-a3  
_paper: _paper:10.1016/j.calphad.2007.01.003:(αTi), paper:sha256-85fd53a1a176b694:hcp-A3  
_tdb: _tdb:SnTi-05Liu.tdb:HCP_A3, tdb:SnTi-07Yin.tdb:HCP_A3, tdb:SnTi-11Wan.tdb:HCP_A3, tdb:SnTi-19Tan.tdb:HCP_A3, tdb:SnTi-98Hay-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): HCP_A3, type code %, sha256 `1a9211ad13916936…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : SN TI% : VA: !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): HCP_A3, type code %, sha256 `b2dedaccad25576a…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : SN TI% : VA: !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): HCP_A3, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : SN TI% : VA: !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): HCP_A3, type code %, sha256 `a09a2a0493b90176…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : SN TI% : VA: !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): HCP_A3, type code %, sha256 `1a838be0ab839173…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : SN TI% : VA: !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.04.010](https://doi.org/10.1016/j.jallcom.2005.04.010) A.A. Bondar, T.Ya. Velikanova, D.B. Borysov, L.V. Artyukh, O.O. Bilous, M.P. Burka et al., Titanium-boride eutectic materials: Phase equilibria and properties of alloys in the Ti-rich portion of the Ti–Sn–B system, Journal of Alloys and Compounds 400, 202-208 (2005).  
_cited as the source of values for this phase_

## LIQUID (Sn–Ti)

- Id: `phase:sn-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 504.81–2500 K, x(Ti) 0–1
- Literature: 30 values (30 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:liquid)

Names (9): _corpus: _corpus:phase:sn-ti:liquid  
_paper: _paper:10.1016/j.calphad.2007.01.003:L, paper:10.1016/j.calphad.2007.01.003:liquid, paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:SnTi-05Liu.tdb:LIQUID, tdb:SnTi-07Yin.tdb:LIQUID, tdb:SnTi-11Wan.tdb:LIQUID, tdb:SnTi-19Tan.tdb:LIQUID, tdb:SnTi-98Hay-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): LIQUID, type code %, sha256 `1a9211ad13916936…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SN TI : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): LIQUID, type code %, sha256 `b2dedaccad25576a…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SN TI : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): LIQUID, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SN TI : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): LIQUID, type code %, sha256 `a09a2a0493b90176…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : SN TI : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): LIQUID, type code %, sha256 `1a838be0ab839173…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : SN TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.04.010](https://doi.org/10.1016/j.jallcom.2005.04.010) A.A. Bondar, T.Ya. Velikanova, D.B. Borysov, L.V. Artyukh, O.O. Bilous, M.P. Burka et al., Titanium-boride eutectic materials: Phase equilibria and properties of alloys in the Ti-rich portion of the Ti–Sn–B system, Journal of Alloys and Compounds 400, 202-208 (2005).  
_cited as the source of values for this phase_

## SN3TI2 (Sn–Ti)

- Id: `phase:sn-ti:sn3ti2`; status `assigned`
- Structure: Sn3Ti2 · oC40 · Cmce (64); type `st:sn3ti2-oc40`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_64_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.6000, Ti 0.4000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1028.43 K, x(Ti) 0.4–0.4
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:sn3ti2)

Names (7): _corpus: _corpus:phase:sn-ti:sn3ti2  
_paper: _paper:10.1007/s00706-005-0392-x:Sn3Ti2, paper:10.1016/j.calphad.2007.01.003:Ti2Sn3  
_tdb: _tdb:SnTi-05Liu.tdb:SN3TI2, tdb:SnTi-07Yin.tdb:SN3TI2, tdb:SnTi-11Wan.tdb:SN3TI2, tdb:SnTi-19Tan.tdb:SN3TI2  


### TDB models of SN3TI2 (4): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): SN3TI2, type code %, sha256 `1a9211ad13916936…`

~~~~text
53: PHASE SN3TI2 %  2 3 2 !
54: CONST SN3TI2 : SN : TI : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): SN3TI2, type code %, sha256 `b2dedaccad25576a…`

~~~~text
54: PHASE SN3TI2 %  2 3 2 !
55: CONST SN3TI2 : SN : TI : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): SN3TI2, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
53: PHASE SN3TI2 %  2 3 2 !
54: CONST SN3TI2 : SN : TI : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): SN3TI2, type code %, sha256 `a09a2a0493b90176…`

~~~~text
52: PHASE SN3TI2 %  2 3 2 !
53: CONST SN3TI2 : SN : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## SN3TI5_D88 (Sn–Ti)

- Id: `phase:sn-ti:sn3ti5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1790 K, x(Ti) 0.62458–0.625
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:sn3ti5-d88)

Names (8): _corpus: _corpus:phase:sn-ti:sn3ti5-d88  
_paper: _paper:10.1016/j.calphad.2007.01.003:Ti5Sn3, paper:sha256-85fd53a1a176b694:Sn3Ti5  
_tdb: _tdb:SnTi-05Liu.tdb:SN3TI5_D88, tdb:SnTi-07Yin.tdb:SN3TI5_D88, tdb:SnTi-11Wan.tdb:SN3TI5_D88, tdb:SnTi-19Tan.tdb:SN3TI5_D88, tdb:SnTi-98Hay-LB.tdb:SN3TI5_D88  


### TDB models of SN3TI5_D88 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): SN3TI5_D88, type code %, sha256 `1a9211ad13916936…`

~~~~text
68: PHASE SN3TI5_D88 %  2 3 5 !
69: CONST SN3TI5_D88 : SN : TI : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): SN3TI5_D88, type code %, sha256 `b2dedaccad25576a…`

~~~~text
65: PHASE SN3TI5_D88 %  2 3 5 !
66: CONST SN3TI5_D88 : SN : TI : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): SN3TI5_D88, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
64: PHASE SN3TI5_D88 %  3 1 3 5 !
65: CONST SN3TI5_D88 : VA : SN : TI : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): SN3TI5_D88, type code %, sha256 `a09a2a0493b90176…`

~~~~text
63: PHASE SN3TI5_D88 %  3 1 3 5 !
64: CONST SN3TI5_D88 : SN VA% : SN : TI : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): SN3TI5_D88, type code %, sha256 `1a838be0ab839173…`

~~~~text
57: PHASE SN3TI5_D88 %  2 3 5 !
58: CONST SN3TI5_D88 : SN : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## SN5TI6 (Sn–Ti)

- Id: `phase:sn-ti:sn5ti6`; status `assigned`
- Structure: Sn5Ti6-beta · hP22 · P6_3/mmc (194); type `st:sn5ti6-beta-hp22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.4545, Ti 0.5455
- Stability: stable in 4 of 4 calculated diagram(s): 300–1762.33 K, x(Ti) 0.54545–0.54545
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:sn5ti6)

Names (7): _corpus: _corpus:phase:sn-ti:sn5ti6  
_paper: _paper:10.1016/j.calphad.2007.01.003:Ti6Sn5, paper:sha256-85fd53a1a176b694:Sn5Ti6  
_tdb: _tdb:SnTi-07Yin.tdb:SN5TI6, tdb:SnTi-11Wan.tdb:SN5TI6, tdb:SnTi-19Tan.tdb:SN5TI6, tdb:SnTi-98Hay-LB.tdb:SN5TI6  


### TDB models of SN5TI6 (4): PHASE and CONSTITUENT statements as written

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): SN5TI6, type code %, sha256 `b2dedaccad25576a…`

~~~~text
60: PHASE SN5TI6 %  2 5 6 !
61: CONST SN5TI6 : SN : TI : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): SN5TI6, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
59: PHASE SN5TI6 %  2 5 6 !
60: CONST SN5TI6 : SN : TI : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): SN5TI6, type code %, sha256 `a09a2a0493b90176…`

~~~~text
58: PHASE SN5TI6 %  2 5 6 !
59: CONST SN5TI6 : SN : TI : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): SN5TI6, type code %, sha256 `1a838be0ab839173…`

~~~~text
52: PHASE SN5TI6 %  2 5 6 !
53: CONST SN5TI6 : SN : TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## SN5TI6_ALPHA (Sn–Ti)

- Id: `phase:sn-ti:sn5ti6-alpha`; status `assigned`
- Structure: Sn5Ti6-alpha · oI44 · Immm (71); type `st:sn5ti6-alpha-oi44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.4545, Ti 0.5455
- Stability: stable in 1 of 1 calculated diagram(s): 300–952.02 K, x(Ti) 0.54545–0.54545
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:sn5ti6-alpha)

Names (2): _corpus: _corpus:phase:sn-ti:sn5ti6-alpha  
_tdb: _tdb:SnTi-05Liu.tdb:SN5TI6_ALPHA  


### TDB models of SN5TI6_ALPHA (1): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): SN5TI6_ALPHA, type code %, sha256 `1a9211ad13916936…`

~~~~text
58: PHASE SN5TI6_ALPHA %  2 5 6 !
59: CONST SN5TI6_ALPHA : SN : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_

## SN5TI6_BETA (Sn–Ti)

- Id: `phase:sn-ti:sn5ti6-beta`; status `assigned`
- Structure: Sn5Ti6-beta · hP22 · P6_3/mmc (194); type `st:sn5ti6-beta-hp22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.4545, Ti 0.5455
- Stability: stable in 1 of 1 calculated diagram(s): 952.02–1774.8 K, x(Ti) 0.54545–0.54545
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:sn5ti6-beta)

Names (2): _corpus: _corpus:phase:sn-ti:sn5ti6-beta  
_tdb: _tdb:SnTi-05Liu.tdb:SN5TI6_BETA  


### TDB models of SN5TI6_BETA (1): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): SN5TI6_BETA, type code %, sha256 `1a9211ad13916936…`

~~~~text
63: PHASE SN5TI6_BETA %  2 5 6 !
64: CONST SN5TI6_BETA : SN : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_

## SNTI2_B82 (Sn–Ti)

- Id: `phase:sn-ti:snti2-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in SnTi-19Tan.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1835.88 K, x(Ti) 0.64488–0.67263
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:snti2-b82)

Names (8): _corpus: _corpus:phase:sn-ti:snti2-b82  
_paper: _paper:10.1016/j.calphad.2007.01.003:Ti2Sn, paper:sha256-85fd53a1a176b694:SnTi2  
_tdb: _tdb:SnTi-05Liu.tdb:SNTI2_B82, tdb:SnTi-07Yin.tdb:SNTI2_B82, tdb:SnTi-11Wan.tdb:SNTI2_B82, tdb:SnTi-19Tan.tdb:SNTI2_B82, tdb:SnTi-98Hay-LB.tdb:SNTI2_B82  


### TDB models of SNTI2_B82 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): SNTI2_B82, type code %, sha256 `1a9211ad13916936…`

~~~~text
73: PHASE SNTI2_B82 %  2 1 2 !
74: CONST SNTI2_B82 : SN : TI : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): SNTI2_B82, type code %, sha256 `b2dedaccad25576a…`

~~~~text
70: PHASE SNTI2_B82 %  2 1 2 !
71: CONST SNTI2_B82 : SN% VA : TI% VA : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): SNTI2_B82, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
69: PHASE SNTI2_B82 %  3 1 1 1 !
70: CONST SNTI2_B82 : SN% TI : TI : TI% VA : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): SNTI2_B82, type code %, sha256 `a09a2a0493b90176…`

~~~~text
68: PHASE SNTI2_B82 %  2 1 2 !
69: CONST SNTI2_B82 : SN% TI : SN TI% : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): SNTI2_B82, type code %, sha256 `1a838be0ab839173…`

~~~~text
62: PHASE SNTI2_B82 %  2 1 2 !
63: CONST SNTI2_B82 : SN : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_

## SNTI3_D019 (Sn–Ti)

- Id: `phase:sn-ti:snti3-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in SnTi-05Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SnTi-11Wan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SnTi-19Tan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SnTi-98Hay-LB.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–2500 K, x(Ti) 0–0.78452
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-ti:snti3-d019)

Names (8): _corpus: _corpus:phase:sn-ti:snti3-d019  
_paper: _paper:10.1016/j.calphad.2007.01.003:Ti3Sn, paper:sha256-85fd53a1a176b694:SnTi3  
_tdb: _tdb:SnTi-05Liu.tdb:SNTI3_D019, tdb:SnTi-07Yin.tdb:SNTI3_D019, tdb:SnTi-11Wan.tdb:SNTI3_D019, tdb:SnTi-19Tan.tdb:SNTI3_D019, tdb:SnTi-98Hay-LB.tdb:SNTI3_D019  


### TDB models of SNTI3_D019 (5): PHASE and CONSTITUENT statements as written

[SnTi-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-05Liu.tdb): SNTI3_D019, type code %, sha256 `1a9211ad13916936…`

~~~~text
78: PHASE SNTI3_D019 %  2 1 3 !
79: CONST SNTI3_D019 : SN% TI : SN TI% : !
~~~~

[SnTi-07Yin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-07Yin.tdb): SNTI3_D019, type code %, sha256 `b2dedaccad25576a…`

~~~~text
75: PHASE SNTI3_D019 %  2 1 3 !
76: CONST SNTI3_D019 : SN% VA : TI : !
~~~~

[SnTi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-11Wan.tdb): SNTI3_D019, type code %, sha256 `f212f46d607d7fcf…`

~~~~text
74: PHASE SNTI3_D019 %  2 1 3 !
75: CONST SNTI3_D019 : SN% TI : SN TI% : !
~~~~

[SnTi-19Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-19Tan.tdb): SNTI3_D019, type code %, sha256 `a09a2a0493b90176…`

~~~~text
73: PHASE SNTI3_D019 %  2 1 3 !
74: CONST SNTI3_D019 : SN% TI : SN TI% : !
~~~~

[SnTi-98Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTi-98Hay-LB.tdb): SNTI3_D019, type code %, sha256 `1a838be0ab839173…`

~~~~text
67: PHASE SNTI3_D019 %  2 1 3 !
68: CONST SNTI3_D019 : SN% TI : SN TI% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2007.01.003](https://doi.org/10.1016/j.calphad.2007.01.003) Fucheng Yin, Jean-Claude Tedenac, Franck Gascoin, Thermodynamic modelling of the Ti–Sn system and calculation of the Co–Ti–Sn system, Calphad 31, 370-379 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s00706-005-0392-x](https://doi.org/10.1007/s00706-005-0392-x) Chunlei Liu, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Thermodynamic Assessment of the Sn–Ti System, Monatsh. Chem. 136, 1921-1930 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.12.006](https://doi.org/10.1016/j.calphad.2010.12.006) Jiang Wang, Chunlei Liu, Christian Leinenbach, Ulrich E. Klotz, Peter J. Uggowitzer, Jörg F. Löffler, Experimental investigation and thermodynamic assessment of the Cu–Sn–Ti ternary system, Calphad 35, 82-94 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101686](https://doi.org/10.1016/j.calphad.2019.101686) J. Tan, G. Xu, X. Tao, F. Chen, Y. Cui, L. Zhou, Calphad, 67, 101686(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.04.010](https://doi.org/10.1016/j.jallcom.2005.04.010) A.A. Bondar, T.Ya. Velikanova, D.B. Borysov, L.V. Artyukh, O.O. Bilous, M.P. Burka et al., Titanium-boride eutectic materials: Phase equilibria and properties of alloys in the Ti-rich portion of the Ti–Sn–B system, Journal of Alloys and Compounds 400, 202-208 (2005).  
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
