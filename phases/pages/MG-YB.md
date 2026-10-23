# Mg–Yb phases

> Mg–Yb system: 5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-YB.html · Markdown: https://data.orchid-project.org/phases/pages/MG-YB.md

5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-YB) · [full JSON](https://data.orchid-project.org/phases/systems/MG-YB.json) · [Mg–Yb system page](https://data.orchid-project.org/systems/MG-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Yb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-yb-bcc-a2); _phase:mg-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 720.02–1240.45 K, x(Yb) 0.90974–1 | 4 | 1 |
| [FCC_A1](#phase-mg-yb-fcc-a1); _phase:mg-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1087.48 K, x(Yb) 0.96206–1 | 2 | 1 |
| [HCP_A3](#phase-mg-yb-hcp-a3); _phase:mg-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–923 K, x(Yb) 0–0.00604 | 2 | 1 |
| [LIQUID](#phase-mg-yb-liquid); _phase:mg-yb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 768.69–2500 K, x(Yb) 0–1 | 6 | 1 |
| [MG2YB_C14](#phase-mg-yb-mg2yb-c14); _phase:mg-yb:mg2yb-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–991.27 K, x(Yb) 0.2945–0.36216 | 8 | 1 |

## BCC_A2 (Mg–Yb)

- Id: `phase:mg-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 720.02–1240.45 K, x(Yb) 0.90974–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-yb:bcc-a2)

Names (3): _corpus: _corpus:phase:mg-yb:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2005.11.060:bcc(Yb)  
_tdb: _tdb:MgYb-06Guo-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MgYb-06Guo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgYb-06Guo-LB.tdb): BCC_A2, type code %B, sha256 `f85e80786337a12b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MG YB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(65)90063-9](https://doi.org/10.1016/0022-5088%2865%2990063-9) O.D. McMasters, K.A. Gschneidner, Ytterbium-magnesium system, Journal of the Less Common Metals 8, 289-298 (1965).  
_cited as the source of values for this phase_

## FCC_A1 (Mg–Yb)

- Id: `phase:mg-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1087.48 K, x(Yb) 0.96206–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:mg-yb:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2005.11.060:fcc(Yb)  
_tdb: _tdb:MgYb-06Guo-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MgYb-06Guo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgYb-06Guo-LB.tdb): FCC_A1, type code %A, sha256 `f85e80786337a12b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MG YB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(65)90063-9](https://doi.org/10.1016/0022-5088%2865%2990063-9) O.D. McMasters, K.A. Gschneidner, Ytterbium-magnesium system, Journal of the Less Common Metals 8, 289-298 (1965).  
_cited as the source of values for this phase_

## HCP_A3 (Mg–Yb)

- Id: `phase:mg-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–923 K, x(Yb) 0–0.00604
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-yb:hcp-a3)

Names (3): _corpus: _corpus:phase:mg-yb:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2005.11.060:hcp(Mg)  
_tdb: _tdb:MgYb-06Guo-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MgYb-06Guo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgYb-06Guo-LB.tdb): HCP_A3, type code %A, sha256 `f85e80786337a12b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MG% YB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(65)90063-9](https://doi.org/10.1016/0022-5088%2865%2990063-9) O.D. McMasters, K.A. Gschneidner, Ytterbium-magnesium system, Journal of the Less Common Metals 8, 289-298 (1965).  
_cited as the source of values for this phase_

## LIQUID (Mg–Yb)

- Id: `phase:mg-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 768.69–2500 K, x(Yb) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-yb:liquid)

Names (3): _corpus: _corpus:phase:mg-yb:liquid  
_paper: _paper:10.1016/j.jallcom.2005.11.060:liq.  
_tdb: _tdb:MgYb-06Guo-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MgYb-06Guo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgYb-06Guo-LB.tdb): LIQUID, type code %, sha256 `f85e80786337a12b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MG YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(65)90063-9](https://doi.org/10.1016/0022-5088%2865%2990063-9) O.D. McMasters, K.A. Gschneidner, Ytterbium-magnesium system, Journal of the Less Common Metals 8, 289-298 (1965).  
_cited as the source of values for this phase_

## MG2YB_C14 (Mg–Yb)

- Id: `phase:mg-yb:mg2yb-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgYb-06Guo-LB.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–991.27 K, x(Yb) 0.2945–0.36216
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-yb:mg2yb-c14)

Names (3): _corpus: _corpus:phase:mg-yb:mg2yb-c14  
_paper: _paper:10.1016/j.jallcom.2005.11.060:Mg2Yb  
_tdb: _tdb:MgYb-06Guo-LB.tdb:MG2YB_C14  


### TDB models of MG2YB_C14 (1): PHASE and CONSTITUENT statements as written

[MgYb-06Guo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgYb-06Guo-LB.tdb): MG2YB_C14, type code %, sha256 `f85e80786337a12b…`

~~~~text
40: PHASE MG2YB_C14 % 2 2 1 !
41: CONST MG2YB_C14 : MG% YB : MG YB% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(65)90063-9](https://doi.org/10.1016/0022-5088%2865%2990063-9) O.D. McMasters, K.A. Gschneidner, Ytterbium-magnesium system, Journal of the Less Common Metals 8, 289-298 (1965).  
_cited as the source of values for this phase_

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
