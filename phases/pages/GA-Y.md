# Ga–Y phases

> Ga–Y system: 10 phases (tier A 7, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-Y.html · Markdown: https://data.orchid-project.org/phases/pages/GA-Y.md

10 phases (tier A 7, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-Y) · [full JSON](https://data.orchid-project.org/phases/systems/GA-Y.json) · [Ga–Y system page](https://data.orchid-project.org/systems/GA-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Y system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-y-a11-orthorhombic); _phase:ga-y:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Y) 0–0 | 3 | 1 |
| [BCC_A2](#phase-ga-y-bcc-a2); _phase:ga-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1760–1790 K | 3 | 1 |
| [FCC_A1](#phase-ga-y-fcc-a1); _phase:ga-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GA2Y_C32](#phase-ga-y-ga2y-c32); _phase:ga-y:ga2y-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1623.04 K, x(Y) 0.33333–0.33333 | 9 | 1 |
| [GA3Y5_LT](#phase-ga-y-ga3y5); _phase:ga-y:ga3y5_ | Ba5Si3 · tP32 · P4/ncc (130) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1073.42 K, x(Y) 0.625–0.625 | 2 | 1 |
| [GA3Y5_D88](#phase-ga-y-ga3y5-d88); _phase:ga-y:ga3y5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1272.72–1574.14 K, x(Y) 0.625–0.625 | 8 | 1 |
| [GA3Y5_MT](#phase-ga-y-ga3y5-mt); _phase:ga-y:ga3y5-mt_ | Ga3Y5 · mC32 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1073.42–1272.72 K, x(Y) 0.625–0.625 | 4 | 1 |
| [GAY_B33](#phase-ga-y-gay-b33); _phase:ga-y:gay-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1671.58 K, x(Y) 0.5–0.5 | 9 | 1 |
| [HCP_A3](#phase-ga-y-hcp-a3); _phase:ga-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1750 K, x(Y) 1–1 | 10 | 1 |
| [LIQUID](#phase-ga-y-liquid); _phase:ga-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.32–2500 K, x(Y) 0–1 | 21 | 1 |

## ORTHORHOMBIC_A11 (Ga–Y)

- Id: `phase:ga-y:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Y) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:a11-orthorhombic)

Names (4): _corpus: _corpus:phase:ga-y:a11-orthorhombic, corpus:phase:ga-y:orthorhombic-a11  
_paper: _paper:10.1007/s10973-012-2861-x:(Ga)  
_tdb: _tdb:GaY-13Idb.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): ORTHORHOMBIC_A11, type code %, sha256 `cbddd22351605c04…`

~~~~text
48: PHASE ORTHORHOMBIC_A11 % 1 1 !
49: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## BCC_A2 (Ga–Y)

- Id: `phase:ga-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1760–1790 K
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:bcc-a2)

Names (3): _corpus: _corpus:phase:ga-y:bcc-a2  
_paper: _paper:10.1007/s10973-012-2861-x:β(Y)  
_tdb: _tdb:GaY-13Idb.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): BCC_A2, type code %B, sha256 `cbddd22351605c04…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : GA Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## FCC_A1 (Ga–Y)

- Id: `phase:ga-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-y:fcc-a1  
_tdb: _tdb:GaY-13Idb.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): FCC_A1, type code %A, sha256 `cbddd22351605c04…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : GA Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase_

## GA2Y_C32 (Ga–Y)

- Id: `phase:ga-y:ga2y-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacvq and oqmd-30368, space group 191
- Stoichiometry: Ga 0.6667, Y 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1623.04 K, x(Y) 0.33333–0.33333
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:ga2y-c32)

Names (5): _corpus: _corpus:phase:ga-y:ga2y-c32  
_mp: _mp:mp-aaaaacvq  
_oqmd: _oqmd:oqmd-30368  
_paper: _paper:10.1007/s10973-012-2861-x:Ga2Y  
_tdb: _tdb:GaY-13Idb.tdb:GA2Y_C32  


### TDB models of GA2Y_C32 (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): GA2Y_C32, type code %, sha256 `cbddd22351605c04…`

~~~~text
53: PHASE GA2Y_C32 % 2 2 1 !
54: CONST GA2Y_C32 : GA : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GA3Y5_LT (Ga–Y)

- Id: `phase:ga-y:ga3y5`; status `assigned`
- Structure: Ba5Si3 · tP32 · P4/ncc (130); type `st:ba5si3-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.3750, Y 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1073.42 K, x(Y) 0.625–0.625
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:ga3y5)

Names (3): _corpus: _corpus:phase:ga-y:ga3y5  
_paper: _paper:10.1007/s10973-012-2861-x:L_Ga3Y5  
_tdb: _tdb:GaY-13Idb.tdb:GA3Y5_LT  


### TDB models of GA3Y5_LT (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): GA3Y5_LT, type code %, sha256 `cbddd22351605c04…`

~~~~text
63: PHASE GA3Y5_LT % 2 3 5 !
64: CONST GA3Y5_LT : GA : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GA3Y5_D88 (Ga–Y)

- Id: `phase:ga-y:ga3y5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 0.3750, Y 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1272.72–1574.14 K, x(Y) 0.625–0.625
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:ga3y5-d88)

Names (3): _corpus: _corpus:phase:ga-y:ga3y5-d88  
_paper: _paper:10.1007/s10973-012-2861-x:H_Ga3Y5  
_tdb: _tdb:GaY-13Idb.tdb:GA3Y5_D88  


### TDB models of GA3Y5_D88 (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): GA3Y5_D88, type code %, sha256 `cbddd22351605c04…`

~~~~text
73: PHASE GA3Y5_D88 % 2 3 5 !
74: CONST GA3Y5_D88 : GA : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GA3Y5_MT (Ga–Y)

- Id: `phase:ga-y:ga3y5-mt`; status `assigned`
- Structure: Ga3Y5 · mC32 · C2/m (12); type `st:ga3y5-mc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MT, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.3750, Y 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1073.42–1272.72 K, x(Y) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:ga3y5-mt)

Names (3): _corpus: _corpus:phase:ga-y:ga3y5-mt  
_paper: _paper:10.1007/s10973-012-2861-x:M_Ga3Y5  
_tdb: _tdb:GaY-13Idb.tdb:GA3Y5_MT  


### TDB models of GA3Y5_MT (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): GA3Y5_MT, type code %, sha256 `cbddd22351605c04…`

~~~~text
68: PHASE GA3Y5_MT % 2 3 5 !
69: CONST GA3Y5_MT : GA : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GAY_B33 (Ga–Y)

- Id: `phase:ga-y:gay-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqxg and oqmd-30366, space group 63
- Stoichiometry: Ga 0.5000, Y 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1671.58 K, x(Y) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:gay-b33)

Names (5): _corpus: _corpus:phase:ga-y:gay-b33  
_mp: _mp:mp-aaaaaqxg  
_oqmd: _oqmd:oqmd-30366  
_paper: _paper:10.1007/s10973-012-2861-x:GaY  
_tdb: _tdb:GaY-13Idb.tdb:GAY_B33  


### TDB models of GAY_B33 (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): GAY_B33, type code %, sha256 `cbddd22351605c04…`

~~~~text
58: PHASE GAY_B33 % 2 1 1 !
59: CONST GAY_B33 : GA : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## HCP_A3 (Ga–Y)

- Id: `phase:ga-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1750 K, x(Y) 1–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:hcp-a3)

Names (3): _corpus: _corpus:phase:ga-y:hcp-a3  
_paper: _paper:10.1007/s10973-012-2861-x:α(Y)  
_tdb: _tdb:GaY-13Idb.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): HCP_A3, type code %A, sha256 `cbddd22351605c04…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : GA Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## LIQUID (Ga–Y)

- Id: `phase:ga-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.32–2500 K, x(Y) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-y:liquid)

Names (3): _corpus: _corpus:phase:ga-y:liquid  
_paper: _paper:10.1007/s10973-012-2861-x:L  
_tdb: _tdb:GaY-13Idb.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaY-13Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/GaY-13Idb.tdb): LIQUID, type code %, sha256 `cbddd22351605c04…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : GA Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-012-2861-x](https://doi.org/10.1007/s10973-012-2861-x) M. Idbenali, C. Servant, Thermodynamic evaluation of the Ga–Y system, J Therm Anal Calorim 112, 245-253 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
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
