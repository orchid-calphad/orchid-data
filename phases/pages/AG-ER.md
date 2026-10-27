# Ag–Er phases

> Ag–Er system: 7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-ER.html · Markdown: https://data.orchid-project.org/phases/pages/AG-ER.md

7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-ER) · [full JSON](https://data.orchid-project.org/phases/systems/AG-ER.json) · [Ag–Er system page](https://data.orchid-project.org/systems/AG-ER.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-ER.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Er system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2ER_C11B](#phase-ag-er-ag2er-c11b); _phase:ag-er:ag2er-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1295.16 K, x(Er) 0.33333–0.33333 | 15 | 2 |
| [AG51ER14](#phase-ag-er-ag51er14); _phase:ag-er:ag51er14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1203.74 K, x(Er) 0.21538–0.22268 | 17 | 2 |
| [AGER_B2](#phase-ag-er-ager-b2); _phase:ag-er:ager-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1475.78 K, x(Er) 0.5–0.5 | 15 | 2 |
| [BCC_A2](#phase-ag-er-bcc-a2); _phase:ag-er:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ag-er-fcc-a1); _phase:ag-er:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1239.98 K, x(Er) 0–0.02978 | 7 | 2 |
| [HCP_A3](#phase-ag-er-hcp-a3); _phase:ag-er:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.86 K, x(Er) 0.99963–1 | 5 | 2 |
| [LIQUID](#phase-ag-er-liquid); _phase:ag-er:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1059.85–2500 K, x(Er) 0–1 | 37 | 2 |

## AG2ER_C11B (Ag–Er)

- Id: `phase:ag-er:ag2er-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.6667, Er 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1295.16 K, x(Er) 0.33333–0.33333
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-er:ag2er-c11b)

Names (5): _corpus: _corpus:phase:ag-er:ag2er-c11b  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Ag2Er, paper:10.1016/j.jallcom.2009.10.039:Ag2Er  
_tdb: _tdb:AgEr-10Lon.tdb:AG2ER_C11B, tdb:AgEr-10Wan.tdb:AG2ER_C11B  


### TDB models of AG2ER_C11B (2): PHASE and CONSTITUENT statements as written

[AgEr-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Lon.tdb): AG2ER_C11B, type code %, sha256 `3e7d3227cef73c92…`

~~~~text
46: PHASE AG2ER_C11B % 2 2 1 !
47: CONST AG2ER_C11B : AG : ER : !
~~~~

[AgEr-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Wan.tdb): AG2ER_C11B, type code %, sha256 `b2618a17c51bcc1d…`

~~~~text
53: PHASE AG2ER_C11B % 2 2 1 !
54: CONST AG2ER_C11B : AG : ER : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90178-7](https://doi.org/10.1016/0022-5088%2869%2990178-7) E. Gebhardt, I. Elssner, J. Höhler, Das system Silber-Erbium, Journal of the Less Common Metals 19, 329-335 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871168](https://doi.org/10.1007/bf02871168) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (1) (1985) 17–19.  
_cited as the source of values for this phase_

## AG51ER14 (Ag–Er)

- Id: `phase:ag-er:ag51er14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–1203.74 K, x(Er) 0.21538–0.22268
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-er:ag51er14)

Names (5): _corpus: _corpus:phase:ag-er:ag51er14  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Ag51Er14, paper:10.1016/j.jallcom.2009.10.039:Ag51Er14  
_tdb: _tdb:AgEr-10Lon.tdb:AG51ER14, tdb:AgEr-10Wan.tdb:AG51ER14  


### TDB models of AG51ER14 (2): PHASE and CONSTITUENT statements as written

[AgEr-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Lon.tdb): AG51ER14, type code %, sha256 `3e7d3227cef73c92…`

~~~~text
41: PHASE AG51ER14 % 2 51 14 !
42: CONST AG51ER14 : AG : ER : !
~~~~

[AgEr-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Wan.tdb): AG51ER14, type code %, sha256 `b2618a17c51bcc1d…`

~~~~text
48: PHASE AG51ER14 % 2 51 14 !
49: CONST AG51ER14 : AG% ER : ER : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90178-7](https://doi.org/10.1016/0022-5088%2869%2990178-7) E. Gebhardt, I. Elssner, J. Höhler, Das system Silber-Erbium, Journal of the Less Common Metals 19, 329-335 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871168](https://doi.org/10.1007/bf02871168) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (1) (1985) 17–19.  
_cited as the source of values for this phase_

## AGER_B2 (Ag–Er)

- Id: `phase:ag-er:ager-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadwv and oqmd-10623, space group 221
- Stoichiometry: Ag 0.5000, Er 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1475.78 K, x(Er) 0.5–0.5
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-er:ager-b2)

Names (7): _corpus: _corpus:phase:ag-er:ager-b2  
_mp: _mp:mp-aaaaadwv  
_oqmd: _oqmd:oqmd-10623  
_paper: _paper:10.1016/j.jallcom.2009.09.036:AgEr, paper:10.1016/j.jallcom.2009.10.039:AgEr  
_tdb: _tdb:AgEr-10Lon.tdb:AGER_B2, tdb:AgEr-10Wan.tdb:AGER_B2  


### TDB models of AGER_B2 (2): PHASE and CONSTITUENT statements as written

[AgEr-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Lon.tdb): AGER_B2, type code %A, sha256 `3e7d3227cef73c92…`

~~~~text
51: PHASE AGER_B2 %A 2 1 1 !
52: CONST AGER_B2 : AG : ER : !
~~~~

[AgEr-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Wan.tdb): AGER_B2, type code %A, sha256 `b2618a17c51bcc1d…`

~~~~text
58: PHASE AGER_B2 %A 2 1 1 !
59: CONST AGER_B2 : AG : ER : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90178-7](https://doi.org/10.1016/0022-5088%2869%2990178-7) E. Gebhardt, I. Elssner, J. Höhler, Das system Silber-Erbium, Journal of the Less Common Metals 19, 329-335 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871168](https://doi.org/10.1007/bf02871168) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (1) (1985) 17–19.  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Er)

- Id: `phase:ag-er:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-er:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-er:bcc-a2  
_tdb: _tdb:AgEr-10Lon.tdb:BCC_A2, tdb:AgEr-10Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgEr-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Lon.tdb): BCC_A2, type code %B, sha256 `3e7d3227cef73c92…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG ER : VA : !
~~~~

[AgEr-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Wan.tdb): BCC_A2, type code %B, sha256 `b2618a17c51bcc1d…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AG ER : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010).  
_assessment that models this phase_

## FCC_A1 (Ag–Er)

- Id: `phase:ag-er:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1239.98 K, x(Er) 0–0.02978
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-er:fcc-a1)

Names (5): _corpus: _corpus:phase:ag-er:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Fcc(Ag), paper:10.1016/j.jallcom.2009.10.039:(Ag)  
_tdb: _tdb:AgEr-10Lon.tdb:FCC_A1, tdb:AgEr-10Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgEr-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Lon.tdb): FCC_A1, type code %A, sha256 `3e7d3227cef73c92…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% ER : VA : !
~~~~

[AgEr-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Wan.tdb): FCC_A1, type code %A, sha256 `b2618a17c51bcc1d…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AG% ER : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90178-7](https://doi.org/10.1016/0022-5088%2869%2990178-7) E. Gebhardt, I. Elssner, J. Höhler, Das system Silber-Erbium, Journal of the Less Common Metals 19, 329-335 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871168](https://doi.org/10.1007/bf02871168) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (1) (1985) 17–19.  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Er)

- Id: `phase:ag-er:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.86 K, x(Er) 0.99963–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-er:hcp-a3)

Names (5): _corpus: _corpus:phase:ag-er:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Hcp(Er), paper:10.1016/j.jallcom.2009.10.039:(Er)  
_tdb: _tdb:AgEr-10Lon.tdb:HCP_A3, tdb:AgEr-10Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgEr-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Lon.tdb): HCP_A3, type code %A, sha256 `3e7d3227cef73c92…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG ER% : VA : !
~~~~

[AgEr-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Wan.tdb): HCP_A3, type code %A, sha256 `b2618a17c51bcc1d…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AG ER% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90178-7](https://doi.org/10.1016/0022-5088%2869%2990178-7) E. Gebhardt, I. Elssner, J. Höhler, Das system Silber-Erbium, Journal of the Less Common Metals 19, 329-335 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871168](https://doi.org/10.1007/bf02871168) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (1) (1985) 17–19.  
_cited as the source of values for this phase_

## LIQUID (Ag–Er)

- Id: `phase:ag-er:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1059.85–2500 K, x(Er) 0–1
- Literature: 37 values (37 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-er:liquid)

Names (5): _corpus: _corpus:phase:ag-er:liquid  
_paper: _paper:10.1016/j.jallcom.2009.09.036:L, paper:10.1016/j.jallcom.2009.10.039:L  
_tdb: _tdb:AgEr-10Lon.tdb:LIQUID, tdb:AgEr-10Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgEr-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Lon.tdb): LIQUID, type code %, sha256 `3e7d3227cef73c92…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG ER : !
~~~~

[AgEr-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgEr-10Wan.tdb): LIQUID, type code %, sha256 `b2618a17c51bcc1d…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AG ER : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90178-7](https://doi.org/10.1016/0022-5088%2869%2990178-7) E. Gebhardt, I. Elssner, J. Höhler, Das system Silber-Erbium, Journal of the Less Common Metals 19, 329-335 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871168](https://doi.org/10.1007/bf02871168) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (1) (1985) 17–19.  
_cited as the source of values for this phase_

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
