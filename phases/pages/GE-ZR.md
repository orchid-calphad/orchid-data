# Ge–Zr phases

> Ge–Zr system: 10 phases (tier A 7, tier B 1, tier C 1, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/GE-ZR.md

10 phases (tier A 7, tier B 1, tier C 1, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/GE-ZR.json) · [Ge–Zr system page](https://data.orchid-project.org/systems/GE-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Zr system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-zr-a4-diamond); _phase:ge-zr:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Zr) 0–0 | 3 | 1 |
| [BCC_A2](#phase-ge-zr-bcc-a2); _phase:ge-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300.62–3589.4 K, x(Zr) 0.99064–1 | 4 | 1 |
| [FCC_A1](#phase-ge-zr-fcc-a1); _phase:ge-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GE2ZR_C49](#phase-ge-zr-ge2zr-c49); _phase:ge-zr:ge2zr-c49_ | ZrSi2 · C49 · oC12 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1793.07 K, x(Zr) 0.33333–0.33333 | 4 | 1 |
| [GE3ZR5_D88](#phase-ge-zr-ge3zr5-d88); _phase:ge-zr:ge3zr5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2612.53 K, x(Zr) 0.625–0.625 | 5 | 1 |
| [GE4ZR5](#phase-ge-zr-ge4zr5); _phase:ge-zr:ge4zr5_ | Si4Zr5 · tP36 · P4_12_12 (92) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2537.53 K, x(Zr) 0.55556–0.55556 | 3 | 1 |
| [GEZR_B27](#phase-ge-zr-gezr-b27); _phase:ge-zr:gezr-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2497.63 K, x(Zr) 0.5–0.5 | 4 | 1 |
| [GEZR3](#phase-ge-zr-gezr3); _phase:ge-zr:gezr3_ | Ti3P · tP32 · P4_2/n (86) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1864.93 K, x(Zr) 0.75–0.75 | 6 | 1 |
| [HCP_A3](#phase-ge-zr-hcp-a3); _phase:ge-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1168.84 K, x(Zr) 0.99058–1 | 0 | 1 |
| [LIQUID](#phase-ge-zr-liquid); _phase:ge-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1206.93–4000 K, x(Zr) 0–1 | 13 | 1 |

## DIAMOND_A4 (Ge–Zr)

- Id: `phase:ge-zr:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Zr) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:a4-diamond)

Names (5): _corpus: _corpus:phase:ge-zr:a4-diamond, corpus:phase:ge-zr:diamond-a4  
_paper: _paper:10.1007/s10853-010-4934-1:(Ge), paper:10.1007/s10853-010-4934-1:Ge  
_tdb: _tdb:GeZr-11Sha.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): DIAMOND_A4, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874981](https://doi.org/10.1007/bf02874981) Abriata JP, Block JC, Arias D (1986) Bull Alloy Phase Diagr 7:43 1413  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Zr)

- Id: `phase:ge-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.62–3589.4 K, x(Zr) 0.99064–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:bcc-a2)

Names (3): _corpus: _corpus:phase:ge-zr:bcc-a2  
_paper: _paper:10.1007/s10853-010-4934-1:(βZr)  
_tdb: _tdb:GeZr-11Sha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): BCC_A2, type code %B, sha256 `407ab2d6f3ec81a0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GE ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ge–Zr)

- Id: `phase:ge-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-zr:fcc-a1  
_tdb: _tdb:GeZr-11Sha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): FCC_A1, type code %A, sha256 `407ab2d6f3ec81a0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GE ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase_

## GE2ZR_C49 (Ge–Zr)

- Id: `phase:ge-zr:ge2zr-c49`; status `assigned`
- Structure: ZrSi2 · C49 · oC12 · Cmcm (63); type `st:c49-zrsi2-oc12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadpm and oqmd-3541, space group 63
- Stoichiometry: Ge 0.6667, Zr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1793.07 K, x(Zr) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:ge2zr-c49)

Names (5): _corpus: _corpus:phase:ge-zr:ge2zr-c49  
_mp: _mp:mp-aaaaadpm  
_oqmd: _oqmd:oqmd-3541  
_paper: _paper:10.1007/s10853-010-4934-1:ZrGe2  
_tdb: _tdb:GeZr-11Sha.tdb:GE2ZR_C49  


### TDB models of GE2ZR_C49 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): GE2ZR_C49, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
46: PHASE GE2ZR_C49 % 2 2 1 !
47: CONST GE2ZR_C49 : GE : ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874981](https://doi.org/10.1007/bf02874981) Abriata JP, Block JC, Arias D (1986) Bull Alloy Phase Diagr 7:43 1413  
_cited as the source of values for this phase_

## GE3ZR5_D88 (Ge–Zr)

- Id: `phase:ge-zr:ge3zr5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabafa and oqmd-13725, space group 193
- Stoichiometry: Ge 0.3750, Zr 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–2612.53 K, x(Zr) 0.625–0.625
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:ge3zr5-d88)

Names (5): _corpus: _corpus:phase:ge-zr:ge3zr5-d88  
_mp: _mp:mp-aaaabafa  
_oqmd: _oqmd:oqmd-13725  
_paper: _paper:10.1007/s10853-010-4934-1:Zr5Ge3  
_tdb: _tdb:GeZr-11Sha.tdb:GE3ZR5_D88  


### TDB models of GE3ZR5_D88 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): GE3ZR5_D88, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
61: PHASE GE3ZR5_D88 % 2 3 5 !
62: CONST GE3ZR5_D88 : GE : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_

## GE4ZR5 (Ge–Zr)

- Id: `phase:ge-zr:ge4zr5`; status `assigned`
- Structure: Si4Zr5 · tP36 · P4_12_12 (92); type `st:si4zr5-tp36`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ge 0.4444, Zr 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–2537.53 K, x(Zr) 0.55556–0.55556
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:ge4zr5)

Names (5): _corpus: _corpus:phase:ge-zr:ge4zr5  
_mp: _mp:mp-aaacqigr  
_oqmd: _oqmd:oqmd-2052678  
_paper: _paper:10.1007/s10853-010-4934-1:Zr5Ge4  
_tdb: _tdb:GeZr-11Sha.tdb:GE4ZR5  


### TDB models of GE4ZR5 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): GE4ZR5, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
56: PHASE GE4ZR5 % 2 4 5 !
57: CONST GE4ZR5 : GE : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_

## GEZR_B27 (Ge–Zr)

- Id: `phase:ge-zr:gezr-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacgjav and oqmd-30506, space group 62
- Stoichiometry: Ge 0.5000, Zr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2497.63 K, x(Zr) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:gezr-b27)

Names (5): _corpus: _corpus:phase:ge-zr:gezr-b27  
_mp: _mp:mp-aaacgjav  
_oqmd: _oqmd:oqmd-30506  
_paper: _paper:10.1007/s10853-010-4934-1:ZrGe  
_tdb: _tdb:GeZr-11Sha.tdb:GEZR_B27  


### TDB models of GEZR_B27 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): GEZR_B27, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
51: PHASE GEZR_B27 % 2 1 1 !
52: CONST GEZR_B27 : GE : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_

## GEZR3 (Ge–Zr)

- Id: `phase:ge-zr:gezr3`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.2500, Zr 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1864.93 K, x(Zr) 0.75–0.75
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:gezr3)

Names (3): _corpus: _corpus:phase:ge-zr:gezr3  
_paper: _paper:10.1007/s10853-010-4934-1:Zr3Ge  
_tdb: _tdb:GeZr-11Sha.tdb:GEZR3  


### TDB models of GEZR3 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): GEZR3, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
66: PHASE GEZR3 % 2 1 3 !
67: CONST GEZR3 : GE : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ge–Zr)

- Id: `phase:ge-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1168.84 K, x(Zr) 0.99058–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-zr:hcp-a3  
_tdb: _tdb:GeZr-11Sha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): HCP_A3, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : GE ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase_

## LIQUID (Ge–Zr)

- Id: `phase:ge-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1206.93–4000 K, x(Zr) 0–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-zr:liquid)

Names (3): _corpus: _corpus:phase:ge-zr:liquid  
_paper: _paper:10.1007/s10853-010-4934-1:Liquid  
_tdb: _tdb:GeZr-11Sha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeZr-11Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/GeZr-11Sha.tdb): LIQUID, type code %, sha256 `407ab2d6f3ec81a0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GE ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-010-4934-1](https://doi.org/10.1007/s10853-010-4934-1) Chunsheng Sha, Liangcai Zhou, Shuhong Liu, Yong Du, Tie Gang, Honghui Xu, Phase equilibria and thermodynamic modeling in the Ge–Zr binary system, J Mater Sci 46, 1405-1413 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874981](https://doi.org/10.1007/bf02874981) Abriata JP, Block JC, Arias D (1986) Bull Alloy Phase Diagr 7:43 1413  
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
