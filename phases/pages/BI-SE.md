# Bi–Se phases

> Bi–Se system: 15 phases (tier A 6, tier C 6, liquid 1, needs_review 1, unresolved_no_candidates 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-SE.html · Markdown: https://data.orchid-project.org/phases/pages/BI-SE.md

15 phases (tier A 6, tier C 6, liquid 1, needs_review 1, unresolved_no_candidates 1); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-SE) · [full JSON](https://data.orchid-project.org/phases/systems/BI-SE.json) · [Bi–Se system page](https://data.orchid-project.org/systems/BI-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Se system (15)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-se-a7-rhombohedral); _phase:bi-se:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–544.55 K, x(Se) 0–0 | 8 | 4 |
| [HEXAGONAL_A8](#phase-bi-se-a8-hexagonal); _phase:bi-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–494 K, x(Se) 1–1 | 4 | 4 |
| [BCC_A2](#phase-bi-se-bcc-a2); _phase:bi-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [BI2SE3_C33](#phase-bi-se-bi2se3-c33); _phase:bi-se:bi2se3-c33_ | Bi2Te3 · C33 · hR5 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–989.65 K, x(Se) 0.59944–0.6002 | 17 | 4 |
| [BI3SE2](#phase-bi-se-bi3se2); _phase:bi-se:bi3se2_ | (Bi3Se2) · hP12 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–746.02 K, x(Se) 0.4–0.4 | 13 | 3 |
| [BI3SE4](#phase-bi-se-bi3se4); _phase:bi-se:bi3se4_ | In3Te4 · hR7 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–935.36 K, x(Se) 0.57143–0.57143 | 4 | 1 |
| [BI4SE3](#phase-bi-se-bi4se3); _phase:bi-se:bi4se3_ | Bi4Se3 · hR7 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–830.56 K, x(Se) 0.42857–0.42857 | 4 | 1 |
| [BI4SE5](#phase-bi-se-bi4se5); _phase:bi-se:bi4se5_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–895.32 K, x(Se) 0.55556–0.55556 | 0 | 1 |
| [BI8SE7](#phase-bi-se-bi8se7); _phase:bi-se:bi8se7_ | Bi8Se7 · hP45 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–855.48 K, x(Se) 0.46667–0.46667 | 4 | 1 |
| [BI8SE9](#phase-bi-se-bi8se9); _phase:bi-se:bi8se9_ | Bi8Se9 · hR17 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–884.69 K, x(Se) 0.52941–0.52941 | 4 | 1 |
| [BISE](#phase-bi-se-bise); _phase:bi-se:bise_ | BiSe · hP12 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–887.03 K, x(Se) 0.40604–0.56195 | 10 | 3 |
| [FCC_A1](#phase-bi-se-fcc-a1); _phase:bi-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-bi-se-hcp-a3); _phase:bi-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-bi-se-liquid); _phase:bi-se:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 494–2500 K, x(Se) 0–1 | 38 | 4 |
| [LIQUID-2](#phase-bi-se-liquid-2); _phase:bi-se:liquid-2_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |

## RHOMBOHEDRAL_A7 (Bi–Se)

- Id: `phase:bi-se:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–544.55 K, x(Se) 0–0
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:a7-rhombohedral)

Names (8): _corpus: _corpus:phase:bi-se:a7-rhombohedral, corpus:phase:bi-se:rhombohedral-a7  
_paper: _paper:10.1007/s11669-024-01093-z:(Bi), paper:10.1016/j.jallcom.2014.08.001:rho  
_tdb: _tdb:BiSe-14Che.tdb:RHOMBOHEDRAL_A7, tdb:BiSe-18Pet.tdb:RHOMBOHEDRAL_A7, tdb:BiSe-20Che.tdb:RHOMBOHEDRAL_A7, tdb:BiSe-24Zho.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (4): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `0fcdd9b2c60c49ee…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `786c91341c5c9003…`

~~~~text
52: PHASE RHOMBOHEDRAL_A7 % 1 1 !
53: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `3896c882c74c8447…`

~~~~text
52: PHASE RHOMBOHEDRAL_A7 % 1 1 !
53: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `145dfc0591be3927…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1975-660607](https://doi.org/10.1515/ijmr-1975-660607) B. Gather, and R. Blachnik, Tenary Systems Containing Chalcogenides. II. The Gold-Bismuth-Selenium System, Z. Metallkd., 1975, 66, p 356–359.  
_cited as the source of values for this phase_

## HEXAGONAL_A8 (Bi–Se)

- Id: `phase:bi-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:a8-hexagonal)

Names (8): _corpus: _corpus:phase:bi-se:a8-hexagonal, corpus:phase:bi-se:hexagonal-a8  
_paper: _paper:10.1007/s11669-024-01093-z:(Se), paper:10.1016/j.jallcom.2014.08.001:hex  
_tdb: _tdb:BiSe-14Che.tdb:HEXAGONAL_A8, tdb:BiSe-18Pet.tdb:HEXAGONAL_A8, tdb:BiSe-20Che.tdb:HEXAGONAL_A8, tdb:BiSe-24Zho.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (4): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): HEXAGONAL_A8, type code %, sha256 `0fcdd9b2c60c49ee…`

~~~~text
56: PHASE HEXAGONAL_A8 % 1 1 !
57: CONST HEXAGONAL_A8 : SE : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): HEXAGONAL_A8, type code %, sha256 `786c91341c5c9003…`

~~~~text
57: PHASE HEXAGONAL_A8 % 1 1 !
58: CONST HEXAGONAL_A8 : SE : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): HEXAGONAL_A8, type code %, sha256 `3896c882c74c8447…`

~~~~text
57: PHASE HEXAGONAL_A8 % 1 1 !
58: CONST HEXAGONAL_A8 : SE : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): HEXAGONAL_A8, type code %, sha256 `145dfc0591be3927…`

~~~~text
56: PHASE HEXAGONAL_A8 % 1 1 !
57: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_

## BCC_A2 (Bi–Se)

- Id: `phase:bi-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bcc-a2)

Names (5): _corpus: _corpus:phase:bi-se:bcc-a2  
_tdb: _tdb:BiSe-14Che.tdb:BCC_A2, tdb:BiSe-18Pet.tdb:BCC_A2, tdb:BiSe-20Che.tdb:BCC_A2, tdb:BiSe-24Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): BCC_A2, type code %B, sha256 `0fcdd9b2c60c49ee…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : BI : VA : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): BCC_A2, type code %B, sha256 `786c91341c5c9003…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : BI : VA : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): BCC_A2, type code %B, sha256 `3896c882c74c8447…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : BI : VA : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BCC_A2, type code %B, sha256 `145dfc0591be3927…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase_

## BI2SE3_C33 (Bi–Se)

- Id: `phase:bi-se:bi2se3-c33`; status `assigned`
- Structure: Bi2Te3 · C33 · hR5 · R-3m (166); type `st:c33-bi2te3-hr5`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–989.65 K, x(Se) 0.59944–0.6002
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bi2se3-c33)

Names (7): _corpus: _corpus:phase:bi-se:bi2se3-c33  
_paper: _paper:10.1007/s11669-024-01093-z:Bi2Se3, paper:10.1016/j.jallcom.2014.08.001:Bi2Se3  
_tdb: _tdb:BiSe-14Che.tdb:BI2SE3_C33, tdb:BiSe-18Pet.tdb:BI2SE3_C33, tdb:BiSe-20Che.tdb:BI2SE3_C33, tdb:BiSe-24Zho.tdb:BI2SE3_C33  


### TDB models of BI2SE3_C33 (4): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): BI2SE3_C33, type code %, sha256 `0fcdd9b2c60c49ee…`

~~~~text
71: PHASE BI2SE3_C33 % 2 2 3 !
72: CONST BI2SE3_C33 : BI : SE : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): BI2SE3_C33, type code %, sha256 `786c91341c5c9003…`

~~~~text
72: PHASE BI2SE3_C33 % 2 2 3 !
73: CONST BI2SE3_C33 : BI% SE : SE% VA : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): BI2SE3_C33, type code %, sha256 `3896c882c74c8447…`

~~~~text
67: PHASE BI2SE3_C33 % 2 2 3 !
68: CONST BI2SE3_C33 : BI : SE : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BI2SE3_C33, type code %, sha256 `145dfc0591be3927…`

~~~~text
91: PHASE BI2SE3_C33 % 2 2 3 !
92: CONST BI2SE3_C33 : BI : SE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_

## BI3SE2 (Bi–Se)

- Id: `phase:bi-se:bi3se2`; status `assigned`
- Structure: (Bi3Se2) · hP12 · P-3m1 (164); type `st:bi3se2-hp12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.6000, Se 0.4000
- Stability: stable in 3 of 3 calculated diagram(s): 300–746.02 K, x(Se) 0.4–0.4
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bi3se2)

Names (6): _corpus: _corpus:phase:bi-se:bi3se2  
_paper: _paper:10.1007/s11669-024-01093-z:Bi3Se2, paper:10.1016/j.jallcom.2014.08.001:Bi3Se2  
_tdb: _tdb:BiSe-14Che.tdb:BI3SE2, tdb:BiSe-18Pet.tdb:BI3SE2, tdb:BiSe-24Zho.tdb:BI3SE2  


### TDB models of BI3SE2 (3): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): BI3SE2, type code %, sha256 `0fcdd9b2c60c49ee…`

~~~~text
61: PHASE BI3SE2 % 2 3 2 !
62: CONST BI3SE2 : BI : SE : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): BI3SE2, type code %, sha256 `786c91341c5c9003…`

~~~~text
62: PHASE BI3SE2 % 2 3 2 !
63: CONST BI3SE2 : BI : SE : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BI3SE2, type code %, sha256 `145dfc0591be3927…`

~~~~text
61: PHASE BI3SE2 % 2 3 2 !
62: CONST BI3SE2 : BI : SE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1975-660607](https://doi.org/10.1515/ijmr-1975-660607) B. Gather, and R. Blachnik, Tenary Systems Containing Chalcogenides. II. The Gold-Bismuth-Selenium System, Z. Metallkd., 1975, 66, p 356–359.  
_cited as the source of values for this phase_

## BI3SE4 (Bi–Se)

- Id: `phase:bi-se:bi3se4`; status `assigned`
- Structure: In3Te4 · hR7 · R-3m (166); type `st:in3te4-hr7`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4286, Se 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–935.36 K, x(Se) 0.57143–0.57143
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bi3se4)

Names (3): _corpus: _corpus:phase:bi-se:bi3se4  
_paper: _paper:10.1007/s11669-024-01093-z:Bi3Se4  
_tdb: _tdb:BiSe-24Zho.tdb:BI3SE4  


### TDB models of BI3SE4 (1): PHASE and CONSTITUENT statements as written

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BI3SE4, type code %, sha256 `145dfc0591be3927…`

~~~~text
86: PHASE BI3SE4 % 2 3 4 !
87: CONST BI3SE4 : BI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_

## BI4SE3 (Bi–Se)

- Id: `phase:bi-se:bi4se3`; status `assigned`
- Structure: Bi4Se3 · hR7 · R-3m (166); type `st:bi4se3-hr7`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.5714, Se 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–830.56 K, x(Se) 0.42857–0.42857
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bi4se3)

Names (3): _corpus: _corpus:phase:bi-se:bi4se3  
_paper: _paper:10.1007/s11669-024-01093-z:Bi4Se3  
_tdb: _tdb:BiSe-24Zho.tdb:BI4SE3  


### TDB models of BI4SE3 (1): PHASE and CONSTITUENT statements as written

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BI4SE3, type code %, sha256 `145dfc0591be3927…`

~~~~text
66: PHASE BI4SE3 % 2 4 3 !
67: CONST BI4SE3 : BI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_

## BI4SE5 (Bi–Se)

- Id: `phase:bi-se:bi4se5`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Bi4Se5) — Hallstedt 2025 mmc2 row for BI4SE5: Bi4Se5
- Stoichiometry: Bi 0.4444, Se 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–895.32 K, x(Se) 0.55556–0.55556
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bi4se5)

