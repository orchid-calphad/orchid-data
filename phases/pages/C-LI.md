# C–Li phases

> C–Li system: 10 phases (tier A 5, tier C 3, liquid 1, gas 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-LI.html · Markdown: https://data.orchid-project.org/phases/pages/C-LI.md

10 phases (tier A 5, tier C 3, liquid 1, gas 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-LI) · [full JSON](https://data.orchid-project.org/phases/systems/C-LI.json) · [C–Li system page](https://data.orchid-project.org/systems/C-LI.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-LI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Li system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-li-a4-diamond); _phase:c-li:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GRAPHITE_A9](#phase-c-li-a9-graphite); _phase:c-li:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.5 K, x(C) 1–1 | 0 | 2 |
| [BCC_A2](#phase-c-li-bcc-a2); _phase:c-li:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.85 K, x(C) 0–0 | 0 | 2 |
| [FCC_A1](#phase-c-li-fcc-a1); _phase:c-li:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-c-li-gas); _phase:c-li:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 1611.4–4000 K, x(C) 0–1 | 0 | 2 |
| [HCP_A3](#phase-c-li-hcp-a3); _phase:c-li:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LI2C2_ALPHA](#phase-c-li-li2c2-alpha); _phase:c-li:li2c2-alpha_ | Rb2O2 · oI8 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–725.35 K, x(C) 0.5–0.5 | 0 | 2 |
| [LI2C2_C1](#phase-c-li-li2c2-c1); _phase:c-li:li2c2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 725–1322.36 K, x(C) 0.5–0.5 | 0 | 2 |
| [LIC6](#phase-c-li-lic6); _phase:c-li:lic6_ | LiC6 · hP7 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-c-li-liquid); _phase:c-li:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 453.6–3999.85 K, x(C) 0–0.50176 | 0 | 2 |

## DIAMOND_A4 (C–Li)

- Id: `phase:c-li:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:a4-diamond)

Names (3): _corpus: _corpus:phase:c-li:a4-diamond  
_tdb: _tdb:LiC-13Koz.tdb:DIAMOND_A4, tdb:LiC-17Lia.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): DIAMOND_A4, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : C : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): DIAMOND_A4, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
58: PHASE DIAMOND_A4 % 1 1 !
59: CONST DIAMOND_A4 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Li)

- Id: `phase:c-li:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.5 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:a9-graphite)

Names (3): _corpus: _corpus:phase:c-li:a9-graphite  
_tdb: _tdb:LiC-13Koz.tdb:GRAPHITE_A9, tdb:LiC-17Lia.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): GRAPHITE_A9, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
57: PHASE GRAPHITE_A9 % 1 1 !
58: CONST GRAPHITE_A9 : C : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): GRAPHITE_A9, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
63: PHASE GRAPHITE_A9 % 1 1 !
64: CONST GRAPHITE_A9 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## BCC_A2 (C–Li)

- Id: `phase:c-li:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.85 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:bcc-a2)

Names (3): _corpus: _corpus:phase:c-li:bcc-a2  
_tdb: _tdb:LiC-13Koz.tdb:BCC_A2, tdb:LiC-17Lia.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): BCC_A2, type code %B, sha256 `2e16ee01fc9080d4…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : LI : VA : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): BCC_A2, type code %B, sha256 `8b41b4fd50a770cf…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## FCC_A1 (C–Li)

- Id: `phase:c-li:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:fcc-a1)

Names (3): _corpus: _corpus:phase:c-li:fcc-a1  
_tdb: _tdb:LiC-13Koz.tdb:FCC_A1, tdb:LiC-17Lia.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): FCC_A1, type code %A, sha256 `2e16ee01fc9080d4…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : LI : VA : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): FCC_A1, type code %A, sha256 `8b41b4fd50a770cf…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## GAS (C–Li)

- Id: `phase:c-li:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1611.4–4000 K, x(C) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:gas)

Names (3): _corpus: _corpus:phase:c-li:gas  
_tdb: _tdb:LiC-13Koz.tdb:GAS, tdb:LiC-17Lia.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): GAS, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
75: PHASE GAS:G % 1 1 !
76: CONST GAS:G : C C2 C3 C4 C5 C60 LI LI2 : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): GAS, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
81: PHASE GAS:G % 1 1 !
82: CONST GAS:G : C C2 C3 C4 C5 C60 LI LI2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## HCP_A3 (C–Li)

- Id: `phase:c-li:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:hcp-a3)

