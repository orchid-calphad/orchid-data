# Cu–Tm phases

> Cu–Tm system: 9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-TM.html · Markdown: https://data.orchid-project.org/phases/pages/CU-TM.md

9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-TM) · [full JSON](https://data.orchid-project.org/phases/systems/CU-TM.json) · [Cu–Tm system page](https://data.orchid-project.org/systems/CU-TM.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-TM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Tm system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-tm-bcc-a2); _phase:cu-tm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CU2TM](#phase-cu-tm-cu2tm); _phase:cu-tm:cu2tm_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1233.33 K, x(Tm) 0.33333–0.33333 | 6 | 1 |
| [CU5TM_C15B](#phase-cu-tm-cu5tm-c15b); _phase:cu-tm:cu5tm-c15b_ | AuBe5 · C15_b · cF24 · F-43m (216) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1273.03 K, x(Tm) 0.16667–0.16667 | 5 | 1 |
| [CU7TM2](#phase-cu-tm-cu7tm2); _phase:cu-tm:cu7tm2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1193.11–1232.63 K, x(Tm) 0.22222–0.22222 | 4 | 1 |
| [CU9TM2](#phase-cu-tm-cu9tm2); _phase:cu-tm:cu9tm2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1293.03 K, x(Tm) 0.18182–0.18182 | 10 | 1 |
| [CUTM_B2](#phase-cu-tm-cutm-b2); _phase:cu-tm:cutm-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1374.88 K, x(Tm) 0.5–0.5 | 6 | 1 |
| [FCC_A1](#phase-cu-tm-fcc-a1); _phase:cu-tm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1369.6 K, x(Tm) 0–1e-05 | 3 | 1 |
| [HCP_A3](#phase-cu-tm-hcp-a3); _phase:cu-tm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.39 K, x(Tm) 0.99812–1 | 2 | 1 |
| [LIQUID](#phase-cu-tm-liquid); _phase:cu-tm:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1178.12–2500 K, x(Tm) 0–1 | 21 | 1 |

## BCC_A2 (Cu–Tm)

- Id: `phase:cu-tm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:bcc-a2)

Names (2): _corpus: _corpus:phase:cu-tm:bcc-a2  
_tdb: _tdb:CuTm-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): BCC_A2, type code %B, sha256 `b25db1e4f57b8e8f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CU TM : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase_

## CU2TM (Cu–Tm)

- Id: `phase:cu-tm:cu2tm`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Tm 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1233.33 K, x(Tm) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:cu2tm)

Names (3): _corpus: _corpus:phase:cu-tm:cu2tm  
_paper: _paper:10.1016/j.jallcom.2009.03.101:Cu2Tm  
_tdb: _tdb:CuTm-09Wan.tdb:CU2TM  


### TDB models of CU2TM (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): CU2TM, type code %, sha256 `b25db1e4f57b8e8f…`

~~~~text
56: PHASE CU2TM % 2 2 1 !
57: CONST CU2TM : CU : TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase; reports values for this phase_

## CU5TM_C15B (Cu–Tm)

- Id: `phase:cu-tm:cu5tm-c15b`; status `assigned`
- Structure: AuBe5 · C15_b · cF24 · F-43m (216); type `st:c15-b-aube5-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtgy and oqmd-17174, space group 216
- Stoichiometry: Cu 0.8333, Tm 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1273.03 K, x(Tm) 0.16667–0.16667
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:cu5tm-c15b)

Names (5): _corpus: _corpus:phase:cu-tm:cu5tm-c15b  
_mp: _mp:mp-aaaabtgy  
_oqmd: _oqmd:oqmd-17174  
_paper: _paper:10.1016/j.jallcom.2009.03.101:Cu5Tm  
_tdb: _tdb:CuTm-09Wan.tdb:CU5TM_C15B  


### TDB models of CU5TM_C15B (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): CU5TM_C15B, type code %, sha256 `b25db1e4f57b8e8f…`

~~~~text
41: PHASE CU5TM_C15B % 2 5 1 !
42: CONST CU5TM_C15B : CU : TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase; reports values for this phase_

## CU7TM2 (Cu–Tm)

- Id: `phase:cu-tm:cu7tm2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu7Tm2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu7Tm2) — Hallstedt 2025 mmc2 row for CU7TM2: Cu7Tm2
- Stoichiometry: Cu 0.7778, Tm 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 1193.11–1232.63 K, x(Tm) 0.22222–0.22222
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:cu7tm2)

Names (3): _corpus: _corpus:phase:cu-tm:cu7tm2  
_paper: _paper:10.1016/j.jallcom.2009.03.101:Cu7Tm2  
_tdb: _tdb:CuTm-09Wan.tdb:CU7TM2  


### TDB models of CU7TM2 (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): CU7TM2, type code %, sha256 `b25db1e4f57b8e8f…`

~~~~text
51: PHASE CU7TM2 % 2 7 2 !
52: CONST CU7TM2 : CU : TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase; reports values for this phase_

## CU9TM2 (Cu–Tm)

- Id: `phase:cu-tm:cu9tm2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu9Tm2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu9Tm2) — Hallstedt 2025 mmc2 row for CU9TM2: Cu9Tm2
- Stoichiometry: Cu 0.8182, Tm 0.1818
- Stability: stable in 1 of 1 calculated diagram(s): 300–1293.03 K, x(Tm) 0.18182–0.18182
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:cu9tm2)

Names (3): _corpus: _corpus:phase:cu-tm:cu9tm2  
_paper: _paper:10.1016/j.jallcom.2009.03.101:Cu9Tm2  
_tdb: _tdb:CuTm-09Wan.tdb:CU9TM2  


### TDB models of CU9TM2 (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): CU9TM2, type code %, sha256 `b25db1e4f57b8e8f…`

~~~~text
46: PHASE CU9TM2 % 2 9 2 !
47: CONST CU9TM2 : CU : TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase; reports values for this phase_

## CUTM_B2 (Cu–Tm)

- Id: `phase:cu-tm:cutm-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaablx and oqmd-29826, space group 221
- Stoichiometry: Cu 0.5000, Tm 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1374.88 K, x(Tm) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:cutm-b2)

Names (5): _corpus: _corpus:phase:cu-tm:cutm-b2  
_mp: _mp:mp-aaaaablx  
_oqmd: _oqmd:oqmd-29826  
_paper: _paper:10.1016/j.jallcom.2009.03.101:CuTm  
_tdb: _tdb:CuTm-09Wan.tdb:CUTM_B2  


### TDB models of CUTM_B2 (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): CUTM_B2, type code %, sha256 `b25db1e4f57b8e8f…`

~~~~text
61: PHASE CUTM_B2 % 2 1 1 !
62: CONST CUTM_B2 : CU : TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cu–Tm)

- Id: `phase:cu-tm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1369.6 K, x(Tm) 0–1e-05
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-tm:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.03.101:(Cu)  
_tdb: _tdb:CuTm-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): FCC_A1, type code %A, sha256 `b25db1e4f57b8e8f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CU% TM : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Cu–Tm)

- Id: `phase:cu-tm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.39 K, x(Tm) 0.99812–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:hcp-a3)

Names (3): _corpus: _corpus:phase:cu-tm:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.03.101:(Tm)  
_tdb: _tdb:CuTm-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): HCP_A3, type code %A, sha256 `b25db1e4f57b8e8f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CU TM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Cu–Tm)

- Id: `phase:cu-tm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1178.12–2500 K, x(Tm) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tm:liquid)

Names (3): _corpus: _corpus:phase:cu-tm:liquid  
_paper: _paper:10.1016/j.jallcom.2009.03.101:L  
_tdb: _tdb:CuTm-09Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuTm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTm-09Wan.tdb): LIQUID, type code %, sha256 `b25db1e4f57b8e8f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CU TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.101](https://doi.org/10.1016/j.jallcom.2009.03.101) C.P. Wang, S.H. Guo, A.T. Tang, F.S. Pan, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–B and Cu–Tm systems, Journal of Alloys and Compounds 482, 67-72 (2009).  
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
