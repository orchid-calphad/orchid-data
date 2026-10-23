# Fe–Y phases

> Fe–Y system: 10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-Y.html · Markdown: https://data.orchid-project.org/phases/pages/FE-Y.md

10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-Y) · [full JSON](https://data.orchid-project.org/phases/systems/FE-Y.json) · [Fe–Y system page](https://data.orchid-project.org/systems/FE-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Y system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-y-bcc-a2); _phase:fe-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2500 K, x(Y) 0–1 | 63 | 5 |
| [FCC_A1](#phase-fe-y-fcc-a1); _phase:fe-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 1169.86–1672.05 K, x(Y) 0–0.00104 | 58 | 5 |
| [FE17Y2](#phase-fe-y-fe17y2); _phase:fe-y:fe17y2_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(Y) 0.10526–0.10526 | 137 | 4 |
| [FE17Y2_HT](#phase-fe-y-fe17y2-ht); _phase:fe-y:fe17y2-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1138.93–1674.71 K, x(Y) 0.10526–0.10526 | 17 | 1 |
| [FE17Y2_LT](#phase-fe-y-fe17y2-lt); _phase:fe-y:fe17y2-lt_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1138.93 K, x(Y) 0.10526–0.10526 | 2 | 1 |
| [FE23Y6_D8A](#phase-fe-y-fe23y6-d8a); _phase:fe-y:fe23y6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1622.45 K, x(Y) 0.19064–0.21318 | 91 | 5 |
| [FE2Y_C15](#phase-fe-y-fe2y-c15); _phase:fe-y:fe2y-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1420.94 K, x(Y) 0.31034–0.33732 | 62 | 5 |
| [FE3Y](#phase-fe-y-fe3y); _phase:fe-y:fe3y_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–1624.4 K, x(Y) 0.25–0.25 | 115 | 5 |
| [HCP_A3](#phase-fe-y-hcp-a3); _phase:fe-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1786.15 K, x(Y) 0.98584–1 | 30 | 5 |
| [LIQUID](#phase-fe-y-liquid); _phase:fe-y:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1119.28–2500 K, x(Y) 0–1 | 210 | 5 |

## BCC_A2 (Fe–Y)

- Id: `phase:fe-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2500 K, x(Y) 0–1
- Literature: 63 values (63 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:bcc-a2)

Names (19): _corpus: _corpus:phase:fe-y:bcc-a2  
_paper: _paper:10.1007/s11669-017-0574-3:α Fe, paper:10.1007/s11669-017-0574-3:β Y, paper:10.1007/s11669-017-0574-3:δ Fe, paper:10.1007/s11669-021-00887-9:αFe, paper:10.1007/s11669-021-00887-9:βY, paper:10.1007/s11669-021-00887-9:δFe, paper:10.1016/j.jallcom.2013.07.010:α Fe, paper:10.1016/j.jallcom.2013.07.010:αFe, paper:10.1016/j.jallcom.2013.07.010:βY, paper:10.1016/j.jallcom.2013.07.010:δ Fe, paper:10.1016/j.jallcom.2013.07.010:δFe, paper:10.20517/jmi.2023.08:bcc(α-Fe), paper:10.20517/jmi.2023.08:bcc(δ-Fe)  
_tdb: _tdb:FeY-14Kar.tdb:BCC_A2, tdb:FeY-17Sae.tdb:BCC_A2, tdb:FeY-21Fan.tdb:BCC_A2, tdb:FeY-23Ye.tdb:BCC_A2, tdb:FeY-97Du.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): BCC_A2, type code %B, sha256 `0e4a9e2361dc9c98…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : FE Y : VA : !
~~~~

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): BCC_A2, type code %B, sha256 `d5fb4919023990bf…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE Y : VA : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): BCC_A2, type code %B, sha256 `d085f7eb5ccf15a0…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE Y : VA : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): BCC_A2, type code %B, sha256 `88f70e0778e85ffb…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE Y : VA : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): BCC_A2, type code %B, sha256 `6ffcbf8e63537db7…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : FE Y : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Y)

- Id: `phase:fe-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1169.86–1672.05 K, x(Y) 0–0.00104
- Literature: 58 values (58 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:fcc-a1)

Names (11): _corpus: _corpus:phase:fe-y:fcc-a1  
_paper: _paper:10.1007/s11669-017-0574-3:γ Fe, paper:10.1007/s11669-021-00887-9:γFe, paper:10.1016/j.jallcom.2013.07.010:γ Fe, paper:10.1016/j.jallcom.2013.07.010:γFe, paper:10.20517/jmi.2023.08:fcc(γ-Fe)  
_tdb: _tdb:FeY-14Kar.tdb:FCC_A1, tdb:FeY-17Sae.tdb:FCC_A1, tdb:FeY-21Fan.tdb:FCC_A1, tdb:FeY-23Ye.tdb:FCC_A1, tdb:FeY-97Du.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): FCC_A1, type code %A, sha256 `0e4a9e2361dc9c98…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : FE% Y : VA : !
~~~~

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): FCC_A1, type code %A, sha256 `d5fb4919023990bf…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% Y : VA : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): FCC_A1, type code %A, sha256 `d085f7eb5ccf15a0…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% Y : VA : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): FCC_A1, type code %A, sha256 `88f70e0778e85ffb…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE% Y : VA : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): FCC_A1, type code %A, sha256 `6ffcbf8e63537db7…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : FE% Y : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## FE17Y2 (Fe–Y)

- Id: `phase:fe-y:fe17y2`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Ni17Th2 · hP38 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ni17Th2 · hP38 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for FE17Y2: Fe17Y2 (high T), see also Th2Zn17
- Candidate (sgte_mmc2): Th2Zn17 · hR19 · R-3m (166) — Hallstedt 2025 mmc2 row for FE17Y2: Fe17Y2 (low T), see also Ni17Th2
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — FeY-17Sae.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), high T'
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — FeY-17Sae.tdb: 'Prototype Th2Zn17 (hR19, R-3m), low T'
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — FeY-21Fan.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), high T'
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — FeY-21Fan.tdb: 'Prototype Th2Zn17 (hR19, R-3m), low T'
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — FeY-23Ye.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), high T'
- Stoichiometry: Fe 0.8947, Y 0.1053
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(Y) 0.10526–0.10526
- Literature: 137 values (137 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:fe17y2)

Names (9): _corpus: _corpus:phase:fe-y:fe17y2  
_paper: _paper:10.1007/s11669-017-0574-3:Fe17Y2, paper:10.1007/s11669-021-00887-9:Fe17Y2, paper:10.1016/j.jallcom.2013.07.010:Fe17Y2, paper:10.20517/jmi.2023.08:Fe17Y2  
_tdb: _tdb:FeY-17Sae.tdb:FE17Y2, tdb:FeY-21Fan.tdb:FE17Y2, tdb:FeY-23Ye.tdb:FE17Y2, tdb:FeY-97Du.tdb:FE17Y2  


### TDB models of FE17Y2 (4): PHASE and CONSTITUENT statements as written

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): FE17Y2, type code %A, sha256 `d5fb4919023990bf…`

~~~~text
44: PHASE FE17Y2 %A 2 17 2 !
45: CONST FE17Y2 : FE : Y : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): FE17Y2, type code %A, sha256 `d085f7eb5ccf15a0…`

