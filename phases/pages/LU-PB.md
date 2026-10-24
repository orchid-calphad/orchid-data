# Lu–Pb phases

> Lu–Pb system: 10 phases (tier A 4, tier C 2, liquid 2, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LU-PB.html · Markdown: https://data.orchid-project.org/phases/pages/LU-PB.md

10 phases (tier A 4, tier C 2, liquid 2, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LU-PB) · [full JSON](https://data.orchid-project.org/phases/systems/LU-PB.json) · [Lu–Pb system page](https://data.orchid-project.org/systems/LU-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/LU-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Lu–Pb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ASSOCI](#phase-lu-pb-associ); _phase:lu-pb:associ_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-lu-pb-bcc-a2); _phase:lu-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-lu-pb-fcc-a1); _phase:lu-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.36 K, x(Pb) 1–1 | 2 | 2 |
| [HCP_A3](#phase-lu-pb-hcp-a3); _phase:lu-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1983.38 K, x(Pb) 0–0.01182 | 4 | 2 |
| [LIQUID](#phase-lu-pb-liquid); _phase:lu-pb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 595.96–2500 K, x(Pb) 0–1 | 28 | 2 |
| [LU5PB3_D88](#phase-lu-pb-lu5pb3-d88); _phase:lu-pb:lu5pb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1967.22 K, x(Pb) 0.375–0.375 | 14 | 2 |
| [LU5PB4_HT](#phase-lu-pb-lu5pb4-ht); _phase:lu-pb:lu5pb4-ht_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1747.98–1772.79 K, x(Pb) 0.44444–0.44444 | 8 | 2 |
| [LU5PB4_LT](#phase-lu-pb-lu5pb4-lt); _phase:lu-pb:lu5pb4-lt_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1749.54 K, x(Pb) 0.44444–0.44444 | 10 | 2 |
| [LU6PB5](#phase-lu-pb-lu6pb5); _phase:lu-pb:lu6pb5_ | Si5V6 · oI44 · Ibam (72) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1445.91 K, x(Pb) 0.45455–0.45455 | 8 | 2 |
| [LUPB2](#phase-lu-pb-lupb2); _phase:lu-pb:lupb2_ | CuZr2 · tI6 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–845.22 K, x(Pb) 0.66667–0.66667 | 8 | 2 |

## ASSOCI (Lu–Pb)

- Id: `phase:lu-pb:associ`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:associ)

Names (2): _corpus: _corpus:phase:lu-pb:associ  
_tdb: _tdb:LuPb-12Idd.tdb:ASSOCI  


### TDB models of ASSOCI (1): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): ASSOCI, type code %, sha256 `33e63b676c5f908f…`

~~~~text
35: PHASE ASSOCI:L % 1 1 !
36: CONST ASSOCI:L : LU LU5PB3 PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase_

## BCC_A2 (Lu–Pb)

- Id: `phase:lu-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:bcc-a2)

Names (3): _corpus: _corpus:phase:lu-pb:bcc-a2  
_tdb: _tdb:LuPb-12Idd.tdb:BCC_A2, tdb:LuPb-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): BCC_A2, type code %B, sha256 `33e63b676c5f908f…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : PB : VA : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): BCC_A2, type code %B, sha256 `602dc6f7866693ae…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : PB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase_

## FCC_A1 (Lu–Pb)

- Id: `phase:lu-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.36 K, x(Pb) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:fcc-a1)

Names (4): _corpus: _corpus:phase:lu-pb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2013.01.007:(Pb)  
_tdb: _tdb:LuPb-12Idd.tdb:FCC_A1, tdb:LuPb-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): FCC_A1, type code %A, sha256 `33e63b676c5f908f…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : PB : VA : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): FCC_A1, type code %A, sha256 `602dc6f7866693ae…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : LU PB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
_cited as the source of values for this phase_

## HCP_A3 (Lu–Pb)

- Id: `phase:lu-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1983.38 K, x(Pb) 0–0.01182
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:hcp-a3)

Names (5): _corpus: _corpus:phase:lu-pb:hcp-a3  
_paper: _paper:10.1007/s10973-011-1881-2:(Lu), paper:10.1016/j.calphad.2013.01.007:(Lu)  
_tdb: _tdb:LuPb-12Idd.tdb:HCP_A3, tdb:LuPb-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): HCP_A3, type code %A, sha256 `33e63b676c5f908f…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : LU% PB : VA : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): HCP_A3, type code %A, sha256 `602dc6f7866693ae…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : LU% PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
_cited as the source of values for this phase_

## LIQUID (Lu–Pb)

- Id: `phase:lu-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 595.96–2500 K, x(Pb) 0–1
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:liquid)

Names (5): _corpus: _corpus:phase:lu-pb:liquid  
_paper: _paper:10.1007/s10973-011-1881-2:Liq, paper:10.1016/j.calphad.2013.01.007:L  
_tdb: _tdb:LuPb-12Idd.tdb:LIQUID, tdb:LuPb-13Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): LIQUID, type code %, sha256 `33e63b676c5f908f…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : LU PB : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): LIQUID, type code %, sha256 `602dc6f7866693ae…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : LU PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
_cited as the source of values for this phase_

## LU5PB3_D88 (Lu–Pb)

- Id: `phase:lu-pb:lu5pb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackxxn and oqmd-30697, space group 193
- Stoichiometry: Lu 0.6250, Pb 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–1967.22 K, x(Pb) 0.375–0.375
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:lu5pb3-d88)

Names (7): _corpus: _corpus:phase:lu-pb:lu5pb3-d88  
_mp: _mp:mp-aaackxxn  
_oqmd: _oqmd:oqmd-30697  
_paper: _paper:10.1007/s10973-011-1881-2:Lu5Pb3, paper:10.1016/j.calphad.2013.01.007:Lu5Pb3  
_tdb: _tdb:LuPb-12Idd.tdb:LU5PB3_D88, tdb:LuPb-13Wan.tdb:LU5PB3_D88  


### TDB models of LU5PB3_D88 (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): LU5PB3_D88, type code %, sha256 `33e63b676c5f908f…`

~~~~text
55: PHASE LU5PB3_D88 % 2 5 3 !
56: CONST LU5PB3_D88 : LU : PB : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): LU5PB3_D88, type code %, sha256 `602dc6f7866693ae…`

~~~~text
50: PHASE LU5PB3_D88 % 2 5 3 !
51: CONST LU5PB3_D88 : LU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
_cited as the source of values for this phase_

## LU5PB4_HT (Lu–Pb)

- Id: `phase:lu-pb:lu5pb4-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (sgte_mmc2): (Lu5Pb4-ht) — Hallstedt 2025 mmc2 row for LU5PB4_HT: Lu5Pb4-ht
- Stoichiometry: Lu 0.5556, Pb 0.4444
- Stability: stable in 2 of 2 calculated diagram(s): 1747.98–1772.79 K, x(Pb) 0.44444–0.44444
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:lu5pb4-ht)

Names (5): _corpus: _corpus:phase:lu-pb:lu5pb4-ht  
_paper: _paper:10.1007/s10973-011-1881-2:βLu5Pb4, paper:10.1016/j.calphad.2013.01.007:βLu5Pb4  
_tdb: _tdb:LuPb-12Idd.tdb:LU5PB4_HT, tdb:LuPb-13Wan.tdb:LU5PB4_HT  


### TDB models of LU5PB4_HT (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): LU5PB4_HT, type code %, sha256 `33e63b676c5f908f…`

~~~~text
65: PHASE LU5PB4_HT % 2 5 4 !
66: CONST LU5PB4_HT : LU : PB : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): LU5PB4_HT, type code %, sha256 `602dc6f7866693ae…`

