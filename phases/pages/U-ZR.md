# U–Zr phases

> U–Zr system: 8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/U-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/U-ZR.md

8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=U-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/U-ZR.json) · [U–Zr system page](https://data.orchid-project.org/systems/U-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/U-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the U–Zr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-u-zr-a20-orthorhombic); _phase:u-zr:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–964.93 K, x(Zr) 0–0.01709 | 9 | 9 |
| [BCC_A2](#phase-u-zr-bcc-a2); _phase:u-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 872.18–3999.6 K, x(Zr) 0–1 | 46 | 9 |
| [FCC_A1](#phase-u-zr-fcc-a1); _phase:u-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 9 calculated diagram(s) | 0 | 9 |
| [HCP_A3](#phase-u-zr-hcp-a3); _phase:u-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–2123.99 K, x(Zr) 0.98173–1 | 8 | 9 |
| [LIQUID](#phase-u-zr-liquid); _phase:u-zr:liquid_ | liquid | liquid | stable in 9 of 9 calculated diagram(s): 1320.49–4000 K, x(Zr) 0–1 | 0 | 9 |
| [TETRAGONAL_U](#phase-u-zr-u-tetragonal); _phase:u-zr:u-tetragonal_ |  | needs_review | stable in 9 of 9 calculated diagram(s): 933–1131.44 K, x(Zr) 0–0.01971 | 13 | 9 |
| [U3ZR7](#phase-u-zr-u3zr7); _phase:u-zr:u3zr7_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–880.85 K, x(Zr) 0.7–0.7 | 0 | 1 |
| [UZR2_DELTA](#phase-u-zr-uzr2-delta); _phase:u-zr:uzr2-delta_ | Hg2U · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 8 of 8 calculated diagram(s): 300–893.38 K, x(Zr) 0.59543–0.89214 | 16 | 8 |

## ORTHORHOMBIC_A20 (U–Zr)

- Id: `phase:u-zr:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 300–964.93 K, x(Zr) 0–0.01709
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:a20-orthorhombic)

Names (12): _corpus: _corpus:phase:u-zr:a20-orthorhombic, corpus:phase:u-zr:orthorhombic-a20  
_paper: _paper:10.1016/j.jnucmat.2013.07.034:α(U)  
_tdb: _tdb:UZr-04Che-LB.tdb:ORTHORHOMBIC_A20, tdb:UZr-10Kur.tdb:ORTHORHOMBIC_A20, tdb:UZr-13Xio.tdb:ORTHORHOMBIC_A20, tdb:UZr-18Qua.tdb:ORTHORHOMBIC_A20, tdb:UZr-18Xie.tdb:ORTHORHOMBIC_A20, tdb:UZr-25Wil.tdb:ORTHORHOMBIC_A20, tdb:UZr-98AEA.tdb:ORTHORHOMBIC_A20, tdb:UZr-98Che.tdb:ORTHORHOMBIC_A20, tdb:UZr-98Kur.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (9): PHASE and CONSTITUENT statements as written

[UZr-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-04Che-LB.tdb): ORTHORHOMBIC_A20, type code %, sha256 `6481e0aab32c5025…`

~~~~text
40: PHASE ORTHORHOMBIC_A20 % 1 1 !
41: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

[UZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-10Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `ffe4a27268b05f08…`

~~~~text
40: PHASE ORTHORHOMBIC_A20 % 1 1 !
41: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

[UZr-13Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-13Xio.tdb): ORTHORHOMBIC_A20, type code %, sha256 `eafa259a3af659a1…`

~~~~text
40: PHASE ORTHORHOMBIC_A20 % 1 1 !
41: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

[UZr-18Qua.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Qua.tdb): ORTHORHOMBIC_A20, type code %, sha256 `03a5d10eb8a85d30…`

~~~~text
43: PHASE ORTHORHOMBIC_A20 % 1 1 !
44: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

[UZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Xie.tdb): ORTHORHOMBIC_A20, type code %, sha256 `7469615c052eb943…`

~~~~text
44: PHASE ORTHORHOMBIC_A20 % 1 1 !
45: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

[UZr-25Wil.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-25Wil.tdb): ORTHORHOMBIC_A20, type code %, sha256 `82222cb1e3065b7a…`

~~~~text
45: PHASE ORTHORHOMBIC_A20 % 1 1 !
46: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

[UZr-98AEA.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98AEA.tdb): ORTHORHOMBIC_A20, type code %, sha256 `bcf26f6ed9ab56b8…`

~~~~text
43: PHASE ORTHORHOMBIC_A20 % 1 1 !
44: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[UZr-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Che.tdb): ORTHORHOMBIC_A20, type code %, sha256 `f8840e9375fb1dd8…`

~~~~text
42: PHASE ORTHORHOMBIC_A20 % 1 1 !
43: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

[UZr-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `50af5e7e903bfaec…`

~~~~text
44: PHASE ORTHORHOMBIC_A20 % 1 1 !
45: CONST ORTHORHOMBIC_A20 : U% ZR : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jnucmat.2013.07.034](https://doi.org/10.1016/j.jnucmat.2013.07.034) Wei Xiong, Wei Xie, Chao Shen, Dane Morgan, Thermodynamic modeling of the U–Zr system – A revisit, Journal of Nuclear Materials 443, 331-341 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.03.005](https://doi.org/10.1016/j.calphad.2004.03.005) Pierre-Yves Chevalier, Evelyne Fischer, Bertrand Cheynet, Progress in the thermodynamic modelling of the O–U–Zr ternary system, Calphad 28, 15-40 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2018.01.023](https://doi.org/10.1016/j.jnucmat.2018.01.023) A. Quaini, C. Guéneau, S. Gossé, N. Dupin, B. Sundman, E. Brackx et al., Contribution to the thermodynamic description of the corium – The U-Zr-O system, Journal of Nuclear Materials 501, 104-131 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2024.155378](https://doi.org/10.1016/j.jnucmat.2024.155378) W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski, A modern reappraisal of the U-Zr phase diagram, Journal of Nuclear Materials 603, 155378 (2025).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(98)00450-4](https://doi.org/10.1016/S0022-3115%2898%2900450-4) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 257, 213-55(1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1007/bf02881432](https://doi.org/10.1007/bf02881432) R. I. Sheldon, D. E. Peterson, The U-Zr (Uranium-Zirconium) system, Bulletin of Alloy Phase Diagrams 10, 165-171 (1989).  
_cited as the source of values for this phase_
- [doi:10.2172/4351828](https://doi.org/10.2172/4351828) F.A. Rough, A.E. Austin, A.A. Bauer, J.R. Doig, THE STABILITY AND EXISTENCE RANGE OF THE ZIRCONIUM-URANIUM EPSILON PHASE, (1956).  
_cited as the source of values for this phase_
- [doi:10.2172/4783490](https://doi.org/10.2172/4783490) S T Zegler, THE URANIUM-RICH END OF THE URANIUM-ZIRCONIUM SYSTEM. Final Report- Metallurgy Program 3.1.3., (1962).  
_cited as the source of values for this phase_

## BCC_A2 (U–Zr)

- Id: `phase:u-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 872.18–3999.6 K, x(Zr) 0–1
- Literature: 46 values (46 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:bcc-a2)

Names (12): _corpus: _corpus:phase:u-zr:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2013.07.034:γ, paper:10.1016/s0022-3115(98)00450-4:bcc_A2  
_tdb: _tdb:UZr-04Che-LB.tdb:BCC_A2, tdb:UZr-10Kur.tdb:BCC_A2, tdb:UZr-13Xio.tdb:BCC_A2, tdb:UZr-18Qua.tdb:BCC_A2, tdb:UZr-18Xie.tdb:BCC_A2, tdb:UZr-25Wil.tdb:BCC_A2, tdb:UZr-98AEA.tdb:BCC_A2, tdb:UZr-98Che.tdb:BCC_A2, tdb:UZr-98Kur.tdb:BCC_A2  


### TDB models of BCC_A2 (9): PHASE and CONSTITUENT statements as written

[UZr-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-04Che-LB.tdb): BCC_A2, type code %B, sha256 `6481e0aab32c5025…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-10Kur.tdb): BCC_A2, type code %B, sha256 `ffe4a27268b05f08…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-13Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-13Xio.tdb): BCC_A2, type code %B, sha256 `eafa259a3af659a1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-18Qua.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Qua.tdb): BCC_A2, type code %B, sha256 `03a5d10eb8a85d30…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Xie.tdb): BCC_A2, type code %B, sha256 `7469615c052eb943…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-25Wil.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-25Wil.tdb): BCC_A2, type code %B, sha256 `82222cb1e3065b7a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-98AEA.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98AEA.tdb): BCC_A2, type code %B, sha256 `bcf26f6ed9ab56b8…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Che.tdb): BCC_A2, type code %B, sha256 `f8840e9375fb1dd8…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : U% ZR% : VA : !
~~~~

[UZr-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Kur.tdb): BCC_A2, type code %B, sha256 `50af5e7e903bfaec…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : U% ZR% : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jnucmat.2013.07.034](https://doi.org/10.1016/j.jnucmat.2013.07.034) Wei Xiong, Wei Xie, Chao Shen, Dane Morgan, Thermodynamic modeling of the U–Zr system – A revisit, Journal of Nuclear Materials 443, 331-341 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0022-3115(98)00450-4](https://doi.org/10.1016/S0022-3115%2898%2900450-4) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 257, 213-55(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.03.005](https://doi.org/10.1016/j.calphad.2004.03.005) Pierre-Yves Chevalier, Evelyne Fischer, Bertrand Cheynet, Progress in the thermodynamic modelling of the O–U–Zr ternary system, Calphad 28, 15-40 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2018.01.023](https://doi.org/10.1016/j.jnucmat.2018.01.023) A. Quaini, C. Guéneau, S. Gossé, N. Dupin, B. Sundman, E. Brackx et al., Contribution to the thermodynamic description of the corium – The U-Zr-O system, Journal of Nuclear Materials 501, 104-131 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2024.155378](https://doi.org/10.1016/j.jnucmat.2024.155378) W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski, A modern reappraisal of the U-Zr phase diagram, Journal of Nuclear Materials 603, 155378 (2025).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1007/bf02881432](https://doi.org/10.1007/bf02881432) R. I. Sheldon, D. E. Peterson, The U-Zr (Uranium-Zirconium) system, Bulletin of Alloy Phase Diagrams 10, 165-171 (1989).  
_cited as the source of values for this phase_
- [doi:10.2172/4351828](https://doi.org/10.2172/4351828) F.A. Rough, A.E. Austin, A.A. Bauer, J.R. Doig, THE STABILITY AND EXISTENCE RANGE OF THE ZIRCONIUM-URANIUM EPSILON PHASE, (1956).  
_cited as the source of values for this phase_
- [doi:10.2172/4783490](https://doi.org/10.2172/4783490) S T Zegler, THE URANIUM-RICH END OF THE URANIUM-ZIRCONIUM SYSTEM. Final Report- Metallurgy Program 3.1.3., (1962).  
_cited as the source of values for this phase_

## FCC_A1 (U–Zr)

- Id: `phase:u-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 9 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:fcc-a1)

Names (10): _corpus: _corpus:phase:u-zr:fcc-a1  
_tdb: _tdb:UZr-04Che-LB.tdb:FCC_A1, tdb:UZr-10Kur.tdb:FCC_A1, tdb:UZr-13Xio.tdb:FCC_A1, tdb:UZr-18Qua.tdb:FCC_A1, tdb:UZr-18Xie.tdb:FCC_A1, tdb:UZr-25Wil.tdb:FCC_A1, tdb:UZr-98AEA.tdb:FCC_A1, tdb:UZr-98Che.tdb:FCC_A1, tdb:UZr-98Kur.tdb:FCC_A1  


### TDB models of FCC_A1 (9): PHASE and CONSTITUENT statements as written

[UZr-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-04Che-LB.tdb): FCC_A1, type code %A, sha256 `6481e0aab32c5025…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-10Kur.tdb): FCC_A1, type code %A, sha256 `ffe4a27268b05f08…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-13Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-13Xio.tdb): FCC_A1, type code %A, sha256 `eafa259a3af659a1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-18Qua.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Qua.tdb): FCC_A1, type code %A, sha256 `03a5d10eb8a85d30…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Xie.tdb): FCC_A1, type code %A, sha256 `7469615c052eb943…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-25Wil.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-25Wil.tdb): FCC_A1, type code %A, sha256 `82222cb1e3065b7a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-98AEA.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98AEA.tdb): FCC_A1, type code %A, sha256 `bcf26f6ed9ab56b8…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Che.tdb): FCC_A1, type code %A, sha256 `f8840e9375fb1dd8…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : U ZR : VA : !
~~~~

[UZr-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Kur.tdb): FCC_A1, type code %A, sha256 `50af5e7e903bfaec…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : U ZR : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2004.03.005](https://doi.org/10.1016/j.calphad.2004.03.005) Pierre-Yves Chevalier, Evelyne Fischer, Bertrand Cheynet, Progress in the thermodynamic modelling of the O–U–Zr ternary system, Calphad 28, 15-40 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2013.07.034](https://doi.org/10.1016/j.jnucmat.2013.07.034) Wei Xiong, Wei Xie, Chao Shen, Dane Morgan, Thermodynamic modeling of the U–Zr system – A revisit, Journal of Nuclear Materials 443, 331-341 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2018.01.023](https://doi.org/10.1016/j.jnucmat.2018.01.023) A. Quaini, C. Guéneau, S. Gossé, N. Dupin, B. Sundman, E. Brackx et al., Contribution to the thermodynamic description of the corium – The U-Zr-O system, Journal of Nuclear Materials 501, 104-131 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2024.155378](https://doi.org/10.1016/j.jnucmat.2024.155378) W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski, A modern reappraisal of the U-Zr phase diagram, Journal of Nuclear Materials 603, 155378 (2025).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(98)00450-4](https://doi.org/10.1016/S0022-3115%2898%2900450-4) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 257, 213-55(1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_

## HCP_A3 (U–Zr)

- Id: `phase:u-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 300–2123.99 K, x(Zr) 0.98173–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:hcp-a3)

