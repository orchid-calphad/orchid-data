# O–Pu phases

> O–Pu system: 14 phases (tier A 6, liquid 2, gas 2, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-PU.html · Markdown: https://data.orchid-project.org/phases/pages/O-PU.md

14 phases (tier A 6, liquid 2, gas 2, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-PU) · [full JSON](https://data.orchid-project.org/phases/systems/O-PU.json) · [O–Pu system page](https://data.orchid-project.org/systems/O-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Pu system (14)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-o-pu-a6-tetragonal); _phase:o-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 3 | 3 |
| [BCC_A2](#phase-o-pu-bcc-a2); _phase:o-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 3 calculated diagram(s): 912–913 K, x(O) 0–0 | 2 | 3 |
| [FCC_A1](#phase-o-pu-fcc-a1); _phase:o-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-o-pu-gas); _phase:o-pu:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300.29–4000 K, x(O) 1e-05–1 | 3 | 3 |
| [ION](#phase-o-pu-ion); _phase:o-pu:ion_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 912–4000 K, x(O) 0–0.6682 | 0 | 3 |
| [LIQUID](#phase-o-pu-liquid); _phase:o-pu:liquid_ | liquid | liquid | not stable in 3 calculated diagram(s) | 19 | 3 |
| [O2GAS](#phase-o-pu-o2gas); _phase:o-pu:o2gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300–1185 K, x(O) 1–1 | 0 | 3 |
| [ALPHA_PU](#phase-o-pu-pu-alpha); _phase:o-pu:pu-alpha_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–405 K, x(O) 0–0 | 1 | 3 |
| [BETA_PU](#phase-o-pu-pu-beta); _phase:o-pu:pu-beta_ |  | needs_review | stable in 1 of 3 calculated diagram(s): 397.62–462.62 K, x(O) 0–0 | 2 | 3 |
| [GAMMA_PU](#phase-o-pu-pu-gamma); _phase:o-pu:pu-gamma_ |  | needs_review | not stable in 3 calculated diagram(s) | 2 | 3 |
| [PU2O3_D52](#phase-o-pu-pu2o3-d52); _phase:o-pu:pu2o3-d52_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–462.62 K, x(O) 0.6–0.6 | 33 | 3 |
| [PUO152_D53](#phase-o-pu-puo152-d53); _phase:o-pu:puo152-d53_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–737.47 K, x(O) 0.60317–0.60317 | 11 | 3 |
| [PUO161_D53](#phase-o-pu-puo161-d53); _phase:o-pu:puo161-d53_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 572.47–1444.76 K, x(O) 0.61717–0.63212 | 21 | 3 |
| [PUO2_C1](#phase-o-pu-puo2-c1); _phase:o-pu:puo2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3043.58 K, x(O) 0.62007–0.66667 | 38 | 3 |

## TETRAGONAL_A6 (O–Pu)

- Id: `phase:o-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:a6-tetragonal)

Names (6): _corpus: _corpus:phase:o-pu:a6-tetragonal  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:δ-Pu, paper:10.1016/j.jnucmat.2008.06.013:δ′-Pu  
_tdb: _tdb:PuO-08Gue.tdb:TETRAGONAL_A6, tdb:PuO-11Gue.tdb:TETRAGONAL_A6, tdb:PuO-23Fou.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): TETRAGONAL_A6, type code %, sha256 `8750a98340781a5d…`

~~~~text
54: PHASE TETRAGONAL_A6 % 1 1 !
55: CONST TETRAGONAL_A6 : PU : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): TETRAGONAL_A6, type code %, sha256 `15a7df38baf15590…`

~~~~text
60: PHASE TETRAGONAL_A6 % 1 1 !
61: CONST TETRAGONAL_A6 : PU : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): TETRAGONAL_A6, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
66: PHASE TETRAGONAL_A6 % 1 1 !
67: CONST TETRAGONAL_A6 : PU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## BCC_A2 (O–Pu)

- Id: `phase:o-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 3 calculated diagram(s): 912–913 K, x(O) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:bcc-a2)

Names (5): _corpus: _corpus:phase:o-pu:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:ε-Pu  
_tdb: _tdb:PuO-08Gue.tdb:BCC_A2, tdb:PuO-11Gue.tdb:BCC_A2, tdb:PuO-23Fou.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): BCC_A2, type code %B, sha256 `8750a98340781a5d…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : PU : VA : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): BCC_A2, type code %B, sha256 `15a7df38baf15590…`

~~~~text
55: PHASE BCC_A2 %B 2 1 3 !
56: CONST BCC_A2 : PU : VA : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): BCC_A2, type code %B, sha256 `fa82e84a7efa7216…`

~~~~text
61: PHASE BCC_A2 %B 2 1 3 !
62: CONST BCC_A2 : PU : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## FCC_A1 (O–Pu)

- Id: `phase:o-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:fcc-a1)

Names (4): _corpus: _corpus:phase:o-pu:fcc-a1  
_tdb: _tdb:PuO-08Gue.tdb:FCC_A1, tdb:PuO-11Gue.tdb:FCC_A1, tdb:PuO-23Fou.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): FCC_A1, type code %A, sha256 `8750a98340781a5d…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : PU : VA : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): FCC_A1, type code %A, sha256 `15a7df38baf15590…`

~~~~text
50: PHASE FCC_A1 %A 2 1 1 !
51: CONST FCC_A1 : PU : O VA% : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): FCC_A1, type code %A, sha256 `fa82e84a7efa7216…`

~~~~text
56: PHASE FCC_A1 %A 2 1 1 !
57: CONST FCC_A1 : PU : O VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## GAS (O–Pu)

- Id: `phase:o-pu:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300.29–4000 K, x(O) 1e-05–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:gas)

Names (5): _corpus: _corpus:phase:o-pu:gas  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:G  
_tdb: _tdb:PuO-08Gue.tdb:GAS, tdb:PuO-11Gue.tdb:GAS, tdb:PuO-23Fou.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): GAS, type code %, sha256 `8750a98340781a5d…`

~~~~text
95: PHASE GAS:G % 1 1 !
96: CONST GAS:G : O O2 O3 PU PUO PUO2 : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): GAS, type code %, sha256 `15a7df38baf15590…`

~~~~text
101: PHASE GAS:G % 1 1 !
102: CONST GAS:G : O O2 O3 PU PUO PUO2 : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): GAS, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
107: PHASE GAS:G % 1 1 !
108: CONST GAS:G : O O2 O3 PU PUO PUO2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## ION (O–Pu)

- Id: `phase:o-pu:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 912–4000 K, x(O) 0–0.6682
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:ion)

Names (4): _corpus: _corpus:phase:o-pu:ion  
_tdb: _tdb:PuO-08Gue.tdb:ION, tdb:PuO-11Gue.tdb:ION, tdb:PuO-23Fou.tdb:ION  


### TDB models of ION (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): ION, type code %, sha256 `8750a98340781a5d…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : PU+3 : O-2 VA O PUO2 : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): ION, type code %, sha256 `15a7df38baf15590…`

~~~~text
42: PHASE ION:Y % 2 1 1 !
43: CONST ION:Y : PU+3 : O-2 VA O PUO2 : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): ION, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
48: PHASE ION:Y % 2 1 1 !
49: CONST ION:Y : PU+3 : O-2 VA O PUO2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## LIQUID (O–Pu)

- Id: `phase:o-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Pu 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:liquid)

Names (6): _corpus: _corpus:phase:o-pu:liquid  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:L, paper:10.1016/j.jnucmat.2008.06.013:L2  
_tdb: _tdb:PuO-08Gue.tdb:LIQUID, tdb:PuO-11Gue.tdb:LIQUID, tdb:PuO-23Fou.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): LIQUID, type code %, sha256 `8750a98340781a5d…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : PU : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): LIQUID, type code %, sha256 `15a7df38baf15590…`

~~~~text
45: PHASE LIQUID:L % 1 1 !
46: CONST LIQUID:L : PU : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): LIQUID, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
51: PHASE LIQUID:L % 1 1 !
52: CONST LIQUID:L : PU : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1007/bf02841705](https://doi.org/10.1007/bf02841705) H. A. Wriedt, The O-Pu (Oxygen-Plutonium) system, Bulletin of Alloy Phase Diagrams 11, 184-202 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(64)90132-1](https://doi.org/10.1016/0022-3115%2864%2990132-1) T.D. Chikalla, C.E. McNeilly, R.E. Skavdahl, The plutonium-oxygen system, Journal of Nuclear Materials 12, 131-141 (1964).  
_cited as the source of values for this phase_

## O2GAS (O–Pu)

- Id: `phase:o-pu:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1185 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:o2gas)

Names (4): _corpus: _corpus:phase:o-pu:o2gas  
_tdb: _tdb:PuO-08Gue.tdb:O2GAS, tdb:PuO-11Gue.tdb:O2GAS, tdb:PuO-23Fou.tdb:O2GAS  


### TDB models of O2GAS (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): O2GAS, type code %, sha256 `8750a98340781a5d…`

~~~~text
92: PHASE O2GAS % 1 1 !
93: CONST O2GAS : O2 :!
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): O2GAS, type code %, sha256 `15a7df38baf15590…`

~~~~text
98: PHASE O2GAS % 1 1 !
99: CONST O2GAS : O2 :!
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): O2GAS, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
104: PHASE O2GAS % 1 1 !
105: CONST O2GAS : O2 :!
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## ALPHA_PU (O–Pu)

- Id: `phase:o-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): alpha-Pu · mP16 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuO-08Gue.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuO-11Gue.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuO-23Fou.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–405 K, x(O) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:pu-alpha)

