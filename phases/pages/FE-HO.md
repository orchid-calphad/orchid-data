# Fe–Ho phases

> Fe–Ho system: 8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-HO.html · Markdown: https://data.orchid-project.org/phases/pages/FE-HO.md

8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-HO) · [full JSON](https://data.orchid-project.org/phases/systems/FE-HO.json) · [Fe–Ho system page](https://data.orchid-project.org/systems/FE-HO.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-HO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Ho system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-ho-bcc-a2); _phase:fe-ho:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1848.57 K, x(Ho) 0–0.00021 | 6 | 2 |
| [FCC_A1](#phase-fe-ho-fcc-a1); _phase:fe-ho:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1184.8–1667.56 K, x(Ho) 0–0.00024 | 5 | 2 |
| [FE17HO2](#phase-fe-ho-fe17ho2); _phase:fe-ho:fe17ho2_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1619.69 K, x(Ho) 0.10526–0.10526 | 21 | 2 |
| [FE23HO6_D8A](#phase-fe-ho-fe23ho6-d8a); _phase:fe-ho:fe23ho6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1613.21 K, x(Ho) 0.2069–0.2069 | 12 | 2 |
| [FE2HO_C15](#phase-fe-ho-fe2ho-c15); _phase:fe-ho:fe2ho-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1569.22 K, x(Ho) 0.33333–0.33333 | 9 | 2 |
| [FE3HO](#phase-fe-ho-fe3ho); _phase:fe-ho:fe3ho_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1583.31 K, x(Ho) 0.25–0.25 | 13 | 2 |
| [HCP_A3](#phase-fe-ho-hcp-a3); _phase:fe-ho:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.48 K, x(Ho) 0.99282–1 | 5 | 2 |
| [LIQUID](#phase-fe-ho-liquid); _phase:fe-ho:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1151.93–2500 K, x(Ho) 0–1 | 43 | 2 |

## BCC_A2 (Fe–Ho)

- Id: `phase:fe-ho:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1848.57 K, x(Ho) 0–0.00021
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-ho:bcc-a2  
_paper: _paper:10.1016/j.jct.2013.11.037:δFe  
_tdb: _tdb:FeHo-14Kar.tdb:BCC_A2, tdb:FeHo-19Xu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): BCC_A2, type code %B, sha256 `41fa95b081c454d8…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : FE% HO% : VA : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): BCC_A2, type code %B, sha256 `93b42acc4ccdb2f9…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% HO% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Ho)

- Id: `phase:fe-ho:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1184.8–1667.56 K, x(Ho) 0–0.00024
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:fcc-a1)

Names (5): _corpus: _corpus:phase:fe-ho:fcc-a1  
_paper: _paper:10.1016/j.jct.2013.11.037:(γFe), paper:10.1016/j.jct.2013.11.037:γFe  
_tdb: _tdb:FeHo-14Kar.tdb:FCC_A1, tdb:FeHo-19Xu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): FCC_A1, type code %A, sha256 `41fa95b081c454d8…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : FE% HO : VA : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): FCC_A1, type code %A, sha256 `93b42acc4ccdb2f9…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% HO : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
_cited as the source of values for this phase_

## FE17HO2 (Fe–Ho)

- Id: `phase:fe-ho:fe17ho2`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.8947, Ho 0.1053
- Stability: stable in 2 of 2 calculated diagram(s): 300–1619.69 K, x(Ho) 0.10526–0.10526
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:fe17ho2)

Names (4): _corpus: _corpus:phase:fe-ho:fe17ho2  
_paper: _paper:10.1016/j.jct.2013.11.037:Fe17Ho2  
_tdb: _tdb:FeHo-14Kar.tdb:FE17HO2, tdb:FeHo-19Xu.tdb:FE17HO2  


### TDB models of FE17HO2 (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): FE17HO2, type code %A, sha256 `41fa95b081c454d8…`

~~~~text
47: PHASE FE17HO2 %A 2 17 2 !
48: CONST FE17HO2 : FE : HO : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): FE17HO2, type code %A, sha256 `93b42acc4ccdb2f9…`

~~~~text
46: PHASE FE17HO2 %A 2 17 2 !
47: CONST FE17HO2 : FE : HO : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jct.2012.09.021](https://doi.org/10.1016/j.jct.2012.09.021) A. Latini, V. Genova, J. Steiner, D. Gozzi, Thermodynamic properties of RE2Co17 intermetallics at high temperatures (RE = Pr, Nd, Gd, Tb, Dy, Ho, Er, Tm, Lu), The Journal of Chemical Thermodynamics 57, 461-469 (2013).  
_cited as the source of values for this phase_
- [doi:10.1021/je7003353](https://doi.org/10.1021/je7003353) D. Gozzi, M. Iervolino, A. Latini, Thermodynamics of Fe-Rich Intermetallics along the Rare Earth Series, J. Chem. Eng. Data 52, 2350-2358 (2007).  
_cited as the source of values for this phase_
- [doi:10.1109/tmag.1966.1065874](https://doi.org/10.1109/tmag.1966.1065874) K. Strnat, G. Hoffer, A. Ray, Magnetic properties of rare--Earth--Iron intermetallic compounds, IEEE Trans. Magn. 2, 489-493 (1966).  
_cited as the source of values for this phase_

## FE23HO6_D8A (Fe–Ho)

- Id: `phase:fe-ho:fe23ho6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.7931, Ho 0.2069
- Stability: stable in 2 of 2 calculated diagram(s): 300–1613.21 K, x(Ho) 0.2069–0.2069
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:fe23ho6-d8a)

Names (4): _corpus: _corpus:phase:fe-ho:fe23ho6-d8a  
_paper: _paper:10.1016/j.jct.2013.11.037:Fe23Ho6  
_tdb: _tdb:FeHo-14Kar.tdb:FE23HO6_D8A, tdb:FeHo-19Xu.tdb:FE23HO6_D8A  


### TDB models of FE23HO6_D8A (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): FE23HO6_D8A, type code %A, sha256 `41fa95b081c454d8…`

~~~~text
52: PHASE FE23HO6_D8A %A 2 23 6 !
53: CONST FE23HO6_D8A : FE : HO : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): FE23HO6_D8A, type code %A, sha256 `93b42acc4ccdb2f9…`

~~~~text
51: PHASE FE23HO6_D8A %A 2 23 6 !
52: CONST FE23HO6_D8A : FE : HO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
_cited as the source of values for this phase_

## FE2HO_C15 (Fe–Ho)

- Id: `phase:fe-ho:fe2ho-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacwc and oqmd-31298, space group 227
- Stoichiometry: Fe 0.6667, Ho 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1569.22 K, x(Ho) 0.33333–0.33333
- Literature: 9 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:fe2ho-c15)

Names (6): _corpus: _corpus:phase:fe-ho:fe2ho-c15  
_mp: _mp:mp-aaaaacwc  
_oqmd: _oqmd:oqmd-31298  
_paper: _paper:10.1016/j.jct.2013.11.037:Fe2Ho  
_tdb: _tdb:FeHo-14Kar.tdb:FE2HO_C15, tdb:FeHo-19Xu.tdb:FE2HO_C15  


### TDB models of FE2HO_C15 (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): FE2HO_C15, type code %A, sha256 `41fa95b081c454d8…`

~~~~text
62: PHASE FE2HO_C15 %A 2 2 1 !
63: CONST FE2HO_C15 : FE : HO : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): FE2HO_C15, type code %A, sha256 `93b42acc4ccdb2f9…`

~~~~text
61: PHASE FE2HO_C15 %A 2 2 1 !
62: CONST FE2HO_C15 : FE : HO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
_cited as the source of values for this phase_

## FE3HO (Fe–Ho)

- Id: `phase:fe-ho:fe3ho`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7500, Ho 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1583.31 K, x(Ho) 0.25–0.25
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:fe3ho)

Names (4): _corpus: _corpus:phase:fe-ho:fe3ho  
_paper: _paper:10.1016/j.jct.2013.11.037:Fe3Ho  
_tdb: _tdb:FeHo-14Kar.tdb:FE3HO, tdb:FeHo-19Xu.tdb:FE3HO  


### TDB models of FE3HO (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): FE3HO, type code %A, sha256 `41fa95b081c454d8…`

~~~~text
57: PHASE FE3HO %A 2 3 1 !
58: CONST FE3HO : FE : HO : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): FE3HO, type code %A, sha256 `93b42acc4ccdb2f9…`

~~~~text
56: PHASE FE3HO %A 2 3 1 !
57: CONST FE3HO : FE : HO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Ho)

