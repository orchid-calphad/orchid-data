# Bi–Zr phases

> Bi–Zr system: 10 phases (tier A 4, tier B 1, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/BI-ZR.md

10 phases (tier A 4, tier B 1, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/BI-ZR.json) · [Bi–Zr system page](https://data.orchid-project.org/systems/BI-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Zr system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-zr-a7-rhombohedral); _phase:bi-zr:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Zr) 0–0 | 0 | 1 |
| [BCC_A2](#phase-bi-zr-bcc-a2); _phase:bi-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 977.93–2342.85 K, x(Zr) 0.86157–1 | 0 | 1 |
| [BI2ZR](#phase-bi-zr-bi2zr); _phase:bi-zr:bi2zr_ | TiAs2 · oP24 · Pnnm (58) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1018.01 K, x(Zr) 0.33333–0.33333 | 0 | 1 |
| [BI2ZR3](#phase-bi-zr-bi2zr3); _phase:bi-zr:bi2zr3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1766.91 K, x(Zr) 0.6–0.6 | 0 | 1 |
| [BI5ZR3](#phase-bi-zr-bi5zr3); _phase:bi-zr:bi5zr3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1004.43–1106.84 K, x(Zr) 0.38168–0.38168 | 0 | 1 |
| [BIZR](#phase-bi-zr-bizr); _phase:bi-zr:bizr_ | SbZr · oC24 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1577.11 K, x(Zr) 0.5–0.5 | 0 | 1 |
| [BIZR2](#phase-bi-zr-bizr2); _phase:bi-zr:bizr2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1614.38 K, x(Zr) 0.66667–0.66667 | 0 | 1 |
| [FCC_A1](#phase-bi-zr-fcc-a1); _phase:bi-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-zr-hcp-a3); _phase:bi-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1172.93 K, x(Zr) 0.95712–1 | 0 | 1 |
| [LIQUID](#phase-bi-zr-liquid); _phase:bi-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 544.55–4000 K, x(Zr) 0–1 | 0 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Zr)

- Id: `phase:bi-zr:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Zr) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:bi-zr:a7-rhombohedral  
_tdb: _tdb:BiZr-22Gao.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `11281eb6a2ab5930…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BCC_A2 (Bi–Zr)

- Id: `phase:bi-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 977.93–2342.85 K, x(Zr) 0.86157–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-zr:bcc-a2  
_tdb: _tdb:BiZr-22Gao.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): BCC_A2, type code %B, sha256 `11281eb6a2ab5930…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BI2ZR (Bi–Zr)

- Id: `phase:bi-zr:bi2zr`; status `assigned`
- Structure: TiAs2 · oP24 · Pnnm (58); type `st:tias2-op24`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Bi 0.6667, Zr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1018.01 K, x(Zr) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:bi2zr)

Names (4): _corpus: _corpus:phase:bi-zr:bi2zr  
_mp: _mp:mp-aaaabrwc  
_oqmd: _oqmd:oqmd-7896  
_tdb: _tdb:BiZr-22Gao.tdb:BI2ZR  


### TDB models of BI2ZR (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): BI2ZR, type code %, sha256 `11281eb6a2ab5930…`

~~~~text
50: PHASE BI2ZR % 2 2 1 !
51: CONST BI2ZR : BI : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BI2ZR3 (Bi–Zr)

- Id: `phase:bi-zr:bi2zr3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Bi2Zr3) — Hallstedt 2025 mmc2 row for BI2ZR3: Bi2Zr3
- Stoichiometry: Bi 0.4000, Zr 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1766.91 K, x(Zr) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:bi2zr3)

Names (2): _corpus: _corpus:phase:bi-zr:bi2zr3  
_tdb: _tdb:BiZr-22Gao.tdb:BI2ZR3  


### TDB models of BI2ZR3 (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): BI2ZR3, type code %, sha256 `11281eb6a2ab5930…`

~~~~text
65: PHASE BI2ZR3 % 2 2 3 !
66: CONST BI2ZR3 : BI : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BI5ZR3 (Bi–Zr)

- Id: `phase:bi-zr:bi5zr3`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): Ga5Ir3 · tP32 · P-4n2 (118) — Hallstedt 2025 mmc2 row for BI5ZR3: Bi5Zr3
- Candidate (tdb_comment): Ga5Ir3 · tP32 · P-4n2 — BiZr-22Gao.tdb: 'Prototype Ga5Ir3 (tP32, P-4n2)'
- Stoichiometry: Bi 0.6183, Zr 0.3817
- Stability: stable in 1 of 1 calculated diagram(s): 1004.43–1106.84 K, x(Zr) 0.38168–0.38168
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:bi5zr3)

Names (2): _corpus: _corpus:phase:bi-zr:bi5zr3  
_tdb: _tdb:BiZr-22Gao.tdb:BI5ZR3  


### TDB models of BI5ZR3 (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): BI5ZR3, type code %, sha256 `11281eb6a2ab5930…`

~~~~text
55: PHASE BI5ZR3 % 2 1.62 1 !
56: CONST BI5ZR3 : BI : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BIZR (Bi–Zr)

- Id: `phase:bi-zr:bizr`; status `assigned`
- Structure: SbZr · oC24 · Cmcm (63); type `st:sbzr-oc24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.5000, Zr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1577.11 K, x(Zr) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:bizr)

Names (2): _corpus: _corpus:phase:bi-zr:bizr  
_tdb: _tdb:BiZr-22Gao.tdb:BIZR  


### TDB models of BIZR (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): BIZR, type code %, sha256 `11281eb6a2ab5930…`

~~~~text
60: PHASE BIZR % 2 1 1 !
61: CONST BIZR : BI : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BIZR2 (Bi–Zr)

- Id: `phase:bi-zr:bizr2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Bi1 Zr2 at x(ZR)=0.6667
- Candidate (sgte_mmc2): (BiZr2) — Hallstedt 2025 mmc2 row for BIZR2: BiZr2
- Stoichiometry: Bi 0.3333, Zr 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1614.38 K, x(Zr) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:bizr2)

Names (2): _corpus: _corpus:phase:bi-zr:bizr2  
_tdb: _tdb:BiZr-22Gao.tdb:BIZR2  


### TDB models of BIZR2 (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): BIZR2, type code %, sha256 `11281eb6a2ab5930…`

~~~~text
70: PHASE BIZR2 % 2 1 2 !
71: CONST BIZR2 : BI : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## FCC_A1 (Bi–Zr)

- Id: `phase:bi-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-zr:fcc-a1  
_tdb: _tdb:BiZr-22Gao.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): FCC_A1, type code %A, sha256 `11281eb6a2ab5930…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## HCP_A3 (Bi–Zr)

- Id: `phase:bi-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1172.93 K, x(Zr) 0.95712–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-zr:hcp-a3  
_tdb: _tdb:BiZr-22Gao.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): HCP_A3, type code %A, sha256 `11281eb6a2ab5930…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI ZR% : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## LIQUID (Bi–Zr)

- Id: `phase:bi-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 544.55–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-zr:liquid)

Names (2): _corpus: _corpus:phase:bi-zr:liquid  
_tdb: _tdb:BiZr-22Gao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiZr-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiZr-22Gao.tdb): LIQUID, type code %, sha256 `11281eb6a2ab5930…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
