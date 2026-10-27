# Bi–Dy phases

> Bi–Dy system: 7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-DY.html · Markdown: https://data.orchid-project.org/phases/pages/BI-DY.md

7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-DY) · [full JSON](https://data.orchid-project.org/phases/systems/BI-DY.json) · [Bi–Dy system page](https://data.orchid-project.org/systems/BI-DY.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-DY.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Dy system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-dy-a7-rhombohedral); _phase:bi-dy:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Dy) 0–0 | 2 | 1 |
| [BCC_A2](#phase-bi-dy-bcc-a2); _phase:bi-dy:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1654.15–2499.15 K, x(Dy) 1–1 | 0 | 1 |
| [BI3DY5](#phase-bi-dy-bi3dy5); _phase:bi-dy:bi3dy5_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1719.23 K, x(Dy) 0.625–0.625 | 10 | 1 |
| [BIDY_B1](#phase-bi-dy-bidy-b1); _phase:bi-dy:bidy-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2023.03 K, x(Dy) 0.5–0.5 | 6 | 1 |
| [FCC_A1](#phase-bi-dy-fcc-a1); _phase:bi-dy:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-dy-hcp-a3); _phase:bi-dy:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.77 K, x(Dy) 1–1 | 2 | 1 |
| [LIQUID](#phase-bi-dy-liquid); _phase:bi-dy:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 543.54–2500 K, x(Dy) 0–1 | 8 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Dy)

- Id: `phase:bi-dy:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Dy) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-dy:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-dy:a7-rhombohedral, corpus:phase:bi-dy:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2013.05.024:Rhomb_A7 (Bi)  
_tdb: _tdb:BiDy-13Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiDy-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `24b216373fd672e5…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Bi–Dy)

- Id: `phase:bi-dy:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1654.15–2499.15 K, x(Dy) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-dy:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-dy:bcc-a2  
_tdb: _tdb:BiDy-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiDy-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb): BCC_A2, type code %B, sha256 `24b216373fd672e5…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI DY% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase_

## BI3DY5 (Bi–Dy)

- Id: `phase:bi-dy:bi3dy5`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Dy 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1719.23 K, x(Dy) 0.625–0.625
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-dy:bi3dy5)

Names (3): _corpus: _corpus:phase:bi-dy:bi3dy5  
_paper: _paper:10.1016/j.tca.2013.05.024:Bi3Dy5  
_tdb: _tdb:BiDy-13Wan.tdb:BI3DY5  


### TDB models of BI3DY5 (1): PHASE and CONSTITUENT statements as written

[BiDy-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb): BI3DY5, type code %, sha256 `24b216373fd672e5…`

~~~~text
51: PHASE BI3DY5 % 2 3 5 !
52: CONST BI3DY5 : BI : DY : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(01)01009-x](https://doi.org/10.1016/s0925-8388%2801%2901009-x) M Drzyzga, J Szade, Structure and magnetism of R5Bi3 (R=Tb, Dy, Ho, Er) and Tb4Bi3, Journal of Alloys and Compounds 321, 27-34 (2001).  
_cited as the source of values for this phase_

## BIDY_B1 (Bi–Dy)

- Id: `phase:bi-dy:bidy-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Dy 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2023.03 K, x(Dy) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-dy:bidy-b1)

Names (3): _corpus: _corpus:phase:bi-dy:bidy-b1  
_paper: _paper:10.1016/j.tca.2013.05.024:BiDy  
_tdb: _tdb:BiDy-13Wan.tdb:BIDY_B1  


### TDB models of BIDY_B1 (1): PHASE and CONSTITUENT statements as written

[BiDy-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb): BIDY_B1, type code %, sha256 `24b216373fd672e5…`

~~~~text
46: PHASE BIDY_B1 % 2 1 1 !
47: CONST BIDY_B1 : BI : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Bi–Dy)

- Id: `phase:bi-dy:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-dy:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-dy:fcc-a1  
_tdb: _tdb:BiDy-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiDy-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb): FCC_A1, type code %A, sha256 `24b216373fd672e5…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase_

## HCP_A3 (Bi–Dy)

- Id: `phase:bi-dy:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.77 K, x(Dy) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-dy:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-dy:hcp-a3  
_paper: _paper:10.1016/j.tca.2013.05.024:Hcp_A3 (Dy)  
_tdb: _tdb:BiDy-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiDy-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb): HCP_A3, type code %A, sha256 `24b216373fd672e5…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI DY% : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Bi–Dy)

- Id: `phase:bi-dy:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 543.54–2500 K, x(Dy) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-dy:liquid)

Names (3): _corpus: _corpus:phase:bi-dy:liquid  
_paper: _paper:10.1016/j.tca.2013.05.024:L  
_tdb: _tdb:BiDy-13Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiDy-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb): LIQUID, type code %, sha256 `24b216373fd672e5…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_

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
