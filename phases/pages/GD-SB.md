# Gd–Sb phases

> Gd–Sb system: 10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-SB.html · Markdown: https://data.orchid-project.org/phases/pages/GD-SB.md

10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-SB) · [full JSON](https://data.orchid-project.org/phases/systems/GD-SB.json) · [Gd–Sb system page](https://data.orchid-project.org/systems/GD-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–Sb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-gd-sb-a7-rhombohedral); _phase:gd-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 2 | 1 |
| [BCC_A2](#phase-gd-sb-bcc-a2); _phase:gd-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1500.84–1586.12 K, x(Sb) 0–0.01911 | 4 | 1 |
| [FCC_A1](#phase-gd-sb-fcc-a1); _phase:gd-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GD16SB39](#phase-gd-sb-gd16sb39); _phase:gd-sb:gd16sb39_ | Gd16Sb39 · mC124 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1053.73 K, x(Sb) 0.70909–0.70909 | 4 | 1 |
| [GD4SB3_D73](#phase-gd-sb-gd4sb3-d73); _phase:gd-sb:gd4sb3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2047.6 K, x(Sb) 0.42857–0.42857 | 4 | 1 |
| [GD5SB3_D88](#phase-gd-sb-gd5sb3-d88); _phase:gd-sb:gd5sb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1917.33 K, x(Sb) 0.375–0.375 | 4 | 1 |
| [GDSB_B1](#phase-gd-sb-gdsb-b1); _phase:gd-sb:gdsb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2113.15 K, x(Sb) 0.5–0.5 | 6 | 1 |
| [GDSB_BETA](#phase-gd-sb-gdsb-beta); _phase:gd-sb:gdsb-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2113.15–2400.73 K, x(Sb) 0.5–0.5 | 4 | 1 |
| [HCP_A3](#phase-gd-sb-hcp-a3); _phase:gd-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1508.15 K, x(Sb) 0–0.04024 | 4 | 1 |
| [LIQUID](#phase-gd-sb-liquid); _phase:gd-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 902.91–2500 K, x(Sb) 0–1 | 18 | 1 |

## RHOMBOHEDRAL_A7 (Gd–Sb)

- Id: `phase:gd-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:gd-sb:a7-rhombohedral, corpus:phase:gd-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.intermet.2007.04.003:Sb  
_tdb: _tdb:GdSb-07Li.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `c37a95274d9b860f…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## BCC_A2 (Gd–Sb)

- Id: `phase:gd-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1500.84–1586.12 K, x(Sb) 0–0.01911
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:bcc-a2)

Names (3): _corpus: _corpus:phase:gd-sb:bcc-a2  
_paper: _paper:10.1016/j.intermet.2007.04.003:βGd  
_tdb: _tdb:GdSb-07Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): BCC_A2, type code %B, sha256 `c37a95274d9b860f…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : GD% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## FCC_A1 (Gd–Sb)

- Id: `phase:gd-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:gd-sb:fcc-a1  
_tdb: _tdb:GdSb-07Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): FCC_A1, type code %A, sha256 `c37a95274d9b860f…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : GD SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase_

## GD16SB39 (Gd–Sb)

- Id: `phase:gd-sb:gd16sb39`; status `assigned`
- Structure: Gd16Sb39 · mC124 · C2/m (12); type `st:gd16sb39-mc124`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.2909, Sb 0.7091
- Stability: stable in 1 of 1 calculated diagram(s): 300–1053.73 K, x(Sb) 0.70909–0.70909
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:gd16sb39)

Names (3): _corpus: _corpus:phase:gd-sb:gd16sb39  
_paper: _paper:10.1016/j.intermet.2007.04.003:GdSb2  
_tdb: _tdb:GdSb-07Li.tdb:GD16SB39  


### TDB models of GD16SB39 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): GD16SB39, type code %, sha256 `c37a95274d9b860f…`

~~~~text
70: PHASE GD16SB39 % 2 16 39 !
71: CONST GD16SB39 : GD : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## GD4SB3_D73 (Gd–Sb)

- Id: `phase:gd-sb:gd4sb3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 0.5714, Sb 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–2047.6 K, x(Sb) 0.42857–0.42857
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:gd4sb3-d73)

Names (3): _corpus: _corpus:phase:gd-sb:gd4sb3-d73  
_paper: _paper:10.1016/j.intermet.2007.04.003:Gd4Sb3  
_tdb: _tdb:GdSb-07Li.tdb:GD4SB3_D73  


### TDB models of GD4SB3_D73 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): GD4SB3_D73, type code %, sha256 `c37a95274d9b860f…`

~~~~text
55: PHASE GD4SB3_D73 % 2 4 3 !
56: CONST GD4SB3_D73 : GD : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## GD5SB3_D88 (Gd–Sb)

- Id: `phase:gd-sb:gd5sb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 0.6250, Sb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1917.33 K, x(Sb) 0.375–0.375
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:gd5sb3-d88)

Names (3): _corpus: _corpus:phase:gd-sb:gd5sb3-d88  
_paper: _paper:10.1016/j.intermet.2007.04.003:Gd5Sb3  
_tdb: _tdb:GdSb-07Li.tdb:GD5SB3_D88  


### TDB models of GD5SB3_D88 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): GD5SB3_D88, type code %, sha256 `c37a95274d9b860f…`

~~~~text
50: PHASE GD5SB3_D88 % 2 5 3 !
51: CONST GD5SB3_D88 : GD : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## GDSB_B1 (Gd–Sb)

- Id: `phase:gd-sb:gdsb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2113.15 K, x(Sb) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:gdsb-b1)

Names (4): _corpus: _corpus:phase:gd-sb:gdsb-b1  
_paper: _paper:10.1016/j.intermet.2007.04.003:GdSb, paper:10.1016/j.intermet.2007.04.003:αGdSb  
_tdb: _tdb:GdSb-07Li.tdb:GDSB_B1  


### TDB models of GDSB_B1 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): GDSB_B1, type code %, sha256 `c37a95274d9b860f…`

~~~~text
60: PHASE GDSB_B1 % 2 1 1 !
61: CONST GDSB_B1 : GD : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## GDSB_BETA (Gd–Sb)

- Id: `phase:gd-sb:gdsb-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Fm-3m (225) — on-hull MP GdSb at x(SB)=0.5000
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD Gd1 Sb1 at x(SB)=0.5000
- Candidate (literature_printed): (GdSb) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (GdSb) — Hallstedt 2025 mmc2 row for GDSB_BETA: GdSb
- Stoichiometry: Gd 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 2113.15–2400.73 K, x(Sb) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:gdsb-beta)

Names (4): _corpus: _corpus:phase:gd-sb:gdsb-beta  
_paper: _paper:10.1016/j.intermet.2007.04.003:BGdSb, paper:10.1016/j.intermet.2007.04.003:βGdSb  
_tdb: _tdb:GdSb-07Li.tdb:GDSB_BETA  


### TDB models of GDSB_BETA (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): GDSB_BETA, type code %, sha256 `c37a95274d9b860f…`

~~~~text
65: PHASE GDSB_BETA % 2 1 1 !
66: CONST GDSB_BETA : GD : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## HCP_A3 (Gd–Sb)

- Id: `phase:gd-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1508.15 K, x(Sb) 0–0.04024
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:gd-sb:hcp-a3  
_paper: _paper:10.1016/j.intermet.2007.04.003:αGd  
_tdb: _tdb:GdSb-07Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): HCP_A3, type code %A, sha256 `c37a95274d9b860f…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : GD% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

## LIQUID (Gd–Sb)

- Id: `phase:gd-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 902.91–2500 K, x(Sb) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-sb:liquid)

Names (4): _corpus: _corpus:phase:gd-sb:liquid  
_paper: _paper:10.1016/j.intermet.2007.04.003:L, paper:10.1016/j.intermet.2007.04.003:liquid  
_tdb: _tdb:GdSb-07Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GdSb-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSb-07Li.tdb): LIQUID, type code %, sha256 `c37a95274d9b860f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : GD SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2007.04.003](https://doi.org/10.1016/j.intermet.2007.04.003) J.Q. Li, Y.X. Jian, H.L. Chen, Y.Q. Liu, Thermodynamic assessment of the Gd–Sb system, Intermetallics 15, 1332-1336 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90075-5](https://doi.org/10.1016/0022-5088%2886%2990075-5) M.N. Abdusalyamova, O.R. Burnashev, K.Y. Mironov, The alloy systems Ln-Sb, Journal of the Less Common Metals 125, 1-6 (1986).  
_cited as the source of values for this phase_

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
