# Ce–Cu phases

> Ce–Cu system: 9 phases (tier A 5, tier C 3, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-CU.html · Markdown: https://data.orchid-project.org/phases/pages/CE-CU.md

9 phases (tier A 5, tier C 3, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-CU) · [full JSON](https://data.orchid-project.org/phases/systems/CE-CU.json) · [Ce–Cu system page](https://data.orchid-project.org/systems/CE-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Cu system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-cu-bcc-a2); _phase:ce-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 980.72–1075 K, x(Cu) 0–0.00716 | 4 | 2 |
| [CECU_B27](#phase-ce-cu-cecu-b27); _phase:ce-cu:cecu-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–788.46 K, x(Cu) 0.5–0.5 | 8 | 2 |
| [CECU2](#phase-ce-cu-cecu2); _phase:ce-cu:cecu2_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1089.95 K, x(Cu) 0.66667–0.66667 | 12 | 2 |
| [CECU4](#phase-ce-cu-cecu4); _phase:ce-cu:cecu4_ | CeCu4 · oP20 · Pnnm (58) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1068.03 K, x(Cu) 0.8–0.8 | 8 | 2 |
| [CECU5_D2D](#phase-ce-cu-cecu5-d2d); _phase:ce-cu:cecu5-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1074.18 K, x(Cu) 0.83333–0.83333 | 8 | 2 |
| [CECU6](#phase-ce-cu-cecu6); _phase:ce-cu:cecu6_ | CeCu6 · oP28 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1211.18 K, x(Cu) 0.85714–0.85714 | 12 | 2 |
| [FCC_A1](#phase-ce-cu-fcc-a1); _phase:ce-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.75 K, x(Cu) 0–1 | 11 | 2 |
| [HCP_A3](#phase-ce-cu-hcp-a3); _phase:ce-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ce-cu-liquid); _phase:ce-cu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 699.98–2500 K, x(Cu) 0–1 | 36 | 2 |

## BCC_A2 (Ce–Cu)

- Id: `phase:ce-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 980.72–1075 K, x(Cu) 0–0.00716
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:bcc-a2)

Names (5): _corpus: _corpus:phase:ce-cu:bcc-a2  
_paper: _paper:10.1007/bf02665998:Ce(bcc), paper:10.1016/j.jallcom.2009.04.083:δCe  
_tdb: _tdb:CeCu-09Bo.tdb:BCC_A2, tdb:CeCu-96Zhu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): BCC_A2, type code %B, sha256 `5e559495ec18884c…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CE% CU : VA : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): BCC_A2, type code %B, sha256 `673f9f27a539576f…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CE% CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## CECU_B27 (Ce–Cu)

- Id: `phase:ce-cu:cecu-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.5000, Cu 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–788.46 K, x(Cu) 0.5–0.5
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:cecu-b27)

Names (5): _corpus: _corpus:phase:ce-cu:cecu-b27  
_paper: _paper:10.1007/bf02665998:CuCe, paper:10.1016/j.jallcom.2009.04.083:CuCe  
_tdb: _tdb:CeCu-09Bo.tdb:CECU_B27, tdb:CeCu-96Zhu.tdb:CECU_B27  


### TDB models of CECU_B27 (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): CECU_B27, type code %, sha256 `5e559495ec18884c…`

~~~~text
46: PHASE CECU_B27 % 2 1 1 !
47: CONST CECU_B27 : CE : CU : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): CECU_B27, type code %, sha256 `673f9f27a539576f…`

~~~~text
47: PHASE CECU_B27 % 2 1 1 !
48: CONST CECU_B27 : CE : CU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## CECU2 (Ce–Cu)

- Id: `phase:ce-cu:cecu2`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.3333, Cu 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1089.95 K, x(Cu) 0.66667–0.66667
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:cecu2)

Names (5): _corpus: _corpus:phase:ce-cu:cecu2  
_paper: _paper:10.1007/bf02665998:Cu2Ce, paper:10.1016/j.jallcom.2009.04.083:Cu2Ce  
_tdb: _tdb:CeCu-09Bo.tdb:CECU2, tdb:CeCu-96Zhu.tdb:CECU2  


### TDB models of CECU2 (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): CECU2, type code %, sha256 `5e559495ec18884c…`

~~~~text
51: PHASE CECU2 % 2 1 2 !
52: CONST CECU2 : CE : CU : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): CECU2, type code %, sha256 `673f9f27a539576f…`

~~~~text
52: PHASE CECU2 % 2 1 2 !
53: CONST CECU2 : CE : CU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## CECU4 (Ce–Cu)

- Id: `phase:ce-cu:cecu4`; status `assigned`
- Structure: CeCu4 · oP20 · Pnnm (58); type `st:cecu4-op20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.2000, Cu 0.8000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1068.03 K, x(Cu) 0.8–0.8
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:cecu4)

Names (5): _corpus: _corpus:phase:ce-cu:cecu4  
_paper: _paper:10.1007/bf02665998:Cu4Ce, paper:10.1016/j.jallcom.2009.04.083:Cu4Ce  
_tdb: _tdb:CeCu-09Bo.tdb:CECU4, tdb:CeCu-96Zhu.tdb:CECU4  


### TDB models of CECU4 (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): CECU4, type code %, sha256 `5e559495ec18884c…`

~~~~text
56: PHASE CECU4 % 2 1 4 !
57: CONST CECU4 : CE : CU : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): CECU4, type code %, sha256 `673f9f27a539576f…`

~~~~text
57: PHASE CECU4 % 2 1 4 !
58: CONST CECU4 : CE : CU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## CECU5_D2D (Ce–Cu)

- Id: `phase:ce-cu:cecu5-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.1667, Cu 0.8333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1074.18 K, x(Cu) 0.83333–0.83333
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:cecu5-d2d)

Names (5): _corpus: _corpus:phase:ce-cu:cecu5-d2d  
_paper: _paper:10.1007/bf02665998:Cu5Ce, paper:10.1016/j.jallcom.2009.04.083:Cu5Ce  
_tdb: _tdb:CeCu-09Bo.tdb:CECU5_D2D, tdb:CeCu-96Zhu.tdb:CECU5_D2D  


### TDB models of CECU5_D2D (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): CECU5_D2D, type code %, sha256 `5e559495ec18884c…`

~~~~text
61: PHASE CECU5_D2D % 2 1 5 !
62: CONST CECU5_D2D : CE : CU : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): CECU5_D2D, type code %, sha256 `673f9f27a539576f…`

~~~~text
62: PHASE CECU5_D2D % 2 1 5 !
63: CONST CECU5_D2D : CE : CU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## CECU6 (Ce–Cu)

- Id: `phase:ce-cu:cecu6`; status `assigned`
- Structure: CeCu6 · oP28 · Pnma (62); type `st:cecu6-op28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.1429, Cu 0.8571
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.18 K, x(Cu) 0.85714–0.85714
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:cecu6)

Names (5): _corpus: _corpus:phase:ce-cu:cecu6  
_paper: _paper:10.1007/bf02665998:Cu6Ce, paper:10.1016/j.jallcom.2009.04.083:Cu6Ce  
_tdb: _tdb:CeCu-09Bo.tdb:CECU6, tdb:CeCu-96Zhu.tdb:CECU6  


### TDB models of CECU6 (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): CECU6, type code %, sha256 `5e559495ec18884c…`

~~~~text
66: PHASE CECU6 % 2 1 6 !
67: CONST CECU6 : CE : CU : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): CECU6, type code %, sha256 `673f9f27a539576f…`

~~~~text
67: PHASE CECU6 % 2 1 6 !
68: CONST CECU6 : CE : CU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## FCC_A1 (Ce–Cu)

- Id: `phase:ce-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.75 K, x(Cu) 0–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:fcc-a1)

Names (7): _corpus: _corpus:phase:ce-cu:fcc-a1  
_paper: _paper:10.1007/bf02665998:Ce(fcc), paper:10.1007/bf02665998:Cu(fcc), paper:10.1016/j.jallcom.2009.04.083:Fcc_Cu, paper:10.1016/j.jallcom.2009.04.083:γCe  
_tdb: _tdb:CeCu-09Bo.tdb:FCC_A1, tdb:CeCu-96Zhu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): FCC_A1, type code %A, sha256 `5e559495ec18884c…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CE% CU% : VA : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): FCC_A1, type code %A, sha256 `673f9f27a539576f…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CE% CU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## HCP_A3 (Ce–Cu)

