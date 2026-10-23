# B–Ta phases

> B–Ta system: 13 phases (tier A 7, tier C 3, liquid 1, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-TA.html · Markdown: https://data.orchid-project.org/phases/pages/B-TA.md

13 phases (tier A 7, tier C 3, liquid 1, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-TA) · [full JSON](https://data.orchid-project.org/phases/systems/B-TA.json) · [B–Ta system page](https://data.orchid-project.org/systems/B-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Ta system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-ta-b-beta-rhombo); _phase:b-ta:b-beta-rhombo_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–3361.75 K, x(B) 1–1 | 9 | 2 |
| [BCC_A2](#phase-b-ta-bcc-a2); _phase:b-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.99 K, x(B) 0–0.02571 | 19 | 2 |
| [FCC_A1](#phase-b-ta-fcc-a1); _phase:b-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-b-ta-hcp-a3); _phase:b-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-b-ta-liquid); _phase:b-ta:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2324.96–4000 K, x(B) 0–1 | 42 | 2 |
| [TA2B_C16](#phase-b-ta-ta2b-c16); _phase:b-ta:ta2b-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2206.36–2690.71 K, x(B) 0.27932–0.33333 | 38 | 2 |
| [TA3B2_D5A](#phase-b-ta-ta3b2-d5a); _phase:b-ta:ta3b2-d5a_ | Si2U3 · D5_a · tP10 · P4/mbm (127) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2473.73 K, x(B) 0.4–0.4 | 20 | 2 |
| [TA3B4_D7B](#phase-b-ta-ta3b4-d7b); _phase:b-ta:ta3b4-d7b_ | Ta3B4 · D7_b · oI14 · Immm (71) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3305.36 K, x(B) 0.57143–0.57143 | 18 | 2 |
| [TA5B6](#phase-b-ta-ta5b6); _phase:b-ta:ta5b6_ | V5B6 · oC22 · Cmmm (65) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2848.48 K, x(B) 0.54545–0.54545 | 1 | 1 |
| [TAB](#phase-b-ta-tab); _phase:b-ta:tab_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–3357.92 K, x(B) 0.5–0.5 | 12 | 1 |
| [TAB_B27](#phase-b-ta-tab-b27); _phase:b-ta:tab-b27_ | FeB · B27 · oP8 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 3008.42–3358.42 K, x(B) 0.48744–0.49581 | 6 | 1 |
| [TAB_B33](#phase-b-ta-tab-b33); _phase:b-ta:tab-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–3168.25 K, x(B) 0.5–0.5 | 13 | 1 |
| [TAB2_C32](#phase-b-ta-tab2-c32); _phase:b-ta:tab2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3309.05 K, x(B) 0.66634–0.74398 | 18 | 2 |

## BETA_RHOMBO_B (B–Ta)

- Id: `phase:b-ta:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — TaB-17OuY.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — TaB-18DaS.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–3361.75 K, x(B) 1–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:b-beta-rhombo)

Names (6): _corpus: _corpus:phase:b-ta:b-beta-rhombo, corpus:phase:b-ta:beta-rhombo-b  
_paper: _paper:10.1007/s11669-017-0603-2:(B), paper:10.1016/j.calphad.2018.08.012:(βB)  
_tdb: _tdb:TaB-17OuY.tdb:BETA_RHOMBO_B, tdb:TaB-18DaS.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): BETA_RHOMBO_B, type code %, sha256 `aaf8efce793d8609…`

~~~~text
44: PHASE BETA_RHOMBO_B % 2 93 12 !
45: CONST BETA_RHOMBO_B : B : B : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): BETA_RHOMBO_B, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
41: PHASE BETA_RHOMBO_B % 2 93 12 !
42: CONST BETA_RHOMBO_B : B : B : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2428137](https://doi.org/10.1149/1.2428137) James M. Leitnaker, Melvin G. Bowman, Paul W. Gilles, High-Temperature Phase Studies in the Tantalum-Boron System between Ta and TaB, J. Electrochem. Soc. 108, 568 (1961).  
_cited as the source of values for this phase_

## BCC_A2 (B–Ta)

- Id: `phase:b-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.99 K, x(B) 0–0.02571
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:bcc-a2)

Names (5): _corpus: _corpus:phase:b-ta:bcc-a2  
_paper: _paper:10.1007/s11669-017-0603-2:(Ta), paper:10.1016/j.calphad.2018.08.012:BCC  
_tdb: _tdb:TaB-17OuY.tdb:BCC_A2, tdb:TaB-18DaS.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): BCC_A2, type code %B, sha256 `aaf8efce793d8609…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : TA% : B VA% : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): BCC_A2, type code %B, sha256 `38b9b30e669c48fb…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : TA% : B VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02736442](https://doi.org/10.1007/bf02736442) V.M. Chad, É.C.T. Ramos, G.C. Coelho, C.A. Nunes, P.A. Suzuki, F. Ferreira, and P. Rogl, Evaluation of the Invariant 885 Reactions in the Ta-Rich Region of the Ta-B System, J Phase Equilibria Diffus., 2006, 27(5), p 452-455  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_

## FCC_A1 (B–Ta)

- Id: `phase:b-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:fcc-a1)

Names (3): _corpus: _corpus:phase:b-ta:fcc-a1  
_tdb: _tdb:TaB-17OuY.tdb:FCC_A1, tdb:TaB-18DaS.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): FCC_A1, type code %A, sha256 `aaf8efce793d8609…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : TA : B VA% : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): FCC_A1, type code %A, sha256 `38b9b30e669c48fb…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : TA : B VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase_

## HCP_A3 (B–Ta)

- Id: `phase:b-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:hcp-a3)

Names (3): _corpus: _corpus:phase:b-ta:hcp-a3  
_tdb: _tdb:TaB-17OuY.tdb:HCP_A3, tdb:TaB-18DaS.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): HCP_A3, type code %A, sha256 `aaf8efce793d8609…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : TA : B VA% : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): HCP_A3, type code %A, sha256 `38b9b30e669c48fb…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : TA : B VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase_

## LIQUID (B–Ta)

- Id: `phase:b-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2324.96–4000 K, x(B) 0–1
- Literature: 42 values (42 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:liquid)

Names (5): _corpus: _corpus:phase:b-ta:liquid  
_paper: _paper:10.1007/s11669-017-0603-2:L, paper:10.1016/j.calphad.2018.08.012:L  
_tdb: _tdb:TaB-17OuY.tdb:LIQUID, tdb:TaB-18DaS.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): LIQUID, type code %, sha256 `aaf8efce793d8609…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B TA : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): LIQUID, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : B TA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02736442](https://doi.org/10.1007/bf02736442) V.M. Chad, É.C.T. Ramos, G.C. Coelho, C.A. Nunes, P.A. Suzuki, F. Ferreira, and P. Rogl, Evaluation of the Invariant 885 Reactions in the Ta-Rich Region of the Ta-B System, J Phase Equilibria Diffus., 2006, 27(5), p 452-455  
_cited as the source of values for this phase_
- [doi:10.1149/1.2428137](https://doi.org/10.1149/1.2428137) James M. Leitnaker, Melvin G. Bowman, Paul W. Gilles, High-Temperature Phase Studies in the Tantalum-Boron System between Ta and TaB, J. Electrochem. Soc. 108, 568 (1961).  
_cited as the source of values for this phase_

## TA2B_C16 (B–Ta)

- Id: `phase:b-ta:ta2b-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2206.36–2690.71 K, x(B) 0.27932–0.33333
- Literature: 38 values (38 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:ta2b-c16)

Names (5): _corpus: _corpus:phase:b-ta:ta2b-c16  
_paper: _paper:10.1007/s11669-017-0603-2:Ta2B, paper:10.1016/j.calphad.2018.08.012:Ta2B  
_tdb: _tdb:TaB-17OuY.tdb:TA2B_C16, tdb:TaB-18DaS.tdb:TA2B_C16  


### TDB models of TA2B_C16 (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): TA2B_C16, type code %, sha256 `aaf8efce793d8609…`

~~~~text
49: PHASE TA2B_C16 % 2 2 1 !
50: CONST TA2B_C16 : TA : B : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): TA2B_C16, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
46: PHASE TA2B_C16 % 2 2 1 !
47: CONST TA2B_C16 : TA : B% VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02736442](https://doi.org/10.1007/bf02736442) V.M. Chad, É.C.T. Ramos, G.C. Coelho, C.A. Nunes, P.A. Suzuki, F. Ferreira, and P. Rogl, Evaluation of the Invariant 885 Reactions in the Ta-Rich Region of the Ta-B System, J Phase Equilibria Diffus., 2006, 27(5), p 452-455  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_

## TA3B2_D5A (B–Ta)

- Id: `phase:b-ta:ta3b2-d5a`; status `assigned`
- Structure: Si2U3 · D5_a · tP10 · P4/mbm (127); type `st:d5-a-si2u3-tp10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaatvz and oqmd-18596, space group 127
- Stoichiometry: B 0.4000, Ta 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2473.73 K, x(B) 0.4–0.4
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:ta3b2-d5a)

Names (7): _corpus: _corpus:phase:b-ta:ta3b2-d5a  
_mp: _mp:mp-aaaaatvz  
_oqmd: _oqmd:oqmd-18596  
_paper: _paper:10.1007/s11669-017-0603-2:Ta3B2, paper:10.1016/j.calphad.2018.08.012:Ta3B2  
_tdb: _tdb:TaB-17OuY.tdb:TA3B2_D5A, tdb:TaB-18DaS.tdb:TA3B2_D5A  


### TDB models of TA3B2_D5A (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): TA3B2_D5A, type code %, sha256 `aaf8efce793d8609…`

~~~~text
54: PHASE TA3B2_D5A % 2 3 2 !
55: CONST TA3B2_D5A : TA : B : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): TA3B2_D5A, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
51: PHASE TA3B2_D5A % 2 3 2 !
52: CONST TA3B2_D5A : TA : B : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02736442](https://doi.org/10.1007/bf02736442) V.M. Chad, É.C.T. Ramos, G.C. Coelho, C.A. Nunes, P.A. Suzuki, F. Ferreira, and P. Rogl, Evaluation of the Invariant 885 Reactions in the Ta-Rich Region of the Ta-B System, J Phase Equilibria Diffus., 2006, 27(5), p 452-455  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_

## TA3B4_D7B (B–Ta)

- Id: `phase:b-ta:ta3b4-d7b`; status `assigned`
- Structure: Ta3B4 · D7_b · oI14 · Immm (71); type `st:d7-b-ta3b4-oi14`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaapac and oqmd-8470, space group 71
- Stoichiometry: B 0.5714, Ta 0.4286
- Stability: stable in 2 of 2 calculated diagram(s): 300–3305.36 K, x(B) 0.57143–0.57143
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:ta3b4-d7b)

Names (7): _corpus: _corpus:phase:b-ta:ta3b4-d7b  
_mp: _mp:mp-aaaaapac  
_oqmd: _oqmd:oqmd-8470  
_paper: _paper:10.1007/s11669-017-0603-2:Ta3B4, paper:10.1016/j.calphad.2018.08.012:Ta3B4  
_tdb: _tdb:TaB-17OuY.tdb:TA3B4_D7B, tdb:TaB-18DaS.tdb:TA3B4_D7B  


### TDB models of TA3B4_D7B (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): TA3B4_D7B, type code %, sha256 `aaf8efce793d8609…`

~~~~text
64: PHASE TA3B4_D7B % 2 3 4 !
65: CONST TA3B4_D7B : TA : B : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): TA3B4_D7B, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
71: PHASE TA3B4_D7B % 2 3 4 !
72: CONST TA3B4_D7B : TA : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_

## TA5B6 (B–Ta)

- Id: `phase:b-ta:ta5b6`; status `assigned`
- Structure: V5B6 · oC22 · Cmmm (65); type `st:v5b6-oc22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5455, Ta 0.4545
- Stability: stable in 1 of 1 calculated diagram(s): 300–2848.48 K, x(B) 0.54545–0.54545
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:ta5b6)

Names (3): _corpus: _corpus:phase:b-ta:ta5b6  
_paper: _paper:10.1016/j.calphad.2018.08.012:Ta5B6  
_tdb: _tdb:TaB-18DaS.tdb:TA5B6  


### TDB models of TA5B6 (1): PHASE and CONSTITUENT statements as written

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): TA5B6, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
66: PHASE TA5B6 % 2 5 6 !
67: CONST TA5B6 : TA : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_

## TAB (B–Ta)

- Id: `phase:b-ta:tab`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Cmcm (63) — on-hull MP TaB at x(TA)=0.5000
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD B1 Ta1 at x(TA)=0.5000
- Candidate (tdb_comment): CrB · oC8 · Cmcm, B33 — TaB-17OuY.tdb: 'Prototype CrB (oC8, Cmcm, B33), low T and FeB (oP8, Pnma, B27), high T'
- Stoichiometry: B 0.5000, Ta 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–3357.92 K, x(B) 0.5–0.5
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:tab)

Names (3): _corpus: _corpus:phase:b-ta:tab  
_paper: _paper:10.1007/s11669-017-0603-2:TaB  
_tdb: _tdb:TaB-17OuY.tdb:TAB  


### TDB models of TAB (1): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): TAB, type code %, sha256 `aaf8efce793d8609…`

~~~~text
59: PHASE TAB % 2 1 1 !
60: CONST TAB : TA : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_

## TAB_B27 (B–Ta)

- Id: `phase:b-ta:tab-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 3008.42–3358.42 K, x(B) 0.48744–0.49581
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:tab-b27)

Names (3): _corpus: _corpus:phase:b-ta:tab-b27  
_paper: _paper:10.1016/j.calphad.2018.08.012:TaB(ht)  
_tdb: _tdb:TaB-18DaS.tdb:TAB_B27  


### TDB models of TAB_B27 (1): PHASE and CONSTITUENT statements as written

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): TAB_B27, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
61: PHASE TAB_B27 % 2 1 1 !
62: CONST TAB_B27 : TA : B% VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_

## TAB_B33 (B–Ta)

- Id: `phase:b-ta:tab-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5000, Ta 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–3168.25 K, x(B) 0.5–0.5
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:tab-b33)

Names (3): _corpus: _corpus:phase:b-ta:tab-b33  
_paper: _paper:10.1016/j.calphad.2018.08.012:TaB(rt)  
_tdb: _tdb:TaB-18DaS.tdb:TAB_B33  


### TDB models of TAB_B33 (1): PHASE and CONSTITUENT statements as written

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): TAB_B33, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
56: PHASE TAB_B33 % 2 1 1 !
57: CONST TAB_B33 : TA : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02736442](https://doi.org/10.1007/bf02736442) V.M. Chad, É.C.T. Ramos, G.C. Coelho, C.A. Nunes, P.A. Suzuki, F. Ferreira, and P. Rogl, Evaluation of the Invariant 885 Reactions in the Ta-Rich Region of the Ta-B System, J Phase Equilibria Diffus., 2006, 27(5), p 452-455  
_cited as the source of values for this phase_

## TAB2_C32 (B–Ta)

- Id: `phase:b-ta:tab2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in TaB-17OuY.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–3309.05 K, x(B) 0.66634–0.74398
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ta:tab2-c32)

