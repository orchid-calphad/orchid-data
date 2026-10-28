# Np–O phases

> Np–O system: 9 phases (tier A 4, tier C 1, liquid 2, gas 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NP-O.html · Markdown: https://data.orchid-project.org/phases/pages/NP-O.md

9 phases (tier A 4, tier C 1, liquid 2, gas 2); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NP-O) · [full JSON](https://data.orchid-project.org/phases/systems/NP-O.json) · [Np–O system page](https://data.orchid-project.org/systems/NP-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/NP-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Np–O system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAG_AD](#phase-np-o-ad-tetrag); _phase:np-o:ad-tetrag_ | beta-Np · A_d · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 555.03–855.95 K, x(O) 0–0 | 0 | 1 |
| [BCC_A2](#phase-np-o-bcc-a2); _phase:np-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 855.95–916.84 K, x(O) 0–0 | 1 | 1 |
| [GAS](#phase-np-o-gas); _phase:np-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 301.03–2500 K, x(O) 0.99993–1 | 2 | 1 |
| [ION](#phase-np-o-ion); _phase:np-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 916.84–2500 K, x(O) 0–0.61213 | 0 | 1 |
| [LIQUID](#phase-np-o-liquid); _phase:np-o:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 6 | 1 |
| [NP2O5](#phase-np-o-np2o5); _phase:np-o:np2o5_ | Np2O5 · mP28 · P2/c (13) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–702.28 K, x(O) 0.71429–0.71429 | 11 | 1 |
| [NPO2_C1](#phase-np-o-npo2-c1); _phase:np-o:npo2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0.65532–0.66667 | 14 | 1 |
| [O2GAS](#phase-np-o-o2gas); _phase:np-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–1187.28 K, x(O) 1–1 | 0 | 1 |
| [ORTHO_AC](#phase-np-o-ortho-ac); _phase:np-o:ortho-ac_ | alpha-Np · A_c · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–555.03 K, x(O) 0–0 | 3 | 1 |

## TETRAG_AD (Np–O)

- Id: `phase:np-o:ad-tetrag`; status `assigned`
- Structure: beta-Np · A_d · tP4 · P4/nmm (129); type `st:a-d-beta-np-tp4`; tier A: standard phase name; confidence high
- Stoichiometry: Np 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 555.03–855.95 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:ad-tetrag)

Names (2): _corpus: _corpus:phase:np-o:ad-tetrag  
_tdb: _tdb:NpO-16Smi.tdb:TETRAG_AD  


### TDB models of TETRAG_AD (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): TETRAG_AD, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
57: PHASE TETRAG_AD % 1 1 !
58: CONST TETRAG_AD : NP : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase_

## BCC_A2 (Np–O)

- Id: `phase:np-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Np 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 855.95–916.84 K, x(O) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:bcc-a2)

Names (3): _corpus: _corpus:phase:np-o:bcc-a2  
_paper: _paper:10.1016/j.jct.2016.07.040:γ-Np  
_tdb: _tdb:NpO-16Smi.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): BCC_A2, type code %B, sha256 `f83f0e3f59b5ca95…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : NP : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase; reports values for this phase_

## GAS (Np–O)

- Id: `phase:np-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.03–2500 K, x(O) 0.99993–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:gas)

Names (4): _corpus: _corpus:phase:np-o:gas  
_paper: _paper:10.1016/j.jct.2016.07.040:G, paper:10.1016/j.jct.2016.07.040:gas  
_tdb: _tdb:NpO-16Smi.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): GAS, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : NP NPO NPO2 O O2 O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011).  
_cited as the source of values for this phase_

## ION (Np–O)

- Id: `phase:np-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 916.84–2500 K, x(O) 0–0.61213
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:ion)

Names (2): _corpus: _corpus:phase:np-o:ion  
_tdb: _tdb:NpO-16Smi.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): ION, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
39: PHASE ION:Y % 2 1 1 !
40: CONST ION:Y : NP+4 : O-2 VA O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase_

## LIQUID (Np–O)

- Id: `phase:np-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Np 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:liquid)

Names (5): _corpus: _corpus:phase:np-o:liquid  
_paper: _paper:10.1016/j.jct.2016.07.040:L, paper:10.1016/j.jct.2016.07.040:L1, paper:10.1016/j.jct.2016.07.040:liquid  
_tdb: _tdb:NpO-16Smi.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): LIQUID, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
42: PHASE LIQUID:L % 1 1 !
43: CONST LIQUID:L : NP : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.4721655](https://doi.org/10.1063/1.4721655) R. Böhler, M. J. Welland, F. De Bruycker, K. Boboridis, A. Janssen, R. Eloirdi et al., Revisiting the melting temperature of NpO2 and the challenges associated with high temperature actinide compound measurements, Journal of Applied Physics 111 (2012).  
_cited as the source of values for this phase_
- [doi:10.1063/1.4825256](https://doi.org/10.1063/1.4825256) Rudy J. M. Konings, Ondrej Beneš, Attila Kovács, Dario Manara, David Sedmidubský, Lev Gorokhov et al., The Thermodynamic Properties of the \<i>f\</i>-Elements and their Compounds. Part 2. The Lanthanide and Actinide Oxides, Journal of Physical and Chemical Reference Data 43 (2014).  
_cited as the source of values for this phase_

## NP2O5 (Np–O)

- Id: `phase:np-o:np2o5`; status `assigned`
- Structure: Np2O5 · mP28 · P2/c (13); type `st:np2o5-mp28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Np 0.2857, O 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–702.28 K, x(O) 0.71429–0.71429
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:np2o5)

Names (4): _corpus: _corpus:phase:np-o:np2o5  
_paper: _paper:10.1016/j.jct.2016.07.040:Np2O5, paper:10.1016/j.jct.2016.07.040:Np2O5(cr)  
_tdb: _tdb:NpO-16Smi.tdb:NP2O5  


### TDB models of NP2O5 (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): NP2O5, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
67: PHASE NP2O5 % 2 2 5 !
68: CONST NP2O5 : NP : O : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.4825256](https://doi.org/10.1063/1.4825256) Rudy J. M. Konings, Ondrej Beneš, Attila Kovács, Dario Manara, David Sedmidubský, Lev Gorokhov et al., The Thermodynamic Properties of the \<i>f\</i>-Elements and their Compounds. Part 2. The Lanthanide and Actinide Oxides, Journal of Physical and Chemical Reference Data 43 (2014).  
_cited as the source of values for this phase_
- [doi:10.1524/ract.1994.6667.s1.109](https://doi.org/10.1524/ract.1994.6667.s1.109) L. Merli, J. Fuger, Thermochemistry of a Few Neptunium and Neodymium Oxides and Hydroxides, Radiochimica Acta 66-67, 109-114 (1994).  
_cited as the source of values for this phase_

## NPO2_C1 (Np–O)

- Id: `phase:np-o:npo2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0.65532–0.66667
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:npo2-c1)

Names (7): _corpus: _corpus:phase:np-o:npo2-c1  
_paper: _paper:10.1016/j.jct.2016.07.040:NpO1.90, paper:10.1016/j.jct.2016.07.040:NpO2, paper:10.1016/j.jct.2016.07.040:NpO2(cr), paper:10.1016/j.jct.2016.07.040:NpO2(g), paper:10.1016/j.jct.2016.07.040:NpO2-x  
_tdb: _tdb:NpO-16Smi.tdb:NPO2_C1  


### TDB models of NPO2_C1 (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): NPO2_C1, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
62: PHASE NPO2_C1:I % 2 1 2 !
63: CONST NPO2_C1:I : NP+3 NP+4 : O-2 VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.4825256](https://doi.org/10.1063/1.4825256) Rudy J. M. Konings, Ondrej Beneš, Attila Kovács, Dario Manara, David Sedmidubský, Lev Gorokhov et al., The Thermodynamic Properties of the \<i>f\</i>-Elements and their Compounds. Part 2. The Lanthanide and Actinide Oxides, Journal of Physical and Chemical Reference Data 43 (2014).  
_cited as the source of values for this phase_
- [doi:10.1021/je60039a029](https://doi.org/10.1021/je60039a029) Elmer J. Huber, Charles E. Holley, Enthalpy of formation of neptunium dioxide, J. Chem. Eng. Data 13, 545-546 (1968).  
_cited as the source of values for this phase_
- [doi:10.1063/1.1698923](https://doi.org/10.1063/1.1698923) Edgar F. Westrum, J. B. Hatcher, Darrell W. Osborne, The Entropy and Low Temperature Heat Capacity of Neptunium Dioxide, The Journal of Chemical Physics 21, 419-423 (1953).  
_cited as the source of values for this phase_
- [doi:10.1063/1.4721655](https://doi.org/10.1063/1.4721655) R. Böhler, M. J. Welland, F. De Bruycker, K. Boboridis, A. Janssen, R. Eloirdi et al., Revisiting the melting temperature of NpO2 and the challenges associated with high temperature actinide compound measurements, Journal of Applied Physics 111 (2012).  
_cited as the source of values for this phase_

## O2GAS (Np–O)

- Id: `phase:np-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1187.28 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:o2gas)

Names (2): _corpus: _corpus:phase:np-o:o2gas  
_tdb: _tdb:NpO-16Smi.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): O2GAS, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase_

## ORTHO_AC (Np–O)

- Id: `phase:np-o:ortho-ac`; status `assigned`
- Structure: alpha-Np · A_c · oP8 · Pnma (62); type `st:a-c-alpha-np-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Np 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–555.03 K, x(O) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-o:ortho-ac)

Names (3): _corpus: _corpus:phase:np-o:ortho-ac  
_paper: _paper:10.1016/j.jct.2016.07.040:α-Np(cr)  
_tdb: _tdb:NpO-16Smi.tdb:ORTHO_AC  


### TDB models of ORTHO_AC (1): PHASE and CONSTITUENT statements as written

[NpO-16Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb): ORTHO_AC, type code %, sha256 `f83f0e3f59b5ca95…`

~~~~text
52: PHASE ORTHO_AC % 1 1 !
53: CONST ORTHO_AC : NP : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.3474238](https://doi.org/10.1063/1.3474238) Rudy J. M. Konings, Ondrej Beneš, The Thermodynamic Properties of the f-Elements and Their Compounds. I. The Lanthanide and Actinide Metals, Journal of Physical and Chemical Reference Data 39 (2010).  
_cited as the source of values for this phase_
- [doi:10.1098/rspa.1970.0118](https://doi.org/10.1098/rspa.1970.0118) J. A. Lee, Kurt Alfred Georg Mendelssohn, P. W. Sutcliffe, Specific heats of plutonium and neptunium, Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences 317, 303-317 (1970).  
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
