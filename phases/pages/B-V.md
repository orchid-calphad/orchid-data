# B–V phases

> B–V system: 11 phases (tier A 5, tier B 1, tier C 3, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-V.html · Markdown: https://data.orchid-project.org/phases/pages/B-V.md

11 phases (tier A 5, tier B 1, tier C 3, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-V) · [full JSON](https://data.orchid-project.org/phases/systems/B-V.json) · [B–V system page](https://data.orchid-project.org/systems/B-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–V system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-v-b-beta-rhombo); _phase:b-v:b-beta-rhombo_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–2405.36 K, x(B) 1–1 | 0 | 4 |
| [MB_B33](#phase-b-v-b33-mb); _phase:b-v:b33-mb_ | CrB · B33 · oC8 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–2858.84 K, x(B) 0.5–0.5 | 1 | 4 |
| [BCC_A2](#phase-b-v-bcc-a2); _phase:b-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.94 K, x(B) 0–0.00786 | 0 | 4 |
| [MB2_C32](#phase-b-v-c32-mb2); _phase:b-v:c32-mb2_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–3040 K, x(B) 0.66667–0.66667 | 1 | 4 |
| [FCC_A1](#phase-b-v-fcc-a1); _phase:b-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-b-v-hcp-a3); _phase:b-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-b-v-liquid); _phase:b-v:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 2004.56–4000 K, x(B) 0–1 | 14 | 4 |
| [V2B3](#phase-b-v-v2b3); _phase:b-v:v2b3_ | V2B3 · oC20 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–2923.06 K, x(B) 0.6–0.6 | 0 | 4 |
| [V3B2_D5A](#phase-b-v-v3b2-d5a); _phase:b-v:v3b2-d5a_ | Si2U3 · D5_a · tP10 · P4/mbm (127) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2195.92 K, x(B) 0.4–0.4 | 1 | 4 |
| [V3B4_D7B](#phase-b-v-v3b4-d7b); _phase:b-v:v3b4-d7b_ | Ta3B4 · D7_b · oI14 · Immm (71) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2912.58 K, x(B) 0.57143–0.57143 | 1 | 4 |
| [V5B6](#phase-b-v-v5b6); _phase:b-v:v5b6_ | V5B6 · oC22 · Cmmm (65) | tier B: DFT-supported (unique MP + OQMD match) | stable in 4 of 4 calculated diagram(s): 300–2857.7 K, x(B) 0.54545–0.54545 | 2 | 4 |

## BETA_RHOMBO_B (B–V)

- Id: `phase:b-v:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — VB-12Hom.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — VB-17Pin.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — VB-81Spe.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — VB-91Pan-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2405.36 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:b-beta-rhombo)

Names (5): _corpus: _corpus:phase:b-v:b-beta-rhombo  
_tdb: _tdb:VB-12Hom.tdb:BETA_RHOMBO_B, tdb:VB-17Pin.tdb:BETA_RHOMBO_B, tdb:VB-81Spe.tdb:BETA_RHOMBO_B, tdb:VB-91Pan-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): BETA_RHOMBO_B, type code %, sha256 `5dc15917ed367b37…`

~~~~text
46: PHASE BETA_RHOMBO_B % 1 1 !
47: CONST BETA_RHOMBO_B : B : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): BETA_RHOMBO_B, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
44: PHASE BETA_RHOMBO_B % 1 1 !
45: CONST BETA_RHOMBO_B : B : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): BETA_RHOMBO_B, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
48: PHASE BETA_RHOMBO_B % 1 1 !
49: CONST BETA_RHOMBO_B : B : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
40: PHASE BETA_RHOMBO_B % 1 1 !
41: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## MB_B33 (B–V)

- Id: `phase:b-v:b33-mb`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MB, no_structure_token, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5000, V 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2858.84 K, x(B) 0.5–0.5
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:b33-mb)

Names (6): _corpus: _corpus:phase:b-v:b33-mb  
_paper: _paper:10.1016/0022-5088(81)90224-1:VB  
_tdb: _tdb:VB-12Hom.tdb:MB_B33, tdb:VB-17Pin.tdb:MB_B33, tdb:VB-81Spe.tdb:MB_B33, tdb:VB-91Pan-LB.tdb:MB_B33  


### TDB models of MB_B33 (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): MB_B33, type code %, sha256 `5dc15917ed367b37…`

~~~~text
56: PHASE MB_B33 % 2 1 1 !
57: CONST MB_B33 : V : B : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): MB_B33, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
54: PHASE MB_B33 % 2 1 1 !
55: CONST MB_B33 : V : B : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): MB_B33, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
58: PHASE MB_B33 % 2 1 1 !
59: CONST MB_B33 : V : B : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): MB_B33, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
50: PHASE MB_B33 % 2 1 1 !
51: CONST MB_B33 : V : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## BCC_A2 (B–V)

- Id: `phase:b-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.94 K, x(B) 0–0.00786
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:bcc-a2)

Names (5): _corpus: _corpus:phase:b-v:bcc-a2  
_tdb: _tdb:VB-12Hom.tdb:BCC_A2, tdb:VB-17Pin.tdb:BCC_A2, tdb:VB-81Spe.tdb:BCC_A2, tdb:VB-91Pan-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): BCC_A2, type code %B, sha256 `5dc15917ed367b37…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : V : B VA% : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): BCC_A2, type code %B, sha256 `672a0c551b49a3b2…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : V : B VA% : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): BCC_A2, type code %B, sha256 `3d2fe26a3074d813…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : V : VA : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): BCC_A2, type code %B, sha256 `6135bb1fbdaf1397…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : V : B VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## MB2_C32 (B–V)

- Id: `phase:b-v:c32-mb2`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaaacfj and oqmd-109274, space group 191
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MB2); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.6667, V 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–3040 K, x(B) 0.66667–0.66667
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:c32-mb2)

Names (8): _corpus: _corpus:phase:b-v:c32-mb2  
_mp: _mp:mp-aaaaacfj  
_oqmd: _oqmd:oqmd-109274  
_paper: _paper:10.1016/0022-5088(81)90224-1:VB2  
_tdb: _tdb:VB-12Hom.tdb:MB2_C32, tdb:VB-17Pin.tdb:MB2_C32, tdb:VB-81Spe.tdb:MB2_C32, tdb:VB-91Pan-LB.tdb:MB2_C32  


### TDB models of MB2_C32 (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): MB2_C32, type code %, sha256 `5dc15917ed367b37…`

~~~~text
76: PHASE MB2_C32 % 2 1 2 !
77: CONST MB2_C32 : V : B : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): MB2_C32, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
74: PHASE MB2_C32 % 2 1 2 !
75: CONST MB2_C32 : V : B : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): MB2_C32, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
78: PHASE MB2_C32 % 2 1 2 !
79: CONST MB2_C32 : V : B : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): MB2_C32, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
70: PHASE MB2_C32 % 2 1 2 !
71: CONST MB2_C32 : V : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## FCC_A1 (B–V)

- Id: `phase:b-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:fcc-a1)

Names (5): _corpus: _corpus:phase:b-v:fcc-a1  
_tdb: _tdb:VB-12Hom.tdb:FCC_A1, tdb:VB-17Pin.tdb:FCC_A1, tdb:VB-81Spe.tdb:FCC_A1, tdb:VB-91Pan-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): FCC_A1, type code %A, sha256 `5dc15917ed367b37…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : V : B VA% : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): FCC_A1, type code %A, sha256 `672a0c551b49a3b2…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : V : B VA% : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): FCC_A1, type code %A, sha256 `3d2fe26a3074d813…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : V : VA : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): FCC_A1, type code %A, sha256 `6135bb1fbdaf1397…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : V : B VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## HCP_A3 (B–V)

- Id: `phase:b-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:hcp-a3)