~~~~text
43: PHASE FE17Y2 %A 2 17 2 !
44: CONST FE17Y2 : FE : Y : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): FE17Y2, type code %A, sha256 `88f70e0778e85ffb…`

~~~~text
50: PHASE FE17Y2 %A 2 17 2 !
51: CONST FE17Y2 : FE : Y : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): FE17Y2, type code %A, sha256 `6ffcbf8e63537db7…`

~~~~text
52: PHASE FE17Y2 %A 2 17 2 !
53: CONST FE17Y2 : FE : Y : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_cited as the source of values for this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1016/0364-5916(84)90033-6](https://doi.org/10.1016/0364-5916%2884%2990033-6) P.R. Subramanian, J.F. Smith, Thermodynamics of Formation of Y-Fe Alloys. Calphad 8(4), 295–305 (1984)  
_cited as the source of values for this phase_
- [doi:10.1021/je7003353](https://doi.org/10.1021/je7003353) D. Gozzi, M. Iervolino, A. Latini, Thermodynamics of Fe-Rich Intermetallics along the Rare Earth Series, J. Chem. Eng. Data 52, 2350-2358 (2007).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.70.144107](https://doi.org/10.1103/physrevb.70.144107) M. Mihalkovič, M. Widom, \<i>Ab initio\</i>calculations of cohesive energies of\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\</mml:math>-based glass-forming alloys, Phys. Rev. B 70 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10) Scott Kirklin, James E Saal, Bryce Meredig, Alex Thompson, Jeff W Doak, Muratahan Aykol et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput Mater 1 (2015).  
_cited as the source of values for this phase_

## FE17Y2_HT (Fe–Y)

- Id: `phase:fe-y:fe17y2-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — FeY-14Kar.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), high T'
- Stoichiometry: Fe 0.8947, Y 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 1138.93–1674.71 K, x(Y) 0.10526–0.10526
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:fe17y2-ht)

Names (4): _corpus: _corpus:phase:fe-y:fe17y2-ht  
_paper: _paper:10.1016/j.jallcom.2013.07.010:Fe17Y2, paper:10.1016/j.jallcom.2013.07.010:Fe17Y2_HT  
_tdb: _tdb:FeY-14Kar.tdb:FE17Y2_HT  


### TDB models of FE17Y2_HT (1): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): FE17Y2_HT, type code %, sha256 `0e4a9e2361dc9c98…`

~~~~text
60: PHASE FE17Y2_HT % 2 17 2 !
61: CONST FE17Y2_HT : FE : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; reports values for this phase_

## FE17Y2_LT (Fe–Y)

- Id: `phase:fe-y:fe17y2-lt`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — FeY-14Kar.tdb: 'Prototype Th2Zn17 (hR19, R-3m), low T'
- Stoichiometry: Fe 0.8947, Y 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 300–1138.93 K, x(Y) 0.10526–0.10526
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:fe17y2-lt)

Names (3): _corpus: _corpus:phase:fe-y:fe17y2-lt  
_paper: _paper:10.1016/j.jallcom.2013.07.010:Fe17Y2_LT  
_tdb: _tdb:FeY-14Kar.tdb:FE17Y2_LT  


### TDB models of FE17Y2_LT (1): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): FE17Y2_LT, type code %A, sha256 `0e4a9e2361dc9c98…`

~~~~text
55: PHASE FE17Y2_LT %A 2 17 2 !
56: CONST FE17Y2_LT : FE : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; reports values for this phase_

## FE23Y6_D8A (Fe–Y)

- Id: `phase:fe-y:fe23y6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeY-14Kar.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeY-17Sae.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1622.45 K, x(Y) 0.19064–0.21318
- Literature: 91 values (91 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:fe23y6-d8a)

Names (10): _corpus: _corpus:phase:fe-y:fe23y6-d8a  
_paper: _paper:10.1007/s11669-017-0574-3:Fe23Y6, paper:10.1007/s11669-021-00887-9:Fe23Y6, paper:10.1016/j.jallcom.2013.07.010:Fe23Y6, paper:10.20517/jmi.2023.08:Fe23Y6  
_tdb: _tdb:FeY-14Kar.tdb:FE23Y6_D8A, tdb:FeY-17Sae.tdb:FE23Y6_D8A, tdb:FeY-21Fan.tdb:FE23Y6_D8A, tdb:FeY-23Ye.tdb:FE23Y6_D8A, tdb:FeY-97Du.tdb:FE23Y6_D8A  


### TDB models of FE23Y6_D8A (5): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): FE23Y6_D8A, type code %A, sha256 `0e4a9e2361dc9c98…`

~~~~text
65: PHASE FE23Y6_D8A %A 2 23 6 !
66: CONST FE23Y6_D8A : FE% Y : FE Y% : !
~~~~

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): FE23Y6_D8A, type code %A, sha256 `d5fb4919023990bf…`

~~~~text
49: PHASE FE23Y6_D8A %A 2 23 6 !
50: CONST FE23Y6_D8A : FE% Y : FE Y% : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): FE23Y6_D8A, type code %A, sha256 `d085f7eb5ccf15a0…`