Names (2): _corpus: _corpus:phase:bi-se:bi4se5  
_tdb: _tdb:BiSe-18Pet.tdb:BI4SE5  


### TDB models of BI4SE5 (1): PHASE and CONSTITUENT statements as written

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): BI4SE5, type code %, sha256 `786c91341c5c9003…`

~~~~text
67: PHASE BI4SE5 % 2 4 5 !
68: CONST BI4SE5 : BI : SE : !
~~~~

## BI8SE7 (Bi–Se)

- Id: `phase:bi-se:bi8se7`; status `assigned`
- Structure: Bi8Se7 · hP45 · P-3m1 (164); type `st:bi8se7-hp45`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.5333, Se 0.4667
- Stability: stable in 1 of 1 calculated diagram(s): 300–855.48 K, x(Se) 0.46667–0.46667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bi8se7)

Names (3): _corpus: _corpus:phase:bi-se:bi8se7  
_paper: _paper:10.1007/s11669-024-01093-z:Bi8Se7  
_tdb: _tdb:BiSe-24Zho.tdb:BI8SE7  


### TDB models of BI8SE7 (1): PHASE and CONSTITUENT statements as written

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BI8SE7, type code %, sha256 `145dfc0591be3927…`

~~~~text
71: PHASE BI8SE7 % 2 8 7 !
72: CONST BI8SE7 : BI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_

