# C–V phases

> C–V system: 11 phases (tier A 5, tier C 4, liquid 1, unresolved_no_candidates 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-V.html · Markdown: https://data.orchid-project.org/phases/pages/C-V.md

11 phases (tier A 5, tier C 4, liquid 1, unresolved_no_candidates 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-V) · [full JSON](https://data.orchid-project.org/phases/systems/C-V.json) · [C–V system page](https://data.orchid-project.org/systems/C-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–V system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-v-a4-diamond); _phase:c-v:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GRAPHITE_A9](#phase-c-v-a9-graphite); _phase:c-v:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 3 |
| [BCC_A2](#phase-c-v-bcc-a2); _phase:c-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2198 K, x(C) 0–0.0383 | 4 | 3 |
| [FCC_A1](#phase-c-v-fcc-a1); _phase:c-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 4 calculated diagram(s): 300–2931.49 K, x(C) 0.37104–0.49502 | 19 | 4 |
| [HCP_A3](#phase-c-v-hcp-a3); _phase:c-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2466.49 K, x(C) 0.28161–0.33333 | 12 | 3 |
| [LIQUID](#phase-c-v-liquid); _phase:c-v:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1920.76–4000 K, x(C) 0–0.64671 | 18 | 3 |
| [V3C2](#phase-c-v-v3c2); _phase:c-v:v3c2_ | Sc2Te3 · hR8 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1591.67 K, x(C) 0.4–0.4 | 0 | 2 |
| [V4C3](#phase-c-v-v4c3); _phase:c-v:v4c3_ | Sc2Te3 · hR8 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1534.2–2150 K, x(C) 0.379–0.379 | 4 | 1 |
| [V6C5](#phase-c-v-v6c5); _phase:c-v:v6c5_ | V6C5 · hP33 · P3_112 (151) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2931.49 K, x(C) 0.37104–0.47241 | 13 | 1 |
| [V6C5-2](#phase-c-v-v6c5-2); _phase:c-v:v6c5-2_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |
| [V8C7](#phase-c-v-v8c7); _phase:c-v:v8c7_ | V8C7 · cP60 · P4_132 (213) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 647.96–1381.99 K, x(C) 0.46667–0.46667 | 11 | 1 |

## DIAMOND_A4 (C–V)

- Id: `phase:c-v:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:a4-diamond)

Names (4): _corpus: _corpus:phase:c-v:a4-diamond  
_tdb: _tdb:VC-06Hu.tdb:DIAMOND_A4, tdb:VC-20Hua.tdb:DIAMOND_A4, tdb:VC-91Hua-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): DIAMOND_A4, type code %, sha256 `b64d86a071f73e7b…`

~~~~text
53: PHASE DIAMOND_A4 % 1 1 !
54: CONST DIAMOND_A4 : C : !
~~~~

[VC-20Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-20Hua.tdb): DIAMOND_A4, type code %, sha256 `b82a6e368e3b247d…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : C : !
~~~~

[VC-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-91Hua-LB.tdb): DIAMOND_A4, type code %, sha256 `7ade7709e53a562d…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.102199](https://doi.org/10.1016/j.calphad.2020.102199) L. Huang, Y. Pan, J. Zhang, Y. Du, F. Luo, P. Zhou, S. Zhang, Calphad, 71, 102199(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820303](https://doi.org/10.1515/ijmr-1991-820303) W. Huang, Z. Metallkd., 82, 174-81(1991).  
_assessment that models this phase_

## GRAPHITE_A9 (C–V)

- Id: `phase:c-v:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:a9-graphite)

Names (5): _corpus: _corpus:phase:c-v:a9-graphite, corpus:phase:c-v:graphite-a9  
_tdb: _tdb:VC-06Hu.tdb:GRAPHITE_A9, tdb:VC-20Hua.tdb:GRAPHITE_A9, tdb:VC-91Hua-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (3): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): GRAPHITE_A9, type code %, sha256 `b64d86a071f73e7b…`

~~~~text
58: PHASE GRAPHITE_A9 % 1 1 !
59: CONST GRAPHITE_A9 : C : !
~~~~

[VC-20Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-20Hua.tdb): GRAPHITE_A9, type code %, sha256 `b82a6e368e3b247d…`

~~~~text
52: PHASE GRAPHITE_A9 % 1 1 !
53: CONST GRAPHITE_A9 : C : !
~~~~

[VC-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-91Hua-LB.tdb): GRAPHITE_A9, type code %, sha256 `7ade7709e53a562d…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.102199](https://doi.org/10.1016/j.calphad.2020.102199) L. Huang, Y. Pan, J. Zhang, Y. Du, F. Luo, P. Zhou, S. Zhang, Calphad, 71, 102199(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820303](https://doi.org/10.1515/ijmr-1991-820303) W. Huang, Z. Metallkd., 82, 174-81(1991).  
_assessment that models this phase_

## BCC_A2 (C–V)

- Id: `phase:c-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2198 K, x(C) 0–0.0383
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:bcc-a2)

Names (5): _corpus: _corpus:phase:c-v:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2005.11.033:bcc-(V)  
_tdb: _tdb:VC-06Hu.tdb:BCC_A2, tdb:VC-20Hua.tdb:BCC_A2, tdb:VC-91Hua-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): BCC_A2, type code %B, sha256 `b64d86a071f73e7b…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : V : C VA% : !
~~~~

[VC-20Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-20Hua.tdb): BCC_A2, type code %B, sha256 `b82a6e368e3b247d…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : V : C VA% : !
~~~~

[VC-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-91Hua-LB.tdb): BCC_A2, type code %B, sha256 `7ade7709e53a562d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : V : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102199](https://doi.org/10.1016/j.calphad.2020.102199) L. Huang, Y. Pan, J. Zhang, Y. Du, F. Luo, P. Zhou, S. Zhang, Calphad, 71, 102199(2020).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820303](https://doi.org/10.1515/ijmr-1991-820303) W. Huang, Z. Metallkd., 82, 174-81(1991).  
_assessment that models this phase_
- [doi:10.1021/j100814a007](https://doi.org/10.1021/j100814a007) E. K. Storms, R. J. McNeal, THE VANADIUM-VANADIUM CARBIDE SYSTEM\<sup>1\</sup>, J. Phys. Chem. 66, 1401-1408 (1962).  
_cited as the source of values for this phase_

## FCC_A1 (C–V)

- Id: `phase:c-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 4 calculated diagram(s): 300–2931.49 K, x(C) 0.37104–0.49502
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:fcc-a1)

Names (6): _corpus: _corpus:phase:c-v:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2005.11.033:VCx  
_tdb: _tdb:VC-06Hu.tdb:A1_FCC, tdb:VC-06Hu.tdb:FCC_A1, tdb:VC-20Hua.tdb:FCC_A1, tdb:VC-91Hua-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): A1_FCC, type code %A, sha256 `b64d86a071f73e7b…`

~~~~text
38: PHASE A1_FCC %A 2 1 1 !
39: CONST A1_FCC : C% VA : V : !
~~~~

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): FCC_A1, type code %A, sha256 `b64d86a071f73e7b…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : V : C% VA : !
~~~~

[VC-20Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-20Hua.tdb): FCC_A1, type code %A, sha256 `b82a6e368e3b247d…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : V : C VA% : !
~~~~

[VC-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-91Hua-LB.tdb): FCC_A1, type code %A, sha256 `7ade7709e53a562d…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : V : C VA% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102199](https://doi.org/10.1016/j.calphad.2020.102199) L. Huang, Y. Pan, J. Zhang, Y. Du, F. Luo, P. Zhou, S. Zhang, Calphad, 71, 102199(2020).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820303](https://doi.org/10.1515/ijmr-1991-820303) W. Huang, Z. Metallkd., 82, 174-81(1991).  
_assessment that models this phase_
- [doi:10.1021/j100814a007](https://doi.org/10.1021/j100814a007) E. K. Storms, R. J. McNeal, THE VANADIUM-VANADIUM CARBIDE SYSTEM\<sup>1\</sup>, J. Phys. Chem. 66, 1401-1408 (1962).  
_cited as the source of values for this phase_
- [doi:10.1016/s1359-6454(97)00204-8](https://doi.org/10.1016/s1359-6454%2897%2900204-8) H Wiesenberger, W Lengauer, P Ettmayer, Reactive diffusion and phase equilibria in the V–C, Nb–C, Ta–C and Ta–N systems, Acta Materialia 46, 651-666 (1998).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00547575](https://doi.org/10.1007/bf00547575) George H. Emmons, Wendell S. Williams, Thermodynamics of order-disorder transformations in vanadium carbide, J Mater Sci 18, 2589-2602 (1983).  
_cited as the source of values for this phase_
- [doi:10.1088/0953-8984/11/1/014](https://doi.org/10.1088/0953-8984/11/1/014) V N Lipatnikov, A I Gusev, P Ettmayer, W Lengauer, Phase transformations in non-stoichiometric vanadium carbide, J. Phys.: Condens. Matter 11, 163-184 (1999).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.7.5041](https://doi.org/10.1103/physrevb.7.5041) L. W. Shacklette, Wendell S. Williams, Influence of Order-Disorder Transformations on the Electrical Resistivity of Vanadium Carbide, Phys. Rev. B 7, 5041-5053 (1973).  
_cited as the source of values for this phase_

## HCP_A3 (C–V)

- Id: `phase:c-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2466.49 K, x(C) 0.28161–0.33333
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:hcp-a3)

Names (5): _corpus: _corpus:phase:c-v:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2005.11.033:V2C  
_tdb: _tdb:VC-06Hu.tdb:HCP_A3, tdb:VC-20Hua.tdb:HCP_A3, tdb:VC-91Hua-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): HCP_A3, type code %A, sha256 `b64d86a071f73e7b…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : V : C% VA : !
~~~~

[VC-20Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-20Hua.tdb): HCP_A3, type code %A, sha256 `b82a6e368e3b247d…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : V : C VA% : !
~~~~

[VC-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-91Hua-LB.tdb): HCP_A3, type code %A, sha256 `7ade7709e53a562d…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : V : C VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102199](https://doi.org/10.1016/j.calphad.2020.102199) L. Huang, Y. Pan, J. Zhang, Y. Du, F. Luo, P. Zhou, S. Zhang, Calphad, 71, 102199(2020).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820303](https://doi.org/10.1515/ijmr-1991-820303) W. Huang, Z. Metallkd., 82, 174-81(1991).  
_assessment that models this phase_
- [doi:10.1016/s1359-6454(97)00204-8](https://doi.org/10.1016/s1359-6454%2897%2900204-8) H Wiesenberger, W Lengauer, P Ettmayer, Reactive diffusion and phase equilibria in the V–C, Nb–C, Ta–C and Ta–N systems, Acta Materialia 46, 651-666 (1998).  
_cited as the source of values for this phase_
- [doi:10.1021/j100814a007](https://doi.org/10.1021/j100814a007) E. K. Storms, R. J. McNeal, THE VANADIUM-VANADIUM CARBIDE SYSTEM\<sup>1\</sup>, J. Phys. Chem. 66, 1401-1408 (1962).  
_cited as the source of values for this phase_

## LIQUID (C–V)

- Id: `phase:c-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1920.76–4000 K, x(C) 0–0.64671
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:liquid)

Names (6): _corpus: _corpus:phase:c-v:liquid  
_paper: _paper:10.1016/j.jallcom.2005.11.033:Liquid, paper:10.1016/j.jallcom.2005.11.033:liquid  
_tdb: _tdb:VC-06Hu.tdb:LIQUID, tdb:VC-20Hua.tdb:LIQUID, tdb:VC-91Hua-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): LIQUID, type code %, sha256 `b64d86a071f73e7b…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : C V : !
~~~~

[VC-20Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-20Hua.tdb): LIQUID, type code %, sha256 `b82a6e368e3b247d…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : C V : !
~~~~

