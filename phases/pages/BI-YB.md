# Bi–Yb phases

> Bi–Yb system: 10 phases (tier A 6, tier C 3, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-YB.html · Markdown: https://data.orchid-project.org/phases/pages/BI-YB.md

10 phases (tier A 6, tier C 3, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-YB) · [full JSON](https://data.orchid-project.org/phases/systems/BI-YB.json) · [Bi–Yb system page](https://data.orchid-project.org/systems/BI-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Yb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-yb-a7-rhombohedral); _phase:bi-yb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Yb) 0–0 | 0 | 2 |
| [BCC_A2](#phase-bi-yb-bcc-a2); _phase:bi-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1033–1101.46 K, x(Yb) 1–1 | 0 | 2 |
| [BI10YB11](#phase-bi-yb-bi10yb11); _phase:bi-yb:bi10yb11_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1173.69 K, x(Yb) 0.52381–0.52381 | 0 | 2 |
| [BI2YB_C49](#phase-bi-yb-bi2yb-c49); _phase:bi-yb:bi2yb-c49_ | ZrSi2 · C49 · oC12 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–923.21 K, x(Yb) 0.33333–0.33333 | 0 | 2 |
| [BI3YB4_D73](#phase-bi-yb-bi3yb4-d73); _phase:bi-yb:bi3yb4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1753.69 K, x(Yb) 0.57143–0.57143 | 0 | 2 |
| [BI3YB5](#phase-bi-yb-bi3yb5); _phase:bi-yb:bi3yb5_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1673.27 K, x(Yb) 0.625–0.625 | 0 | 2 |
| [BIYB2](#phase-bi-yb-biyb2); _phase:bi-yb:biyb2_ | La2Sb · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1371.74 K, x(Yb) 0.66667–0.66667 | 0 | 2 |
| [FCC_A1](#phase-bi-yb-fcc-a1); _phase:bi-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1033 K, x(Yb) 1–1 | 0 | 2 |
| [HCP_A3](#phase-bi-yb-hcp-a3); _phase:bi-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-bi-yb-liquid); _phase:bi-yb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 522.95–2500 K, x(Yb) 0–1 | 0 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Yb)

- Id: `phase:bi-yb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Yb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:bi-yb:a7-rhombohedral  
_tdb: _tdb:BiYb-15Wan-ass.tdb:RHOMBOHEDRAL_A7, tdb:BiYb-15Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9fc0594db1361f49…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `ed5077d1b21a110f…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## BCC_A2 (Bi–Yb)

- Id: `phase:bi-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1033–1101.46 K, x(Yb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:bcc-a2)

Names (3): _corpus: _corpus:phase:bi-yb:bcc-a2  
_tdb: _tdb:BiYb-15Wan-ass.tdb:BCC_A2, tdb:BiYb-15Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): BCC_A2, type code %B, sha256 `9fc0594db1361f49…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI YB% : VA : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): BCC_A2, type code %B, sha256 `ed5077d1b21a110f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI YB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## BI10YB11 (Bi–Yb)

- Id: `phase:bi-yb:bi10yb11`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4762, Yb 0.5238
- Stability: stable in 2 of 2 calculated diagram(s): 300–1173.69 K, x(Yb) 0.52381–0.52381
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:bi10yb11)

Names (3): _corpus: _corpus:phase:bi-yb:bi10yb11  
_tdb: _tdb:BiYb-15Wan-ass.tdb:BI10YB11, tdb:BiYb-15Wan.tdb:BI10YB11  


### TDB models of BI10YB11 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): BI10YB11, type code %, sha256 `9fc0594db1361f49…`

~~~~text
55: PHASE BI10YB11 % 2 10 11 !
56: CONST BI10YB11 : BI : YB : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): BI10YB11, type code %, sha256 `ed5077d1b21a110f…`

~~~~text
51: PHASE BI10YB11 % 2 10 11 !
52: CONST BI10YB11 : BI : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## BI2YB_C49 (Bi–Yb)

- Id: `phase:bi-yb:bi2yb-c49`; status `assigned`
- Structure: ZrSi2 · C49 · oC12 · Cmcm (63); type `st:c49-zrsi2-oc12`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.6667, Yb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–923.21 K, x(Yb) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:bi2yb-c49)

Names (3): _corpus: _corpus:phase:bi-yb:bi2yb-c49  
_tdb: _tdb:BiYb-15Wan-ass.tdb:BI2YB_C49, tdb:BiYb-15Wan.tdb:BI2YB_C49  


### TDB models of BI2YB_C49 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): BI2YB_C49, type code %, sha256 `9fc0594db1361f49…`

~~~~text
50: PHASE BI2YB_C49 % 2 2 1 !
51: CONST BI2YB_C49 : BI : YB : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): BI2YB_C49, type code %, sha256 `ed5077d1b21a110f…`

~~~~text
46: PHASE BI2YB_C49 % 2 2 1 !
47: CONST BI2YB_C49 : BI : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## BI3YB4_D73 (Bi–Yb)

- Id: `phase:bi-yb:bi3yb4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.4286, Yb 0.5714
- Stability: stable in 2 of 2 calculated diagram(s): 300–1753.69 K, x(Yb) 0.57143–0.57143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:bi3yb4-d73)

Names (3): _corpus: _corpus:phase:bi-yb:bi3yb4-d73  
_tdb: _tdb:BiYb-15Wan-ass.tdb:BI3YB4_D73, tdb:BiYb-15Wan.tdb:BI3YB4_D73  


### TDB models of BI3YB4_D73 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): BI3YB4_D73, type code %, sha256 `9fc0594db1361f49…`

~~~~text
60: PHASE BI3YB4_D73 % 2 3 4 !
61: CONST BI3YB4_D73 : BI : YB : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): BI3YB4_D73, type code %, sha256 `ed5077d1b21a110f…`

~~~~text
56: PHASE BI3YB4_D73 % 2 3 4 !
57: CONST BI3YB4_D73 : BI : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## BI3YB5 (Bi–Yb)

- Id: `phase:bi-yb:bi3yb5`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Yb 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–1673.27 K, x(Yb) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:bi3yb5)

Names (3): _corpus: _corpus:phase:bi-yb:bi3yb5  
_tdb: _tdb:BiYb-15Wan-ass.tdb:BI3YB5, tdb:BiYb-15Wan.tdb:BI3YB5  


### TDB models of BI3YB5 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): BI3YB5, type code %, sha256 `9fc0594db1361f49…`

~~~~text
65: PHASE BI3YB5 % 2 3 5 !
66: CONST BI3YB5 : BI : YB : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): BI3YB5, type code %, sha256 `ed5077d1b21a110f…`

~~~~text
61: PHASE BI3YB5 % 2 3 5 !
62: CONST BI3YB5 : BI : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## BIYB2 (Bi–Yb)

- Id: `phase:bi-yb:biyb2`; status `assigned`
- Structure: La2Sb · tI12 · I4/mmm (139); type `st:la2sb-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3333, Yb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1371.74 K, x(Yb) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:biyb2)

Names (3): _corpus: _corpus:phase:bi-yb:biyb2  
_tdb: _tdb:BiYb-15Wan-ass.tdb:BIYB2, tdb:BiYb-15Wan.tdb:BIYB2  


### TDB models of BIYB2 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): BIYB2, type code %, sha256 `9fc0594db1361f49…`

~~~~text
70: PHASE BIYB2 % 2 1 2 !
71: CONST BIYB2 : BI : YB : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): BIYB2, type code %, sha256 `ed5077d1b21a110f…`

~~~~text
66: PHASE BIYB2 % 2 1 2 !
67: CONST BIYB2 : BI : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## FCC_A1 (Bi–Yb)

- Id: `phase:bi-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1033 K, x(Yb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-yb:fcc-a1  
_tdb: _tdb:BiYb-15Wan-ass.tdb:FCC_A1, tdb:BiYb-15Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): FCC_A1, type code %A, sha256 `9fc0594db1361f49…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI YB% : VA : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): FCC_A1, type code %A, sha256 `ed5077d1b21a110f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI YB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## HCP_A3 (Bi–Yb)

- Id: `phase:bi-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-yb:hcp-a3  
_tdb: _tdb:BiYb-15Wan-ass.tdb:HCP_A3, tdb:BiYb-15Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): HCP_A3, type code %A, sha256 `9fc0594db1361f49…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI YB : VA: !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): HCP_A3, type code %A, sha256 `ed5077d1b21a110f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI YB : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## LIQUID (Bi–Yb)

- Id: `phase:bi-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 522.95–2500 K, x(Yb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-yb:liquid)

Names (3): _corpus: _corpus:phase:bi-yb:liquid  
_tdb: _tdb:BiYb-15Wan-ass.tdb:LIQUID, tdb:BiYb-15Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiYb-15Wan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan-ass.tdb): LIQUID, type code %, sha256 `9fc0594db1361f49…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI BI3YB4 YB : !
~~~~

[BiYb-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiYb-15Wan.tdb): LIQUID, type code %, sha256 `ed5077d1b21a110f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
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