## BI8SE9 (Bi–Se)

- Id: `phase:bi-se:bi8se9`; status `assigned`
- Structure: Bi8Se9 · hR17 · R-3m (166); type `st:bi8se9-hr17`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4706, Se 0.5294
- Stability: stable in 1 of 1 calculated diagram(s): 300–884.69 K, x(Se) 0.52941–0.52941
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bi8se9)

Names (3): _corpus: _corpus:phase:bi-se:bi8se9  
_paper: _paper:10.1007/s11669-024-01093-z:Bi8Se9  
_tdb: _tdb:BiSe-24Zho.tdb:BI8SE9  


### TDB models of BI8SE9 (1): PHASE and CONSTITUENT statements as written

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BI8SE9, type code %, sha256 `145dfc0591be3927…`

~~~~text
81: PHASE BI8SE9 % 2 8 9 !
82: CONST BI8SE9 : BI : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_

## BISE (Bi–Se)

- Id: `phase:bi-se:bise`; status `assigned`
- Structure: BiSe · hP12 · P-3m1 (164); type `st:bise-hp12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 300–887.03 K, x(Se) 0.40604–0.56195
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:bise)

Names (6): _corpus: _corpus:phase:bi-se:bise  
_paper: _paper:10.1007/s11669-024-01093-z:BiSe, paper:10.1016/j.jallcom.2014.08.001:BiSe  
_tdb: _tdb:BiSe-14Che.tdb:BISE, tdb:BiSe-20Che.tdb:BISE, tdb:BiSe-24Zho.tdb:BISE  


### TDB models of BISE (3): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): BISE, type code %, sha256 `0fcdd9b2c60c49ee…`

~~~~text
66: PHASE BISE % 3 2 1 2 !
67: CONST BISE : BI : BI SE : SE : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): BISE, type code %, sha256 `3896c882c74c8447…`

~~~~text
62: PHASE BISE % 3 2 1 2 !
63: CONST BISE : BI : BI SE : SE : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): BISE, type code %, sha256 `145dfc0591be3927…`

~~~~text
76: PHASE BISE % 2 1 1 !
77: CONST BISE : BI : SE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Se)

- Id: `phase:bi-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:fcc-a1)

