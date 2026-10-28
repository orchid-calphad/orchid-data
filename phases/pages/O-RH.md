# O–Rh phases

> O–Rh system: 8 phases (tier A 5, liquid 1, gas 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-RH.html · Markdown: https://data.orchid-project.org/phases/pages/O-RH.md

8 phases (tier A 5, liquid 1, gas 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-RH) · [full JSON](https://data.orchid-project.org/phases/systems/O-RH.json) · [O–Rh system page](https://data.orchid-project.org/systems/O-RH.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-RH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Rh system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-rh-bcc-a2); _phase:o-rh:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-o-rh-fcc-a1); _phase:o-rh:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.5 K, x(O) 0–0 | 0 | 2 |
| [GAS](#phase-o-rh-gas); _phase:o-rh:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 1423.78–4002.08 K, x(O) 0.27959–1 | 3 | 2 |
| [HCP_A3](#phase-o-rh-hcp-a3); _phase:o-rh:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-o-rh-ion); _phase:o-rh:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2237–4002.08 K, x(O) 0–1e-05 | 0 | 2 |
| [O2GAS](#phase-o-rh-o2gas); _phase:o-rh:o2gas_ | gas | gas | stable in 1 of 2 calculated diagram(s): 300–375 K, x(O) 1–1 | 0 | 2 |
| [RH2O3_D51](#phase-o-rh-rh2o3-d51); _phase:o-rh:rh2o3-d51_ | alpha-Al2O3 · D5_1 · hR10 · R-3c (167) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1423.78 K, x(O) 0.6–0.6 | 13 | 2 |
| [RHO2_C4](#phase-o-rh-rho2-c4); _phase:o-rh:rho2-c4_ | TiO2 · C4 · tP6 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 300–375 K, x(O) 0.66667–0.66667 | 0 | 2 |

## BCC_A2 (O–Rh)

- Id: `phase:o-rh:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Rh 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:bcc-a2)

Names (3): _corpus: _corpus:phase:o-rh:bcc-a2  
_tdb: _tdb:RhO-18Gos.tdb:BCC_A2, tdb:RhO-22Lau.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): BCC_A2, type code %B, sha256 `bd914914bb3156cf…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : RH : VA : !
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): BCC_A2, type code %B, sha256 `901d58a456a36a21…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : RH : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## FCC_A1 (O–Rh)

- Id: `phase:o-rh:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.5 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:fcc-a1)

Names (3): _corpus: _corpus:phase:o-rh:fcc-a1  
_tdb: _tdb:RhO-18Gos.tdb:FCC_A1, tdb:RhO-22Lau.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): FCC_A1, type code %A, sha256 `bd914914bb3156cf…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : RH : VA : !
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): FCC_A1, type code %A, sha256 `901d58a456a36a21…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : RH : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## GAS (O–Rh)

- Id: `phase:o-rh:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1423.78–4002.08 K, x(O) 0.27959–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:gas)

Names (4): _corpus: _corpus:phase:o-rh:gas  
_paper: _paper:10.1016/j.jnucmat.2017.12.034:Gas  
_tdb: _tdb:RhO-18Gos.tdb:GAS, tdb:RhO-22Lau.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): GAS, type code %, sha256 `bd914914bb3156cf…`

~~~~text
67: PHASE GAS:G % 1 1 !
68: CONST GAS:G : O O2 O3 RH RHO RHO2 : !
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): GAS, type code %, sha256 `901d58a456a36a21…`

~~~~text
68: PHASE GAS:G % 1 1 !
69: CONST GAS:G : O O2 O3 RH RHO RHO2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(68)90070-2](https://doi.org/10.1016/0022-5088%2868%2990070-2) Olaf Muller, Rustum Roy, Formation and stability of the platinum and rhodium oxides at high oxygen pressures and the structures of Pt3O4, β-PtO2 and RhO2, Journal of the Less Common Metals 16, 129-146 (1968).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(76)80009-3](https://doi.org/10.1016/0040-6031%2876%2980009-3) G. Bayer, H.G. Wiedemann, Bildung und thermische stabilität von rhodium-oxiden, Thermochimica Acta 15, 213-226 (1976).  
_cited as the source of values for this phase_

## HCP_A3 (O–Rh)

- Id: `phase:o-rh:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Rh 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:hcp-a3)

Names (3): _corpus: _corpus:phase:o-rh:hcp-a3  
_tdb: _tdb:RhO-18Gos.tdb:HCP_A3, tdb:RhO-22Lau.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): HCP_A3, type code %A, sha256 `bd914914bb3156cf…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : RH : VA : !
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): HCP_A3, type code %A, sha256 `901d58a456a36a21…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : RH : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## ION (O–Rh)

- Id: `phase:o-rh:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2237–4002.08 K, x(O) 0–1e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:ion)

Names (3): _corpus: _corpus:phase:o-rh:ion  
_tdb: _tdb:RhO-18Gos.tdb:ION, tdb:RhO-22Lau.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): ION, type code %, sha256 `bd914914bb3156cf…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : RH+3 : O-2 VA : !
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): ION, type code %, sha256 `901d58a456a36a21…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : RH+3 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## O2GAS (O–Rh)

- Id: `phase:o-rh:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–375 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:o2gas)