Names (11): _corpus: _corpus:phase:u-zr:hcp-a3  
_paper: _paper:10.1016/j.jnucmat.2013.07.034:α(Zr)  
_tdb: _tdb:UZr-04Che-LB.tdb:HCP_A3, tdb:UZr-10Kur.tdb:HCP_A3, tdb:UZr-13Xio.tdb:HCP_A3, tdb:UZr-18Qua.tdb:HCP_A3, tdb:UZr-18Xie.tdb:HCP_A3, tdb:UZr-25Wil.tdb:HCP_A3, tdb:UZr-98AEA.tdb:HCP_A3, tdb:UZr-98Che.tdb:HCP_A3, tdb:UZr-98Kur.tdb:HCP_A3  


### TDB models of HCP_A3 (9): PHASE and CONSTITUENT statements as written

[UZr-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-04Che-LB.tdb): HCP_A3, type code %A, sha256 `6481e0aab32c5025…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-10Kur.tdb): HCP_A3, type code %A, sha256 `ffe4a27268b05f08…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-13Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-13Xio.tdb): HCP_A3, type code %A, sha256 `eafa259a3af659a1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-18Qua.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Qua.tdb): HCP_A3, type code %A, sha256 `03a5d10eb8a85d30…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Xie.tdb): HCP_A3, type code %A, sha256 `7469615c052eb943…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-25Wil.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-25Wil.tdb): HCP_A3, type code %A, sha256 `82222cb1e3065b7a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-98AEA.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98AEA.tdb): HCP_A3, type code %A, sha256 `bcf26f6ed9ab56b8…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Che.tdb): HCP_A3, type code %A, sha256 `f8840e9375fb1dd8…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : U ZR% : VA : !
~~~~