[VC-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-91Hua-LB.tdb): LIQUID, type code %, sha256 `7ade7709e53a562d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102199](https://doi.org/10.1016/j.calphad.2020.102199) L. Huang, Y. Pan, J. Zhang, Y. Du, F. Luo, P. Zhou, S. Zhang, Calphad, 71, 102199(2020).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820303](https://doi.org/10.1515/ijmr-1991-820303) W. Huang, Z. Metallkd., 82, 174-81(1991).  
_assessment that models this phase_
- [doi:10.1021/j100814a007](https://doi.org/10.1021/j100814a007) E. K. Storms, R. J. McNeal, THE VANADIUM-VANADIUM CARBIDE SYSTEM\<sup>1\</sup>, J. Phys. Chem. 66, 1401-1408 (1962).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00547575](https://doi.org/10.1007/bf00547575) George H. Emmons, Wendell S. Williams, Thermodynamics of order-disorder transformations in vanadium carbide, J Mater Sci 18, 2589-2602 (1983).  
_cited as the source of values for this phase_
- [doi:10.1088/0953-8984/11/1/014](https://doi.org/10.1088/0953-8984/11/1/014) V N Lipatnikov, A I Gusev, P Ettmayer, W Lengauer, Phase transformations in non-stoichiometric vanadium carbide, J. Phys.: Condens. Matter 11, 163-184 (1999).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.7.5041](https://doi.org/10.1103/physrevb.7.5041) L. W. Shacklette, Wendell S. Williams, Influence of Order-Disorder Transformations on the Electrical Resistivity of Vanadium Carbide, Phys. Rev. B 7, 5041-5053 (1973).  
_cited as the source of values for this phase_

## V3C2 (C–V)

- Id: `phase:c-v:v3c2`; status `assigned`
- Structure: Sc2Te3 · hR8 · R-3m (166); type `st:sc2te3-hr8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–1591.67 K, x(C) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:v3c2)

