# Be–Cu phases

> Be–Cu system: 6 phases (tier A 5, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BE-CU.html · Markdown: https://data.orchid-project.org/phases/pages/BE-CU.md

6 phases (tier A 5, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BE-CU) · [full JSON](https://data.orchid-project.org/phases/systems/BE-CU.json) · [Be–Cu system page](https://data.orchid-project.org/systems/BE-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/BE-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Be–Cu system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-be-cu-bcc-a2); _phase:be-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 894.15–1560.09 K, x(Cu) 0–0.72382 | 19 | 2 |
| [B2_BCC](#phase-be-cu-bcc-b2); _phase:be-cu:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1560.09 K, x(Cu) 0–0.72382 | 11 | 1 |
| [C15_LAVES](#phase-be-cu-c15-laves); _phase:be-cu:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1489.49 K, x(Cu) 0.19343–0.36442 | 12 | 1 |
| [FCC_A1](#phase-be-cu-fcc-a1); _phase:be-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.6 K, x(Cu) 0.85163–1 | 13 | 1 |
| [HCP_A3](#phase-be-cu-hcp-a3); _phase:be-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1540.47 K, x(Cu) 0–0.08532 | 4 | 1 |
| [LIQUID](#phase-be-cu-liquid); _phase:be-cu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1132.1–2500 K, x(Cu) 0–1 | 12 | 1 |

## BCC_A2 (Be–Cu)

- Id: `phase:be-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 894.15–1560.09 K, x(Cu) 0–0.72382
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-cu:bcc-a2)

Names (5): _corpus: _corpus:phase:be-cu:bcc-a2  
_paper: _paper:10.1007/s10853-017-1777-z:(βBe), paper:10.1007/s10853-017-1777-z:β  
_tdb: _tdb:BeCu-18Liu.tdb:A2_BCC, tdb:BeCu-18Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BeCu-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb): A2_BCC, type code %B, sha256 `a0c9e1104448efba…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : BE% CU : VA : !
~~~~

[BeCu-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb): BCC_A2, type code %B, sha256 `a0c9e1104448efba…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BE% CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z) Yuling Liu, Bo Sundman, Yong Du, Jiong Wang, Shuhong Liu, Wei Ping Gong et al., A stepwise thermodynamic modeling of the phase diagram for the Cu–Be system, J Mater Sci 53, 3756-3766 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0036-9748(74)90399-8](https://doi.org/10.1016/0036-9748%2874%2990399-8) X Auvray, R Graf, A Guinier, Etude des alliages cuivre - beryllium au voisinage de la composition eutectoïde, Scripta Metallurgica 8, 995-1004 (1974).  
_cited as the source of values for this phase_

## B2_BCC (Be–Cu)

- Id: `phase:be-cu:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: BeCu-18Liu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in BeCu-18Liu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1560.09 K, x(Cu) 0–0.72382
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-cu:bcc-b2)

Names (4): _corpus: _corpus:phase:be-cu:bcc-b2, corpus:phase:be-cu:b2-bcc  
_paper: _paper:10.1007/s10853-017-1777-z:γ  
_tdb: _tdb:BeCu-18Liu.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[BeCu-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb): B2_BCC, type code %BO, sha256 `a0c9e1104448efba…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : BE% CU : BE CU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z) Yuling Liu, Bo Sundman, Yong Du, Jiong Wang, Shuhong Liu, Wei Ping Gong et al., A stepwise thermodynamic modeling of the phase diagram for the Cu–Be system, J Mater Sci 53, 3756-3766 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0036-9748(74)90399-8](https://doi.org/10.1016/0036-9748%2874%2990399-8) X Auvray, R Graf, A Guinier, Etude des alliages cuivre - beryllium au voisinage de la composition eutectoïde, Scripta Metallurgica 8, 995-1004 (1974).  
_cited as the source of values for this phase_

## C15_LAVES (Be–Cu)

- Id: `phase:be-cu:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in BeCu-18Liu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1489.49 K, x(Cu) 0.19343–0.36442
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-cu:c15-laves)

Names (3): _corpus: _corpus:phase:be-cu:c15-laves  
_paper: _paper:10.1007/s10853-017-1777-z:δ  
_tdb: _tdb:BeCu-18Liu.tdb:C15_LAVES  


### TDB models of C15_LAVES (1): PHASE and CONSTITUENT statements as written

[BeCu-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb): C15_LAVES, type code %, sha256 `a0c9e1104448efba…`

~~~~text
55: PHASE C15_LAVES % 2 2 1 !
56: CONST C15_LAVES : BE% CU : BE CU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z) Yuling Liu, Bo Sundman, Yong Du, Jiong Wang, Shuhong Liu, Wei Ping Gong et al., A stepwise thermodynamic modeling of the phase diagram for the Cu–Be system, J Mater Sci 53, 3756-3766 (2018).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Be–Cu)

- Id: `phase:be-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.6 K, x(Cu) 0.85163–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-cu:fcc-a1)

Names (3): _corpus: _corpus:phase:be-cu:fcc-a1  
_paper: _paper:10.1007/s10853-017-1777-z:(Cu)  
_tdb: _tdb:BeCu-18Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BeCu-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb): FCC_A1, type code %A, sha256 `a0c9e1104448efba…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BE CU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z) Yuling Liu, Bo Sundman, Yong Du, Jiong Wang, Shuhong Liu, Wei Ping Gong et al., A stepwise thermodynamic modeling of the phase diagram for the Cu–Be system, J Mater Sci 53, 3756-3766 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0036-9748(74)90399-8](https://doi.org/10.1016/0036-9748%2874%2990399-8) X Auvray, R Graf, A Guinier, Etude des alliages cuivre - beryllium au voisinage de la composition eutectoïde, Scripta Metallurgica 8, 995-1004 (1974).  
_cited as the source of values for this phase_

## HCP_A3 (Be–Cu)

- Id: `phase:be-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1540.47 K, x(Cu) 0–0.08532
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:be-cu:hcp-a3  
_paper: _paper:10.1007/s10853-017-1777-z:(αBe)  
_tdb: _tdb:BeCu-18Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BeCu-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb): HCP_A3, type code %A, sha256 `a0c9e1104448efba…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : BE% CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z) Yuling Liu, Bo Sundman, Yong Du, Jiong Wang, Shuhong Liu, Wei Ping Gong et al., A stepwise thermodynamic modeling of the phase diagram for the Cu–Be system, J Mater Sci 53, 3756-3766 (2018).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Be–Cu)

- Id: `phase:be-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1132.1–2500 K, x(Cu) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-cu:liquid)

Names (3): _corpus: _corpus:phase:be-cu:liquid  
_paper: _paper:10.1007/s10853-017-1777-z:Liquid  
_tdb: _tdb:BeCu-18Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BeCu-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb): LIQUID, type code %, sha256 `a0c9e1104448efba…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BE CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z) Yuling Liu, Bo Sundman, Yong Du, Jiong Wang, Shuhong Liu, Wei Ping Gong et al., A stepwise thermodynamic modeling of the phase diagram for the Cu–Be system, J Mater Sci 53, 3756-3766 (2018).  
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
