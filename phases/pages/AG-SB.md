# Ag–Sb phases

> Ag–Sb system: 6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-SB.html · Markdown: https://data.orchid-project.org/phases/pages/AG-SB.md

6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-SB) · [full JSON](https://data.orchid-project.org/phases/systems/AG-SB.json) · [Ag–Sb system page](https://data.orchid-project.org/systems/AG-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Sb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-ag-sb-a7-rhombohedral); _phase:ag-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 3 | 3 |
| [AG3SB](#phase-ag-sb-ag3sb); _phase:ag-sb:ag3sb_ | Ag3Sb · oP4 · Pmm2 (25) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–835.48 K, x(Sb) 0.21476–0.28056 | 6 | 3 |
| [BCC_A2](#phase-ag-sb-bcc-a2); _phase:ag-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-ag-sb-fcc-a1); _phase:ag-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1238.93 K, x(Sb) 0–0.07459 | 3 | 3 |
| [HCP_A3](#phase-ag-sb-hcp-a3); _phase:ag-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–975.49 K, x(Sb) 0.07993–0.17166 | 6 | 3 |
| [LIQUID](#phase-ag-sb-liquid); _phase:ag-sb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 753.19–2500 K, x(Sb) 0–1 | 9 | 3 |

## RHOMBOHEDRAL_A7 (Ag–Sb)

- Id: `phase:ag-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:ag-sb:a7-rhombohedral, corpus:phase:ag-sb:rhombohedral-a7  
_paper: _paper:10.1007/s11669-007-9085-y:(Sb)  
_tdb: _tdb:AgSb-07Zor.tdb:RHOMBOHEDRAL_A7, tdb:AgSb-94Lee.tdb:RHOMBOHEDRAL_A7, tdb:AgSb-96Oh-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[AgSb-07Zor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-07Zor.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `4a4d3ab63e7357b5…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AgSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-94Lee.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9a293f35c50f2f4c…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AgSb-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-96Oh-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `09269ee847372619…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-007-9085-y](https://doi.org/10.1007/s11669-007-9085-y) E. Zoro, C. Servant, B. Legendre, Thermodynamic Modeling of the Ag-Au-Sb Ternary System, J Phs Eqil and Diff 28, 250-257 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02671976](https://doi.org/10.1007/bf02671976) H. Okamoto, Phase Diagram Updates Ag-Sb (Silver-Antimony), J. Phase Equilibria, 1993, 14, p 531-532  
_cited as the source of values for this phase_

## AG3SB (Ag–Sb)

- Id: `phase:ag-sb:ag3sb`; status `assigned`
- Structure: Ag3Sb · oP4 · Pmm2 (25); type `st:ag3sb-op4`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 300–835.48 K, x(Sb) 0.21476–0.28056
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sb:ag3sb)

Names (6): _corpus: _corpus:phase:ag-sb:ag3sb  
_paper: _paper:10.1007/s11669-007-9085-y:ε  
_system_alias: _system_alias:ag-sb:epsilon  
_tdb: _tdb:AgSb-07Zor.tdb:AG3SB, tdb:AgSb-94Lee.tdb:AG3SB, tdb:AgSb-96Oh-LB.tdb:AG3SB  


### TDB models of AG3SB (3): PHASE and CONSTITUENT statements as written

[AgSb-07Zor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-07Zor.tdb): AG3SB, type code %, sha256 `4a4d3ab63e7357b5…`

~~~~text
48: PHASE AG3SB % 2 3 1 !
49: CONST AG3SB : AG SB : AG SB : !
~~~~

[AgSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-94Lee.tdb): AG3SB, type code %, sha256 `9a293f35c50f2f4c…`

~~~~text
49: PHASE AG3SB % 2 3 1 !
50: CONST AG3SB : AG SB : AG SB : !
~~~~

[AgSb-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-96Oh-LB.tdb): AG3SB, type code %, sha256 `09269ee847372619…`

~~~~text
51: PHASE AG3SB % 2 3 1 !
52: CONST AG3SB : AG SB : AG SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-007-9085-y](https://doi.org/10.1007/s11669-007-9085-y) E. Zoro, C. Servant, B. Legendre, Thermodynamic Modeling of the Ag-Au-Sb Ternary System, J Phs Eqil and Diff 28, 250-257 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02671976](https://doi.org/10.1007/bf02671976) H. Okamoto, Phase Diagram Updates Ag-Sb (Silver-Antimony), J. Phase Equilibria, 1993, 14, p 531-532  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Sb)

- Id: `phase:ag-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sb:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-sb:bcc-a2  
_tdb: _tdb:AgSb-07Zor.tdb:BCC_A2, tdb:AgSb-94Lee.tdb:BCC_A2, tdb:AgSb-96Oh-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AgSb-07Zor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-07Zor.tdb): BCC_A2, type code %B, sha256 `4a4d3ab63e7357b5…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG SB : VA : !
~~~~

[AgSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-94Lee.tdb): BCC_A2, type code %B, sha256 `9a293f35c50f2f4c…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG SB : VA : !
~~~~

[AgSb-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-96Oh-LB.tdb): BCC_A2, type code %B, sha256 `09269ee847372619…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AG SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-007-9085-y](https://doi.org/10.1007/s11669-007-9085-y) E. Zoro, C. Servant, B. Legendre, Thermodynamic Modeling of the Ag-Au-Sb Ternary System, J Phs Eqil and Diff 28, 250-257 (2007).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_

## FCC_A1 (Ag–Sb)

- Id: `phase:ag-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1238.93 K, x(Sb) 0–0.07459
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sb:fcc-a1)

Names (6): _corpus: _corpus:phase:ag-sb:fcc-a1  
_paper: _paper:10.1007/s11669-007-9085-y:α  
_system_alias: _system_alias:ag-sb:alpha  
_tdb: _tdb:AgSb-07Zor.tdb:FCC_A1, tdb:AgSb-94Lee.tdb:FCC_A1, tdb:AgSb-96Oh-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AgSb-07Zor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-07Zor.tdb): FCC_A1, type code %A, sha256 `4a4d3ab63e7357b5…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% SB : VA : !
~~~~

[AgSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-94Lee.tdb): FCC_A1, type code %A, sha256 `9a293f35c50f2f4c…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% SB : VA : !
~~~~

[AgSb-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-96Oh-LB.tdb): FCC_A1, type code %A, sha256 `09269ee847372619…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AG% SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-007-9085-y](https://doi.org/10.1007/s11669-007-9085-y) E. Zoro, C. Servant, B. Legendre, Thermodynamic Modeling of the Ag-Au-Sb Ternary System, J Phs Eqil and Diff 28, 250-257 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02671976](https://doi.org/10.1007/bf02671976) H. Okamoto, Phase Diagram Updates Ag-Sb (Silver-Antimony), J. Phase Equilibria, 1993, 14, p 531-532  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Sb)

- Id: `phase:ag-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–975.49 K, x(Sb) 0.07993–0.17166
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sb:hcp-a3)

Names (6): _corpus: _corpus:phase:ag-sb:hcp-a3  
_paper: _paper:10.1007/s11669-007-9085-y:ζ  
_system_alias: _system_alias:ag-sb:zeta  
_tdb: _tdb:AgSb-07Zor.tdb:HCP_A3, tdb:AgSb-94Lee.tdb:HCP_A3, tdb:AgSb-96Oh-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AgSb-07Zor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-07Zor.tdb): HCP_A3, type code %A, sha256 `4a4d3ab63e7357b5…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG SB : VA : !
~~~~

[AgSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-94Lee.tdb): HCP_A3, type code %A, sha256 `9a293f35c50f2f4c…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG SB : VA : !
~~~~