Names (5): _corpus: _corpus:phase:o-pu:pu-alpha  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:α-Pu  
_tdb: _tdb:PuO-08Gue.tdb:ALPHA_PU, tdb:PuO-11Gue.tdb:ALPHA_PU, tdb:PuO-23Fou.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): ALPHA_PU, type code %, sha256 `8750a98340781a5d…`

~~~~text
59: PHASE ALPHA_PU % 1 1 !
60: CONST ALPHA_PU : PU : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): ALPHA_PU, type code %, sha256 `15a7df38baf15590…`

~~~~text
65: PHASE ALPHA_PU % 1 1 !
66: CONST ALPHA_PU : PU : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): ALPHA_PU, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
71: PHASE ALPHA_PU % 1 1 !
72: CONST ALPHA_PU : PU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## BETA_PU (O–Pu)

- Id: `phase:o-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): beta-Pu · mC34 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuO-08Gue.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuO-11Gue.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuO-23Fou.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 3 calculated diagram(s): 397.62–462.62 K, x(O) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:pu-beta)

Names (5): _corpus: _corpus:phase:o-pu:pu-beta  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:β-Pu  
_tdb: _tdb:PuO-08Gue.tdb:BETA_PU, tdb:PuO-11Gue.tdb:BETA_PU, tdb:PuO-23Fou.tdb:BETA_PU  


### TDB models of BETA_PU (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): BETA_PU, type code %, sha256 `8750a98340781a5d…`

~~~~text
64: PHASE BETA_PU % 1 1 !
65: CONST BETA_PU : PU : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): BETA_PU, type code %, sha256 `15a7df38baf15590…`

~~~~text
70: PHASE BETA_PU % 1 1 !
71: CONST BETA_PU : PU : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): BETA_PU, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
76: PHASE BETA_PU % 1 1 !
77: CONST BETA_PU : PU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## GAMMA_PU (O–Pu)

- Id: `phase:o-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): gamma-Pu · oF8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuO-08Gue.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuO-11Gue.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuO-23Fou.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stoichiometry: Pu 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:pu-gamma)