Names (5): _corpus: _corpus:phase:b-ta:tab2-c32  
_paper: _paper:10.1007/s11669-017-0603-2:TaB2, paper:10.1016/j.calphad.2018.08.012:TaB2  
_tdb: _tdb:TaB-17OuY.tdb:TAB2_C32, tdb:TaB-18DaS.tdb:TAB2_C32  


### TDB models of TAB2_C32 (2): PHASE and CONSTITUENT statements as written

[TaB-17OuY.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-17OuY.tdb): TAB2_C32, type code %, sha256 `aaf8efce793d8609…`

~~~~text
69: PHASE TAB2_C32 % 2 1 2 !
70: CONST TAB2_C32 : B TA% : B% TA : !
~~~~

[TaB-18DaS.tdb](https://orchid-project.org/data/databases/sgte-binary/TaB-18DaS.tdb): TAB2_C32, type code %, sha256 `38b9b30e669c48fb…`

~~~~text
76: PHASE TAB2_C32 % 2 1 2 !
77: CONST TAB2_C32 : TA% VA : B% VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-017-0603-2](https://doi.org/10.1007/s11669-017-0603-2) Xuemei OuYang, Fucheng Yin, Jingxian Hu, Ye Liu, Zhaohui Long, Thermodynamic Modeling of B-Ta and B-C-Ta Systems, J. Phase Equilib. Diffus. 38, 874-886 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.012](https://doi.org/10.1016/j.calphad.2018.08.012) Antonio Augusto Araujo Pinto da Silva, Flavio Ferreira, Belmira Benedita de Lima-Kühn, Gilberto Carvalho Coelho, Carlos Angelo Nunes, Pauline Vilasi et al., The Ta-B system: Key experiments and thermodynamic modeling, Calphad 63, 107-115 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2015.01.144](https://doi.org/10.1016/j.jallcom.2015.01.144) Xiaozheng Zhang, Erjun Zhao, Zhijian Wu, Prediction of new high pressure phase of TaB3: First-principles, Journal of Alloys and Compounds 632, 37-43 (2015).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668242](https://doi.org/10.1007/bf02668242) H. Okamoto, Comment on B-Ta (boron-tantalum), JPE 14, 393-394 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2428137](https://doi.org/10.1149/1.2428137) James M. Leitnaker, Melvin G. Bowman, Paul W. Gilles, High-Temperature Phase Studies in the Tantalum-Boron System between Ta and TaB, J. Electrochem. Soc. 108, 568 (1961).  
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