Names (5): _corpus: _corpus:phase:bi-se:fcc-a1  
_tdb: _tdb:BiSe-14Che.tdb:FCC_A1, tdb:BiSe-18Pet.tdb:FCC_A1, tdb:BiSe-20Che.tdb:FCC_A1, tdb:BiSe-24Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): FCC_A1, type code %A, sha256 `0fcdd9b2c60c49ee…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : BI : VA : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): FCC_A1, type code %A, sha256 `786c91341c5c9003…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : BI : VA : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): FCC_A1, type code %A, sha256 `3896c882c74c8447…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : BI : VA : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): FCC_A1, type code %A, sha256 `145dfc0591be3927…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase_

## HCP_A3 (Bi–Se)

- Id: `phase:bi-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:hcp-a3)

Names (5): _corpus: _corpus:phase:bi-se:hcp-a3  
_tdb: _tdb:BiSe-14Che.tdb:HCP_A3, tdb:BiSe-18Pet.tdb:HCP_A3, tdb:BiSe-20Che.tdb:HCP_A3, tdb:BiSe-24Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): HCP_A3, type code %A, sha256 `0fcdd9b2c60c49ee…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : BI : VA : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): HCP_A3, type code %A, sha256 `786c91341c5c9003…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : BI : VA : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): HCP_A3, type code %A, sha256 `3896c882c74c8447…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : BI : VA : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): HCP_A3, type code %A, sha256 `145dfc0591be3927…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase_

## LIQUID (Bi–Se)

- Id: `phase:bi-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 494–2500 K, x(Se) 0–1
- Literature: 38 values (38 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:liquid)