Names (5): _corpus: _corpus:phase:o-pu:pu-gamma  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:γ-Pu  
_tdb: _tdb:PuO-08Gue.tdb:GAMMA_PU, tdb:PuO-11Gue.tdb:GAMMA_PU, tdb:PuO-23Fou.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): GAMMA_PU, type code %, sha256 `8750a98340781a5d…`

~~~~text
69: PHASE GAMMA_PU % 1 1 !
70: CONST GAMMA_PU : PU : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): GAMMA_PU, type code %, sha256 `15a7df38baf15590…`

~~~~text
75: PHASE GAMMA_PU % 1 1 !
76: CONST GAMMA_PU : PU : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): GAMMA_PU, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
81: PHASE GAMMA_PU % 1 1 !
82: CONST GAMMA_PU : PU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## PU2O3_D52 (O–Pu)

- Id: `phase:o-pu:pu2o3-d52`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–462.62 K, x(O) 0.6–0.6
- Literature: 33 values (33 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:pu2o3-d52)

Names (5): _corpus: _corpus:phase:o-pu:pu2o3-d52  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:Pu2O3  
_tdb: _tdb:PuO-08Gue.tdb:PU2O3_D52, tdb:PuO-11Gue.tdb:PU2O3_D52, tdb:PuO-23Fou.tdb:PU2O3_D52  