[UZr-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Kur.tdb): HCP_A3, type code %A, sha256 `50af5e7e903bfaec…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : U ZR% : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jnucmat.2013.07.034](https://doi.org/10.1016/j.jnucmat.2013.07.034) Wei Xiong, Wei Xie, Chao Shen, Dane Morgan, Thermodynamic modeling of the U–Zr system – A revisit, Journal of Nuclear Materials 443, 331-341 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.03.005](https://doi.org/10.1016/j.calphad.2004.03.005) Pierre-Yves Chevalier, Evelyne Fischer, Bertrand Cheynet, Progress in the thermodynamic modelling of the O–U–Zr ternary system, Calphad 28, 15-40 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2018.01.023](https://doi.org/10.1016/j.jnucmat.2018.01.023) A. Quaini, C. Guéneau, S. Gossé, N. Dupin, B. Sundman, E. Brackx et al., Contribution to the thermodynamic description of the corium – The U-Zr-O system, Journal of Nuclear Materials 501, 104-131 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2024.155378](https://doi.org/10.1016/j.jnucmat.2024.155378) W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski, A modern reappraisal of the U-Zr phase diagram, Journal of Nuclear Materials 603, 155378 (2025).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(98)00450-4](https://doi.org/10.1016/S0022-3115%2898%2900450-4) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 257, 213-55(1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1007/bf02881432](https://doi.org/10.1007/bf02881432) R. I. Sheldon, D. E. Peterson, The U-Zr (Uranium-Zirconium) system, Bulletin of Alloy Phase Diagrams 10, 165-171 (1989).  
_cited as the source of values for this phase_
- [doi:10.2172/4351828](https://doi.org/10.2172/4351828) F.A. Rough, A.E. Austin, A.A. Bauer, J.R. Doig, THE STABILITY AND EXISTENCE RANGE OF THE ZIRCONIUM-URANIUM EPSILON PHASE, (1956).  
_cited as the source of values for this phase_

## LIQUID (U–Zr)

- Id: `phase:u-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 1320.49–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:liquid)