Names (5): _corpus: _corpus:phase:b-v:hcp-a3  
_tdb: _tdb:VB-12Hom.tdb:HCP_A3, tdb:VB-17Pin.tdb:HCP_A3, tdb:VB-81Spe.tdb:HCP_A3, tdb:VB-91Pan-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): HCP_A3, type code %A, sha256 `5dc15917ed367b37…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : V : B VA% : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): HCP_A3, type code %A, sha256 `672a0c551b49a3b2…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : V : B VA% : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): HCP_A3, type code %A, sha256 `3d2fe26a3074d813…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : V : VA : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): HCP_A3, type code %A, sha256 `6135bb1fbdaf1397…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : V : B VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## LIQUID (B–V)

- Id: `phase:b-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 2004.56–4000 K, x(B) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:liquid)

Names (6): _corpus: _corpus:phase:b-v:liquid  
_paper: _paper:10.1016/0022-5088(81)90224-1:L  
_tdb: _tdb:VB-12Hom.tdb:LIQUID, tdb:VB-17Pin.tdb:LIQUID, tdb:VB-81Spe.tdb:LIQUID, tdb:VB-91Pan-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): LIQUID, type code %, sha256 `5dc15917ed367b37…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : B V : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): LIQUID, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B V : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): LIQUID, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : B V : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): LIQUID, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : B V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## V2B3 (B–V)

