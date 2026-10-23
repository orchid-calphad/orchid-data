# La–Pt phases

> La–Pt system: 12 phases (tier A 8, tier B 1, tier C 1, liquid 1, needs_review 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LA-PT.html · Markdown: https://data.orchid-project.org/phases/pages/LA-PT.md

12 phases (tier A 8, tier B 1, tier C 1, liquid 1, needs_review 1); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LA-PT) · [full JSON](https://data.orchid-project.org/phases/systems/LA-PT.json) · [La–Pt system page](https://data.orchid-project.org/systems/LA-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/LA-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the La–Pt system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-la-pt-bcc-a2); _phase:la-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1134–1209 K, x(Pt) 0–0 | 0 | 1 |
| [DHCP](#phase-la-pt-dhcp-a3); _phase:la-pt:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–550 K, x(Pt) 0–0 | 2 | 1 |
| [FCC_A1](#phase-la-pt-fcc-a1); _phase:la-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499 K, x(Pt) 0–1 | 2 | 1 |
| [HCP_A3](#phase-la-pt-hcp-a3); _phase:la-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LA2PT7](#phase-la-pt-la2pt7); _phase:la-pt:la2pt7_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 745.96–2350.25 K, x(Pt) 0.77778–0.77778 | 2 | 1 |
| [LA3PT2](#phase-la-pt-la3pt2); _phase:la-pt:la3pt2_ | Er3Ni2 · hR15 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 470.06–1319.6 K, x(Pt) 0.4–0.4 | 4 | 1 |
| [LA3PT4](#phase-la-pt-la3pt4); _phase:la-pt:la3pt4_ | Pd4Pu3 · hR14 · R-3 (148) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1191.57 K, x(Pt) 0.57143–0.57143 | 2 | 1 |
| [LA7PT3_D102](#phase-la-pt-la7pt3-d102); _phase:la-pt:la7pt3-d102_ | Fe3Th7 · D10_2 · hP20 · P6_3mc (186) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1167.63 K, x(Pt) 0.3–0.3 | 4 | 1 |
| [LAPT_B33](#phase-la-pt-lapt-b33); _phase:la-pt:lapt-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1601.54 K, x(Pt) 0.5–0.5 | 6 | 1 |
| [LAPT2_C15](#phase-la-pt-lapt2-c15); _phase:la-pt:lapt2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1761.23 K, x(Pt) 0.66667–0.7544 | 5 | 1 |
| [LAPT5_D2D](#phase-la-pt-lapt5-d2d); _phase:la-pt:lapt5-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2514.78 K, x(Pt) 0.83333–0.83333 | 3 | 1 |
| [LIQUID](#phase-la-pt-liquid); _phase:la-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1009.23–2514.78 K, x(Pt) 0–1 | 12 | 1 |

## BCC_A2 (La–Pt)

- Id: `phase:la-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1134–1209 K, x(Pt) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:bcc-a2)

Names (2): _corpus: _corpus:phase:la-pt:bcc-a2  
_tdb: _tdb:LaPt-06Rei.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): BCC_A2, type code %B, sha256 `2f34d1537e937633…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : LA% PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase_

## DHCP (La–Pt)

- Id: `phase:la-pt:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–550 K, x(Pt) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:dhcp-a3)

Names (3): _corpus: _corpus:phase:la-pt:dhcp-a3  
_paper: _paper:10.1016/j.jallcom.2005.10.016:La(fcc)  
_tdb: _tdb:LaPt-06Rei.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): DHCP, type code %, sha256 `2f34d1537e937633…`

~~~~text
49: PHASE DHCP % 1 1 !
50: CONST DHCP : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (La–Pt)

- Id: `phase:la-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499 K, x(Pt) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:fcc-a1)

Names (3): _corpus: _corpus:phase:la-pt:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2005.10.016:(Pt)  
_tdb: _tdb:LaPt-06Rei.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): FCC_A1, type code %A, sha256 `2f34d1537e937633…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : LA% PT% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (La–Pt)

- Id: `phase:la-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pt 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:hcp-a3)

Names (2): _corpus: _corpus:phase:la-pt:hcp-a3  
_tdb: _tdb:LaPt-06Rei.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): HCP_A3, type code %A, sha256 `2f34d1537e937633…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase_

## LA2PT7 (La–Pt)

- Id: `phase:la-pt:la2pt7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (La2Pt7) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (La2Pt7) — Hallstedt 2025 mmc2 row for LA2PT7: La2Pt7
- Stoichiometry: La 0.2222, Pt 0.7778
- Stability: stable in 1 of 1 calculated diagram(s): 745.96–2350.25 K, x(Pt) 0.77778–0.77778
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:la2pt7)

Names (3): _corpus: _corpus:phase:la-pt:la2pt7  
_paper: _paper:10.1016/j.jallcom.2005.10.016:Pt7La2  
_tdb: _tdb:LaPt-06Rei.tdb:LA2PT7  


### TDB models of LA2PT7 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LA2PT7, type code %, sha256 `2f34d1537e937633…`

~~~~text
79: PHASE LA2PT7 % 2 2 7 !
80: CONST LA2PT7 : LA : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## LA3PT2 (La–Pt)

- Id: `phase:la-pt:la3pt2`; status `assigned`
- Structure: Er3Ni2 · hR15 · R-3 (148); type `st:er3ni2-hr15`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: La 0.6000, Pt 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 470.06–1319.6 K, x(Pt) 0.4–0.4
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:la3pt2)

Names (3): _corpus: _corpus:phase:la-pt:la3pt2  
_paper: _paper:10.1016/j.jallcom.2005.10.016:Pt2La3  
_tdb: _tdb:LaPt-06Rei.tdb:LA3PT2  


### TDB models of LA3PT2 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LA3PT2, type code %, sha256 `2f34d1537e937633…`

~~~~text
59: PHASE LA3PT2 % 2 3 2 !
60: CONST LA3PT2 : LA : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## LA3PT4 (La–Pt)

- Id: `phase:la-pt:la3pt4`; status `assigned`
- Structure: Pd4Pu3 · hR14 · R-3 (148); type `st:pd4pu3-hr14`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: La 0.4286, Pt 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1191.57 K, x(Pt) 0.57143–0.57143
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:la3pt4)

Names (5): _corpus: _corpus:phase:la-pt:la3pt4  
_mp: _mp:mp-aaackwkm  
_oqmd: _oqmd:oqmd-2027663  
_paper: _paper:10.1016/j.jallcom.2005.10.016:Pt4La3  
_tdb: _tdb:LaPt-06Rei.tdb:LA3PT4  


### TDB models of LA3PT4 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LA3PT4, type code %, sha256 `2f34d1537e937633…`

~~~~text
69: PHASE LA3PT4 % 2 3 4 !
70: CONST LA3PT4 : LA : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## LA7PT3_D102 (La–Pt)

- Id: `phase:la-pt:la7pt3-d102`; status `assigned`
- Structure: Fe3Th7 · D10_2 · hP20 · P6_3mc (186); type `st:d10-2-fe3th7-hp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacprqb and oqmd-1821163, space group 186
- Stoichiometry: La 0.7000, Pt 0.3000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1167.63 K, x(Pt) 0.3–0.3
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:la7pt3-d102)

Names (5): _corpus: _corpus:phase:la-pt:la7pt3-d102  
_mp: _mp:mp-aaacprqb  
_oqmd: _oqmd:oqmd-1821163  
_paper: _paper:10.1016/j.jallcom.2005.10.016:Pt3La7  
_tdb: _tdb:LaPt-06Rei.tdb:LA7PT3_D102  


### TDB models of LA7PT3_D102 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LA7PT3_D102, type code %, sha256 `2f34d1537e937633…`

~~~~text
54: PHASE LA7PT3_D102 % 2 7 3 !
55: CONST LA7PT3_D102 : LA : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## LAPT_B33 (La–Pt)

- Id: `phase:la-pt:lapt-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfakm and oqmd-30659, space group 63
- Stoichiometry: La 0.5000, Pt 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1601.54 K, x(Pt) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:lapt-b33)

Names (5): _corpus: _corpus:phase:la-pt:lapt-b33  
_mp: _mp:mp-aaacfakm  
_oqmd: _oqmd:oqmd-30659  
_paper: _paper:10.1016/j.jallcom.2005.10.016:PtLa  
_tdb: _tdb:LaPt-06Rei.tdb:LAPT_B33  


### TDB models of LAPT_B33 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LAPT_B33, type code %, sha256 `2f34d1537e937633…`

~~~~text
64: PHASE LAPT_B33 % 2 1 1 !
65: CONST LAPT_B33 : LA : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## LAPT2_C15 (La–Pt)

- Id: `phase:la-pt:lapt2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1761.23 K, x(Pt) 0.66667–0.7544
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:lapt2-c15)

Names (3): _corpus: _corpus:phase:la-pt:lapt2-c15  
_paper: _paper:10.1016/j.jallcom.2005.10.016:Pt2La  
_tdb: _tdb:LaPt-06Rei.tdb:LAPT2_C15  


### TDB models of LAPT2_C15 (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LAPT2_C15, type code %, sha256 `2f34d1537e937633…`

~~~~text
74: PHASE LAPT2_C15 % 2 1 2 !
75: CONST LAPT2_C15 : LA% PT : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## LAPT5_D2D (La–Pt)

- Id: `phase:la-pt:lapt5-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacsm and oqmd-17574, space group 191
- Stoichiometry: La 0.1667, Pt 0.8333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2514.78 K, x(Pt) 0.83333–0.83333
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:lapt5-d2d)

Names (5): _corpus: _corpus:phase:la-pt:lapt5-d2d  
_mp: _mp:mp-aaaaacsm  
_oqmd: _oqmd:oqmd-17574  
_paper: _paper:10.1016/j.jallcom.2005.10.016:Pt5La  
_tdb: _tdb:LaPt-06Rei.tdb:LAPT5_D2D  


### TDB models of LAPT5_D2D (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LAPT5_D2D, type code %, sha256 `2f34d1537e937633…`

~~~~text
84: PHASE LAPT5_D2D % 2 1 5 !
85: CONST LAPT5_D2D : LA : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

## LIQUID (La–Pt)

- Id: `phase:la-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1009.23–2514.78 K, x(Pt) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pt:liquid)

Names (3): _corpus: _corpus:phase:la-pt:liquid  
_paper: _paper:10.1016/j.jallcom.2005.10.016:L  
_tdb: _tdb:LaPt-06Rei.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LaPt-06Rei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPt-06Rei.tdb): LIQUID, type code %, sha256 `2f34d1537e937633…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : LA PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.016](https://doi.org/10.1016/j.jallcom.2005.10.016) S. Reimann, H.-J. Schaller, Constitution and thermodynamics of Pt–La alloys, Journal of Alloys and Compounds 419, 133-139 (2006).  
_assessment that models this phase; reports values for this phase_

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
