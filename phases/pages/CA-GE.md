# Ca–Ge phases

> Ca–Ge system: 10 phases (tier A 8, tier C 1, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-GE.html · Markdown: https://data.orchid-project.org/phases/pages/CA-GE.md

10 phases (tier A 8, tier C 1, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-GE) · [full JSON](https://data.orchid-project.org/phases/systems/CA-GE.json) · [Ca–Ge system page](https://data.orchid-project.org/systems/CA-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Ge system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ca-ge-a4-diamond); _phase:ca-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.8 K, x(Ge) 1–1 | 3 | 1 |
| [BCC_A2](#phase-ca-ge-bcc-a2); _phase:ca-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 716.03–1115 K, x(Ge) 0–0 | 3 | 1 |
| [CA2GE_C37](#phase-ca-ge-ca2ge-c37); _phase:ca-ge:ca2ge-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1579.56 K, x(Ge) 0.33333–0.33333 | 13 | 1 |
| [CA5GE3_D8L](#phase-ca-ge-ca5ge3-d8l); _phase:ca-ge:ca5ge3-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1505.68 K, x(Ge) 0.375–0.375 | 10 | 1 |
| [CA7GE6](#phase-ca-ge-ca7ge6); _phase:ca-ge:ca7ge6_ | Ca7Sn6 · oP52 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1441.44 K, x(Ge) 0.46154–0.46154 | 8 | 1 |
| [CAGE_B33](#phase-ca-ge-cage-b33); _phase:ca-ge:cage-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1447.01 K, x(Ge) 0.5–0.5 | 14 | 1 |
| [CAGE2_C12](#phase-ca-ge-cage2-c12); _phase:ca-ge:cage2-c12_ | CaSi2 · C12 · hR6 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1116.25 K, x(Ge) 0.66667–0.66667 | 14 | 1 |
| [FCC_A1](#phase-ca-ge-fcc-a1); _phase:ca-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Ge) 0–0 | 0 | 1 |
| [HCP_A3](#phase-ca-ge-hcp-a3); _phase:ca-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ca-ge-liquid); _phase:ca-ge:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1045.38–2500 K, x(Ge) 0–1 | 22 | 1 |

## DIAMOND_A4 (Ca–Ge)

- Id: `phase:ca-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.8 K, x(Ge) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:a4-diamond)

Names (4): _corpus: _corpus:phase:ca-ge:a4-diamond, corpus:phase:ca-ge:diamond-a4  
_paper: _paper:10.1016/j.jallcom.2010.02.189:Ge  
_tdb: _tdb:CaGe-10Dja.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): DIAMOND_A4, type code %, sha256 `cb8f461fa9247dd9…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
_cited as the source of values for this phase_

## BCC_A2 (Ca–Ge)

- Id: `phase:ca-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 716.03–1115 K, x(Ge) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:bcc-a2)

Names (3): _corpus: _corpus:phase:ca-ge:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2010.02.189:βCa  
_tdb: _tdb:CaGe-10Dja.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): BCC_A2, type code %B, sha256 `cb8f461fa9247dd9…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CA% GE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
_cited as the source of values for this phase_

## CA2GE_C37 (Ca–Ge)

- Id: `phase:ca-ge:ca2ge-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaals and oqmd-7763, space group 62
- Stoichiometry: Ca 0.6667, Ge 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1579.56 K, x(Ge) 0.33333–0.33333
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:ca2ge-c37)

Names (5): _corpus: _corpus:phase:ca-ge:ca2ge-c37  
_mp: _mp:mp-aaaaaals  
_oqmd: _oqmd:oqmd-7763  
_paper: _paper:10.1016/j.jallcom.2010.02.189:Ca2Ge  
_tdb: _tdb:CaGe-10Dja.tdb:CA2GE_C37  


### TDB models of CA2GE_C37 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): CA2GE_C37, type code %, sha256 `cb8f461fa9247dd9…`

~~~~text
48: PHASE CA2GE_C37 % 2 2 1 !
49: CONST CA2GE_C37 : CA : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2009.11.007](https://doi.org/10.1016/j.jssc.2009.11.007) Zhiwen Yang, Dongmin Shi, Bin Wen, Roderick Melnik, Shan Yao, Tingju Li, First-principle studies of Ca–X (X=Si,Ge,Sn,Pb) intermetallic compounds, Journal of Solid State Chemistry 183, 136-143 (2010).  
_cited as the source of values for this phase_

## CA5GE3_D8L (Ca–Ge)

- Id: `phase:ca-ge:ca5ge3-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacum and oqmd-7694, space group 140
- Stoichiometry: Ca 0.6250, Ge 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1505.68 K, x(Ge) 0.375–0.375
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:ca5ge3-d8l)

Names (5): _corpus: _corpus:phase:ca-ge:ca5ge3-d8l  
_mp: _mp:mp-aaaaacum  
_oqmd: _oqmd:oqmd-7694  
_paper: _paper:10.1016/j.jallcom.2010.02.189:Ca5Ge3  
_tdb: _tdb:CaGe-10Dja.tdb:CA5GE3_D8L  


### TDB models of CA5GE3_D8L (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): CA5GE3_D8L, type code %, sha256 `cb8f461fa9247dd9…`

~~~~text
53: PHASE CA5GE3_D8L % 2 5 3 !
54: CONST CA5GE3_D8L : CA : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2009.11.007](https://doi.org/10.1016/j.jssc.2009.11.007) Zhiwen Yang, Dongmin Shi, Bin Wen, Roderick Melnik, Shan Yao, Tingju Li, First-principle studies of Ca–X (X=Si,Ge,Sn,Pb) intermetallic compounds, Journal of Solid State Chemistry 183, 136-143 (2010).  
_cited as the source of values for this phase_

## CA7GE6 (Ca–Ge)

- Id: `phase:ca-ge:ca7ge6`; status `assigned`
- Structure: Ca7Sn6 · oP52 · Pnma (62); type `st:ca7sn6-op52`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.5385, Ge 0.4615
- Stability: stable in 1 of 1 calculated diagram(s): 300–1441.44 K, x(Ge) 0.46154–0.46154
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:ca7ge6)

Names (3): _corpus: _corpus:phase:ca-ge:ca7ge6  
_paper: _paper:10.1016/j.jallcom.2010.02.189:Ca7Ge6  
_tdb: _tdb:CaGe-10Dja.tdb:CA7GE6  


### TDB models of CA7GE6 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): CA7GE6, type code %, sha256 `cb8f461fa9247dd9…`

~~~~text
58: PHASE CA7GE6 % 2 7 6 !
59: CONST CA7GE6 : CA : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2009.11.007](https://doi.org/10.1016/j.jssc.2009.11.007) Zhiwen Yang, Dongmin Shi, Bin Wen, Roderick Melnik, Shan Yao, Tingju Li, First-principle studies of Ca–X (X=Si,Ge,Sn,Pb) intermetallic compounds, Journal of Solid State Chemistry 183, 136-143 (2010).  
_cited as the source of values for this phase_

## CAGE_B33 (Ca–Ge)

- Id: `phase:ca-ge:cage-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadmu and oqmd-7940, space group 63
- Stoichiometry: Ca 0.5000, Ge 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1447.01 K, x(Ge) 0.5–0.5
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:cage-b33)

Names (5): _corpus: _corpus:phase:ca-ge:cage-b33  
_mp: _mp:mp-aaaaadmu  
_oqmd: _oqmd:oqmd-7940  
_paper: _paper:10.1016/j.jallcom.2010.02.189:CaGe  
_tdb: _tdb:CaGe-10Dja.tdb:CAGE_B33  


### TDB models of CAGE_B33 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): CAGE_B33, type code %, sha256 `cb8f461fa9247dd9…`

~~~~text
63: PHASE CAGE_B33 % 2 1 1 !
64: CONST CAGE_B33 : CA : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2009.11.007](https://doi.org/10.1016/j.jssc.2009.11.007) Zhiwen Yang, Dongmin Shi, Bin Wen, Roderick Melnik, Shan Yao, Tingju Li, First-principle studies of Ca–X (X=Si,Ge,Sn,Pb) intermetallic compounds, Journal of Solid State Chemistry 183, 136-143 (2010).  
_cited as the source of values for this phase_

## CAGE2_C12 (Ca–Ge)

- Id: `phase:ca-ge:cage2-c12`; status `assigned`
- Structure: CaSi2 · C12 · hR6 · R-3m (166); type `st:c12-casi2-hr6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabghlg and oqmd-13940, space group 166
- Stoichiometry: Ca 0.3333, Ge 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1116.25 K, x(Ge) 0.66667–0.66667
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:cage2-c12)

Names (5): _corpus: _corpus:phase:ca-ge:cage2-c12  
_mp: _mp:mp-aaabghlg  
_oqmd: _oqmd:oqmd-13940  
_paper: _paper:10.1016/j.jallcom.2010.02.189:CaGe2  
_tdb: _tdb:CaGe-10Dja.tdb:CAGE2_C12  


### TDB models of CAGE2_C12 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): CAGE2_C12, type code %, sha256 `cb8f461fa9247dd9…`

~~~~text
68: PHASE CAGE2_C12 % 2 1 2 !
69: CONST CAGE2_C12 : CA : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2009.11.007](https://doi.org/10.1016/j.jssc.2009.11.007) Zhiwen Yang, Dongmin Shi, Bin Wen, Roderick Melnik, Shan Yao, Tingju Li, First-principle studies of Ca–X (X=Si,Ge,Sn,Pb) intermetallic compounds, Journal of Solid State Chemistry 183, 136-143 (2010).  
_cited as the source of values for this phase_

## FCC_A1 (Ca–Ge)

- Id: `phase:ca-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Ge) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:fcc-a1)

Names (2): _corpus: _corpus:phase:ca-ge:fcc-a1  
_tdb: _tdb:CaGe-10Dja.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): FCC_A1, type code %A, sha256 `cb8f461fa9247dd9…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CA% GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase_

## HCP_A3 (Ca–Ge)

- Id: `phase:ca-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-ge:hcp-a3  
_tdb: _tdb:CaGe-10Dja.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): HCP_A3, type code %A, sha256 `cb8f461fa9247dd9…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CA GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase_

## LIQUID (Ca–Ge)

- Id: `phase:ca-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1045.38–2500 K, x(Ge) 0–1
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ge:liquid)

Names (3): _corpus: _corpus:phase:ca-ge:liquid  
_paper: _paper:10.1016/j.jallcom.2010.02.189:Liq  
_tdb: _tdb:CaGe-10Dja.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaGe-10Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/CaGe-10Dja.tdb): LIQUID, type code %, sha256 `cb8f461fa9247dd9…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CA GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.189](https://doi.org/10.1016/j.jallcom.2010.02.189) Y. Djaballah, A. Pasturel, A. Belgacem-Bouzida, Thermodynamic assessment of the calcium–germanium system, Journal of Alloys and Compounds 497, 74-79 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00326-2](https://doi.org/10.1016/s0925-8388%2802%2900326-2) A Palenzona, P Manfrinetti, M.L Fornasini, The phase diagram of the Ca–Ge system, Journal of Alloys and Compounds 345, 144-147 (2002).  
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
