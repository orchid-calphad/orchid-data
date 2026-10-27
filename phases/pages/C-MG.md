# C–Mg phases

> C–Mg system: 9 phases (tier A 5, tier C 2, liquid 1, gas 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-MG.html · Markdown: https://data.orchid-project.org/phases/pages/C-MG.md

9 phases (tier A 5, tier C 2, liquid 1, gas 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-MG) · [full JSON](https://data.orchid-project.org/phases/systems/C-MG.json) · [Markdown](https://data.orchid-project.org/phases/pages/C-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Mg system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-mg-a4-diamond); _phase:c-mg:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GRAPHITE_A9](#phase-c-mg-a9-graphite); _phase:c-mg:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.5 K, x(C) 1–1 | 0 | 3 |
| [BCC_A2](#phase-c-mg-bcc-a2); _phase:c-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-c-mg-fcc-a1); _phase:c-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-c-mg-gas); _phase:c-mg:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 1367.53–4000 K, x(C) 0–1 | 0 | 3 |
| [HCP_A3](#phase-c-mg-hcp-a3); _phase:c-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.54 K, x(C) 0–0.0001 | 0 | 3 |
| [LIQUID](#phase-c-mg-liquid); _phase:c-mg:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 688.82–3999.54 K, x(C) 0–0.25128 | 0 | 3 |
| [MG2C3](#phase-c-mg-mg2c3); _phase:c-mg:mg2c3_ | Mg2C3 · oP10 · Pnnm (58) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 3 calculated diagram(s): 300–930.23 K, x(C) 0.6–0.6 | 0 | 3 |
| [MGC2](#phase-c-mg-mgc2); _phase:c-mg:mgc2_ | MgC2 · tP6 · P4_2/mnm (136) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 3 calculated diagram(s): 300–869.96 K, x(C) 0.66667–0.66667 | 0 | 3 |

## DIAMOND_A4 (C–Mg)

- Id: `phase:c-mg:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:a4-diamond)

Names (4): _corpus: _corpus:phase:c-mg:a4-diamond  
_tdb: _tdb:MgC-06Hal.tdb:DIAMOND_A4, tdb:MgC-10Hu.tdb:DIAMOND_A4, tdb:MgC-12Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): DIAMOND_A4, type code %, sha256 `cdafe04b706df3aa…`

~~~~text
56: PHASE DIAMOND_A4 % 1 1 !
57: CONST DIAMOND_A4 : C : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): DIAMOND_A4, type code %, sha256 `2ed80eae8ee075a6…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : C : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): DIAMOND_A4, type code %, sha256 `662147a17bbe63f9…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Mg)

- Id: `phase:c-mg:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.5 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:a9-graphite)

Names (4): _corpus: _corpus:phase:c-mg:a9-graphite  
_tdb: _tdb:MgC-06Hal.tdb:GRAPHITE_A9, tdb:MgC-10Hu.tdb:GRAPHITE_A9, tdb:MgC-12Che.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): GRAPHITE_A9, type code %, sha256 `cdafe04b706df3aa…`

~~~~text
61: PHASE GRAPHITE_A9 % 1 1 !
62: CONST GRAPHITE_A9 : C : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): GRAPHITE_A9, type code %, sha256 `2ed80eae8ee075a6…`

~~~~text
57: PHASE GRAPHITE_A9 % 1 1 !
58: CONST GRAPHITE_A9 : C : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): GRAPHITE_A9, type code %, sha256 `662147a17bbe63f9…`

~~~~text
57: PHASE GRAPHITE_A9 % 1 1 !
58: CONST GRAPHITE_A9 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## BCC_A2 (C–Mg)

- Id: `phase:c-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:bcc-a2)

Names (4): _corpus: _corpus:phase:c-mg:bcc-a2  
_tdb: _tdb:MgC-06Hal.tdb:BCC_A2, tdb:MgC-10Hu.tdb:BCC_A2, tdb:MgC-12Che.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): BCC_A2, type code %B, sha256 `cdafe04b706df3aa…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : MG : C VA% : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): BCC_A2, type code %B, sha256 `2ed80eae8ee075a6…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : MG : C VA% : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): BCC_A2, type code %B, sha256 `662147a17bbe63f9…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : MG : C VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## FCC_A1 (C–Mg)

- Id: `phase:c-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:fcc-a1)

Names (4): _corpus: _corpus:phase:c-mg:fcc-a1  
_tdb: _tdb:MgC-06Hal.tdb:FCC_A1, tdb:MgC-10Hu.tdb:FCC_A1, tdb:MgC-12Che.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): FCC_A1, type code %A, sha256 `cdafe04b706df3aa…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : MG : C VA% : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): FCC_A1, type code %A, sha256 `2ed80eae8ee075a6…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : MG : C VA% : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): FCC_A1, type code %A, sha256 `662147a17bbe63f9…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : MG : C VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## GAS (C–Mg)

