# Am–O phases

> Am–O system: 10 phases (tier A 5, liquid 2, gas 2, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AM-O.html · Markdown: https://data.orchid-project.org/phases/pages/AM-O.md

10 phases (tier A 5, liquid 2, gas 2, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AM-O) · [full JSON](https://data.orchid-project.org/phases/systems/AM-O.json) · [Am–O system page](https://data.orchid-project.org/systems/AM-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/AM-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Am–O system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AM2O3_D52](#phase-am-o-am2o3-d52); _phase:am-o:am2o3-d52_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–675 K, x(O) 0.6–0.6 | 0 | 2 |
| [AMO1_62_D53](#phase-am-o-amo1-d53-62); _phase:am-o:amo1-d53-62_ |  | needs_review | not stable in 2 calculated diagram(s) | 0 | 2 |
| [AMO2_C1](#phase-am-o-amo2-c1); _phase:am-o:amo2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2306.9 K, x(O) 0.62168–0.66667 | 0 | 2 |
| [BCC_A2](#phase-am-o-bcc-a2); _phase:am-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [DHCP](#phase-am-o-dhcp-a3); _phase:am-o:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–675 K, x(O) 0–0 | 0 | 2 |
| [FCC_A1](#phase-am-o-fcc-a1); _phase:am-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-am-o-gas); _phase:am-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300.71–2500 K, x(O) 0–1 | 0 | 2 |
| [ION](#phase-am-o-ion); _phase:am-o:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2210.05–2500 K, x(O) 0–0.62919 | 0 | 2 |
| [LIQUID](#phase-am-o-liquid); _phase:am-o:liquid_ | liquid | liquid | not stable in 2 calculated diagram(s) | 1 | 2 |
| [O2GAS](#phase-am-o-o2gas); _phase:am-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1 | 0 | 2 |

## AM2O3_D52 (Am–O)

- Id: `phase:am-o:am2o3-d52`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–675 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:am2o3-d52)

Names (3): _corpus: _corpus:phase:am-o:am2o3-d52  
_tdb: _tdb:AmO-11Got.tdb:AM2O3_D52, tdb:AmO-17Epi.tdb:AM2O3_D52  


### TDB models of AM2O3_D52 (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): AM2O3_D52, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
65: PHASE AM2O3_D52:I % 2 2 3 !
66: CONST AM2O3_D52:I : AM+3 : O-2 : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): AM2O3_D52, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
64: PHASE AM2O3_D52:I % 2 2 3 !
65: CONST AM2O3_D52:I : AM+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## AMO1_62_D53 (Am–O)

- Id: `phase:am-o:amo1-d53-62`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D5_3; stoichiometry_contradicts_D5_3:AmO-11Got.tdb; unrecognised_name_tokens:62
- Candidate (name_token): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Strukturbericht/word 'D53' in the TDB name
- Candidate (sgte_mmc2): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Hallstedt 2025 mmc2 row for AMO1_62_D53: AmO1.62
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3 — AmO-11Got.tdb: 'Prototype Mn2O3 (cI80, Ia-3)'
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3 — AmO-17Epi.tdb: 'Prototype Mn2O3 (cI80, Ia-3)'
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:amo1-d53-62)

Names (3): _corpus: _corpus:phase:am-o:amo1-d53-62  
_tdb: _tdb:AmO-11Got.tdb:AMO1_62_D53, tdb:AmO-17Epi.tdb:AMO1_62_D53  


### TDB models of AMO1_62_D53 (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): AMO1_62_D53, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
70: PHASE AMO1_62_D53 % 2 1 1.62 !
71: CONST AMO1_62_D53 : AM : O : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): AMO1_62_D53, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
69: PHASE AMO1_62_D53:I % 3 2 3 1 !
70: CONST AMO1_62_D53:I : AM+3 AM+4 : O-2 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## AMO2_C1 (Am–O)

- Id: `phase:am-o:amo2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2306.9 K, x(O) 0.62168–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:amo2-c1)

Names (3): _corpus: _corpus:phase:am-o:amo2-c1  
_tdb: _tdb:AmO-11Got.tdb:AMO2_C1, tdb:AmO-17Epi.tdb:AMO2_C1  


### TDB models of AMO2_C1 (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): AMO2_C1, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
60: PHASE AMO2_C1:I % 3 1 2 1 !
61: CONST AMO2_C1:I : AM+3 AM+4 : O-2 VA : O-2 VA : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): AMO2_C1, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
59: PHASE AMO2_C1:I % 3 1 2 1 !
60: CONST AMO2_C1:I : AM+3 AM+4 : O-2 VA : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## BCC_A2 (Am–O)

- Id: `phase:am-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Am 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:bcc-a2)

Names (3): _corpus: _corpus:phase:am-o:bcc-a2  
_tdb: _tdb:AmO-11Got.tdb:BCC_A2, tdb:AmO-17Epi.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): BCC_A2, type code %B, sha256 `1d255c8beb1f09b8…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : AM : VA : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): BCC_A2, type code %B, sha256 `ca6b8ebfc913b566…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : AM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## DHCP (Am–O)

- Id: `phase:am-o:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Am 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–675 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:dhcp-a3)

Names (3): _corpus: _corpus:phase:am-o:dhcp-a3  
_tdb: _tdb:AmO-11Got.tdb:DHCP, tdb:AmO-17Epi.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): DHCP, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
55: PHASE DHCP % 1 1 !
56: CONST DHCP : AM : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): DHCP, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
54: PHASE DHCP % 1 1 !
55: CONST DHCP : AM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## FCC_A1 (Am–O)

- Id: `phase:am-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Am 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:fcc-a1)

Names (3): _corpus: _corpus:phase:am-o:fcc-a1  
_tdb: _tdb:AmO-11Got.tdb:FCC_A1, tdb:AmO-17Epi.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): FCC_A1, type code %A, sha256 `1d255c8beb1f09b8…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : AM : VA : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): FCC_A1, type code %A, sha256 `ca6b8ebfc913b566…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : AM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## GAS (Am–O)

- Id: `phase:am-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.71–2500 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:gas)

Names (3): _corpus: _corpus:phase:am-o:gas  
_tdb: _tdb:AmO-11Got.tdb:GAS, tdb:AmO-17Epi.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): GAS, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
76: PHASE GAS:G % 1 1 !
77: CONST GAS:G : AM AMO AMO2 O O2 O3 : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): GAS, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
75: PHASE GAS:G % 1 1 !
76: CONST GAS:G : AM AMO AMO2 O O2 O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## ION (Am–O)

- Id: `phase:am-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2210.05–2500 K, x(O) 0–0.62919
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:ion)

