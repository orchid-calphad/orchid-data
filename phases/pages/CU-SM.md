# Cu–Sm phases

> Cu–Sm system: 10 phases (tier A 5, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-SM.html · Markdown: https://data.orchid-project.org/phases/pages/CU-SM.md

10 phases (tier A 5, tier C 2, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-SM) · [full JSON](https://data.orchid-project.org/phases/systems/CU-SM.json) · [Cu–Sm system page](https://data.orchid-project.org/systems/CU-SM.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-SM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Sm system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-sm-bcc-a2); _phase:cu-sm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1190.48–2500 K, x(Sm) 0.99877–1 | 1 | 1 |
| [CU2SM](#phase-cu-sm-cu2sm); _phase:cu-sm:cu2sm_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1128.27 K, x(Sm) 0.33333–0.33333 | 3 | 1 |
| [CU4SM](#phase-cu-sm-cu4sm); _phase:cu-sm:cu4sm_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1151.17 K, x(Sm) 0.2–0.2 | 2 | 1 |
| [CU5SM_D2D](#phase-cu-sm-cu5sm-d2d); _phase:cu-sm:cu5sm-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1198.43 K, x(Sm) 0.16667–0.16667 | 2 | 1 |
| [CU6SM](#phase-cu-sm-cu6sm); _phase:cu-sm:cu6sm_ | CeCu6 · oP28 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1240.16 K, x(Sm) 0.14286–0.14286 | 3 | 1 |
| [CUSM](#phase-cu-sm-cusm); _phase:cu-sm:cusm_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1057.83 K, x(Sm) 0.5–0.5 | 3 | 1 |
| [FCC_A1](#phase-cu-sm-fcc-a1); _phase:cu-sm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1366.17 K, x(Sm) 0–0 | 1 | 1 |
| [HCP_A3](#phase-cu-sm-hcp-a3); _phase:cu-sm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 999.28–1335.48 K, x(Sm) 0.99992–1 | 0 | 1 |
| [LIQUID](#phase-cu-sm-liquid); _phase:cu-sm:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 827.58–2500 K, x(Sm) 0–1 | 10 | 1 |
| [RHOMB_C19](#phase-cu-sm-rhomb-c19); _phase:cu-sm:rhomb-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1194.28 K, x(Sm) 1–1 | 1 | 1 |

## BCC_A2 (Cu–Sm)

- Id: `phase:cu-sm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1190.48–2500 K, x(Sm) 0.99877–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-sm:bcc-a2  
_paper: _paper:10.1007/bf02665998:Sm(bcc)  
_tdb: _tdb:CuSm-96Zhu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): BCC_A2, type code %B, sha256 `c172df98a0ac4787…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CU SM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CU2SM (Cu–Sm)

- Id: `phase:cu-sm:cu2sm`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Sm 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1128.27 K, x(Sm) 0.33333–0.33333
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:cu2sm)

Names (3): _corpus: _corpus:phase:cu-sm:cu2sm  
_paper: _paper:10.1007/bf02665998:Cu2Sm  
_tdb: _tdb:CuSm-96Zhu.tdb:CU2SM  


### TDB models of CU2SM (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): CU2SM, type code %, sha256 `c172df98a0ac4787…`

~~~~text
68: PHASE CU2SM % 2 2 1 !
69: CONST CU2SM : CU : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CU4SM (Cu–Sm)

- Id: `phase:cu-sm:cu4sm`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu4Sm) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu4Sm) — Hallstedt 2025 mmc2 row for CU4SM: Cu4Sm
- Stoichiometry: Cu 0.8000, Sm 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1151.17 K, x(Sm) 0.2–0.2
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:cu4sm)

Names (3): _corpus: _corpus:phase:cu-sm:cu4sm  
_paper: _paper:10.1007/bf02665998:Cu4Sm  
_tdb: _tdb:CuSm-96Zhu.tdb:CU4SM  


### TDB models of CU4SM (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): CU4SM, type code %, sha256 `c172df98a0ac4787…`

~~~~text
63: PHASE CU4SM % 2 4 1 !
64: CONST CU4SM : CU : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CU5SM_D2D (Cu–Sm)

- Id: `phase:cu-sm:cu5sm-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaait and oqmd-31281, space group 191
- Stoichiometry: Cu 0.8333, Sm 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1198.43 K, x(Sm) 0.16667–0.16667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:cu5sm-d2d)

Names (5): _corpus: _corpus:phase:cu-sm:cu5sm-d2d  
_mp: _mp:mp-aaaaaait  
_oqmd: _oqmd:oqmd-31281  
_paper: _paper:10.1007/bf02665998:Cu5Sm  
_tdb: _tdb:CuSm-96Zhu.tdb:CU5SM_D2D  


### TDB models of CU5SM_D2D (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): CU5SM_D2D, type code %, sha256 `c172df98a0ac4787…`

~~~~text
58: PHASE CU5SM_D2D % 2 5 1 !
59: CONST CU5SM_D2D : CU : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CU6SM (Cu–Sm)

- Id: `phase:cu-sm:cu6sm`; status `assigned`
- Structure: CeCu6 · oP28 · Pnma (62); type `st:cecu6-op28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.8571, Sm 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–1240.16 K, x(Sm) 0.14286–0.14286
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:cu6sm)

Names (3): _corpus: _corpus:phase:cu-sm:cu6sm  
_paper: _paper:10.1007/bf02665998:Cu6Sm  
_tdb: _tdb:CuSm-96Zhu.tdb:CU6SM  


### TDB models of CU6SM (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): CU6SM, type code %, sha256 `c172df98a0ac4787…`

~~~~text
53: PHASE CU6SM % 2 6 1 !
54: CONST CU6SM : CU : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CUSM (Cu–Sm)

- Id: `phase:cu-sm:cusm`; status `needs_review`
- No structure assigned. Why: dft_space_group_62_matches_5_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Pnma (62) — on-hull MP SmCu at x(SM)=0.5000
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Cu1 Sm1 at x(SM)=0.5000
- Candidate (dft_space_group_and_stoichiometry): GeS · B16 · oP8 · Pnma (62) — space group 62 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): FeB · B27 · oP8 · Pnma (62) — space group 62 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): SnS · B29 · oP8 · Pnma (62) — space group 62 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): MnP · B31 · oP8 · Pnma (62) — space group 62 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): FeAs · oP8 · Pnma (62) — space group 62 and stoichiometry match
- Candidate (literature_printed): CsCl · cP2 — printed with a label mapped to this phase
- Stoichiometry: Cu 0.5000, Sm 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1057.83 K, x(Sm) 0.5–0.5
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:cusm)

Names (3): _corpus: _corpus:phase:cu-sm:cusm  
_paper: _paper:10.1007/bf02665998:CuSm  
_tdb: _tdb:CuSm-96Zhu.tdb:CUSM  


### TDB models of CUSM (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): CUSM, type code %, sha256 `c172df98a0ac4787…`

~~~~text
73: PHASE CUSM % 2 1 1 !
74: CONST CUSM : CU : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cu–Sm)

