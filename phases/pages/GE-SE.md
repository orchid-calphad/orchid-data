# Ge–Se phases

> Ge–Se system: 11 phases (tier A 7, tier C 3, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-SE.html · Markdown: https://data.orchid-project.org/phases/pages/GE-SE.md

11 phases (tier A 7, tier C 3, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-SE) · [full JSON](https://data.orchid-project.org/phases/systems/GE-SE.json) · [Ge–Se system page](https://data.orchid-project.org/systems/GE-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Se system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-se-a4-diamond); _phase:ge-se:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Se) 0–0 | 0 | 1 |
| [HEXAGONAL_A8](#phase-ge-se-a8-hexagonal); _phase:ge-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1 | 0 | 1 |
| [BCC_A2](#phase-ge-se-bcc-a2); _phase:ge-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ge-se-fcc-a1); _phase:ge-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GE3SE7](#phase-ge-se-ge3se7); _phase:ge-se:ge3se7_ | Ge4Se9 · oP52 · Pca2_1 (29) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–653.06 K, x(Se) 0.7–0.7 | 0 | 1 |
| [GESE_B1](#phase-ge-se-gese-b1); _phase:ge-se:gese-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 930.58–956.23 K, x(Se) 0.5–0.5 | 0 | 1 |
| [GESE_B16](#phase-ge-se-gese-b16); _phase:ge-se:gese-b16_ | GeS · B16 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–930.58 K, x(Se) 0.5–0.5 | 0 | 1 |
| [GESE2_ALPHA](#phase-ge-se-gese2-alpha); _phase:ge-se:gese2-alpha_ | GeS2-beta · mP48 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–420 K, x(Se) 0.66667–0.66667 | 0 | 1 |
| [GESE2_BETA](#phase-ge-se-gese2-beta); _phase:ge-se:gese2-beta_ | GeSe2 · tI12 · I-4 (82) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 420–1027.17 K, x(Se) 0.66667–0.66667 | 0 | 1 |
| [HCP_A3](#phase-ge-se-hcp-a3); _phase:ge-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ge-se-liquid); _phase:ge-se:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 469.66–2500 K, x(Se) 0–1 | 0 | 1 |

## DIAMOND_A4 (Ge–Se)

- Id: `phase:ge-se:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Se) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:a4-diamond)

Names (2): _corpus: _corpus:phase:ge-se:a4-diamond  
_tdb: _tdb:GeSe-22Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): DIAMOND_A4, type code %, sha256 `04b410a9a7212717…`

~~~~text
50: PHASE DIAMOND_A4 % 1 1 !
51: CONST DIAMOND_A4 : GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## HEXAGONAL_A8 (Ge–Se)

- Id: `phase:ge-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:a8-hexagonal)

Names (2): _corpus: _corpus:phase:ge-se:a8-hexagonal  
_tdb: _tdb:GeSe-22Che.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): HEXAGONAL_A8, type code %, sha256 `04b410a9a7212717…`

~~~~text
55: PHASE HEXAGONAL_A8 % 1 1 !
56: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## BCC_A2 (Ge–Se)

- Id: `phase:ge-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-se:bcc-a2  
_tdb: _tdb:GeSe-22Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): BCC_A2, type code %B, sha256 `04b410a9a7212717…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## FCC_A1 (Ge–Se)

- Id: `phase:ge-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-se:fcc-a1  
_tdb: _tdb:GeSe-22Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): FCC_A1, type code %A, sha256 `04b410a9a7212717…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GE3SE7 (Ge–Se)

- Id: `phase:ge-se:ge3se7`; status `assigned`
- Structure: Ge4Se9 · oP52 · Pca2_1 (29); type `st:ge4se9-op52`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.3000, Se 0.7000
- Stability: stable in 1 of 1 calculated diagram(s): 300–653.06 K, x(Se) 0.7–0.7
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:ge3se7)

Names (2): _corpus: _corpus:phase:ge-se:ge3se7  
_tdb: _tdb:GeSe-22Che.tdb:GE3SE7  


### TDB models of GE3SE7 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): GE3SE7, type code %, sha256 `04b410a9a7212717…`

~~~~text
80: PHASE GE3SE7 % 2 3 7 !
81: CONST GE3SE7 : GE : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GESE_B1 (Ge–Se)

- Id: `phase:ge-se:gese-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 0.5000, Se 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 930.58–956.23 K, x(Se) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:gese-b1)

Names (2): _corpus: _corpus:phase:ge-se:gese-b1  
_tdb: _tdb:GeSe-22Che.tdb:GESE_B1  


### TDB models of GESE_B1 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): GESE_B1, type code %, sha256 `04b410a9a7212717…`

~~~~text
65: PHASE GESE_B1 % 2 1 1 !
66: CONST GESE_B1 : GE : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GESE_B16 (Ge–Se)

- Id: `phase:ge-se:gese-b16`; status `assigned`
- Structure: GeS · B16 · oP8 · Pnma (62); type `st:b16-ges-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 0.5000, Se 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–930.58 K, x(Se) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:gese-b16)

Names (2): _corpus: _corpus:phase:ge-se:gese-b16  
_tdb: _tdb:GeSe-22Che.tdb:GESE_B16  


### TDB models of GESE_B16 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): GESE_B16, type code %, sha256 `04b410a9a7212717…`

~~~~text
60: PHASE GESE_B16 % 2 1 1 !
61: CONST GESE_B16 : GE : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GESE2_ALPHA (Ge–Se)

- Id: `phase:ge-se:gese2-alpha`; status `assigned`
- Structure: GeS2-beta · mP48 · P2_1/c (14); type `st:ges2-beta-mp48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.3333, Se 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–420 K, x(Se) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:gese2-alpha)

Names (2): _corpus: _corpus:phase:ge-se:gese2-alpha  
_tdb: _tdb:GeSe-22Che.tdb:GESE2_ALPHA  


### TDB models of GESE2_ALPHA (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): GESE2_ALPHA, type code %, sha256 `04b410a9a7212717…`

~~~~text
70: PHASE GESE2_ALPHA % 2 1 2 !
71: CONST GESE2_ALPHA : GE : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GESE2_BETA (Ge–Se)

- Id: `phase:ge-se:gese2-beta`; status `assigned`
- Structure: GeSe2 · tI12 · I-4 (82); type `st:gese2-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.3333, Se 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 420–1027.17 K, x(Se) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:gese2-beta)

Names (2): _corpus: _corpus:phase:ge-se:gese2-beta  
_tdb: _tdb:GeSe-22Che.tdb:GESE2_BETA  


### TDB models of GESE2_BETA (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): GESE2_BETA, type code %, sha256 `04b410a9a7212717…`

~~~~text
75: PHASE GESE2_BETA % 2 1 2 !
76: CONST GESE2_BETA : GE : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## HCP_A3 (Ge–Se)

- Id: `phase:ge-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-se:hcp-a3  
_tdb: _tdb:GeSe-22Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): HCP_A3, type code %A, sha256 `04b410a9a7212717…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## LIQUID (Ge–Se)

- Id: `phase:ge-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 469.66–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-se:liquid)

Names (2): _corpus: _corpus:phase:ge-se:liquid  
_tdb: _tdb:GeSe-22Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeSe-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb): LIQUID, type code %, sha256 `04b410a9a7212717…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : GE GESE2 SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

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
