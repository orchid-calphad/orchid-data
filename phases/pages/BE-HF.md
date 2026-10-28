# Be–Hf phases

> Be–Hf system: 7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BE-HF.html · Markdown: https://data.orchid-project.org/phases/pages/BE-HF.md

7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BE-HF) · [full JSON](https://data.orchid-project.org/phases/systems/BE-HF.json) · [Be–Hf system page](https://data.orchid-project.org/systems/BE-HF.html) · [Markdown](https://data.orchid-project.org/phases/pages/BE-HF.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Be–Hf system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-be-hf-bcc-a2); _phase:be-hf:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1526.98–3999.73 K, x(Hf) 0–1 | 0 | 1 |
| [BE17HF2](#phase-be-hf-be17hf2); _phase:be-hf:be17hf2_ | Th2Zn17 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2174.33 K, x(Hf) 0.10526–0.10526 | 0 | 1 |
| [BE2HF_C32](#phase-be-hf-be2hf-c32); _phase:be-hf:be2hf-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1639.58 K, x(Hf) 0.33333–0.33333 | 0 | 1 |
| [BE5HF_D2D](#phase-be-hf-be5hf-d2d); _phase:be-hf:be5hf-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1885.74 K, x(Hf) 0.16667–0.16667 | 0 | 1 |
| [FCC_A1](#phase-be-hf-fcc-a1); _phase:be-hf:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-be-hf-hcp-a3); _phase:be-hf:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2016.02 K, x(Hf) 0–1 | 0 | 1 |
| [LIQUID](#phase-be-hf-liquid); _phase:be-hf:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1415.02–4000 K, x(Hf) 0–1 | 0 | 1 |

## BCC_A2 (Be–Hf)

- Id: `phase:be-hf:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1526.98–3999.73 K, x(Hf) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-hf:bcc-a2)

Names (2): _corpus: _corpus:phase:be-hf:bcc-a2  
_tdb: _tdb:BeHf-85Sau.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BeHf-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeHf-85Sau.tdb): BCC_A2, type code %B, sha256 `0c6236a0a4eadf3c…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BE% HF% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## BE17HF2 (Be–Hf)

- Id: `phase:be-hf:be17hf2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Be 0.8947, Hf 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 300–2174.33 K, x(Hf) 0.10526–0.10526
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-hf:be17hf2)

Names (2): _corpus: _corpus:phase:be-hf:be17hf2  
_tdb: _tdb:BeHf-85Sau.tdb:BE17HF2  


### TDB models of BE17HF2 (1): PHASE and CONSTITUENT statements as written

[BeHf-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeHf-85Sau.tdb): BE17HF2, type code %, sha256 `0c6236a0a4eadf3c…`

~~~~text
41: PHASE BE17HF2 % 2 17 2 !
42: CONST BE17HF2 : BE : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## BE2HF_C32 (Be–Hf)

- Id: `phase:be-hf:be2hf-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Be 0.6667, Hf 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1639.58 K, x(Hf) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-hf:be2hf-c32)

Names (2): _corpus: _corpus:phase:be-hf:be2hf-c32  
_tdb: _tdb:BeHf-85Sau.tdb:BE2HF_C32  


### TDB models of BE2HF_C32 (1): PHASE and CONSTITUENT statements as written

[BeHf-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeHf-85Sau.tdb): BE2HF_C32, type code %, sha256 `0c6236a0a4eadf3c…`

~~~~text
51: PHASE BE2HF_C32 % 2 2 1 !
52: CONST BE2HF_C32 : BE : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## BE5HF_D2D (Be–Hf)

- Id: `phase:be-hf:be5hf-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaczx and oqmd-10884, space group 191
- Stoichiometry: Be 0.8333, Hf 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1885.74 K, x(Hf) 0.16667–0.16667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-hf:be5hf-d2d)

Names (4): _corpus: _corpus:phase:be-hf:be5hf-d2d  
_mp: _mp:mp-aaaaaczx  
_oqmd: _oqmd:oqmd-10884  
_tdb: _tdb:BeHf-85Sau.tdb:BE5HF_D2D  


### TDB models of BE5HF_D2D (1): PHASE and CONSTITUENT statements as written

[BeHf-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeHf-85Sau.tdb): BE5HF_D2D, type code %, sha256 `0c6236a0a4eadf3c…`

~~~~text
46: PHASE BE5HF_D2D % 2 5 1 !
47: CONST BE5HF_D2D : BE : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## FCC_A1 (Be–Hf)

- Id: `phase:be-hf:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-hf:fcc-a1)

Names (2): _corpus: _corpus:phase:be-hf:fcc-a1  
_tdb: _tdb:BeHf-85Sau.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BeHf-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeHf-85Sau.tdb): FCC_A1, type code %A, sha256 `0c6236a0a4eadf3c…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BE HF : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## HCP_A3 (Be–Hf)

- Id: `phase:be-hf:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2016.02 K, x(Hf) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-hf:hcp-a3)

Names (2): _corpus: _corpus:phase:be-hf:hcp-a3  
_tdb: _tdb:BeHf-85Sau.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BeHf-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeHf-85Sau.tdb): HCP_A3, type code %A, sha256 `0c6236a0a4eadf3c…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BE% HF% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## LIQUID (Be–Hf)

- Id: `phase:be-hf:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1415.02–4000 K, x(Hf) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-hf:liquid)

Names (2): _corpus: _corpus:phase:be-hf:liquid  
_tdb: _tdb:BeHf-85Sau.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BeHf-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeHf-85Sau.tdb): LIQUID, type code %, sha256 `0c6236a0a4eadf3c…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BE HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
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
