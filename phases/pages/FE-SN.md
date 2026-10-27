# Fe–Sn phases

> Fe–Sn system: 10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-SN.html · Markdown: https://data.orchid-project.org/phases/pages/FE-SN.md

10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-SN) · [full JSON](https://data.orchid-project.org/phases/systems/FE-SN.json) · [Fe–Sn system page](https://data.orchid-project.org/systems/FE-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Sn system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-fe-sn-a4-diamond); _phase:fe-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [BCT_A5](#phase-fe-sn-a5-bct); _phase:fe-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 6 | 3 |
| [BCC_A2](#phase-fe-sn-bcc-a2); _phase:fe-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1829.2 K, x(Sn) 0–0.08794 | 22 | 3 |
| [FCC_A1](#phase-fe-sn-fcc-a1); _phase:fe-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1124.83–1689.83 K, x(Sn) 0–0.00852 | 0 | 3 |
| [FE3SN2](#phase-fe-sn-fe3sn2); _phase:fe-sn:fe3sn2_ | Fe3Sn2 · hR10 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 875.05–1080.32 K, x(Sn) 0.4–0.4 | 20 | 3 |
| [FE5SN3_B82](#phase-fe-sn-fe5sn3-b82); _phase:fe-sn:fe5sn3-b82_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 1040.58–1181.15 K, x(Sn) 0.375–0.375 | 14 | 3 |
| [FESN_B35](#phase-fe-sn-fesn-b35); _phase:fe-sn:fesn-b35_ | CoSn · B35 · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1042.51 K, x(Sn) 0.5–0.5 | 28 | 3 |
| [FESN2_C16](#phase-fe-sn-fesn2-c16); _phase:fe-sn:fesn2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–786.12 K, x(Sn) 0.66667–0.66667 | 23 | 3 |
| [HCP_A3](#phase-fe-sn-hcp-a3); _phase:fe-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-fe-sn-liquid); _phase:fe-sn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 505.08–2500 K, x(Sn) 0–1 | 28 | 3 |

## DIAMOND_A4 (Fe–Sn)

- Id: `phase:fe-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:a4-diamond)

Names (4): _corpus: _corpus:phase:fe-sn:a4-diamond  
_tdb: _tdb:FeSn-10Hua.tdb:DIAMOND_A4, tdb:FeSn-20Laf.tdb:DIAMOND_A4, tdb:FeSn-96Har-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): DIAMOND_A4, type code %, sha256 `a4b20e684dcb573a…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): DIAMOND_A4, type code %, sha256 `9fdbfba0e895036a…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): DIAMOND_A4, type code %, sha256 `ad3eeabb86656e73…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase_

## BCT_A5 (Fe–Sn)

- Id: `phase:fe-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:a5-bct)

Names (6): _corpus: _corpus:phase:fe-sn:a5-bct, corpus:phase:fe-sn:bct-a5  
_paper: _paper:10.1016/j.intermet.2010.01.026:BCT_A5  
_tdb: _tdb:FeSn-10Hua.tdb:BCT_A5, tdb:FeSn-20Laf.tdb:BCT_A5, tdb:FeSn-96Har-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): BCT_A5, type code %, sha256 `a4b20e684dcb573a…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : SN : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): BCT_A5, type code %, sha256 `9fdbfba0e895036a…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : SN : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): BCT_A5, type code %, sha256 `ad3eeabb86656e73…`

~~~~text
45: PHASE BCT_A5 % 1 1 !
46: CONST BCT_A5 : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(75)90039-5](https://doi.org/10.1016/0001-6160%2875%2990039-5) J.J Connolly, J.V McAllan, The tin-iron eutectic, Acta Metallurgica 23, 1209-1214 (1975).  
_cited as the source of values for this phase_

## BCC_A2 (Fe–Sn)

- Id: `phase:fe-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1829.2 K, x(Sn) 0–0.08794
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:bcc-a2)

Names (5): _corpus: _corpus:phase:fe-sn:bcc-a2  
_paper: _paper:10.1016/j.intermet.2010.01.026:BCC_A2  
_tdb: _tdb:FeSn-10Hua.tdb:BCC_A2, tdb:FeSn-20Laf.tdb:BCC_A2, tdb:FeSn-96Har-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): BCC_A2, type code %B, sha256 `a4b20e684dcb573a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% SN : VA : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): BCC_A2, type code %B, sha256 `9fdbfba0e895036a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% SN : VA : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): BCC_A2, type code %B, sha256 `ad3eeabb86656e73…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf01730231](https://doi.org/10.1007/bf01730231) M. Singh, S. Bhan, Contribution to the Fe—Sn system, J Mater Sci Lett 5, 733-735 (1986).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Sn)

- Id: `phase:fe-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1124.83–1689.83 K, x(Sn) 0–0.00852
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-sn:fcc-a1  
_tdb: _tdb:FeSn-10Hua.tdb:FCC_A1, tdb:FeSn-20Laf.tdb:FCC_A1, tdb:FeSn-96Har-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): FCC_A1, type code %A, sha256 `a4b20e684dcb573a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% SN : VA : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): FCC_A1, type code %A, sha256 `9fdbfba0e895036a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% SN : VA : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): FCC_A1, type code %A, sha256 `ad3eeabb86656e73…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase_

## FE3SN2 (Fe–Sn)

- Id: `phase:fe-sn:fe3sn2`; status `assigned`
- Structure: Fe3Sn2 · hR10 · R-3m (166); type `st:fe3sn2-hr10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.6000, Sn 0.4000
- Stability: stable in 3 of 3 calculated diagram(s): 875.05–1080.32 K, x(Sn) 0.4–0.4
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:fe3sn2)

