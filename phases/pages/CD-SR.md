# Cd–Sr phases

> Cd–Sr system: 10 phases (tier A 5, tier B 1, tier C 3, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-SR.html · Markdown: https://data.orchid-project.org/phases/pages/CD-SR.md

10 phases (tier A 5, tier B 1, tier C 3, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-SR) · [full JSON](https://data.orchid-project.org/phases/systems/CD-SR.json) · [Cd–Sr system page](https://data.orchid-project.org/systems/CD-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Sr system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-sr-bcc-a2); _phase:cd-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 820.12–2500 K, x(Sr) 0.99985–1 | 0 | 1 |
| [CD11SR](#phase-cd-sr-cd11sr); _phase:cd-sr:cd11sr_ | BaCd11 · tI48 · I4_1/amd (141) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–804.01 K, x(Sr) 0.08333–0.08333 | 0 | 1 |
| [CD2SR](#phase-cd-sr-cd2sr); _phase:cd-sr:cd2sr_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1004.07 K, x(Sr) 0.33333–0.33333 | 0 | 1 |
| [CD3SR5_D8L](#phase-cd-sr-cd3sr5-d8l); _phase:cd-sr:cd3sr5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–702.76 K, x(Sr) 0.625–0.625 | 0 | 1 |
| [CD58SR13](#phase-cd-sr-cd58sr13); _phase:cd-sr:cd58sr13_ | Gd13Zn58 · hP142 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–899.32 K, x(Sr) 0.1831–0.1831 | 0 | 1 |
| [CD6SR](#phase-cd-sr-cd6sr); _phase:cd-sr:cd6sr_ | Cd6Y · cI184 · Im-3 (204) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–871.15 K, x(Sr) 0.14286–0.14286 | 0 | 1 |
| [CDSR_B2](#phase-cd-sr-cdsr-b2); _phase:cd-sr:cdsr-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–848.63 K, x(Sr) 0.5–0.5 | 0 | 1 |
| [FCC_A1](#phase-cd-sr-fcc-a1); _phase:cd-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–820.12 K, x(Sr) 0.99985–1 | 0 | 1 |
| [HCP_A3](#phase-cd-sr-hcp-a3); _phase:cd-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–600.76 K, x(Sr) 0–0 | 0 | 1 |
| [LIQUID](#phase-cd-sr-liquid); _phase:cd-sr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 591.76–2500 K, x(Sr) 0–1 | 2 | 1 |

## BCC_A2 (Cd–Sr)

- Id: `phase:cd-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 820.12–2500 K, x(Sr) 0.99985–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-sr:bcc-a2  
_tdb: _tdb:CdSr-13Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): BCC_A2, type code %B, sha256 `f024ca7b33eda1c2…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CD SR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## CD11SR (Cd–Sr)

- Id: `phase:cd-sr:cd11sr`; status `assigned`
- Structure: BaCd11 · tI48 · I4_1/amd (141); type `st:bacd11-ti48`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cd 0.9167, Sr 0.0833
- Stability: stable in 1 of 1 calculated diagram(s): 300–804.01 K, x(Sr) 0.08333–0.08333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:cd11sr)

Names (4): _corpus: _corpus:phase:cd-sr:cd11sr  
_mp: _mp:mp-aaabgldi  
_oqmd: _oqmd:oqmd-19300  
_tdb: _tdb:CdSr-13Zha.tdb:CD11SR  


### TDB models of CD11SR (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): CD11SR, type code %, sha256 `f024ca7b33eda1c2…`

~~~~text
41: PHASE CD11SR % 2 11 1 !
42: CONST CD11SR : CD : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## CD2SR (Cd–Sr)

- Id: `phase:cd-sr:cd2sr`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.6667, Sr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1004.07 K, x(Sr) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:cd2sr)

Names (2): _corpus: _corpus:phase:cd-sr:cd2sr  
_tdb: _tdb:CdSr-13Zha.tdb:CD2SR  


### TDB models of CD2SR (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): CD2SR, type code %, sha256 `f024ca7b33eda1c2…`

~~~~text
56: PHASE CD2SR % 2 2 1 !
57: CONST CD2SR : CD : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## CD3SR5_D8L (Cd–Sr)

- Id: `phase:cd-sr:cd3sr5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.3750, Sr 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–702.76 K, x(Sr) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:cd3sr5-d8l)

Names (2): _corpus: _corpus:phase:cd-sr:cd3sr5-d8l  
_tdb: _tdb:CdSr-13Zha.tdb:CD3SR5_D8L  


### TDB models of CD3SR5_D8L (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): CD3SR5_D8L, type code %, sha256 `f024ca7b33eda1c2…`

~~~~text
66: PHASE CD3SR5_D8L % 2 3 5 !
67: CONST CD3SR5_D8L : CD : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## CD58SR13 (Cd–Sr)

- Id: `phase:cd-sr:cd58sr13`; status `assigned`
- Structure: Gd13Zn58 · hP142 · P6_3/mmc (194); type `st:gd13zn58-hp142`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.8169, Sr 0.1831
- Stability: stable in 1 of 1 calculated diagram(s): 300–899.32 K, x(Sr) 0.1831–0.1831
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:cd58sr13)

Names (2): _corpus: _corpus:phase:cd-sr:cd58sr13  
_tdb: _tdb:CdSr-13Zha.tdb:CD58SR13  


### TDB models of CD58SR13 (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): CD58SR13, type code %, sha256 `f024ca7b33eda1c2…`

~~~~text
51: PHASE CD58SR13 % 2 58 13 !
52: CONST CD58SR13 : CD : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## CD6SR (Cd–Sr)

- Id: `phase:cd-sr:cd6sr`; status `assigned`
- Structure: Cd6Y · cI184 · Im-3 (204); type `st:cd6y-ci184`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.8571, Sr 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–871.15 K, x(Sr) 0.14286–0.14286
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:cd6sr)

Names (2): _corpus: _corpus:phase:cd-sr:cd6sr  
_tdb: _tdb:CdSr-13Zha.tdb:CD6SR  


### TDB models of CD6SR (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): CD6SR, type code %, sha256 `f024ca7b33eda1c2…`

~~~~text
46: PHASE CD6SR % 2 6 1 !
47: CONST CD6SR : CD : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## CDSR_B2 (Cd–Sr)

- Id: `phase:cd-sr:cdsr-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtcy and oqmd-17067, space group 221
- Stoichiometry: Cd 0.5000, Sr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–848.63 K, x(Sr) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:cdsr-b2)

Names (4): _corpus: _corpus:phase:cd-sr:cdsr-b2  
_mp: _mp:mp-aaaabtcy  
_oqmd: _oqmd:oqmd-17067  
_tdb: _tdb:CdSr-13Zha.tdb:CDSR_B2  


### TDB models of CDSR_B2 (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): CDSR_B2, type code %, sha256 `f024ca7b33eda1c2…`

~~~~text
61: PHASE CDSR_B2 % 2 1 1 !
62: CONST CDSR_B2 : CD : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## FCC_A1 (Cd–Sr)

- Id: `phase:cd-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–820.12 K, x(Sr) 0.99985–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-sr:fcc-a1  
_tdb: _tdb:CdSr-13Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): FCC_A1, type code %A, sha256 `f024ca7b33eda1c2…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CD SR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## HCP_A3 (Cd–Sr)

- Id: `phase:cd-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–600.76 K, x(Sr) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:hcp-a3)

Names (2): _corpus: _corpus:phase:cd-sr:hcp-a3  
_tdb: _tdb:CdSr-13Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): HCP_A3, type code %A, sha256 `f024ca7b33eda1c2…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CD% SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## LIQUID (Cd–Sr)

- Id: `phase:cd-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 591.76–2500 K, x(Sr) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sr:liquid)

Names (3): _corpus: _corpus:phase:cd-sr:liquid  
_paper: _paper:10.1016/j.calphad.2013.06.005:Liquid  
_tdb: _tdb:CdSr-13Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdSr-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSr-13Zha.tdb): LIQUID, type code %, sha256 `f024ca7b33eda1c2…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CD SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
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
