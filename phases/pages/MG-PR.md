# Mg–Pr phases

> Mg–Pr system: 11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-PR.html · Markdown: https://data.orchid-project.org/phases/pages/MG-PR.md

11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-PR) · [full JSON](https://data.orchid-project.org/phases/systems/MG-PR.json) · [Mg–Pr system page](https://data.orchid-project.org/systems/MG-PR.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-PR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Pr system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-pr-bcc-a2); _phase:mg-pr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 782.6–2499 K, x(Pr) 0.63957–1 | 18 | 3 |
| [B2_BCC](#phase-mg-pr-bcc-b2); _phase:mg-pr:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.13 K, x(Pr) 0.45989–1 | 10 | 1 |
| [DHCP](#phase-mg-pr-dhcp-a3); _phase:mg-pr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Pr) 0.21896–1 | 9 | 3 |
| [FCC_A1](#phase-mg-pr-fcc-a1); _phase:mg-pr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-mg-pr-hcp-a3); _phase:mg-pr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–932.95 K, x(Pr) 0–0.00237 | 9 | 3 |
| [LIQUID](#phase-mg-pr-liquid); _phase:mg-pr:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 837.03–2500 K, x(Pr) 0–1 | 69 | 3 |
| [MG12PR_D2B](#phase-mg-pr-mg12pr-d2b); _phase:mg-pr:mg12pr-d2b_ | Mn12Th · D2_b · tI26 · I4/mmm (139) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–852.72 K, x(Pr) 0.07692–0.07692 | 17 | 3 |
| [MG2PR_C15](#phase-mg-pr-mg2pr-c15); _phase:mg-pr:mg2pr-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 932.78–1012.8 K, x(Pr) 0.33333–0.33333 | 26 | 3 |
| [MG3PR_D03](#phase-mg-pr-mg3pr-d03); _phase:mg-pr:mg3pr-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1063.03 K, x(Pr) 0.17988–0.25 | 35 | 3 |
| [MG41PR5](#phase-mg-pr-mg41pr5); _phase:mg-pr:mg41pr5_ | Ce5Mg41 · tI92 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–862.94 K, x(Pr) 0.10722–0.1087 | 17 | 3 |
| [MGPR_B2](#phase-mg-pr-mgpr-b2); _phase:mg-pr:mgpr-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1071 K, x(Pr) 0.4809–1 | 33 | 2 |

## BCC_A2 (Mg–Pr)

- Id: `phase:mg-pr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 3 calculated diagram(s): 782.6–2499 K, x(Pr) 0.63957–1
- Literature: 18 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:bcc-a2)

Names (7): _corpus: _corpus:phase:mg-pr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2007.05.007:bcc(Pr), paper:10.1016/j.commatsci.2014.11.050:βPr, paper:10.1016/j.jallcom.2005.03.033:bcc(Pr)  
_tdb: _tdb:MgPr-05Guo.tdb:BCC_A2, tdb:MgPr-08Guo.tdb:BCC_A2, tdb:MgPr-15Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): BCC_A2, type code %B, sha256 `663c0d9edf4eb106…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MG PR% : VA% : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): BCC_A2, type code %B, sha256 `33b8964cbc88b29c…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MG PR% : VA% : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): BCC_A2, type code %B, sha256 `43684dde82c30e77…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MG PR% : VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## B2_BCC (Mg–Pr)

- Id: `phase:mg-pr:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: MgPr-08Guo.tdb: ordered phase with disordered part BCC_A2 (order/disorder model)
- Caveat: partitioned order/disorder model in MgPr-08Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.13 K, x(Pr) 0.45989–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:bcc-b2)

Names (4): _corpus: _corpus:phase:mg-pr:bcc-b2, corpus:phase:mg-pr:b2-bcc  
_paper: _paper:10.1016/j.calphad.2007.05.007:MgPr  
_tdb: _tdb:MgPr-08Guo.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): B2_BCC, type code %BO, sha256 `33b8964cbc88b29c…`

~~~~text
41: PHASE B2_BCC %BO 3 0.5 0.5 3 !
42: CONST B2_BCC : MG% PR : MG PR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_

## DHCP (Mg–Pr)

- Id: `phase:mg-pr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Pr) 0.21896–1
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:dhcp-a3)

Names (8): _corpus: _corpus:phase:mg-pr:dhcp-a3, corpus:phase:mg-pr:dhcp  
_paper: _paper:10.1016/j.calphad.2007.05.007:dhcp(Pr), paper:10.1016/j.commatsci.2014.11.050:αPr, paper:10.1016/j.jallcom.2005.03.033:dhcp(Pr)  
_tdb: _tdb:MgPr-05Guo.tdb:DHCP, tdb:MgPr-08Guo.tdb:DHCP, tdb:MgPr-15Wan.tdb:DHCP  


### TDB models of DHCP (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): DHCP, type code %A, sha256 `663c0d9edf4eb106…`

~~~~text
44: PHASE DHCP %A 1 1 !
45: CONST DHCP : MG PR% : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): DHCP, type code %A, sha256 `33b8964cbc88b29c…`

~~~~text
51: PHASE DHCP %A 1 1 !
52: CONST DHCP : MG PR% : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): DHCP, type code %A, sha256 `43684dde82c30e77…`

~~~~text
40: PHASE DHCP %A 1 1 !
41: CONST DHCP : MG PR% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## FCC_A1 (Mg–Pr)

- Id: `phase:mg-pr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:fcc-a1)

Names (4): _corpus: _corpus:phase:mg-pr:fcc-a1  
_tdb: _tdb:MgPr-05Guo.tdb:FCC_A1, tdb:MgPr-08Guo.tdb:FCC_A1, tdb:MgPr-15Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): FCC_A1, type code %A, sha256 `663c0d9edf4eb106…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MG PR : VA% : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): FCC_A1, type code %A, sha256 `33b8964cbc88b29c…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MG PR : VA% : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): FCC_A1, type code %A, sha256 `43684dde82c30e77…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MG PR : VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase_

## HCP_A3 (Mg–Pr)

- Id: `phase:mg-pr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–932.95 K, x(Pr) 0–0.00237
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:hcp-a3)

Names (7): _corpus: _corpus:phase:mg-pr:hcp-a3  
_paper: _paper:10.1016/j.calphad.2007.05.007:hcp(Mg), paper:10.1016/j.commatsci.2014.11.050:(Mg), paper:10.1016/j.jallcom.2005.03.033:hcp(Mg)  
_tdb: _tdb:MgPr-05Guo.tdb:HCP_A3, tdb:MgPr-08Guo.tdb:HCP_A3, tdb:MgPr-15Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): HCP_A3, type code %A, sha256 `663c0d9edf4eb106…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MG% PR : VA% : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): HCP_A3, type code %A, sha256 `33b8964cbc88b29c…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : MG% PR : VA% : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): HCP_A3, type code %A, sha256 `43684dde82c30e77…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MG% PR : VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## LIQUID (Mg–Pr)

- Id: `phase:mg-pr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 837.03–2500 K, x(Pr) 0–1
- Literature: 69 values (69 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:liquid)

Names (8): _corpus: _corpus:phase:mg-pr:liquid  
_paper: _paper:10.1016/j.calphad.2007.05.007:L, paper:10.1016/j.commatsci.2014.11.050:Liquid, paper:10.1016/j.jallcom.2005.03.033:liq, paper:10.1016/j.jallcom.2005.03.033:liq.  
_tdb: _tdb:MgPr-05Guo.tdb:LIQUID, tdb:MgPr-08Guo.tdb:LIQUID, tdb:MgPr-15Wan.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): LIQUID, type code %, sha256 `663c0d9edf4eb106…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MG PR : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): LIQUID, type code %, sha256 `33b8964cbc88b29c…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MG PR : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): LIQUID, type code %, sha256 `43684dde82c30e77…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MG PR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## MG12PR_D2B (Mg–Pr)

- Id: `phase:mg-pr:mg12pr-d2b`; status `assigned`
- Structure: Mn12Th · D2_b · tI26 · I4/mmm (139); type `st:d2-b-mn12th-ti26`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.9231, Pr 0.0769
- Stability: stable in 3 of 3 calculated diagram(s): 300–852.72 K, x(Pr) 0.07692–0.07692
- Literature: 17 values (17 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:mg12pr-d2b)

Names (7): _corpus: _corpus:phase:mg-pr:mg12pr-d2b  
_paper: _paper:10.1016/j.calphad.2007.05.007:Mg12Pr, paper:10.1016/j.commatsci.2014.11.050:PrMg12, paper:10.1016/j.jallcom.2005.03.033:Mg12Pr  
_tdb: _tdb:MgPr-05Guo.tdb:MG12PR_D2B, tdb:MgPr-08Guo.tdb:MG12PR_D2B, tdb:MgPr-15Wan.tdb:MG12PR_D2B  


### TDB models of MG12PR_D2B (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): MG12PR_D2B, type code %, sha256 `663c0d9edf4eb106…`

~~~~text
49: PHASE MG12PR_D2B % 2 12 1 !
50: CONST MG12PR_D2B : MG : PR : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): MG12PR_D2B, type code %, sha256 `33b8964cbc88b29c…`

~~~~text
56: PHASE MG12PR_D2B % 2 12 1 !
57: CONST MG12PR_D2B : MG : PR : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): MG12PR_D2B, type code %, sha256 `43684dde82c30e77…`