~~~~text
48: PHASE FE23Y6_D8A %A 2 23 6 !
49: CONST FE23Y6_D8A : FE : Y : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): FE23Y6_D8A, type code %A, sha256 `88f70e0778e85ffb…`

~~~~text
55: PHASE FE23Y6_D8A %A 2 23 6 !
56: CONST FE23Y6_D8A : FE : Y : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): FE23Y6_D8A, type code %A, sha256 `6ffcbf8e63537db7…`

~~~~text
57: PHASE FE23Y6_D8A %A 2 23 6 !
58: CONST FE23Y6_D8A : FE : Y : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(84)90033-6](https://doi.org/10.1016/0364-5916%2884%2990033-6) P.R. Subramanian, J.F. Smith, Thermodynamics of Formation of Y-Fe Alloys. Calphad 8(4), 295–305 (1984)  
_cited as the source of values for this phase_
- [doi:10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10) Scott Kirklin, James E Saal, Bryce Meredig, Alex Thompson, Jeff W Doak, Muratahan Aykol et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput Mater 1 (2015).  
_cited as the source of values for this phase_
- [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013).  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/15/7/010](https://doi.org/10.1088/0305-4608/15/7/010) J Inoue, M Shimizu, Electronic structure and magnetic properties of Y-Co, Y-Fe and Y-Mn intermetallic compounds, J. Phys. F: Met. Phys. 15, 1511-1524 (1985).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.70.144107](https://doi.org/10.1103/physrevb.70.144107) M. Mihalkovič, M. Widom, \<i>Ab initio\</i>calculations of cohesive energies of\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\</mml:math>-based glass-forming alloys, Phys. Rev. B 70 (2004).  
_cited as the source of values for this phase_

## FE2Y_C15 (Fe–Y)

- Id: `phase:fe-y:fe2y-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeY-17Sae.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1420.94 K, x(Y) 0.31034–0.33732
- Literature: 62 values (62 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:fe2y-c15)

Names (10): _corpus: _corpus:phase:fe-y:fe2y-c15  
_paper: _paper:10.1007/s11669-017-0574-3:Fe2Y, paper:10.1007/s11669-021-00887-9:Fe2Y, paper:10.1016/j.jallcom.2013.07.010:Fe2Y, paper:10.20517/jmi.2023.08:Fe2Y  
_tdb: _tdb:FeY-14Kar.tdb:FE2Y_C15, tdb:FeY-17Sae.tdb:FE2Y_C15, tdb:FeY-21Fan.tdb:FE2Y_C15, tdb:FeY-23Ye.tdb:FE2Y_C15, tdb:FeY-97Du.tdb:FE2Y_C15  


### TDB models of FE2Y_C15 (5): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): FE2Y_C15, type code %A, sha256 `0e4a9e2361dc9c98…`

~~~~text
75: PHASE FE2Y_C15 %A 2 2 1 !
76: CONST FE2Y_C15 : FE : FE Y% : !
~~~~

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): FE2Y_C15, type code %A, sha256 `d5fb4919023990bf…`

~~~~text
59: PHASE FE2Y_C15 %A 2 2 1 !
60: CONST FE2Y_C15 : FE% Y : FE Y% : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): FE2Y_C15, type code %A, sha256 `d085f7eb5ccf15a0…`

~~~~text
58: PHASE FE2Y_C15 %A 2 2 1 !
59: CONST FE2Y_C15 : FE : Y : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): FE2Y_C15, type code %A, sha256 `88f70e0778e85ffb…`

~~~~text
65: PHASE FE2Y_C15 %A 2 2 1 !
66: CONST FE2Y_C15 : FE : Y : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): FE2Y_C15, type code %A, sha256 `6ffcbf8e63537db7…`

~~~~text
67: PHASE FE2Y_C15 %A 2 2 1 !
68: CONST FE2Y_C15 : FE : Y : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(84)90033-6](https://doi.org/10.1016/0364-5916%2884%2990033-6) P.R. Subramanian, J.F. Smith, Thermodynamics of Formation of Y-Fe Alloys. Calphad 8(4), 295–305 (1984)  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(83)90138-8](https://doi.org/10.1016/0022-5088%2883%2990138-8) G.K. Shenoy, B. Schuttler, P.J. Viccaro, D. Niarchos, Magnetic properties of intermetallic hydrides, Journal of the Less Common Metals 94, 37-44 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0038-1098(76)91181-9](https://doi.org/10.1016/0038-1098%2876%2991181-9) K.H.J. Buschow, Hydrogen absorption and its effect on the magnetic properties of rare-earth iron intermetallics, Solid State Communications 19, 421-423 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jmmm.2015.12.026](https://doi.org/10.1016/j.jmmm.2015.12.026) Wenxu Zhang, Wanli Zhang, Collapse of the magnetic moment under pressure of AFe2 (A=Y, Zr, Lu and Hf) in the cubic Laves phase, Journal of Magnetism and Magnetic Materials 404, 83-90 (2016).  
_cited as the source of values for this phase_
- [doi:10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10) Scott Kirklin, James E Saal, Bryce Meredig, Alex Thompson, Jeff W Doak, Muratahan Aykol et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput Mater 1 (2015).  
_cited as the source of values for this phase_

## FE3Y (Fe–Y)

- Id: `phase:fe-y:fe3y`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7500, Y 0.2500
- Stability: stable in 5 of 5 calculated diagram(s): 300–1624.4 K, x(Y) 0.25–0.25
- Literature: 115 values (115 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:fe3y)

Names (10): _corpus: _corpus:phase:fe-y:fe3y  
_paper: _paper:10.1007/s11669-017-0574-3:Fe3Y, paper:10.1007/s11669-021-00887-9:Fe3Y, paper:10.1016/j.jallcom.2013.07.010:Fe3Y, paper:10.20517/jmi.2023.08:Fe3Y  
_tdb: _tdb:FeY-14Kar.tdb:FE3Y, tdb:FeY-17Sae.tdb:FE3Y, tdb:FeY-21Fan.tdb:FE3Y, tdb:FeY-23Ye.tdb:FE3Y, tdb:FeY-97Du.tdb:FE3Y  


### TDB models of FE3Y (5): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): FE3Y, type code %A, sha256 `0e4a9e2361dc9c98…`

~~~~text
70: PHASE FE3Y %A 2 3 1 !
71: CONST FE3Y : FE : Y : !
~~~~

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): FE3Y, type code %A, sha256 `d5fb4919023990bf…`

~~~~text
54: PHASE FE3Y %A 2 3 1 !
55: CONST FE3Y : FE : Y : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): FE3Y, type code %A, sha256 `d085f7eb5ccf15a0…`

~~~~text
53: PHASE FE3Y %A 2 3 1 !
54: CONST FE3Y : FE : Y : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): FE3Y, type code %A, sha256 `88f70e0778e85ffb…`

~~~~text
60: PHASE FE3Y %A 2 3 1 !
61: CONST FE3Y : FE : Y : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): FE3Y, type code %A, sha256 `6ffcbf8e63537db7…`

~~~~text
62: PHASE FE3Y %A 2 3 1 !
63: CONST FE3Y : FE : Y : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1016/0364-5916(84)90033-6](https://doi.org/10.1016/0364-5916%2884%2990033-6) P.R. Subramanian, J.F. Smith, Thermodynamics of Formation of Y-Fe Alloys. Calphad 8(4), 295–305 (1984)  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.70.144107](https://doi.org/10.1103/physrevb.70.144107) M. Mihalkovič, M. Widom, \<i>Ab initio\</i>calculations of cohesive energies of\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\</mml:math>-based glass-forming alloys, Phys. Rev. B 70 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90180-6](https://doi.org/10.1016/0022-5088%2876%2990180-6) A.R. Miedema, On the heat of formation of solid alloys. II, Journal of the Less Common Metals 46, 67-83 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_
- [doi:10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10) Scott Kirklin, James E Saal, Bryce Meredig, Alex Thompson, Jeff W Doak, Muratahan Aykol et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput Mater 1 (2015).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Y)

- Id: `phase:fe-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1786.15 K, x(Y) 0.98584–1
- Literature: 30 values (30 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:hcp-a3)

Names (10): _corpus: _corpus:phase:fe-y:hcp-a3  
_paper: _paper:10.1007/s11669-017-0574-3:α Y, paper:10.1007/s11669-021-00887-9:αY, paper:10.1016/j.jallcom.2013.07.010:α Y, paper:10.1016/j.jallcom.2013.07.010:αY  
_tdb: _tdb:FeY-14Kar.tdb:HCP_A3, tdb:FeY-17Sae.tdb:HCP_A3, tdb:FeY-21Fan.tdb:HCP_A3, tdb:FeY-23Ye.tdb:HCP_A3, tdb:FeY-97Du.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): HCP_A3, type code %, sha256 `0e4a9e2361dc9c98…`