Names (3): _corpus: _corpus:phase:am-o:ion  
_tdb: _tdb:AmO-11Got.tdb:ION, tdb:AmO-17Epi.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): ION, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
40: PHASE ION:Y % 2 1 1 !
41: CONST ION:Y : AM+3 : O-2 VA O : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): ION, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
39: PHASE ION:Y % 2 1 1 !
40: CONST ION:Y : AM+3 : O-2 VA O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

## LIQUID (Am–O)

- Id: `phase:am-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Am 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:liquid)

Names (4): _corpus: _corpus:phase:am-o:liquid  
_paper: _paper:10.1021/acs.inorgchem.7b00572:liquid  
_tdb: _tdb:AmO-11Got.tdb:LIQUID, tdb:AmO-17Epi.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): LIQUID, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : AM : !
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): LIQUID, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : AM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_

## O2GAS (Am–O)

- Id: `phase:am-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-o:o2gas)

Names (3): _corpus: _corpus:phase:am-o:o2gas  
_tdb: _tdb:AmO-11Got.tdb:O2GAS, tdb:AmO-17Epi.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[AmO-11Got.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb): O2GAS, type code %, sha256 `1d255c8beb1f09b8…`

~~~~text
73: PHASE O2GAS % 1 1 !
74: CONST O2GAS : O2 :!
~~~~

[AmO-17Epi.tdb](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb): O2GAS, type code %, sha256 `ca6b8ebfc913b566…`

~~~~text
72: PHASE O2GAS % 1 1 !
73: CONST O2GAS : O2 :!
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_assessment that models this phase_
- [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017).  
_assessment that models this phase_

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