~~~~text
45: PHASE MG12PR_D2B % 2 12 1 !
46: CONST MG12PR_D2B : MG : PR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## MG2PR_C15 (Mg–Pr)

- Id: `phase:mg-pr:mg2pr-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.6667, Pr 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 932.78–1012.8 K, x(Pr) 0.33333–0.33333
- Literature: 26 values (26 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:mg2pr-c15)

Names (8): _corpus: _corpus:phase:mg-pr:mg2pr-c15  
_paper: _paper:10.1016/j.calphad.2007.05.007:Mg2Pr, paper:10.1016/j.commatsci.2014.11.050:Mg2Pr, paper:10.1016/j.commatsci.2014.11.050:PrMg2, paper:10.1016/j.jallcom.2005.03.033:Mg2Pr  
_tdb: _tdb:MgPr-05Guo.tdb:MG2PR_C15, tdb:MgPr-08Guo.tdb:MG2PR_C15, tdb:MgPr-15Wan.tdb:MG2PR_C15  


### TDB models of MG2PR_C15 (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): MG2PR_C15, type code %, sha256 `663c0d9edf4eb106…`

~~~~text
64: PHASE MG2PR_C15 % 2 2 1 !
65: CONST MG2PR_C15 : MG : PR : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): MG2PR_C15, type code %, sha256 `33b8964cbc88b29c…`

~~~~text
71: PHASE MG2PR_C15 % 2 2 1 !
72: CONST MG2PR_C15 : MG : PR : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): MG2PR_C15, type code %, sha256 `43684dde82c30e77…`

~~~~text
60: PHASE MG2PR_C15 % 2 2 1 !
61: CONST MG2PR_C15 : MG : PR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## MG3PR_D03 (Mg–Pr)

- Id: `phase:mg-pr:mg3pr-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1063.03 K, x(Pr) 0.17988–0.25
- Literature: 35 values (35 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:mg3pr-d03)