- Id: `phase:c-mg:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1367.53–4000 K, x(C) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:gas)

Names (4): _corpus: _corpus:phase:c-mg:gas  
_tdb: _tdb:MgC-06Hal.tdb:GAS, tdb:MgC-10Hu.tdb:GAS, tdb:MgC-12Che.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): GAS, type code %, sha256 `cdafe04b706df3aa…`

~~~~text
74: PHASE GAS:G % 1 1 !
75: CONST GAS:G : C C2 C3 C4 C5 C60 MG MG2 : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): GAS, type code %, sha256 `2ed80eae8ee075a6…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : C C2 C3 C4 C5 C60 MG MG2 : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): GAS, type code %, sha256 `662147a17bbe63f9…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : C C2 C3 C4 C5 C60 MG MG2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## HCP_A3 (C–Mg)

- Id: `phase:c-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.54 K, x(C) 0–0.0001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:hcp-a3)

Names (4): _corpus: _corpus:phase:c-mg:hcp-a3  
_tdb: _tdb:MgC-06Hal.tdb:HCP_A3, tdb:MgC-10Hu.tdb:HCP_A3, tdb:MgC-12Che.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): HCP_A3, type code %, sha256 `cdafe04b706df3aa…`

~~~~text
51: PHASE HCP_A3 % 2 1 0.5 !
52: CONST HCP_A3 : MG% : C VA% : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): HCP_A3, type code %, sha256 `2ed80eae8ee075a6…`

~~~~text
47: PHASE HCP_A3 % 2 1 0.5 !
48: CONST HCP_A3 : MG% : C VA% : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): HCP_A3, type code %, sha256 `662147a17bbe63f9…`

~~~~text
47: PHASE HCP_A3 % 2 1 0.5 !
48: CONST HCP_A3 : MG% : C VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## LIQUID (C–Mg)

- Id: `phase:c-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 688.82–3999.54 K, x(C) 0–0.25128
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:liquid)

Names (4): _corpus: _corpus:phase:c-mg:liquid  
_tdb: _tdb:MgC-06Hal.tdb:LIQUID, tdb:MgC-10Hu.tdb:LIQUID, tdb:MgC-12Che.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): LIQUID, type code %, sha256 `cdafe04b706df3aa…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : C MG : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): LIQUID, type code %, sha256 `2ed80eae8ee075a6…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : C MG : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): LIQUID, type code %, sha256 `662147a17bbe63f9…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : C MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## MG2C3 (C–Mg)

- Id: `phase:c-mg:mg2c3`; status `assigned`
- Structure: Mg2C3 · oP10 · Pnnm (58); type `st:mg2c3-op10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.6000, Mg 0.4000
- Stability: stable in 1 of 3 calculated diagram(s): 300–930.23 K, x(C) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:mg2c3)

Names (4): _corpus: _corpus:phase:c-mg:mg2c3  
_tdb: _tdb:MgC-06Hal.tdb:MG2C3, tdb:MgC-10Hu.tdb:MG2C3, tdb:MgC-12Che.tdb:MG2C3  


### TDB models of MG2C3 (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): MG2C3, type code %, sha256 `cdafe04b706df3aa…`

~~~~text
66: PHASE MG2C3 % 2 2 3 !
67: CONST MG2C3 : MG : C : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): MG2C3, type code %, sha256 `2ed80eae8ee075a6…`

~~~~text
62: PHASE MG2C3 % 2 2 3 !
63: CONST MG2C3 : MG : C : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): MG2C3, type code %, sha256 `662147a17bbe63f9…`

~~~~text
62: PHASE MG2C3 % 2 2 3 !
63: CONST MG2C3 : MG : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## MGC2 (C–Mg)

- Id: `phase:c-mg:mgc2`; status `assigned`
- Structure: MgC2 · tP6 · P4_2/mnm (136); type `st:mgc2-tp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.6667, Mg 0.3333
- Stability: stable in 1 of 3 calculated diagram(s): 300–869.96 K, x(C) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mg:mgc2)

Names (4): _corpus: _corpus:phase:c-mg:mgc2  
_tdb: _tdb:MgC-06Hal.tdb:MGC2, tdb:MgC-10Hu.tdb:MGC2, tdb:MgC-12Che.tdb:MGC2  


### TDB models of MGC2 (3): PHASE and CONSTITUENT statements as written

[MgC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-06Hal.tdb): MGC2, type code %, sha256 `cdafe04b706df3aa…`

~~~~text
71: PHASE MGC2 % 2 1 2 !
72: CONST MGC2 : MG : C : !
~~~~

[MgC-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-10Hu.tdb): MGC2, type code %, sha256 `2ed80eae8ee075a6…`

~~~~text
67: PHASE MGC2 % 2 1 2 !
68: CONST MGC2 : MG : C : !
~~~~

[MgC-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/MgC-12Che.tdb): MGC2, type code %, sha256 `662147a17bbe63f9…`

~~~~text
67: PHASE MGC2 % 2 1 2 !
68: CONST MGC2 : MG : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB1001097H](https://doi.org/10.2298/JMMB1001097H) B. Hu, Y. Du, H. Xu, W. Sun, W.W. Zhang, D. Zhao, J. Mining Metall. B, 46, 97-103(2010).  
_assessment that models this phase_
- [doi:10.3139/146.110787](https://doi.org/10.3139/146.110787) H.-L. Chen, R. Schmid-Fetzer, Int. J. Mater. Res., 103, 1294-1301(2012).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
