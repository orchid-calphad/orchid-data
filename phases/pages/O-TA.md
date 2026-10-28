# O–Ta phases

> O–Ta system: 8 phases (tier A 3, tier C 2, liquid 2, gas 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-TA.html · Markdown: https://data.orchid-project.org/phases/pages/O-TA.md

8 phases (tier A 3, tier C 2, liquid 2, gas 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-TA) · [full JSON](https://data.orchid-project.org/phases/systems/O-TA.json) · [O–Ta system page](https://data.orchid-project.org/systems/O-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Ta system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-ta-bcc-a2); _phase:o-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3762.45 K, x(O) 0–0.05535 | 4 | 3 |
| [FCC_A1](#phase-o-ta-fcc-a1); _phase:o-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-o-ta-hcp-a3); _phase:o-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ION](#phase-o-ta-ion); _phase:o-ta:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1787.58–4000 K, x(O) 0–0.71429 | 0 | 2 |
| [LIQUID](#phase-o-ta-liquid); _phase:o-ta:liquid_ | liquid | liquid | stable in 1 of 3 calculated diagram(s): 1914.25–4000 K, x(O) 0–0.7154 | 7 | 3 |
| [O2GAS](#phase-o-ta-o2gas); _phase:o-ta:o2gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(O) 1–1 | 0 | 3 |
| [TA2O5_HT](#phase-o-ta-ta2o5-ht); _phase:o-ta:ta2o5-ht_ | Ta2O5 · tI44 · I4_1/amd (141) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 1592.88–2169.22 K, x(O) 0.71429–0.71429 | 0 | 3 |
| [TA2O5_LT](#phase-o-ta-ta2o5-lt); _phase:o-ta:ta2o5-lt_ | Ta2O5 · oP14 · Pccm (49) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1593.01 K, x(O) 0.71429–0.71429 | 0 | 3 |

## BCC_A2 (O–Ta)

- Id: `phase:o-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3762.45 K, x(O) 0–0.05535
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:bcc-a2)

Names (5): _corpus: _corpus:phase:o-ta:bcc-a2  
_paper: _paper:10.1002/adem.202200162:bcc  
_tdb: _tdb:TaO-22Geb.tdb:BCC_A2, tdb:TaO-22Mei-ass.tdb:BCC_A2, tdb:TaO-22Mei-ion.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): BCC_A2, type code %B, sha256 `886665f3a1ed281c…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : TA : O VA : !
~~~~

[TaO-22Mei-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ass.tdb): BCC_A2, type code %B, sha256 `50b2e3a96e3d3b0a…`

~~~~text
42: PHASE BCC_A2 %B 2 1 1 !
43: CONST BCC_A2 : TA : O VA : !
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): BCC_A2, type code %B, sha256 `88e6b32a58541759…`

~~~~text
48: PHASE BCC_A2 %B 2 1 1 !
49: CONST BCC_A2 : TA : O VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02648373](https://doi.org/10.1007/bf02648373) S. P. Garg, N. Krishnamurthy, A. Awasthi, M. Venkatraman, J. Phase Equilib. 1996, 17, 63.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(72)90062-8](https://doi.org/10.1016/0022-5088%2872%2990062-8) H. Jehn, E. Olzi, J. Less-Common Met. 1972, 27, 297.  
_cited as the source of values for this phase_

## FCC_A1 (O–Ta)

- Id: `phase:o-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ta 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:fcc-a1)

Names (4): _corpus: _corpus:phase:o-ta:fcc-a1  
_tdb: _tdb:TaO-22Geb.tdb:FCC_A1, tdb:TaO-22Mei-ass.tdb:FCC_A1, tdb:TaO-22Mei-ion.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): FCC_A1, type code %A, sha256 `886665f3a1ed281c…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : TA : VA : !
~~~~

[TaO-22Mei-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ass.tdb): FCC_A1, type code %A, sha256 `50b2e3a96e3d3b0a…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : TA : VA : !
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): FCC_A1, type code %A, sha256 `88e6b32a58541759…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase_

## HCP_A3 (O–Ta)

- Id: `phase:o-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ta 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:hcp-a3)

Names (4): _corpus: _corpus:phase:o-ta:hcp-a3  
_tdb: _tdb:TaO-22Geb.tdb:HCP_A3, tdb:TaO-22Mei-ass.tdb:HCP_A3, tdb:TaO-22Mei-ion.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): HCP_A3, type code %A, sha256 `886665f3a1ed281c…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : TA : VA : !
~~~~

[TaO-22Mei-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ass.tdb): HCP_A3, type code %A, sha256 `50b2e3a96e3d3b0a…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : TA : VA : !
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): HCP_A3, type code %A, sha256 `88e6b32a58541759…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase_

## ION (O–Ta)

- Id: `phase:o-ta:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1787.58–4000 K, x(O) 0–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:ion)

Names (3): _corpus: _corpus:phase:o-ta:ion  
_tdb: _tdb:TaO-22Geb.tdb:ION, tdb:TaO-22Mei-ion.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): ION, type code %, sha256 `886665f3a1ed281c…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : TA+2 TA+5 : O-2 VA : !
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): ION, type code %, sha256 `88e6b32a58541759…`

~~~~text
38: PHASE ION:Y % 2 1 1 !
39: CONST ION:Y : TA+5 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase_

## LIQUID (O–Ta)

- Id: `phase:o-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 3 calculated diagram(s): 1914.25–4000 K, x(O) 0–0.7154
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:liquid)

Names (6): _corpus: _corpus:phase:o-ta:liquid  
_paper: _paper:10.1002/adem.202200162:liquid2, paper:10.1016/j.calphad.2022.102391:liquid  
_tdb: _tdb:TaO-22Geb.tdb:LIQUID, tdb:TaO-22Mei-ass.tdb:LIQUID, tdb:TaO-22Mei-ion.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): LIQUID, type code %, sha256 `886665f3a1ed281c…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : TA : !
~~~~

[TaO-22Mei-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ass.tdb): LIQUID, type code %, sha256 `50b2e3a96e3d3b0a…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : O TA TA2O5 : !
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): LIQUID, type code %, sha256 `88e6b32a58541759…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : TA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02648373](https://doi.org/10.1007/bf02648373) S. P. Garg, N. Krishnamurthy, A. Awasthi, M. Venkatraman, J. Phase Equilib. 1996, 17, 63.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(72)90062-8](https://doi.org/10.1016/0022-5088%2872%2990062-8) H. Jehn, E. Olzi, J. Less-Common Met. 1972, 27, 297.  
_cited as the source of values for this phase_

## O2GAS (O–Ta)

- Id: `phase:o-ta:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:o2gas)

Names (4): _corpus: _corpus:phase:o-ta:o2gas  
_tdb: _tdb:TaO-22Geb.tdb:O2GAS, tdb:TaO-22Mei-ass.tdb:O2GAS, tdb:TaO-22Mei-ion.tdb:O2GAS  


### TDB models of O2GAS (3): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): O2GAS, type code %, sha256 `886665f3a1ed281c…`

~~~~text
61: PHASE O2GAS % 1 1 !
62: CONST O2GAS : O2 :!
~~~~

[TaO-22Mei-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ass.tdb): O2GAS, type code %, sha256 `50b2e3a96e3d3b0a…`

~~~~text
60: PHASE O2GAS % 1 1 !
61: CONST O2GAS : O2 :!
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): O2GAS, type code %, sha256 `88e6b32a58541759…`

~~~~text
66: PHASE O2GAS % 1 1 !
67: CONST O2GAS : O2 :!
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase_

## TA2O5_HT (O–Ta)

- Id: `phase:o-ta:ta2o5-ht`; status `assigned`
- Structure: Ta2O5 · tI44 · I4_1/amd (141); type `st:ta2o5-ti44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: O 0.7143, Ta 0.2857
- Stability: stable in 3 of 3 calculated diagram(s): 1592.88–2169.22 K, x(O) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:ta2o5-ht)

Names (4): _corpus: _corpus:phase:o-ta:ta2o5-ht  
_tdb: _tdb:TaO-22Geb.tdb:TA2O5_HT, tdb:TaO-22Mei-ass.tdb:TA2O5_HT, tdb:TaO-22Mei-ion.tdb:TA2O5_HT  


### TDB models of TA2O5_HT (3): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): TA2O5_HT, type code %, sha256 `886665f3a1ed281c…`

~~~~text
58: PHASE TA2O5_HT % 2 2 5 !
59: CONST TA2O5_HT : TA : O : !
~~~~

[TaO-22Mei-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ass.tdb): TA2O5_HT, type code %, sha256 `50b2e3a96e3d3b0a…`

~~~~text
57: PHASE TA2O5_HT % 2 2 5 !
58: CONST TA2O5_HT : TA : O : !
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): TA2O5_HT, type code %, sha256 `88e6b32a58541759…`

~~~~text
63: PHASE TA2O5_HT % 2 2 5 !
64: CONST TA2O5_HT : TA : O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase_

## TA2O5_LT (O–Ta)

- Id: `phase:o-ta:ta2o5-lt`; status `assigned`
- Structure: Ta2O5 · oP14 · Pccm (49); type `st:ta2o5-op14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: O 0.7143, Ta 0.2857
- Stability: stable in 3 of 3 calculated diagram(s): 300–1593.01 K, x(O) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ta:ta2o5-lt)

Names (4): _corpus: _corpus:phase:o-ta:ta2o5-lt  
_tdb: _tdb:TaO-22Geb.tdb:TA2O5_LT, tdb:TaO-22Mei-ass.tdb:TA2O5_LT, tdb:TaO-22Mei-ion.tdb:TA2O5_LT  


### TDB models of TA2O5_LT (3): PHASE and CONSTITUENT statements as written

[TaO-22Geb.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Geb.tdb): TA2O5_LT, type code %, sha256 `886665f3a1ed281c…`

~~~~text
53: PHASE TA2O5_LT % 2 2 5 !
54: CONST TA2O5_LT : TA : O : !
~~~~

[TaO-22Mei-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ass.tdb): TA2O5_LT, type code %, sha256 `50b2e3a96e3d3b0a…`

~~~~text
52: PHASE TA2O5_LT % 2 2 5 !
53: CONST TA2O5_LT : TA : O : !
~~~~

[TaO-22Mei-ion.tdb](https://orchid-project.org/data/databases/sgte-binary/TaO-22Mei-ion.tdb): TA2O5_LT, type code %, sha256 `88e6b32a58541759…`

~~~~text
58: PHASE TA2O5_LT % 2 2 5 !
59: CONST TA2O5_LT : TA : O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.202200162](https://doi.org/10.1002/adem.202200162) Julian Gebauer, Peter Franke, Hans Jürgen Seifert, Thermodynamic Evaluation of the system Ta–O and Preliminary Assessment of the Systems Al–Nb–O and Al–Ta–O, Adv Eng Mater 24 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102391](https://doi.org/10.1016/j.calphad.2022.102391) Kevin J. Meisner, Rahim Zaman, Bi-Cheng Zhou, Thermodynamic modeling of the Ta-O system, Calphad 76, 102391 (2022).  
_assessment that models this phase_

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
