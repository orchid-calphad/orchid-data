# As–Si phases

> As–Si system: 8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-SI.html · Markdown: https://data.orchid-project.org/phases/pages/AS-SI.md

8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-SI) · [full JSON](https://data.orchid-project.org/phases/systems/AS-SI.json) · [Markdown](https://data.orchid-project.org/phases/pages/AS-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–Si system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-as-si-a4-diamond); _phase:as-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1687 K, x(As) 0–0.05886 | 0 | 1 |
| [RHOMBOHEDRAL_A7](#phase-as-si-a7-rhombohedral); _phase:as-si:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1090 K, x(As) 1–1 | 0 | 1 |
| [BCC_A2](#phase-as-si-bcc-a2); _phase:as-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-as-si-fcc-a1); _phase:as-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-as-si-hcp-a3); _phase:as-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-as-si-liquid); _phase:as-si:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1073.46–2500 K, x(As) 0–1 | 0 | 1 |
| [SIAS](#phase-as-si-sias); _phase:as-si:sias_ | SiAs · mC24 · C2/m (12) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1385.97 K, x(As) 0.5–0.5 | 0 | 1 |
| [SIAS2](#phase-as-si-sias2); _phase:as-si:sias2_ | GeAs2 · oP24 · Pbam (55) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1249.77 K, x(As) 0.66667–0.66667 | 0 | 1 |

## DIAMOND_A4 (As–Si)

- Id: `phase:as-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1687 K, x(As) 0–0.05886
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:a4-diamond)

Names (2): _corpus: _corpus:phase:as-si:a4-diamond  
_tdb: _tdb:SiAs-21Wu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): DIAMOND_A4, type code %, sha256 `227b4fb79ef39210…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : AS SI% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (As–Si)

- Id: `phase:as-si:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1090 K, x(As) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:as-si:a7-rhombohedral  
_tdb: _tdb:SiAs-21Wu.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `227b4fb79ef39210…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## BCC_A2 (As–Si)

- Id: `phase:as-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:bcc-a2)

Names (2): _corpus: _corpus:phase:as-si:bcc-a2  
_tdb: _tdb:SiAs-21Wu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): BCC_A2, type code %B, sha256 `227b4fb79ef39210…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AS SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## FCC_A1 (As–Si)

- Id: `phase:as-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:fcc-a1)

Names (2): _corpus: _corpus:phase:as-si:fcc-a1  
_tdb: _tdb:SiAs-21Wu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): FCC_A1, type code %A, sha256 `227b4fb79ef39210…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AS SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## HCP_A3 (As–Si)

- Id: `phase:as-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:hcp-a3)

Names (2): _corpus: _corpus:phase:as-si:hcp-a3  
_tdb: _tdb:SiAs-21Wu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): HCP_A3, type code %A, sha256 `227b4fb79ef39210…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AS SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## LIQUID (As–Si)

- Id: `phase:as-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1073.46–2500 K, x(As) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:liquid)

Names (2): _corpus: _corpus:phase:as-si:liquid  
_tdb: _tdb:SiAs-21Wu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): LIQUID, type code %, sha256 `227b4fb79ef39210…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AS SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## SIAS (As–Si)

- Id: `phase:as-si:sias`; status `assigned`
- Structure: SiAs · mC24 · C2/m (12); type `st:sias-mc24`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: As 0.5000, Si 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1385.97 K, x(As) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:sias)

Names (4): _corpus: _corpus:phase:as-si:sias  
_mp: _mp:mp-aaaaactr  
_oqmd: _oqmd:oqmd-8010  
_tdb: _tdb:SiAs-21Wu.tdb:SIAS  


### TDB models of SIAS (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): SIAS, type code %, sha256 `227b4fb79ef39210…`

~~~~text
52: PHASE SIAS % 2 1 1 !
53: CONST SIAS : SI : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## SIAS2 (As–Si)

- Id: `phase:as-si:sias2`; status `assigned`
- Structure: GeAs2 · oP24 · Pbam (55); type `st:geas2-op24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_55_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: As 0.6667, Si 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1249.77 K, x(As) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-si:sias2)

Names (2): _corpus: _corpus:phase:as-si:sias2  
_tdb: _tdb:SiAs-21Wu.tdb:SIAS2  


### TDB models of SIAS2 (1): PHASE and CONSTITUENT statements as written

[SiAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/SiAs-21Wu.tdb): SIAS2, type code %, sha256 `227b4fb79ef39210…`

~~~~text
57: PHASE SIAS2 % 2 1 2 !
58: CONST SIAS2 : SI : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
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
