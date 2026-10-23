# Au–Bi phases

> Au–Bi system: 6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-BI.html · Markdown: https://data.orchid-project.org/phases/pages/AU-BI.md

6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-BI) · [full JSON](https://data.orchid-project.org/phases/systems/AU-BI.json) · [Au–Bi system page](https://data.orchid-project.org/systems/AU-BI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-BI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Bi system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-au-bi-a7-rhombohedral); _phase:au-bi:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Bi) 0.99641–1 | 25 | 3 |
| [AU2BI_C15](#phase-au-bi-au2bi-c15); _phase:au-bi:au2bi-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 349.81–651.15 K, x(Bi) 0.33333–0.33333 | 39 | 3 |
| [BCC_A2](#phase-au-bi-bcc-a2); _phase:au-bi:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-au-bi-fcc-a1); _phase:au-bi:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1372.33 K, x(Bi) 0–0.00068 | 24 | 3 |
| [HCP_A3](#phase-au-bi-hcp-a3); _phase:au-bi:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-au-bi-liquid); _phase:au-bi:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 512.86–2500 K, x(Bi) 0–1 | 33 | 3 |

## RHOMBOHEDRAL_A7 (Au–Bi)

- Id: `phase:au-bi:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Bi) 0.99641–1
- Literature: 25 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-bi:a7-rhombohedral)

Names (8): _corpus: _corpus:phase:au-bi:a7-rhombohedral, corpus:phase:au-bi:rhombohedral-a7  
_paper: _paper:10.1016/0040-6031(88)87046-1:Bi(liq), paper:10.1016/0040-6031(88)87046-1:Bi(rho), paper:10.1016/j.calphad.2006.07.002:(Bi)  
_tdb: _tdb:AuBi-06Ser.tdb:RHOMBOHEDRAL_A7, tdb:AuBi-07Wan.tdb:RHOMBOHEDRAL_A7, tdb:AuBi-88Che-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[AuBi-06Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-06Ser.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `211df8efcc0e7604…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[AuBi-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-07Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `2708fcbef3e06ed3…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : AU BI% : !
~~~~

[AuBi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-88Che-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `7247b351d3e4203e…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0040-6031(88)87046-1](https://doi.org/10.1016/0040-6031%2888%2987046-1) P.-Y. Chevalier, Thermodynamic evaluation of the Au-Bi system, Thermochimica Acta 130, 15-24 (1988).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2006.07.002](https://doi.org/10.1016/j.calphad.2006.07.002) C. Servant, E. Zoro, B. Legendre, Thermodynamic reassessment of the Au–Bi system, Calphad 30, 443-448 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0090-z](https://doi.org/10.1007/s11664-007-0090-z) J. Wang, F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic Modeling of the Au-Bi-Sb Ternary System, Journal of Elec Materi 36, 568-577 (2007).  
_assessment that models this phase_
- [doi:10.1007/bf02868093](https://doi.org/10.1007/bf02868093) H. Okamoto and T.B. Massalski, Bull. Alloy Phase Diagrams 4, 401 (1983).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19060500116](https://doi.org/10.1002/zaac.19060500116) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIII. Über die Legierungen des Goldes mit Wismut und Antimon, Z. Anorg. Chem. 50, 145-157 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_

## AU2BI_C15 (Au–Bi)

- Id: `phase:au-bi:au2bi-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgljl and oqmd-646874, space group 227
- Stoichiometry: Au 0.6667, Bi 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 349.81–651.15 K, x(Bi) 0.33333–0.33333
- Literature: 39 values (39 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-bi:au2bi-c15)

Names (8): _corpus: _corpus:phase:au-bi:au2bi-c15  
_mp: _mp:mp-aaabgljl  
_oqmd: _oqmd:oqmd-646874  
_paper: _paper:10.1016/0040-6031(88)87046-1:Au2Bi, paper:10.1016/j.calphad.2006.07.002:Au2Bi  
_tdb: _tdb:AuBi-06Ser.tdb:AU2BI_C15, tdb:AuBi-07Wan.tdb:AU2BI_C15, tdb:AuBi-88Che-LB.tdb:AU2BI_C15  


### TDB models of AU2BI_C15 (3): PHASE and CONSTITUENT statements as written

[AuBi-06Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-06Ser.tdb): AU2BI_C15, type code %, sha256 `211df8efcc0e7604…`

~~~~text
48: PHASE AU2BI_C15 % 2 2 1 !
49: CONST AU2BI_C15 : AU : BI : !
~~~~

[AuBi-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-07Wan.tdb): AU2BI_C15, type code %, sha256 `2708fcbef3e06ed3…`

~~~~text
46: PHASE AU2BI_C15 % 2 2 1 !
47: CONST AU2BI_C15 : AU : BI : !
~~~~

[AuBi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-88Che-LB.tdb): AU2BI_C15, type code %, sha256 `7247b351d3e4203e…`

~~~~text
51: PHASE AU2BI_C15 % 2 2 1 !
52: CONST AU2BI_C15 : AU : BI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2006.07.002](https://doi.org/10.1016/j.calphad.2006.07.002) C. Servant, E. Zoro, B. Legendre, Thermodynamic reassessment of the Au–Bi system, Calphad 30, 443-448 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(88)87046-1](https://doi.org/10.1016/0040-6031%2888%2987046-1) P.-Y. Chevalier, Thermodynamic evaluation of the Au-Bi system, Thermochimica Acta 130, 15-24 (1988).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0090-z](https://doi.org/10.1007/s11664-007-0090-z) J. Wang, F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic Modeling of the Au-Bi-Sb Ternary System, Journal of Elec Materi 36, 568-577 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060500116](https://doi.org/10.1002/zaac.19060500116) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIII. Über die Legierungen des Goldes mit Wismut und Antimon, Z. Anorg. Chem. 50, 145-157 (1906).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868093](https://doi.org/10.1007/bf02868093) H. Okamoto and T.B. Massalski, Bull. Alloy Phase Diagrams 4, 401 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Bi)

- Id: `phase:au-bi:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-bi:bcc-a2)

Names (4): _corpus: _corpus:phase:au-bi:bcc-a2  
_tdb: _tdb:AuBi-06Ser.tdb:BCC_A2, tdb:AuBi-07Wan.tdb:BCC_A2, tdb:AuBi-88Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AuBi-06Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-06Ser.tdb): BCC_A2, type code %B, sha256 `211df8efcc0e7604…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AU BI : VA : !
~~~~

[AuBi-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-07Wan.tdb): BCC_A2, type code %B, sha256 `2708fcbef3e06ed3…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AU BI : VA : !
~~~~

[AuBi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-88Che-LB.tdb): BCC_A2, type code %B, sha256 `7247b351d3e4203e…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AU BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-007-0090-z](https://doi.org/10.1007/s11664-007-0090-z) J. Wang, F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic Modeling of the Au-Bi-Sb Ternary System, Journal of Elec Materi 36, 568-577 (2007).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(88)87046-1](https://doi.org/10.1016/0040-6031%2888%2987046-1) P.-Y. Chevalier, Thermodynamic evaluation of the Au-Bi system, Thermochimica Acta 130, 15-24 (1988).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.07.002](https://doi.org/10.1016/j.calphad.2006.07.002) C. Servant, E. Zoro, B. Legendre, Thermodynamic reassessment of the Au–Bi system, Calphad 30, 443-448 (2006).  
_assessment that models this phase_

## FCC_A1 (Au–Bi)

- Id: `phase:au-bi:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1372.33 K, x(Bi) 0–0.00068
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-bi:fcc-a1)

Names (7): _corpus: _corpus:phase:au-bi:fcc-a1  
_paper: _paper:10.1016/0040-6031(88)87046-1:fcc, paper:10.1016/j.calphad.2006.07.002:Fcc, paper:10.1016/j.calphad.2006.07.002:fcc  
_tdb: _tdb:AuBi-06Ser.tdb:FCC_A1, tdb:AuBi-07Wan.tdb:FCC_A1, tdb:AuBi-88Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AuBi-06Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-06Ser.tdb): FCC_A1, type code %A, sha256 `211df8efcc0e7604…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AU% BI : VA : !
~~~~

[AuBi-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-07Wan.tdb): FCC_A1, type code %A, sha256 `2708fcbef3e06ed3…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AU% BI : VA : !
~~~~

[AuBi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-88Che-LB.tdb): FCC_A1, type code %A, sha256 `7247b351d3e4203e…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AU% BI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.07.002](https://doi.org/10.1016/j.calphad.2006.07.002) C. Servant, E. Zoro, B. Legendre, Thermodynamic reassessment of the Au–Bi system, Calphad 30, 443-448 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(88)87046-1](https://doi.org/10.1016/0040-6031%2888%2987046-1) P.-Y. Chevalier, Thermodynamic evaluation of the Au-Bi system, Thermochimica Acta 130, 15-24 (1988).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0090-z](https://doi.org/10.1007/s11664-007-0090-z) J. Wang, F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic Modeling of the Au-Bi-Sb Ternary System, Journal of Elec Materi 36, 568-577 (2007).  
_assessment that models this phase_
- [doi:10.1007/bf02868093](https://doi.org/10.1007/bf02868093) H. Okamoto and T.B. Massalski, Bull. Alloy Phase Diagrams 4, 401 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Bi)

- Id: `phase:au-bi:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-bi:hcp-a3)

Names (4): _corpus: _corpus:phase:au-bi:hcp-a3  
_tdb: _tdb:AuBi-06Ser.tdb:HCP_A3, tdb:AuBi-07Wan.tdb:HCP_A3, tdb:AuBi-88Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AuBi-06Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-06Ser.tdb): HCP_A3, type code %A, sha256 `211df8efcc0e7604…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AU BI : VA : !
~~~~

[AuBi-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-07Wan.tdb): HCP_A3, type code %A, sha256 `2708fcbef3e06ed3…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AU BI : VA : !
~~~~

