# Fe–Tm phases

> Fe–Tm system: 8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-TM.html · Markdown: https://data.orchid-project.org/phases/pages/FE-TM.md

8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-TM) · [full JSON](https://data.orchid-project.org/phases/systems/FE-TM.json) · [Fe–Tm system page](https://data.orchid-project.org/systems/FE-TM.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-TM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Tm system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-tm-bcc-a2); _phase:fe-tm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1828.72 K, x(Tm) 0–0 | 11 | 2 |
| [FCC_A1](#phase-fe-tm-fcc-a1); _phase:fe-tm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1184.81–1667.47 K, x(Tm) 0–0 | 10 | 2 |
| [FE17TM2](#phase-fe-tm-fe17tm2); _phase:fe-tm:fe17tm2_ | CeMg10 · hP44 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1573.32 K, x(Tm) 0.10526–0.10526 | 20 | 2 |
| [FE23TM6_D8A](#phase-fe-tm-fe23tm6-d8a); _phase:fe-tm:fe23tm6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1547.2 K, x(Tm) 0.2069–0.2069 | 8 | 2 |
| [FE2TM_C15](#phase-fe-tm-fe2tm-c15); _phase:fe-tm:fe2tm-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1575.26 K, x(Tm) 0.33333–0.33333 | 10 | 2 |
| [FE3TM](#phase-fe-tm-fe3tm); _phase:fe-tm:fe3tm_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1552.52 K, x(Tm) 0.25–0.25 | 16 | 2 |
| [HCP_A3](#phase-fe-tm-hcp-a3); _phase:fe-tm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.47 K, x(Tm) 0.99552–1 | 6 | 2 |
| [LIQUID](#phase-fe-tm-liquid); _phase:fe-tm:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1182.58–2500 K, x(Tm) 0–1 | 25 | 2 |

## BCC_A2 (Fe–Tm)

- Id: `phase:fe-tm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1828.72 K, x(Tm) 0–0
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:bcc-a2)

Names (5): _corpus: _corpus:phase:fe-tm:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.01.003:alphaFe, paper:10.1016/j.calphad.2014.01.003:deltaFe  
_tdb: _tdb:FeTm-14Kar.tdb:BCC_A2, tdb:FeTm-19Xu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): BCC_A2, type code %B, sha256 `33698064a8ea2f8d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE : VA : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): BCC_A2, type code %B, sha256 `2d52128c27ee96d2…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_

## FCC_A1 (Fe–Tm)

- Id: `phase:fe-tm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 1184.81–1667.47 K, x(Tm) 0–0
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-tm:fcc-a1  
_paper: _paper:10.1016/j.calphad.2014.01.003:gammaFe  
_tdb: _tdb:FeTm-14Kar.tdb:FCC_A1, tdb:FeTm-19Xu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): FCC_A1, type code %A, sha256 `33698064a8ea2f8d…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE : VA : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): FCC_A1, type code %A, sha256 `2d52128c27ee96d2…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_

## FE17TM2 (Fe–Tm)

- Id: `phase:fe-tm:fe17tm2`; status `assigned`
- Structure: CeMg10 · hP44 · P6_3/mmc (194); type `st:cemg10-hp44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.8947, Tm 0.1053
- Stability: stable in 2 of 2 calculated diagram(s): 300–1573.32 K, x(Tm) 0.10526–0.10526
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:fe17tm2)

Names (5): _corpus: _corpus:phase:fe-tm:fe17tm2  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe17Tm2, paper:10.1016/j.calphad.2014.01.003:Fe17Tm2(no stable)  
_tdb: _tdb:FeTm-14Kar.tdb:FE17TM2, tdb:FeTm-19Xu.tdb:FE17TM2  


### TDB models of FE17TM2 (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): FE17TM2, type code %A, sha256 `33698064a8ea2f8d…`

~~~~text
45: PHASE FE17TM2 %A 2 17 2 !
46: CONST FE17TM2 : FE : TM : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): FE17TM2, type code %A, sha256 `2d52128c27ee96d2…`

~~~~text
48: PHASE FE17TM2 %A 2 17 2 !
49: CONST FE17TM2 : FE : TM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_
- [doi:10.1021/je7003353](https://doi.org/10.1021/je7003353) D. Gozzi, M. Iervolino, A. Latini, Thermodynamics of Fe-Rich Intermetallics along the Rare Earth Series, J. Chem. Eng. Data 52, 2350-2358 (2007).  
_cited as the source of values for this phase_

## FE23TM6_D8A (Fe–Tm)

- Id: `phase:fe-tm:fe23tm6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.7931, Tm 0.2069
- Stability: stable in 2 of 2 calculated diagram(s): 300–1547.2 K, x(Tm) 0.2069–0.2069
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:fe23tm6-d8a)

Names (4): _corpus: _corpus:phase:fe-tm:fe23tm6-d8a  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe23Tm6  
_tdb: _tdb:FeTm-14Kar.tdb:FE23TM6_D8A, tdb:FeTm-19Xu.tdb:FE23TM6_D8A  


### TDB models of FE23TM6_D8A (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): FE23TM6_D8A, type code %A, sha256 `33698064a8ea2f8d…`

~~~~text
50: PHASE FE23TM6_D8A %A 2 23 6 !
51: CONST FE23TM6_D8A : FE : TM : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): FE23TM6_D8A, type code %A, sha256 `2d52128c27ee96d2…`

~~~~text
53: PHASE FE23TM6_D8A %A 2 23 6 !
54: CONST FE23TM6_D8A : FE : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_

## FE2TM_C15 (Fe–Tm)

- Id: `phase:fe-tm:fe2tm-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgmyp and oqmd-17236, space group 227
- Stoichiometry: Fe 0.6667, Tm 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1575.26 K, x(Tm) 0.33333–0.33333
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:fe2tm-c15)

Names (6): _corpus: _corpus:phase:fe-tm:fe2tm-c15  
_mp: _mp:mp-aaabgmyp  
_oqmd: _oqmd:oqmd-17236  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe2Tm  
_tdb: _tdb:FeTm-14Kar.tdb:FE2TM_C15, tdb:FeTm-19Xu.tdb:FE2TM_C15  


### TDB models of FE2TM_C15 (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): FE2TM_C15, type code %A, sha256 `33698064a8ea2f8d…`

~~~~text
60: PHASE FE2TM_C15 %A 2 2 1 !
61: CONST FE2TM_C15 : FE : TM : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): FE2TM_C15, type code %A, sha256 `2d52128c27ee96d2…`

~~~~text
63: PHASE FE2TM_C15 %A 2 2 1 !
64: CONST FE2TM_C15 : FE : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_

## FE3TM (Fe–Tm)

- Id: `phase:fe-tm:fe3tm`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7500, Tm 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1552.52 K, x(Tm) 0.25–0.25
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:fe3tm)

Names (4): _corpus: _corpus:phase:fe-tm:fe3tm  
_paper: _paper:10.1016/j.calphad.2014.01.003:Fe3Tm  
_tdb: _tdb:FeTm-14Kar.tdb:FE3TM, tdb:FeTm-19Xu.tdb:FE3TM  


### TDB models of FE3TM (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): FE3TM, type code %A, sha256 `33698064a8ea2f8d…`

~~~~text
55: PHASE FE3TM %A 2 3 1 !
56: CONST FE3TM : FE : TM : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): FE3TM, type code %A, sha256 `2d52128c27ee96d2…`

~~~~text
58: PHASE FE3TM %A 2 3 1 !
59: CONST FE3TM : FE : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_

## HCP_A3 (Fe–Tm)

- Id: `phase:fe-tm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.47 K, x(Tm) 0.99552–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:hcp-a3)

Names (6): _corpus: _corpus:phase:fe-tm:hcp-a3  
_paper: _paper:10.1016/j.calphad.2014.01.003:(alphaTm), paper:10.1016/j.calphad.2014.01.003:(betaTm), paper:10.1016/j.calphad.2014.01.003:alphaTm  
_tdb: _tdb:FeTm-14Kar.tdb:HCP_A3, tdb:FeTm-19Xu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): HCP_A3, type code %A, sha256 `33698064a8ea2f8d…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE TM% : VA : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): HCP_A3, type code %A, sha256 `2d52128c27ee96d2…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : FE TM% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
_assessment that models this phase_

## LIQUID (Fe–Tm)

- Id: `phase:fe-tm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1182.58–2500 K, x(Tm) 0–1
- Literature: 25 values (25 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-tm:liquid)

Names (5): _corpus: _corpus:phase:fe-tm:liquid  
_paper: _paper:10.1016/j.calphad.2014.01.003:L, paper:10.1016/j.calphad.2014.01.003:Liq  
_tdb: _tdb:FeTm-14Kar.tdb:LIQUID, tdb:FeTm-19Xu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FeTm-14Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-14Kar.tdb): LIQUID, type code %, sha256 `33698064a8ea2f8d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE TM : !
~~~~

[FeTm-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTm-19Xu.tdb): LIQUID, type code %, sha256 `2d52128c27ee96d2…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.01.003](https://doi.org/10.1016/j.calphad.2014.01.003) S. Kardellass, C. Servant, N. Selhaoui, A. Iddaoudi, Thermodynamic evaluations of the iron–lutetium and iron–thulium systems, Calphad 46, 42-54 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101646](https://doi.org/10.1016/j.calphad.2019.101646) L. Xu, J. Wang, S. Li, X.L. Chen, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101646(2019).  
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
