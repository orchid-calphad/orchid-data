# Co–Dy phases

> Co–Dy system: 11 phases (tier A 6, tier C 3, liquid 1, needs_review 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-DY.html · Markdown: https://data.orchid-project.org/phases/pages/CO-DY.md

11 phases (tier A 6, tier C 3, liquid 1, needs_review 1); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-DY) · [full JSON](https://data.orchid-project.org/phases/systems/CO-DY.json) · [Co–Dy system page](https://data.orchid-project.org/systems/CO-DY.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-DY.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Dy system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-dy-bcc-a2); _phase:co-dy:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1654.26–2499.96 K, x(Dy) 0.99965–1 | 0 | 2 |
| [CO17DY2](#phase-co-dy-co17dy2); _phase:co-dy:co17dy2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1661.95 K, x(Dy) 0.10526–0.16002 | 0 | 2 |
| [CO2DY_C15](#phase-co-dy-co2dy-c15); _phase:co-dy:co2dy-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1552.42 K, x(Dy) 0.33333–0.33333 | 0 | 2 |
| [CO3DY](#phase-co-dy-co3dy); _phase:co-dy:co3dy_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1623.82 K, x(Dy) 0.25–0.25 | 0 | 2 |
| [CO5DY_D2D](#phase-co-dy-co5dy-d2d); _phase:co-dy:co5dy-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1404.85–1616.18 K, x(Dy) 0.16667–0.16667 | 0 | 1 |
| [CO7DY12](#phase-co-dy-co7dy12); _phase:co-dy:co7dy12_ | Co7Ho12 · mP38 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1031.58 K, x(Dy) 0.63158–0.63158 | 0 | 2 |
| [CO7DY2](#phase-co-dy-co7dy2); _phase:co-dy:co7dy2_ | Co7Gd2 · hR18 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1615.53 K, x(Dy) 0.22222–0.22222 | 0 | 2 |
| [CODY3_D011](#phase-co-dy-cody3-d011); _phase:co-dy:cody3-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1143.89 K, x(Dy) 0.75–0.75 | 0 | 2 |
| [FCC_A1](#phase-co-dy-fcc-a1); _phase:co-dy:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 632.49–1773.89 K, x(Dy) 0–0.00174 | 0 | 2 |
| [HCP_A3](#phase-co-dy-hcp-a3); _phase:co-dy:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1689.99 K, x(Dy) 0–1 | 0 | 2 |
| [LIQUID](#phase-co-dy-liquid); _phase:co-dy:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 993.35–2500 K, x(Dy) 0–1 | 0 | 2 |

## BCC_A2 (Co–Dy)

- Id: `phase:co-dy:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1654.26–2499.96 K, x(Dy) 0.99965–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:bcc-a2)

Names (3): _corpus: _corpus:phase:co-dy:bcc-a2  
_tdb: _tdb:CoDy-96Su.tdb:BCC_A2, tdb:CoDy-98Su.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): BCC_A2, type code %B, sha256 `6bdfab6e817c7d70…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CO DY : VA : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): BCC_A2, type code %B, sha256 `ef3d3e66257222b3…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : CO DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## CO17DY2 (Co–Dy)

- Id: `phase:co-dy:co17dy2`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_rows_disagree
- Candidate (dft_mp): R-3m (166) — on-hull MP Dy2Co17 at x(DY)=0.1053
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Co17 Dy2 at x(DY)=0.1053
- Candidate (sgte_mmc2): CaCu5 · D2_d · hP6 · P6/mmm (191) — Hallstedt 2025 mmc2 row for CO17DY2: Co5Dy
- Candidate (sgte_mmc2): Th2Zn17 · hR19 · R-3m (166) — Hallstedt 2025 mmc2 row for CO17DY2: Co17Dy2
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — CoDy-96Su.tdb: 'Prototype Th2Zn17 (hR19, R-3m)'
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — CoDy-98Su.tdb: 'Prototype Th2Zn17 (hR19, R-3m) and CaCu5 (hP6, P6/mmm)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1661.95 K, x(Dy) 0.10526–0.16002
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:co17dy2)

Names (3): _corpus: _corpus:phase:co-dy:co17dy2  
_tdb: _tdb:CoDy-96Su.tdb:CO17DY2, tdb:CoDy-98Su.tdb:CO17DY2  


### TDB models of CO17DY2 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): CO17DY2, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
49: PHASE CO17DY2 %A 2 17 2 !
50: CONST CO17DY2 : CO : DY : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): CO17DY2, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
58: PHASE CO17DY2 %A 3 15 1 2 !
59: CONST CO17DY2 : CO : CO2 DY : CO2 DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## CO2DY_C15 (Co–Dy)

- Id: `phase:co-dy:co2dy-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadxc and oqmd-20722, space group 227
- Stoichiometry: Co 0.6667, Dy 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1552.42 K, x(Dy) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:co2dy-c15)

Names (5): _corpus: _corpus:phase:co-dy:co2dy-c15  
_mp: _mp:mp-aaaaadxc  
_oqmd: _oqmd:oqmd-20722  
_tdb: _tdb:CoDy-96Su.tdb:CO2DY_C15, tdb:CoDy-98Su.tdb:CO2DY_C15  


### TDB models of CO2DY_C15 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): CO2DY_C15, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
69: PHASE CO2DY_C15 %A 2 2 1 !
70: CONST CO2DY_C15 : CO : DY : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): CO2DY_C15, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
73: PHASE CO2DY_C15 %A 2 2 1 !
74: CONST CO2DY_C15 : CO : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## CO3DY (Co–Dy)

- Id: `phase:co-dy:co3dy`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.7500, Dy 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1623.82 K, x(Dy) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:co3dy)

Names (3): _corpus: _corpus:phase:co-dy:co3dy  
_tdb: _tdb:CoDy-96Su.tdb:CO3DY, tdb:CoDy-98Su.tdb:CO3DY  


### TDB models of CO3DY (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): CO3DY, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
64: PHASE CO3DY %A 2 3 1 !
65: CONST CO3DY : CO : DY : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): CO3DY, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
68: PHASE CO3DY %A 2 3 1 !
69: CONST CO3DY : CO : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## CO5DY_D2D (Co–Dy)

- Id: `phase:co-dy:co5dy-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.8333, Dy 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 1404.85–1616.18 K, x(Dy) 0.16667–0.16667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:co5dy-d2d)

Names (2): _corpus: _corpus:phase:co-dy:co5dy-d2d  
_tdb: _tdb:CoDy-96Su.tdb:CO5DY_D2D  


### TDB models of CO5DY_D2D (1): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): CO5DY_D2D, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
54: PHASE CO5DY_D2D %A 2 5 1 !
55: CONST CO5DY_D2D : CO : DY : !
~~~~

## CO7DY12 (Co–Dy)

- Id: `phase:co-dy:co7dy12`; status `assigned`
- Structure: Co7Ho12 · mP38 · P2_1/c (14); type `st:co7ho12-mp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.3684, Dy 0.6316
- Stability: stable in 2 of 2 calculated diagram(s): 300–1031.58 K, x(Dy) 0.63158–0.63158
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:co7dy12)

Names (3): _corpus: _corpus:phase:co-dy:co7dy12  
_tdb: _tdb:CoDy-96Su.tdb:CO7DY12, tdb:CoDy-98Su.tdb:CO7DY12  


### TDB models of CO7DY12 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): CO7DY12, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
74: PHASE CO7DY12 %A 2 7 12 !
75: CONST CO7DY12 : CO : DY : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): CO7DY12, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
78: PHASE CO7DY12 %A 2 7 12 !
79: CONST CO7DY12 : CO : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## CO7DY2 (Co–Dy)

- Id: `phase:co-dy:co7dy2`; status `assigned`
- Structure: Co7Gd2 · hR18 · R-3m (166); type `st:co7gd2-hr18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.7778, Dy 0.2222
- Stability: stable in 2 of 2 calculated diagram(s): 300–1615.53 K, x(Dy) 0.22222–0.22222
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:co7dy2)

Names (3): _corpus: _corpus:phase:co-dy:co7dy2  
_tdb: _tdb:CoDy-96Su.tdb:CO7DY2, tdb:CoDy-98Su.tdb:CO7DY2  


### TDB models of CO7DY2 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): CO7DY2, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
59: PHASE CO7DY2 %A 2 7 2 !
60: CONST CO7DY2 : CO : DY : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): CO7DY2, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
63: PHASE CO7DY2 %A 2 7 2 !
64: CONST CO7DY2 : CO : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## CODY3_D011 (Co–Dy)

- Id: `phase:co-dy:cody3-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabkufg and oqmd-18446, space group 62
- Stoichiometry: Co 0.2500, Dy 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1143.89 K, x(Dy) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:cody3-d011)

Names (5): _corpus: _corpus:phase:co-dy:cody3-d011  
_mp: _mp:mp-aaabkufg  
_oqmd: _oqmd:oqmd-18446  
_tdb: _tdb:CoDy-96Su.tdb:CODY3_D011, tdb:CoDy-98Su.tdb:CODY3_D011  


### TDB models of CODY3_D011 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): CODY3_D011, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
79: PHASE CODY3_D011 %A 2 1 3 !
80: CONST CODY3_D011 : CO : DY : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): CODY3_D011, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
83: PHASE CODY3_D011 %A 2 1 3 !
84: CONST CODY3_D011 : CO : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## FCC_A1 (Co–Dy)

- Id: `phase:co-dy:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 632.49–1773.89 K, x(Dy) 0–0.00174
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:fcc-a1)

Names (3): _corpus: _corpus:phase:co-dy:fcc-a1  
_tdb: _tdb:CoDy-96Su.tdb:FCC_A1, tdb:CoDy-98Su.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): FCC_A1, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CO% DY : VA : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): FCC_A1, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : CO% DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## HCP_A3 (Co–Dy)

- Id: `phase:co-dy:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1689.99 K, x(Dy) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:hcp-a3)

Names (3): _corpus: _corpus:phase:co-dy:hcp-a3  
_tdb: _tdb:CoDy-96Su.tdb:HCP_A3, tdb:CoDy-98Su.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): HCP_A3, type code %A, sha256 `6bdfab6e817c7d70…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CO% DY% : VA : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): HCP_A3, type code %A, sha256 `ef3d3e66257222b3…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : CO% DY% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
_assessment that models this phase_

## LIQUID (Co–Dy)

- Id: `phase:co-dy:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 993.35–2500 K, x(Dy) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-dy:liquid)

Names (3): _corpus: _corpus:phase:co-dy:liquid  
_tdb: _tdb:CoDy-96Su.tdb:LIQUID, tdb:CoDy-98Su.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CoDy-96Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-96Su.tdb): LIQUID, type code %, sha256 `6bdfab6e817c7d70…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CO DY : !
~~~~

[CoDy-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoDy-98Su.tdb): LIQUID, type code %, sha256 `ef3d3e66257222b3…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : CO DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1998-0099](https://doi.org/10.3139/ijmr-1998-0099) X. Su, W. Zhang, Z. Du, Z. Metallkd., 89, 522-26(1998).  
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
