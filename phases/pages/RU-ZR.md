# Ru–Zr phases

> Ru–Zr system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RU-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/RU-ZR.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RU-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/RU-ZR.json) · [Ru–Zr system page](https://data.orchid-project.org/systems/RU-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/RU-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ru–Zr system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ru-zr-bcc-a2); _phase:ru-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 697.39–3999.38 K, x(Zr) 0.87403–1 | 4 | 2 |
| [C14_LAVES](#phase-ru-zr-c14-laves); _phase:ru-zr:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1567.76–2068.2 K, x(Zr) 0.33333–0.33334 | 11 | 1 |
| [FCC_A1](#phase-ru-zr-fcc-a1); _phase:ru-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ru-zr-hcp-a3); _phase:ru-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2620.93 K, x(Zr) 0–1 | 6 | 2 |
| [LIQUID](#phase-ru-zr-liquid); _phase:ru-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1494.38–4000 K, x(Zr) 0–1 | 10 | 2 |
| [RU2ZR_C14](#phase-ru-zr-ru2zr-c14); _phase:ru-zr:ru2zr-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1558.48–2109.89 K, x(Zr) 0.33333–0.33333 | 0 | 1 |
| [RUZR_B2](#phase-ru-zr-ruzr-b2); _phase:ru-zr:ruzr-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2401.63 K, x(Zr) 0.5–0.51181 | 19 | 2 |

## BCC_A2 (Ru–Zr)

- Id: `phase:ru-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 697.39–3999.38 K, x(Zr) 0.87403–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-zr:bcc-a2)

Names (4): _corpus: _corpus:phase:ru-zr:bcc-a2  
_paper: _paper:10.1007/s11669-007-9084-z:β(Zr)  
_tdb: _tdb:RuZr-05Che-LB.tdb:BCC_A2, tdb:RuZr-07Idb.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[RuZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-05Che-LB.tdb): BCC_A2, type code %B, sha256 `5b8a10c1760f63f1…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : RU ZR% : VA : !
~~~~

[RuZr-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-07Idb.tdb): BCC_A2, type code %B, sha256 `7b022e6cd42b0237…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : RU ZR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-007-9084-z](https://doi.org/10.1007/s11669-007-9084-z) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic Assessment of the Ru-Zr Binary System, J Phs Eqil and Diff 28, 243-249 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667814](https://doi.org/10.1007/bf02667814) H. Okamoto, The Ru-Zr system (ruthenium-zirconium), JPE 14, 225-227 (1993).  
_cited as the source of values for this phase_

## C14_LAVES (Ru–Zr)

- Id: `phase:ru-zr:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in RuZr-07Idb.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1567.76–2068.2 K, x(Zr) 0.33333–0.33334
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-zr:c14-laves)

Names (3): _corpus: _corpus:phase:ru-zr:c14-laves  
_paper: _paper:10.1007/s11669-007-9084-z:Ru2Zr  
_tdb: _tdb:RuZr-07Idb.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[RuZr-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-07Idb.tdb): C14_LAVES, type code %, sha256 `7b022e6cd42b0237…`

~~~~text
49: PHASE C14_LAVES % 2 2 1 !
50: CONST C14_LAVES : RU% ZR : RU ZR% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-007-9084-z](https://doi.org/10.1007/s11669-007-9084-z) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic Assessment of the Ru-Zr Binary System, J Phs Eqil and Diff 28, 243-249 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667814](https://doi.org/10.1007/bf02667814) H. Okamoto, The Ru-Zr system (ruthenium-zirconium), JPE 14, 225-227 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(96)00069-6](https://doi.org/10.1016/s0966-9795%2896%2900069-6) K. Mahdouk, K. Elaissaoui, J. Charles, L. Bouirden, and J.-C. Gachon, Calorimetric Study and Optimization of the Ruthenium-Zirconium Phase Diagram, Intermetallics, 1997, 5, p 111-116  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(85)90032-x](https://doi.org/10.1016/0364-5916%2885%2990032-x) C. Colinet, A. Pasturel, P. Hicter, Calphad 9 (1985) 71–99.  
_cited as the source of values for this phase_

## FCC_A1 (Ru–Zr)

- Id: `phase:ru-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:ru-zr:fcc-a1  
_tdb: _tdb:RuZr-05Che-LB.tdb:FCC_A1, tdb:RuZr-07Idb.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[RuZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-05Che-LB.tdb): FCC_A1, type code %A, sha256 `5b8a10c1760f63f1…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : RU ZR : VA : !
~~~~

[RuZr-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-07Idb.tdb): FCC_A1, type code %A, sha256 `7b022e6cd42b0237…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : RU ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-007-9084-z](https://doi.org/10.1007/s11669-007-9084-z) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic Assessment of the Ru-Zr Binary System, J Phs Eqil and Diff 28, 243-249 (2007).  
_assessment that models this phase_

## HCP_A3 (Ru–Zr)

- Id: `phase:ru-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2620.93 K, x(Zr) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-zr:hcp-a3)

Names (5): _corpus: _corpus:phase:ru-zr:hcp-a3  
_paper: _paper:10.1007/s11669-007-9084-z:(Ru), paper:10.1007/s11669-007-9084-z:α(Zr)  
_tdb: _tdb:RuZr-05Che-LB.tdb:HCP_A3, tdb:RuZr-07Idb.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[RuZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-05Che-LB.tdb): HCP_A3, type code %, sha256 `5b8a10c1760f63f1…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : RU ZR : VA : !
~~~~

[RuZr-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-07Idb.tdb): HCP_A3, type code %, sha256 `7b022e6cd42b0237…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : RU ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-007-9084-z](https://doi.org/10.1007/s11669-007-9084-z) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic Assessment of the Ru-Zr Binary System, J Phs Eqil and Diff 28, 243-249 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667814](https://doi.org/10.1007/bf02667814) H. Okamoto, The Ru-Zr system (ruthenium-zirconium), JPE 14, 225-227 (1993).  
_cited as the source of values for this phase_

## LIQUID (Ru–Zr)

- Id: `phase:ru-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1494.38–4000 K, x(Zr) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-zr:liquid)

Names (5): _corpus: _corpus:phase:ru-zr:liquid  
_paper: _paper:10.1007/s11669-007-9084-z:L, paper:10.1007/s11669-007-9084-z:liquid  
_tdb: _tdb:RuZr-05Che-LB.tdb:LIQUID, tdb:RuZr-07Idb.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[RuZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-05Che-LB.tdb): LIQUID, type code %, sha256 `5b8a10c1760f63f1…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : RU ZR : !
~~~~

[RuZr-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-07Idb.tdb): LIQUID, type code %, sha256 `7b022e6cd42b0237…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : RU ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-007-9084-z](https://doi.org/10.1007/s11669-007-9084-z) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic Assessment of the Ru-Zr Binary System, J Phs Eqil and Diff 28, 243-249 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667814](https://doi.org/10.1007/bf02667814) H. Okamoto, The Ru-Zr system (ruthenium-zirconium), JPE 14, 225-227 (1993).  
_cited as the source of values for this phase_

## RU2ZR_C14 (Ru–Zr)

- Id: `phase:ru-zr:ru2zr-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Ru 0.6667, Zr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1558.48–2109.89 K, x(Zr) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-zr:ru2zr-c14)

Names (2): _corpus: _corpus:phase:ru-zr:ru2zr-c14  
_tdb: _tdb:RuZr-05Che-LB.tdb:RU2ZR_C14  


### TDB models of RU2ZR_C14 (1): PHASE and CONSTITUENT statements as written

[RuZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-05Che-LB.tdb): RU2ZR_C14, type code %, sha256 `5b8a10c1760f63f1…`

~~~~text
41: PHASE RU2ZR_C14 % 2 2 1 !
42: CONST RU2ZR_C14 : RU : ZR : !
~~~~

## RUZR_B2 (Ru–Zr)

- Id: `phase:ru-zr:ruzr-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in RuZr-07Idb.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–2401.63 K, x(Zr) 0.5–0.51181
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-zr:ruzr-b2)

Names (4): _corpus: _corpus:phase:ru-zr:ruzr-b2  
_paper: _paper:10.1007/s11669-007-9084-z:RuZr  
_tdb: _tdb:RuZr-05Che-LB.tdb:RUZR_B2, tdb:RuZr-07Idb.tdb:RUZR_B2  


### TDB models of RUZR_B2 (2): PHASE and CONSTITUENT statements as written

[RuZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-05Che-LB.tdb): RUZR_B2, type code %, sha256 `5b8a10c1760f63f1…`

~~~~text
46: PHASE RUZR_B2 % 2 1 1 !
47: CONST RUZR_B2 : RU : ZR : !
~~~~

[RuZr-07Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/RuZr-07Idb.tdb): RUZR_B2, type code %, sha256 `7b022e6cd42b0237…`

~~~~text
54: PHASE RUZR_B2 % 2 1 1 !
55: CONST RUZR_B2 : RU% ZR : RU ZR% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-007-9084-z](https://doi.org/10.1007/s11669-007-9084-z) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic Assessment of the Ru-Zr Binary System, J Phs Eqil and Diff 28, 243-249 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667814](https://doi.org/10.1007/bf02667814) H. Okamoto, The Ru-Zr system (ruthenium-zirconium), JPE 14, 225-227 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(96)00069-6](https://doi.org/10.1016/s0966-9795%2896%2900069-6) K. Mahdouk, K. Elaissaoui, J. Charles, L. Bouirden, and J.-C. Gachon, Calorimetric Study and Optimization of the Ruthenium-Zirconium Phase Diagram, Intermetallics, 1997, 5, p 111-116  
_cited as the source of values for this phase_
- [doi:10.1007/bf02628390](https://doi.org/10.1007/bf02628390) Letitia Topor, O. J. Kleppa, Thermochemistry of the intermetallic compounds RuTi, RuZr, and RuHf, Metall Trans A 19, 1061-1066 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90449-9](https://doi.org/10.1016/0022-5088%2889%2990449-9) Letitia Topor, O.J. Kleppa, Enthalpies of formation of equiatomic compounds of titanium, zirconium and hafnium with late transition metals: Systematic aspects and comparisons with predicted values, Journal of the Less Common Metals 155, 61-73 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(85)90032-x](https://doi.org/10.1016/0364-5916%2885%2990032-x) C. Colinet, A. Pasturel, P. Hicter, Calphad 9 (1985) 71–99.  
_cited as the source of values for this phase_
- [doi:10.1016/s0036-9748(88)80148-0](https://doi.org/10.1016/s0036-9748%2888%2980148-0) R.E. Watson, M. Weinert, J.W. Davenport, G.W. Fernando, The energetics of transition metal alloy formation: Theory versus experiment, Scripta Metallurgica 22, 1285-1289 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(01)00956-2](https://doi.org/10.1016/s0925-8388%2801%2900956-2) Qiti Guo, Ole Jakob Kleppa, The standard enthalpies of formation of the compounds of early transition metals with late transition metals and with noble metals as determined by Kleppa and co-workers at the University of Chicago — A review, Journal of Alloys and Compounds 321, 169-182 (2001).  
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
