# Be–Ti phases

> Be–Ti system: 11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BE-TI.html · Markdown: https://data.orchid-project.org/phases/pages/BE-TI.md

11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BE-TI) · [full JSON](https://data.orchid-project.org/phases/systems/BE-TI.json) · [Be–Ti system page](https://data.orchid-project.org/systems/BE-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/BE-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Be–Ti system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_B2](#phase-be-ti-bcc-b2); _phase:be-ti:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1074.19–2499.73 K, x(Ti) 0–1 | 4 | 1 |
| [BE10TI](#phase-be-ti-be10ti); _phase:be-ti:be10ti_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1890.42 K, x(Ti) 0.09091–0.09091 | 0 | 1 |
| [BE12TI_D2B](#phase-be-ti-be12ti-d2b); _phase:be-ti:be12ti-d2b_ | Mn12Th · D2_b · tI26 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1839.94 K, x(Ti) 0.07692–0.07692 | 0 | 1 |
| [BE13TI2](#phase-be-ti-be13ti2); _phase:be-ti:be13ti2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1832.99 K, x(Ti) 0.13333–0.13333 | 0 | 1 |
| [BE17TI2](#phase-be-ti-be17ti2); _phase:be-ti:be17ti2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1939.92 K, x(Ti) 0.10526–0.10526 | 0 | 1 |
| [BE2TI_C15](#phase-be-ti-be2ti-c15); _phase:be-ti:be2ti-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1620.24 K, x(Ti) 0.33333–0.33333 | 0 | 1 |
| [BE3TI](#phase-be-ti-be3ti); _phase:be-ti:be3ti_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1730.52 K, x(Ti) 0.25–0.25 | 0 | 1 |
| [BE5TI4](#phase-be-ti-be5ti4); _phase:be-ti:be5ti4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1457.9 K, x(Ti) 0.44444–0.44444 | 0 | 1 |
| [FCC_A1](#phase-be-ti-fcc-a1); _phase:be-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-be-ti-hcp-a3); _phase:be-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1729.16 K, x(Ti) 0–1 | 0 | 1 |
| [LIQUID](#phase-be-ti-liquid); _phase:be-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1250–2500 K, x(Ti) 0–1 | 0 | 1 |

## BCC_B2 (Be–Ti)

- Id: `phase:be-ti:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in BeTi-06Tok.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1074.19–2499.73 K, x(Ti) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:bcc-b2)

Names (3): _corpus: _corpus:phase:be-ti:bcc-b2  
_paper: _paper:10.1361/105497106x92844:TiBe(B2)  
_tdb: _tdb:BeTi-06Tok.tdb:BCC_B2  


### TDB models of BCC_B2 (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BCC_B2, type code %B, sha256 `99382030a5f6684b…`

~~~~text
38: PHASE BCC_B2 %B 3 0.5 0.5 3 !
39: CONST BCC_B2 : BE% TI : BE TI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(79)90010-5](https://doi.org/10.1016/0364-5916%2879%2990010-5) Larry Kaufman, Lee E. Tanner, Coupled phase diagrams and thermochemical descriptions of the titanium-beryllium, zirconium-beryllium and hafnium-beryllium systems, Calphad 3, 91-107 (1979).  
_cited as the source of values for this phase_

## BE10TI (Be–Ti)

- Id: `phase:be-ti:be10ti`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Be10Ti) — Hallstedt 2025 mmc2 row for BE10TI: Be10Ti
- Stoichiometry: Be 0.9091, Ti 0.0909
- Stability: stable in 1 of 1 calculated diagram(s): 300–1890.42 K, x(Ti) 0.09091–0.09091
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:be10ti)

Names (2): _corpus: _corpus:phase:be-ti:be10ti  
_tdb: _tdb:BeTi-06Tok.tdb:BE10TI  


### TDB models of BE10TI (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BE10TI, type code %, sha256 `99382030a5f6684b…`

~~~~text
53: PHASE BE10TI % 2 10 1 !
54: CONST BE10TI : BE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## BE12TI_D2B (Be–Ti)

- Id: `phase:be-ti:be12ti-d2b`; status `assigned`
- Structure: Mn12Th · D2_b · tI26 · I4/mmm (139); type `st:d2-b-mn12th-ti26`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackvgd and oqmd-28706, space group 139
- Stoichiometry: Be 0.9231, Ti 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–1839.94 K, x(Ti) 0.07692–0.07692
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:be12ti-d2b)

Names (4): _corpus: _corpus:phase:be-ti:be12ti-d2b  
_mp: _mp:mp-aaackvgd  
_oqmd: _oqmd:oqmd-28706  
_tdb: _tdb:BeTi-06Tok.tdb:BE12TI_D2B  


### TDB models of BE12TI_D2B (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BE12TI_D2B, type code %, sha256 `99382030a5f6684b…`

~~~~text
48: PHASE BE12TI_D2B % 2 12 1 !
49: CONST BE12TI_D2B : BE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## BE13TI2 (Be–Ti)

- Id: `phase:be-ti:be13ti2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Be13Ti2) — Hallstedt 2025 mmc2 row for BE13TI2: Be13Ti2
- Stoichiometry: Be 0.8667, Ti 0.1333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1832.99 K, x(Ti) 0.13333–0.13333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:be13ti2)

Names (2): _corpus: _corpus:phase:be-ti:be13ti2  
_tdb: _tdb:BeTi-06Tok.tdb:BE13TI2  


### TDB models of BE13TI2 (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BE13TI2, type code %, sha256 `99382030a5f6684b…`

~~~~text
64: PHASE BE13TI2 % 2 13 2 !
65: CONST BE13TI2 : BE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## BE17TI2 (Be–Ti)

- Id: `phase:be-ti:be17ti2`; status `needs_review`
- No structure assigned. Why: mp_oqmd_space_groups_differ; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP Ti2Be17 at x(TI)=0.1053
- Candidate (dft_oqmd): R-3m (166) — on-hull OQMD Be17 Ti2 at x(TI)=0.1053
- Candidate (sgte_mmc2): Ni17Th2 · hP38 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for BE17TI2: Be17Ti2 (high T), see also Th2Zn17
- Candidate (sgte_mmc2): Th2Zn17 · hR19 · R-3m (166) — Hallstedt 2025 mmc2 row for BE17TI2: Be17Ti2 (low T), see also Ni17Th2
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — BeTi-06Tok.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), beta'
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — BeTi-06Tok.tdb: 'Prototype Th2Zn17 (hR19, R-3m), alpha'
- Stoichiometry: Be 0.8947, Ti 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 300–1939.92 K, x(Ti) 0.10526–0.10526
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:be17ti2)

Names (2): _corpus: _corpus:phase:be-ti:be17ti2  
_tdb: _tdb:BeTi-06Tok.tdb:BE17TI2  


### TDB models of BE17TI2 (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BE17TI2, type code %, sha256 `99382030a5f6684b…`

~~~~text
59: PHASE BE17TI2 % 2 17 2 !
60: CONST BE17TI2 : BE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## BE2TI_C15 (Be–Ti)

- Id: `phase:be-ti:be2ti-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaebt and oqmd-10907, space group 227
- Stoichiometry: Be 0.6667, Ti 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1620.24 K, x(Ti) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:be2ti-c15)

Names (4): _corpus: _corpus:phase:be-ti:be2ti-c15  
_mp: _mp:mp-aaaaaebt  
_oqmd: _oqmd:oqmd-10907  
_tdb: _tdb:BeTi-06Tok.tdb:BE2TI_C15  


### TDB models of BE2TI_C15 (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BE2TI_C15, type code %, sha256 `99382030a5f6684b…`

~~~~text
74: PHASE BE2TI_C15 % 2 2 1 !
75: CONST BE2TI_C15 : BE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## BE3TI (Be–Ti)

- Id: `phase:be-ti:be3ti`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Be 0.7500, Ti 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1730.52 K, x(Ti) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:be3ti)

Names (2): _corpus: _corpus:phase:be-ti:be3ti  
_tdb: _tdb:BeTi-06Tok.tdb:BE3TI  


### TDB models of BE3TI (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BE3TI, type code %, sha256 `99382030a5f6684b…`

~~~~text
69: PHASE BE3TI % 2 3 1 !
70: CONST BE3TI : BE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## BE5TI4 (Be–Ti)

- Id: `phase:be-ti:be5ti4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Be5Ti4) — Hallstedt 2025 mmc2 row for BE5TI4: Be5Ti4
- Stoichiometry: Be 0.5556, Ti 0.4444
- Stability: stable in 1 of 1 calculated diagram(s): 300–1457.9 K, x(Ti) 0.44444–0.44444
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:be5ti4)

Names (2): _corpus: _corpus:phase:be-ti:be5ti4  
_tdb: _tdb:BeTi-06Tok.tdb:BE5TI4  


### TDB models of BE5TI4 (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): BE5TI4, type code %, sha256 `99382030a5f6684b…`

~~~~text
79: PHASE BE5TI4 % 2 5 4 !
80: CONST BE5TI4 : BE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## FCC_A1 (Be–Ti)

- Id: `phase:be-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:fcc-a1)

Names (2): _corpus: _corpus:phase:be-ti:fcc-a1  
_tdb: _tdb:BeTi-06Tok.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): FCC_A1, type code %A, sha256 `99382030a5f6684b…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BE TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## HCP_A3 (Be–Ti)

- Id: `phase:be-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1729.16 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:hcp-a3)

Names (2): _corpus: _corpus:phase:be-ti:hcp-a3  
_tdb: _tdb:BeTi-06Tok.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): HCP_A3, type code %A, sha256 `99382030a5f6684b…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : BE% TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
_assessment that models this phase_

## LIQUID (Be–Ti)

- Id: `phase:be-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1250–2500 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-ti:liquid)

Names (2): _corpus: _corpus:phase:be-ti:liquid  
_tdb: _tdb:BeTi-06Tok.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BeTi-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeTi-06Tok.tdb): LIQUID, type code %, sha256 `99382030a5f6684b…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BE TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497106X92844](https://doi.org/10.1361/105497106X92844) T. Tokunaga, H. Ohtani, M.Hasebe, J. Phase Equilib. Diffus., 27, 83-91(2006).  
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
