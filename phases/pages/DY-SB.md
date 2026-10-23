# Dy–Sb phases

> Dy–Sb system: 12 phases (tier A 7, liquid 1, needs_review 2, unresolved_no_candidates 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/DY-SB.html · Markdown: https://data.orchid-project.org/phases/pages/DY-SB.md

12 phases (tier A 7, liquid 1, needs_review 2, unresolved_no_candidates 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=DY-SB) · [full JSON](https://data.orchid-project.org/phases/systems/DY-SB.json) · [Dy–Sb system page](https://data.orchid-project.org/systems/DY-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/DY-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Dy–Sb system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-dy-sb-a7-rhombohedral); _phase:dy-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 2 | 1 |
| [BCC_A2](#phase-dy-sb-bcc-a2); _phase:dy-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1648.83–1685.1 K, x(Sb) 0–0.00169 | 2 | 1 |
| [DY4SB3_HT](#phase-dy-sb-dy4sb3); _phase:dy-sb:dy4sb3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1903.97–2040.3 K, x(Sb) 0.42857–0.42857 | 6 | 1 |
| [DY4SB3_D73](#phase-dy-sb-dy4sb3-d73); _phase:dy-sb:dy4sb3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1095.44–1903.97 K, x(Sb) 0.42857–0.42857 | 4 | 1 |
| [DY4SB3-HT](#phase-dy-sb-dy4sb3-ht); _phase:dy-sb:dy4sb3-ht_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |
| [DY5SB3_D88](#phase-dy-sb-dy5sb3-d88); _phase:dy-sb:dy5sb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1944.87 K, x(Sb) 0.375–0.375 | 6 | 1 |
| [DYSB_HT](#phase-dy-sb-dysb); _phase:dy-sb:dysb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2162.56–2422.56 K, x(Sb) 0.5–0.5 | 8 | 1 |
| [DYSB_B1](#phase-dy-sb-dysb-b1); _phase:dy-sb:dysb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2162.56 K, x(Sb) 0.5–0.5 | 12 | 1 |
| [DYSB-HT](#phase-dy-sb-dysb-ht); _phase:dy-sb:dysb-ht_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |
| [FCC_A1](#phase-dy-sb-fcc-a1); _phase:dy-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-dy-sb-hcp-a3); _phase:dy-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1654.15 K, x(Sb) 0–0.00505 | 4 | 1 |
| [LIQUID](#phase-dy-sb-liquid); _phase:dy-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 897.96–2500 K, x(Sb) 0–1 | 16 | 1 |

## RHOMBOHEDRAL_A7 (Dy–Sb)

- Id: `phase:dy-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:dy-sb:a7-rhombohedral, corpus:phase:dy-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2009.09.006:Rho  
_tdb: _tdb:DySb-10Lon.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `f3df3a161165c0af…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Dy–Sb)

- Id: `phase:dy-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1648.83–1685.1 K, x(Sb) 0–0.00169
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:bcc-a2)

Names (3): _corpus: _corpus:phase:dy-sb:bcc-a2  
_paper: _paper:10.1016/j.tca.2009.09.006:Bcc(Dy)  
_tdb: _tdb:DySb-10Lon.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): BCC_A2, type code %B, sha256 `f3df3a161165c0af…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : DY% SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_

## DY4SB3_HT (Dy–Sb)

- Id: `phase:dy-sb:dy4sb3`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Dy4Sb3-ht) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Dy4Sb3-ht) — Hallstedt 2025 mmc2 row for DY4SB3_HT: Dy4Sb3 (high T)
- Stoichiometry: Dy 0.5714, Sb 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 1903.97–2040.3 K, x(Sb) 0.42857–0.42857
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:dy4sb3)

Names (3): _corpus: _corpus:phase:dy-sb:dy4sb3  
_paper: _paper:10.1016/j.tca.2009.09.006:β.Dy4Sb3  
_tdb: _tdb:DySb-10Lon.tdb:DY4SB3_HT  


### TDB models of DY4SB3_HT (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): DY4SB3_HT, type code %, sha256 `f3df3a161165c0af…`

~~~~text
57: PHASE DY4SB3_HT % 2 4 3 !
58: CONST DY4SB3_HT : DY : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_

## DY4SB3_D73 (Dy–Sb)

- Id: `phase:dy-sb:dy4sb3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 0.5714, Sb 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 1095.44–1903.97 K, x(Sb) 0.42857–0.42857
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:dy4sb3-d73)

Names (3): _corpus: _corpus:phase:dy-sb:dy4sb3-d73  
_paper: _paper:10.1016/j.tca.2009.09.006:α.Dy4Sb3  
_tdb: _tdb:DySb-10Lon.tdb:DY4SB3_D73  


### TDB models of DY4SB3_D73 (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): DY4SB3_D73, type code %, sha256 `f3df3a161165c0af…`

~~~~text
52: PHASE DY4SB3_D73 % 2 4 3 !
53: CONST DY4SB3_D73 : DY : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(03)00080-x](https://doi.org/10.1016/s0925-8388%2803%2900080-x) A.V. Morozkin, Dy–Sb–Si system at 1100 K and ternary intermetallic phases in the Dy–Sb–Si and Gd–Sb–Si systems, Journal of Alloys and Compounds 358, L6-L8 (2003).  
_cited as the source of values for this phase_

## DY4SB3-HT (Dy–Sb)

- Id: `phase:dy-sb:dy4sb3-ht`; status `unresolved_no_candidates`
- No structure assigned. Why: no_bundled_tdb_model; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:dy4sb3-ht)

Names (1): _corpus: _corpus:phase:dy-sb:dy4sb3-ht  


## DY5SB3_D88 (Dy–Sb)

- Id: `phase:dy-sb:dy5sb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacprmd and oqmd-656229, space group 193
- Stoichiometry: Dy 0.6250, Sb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1944.87 K, x(Sb) 0.375–0.375
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:dy5sb3-d88)

Names (5): _corpus: _corpus:phase:dy-sb:dy5sb3-d88  
_mp: _mp:mp-aaacprmd  
_oqmd: _oqmd:oqmd-656229  
_paper: _paper:10.1016/j.tca.2009.09.006:Dy5Sb3  
_tdb: _tdb:DySb-10Lon.tdb:DY5SB3_D88  


### TDB models of DY5SB3_D88 (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): DY5SB3_D88, type code %, sha256 `f3df3a161165c0af…`

~~~~text
47: PHASE DY5SB3_D88 % 2 5 3 !
48: CONST DY5SB3_D88 : DY : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(03)00080-x](https://doi.org/10.1016/s0925-8388%2803%2900080-x) A.V. Morozkin, Dy–Sb–Si system at 1100 K and ternary intermetallic phases in the Dy–Sb–Si and Gd–Sb–Si systems, Journal of Alloys and Compounds 358, L6-L8 (2003).  
_cited as the source of values for this phase_

## DYSB_HT (Dy–Sb)

- Id: `phase:dy-sb:dysb`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Fm-3m (225) — on-hull MP DySb at x(SB)=0.5000
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Dy1 Sb1 at x(SB)=0.5000
- Candidate (literature_printed): (DySb-ht) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (DySb-ht) — Hallstedt 2025 mmc2 row for DYSB_HT: DySb (high T)
- Stoichiometry: Dy 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 2162.56–2422.56 K, x(Sb) 0.5–0.5
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:dysb)

Names (3): _corpus: _corpus:phase:dy-sb:dysb  
_paper: _paper:10.1016/j.tca.2009.09.006:β.DySb  
_tdb: _tdb:DySb-10Lon.tdb:DYSB_HT  


### TDB models of DYSB_HT (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): DYSB_HT, type code %, sha256 `f3df3a161165c0af…`

~~~~text
67: PHASE DYSB_HT % 2 1 1 !
68: CONST DYSB_HT : DY : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_

## DYSB_B1 (Dy–Sb)

- Id: `phase:dy-sb:dysb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2162.56 K, x(Sb) 0.5–0.5
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:dysb-b1)

Names (3): _corpus: _corpus:phase:dy-sb:dysb-b1  
_paper: _paper:10.1016/j.tca.2009.09.006:α.DySb  
_tdb: _tdb:DySb-10Lon.tdb:DYSB_B1  


### TDB models of DYSB_B1 (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): DYSB_B1, type code %, sha256 `f3df3a161165c0af…`

~~~~text
62: PHASE DYSB_B1 % 2 1 1 !
63: CONST DYSB_B1 : DY : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(03)00080-x](https://doi.org/10.1016/s0925-8388%2803%2900080-x) A.V. Morozkin, Dy–Sb–Si system at 1100 K and ternary intermetallic phases in the Dy–Sb–Si and Gd–Sb–Si systems, Journal of Alloys and Compounds 358, L6-L8 (2003).  
_cited as the source of values for this phase_

## DYSB-HT (Dy–Sb)

- Id: `phase:dy-sb:dysb-ht`; status `unresolved_no_candidates`
- No structure assigned. Why: no_bundled_tdb_model; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:dysb-ht)

Names (1): _corpus: _corpus:phase:dy-sb:dysb-ht  


## FCC_A1 (Dy–Sb)

- Id: `phase:dy-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:dy-sb:fcc-a1  
_tdb: _tdb:DySb-10Lon.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): FCC_A1, type code %A, sha256 `f3df3a161165c0af…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : DY SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase_

## HCP_A3 (Dy–Sb)

- Id: `phase:dy-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1654.15 K, x(Sb) 0–0.00505
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:dy-sb:hcp-a3  
_paper: _paper:10.1016/j.tca.2009.09.006:Hcp(Dy)  
_tdb: _tdb:DySb-10Lon.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): HCP_A3, type code %A, sha256 `f3df3a161165c0af…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : DY% SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Dy–Sb)

- Id: `phase:dy-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 897.96–2500 K, x(Sb) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-sb:liquid)

Names (3): _corpus: _corpus:phase:dy-sb:liquid  
_paper: _paper:10.1016/j.tca.2009.09.006:L  
_tdb: _tdb:DySb-10Lon.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[DySb-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb): LIQUID, type code %, sha256 `f3df3a161165c0af…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : DY SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010).  
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
