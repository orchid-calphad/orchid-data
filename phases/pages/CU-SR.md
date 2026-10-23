# Cu–Sr phases

> Cu–Sr system: 6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-SR.html · Markdown: https://data.orchid-project.org/phases/pages/CU-SR.md

6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-SR) · [full JSON](https://data.orchid-project.org/phases/systems/CU-SR.json) · [Cu–Sr system page](https://data.orchid-project.org/systems/CU-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Sr system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-sr-bcc-a2); _phase:cu-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300.07–2498.82 K, x(Sr) 0.99998–1 | 0 | 1 |
| [CU5SR_D2D](#phase-cu-sr-cu5sr-d2d); _phase:cu-sr:cu5sr-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1118.42 K, x(Sr) 0.16667–0.16667 | 0 | 1 |
| [CUSR](#phase-cu-sr-cusr); _phase:cu-sr:cusr_ | BaCu · hP8 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–858.99 K, x(Sr) 0.5–0.5 | 0 | 1 |
| [FCC_A1](#phase-cu-sr-fcc-a1); _phase:cu-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1401.02 K, x(Sr) 0–1 | 0 | 1 |
| [HCP_A3](#phase-cu-sr-hcp-a3); _phase:cu-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cu-sr-liquid); _phase:cu-sr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 779.33–2500 K, x(Sr) 0–1 | 1 | 1 |

## BCC_A2 (Cu–Sr)

- Id: `phase:cu-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.07–2498.82 K, x(Sr) 0.99998–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sr:bcc-a2)

Names (2): _corpus: _corpus:phase:cu-sr:bcc-a2  
_tdb: _tdb:CuSr-96Ris-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuSr-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSr-96Ris-LB.tdb): BCC_A2, type code %B, sha256 `5eb3641bdde41c76…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CU SR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## CU5SR_D2D (Cu–Sr)

- Id: `phase:cu-sr:cu5sr-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaeaw and oqmd-24615, space group 191
- Stoichiometry: Cu 0.8333, Sr 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1118.42 K, x(Sr) 0.16667–0.16667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sr:cu5sr-d2d)

Names (4): _corpus: _corpus:phase:cu-sr:cu5sr-d2d  
_mp: _mp:mp-aaaaaeaw  
_oqmd: _oqmd:oqmd-24615  
_tdb: _tdb:CuSr-96Ris-LB.tdb:CU5SR_D2D  


### TDB models of CU5SR_D2D (1): PHASE and CONSTITUENT statements as written

[CuSr-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSr-96Ris-LB.tdb): CU5SR_D2D, type code %, sha256 `5eb3641bdde41c76…`

~~~~text
48: PHASE CU5SR_D2D % 2 5 1 !
49: CONST CU5SR_D2D : CU : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## CUSR (Cu–Sr)

- Id: `phase:cu-sr:cusr`; status `assigned`
- Structure: BaCu · hP8 · P6_3/mmc (194); type `st:bacu-hp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_194_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.5000, Sr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–858.99 K, x(Sr) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sr:cusr)

Names (2): _corpus: _corpus:phase:cu-sr:cusr  
_tdb: _tdb:CuSr-96Ris-LB.tdb:CUSR  


### TDB models of CUSR (1): PHASE and CONSTITUENT statements as written

[CuSr-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSr-96Ris-LB.tdb): CUSR, type code %, sha256 `5eb3641bdde41c76…`

~~~~text
53: PHASE CUSR % 2 1 1 !
54: CONST CUSR : CU : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## FCC_A1 (Cu–Sr)

- Id: `phase:cu-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1401.02 K, x(Sr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sr:fcc-a1)

Names (2): _corpus: _corpus:phase:cu-sr:fcc-a1  
_tdb: _tdb:CuSr-96Ris-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuSr-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSr-96Ris-LB.tdb): FCC_A1, type code %A, sha256 `5eb3641bdde41c76…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CU% SR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## HCP_A3 (Cu–Sr)

- Id: `phase:cu-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sr:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-sr:hcp-a3  
_tdb: _tdb:CuSr-96Ris-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuSr-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSr-96Ris-LB.tdb): HCP_A3, type code %A, sha256 `5eb3641bdde41c76…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CU SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## LIQUID (Cu–Sr)

- Id: `phase:cu-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 779.33–2500 K, x(Sr) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sr:liquid)

Names (3): _corpus: _corpus:phase:cu-sr:liquid  
_paper: _paper:10.1016/s0364-5916(96)00022-3:liquid  
_tdb: _tdb:CuSr-96Ris-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuSr-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSr-96Ris-LB.tdb): LIQUID, type code %, sha256 `5eb3641bdde41c76…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CU SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
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
