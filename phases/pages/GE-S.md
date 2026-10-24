# Ge–S phases

> Ge–S system: 10 phases (tier A 6, liquid 1, needs_review 3); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-S.html · Markdown: https://data.orchid-project.org/phases/pages/GE-S.md

10 phases (tier A 6, liquid 1, needs_review 3); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-S) · [full JSON](https://data.orchid-project.org/phases/systems/GE-S.json) · [Ge–S system page](https://data.orchid-project.org/systems/GE-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–S system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-ge-s-a16-orthorhombic); _phase:ge-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–368.3 K, x(S) 1–1 | 0 | 1 |
| [DIAMOND_A4](#phase-ge-s-a4-diamond); _phase:ge-s:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(S) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ge-s-bcc-a2); _phase:ge-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ge-s-fcc-a1); _phase:ge-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GES_B16](#phase-ge-s-ges-b16); _phase:ge-s:ges-b16_ | GeS · B16 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–863.49 K, x(S) 0.5–0.5 | 0 | 1 |
| [GES_BETA](#phase-ge-s-ges-beta); _phase:ge-s:ges-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 863.49–950.37 K, x(S) 0.5–0.5 | 0 | 1 |
| [GES2](#phase-ge-s-ges2); _phase:ge-s:ges2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1109.08 K, x(S) 0.66667–0.66667 | 13 | 1 |
| [HCP_A3](#phase-ge-s-hcp-a3); _phase:ge-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ge-s-liquid); _phase:ge-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.08–2500 K, x(S) 0–1 | 0 | 1 |
| [MONOCLINIC_S](#phase-ge-s-s-monoclinic); _phase:ge-s:s-monoclinic_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 368.3–391.08 K, x(S) 1–1 | 0 | 1 |

## ORTHORHOMBIC_A16 (Ge–S)

- Id: `phase:ge-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–368.3 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:ge-s:a16-orthorhombic  
_tdb: _tdb:GeS-22Che.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): ORTHORHOMBIC_A16, type code %, sha256 `785db495efac14d1…`

~~~~text
51: PHASE ORTHORHOMBIC_A16 % 1 1 !
52: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## DIAMOND_A4 (Ge–S)

- Id: `phase:ge-s:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:a4-diamond)

Names (2): _corpus: _corpus:phase:ge-s:a4-diamond  
_tdb: _tdb:GeS-22Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): DIAMOND_A4, type code %, sha256 `785db495efac14d1…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## BCC_A2 (Ge–S)

- Id: `phase:ge-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-s:bcc-a2  
_tdb: _tdb:GeS-22Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): BCC_A2, type code %B, sha256 `785db495efac14d1…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : GE S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## FCC_A1 (Ge–S)

- Id: `phase:ge-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-s:fcc-a1  
_tdb: _tdb:GeS-22Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): FCC_A1, type code %A, sha256 `785db495efac14d1…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : GE S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GES_B16 (Ge–S)

- Id: `phase:ge-s:ges-b16`; status `assigned`
- Structure: GeS · B16 · oP8 · Pnma (62); type `st:b16-ges-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 0.5000, S 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–863.49 K, x(S) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:ges-b16)

Names (2): _corpus: _corpus:phase:ge-s:ges-b16  
_tdb: _tdb:GeS-22Che.tdb:GES_B16  


### TDB models of GES_B16 (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): GES_B16, type code %, sha256 `785db495efac14d1…`

~~~~text
61: PHASE GES_B16 % 2 1 1 !
62: CONST GES_B16 : GE : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GES_BETA (Ge–S)

- Id: `phase:ge-s:ges-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Pnma (62) — on-hull MP GeS at x(S)=0.5000
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Ge1 S1 at x(S)=0.5000
- Candidate (sgte_mmc2): (GeS) — Hallstedt 2025 mmc2 row for GES_BETA: GeS (high-T)
- Stoichiometry: Ge 0.5000, S 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 863.49–950.37 K, x(S) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:ges-beta)

Names (2): _corpus: _corpus:phase:ge-s:ges-beta  
_tdb: _tdb:GeS-22Che.tdb:GES_BETA  


### TDB models of GES_BETA (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): GES_BETA, type code %, sha256 `785db495efac14d1…`

~~~~text
66: PHASE GES_BETA % 2 1 1 !
67: CONST GES_BETA : GE : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## GES2 (Ge–S)

- Id: `phase:ge-s:ges2`; status `needs_review`
- No structure assigned. Why: dft_space_group_14_matches_0_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P2_1/c (14) — on-hull MP GeS2 at x(S)=0.6667
- Candidate (dft_oqmd): P21/c (14) — on-hull OQMD Ge1 S2 at x(S)=0.6667
- Candidate (sgte_mmc2): GeS2-alpha · mP36 · Pc (7) — Hallstedt 2025 mmc2 row for GES2: GeS2 (low-T)
- Candidate (sgte_mmc2): GeS2-beta · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for GES2: GeS2 (high-T)
- Candidate (tdb_comment): GeS2 · mP36 · Pc — GeS-22Che.tdb: 'Prototype GeS2 (mP36, Pc) alpha'
- Candidate (tdb_comment): GeS2 · mP48 · P2_1/c — GeS-22Che.tdb: 'Prototype GeS2 (mP48, P2_1/c) beta'
- Stoichiometry: Ge 0.3333, S 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1109.08 K, x(S) 0.66667–0.66667
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:ges2)

Names (3): _corpus: _corpus:phase:ge-s:ges2  
_paper: _paper:10.1007/s11664-022-09474-1:GeS2  
_tdb: _tdb:GeS-22Che.tdb:GES2  


### TDB models of GES2 (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): GES2, type code %, sha256 `785db495efac14d1…`

~~~~text
72: PHASE GES2 % 2 1 2 !
73: CONST GES2 : GE : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1107/s0567740875006851](https://doi.org/10.1107/s0567740875006851) G. Dittmar, H. Schäfer, Die Kristallstruktur von H.T.-GeS\<sub>2\</sub>, Acta Crystallogr B Struct Sci 31, 2060-2064 (1975).  
_cited as the source of values for this phase_

## HCP_A3 (Ge–S)

- Id: `phase:ge-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-s:hcp-a3  
_tdb: _tdb:GeS-22Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): HCP_A3, type code %A, sha256 `785db495efac14d1…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## LIQUID (Ge–S)

- Id: `phase:ge-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.08–2500 K, x(S) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:liquid)

Names (2): _corpus: _corpus:phase:ge-s:liquid  
_tdb: _tdb:GeS-22Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): LIQUID, type code %, sha256 `785db495efac14d1…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : GE GES2 S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_

## MONOCLINIC_S (Ge–S)

- Id: `phase:ge-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — GeS-22Che.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 368.3–391.08 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-s:s-monoclinic)

Names (2): _corpus: _corpus:phase:ge-s:s-monoclinic  
_tdb: _tdb:GeS-22Che.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[GeS-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb): MONOCLINIC_S, type code %, sha256 `785db495efac14d1…`

~~~~text
56: PHASE MONOCLINIC_S % 1 1 !
57: CONST MONOCLINIC_S : S : !
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
