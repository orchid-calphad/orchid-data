# Al–Er phases

> Al–Er system: 10 phases (tier A 6, tier B 1, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-ER.html · Markdown: https://data.orchid-project.org/phases/pages/AL-ER.md

10 phases (tier A 6, tier B 1, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-ER) · [full JSON](https://data.orchid-project.org/phases/systems/AL-ER.json) · [Al–Er system page](https://data.orchid-project.org/systems/AL-ER.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-ER.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Er system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2ER_C15](#phase-al-er-al2er-c15); _phase:al-er:al2er-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1731.83 K, x(Er) 0.31411–0.35442 | 0 | 2 |
| [AL2ER3](#phase-al-er-al2er3); _phase:al-er:al2er3_ | Al2Zr3 · tP20 · P4_2/mnm (136) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1357.07 K, x(Er) 0.6–0.6 | 1 | 2 |
| [AL3ER](#phase-al-er-al3er); _phase:al-er:al3er_ | Al3Ho · hR20 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1383.85 K, x(Er) 0.25–0.25 | 0 | 1 |
| [AL3ER_L12](#phase-al-er-al3er-l12); _phase:al-er:al3er-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1277.87 K, x(Er) 0.25–0.25 | 0 | 1 |
| [ALER](#phase-al-er-aler); _phase:al-er:aler_ | AlDy · oP16 · Pbcm (57) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–1410.22 K, x(Er) 0.5–0.5 | 3 | 2 |
| [ALER2_C37](#phase-al-er-aler2-c37); _phase:al-er:aler2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1329.58 K, x(Er) 0.66667–0.66667 | 0 | 2 |
| [BCC_A2](#phase-al-er-bcc-a2); _phase:al-er:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-al-er-fcc-a1); _phase:al-er:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–949.47 K, x(Er) 0–0 | 0 | 2 |
| [HCP_A3](#phase-al-er-hcp-a3); _phase:al-er:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.68 K, x(Er) 0.99947–1 | 0 | 2 |
| [LIQUID](#phase-al-er-liquid); _phase:al-er:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 912.03–2500 K, x(Er) 0–1 | 0 | 2 |

## AL2ER_C15 (Al–Er)

- Id: `phase:al-er:al2er-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlEr-02Cac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlEr-22Xu.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1731.83 K, x(Er) 0.31411–0.35442
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:al2er-c15)

Names (3): _corpus: _corpus:phase:al-er:al2er-c15  
_tdb: _tdb:AlEr-02Cac.tdb:AL2ER_C15, tdb:AlEr-22Xu.tdb:AL2ER_C15  


### TDB models of AL2ER_C15 (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): AL2ER_C15, type code %, sha256 `263c39948e36dfd7…`

~~~~text
64: PHASE AL2ER_C15 % 2 2 1 !
65: CONST AL2ER_C15 : AL% ER : AL ER% : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): AL2ER_C15, type code %, sha256 `fa89fd62a159d002…`

~~~~text
47: PHASE AL2ER_C15 % 2 2 1 !
48: CONST AL2ER_C15 : AL% ER : AL ER% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## AL2ER3 (Al–Er)

- Id: `phase:al-er:al2er3`; status `assigned`
- Structure: Al2Zr3 · tP20 · P4_2/mnm (136); type `st:al2zr3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Er 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1357.07 K, x(Er) 0.6–0.6
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:al2er3)

Names (4): _corpus: _corpus:phase:al-er:al2er3  
_paper: _paper:10.1016/j.calphad.2008.05.002:Al2Er3  
_tdb: _tdb:AlEr-02Cac.tdb:AL2ER3, tdb:AlEr-22Xu.tdb:AL2ER3  


### TDB models of AL2ER3 (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): AL2ER3, type code %, sha256 `263c39948e36dfd7…`

~~~~text
74: PHASE AL2ER3 % 2 2 3 !
75: CONST AL2ER3 : AL : ER : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): AL2ER3, type code %, sha256 `fa89fd62a159d002…`

~~~~text
57: PHASE AL2ER3 % 2 2 3 !
58: CONST AL2ER3 : AL : ER : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.05.002](https://doi.org/10.1016/j.calphad.2008.05.002) L.G. Zhang, L.B. Liu, G.X. Huang, H.Y. Qi, B.R. Jia, Z.P. Jin, Thermodynamic assessment of the Al–Cu–Er system, Calphad 32, 527-534 (2008).  
_reports values for this phase_

## AL3ER (Al–Er)

- Id: `phase:al-er:al3er`; status `assigned`
- Structure: Al3Ho · hR20 · R-3m (166); type `st:al3ho-hr20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.7500, Er 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1383.85 K, x(Er) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:al3er)

Names (2): _corpus: _corpus:phase:al-er:al3er  
_tdb: _tdb:AlEr-22Xu.tdb:AL3ER  


### TDB models of AL3ER (1): PHASE and CONSTITUENT statements as written

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): AL3ER, type code %, sha256 `fa89fd62a159d002…`

~~~~text
42: PHASE AL3ER % 2 3 1 !
43: CONST AL3ER : AL : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_

## AL3ER_L12 (Al–Er)

- Id: `phase:al-er:al3er-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.7500, Er 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1277.87 K, x(Er) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:al3er-l12)

Names (2): _corpus: _corpus:phase:al-er:al3er-l12  
_tdb: _tdb:AlEr-02Cac.tdb:AL3ER_L12  


### TDB models of AL3ER_L12 (1): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): AL3ER_L12, type code %, sha256 `263c39948e36dfd7…`

~~~~text
59: PHASE AL3ER_L12 % 2 3 1 !
60: CONST AL3ER_L12 : AL : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## ALER (Al–Er)

- Id: `phase:al-er:aler`; status `assigned`
- Structure: AlDy · oP16 · Pbcm (57); type `st:aldy-op16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.5000, Er 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1410.22 K, x(Er) 0.5–0.5
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:aler)

Names (6): _corpus: _corpus:phase:al-er:aler  
_mp: _mp:mp-aaacpqmt  
_oqmd: _oqmd:oqmd-658342  
_paper: _paper:10.1016/j.calphad.2008.05.002:AlEr  
_tdb: _tdb:AlEr-02Cac.tdb:ALER, tdb:AlEr-22Xu.tdb:ALER  


### TDB models of ALER (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): ALER, type code %, sha256 `263c39948e36dfd7…`

~~~~text
69: PHASE ALER % 2 1 1 !
70: CONST ALER : AL : ER : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): ALER, type code %, sha256 `fa89fd62a159d002…`

~~~~text
52: PHASE ALER % 2 1 1 !
53: CONST ALER : AL : ER : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.05.002](https://doi.org/10.1016/j.calphad.2008.05.002) L.G. Zhang, L.B. Liu, G.X. Huang, H.Y. Qi, B.R. Jia, Z.P. Jin, Thermodynamic assessment of the Al–Cu–Er system, Calphad 32, 527-534 (2008).  
_reports values for this phase_

## ALER2_C37 (Al–Er)

- Id: `phase:al-er:aler2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacktmh and oqmd-1436042, space group 62
- Stoichiometry: Al 0.3333, Er 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1329.58 K, x(Er) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:aler2-c37)

Names (5): _corpus: _corpus:phase:al-er:aler2-c37  
_mp: _mp:mp-aaacktmh  
_oqmd: _oqmd:oqmd-1436042  
_tdb: _tdb:AlEr-02Cac.tdb:ALER2_C37, tdb:AlEr-22Xu.tdb:ALER2_C37  


### TDB models of ALER2_C37 (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): ALER2_C37, type code %, sha256 `263c39948e36dfd7…`

~~~~text
79: PHASE ALER2_C37 % 2 1 2 !
80: CONST ALER2_C37 : AL : ER : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): ALER2_C37, type code %, sha256 `fa89fd62a159d002…`

~~~~text
62: PHASE ALER2_C37 % 2 1 2 !
63: CONST ALER2_C37 : AL : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## BCC_A2 (Al–Er)

- Id: `phase:al-er:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:bcc-a2)

Names (3): _corpus: _corpus:phase:al-er:bcc-a2  
_tdb: _tdb:AlEr-02Cac.tdb:BCC_A2, tdb:AlEr-22Xu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): BCC_A2, type code %, sha256 `263c39948e36dfd7…`

~~~~text
49: PHASE BCC_A2 % 2 1 3 !
50: CONST BCC_A2 : AL ER : VA : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): BCC_A2, type code %B, sha256 `fa89fd62a159d002…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AL ER : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## FCC_A1 (Al–Er)

- Id: `phase:al-er:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–949.47 K, x(Er) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:fcc-a1)

Names (3): _corpus: _corpus:phase:al-er:fcc-a1  
_tdb: _tdb:AlEr-02Cac.tdb:FCC_A1, tdb:AlEr-22Xu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): FCC_A1, type code %, sha256 `263c39948e36dfd7…`

~~~~text
34: PHASE FCC_A1 % 2 1 1 !
35: CONST FCC_A1 : AL% ER : VA : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): FCC_A1, type code %A, sha256 `fa89fd62a159d002…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AL% ER : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## HCP_A3 (Al–Er)

- Id: `phase:al-er:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.68 K, x(Er) 0.99947–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:hcp-a3)

Names (3): _corpus: _corpus:phase:al-er:hcp-a3  
_tdb: _tdb:AlEr-02Cac.tdb:HCP_A3, tdb:AlEr-22Xu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): HCP_A3, type code %, sha256 `263c39948e36dfd7…`

~~~~text
54: PHASE HCP_A3 % 2 1 0.5 !
55: CONST HCP_A3 : AL ER% : VA : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): HCP_A3, type code %A, sha256 `fa89fd62a159d002…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AL ER% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## LIQUID (Al–Er)

- Id: `phase:al-er:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 912.03–2500 K, x(Er) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-er:liquid)

Names (3): _corpus: _corpus:phase:al-er:liquid  
_tdb: _tdb:AlEr-02Cac.tdb:LIQUID, tdb:AlEr-22Xu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AlEr-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-02Cac.tdb): LIQUID, type code %, sha256 `263c39948e36dfd7…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AL ER : !
~~~~

[AlEr-22Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlEr-22Xu.tdb): LIQUID, type code %, sha256 `fa89fd62a159d002…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AL ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102482](https://doi.org/10.1016/j.calphad.2022.102482) L. Xu, X. Shi, D. Xia, D. Huang, H. Tang, Calphad, 79, 102482(2022).  
_assessment that models this phase_
- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

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
