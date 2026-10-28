# Ag–Ba phases

> Ag–Ba system: 8 phases (tier A 4, tier B 1, tier C 2, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-BA.html · Markdown: https://data.orchid-project.org/phases/pages/AG-BA.md

8 phases (tier A 4, tier B 1, tier C 2, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-BA) · [full JSON](https://data.orchid-project.org/phases/systems/AG-BA.json) · [Ag–Ba system page](https://data.orchid-project.org/systems/AG-BA.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-BA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ba system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2BA](#phase-ag-ba-ag2ba); _phase:ag-ba:ag2ba_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1031.88 K, x(Ba) 0.33333–0.33333 | 0 | 1 |
| [AG2BA3](#phase-ag-ba-ag2ba3); _phase:ag-ba:ag2ba3_ | Er3Ni2 · hR15 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–635.83 K, x(Ba) 0.6–0.6 | 0 | 1 |
| [AG5BA](#phase-ag-ba-ag5ba); _phase:ag-ba:ag5ba_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–981.48 K, x(Ba) 0.16667–0.16667 | 0 | 1 |
| [AGBA_B27](#phase-ag-ba-agba-b27); _phase:ag-ba:agba-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–837.61 K, x(Ba) 0.5–0.5 | 0 | 1 |
| [BCC_A2](#phase-ag-ba-bcc-a2); _phase:ag-ba:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Ba) 0.99936–1 | 0 | 1 |
| [FCC_A1](#phase-ag-ba-fcc-a1); _phase:ag-ba:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1267.02 K, x(Ba) 0–0.00017 | 0 | 1 |
| [HCP_A3](#phase-ag-ba-hcp-a3); _phase:ag-ba:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-ba-liquid); _phase:ag-ba:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 604.93–2500 K, x(Ba) 0–1 | 0 | 1 |

## AG2BA (Ag–Ba)

- Id: `phase:ag-ba:ag2ba`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.6667, Ba 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1031.88 K, x(Ba) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:ag2ba)

Names (2): _corpus: _corpus:phase:ag-ba:ag2ba  
_tdb: _tdb:AgBa-95Che-LB.tdb:AG2BA  


### TDB models of AG2BA (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): AG2BA, type code %, sha256 `d537feedfa4ddf97…`

~~~~text
51: PHASE AG2BA % 2 2 1 !
52: CONST AG2BA : AG : BA : !
~~~~

## AG2BA3 (Ag–Ba)

- Id: `phase:ag-ba:ag2ba3`; status `assigned`
- Structure: Er3Ni2 · hR15 · R-3 (148); type `st:er3ni2-hr15`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.4000, Ba 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–635.83 K, x(Ba) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:ag2ba3)

Names (2): _corpus: _corpus:phase:ag-ba:ag2ba3  
_tdb: _tdb:AgBa-95Che-LB.tdb:AG2BA3  


### TDB models of AG2BA3 (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): AG2BA3, type code %, sha256 `d537feedfa4ddf97…`

~~~~text
61: PHASE AG2BA3 % 2 2 3 !
62: CONST AG2BA3 : AG : BA : !
~~~~

## AG5BA (Ag–Ba)

- Id: `phase:ag-ba:ag5ba`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ag 0.8333, Ba 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–981.48 K, x(Ba) 0.16667–0.16667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:ag5ba)

Names (4): _corpus: _corpus:phase:ag-ba:ag5ba  
_mp: _mp:mp-aaaaacru  
_oqmd: _oqmd:oqmd-10352  
_tdb: _tdb:AgBa-95Che-LB.tdb:AG5BA  


### TDB models of AG5BA (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): AG5BA, type code %, sha256 `d537feedfa4ddf97…`

~~~~text
46: PHASE AG5BA % 2 5 1 !
47: CONST AG5BA : AG : BA : !
~~~~

## AGBA_B27 (Ag–Ba)

- Id: `phase:ag-ba:agba-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaarnk and oqmd-10350, space group 62
- Stoichiometry: Ag 0.5000, Ba 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–837.61 K, x(Ba) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:agba-b27)

Names (4): _corpus: _corpus:phase:ag-ba:agba-b27  
_mp: _mp:mp-aaaaarnk  
_oqmd: _oqmd:oqmd-10350  
_tdb: _tdb:AgBa-95Che-LB.tdb:AGBA_B27  


### TDB models of AGBA_B27 (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): AGBA_B27, type code %, sha256 `d537feedfa4ddf97…`

~~~~text
56: PHASE AGBA_B27 % 2 1 1 !
57: CONST AGBA_B27 : AG : BA : !
~~~~

## BCC_A2 (Ag–Ba)

- Id: `phase:ag-ba:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Ba) 0.99936–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-ba:bcc-a2  
_tdb: _tdb:AgBa-95Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): BCC_A2, type code %B, sha256 `d537feedfa4ddf97…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG BA% : VA : !
~~~~

## FCC_A1 (Ag–Ba)

- Id: `phase:ag-ba:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1267.02 K, x(Ba) 0–0.00017
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:fcc-a1)

Names (2): _corpus: _corpus:phase:ag-ba:fcc-a1  
_tdb: _tdb:AgBa-95Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): FCC_A1, type code %A, sha256 `d537feedfa4ddf97…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% BA : VA : !
~~~~

## HCP_A3 (Ag–Ba)

- Id: `phase:ag-ba:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-ba:hcp-a3  
_tdb: _tdb:AgBa-95Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): HCP_A3, type code %A, sha256 `d537feedfa4ddf97…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG BA : VA : !
~~~~

## LIQUID (Ag–Ba)

- Id: `phase:ag-ba:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 604.93–2500 K, x(Ba) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ba:liquid)

Names (2): _corpus: _corpus:phase:ag-ba:liquid  
_tdb: _tdb:AgBa-95Che-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgBa-95Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBa-95Che-LB.tdb): LIQUID, type code %, sha256 `d537feedfa4ddf97…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG BA : !
~~~~

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
