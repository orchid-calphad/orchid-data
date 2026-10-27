# Bi–Tb phases

> Bi–Tb system: 9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-TB.html · Markdown: https://data.orchid-project.org/phases/pages/BI-TB.md

9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-TB) · [full JSON](https://data.orchid-project.org/phases/systems/BI-TB.json) · [Bi–Tb system page](https://data.orchid-project.org/systems/BI-TB.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-TB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Tb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-tb-a7-rhombohedral); _phase:bi-tb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Tb) 0–0 | 2 | 1 |
| [BCC_A2](#phase-bi-tb-bcc-a2); _phase:bi-tb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1539.58–1967 K, x(Tb) 0.99051–1 | 2 | 1 |
| [BI3TB4_D73](#phase-bi-tb-bi3tb4-d73); _phase:bi-tb:bi3tb4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1876.41 K, x(Tb) 0.57143–0.57143 | 4 | 1 |
| [BI3TB5_LT](#phase-bi-tb-bi3tb5); _phase:bi-tb:bi3tb5_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 316.83–1682.24 K, x(Tb) 0.625–0.625 | 4 | 1 |
| [BI3TB5_D88](#phase-bi-tb-bi3tb5-d88); _phase:bi-tb:bi3tb5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1682.24–1758.85 K, x(Tb) 0.625–0.625 | 4 | 1 |
| [BITB_B1](#phase-bi-tb-bitb-b1); _phase:bi-tb:bitb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2032.88 K, x(Tb) 0.5–0.5 | 6 | 1 |
| [FCC_A1](#phase-bi-tb-fcc-a1); _phase:bi-tb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-tb-hcp-a3); _phase:bi-tb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1562 K, x(Tb) 0.99235–1 | 4 | 1 |
| [LIQUID](#phase-bi-tb-liquid); _phase:bi-tb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 543.42–2500 K, x(Tb) 0–1 | 12 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Tb)

- Id: `phase:bi-tb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Tb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:bi-tb:a7-rhombohedral  
_paper: _paper:10.1007/s11669-011-9939-1:(Bi)  
_tdb: _tdb:BiTb-11Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `86634d657f268f1a…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI% TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Bi–Tb)

- Id: `phase:bi-tb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1539.58–1967 K, x(Tb) 0.99051–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:bcc-a2)

Names (3): _corpus: _corpus:phase:bi-tb:bcc-a2  
_paper: _paper:10.1007/s11669-011-9939-1:βTb  
_tdb: _tdb:BiTb-11Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): BCC_A2, type code %B, sha256 `86634d657f268f1a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI TB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_

## BI3TB4_D73 (Bi–Tb)

- Id: `phase:bi-tb:bi3tb4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.4286, Tb 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1876.41 K, x(Tb) 0.57143–0.57143
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:bi3tb4-d73)

Names (3): _corpus: _corpus:phase:bi-tb:bi3tb4-d73  
_paper: _paper:10.1007/s11669-011-9939-1:Bi3Tb4  
_tdb: _tdb:BiTb-11Wan.tdb:BI3TB4_D73  


### TDB models of BI3TB4_D73 (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): BI3TB4_D73, type code %, sha256 `86634d657f268f1a…`

~~~~text
55: PHASE BI3TB4_D73 % 2 3 4 !
56: CONST BI3TB4_D73 : BI : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_

## BI3TB5_LT (Bi–Tb)

- Id: `phase:bi-tb:bi3tb5`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Tb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 316.83–1682.24 K, x(Tb) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:bi3tb5)

Names (3): _corpus: _corpus:phase:bi-tb:bi3tb5  
_paper: _paper:10.1007/s11669-011-9939-1:αBi3Tb5  
_tdb: _tdb:BiTb-11Wan.tdb:BI3TB5_LT  


### TDB models of BI3TB5_LT (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): BI3TB5_LT, type code %, sha256 `86634d657f268f1a…`

~~~~text
60: PHASE BI3TB5_LT % 2 3 5 !
61: CONST BI3TB5_LT : BI : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_

## BI3TB5_D88 (Bi–Tb)

- Id: `phase:bi-tb:bi3tb5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.3750, Tb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1682.24–1758.85 K, x(Tb) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:bi3tb5-d88)

Names (3): _corpus: _corpus:phase:bi-tb:bi3tb5-d88  
_paper: _paper:10.1007/s11669-011-9939-1:βBi3Tb5  
_tdb: _tdb:BiTb-11Wan.tdb:BI3TB5_D88  


### TDB models of BI3TB5_D88 (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): BI3TB5_D88, type code %, sha256 `86634d657f268f1a…`

~~~~text
65: PHASE BI3TB5_D88 % 2 3 5 !
66: CONST BI3TB5_D88 : BI : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_

## BITB_B1 (Bi–Tb)

- Id: `phase:bi-tb:bitb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Tb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2032.88 K, x(Tb) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:bitb-b1)

Names (3): _corpus: _corpus:phase:bi-tb:bitb-b1  
_paper: _paper:10.1007/s11669-011-9939-1:BiTb  
_tdb: _tdb:BiTb-11Wan.tdb:BITB_B1  


### TDB models of BITB_B1 (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): BITB_B1, type code %, sha256 `86634d657f268f1a…`

~~~~text
50: PHASE BITB_B1 % 2 1 1 !
51: CONST BITB_B1 : BI : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Bi–Tb)

- Id: `phase:bi-tb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-tb:fcc-a1  
_tdb: _tdb:BiTb-11Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): FCC_A1, type code %A, sha256 `86634d657f268f1a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase_

## HCP_A3 (Bi–Tb)

- Id: `phase:bi-tb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1562 K, x(Tb) 0.99235–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-tb:hcp-a3  
_paper: _paper:10.1007/s11669-011-9939-1:αTb  
_tdb: _tdb:BiTb-11Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): HCP_A3, type code %A, sha256 `86634d657f268f1a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI TB% : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Bi–Tb)

- Id: `phase:bi-tb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 543.42–2500 K, x(Tb) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tb:liquid)

Names (3): _corpus: _corpus:phase:bi-tb:liquid  
_paper: _paper:10.1007/s11669-011-9939-1:L  
_tdb: _tdb:BiTb-11Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiTb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTb-11Wan.tdb): LIQUID, type code %, sha256 `86634d657f268f1a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
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