[AgSb-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-96Oh-LB.tdb): HCP_A3, type code %A, sha256 `09269ee847372619…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AG SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-007-9085-y](https://doi.org/10.1007/s11669-007-9085-y) E. Zoro, C. Servant, B. Legendre, Thermodynamic Modeling of the Ag-Au-Sb Ternary System, J Phs Eqil and Diff 28, 250-257 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02671976](https://doi.org/10.1007/bf02671976) H. Okamoto, Phase Diagram Updates Ag-Sb (Silver-Antimony), J. Phase Equilibria, 1993, 14, p 531-532  
_cited as the source of values for this phase_

## LIQUID (Ag–Sb)

- Id: `phase:ag-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 753.19–2500 K, x(Sb) 0–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sb:liquid)

Names (5): _corpus: _corpus:phase:ag-sb:liquid  
_paper: _paper:10.1007/s11669-007-9085-y:L  
_tdb: _tdb:AgSb-07Zor.tdb:LIQUID, tdb:AgSb-94Lee.tdb:LIQUID, tdb:AgSb-96Oh-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AgSb-07Zor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-07Zor.tdb): LIQUID, type code %, sha256 `4a4d3ab63e7357b5…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG SB : !
~~~~

[AgSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-94Lee.tdb): LIQUID, type code %, sha256 `9a293f35c50f2f4c…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG SB : !
~~~~

[AgSb-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSb-96Oh-LB.tdb): LIQUID, type code %, sha256 `09269ee847372619…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AG SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-007-9085-y](https://doi.org/10.1007/s11669-007-9085-y) E. Zoro, C. Servant, B. Legendre, Thermodynamic Modeling of the Ag-Au-Sb Ternary System, J Phs Eqil and Diff 28, 250-257 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02671976](https://doi.org/10.1007/bf02671976) H. Okamoto, Phase Diagram Updates Ag-Sb (Silver-Antimony), J. Phase Equilibria, 1993, 14, p 531-532  
_cited as the source of values for this phase_

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
