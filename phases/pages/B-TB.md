# B–Tb phases

> B–Tb system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-TB.html · Markdown: https://data.orchid-project.org/phases/pages/B-TB.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-TB) · [full JSON](https://data.orchid-project.org/phases/systems/B-TB.json) · [Markdown](https://data.orchid-project.org/phases/pages/B-TB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Tb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-tb-b-alpha-rhombo); _phase:b-tb:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-tb-b-beta-rhombo); _phase:b-tb:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2350.35 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-tb-bcc-a2); _phase:b-tb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1562–3999.5 K, x(B) 0–0 | 0 | 1 |
| [HCP_A3](#phase-b-tb-hcp-a3); _phase:b-tb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1562 K, x(B) 0–0 | 0 | 1 |
| [LIQUID](#phase-b-tb-liquid); _phase:b-tb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1473.31–4000 K, x(B) 0–1 | 0 | 1 |
| [TBB12_D2F](#phase-b-tb-tbb12-d2f); _phase:b-tb:tbb12-d2f_ | UB12 · D2_f · cF52 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2472.5 K, x(B) 0.92308–0.92308 | 0 | 1 |
| [TBB2_C32](#phase-b-tb-tbb2-c32); _phase:b-tb:tbb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2373.37 K, x(B) 0.66667–0.66667 | 0 | 1 |
| [TBB4_D1E](#phase-b-tb-tbb4-d1e); _phase:b-tb:tbb4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2872.59 K, x(B) 0.8–0.8 | 0 | 1 |
| [TBB6_D21](#phase-b-tb-tbb6-d21); _phase:b-tb:tbb6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2613.15 K, x(B) 0.85714–0.85714 | 0 | 1 |
| [TBB66](#phase-b-tb-tbb66); _phase:b-tb:tbb66_ | YB66 · cF1936 · Fm-3c (226) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1029.19–2374.12 K, x(B) 0.98507–0.98507 | 0 | 1 |

## ALPHA_RHOMBO_B (B–Tb)

- Id: `phase:b-tb:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — TbB-22Wei.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-tb:b-alpha-rhombo  
_tdb: _tdb:TbB-22Wei.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): ALPHA_RHOMBO_B, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
35: PHASE ALPHA_RHOMBO_B % 1 1 !
36: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Tb)

- Id: `phase:b-tb:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — TbB-22Wei.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2350.35 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-tb:b-beta-rhombo  
_tdb: _tdb:TbB-22Wei.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): BETA_RHOMBO_B, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
40: PHASE BETA_RHOMBO_B % 1 1 !
41: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## BCC_A2 (B–Tb)

- Id: `phase:b-tb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Tb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1562–3999.5 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:bcc-a2)

Names (2): _corpus: _corpus:phase:b-tb:bcc-a2  
_tdb: _tdb:TbB-22Wei.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): BCC_A2, type code %B, sha256 `21c9d9c830b1c061…`

~~~~text
25: PHASE BCC_A2 %B 2 1 3 !
26: CONST BCC_A2 : TB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## HCP_A3 (B–Tb)

- Id: `phase:b-tb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Tb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1562 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:hcp-a3)

Names (2): _corpus: _corpus:phase:b-tb:hcp-a3  
_tdb: _tdb:TbB-22Wei.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): HCP_A3, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
30: PHASE HCP_A3 % 2 1 0.5 !
31: CONST HCP_A3 : TB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## LIQUID (B–Tb)

- Id: `phase:b-tb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1473.31–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:liquid)

Names (2): _corpus: _corpus:phase:b-tb:liquid  
_tdb: _tdb:TbB-22Wei.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): LIQUID, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : B TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## TBB12_D2F (B–Tb)

- Id: `phase:b-tb:tbb12-d2f`; status `assigned`
- Structure: UB12 · D2_f · cF52 · Fm-3m (225); type `st:d2-f-ub12-cf52`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackvgc and oqmd-28615, space group 225
- Stoichiometry: B 0.9231, Tb 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–2472.5 K, x(B) 0.92308–0.92308
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:tbb12-d2f)

Names (4): _corpus: _corpus:phase:b-tb:tbb12-d2f  
_mp: _mp:mp-aaackvgc  
_oqmd: _oqmd:oqmd-28615  
_tdb: _tdb:TbB-22Wei.tdb:TBB12_D2F  


### TDB models of TBB12_D2F (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): TBB12_D2F, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
60: PHASE TBB12_D2F % 2 1 12 !
61: CONST TBB12_D2F : TB : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## TBB2_C32 (B–Tb)

- Id: `phase:b-tb:tbb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.6667, Tb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2373.37 K, x(B) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:tbb2-c32)

Names (2): _corpus: _corpus:phase:b-tb:tbb2-c32  
_tdb: _tdb:TbB-22Wei.tdb:TBB2_C32  


### TDB models of TBB2_C32 (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): TBB2_C32, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
45: PHASE TBB2_C32 % 2 1 2 !
46: CONST TBB2_C32 : TB : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## TBB4_D1E (B–Tb)

- Id: `phase:b-tb:tbb4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgiov and oqmd-12246, space group 127
- Stoichiometry: B 0.8000, Tb 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2872.59 K, x(B) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:tbb4-d1e)

Names (4): _corpus: _corpus:phase:b-tb:tbb4-d1e  
_mp: _mp:mp-aaabgiov  
_oqmd: _oqmd:oqmd-12246  
_tdb: _tdb:TbB-22Wei.tdb:TBB4_D1E  


### TDB models of TBB4_D1E (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): TBB4_D1E, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
50: PHASE TBB4_D1E % 2 1 4 !
51: CONST TBB4_D1E : TB : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## TBB6_D21 (B–Tb)

- Id: `phase:b-tb:tbb6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.8571, Tb 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–2613.15 K, x(B) 0.85714–0.85714
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:tbb6-d21)

Names (2): _corpus: _corpus:phase:b-tb:tbb6-d21  
_tdb: _tdb:TbB-22Wei.tdb:TBB6_D21  


### TDB models of TBB6_D21 (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): TBB6_D21, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
55: PHASE TBB6_D21 % 2 1 6 !
56: CONST TBB6_D21 : TB : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## TBB66 (B–Tb)

- Id: `phase:b-tb:tbb66`; status `assigned`
- Structure: YB66 · cF1936 · Fm-3c (226); type `st:yb66-cf1936`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.9851, Tb 0.0149
- Stability: stable in 1 of 1 calculated diagram(s): 1029.19–2374.12 K, x(B) 0.98507–0.98507
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-tb:tbb66)

Names (2): _corpus: _corpus:phase:b-tb:tbb66  
_tdb: _tdb:TbB-22Wei.tdb:TBB66  


### TDB models of TBB66 (1): PHASE and CONSTITUENT statements as written

[TbB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/TbB-22Wei.tdb): TBB66, type code %, sha256 `21c9d9c830b1c061…`

~~~~text
65: PHASE TBB66 % 2 1 66 !
66: CONST TBB66 : TB : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
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