~~~~text
50: PHASE HCP_A3 % 2 1 0.5 !
51: CONST HCP_A3 : FE Y% : VA : !
~~~~

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): HCP_A3, type code %, sha256 `d5fb4919023990bf…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : FE Y% : VA : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): HCP_A3, type code %, sha256 `d085f7eb5ccf15a0…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : FE Y% : VA : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): HCP_A3, type code %, sha256 `88f70e0778e85ffb…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : FE Y% : VA : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): HCP_A3, type code %, sha256 `6ffcbf8e63537db7…`

~~~~text
46: PHASE HCP_A3 % 2 1 0.5 !
47: CONST HCP_A3 : FE Y% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## LIQUID (Fe–Y)

- Id: `phase:fe-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1119.28–2500 K, x(Y) 0–1
- Literature: 210 values (207 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-y:liquid)

Names (14): _corpus: _corpus:phase:fe-y:liquid  
_paper: _paper:10.1007/s11669-017-0574-3:Liq, paper:10.1007/s11669-017-0574-3:liquid, paper:10.1007/s11669-021-00887-9:L, paper:10.1007/s11669-021-00887-9:Liquid, paper:10.1016/j.jallcom.2013.07.010:L, paper:10.1016/j.jallcom.2013.07.010:Liq, paper:10.1016/j.jallcom.2013.07.010:liquid, paper:10.20517/jmi.2023.08:L  
_tdb: _tdb:FeY-14Kar.tdb:LIQUID, tdb:FeY-17Sae.tdb:LIQUID, tdb:FeY-21Fan.tdb:LIQUID, tdb:FeY-23Ye.tdb:LIQUID, tdb:FeY-97Du.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[FeY-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-14Kar.tdb): LIQUID, type code %, sha256 `0e4a9e2361dc9c98…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : FE Y : !
~~~~

[FeY-17Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-17Sae.tdb): LIQUID, type code %, sha256 `d5fb4919023990bf…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE Y : !
~~~~

