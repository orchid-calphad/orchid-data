# Fe–Sm phases

> Fe–Sm system: 8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-SM.html · Markdown: https://data.orchid-project.org/phases/pages/FE-SM.md

8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-SM) · [full JSON](https://data.orchid-project.org/phases/systems/FE-SM.json) · [Fe–Sm system page](https://data.orchid-project.org/systems/FE-SM.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-SM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Sm system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-sm-bcc-a2); _phase:fe-sm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Sm) 0–1 | 0 | 2 |
| [FCC_A1](#phase-fe-sm-fcc-a1); _phase:fe-sm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1160.33–1668.46 K, x(Sm) 0–0.00296 | 2 | 2 |
| [FE17SM2](#phase-fe-sm-fe17sm2); _phase:fe-sm:fe17sm2_ | Th2Zn17 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1555.73 K, x(Sm) 0.10526–0.10526 | 17 | 2 |
| [FE2SM_C15](#phase-fe-sm-fe2sm-c15); _phase:fe-sm:fe2sm-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1173.81 K, x(Sm) 0.33333–0.33333 | 4 | 2 |
| [FE3SM](#phase-fe-sm-fe3sm); _phase:fe-sm:fe3sm_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1286.86 K, x(Sm) 0.25–0.25 | 4 | 2 |
| [HCP_A3](#phase-fe-sm-hcp-a3); _phase:fe-sm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 977–1196 K, x(Sm) 0.34–1 | 0 | 2 |
| [LIQUID](#phase-fe-sm-liquid); _phase:fe-sm:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 994.67–2500 K, x(Sm) 0–1 | 8 | 2 |
| [RHOMB_C19](#phase-fe-sm-rhomb-c19); _phase:fe-sm:rhomb-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1192.36 K, x(Sm) 0.99953–1 | 2 | 2 |

## BCC_A2 (Fe–Sm)

- Id: `phase:fe-sm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Sm) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:bcc-a2)

Names (3): _corpus: _corpus:phase:fe-sm:bcc-a2  
_tdb: _tdb:FeSm-02Zin.tdb:BCC_A2, tdb:FeSm-17Che.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): BCC_A2, type code %B, sha256 `f9381a4b6ae265f7…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% SM% : VA : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): BCC_A2, type code %B, sha256 `ee2803e2feb0f407…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% SM% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase_

## FCC_A1 (Fe–Sm)

- Id: `phase:fe-sm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1160.33–1668.46 K, x(Sm) 0–0.00296
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-sm:fcc-a1  
_paper: _paper:10.1016/s0925-8388(01)01990-9:f.c.c. Fe  
_tdb: _tdb:FeSm-02Zin.tdb:FCC_A1, tdb:FeSm-17Che.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): FCC_A1, type code %A, sha256 `f9381a4b6ae265f7…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% SM : VA : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): FCC_A1, type code %A, sha256 `ee2803e2feb0f407…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% SM : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(71)90124-x](https://doi.org/10.1016/0022-5088%2871%2990124-x) K.H.J. Buschow, The samarium-iron system, Journal of the Less Common Metals 25, 131-134 (1971).  
_cited as the source of values for this phase_

## FE17SM2 (Fe–Sm)

- Id: `phase:fe-sm:fe17sm2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.8947, Sm 0.1053
- Stability: stable in 2 of 2 calculated diagram(s): 300–1555.73 K, x(Sm) 0.10526–0.10526
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:fe17sm2)

Names (4): _corpus: _corpus:phase:fe-sm:fe17sm2  
_paper: _paper:10.1016/s0925-8388(01)01990-9:Fe17Sm2  
_tdb: _tdb:FeSm-02Zin.tdb:FE17SM2, tdb:FeSm-17Che.tdb:FE17SM2  


### TDB models of FE17SM2 (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): FE17SM2, type code %A, sha256 `f9381a4b6ae265f7…`

~~~~text
51: PHASE FE17SM2 %A 2 17 2 !
52: CONST FE17SM2 : FE : SM : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): FE17SM2, type code %A, sha256 `ee2803e2feb0f407…`

~~~~text
49: PHASE FE17SM2 %A 2 17 2 !
50: CONST FE17SM2 : FE : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(71)90124-x](https://doi.org/10.1016/0022-5088%2871%2990124-x) K.H.J. Buschow, The samarium-iron system, Journal of the Less Common Metals 25, 131-134 (1971).  
_cited as the source of values for this phase_

## FE2SM_C15 (Fe–Sm)

- Id: `phase:fe-sm:fe2sm-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.6667, Sm 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1173.81 K, x(Sm) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:fe2sm-c15)

Names (4): _corpus: _corpus:phase:fe-sm:fe2sm-c15  
_paper: _paper:10.1016/s0925-8388(01)01990-9:Fe2Sm  
_tdb: _tdb:FeSm-02Zin.tdb:FE2SM_C15, tdb:FeSm-17Che.tdb:FE2SM_C15  


### TDB models of FE2SM_C15 (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): FE2SM_C15, type code %A, sha256 `f9381a4b6ae265f7…`

~~~~text
61: PHASE FE2SM_C15 %A 2 2 1 !
62: CONST FE2SM_C15 : FE : SM : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): FE2SM_C15, type code %A, sha256 `ee2803e2feb0f407…`

~~~~text
59: PHASE FE2SM_C15 %A 2 2 1 !
60: CONST FE2SM_C15 : FE : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(71)90124-x](https://doi.org/10.1016/0022-5088%2871%2990124-x) K.H.J. Buschow, The samarium-iron system, Journal of the Less Common Metals 25, 131-134 (1971).  
_cited as the source of values for this phase_

## FE3SM (Fe–Sm)

- Id: `phase:fe-sm:fe3sm`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7500, Sm 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1286.86 K, x(Sm) 0.25–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:fe3sm)

Names (4): _corpus: _corpus:phase:fe-sm:fe3sm  
_paper: _paper:10.1016/s0925-8388(01)01990-9:Fe3Sm  
_tdb: _tdb:FeSm-02Zin.tdb:FE3SM, tdb:FeSm-17Che.tdb:FE3SM  


### TDB models of FE3SM (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): FE3SM, type code %A, sha256 `f9381a4b6ae265f7…`

~~~~text
56: PHASE FE3SM %A 2 3 1 !
57: CONST FE3SM : FE : SM : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): FE3SM, type code %A, sha256 `ee2803e2feb0f407…`

~~~~text
54: PHASE FE3SM %A 2 3 1 !
55: CONST FE3SM : FE : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(71)90124-x](https://doi.org/10.1016/0022-5088%2871%2990124-x) K.H.J. Buschow, The samarium-iron system, Journal of the Less Common Metals 25, 131-134 (1971).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Sm)

- Id: `phase:fe-sm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 977–1196 K, x(Sm) 0.34–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:hcp-a3)

Names (3): _corpus: _corpus:phase:fe-sm:hcp-a3  
_tdb: _tdb:FeSm-02Zin.tdb:HCP_A3, tdb:FeSm-17Che.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): HCP_A3, type code %A, sha256 `f9381a4b6ae265f7…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE SM% : VA : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): HCP_A3, type code %A, sha256 `ee2803e2feb0f407…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE SM% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase_

## LIQUID (Fe–Sm)

- Id: `phase:fe-sm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 994.67–2500 K, x(Sm) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:liquid)