[AuBi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-88Che-LB.tdb): HCP_A3, type code %A, sha256 `7247b351d3e4203e…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AU BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-007-0090-z](https://doi.org/10.1007/s11664-007-0090-z) J. Wang, F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic Modeling of the Au-Bi-Sb Ternary System, Journal of Elec Materi 36, 568-577 (2007).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(88)87046-1](https://doi.org/10.1016/0040-6031%2888%2987046-1) P.-Y. Chevalier, Thermodynamic evaluation of the Au-Bi system, Thermochimica Acta 130, 15-24 (1988).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.07.002](https://doi.org/10.1016/j.calphad.2006.07.002) C. Servant, E. Zoro, B. Legendre, Thermodynamic reassessment of the Au–Bi system, Calphad 30, 443-448 (2006).  
_assessment that models this phase_

## LIQUID (Au–Bi)

- Id: `phase:au-bi:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 512.86–2500 K, x(Bi) 0–1
- Literature: 33 values (33 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-bi:liquid)

Names (7): _corpus: _corpus:phase:au-bi:liquid  
_paper: _paper:10.1016/0040-6031(88)87046-1:Au(liq), paper:10.1016/0040-6031(88)87046-1:L, paper:10.1016/j.calphad.2006.07.002:L  
_tdb: _tdb:AuBi-06Ser.tdb:LIQUID, tdb:AuBi-07Wan.tdb:LIQUID, tdb:AuBi-88Che-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AuBi-06Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-06Ser.tdb): LIQUID, type code %, sha256 `211df8efcc0e7604…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AU BI : !
~~~~

[AuBi-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-07Wan.tdb): LIQUID, type code %, sha256 `2708fcbef3e06ed3…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AU BI : !
~~~~