Names (3): _corpus: _corpus:phase:c-li:hcp-a3  
_tdb: _tdb:LiC-13Koz.tdb:HCP_A3, tdb:LiC-17Lia.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): HCP_A3, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
47: PHASE HCP_A3 % 2 1 0.5 !
48: CONST HCP_A3 : LI : VA : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): HCP_A3, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
53: PHASE HCP_A3 % 2 1 0.5 !
54: CONST HCP_A3 : LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## LI2C2_ALPHA (C–Li)

- Id: `phase:c-li:li2c2-alpha`; status `assigned`
- Structure: Rb2O2 · oI8 · Immm (71); type `st:rb2o2-oi8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.5000, Li 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–725.35 K, x(C) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:li2c2-alpha)

Names (3): _corpus: _corpus:phase:c-li:li2c2-alpha  
_tdb: _tdb:LiC-13Koz.tdb:LI2C2_ALPHA, tdb:LiC-17Lia.tdb:LI2C2_ALPHA  


### TDB models of LI2C2_ALPHA (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): LI2C2_ALPHA, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
62: PHASE LI2C2_ALPHA % 2 1 1 !
63: CONST LI2C2_ALPHA : LI : C : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): LI2C2_ALPHA, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
68: PHASE LI2C2_ALPHA % 2 1 1 !
69: CONST LI2C2_ALPHA : LI : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## LI2C2_C1 (C–Li)

- Id: `phase:c-li:li2c2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.5000, Li 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 725–1322.36 K, x(C) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:li2c2-c1)

Names (3): _corpus: _corpus:phase:c-li:li2c2-c1  
_tdb: _tdb:LiC-13Koz.tdb:LI2C2_C1, tdb:LiC-17Lia.tdb:LI2C2_C1  


### TDB models of LI2C2_C1 (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): LI2C2_C1, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
67: PHASE LI2C2_C1 % 2 1 1 !
68: CONST LI2C2_C1 : LI : C : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): LI2C2_C1, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
73: PHASE LI2C2_C1 % 2 1 1 !
74: CONST LI2C2_C1 : LI : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## LIC6 (C–Li)

- Id: `phase:c-li:lic6`; status `assigned`
- Structure: LiC6 · hP7 · P6/mmm (191); type `st:lic6-hp7`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.8571, Li 0.1429
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:lic6)

Names (3): _corpus: _corpus:phase:c-li:lic6  
_tdb: _tdb:LiC-13Koz.tdb:LIC6, tdb:LiC-17Lia.tdb:LIC6  


### TDB models of LIC6 (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): LIC6, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
72: PHASE LIC6 % 2 1 6 !
73: CONST LIC6 : LI : C : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): LIC6, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
78: PHASE LIC6 % 2 1 6 !
79: CONST LIC6 : LI : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

## LIQUID (C–Li)

- Id: `phase:c-li:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 453.6–3999.85 K, x(C) 0–0.50176
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-li:liquid)

Names (3): _corpus: _corpus:phase:c-li:liquid  
_tdb: _tdb:LiC-13Koz.tdb:LIQUID, tdb:LiC-17Lia.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[LiC-13Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-13Koz.tdb): LIQUID, type code %, sha256 `2e16ee01fc9080d4…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : C LI : !
~~~~

[LiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiC-17Lia.tdb): LIQUID, type code %, sha256 `8b41b4fd50a770cf…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : C LI LI2C2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.3139/146.110960](https://doi.org/10.3139/146.110960) A. Kozlov, M. Seyring, M. Drue, M. Rettenmayr, R. Schmid-Fetzer, Int. J. Mater. Res., 104, 1066-78(2013).  
_assessment that models this phase_

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