Names (5): _corpus: _corpus:phase:fe-sn:fe3sn2  
_paper: _paper:10.1016/j.intermet.2010.01.026:Fe3Sn2  
_tdb: _tdb:FeSn-10Hua.tdb:FE3SN2, tdb:FeSn-20Laf.tdb:FE3SN2, tdb:FeSn-96Har-LB.tdb:FE3SN2  


### TDB models of FE3SN2 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): FE3SN2, type code %, sha256 `a4b20e684dcb573a…`

~~~~text
60: PHASE FE3SN2 % 2 3 2  !
61: CONST FE3SN2 : FE : SN : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): FE3SN2, type code %, sha256 `9fdbfba0e895036a…`

~~~~text
57: PHASE FE3SN2 % 2 3 2  !
58: CONST FE3SN2 : FE : SN : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): FE3SN2, type code %, sha256 `ad3eeabb86656e73…`

~~~~text
55: PHASE FE3SN2 % 2 3 2  !
56: CONST FE3SN2 : FE : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf01730231](https://doi.org/10.1007/bf01730231) M. Singh, S. Bhan, Contribution to the Fe—Sn system, J Mater Sci Lett 5, 733-735 (1986).  
_cited as the source of values for this phase_

## FE5SN3_B82 (Fe–Sn)

- Id: `phase:fe-sn:fe5sn3-b82`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_B8_2; stoichiometry_contradicts_B8_2:FeSn-10Hua.tdb; stoichiometry_contradicts_B8_2:FeSn-20Laf.tdb; stoichiometry_contradicts_B8_2:FeSn-96Har-LB.tdb
- Candidate (literature_printed): InNi2 · hP6 — printed with a label mapped to this phase
- Candidate (name_token): InNi2 · B8_2 · hP6 · P6_3/mmc (194) — Strukturbericht/word 'B82' in the TDB name
- Candidate (sgte_mmc2): InNi2 · B8_2 · hP6 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for FE5SN3_B82: Fe5Sn3
- Candidate (tdb_comment): InNi2 · hP6 · P6_3/mmc — FeSn-10Hua.tdb: 'Prototype InNi2 (hP6, P6_3/mmc)'
- Candidate (tdb_comment): InNi2 · hP6 · P6_3/mmc — FeSn-20Laf.tdb: 'Prototype InNi2 (hP6, P6_3/mmc)'
- Candidate (tdb_comment): InNi2 · hP6 · P6_3/mmc — FeSn-96Har-LB.tdb: 'Prototype InNi2 (hP6, P6_3/mmc)'
- Stoichiometry: Fe 0.6250, Sn 0.3750
- Stability: stable in 3 of 3 calculated diagram(s): 1040.58–1181.15 K, x(Sn) 0.375–0.375
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:fe5sn3-b82)

