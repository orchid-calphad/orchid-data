# Bi–Zn phases

> Bi–Zn system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/BI-ZN.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/BI-ZN.json) · [Bi–Zn system page](https://data.orchid-project.org/systems/BI-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Zn system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-zn-a7-rhombohedral); _phase:bi-zn:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–544.55 K, x(Zn) 0–0.01636 | 5 | 5 |
| [BCC_A2](#phase-bi-zn-bcc-a2); _phase:bi-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-bi-zn-fcc-a1); _phase:bi-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-bi-zn-hcp-a3); _phase:bi-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2498.93 K, x(Zn) 0.99584–1 | 8 | 5 |
| [LIQUID](#phase-bi-zn-liquid); _phase:bi-zn:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 520.1–2500 K, x(Zn) 0–1 | 22 | 5 |

## RHOMBOHEDRAL_A7 (Bi–Zn)

- Id: `phase:bi-zn:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–544.55 K, x(Zn) 0–0.01636
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zn:a7-rhombohedral)

Names (9): _corpus: _corpus:phase:bi-zn:a7-rhombohedral, corpus:phase:bi-zn:rhombohedral-a7  
_paper: _paper:10.1016/s0364-5916(00)00011-0:Rhombohedral solution, paper:10.1088/0965-0393/13/3/006:Bi  
_tdb: _tdb:BiZn-00Mal-LB.tdb:RHOMBOHEDRAL_A7, tdb:BiZn-03Kim.tdb:RHOMBOHEDRAL_A7, tdb:BiZn-05Dja.tdb:RHOMBOHEDRAL_A7, tdb:BiZn-07Viz.tdb:RHOMBOHEDRAL_A7, tdb:BiZn-85Gir.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (5): PHASE and CONSTITUENT statements as written

[BiZn-00Mal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-00Mal-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `dc7817b37fd01700…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI% ZN : !
~~~~

[BiZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-03Kim.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `33acdc44f5718ce5…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : BI% ZN : !
~~~~

[BiZn-05Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-05Dja.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `f5ecc95e0f1b3aaf…`

~~~~text
36: PHASE RHOMBOHEDRAL_A7 % 1 1 !
37: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiZn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-07Viz.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `0d71ac7c1215c028…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : BI% ZN : !
~~~~

[BiZn-85Gir.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-85Gir.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `303007160c50d88d…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1088/0965-0393/13/3/006](https://doi.org/10.1088/0965-0393/13/3/006) Y Djaballah, L Bennour, F Bouharkat, A Belgacem-Bouzida, Thermodynamic assessment of the binary system (Bi–Zn), Modelling Simul. Mater. Sci. Eng. 13, 361-369 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(00)00011-0](https://doi.org/10.1016/S0364-5916%2800%2900011-0) D.V. Malakhov, Calphad, 24, 1-14(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02095-0](https://doi.org/10.1016/0925-8388%2895%2902095-0) F. Bouharkat, J.J. Counioux, J.R. Vignalou, J. Said, Miscibility study in the bismuth-zinc system extension to the isotherms 425 and 500°C of the ternary system BiSbZn, Journal of Alloys and Compounds 238, 149-154 (1996).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Zn)

- Id: `phase:bi-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zn:bcc-a2)

Names (5): _corpus: _corpus:phase:bi-zn:bcc-a2  
_tdb: _tdb:BiZn-00Mal-LB.tdb:BCC_A2, tdb:BiZn-03Kim.tdb:BCC_A2, tdb:BiZn-07Viz.tdb:BCC_A2, tdb:BiZn-85Gir.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[BiZn-00Mal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-00Mal-LB.tdb): BCC_A2, type code %B, sha256 `dc7817b37fd01700…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI ZN : VA : !
~~~~

[BiZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-03Kim.tdb): BCC_A2, type code %B, sha256 `33acdc44f5718ce5…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : BI ZN : VA : !
~~~~

[BiZn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-07Viz.tdb): BCC_A2, type code %B, sha256 `0d71ac7c1215c028…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BI ZN : VA : !
~~~~

[BiZn-85Gir.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-85Gir.tdb): BCC_A2, type code %B, sha256 `303007160c50d88d…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI ZN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00011-0](https://doi.org/10.1016/S0364-5916%2800%2900011-0) D.V. Malakhov, Calphad, 24, 1-14(2000).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_

## FCC_A1 (Bi–Zn)

- Id: `phase:bi-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zn:fcc-a1)

Names (5): _corpus: _corpus:phase:bi-zn:fcc-a1  
_tdb: _tdb:BiZn-00Mal-LB.tdb:FCC_A1, tdb:BiZn-03Kim.tdb:FCC_A1, tdb:BiZn-07Viz.tdb:FCC_A1, tdb:BiZn-85Gir.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[BiZn-00Mal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-00Mal-LB.tdb): FCC_A1, type code %A, sha256 `dc7817b37fd01700…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI ZN : VA : !
~~~~

[BiZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-03Kim.tdb): FCC_A1, type code %A, sha256 `33acdc44f5718ce5…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : BI ZN : VA : !
~~~~

[BiZn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-07Viz.tdb): FCC_A1, type code %A, sha256 `0d71ac7c1215c028…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BI ZN : VA : !
~~~~

[BiZn-85Gir.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-85Gir.tdb): FCC_A1, type code %A, sha256 `303007160c50d88d…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI ZN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00011-0](https://doi.org/10.1016/S0364-5916%2800%2900011-0) D.V. Malakhov, Calphad, 24, 1-14(2000).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_

## HCP_A3 (Bi–Zn)

- Id: `phase:bi-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2498.93 K, x(Zn) 0.99584–1
- Literature: 8 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zn:hcp-a3)

Names (9): _corpus: _corpus:phase:bi-zn:hcp-a3  
_paper: _paper:10.1016/s0364-5916(00)00011-0:HCP solution, paper:10.1016/s0364-5916(00)00011-0:Hexagonal solution, paper:10.1088/0965-0393/13/3/006:Zn  
_tdb: _tdb:BiZn-00Mal-LB.tdb:HCP_A3, tdb:BiZn-03Kim.tdb:HCP_A3, tdb:BiZn-05Dja.tdb:HCP_A3, tdb:BiZn-07Viz.tdb:HCP_A3, tdb:BiZn-85Gir.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[BiZn-00Mal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-00Mal-LB.tdb): HCP_A3, type code %A, sha256 `dc7817b37fd01700…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI ZN% : VA: !
~~~~

[BiZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-03Kim.tdb): HCP_A3, type code %A, sha256 `33acdc44f5718ce5…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : BI ZN% : VA: !
~~~~

[BiZn-05Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-05Dja.tdb): HCP_A3, type code %A, sha256 `f5ecc95e0f1b3aaf…`

~~~~text
31: PHASE HCP_A3 %A 2 1 0.5 !
32: CONST HCP_A3 : ZN : VA: !
~~~~

[BiZn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-07Viz.tdb): HCP_A3, type code %A, sha256 `0d71ac7c1215c028…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BI ZN% : VA: !
~~~~

[BiZn-85Gir.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-85Gir.tdb): HCP_A3, type code %A, sha256 `303007160c50d88d…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI ZN% : VA: !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1088/0965-0393/13/3/006](https://doi.org/10.1088/0965-0393/13/3/006) Y Djaballah, L Bennour, F Bouharkat, A Belgacem-Bouzida, Thermodynamic assessment of the binary system (Bi–Zn), Modelling Simul. Mater. Sci. Eng. 13, 361-369 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(00)00011-0](https://doi.org/10.1016/S0364-5916%2800%2900011-0) D.V. Malakhov, Calphad, 24, 1-14(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02095-0](https://doi.org/10.1016/0925-8388%2895%2902095-0) F. Bouharkat, J.J. Counioux, J.R. Vignalou, J. Said, Miscibility study in the bismuth-zinc system extension to the isotherms 425 and 500°C of the ternary system BiSbZn, Journal of Alloys and Compounds 238, 149-154 (1996).  
_cited as the source of values for this phase_

## LIQUID (Bi–Zn)

- Id: `phase:bi-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 520.1–2500 K, x(Zn) 0–1
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zn:liquid)

Names (11): _corpus: _corpus:phase:bi-zn:liquid, corpus:phase:bi-zn:liquid-2  
_paper: _paper:10.1016/s0364-5916(00)00011-0:Liquid, paper:10.1088/0965-0393/13/3/006:1 liq, paper:10.1088/0965-0393/13/3/006:liq 1, paper:10.1088/0965-0393/13/3/006:liq 2  
_tdb: _tdb:BiZn-00Mal-LB.tdb:LIQUID, tdb:BiZn-03Kim.tdb:LIQUID, tdb:BiZn-05Dja.tdb:LIQUID, tdb:BiZn-07Viz.tdb:LIQUID, tdb:BiZn-85Gir.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[BiZn-00Mal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-00Mal-LB.tdb): LIQUID, type code %, sha256 `dc7817b37fd01700…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI ZN : !
~~~~

[BiZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-03Kim.tdb): LIQUID, type code %, sha256 `33acdc44f5718ce5…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : BI ZN : !
~~~~

[BiZn-05Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-05Dja.tdb): LIQUID, type code %, sha256 `f5ecc95e0f1b3aaf…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : BI ZN : !
~~~~

[BiZn-07Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-07Viz.tdb): LIQUID, type code %, sha256 `0d71ac7c1215c028…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BI ZN : !
~~~~

[BiZn-85Gir.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZn-85Gir.tdb): LIQUID, type code %, sha256 `303007160c50d88d…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI ZN : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1088/0965-0393/13/3/006](https://doi.org/10.1088/0965-0393/13/3/006) Y Djaballah, L Bennour, F Bouharkat, A Belgacem-Bouzida, Thermodynamic assessment of the binary system (Bi–Zn), Modelling Simul. Mater. Sci. Eng. 13, 361-369 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(00)00011-0](https://doi.org/10.1016/S0364-5916%2800%2900011-0) D.V. Malakhov, Calphad, 24, 1-14(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.002](https://doi.org/10.1016/j.calphad.2007.05.002) J. Vizdal, M.H. Braga, A. Kroupa, K.W. Richter, D. Soares, L.F. Malheiros, J. Ferreira, Calphad, 31, 438-48(2007).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02095-0](https://doi.org/10.1016/0925-8388%2895%2902095-0) F. Bouharkat, J.J. Counioux, J.R. Vignalou, J. Said, Miscibility study in the bismuth-zinc system extension to the isotherms 425 and 500°C of the ternary system BiSbZn, Journal of Alloys and Compounds 238, 149-154 (1996).  
_cited as the source of values for this phase_
- [doi:10.3139/146.030390](https://doi.org/10.3139/146.030390) Sung S. Kim, Thomas H. Sanders, Thermodynamic Assessment of the Miscibility Gaps and the Metastable Liquidi in the Zn–Bi, Zn–Pb, and Zn–Tl Systems, MEKU 94, 390-395 (2003).  
_cited as the source of values for this phase_
- [doi:10.1143/jpsj.62.2388](https://doi.org/10.1143/jpsj.62.2388) Satoshi Kanai, Yoshimi Tsuchiya, Sound Velocity in the Liquid Bismuth-Zinc System, J. Phys. Soc. Jpn. 62, 2388-2394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1955-461101](https://doi.org/10.1515/ijmr-1955-461101) Woligang Seith, Heinz Johnen, Jürgen Wagner, Zur Kenntnis von Mischungslücken im flüssigen Zustand bei metallischen Zwei- und Dreistoffsystemen, International Journal of Materials Research 46, 773-779 (1955).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1992-830710](https://doi.org/10.1515/ijmr-1992-830710) Ram Nadan Singh, Ferdinand Sommer, A Simple Model for Demixing Binary Liquid Alloys, International Journal of Materials Research 83, 533-540 (1992).  
_cited as the source of values for this phase_
- [doi:10.2320/matertrans1960.21.226](https://doi.org/10.2320/matertrans1960.21.226) Kazuhisa Okajima, Hiroshi Sakao, Equilibria between the Two Immiscible Liquid Phases in the Zinc-Bismuth System, Trans. JIM 21, 226-236 (1980).  
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