Names (4): _corpus: _corpus:phase:fe-sm:liquid  
_paper: _paper:10.1016/s0925-8388(01)01990-9:Liquid  
_tdb: _tdb:FeSm-02Zin.tdb:LIQUID, tdb:FeSm-17Che.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): LIQUID, type code %, sha256 `f9381a4b6ae265f7…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE SM : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): LIQUID, type code %, sha256 `ee2803e2feb0f407…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(71)90124-x](https://doi.org/10.1016/0022-5088%2871%2990124-x) K.H.J. Buschow, The samarium-iron system, Journal of the Less Common Metals 25, 131-134 (1971).  
_cited as the source of values for this phase_

## RHOMB_C19 (Fe–Sm)

- Id: `phase:fe-sm:rhomb-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1192.36 K, x(Sm) 0.99953–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sm:rhomb-c19)

Names (4): _corpus: _corpus:phase:fe-sm:rhomb-c19  
_paper: _paper:10.1016/s0925-8388(01)01990-9:α-Sm  
_tdb: _tdb:FeSm-02Zin.tdb:RHOMB_C19, tdb:FeSm-17Che.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (2): PHASE and CONSTITUENT statements as written

[FeSm-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-02Zin.tdb): RHOMB_C19, type code %, sha256 `f9381a4b6ae265f7…`

~~~~text
46: PHASE RHOMB_C19 % 1 1 !
47: CONST RHOMB_C19 : FE SM% : !
~~~~

[FeSm-17Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSm-17Che.tdb): RHOMB_C19, type code %, sha256 `ee2803e2feb0f407…`

~~~~text
44: PHASE RHOMB_C19 % 1 1 !
45: CONST RHOMB_C19 : SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.07.005](https://doi.org/10.1016/j.calphad.2017.07.005) X.L. Chen, J. Wang, T.L. Chen, X.D. Lin, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 58, 151-59(2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(71)90124-x](https://doi.org/10.1016/0022-5088%2871%2990124-x) K.H.J. Buschow, The samarium-iron system, Journal of the Less Common Metals 25, 131-134 (1971).  
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
