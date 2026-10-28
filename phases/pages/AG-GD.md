# Ag–Gd phases

> Ag–Gd system: 7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-GD.html · Markdown: https://data.orchid-project.org/phases/pages/AG-GD.md

7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-GD) · [full JSON](https://data.orchid-project.org/phases/systems/AG-GD.json) · [Ag–Gd system page](https://data.orchid-project.org/systems/AG-GD.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-GD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Gd system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2GD_C11B](#phase-ag-gd-ag2gd-c11b); _phase:ag-gd:ag2gd-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1104.66 K, x(Gd) 0.33333–0.33333 | 10 | 2 |
| [AG51GD14](#phase-ag-gd-ag51gd14); _phase:ag-gd:ag51gd14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1245.13 K, x(Gd) 0.21538–0.21538 | 16 | 2 |
| [AGGD_B2](#phase-ag-gd-aggd-b2); _phase:ag-gd:aggd-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1395.91 K, x(Gd) 0.5–0.5 | 15 | 2 |
| [BCC_A2](#phase-ag-gd-bcc-a2); _phase:ag-gd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1507.85–2499.83 K, x(Gd) 0.99849–1 | 3 | 2 |
| [FCC_A1](#phase-ag-gd-fcc-a1); _phase:ag-gd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1239.85 K, x(Gd) 0–0.00856 | 9 | 2 |
| [HCP_A3](#phase-ag-gd-hcp-a3); _phase:ag-gd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1582.85 K, x(Gd) 0.99713–1 | 5 | 2 |
| [LIQUID](#phase-ag-gd-liquid); _phase:ag-gd:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1052.14–2500 K, x(Gd) 0–1 | 37 | 2 |

## AG2GD_C11B (Ag–Gd)

- Id: `phase:ag-gd:ag2gd-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.6667, Gd 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1104.66 K, x(Gd) 0.33333–0.33333
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-gd:ag2gd-c11b)

Names (5): _corpus: _corpus:phase:ag-gd:ag2gd-c11b  
_paper: _paper:10.1016/j.jallcom.2007.11.049:Ag2Gd, paper:10.1016/j.jallcom.2008.09.129:Ag2Gd  
_tdb: _tdb:AgGd-08Wan.tdb:AG2GD_C11B, tdb:AgGd-09Wan.tdb:AG2GD_C11B  


### TDB models of AG2GD_C11B (2): PHASE and CONSTITUENT statements as written

[AgGd-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-08Wan.tdb): AG2GD_C11B, type code %, sha256 `7fcc4d1b12e901c5…`

~~~~text
48: PHASE AG2GD_C11B % 2 2 1 !
49: CONST AG2GD_C11B : AG : GD : !
~~~~

[AgGd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-09Wan.tdb): AG2GD_C11B, type code %, sha256 `80addf620c78d7fe…`

~~~~text
51: PHASE AG2GD_C11B % 2 2 1 !
52: CONST AG2GD_C11B : AG : GD : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.11.049](https://doi.org/10.1016/j.jallcom.2007.11.049) H. Wang, L.G. Zhang, W.J. Zhu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Gd binary system, Journal of Alloys and Compounds 466, 165-168 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90049-5](https://doi.org/10.1016/0022-5088%2872%2990049-5) Gonde Kiessler, Erich Gebhardt, Siegfried Steeb, Das system silber-gadolinium, Journal of the Less Common Metals 26, 293-298 (1972).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_

## AG51GD14 (Ag–Gd)

- Id: `phase:ag-gd:ag51gd14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.7846, Gd 0.2154
- Stability: stable in 2 of 2 calculated diagram(s): 300–1245.13 K, x(Gd) 0.21538–0.21538
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-gd:ag51gd14)

Names (5): _corpus: _corpus:phase:ag-gd:ag51gd14  
_paper: _paper:10.1016/j.jallcom.2007.11.049:Ag51Gd14, paper:10.1016/j.jallcom.2008.09.129:Ag51Gd14  
_tdb: _tdb:AgGd-08Wan.tdb:AG51GD14, tdb:AgGd-09Wan.tdb:AG51GD14  


### TDB models of AG51GD14 (2): PHASE and CONSTITUENT statements as written

[AgGd-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-08Wan.tdb): AG51GD14, type code %, sha256 `7fcc4d1b12e901c5…`

~~~~text
43: PHASE AG51GD14 % 2 51 14 !
44: CONST AG51GD14 : AG : GD : !
~~~~

[AgGd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-09Wan.tdb): AG51GD14, type code %, sha256 `80addf620c78d7fe…`

~~~~text
46: PHASE AG51GD14 % 2 51 14 !
47: CONST AG51GD14 : AG : GD : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.11.049](https://doi.org/10.1016/j.jallcom.2007.11.049) H. Wang, L.G. Zhang, W.J. Zhu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Gd binary system, Journal of Alloys and Compounds 466, 165-168 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90049-5](https://doi.org/10.1016/0022-5088%2872%2990049-5) Gonde Kiessler, Erich Gebhardt, Siegfried Steeb, Das system silber-gadolinium, Journal of the Less Common Metals 26, 293-298 (1972).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_

## AGGD_B2 (Ag–Gd)

- Id: `phase:ag-gd:aggd-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabewyd and oqmd-10632, space group 221
- Stoichiometry: Ag 0.5000, Gd 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1395.91 K, x(Gd) 0.5–0.5
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-gd:aggd-b2)

Names (7): _corpus: _corpus:phase:ag-gd:aggd-b2  
_mp: _mp:mp-aaabewyd  
_oqmd: _oqmd:oqmd-10632  
_paper: _paper:10.1016/j.jallcom.2007.11.049:AgGd, paper:10.1016/j.jallcom.2008.09.129:AgGd  
_tdb: _tdb:AgGd-08Wan.tdb:AGGD_B2, tdb:AgGd-09Wan.tdb:AGGD_B2  


### TDB models of AGGD_B2 (2): PHASE and CONSTITUENT statements as written

[AgGd-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-08Wan.tdb): AGGD_B2, type code %, sha256 `7fcc4d1b12e901c5…`

~~~~text
53: PHASE AGGD_B2 % 2 1 1 !
54: CONST AGGD_B2 : AG : GD : !
~~~~

[AgGd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-09Wan.tdb): AGGD_B2, type code %A, sha256 `80addf620c78d7fe…`

~~~~text
56: PHASE AGGD_B2 %A 2 1 1 !
57: CONST AGGD_B2 : AG : GD : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.11.049](https://doi.org/10.1016/j.jallcom.2007.11.049) H. Wang, L.G. Zhang, W.J. Zhu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Gd binary system, Journal of Alloys and Compounds 466, 165-168 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90049-5](https://doi.org/10.1016/0022-5088%2872%2990049-5) Gonde Kiessler, Erich Gebhardt, Siegfried Steeb, Das system silber-gadolinium, Journal of the Less Common Metals 26, 293-298 (1972).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Gd)

- Id: `phase:ag-gd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1507.85–2499.83 K, x(Gd) 0.99849–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-gd:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-gd:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.09.129:βGd  
_tdb: _tdb:AgGd-08Wan.tdb:BCC_A2, tdb:AgGd-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgGd-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-08Wan.tdb): BCC_A2, type code %B, sha256 `7fcc4d1b12e901c5…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG GD% : VA : !
~~~~

[AgGd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-09Wan.tdb): BCC_A2, type code %B, sha256 `80addf620c78d7fe…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AG GD% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.11.049](https://doi.org/10.1016/j.jallcom.2007.11.049) H. Wang, L.G. Zhang, W.J. Zhu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Gd binary system, Journal of Alloys and Compounds 466, 165-168 (2008).  
_assessment that models this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(72)90049-5](https://doi.org/10.1016/0022-5088%2872%2990049-5) Gonde Kiessler, Erich Gebhardt, Siegfried Steeb, Das system silber-gadolinium, Journal of the Less Common Metals 26, 293-298 (1972).  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Gd)

- Id: `phase:ag-gd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1239.85 K, x(Gd) 0–0.00856
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-gd:fcc-a1)

Names (5): _corpus: _corpus:phase:ag-gd:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.11.049:Fcc(Ag), paper:10.1016/j.jallcom.2008.09.129:(Ag)  
_tdb: _tdb:AgGd-08Wan.tdb:FCC_A1, tdb:AgGd-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgGd-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-08Wan.tdb): FCC_A1, type code %A, sha256 `7fcc4d1b12e901c5…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% GD : VA : !
~~~~

[AgGd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-09Wan.tdb): FCC_A1, type code %A, sha256 `80addf620c78d7fe…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AG% GD : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.11.049](https://doi.org/10.1016/j.jallcom.2007.11.049) H. Wang, L.G. Zhang, W.J. Zhu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Gd binary system, Journal of Alloys and Compounds 466, 165-168 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90049-5](https://doi.org/10.1016/0022-5088%2872%2990049-5) Gonde Kiessler, Erich Gebhardt, Siegfried Steeb, Das system silber-gadolinium, Journal of the Less Common Metals 26, 293-298 (1972).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Gd)

- Id: `phase:ag-gd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1582.85 K, x(Gd) 0.99713–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-gd:hcp-a3)

Names (5): _corpus: _corpus:phase:ag-gd:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2007.11.049:Gd, paper:10.1016/j.jallcom.2008.09.129:αGd  
_tdb: _tdb:AgGd-08Wan.tdb:HCP_A3, tdb:AgGd-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgGd-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-08Wan.tdb): HCP_A3, type code %A, sha256 `7fcc4d1b12e901c5…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG GD% : VA : !
~~~~

[AgGd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-09Wan.tdb): HCP_A3, type code %A, sha256 `80addf620c78d7fe…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AG GD% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.11.049](https://doi.org/10.1016/j.jallcom.2007.11.049) H. Wang, L.G. Zhang, W.J. Zhu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Gd binary system, Journal of Alloys and Compounds 466, 165-168 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90049-5](https://doi.org/10.1016/0022-5088%2872%2990049-5) Gonde Kiessler, Erich Gebhardt, Siegfried Steeb, Das system silber-gadolinium, Journal of the Less Common Metals 26, 293-298 (1972).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_

## LIQUID (Ag–Gd)

- Id: `phase:ag-gd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1052.14–2500 K, x(Gd) 0–1
- Literature: 37 values (37 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-gd:liquid)

Names (5): _corpus: _corpus:phase:ag-gd:liquid  
_paper: _paper:10.1016/j.jallcom.2007.11.049:L, paper:10.1016/j.jallcom.2008.09.129:L  
_tdb: _tdb:AgGd-08Wan.tdb:LIQUID, tdb:AgGd-09Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgGd-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-08Wan.tdb): LIQUID, type code %, sha256 `7fcc4d1b12e901c5…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG GD : !
~~~~

[AgGd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGd-09Wan.tdb): LIQUID, type code %, sha256 `80addf620c78d7fe…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AG GD : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.11.049](https://doi.org/10.1016/j.jallcom.2007.11.049) H. Wang, L.G. Zhang, W.J. Zhu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Gd binary system, Journal of Alloys and Compounds 466, 165-168 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90049-5](https://doi.org/10.1016/0022-5088%2872%2990049-5) Gonde Kiessler, Erich Gebhardt, Siegfried Steeb, Das system silber-gadolinium, Journal of the Less Common Metals 26, 293-298 (1972).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
