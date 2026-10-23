# Bi–Ca phases

> Bi–Ca system: 8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-CA.html · Markdown: https://data.orchid-project.org/phases/pages/BI-CA.md

8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-CA) · [full JSON](https://data.orchid-project.org/phases/systems/BI-CA.json) · [Bi–Ca system page](https://data.orchid-project.org/systems/BI-CA.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-CA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Ca system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-ca-a7-rhombohedral); _phase:bi-ca:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Ca) 0–0 | 0 | 1 |
| [BCC_A2](#phase-bi-ca-bcc-a2); _phase:bi-ca:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 716.03–2500 K, x(Ca) 1–1 | 0 | 1 |
| [BI10CA11_HT](#phase-bi-ca-bi10ca11-ht); _phase:bi-ca:bi10ca11-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 767–1370.16 K, x(Ca) 0.52381–0.52381 | 0 | 1 |
| [BI10CA11_LT](#phase-bi-ca-bi10ca11-lt); _phase:bi-ca:bi10ca11-lt_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–767 K, x(Ca) 0.52381–0.52381 | 0 | 1 |
| [BI3CA5](#phase-bi-ca-bi3ca5); _phase:bi-ca:bi3ca5_ | Sb3Yb5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1624.27 K, x(Ca) 0.625–0.625 | 0 | 1 |
| [FCC_A1](#phase-bi-ca-fcc-a1); _phase:bi-ca:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Ca) 1–1 | 0 | 1 |
| [HCP_A3](#phase-bi-ca-hcp-a3); _phase:bi-ca:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-bi-ca-liquid); _phase:bi-ca:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 542.57–2500 K, x(Ca) 0–1 | 0 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Ca)

- Id: `phase:bi-ca:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Ca) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:bi-ca:a7-rhombohedral  
_tdb: _tdb:BiCa-22Gao.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `3dc2186b03d995a0…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BCC_A2 (Bi–Ca)

- Id: `phase:bi-ca:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 716.03–2500 K, x(Ca) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-ca:bcc-a2  
_tdb: _tdb:BiCa-22Gao.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): BCC_A2, type code %B, sha256 `3dc2186b03d995a0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI CA% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BI10CA11_HT (Bi–Ca)

- Id: `phase:bi-ca:bi10ca11-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): I4/mmm (139) — on-hull MP Ca11Bi10 at x(CA)=0.5238
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Bi10 Ca11 at x(CA)=0.5238
- Candidate (sgte_mmc2): (Bi10Ca11) — Hallstedt 2025 mmc2 row for BI10CA11_HT: Bi10Ca11 (high T)
- Stoichiometry: Bi 0.4762, Ca 0.5238
- Stability: stable in 1 of 1 calculated diagram(s): 767–1370.16 K, x(Ca) 0.52381–0.52381
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:bi10ca11-ht)

Names (2): _corpus: _corpus:phase:bi-ca:bi10ca11-ht  
_tdb: _tdb:BiCa-22Gao.tdb:BI10CA11_HT  


### TDB models of BI10CA11_HT (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): BI10CA11_HT, type code %, sha256 `3dc2186b03d995a0…`

~~~~text
51: PHASE BI10CA11_HT % 2 10 11 !
52: CONST BI10CA11_HT : BI : CA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BI10CA11_LT (Bi–Ca)

- Id: `phase:bi-ca:bi10ca11-lt`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4762, Ca 0.5238
- Stability: stable in 1 of 1 calculated diagram(s): 300–767 K, x(Ca) 0.52381–0.52381
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:bi10ca11-lt)

Names (2): _corpus: _corpus:phase:bi-ca:bi10ca11-lt  
_tdb: _tdb:BiCa-22Gao.tdb:BI10CA11_LT  


### TDB models of BI10CA11_LT (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): BI10CA11_LT, type code %, sha256 `3dc2186b03d995a0…`

~~~~text
46: PHASE BI10CA11_LT % 2 10 11 !
47: CONST BI10CA11_LT : BI : CA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## BI3CA5 (Bi–Ca)

- Id: `phase:bi-ca:bi3ca5`; status `assigned`
- Structure: Sb3Yb5 · oP32 · Pnma (62); type `st:sb3yb5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Ca 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1624.27 K, x(Ca) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:bi3ca5)

Names (2): _corpus: _corpus:phase:bi-ca:bi3ca5  
_tdb: _tdb:BiCa-22Gao.tdb:BI3CA5  


### TDB models of BI3CA5 (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): BI3CA5, type code %, sha256 `3dc2186b03d995a0…`

~~~~text
56: PHASE BI3CA5 % 2 3 5 !
57: CONST BI3CA5 : BI : CA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## FCC_A1 (Bi–Ca)

- Id: `phase:bi-ca:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Ca) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-ca:fcc-a1  
_tdb: _tdb:BiCa-22Gao.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): FCC_A1, type code %A, sha256 `3dc2186b03d995a0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI CA% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## HCP_A3 (Bi–Ca)

- Id: `phase:bi-ca:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-ca:hcp-a3  
_tdb: _tdb:BiCa-22Gao.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): HCP_A3, type code %A, sha256 `3dc2186b03d995a0…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI CA : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
_assessment that models this phase_

## LIQUID (Bi–Ca)

- Id: `phase:bi-ca:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 542.57–2500 K, x(Ca) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ca:liquid)

Names (2): _corpus: _corpus:phase:bi-ca:liquid  
_tdb: _tdb:BiCa-22Gao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiCa-22Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCa-22Gao.tdb): LIQUID, type code %, sha256 `3dc2186b03d995a0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI CA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8428](https://doi.org/10.1515/ijmr-2021-8428) F. Gao, Y. Liu, P. Zhou, D. Huang, T. Fu, S. Zhang, Y. Du, Int. J. Mater. Res., 113, 419-27(2022).  
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
