# B–Ho phases

> B–Ho system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-HO.html · Markdown: https://data.orchid-project.org/phases/pages/B-HO.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-HO) · [full JSON](https://data.orchid-project.org/phases/systems/B-HO.json) · [Markdown](https://data.orchid-project.org/phases/pages/B-HO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Ho system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-ho-b-alpha-rhombo); _phase:b-ho:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-ho-b-beta-rhombo); _phase:b-ho:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2353.29 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-ho-bcc-a2); _phase:b-ho:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-ho-hcp-a3); _phase:b-ho:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1754 K, x(B) 0–0 | 0 | 1 |
| [HOB12_D2F](#phase-b-ho-hob12-d2f); _phase:b-ho:hob12-d2f_ | UB12 · D2_f · cF52 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2372.51 K, x(B) 0.92308–0.92308 | 0 | 1 |
| [HOB2_C32](#phase-b-ho-hob2-c32); _phase:b-ho:hob2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2476.14 K, x(B) 0.66667–0.66667 | 0 | 1 |
| [HOB4_D1E](#phase-b-ho-hob4-d1e); _phase:b-ho:hob4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2773.52 K, x(B) 0.8–0.8 | 0 | 1 |
| [HOB6_D21](#phase-b-ho-hob6-d21); _phase:b-ho:hob6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2453.4 K, x(B) 0.85714–0.85714 | 0 | 1 |
| [HOB66](#phase-b-ho-hob66); _phase:b-ho:hob66_ | YB66 · cF1936 · Fm-3c (226) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2339.45 K, x(B) 0.98507–0.98507 | 0 | 1 |
| [LIQUID](#phase-b-ho-liquid); _phase:b-ho:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1717.07–4000 K, x(B) 0–1 | 0 | 1 |

## ALPHA_RHOMBO_B (B–Ho)

- Id: `phase:b-ho:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — HoB-20Wei.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-ho:b-alpha-rhombo  
_tdb: _tdb:HoB-20Wei.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): ALPHA_RHOMBO_B, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
38: PHASE ALPHA_RHOMBO_B % 1 1 !
39: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Ho)

- Id: `phase:b-ho:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — HoB-20Wei.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2353.29 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-ho:b-beta-rhombo  
_tdb: _tdb:HoB-20Wei.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): BETA_RHOMBO_B, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
43: PHASE BETA_RHOMBO_B % 1 1 !
44: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## BCC_A2 (B–Ho)

- Id: `phase:b-ho:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ho 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:bcc-a2)

Names (2): _corpus: _corpus:phase:b-ho:bcc-a2  
_tdb: _tdb:HoB-20Wei.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): BCC_A2, type code %B, sha256 `2e0ce826e6e1fe99…`

~~~~text
28: PHASE BCC_A2 %B 2 1 3 !
29: CONST BCC_A2 : HO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## HCP_A3 (B–Ho)

- Id: `phase:b-ho:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ho 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1754 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:hcp-a3)

Names (2): _corpus: _corpus:phase:b-ho:hcp-a3  
_tdb: _tdb:HoB-20Wei.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): HCP_A3, type code %A, sha256 `2e0ce826e6e1fe99…`

~~~~text
33: PHASE HCP_A3 %A 2 1 0.5 !
34: CONST HCP_A3 : HO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## HOB12_D2F (B–Ho)

- Id: `phase:b-ho:hob12-d2f`; status `assigned`
- Structure: UB12 · D2_f · cF52 · Fm-3m (225); type `st:d2-f-ub12-cf52`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackwab and oqmd-28455, space group 225
- Stoichiometry: B 0.9231, Ho 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–2372.51 K, x(B) 0.92308–0.92308
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:hob12-d2f)

Names (4): _corpus: _corpus:phase:b-ho:hob12-d2f  
_mp: _mp:mp-aaackwab  
_oqmd: _oqmd:oqmd-28455  
_tdb: _tdb:HoB-20Wei.tdb:HOB12_D2F  


### TDB models of HOB12_D2F (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): HOB12_D2F, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
63: PHASE HOB12_D2F % 2 1 12 !
64: CONST HOB12_D2F : HO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## HOB2_C32 (B–Ho)

- Id: `phase:b-ho:hob2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadjf and oqmd-8366, space group 191
- Stoichiometry: B 0.6667, Ho 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2476.14 K, x(B) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:hob2-c32)

Names (4): _corpus: _corpus:phase:b-ho:hob2-c32  
_mp: _mp:mp-aaaaadjf  
_oqmd: _oqmd:oqmd-8366  
_tdb: _tdb:HoB-20Wei.tdb:HOB2_C32  


### TDB models of HOB2_C32 (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): HOB2_C32, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
48: PHASE HOB2_C32 % 2 1 2 !
49: CONST HOB2_C32 : HO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## HOB4_D1E (B–Ho)

- Id: `phase:b-ho:hob4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.8000, Ho 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2773.52 K, x(B) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:hob4-d1e)

Names (2): _corpus: _corpus:phase:b-ho:hob4-d1e  
_tdb: _tdb:HoB-20Wei.tdb:HOB4_D1E  


### TDB models of HOB4_D1E (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): HOB4_D1E, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
53: PHASE HOB4_D1E % 2 1 4 !
54: CONST HOB4_D1E : HO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## HOB6_D21 (B–Ho)

- Id: `phase:b-ho:hob6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.8571, Ho 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–2453.4 K, x(B) 0.85714–0.85714
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:hob6-d21)

Names (2): _corpus: _corpus:phase:b-ho:hob6-d21  
_tdb: _tdb:HoB-20Wei.tdb:HOB6_D21  


### TDB models of HOB6_D21 (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): HOB6_D21, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
58: PHASE HOB6_D21 % 2 1 6 !
59: CONST HOB6_D21 : HO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## HOB66 (B–Ho)

- Id: `phase:b-ho:hob66`; status `assigned`
- Structure: YB66 · cF1936 · Fm-3c (226); type `st:yb66-cf1936`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.9851, Ho 0.0149
- Stability: stable in 1 of 1 calculated diagram(s): 300–2339.45 K, x(B) 0.98507–0.98507
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:hob66)

Names (2): _corpus: _corpus:phase:b-ho:hob66  
_tdb: _tdb:HoB-20Wei.tdb:HOB66  


### TDB models of HOB66 (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): HOB66, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
68: PHASE HOB66 % 2 1 66 !
69: CONST HOB66 : HO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

## LIQUID (B–Ho)

- Id: `phase:b-ho:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1717.07–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ho:liquid)

Names (2): _corpus: _corpus:phase:b-ho:liquid  
_tdb: _tdb:HoB-20Wei.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HoB-20Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/HoB-20Wei.tdb): LIQUID, type code %, sha256 `2e0ce826e6e1fe99…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : B HO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101796](https://doi.org/10.1016/j.calphad.2020.101796) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 70, 101796(2020).  
_assessment that models this phase_

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