Names (10): _corpus: _corpus:phase:u-zr:liquid  
_tdb: _tdb:UZr-04Che-LB.tdb:LIQUID, tdb:UZr-10Kur.tdb:LIQUID, tdb:UZr-13Xio.tdb:LIQUID, tdb:UZr-18Qua.tdb:LIQUID, tdb:UZr-18Xie.tdb:LIQUID, tdb:UZr-25Wil.tdb:LIQUID, tdb:UZr-98AEA.tdb:LIQUID, tdb:UZr-98Che.tdb:LIQUID, tdb:UZr-98Kur.tdb:LIQUID  


### TDB models of LIQUID (9): PHASE and CONSTITUENT statements as written

[UZr-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-04Che-LB.tdb): LIQUID, type code %, sha256 `6481e0aab32c5025…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : U ZR : !
~~~~

[UZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-10Kur.tdb): LIQUID, type code %, sha256 `ffe4a27268b05f08…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : U ZR : !
~~~~

[UZr-13Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-13Xio.tdb): LIQUID, type code %, sha256 `eafa259a3af659a1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : U ZR : !
~~~~

[UZr-18Qua.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Qua.tdb): LIQUID, type code %, sha256 `03a5d10eb8a85d30…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : U ZR : !
~~~~

[UZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Xie.tdb): LIQUID, type code %, sha256 `7469615c052eb943…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : U ZR : !
~~~~

[UZr-25Wil.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-25Wil.tdb): LIQUID, type code %, sha256 `82222cb1e3065b7a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : U ZR : !
~~~~

