# Ni–Se phases

> Ni–Se system: 10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-SE.html · Markdown: https://data.orchid-project.org/phases/pages/NI-SE.md

10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-SE) · [full JSON](https://data.orchid-project.org/phases/systems/NI-SE.json) · [Ni–Se system page](https://data.orchid-project.org/systems/NI-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Se system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-ni-se-a8-hexagonal); _phase:ni-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–497.13 K, x(Se) 1–1 | 3 | 1 |
| [BCC_A2](#phase-ni-se-bcc-a2); _phase:ni-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ni-se-fcc-a1); _phase:ni-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1741.24 K, x(Se) 0–0 | 6 | 1 |
| [HCP_A3](#phase-ni-se-hcp-a3); _phase:ni-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ni-se-liquid); _phase:ni-se:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 490.13–2500 K, x(Se) 0–1 | 18 | 1 |
| [NI3SE2_HT](#phase-ni-se-ni3se2); _phase:ni-se:ni3se2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 839.29–1057.48 K, x(Se) 0.405–0.405 | 14 | 1 |
| [NI3SE2_D5E](#phase-ni-se-ni3se2-d5e); _phase:ni-se:ni3se2-d5e_ | Ni3S2 · D5_e · hR5 · R32 (155) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–865.64 K, x(Se) 0.4–0.4 | 8 | 1 |
| [NI6SE5](#phase-ni-se-ni6se5); _phase:ni-se:ni6se5_ | Ni6Se5 · oP88 · Pca2_1 (29) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 672.72–920.29 K, x(Se) 0.45455–0.45455 | 8 | 1 |
| [NISE_B81](#phase-ni-se-nise-b81); _phase:ni-se:nise-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1231.3 K, x(Se) 0.50889–0.57024 | 19 | 1 |
| [NISE2_C2](#phase-ni-se-nise2-c2); _phase:ni-se:nise2-c2_ | beta-FeS2 · C2 · cP12 · Pa-3 (205) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1131.01 K, x(Se) 0.66667–0.66667 | 9 | 1 |

## HEXAGONAL_A8 (Ni–Se)

- Id: `phase:ni-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–497.13 K, x(Se) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:a8-hexagonal)

Names (4): _corpus: _corpus:phase:ni-se:a8-hexagonal, corpus:phase:ni-se:hexagonal-a8  
_paper: _paper:10.1007/s11669-021-00906-9:hex_A8 (Se)  
_tdb: _tdb:NiSe-21Zob.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): HEXAGONAL_A8, type code %, sha256 `1b075f9b26619344…`

~~~~text
50: PHASE HEXAGONAL_A8 % 1 1 !
51: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
_cited as the source of values for this phase_

## BCC_A2 (Ni–Se)

- Id: `phase:ni-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:bcc-a2)

Names (2): _corpus: _corpus:phase:ni-se:bcc-a2  
_tdb: _tdb:NiSe-21Zob.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): BCC_A2, type code %B, sha256 `1b075f9b26619344…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase_

## FCC_A1 (Ni–Se)

- Id: `phase:ni-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1741.24 K, x(Se) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:fcc-a1)

Names (3): _corpus: _corpus:phase:ni-se:fcc-a1  
_paper: _paper:10.1007/s11669-021-00906-9:FCC_A1  
_tdb: _tdb:NiSe-21Zob.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): FCC_A1, type code %A, sha256 `1b075f9b26619344…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
_cited as the source of values for this phase_

## HCP_A3 (Ni–Se)

- Id: `phase:ni-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:hcp-a3)

Names (2): _corpus: _corpus:phase:ni-se:hcp-a3  
_tdb: _tdb:NiSe-21Zob.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): HCP_A3, type code %A, sha256 `1b075f9b26619344…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase_

## LIQUID (Ni–Se)

- Id: `phase:ni-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 490.13–2500 K, x(Se) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:liquid)

Names (4): _corpus: _corpus:phase:ni-se:liquid  
_paper: _paper:10.1007/s11669-021-00906-9:Liquid, paper:10.1007/s11669-021-00906-9:Liquid’  
_tdb: _tdb:NiSe-21Zob.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): LIQUID, type code %, sha256 `1b075f9b26619344…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : NI NISE SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
_cited as the source of values for this phase_

## NI3SE2_HT (Ni–Se)

- Id: `phase:ni-se:ni3se2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Ni3Se2-ht) · cF\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ni3Se2-ht) — Hallstedt 2025 mmc2 row for NI3SE2_HT: Ni3Se2 (high T)
- Stoichiometry: Ni 0.5950, Se 0.4050
- Stability: stable in 1 of 1 calculated diagram(s): 839.29–1057.48 K, x(Se) 0.405–0.405
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:ni3se2)

Names (4): _corpus: _corpus:phase:ni-se:ni3se2, corpus:phase:ni-se:ni3se2-ht  
_paper: _paper:10.1007/s11669-021-00906-9:Ni3Se2_HT  
_tdb: _tdb:NiSe-21Zob.tdb:NI3SE2_HT  