### TDB models of PU2O3_D52 (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): PU2O3_D52, type code %, sha256 `8750a98340781a5d…`

~~~~text
74: PHASE PU2O3_D52:I % 2 2 3 !
75: CONST PU2O3_D52:I : PU+3 : O-2 : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): PU2O3_D52, type code %, sha256 `15a7df38baf15590…`

~~~~text
80: PHASE PU2O3_D52:I % 2 2 3 !
81: CONST PU2O3_D52:I : PU+3 : O-2 : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): PU2O3_D52, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
86: PHASE PU2O3_D52:I % 2 2 3 !
87: CONST PU2O3_D52:I : PU+3 : O-2 : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1007/bf02841705](https://doi.org/10.1007/bf02841705) H. A. Wriedt, The O-Pu (Oxygen-Plutonium) system, Bulletin of Alloy Phase Diagrams 11, 184-202 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0021-9614(77)90040-4](https://doi.org/10.1016/0021-9614%2877%2990040-4) Pierre Chereau, Guy Déan, Michel De Franco, Paul Gerdanian, High-temperature microcalorimetric measurements of partial molar enthalpy of solution, ΔH(O2), in plutonium + oxygen, The Journal of Chemical Thermodynamics 9, 211-219 (1977).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(87)90289-3](https://doi.org/10.1016/0022-3115%2887%2990289-3) T.M. Besmann, Phase equilibria and thermodynamics of the Pu-O system: 1400 K to 1610 K, Journal of Nuclear Materials 144, 141-150 (1987).  
_cited as the source of values for this phase_
- [doi:10.1063/1.441691](https://doi.org/10.1063/1.441691) Howard E. Flotow, Marvin Tetenbaum, Heat capacity and thermodynamic functions of β-242Pu2O3 from 8 to 350 K. Contributions to the excess entropy, The Journal of Chemical Physics 74, 5269-5277 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-1902(65)80259-7](https://doi.org/10.1016/0022-1902%2865%2980259-7) E.R. Gardner, T.L. Markin, R.S. Street, The plutonium-oxygen phase diagram, Journal of Inorganic and Nuclear Chemistry 27, 541-551 (1965).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(64)90132-1](https://doi.org/10.1016/0022-3115%2864%2990132-1) T.D. Chikalla, C.E. McNeilly, R.E. Skavdahl, The plutonium-oxygen system, Journal of Nuclear Materials 12, 131-141 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(76)90114-8](https://doi.org/10.1016/0022-3115%2876%2990114-8) Jean-Claude Boivineau, Etude par rayons x du diagramme plutonium-oxygene de la temperature ambiante jusqu'a 1100°c, Journal of Nuclear Materials 60, 31-38 (1976).  
_cited as the source of values for this phase_

## PUO152_D53 (O–Pu)

- Id: `phase:o-pu:puo152-d53`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D5_3; stoichiometry_contradicts_D5_3:PuO-08Gue.tdb; stoichiometry_contradicts_D5_3:PuO-11Gue.tdb; stoichiometry_contradicts_D5_3:PuO-23Fou.tdb
- Candidate (literature_printed): Mn2O3 · cI80 — printed with a label mapped to this phase
- Candidate (name_token): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Strukturbericht/word 'D53' in the TDB name
- Candidate (sgte_mmc2): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Hallstedt 2025 mmc2 row for PUO152_D53: PuO1.52
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3 — PuO-08Gue.tdb: 'Prototype Mn2O3 (cI80, Ia-3)'
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3 — PuO-11Gue.tdb: 'Prototype Mn2O3 (cI80, Ia-3)'
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3 — PuO-23Fou.tdb: 'Prototype Mn2O3 (cI80, Ia-3)'
- Stoichiometry: O 0.6032, Pu 0.3968
- Stability: stable in 3 of 3 calculated diagram(s): 300–737.47 K, x(O) 0.60317–0.60317
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:puo152-d53)

Names (5): _corpus: _corpus:phase:o-pu:puo152-d53  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:PuO1.52  
_tdb: _tdb:PuO-08Gue.tdb:PUO152_D53, tdb:PuO-11Gue.tdb:PUO152_D53, tdb:PuO-23Fou.tdb:PUO152_D53  


### TDB models of PUO152_D53 (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): PUO152_D53, type code %, sha256 `8750a98340781a5d…`

~~~~text
79: PHASE PUO152_D53 % 2 1 1.52 !
80: CONST PUO152_D53 : PU : O : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): PUO152_D53, type code %, sha256 `15a7df38baf15590…`

