# Mg–Tb phases

> Mg–Tb system: 9 phases (tier A 6, tier C 2, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-TB.html · Markdown: https://data.orchid-project.org/phases/pages/MG-TB.md

9 phases (tier A 6, tier C 2, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-TB) · [full JSON](https://data.orchid-project.org/phases/systems/MG-TB.json) · [Mg–Tb system page](https://data.orchid-project.org/systems/MG-TB.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-TB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Tb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-tb-bcc-a2); _phase:mg-tb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 4 | 1 |
| [B2_BCC](#phase-mg-tb-bcc-b2); _phase:mg-tb:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.1 K, x(Tb) 0.4723–1 | 6 | 1 |
| [MG3M_D03](#phase-mg-tb-d03-mg3m); _phase:mg-tb:d03-mg3m_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–877.78 K, x(Tb) 0.21023–0.25 | 4 | 1 |
| [FCC_A1](#phase-mg-tb-fcc-a1); _phase:mg-tb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-mg-tb-hcp-a3); _phase:mg-tb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1567.44 K, x(Tb) 0–1 | 4 | 1 |
| [LIQUID](#phase-mg-tb-liquid); _phase:mg-tb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 803.32–2500 K, x(Tb) 0–1 | 12 | 1 |
| [MG24TB5_A12](#phase-mg-tb-mg24tb5-a12); _phase:mg-tb:mg24tb5-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–827.77 K, x(Tb) 0.17241–0.17241 | 4 | 1 |
| [MG2TB_C14](#phase-mg-tb-mg2tb-c14); _phase:mg-tb:mg2tb-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–992.86 K, x(Tb) 0.32045–0.33333 | 4 | 1 |
| [MG5M](#phase-mg-tb-mg5m); _phase:mg-tb:mg5m_ | Cd45Sm11 · cF448 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–817.81 K, x(Tb) 0.16667–0.16667 | 4 | 1 |

## BCC_A2 (Mg–Tb)

- Id: `phase:mg-tb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:bcc-a2)

Names (3): _corpus: _corpus:phase:mg-tb:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2005.11.060:bcc(Tb)  
_tdb: _tdb:MgTb-06Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): BCC_A2, type code %B, sha256 `69acc44761df0f6c…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MG TB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_

## B2_BCC (Mg–Tb)

- Id: `phase:mg-tb:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: MgTb-06Guo.tdb: ordered phase with disordered part BCC_A2 (order/disorder model)
- Caveat: partitioned order/disorder model in MgTb-06Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.1 K, x(Tb) 0.4723–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:bcc-b2)

Names (4): _corpus: _corpus:phase:mg-tb:bcc-b2, corpus:phase:mg-tb:b2-bcc  
_paper: _paper:10.1016/j.jallcom.2005.11.060:MgTb  
_tdb: _tdb:MgTb-06Guo.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): B2_BCC, type code %BO, sha256 `69acc44761df0f6c…`

~~~~text
35: PHASE B2_BCC %BO 3 0.5 0.5 3 !
36: CONST B2_BCC : MG% TB : MG TB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_

## MG3M_D03 (Mg–Tb)

- Id: `phase:mg-tb:d03-mg3m`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MG3M); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–877.78 K, x(Tb) 0.21023–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:d03-mg3m)

Names (4): _corpus: _corpus:phase:mg-tb:d03-mg3m, corpus:phase:mg-tb:mg3m-d03  
_paper: _paper:10.1016/j.jallcom.2005.11.060:Mg3Tb  
_tdb: _tdb:MgTb-06Guo.tdb:MG3M_D03  


### TDB models of MG3M_D03 (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): MG3M_D03, type code %, sha256 `69acc44761df0f6c…`

~~~~text
56: PHASE MG3M_D03 % 2 3 1 !
57: CONST MG3M_D03 : MG : MG TB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Mg–Tb)

- Id: `phase:mg-tb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:fcc-a1)

Names (2): _corpus: _corpus:phase:mg-tb:fcc-a1  
_tdb: _tdb:MgTb-06Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): FCC_A1, type code %A, sha256 `69acc44761df0f6c…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase_

## HCP_A3 (Mg–Tb)

- Id: `phase:mg-tb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1567.44 K, x(Tb) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:hcp-a3)

Names (4): _corpus: _corpus:phase:mg-tb:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2005.11.060:hcp, paper:10.1016/j.jallcom.2005.11.060:hcp(Tb)  
_tdb: _tdb:MgTb-06Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): HCP_A3, type code %A, sha256 `69acc44761df0f6c…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MG TB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Mg–Tb)

- Id: `phase:mg-tb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 803.32–2500 K, x(Tb) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:liquid)

Names (3): _corpus: _corpus:phase:mg-tb:liquid  
_paper: _paper:10.1016/j.jallcom.2005.11.060:liq.  
_tdb: _tdb:MgTb-06Guo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): LIQUID, type code %, sha256 `69acc44761df0f6c…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MG TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_

## MG24TB5_A12 (Mg–Tb)

- Id: `phase:mg-tb:mg24tb5-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.8276, Tb 0.1724
- Stability: stable in 1 of 1 calculated diagram(s): 300–827.77 K, x(Tb) 0.17241–0.17241
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:mg24tb5-a12)

Names (3): _corpus: _corpus:phase:mg-tb:mg24tb5-a12  
_paper: _paper:10.1016/j.jallcom.2005.11.060:Mg24Tb5  
_tdb: _tdb:MgTb-06Guo.tdb:MG24TB5_A12  


### TDB models of MG24TB5_A12 (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): MG24TB5_A12, type code %, sha256 `69acc44761df0f6c…`

~~~~text
51: PHASE MG24TB5_A12 % 2 24 5 !
52: CONST MG24TB5_A12 : MG : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_

## MG2TB_C14 (Mg–Tb)

- Id: `phase:mg-tb:mg2tb-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–992.86 K, x(Tb) 0.32045–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:mg2tb-c14)

Names (3): _corpus: _corpus:phase:mg-tb:mg2tb-c14  
_paper: _paper:10.1016/j.jallcom.2005.11.060:Mg2Tb  
_tdb: _tdb:MgTb-06Guo.tdb:MG2TB_C14  


### TDB models of MG2TB_C14 (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): MG2TB_C14, type code %, sha256 `69acc44761df0f6c…`

~~~~text
61: PHASE MG2TB_C14 % 2 2 1 !
62: CONST MG2TB_C14 : MG : MG TB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_

## MG5M (Mg–Tb)

- Id: `phase:mg-tb:mg5m`; status `assigned`
- Structure: Cd45Sm11 · cF448 · F-43m (216); type `st:cd45sm11-cf448`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MG5M, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.8333, Tb 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–817.81 K, x(Tb) 0.16667–0.16667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tb:mg5m)

Names (3): _corpus: _corpus:phase:mg-tb:mg5m  
_paper: _paper:10.1016/j.jallcom.2005.11.060:Mg5Tb  
_tdb: _tdb:MgTb-06Guo.tdb:MG5M  


### TDB models of MG5M (1): PHASE and CONSTITUENT statements as written

[MgTb-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTb-06Guo.tdb): MG5M, type code %, sha256 `69acc44761df0f6c…`

~~~~text
45: PHASE MG5M % 2 5 1 !
46: CONST MG5M : MG : TB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
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