- Id: `phase:fe-ho:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.48 K, x(Ho) 0.99282–1
- Literature: 5 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-ho:hcp-a3  
_paper: _paper:10.1016/j.jct.2013.11.037:(αHo)  
_tdb: _tdb:FeHo-14Kar.tdb:HCP_A3, tdb:FeHo-19Xu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): HCP_A3, type code %A, sha256 `41fa95b081c454d8…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : FE HO% : VA : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): HCP_A3, type code %A, sha256 `93b42acc4ccdb2f9…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE HO% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
_cited as the source of values for this phase_

## LIQUID (Fe–Ho)

- Id: `phase:fe-ho:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1151.93–2500 K, x(Ho) 0–1
- Literature: 43 values (42 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ho:liquid)

Names (6): _corpus: _corpus:phase:fe-ho:liquid  
_paper: _paper:10.1016/j.jct.2013.11.037:L, paper:10.1016/j.jct.2013.11.037:Liq, paper:10.1016/j.jct.2013.11.037:liquid  
_tdb: _tdb:FeHo-14Kar.tdb:LIQUID, tdb:FeHo-19Xu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FeHo-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-14Kar.tdb): LIQUID, type code %, sha256 `41fa95b081c454d8…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : FE HO : !
~~~~

[FeHo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeHo-19Xu.tdb): LIQUID, type code %, sha256 `93b42acc4ccdb2f9…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE HO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jct.2013.11.037](https://doi.org/10.1016/j.jct.2013.11.037) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, M. Ait Amar, L. Bouirden, A thermodynamic assessment of the Iron+Holmium phase diagram, The Journal of Chemical Thermodynamics 74, 78-84 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1007/bf03038385](https://doi.org/10.1007/bf03038385) G. J. Roe, T. J. O’Keefe, The Fe−Ho binary system, Metall Trans 1, 2565-2568 (1970).  
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
