# Nb–O phases

> Nb–O system: 10 phases (tier A 3, tier B 1, tier C 2, liquid 2, gas 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-O.html · Markdown: https://data.orchid-project.org/phases/pages/NB-O.md

10 phases (tier A 3, tier B 1, tier C 2, liquid 2, gas 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-O) · [full JSON](https://data.orchid-project.org/phases/systems/NB-O.json) · [Nb–O system page](https://data.orchid-project.org/systems/NB-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–O system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-o-bcc-a2); _phase:nb-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2749.99 K, x(O) 0–0.09041 | 0 | 2 |
| [FCC_A1](#phase-nb-o-fcc-a1); _phase:nb-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-nb-o-gas); _phase:nb-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 301.19–4000 K, x(O) 0.67471–1 | 0 | 2 |
| [HCP_A3](#phase-nb-o-hcp-a3); _phase:nb-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-nb-o-ion); _phase:nb-o:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1782.33–4000 K, x(O) 1e-05–0.71423 | 0 | 2 |
| [LIQUID](#phase-nb-o-liquid); _phase:nb-o:liquid_ | liquid | liquid | not stable in 2 calculated diagram(s) | 0 | 2 |
| [NB2O5](#phase-nb-o-nb2o5); _phase:nb-o:nb2o5_ | Nb2O5 · mP99 · P2/m (10) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1966.19 K, x(O) 0.71429–0.71429 | 0 | 2 |
| [NBO](#phase-nb-o-nbo); _phase:nb-o:nbo_ | NbO · cP6 · Pm-3m (221) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–2218.25 K, x(O) 0.5–0.5 | 0 | 2 |
| [NBO2](#phase-nb-o-nbo2); _phase:nb-o:nbo2_ | NbO2 · tI96 · I4_1/a (88) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2181.28 K, x(O) 0.66667–0.66667 | 1 | 2 |
| [O2GAS](#phase-nb-o-o2gas); _phase:nb-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1 | 0 | 2 |

## BCC_A2 (Nb–O)

- Id: `phase:nb-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2749.99 K, x(O) 0–0.09041
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:bcc-a2)

Names (3): _corpus: _corpus:phase:nb-o:bcc-a2  
_tdb: _tdb:NbO-07Jer.tdb:BCC_A2, tdb:NbO-97Dup-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): BCC_A2, type code %B, sha256 `30d68ef18e1752dc…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : NB : O VA : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): BCC_A2, type code %B, sha256 `7461691cb95cdbdf…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : NB : O VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## FCC_A1 (Nb–O)

- Id: `phase:nb-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Nb 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:fcc-a1)

Names (3): _corpus: _corpus:phase:nb-o:fcc-a1  
_tdb: _tdb:NbO-07Jer.tdb:FCC_A1, tdb:NbO-97Dup-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): FCC_A1, type code %A, sha256 `30d68ef18e1752dc…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : NB : VA : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): FCC_A1, type code %A, sha256 `7461691cb95cdbdf…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : NB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## GAS (Nb–O)

- Id: `phase:nb-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 301.19–4000 K, x(O) 0.67471–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:gas)

Names (3): _corpus: _corpus:phase:nb-o:gas  
_tdb: _tdb:NbO-07Jer.tdb:GAS, tdb:NbO-97Dup-LB.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): GAS, type code %, sha256 `30d68ef18e1752dc…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : NB NBO NBO2 O O2 O3 : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): GAS, type code %, sha256 `7461691cb95cdbdf…`

~~~~text
76: PHASE GAS:G % 1 1 !
77: CONST GAS:G : NB NBO NBO2 O O2 O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## HCP_A3 (Nb–O)

- Id: `phase:nb-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:hcp-a3)

Names (3): _corpus: _corpus:phase:nb-o:hcp-a3  
_tdb: _tdb:NbO-07Jer.tdb:HCP_A3, tdb:NbO-97Dup-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): HCP_A3, type code %A, sha256 `30d68ef18e1752dc…`

~~~~text
52: PHASE HCP_A3 %A 2 1 1 !
53: CONST HCP_A3 : NB : O VA : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): HCP_A3, type code %A, sha256 `7461691cb95cdbdf…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : NB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## ION (Nb–O)

- Id: `phase:nb-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1782.33–4000 K, x(O) 1e-05–0.71423
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:ion)

Names (3): _corpus: _corpus:phase:nb-o:ion  
_tdb: _tdb:NbO-07Jer.tdb:ION, tdb:NbO-97Dup-LB.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): ION, type code %, sha256 `30d68ef18e1752dc…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : NB+2 : O-2 VA NBO2 NBO5/2 : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): ION, type code %, sha256 `7461691cb95cdbdf…`

~~~~text
40: PHASE ION:Y % 2 1 1 !
41: CONST ION:Y : NB+2 : O-2 VA NBO2 NBO5/2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## LIQUID (Nb–O)

- Id: `phase:nb-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Nb 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:liquid)

Names (3): _corpus: _corpus:phase:nb-o:liquid  
_tdb: _tdb:NbO-07Jer.tdb:LIQUID, tdb:NbO-97Dup-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): LIQUID, type code %, sha256 `30d68ef18e1752dc…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : NB : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): LIQUID, type code %, sha256 `7461691cb95cdbdf…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : NB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## NB2O5 (Nb–O)

- Id: `phase:nb-o:nb2o5`; status `assigned`
- Structure: Nb2O5 · mP99 · P2/m (10); type `st:nb2o5-mp99`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Nb 0.2857, O 0.7143
- Stability: stable in 2 of 2 calculated diagram(s): 300–1966.19 K, x(O) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:nb2o5)

Names (3): _corpus: _corpus:phase:nb-o:nb2o5  
_tdb: _tdb:NbO-07Jer.tdb:NB2O5, tdb:NbO-97Dup-LB.tdb:NB2O5  


### TDB models of NB2O5 (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): NB2O5, type code %, sha256 `30d68ef18e1752dc…`

~~~~text
67: PHASE NB2O5 % 2 2 5 !
68: CONST NB2O5 : NB : O : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): NB2O5, type code %, sha256 `7461691cb95cdbdf…`

~~~~text
70: PHASE NB2O5 % 2 2 5 !
71: CONST NB2O5 : NB : O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## NBO (Nb–O)

- Id: `phase:nb-o:nbo`; status `assigned`
- Structure: NbO · cP6 · Pm-3m (221); type `st:nbo-cp6`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Nb 0.5000, O 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2218.25 K, x(O) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:nbo)

Names (5): _corpus: _corpus:phase:nb-o:nbo  
_mp: _mp:mp-aaaaadkx  
_oqmd: _oqmd:oqmd-2921  
_tdb: _tdb:NbO-07Jer.tdb:NBO, tdb:NbO-97Dup-LB.tdb:NBO  


### TDB models of NBO (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): NBO, type code %, sha256 `30d68ef18e1752dc…`

~~~~text
57: PHASE NBO % 2 1 1 !
58: CONST NBO : NB : O : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): NBO, type code %, sha256 `7461691cb95cdbdf…`

~~~~text
60: PHASE NBO % 2 1 1 !
61: CONST NBO : NB : O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

## NBO2 (Nb–O)

- Id: `phase:nb-o:nbo2`; status `assigned`
- Structure: NbO2 · tI96 · I4_1/a (88); type `st:nbo2-ti96`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Nb 0.3333, O 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–2181.28 K, x(O) 0.66667–0.66667
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:nbo2)

Names (4): _corpus: _corpus:phase:nb-o:nbo2  
_paper: _paper:10.1016/j.jnucmat.2006.10.008:NbO2  
_tdb: _tdb:NbO-07Jer.tdb:NBO2, tdb:NbO-97Dup-LB.tdb:NBO2  


### TDB models of NBO2 (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): NBO2, type code %, sha256 `30d68ef18e1752dc…`

~~~~text
62: PHASE NBO2 % 2 1 2 !
63: CONST NBO2 : NB : O : !
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): NBO2, type code %, sha256 `7461691cb95cdbdf…`

~~~~text
65: PHASE NBO2 % 2 1 2 !
66: CONST NBO2 : NB : O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/physrevb.13.2965](https://doi.org/10.1103/physrevb.13.2965) R. Pynn, J. D. Axe, R. Thomas, Structural distortions in the low-temperature phase of\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">NbO\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>2\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>, Phys. Rev. B 13, 2965-2975 (1976).  
_cited as the source of values for this phase_

## O2GAS (Nb–O)

- Id: `phase:nb-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-o:o2gas)

Names (3): _corpus: _corpus:phase:nb-o:o2gas  
_tdb: _tdb:NbO-07Jer.tdb:O2GAS, tdb:NbO-97Dup-LB.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[NbO-07Jer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb): O2GAS, type code %, sha256 `30d68ef18e1752dc…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 :!
~~~~

[NbO-97Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb): O2GAS, type code %, sha256 `7461691cb95cdbdf…`

~~~~text
73: PHASE O2GAS % 1 1 !
74: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007).  
_assessment that models this phase_

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