### TDB models of NI3SE2_HT (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): NI3SE2_HT, type code %, sha256 `1b075f9b26619344…`

~~~~text
60: PHASE NI3SE2_HT % 2 0.595 0.405 !
61: CONST NI3SE2_HT : NI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
_cited as the source of values for this phase_

## NI3SE2_D5E (Ni–Se)

- Id: `phase:ni-se:ni3se2-d5e`; status `assigned`
- Structure: Ni3S2 · D5_e · hR5 · R32 (155); type `st:d5-e-ni3s2-hr5`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadbc and oqmd-5233, space group 155
- Stoichiometry: Ni 0.6000, Se 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–865.64 K, x(Se) 0.4–0.4
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:ni3se2-d5e)

Names (5): _corpus: _corpus:phase:ni-se:ni3se2-d5e  
_mp: _mp:mp-aaaaadbc  
_oqmd: _oqmd:oqmd-5233  
_paper: _paper:10.1007/s11669-021-00906-9:Ni3Se2_LT  
_tdb: _tdb:NiSe-21Zob.tdb:NI3SE2_D5E  


### TDB models of NI3SE2_D5E (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): NI3SE2_D5E, type code %, sha256 `1b075f9b26619344…`

~~~~text
55: PHASE NI3SE2_D5E % 2 3 2 !
56: CONST NI3SE2_D5E : NI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
_cited as the source of values for this phase_

## NI6SE5 (Ni–Se)

- Id: `phase:ni-se:ni6se5`; status `assigned`
- Structure: Ni6Se5 · oP88 · Pca2_1 (29); type `st:ni6se5-op88`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.5455, Se 0.4545
- Stability: stable in 1 of 1 calculated diagram(s): 672.72–920.29 K, x(Se) 0.45455–0.45455
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:ni6se5)

Names (3): _corpus: _corpus:phase:ni-se:ni6se5  
_paper: _paper:10.1007/s11669-021-00906-9:Ni6Se5  
_tdb: _tdb:NiSe-21Zob.tdb:NI6SE5  


### TDB models of NI6SE5 (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): NI6SE5, type code %, sha256 `1b075f9b26619344…`

~~~~text
65: PHASE NI6SE5 % 2 6 5 !
66: CONST NI6SE5 : NI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
_cited as the source of values for this phase_

## NISE_B81 (Ni–Se)

- Id: `phase:ni-se:nise-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1231.3 K, x(Se) 0.50889–0.57024
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:nise-b81)

Names (3): _corpus: _corpus:phase:ni-se:nise-b81  
_paper: _paper:10.1007/s11669-021-00906-9:NiSe  
_tdb: _tdb:NiSe-21Zob.tdb:NISE_B81  


### TDB models of NISE_B81 (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): NISE_B81, type code %, sha256 `1b075f9b26619344…`

~~~~text
70: PHASE NISE_B81 % 2 1 1 !
71: CONST NISE_B81 : NI% SE : SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.26-2085](https://doi.org/10.3891/acta.chem.scand.26-2085) Fredrik Grønvold, Mats Nygren, D. Simov, H. A. Øye, Sigfrid Svensson, High-Temperature Reaction Calorimeter. Enthalpy of Formation of Iron Selenides and Nickel Selenides at 1050 K., Acta Chem. Scand. 26, 2085-2099 (1972).  
_cited as the source of values for this phase_

## NISE2_C2 (Ni–Se)

- Id: `phase:ni-se:nise2-c2`; status `assigned`
- Structure: beta-FeS2 · C2 · cP12 · Pa-3 (205); type `st:c2-beta-fes2-cp12`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 0.3333, Se 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1131.01 K, x(Se) 0.66667–0.66667
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-se:nise2-c2)

Names (3): _corpus: _corpus:phase:ni-se:nise2-c2  
_paper: _paper:10.1007/s11669-021-00906-9:NiSe2  
_tdb: _tdb:NiSe-21Zob.tdb:NISE2_C2  


### TDB models of NISE2_C2 (1): PHASE and CONSTITUENT statements as written

[NiSe-21Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSe-21Zob.tdb): NISE2_C2, type code %, sha256 `1b075f9b26619344…`

~~~~text
75: PHASE NISE2_C2 % 2 1 2 !
76: CONST NISE2_C2 : NI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00906-9](https://doi.org/10.1007/s11669-021-00906-9) Ondřej Zobač, Kateřina Buchlovská, Jana Pavlů, Aleš Kroupa, Thermodynamic Description of Binary System Nickel-Selenium, J. Phase Equilib. Diffus. 42, 468-478 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00905165](https://doi.org/10.1007/bf00905165) K. L. Komarek, K. Wessely, Die Systeme Nickel?Selen und Kobalt?Nickel-Selen, Monatshefte fr Chemie 103, 923-933 (1972).  
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