Names (3): _corpus: _corpus:phase:o-rh:o2gas  
_tdb: _tdb:RhO-18Gos.tdb:O2GAS, tdb:RhO-22Lau.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): O2GAS, type code %, sha256 `bd914914bb3156cf…`

~~~~text
64: PHASE O2GAS % 1 1 !
65: CONST O2GAS : O2 :!
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): O2GAS, type code %, sha256 `901d58a456a36a21…`

~~~~text
65: PHASE O2GAS % 1 1 !
66: CONST O2GAS : O2 :!
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## RH2O3_D51 (O–Rh)

- Id: `phase:o-rh:rh2o3-d51`; status `assigned`
- Structure: alpha-Al2O3 · D5_1 · hR10 · R-3c (167); type `st:d5-1-alpha-al2o3-hr10`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1423.78 K, x(O) 0.6–0.6
- Literature: 13 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:rh2o3-d51)

Names (4): _corpus: _corpus:phase:o-rh:rh2o3-d51  
_paper: _paper:10.1016/j.jnucmat.2017.12.034:Rh2O3  
_tdb: _tdb:RhO-18Gos.tdb:RH2O3_D51, tdb:RhO-22Lau.tdb:RH2O3_D51  


### TDB models of RH2O3_D51 (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): RH2O3_D51, type code %, sha256 `bd914914bb3156cf…`

~~~~text
56: PHASE RH2O3_D51:I % 2 2 3 !
57: CONST RH2O3_D51:I : RH+3 : O-2 : !
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): RH2O3_D51, type code %, sha256 `901d58a456a36a21…`

~~~~text
57: PHASE RH2O3_D51:I % 2 2 3 !
58: CONST RH2O3_D51:I : RH+3 : O-2 : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/s0016-7037(97)00209-3](https://doi.org/10.1016/s0016-7037%2897%2900209-3) Johan Nell, Hugh ST.C. O'Neill, The Gibbs free energy of formation and heat capacity of β-Rh2O3 and MgRh2O4, the MgORhO phase diagram, and constraints on the stability of Mg2Rh 4+O4, Geochimica et Cosmochimica Acta 61, 4159-4171 (1997).  
_cited as the source of values for this phase_
- [doi:10.1524/zpch.1969.67.4_6.277](https://doi.org/10.1524/zpch.1969.67.4_6.277) H. Kleykamp, Freie Bildungsenthalpie von Rhodiumsesquioxid\*, Zeitschrift für Physikalische Chemie 67, 277-283 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02665468](https://doi.org/10.1007/bf02665468) K. T. Jacob, M. V. Sriram, Phase relations and gibbs energies in the system Mn-Rh-O, Metall Mater Trans A 25, 1347-1357 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(85)90079-7](https://doi.org/10.1016/0022-5088%2885%2990079-7) C Mallika, O.M Sreedharan, M.S Chandrasekharaiah, Determination of the standard Gibbs energy of formation of Rh2O3(s) and IrO2(s) from solid oxide electrolyte electromotive force measurements, Journal of the Less Common Metals 107, 203-212 (1985).  
_cited as the source of values for this phase_
- [doi:10.1515/htmp.2000.19.1.11](https://doi.org/10.1515/htmp.2000.19.1.11) Κ. T. Jacob,, T. Uda,, Τ. H. Okabe,, Y. Waseda,, The Standard Enthalpy and Entropy of Formation of Rh2O3 - A Third-Law Optimization, High Temperature Materials and Processes 19, 11-16 (2000).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(76)80009-3](https://doi.org/10.1016/0040-6031%2876%2980009-3) G. Bayer, H.G. Wiedemann, Bildung und thermische stabilität von rhodium-oxiden, Thermochimica Acta 15, 213-226 (1976).  
_cited as the source of values for this phase_
- [doi:10.1524/zpch.1964.41.1_2.078](https://doi.org/10.1524/zpch.1964.41.1_2.078) Norbert G. Schmahl, Erich Minzl, Die thermische Zersetzung des Rhodium(III)-oxids und deren Beeinflussung durch Legierungsbildung mit Platin und Palladium, Zeitschrift für Physikalische Chemie 41, 78-96 (1964).  
_cited as the source of values for this phase_

## RHO2_C4 (O–Rh)

- Id: `phase:o-rh:rho2-c4`; status `assigned`
- Structure: TiO2 · C4 · tP6 · P4_2/mnm (136); type `st:c4-tio2-tp6`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–375 K, x(O) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-rh:rho2-c4)

Names (3): _corpus: _corpus:phase:o-rh:rho2-c4  
_tdb: _tdb:RhO-18Gos.tdb:RHO2_C4, tdb:RhO-22Lau.tdb:RHO2_C4  


### TDB models of RHO2_C4 (2): PHASE and CONSTITUENT statements as written

[RhO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-18Gos.tdb): RHO2_C4, type code %, sha256 `bd914914bb3156cf…`

~~~~text
61: PHASE RHO2_C4:I % 2 1 2 !
62: CONST RHO2_C4:I : RH+4 : O-2 : !
~~~~

[RhO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/RhO-22Lau.tdb): RHO2_C4, type code %, sha256 `901d58a456a36a21…`

~~~~text
62: PHASE RHO2_C4:I % 2 1 2 !
63: CONST RHO2_C4:I : RH+4 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
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