- Id: `phase:b-v:v2b3`; status `assigned`
- Structure: V2B3 · oC20 · Cmcm (63); type `st:v2b3-oc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.6000, V 0.4000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2923.06 K, x(B) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:v2b3)

Names (5): _corpus: _corpus:phase:b-v:v2b3  
_tdb: _tdb:VB-12Hom.tdb:V2B3, tdb:VB-17Pin.tdb:V2B3, tdb:VB-81Spe.tdb:V2B3, tdb:VB-91Pan-LB.tdb:V2B3  


### TDB models of V2B3 (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): V2B3, type code %, sha256 `5dc15917ed367b37…`

~~~~text
71: PHASE V2B3 % 2 2 3 !
72: CONST V2B3 : V : B : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): V2B3, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
69: PHASE V2B3 % 2 2 3 !
70: CONST V2B3 : V : B : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): V2B3, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
73: PHASE V2B3 % 2 2 3 !
74: CONST V2B3 : V : B : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): V2B3, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
65: PHASE V2B3 % 2 2 3 !
66: CONST V2B3 : V : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## V3B2_D5A (B–V)

- Id: `phase:b-v:v3b2-d5a`; status `assigned`
- Structure: Si2U3 · D5_a · tP10 · P4/mbm (127); type `st:d5-a-si2u3-tp10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadcl and oqmd-18594, space group 127
- Stoichiometry: B 0.4000, V 0.6000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2195.92 K, x(B) 0.4–0.4
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:v3b2-d5a)

Names (8): _corpus: _corpus:phase:b-v:v3b2-d5a  
_mp: _mp:mp-aaaaadcl  
_oqmd: _oqmd:oqmd-18594  
_paper: _paper:10.1016/0022-5088(81)90224-1:V3B2  
_tdb: _tdb:VB-12Hom.tdb:V3B2_D5A, tdb:VB-17Pin.tdb:V3B2_D5A, tdb:VB-81Spe.tdb:V3B2_D5A, tdb:VB-91Pan-LB.tdb:V3B2_D5A  


### TDB models of V3B2_D5A (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): V3B2_D5A, type code %, sha256 `5dc15917ed367b37…`

~~~~text
51: PHASE V3B2_D5A % 2 3 2 !
52: CONST V3B2_D5A : V : B : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): V3B2_D5A, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
49: PHASE V3B2_D5A % 2 3 2 !
50: CONST V3B2_D5A : V : B : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): V3B2_D5A, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
53: PHASE V3B2_D5A % 2 3 2 !
54: CONST V3B2_D5A : V : B : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): V3B2_D5A, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
45: PHASE V3B2_D5A % 2 3 2 !
46: CONST V3B2_D5A : V : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## V3B4_D7B (B–V)

- Id: `phase:b-v:v3b4-d7b`; status `assigned`
- Structure: Ta3B4 · D7_b · oI14 · Immm (71); type `st:d7-b-ta3b4-oi14`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgkda and oqmd-28626, space group 71
- Stoichiometry: B 0.5714, V 0.4286
- Stability: stable in 4 of 4 calculated diagram(s): 300–2912.58 K, x(B) 0.57143–0.57143
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:v3b4-d7b)

