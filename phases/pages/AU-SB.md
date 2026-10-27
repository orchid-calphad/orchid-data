# Au–Sb phases

> Au–Sb system: 6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-SB.html · Markdown: https://data.orchid-project.org/phases/pages/AU-SB.md

6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-SB) · [full JSON](https://data.orchid-project.org/phases/systems/AU-SB.json) · [Au–Sb system page](https://data.orchid-project.org/systems/AU-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Sb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-au-sb-a7-rhombohedral); _phase:au-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 8 | 5 |
| [AUSB2_C2](#phase-au-sb-ausb2-c2); _phase:au-sb:ausb2-c2_ | beta-FeS2 · C2 · cP12 · Pa-3 (205) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–739.98 K, x(Sb) 0.66667–0.66667 | 32 | 5 |
| [BCC_A2](#phase-au-sb-bcc-a2); _phase:au-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-au-sb-fcc-a1); _phase:au-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1358.38 K, x(Sb) 0–0.01282 | 10 | 5 |
| [HCP_A3](#phase-au-sb-hcp-a3); _phase:au-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-au-sb-liquid); _phase:au-sb:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 626.23–2500 K, x(Sb) 0–1 | 19 | 5 |

## RHOMBOHEDRAL_A7 (Au–Sb)

- Id: `phase:au-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sb:a7-rhombohedral)

Names (8): _corpus: _corpus:phase:au-sb:a7-rhombohedral, corpus:phase:au-sb:rhombohedral-a7  
_paper: _paper:10.1007/s11664-002-0125-4:(Sb)  
_tdb: _tdb:AuSb-02Kim.tdb:RHOMBOHEDRAL_A7, tdb:AuSb-03Liu.tdb:RHOMBOHEDRAL_A7, tdb:AuSb-11Wan.tdb:RHOMBOHEDRAL_A7, tdb:AuSb-13Gie.tdb:RHOMBOHEDRAL_A7, tdb:AuSb-89Che-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (5): PHASE and CONSTITUENT statements as written

[AuSb-02Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-02Kim.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `db53175b1bacbeb5…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AuSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-03Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `c4f2198262a6e367…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `0354d7420fa903d8…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AuSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-13Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `420d77300456541e…`

~~~~text
39: PHASE RHOMBOHEDRAL_A7 % 1 1 !
40: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AuSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-89Che-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `080bb55f5b276348…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s11664-002-0125-4](https://doi.org/10.1007/s11664-002-0125-4) Jong Hoon Kim, Sang Won Jeong, Hyuck Mo Lee, A thermodynamic study of phase equilibria in the Au-Sb-Sn solder system, Journal of Elec Materi 31, 557-563 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3) Pierre-Yves Chevalier, A thermodynamic evaluation of the Au-Sb and Au-Tl systems, Thermochimica Acta 155, 211-225 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2013.04.186](https://doi.org/10.1016/j.jallcom.2013.04.186) Wojciech Gierlotka, Thermodynamic description of the binary Au–Sb and ternary Au–In–Sb systems, Journal of Alloys and Compounds 579, 533-539 (2013).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060500116](https://doi.org/10.1002/zaac.19060500116) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIII. Über die Legierungen des Goldes mit Wismut und Antimon, Z. Anorg. Chem. 50, 145-157 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19322090312](https://doi.org/10.1002/zaac.19322090312) A. T. Grigorjew, Über die Legierungen des Goldes mit Antimon, Z. Anorg. Allg. Chem. 209, 289-294 (1932).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868954](https://doi.org/10.1007/bf02868954) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diagrams 5 (1984) 166.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_

## AUSB2_C2 (Au–Sb)

- Id: `phase:au-sb:ausb2-c2`; status `assigned`
- Structure: beta-FeS2 · C2 · cP12 · Pa-3 (205); type `st:c2-beta-fes2-cp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabck and oqmd-7245, space group 205
- Stoichiometry: Au 0.3333, Sb 0.6667
- Stability: stable in 5 of 5 calculated diagram(s): 300–739.98 K, x(Sb) 0.66667–0.66667
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sb:ausb2-c2)

Names (10): _corpus: _corpus:phase:au-sb:ausb2-c2  
_mp: _mp:mp-aaaaabck  
_oqmd: _oqmd:oqmd-7245  
_paper: _paper:10.1007/s11664-002-0125-4:AuSb2, paper:10.1016/j.jallcom.2013.04.186:AuSb2  
_tdb: _tdb:AuSb-02Kim.tdb:AUSB2_C2, tdb:AuSb-03Liu.tdb:AUSB2_C2, tdb:AuSb-11Wan.tdb:AUSB2_C2, tdb:AuSb-13Gie.tdb:AUSB2_C2, tdb:AuSb-89Che-LB.tdb:AUSB2_C2  


### TDB models of AUSB2_C2 (5): PHASE and CONSTITUENT statements as written

[AuSb-02Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-02Kim.tdb): AUSB2_C2, type code %, sha256 `db53175b1bacbeb5…`

~~~~text
46: PHASE AUSB2_C2 % 2 1 2 !
47: CONST AUSB2_C2 : AU : SB : !
~~~~

[AuSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-03Liu.tdb): AUSB2_C2, type code %, sha256 `c4f2198262a6e367…`

~~~~text
45: PHASE AUSB2_C2 % 2 1 2 !
46: CONST AUSB2_C2 : AU : SB : !
~~~~

[AuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-11Wan.tdb): AUSB2_C2, type code %, sha256 `0354d7420fa903d8…`

~~~~text
45: PHASE AUSB2_C2 % 2 1 2 !
46: CONST AUSB2_C2 : AU : SB : !
~~~~

[AuSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-13Gie.tdb): AUSB2_C2, type code %, sha256 `420d77300456541e…`

~~~~text
44: PHASE AUSB2_C2 % 2 1 2 !
45: CONST AUSB2_C2 : AU : SB : !
~~~~

[AuSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-89Che-LB.tdb): AUSB2_C2, type code %, sha256 `080bb55f5b276348…`

~~~~text
47: PHASE AUSB2_C2 % 2 1 2 !
48: CONST AUSB2_C2 : AU : SB : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s11664-002-0125-4](https://doi.org/10.1007/s11664-002-0125-4) Jong Hoon Kim, Sang Won Jeong, Hyuck Mo Lee, A thermodynamic study of phase equilibria in the Au-Sb-Sn solder system, Journal of Elec Materi 31, 557-563 (2002).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.04.186](https://doi.org/10.1016/j.jallcom.2013.04.186) Wojciech Gierlotka, Thermodynamic description of the binary Au–Sb and ternary Au–In–Sb systems, Journal of Alloys and Compounds 579, 533-539 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3) Pierre-Yves Chevalier, A thermodynamic evaluation of the Au-Sb and Au-Tl systems, Thermochimica Acta 155, 211-225 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060500116](https://doi.org/10.1002/zaac.19060500116) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIII. Über die Legierungen des Goldes mit Wismut und Antimon, Z. Anorg. Chem. 50, 145-157 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19322090312](https://doi.org/10.1002/zaac.19322090312) A. T. Grigorjew, Über die Legierungen des Goldes mit Antimon, Z. Anorg. Allg. Chem. 209, 289-294 (1932).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868954](https://doi.org/10.1007/bf02868954) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diagrams 5 (1984) 166.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_
- [doi:10.1021/j150541a006](https://doi.org/10.1021/j150541a006) O. J. Kleppa, Heat of Formation of Some Solid and Liquid Binary Alloys of Gold with Cadmium, Indium, Tin and Antimony, J. Phys. Chem. 60, 858-863 (1956).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Sb)

- Id: `phase:au-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sb:bcc-a2)

Names (6): _corpus: _corpus:phase:au-sb:bcc-a2  
_tdb: _tdb:AuSb-02Kim.tdb:BCC_A2, tdb:AuSb-03Liu.tdb:BCC_A2, tdb:AuSb-11Wan.tdb:BCC_A2, tdb:AuSb-13Gie.tdb:BCC_A2, tdb:AuSb-89Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[AuSb-02Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-02Kim.tdb): BCC_A2, type code %B, sha256 `db53175b1bacbeb5…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AU SB : VA : !
~~~~

[AuSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-03Liu.tdb): BCC_A2, type code %B, sha256 `c4f2198262a6e367…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU SB : VA : !
~~~~

[AuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-11Wan.tdb): BCC_A2, type code %B, sha256 `0354d7420fa903d8…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU SB : VA : !
~~~~

[AuSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-13Gie.tdb): BCC_A2, type code %B, sha256 `420d77300456541e…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : AU SB : VA : !
~~~~

[AuSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-89Che-LB.tdb): BCC_A2, type code %B, sha256 `080bb55f5b276348…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AU SB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11664-002-0125-4](https://doi.org/10.1007/s11664-002-0125-4) Jong Hoon Kim, Sang Won Jeong, Hyuck Mo Lee, A thermodynamic study of phase equilibria in the Au-Sb-Sn solder system, Journal of Elec Materi 31, 557-563 (2002).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3) Pierre-Yves Chevalier, A thermodynamic evaluation of the Au-Sb and Au-Tl systems, Thermochimica Acta 155, 211-225 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2013.04.186](https://doi.org/10.1016/j.jallcom.2013.04.186) Wojciech Gierlotka, Thermodynamic description of the binary Au–Sb and ternary Au–In–Sb systems, Journal of Alloys and Compounds 579, 533-539 (2013).  
_assessment that models this phase_

## FCC_A1 (Au–Sb)

- Id: `phase:au-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1358.38 K, x(Sb) 0–0.01282
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sb:fcc-a1)

Names (7): _corpus: _corpus:phase:au-sb:fcc-a1  
_paper: _paper:10.1007/s11664-002-0125-4:(Au)  
_tdb: _tdb:AuSb-02Kim.tdb:FCC_A1, tdb:AuSb-03Liu.tdb:FCC_A1, tdb:AuSb-11Wan.tdb:FCC_A1, tdb:AuSb-13Gie.tdb:FCC_A1, tdb:AuSb-89Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[AuSb-02Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-02Kim.tdb): FCC_A1, type code %A, sha256 `db53175b1bacbeb5…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AU% SB : VA : !
~~~~

[AuSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-03Liu.tdb): FCC_A1, type code %A, sha256 `c4f2198262a6e367…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% SB : VA : !
~~~~

[AuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-11Wan.tdb): FCC_A1, type code %A, sha256 `0354d7420fa903d8…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% SB : VA : !
~~~~

[AuSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-13Gie.tdb): FCC_A1, type code %A, sha256 `420d77300456541e…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : AU% SB : VA : !
~~~~

[AuSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-89Che-LB.tdb): FCC_A1, type code %A, sha256 `080bb55f5b276348…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AU% SB : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/s11664-002-0125-4](https://doi.org/10.1007/s11664-002-0125-4) Jong Hoon Kim, Sang Won Jeong, Hyuck Mo Lee, A thermodynamic study of phase equilibria in the Au-Sb-Sn solder system, Journal of Elec Materi 31, 557-563 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3) Pierre-Yves Chevalier, A thermodynamic evaluation of the Au-Sb and Au-Tl systems, Thermochimica Acta 155, 211-225 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2013.04.186](https://doi.org/10.1016/j.jallcom.2013.04.186) Wojciech Gierlotka, Thermodynamic description of the binary Au–Sb and ternary Au–In–Sb systems, Journal of Alloys and Compounds 579, 533-539 (2013).  
_assessment that models this phase_
- [doi:10.1002/pssa.2210240241](https://doi.org/10.1002/pssa.2210240241) B. Pardo, Et C. Pariset, M. Gasgnier, Étude des “taches interdites” apparaissant par diffraction électronique dans le cas de couches minces or-antimoine, Phys. Stat. Sol. (a) 24, K91-K93 (1974).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19060500116](https://doi.org/10.1002/zaac.19060500116) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIII. Über die Legierungen des Goldes mit Wismut und Antimon, Z. Anorg. Chem. 50, 145-157 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19322090312](https://doi.org/10.1002/zaac.19322090312) A. T. Grigorjew, Über die Legierungen des Goldes mit Antimon, Z. Anorg. Allg. Chem. 209, 289-294 (1932).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868954](https://doi.org/10.1007/bf02868954) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diagrams 5 (1984) 166.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Sb)

- Id: `phase:au-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sb:hcp-a3)

Names (6): _corpus: _corpus:phase:au-sb:hcp-a3  
_tdb: _tdb:AuSb-02Kim.tdb:HCP_A3, tdb:AuSb-03Liu.tdb:HCP_A3, tdb:AuSb-11Wan.tdb:HCP_A3, tdb:AuSb-13Gie.tdb:HCP_A3, tdb:AuSb-89Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[AuSb-02Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-02Kim.tdb): HCP_A3, type code %A, sha256 `db53175b1bacbeb5…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AU SB : VA : !
~~~~

[AuSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-03Liu.tdb): HCP_A3, type code %A, sha256 `c4f2198262a6e367…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU SB : VA : !
~~~~

[AuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-11Wan.tdb): HCP_A3, type code %A, sha256 `0354d7420fa903d8…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU SB : VA : !
~~~~

[AuSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-13Gie.tdb): HCP_A3, type code %A, sha256 `420d77300456541e…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : AU SB : VA : !
~~~~

[AuSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-89Che-LB.tdb): HCP_A3, type code %A, sha256 `080bb55f5b276348…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AU SB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11664-002-0125-4](https://doi.org/10.1007/s11664-002-0125-4) Jong Hoon Kim, Sang Won Jeong, Hyuck Mo Lee, A thermodynamic study of phase equilibria in the Au-Sb-Sn solder system, Journal of Elec Materi 31, 557-563 (2002).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3) Pierre-Yves Chevalier, A thermodynamic evaluation of the Au-Sb and Au-Tl systems, Thermochimica Acta 155, 211-225 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2013.04.186](https://doi.org/10.1016/j.jallcom.2013.04.186) Wojciech Gierlotka, Thermodynamic description of the binary Au–Sb and ternary Au–In–Sb systems, Journal of Alloys and Compounds 579, 533-539 (2013).  
_assessment that models this phase_

## LIQUID (Au–Sb)

- Id: `phase:au-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 626.23–2500 K, x(Sb) 0–1
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sb:liquid)

Names (8): _corpus: _corpus:phase:au-sb:liquid  
_paper: _paper:10.1007/s11664-002-0125-4:L, paper:10.1016/j.jallcom.2013.04.186:liquid  
_tdb: _tdb:AuSb-02Kim.tdb:LIQUID, tdb:AuSb-03Liu.tdb:LIQUID, tdb:AuSb-11Wan.tdb:LIQUID, tdb:AuSb-13Gie.tdb:LIQUID, tdb:AuSb-89Che-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[AuSb-02Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-02Kim.tdb): LIQUID, type code %, sha256 `db53175b1bacbeb5…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AU SB : !
~~~~

[AuSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-03Liu.tdb): LIQUID, type code %, sha256 `c4f2198262a6e367…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU SB : !
~~~~

[AuSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-11Wan.tdb): LIQUID, type code %, sha256 `0354d7420fa903d8…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU SB : !
~~~~

[AuSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-13Gie.tdb): LIQUID, type code %, sha256 `420d77300456541e…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : AU SB : !
~~~~

[AuSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSb-89Che-LB.tdb): LIQUID, type code %, sha256 `080bb55f5b276348…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AU SB : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/s11664-002-0125-4](https://doi.org/10.1007/s11664-002-0125-4) Jong Hoon Kim, Sang Won Jeong, Hyuck Mo Lee, A thermodynamic study of phase equilibria in the Au-Sb-Sn solder system, Journal of Elec Materi 31, 557-563 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3) Pierre-Yves Chevalier, A thermodynamic evaluation of the Au-Sb and Au-Tl systems, Thermochimica Acta 155, 211-225 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.186](https://doi.org/10.1016/j.jallcom.2013.04.186) Wojciech Gierlotka, Thermodynamic description of the binary Au–Sb and ternary Au–In–Sb systems, Journal of Alloys and Compounds 579, 533-539 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060500116](https://doi.org/10.1002/zaac.19060500116) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIII. Über die Legierungen des Goldes mit Wismut und Antimon, Z. Anorg. Chem. 50, 145-157 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19322090312](https://doi.org/10.1002/zaac.19322090312) A. T. Grigorjew, Über die Legierungen des Goldes mit Antimon, Z. Anorg. Allg. Chem. 209, 289-294 (1932).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868954](https://doi.org/10.1007/bf02868954) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diagrams 5 (1984) 166.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_
- [doi:10.1002/pssa.2210240241](https://doi.org/10.1002/pssa.2210240241) B. Pardo, Et C. Pariset, M. Gasgnier, Étude des “taches interdites” apparaissant par diffraction électronique dans le cas de couches minces or-antimoine, Phys. Stat. Sol. (a) 24, K91-K93 (1974).  
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