[AuBi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuBi-88Che-LB.tdb): LIQUID, type code %, sha256 `7247b351d3e4203e…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AU BI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2006.07.002](https://doi.org/10.1016/j.calphad.2006.07.002) C. Servant, E. Zoro, B. Legendre, Thermodynamic reassessment of the Au–Bi system, Calphad 30, 443-448 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(88)87046-1](https://doi.org/10.1016/0040-6031%2888%2987046-1) P.-Y. Chevalier, Thermodynamic evaluation of the Au-Bi system, Thermochimica Acta 130, 15-24 (1988).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0090-z](https://doi.org/10.1007/s11664-007-0090-z) J. Wang, F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic Modeling of the Au-Bi-Sb Ternary System, Journal of Elec Materi 36, 568-577 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060500116](https://doi.org/10.1002/zaac.19060500116) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIII. Über die Legierungen des Goldes mit Wismut und Antimon, Z. Anorg. Chem. 50, 145-157 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(81)80143-8](https://doi.org/10.1016/0040-6031%2881%2980143-8) Peter C. Wallbrecht, Roger Blachnik, Kennth C. Mills, The heat capacity and enthalpy of some Hume—Rothery phases formed by copper, silver and gold. Part I. Cu + Sb, Ag + Sb, Au + Sb, Au + Bi systems, Thermochimica Acta 45, 189-198 (1981).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868093](https://doi.org/10.1007/bf02868093) H. Okamoto and T.B. Massalski, Bull. Alloy Phase Diagrams 4, 401 (1983).  
_cited as the source of values for this phase_

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