[FeY-21Fan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-21Fan.tdb): LIQUID, type code %, sha256 `d085f7eb5ccf15a0…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE Y : !
~~~~

[FeY-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-23Ye.tdb): LIQUID, type code %, sha256 `88f70e0778e85ffb…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : FE Y : !
~~~~

[FeY-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeY-97Du.tdb): LIQUID, type code %, sha256 `6ffcbf8e63537db7…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : FE Y : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2013.07.010](https://doi.org/10.1016/j.jallcom.2013.07.010) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the iron–yttrium system, Journal of Alloys and Compounds 583, 598-606 (2014).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0574-3](https://doi.org/10.1007/s11669-017-0574-3) I. Saenko, O. Fabrichnaya, A. Udovsky, New Thermodynamic Assessment of the Fe-Y System, J. Phase Equilib. Diffus. 38, 684-699 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-021-00887-9](https://doi.org/10.1007/s11669-021-00887-9) Ling Fan, Chen Shen, Kun Hu, Huashan Liu, Hongbin Zhang, DFT Calculations and Thermodynamic Re-Assessment of the Fe-Y Binary System, J. Phase Equilib. Diffus. 42, 348-362 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_
- [doi:10.1007/s11669-017-0546-7](https://doi.org/10.1007/s11669-017-0546-7) B. Konar, J. Kim, I.-H. Jung, Critical Systematic Evaluation and Thermodynamic Optimization of the Fe-RE system: RE= Gd, Tb, Dy, Ho, Er, Tm, Lu, and Y. J. Phase Equilib. Diff. 38(4), 509–542 (2017)  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
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