~~~~text
85: PHASE PUO152_D53 % 2 1 1.52 !
86: CONST PUO152_D53 : PU : O : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): PUO152_D53, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
91: PHASE PUO152_D53 % 2 1 1.52 !
92: CONST PUO152_D53 : PU : O : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1007/bf02841705](https://doi.org/10.1007/bf02841705) H. A. Wriedt, The O-Pu (Oxygen-Plutonium) system, Bulletin of Alloy Phase Diagrams 11, 184-202 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-1902(65)80259-7](https://doi.org/10.1016/0022-1902%2865%2980259-7) E.R. Gardner, T.L. Markin, R.S. Street, The plutonium-oxygen phase diagram, Journal of Inorganic and Nuclear Chemistry 27, 541-551 (1965).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(76)90114-8](https://doi.org/10.1016/0022-3115%2876%2990114-8) Jean-Claude Boivineau, Etude par rayons x du diagramme plutonium-oxygene de la temperature ambiante jusqu'a 1100°c, Journal of Nuclear Materials 60, 31-38 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(64)90132-1](https://doi.org/10.1016/0022-3115%2864%2990132-1) T.D. Chikalla, C.E. McNeilly, R.E. Skavdahl, The plutonium-oxygen system, Journal of Nuclear Materials 12, 131-141 (1964).  
_cited as the source of values for this phase_

## PUO161_D53 (O–Pu)

- Id: `phase:o-pu:puo161-d53`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 572.47–1444.76 K, x(O) 0.61717–0.63212
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:puo161-d53)

Names (5): _corpus: _corpus:phase:o-pu:puo161-d53  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:PuO1.61  
_tdb: _tdb:PuO-08Gue.tdb:PUO161_D53, tdb:PuO-11Gue.tdb:PUO161_D53, tdb:PuO-23Fou.tdb:PUO161_D53  


### TDB models of PUO161_D53 (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): PUO161_D53, type code %, sha256 `8750a98340781a5d…`

~~~~text
84: PHASE PUO161_D53:I % 3 2 3 1 !
85: CONST PUO161_D53:I : PU+3 PU+4 : O-2 : O-2 VA : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): PUO161_D53, type code %, sha256 `15a7df38baf15590…`

