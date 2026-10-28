# Ge–P phases

> Ge–P system: 8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-P.html · Markdown: https://data.orchid-project.org/phases/pages/GE-P.md

8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-P) · [full JSON](https://data.orchid-project.org/phases/systems/GE-P.json) · [Ge–P system page](https://data.orchid-project.org/systems/GE-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–P system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-p-a4-diamond); _phase:ge-p:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(P) 0–0.00248 | 0 | 2 |
| [BCC_A2](#phase-ge-p-bcc-a2); _phase:ge-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ge-p-fcc-a1); _phase:ge-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GEP](#phase-ge-p-gep); _phase:ge-p:gep_ | SiAs · mC24 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1002 K, x(P) 0.5–0.5 | 31 | 2 |
| [HCP_A3](#phase-ge-p-hcp-a3); _phase:ge-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ge-p-liquid); _phase:ge-p:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 841.27–2500 K, x(P) 0–1 | 1 | 2 |
| [RED_P](#phase-ge-p-p-red); _phase:ge-p:p-red_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–852.36 K, x(P) 1–1 | 0 | 2 |
| [WHITE_P](#phase-ge-p-p-white); _phase:ge-p:p-white_ |  | needs_review | not stable in 2 calculated diagram(s) | 0 | 2 |

## DIAMOND_A4 (Ge–P)

- Id: `phase:ge-p:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(P) 0–0.00248
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:a4-diamond)

Names (3): _corpus: _corpus:phase:ge-p:a4-diamond  
_tdb: _tdb:GeP-21Don.tdb:DIAMOND_A4, tdb:GeP-22Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): DIAMOND_A4, type code %, sha256 `e3a892ddc27c2127…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : GE% P : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): DIAMOND_A4, type code %, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## BCC_A2 (Ge–P)

- Id: `phase:ge-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:bcc-a2)

Names (3): _corpus: _corpus:phase:ge-p:bcc-a2  
_tdb: _tdb:GeP-21Don.tdb:BCC_A2, tdb:GeP-22Che.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): BCC_A2, type code %B, sha256 `e3a892ddc27c2127…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GE P : VA : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): BCC_A2, type code %B, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : GE P : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## FCC_A1 (Ge–P)

- Id: `phase:ge-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:fcc-a1)

Names (3): _corpus: _corpus:phase:ge-p:fcc-a1  
_tdb: _tdb:GeP-21Don.tdb:FCC_A1, tdb:GeP-22Che.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): FCC_A1, type code %A, sha256 `e3a892ddc27c2127…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GE P : VA : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): FCC_A1, type code %A, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : GE P : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GEP (Ge–P)

- Id: `phase:ge-p:gep`; status `assigned`
- Structure: SiAs · mC24 · C2/m (12); type `st:sias-mc24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.5000, P 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1002 K, x(P) 0.5–0.5
- Literature: 31 values (31 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:gep)

Names (5): _corpus: _corpus:phase:ge-p:gep  
_paper: _paper:10.1007/s11664-021-08861-4:GeP, paper:10.1007/s11664-022-09474-1:GeP  
_tdb: _tdb:GeP-21Don.tdb:GEP, tdb:GeP-22Che.tdb:GEP  


### TDB models of GEP (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): GEP, type code %, sha256 `e3a892ddc27c2127…`

~~~~text
56: PHASE GEP % 2 1 1 !
57: CONST GEP : GE : P : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): GEP, type code %, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
59: PHASE GEP % 2 1 1 !
60: CONST GEP : GE : P : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3891/acta.chem.scand.21-0593](https://doi.org/10.3891/acta.chem.scand.21-0593) Tommy Wadsten, M. Vikan, C. Krohn, Åke Nilsson, H. Theorell, R. Blinc et al., The Crystal Structures of SiP2, SiAs2, and GeP., Acta Chem. Scand. 21, 593-594 (1967).  
_cited as the source of values for this phase_
- [doi:10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10) Scott Kirklin, James E Saal, Bryce Meredig, Alex Thompson, Jeff W Doak, Muratahan Aykol et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput Mater 1 (2015).  
_cited as the source of values for this phase_
- [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2014.04.021](https://doi.org/10.1016/j.jssc.2014.04.021) Kathleen Lee, Sarah Synnestvedt, Maverick Bellard, Kirill Kovnir, GeP and (Ge1−Sn )(P1−Ge ) (x≈0.12, y≈0.05): Synthesis, structure, and properties of two-dimensional layered tetrel phosphides, Journal of Solid State Chemistry 224, 62-70 (2015).  
_cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2012.02.005](https://doi.org/10.1016/j.commatsci.2012.02.005) Stefano Curtarolo, Wahyu Setyawan, Gus L.W. Hart, Michal Jahnatek, Roman V. Chepulskii, Richard H. Taylor et al., AFLOW: An automatic framework for high-throughput materials discovery, Computational Materials Science 58, 218-226 (2012).  
_cited as the source of values for this phase_

## HCP_A3 (Ge–P)

- Id: `phase:ge-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:hcp-a3)

Names (3): _corpus: _corpus:phase:ge-p:hcp-a3  
_tdb: _tdb:GeP-21Don.tdb:HCP_A3, tdb:GeP-22Che.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): HCP_A3, type code %A, sha256 `e3a892ddc27c2127…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : GE P : VA : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): HCP_A3, type code %A, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : GE P : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## LIQUID (Ge–P)

- Id: `phase:ge-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 841.27–2500 K, x(P) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:liquid)

Names (4): _corpus: _corpus:phase:ge-p:liquid  
_paper: _paper:10.1007/s11664-021-08861-4:liquid  
_tdb: _tdb:GeP-21Don.tdb:LIQUID, tdb:GeP-22Che.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): LIQUID, type code %, sha256 `e3a892ddc27c2127…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GE P : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): LIQUID, type code %, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GE P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## RED_P (Ge–P)

- Id: `phase:ge-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–852.36 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:p-red)

Names (3): _corpus: _corpus:phase:ge-p:p-red  
_tdb: _tdb:GeP-21Don.tdb:RED_P, tdb:GeP-22Che.tdb:RED_P  


### TDB models of RED_P (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): RED_P, type code %, sha256 `e3a892ddc27c2127…`

~~~~text
51: PHASE RED_P % 1 1 !
52: CONST RED_P : P : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): RED_P, type code %, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
54: PHASE RED_P % 1 1 !
55: CONST RED_P : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## WHITE_P (Ge–P)

- Id: `phase:ge-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-p:p-white)

Names (3): _corpus: _corpus:phase:ge-p:p-white  
_tdb: _tdb:GeP-21Don.tdb:WHITE_P, tdb:GeP-22Che.tdb:WHITE_P  


### TDB models of WHITE_P (2): PHASE and CONSTITUENT statements as written

[GeP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-21Don.tdb): WHITE_P, type code %, sha256 `e3a892ddc27c2127…`

~~~~text
46: PHASE WHITE_P % 1 1 !
47: CONST WHITE_P : P : !
~~~~

[GeP-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeP-22Che.tdb): WHITE_P, type code %, sha256 `3ebe2eeb4e7cc01d…`

~~~~text
49: PHASE WHITE_P % 1 1 !
50: CONST WHITE_P : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
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