[UZr-98AEA.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98AEA.tdb): LIQUID, type code %, sha256 `bcf26f6ed9ab56b8…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : U ZR : !
~~~~

[UZr-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Che.tdb): LIQUID, type code %, sha256 `f8840e9375fb1dd8…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : U ZR : !
~~~~

[UZr-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Kur.tdb): LIQUID, type code %, sha256 `50af5e7e903bfaec…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : U ZR : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2004.03.005](https://doi.org/10.1016/j.calphad.2004.03.005) Pierre-Yves Chevalier, Evelyne Fischer, Bertrand Cheynet, Progress in the thermodynamic modelling of the O–U–Zr ternary system, Calphad 28, 15-40 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2013.07.034](https://doi.org/10.1016/j.jnucmat.2013.07.034) Wei Xiong, Wei Xie, Chao Shen, Dane Morgan, Thermodynamic modeling of the U–Zr system – A revisit, Journal of Nuclear Materials 443, 331-341 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2018.01.023](https://doi.org/10.1016/j.jnucmat.2018.01.023) A. Quaini, C. Guéneau, S. Gossé, N. Dupin, B. Sundman, E. Brackx et al., Contribution to the thermodynamic description of the corium – The U-Zr-O system, Journal of Nuclear Materials 501, 104-131 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2024.155378](https://doi.org/10.1016/j.jnucmat.2024.155378) W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski, A modern reappraisal of the U-Zr phase diagram, Journal of Nuclear Materials 603, 155378 (2025).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(98)00450-4](https://doi.org/10.1016/S0022-3115%2898%2900450-4) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 257, 213-55(1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_

## TETRAGONAL_U (U–Zr)

- Id: `phase:u-zr:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UZr-04Che-LB.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UZr-10Kur.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UZr-13Xio.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UZr-18Qua.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UZr-18Xie.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UZr-25Wil.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UZr-98AEA.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 9 of 9 calculated diagram(s): 933–1131.44 K, x(Zr) 0–0.01971
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:u-tetragonal)

