# Cl–K phases

> Cl–K system: 7 phases (tier A 4, liquid 2, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CL-K.html · Markdown: https://data.orchid-project.org/phases/pages/CL-K.md

7 phases (tier A 4, liquid 2, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CL-K) · [full JSON](https://data.orchid-project.org/phases/systems/CL-K.json) · [Markdown](https://data.orchid-project.org/phases/pages/CL-K.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cl–K system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cl-k-bcc-a2); _phase:cl-k:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(Cl) 0–0 | 0 | 1 |
| [FCC_A1](#phase-cl-k-fcc-a1); _phase:cl-k:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-cl-k-gas); _phase:cl-k:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Cl) 0–1 | 0 | 1 |
| [HCP_A3](#phase-cl-k-hcp-a3); _phase:cl-k:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-cl-k-ion); _phase:cl-k:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 336.53–1753.47 K, x(Cl) 0–0.5 | 0 | 1 |
| [KCL_B1](#phase-cl-k-kcl-b1); _phase:cl-k:kcl-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1044 K, x(Cl) 0.5–0.5 | 0 | 1 |
| [LIQUID](#phase-cl-k-liquid); _phase:cl-k:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 336.53–1753.19 K, x(Cl) 0–0.5 | 0 | 1 |

## BCC_A2 (Cl–K)

- Id: `phase:cl-k:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: K 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(Cl) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cl-k:bcc-a2)

Names (2): _corpus: _corpus:phase:cl-k:bcc-a2  
_tdb: _tdb:KCl-18McM.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[KCl-18McM.tdb](https://orchid-project.org/data/databases/sgte-binary/KCl-18McM.tdb): BCC_A2, type code %B, sha256 `baf0bbe77634fedb…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2018.06.013](https://doi.org/10.1016/j.solener.2018.06.013) J.W. McMurray, S.S. Raiman, Solar Energy, 170, 1039-42(2018).  
_assessment that models this phase_

## FCC_A1 (Cl–K)

- Id: `phase:cl-k:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: K 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cl-k:fcc-a1)

Names (2): _corpus: _corpus:phase:cl-k:fcc-a1  
_tdb: _tdb:KCl-18McM.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[KCl-18McM.tdb](https://orchid-project.org/data/databases/sgte-binary/KCl-18McM.tdb): FCC_A1, type code %A, sha256 `baf0bbe77634fedb…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2018.06.013](https://doi.org/10.1016/j.solener.2018.06.013) J.W. McMurray, S.S. Raiman, Solar Energy, 170, 1039-42(2018).  
_assessment that models this phase_

## GAS (Cl–K)

- Id: `phase:cl-k:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Cl) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cl-k:gas)

Names (2): _corpus: _corpus:phase:cl-k:gas  
_tdb: _tdb:KCl-18McM.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[KCl-18McM.tdb](https://orchid-project.org/data/databases/sgte-binary/KCl-18McM.tdb): GAS, type code %, sha256 `baf0bbe77634fedb…`

~~~~text
61: PHASE GAS:G % 1 1 !
62: CONST GAS:G : CL CL2 K K2 KCL K2CL2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2018.06.013](https://doi.org/10.1016/j.solener.2018.06.013) J.W. McMurray, S.S. Raiman, Solar Energy, 170, 1039-42(2018).  
_assessment that models this phase_

## HCP_A3 (Cl–K)

- Id: `phase:cl-k:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: K 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cl-k:hcp-a3)

Names (2): _corpus: _corpus:phase:cl-k:hcp-a3  
_tdb: _tdb:KCl-18McM.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[KCl-18McM.tdb](https://orchid-project.org/data/databases/sgte-binary/KCl-18McM.tdb): HCP_A3, type code %A, sha256 `baf0bbe77634fedb…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2018.06.013](https://doi.org/10.1016/j.solener.2018.06.013) J.W. McMurray, S.S. Raiman, Solar Energy, 170, 1039-42(2018).  
_assessment that models this phase_

## ION (Cl–K)

- Id: `phase:cl-k:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 336.53–1753.47 K, x(Cl) 0–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cl-k:ion)

Names (2): _corpus: _corpus:phase:cl-k:ion  
_tdb: _tdb:KCl-18McM.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[KCl-18McM.tdb](https://orchid-project.org/data/databases/sgte-binary/KCl-18McM.tdb): ION, type code %, sha256 `baf0bbe77634fedb…`

~~~~text
35: PHASE ION:Y % 2 1 1 !
36: CONST ION:Y : K+1 : CL-1 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2018.06.013](https://doi.org/10.1016/j.solener.2018.06.013) J.W. McMurray, S.S. Raiman, Solar Energy, 170, 1039-42(2018).  
_assessment that models this phase_

## KCL_B1 (Cl–K)

- Id: `phase:cl-k:kcl-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Cl 0.5000, K 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1044 K, x(Cl) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cl-k:kcl-b1)

Names (2): _corpus: _corpus:phase:cl-k:kcl-b1  
_tdb: _tdb:KCl-18McM.tdb:KCL_B1  


### TDB models of KCL_B1 (1): PHASE and CONSTITUENT statements as written

[KCl-18McM.tdb](https://orchid-project.org/data/databases/sgte-binary/KCl-18McM.tdb): KCL_B1, type code %, sha256 `baf0bbe77634fedb…`

~~~~text
58: PHASE KCL_B1 % 2 1 1 !
59: CONST KCL_B1 : K : CL : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2018.06.013](https://doi.org/10.1016/j.solener.2018.06.013) J.W. McMurray, S.S. Raiman, Solar Energy, 170, 1039-42(2018).  
_assessment that models this phase_

## LIQUID (Cl–K)

- Id: `phase:cl-k:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 336.53–1753.19 K, x(Cl) 0–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cl-k:liquid)

Names (2): _corpus: _corpus:phase:cl-k:liquid  
_tdb: _tdb:KCl-18McM.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[KCl-18McM.tdb](https://orchid-project.org/data/databases/sgte-binary/KCl-18McM.tdb): LIQUID, type code %, sha256 `baf0bbe77634fedb…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : K KCL : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2018.06.013](https://doi.org/10.1016/j.solener.2018.06.013) J.W. McMurray, S.S. Raiman, Solar Energy, 170, 1039-42(2018).  
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