~~~~text
90: PHASE PUO161_D53:I % 3 2 3 1 !
91: CONST PUO161_D53:I : PU+3 PU+4 : O-2 : O-2 VA : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): PUO161_D53, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
96: PHASE PUO161_D53:I % 3 2 3 1 !
97: CONST PUO161_D53:I : PU+3 PU+4 : O-2 : O-2 VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1007/bf02841705](https://doi.org/10.1007/bf02841705) H. A. Wriedt, The O-Pu (Oxygen-Plutonium) system, Bulletin of Alloy Phase Diagrams 11, 184-202 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(76)90114-8](https://doi.org/10.1016/0022-3115%2876%2990114-8) Jean-Claude Boivineau, Etude par rayons x du diagramme plutonium-oxygene de la temperature ambiante jusqu'a 1100°c, Journal of Nuclear Materials 60, 31-38 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-1902(65)80259-7](https://doi.org/10.1016/0022-1902%2865%2980259-7) E.R. Gardner, T.L. Markin, R.S. Street, The plutonium-oxygen phase diagram, Journal of Inorganic and Nuclear Chemistry 27, 541-551 (1965).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(87)90289-3](https://doi.org/10.1016/0022-3115%2887%2990289-3) T.M. Besmann, Phase equilibria and thermodynamics of the Pu-O system: 1400 K to 1610 K, Journal of Nuclear Materials 144, 141-150 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(64)90132-1](https://doi.org/10.1016/0022-3115%2864%2990132-1) T.D. Chikalla, C.E. McNeilly, R.E. Skavdahl, The plutonium-oxygen system, Journal of Nuclear Materials 12, 131-141 (1964).  
_cited as the source of values for this phase_

## PUO2_C1 (O–Pu)

- Id: `phase:o-pu:puo2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3043.58 K, x(O) 0.62007–0.66667
- Literature: 38 values (38 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pu:puo2-c1)

Names (7): _corpus: _corpus:phase:o-pu:puo2-c1  
_paper: _paper:10.1016/j.jnucmat.2008.06.013:PuO2, paper:10.1016/j.jnucmat.2008.06.013:PuO2(2), paper:10.1016/j.jnucmat.2008.06.013:PuO2-x  
_tdb: _tdb:PuO-08Gue.tdb:PUO2_C1, tdb:PuO-11Gue.tdb:PUO2_C1, tdb:PuO-23Fou.tdb:PUO2_C1  


### TDB models of PUO2_C1 (3): PHASE and CONSTITUENT statements as written

[PuO-08Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-08Gue.tdb): PUO2_C1, type code %, sha256 `8750a98340781a5d…`

~~~~text
89: PHASE PUO2_C1:I % 2 1 2 !
90: CONST PUO2_C1:I : PU+3 PU+4 : O-2 VA : !
~~~~

[PuO-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-11Gue.tdb): PUO2_C1, type code %, sha256 `15a7df38baf15590…`

~~~~text
95: PHASE PUO2_C1:I % 3 1 2 1 !
96: CONST PUO2_C1:I : PU+3 PU+4 : O-2% VA : O-2 VA% : !
~~~~

[PuO-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuO-23Fou.tdb): PUO2_C1, type code %, sha256 `fa82e84a7efa7216…`

~~~~text
101: PHASE PUO2_C1:I % 3 1 2 1 !
102: CONST PUO2_C1:I : PU+3 PU+4 : O-2% VA : O-2 VA% : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.jnucmat.2008.06.013](https://doi.org/10.1016/j.jnucmat.2008.06.013) Christine Guéneau, Christian Chatillon, Bo Sundman, Thermodynamic modelling of the plutonium–oxygen system, Journal of Nuclear Materials 378, 257-272 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1007/bf02841705](https://doi.org/10.1007/bf02841705) H. A. Wriedt, The O-Pu (Oxygen-Plutonium) system, Bulletin of Alloy Phase Diagrams 11, 184-202 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(64)90132-1](https://doi.org/10.1016/0022-3115%2864%2990132-1) T.D. Chikalla, C.E. McNeilly, R.E. Skavdahl, The plutonium-oxygen system, Journal of Nuclear Materials 12, 131-141 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(76)90114-8](https://doi.org/10.1016/0022-3115%2876%2990114-8) Jean-Claude Boivineau, Etude par rayons x du diagramme plutonium-oxygene de la temperature ambiante jusqu'a 1100°c, Journal of Nuclear Materials 60, 31-38 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(87)90289-3](https://doi.org/10.1016/0022-3115%2887%2990289-3) T.M. Besmann, Phase equilibria and thermodynamics of the Pu-O system: 1400 K to 1610 K, Journal of Nuclear Materials 144, 141-150 (1987).  
_cited as the source of values for this phase_
- [doi:10.1063/1.441691](https://doi.org/10.1063/1.441691) Howard E. Flotow, Marvin Tetenbaum, Heat capacity and thermodynamic functions of β-242Pu2O3 from 8 to 350 K. Contributions to the excess entropy, The Journal of Chemical Physics 74, 5269-5277 (1981).  
_cited as the source of values for this phase_
- [doi:10.1007/bf01489634](https://doi.org/10.1007/bf01489634) M. M. Popov, M. I. Ivanov, Heats of formation of PuO2 AND U3O8, The Soviet Journal of Atomic Energy 2, 439-443 (1957).  
_cited as the source of values for this phase_
- [doi:10.1016/0021-9614(69)90039-1](https://doi.org/10.1016/0021-9614%2869%2990039-1) Gerald K. Johnson, Erven H. Van Deventer, Owen L. Kruger, Ward N. Hubbard, The enthalpies of formation of plutonium dioxide and plutonium mononitride, The Journal of Chemical Thermodynamics 1, 89-98 (1969).  
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
