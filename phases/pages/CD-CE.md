# Cd–Ce phases

> Cd–Ce system: 11 phases (tier A 6, tier C 4, liquid 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-CE.html · Markdown: https://data.orchid-project.org/phases/pages/CD-CE.md

11 phases (tier A 6, tier C 4, liquid 1); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-CE) · [full JSON](https://data.orchid-project.org/phases/systems/CD-CE.json) · [Cd–Ce system page](https://data.orchid-project.org/systems/CD-CE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-CE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Ce system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-ce-bcc-a2); _phase:cd-ce:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 707.62–1072 K, x(Ce) 0.89747–1 | 0 | 1 |
| [CD11CE_D2E](#phase-cd-ce-cd11ce-d2e); _phase:cd-ce:cd11ce-d2e_ | BaHg11 · D2_e · cP36 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–882.41 K, x(Ce) 0.08333–0.08333 | 0 | 1 |
| [CD17CE2](#phase-cd-ce-cd17ce2); _phase:cd-ce:cd17ce2_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 804.29–885.7 K, x(Ce) 0.10526–0.10526 | 0 | 1 |
| [CD2CE](#phase-cd-ce-cd2ce); _phase:cd-ce:cd2ce_ | Cd2Ce · hP3 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1255.19 K, x(Ce) 0.33333–0.34703 | 0 | 1 |
| [CD3CE_D03](#phase-cd-ce-cd3ce-d03); _phase:cd-ce:cd3ce-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1130 K, x(Ce) 0.25–0.25 | 0 | 1 |
| [CD58CE13](#phase-cd-ce-cd58ce13); _phase:cd-ce:cd58ce13_ | Gd13Zn58 · hP142 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1146.71 K, x(Ce) 0.17623–0.18406 | 0 | 1 |
| [CD6CE](#phase-cd-ce-cd6ce); _phase:cd-ce:cd6ce_ | Cd37Ce6 · cP188 · Pn-3 (201) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1003.31 K, x(Ce) 0.14286–0.14286 | 0 | 1 |
| [CDCE_B2](#phase-cd-ce-cdce-b2); _phase:cd-ce:cdce-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1232.74 K, x(Ce) 0.5–0.51832 | 0 | 1 |
| [FCC_A1](#phase-cd-ce-fcc-a1); _phase:cd-ce:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1065 K, x(Ce) 0.98814–1 | 0 | 1 |
| [HCP_A3](#phase-cd-ce-hcp-a3); _phase:cd-ce:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–594.22 K, x(Ce) 0–0 | 0 | 1 |
| [LIQUID](#phase-cd-ce-liquid); _phase:cd-ce:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 594.22–2500 K, x(Ce) 0–1 | 0 | 1 |

## BCC_A2 (Cd–Ce)

- Id: `phase:cd-ce:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 707.62–1072 K, x(Ce) 0.89747–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-ce:bcc-a2  
_tdb: _tdb:CdCe-23Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): BCC_A2, type code %B, sha256 `4d8c062ecb33af20…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CD CE% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## CD11CE_D2E (Cd–Ce)

- Id: `phase:cd-ce:cd11ce-d2e`; status `assigned`
- Structure: BaHg11 · D2_e · cP36 · Pm-3m (221); type `st:d2-e-bahg11-cp36`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabkkwv and oqmd-19353, space group 221
- Stoichiometry: Cd 0.9167, Ce 0.0833
- Stability: stable in 1 of 1 calculated diagram(s): 300–882.41 K, x(Ce) 0.08333–0.08333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:cd11ce-d2e)

Names (4): _corpus: _corpus:phase:cd-ce:cd11ce-d2e  
_mp: _mp:mp-aaabkkwv  
_oqmd: _oqmd:oqmd-19353  
_tdb: _tdb:CdCe-23Liu.tdb:CD11CE_D2E  


### TDB models of CD11CE_D2E (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): CD11CE_D2E, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
48: PHASE CD11CE_D2E % 2 11 1 !
49: CONST CD11CE_D2E : CD : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## CD17CE2 (Cd–Ce)

- Id: `phase:cd-ce:cd17ce2`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.8947, Ce 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 804.29–885.7 K, x(Ce) 0.10526–0.10526
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:cd17ce2)

Names (2): _corpus: _corpus:phase:cd-ce:cd17ce2  
_tdb: _tdb:CdCe-23Liu.tdb:CD17CE2  


### TDB models of CD17CE2 (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): CD17CE2, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
53: PHASE CD17CE2 % 2 17 2 !
54: CONST CD17CE2 : CD : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## CD2CE (Cd–Ce)

- Id: `phase:cd-ce:cd2ce`; status `assigned`
- Structure: Cd2Ce · hP3 · P-3m1 (164); type `st:cd2ce-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1255.19 K, x(Ce) 0.33333–0.34703
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:cd2ce)

Names (2): _corpus: _corpus:phase:cd-ce:cd2ce  
_tdb: _tdb:CdCe-23Liu.tdb:CD2CE  


### TDB models of CD2CE (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): CD2CE, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
73: PHASE CD2CE % 2 2 1 !
74: CONST CD2CE : CD% CE : CD CE% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## CD3CE_D03 (Cd–Ce)

- Id: `phase:cd-ce:cd3ce-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.7500, Ce 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1130 K, x(Ce) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:cd3ce-d03)

Names (2): _corpus: _corpus:phase:cd-ce:cd3ce-d03  
_tdb: _tdb:CdCe-23Liu.tdb:CD3CE_D03  


### TDB models of CD3CE_D03 (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): CD3CE_D03, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
68: PHASE CD3CE_D03 % 2 3 1 !
69: CONST CD3CE_D03 : CD : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## CD58CE13 (Cd–Ce)

- Id: `phase:cd-ce:cd58ce13`; status `assigned`
- Structure: Gd13Zn58 · hP142 · P6_3/mmc (194); type `st:gd13zn58-hp142`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1146.71 K, x(Ce) 0.17623–0.18406
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:cd58ce13)

Names (2): _corpus: _corpus:phase:cd-ce:cd58ce13  
_tdb: _tdb:CdCe-23Liu.tdb:CD58CE13  


### TDB models of CD58CE13 (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): CD58CE13, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
63: PHASE CD58CE13 % 2 58 13 !
64: CONST CD58CE13 : CD% CE : CD CE% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## CD6CE (Cd–Ce)

- Id: `phase:cd-ce:cd6ce`; status `assigned`
- Structure: Cd37Ce6 · cP188 · Pn-3 (201); type `st:cd37ce6-cp188`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.8571, Ce 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–1003.31 K, x(Ce) 0.14286–0.14286
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:cd6ce)

Names (2): _corpus: _corpus:phase:cd-ce:cd6ce  
_tdb: _tdb:CdCe-23Liu.tdb:CD6CE  


### TDB models of CD6CE (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): CD6CE, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
58: PHASE CD6CE % 2 6 1 !
59: CONST CD6CE : CD : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## CDCE_B2 (Cd–Ce)

- Id: `phase:cd-ce:cdce-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CdCe-23Liu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1232.74 K, x(Ce) 0.5–0.51832
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:cdce-b2)

Names (2): _corpus: _corpus:phase:cd-ce:cdce-b2  
_tdb: _tdb:CdCe-23Liu.tdb:CDCE_B2  


### TDB models of CDCE_B2 (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): CDCE_B2, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
78: PHASE CDCE_B2 % 2 1 1 !
79: CONST CDCE_B2 : CD% CE : CE CD% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## FCC_A1 (Cd–Ce)

- Id: `phase:cd-ce:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1065 K, x(Ce) 0.98814–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-ce:fcc-a1  
_tdb: _tdb:CdCe-23Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): FCC_A1, type code %A, sha256 `4d8c062ecb33af20…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CD CE% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## HCP_A3 (Cd–Ce)

- Id: `phase:cd-ce:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–594.22 K, x(Ce) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:hcp-a3)

Names (2): _corpus: _corpus:phase:cd-ce:hcp-a3  
_tdb: _tdb:CdCe-23Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): HCP_A3, type code %A, sha256 `4d8c062ecb33af20…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CD% CE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
_assessment that models this phase_

## LIQUID (Cd–Ce)

- Id: `phase:cd-ce:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 594.22–2500 K, x(Ce) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ce:liquid)

Names (2): _corpus: _corpus:phase:cd-ce:liquid  
_tdb: _tdb:CdCe-23Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdCe-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCe-23Liu.tdb): LIQUID, type code %, sha256 `4d8c062ecb33af20…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CD CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8214](https://doi.org/10.1515/ijmr-2021-8214) J. Liu, X. Huang, Q. Du, L. Ouyang, J. Xiao, Y. Li, Int. J. Mater. Res., 114, 1101-10(2023).  
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