Names (12): _corpus: _corpus:phase:u-zr:u-tetragonal, corpus:phase:u-zr:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2013.07.034:β(U)  
_tdb: _tdb:UZr-04Che-LB.tdb:TETRAGONAL_U, tdb:UZr-10Kur.tdb:TETRAGONAL_U, tdb:UZr-13Xio.tdb:TETRAGONAL_U, tdb:UZr-18Qua.tdb:TETRAGONAL_U, tdb:UZr-18Xie.tdb:TETRAGONAL_U, tdb:UZr-25Wil.tdb:TETRAGONAL_U, tdb:UZr-98AEA.tdb:TETRAGONAL_U, tdb:UZr-98Che.tdb:TETRAGONAL_U, tdb:UZr-98Kur.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (9): PHASE and CONSTITUENT statements as written

[UZr-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-04Che-LB.tdb): TETRAGONAL_U, type code %, sha256 `6481e0aab32c5025…`

~~~~text
45: PHASE TETRAGONAL_U % 1 1 !
46: CONST TETRAGONAL_U : U% ZR : !
~~~~

[UZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-10Kur.tdb): TETRAGONAL_U, type code %, sha256 `ffe4a27268b05f08…`

~~~~text
45: PHASE TETRAGONAL_U % 1 1 !
46: CONST TETRAGONAL_U : U% ZR : !
~~~~

[UZr-13Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-13Xio.tdb): TETRAGONAL_U, type code %, sha256 `eafa259a3af659a1…`

~~~~text
45: PHASE TETRAGONAL_U % 1 1 !
46: CONST TETRAGONAL_U : U% ZR : !
~~~~

[UZr-18Qua.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Qua.tdb): TETRAGONAL_U, type code %, sha256 `03a5d10eb8a85d30…`

~~~~text
48: PHASE TETRAGONAL_U % 1 1 !
49: CONST TETRAGONAL_U : U% ZR : !
~~~~

[UZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Xie.tdb): TETRAGONAL_U, type code %, sha256 `7469615c052eb943…`

~~~~text
49: PHASE TETRAGONAL_U % 1 1 !
50: CONST TETRAGONAL_U : U% ZR : !
~~~~

[UZr-25Wil.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-25Wil.tdb): TETRAGONAL_U, type code %, sha256 `82222cb1e3065b7a…`

~~~~text
50: PHASE TETRAGONAL_U % 1 1 !
51: CONST TETRAGONAL_U : U% ZR : !
~~~~

[UZr-98AEA.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98AEA.tdb): TETRAGONAL_U, type code %, sha256 `bcf26f6ed9ab56b8…`

~~~~text
48: PHASE TETRAGONAL_U % 1 1 !
49: CONST TETRAGONAL_U : U : !
~~~~

[UZr-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Che.tdb): TETRAGONAL_U, type code %, sha256 `f8840e9375fb1dd8…`

~~~~text
47: PHASE TETRAGONAL_U % 1 1 !
48: CONST TETRAGONAL_U : U% ZR : !
~~~~

[UZr-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Kur.tdb): TETRAGONAL_U, type code %, sha256 `50af5e7e903bfaec…`