~~~~text
60: PHASE LU5PB4_HT % 2 5 4 !
61: CONST LU5PB4_HT : LU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
_cited as the source of values for this phase_

## LU5PB4_LT (Lu–Pb)

- Id: `phase:lu-pb:lu5pb4-lt`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (sgte_mmc2): (Lu5Pb4-lt) — Hallstedt 2025 mmc2 row for LU5PB4_LT: Lu5Pb5-lt
- Stoichiometry: Lu 0.5556, Pb 0.4444
- Stability: stable in 2 of 2 calculated diagram(s): 300–1749.54 K, x(Pb) 0.44444–0.44444
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:lu5pb4-lt)

Names (5): _corpus: _corpus:phase:lu-pb:lu5pb4-lt  
_paper: _paper:10.1007/s10973-011-1881-2:αLu5Pb4, paper:10.1016/j.calphad.2013.01.007:αLu5Pb4  
_tdb: _tdb:LuPb-12Idd.tdb:LU5PB4_LT, tdb:LuPb-13Wan.tdb:LU5PB4_LT  


### TDB models of LU5PB4_LT (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): LU5PB4_LT, type code %, sha256 `33e63b676c5f908f…`

~~~~text
60: PHASE LU5PB4_LT % 2 5 4 !
61: CONST LU5PB4_LT : LU : PB : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): LU5PB4_LT, type code %, sha256 `602dc6f7866693ae…`

