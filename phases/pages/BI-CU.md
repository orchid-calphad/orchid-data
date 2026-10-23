# Bi–Cu phases

> Bi–Cu system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-CU.html · Markdown: https://data.orchid-project.org/phases/pages/BI-CU.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-CU) · [full JSON](https://data.orchid-project.org/phases/systems/BI-CU.json) · [Bi–Cu system page](https://data.orchid-project.org/systems/BI-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Cu system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-cu-a7-rhombohedral); _phase:bi-cu:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Cu) 0–0 | 0 | 2 |
| [BCC_A2](#phase-bi-cu-bcc-a2); _phase:bi-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-bi-cu-fcc-a1); _phase:bi-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.52 K, x(Cu) 0.99875–1 | 0 | 2 |
| [HCP_A3](#phase-bi-cu-hcp-a3); _phase:bi-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-bi-cu-liquid); _phase:bi-cu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 543.66–2500 K, x(Cu) 0–1 | 3 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Cu)

- Id: `phase:bi-cu:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Cu) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cu:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:bi-cu:a7-rhombohedral  
_tdb: _tdb:BiCu-89Tep-LB.tdb:RHOMBOHEDRAL_A7, tdb:BiCu-90Tep.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiCu-89Tep-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-89Tep-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `f9abbe5e46364f6c…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiCu-90Tep.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-90Tep.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `ee69358a29e6f6d1…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(90)80598-S](https://doi.org/10.1016/0040-6031%2890%2980598-S) O. Teppo, J. Niemela, P. Taskinen, Thermochim. Acta, 173, 137-50 (1990)  
_assessment that models this phase_

## BCC_A2 (Bi–Cu)

- Id: `phase:bi-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cu:bcc-a2)

Names (3): _corpus: _corpus:phase:bi-cu:bcc-a2  
_tdb: _tdb:BiCu-89Tep-LB.tdb:BCC_A2, tdb:BiCu-90Tep.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiCu-89Tep-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-89Tep-LB.tdb): BCC_A2, type code %, sha256 `f9abbe5e46364f6c…`

~~~~text
38: PHASE BCC_A2 % 2 1 3 !
39: CONST BCC_A2 : BI CU : VA : !
~~~~

[BiCu-90Tep.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-90Tep.tdb): BCC_A2, type code %B, sha256 `ee69358a29e6f6d1…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : BI CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(90)80598-S](https://doi.org/10.1016/0040-6031%2890%2980598-S) O. Teppo, J. Niemela, P. Taskinen, Thermochim. Acta, 173, 137-50 (1990)  
_assessment that models this phase_

## FCC_A1 (Bi–Cu)

- Id: `phase:bi-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.52 K, x(Cu) 0.99875–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cu:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-cu:fcc-a1  
_tdb: _tdb:BiCu-89Tep-LB.tdb:FCC_A1, tdb:BiCu-90Tep.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiCu-89Tep-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-89Tep-LB.tdb): FCC_A1, type code %, sha256 `f9abbe5e46364f6c…`

~~~~text
33: PHASE FCC_A1 % 2 1 1 !
34: CONST FCC_A1 : BI CU% : VA : !
~~~~

[BiCu-90Tep.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-90Tep.tdb): FCC_A1, type code %A, sha256 `ee69358a29e6f6d1…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : BI CU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(90)80598-S](https://doi.org/10.1016/0040-6031%2890%2980598-S) O. Teppo, J. Niemela, P. Taskinen, Thermochim. Acta, 173, 137-50 (1990)  
_assessment that models this phase_

## HCP_A3 (Bi–Cu)

- Id: `phase:bi-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-cu:hcp-a3  
_tdb: _tdb:BiCu-89Tep-LB.tdb:HCP_A3, tdb:BiCu-90Tep.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiCu-89Tep-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-89Tep-LB.tdb): HCP_A3, type code %, sha256 `f9abbe5e46364f6c…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : BI CU : VA: !
~~~~

[BiCu-90Tep.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-90Tep.tdb): HCP_A3, type code %A, sha256 `ee69358a29e6f6d1…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : BI CU : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(90)80598-S](https://doi.org/10.1016/0040-6031%2890%2980598-S) O. Teppo, J. Niemela, P. Taskinen, Thermochim. Acta, 173, 137-50 (1990)  
_assessment that models this phase_

## LIQUID (Bi–Cu)

- Id: `phase:bi-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 543.66–2500 K, x(Cu) 0–1
- Literature: 3 values (0 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cu:liquid)

Names (4): _corpus: _corpus:phase:bi-cu:liquid  
_paper: _paper:10.1002/crat.200800391:liquid  
_tdb: _tdb:BiCu-89Tep-LB.tdb:LIQUID, tdb:BiCu-90Tep.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiCu-89Tep-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-89Tep-LB.tdb): LIQUID, type code %, sha256 `f9abbe5e46364f6c…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : BI CU : !
~~~~

[BiCu-90Tep.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCu-90Tep.tdb): LIQUID, type code %, sha256 `ee69358a29e6f6d1…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : BI CU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0040-6031(90)80598-S](https://doi.org/10.1016/0040-6031%2890%2980598-S) O. Teppo, J. Niemela, P. Taskinen, Thermochim. Acta, 173, 137-50 (1990)  
_assessment that models this phase_
- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_reports values for this phase_

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