~~~~text
49: PHASE TETRAGONAL_U % 1 1 !
50: CONST TETRAGONAL_U : U% ZR : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.jnucmat.2013.07.034](https://doi.org/10.1016/j.jnucmat.2013.07.034) Wei Xiong, Wei Xie, Chao Shen, Dane Morgan, Thermodynamic modeling of the U–Zr system – A revisit, Journal of Nuclear Materials 443, 331-341 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.03.005](https://doi.org/10.1016/j.calphad.2004.03.005) Pierre-Yves Chevalier, Evelyne Fischer, Bertrand Cheynet, Progress in the thermodynamic modelling of the O–U–Zr ternary system, Calphad 28, 15-40 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2018.01.023](https://doi.org/10.1016/j.jnucmat.2018.01.023) A. Quaini, C. Guéneau, S. Gossé, N. Dupin, B. Sundman, E. Brackx et al., Contribution to the thermodynamic description of the corium – The U-Zr-O system, Journal of Nuclear Materials 501, 104-131 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2024.155378](https://doi.org/10.1016/j.jnucmat.2024.155378) W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski, A modern reappraisal of the U-Zr phase diagram, Journal of Nuclear Materials 603, 155378 (2025).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(98)00450-4](https://doi.org/10.1016/S0022-3115%2898%2900450-4) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 257, 213-55(1998).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1007/bf02881432](https://doi.org/10.1007/bf02881432) R. I. Sheldon, D. E. Peterson, The U-Zr (Uranium-Zirconium) system, Bulletin of Alloy Phase Diagrams 10, 165-171 (1989).  
_cited as the source of values for this phase_
- [doi:10.2172/4783490](https://doi.org/10.2172/4783490) S T Zegler, THE URANIUM-RICH END OF THE URANIUM-ZIRCONIUM SYSTEM. Final Report- Metallurgy Program 3.1.3., (1962).  
_cited as the source of values for this phase_

## U3ZR7 (U–Zr)

- Id: `phase:u-zr:u3zr7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Candidate (tdb_comment): Hg2U · hP3 · P6/mmm — UZr-98Che.tdb: 'Prototype Hg2U (hP3, P6/mmm)'
- Stoichiometry: U 0.3000, Zr 0.7000
- Stability: stable in 1 of 1 calculated diagram(s): 300–880.85 K, x(Zr) 0.7–0.7
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:u3zr7)

Names (2): _corpus: _corpus:phase:u-zr:u3zr7  
_tdb: _tdb:UZr-98Che.tdb:U3ZR7  


### TDB models of U3ZR7 (1): PHASE and CONSTITUENT statements as written

[UZr-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Che.tdb): U3ZR7, type code %, sha256 `f8840e9375fb1dd8…`

~~~~text
52: PHASE U3ZR7 % 2 3 7 !
53: CONST U3ZR7 : U : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(98)00450-4](https://doi.org/10.1016/S0022-3115%2898%2900450-4) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 257, 213-55(1998).  
_assessment that models this phase_

## UZR2_DELTA (U–Zr)

- Id: `phase:u-zr:uzr2-delta`; status `assigned`
- Structure: Hg2U · hP3 · P6/mmm (191); type `st:hg2u-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 8 of 8 calculated diagram(s): 300–893.38 K, x(Zr) 0.59543–0.89214
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-zr:uzr2-delta)

Names (10): _corpus: _corpus:phase:u-zr:uzr2-delta  
_paper: _paper:10.1016/j.jnucmat.2013.07.034:δ  
_tdb: _tdb:UZr-04Che-LB.tdb:UZR2_DELTA, tdb:UZr-10Kur.tdb:UZR2_DELTA, tdb:UZr-13Xio.tdb:UZR2_DELTA, tdb:UZr-18Qua.tdb:UZR2_DELTA, tdb:UZr-18Xie.tdb:UZR2_DELTA, tdb:UZr-25Wil.tdb:UZR2_DELTA, tdb:UZr-98AEA.tdb:UZR2_DELTA, tdb:UZr-98Kur.tdb:UZR2_DELTA  


### TDB models of UZR2_DELTA (8): PHASE and CONSTITUENT statements as written

[UZr-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-04Che-LB.tdb): UZR2_DELTA, type code %, sha256 `6481e0aab32c5025…`

~~~~text
50: PHASE UZR2_DELTA % 2 2 1 !
51: CONST UZR2_DELTA : U ZR : ZR : !
~~~~

[UZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-10Kur.tdb): UZR2_DELTA, type code %, sha256 `ffe4a27268b05f08…`

~~~~text
51: PHASE UZR2_DELTA % 2 1 2 !
52: CONST UZR2_DELTA : U% ZR : U ZR% : !
~~~~

[UZr-13Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-13Xio.tdb): UZR2_DELTA, type code %, sha256 `eafa259a3af659a1…`

~~~~text
51: PHASE UZR2_DELTA % 2 1 2 !
52: CONST UZR2_DELTA : ZR : U ZR : !
~~~~

[UZr-18Qua.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Qua.tdb): UZR2_DELTA, type code %, sha256 `03a5d10eb8a85d30…`

~~~~text
54: PHASE UZR2_DELTA % 2 1 2 !
55: CONST UZR2_DELTA : ZR : U ZR : !
~~~~

[UZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-18Xie.tdb): UZR2_DELTA, type code %, sha256 `7469615c052eb943…`

~~~~text
55: PHASE UZR2_DELTA % 2 1 2 !
56: CONST UZR2_DELTA : ZR : U ZR : !
~~~~

[UZr-25Wil.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-25Wil.tdb): UZR2_DELTA, type code %, sha256 `82222cb1e3065b7a…`

~~~~text
56: PHASE UZR2_DELTA % 2 1 2 !
57: CONST UZR2_DELTA : ZR : U ZR : !
~~~~

[UZr-98AEA.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98AEA.tdb): UZR2_DELTA, type code %, sha256 `bcf26f6ed9ab56b8…`

~~~~text
53: PHASE UZR2_DELTA % 1 1 !
54: CONST UZR2_DELTA : U ZR : !
~~~~

[UZr-98Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/UZr-98Kur.tdb): UZR2_DELTA, type code %, sha256 `50af5e7e903bfaec…`

~~~~text
54: PHASE UZR2_DELTA % 2 1 2 !
55: CONST UZR2_DELTA : U% ZR : U ZR% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.jnucmat.2013.07.034](https://doi.org/10.1016/j.jnucmat.2013.07.034) Wei Xiong, Wei Xie, Chao Shen, Dane Morgan, Thermodynamic modeling of the U–Zr system – A revisit, Journal of Nuclear Materials 443, 331-341 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.03.005](https://doi.org/10.1016/j.calphad.2004.03.005) Pierre-Yves Chevalier, Evelyne Fischer, Bertrand Cheynet, Progress in the thermodynamic modelling of the O–U–Zr ternary system, Calphad 28, 15-40 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2018.01.023](https://doi.org/10.1016/j.jnucmat.2018.01.023) A. Quaini, C. Guéneau, S. Gossé, N. Dupin, B. Sundman, E. Brackx et al., Contribution to the thermodynamic description of the corium – The U-Zr-O system, Journal of Nuclear Materials 501, 104-131 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2024.155378](https://doi.org/10.1016/j.jnucmat.2024.155378) W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski, A modern reappraisal of the U-Zr phase diagram, Journal of Nuclear Materials 603, 155378 (2025).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00176-5](https://doi.org/10.1016/S0925-8388%2898%2900176-5) M. Kurata, T. Ogata, K. Nakamura, T. Ogawa, J. Alloys Compd., 271-273, 636-40(1998).  
_assessment that models this phase_
- [doi:10.1007/bf02881432](https://doi.org/10.1007/bf02881432) R. I. Sheldon, D. E. Peterson, The U-Zr (Uranium-Zirconium) system, Bulletin of Alloy Phase Diagrams 10, 165-171 (1989).  
_cited as the source of values for this phase_
- [doi:10.2172/4351828](https://doi.org/10.2172/4351828) F.A. Rough, A.E. Austin, A.A. Bauer, J.R. Doig, THE STABILITY AND EXISTENCE RANGE OF THE ZIRCONIUM-URANIUM EPSILON PHASE, (1956).  
_cited as the source of values for this phase_

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
