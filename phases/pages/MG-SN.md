# Mg–Sn phases

> Mg–Sn system: 7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-SN.html · Markdown: https://data.orchid-project.org/phases/pages/MG-SN.md

7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-SN) · [full JSON](https://data.orchid-project.org/phases/systems/MG-SN.json) · [Mg–Sn system page](https://data.orchid-project.org/systems/MG-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Sn system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-mg-sn-a4-diamond); _phase:mg-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [BCT_A5](#phase-mg-sn-a5-bct); _phase:mg-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 8 | 5 |
| [BCC_A2](#phase-mg-sn-bcc-a2); _phase:mg-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-mg-sn-fcc-a1); _phase:mg-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-mg-sn-hcp-a3); _phase:mg-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–935.87 K, x(Sn) 0–0.07118 | 11 | 5 |
| [LIQUID](#phase-mg-sn-liquid); _phase:mg-sn:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 473.15–2500 K, x(Sn) 0–1 | 34 | 5 |
| [MG2SN_C1](#phase-mg-sn-mg2sn-c1); _phase:mg-sn:mg2sn-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1048.62 K, x(Sn) 0.33333–0.34338 | 29 | 5 |

## DIAMOND_A4 (Mg–Sn)

- Id: `phase:mg-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sn:a4-diamond)

Names (6): _corpus: _corpus:phase:mg-sn:a4-diamond  
_tdb: _tdb:MgSn-04Fri.tdb:DIAMOND_A4, tdb:MgSn-10Men.tdb:DIAMOND_A4, tdb:MgSn-12Mie.tdb:DIAMOND_A4, tdb:MgSn-21Zha.tdb:DIAMOND_A4, tdb:MgSn-99Mor.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[MgSn-04Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-04Fri.tdb): DIAMOND_A4, type code %, sha256 `932f4c7c0ab6221d…`

~~~~text
50: PHASE DIAMOND_A4 % 1 1 !
51: CONST DIAMOND_A4 : SN : !
~~~~

[MgSn-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-10Men.tdb): DIAMOND_A4, type code %, sha256 `05ff105fc20ac101…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

[MgSn-12Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-12Mie.tdb): DIAMOND_A4, type code %, sha256 `c5854f47494b5707…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

[MgSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-21Zha.tdb): DIAMOND_A4, type code %, sha256 `d87760e638a43659…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

[MgSn-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-99Mor.tdb): DIAMOND_A4, type code %, sha256 `b130ac8424b73691…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.08.124](https://doi.org/10.1016/j.jallcom.2010.08.124) F.G. Meng, J. Wang, L.B. Liu, Z.P. Jin, Thermodynamic modeling of the Mg–Sn–Zn ternary system, Journal of Alloys and Compounds 508, 570-581 (2010).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_
- [doi:10.2298/JMMB110731008M](https://doi.org/10.2298/JMMB110731008M) J. Miettinen, G. Vassilev, J. Min. Metall. B, 48, 53-62(2012).  
_assessment that models this phase_

## BCT_A5 (Mg–Sn)

- Id: `phase:mg-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sn:a5-bct)

Names (8): _corpus: _corpus:phase:mg-sn:a5-bct, corpus:phase:mg-sn:bct-a5  
_paper: _paper:10.1016/j.jallcom.2010.08.124:bct(Sn)  
_tdb: _tdb:MgSn-04Fri.tdb:BCT_A5, tdb:MgSn-10Men.tdb:BCT_A5, tdb:MgSn-12Mie.tdb:BCT_A5, tdb:MgSn-21Zha.tdb:BCT_A5, tdb:MgSn-99Mor.tdb:BCT_A5  


### TDB models of BCT_A5 (5): PHASE and CONSTITUENT statements as written

[MgSn-04Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-04Fri.tdb): BCT_A5, type code %, sha256 `932f4c7c0ab6221d…`

~~~~text
55: PHASE BCT_A5 % 1 1 !
56: CONST BCT_A5 : SN : !
~~~~

[MgSn-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-10Men.tdb): BCT_A5, type code %, sha256 `05ff105fc20ac101…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : SN : !
~~~~

[MgSn-12Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-12Mie.tdb): BCT_A5, type code %, sha256 `c5854f47494b5707…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : SN : !
~~~~

[MgSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-21Zha.tdb): BCT_A5, type code %, sha256 `d87760e638a43659…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : SN : !
~~~~

[MgSn-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-99Mor.tdb): BCT_A5, type code %, sha256 `b130ac8424b73691…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : SN : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2010.08.124](https://doi.org/10.1016/j.jallcom.2010.08.124) F.G. Meng, J. Wang, L.B. Liu, Z.P. Jin, Thermodynamic modeling of the Mg–Sn–Zn ternary system, Journal of Alloys and Compounds 508, 570-581 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_
- [doi:10.2298/JMMB110731008M](https://doi.org/10.2298/JMMB110731008M) J. Miettinen, G. Vassilev, J. Min. Metall. B, 48, 53-62(2012).  
_assessment that models this phase_
- [doi:10.1002/zaac.19050460112](https://doi.org/10.1002/zaac.19050460112) N. S. Kurnakow, N. J. Stepanow, Über die Legierungen des Magnesiums mit Zinn und Blei, Z. Anorg. Chem. 46, 177-192 (1905).  
_cited as the source of values for this phase_
- [doi:10.1051/jcp/1993900181](https://doi.org/10.1051/jcp/1993900181) SG Fries, HL Lukas, Optimisation of the Mg-Sn System, J. Chim. Phys. 90, 181-187 (1993).  
_cited as the source of values for this phase_

## BCC_A2 (Mg–Sn)

- Id: `phase:mg-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sn:bcc-a2)

Names (6): _corpus: _corpus:phase:mg-sn:bcc-a2  
_tdb: _tdb:MgSn-04Fri.tdb:BCC_A2, tdb:MgSn-10Men.tdb:BCC_A2, tdb:MgSn-12Mie.tdb:BCC_A2, tdb:MgSn-21Zha.tdb:BCC_A2, tdb:MgSn-99Mor.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[MgSn-04Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-04Fri.tdb): BCC_A2, type code %B, sha256 `932f4c7c0ab6221d…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : MG SN : VA : !
~~~~

[MgSn-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-10Men.tdb): BCC_A2, type code %B, sha256 `05ff105fc20ac101…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MG SN : VA : !
~~~~

[MgSn-12Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-12Mie.tdb): BCC_A2, type code %B, sha256 `c5854f47494b5707…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MG SN : VA : !
~~~~

[MgSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-21Zha.tdb): BCC_A2, type code %B, sha256 `d87760e638a43659…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MG SN : VA : !
~~~~

[MgSn-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-99Mor.tdb): BCC_A2, type code %B, sha256 `b130ac8424b73691…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MG SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.08.124](https://doi.org/10.1016/j.jallcom.2010.08.124) F.G. Meng, J. Wang, L.B. Liu, Z.P. Jin, Thermodynamic modeling of the Mg–Sn–Zn ternary system, Journal of Alloys and Compounds 508, 570-581 (2010).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_
- [doi:10.2298/JMMB110731008M](https://doi.org/10.2298/JMMB110731008M) J. Miettinen, G. Vassilev, J. Min. Metall. B, 48, 53-62(2012).  
_assessment that models this phase_

## FCC_A1 (Mg–Sn)

- Id: `phase:mg-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sn:fcc-a1)

Names (6): _corpus: _corpus:phase:mg-sn:fcc-a1  
_tdb: _tdb:MgSn-04Fri.tdb:FCC_A1, tdb:MgSn-10Men.tdb:FCC_A1, tdb:MgSn-12Mie.tdb:FCC_A1, tdb:MgSn-21Zha.tdb:FCC_A1, tdb:MgSn-99Mor.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[MgSn-04Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-04Fri.tdb): FCC_A1, type code %A, sha256 `932f4c7c0ab6221d…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : MG SN : VA : !
~~~~

[MgSn-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-10Men.tdb): FCC_A1, type code %A, sha256 `05ff105fc20ac101…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MG SN : VA : !
~~~~

[MgSn-12Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-12Mie.tdb): FCC_A1, type code %A, sha256 `c5854f47494b5707…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MG SN : VA : !
~~~~

[MgSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-21Zha.tdb): FCC_A1, type code %A, sha256 `d87760e638a43659…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MG SN : VA : !
~~~~

[MgSn-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-99Mor.tdb): FCC_A1, type code %A, sha256 `b130ac8424b73691…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MG SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.08.124](https://doi.org/10.1016/j.jallcom.2010.08.124) F.G. Meng, J. Wang, L.B. Liu, Z.P. Jin, Thermodynamic modeling of the Mg–Sn–Zn ternary system, Journal of Alloys and Compounds 508, 570-581 (2010).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_
- [doi:10.2298/JMMB110731008M](https://doi.org/10.2298/JMMB110731008M) J. Miettinen, G. Vassilev, J. Min. Metall. B, 48, 53-62(2012).  
_assessment that models this phase_

## HCP_A3 (Mg–Sn)

- Id: `phase:mg-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–935.87 K, x(Sn) 0–0.07118
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sn:hcp-a3)

Names (7): _corpus: _corpus:phase:mg-sn:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2010.08.124:hcp(Mg)  
_tdb: _tdb:MgSn-04Fri.tdb:HCP_A3, tdb:MgSn-10Men.tdb:HCP_A3, tdb:MgSn-12Mie.tdb:HCP_A3, tdb:MgSn-21Zha.tdb:HCP_A3, tdb:MgSn-99Mor.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[MgSn-04Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-04Fri.tdb): HCP_A3, type code %, sha256 `932f4c7c0ab6221d…`

~~~~text
45: PHASE HCP_A3 % 2 1 0.5 !
46: CONST HCP_A3 : MG% SN : VA : !
~~~~

[MgSn-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-10Men.tdb): HCP_A3, type code %, sha256 `05ff105fc20ac101…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : MG% SN : VA : !
~~~~

[MgSn-12Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-12Mie.tdb): HCP_A3, type code %, sha256 `c5854f47494b5707…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : MG% SN : VA : !
~~~~

[MgSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-21Zha.tdb): HCP_A3, type code %, sha256 `d87760e638a43659…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : MG% SN : VA : !
~~~~

[MgSn-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-99Mor.tdb): HCP_A3, type code %, sha256 `b130ac8424b73691…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : MG% SN : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2010.08.124](https://doi.org/10.1016/j.jallcom.2010.08.124) F.G. Meng, J. Wang, L.B. Liu, Z.P. Jin, Thermodynamic modeling of the Mg–Sn–Zn ternary system, Journal of Alloys and Compounds 508, 570-581 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_
- [doi:10.2298/JMMB110731008M](https://doi.org/10.2298/JMMB110731008M) J. Miettinen, G. Vassilev, J. Min. Metall. B, 48, 53-62(2012).  
_assessment that models this phase_
- [doi:10.1002/bbpc.19340400806](https://doi.org/10.1002/bbpc.19340400806) G. Grube, H. Vosskühler, Z. Electrochem. 40 (1934) 566–570.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19050460112](https://doi.org/10.1002/zaac.19050460112) N. S. Kurnakow, N. J. Stepanow, Über die Legierungen des Magnesiums mit Zinn und Blei, Z. Anorg. Chem. 46, 177-192 (1905).  
_cited as the source of values for this phase_
- [doi:10.1051/jcp/1993900181](https://doi.org/10.1051/jcp/1993900181) SG Fries, HL Lukas, Optimisation of the Mg-Sn System, J. Chim. Phys. 90, 181-187 (1993).  
_cited as the source of values for this phase_

## LIQUID (Mg–Sn)

- Id: `phase:mg-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 473.15–2500 K, x(Sn) 0–1
- Literature: 34 values (34 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sn:liquid)

Names (9): _corpus: _corpus:phase:mg-sn:liquid  
_paper: _paper:10.1016/j.intermet.2007.10.010:liquid, paper:10.1016/j.jallcom.2010.08.124:L, paper:10.1361/105497199770335785:Liquid  
_tdb: _tdb:MgSn-04Fri.tdb:LIQUID, tdb:MgSn-10Men.tdb:LIQUID, tdb:MgSn-12Mie.tdb:LIQUID, tdb:MgSn-21Zha.tdb:LIQUID, tdb:MgSn-99Mor.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[MgSn-04Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-04Fri.tdb): LIQUID, type code %, sha256 `932f4c7c0ab6221d…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : MG MG2SN SN : !
~~~~

[MgSn-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-10Men.tdb): LIQUID, type code %, sha256 `05ff105fc20ac101…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MG MG2SN SN : !
~~~~

[MgSn-12Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-12Mie.tdb): LIQUID, type code %, sha256 `c5854f47494b5707…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MG SN : !
~~~~

[MgSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-21Zha.tdb): LIQUID, type code %, sha256 `d87760e638a43659…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MG MG2SN SN : !
~~~~

[MgSn-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-99Mor.tdb): LIQUID, type code %, sha256 `b130ac8424b73691…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MG SN : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jallcom.2010.08.124](https://doi.org/10.1016/j.jallcom.2010.08.124) F.G. Meng, J. Wang, L.B. Liu, Z.P. Jin, Thermodynamic modeling of the Mg–Sn–Zn ternary system, Journal of Alloys and Compounds 508, 570-581 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.2298/JMMB110731008M](https://doi.org/10.2298/JMMB110731008M) J. Miettinen, G. Vassilev, J. Min. Metall. B, 48, 53-62(2012).  
_assessment that models this phase_
- [doi:10.1002/zaac.19050460112](https://doi.org/10.1002/zaac.19050460112) N. S. Kurnakow, N. J. Stepanow, Über die Legierungen des Magnesiums mit Zinn und Blei, Z. Anorg. Chem. 46, 177-192 (1905).  
_cited as the source of values for this phase_
- [doi:10.1051/jcp/1993900181](https://doi.org/10.1051/jcp/1993900181) SG Fries, HL Lukas, Optimisation of the Mg-Sn System, J. Chim. Phys. 90, 181-187 (1993).  
_cited as the source of values for this phase_
- [doi:10.1002/bbpc.19340400806](https://doi.org/10.1002/bbpc.19340400806) G. Grube, H. Vosskühler, Z. Electrochem. 40 (1934) 566–570.  
_cited as the source of values for this phase_
- [doi:10.1007/bf02654364](https://doi.org/10.1007/bf02654364) Charles A. Eckert, Robert B. Irwin, Jeffery S. Smith, Thermodynamic activity of magnesium in several highly-solvating liquid alloys, Metall Trans B 14, 451-458 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(74)90111-1](https://doi.org/10.1016/0022-3115%2874%2990111-1) J.J. Egan, Thermodynamics of liquid magnesium alloys using CaF2 solid electrolytes, Journal of Nuclear Materials 51, 30-35 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2007.10.010](https://doi.org/10.1016/j.intermet.2007.10.010) A. Kozlov, M. Ohno, R. Arroyave, Z.K. Liu, R. Schmid-Fetzer, Phase equilibria, thermodynamics and solidification microstructures of Mg–Sn–Ca alloys, Part 1: Experimental investigation and thermodynamic modeling of the ternary Mg–Sn–Ca system, Intermetallics 16, 299-315 (2008).  
_reports values for this phase_

## MG2SN_C1 (Mg–Sn)

- Id: `phase:mg-sn:mg2sn-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1048.62 K, x(Sn) 0.33333–0.34338
- Literature: 29 values (29 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sn:mg2sn-c1)

Names (7): _corpus: _corpus:phase:mg-sn:mg2sn-c1  
_paper: _paper:10.1016/j.jallcom.2010.08.124:Mg2Sn  
_tdb: _tdb:MgSn-04Fri.tdb:MG2SN_C1, tdb:MgSn-10Men.tdb:MG2SN_C1, tdb:MgSn-12Mie.tdb:MG2SN_C1, tdb:MgSn-21Zha.tdb:MG2SN_C1, tdb:MgSn-99Mor.tdb:MG2SN_C1  


### TDB models of MG2SN_C1 (5): PHASE and CONSTITUENT statements as written

[MgSn-04Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-04Fri.tdb): MG2SN_C1, type code %, sha256 `932f4c7c0ab6221d…`

~~~~text
60: PHASE MG2SN_C1 % 2 2 1 !
61: CONST MG2SN_C1 : MG : SN : !
~~~~

[MgSn-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-10Men.tdb): MG2SN_C1, type code %, sha256 `05ff105fc20ac101…`

~~~~text
56: PHASE MG2SN_C1 % 2 2 1 !
57: CONST MG2SN_C1 : MG : SN : !
~~~~

[MgSn-12Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-12Mie.tdb): MG2SN_C1, type code %, sha256 `c5854f47494b5707…`

~~~~text
53: PHASE MG2SN_C1 % 2 2 1 !
54: CONST MG2SN_C1 : MG : SN : !
~~~~

[MgSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-21Zha.tdb): MG2SN_C1, type code %, sha256 `d87760e638a43659…`

~~~~text
55: PHASE MG2SN_C1 % 2 2 1 !
56: CONST MG2SN_C1 : MG VA : SN : !
~~~~

[MgSn-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSn-99Mor.tdb): MG2SN_C1, type code %, sha256 `b130ac8424b73691…`

~~~~text
51: PHASE MG2SN_C1 % 2 2 1 !
52: CONST MG2SN_C1 : MG : SN : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jallcom.2010.08.124](https://doi.org/10.1016/j.jallcom.2010.08.124) F.G. Meng, J. Wang, L.B. Liu, Z.P. Jin, Thermodynamic modeling of the Mg–Sn–Zn ternary system, Journal of Alloys and Compounds 508, 570-581 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_
- [doi:10.2298/JMMB110731008M](https://doi.org/10.2298/JMMB110731008M) J. Miettinen, G. Vassilev, J. Min. Metall. B, 48, 53-62(2012).  
_assessment that models this phase_
- [doi:10.1002/zaac.19050460112](https://doi.org/10.1002/zaac.19050460112) N. S. Kurnakow, N. J. Stepanow, Über die Legierungen des Magnesiums mit Zinn und Blei, Z. Anorg. Chem. 46, 177-192 (1905).  
_cited as the source of values for this phase_
- [doi:10.1051/jcp/1993900181](https://doi.org/10.1051/jcp/1993900181) SG Fries, HL Lukas, Optimisation of the Mg-Sn System, J. Chim. Phys. 90, 181-187 (1993).  
_cited as the source of values for this phase_
- [doi:10.1002/bbpc.19340400806](https://doi.org/10.1002/bbpc.19340400806) G. Grube, H. Vosskühler, Z. Electrochem. 40 (1934) 566–570.  
_cited as the source of values for this phase_
- [doi:10.1007/bf02654364](https://doi.org/10.1007/bf02654364) Charles A. Eckert, Robert B. Irwin, Jeffery S. Smith, Thermodynamic activity of magnesium in several highly-solvating liquid alloys, Metall Trans B 14, 451-458 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(74)90111-1](https://doi.org/10.1016/0022-3115%2874%2990111-1) J.J. Egan, Thermodynamics of liquid magnesium alloys using CaF2 solid electrolytes, Journal of Nuclear Materials 51, 30-35 (1974).  
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