Names (5): _corpus: _corpus:phase:fe-sn:fe5sn3-b82  
_paper: _paper:10.1016/j.intermet.2010.01.026:Fe5Sn3  
_tdb: _tdb:FeSn-10Hua.tdb:FE5SN3_B82, tdb:FeSn-20Laf.tdb:FE5SN3_B82, tdb:FeSn-96Har-LB.tdb:FE5SN3_B82  


### TDB models of FE5SN3_B82 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): FE5SN3_B82, type code %, sha256 `a4b20e684dcb573a…`

~~~~text
55: PHASE FE5SN3_B82 % 2 5 3  !
56: CONST FE5SN3_B82 : FE : SN : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): FE5SN3_B82, type code %, sha256 `9fdbfba0e895036a…`

~~~~text
52: PHASE FE5SN3_B82 % 2 5 3  !
53: CONST FE5SN3_B82 : FE : SN : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): FE5SN3_B82, type code %, sha256 `ad3eeabb86656e73…`

~~~~text
50: PHASE FE5SN3_B82 % 2 5 3  !
51: CONST FE5SN3_B82 : FE : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf01730231](https://doi.org/10.1007/bf01730231) M. Singh, S. Bhan, Contribution to the Fe—Sn system, J Mater Sci Lett 5, 733-735 (1986).  
_cited as the source of values for this phase_

## FESN_B35 (Fe–Sn)

- Id: `phase:fe-sn:fesn-b35`; status `assigned`
- Structure: CoSn · B35 · hP6 · P6/mmm (191); type `st:b35-cosn-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabfls and oqmd-19577, space group 191
- Stoichiometry: Fe 0.5000, Sn 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1042.51 K, x(Sn) 0.5–0.5
- Literature: 28 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:fesn-b35)

Names (8): _corpus: _corpus:phase:fe-sn:fesn-b35  
_mp: _mp:mp-aaaabfls  
_oqmd: _oqmd:oqmd-19577  
_paper: _paper:10.1016/j.intermet.2010.01.026:FeSn, paper:10.1016/s0364-5916(96)00021-1:FeSn  
_tdb: _tdb:FeSn-10Hua.tdb:FESN_B35, tdb:FeSn-20Laf.tdb:FESN_B35, tdb:FeSn-96Har-LB.tdb:FESN_B35  


### TDB models of FESN_B35 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): FESN_B35, type code %, sha256 `a4b20e684dcb573a…`

~~~~text
65: PHASE FESN_B35 % 2 1 1  !
66: CONST FESN_B35 : FE : SN : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): FESN_B35, type code %, sha256 `9fdbfba0e895036a…`

~~~~text
62: PHASE FESN_B35 % 2 1 1  !
63: CONST FESN_B35 : FE : SN : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): FESN_B35, type code %, sha256 `ad3eeabb86656e73…`

~~~~text
60: PHASE FESN_B35 % 2 1 1  !
61: CONST FESN_B35 : FE : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf01730231](https://doi.org/10.1007/bf01730231) M. Singh, S. Bhan, Contribution to the Fe—Sn system, J Mater Sci Lett 5, 733-735 (1986).  
_cited as the source of values for this phase_

## FESN2_C16 (Fe–Sn)

- Id: `phase:fe-sn:fesn2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 0.3333, Sn 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–786.12 K, x(Sn) 0.66667–0.66667
- Literature: 23 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:fesn2-c16)