Names (3): _corpus: _corpus:phase:c-v:v3c2  
_tdb: _tdb:VC-20Hua.tdb:V3C2, tdb:VC-91Hua-LB.tdb:V3C2  


### TDB models of V3C2 (2): PHASE and CONSTITUENT statements as written

[VC-20Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-20Hua.tdb): V3C2, type code %, sha256 `b82a6e368e3b247d…`

~~~~text
58: PHASE V3C2 % 2 3 2 !
59: CONST V3C2 : V : C : !
~~~~

[VC-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-91Hua-LB.tdb): V3C2, type code %, sha256 `7ade7709e53a562d…`

~~~~text
56: PHASE V3C2 % 2 3 2 !
57: CONST V3C2 : V : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.102199](https://doi.org/10.1016/j.calphad.2020.102199) L. Huang, Y. Pan, J. Zhang, Y. Du, F. Luo, P. Zhou, S. Zhang, Calphad, 71, 102199(2020).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820303](https://doi.org/10.1515/ijmr-1991-820303) W. Huang, Z. Metallkd., 82, 174-81(1991).  
_assessment that models this phase_

## V4C3 (C–V)

- Id: `phase:c-v:v4c3`; status `assigned`
- Structure: Sc2Te3 · hR8 · R-3m (166); type `st:sc2te3-hr8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 1534.2–2150 K, x(C) 0.379–0.379
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:v4c3)

Names (3): _corpus: _corpus:phase:c-v:v4c3  
_paper: _paper:10.1016/j.jallcom.2005.11.033:V4C3-x  
_tdb: _tdb:VC-06Hu.tdb:V4C3  


### TDB models of V4C3 (1): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): V4C3, type code %, sha256 `b64d86a071f73e7b…`

~~~~text
64: PHASE V4C3 % 2 0.621 0.379 !
65: CONST V4C3 : V : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s1359-6454(97)00204-8](https://doi.org/10.1016/s1359-6454%2897%2900204-8) H Wiesenberger, W Lengauer, P Ettmayer, Reactive diffusion and phase equilibria in the V–C, Nb–C, Ta–C and Ta–N systems, Acta Materialia 46, 651-666 (1998).  
_cited as the source of values for this phase_

## V6C5 (C–V)

- Id: `phase:c-v:v6c5`; status `assigned`
- Structure: V6C5 · hP33 · P3_112 (151); type `st:v6c5-hp33`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–2931.49 K, x(C) 0.37104–0.47241
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:v6c5)

Names (3): _corpus: _corpus:phase:c-v:v6c5  
_paper: _paper:10.1016/j.jallcom.2005.11.033:V6C5  
_tdb: _tdb:VC-06Hu.tdb:V6C5  


### TDB models of V6C5 (1): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): V6C5, type code %AY, sha256 `b64d86a071f73e7b…`

~~~~text
69: PHASE V6C5 %AY 3 0.833333 0.166667 1 !
70: CONST V6C5 : C VA : C VA : V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1088/0953-8984/11/1/014](https://doi.org/10.1088/0953-8984/11/1/014) V N Lipatnikov, A I Gusev, P Ettmayer, W Lengauer, Phase transformations in non-stoichiometric vanadium carbide, J. Phys.: Condens. Matter 11, 163-184 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00547575](https://doi.org/10.1007/bf00547575) George H. Emmons, Wendell S. Williams, Thermodynamics of order-disorder transformations in vanadium carbide, J Mater Sci 18, 2589-2602 (1983).  
_cited as the source of values for this phase_

## V6C5-2 (C–V)

- Id: `phase:c-v:v6c5-2`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:2; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:v6c5-2)

Names (1): _corpus: _corpus:phase:c-v:v6c5-2  


## V8C7 (C–V)

- Id: `phase:c-v:v8c7`; status `assigned`
- Structure: V8C7 · cP60 · P4_132 (213); type `st:v8c7-cp60`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 647.96–1381.99 K, x(C) 0.46667–0.46667
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-v:v8c7)

Names (3): _corpus: _corpus:phase:c-v:v8c7  
_paper: _paper:10.1016/j.jallcom.2005.11.033:V8C7  
_tdb: _tdb:VC-06Hu.tdb:V8C7  


### TDB models of V8C7 (1): PHASE and CONSTITUENT statements as written

[VC-06Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/VC-06Hu.tdb): V8C7, type code %, sha256 `b64d86a071f73e7b…`

~~~~text
74: PHASE V8C7 % 2 1 0.875 !
75: CONST V8C7 : V : C : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.033](https://doi.org/10.1016/j.jallcom.2005.11.033) Jincheng Hu, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic re-assessment of the V–C system, Journal of Alloys and Compounds 421, 120-127 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1088/0953-8984/11/1/014](https://doi.org/10.1088/0953-8984/11/1/014) V N Lipatnikov, A I Gusev, P Ettmayer, W Lengauer, Phase transformations in non-stoichiometric vanadium carbide, J. Phys.: Condens. Matter 11, 163-184 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00547575](https://doi.org/10.1007/bf00547575) George H. Emmons, Wendell S. Williams, Thermodynamics of order-disorder transformations in vanadium carbide, J Mater Sci 18, 2589-2602 (1983).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.7.5041](https://doi.org/10.1103/physrevb.7.5041) L. W. Shacklette, Wendell S. Williams, Influence of Order-Disorder Transformations on the Electrical Resistivity of Vanadium Carbide, Phys. Rev. B 7, 5041-5053 (1973).  
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
