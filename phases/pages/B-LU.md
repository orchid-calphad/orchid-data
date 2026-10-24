# B–Lu phases

> B–Lu system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-LU.html · Markdown: https://data.orchid-project.org/phases/pages/B-LU.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-LU) · [full JSON](https://data.orchid-project.org/phases/systems/B-LU.json) · [B–Lu system page](https://data.orchid-project.org/systems/B-LU.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-LU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Lu system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-lu-b-alpha-rhombo); _phase:b-lu:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-lu-b-beta-rhombo); _phase:b-lu:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2350.67 K, x(B) 1–1 | 2 | 1 |
| [BCC_A2](#phase-b-lu-bcc-a2); _phase:b-lu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-b-lu-fcc-a1); _phase:b-lu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-lu-hcp-a3); _phase:b-lu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.75 K, x(B) 0–0.00087 | 2 | 1 |
| [LIQUID](#phase-b-lu-liquid); _phase:b-lu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1767.35–4000 K, x(B) 0–1 | 12 | 1 |
| [LUB12_D2F](#phase-b-lu-lub12-d2f); _phase:b-lu:lub12-d2f_ | UB12 · D2_f · cF52 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2449.26 K, x(B) 0.92308–0.92308 | 4 | 1 |
| [LUB2_C32](#phase-b-lu-lub2-c32); _phase:b-lu:lub2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2524.98 K, x(B) 0.66667–0.66667 | 4 | 1 |
| [LUB4_D1E](#phase-b-lu-lub4-d1e); _phase:b-lu:lub4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2873.35 K, x(B) 0.8–0.8 | 6 | 1 |
| [LUB66](#phase-b-lu-lub66); _phase:b-lu:lub66_ | YB66 · cF1936 · Fm-3c (226) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2380.33 K, x(B) 0.98507–0.98507 | 5 | 1 |

## ALPHA_RHOMBO_B (B–Lu)

- Id: `phase:b-lu:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — LuB-20Li.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-lu:b-alpha-rhombo  
_tdb: _tdb:LuB-20Li.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): ALPHA_RHOMBO_B, type code %, sha256 `209af1f02647e3d6…`

~~~~text
40: PHASE ALPHA_RHOMBO_B % 1 1 !
41: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Lu)

- Id: `phase:b-lu:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — LuB-20Li.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2350.67 K, x(B) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:b-beta-rhombo)

Names (4): _corpus: _corpus:phase:b-lu:b-beta-rhombo, corpus:phase:b-lu:beta-rhombo-b  
_paper: _paper:10.1016/j.calphad.2020.101740:β-B  
_tdb: _tdb:LuB-20Li.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): BETA_RHOMBO_B, type code %, sha256 `209af1f02647e3d6…`

~~~~text
45: PHASE BETA_RHOMBO_B % 1 1 !
46: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (B–Lu)

- Id: `phase:b-lu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: B 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:bcc-a2)

Names (2): _corpus: _corpus:phase:b-lu:bcc-a2  
_tdb: _tdb:LuB-20Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): BCC_A2, type code %B, sha256 `209af1f02647e3d6…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : B : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_

## FCC_A1 (B–Lu)

- Id: `phase:b-lu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: B 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:fcc-a1)

Names (2): _corpus: _corpus:phase:b-lu:fcc-a1  
_tdb: _tdb:LuB-20Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): FCC_A1, type code %A, sha256 `209af1f02647e3d6…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : B : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_

## HCP_A3 (B–Lu)

- Id: `phase:b-lu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.75 K, x(B) 0–0.00087
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:hcp-a3)

Names (3): _corpus: _corpus:phase:b-lu:hcp-a3  
_paper: _paper:10.1016/j.calphad.2020.101740:α-Lu  
_tdb: _tdb:LuB-20Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): HCP_A3, type code %A, sha256 `209af1f02647e3d6…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : B LU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## LIQUID (B–Lu)

- Id: `phase:b-lu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1767.35–4000 K, x(B) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:liquid)

Names (3): _corpus: _corpus:phase:b-lu:liquid  
_paper: _paper:10.1016/j.calphad.2020.101740:L  
_tdb: _tdb:LuB-20Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): LIQUID, type code %, sha256 `209af1f02647e3d6…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : B LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## LUB12_D2F (B–Lu)

- Id: `phase:b-lu:lub12-d2f`; status `assigned`
- Structure: UB12 · D2_f · cF52 · Fm-3m (225); type `st:d2-f-ub12-cf52`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackvor and oqmd-28503, space group 225
- Stoichiometry: B 0.9231, Lu 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–2449.26 K, x(B) 0.92308–0.92308
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:lub12-d2f)

Names (5): _corpus: _corpus:phase:b-lu:lub12-d2f  
_mp: _mp:mp-aaackvor  
_oqmd: _oqmd:oqmd-28503  
_paper: _paper:10.1016/j.calphad.2020.101740:LuB12  
_tdb: _tdb:LuB-20Li.tdb:LUB12_D2F  


### TDB models of LUB12_D2F (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): LUB12_D2F, type code %, sha256 `209af1f02647e3d6…`

~~~~text
60: PHASE LUB12_D2F % 2 1 12 !
61: CONST LUB12_D2F : LU : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## LUB2_C32 (B–Lu)

- Id: `phase:b-lu:lub2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqpn and oqmd-115218, space group 191
- Stoichiometry: B 0.6667, Lu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2524.98 K, x(B) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:lub2-c32)

Names (5): _corpus: _corpus:phase:b-lu:lub2-c32  
_mp: _mp:mp-aaaaaqpn  
_oqmd: _oqmd:oqmd-115218  
_paper: _paper:10.1016/j.calphad.2020.101740:LuB2  
_tdb: _tdb:LuB-20Li.tdb:LUB2_C32  


### TDB models of LUB2_C32 (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): LUB2_C32, type code %, sha256 `209af1f02647e3d6…`

~~~~text
50: PHASE LUB2_C32 % 2 1 2 !
51: CONST LUB2_C32 : LU : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## LUB4_D1E (B–Lu)

- Id: `phase:b-lu:lub4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgnkp and oqmd-19137, space group 127
- Stoichiometry: B 0.8000, Lu 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2873.35 K, x(B) 0.8–0.8
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:lub4-d1e)

Names (5): _corpus: _corpus:phase:b-lu:lub4-d1e  
_mp: _mp:mp-aaabgnkp  
_oqmd: _oqmd:oqmd-19137  
_paper: _paper:10.1016/j.calphad.2020.101740:LuB4  
_tdb: _tdb:LuB-20Li.tdb:LUB4_D1E  


### TDB models of LUB4_D1E (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): LUB4_D1E, type code %, sha256 `209af1f02647e3d6…`

~~~~text
55: PHASE LUB4_D1E % 2 1 4 !
56: CONST LUB4_D1E : LU : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

## LUB66 (B–Lu)

- Id: `phase:b-lu:lub66`; status `assigned`
- Structure: YB66 · cF1936 · Fm-3c (226); type `st:yb66-cf1936`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.9851, Lu 0.0149
- Stability: stable in 1 of 1 calculated diagram(s): 300–2380.33 K, x(B) 0.98507–0.98507
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-lu:lub66)

Names (3): _corpus: _corpus:phase:b-lu:lub66  
_paper: _paper:10.1016/j.calphad.2020.101740:LuB66  
_tdb: _tdb:LuB-20Li.tdb:LUB66  


### TDB models of LUB66 (1): PHASE and CONSTITUENT statements as written

[LuB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LuB-20Li.tdb): LUB66, type code %, sha256 `209af1f02647e3d6…`

~~~~text
65: PHASE LUB66 % 2 1 66 !
66: CONST LUB66 : LU : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_

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