Names (6): _corpus: _corpus:phase:fe-sn:fesn2-c16  
_paper: _paper:10.1016/j.intermet.2010.01.026:FeSn2, paper:10.1016/s0364-5916(96)00021-1:FeSn2  
_tdb: _tdb:FeSn-10Hua.tdb:FESN2_C16, tdb:FeSn-20Laf.tdb:FESN2_C16, tdb:FeSn-96Har-LB.tdb:FESN2_C16  


### TDB models of FESN2_C16 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): FESN2_C16, type code %, sha256 `a4b20e684dcb573a…`

~~~~text
70: PHASE FESN2_C16 % 2 1 2  !
71: CONST FESN2_C16 : FE : SN : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): FESN2_C16, type code %, sha256 `9fdbfba0e895036a…`

~~~~text
67: PHASE FESN2_C16 % 2 1 2  !
68: CONST FESN2_C16 : FE : SN : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): FESN2_C16, type code %, sha256 `ad3eeabb86656e73…`

~~~~text
65: PHASE FESN2_C16 % 2 1 2  !
66: CONST FESN2_C16 : FE : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(75)90039-5](https://doi.org/10.1016/0001-6160%2875%2990039-5) J.J Connolly, J.V McAllan, The tin-iron eutectic, Acta Metallurgica 23, 1209-1214 (1975).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Sn)

- Id: `phase:fe-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-sn:hcp-a3  
_tdb: _tdb:FeSn-10Hua.tdb:HCP_A3, tdb:FeSn-20Laf.tdb:HCP_A3, tdb:FeSn-96Har-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): HCP_A3, type code %A, sha256 `a4b20e684dcb573a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE SN : VA : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): HCP_A3, type code %A, sha256 `9fdbfba0e895036a…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE SN : VA : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): HCP_A3, type code %A, sha256 `ad3eeabb86656e73…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase_

## LIQUID (Fe–Sn)

- Id: `phase:fe-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 505.08–2500 K, x(Sn) 0–1
- Literature: 28 values (28 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sn:liquid)

Names (5): _corpus: _corpus:phase:fe-sn:liquid  
_paper: _paper:10.1016/j.intermet.2010.01.026:Liquid  
_tdb: _tdb:FeSn-10Hua.tdb:LIQUID, tdb:FeSn-20Laf.tdb:LIQUID, tdb:FeSn-96Har-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[FeSn-10Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-10Hua.tdb): LIQUID, type code %, sha256 `a4b20e684dcb573a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE SN : !
~~~~

[FeSn-20Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-20Laf.tdb): LIQUID, type code %, sha256 `9fdbfba0e895036a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE SN : !
~~~~

[FeSn-96Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSn-96Har-LB.tdb): LIQUID, type code %, sha256 `ad3eeabb86656e73…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2010.01.026](https://doi.org/10.1016/j.intermet.2010.01.026) Yu-Chih Huang, Wojciech Gierlotka, Sinn-Wen Chen, Sn–Bi–Fe thermodynamic modeling and Sn–Bi/Fe interfacial reactions, Intermetallics 18, 984-991 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(96)00021-1](https://doi.org/10.1016/S0364-5916%2896%2900021-1) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 20, 139-49(1996).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2019.153200](https://doi.org/10.1016/j.jallcom.2019.153200) Paul Lafaye, Caroline Toffolon-Masclet, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modelling of the Fe–Sn–Zr system based on new experiments and first-principles calculations, Journal of Alloys and Compounds 821, 153200 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf01730231](https://doi.org/10.1007/bf01730231) M. Singh, S. Bhan, Contribution to the Fe—Sn system, J Mater Sci Lett 5, 733-735 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(75)90039-5](https://doi.org/10.1016/0001-6160%2875%2990039-5) J.J Connolly, J.V McAllan, The tin-iron eutectic, Acta Metallurgica 23, 1209-1214 (1975).  
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
