# Cu–Th phases

> Cu–Th system: 8 phases (tier A 5, tier B 1, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-TH.html · Markdown: https://data.orchid-project.org/phases/pages/CU-TH.md

8 phases (tier A 5, tier B 1, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-TH) · [full JSON](https://data.orchid-project.org/phases/systems/CU-TH.json) · [Cu–Th system page](https://data.orchid-project.org/systems/CU-TH.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-TH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Th system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-th-bcc-a2); _phase:cu-th:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1633.42–3999.24 K, x(Th) 0.99871–1 | 0 | 1 |
| [CU18TH5](#phase-cu-th-cu18th5); _phase:cu-th:cu18th5_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1325 K, x(Th) 0.21739–0.21739 | 6 | 1 |
| [CU2TH_C32](#phase-cu-th-cu2th-c32); _phase:cu-th:cu2th-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1287.39 K, x(Th) 0.33333–0.33333 | 6 | 1 |
| [CU6TH](#phase-cu-th-cu6th); _phase:cu-th:cu6th_ | CeCu6 · oP28 · Pnma (62) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 967.14–1328.51 K, x(Th) 0.14286–0.14286 | 6 | 1 |
| [CUTH2_C16](#phase-cu-th-cuth2-c16); _phase:cu-th:cuth2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1277.37 K, x(Th) 0.66667–0.66667 | 6 | 1 |
| [FCC_A1](#phase-cu-th-fcc-a1); _phase:cu-th:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1633.42 K, x(Th) 0–1 | 4 | 1 |
| [HCP_A3](#phase-cu-th-hcp-a3); _phase:cu-th:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cu-th-liquid); _phase:cu-th:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1157.84–4000 K, x(Th) 0–1 | 18 | 1 |

## BCC_A2 (Cu–Th)

- Id: `phase:cu-th:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1633.42–3999.24 K, x(Th) 0.99871–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:bcc-a2)

Names (2): _corpus: _corpus:phase:cu-th:bcc-a2  
_tdb: _tdb:CuTh-08Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): BCC_A2, type code %B, sha256 `8ae901d23dd6c3e4…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CU TH% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase_

## CU18TH5 (Cu–Th)

- Id: `phase:cu-th:cu18th5`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (literature_printed): Ag51Gd14 · hP68 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ag51Gd14 · hP68 · P6/m (175) — Hallstedt 2025 mmc2 row for CU18TH5: Cu51Th14
- Candidate (tdb_comment): Ag51Gd14 · hP68 · P6/m — CuTh-08Wan.tdb: 'Prototype Ag51Gd14 (hP68, P6/m)'
- Stoichiometry: Cu 0.7826, Th 0.2174
- Stability: stable in 1 of 1 calculated diagram(s): 300–1325 K, x(Th) 0.21739–0.21739
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:cu18th5)

Names (3): _corpus: _corpus:phase:cu-th:cu18th5  
_paper: _paper:10.1016/j.jallcom.2007.04.017:Cu3.6Th  
_tdb: _tdb:CuTh-08Wan.tdb:CU18TH5  


### TDB models of CU18TH5 (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): CU18TH5, type code %, sha256 `8ae901d23dd6c3e4…`

~~~~text
49: PHASE CU18TH5 % 2 18 5 !
50: CONST CU18TH5 : CU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90128-7](https://doi.org/10.1016/0022-5088%2871%2990128-7) R.J. Schiltz, E.R. Stevens, O.N. Carlson, The thorium-copper system, Journal of the Less Common Metals 25, 175-185 (1971).  
_cited as the source of values for this phase_

## CU2TH_C32 (Cu–Th)

- Id: `phase:cu-th:cu2th-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacaz and oqmd-88945, space group 191
- Stoichiometry: Cu 0.6667, Th 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1287.39 K, x(Th) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:cu2th-c32)

Names (5): _corpus: _corpus:phase:cu-th:cu2th-c32  
_mp: _mp:mp-aaaaacaz  
_oqmd: _oqmd:oqmd-88945  
_paper: _paper:10.1016/j.jallcom.2007.04.017:Cu2Th  
_tdb: _tdb:CuTh-08Wan.tdb:CU2TH_C32  


### TDB models of CU2TH_C32 (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): CU2TH_C32, type code %, sha256 `8ae901d23dd6c3e4…`

~~~~text
54: PHASE CU2TH_C32 % 2 2 1 !
55: CONST CU2TH_C32 : CU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90128-7](https://doi.org/10.1016/0022-5088%2871%2990128-7) R.J. Schiltz, E.R. Stevens, O.N. Carlson, The thorium-copper system, Journal of the Less Common Metals 25, 175-185 (1971).  
_cited as the source of values for this phase_

## CU6TH (Cu–Th)

- Id: `phase:cu-th:cu6th`; status `assigned`
- Structure: CeCu6 · oP28 · Pnma (62); type `st:cecu6-op28`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cu 0.8571, Th 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 967.14–1328.51 K, x(Th) 0.14286–0.14286
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:cu6th)

Names (5): _corpus: _corpus:phase:cu-th:cu6th  
_mp: _mp:mp-aaaaaszq  
_oqmd: _oqmd:oqmd-19585  
_paper: _paper:10.1016/j.jallcom.2007.04.017:Cu6Th  
_tdb: _tdb:CuTh-08Wan.tdb:CU6TH  


### TDB models of CU6TH (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): CU6TH, type code %, sha256 `8ae901d23dd6c3e4…`

~~~~text
44: PHASE CU6TH % 2 6 1 !
45: CONST CU6TH : CU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90128-7](https://doi.org/10.1016/0022-5088%2871%2990128-7) R.J. Schiltz, E.R. Stevens, O.N. Carlson, The thorium-copper system, Journal of the Less Common Metals 25, 175-185 (1971).  
_cited as the source of values for this phase_

## CUTH2_C16 (Cu–Th)

- Id: `phase:cu-th:cuth2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.3333, Th 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1277.37 K, x(Th) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:cuth2-c16)

Names (3): _corpus: _corpus:phase:cu-th:cuth2-c16  
_paper: _paper:10.1016/j.jallcom.2007.04.017:CuTh2  
_tdb: _tdb:CuTh-08Wan.tdb:CUTH2_C16  


### TDB models of CUTH2_C16 (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): CUTH2_C16, type code %, sha256 `8ae901d23dd6c3e4…`

~~~~text
59: PHASE CUTH2_C16 % 2 1 2 !
60: CONST CUTH2_C16 : CU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90128-7](https://doi.org/10.1016/0022-5088%2871%2990128-7) R.J. Schiltz, E.R. Stevens, O.N. Carlson, The thorium-copper system, Journal of the Less Common Metals 25, 175-185 (1971).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Th)

- Id: `phase:cu-th:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1633.42 K, x(Th) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-th:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.04.017:(Cu), paper:10.1016/j.jallcom.2007.04.017:(αTh)  
_tdb: _tdb:CuTh-08Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): FCC_A1, type code %A, sha256 `8ae901d23dd6c3e4…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CU% TH% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90128-7](https://doi.org/10.1016/0022-5088%2871%2990128-7) R.J. Schiltz, E.R. Stevens, O.N. Carlson, The thorium-copper system, Journal of the Less Common Metals 25, 175-185 (1971).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Th)

- Id: `phase:cu-th:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-th:hcp-a3  
_tdb: _tdb:CuTh-08Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): HCP_A3, type code %A, sha256 `8ae901d23dd6c3e4…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase_

## LIQUID (Cu–Th)

- Id: `phase:cu-th:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1157.84–4000 K, x(Th) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-th:liquid)

Names (3): _corpus: _corpus:phase:cu-th:liquid  
_paper: _paper:10.1016/j.jallcom.2007.04.017:L  
_tdb: _tdb:CuTh-08Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTh-08Wan.tdb): LIQUID, type code %, sha256 `8ae901d23dd6c3e4…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CU TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90128-7](https://doi.org/10.1016/0022-5088%2871%2990128-7) R.J. Schiltz, E.R. Stevens, O.N. Carlson, The thorium-copper system, Journal of the Less Common Metals 25, 175-185 (1971).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
