# Cu–Hf phases

> Cu–Hf system: 9 phases (tier A 4, tier B 1, tier C 3, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-HF.html · Markdown: https://data.orchid-project.org/phases/pages/CU-HF.md

9 phases (tier A 4, tier B 1, tier C 3, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-HF) · [full JSON](https://data.orchid-project.org/phases/systems/CU-HF.json) · [Cu–Hf system page](https://data.orchid-project.org/systems/CU-HF.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-HF.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Hf system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-hf-bcc-a2); _phase:cu-hf:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1812.79–3999.73 K, x(Hf) 0.9556–1 | 6 | 3 |
| [CU10HF7](#phase-cu-hf-cu10hf7); _phase:cu-hf:cu10hf7_ | Ni10Zr7 · oC68 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1279.43 K, x(Hf) 0.41176–0.41176 | 35 | 3 |
| [CU51HF14](#phase-cu-hf-cu51hf14); _phase:cu-hf:cu51hf14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1388 K, x(Hf) 0.21538–0.21538 | 37 | 3 |
| [CU5HF_C15B](#phase-cu-hf-cu5hf-c15b); _phase:cu-hf:cu5hf-c15b_ | AuBe5 · C15_b · cF24 · F-43m (216) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1332.63 K, x(Hf) 0.16667–0.16667 | 25 | 3 |
| [CU8HF3](#phase-cu-hf-cu8hf3); _phase:cu-hf:cu8hf3_ | Cu8Hf3 · oP44 · Pnma (62) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–1274.49 K, x(Hf) 0.27273–0.27273 | 26 | 3 |
| [CUHF2](#phase-cu-hf-cuhf2); _phase:cu-hf:cuhf2_ | CuZr2 · tI6 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1611.26 K, x(Hf) 0.66667–0.66667 | 39 | 3 |
| [FCC_A1](#phase-cu-hf-fcc-a1); _phase:cu-hf:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1387.77 K, x(Hf) 0–0.0042 | 13 | 3 |
| [HCP_A3](#phase-cu-hf-hcp-a3); _phase:cu-hf:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2501.02 K, x(Hf) 0.99379–1 | 15 | 3 |
| [LIQUID](#phase-cu-hf-liquid); _phase:cu-hf:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1233.92–4000 K, x(Hf) 0–1 | 76 | 3 |

## BCC_A2 (Cu–Hf)

- Id: `phase:cu-hf:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1812.79–3999.73 K, x(Hf) 0.9556–1
- Literature: 6 values (6 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:bcc-a2)

Names (7): _corpus: _corpus:phase:cu-hf:bcc-a2  
_paper: _paper:10.1007/s11106-008-9008-4:(βHf), paper:10.1016/j.actamat.2012.10.014:bcc, paper:10.1016/j.jallcom.2006.02.013:bcc  
_tdb: _tdb:CuHf-06Lia.tdb:BCC_A2, tdb:CuHf-08Tur.tdb:BCC_A2, tdb:CuHf-13Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): BCC_A2, type code %B, sha256 `0c635db89455db21…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CU HF% : VA : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): BCC_A2, type code %B, sha256 `06d472151340d413…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CU HF% : VA : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): BCC_A2, type code %B, sha256 `e3133d3e66ab9d10…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CU HF% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(74)90184-6](https://doi.org/10.1016/0022-3115%2874%2990184-6) B. Pieraggi, F. Dabosi, M. Armand, Diagramme de phases des alliages hafnium-cuivre riches en hafnium, Journal of Nuclear Materials 52, 336-338 (1974).  
_cited as the source of values for this phase_

## CU10HF7 (Cu–Hf)

- Id: `phase:cu-hf:cu10hf7`; status `assigned`
- Structure: Ni10Zr7 · oC68 · Cmce (64); type `st:ni10zr7-oc68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.5882, Hf 0.4118
- Stability: stable in 3 of 3 calculated diagram(s): 300–1279.43 K, x(Hf) 0.41176–0.41176
- Literature: 35 values (34 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:cu10hf7)

Names (7): _corpus: _corpus:phase:cu-hf:cu10hf7  
_paper: _paper:10.1007/s11106-008-9008-4:Cu10Hf7, paper:10.1016/j.actamat.2012.10.014:Cu10Hf7, paper:10.1016/j.jallcom.2006.02.013:Cu10Hf7  
_tdb: _tdb:CuHf-06Lia.tdb:CU10HF7, tdb:CuHf-08Tur.tdb:CU10HF7, tdb:CuHf-13Zho.tdb:CU10HF7  


### TDB models of CU10HF7 (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): CU10HF7, type code %, sha256 `0c635db89455db21…`

~~~~text
55: PHASE CU10HF7 % 2 10 7 !
56: CONST CU10HF7 : CU : HF : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): CU10HF7, type code %, sha256 `06d472151340d413…`

~~~~text
63: PHASE CU10HF7 % 2 10 7 !
64: CONST CU10HF7 : CU : HF : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): CU10HF7, type code %, sha256 `e3133d3e66ab9d10…`

~~~~text
57: PHASE CU10HF7 % 2 10 7 !
58: CONST CU10HF7 : CU : HF : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1107/s0108270197007142](https://doi.org/10.1107/s0108270197007142) J.-M. Joubert, R. Cerný, K. Yvon, M. Latroche, A. Percheron-Guégan, Zirconium–Nickel, Zr\<sub>7\</sub>Ni\<sub>10\</sub>: Space Group Revision for the Stoichiometric Phase, Acta Crystallogr C Cryst Struct Commun 53, 1536-1538 (1997).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877460](https://doi.org/10.1007/bf02877460) P.R. Subramanian, D.E. Laughlin, Bull. Alloy Phase Diagrams 9 (1) (1988) 51–55.  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667755](https://doi.org/10.1007/bf02667755) O. J. Kleppa, Shunroku Watanabe, Thermochemistry of alloys of transition metals: Part III. Copper-Silver, -Titanium, Zirconium, and -Hafnium at 1373 K, Metall Trans B 13, 391-401 (1982).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02736446](https://doi.org/10.1007/bf02736446) R. H. Woodman, B. R. Klotz, L. J. Kecskes, Observation of incongruent melting in Cu10Hf7, JPED 27, 477-481 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(74)90184-6](https://doi.org/10.1016/0022-3115%2874%2990184-6) B. Pieraggi, F. Dabosi, M. Armand, Diagramme de phases des alliages hafnium-cuivre riches en hafnium, Journal of Nuclear Materials 52, 336-338 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2007.01.037](https://doi.org/10.1016/j.actamat.2007.01.037) G. Ghosh, First-principles calculations of structural energetics of Cu–TM (TM=Ti, Zr, Hf) intermetallics, Acta Materialia 55, 3347-3374 (2007).  
_cited as the source of values for this phase_

## CU51HF14 (Cu–Hf)

- Id: `phase:cu-hf:cu51hf14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.7846, Hf 0.2154
- Stability: stable in 3 of 3 calculated diagram(s): 300–1388 K, x(Hf) 0.21538–0.21538
- Literature: 37 values (36 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:cu51hf14)

Names (7): _corpus: _corpus:phase:cu-hf:cu51hf14  
_paper: _paper:10.1007/s11106-008-9008-4:Cu51Hf14, paper:10.1016/j.actamat.2012.10.014:Cu51Hf14, paper:10.1016/j.jallcom.2006.02.013:Cu51Hf14  
_tdb: _tdb:CuHf-06Lia.tdb:CU51HF14, tdb:CuHf-08Tur.tdb:CU51HF14, tdb:CuHf-13Zho.tdb:CU51HF14  


### TDB models of CU51HF14 (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): CU51HF14, type code %, sha256 `0c635db89455db21…`

~~~~text
45: PHASE CU51HF14 % 2 51 14 !
46: CONST CU51HF14 : CU : HF : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): CU51HF14, type code %, sha256 `06d472151340d413…`

~~~~text
53: PHASE CU51HF14 % 2 51 14 !
54: CONST CU51HF14 : CU : HF : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): CU51HF14, type code %, sha256 `e3133d3e66ab9d10…`

~~~~text
47: PHASE CU51HF14 % 2 51 14 !
48: CONST CU51HF14 : CU : HF : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1107/s0567740875003378](https://doi.org/10.1107/s0567740875003378) J.-P. Gabathuler, P. White, E. Parthé, Zr\<sub>14\</sub>Cu\<sub>51\</sub> and Hf\<sub>14\</sub>Cu\<sub>51\</sub> with GdAg\<sub>3.6\</sub> structure type, Acta Crystallogr B Struct Sci 31, 608-610 (1975).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877460](https://doi.org/10.1007/bf02877460) P.R. Subramanian, D.E. Laughlin, Bull. Alloy Phase Diagrams 9 (1) (1988) 51–55.  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5416(74)90021-4](https://doi.org/10.1016/0025-5416%2874%2990021-4) A.J Perry, Copper-Cu5Hf alloys: Their constitution and some properties after directional solidification, Materials Science and Engineering 13, 57-62 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667755](https://doi.org/10.1007/bf02667755) O. J. Kleppa, Shunroku Watanabe, Thermochemistry of alloys of transition metals: Part III. Copper-Silver, -Titanium, Zirconium, and -Hafnium at 1373 K, Metall Trans B 13, 391-401 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(74)90184-6](https://doi.org/10.1016/0022-3115%2874%2990184-6) B. Pieraggi, F. Dabosi, M. Armand, Diagramme de phases des alliages hafnium-cuivre riches en hafnium, Journal of Nuclear Materials 52, 336-338 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2007.01.037](https://doi.org/10.1016/j.actamat.2007.01.037) G. Ghosh, First-principles calculations of structural energetics of Cu–TM (TM=Ti, Zr, Hf) intermetallics, Acta Materialia 55, 3347-3374 (2007).  
_cited as the source of values for this phase_

## CU5HF_C15B (Cu–Hf)

- Id: `phase:cu-hf:cu5hf-c15b`; status `assigned`
- Structure: AuBe5 · C15_b · cF24 · F-43m (216); type `st:c15-b-aube5-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.8333, Hf 0.1667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1332.63 K, x(Hf) 0.16667–0.16667
- Literature: 25 values (24 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:cu5hf-c15b)

Names (7): _corpus: _corpus:phase:cu-hf:cu5hf-c15b  
_paper: _paper:10.1007/s11106-008-9008-4:Cu5Hf, paper:10.1016/j.actamat.2012.10.014:Cu5Hf, paper:10.1016/j.jallcom.2006.02.013:Cu5Hf  
_tdb: _tdb:CuHf-06Lia.tdb:CU5HF_C15B, tdb:CuHf-08Tur.tdb:CU5HF_C15B, tdb:CuHf-13Zho.tdb:CU5HF_C15B  


### TDB models of CU5HF_C15B (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): CU5HF_C15B, type code %, sha256 `0c635db89455db21…`

~~~~text
40: PHASE CU5HF_C15B % 2 5 1 !
41: CONST CU5HF_C15B : CU : HF : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): CU5HF_C15B, type code %, sha256 `06d472151340d413…`

~~~~text
48: PHASE CU5HF_C15B % 2 5 1 !
49: CONST CU5HF_C15B : CU : HF : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): CU5HF_C15B, type code %, sha256 `e3133d3e66ab9d10…`

~~~~text
42: PHASE CU5HF_C15B % 2 5 1 !
43: CONST CU5HF_C15B : CU : HF : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0025-5416(74)90021-4](https://doi.org/10.1016/0025-5416%2874%2990021-4) A.J Perry, Copper-Cu5Hf alloys: Their constitution and some properties after directional solidification, Materials Science and Engineering 13, 57-62 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2007.01.037](https://doi.org/10.1016/j.actamat.2007.01.037) G. Ghosh, First-principles calculations of structural energetics of Cu–TM (TM=Ti, Zr, Hf) intermetallics, Acta Materialia 55, 3347-3374 (2007).  
_cited as the source of values for this phase_

## CU8HF3 (Cu–Hf)

- Id: `phase:cu-hf:cu8hf3`; status `assigned`
- Structure: Cu8Hf3 · oP44 · Pnma (62); type `st:cu8hf3-op44`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cu 0.7273, Hf 0.2727
- Stability: stable in 3 of 3 calculated diagram(s): 300–1274.49 K, x(Hf) 0.27273–0.27273
- Literature: 26 values (26 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:cu8hf3)

Names (9): _corpus: _corpus:phase:cu-hf:cu8hf3  
_mp: _mp:mp-aaaaakwv  
_oqmd: _oqmd:oqmd-32345  
_paper: _paper:10.1007/s11106-008-9008-4:Cu8Hf3, paper:10.1016/j.actamat.2012.10.014:Cu8Hf3, paper:10.1016/j.jallcom.2006.02.013:Cu8Hf3  
_tdb: _tdb:CuHf-06Lia.tdb:CU8HF3, tdb:CuHf-08Tur.tdb:CU8HF3, tdb:CuHf-13Zho.tdb:CU8HF3  


### TDB models of CU8HF3 (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): CU8HF3, type code %, sha256 `0c635db89455db21…`

~~~~text
50: PHASE CU8HF3 % 2 8 3 !
51: CONST CU8HF3 : CU : HF : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): CU8HF3, type code %, sha256 `06d472151340d413…`

~~~~text
58: PHASE CU8HF3 % 2 8 3 !
59: CONST CU8HF3 : CU : HF : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): CU8HF3, type code %, sha256 `e3133d3e66ab9d10…`

~~~~text
52: PHASE CU8HF3 % 2 8 3 !
53: CONST CU8HF3 : CU : HF : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(75)90085-5](https://doi.org/10.1016/0022-5088%2875%2990085-5) Lars Bsenko, Crystallographic data for intermediate phases in the copper-zirconium and copper-hafnium systems, Journal of the Less Common Metals 40, 365-366 (1975).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877460](https://doi.org/10.1007/bf02877460) P.R. Subramanian, D.E. Laughlin, Bull. Alloy Phase Diagrams 9 (1) (1988) 51–55.  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2007.01.037](https://doi.org/10.1016/j.actamat.2007.01.037) G. Ghosh, First-principles calculations of structural energetics of Cu–TM (TM=Ti, Zr, Hf) intermetallics, Acta Materialia 55, 3347-3374 (2007).  
_cited as the source of values for this phase_

## CUHF2 (Cu–Hf)

- Id: `phase:cu-hf:cuhf2`; status `assigned`
- Structure: CuZr2 · tI6 · I4/mmm (139); type `st:cuzr2-ti6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.3333, Hf 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1611.26 K, x(Hf) 0.66667–0.66667
- Literature: 39 values (38 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:cuhf2)

Names (7): _corpus: _corpus:phase:cu-hf:cuhf2  
_paper: _paper:10.1007/s11106-008-9008-4:CuHf2, paper:10.1016/j.actamat.2012.10.014:CuHf2, paper:10.1016/j.jallcom.2006.02.013:CuHf2  
_tdb: _tdb:CuHf-06Lia.tdb:CUHF2, tdb:CuHf-08Tur.tdb:CUHF2, tdb:CuHf-13Zho.tdb:CUHF2  


### TDB models of CUHF2 (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): CUHF2, type code %, sha256 `0c635db89455db21…`

~~~~text
60: PHASE CUHF2 % 2 1 2 !
61: CONST CUHF2 : CU : HF : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): CUHF2, type code %, sha256 `06d472151340d413…`

~~~~text
68: PHASE CUHF2 % 2 1 2 !
69: CONST CUHF2 : CU : HF : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): CUHF2, type code %, sha256 `e3133d3e66ab9d10…`

~~~~text
62: PHASE CUHF2 % 2 1 2 !
63: CONST CUHF2 : CU : HF : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-3115(74)90184-6](https://doi.org/10.1016/0022-3115%2874%2990184-6) B. Pieraggi, F. Dabosi, M. Armand, Diagramme de phases des alliages hafnium-cuivre riches en hafnium, Journal of Nuclear Materials 52, 336-338 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667755](https://doi.org/10.1007/bf02667755) O. J. Kleppa, Shunroku Watanabe, Thermochemistry of alloys of transition metals: Part III. Copper-Silver, -Titanium, Zirconium, and -Hafnium at 1373 K, Metall Trans B 13, 391-401 (1982).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02736446](https://doi.org/10.1007/bf02736446) R. H. Woodman, B. R. Klotz, L. J. Kecskes, Observation of incongruent melting in Cu10Hf7, JPED 27, 477-481 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877460](https://doi.org/10.1007/bf02877460) P.R. Subramanian, D.E. Laughlin, Bull. Alloy Phase Diagrams 9 (1) (1988) 51–55.  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2007.01.037](https://doi.org/10.1016/j.actamat.2007.01.037) G. Ghosh, First-principles calculations of structural energetics of Cu–TM (TM=Ti, Zr, Hf) intermetallics, Acta Materialia 55, 3347-3374 (2007).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Hf)

- Id: `phase:cu-hf:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1387.77 K, x(Hf) 0–0.0042
- Literature: 13 values (12 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:fcc-a1)

Names (7): _corpus: _corpus:phase:cu-hf:fcc-a1  
_paper: _paper:10.1007/s11106-008-9008-4:(Cu), paper:10.1016/j.actamat.2012.10.014:fcc, paper:10.1016/j.jallcom.2006.02.013:fcc  
_tdb: _tdb:CuHf-06Lia.tdb:FCC_A1, tdb:CuHf-08Tur.tdb:FCC_A1, tdb:CuHf-13Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): FCC_A1, type code %A, sha256 `0c635db89455db21…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CU% HF : VA : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): FCC_A1, type code %A, sha256 `06d472151340d413…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CU% HF : VA : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): FCC_A1, type code %A, sha256 `e3133d3e66ab9d10…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CU% HF : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0025-5416(74)90021-4](https://doi.org/10.1016/0025-5416%2874%2990021-4) A.J Perry, Copper-Cu5Hf alloys: Their constitution and some properties after directional solidification, Materials Science and Engineering 13, 57-62 (1974).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Hf)

- Id: `phase:cu-hf:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2501.02 K, x(Hf) 0.99379–1
- Literature: 15 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:hcp-a3)

Names (7): _corpus: _corpus:phase:cu-hf:hcp-a3  
_paper: _paper:10.1007/s11106-008-9008-4:(αHf), paper:10.1016/j.actamat.2012.10.014:hcp, paper:10.1016/j.jallcom.2006.02.013:hcp  
_tdb: _tdb:CuHf-06Lia.tdb:HCP_A3, tdb:CuHf-08Tur.tdb:HCP_A3, tdb:CuHf-13Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): HCP_A3, type code %A, sha256 `0c635db89455db21…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CU HF% : VA : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): HCP_A3, type code %A, sha256 `06d472151340d413…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CU HF% : VA : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): HCP_A3, type code %A, sha256 `e3133d3e66ab9d10…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CU HF% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(74)90184-6](https://doi.org/10.1016/0022-3115%2874%2990184-6) B. Pieraggi, F. Dabosi, M. Armand, Diagramme de phases des alliages hafnium-cuivre riches en hafnium, Journal of Nuclear Materials 52, 336-338 (1974).  
_cited as the source of values for this phase_

## LIQUID (Cu–Hf)

- Id: `phase:cu-hf:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1233.92–4000 K, x(Hf) 0–1
- Literature: 76 values (73 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-hf:liquid)

Names (10): _corpus: _corpus:phase:cu-hf:liquid  
_paper: _paper:10.1007/s11106-008-9008-4:L, paper:10.1016/j.actamat.2012.10.014:L, paper:10.1016/j.actamat.2012.10.014:Liquid, paper:10.1016/j.actamat.2012.10.014:liquid, paper:10.1016/j.jallcom.2006.02.013:Liquid, paper:10.1016/j.jallcom.2006.02.013:liquid  
_tdb: _tdb:CuHf-06Lia.tdb:LIQUID, tdb:CuHf-08Tur.tdb:LIQUID, tdb:CuHf-13Zho.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CuHf-06Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-06Lia.tdb): LIQUID, type code %, sha256 `0c635db89455db21…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CU HF : !
~~~~

[CuHf-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-08Tur.tdb): LIQUID, type code %, sha256 `06d472151340d413…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CU CUHF CUHF3 HF : !
~~~~

[CuHf-13Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CuHf-13Zho.tdb): LIQUID, type code %, sha256 `e3133d3e66ab9d10…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CU HF : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.actamat.2012.10.014](https://doi.org/10.1016/j.actamat.2012.10.014) Yu Zhong, Arkapol Saengdeejing, Laszlo Kecskes, Bradley Klotz, Zi-Kui Liu, Experimental and computational studies of the Cu–Hf binary system, Acta Materialia 61, 660-669 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-008-9008-4](https://doi.org/10.1007/s11106-008-9008-4) M. A. Turchanin, P. G. Agraval, Thermodynamic assessment of the copper-hafnium system, Powder Metall Met Ceram 47, 223-233 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.02.013](https://doi.org/10.1016/j.jallcom.2006.02.013) Dong Liang, Yajun Liu, Reevaluation of the Cu–Hf binary system, Journal of Alloys and Compounds 426, 101-105 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(74)90184-6](https://doi.org/10.1016/0022-3115%2874%2990184-6) B. Pieraggi, F. Dabosi, M. Armand, Diagramme de phases des alliages hafnium-cuivre riches en hafnium, Journal of Nuclear Materials 52, 336-338 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877460](https://doi.org/10.1007/bf02877460) P.R. Subramanian, D.E. Laughlin, Bull. Alloy Phase Diagrams 9 (1) (1988) 51–55.  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5416(74)90021-4](https://doi.org/10.1016/0025-5416%2874%2990021-4) A.J Perry, Copper-Cu5Hf alloys: Their constitution and some properties after directional solidification, Materials Science and Engineering 13, 57-62 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02736446](https://doi.org/10.1007/bf02736446) R. H. Woodman, B. R. Klotz, L. J. Kecskes, Observation of incongruent melting in Cu10Hf7, JPED 27, 477-481 (2006).  
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