- Id: `phase:ce-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:ce-cu:hcp-a3  
_tdb: _tdb:CeCu-09Bo.tdb:HCP_A3, tdb:CeCu-96Zhu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): HCP_A3, type code %A, sha256 `5e559495ec18884c…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CE CU% : VA : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): HCP_A3, type code %A, sha256 `673f9f27a539576f…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CE CU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase_

## LIQUID (Ce–Cu)

- Id: `phase:ce-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 699.98–2500 K, x(Cu) 0–1
- Literature: 36 values (36 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-cu:liquid)

Names (5): _corpus: _corpus:phase:ce-cu:liquid  
_paper: _paper:10.1007/bf02665998:L, paper:10.1016/j.jallcom.2009.04.083:L  
_tdb: _tdb:CeCu-09Bo.tdb:LIQUID, tdb:CeCu-96Zhu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CeCu-09Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-09Bo.tdb): LIQUID, type code %, sha256 `5e559495ec18884c…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CE CU : !
~~~~

[CeCu-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCu-96Zhu.tdb): LIQUID, type code %, sha256 `673f9f27a539576f…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CE CU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.083](https://doi.org/10.1016/j.jallcom.2009.04.083) H. Bo, S. Jin, L.G. Zhang, X.M. Chen, H.M. Chen, L.B. Liu et al., Thermodynamic assessment of Al–Ce–Cu system, Journal of Alloys and Compounds 484, 286-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
