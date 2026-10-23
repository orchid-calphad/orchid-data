# Cu–Pr phases

> Cu–Pr system: 11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-PR.html · Markdown: https://data.orchid-project.org/phases/pages/CU-PR.md

11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-PR) · [full JSON](https://data.orchid-project.org/phases/systems/CU-PR.json) · [Cu–Pr system page](https://data.orchid-project.org/systems/CU-PR.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-PR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Pr system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-pr-bcc-a2); _phase:cu-pr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1063.4–2298.4 K, x(Pr) 0.99845–1 | 0 | 1 |
| [CU2PR](#phase-cu-pr-cu2pr); _phase:cu-pr:cu2pr_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1104.22 K, x(Pr) 0.33333–0.33333 | 3 | 1 |
| [CU4PR](#phase-cu-pr-cu4pr); _phase:cu-pr:cu4pr_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1091.84 K, x(Pr) 0.2–0.2 | 2 | 1 |
| [CU5PR_D2D](#phase-cu-pr-cu5pr-d2d); _phase:cu-pr:cu5pr-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1107.11 K, x(Pr) 0.16667–0.16667 | 2 | 1 |
| [CU6PR](#phase-cu-pr-cu6pr); _phase:cu-pr:cu6pr_ | CeCu6 · oP28 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1218.29 K, x(Pr) 0.14286–0.14286 | 4 | 1 |
| [CUPR_B27](#phase-cu-pr-cupr-b27); _phase:cu-pr:cupr-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 2 | 1 |
| [DHCP](#phase-cu-pr-dhcp); _phase:cu-pr:dhcp_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 0 |
| [DHCP](#phase-cu-pr-dhcp-a3); _phase:cu-pr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1203 K, x(Pr) 1–1 | 2 | 1 |
| [FCC_A1](#phase-cu-pr-fcc-a1); _phase:cu-pr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1367.31 K, x(Pr) 0–0 | 1 | 1 |
| [HCP_A3](#phase-cu-pr-hcp-a3); _phase:cu-pr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cu-pr-liquid); _phase:cu-pr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 564.75–2500 K, x(Pr) 0–1 | 10 | 1 |

## BCC_A2 (Cu–Pr)

- Id: `phase:cu-pr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1063.4–2298.4 K, x(Pr) 0.99845–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:bcc-a2)

Names (2): _corpus: _corpus:phase:cu-pr:bcc-a2  
_tdb: _tdb:CuPr-96Zhu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): BCC_A2, type code %B, sha256 `80386a76c9a9fa0e…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU PR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase_

## CU2PR (Cu–Pr)

- Id: `phase:cu-pr:cu2pr`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Pr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1104.22 K, x(Pr) 0.33333–0.33333
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:cu2pr)

Names (3): _corpus: _corpus:phase:cu-pr:cu2pr  
_paper: _paper:10.1007/bf02665998:Cu2Pr  
_tdb: _tdb:CuPr-96Zhu.tdb:CU2PR  


### TDB models of CU2PR (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): CU2PR, type code %, sha256 `80386a76c9a9fa0e…`

~~~~text
65: PHASE CU2PR % 2 2 1 !
66: CONST CU2PR : CU : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CU4PR (Cu–Pr)

- Id: `phase:cu-pr:cu4pr`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu4Pr) · o\*\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu4Pr) — Hallstedt 2025 mmc2 row for CU4PR: Cu4Pr
- Stoichiometry: Cu 0.8000, Pr 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1091.84 K, x(Pr) 0.2–0.2
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:cu4pr)

Names (3): _corpus: _corpus:phase:cu-pr:cu4pr  
_paper: _paper:10.1007/bf02665998:Cu4Pr  
_tdb: _tdb:CuPr-96Zhu.tdb:CU4PR  


### TDB models of CU4PR (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): CU4PR, type code %, sha256 `80386a76c9a9fa0e…`

~~~~text
60: PHASE CU4PR % 2 4 1 !
61: CONST CU4PR : CU : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CU5PR_D2D (Cu–Pr)

- Id: `phase:cu-pr:cu5pr-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadqs and oqmd-29756, space group 191
- Stoichiometry: Cu 0.8333, Pr 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1107.11 K, x(Pr) 0.16667–0.16667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:cu5pr-d2d)

Names (5): _corpus: _corpus:phase:cu-pr:cu5pr-d2d  
_mp: _mp:mp-aaaaadqs  
_oqmd: _oqmd:oqmd-29756  
_paper: _paper:10.1007/bf02665998:Cu5Pr  
_tdb: _tdb:CuPr-96Zhu.tdb:CU5PR_D2D  


### TDB models of CU5PR_D2D (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): CU5PR_D2D, type code %, sha256 `80386a76c9a9fa0e…`

~~~~text
55: PHASE CU5PR_D2D % 2 5 1 !
56: CONST CU5PR_D2D : CU : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CU6PR (Cu–Pr)

- Id: `phase:cu-pr:cu6pr`; status `assigned`
- Structure: CeCu6 · oP28 · Pnma (62); type `st:cecu6-op28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.8571, Pr 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–1218.29 K, x(Pr) 0.14286–0.14286
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:cu6pr)

Names (3): _corpus: _corpus:phase:cu-pr:cu6pr  
_paper: _paper:10.1007/bf02665998:Cu6Pr  
_tdb: _tdb:CuPr-96Zhu.tdb:CU6PR  


### TDB models of CU6PR (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): CU6PR, type code %, sha256 `80386a76c9a9fa0e…`

~~~~text
50: PHASE CU6PR % 2 6 1 !
51: CONST CU6PR : CU : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## CUPR_B27 (Cu–Pr)

- Id: `phase:cu-pr:cupr-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacjkhn and oqmd-29755, space group 62
- Stoichiometry: Cu 0.5000, Pr 0.5000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:cupr-b27)

Names (5): _corpus: _corpus:phase:cu-pr:cupr-b27  
_mp: _mp:mp-aaacjkhn  
_oqmd: _oqmd:oqmd-29755  
_paper: _paper:10.1007/bf02665998:CuPr  
_tdb: _tdb:CuPr-96Zhu.tdb:CUPR_B27  


### TDB models of CUPR_B27 (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): CUPR_B27, type code %, sha256 `80386a76c9a9fa0e…`

~~~~text
70: PHASE CUPR_B27 % 2 1 1 !
71: CONST CUPR_B27 : CU : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## DHCP (Cu–Pr)

- Id: `phase:cu-pr:dhcp`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:dhcp)

Names (1): _corpus: _corpus:phase:cu-pr:dhcp  


## DHCP (Cu–Pr)

- Id: `phase:cu-pr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1203 K, x(Pr) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:dhcp-a3)

Names (4): _corpus: _corpus:phase:cu-pr:dhcp-a3  
_paper: _paper:10.1007/bf02665998:Pr(bcc), paper:10.1007/bf02665998:Pr(dcph)  
_tdb: _tdb:CuPr-96Zhu.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): DHCP, type code %, sha256 `80386a76c9a9fa0e…`

~~~~text
45: PHASE DHCP % 1 1 !
46: CONST DHCP : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cu–Pr)

- Id: `phase:cu-pr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1367.31 K, x(Pr) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-pr:fcc-a1  
_paper: _paper:10.1007/bf02665998:Cu(fcc)  
_tdb: _tdb:CuPr-96Zhu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): FCC_A1, type code %A, sha256 `80386a76c9a9fa0e…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Cu–Pr)

- Id: `phase:cu-pr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-pr:hcp-a3  
_tdb: _tdb:CuPr-96Zhu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): HCP_A3, type code %A, sha256 `80386a76c9a9fa0e…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
_assessment that models this phase_

## LIQUID (Cu–Pr)

- Id: `phase:cu-pr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 564.75–2500 K, x(Pr) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pr:liquid)

Names (4): _corpus: _corpus:phase:cu-pr:liquid  
_paper: _paper:10.1007/bf02665998:L, paper:10.1007/bf02665998:liquid  
_tdb: _tdb:CuPr-96Zhu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuPr-96Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPr-96Zhu.tdb): LIQUID, type code %, sha256 `80386a76c9a9fa0e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02665998](https://doi.org/10.1007/BF02665998) W. Zhuang, Z.-Y. Qiao, S. Wei, J. Shen, J. Phase Equilib., 17, 508-21(1996).  
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
