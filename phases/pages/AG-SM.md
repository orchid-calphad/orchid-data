# Ag–Sm phases

> Ag–Sm system: 9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-SM.html · Markdown: https://data.orchid-project.org/phases/pages/AG-SM.md

9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-SM) · [full JSON](https://data.orchid-project.org/phases/systems/AG-SM.json) · [Ag–Sm system page](https://data.orchid-project.org/systems/AG-SM.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-SM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Sm system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2SM_ALPHA](#phase-ag-sm-ag2sm-alpha); _phase:ag-sm:ag2sm-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–966.92 K, x(Sm) 0.33333–0.33333 | 8 | 1 |
| [AG2SM_BETA](#phase-ag-sm-ag2sm-beta); _phase:ag-sm:ag2sm-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 966.92–1061.99 K, x(Sm) 0.33333–0.33333 | 6 | 1 |
| [AG51SM14](#phase-ag-sm-ag51sm14); _phase:ag-sm:ag51sm14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1214.39 K, x(Sm) 0.21538–0.21538 | 14 | 1 |
| [AGSM_B2](#phase-ag-sm-agsm-b2); _phase:ag-sm:agsm-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1226.63 K, x(Sm) 0.5–0.5 | 13 | 1 |
| [BCC_A2](#phase-ag-sm-bcc-a2); _phase:ag-sm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1195.4–2500 K, x(Sm) 0.99937–1 | 0 | 1 |
| [FCC_A1](#phase-ag-sm-fcc-a1); _phase:ag-sm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1235.93 K, x(Sm) 0–0 | 4 | 1 |
| [HCP_A3](#phase-ag-sm-hcp-a3); _phase:ag-sm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 930.02–1195.4 K, x(Sm) 0.99913–1 | 0 | 1 |
| [LIQUID](#phase-ag-sm-liquid); _phase:ag-sm:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 953.55–2500 K, x(Sm) 0–1 | 17 | 1 |
| [RHOMB_C19](#phase-ag-sm-rhomb-c19); _phase:ag-sm:rhomb-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1191.87 K, x(Sm) 1–1 | 0 | 1 |

## AG2SM_ALPHA (Ag–Sm)

- Id: `phase:ag-sm:ag2sm-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Ag2 Sm1 at x(SM)=0.3333
- Candidate (sgte_mmc2): (Ag2Sm-alpha) — Hallstedt 2025 mmc2 row for AG2SM_ALPHA: Ag2Sm-alpha
- Stoichiometry: Ag 0.6667, Sm 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–966.92 K, x(Sm) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:ag2sm-alpha)

Names (4): _corpus: _corpus:phase:ag-sm:ag2sm-alpha  
_paper: _paper:10.1007/s11669-020-00813-5:(αSm), paper:10.1007/s11669-020-00813-5:αAg2Sm  
_tdb: _tdb:AgSm-20Zho.tdb:AG2SM_ALPHA  


### TDB models of AG2SM_ALPHA (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): AG2SM_ALPHA, type code %, sha256 `032995b1ab9a604b…`

~~~~text
65: PHASE AG2SM_ALPHA % 2 2 1 !
66: CONST AG2SM_ALPHA : AG : SM : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90217-9](https://doi.org/10.1016/0022-5088%2880%2990217-9) Isolde Stapf, Gonde Kiessler, Hermann Jehn, Erich Gebhardt, Adolf Mulokozi, Der aufbau des systems silber-samarium, Journal of the Less Common Metals 71, P19-P27 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2005.07.069](https://doi.org/10.1016/j.jallcom.2005.07.069) S.V. Meschel, O.J. Kleppa, Thermochemistry of some binary alloys of Samarium with the noble metals (Cu, Ag, Au) by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 416, 93-97 (2006).  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414020265](https://doi.org/10.1134/s0036024414020265) V. S. Sudavtsova, M. A. Shevchenko, V. V. Berezutskii, M. I. Ivanov, V. G. Kudin, Thermodynamic properties of melts of the binary Ag(Au)-Sm systems, Russ. J. Phys. Chem. 88, 200-206 (2014).  
_cited as the source of values for this phase_

## AG2SM_BETA (Ag–Sm)

- Id: `phase:ag-sm:ag2sm-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Ag2 Sm1 at x(SM)=0.3333
- Candidate (sgte_mmc2): (Ag2Sm-beta) — Hallstedt 2025 mmc2 row for AG2SM_BETA: Ag2Sm-beta
- Stoichiometry: Ag 0.6667, Sm 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 966.92–1061.99 K, x(Sm) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:ag2sm-beta)

Names (3): _corpus: _corpus:phase:ag-sm:ag2sm-beta  
_paper: _paper:10.1007/s11669-020-00813-5:βAg2Sm  
_tdb: _tdb:AgSm-20Zho.tdb:AG2SM_BETA  


### TDB models of AG2SM_BETA (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): AG2SM_BETA, type code %, sha256 `032995b1ab9a604b…`

~~~~text
70: PHASE AG2SM_BETA % 2 2 1 !
71: CONST AG2SM_BETA : AG : SM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90217-9](https://doi.org/10.1016/0022-5088%2880%2990217-9) Isolde Stapf, Gonde Kiessler, Hermann Jehn, Erich Gebhardt, Adolf Mulokozi, Der aufbau des systems silber-samarium, Journal of the Less Common Metals 71, P19-P27 (1980).  
_cited as the source of values for this phase_

## AG51SM14 (Ag–Sm)

- Id: `phase:ag-sm:ag51sm14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.7846, Sm 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–1214.39 K, x(Sm) 0.21538–0.21538
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:ag51sm14)

Names (3): _corpus: _corpus:phase:ag-sm:ag51sm14  
_paper: _paper:10.1007/s11669-020-00813-5:Ag51Sm14  
_tdb: _tdb:AgSm-20Zho.tdb:AG51SM14  


### TDB models of AG51SM14 (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): AG51SM14, type code %, sha256 `032995b1ab9a604b…`

~~~~text
60: PHASE AG51SM14 % 2 51 14 !
61: CONST AG51SM14 : AG : SM : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90217-9](https://doi.org/10.1016/0022-5088%2880%2990217-9) Isolde Stapf, Gonde Kiessler, Hermann Jehn, Erich Gebhardt, Adolf Mulokozi, Der aufbau des systems silber-samarium, Journal of the Less Common Metals 71, P19-P27 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2005.07.069](https://doi.org/10.1016/j.jallcom.2005.07.069) S.V. Meschel, O.J. Kleppa, Thermochemistry of some binary alloys of Samarium with the noble metals (Cu, Ag, Au) by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 416, 93-97 (2006).  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414020265](https://doi.org/10.1134/s0036024414020265) V. S. Sudavtsova, M. A. Shevchenko, V. V. Berezutskii, M. I. Ivanov, V. G. Kudin, Thermodynamic properties of melts of the binary Ag(Au)-Sm systems, Russ. J. Phys. Chem. 88, 200-206 (2014).  
_cited as the source of values for this phase_

## AGSM_B2 (Ag–Sm)

- Id: `phase:ag-sm:agsm-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadrf and oqmd-10667, space group 221
- Stoichiometry: Ag 0.5000, Sm 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1226.63 K, x(Sm) 0.5–0.5
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:agsm-b2)

Names (5): _corpus: _corpus:phase:ag-sm:agsm-b2  
_mp: _mp:mp-aaaaadrf  
_oqmd: _oqmd:oqmd-10667  
_paper: _paper:10.1007/s11669-020-00813-5:AgSm  
_tdb: _tdb:AgSm-20Zho.tdb:AGSM_B2  


### TDB models of AGSM_B2 (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): AGSM_B2, type code %, sha256 `032995b1ab9a604b…`

~~~~text
75: PHASE AGSM_B2 % 2 1 1 !
76: CONST AGSM_B2 : AG : SM : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90217-9](https://doi.org/10.1016/0022-5088%2880%2990217-9) Isolde Stapf, Gonde Kiessler, Hermann Jehn, Erich Gebhardt, Adolf Mulokozi, Der aufbau des systems silber-samarium, Journal of the Less Common Metals 71, P19-P27 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2005.07.069](https://doi.org/10.1016/j.jallcom.2005.07.069) S.V. Meschel, O.J. Kleppa, Thermochemistry of some binary alloys of Samarium with the noble metals (Cu, Ag, Au) by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 416, 93-97 (2006).  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414020265](https://doi.org/10.1134/s0036024414020265) V. S. Sudavtsova, M. A. Shevchenko, V. V. Berezutskii, M. I. Ivanov, V. G. Kudin, Thermodynamic properties of melts of the binary Ag(Au)-Sm systems, Russ. J. Phys. Chem. 88, 200-206 (2014).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Sm)

- Id: `phase:ag-sm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1195.4–2500 K, x(Sm) 0.99937–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-sm:bcc-a2  
_tdb: _tdb:AgSm-20Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): BCC_A2, type code %B, sha256 `032995b1ab9a604b…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : AG SM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase_

## FCC_A1 (Ag–Sm)

- Id: `phase:ag-sm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1235.93 K, x(Sm) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-sm:fcc-a1  
_paper: _paper:10.1007/s11669-020-00813-5:(Ag)  
_tdb: _tdb:AgSm-20Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): FCC_A1, type code %A, sha256 `032995b1ab9a604b…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : AG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90217-9](https://doi.org/10.1016/0022-5088%2880%2990217-9) Isolde Stapf, Gonde Kiessler, Hermann Jehn, Erich Gebhardt, Adolf Mulokozi, Der aufbau des systems silber-samarium, Journal of the Less Common Metals 71, P19-P27 (1980).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Sm)

- Id: `phase:ag-sm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 930.02–1195.4 K, x(Sm) 0.99913–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-sm:hcp-a3  
_tdb: _tdb:AgSm-20Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): HCP_A3, type code %A, sha256 `032995b1ab9a604b…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : AG SM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase_

## LIQUID (Ag–Sm)

- Id: `phase:ag-sm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 953.55–2500 K, x(Sm) 0–1
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:liquid)

Names (3): _corpus: _corpus:phase:ag-sm:liquid  
_paper: _paper:10.1007/s11669-020-00813-5:Liquid  
_tdb: _tdb:AgSm-20Zho.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): LIQUID, type code %, sha256 `032995b1ab9a604b…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : AG SM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90217-9](https://doi.org/10.1016/0022-5088%2880%2990217-9) Isolde Stapf, Gonde Kiessler, Hermann Jehn, Erich Gebhardt, Adolf Mulokozi, Der aufbau des systems silber-samarium, Journal of the Less Common Metals 71, P19-P27 (1980).  
_cited as the source of values for this phase_

## RHOMB_C19 (Ag–Sm)

- Id: `phase:ag-sm:rhomb-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stoichiometry: Sm 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1191.87 K, x(Sm) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sm:rhomb-c19)

Names (2): _corpus: _corpus:phase:ag-sm:rhomb-c19  
_tdb: _tdb:AgSm-20Zho.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (1): PHASE and CONSTITUENT statements as written

[AgSm-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSm-20Zho.tdb): RHOMB_C19, type code %, sha256 `032995b1ab9a604b…`

~~~~text
55: PHASE RHOMB_C19 % 1 1 !
56: CONST RHOMB_C19 : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
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
