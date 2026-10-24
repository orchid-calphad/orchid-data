# Ca–Cu phases

> Ca–Cu system: 7 phases (tier A 4, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-CU.html · Markdown: https://data.orchid-project.org/phases/pages/CA-CU.md

7 phases (tier A 4, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-CU) · [full JSON](https://data.orchid-project.org/phases/systems/CA-CU.json) · [Ca–Cu system page](https://data.orchid-project.org/systems/CA-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Cu system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-cu-bcc-a2); _phase:ca-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 680.6–1124.71 K, x(Cu) 0–1e-05 | 0 | 2 |
| [CA2CU](#phase-ca-cu-ca2cu); _phase:ca-cu:ca2cu_ | Ca2Cu · oP12 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–785.47 K, x(Cu) 0.33333–0.33333 | 1 | 2 |
| [CACU](#phase-ca-cu-cacu); _phase:ca-cu:cacu_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–841.26 K, x(Cu) 0.5–0.5 | 1 | 2 |
| [CACU5_D2D](#phase-ca-cu-cacu5-d2d); _phase:ca-cu:cacu5-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1223.63 K, x(Cu) 0.83333–0.83333 | 0 | 2 |
| [FCC_A1](#phase-ca-cu-fcc-a1); _phase:ca-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.87 K, x(Cu) 0–1 | 0 | 2 |
| [HCP_A3](#phase-ca-cu-hcp-a3); _phase:ca-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ca-cu-liquid); _phase:ca-cu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 753.69–2500 K, x(Cu) 0–1 | 4 | 2 |

## BCC_A2 (Ca–Cu)

- Id: `phase:ca-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 680.6–1124.71 K, x(Cu) 0–1e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-cu:bcc-a2)

Names (3): _corpus: _corpus:phase:ca-cu:bcc-a2  
_tdb: _tdb:CaCu-96Ris-LB.tdb:BCC_A2, tdb:CaCu-97Ais.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CaCu-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-96Ris-LB.tdb): BCC_A2, type code %B, sha256 `a46c915ad7d9c07f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CA% CU : VA : !
~~~~

[CaCu-97Ais.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-97Ais.tdb): BCC_A2, type code %B, sha256 `649c86c7eee5fdbf…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CA% CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## CA2CU (Ca–Cu)

- Id: `phase:ca-cu:ca2cu`; status `assigned`
- Structure: Ca2Cu · oP12 · Pnma (62); type `st:ca2cu-op12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_6_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.6667, Cu 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–785.47 K, x(Cu) 0.33333–0.33333
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-cu:ca2cu)

Names (4): _corpus: _corpus:phase:ca-cu:ca2cu  
_paper: _paper:10.1016/s0364-5916(96)00022-3:Ca2Cu  
_tdb: _tdb:CaCu-96Ris-LB.tdb:CA2CU, tdb:CaCu-97Ais.tdb:CA2CU  


### TDB models of CA2CU (2): PHASE and CONSTITUENT statements as written

[CaCu-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-96Ris-LB.tdb): CA2CU, type code %, sha256 `a46c915ad7d9c07f…`

~~~~text
41: PHASE CA2CU % 2 2 1 !
42: CONST CA2CU : CA : CU : !
~~~~

[CaCu-97Ais.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-97Ais.tdb): CA2CU, type code %, sha256 `649c86c7eee5fdbf…`

~~~~text
45: PHASE CA2CU % 2 2 1 !
46: CONST CA2CU : CA : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase; reports values for this phase_

## CACU (Ca–Cu)

- Id: `phase:ca-cu:cacu`; status `needs_review`
- No structure assigned. Why: dft_space_group_62_matches_0_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Pnma (62) — on-hull MP CaCu at x(CU)=0.5000
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Ca1 Cu1 at x(CU)=0.5000
- Candidate (sgte_mmc2): CaCu-alpha · mP20 · P2_1/m (11) — Hallstedt 2025 mmc2 row for CACU: alpha-CaCu
- Candidate (sgte_mmc2): CaCu-beta · oP40 · Pnma (62) — Hallstedt 2025 mmc2 row for CACU: beta-CaCu
- Candidate (tdb_comment): alpha-CaCu · mP20 · P2_1/m — CaCu-96Ris-LB.tdb: 'Prototype alpha-CaCu (mP20, P2_1/m)'
- Candidate (tdb_comment): alpha-CaCu · mP20 · P2_1/m — CaCu-97Ais.tdb: 'Prototype alpha-CaCu (mP20, P2_1/m)'
- Stoichiometry: Ca 0.5000, Cu 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–841.26 K, x(Cu) 0.5–0.5
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-cu:cacu)

Names (4): _corpus: _corpus:phase:ca-cu:cacu  
_paper: _paper:10.1016/s0364-5916(96)00022-3:CaCu  
_tdb: _tdb:CaCu-96Ris-LB.tdb:CACU, tdb:CaCu-97Ais.tdb:CACU  


### TDB models of CACU (2): PHASE and CONSTITUENT statements as written

[CaCu-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-96Ris-LB.tdb): CACU, type code %, sha256 `a46c915ad7d9c07f…`

~~~~text
47: PHASE CACU % 2 1 1 !
48: CONST CACU : CA : CU : !
~~~~

[CaCu-97Ais.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-97Ais.tdb): CACU, type code %, sha256 `649c86c7eee5fdbf…`

~~~~text
51: PHASE CACU % 2 1 1 !
52: CONST CACU : CA : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase; reports values for this phase_

## CACU5_D2D (Ca–Cu)

- Id: `phase:ca-cu:cacu5-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacuk and oqmd-10978, space group 191
- Stoichiometry: Ca 0.1667, Cu 0.8333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1223.63 K, x(Cu) 0.83333–0.83333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-cu:cacu5-d2d)

Names (5): _corpus: _corpus:phase:ca-cu:cacu5-d2d  
_mp: _mp:mp-aaaaacuk  
_oqmd: _oqmd:oqmd-10978  
_tdb: _tdb:CaCu-96Ris-LB.tdb:CACU5_D2D, tdb:CaCu-97Ais.tdb:CACU5_D2D  


### TDB models of CACU5_D2D (2): PHASE and CONSTITUENT statements as written

[CaCu-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-96Ris-LB.tdb): CACU5_D2D, type code %, sha256 `a46c915ad7d9c07f…`

~~~~text
52: PHASE CACU5_D2D % 2 1 5 !
53: CONST CACU5_D2D : CA : CU : !
~~~~

[CaCu-97Ais.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-97Ais.tdb): CACU5_D2D, type code %, sha256 `649c86c7eee5fdbf…`

~~~~text
56: PHASE CACU5_D2D % 2 1 5 !
57: CONST CACU5_D2D : CA : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## FCC_A1 (Ca–Cu)

- Id: `phase:ca-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.87 K, x(Cu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-cu:fcc-a1)

Names (3): _corpus: _corpus:phase:ca-cu:fcc-a1  
_tdb: _tdb:CaCu-96Ris-LB.tdb:FCC_A1, tdb:CaCu-97Ais.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CaCu-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-96Ris-LB.tdb): FCC_A1, type code %A, sha256 `a46c915ad7d9c07f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CA% CU% : VA : !
~~~~

[CaCu-97Ais.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-97Ais.tdb): FCC_A1, type code %A, sha256 `649c86c7eee5fdbf…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CA% CU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## HCP_A3 (Ca–Cu)

- Id: `phase:ca-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:ca-cu:hcp-a3  
_tdb: _tdb:CaCu-96Ris-LB.tdb:HCP_A3, tdb:CaCu-97Ais.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CaCu-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-96Ris-LB.tdb): HCP_A3, type code %A, sha256 `a46c915ad7d9c07f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CA CU : VA : !
~~~~

[CaCu-97Ais.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-97Ais.tdb): HCP_A3, type code %A, sha256 `649c86c7eee5fdbf…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CA CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00022-3](https://doi.org/10.1016/S0364-5916%2896%2900022-3) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, Calphad, 20, 151-60(1996).  
_assessment that models this phase_

## LIQUID (Ca–Cu)

- Id: `phase:ca-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 753.69–2500 K, x(Cu) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-cu:liquid)

Names (4): _corpus: _corpus:phase:ca-cu:liquid  
_paper: _paper:10.1016/s0364-5916(96)00022-3:liquid  
_tdb: _tdb:CaCu-96Ris-LB.tdb:LIQUID, tdb:CaCu-97Ais.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CaCu-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-96Ris-LB.tdb): LIQUID, type code %, sha256 `a46c915ad7d9c07f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CA CU : !
~~~~

[CaCu-97Ais.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCu-97Ais.tdb): LIQUID, type code %, sha256 `649c86c7eee5fdbf…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CA CU : !
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
