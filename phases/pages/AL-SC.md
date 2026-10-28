# Al–Sc phases

> Al–Sc system: 8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-SC.html · Markdown: https://data.orchid-project.org/phases/pages/AL-SC.md

8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-SC) · [full JSON](https://data.orchid-project.org/phases/systems/AL-SC.json) · [Al–Sc system page](https://data.orchid-project.org/systems/AL-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Sc system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2SC_C15](#phase-al-sc-al2sc-c15); _phase:al-sc:al2sc-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1694.37 K, x(Sc) 0.33333–0.33333 | 22 | 3 |
| [AL3SC_L12](#phase-al-sc-al3sc-l12); _phase:al-sc:al3sc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1603.68 K, x(Sc) 0.25–0.25 | 17 | 3 |
| [ALSC_B2](#phase-al-sc-alsc-b2); _phase:al-sc:alsc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1574.74 K, x(Sc) 0.5–0.5 | 25 | 3 |
| [ALSC2_B82](#phase-al-sc-alsc2-b82); _phase:al-sc:alsc2-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1570.95 K, x(Sc) 0.66667–0.66667 | 30 | 3 |
| [BCC_A2](#phase-al-sc-bcc-a2); _phase:al-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1242.39–2500 K, x(Sc) 0.29125–1 | 14 | 3 |
| [FCC_A1](#phase-al-sc-fcc-a1); _phase:al-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–933.47 K, x(Sc) 0–0.0024 | 10 | 3 |
| [HCP_A3](#phase-al-sc-hcp-a3); _phase:al-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1805.33 K, x(Sc) 0.89758–1 | 9 | 3 |
| [LIQUID](#phase-al-sc-liquid); _phase:al-sc:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 930.94–2500 K, x(Sc) 0–1 | 64 | 3 |

## AL2SC_C15 (Al–Sc)

- Id: `phase:al-sc:al2sc-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabfh and oqmd-10541, space group 227
- Stoichiometry: Al 0.6667, Sc 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1694.37 K, x(Sc) 0.33333–0.33333
- Literature: 22 values (22 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:al2sc-c15)

Names (9): _corpus: _corpus:phase:al-sc:al2sc-c15  
_mp: _mp:mp-aaaaabfh  
_oqmd: _oqmd:oqmd-10541  
_paper: _paper:10.1016/j.jallcom.2009.10.003:Al2Sc, paper:10.1016/s0966-9795(98)00022-3:ScAl2, paper:10.1361/105497198770342120:Al2Sc  
_tdb: _tdb:AlSc-10Bo.tdb:AL2SC_C15, tdb:AlSc-98Mur.tdb:AL2SC_C15, tdb:AlSc-99Cac-LB.tdb:AL2SC_C15  


### TDB models of AL2SC_C15 (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): AL2SC_C15, type code %, sha256 `45d2f4a9a159e401…`

~~~~text
45: PHASE AL2SC_C15 % 2 2 1 !
46: CONST AL2SC_C15 : AL : SC : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): AL2SC_C15, type code %, sha256 `c476dee15cbcc541…`

~~~~text
50: PHASE AL2SC_C15 % 2 2 1 !
51: CONST AL2SC_C15 : AL : SC : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): AL2SC_C15, type code %, sha256 `3bd2989713373b92…`

~~~~text
52: PHASE AL2SC_C15 % 2 2 1 !
53: CONST AL2SC_C15 : AL : SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
_cited as the source of values for this phase_

## AL3SC_L12 (Al–Sc)

- Id: `phase:al-sc:al3sc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaddp and oqmd-18716, space group 221
- Stoichiometry: Al 0.7500, Sc 0.2500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1603.68 K, x(Sc) 0.25–0.25
- Literature: 17 values (17 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:al3sc-l12)

Names (9): _corpus: _corpus:phase:al-sc:al3sc-l12  
_mp: _mp:mp-aaaaaddp  
_oqmd: _oqmd:oqmd-18716  
_paper: _paper:10.1016/j.jallcom.2009.10.003:Al3Sc, paper:10.1016/s0966-9795(98)00022-3:ScAl3, paper:10.1361/105497198770342120:Al3Sc  
_tdb: _tdb:AlSc-10Bo.tdb:AL3SC_L12, tdb:AlSc-98Mur.tdb:AL3SC_L12, tdb:AlSc-99Cac-LB.tdb:AL3SC_L12  


### TDB models of AL3SC_L12 (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): AL3SC_L12, type code %, sha256 `45d2f4a9a159e401…`

~~~~text
40: PHASE AL3SC_L12 % 2 3 1 !
41: CONST AL3SC_L12 : AL : SC : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): AL3SC_L12, type code %, sha256 `c476dee15cbcc541…`

~~~~text
45: PHASE AL3SC_L12 % 2 3 1 !
46: CONST AL3SC_L12 : AL : SC : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): AL3SC_L12, type code %, sha256 `3bd2989713373b92…`

~~~~text
47: PHASE AL3SC_L12 % 2 3 1 !
48: CONST AL3SC_L12 : AL : SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
_cited as the source of values for this phase_

## ALSC_B2 (Al–Sc)

- Id: `phase:al-sc:alsc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.5000, Sc 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1574.74 K, x(Sc) 0.5–0.5
- Literature: 25 values (25 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:alsc-b2)

Names (7): _corpus: _corpus:phase:al-sc:alsc-b2  
_paper: _paper:10.1016/j.jallcom.2009.10.003:AlSc, paper:10.1016/s0966-9795(98)00022-3:ScAl, paper:10.1361/105497198770342120:AlSc  
_tdb: _tdb:AlSc-10Bo.tdb:ALSC_B2, tdb:AlSc-98Mur.tdb:ALSC_B2, tdb:AlSc-99Cac-LB.tdb:ALSC_B2  


### TDB models of ALSC_B2 (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): ALSC_B2, type code %, sha256 `45d2f4a9a159e401…`

~~~~text
50: PHASE ALSC_B2 % 2 1 1 !
51: CONST ALSC_B2 : AL : SC : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): ALSC_B2, type code %, sha256 `c476dee15cbcc541…`

~~~~text
55: PHASE ALSC_B2 % 2 1 1 !
56: CONST ALSC_B2 : AL : SC : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): ALSC_B2, type code %, sha256 `3bd2989713373b92…`

~~~~text
57: PHASE ALSC_B2 % 2 1 1 !
58: CONST ALSC_B2 : AL : SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
_cited as the source of values for this phase_

## ALSC2_B82 (Al–Sc)

- Id: `phase:al-sc:alsc2-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqpo and oqmd-10540, space group 194
- Stoichiometry: Al 0.3333, Sc 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1570.95 K, x(Sc) 0.66667–0.66667
- Literature: 30 values (30 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:alsc2-b82)

Names (9): _corpus: _corpus:phase:al-sc:alsc2-b82  
_mp: _mp:mp-aaaaaqpo  
_oqmd: _oqmd:oqmd-10540  
_paper: _paper:10.1016/j.jallcom.2009.10.003:AlSc2, paper:10.1016/s0966-9795(98)00022-3:Sc2Al, paper:10.1361/105497198770342120:AlSc2  
_tdb: _tdb:AlSc-10Bo.tdb:ALSC2_B82, tdb:AlSc-98Mur.tdb:ALSC2_B82, tdb:AlSc-99Cac-LB.tdb:ALSC2_B82  


### TDB models of ALSC2_B82 (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): ALSC2_B82, type code %, sha256 `45d2f4a9a159e401…`

~~~~text
55: PHASE ALSC2_B82 % 2 1 2 !
56: CONST ALSC2_B82 : AL : SC : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): ALSC2_B82, type code %, sha256 `c476dee15cbcc541…`

~~~~text
60: PHASE ALSC2_B82 % 2 1 2 !
61: CONST ALSC2_B82 : AL : SC : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): ALSC2_B82, type code %, sha256 `3bd2989713373b92…`

~~~~text
62: PHASE ALSC2_B82 % 2 1 2 !
63: CONST ALSC2_B82 : AL : SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
_cited as the source of values for this phase_

## BCC_A2 (Al–Sc)

- Id: `phase:al-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1242.39–2500 K, x(Sc) 0.29125–1
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:bcc-a2)

Names (8): _corpus: _corpus:phase:al-sc:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2009.10.003:βSc, paper:10.1016/s0966-9795(98)00022-3:(βSc), paper:10.1361/105497198770342120:(βSc), paper:10.1361/105497198770342120:βSc  
_tdb: _tdb:AlSc-10Bo.tdb:BCC_A2, tdb:AlSc-98Mur.tdb:BCC_A2, tdb:AlSc-99Cac-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): BCC_A2, type code %B, sha256 `45d2f4a9a159e401…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL SC : VA : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): BCC_A2, type code %B, sha256 `c476dee15cbcc541…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL SC : VA : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): BCC_A2, type code %B, sha256 `3bd2989713373b92…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL SC : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
_cited as the source of values for this phase_

## FCC_A1 (Al–Sc)

- Id: `phase:al-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–933.47 K, x(Sc) 0–0.0024
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:fcc-a1)

Names (8): _corpus: _corpus:phase:al-sc:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.10.003:Fcc_Al, paper:10.1016/s0966-9795(98)00022-3:(Al), paper:10.1361/105497198770342120:(Al), paper:10.1361/105497198770342120:Al  
_tdb: _tdb:AlSc-10Bo.tdb:FCC_A1, tdb:AlSc-98Mur.tdb:FCC_A1, tdb:AlSc-99Cac-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): FCC_A1, type code %A, sha256 `45d2f4a9a159e401…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL SC : VA : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): FCC_A1, type code %A, sha256 `c476dee15cbcc541…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL SC : VA : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): FCC_A1, type code %A, sha256 `3bd2989713373b92…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL SC : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
_cited as the source of values for this phase_

## HCP_A3 (Al–Sc)

- Id: `phase:al-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1805.33 K, x(Sc) 0.89758–1
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:hcp-a3)

Names (7): _corpus: _corpus:phase:al-sc:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.10.003:αSc, paper:10.1016/s0966-9795(98)00022-3:(αSc), paper:10.1361/105497198770342120:(αSc)  
_tdb: _tdb:AlSc-10Bo.tdb:HCP_A3, tdb:AlSc-98Mur.tdb:HCP_A3, tdb:AlSc-99Cac-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): HCP_A3, type code %A, sha256 `45d2f4a9a159e401…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL SC : VA : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): HCP_A3, type code %A, sha256 `c476dee15cbcc541…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL SC : VA : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): HCP_A3, type code %A, sha256 `3bd2989713373b92…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL SC : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
_cited as the source of values for this phase_

## LIQUID (Al–Sc)

- Id: `phase:al-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 930.94–2500 K, x(Sc) 0–1
- Literature: 64 values (64 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sc:liquid)

Names (7): _corpus: _corpus:phase:al-sc:liquid  
_paper: _paper:10.1016/j.jallcom.2009.10.003:L, paper:10.1016/s0966-9795(98)00022-3:L, paper:10.1361/105497198770342120:L  
_tdb: _tdb:AlSc-10Bo.tdb:LIQUID, tdb:AlSc-98Mur.tdb:LIQUID, tdb:AlSc-99Cac-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-10Bo.tdb): LIQUID, type code %, sha256 `45d2f4a9a159e401…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL SC : !
~~~~

[AlSc-98Mur.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-98Mur.tdb): LIQUID, type code %, sha256 `c476dee15cbcc541…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL SC : !
~~~~

[AlSc-99Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSc-99Cac-LB.tdb): LIQUID, type code %, sha256 `3bd2989713373b92…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0966-9795(98)00022-3](https://doi.org/10.1016/S0966-9795%2898%2900022-3) G. Cacciamani, P. Riani, G. Borzone, N. Parodi, A. Saccone, R. Ferro, A. Pisch, R. Schmid-Fetzer, Intermetallics, 7, 101-108(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120) J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.03.002](https://doi.org/10.1016/j.calphad.2008.03.002) Y.B. Kang, A.D. Pelton, P. Chartrand, C.D. Fuerst, CALPHAD 32 (2008) 413–422.  
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