- Id: `phase:cu-sm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1366.17 K, x(Sm) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-sm:fcc-a1  
_paper: _paper:10.1007/bf02665998:Cu(fcc)  
_tdb: _tdb:CuSm-96Zhu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): FCC_A1, type code %A, sha256 `c172df98a0ac4787…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Cu–Sm)

- Id: `phase:cu-sm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 999.28–1335.48 K, x(Sm) 0.99992–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-sm:hcp-a3  
_tdb: _tdb:CuSm-96Zhu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): HCP_A3, type code %A, sha256 `c172df98a0ac4787…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CU SM : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase_

## LIQUID (Cu–Sm)

- Id: `phase:cu-sm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 827.58–2500 K, x(Sm) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:liquid)

Names (3): _corpus: _corpus:phase:cu-sm:liquid  
_paper: _paper:10.1007/bf02665998:liq  
_tdb: _tdb:CuSm-96Zhu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): LIQUID, type code %, sha256 `c172df98a0ac4787…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CU SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## RHOMB_C19 (Cu–Sm)

- Id: `phase:cu-sm:rhomb-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stoichiometry: Sm 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1194.28 K, x(Sm) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sm:rhomb-c19)

Names (3): _corpus: _corpus:phase:cu-sm:rhomb-c19  
_paper: _paper:10.1007/bf02665998:Sm(rhomb)  
_tdb: _tdb:CuSm-96Zhu.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (1): PHASE and CONSTITUENT statements as written

[CuSm-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSm-96Zhu.tdb): RHOMB_C19, type code %, sha256 `c172df98a0ac4787…`

~~~~text
48: PHASE RHOMB_C19 % 1 1 !
49: CONST RHOMB_C19 : SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

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