Names (7): _corpus: _corpus:phase:bi-se:liquid  
_paper: _paper:10.1007/s11669-024-01093-z:Liquid#1, paper:10.1016/j.jallcom.2014.08.001:Liq  
_tdb: _tdb:BiSe-14Che.tdb:LIQUID, tdb:BiSe-18Pet.tdb:LIQUID, tdb:BiSe-20Che.tdb:LIQUID, tdb:BiSe-24Zho.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[BiSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-14Che.tdb): LIQUID, type code %, sha256 `0fcdd9b2c60c49ee…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : BI BI2SE3 SE : !
~~~~

[BiSe-18Pet.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-18Pet.tdb): LIQUID, type code %, sha256 `786c91341c5c9003…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : BI BI2SE3 SE : !
~~~~

[BiSe-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-20Che.tdb): LIQUID, type code %, sha256 `3896c882c74c8447…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : BI BI2SE3 SE : !
~~~~

[BiSe-24Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BiSe-24Zho.tdb): LIQUID, type code %, sha256 `145dfc0591be3927…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : BI BI2SE3 SE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z) Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101744](https://doi.org/10.1016/j.calphad.2020.101744) S.-W. Chen, Y. Hutabalian, W. Gierlotka, C.-H. Wang, S.-T. Lu, Calphad, 68, 101744(2020).  
_assessment that models this phase_
- [doi:10.1007/s10973-021-10975-0](https://doi.org/10.1007/s10973-021-10975-0) Gunel S. Hasanova, Aytan I. Aghazade, Dunya M. Babanly, Samira Z. Imamaliyeva, Yusif A. Yusibov, Mahammad B. Babanly, Experimental study of the phase relations and thermodynamic properties of Bi-Se system, J Therm Anal Calorim 147, 6403-6414 (2022).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1975-660607](https://doi.org/10.1515/ijmr-1975-660607) B. Gather, and R. Blachnik, Tenary Systems Containing Chalcogenides. II. The Gold-Bismuth-Selenium System, Z. Metallkd., 1975, 66, p 356–359.  
_cited as the source of values for this phase_

## LIQUID-2 (Bi–Se)

- Id: `phase:bi-se:liquid-2`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:2,LIQUID; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-se:liquid-2)

Names (1): _corpus: _corpus:phase:bi-se:liquid-2  


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
