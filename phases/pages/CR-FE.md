# Cr–Fe phases

> Cr–Fe system: 9 phases (tier A 7, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-FE.html · Markdown: https://data.orchid-project.org/phases/pages/CR-FE.md

9 phases (tier A 7, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-FE) · [full JSON](https://data.orchid-project.org/phases/systems/CR-FE.json) · [Cr–Fe system page](https://data.orchid-project.org/systems/CR-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Fe system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [CHI_A12](#phase-cr-fe-a12-chi); _phase:cr-fe:a12-chi_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-cr-fe-bcc-a2); _phase:cr-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2180.98 K, x(Fe) 0–1 | 10 | 7 |
| [C14_LAVES](#phase-cr-fe-c14-laves); _phase:cr-fe:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [SIGMA_D8B](#phase-cr-fe-d8b-sigma); _phase:cr-fe:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 704.29–1104.5 K, x(Fe) 0.48378–0.57894 | 41 | 7 |
| [FCC_A1](#phase-cr-fe-fcc-a1); _phase:cr-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 7 calculated diagram(s): 1117.16–1671.06 K, x(Fe) 0.87767–1 | 2 | 7 |
| [HCP_A3](#phase-cr-fe-hcp-a3); _phase:cr-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [HIGH_SIGMA](#phase-cr-fe-high-sigma); _phase:cr-fe:high-sigma_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cr-fe-liquid); _phase:cr-fe:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1782.96–4000 K, x(Fe) 0–1 | 3 | 7 |
| [SIGMA_OLD](#phase-cr-fe-old-sigma); _phase:cr-fe:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 786.21–1104.5 K, x(Fe) 0.48601–0.56338 | 0 | 1 |

## CHI_A12 (Cr–Fe)

- Id: `phase:cr-fe:a12-chi`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:a12-chi)

Names (2): _corpus: _corpus:phase:cr-fe:a12-chi  
_tdb: _tdb:CrFe-87And-LB.tdb:CHI_A12  


### TDB models of CHI_A12 (1): PHASE and CONSTITUENT statements as written

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): CHI_A12, type code %, sha256 `aee44c07511fe31f…`

~~~~text
61: PHASE CHI_A12 % 3 24 10 24 !
62: CONST CHI_A12 : CR FE : CR : CR FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_

## BCC_A2 (Cr–Fe)

- Id: `phase:cr-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–2180.98 K, x(Fe) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:bcc-a2)

Names (10): _corpus: _corpus:phase:cr-fe:bcc-a2  
_paper: _paper:10.1016/j.calphad.2017.10.002:BCC, paper:10.1016/j.calphad.2017.10.002:BCC'  
_tdb: _tdb:CrFe-11Xio.tdb:BCC_A2, tdb:CrFe-18Jac.tdb:BCC_A2, tdb:CrFe-20Ost.tdb:BCC_A2, tdb:CrFe-21Laf.tdb:BCC_A2, tdb:CrFe-23Zha.tdb:BCC_A2, tdb:CrFe-82Her.tdb:BCC_A2, tdb:CrFe-87And-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[CrFe-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-11Xio.tdb): BCC_A2, type code %B, sha256 `c6bdc1ced82c0a31…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CR FE : VA : !
~~~~

[CrFe-18Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-18Jac.tdb): BCC_A2, type code %B, sha256 `97353b426c2d299a…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CR FE : VA : !
~~~~

[CrFe-20Ost.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-20Ost.tdb): BCC_A2, type code %B, sha256 `c009125a792bbcf5…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR FE : VA : !
~~~~

[CrFe-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-21Laf.tdb): BCC_A2, type code %B, sha256 `a466cbb58ce8fff8…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR FE : VA : !
~~~~

[CrFe-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-23Zha.tdb): BCC_A2, type code %B, sha256 `093591c8faaf3d7d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR FE : VA : !
~~~~

[CrFe-82Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-82Her.tdb): BCC_A2, type code %B, sha256 `a426ac8fa1a94471…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR FE : VA : !
~~~~

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): BCC_A2, type code %B, sha256 `aee44c07511fe31f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CR FE : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2017.10.002](https://doi.org/10.1016/j.calphad.2017.10.002) Aurélie Jacob, Erwin Povoden-Karadeniz, Ernst Kozeschnik, Revised thermodynamic description of the Fe-Cr system based on an improved sublattice model of the σ phase, Calphad 60, 16-28 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(82)90018-9](https://doi.org/10.1016/0364-5916%2882%2990018-9) Staffan Hertzman, Bo Sundman, A thermodynamic analysis of the fe-cr system, Calphad 6, 67-80 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.05.002](https://doi.org/10.1016/j.calphad.2011.05.002) Wei Xiong, Peter Hedström, Malin Selleby, Joakim Odqvist, Mattias Thuvander, Qing Chen, An improved thermodynamic modeling of the Fe–Cr system down to zero kelvin coupled with key experiments, Calphad 35, 355-366 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2020.156122](https://doi.org/10.1016/j.jallcom.2020.156122) Marlena Ostrowska, Gabriele Cacciamani, Thermodynamic modelling of the σ and μ phases in several ternary systems containing Co, Cr, Fe, Mo, Re and W, Journal of Alloys and Compounds 845, 156122 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2020.152692](https://doi.org/10.1016/j.jnucmat.2020.152692) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Experimental study, first-principles calculation and thermodynamic modelling of the Cr–Fe–Nb–Sn–Zr quinary system for application as cladding materials in nuclear reactors., Journal of Nuclear Materials 544, 152692 (2021).  
_assessment that models this phase_
- [doi:10.1080/10408431003788472](https://doi.org/10.1080/10408431003788472) Wei Xiong, Malin Selleby, Qing Chen, Joakim Odqvist, Yong Du, Phase Equilibria and Thermodynamic Properties in the Fe-Cr System, Critical Reviews in Solid State and Materials Sciences 35, 125-152 (2010).  
_cited as the source of values for this phase_

## C14_LAVES (Cr–Fe)

- Id: `phase:cr-fe:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrFe-87And-LB.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:c14-laves)

Names (2): _corpus: _corpus:phase:cr-fe:c14-laves  
_tdb: _tdb:CrFe-87And-LB.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): C14_LAVES, type code %, sha256 `aee44c07511fe31f…`

~~~~text
66: PHASE C14_LAVES % 2 2 1 !
67: CONST C14_LAVES : CR% FE% : CR FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_

## SIGMA_D8B (Cr–Fe)

- Id: `phase:cr-fe:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrFe-11Xio.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrFe-18Jac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrFe-20Ost.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrFe-21Laf.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrFe-23Zha.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 704.29–1104.5 K, x(Fe) 0.48378–0.57894
- Literature: 41 values (41 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:d8b-sigma)

Names (10): _corpus: _corpus:phase:cr-fe:d8b-sigma, corpus:phase:cr-fe:sigma-d8b  
_paper: _paper:10.1016/j.calphad.2017.10.002:σ  
_tdb: _tdb:CrFe-11Xio.tdb:SIGMA_D8B, tdb:CrFe-18Jac.tdb:SIGMA_D8B, tdb:CrFe-20Ost.tdb:SIGMA_D8B, tdb:CrFe-21Laf.tdb:SIGMA_D8B, tdb:CrFe-23Zha.tdb:SIGMA_D8B, tdb:CrFe-82Her.tdb:SIGMA_D8B, tdb:CrFe-87And-LB.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (7): PHASE and CONSTITUENT statements as written

[CrFe-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-11Xio.tdb): SIGMA_D8B, type code %, sha256 `c6bdc1ced82c0a31…`

~~~~text
42: PHASE SIGMA_D8B % 2 10 20 !
43: CONST SIGMA_D8B : CR FE : CR FE : !
~~~~

[CrFe-18Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-18Jac.tdb): SIGMA_D8B, type code %, sha256 `97353b426c2d299a…`

~~~~text
39: PHASE SIGMA_D8B % 3 10 4 16 !
40: CONST SIGMA_D8B : CR FE : CR FE : CR FE : !
~~~~

[CrFe-20Ost.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-20Ost.tdb): SIGMA_D8B, type code %, sha256 `c009125a792bbcf5…`

~~~~text
42: PHASE SIGMA_D8B % 3 10 4 16 !
43: CONST SIGMA_D8B : CR FE : CR FE : CR FE : !
~~~~

[CrFe-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-21Laf.tdb): SIGMA_D8B, type code %, sha256 `a466cbb58ce8fff8…`

~~~~text
42: PHASE SIGMA_D8B % 2 10 20 !
43: CONST SIGMA_D8B : CR FE : CR FE : !
~~~~

[CrFe-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-23Zha.tdb): SIGMA_D8B, type code %, sha256 `093591c8faaf3d7d…`

~~~~text
45: PHASE SIGMA_D8B % 3 10 4 16 !
46: CONST SIGMA_D8B : CR FE : CR FE : CR FE : !
~~~~

[CrFe-82Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-82Her.tdb): SIGMA_D8B, type code %, sha256 `a426ac8fa1a94471…`

~~~~text
41: PHASE SIGMA_D8B % 3 10 4 16 !
42: CONST SIGMA_D8B : FE : CR : CR FE : !
~~~~

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): SIGMA_D8B, type code %, sha256 `aee44c07511fe31f…`

~~~~text
46: PHASE SIGMA_D8B % 3 10 4 16 !
47: CONST SIGMA_D8B : FE : CR : CR FE : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2017.10.002](https://doi.org/10.1016/j.calphad.2017.10.002) Aurélie Jacob, Erwin Povoden-Karadeniz, Ernst Kozeschnik, Revised thermodynamic description of the Fe-Cr system based on an improved sublattice model of the σ phase, Calphad 60, 16-28 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(82)90018-9](https://doi.org/10.1016/0364-5916%2882%2990018-9) Staffan Hertzman, Bo Sundman, A thermodynamic analysis of the fe-cr system, Calphad 6, 67-80 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.05.002](https://doi.org/10.1016/j.calphad.2011.05.002) Wei Xiong, Peter Hedström, Malin Selleby, Joakim Odqvist, Mattias Thuvander, Qing Chen, An improved thermodynamic modeling of the Fe–Cr system down to zero kelvin coupled with key experiments, Calphad 35, 355-366 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2020.156122](https://doi.org/10.1016/j.jallcom.2020.156122) Marlena Ostrowska, Gabriele Cacciamani, Thermodynamic modelling of the σ and μ phases in several ternary systems containing Co, Cr, Fe, Mo, Re and W, Journal of Alloys and Compounds 845, 156122 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2020.152692](https://doi.org/10.1016/j.jnucmat.2020.152692) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Experimental study, first-principles calculation and thermodynamic modelling of the Cr–Fe–Nb–Sn–Zr quinary system for application as cladding materials in nuclear reactors., Journal of Nuclear Materials 544, 152692 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.09.002](https://doi.org/10.1016/j.calphad.2006.09.002) Marcel H. F. Sluiter, Ab initio lattice stabilities of some elemental complex structures, Calphad (2006).  
_cited as the source of values for this phase_
- [doi:10.1080/10408431003788472](https://doi.org/10.1080/10408431003788472) Wei Xiong, Malin Selleby, Qing Chen, Joakim Odqvist, Yong Du, Phase Equilibria and Thermodynamic Properties in the Fe-Cr System, Critical Reviews in Solid State and Materials Sciences 35, 125-152 (2010).  
_cited as the source of values for this phase_

## FCC_A1 (Cr–Fe)

- Id: `phase:cr-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 7 calculated diagram(s): 1117.16–1671.06 K, x(Fe) 0.87767–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:fcc-a1)

Names (9): _corpus: _corpus:phase:cr-fe:fcc-a1  
_paper: _paper:10.1016/j.calphad.2017.10.002:FCC  
_tdb: _tdb:CrFe-11Xio.tdb:FCC_A1, tdb:CrFe-18Jac.tdb:FCC_A1, tdb:CrFe-20Ost.tdb:FCC_A1, tdb:CrFe-21Laf.tdb:FCC_A1, tdb:CrFe-23Zha.tdb:FCC_A1, tdb:CrFe-82Her.tdb:FCC_A1, tdb:CrFe-87And-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[CrFe-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-11Xio.tdb): FCC_A1, type code %A, sha256 `c6bdc1ced82c0a31…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CR FE : VA : !
~~~~

[CrFe-18Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-18Jac.tdb): FCC_A1, type code %A, sha256 `97353b426c2d299a…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CR FE : VA : !
~~~~

[CrFe-20Ost.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-20Ost.tdb): FCC_A1, type code %A, sha256 `c009125a792bbcf5…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR FE : VA : !
~~~~

[CrFe-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-21Laf.tdb): FCC_A1, type code %A, sha256 `a466cbb58ce8fff8…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR FE : VA : !
~~~~

[CrFe-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-23Zha.tdb): FCC_A1, type code %A, sha256 `093591c8faaf3d7d…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR FE : VA : !
~~~~

[CrFe-82Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-82Her.tdb): FCC_A1, type code %A, sha256 `a426ac8fa1a94471…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR FE : VA : !
~~~~

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): FCC_A1, type code %A, sha256 `aee44c07511fe31f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CR FE : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2017.10.002](https://doi.org/10.1016/j.calphad.2017.10.002) Aurélie Jacob, Erwin Povoden-Karadeniz, Ernst Kozeschnik, Revised thermodynamic description of the Fe-Cr system based on an improved sublattice model of the σ phase, Calphad 60, 16-28 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(82)90018-9](https://doi.org/10.1016/0364-5916%2882%2990018-9) Staffan Hertzman, Bo Sundman, A thermodynamic analysis of the fe-cr system, Calphad 6, 67-80 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.05.002](https://doi.org/10.1016/j.calphad.2011.05.002) Wei Xiong, Peter Hedström, Malin Selleby, Joakim Odqvist, Mattias Thuvander, Qing Chen, An improved thermodynamic modeling of the Fe–Cr system down to zero kelvin coupled with key experiments, Calphad 35, 355-366 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2020.156122](https://doi.org/10.1016/j.jallcom.2020.156122) Marlena Ostrowska, Gabriele Cacciamani, Thermodynamic modelling of the σ and μ phases in several ternary systems containing Co, Cr, Fe, Mo, Re and W, Journal of Alloys and Compounds 845, 156122 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2020.152692](https://doi.org/10.1016/j.jnucmat.2020.152692) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Experimental study, first-principles calculation and thermodynamic modelling of the Cr–Fe–Nb–Sn–Zr quinary system for application as cladding materials in nuclear reactors., Journal of Nuclear Materials 544, 152692 (2021).  
_assessment that models this phase_
- [doi:10.1080/10408431003788472](https://doi.org/10.1080/10408431003788472) Wei Xiong, Malin Selleby, Qing Chen, Joakim Odqvist, Yong Du, Phase Equilibria and Thermodynamic Properties in the Fe-Cr System, Critical Reviews in Solid State and Materials Sciences 35, 125-152 (2010).  
_cited as the source of values for this phase_

## HCP_A3 (Cr–Fe)

- Id: `phase:cr-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:hcp-a3)

Names (7): _corpus: _corpus:phase:cr-fe:hcp-a3  
_tdb: _tdb:CrFe-18Jac.tdb:HCP_A3, tdb:CrFe-20Ost.tdb:HCP_A3, tdb:CrFe-21Laf.tdb:HCP_A3, tdb:CrFe-23Zha.tdb:HCP_A3, tdb:CrFe-82Her.tdb:HCP_A3, tdb:CrFe-87And-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[CrFe-18Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-18Jac.tdb): HCP_A3, type code %A, sha256 `97353b426c2d299a…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : CR FE : VA : !
~~~~

[CrFe-20Ost.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-20Ost.tdb): HCP_A3, type code %A, sha256 `c009125a792bbcf5…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CR FE : VA : !
~~~~

[CrFe-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-21Laf.tdb): HCP_A3, type code %A, sha256 `a466cbb58ce8fff8…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CR FE : VA : !
~~~~

[CrFe-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-23Zha.tdb): HCP_A3, type code %A, sha256 `093591c8faaf3d7d…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CR FE : VA : !
~~~~

[CrFe-82Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-82Her.tdb): HCP_A3, type code %A, sha256 `a426ac8fa1a94471…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR FE : VA : !
~~~~

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): HCP_A3, type code %A, sha256 `aee44c07511fe31f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CR FE : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(82)90018-9](https://doi.org/10.1016/0364-5916%2882%2990018-9) Staffan Hertzman, Bo Sundman, A thermodynamic analysis of the fe-cr system, Calphad 6, 67-80 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.002](https://doi.org/10.1016/j.calphad.2017.10.002) Aurélie Jacob, Erwin Povoden-Karadeniz, Ernst Kozeschnik, Revised thermodynamic description of the Fe-Cr system based on an improved sublattice model of the σ phase, Calphad 60, 16-28 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2020.156122](https://doi.org/10.1016/j.jallcom.2020.156122) Marlena Ostrowska, Gabriele Cacciamani, Thermodynamic modelling of the σ and μ phases in several ternary systems containing Co, Cr, Fe, Mo, Re and W, Journal of Alloys and Compounds 845, 156122 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2020.152692](https://doi.org/10.1016/j.jnucmat.2020.152692) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Experimental study, first-principles calculation and thermodynamic modelling of the Cr–Fe–Nb–Sn–Zr quinary system for application as cladding materials in nuclear reactors., Journal of Nuclear Materials 544, 152692 (2021).  
_assessment that models this phase_

## HIGH_SIGMA (Cr–Fe)

- Id: `phase:cr-fe:high-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:HIGH
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (sgte_mmc2): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for HIGH_SIGMA: CrMn (shown not to exist as a separate phase from sigma)
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm, D8_b — CrFe-87And-LB.tdb: 'Prototype CrFe (tP30, P4_2/mnm, D8_b)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:high-sigma)

Names (2): _corpus: _corpus:phase:cr-fe:high-sigma  
_tdb: _tdb:CrFe-87And-LB.tdb:HIGH_SIGMA  


### TDB models of HIGH_SIGMA (1): PHASE and CONSTITUENT statements as written

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): HIGH_SIGMA, type code %, sha256 `aee44c07511fe31f…`

~~~~text
56: PHASE HIGH_SIGMA % 3 10 4 16 !
57: CONST HIGH_SIGMA : FE : CR : CR FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_

## LIQUID (Cr–Fe)

- Id: `phase:cr-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1782.96–4000 K, x(Fe) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:liquid)

Names (9): _corpus: _corpus:phase:cr-fe:liquid  
_paper: _paper:10.1016/j.calphad.2017.10.002:L  
_tdb: _tdb:CrFe-11Xio.tdb:LIQUID, tdb:CrFe-18Jac.tdb:LIQUID, tdb:CrFe-20Ost.tdb:LIQUID, tdb:CrFe-21Laf.tdb:LIQUID, tdb:CrFe-23Zha.tdb:LIQUID, tdb:CrFe-82Her.tdb:LIQUID, tdb:CrFe-87And-LB.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[CrFe-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-11Xio.tdb): LIQUID, type code %A, sha256 `c6bdc1ced82c0a31…`

~~~~text
27: PHASE LIQUID:L %A 1 1 !
28: CONST LIQUID:L : CR FE : !
~~~~

[CrFe-18Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-18Jac.tdb): LIQUID, type code %, sha256 `97353b426c2d299a…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CR FE : !
~~~~

[CrFe-20Ost.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-20Ost.tdb): LIQUID, type code %, sha256 `c009125a792bbcf5…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CR FE : !
~~~~

[CrFe-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-21Laf.tdb): LIQUID, type code %, sha256 `a466cbb58ce8fff8…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CR FE : !
~~~~

[CrFe-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-23Zha.tdb): LIQUID, type code %, sha256 `093591c8faaf3d7d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR FE : !
~~~~

[CrFe-82Her.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-82Her.tdb): LIQUID, type code %, sha256 `a426ac8fa1a94471…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR FE : !
~~~~

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): LIQUID, type code %, sha256 `aee44c07511fe31f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CR FE : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2017.10.002](https://doi.org/10.1016/j.calphad.2017.10.002) Aurélie Jacob, Erwin Povoden-Karadeniz, Ernst Kozeschnik, Revised thermodynamic description of the Fe-Cr system based on an improved sublattice model of the σ phase, Calphad 60, 16-28 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(82)90018-9](https://doi.org/10.1016/0364-5916%2882%2990018-9) Staffan Hertzman, Bo Sundman, A thermodynamic analysis of the fe-cr system, Calphad 6, 67-80 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.05.002](https://doi.org/10.1016/j.calphad.2011.05.002) Wei Xiong, Peter Hedström, Malin Selleby, Joakim Odqvist, Mattias Thuvander, Qing Chen, An improved thermodynamic modeling of the Fe–Cr system down to zero kelvin coupled with key experiments, Calphad 35, 355-366 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2020.156122](https://doi.org/10.1016/j.jallcom.2020.156122) Marlena Ostrowska, Gabriele Cacciamani, Thermodynamic modelling of the σ and μ phases in several ternary systems containing Co, Cr, Fe, Mo, Re and W, Journal of Alloys and Compounds 845, 156122 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2020.152692](https://doi.org/10.1016/j.jnucmat.2020.152692) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Experimental study, first-principles calculation and thermodynamic modelling of the Cr–Fe–Nb–Sn–Zr quinary system for application as cladding materials in nuclear reactors., Journal of Nuclear Materials 544, 152692 (2021).  
_assessment that models this phase_
- [doi:10.1080/10408431003788472](https://doi.org/10.1080/10408431003788472) Wei Xiong, Malin Selleby, Qing Chen, Joakim Odqvist, Yong Du, Phase Equilibria and Thermodynamic Properties in the Fe-Cr System, Critical Reviews in Solid State and Materials Sciences 35, 125-152 (2010).  
_cited as the source of values for this phase_

## SIGMA_OLD (Cr–Fe)

- Id: `phase:cr-fe:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 786.21–1104.5 K, x(Fe) 0.48601–0.56338
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-fe:old-sigma)

Names (2): _corpus: _corpus:phase:cr-fe:old-sigma  
_tdb: _tdb:CrFe-87And-LB.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (1): PHASE and CONSTITUENT statements as written

[CrFe-87And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrFe-87And-LB.tdb): SIGMA_OLD, type code %, sha256 `aee44c07511fe31f…`

~~~~text
51: PHASE SIGMA_OLD % 3 8 4 18 !
52: CONST SIGMA_OLD : FE : CR : CR FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(87)90021-6](https://doi.org/10.1016/0364-5916%2887%2990021-6) Jan-Olof Andersson, Bo Sundman, Thermodynamic properties of the CrFe system, Calphad 11, 83-92 (1987).  
_assessment that models this phase_

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