Names (7): _corpus: _corpus:phase:mg-pr:mg3pr-d03  
_paper: _paper:10.1016/j.calphad.2007.05.007:Mg3Pr, paper:10.1016/j.commatsci.2014.11.050:PrMg3, paper:10.1016/j.jallcom.2005.03.033:Mg3Pr  
_tdb: _tdb:MgPr-05Guo.tdb:MG3PR_D03, tdb:MgPr-08Guo.tdb:MG3PR_D03, tdb:MgPr-15Wan.tdb:MG3PR_D03  


### TDB models of MG3PR_D03 (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): MG3PR_D03, type code %, sha256 `663c0d9edf4eb106…`

~~~~text
59: PHASE MG3PR_D03 % 2 3 1 !
60: CONST MG3PR_D03 : MG : MG PR% : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): MG3PR_D03, type code %, sha256 `33b8964cbc88b29c…`

~~~~text
66: PHASE MG3PR_D03 % 2 3 1 !
67: CONST MG3PR_D03 : MG : MG PR% : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): MG3PR_D03, type code %, sha256 `43684dde82c30e77…`

~~~~text
55: PHASE MG3PR_D03 % 2 3 1 !
56: CONST MG3PR_D03 : MG : PR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## MG41PR5 (Mg–Pr)

- Id: `phase:mg-pr:mg41pr5`; status `assigned`
- Structure: Ce5Mg41 · tI92 · I4/m (87); type `st:ce5mg41-ti92`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 300–862.94 K, x(Pr) 0.10722–0.1087
- Literature: 17 values (17 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:mg41pr5)

