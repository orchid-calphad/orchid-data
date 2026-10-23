# Bi–Sn phases

> Bi–Sn system: 7 phases (tier A 6, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-SN.html · Markdown: https://data.orchid-project.org/phases/pages/BI-SN.md

7 phases (tier A 6, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-SN) · [full JSON](https://data.orchid-project.org/phases/systems/BI-SN.json) · [Bi–Sn system page](https://data.orchid-project.org/systems/BI-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Sn system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-bi-sn-a4-diamond); _phase:bi-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [BCT_A5](#phase-bi-sn-a5-bct); _phase:bi-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–650.08 K, x(Sn) 0.83805–1 | 0 | 6 |
| [RHOMBOHEDRAL_A7](#phase-bi-sn-a7-rhombohedral); _phase:bi-sn:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–544.55 K, x(Sn) 0–0.06933 | 0 | 6 |
| [BCC_A2](#phase-bi-sn-bcc-a2); _phase:bi-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [FCC_A1](#phase-bi-sn-fcc-a1); _phase:bi-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [HCP_A3](#phase-bi-sn-hcp-a3); _phase:bi-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-bi-sn-liquid); _phase:bi-sn:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 411.51–2500 K, x(Sn) 0–1 | 0 | 6 |

## DIAMOND_A4 (Bi–Sn)

- Id: `phase:bi-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-sn:a4-diamond)

Names (7): _corpus: _corpus:phase:bi-sn:a4-diamond  
_tdb: _tdb:BiSn-07Viz.tdb:DIAMOND_A4, tdb:BiSn-08Li.tdb:DIAMOND_A4, tdb:BiSn-80Che.tdb:DIAMOND_A4, tdb:BiSn-94Kat.tdb:DIAMOND_A4, tdb:BiSn-94Oht-LB.tdb:DIAMOND_A4, tdb:BiSn-96Lee.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (6): PHASE and CONSTITUENT statements as written

[BiSn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-07Viz.tdb): DIAMOND_A4, type code %, sha256 `9e4059d48e86c005…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

[BiSn-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-08Li.tdb): DIAMOND_A4, type code %, sha256 `6265b534330c58e5…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

[BiSn-80Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-80Che.tdb): DIAMOND_A4, type code %, sha256 `a9c046d1a43fa5f2…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

[BiSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Kat.tdb): DIAMOND_A4, type code %, sha256 `82389ac2c0ef4c47…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SN : !
~~~~

[BiSn-94Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Oht-LB.tdb): DIAMOND_A4, type code %, sha256 `6a2b00e5e43a3110…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

[BiSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-96Lee.tdb): DIAMOND_A4, type code %, sha256 `fc1597e2aacca982…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02651369](https://doi.org/10.1007/BF02651369) H. Ohtani, K. Ishida, J. Electron. Mater., 23, 747-55 (1994).  
_assessment that models this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.07.008](https://doi.org/10.1016/j.calphad.2007.07.008) Zuoan Li, Zhanmin Cao, Sabine Knott, Adolf Mikula, Yong Du, Zhiyu Qiao, Thermodynamic investigation of the Ag–Bi–Sn ternary system, Calphad 32, 152-163 (2008).  
_assessment that models this phase_

## BCT_A5 (Bi–Sn)

- Id: `phase:bi-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–650.08 K, x(Sn) 0.83805–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-sn:a5-bct)

Names (7): _corpus: _corpus:phase:bi-sn:a5-bct  
_tdb: _tdb:BiSn-07Viz.tdb:BCT_A5, tdb:BiSn-08Li.tdb:BCT_A5, tdb:BiSn-80Che.tdb:BCT_A5, tdb:BiSn-94Kat.tdb:BCT_A5, tdb:BiSn-94Oht-LB.tdb:BCT_A5, tdb:BiSn-96Lee.tdb:BCT_A5  


### TDB models of BCT_A5 (6): PHASE and CONSTITUENT statements as written

[BiSn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-07Viz.tdb): BCT_A5, type code %, sha256 `9e4059d48e86c005…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : BI SN% : !
~~~~

[BiSn-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-08Li.tdb): BCT_A5, type code %, sha256 `6265b534330c58e5…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : BI SN% : !
~~~~

[BiSn-80Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-80Che.tdb): BCT_A5, type code %, sha256 `a9c046d1a43fa5f2…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : BI SN% : !
~~~~

[BiSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Kat.tdb): BCT_A5, type code %, sha256 `82389ac2c0ef4c47…`

~~~~text
45: PHASE BCT_A5 % 1 1 !
46: CONST BCT_A5 : BI SN% : !
~~~~

[BiSn-94Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Oht-LB.tdb): BCT_A5, type code %, sha256 `6a2b00e5e43a3110…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : BI SN% : !
~~~~

[BiSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-96Lee.tdb): BCT_A5, type code %, sha256 `fc1597e2aacca982…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : BI SN% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02651369](https://doi.org/10.1007/BF02651369) H. Ohtani, K. Ishida, J. Electron. Mater., 23, 747-55 (1994).  
_assessment that models this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.07.008](https://doi.org/10.1016/j.calphad.2007.07.008) Zuoan Li, Zhanmin Cao, Sabine Knott, Adolf Mikula, Yong Du, Zhiyu Qiao, Thermodynamic investigation of the Ag–Bi–Sn ternary system, Calphad 32, 152-163 (2008).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (Bi–Sn)

- Id: `phase:bi-sn:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–544.55 K, x(Sn) 0–0.06933
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-sn:a7-rhombohedral)

Names (7): _corpus: _corpus:phase:bi-sn:a7-rhombohedral  
_tdb: _tdb:BiSn-07Viz.tdb:RHOMBOHEDRAL_A7, tdb:BiSn-08Li.tdb:RHOMBOHEDRAL_A7, tdb:BiSn-80Che.tdb:RHOMBOHEDRAL_A7, tdb:BiSn-94Kat.tdb:RHOMBOHEDRAL_A7, tdb:BiSn-94Oht-LB.tdb:RHOMBOHEDRAL_A7, tdb:BiSn-96Lee.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (6): PHASE and CONSTITUENT statements as written

[BiSn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-07Viz.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9e4059d48e86c005…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : BI% SN : !
~~~~

[BiSn-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-08Li.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6265b534330c58e5…`

~~~~text
52: PHASE RHOMBOHEDRAL_A7 % 1 1 !
53: CONST RHOMBOHEDRAL_A7 : BI% SN : !
~~~~

[BiSn-80Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-80Che.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `a9c046d1a43fa5f2…`

~~~~text
55: PHASE RHOMBOHEDRAL_A7 % 1 1 !
56: CONST RHOMBOHEDRAL_A7 : BI% SN : !
~~~~

[BiSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Kat.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `82389ac2c0ef4c47…`

~~~~text
50: PHASE RHOMBOHEDRAL_A7 % 1 1 !
51: CONST RHOMBOHEDRAL_A7 : BI% SN : !
~~~~

[BiSn-94Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Oht-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6a2b00e5e43a3110…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : BI% SN : !
~~~~

[BiSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-96Lee.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `fc1597e2aacca982…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : BI% SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02651369](https://doi.org/10.1007/BF02651369) H. Ohtani, K. Ishida, J. Electron. Mater., 23, 747-55 (1994).  
_assessment that models this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.07.008](https://doi.org/10.1016/j.calphad.2007.07.008) Zuoan Li, Zhanmin Cao, Sabine Knott, Adolf Mikula, Yong Du, Zhiyu Qiao, Thermodynamic investigation of the Ag–Bi–Sn ternary system, Calphad 32, 152-163 (2008).  
_assessment that models this phase_

## BCC_A2 (Bi–Sn)

- Id: `phase:bi-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-sn:bcc-a2)

Names (7): _corpus: _corpus:phase:bi-sn:bcc-a2  
_tdb: _tdb:BiSn-07Viz.tdb:BCC_A2, tdb:BiSn-08Li.tdb:BCC_A2, tdb:BiSn-80Che.tdb:BCC_A2, tdb:BiSn-94Kat.tdb:BCC_A2, tdb:BiSn-94Oht-LB.tdb:BCC_A2, tdb:BiSn-96Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[BiSn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-07Viz.tdb): BCC_A2, type code %B, sha256 `9e4059d48e86c005…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI SN : VA : !
~~~~

[BiSn-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-08Li.tdb): BCC_A2, type code %B, sha256 `6265b534330c58e5…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : BI SN : VA : !
~~~~

[BiSn-80Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-80Che.tdb): BCC_A2, type code %B, sha256 `a9c046d1a43fa5f2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI SN : VA : !
~~~~

[BiSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Kat.tdb): BCC_A2, type code %B, sha256 `82389ac2c0ef4c47…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : BI SN : VA : !
~~~~

[BiSn-94Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Oht-LB.tdb): BCC_A2, type code %B, sha256 `6a2b00e5e43a3110…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI SN : VA : !
~~~~

[BiSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-96Lee.tdb): BCC_A2, type code %B, sha256 `fc1597e2aacca982…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI SN : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02651369](https://doi.org/10.1007/BF02651369) H. Ohtani, K. Ishida, J. Electron. Mater., 23, 747-55 (1994).  
_assessment that models this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.07.008](https://doi.org/10.1016/j.calphad.2007.07.008) Zuoan Li, Zhanmin Cao, Sabine Knott, Adolf Mikula, Yong Du, Zhiyu Qiao, Thermodynamic investigation of the Ag–Bi–Sn ternary system, Calphad 32, 152-163 (2008).  
_assessment that models this phase_

## FCC_A1 (Bi–Sn)

- Id: `phase:bi-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-sn:fcc-a1)

Names (7): _corpus: _corpus:phase:bi-sn:fcc-a1  
_tdb: _tdb:BiSn-07Viz.tdb:FCC_A1, tdb:BiSn-08Li.tdb:FCC_A1, tdb:BiSn-80Che.tdb:FCC_A1, tdb:BiSn-94Kat.tdb:FCC_A1, tdb:BiSn-94Oht-LB.tdb:FCC_A1, tdb:BiSn-96Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[BiSn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-07Viz.tdb): FCC_A1, type code %A, sha256 `9e4059d48e86c005…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI SN : VA : !
~~~~

[BiSn-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-08Li.tdb): FCC_A1, type code %A, sha256 `6265b534330c58e5…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BI SN : VA : !
~~~~

[BiSn-80Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-80Che.tdb): FCC_A1, type code %A, sha256 `a9c046d1a43fa5f2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI SN : VA : !
~~~~

[BiSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Kat.tdb): FCC_A1, type code %A, sha256 `82389ac2c0ef4c47…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : BI SN : VA : !
~~~~

[BiSn-94Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Oht-LB.tdb): FCC_A1, type code %A, sha256 `6a2b00e5e43a3110…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI SN : VA : !
~~~~

[BiSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-96Lee.tdb): FCC_A1, type code %A, sha256 `fc1597e2aacca982…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI SN : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02651369](https://doi.org/10.1007/BF02651369) H. Ohtani, K. Ishida, J. Electron. Mater., 23, 747-55 (1994).  
_assessment that models this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.07.008](https://doi.org/10.1016/j.calphad.2007.07.008) Zuoan Li, Zhanmin Cao, Sabine Knott, Adolf Mikula, Yong Du, Zhiyu Qiao, Thermodynamic investigation of the Ag–Bi–Sn ternary system, Calphad 32, 152-163 (2008).  
_assessment that models this phase_

## HCP_A3 (Bi–Sn)

- Id: `phase:bi-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-sn:hcp-a3)

Names (7): _corpus: _corpus:phase:bi-sn:hcp-a3  
_tdb: _tdb:BiSn-07Viz.tdb:HCP_A3, tdb:BiSn-08Li.tdb:HCP_A3, tdb:BiSn-80Che.tdb:HCP_A3, tdb:BiSn-94Kat.tdb:HCP_A3, tdb:BiSn-94Oht-LB.tdb:HCP_A3, tdb:BiSn-96Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[BiSn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-07Viz.tdb): HCP_A3, type code %A, sha256 `9e4059d48e86c005…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI SN : VA: !
~~~~

[BiSn-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-08Li.tdb): HCP_A3, type code %A, sha256 `6265b534330c58e5…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : BI SN : VA: !
~~~~

[BiSn-80Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-80Che.tdb): HCP_A3, type code %A, sha256 `a9c046d1a43fa5f2…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI SN : VA: !
~~~~

[BiSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Kat.tdb): HCP_A3, type code %A, sha256 `82389ac2c0ef4c47…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : BI SN : VA: !
~~~~

[BiSn-94Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Oht-LB.tdb): HCP_A3, type code %A, sha256 `6a2b00e5e43a3110…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI SN : VA: !
~~~~

[BiSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-96Lee.tdb): HCP_A3, type code %A, sha256 `fc1597e2aacca982…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI SN : VA: !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02651369](https://doi.org/10.1007/BF02651369) H. Ohtani, K. Ishida, J. Electron. Mater., 23, 747-55 (1994).  
_assessment that models this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.07.008](https://doi.org/10.1016/j.calphad.2007.07.008) Zuoan Li, Zhanmin Cao, Sabine Knott, Adolf Mikula, Yong Du, Zhiyu Qiao, Thermodynamic investigation of the Ag–Bi–Sn ternary system, Calphad 32, 152-163 (2008).  
_assessment that models this phase_

## LIQUID (Bi–Sn)

- Id: `phase:bi-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 411.51–2500 K, x(Sn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-sn:liquid)

Names (7): _corpus: _corpus:phase:bi-sn:liquid  
_tdb: _tdb:BiSn-07Viz.tdb:LIQUID, tdb:BiSn-08Li.tdb:LIQUID, tdb:BiSn-80Che.tdb:LIQUID, tdb:BiSn-94Kat.tdb:LIQUID, tdb:BiSn-94Oht-LB.tdb:LIQUID, tdb:BiSn-96Lee.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[BiSn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-07Viz.tdb): LIQUID, type code %, sha256 `9e4059d48e86c005…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI SN : !
~~~~

[BiSn-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-08Li.tdb): LIQUID, type code %, sha256 `6265b534330c58e5…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BI SN : !
~~~~

[BiSn-80Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-80Che.tdb): LIQUID, type code %, sha256 `a9c046d1a43fa5f2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI SN : !
~~~~

[BiSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Kat.tdb): LIQUID, type code %, sha256 `82389ac2c0ef4c47…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : BI SN : !
~~~~

[BiSn-94Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-94Oht-LB.tdb): LIQUID, type code %, sha256 `6a2b00e5e43a3110…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI SN : !
~~~~

[BiSn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSn-96Lee.tdb): LIQUID, type code %, sha256 `fc1597e2aacca982…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02651369](https://doi.org/10.1007/BF02651369) H. Ohtani, K. Ishida, J. Electron. Mater., 23, 747-55 (1994).  
_assessment that models this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/BF02666734](https://doi.org/10.1007/BF02666734) B.-J. Lee, C.-S. Oh, J.-H. Shim, J. Electron. Mater., 25, 983-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.07.008](https://doi.org/10.1016/j.calphad.2007.07.008) Zuoan Li, Zhanmin Cao, Sabine Knott, Adolf Mikula, Yong Du, Zhiyu Qiao, Thermodynamic investigation of the Ag–Bi–Sn ternary system, Calphad 32, 152-163 (2008).  
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