~~~~text
55: PHASE LU5PB4_LT % 2 5 4 !
56: CONST LU5PB4_LT : LU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
_cited as the source of values for this phase_

## LU6PB5 (Lu–Pb)

- Id: `phase:lu-pb:lu6pb5`; status `assigned`
- Structure: Si5V6 · oI44 · Ibam (72); type `st:si5v6-oi44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Lu 0.5455, Pb 0.4545
- Stability: stable in 2 of 2 calculated diagram(s): 300–1445.91 K, x(Pb) 0.45455–0.45455
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:lu6pb5)

Names (5): _corpus: _corpus:phase:lu-pb:lu6pb5  
_paper: _paper:10.1007/s10973-011-1881-2:Lu6Pb5, paper:10.1016/j.calphad.2013.01.007:Lu6Pb5  
_tdb: _tdb:LuPb-12Idd.tdb:LU6PB5, tdb:LuPb-13Wan.tdb:LU6PB5  


### TDB models of LU6PB5 (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): LU6PB5, type code %, sha256 `33e63b676c5f908f…`

~~~~text
70: PHASE LU6PB5 % 2 6 5 !
71: CONST LU6PB5 : LU : PB : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): LU6PB5, type code %, sha256 `602dc6f7866693ae…`

~~~~text
65: PHASE LU6PB5 % 2 6 5 !
66: CONST LU6PB5 : LU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
_cited as the source of values for this phase_

## LUPB2 (Lu–Pb)

- Id: `phase:lu-pb:lupb2`; status `assigned`
- Structure: CuZr2 · tI6 · I4/mmm (139); type `st:cuzr2-ti6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Lu 0.3333, Pb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–845.22 K, x(Pb) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:lu-pb:lupb2)

Names (5): _corpus: _corpus:phase:lu-pb:lupb2  
_paper: _paper:10.1007/s10973-011-1881-2:LuPb2, paper:10.1016/j.calphad.2013.01.007:LuPb2  
_tdb: _tdb:LuPb-12Idd.tdb:LUPB2, tdb:LuPb-13Wan.tdb:LUPB2  


### TDB models of LUPB2 (2): PHASE and CONSTITUENT statements as written

[LuPb-12Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-12Idd.tdb): LUPB2, type code %, sha256 `33e63b676c5f908f…`

~~~~text
75: PHASE LUPB2 % 2 1 2 !
76: CONST LUPB2 : LU : PB : !
~~~~

[LuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LuPb-13Wan.tdb): LUPB2, type code %, sha256 `602dc6f7866693ae…`

~~~~text
70: PHASE LUPB2 % 2 1 2 !
71: CONST LUPB2 : LU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-011-1881-2](https://doi.org/10.1007/s10973-011-1881-2) A. Iddaoudi, N. Selhaoui, M. Ait Amar, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Lu–Pb binary system, J Therm Anal Calorim 110, 923-928 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90179-9](https://doi.org/10.1016/0022-5088%2869%2990179-9) O.D. McMasters, K.A. Gschneidner, The lutetium-lead system, Journal of the Less Common Metals 19, 337-344 (1969).  
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
