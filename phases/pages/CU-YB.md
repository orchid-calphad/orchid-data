# Cu–Yb phases

> Cu–Yb system: 9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-YB.html · Markdown: https://data.orchid-project.org/phases/pages/CU-YB.md

9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-YB) · [full JSON](https://data.orchid-project.org/phases/systems/CU-YB.json) · [Cu–Yb system page](https://data.orchid-project.org/systems/CU-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Yb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-yb-bcc-a2); _phase:cu-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1031.31–1096.99 K, x(Yb) 0.99962–1 | 0 | 1 |
| [CU2YB](#phase-cu-yb-cu2yb); _phase:cu-yb:cu2yb_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1025.43 K, x(Yb) 0.33333–0.33333 | 4 | 1 |
| [CU5YB_D2D](#phase-cu-yb-cu5yb-d2d); _phase:cu-yb:cu5yb-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1151.01 K, x(Yb) 0.16667–0.16667 | 4 | 1 |
| [CU7YB2](#phase-cu-yb-cu7yb2); _phase:cu-yb:cu7yb2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1095.2 K, x(Yb) 0.22222–0.22222 | 4 | 1 |
| [CU9YB2](#phase-cu-yb-cu9yb2); _phase:cu-yb:cu9yb2_ | Cu9Yb2 · mC7448 · C2 (5) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1187.08 K, x(Yb) 0.18182–0.18182 | 6 | 1 |
| [CUYB_B27](#phase-cu-yb-cuyb-b27); _phase:cu-yb:cuyb-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–905.19 K, x(Yb) 0.5–0.5 | 4 | 1 |
| [FCC_A1](#phase-cu-yb-fcc-a1); _phase:cu-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1370 K, x(Yb) 0–1 | 4 | 1 |
| [HCP_A3](#phase-cu-yb-hcp-a3); _phase:cu-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cu-yb-liquid); _phase:cu-yb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 747.97–2500 K, x(Yb) 0–1 | 14 | 1 |

## BCC_A2 (Cu–Yb)

- Id: `phase:cu-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1031.31–1096.99 K, x(Yb) 0.99962–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:bcc-a2)

Names (2): _corpus: _corpus:phase:cu-yb:bcc-a2  
_tdb: _tdb:CuYb-07Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): BCC_A2, type code %B, sha256 `d08c0b2a0da7e0ac…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CU YB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase_

## CU2YB (Cu–Yb)

- Id: `phase:cu-yb:cu2yb`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Yb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1025.43 K, x(Yb) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:cu2yb)

Names (3): _corpus: _corpus:phase:cu-yb:cu2yb  
_paper: _paper:10.1016/j.calphad.2006.11.003:Cu2Yb  
_tdb: _tdb:CuYb-07Zha.tdb:CU2YB  


### TDB models of CU2YB (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): CU2YB, type code %, sha256 `d08c0b2a0da7e0ac…`

~~~~text
65: PHASE CU2YB % 2 2 1 !
66: CONST CU2YB : CU : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90158-5](https://doi.org/10.1016/0022-5088%2871%2990158-5) A. Iandelli, A. Palenzona, The ytterbium-copper system, Journal of the Less Common Metals 25, 333-335 (1971).  
_cited as the source of values for this phase_

## CU5YB_D2D (Cu–Yb)

- Id: `phase:cu-yb:cu5yb-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.8333, Yb 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1151.01 K, x(Yb) 0.16667–0.16667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:cu5yb-d2d)

Names (3): _corpus: _corpus:phase:cu-yb:cu5yb-d2d  
_paper: _paper:10.1016/j.calphad.2006.11.003:Cu5Yb  
_tdb: _tdb:CuYb-07Zha.tdb:CU5YB_D2D  


### TDB models of CU5YB_D2D (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): CU5YB_D2D, type code %, sha256 `d08c0b2a0da7e0ac…`

~~~~text
50: PHASE CU5YB_D2D % 2 5 1 !
51: CONST CU5YB_D2D : CU : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90158-5](https://doi.org/10.1016/0022-5088%2871%2990158-5) A. Iandelli, A. Palenzona, The ytterbium-copper system, Journal of the Less Common Metals 25, 333-335 (1971).  
_cited as the source of values for this phase_

## CU7YB2 (Cu–Yb)

- Id: `phase:cu-yb:cu7yb2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu7Yb2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu7Yb2) — Hallstedt 2025 mmc2 row for CU7YB2: Cu7Yb2
- Stoichiometry: Cu 0.7778, Yb 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 300–1095.2 K, x(Yb) 0.22222–0.22222
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:cu7yb2)

Names (3): _corpus: _corpus:phase:cu-yb:cu7yb2  
_paper: _paper:10.1016/j.calphad.2006.11.003:Cu7Yb2  
_tdb: _tdb:CuYb-07Zha.tdb:CU7YB2  


### TDB models of CU7YB2 (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): CU7YB2, type code %, sha256 `d08c0b2a0da7e0ac…`

~~~~text
60: PHASE CU7YB2 % 2 7 2 !
61: CONST CU7YB2 : CU : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90158-5](https://doi.org/10.1016/0022-5088%2871%2990158-5) A. Iandelli, A. Palenzona, The ytterbium-copper system, Journal of the Less Common Metals 25, 333-335 (1971).  
_cited as the source of values for this phase_

## CU9YB2 (Cu–Yb)

- Id: `phase:cu-yb:cu9yb2`; status `assigned`
- Structure: Cu9Yb2 · mC7448 · C2 (5); type `st:cu9yb2-mc7448`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.8182, Yb 0.1818
- Stability: stable in 1 of 1 calculated diagram(s): 300–1187.08 K, x(Yb) 0.18182–0.18182
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:cu9yb2)

Names (3): _corpus: _corpus:phase:cu-yb:cu9yb2  
_paper: _paper:10.1016/j.calphad.2006.11.003:Cu9Yb2  
_tdb: _tdb:CuYb-07Zha.tdb:CU9YB2  


### TDB models of CU9YB2 (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): CU9YB2, type code %, sha256 `d08c0b2a0da7e0ac…`

~~~~text
55: PHASE CU9YB2 % 2 9 2 !
56: CONST CU9YB2 : CU : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90158-5](https://doi.org/10.1016/0022-5088%2871%2990158-5) A. Iandelli, A. Palenzona, The ytterbium-copper system, Journal of the Less Common Metals 25, 333-335 (1971).  
_cited as the source of values for this phase_

## CUYB_B27 (Cu–Yb)

- Id: `phase:cu-yb:cuyb-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.5000, Yb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–905.19 K, x(Yb) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:cuyb-b27)

Names (3): _corpus: _corpus:phase:cu-yb:cuyb-b27  
_paper: _paper:10.1016/j.calphad.2006.11.003:CuYb  
_tdb: _tdb:CuYb-07Zha.tdb:CUYB_B27  


### TDB models of CUYB_B27 (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): CUYB_B27, type code %, sha256 `d08c0b2a0da7e0ac…`

~~~~text
70: PHASE CUYB_B27 % 2 1 1 !
71: CONST CUYB_B27 : CU : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90158-5](https://doi.org/10.1016/0022-5088%2871%2990158-5) A. Iandelli, A. Palenzona, The ytterbium-copper system, Journal of the Less Common Metals 25, 333-335 (1971).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Yb)

- Id: `phase:cu-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1370 K, x(Yb) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-yb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2006.11.003:FCC(Cu), paper:10.1016/j.calphad.2006.11.003:FCC(Yb)  
_tdb: _tdb:CuYb-07Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): FCC_A1, type code %A, sha256 `d08c0b2a0da7e0ac…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CU% YB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90158-5](https://doi.org/10.1016/0022-5088%2871%2990158-5) A. Iandelli, A. Palenzona, The ytterbium-copper system, Journal of the Less Common Metals 25, 333-335 (1971).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Yb)

- Id: `phase:cu-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-yb:hcp-a3  
_tdb: _tdb:CuYb-07Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): HCP_A3, type code %A, sha256 `d08c0b2a0da7e0ac…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CU YB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase_

## LIQUID (Cu–Yb)

- Id: `phase:cu-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 747.97–2500 K, x(Yb) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-yb:liquid)

Names (3): _corpus: _corpus:phase:cu-yb:liquid  
_paper: _paper:10.1016/j.calphad.2006.11.003:L  
_tdb: _tdb:CuYb-07Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuYb-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuYb-07Zha.tdb): LIQUID, type code %, sha256 `d08c0b2a0da7e0ac…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CU YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90158-5](https://doi.org/10.1016/0022-5088%2871%2990158-5) A. Iandelli, A. Palenzona, The ytterbium-copper system, Journal of the Less Common Metals 25, 333-335 (1971).  
_cited as the source of values for this phase_

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
