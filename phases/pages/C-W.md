# C–W phases

> C–W system: 7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-W.html · Markdown: https://data.orchid-project.org/phases/pages/C-W.md

7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-W) · [full JSON](https://data.orchid-project.org/phases/systems/C-W.json) · [C–W system page](https://data.orchid-project.org/systems/C-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–W system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-w-a4-diamond); _phase:c-w:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 3 |
| [GRAPHITE_A9](#phase-c-w-a9-graphite); _phase:c-w:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 3 |
| [BCC_A2](#phase-c-w-bcc-a2); _phase:c-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.89 K, x(C) 0–0.00917 | 6 | 3 |
| [FCC_A1](#phase-c-w-fcc-a1); _phase:c-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2800.4–3024.19 K, x(C) 0.37193–0.39271 | 12 | 3 |
| [HCP_A3](#phase-c-w-hcp-a3); _phase:c-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1519.61–3050 K, x(C) 0.26949–0.33153 | 15 | 3 |
| [LIQUID](#phase-c-w-liquid); _phase:c-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2980.55–4000 K, x(C) 0–0.58533 | 18 | 3 |
| [MC_SHP](#phase-c-w-mc-shp); _phase:c-w:mc-shp_ | WC · B_h · hP2 · P-6m2 (187) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–3047.41 K, x(C) 0.5–0.5 | 12 | 3 |

## DIAMOND_A4 (C–W)

- Id: `phase:c-w:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-w:a4-diamond)

Names (4): _corpus: _corpus:phase:c-w:a4-diamond  
_tdb: _tdb:WC-22He-3g.tdb:DIAMOND_A4, tdb:WC-86Gus.tdb:DIAMOND_A4, tdb:WC-93Jon-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[WC-22He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-22He-3g.tdb): DIAMOND_A4, type code %, sha256 `c5248688e6b030ed…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

[WC-86Gus.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-86Gus.tdb): DIAMOND_A4, type code %, sha256 `703f22b1c9570abb…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : C : !
~~~~

[WC-93Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-93Jon-LB.tdb): DIAMOND_A4, type code %, sha256 `70b8892cd7de3337…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102449](https://doi.org/10.1016/j.calphad.2022.102449) Zhangting He, Malin Selleby, A third generation Calphad description of W–C including a revision of liquid C, Calphad 78, 102449 (2022).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.7.653](https://doi.org/10.1179/mst.1986.2.7.653) P. Gustafson, Thermodynamic evaluation of C–W system, Materials Science and Technology 2, 653-658 (1986).  
_assessment that models this phase_

## GRAPHITE_A9 (C–W)

- Id: `phase:c-w:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-w:a9-graphite)

Names (4): _corpus: _corpus:phase:c-w:a9-graphite  
_tdb: _tdb:WC-22He-3g.tdb:GRAPHITE_A9, tdb:WC-86Gus.tdb:GRAPHITE_A9, tdb:WC-93Jon-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (3): PHASE and CONSTITUENT statements as written

[WC-22He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-22He-3g.tdb): GRAPHITE_A9, type code %, sha256 `c5248688e6b030ed…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

[WC-86Gus.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-86Gus.tdb): GRAPHITE_A9, type code %, sha256 `703f22b1c9570abb…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : C : !
~~~~

[WC-93Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-93Jon-LB.tdb): GRAPHITE_A9, type code %, sha256 `70b8892cd7de3337…`

~~~~text
51: PHASE GRAPHITE_A9 % 1 1 !
52: CONST GRAPHITE_A9 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102449](https://doi.org/10.1016/j.calphad.2022.102449) Zhangting He, Malin Selleby, A third generation Calphad description of W–C including a revision of liquid C, Calphad 78, 102449 (2022).  
_assessment that models this phase_
- [doi:10.1179/mst.1986.2.7.653](https://doi.org/10.1179/mst.1986.2.7.653) P. Gustafson, Thermodynamic evaluation of C–W system, Materials Science and Technology 2, 653-658 (1986).  
_assessment that models this phase_

## BCC_A2 (C–W)

- Id: `phase:c-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.89 K, x(C) 0–0.00917
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-w:bcc-a2)

Names (5): _corpus: _corpus:phase:c-w:bcc-a2  
_paper: _paper:10.1016/j.calphad.2022.102449:bcc  
_tdb: _tdb:WC-22He-3g.tdb:BCC_A2, tdb:WC-86Gus.tdb:BCC_A2, tdb:WC-93Jon-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[WC-22He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-22He-3g.tdb): BCC_A2, type code %B, sha256 `c5248688e6b030ed…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : W : C VA% : !
~~~~

[WC-86Gus.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-86Gus.tdb): BCC_A2, type code %B, sha256 `703f22b1c9570abb…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : W : C VA% : !
~~~~

[WC-93Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-93Jon-LB.tdb): BCC_A2, type code %B, sha256 `70b8892cd7de3337…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : W : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2022.102449](https://doi.org/10.1016/j.calphad.2022.102449) Zhangting He, Malin Selleby, A third generation Calphad description of W–C including a revision of liquid C, Calphad 78, 102449 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/mst.1986.2.7.653](https://doi.org/10.1179/mst.1986.2.7.653) P. Gustafson, Thermodynamic evaluation of C–W system, Materials Science and Technology 2, 653-658 (1986).  
_assessment that models this phase_
- [doi:10.1016/0008-6223(86)90113-2](https://doi.org/10.1016/0008-6223%2886%2990113-2) P. Gustafson, Thermodynamic evaluation of C-W system, Mater. Sci. Technol. 2 (1986) 653–658, http://dx.doi.org/10.1179/mst.1986.2.7.653.  
_cited as the source of values for this phase_
- [doi:10.1134/s0020168506020051](https://doi.org/10.1134/s0020168506020051) A. S. Kurlov, A. I. Gusev, Tungsten carbides and W-C phase diagram, Inorg Mater 42, 121-127 (2006).  
_cited as the source of values for this phase_

## FCC_A1 (C–W)

- Id: `phase:c-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2800.4–3024.19 K, x(C) 0.37193–0.39271
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-w:fcc-a1)

Names (5): _corpus: _corpus:phase:c-w:fcc-a1  
_paper: _paper:10.1016/j.calphad.2022.102449:fcc  
_tdb: _tdb:WC-22He-3g.tdb:FCC_A1, tdb:WC-86Gus.tdb:FCC_A1, tdb:WC-93Jon-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[WC-22He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-22He-3g.tdb): FCC_A1, type code %A, sha256 `c5248688e6b030ed…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : W : C VA% : !
~~~~

[WC-86Gus.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-86Gus.tdb): FCC_A1, type code %A, sha256 `703f22b1c9570abb…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : W : C VA% : !
~~~~

[WC-93Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-93Jon-LB.tdb): FCC_A1, type code %A, sha256 `70b8892cd7de3337…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : W : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102449](https://doi.org/10.1016/j.calphad.2022.102449) Zhangting He, Malin Selleby, A third generation Calphad description of W–C including a revision of liquid C, Calphad 78, 102449 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/mst.1986.2.7.653](https://doi.org/10.1179/mst.1986.2.7.653) P. Gustafson, Thermodynamic evaluation of C–W system, Materials Science and Technology 2, 653-658 (1986).  
_assessment that models this phase_
- [doi:10.1016/0008-6223(86)90113-2](https://doi.org/10.1016/0008-6223%2886%2990113-2) P. Gustafson, Thermodynamic evaluation of C-W system, Mater. Sci. Technol. 2 (1986) 653–658, http://dx.doi.org/10.1179/mst.1986.2.7.653.  
_cited as the source of values for this phase_

## HCP_A3 (C–W)

- Id: `phase:c-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1519.61–3050 K, x(C) 0.26949–0.33153
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-w:hcp-a3)

Names (5): _corpus: _corpus:phase:c-w:hcp-a3  
_paper: _paper:10.1016/j.calphad.2022.102449:hcp  
_tdb: _tdb:WC-22He-3g.tdb:HCP_A3, tdb:WC-86Gus.tdb:HCP_A3, tdb:WC-93Jon-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[WC-22He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-22He-3g.tdb): HCP_A3, type code %A, sha256 `c5248688e6b030ed…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : W : C VA% : !
~~~~

[WC-86Gus.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-86Gus.tdb): HCP_A3, type code %A, sha256 `703f22b1c9570abb…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : W : C VA% : !
~~~~

[WC-93Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-93Jon-LB.tdb): HCP_A3, type code %A, sha256 `70b8892cd7de3337…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : W : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2022.102449](https://doi.org/10.1016/j.calphad.2022.102449) Zhangting He, Malin Selleby, A third generation Calphad description of W–C including a revision of liquid C, Calphad 78, 102449 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/mst.1986.2.7.653](https://doi.org/10.1179/mst.1986.2.7.653) P. Gustafson, Thermodynamic evaluation of C–W system, Materials Science and Technology 2, 653-658 (1986).  
_assessment that models this phase_
- [doi:10.1016/0008-6223(86)90113-2](https://doi.org/10.1016/0008-6223%2886%2990113-2) P. Gustafson, Thermodynamic evaluation of C-W system, Mater. Sci. Technol. 2 (1986) 653–658, http://dx.doi.org/10.1179/mst.1986.2.7.653.  
_cited as the source of values for this phase_
- [doi:10.1134/s0020168506020051](https://doi.org/10.1134/s0020168506020051) A. S. Kurlov, A. I. Gusev, Tungsten carbides and W-C phase diagram, Inorg Mater 42, 121-127 (2006).  
_cited as the source of values for this phase_

## LIQUID (C–W)

- Id: `phase:c-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2980.55–4000 K, x(C) 0–0.58533
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-w:liquid)

Names (5): _corpus: _corpus:phase:c-w:liquid  
_paper: _paper:10.1016/j.calphad.2022.102449:L  
_tdb: _tdb:WC-22He-3g.tdb:LIQUID, tdb:WC-86Gus.tdb:LIQUID, tdb:WC-93Jon-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[WC-22He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-22He-3g.tdb): LIQUID, type code %, sha256 `c5248688e6b030ed…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C W : !
~~~~

[WC-86Gus.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-86Gus.tdb): LIQUID, type code %, sha256 `703f22b1c9570abb…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : C W : !
~~~~

[WC-93Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-93Jon-LB.tdb): LIQUID, type code %, sha256 `70b8892cd7de3337…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : C W : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102449](https://doi.org/10.1016/j.calphad.2022.102449) Zhangting He, Malin Selleby, A third generation Calphad description of W–C including a revision of liquid C, Calphad 78, 102449 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/mst.1986.2.7.653](https://doi.org/10.1179/mst.1986.2.7.653) P. Gustafson, Thermodynamic evaluation of C–W system, Materials Science and Technology 2, 653-658 (1986).  
_assessment that models this phase_
- [doi:10.1016/0008-6223(86)90113-2](https://doi.org/10.1016/0008-6223%2886%2990113-2) P. Gustafson, Thermodynamic evaluation of C-W system, Mater. Sci. Technol. 2 (1986) 653–658, http://dx.doi.org/10.1179/mst.1986.2.7.653.  
_cited as the source of values for this phase_

## MC_SHP (C–W)

- Id: `phase:c-w:mc-shp`; status `assigned`
- Structure: WC · B_h · hP2 · P-6m2 (187); type `st:b-h-wc-hp2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MC,SHP, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–3047.41 K, x(C) 0.5–0.5
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-w:mc-shp)

Names (5): _corpus: _corpus:phase:c-w:mc-shp  
_paper: _paper:10.1016/j.calphad.2022.102449:WC  
_tdb: _tdb:WC-22He-3g.tdb:MC_SHP, tdb:WC-86Gus.tdb:MC_SHP, tdb:WC-93Jon-LB.tdb:MC_SHP  


### TDB models of MC_SHP (3): PHASE and CONSTITUENT statements as written

[WC-22He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-22He-3g.tdb): MC_SHP, type code %, sha256 `c5248688e6b030ed…`

~~~~text
55: PHASE MC_SHP % 2 1 1 !
56: CONST MC_SHP : W : C : !
~~~~

[WC-86Gus.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-86Gus.tdb): MC_SHP, type code %, sha256 `703f22b1c9570abb…`

~~~~text
50: PHASE MC_SHP % 2 1 1 !
51: CONST MC_SHP : W : C : !
~~~~

[WC-93Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WC-93Jon-LB.tdb): MC_SHP, type code %, sha256 `70b8892cd7de3337…`

~~~~text
56: PHASE MC_SHP % 2 1 1 !
57: CONST MC_SHP : W : C : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2022.102449](https://doi.org/10.1016/j.calphad.2022.102449) Zhangting He, Malin Selleby, A third generation Calphad description of W–C including a revision of liquid C, Calphad 78, 102449 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/mst.1986.2.7.653](https://doi.org/10.1179/mst.1986.2.7.653) P. Gustafson, Thermodynamic evaluation of C–W system, Materials Science and Technology 2, 653-658 (1986).  
_assessment that models this phase_
- [doi:10.1016/0008-6223(86)90113-2](https://doi.org/10.1016/0008-6223%2886%2990113-2) P. Gustafson, Thermodynamic evaluation of C-W system, Mater. Sci. Technol. 2 (1986) 653–658, http://dx.doi.org/10.1179/mst.1986.2.7.653.  
_cited as the source of values for this phase_
- [doi:10.1134/s0020168506020051](https://doi.org/10.1134/s0020168506020051) A. S. Kurlov, A. I. Gusev, Tungsten carbides and W-C phase diagram, Inorg Mater 42, 121-127 (2006).  
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