Names (8): _corpus: _corpus:phase:b-v:v3b4-d7b  
_mp: _mp:mp-aaabgkda  
_oqmd: _oqmd:oqmd-28626  
_paper: _paper:10.1016/0022-5088(81)90224-1:V3B4  
_tdb: _tdb:VB-12Hom.tdb:V3B4_D7B, tdb:VB-17Pin.tdb:V3B4_D7B, tdb:VB-81Spe.tdb:V3B4_D7B, tdb:VB-91Pan-LB.tdb:V3B4_D7B  


### TDB models of V3B4_D7B (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): V3B4_D7B, type code %, sha256 `5dc15917ed367b37…`

~~~~text
66: PHASE V3B4_D7B % 2 3 4 !
67: CONST V3B4_D7B : V : B : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): V3B4_D7B, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
64: PHASE V3B4_D7B % 2 3 4 !
65: CONST V3B4_D7B : V : B : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): V3B4_D7B, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
68: PHASE V3B4_D7B % 2 3 4 !
69: CONST V3B4_D7B : V : B : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): V3B4_D7B, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
60: PHASE V3B4_D7B % 2 3 4 !
61: CONST V3B4_D7B : V : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
_assessment that models this phase_

## V5B6 (B–V)

- Id: `phase:b-v:v5b6`; status `assigned`
- Structure: V5B6 · oC22 · Cmmm (65); type `st:v5b6-oc22`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: B 0.5455, V 0.4545
- Stability: stable in 4 of 4 calculated diagram(s): 300–2857.7 K, x(B) 0.54545–0.54545
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-v:v5b6)

Names (8): _corpus: _corpus:phase:b-v:v5b6  
_mp: _mp:mp-aaacqqrp  
_oqmd: _oqmd:oqmd-1454661  
_paper: _paper:10.1016/0022-5088(81)90224-1:V5B6  
_tdb: _tdb:VB-12Hom.tdb:V5B6, tdb:VB-17Pin.tdb:V5B6, tdb:VB-81Spe.tdb:V5B6, tdb:VB-91Pan-LB.tdb:V5B6  


### TDB models of V5B6 (4): PHASE and CONSTITUENT statements as written

[VB-12Hom.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-12Hom.tdb): V5B6, type code %, sha256 `5dc15917ed367b37…`

~~~~text
61: PHASE V5B6 % 2 5 6 !
62: CONST V5B6 : V : B : !
~~~~

[VB-17Pin.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-17Pin.tdb): V5B6, type code %, sha256 `672a0c551b49a3b2…`

~~~~text
59: PHASE V5B6 % 2 5 6 !
60: CONST V5B6 : V : B : !
~~~~

[VB-81Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-81Spe.tdb): V5B6, type code %, sha256 `3d2fe26a3074d813…`

~~~~text
63: PHASE V5B6 % 2 5 6 !
64: CONST V5B6 : V : B : !
~~~~

[VB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VB-91Pan-LB.tdb): V5B6, type code %, sha256 `6135bb1fbdaf1397…`

~~~~text
55: PHASE V5B6 % 2 5 6 !
56: CONST V5B6 : V : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(81)90224-1](https://doi.org/10.1016/0022-5088%2881%2990224-1) K.E. Spear, J.H. Blanks, M.S. Wang, Thermodynamic modeling of the VB system, Journal of the Less Common Metals 82, 237-243 (1981).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.10.001](https://doi.org/10.1016/j.calphad.2017.10.001) A.A.A. Pinto da Silva, N. Chaia, F. Ferreira, G.C. Coelho, J.-M. Fiorani, N. David, M. Vilasi, C.A. Nunes, Calphad, 59, 199-206(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2011.11.155](https://doi.org/10.1016/j.jallcom.2011.11.155) Viera Homolová, Aleš Kroupa, Anna Výrostková, Calculation of Fe–B–V ternary phase diagram, Journal of Alloys and Compounds 520, 30-35 (2012).  
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