Names (7): _corpus: _corpus:phase:mg-pr:mg41pr5  
_paper: _paper:10.1016/j.calphad.2007.05.007:Mg41Pr5, paper:10.1016/j.commatsci.2014.11.050:Pr5Mg41, paper:10.1016/j.jallcom.2005.03.033:Mg41Pr5  
_tdb: _tdb:MgPr-05Guo.tdb:MG41PR5, tdb:MgPr-08Guo.tdb:MG41PR5, tdb:MgPr-15Wan.tdb:MG41PR5  


### TDB models of MG41PR5 (3): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): MG41PR5, type code %, sha256 `663c0d9edf4eb106…`

~~~~text
54: PHASE MG41PR5 % 2 41 5 !
55: CONST MG41PR5 : MG% PR : MG PR% : !
~~~~

[MgPr-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-08Guo.tdb): MG41PR5, type code %, sha256 `33b8964cbc88b29c…`

~~~~text
61: PHASE MG41PR5 % 2 41 5 !
62: CONST MG41PR5 : MG : PR : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): MG41PR5, type code %, sha256 `43684dde82c30e77…`

~~~~text
50: PHASE MG41PR5 % 2 41 5 !
51: CONST MG41PR5 : MG : PR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
_cited as the source of values for this phase_

## MGPR_B2 (Mg–Pr)

- Id: `phase:mg-pr:mgpr-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgPr-05Guo.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1071 K, x(Pr) 0.4809–1
- Literature: 33 values (33 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pr:mgpr-b2)

Names (5): _corpus: _corpus:phase:mg-pr:mgpr-b2  
_paper: _paper:10.1016/j.commatsci.2014.11.050:PrMg, paper:10.1016/j.jallcom.2005.03.033:MgPr  
_tdb: _tdb:MgPr-05Guo.tdb:MGPR_B2, tdb:MgPr-15Wan.tdb:MGPR_B2  


### TDB models of MGPR_B2 (2): PHASE and CONSTITUENT statements as written

[MgPr-05Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-05Guo.tdb): MGPR_B2, type code %, sha256 `663c0d9edf4eb106…`

~~~~text
69: PHASE MGPR_B2 % 2 1 1 !
70: CONST MGPR_B2 : MG% PR : MG PR% : !
~~~~

[MgPr-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPr-15Wan.tdb): MGPR_B2, type code %, sha256 `43684dde82c30e77…`

~~~~text
65: PHASE MGPR_B2 % 2 1 1 !
66: CONST MGPR_B2 : MG : MG PR% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2014.11.050](https://doi.org/10.1016/j.commatsci.2014.11.050) Peisheng Wang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Mg–Pr system, Computational Materials Science 104, 138-142 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.03.033](https://doi.org/10.1016/j.jallcom.2005.03.033) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Mg–Pr system, Journal of Alloys and Compounds 399, 183-188 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(93)90010-s](https://doi.org/10.1016/0966-9795%2893%2990010-s) A. Saccone, A.M. Cardinale, S. Delfino, R. Ferro, A contribution to the rare earth intermetallic chemistry: Praseodymium-magnesium alloy system, Intermetallics 1, 151-158 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(00)01377-3](https://doi.org/10.1016/s0925-8388%2800%2901377-3) A. Saccone, D. Macciò, J.A.J. Robinson, F.H. Hayes, R. Ferro, Smith thermal analysis of selected Pr–Mg alloys, Journal of Alloys and Compounds 317-318, 497-502 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.05.005](https://doi.org/10.1016/j.calphad.2012.05.005) Y. Kang, L. Jin, P. Chartrand, A.E. Gheribi, K. Bai, P. Wu, CALPHAD 38 (2012) 100–116.  
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
