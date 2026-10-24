# Mo–Pd phases

> Mo–Pd system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-PD.html · Markdown: https://data.orchid-project.org/phases/pages/MO-PD.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-PD) · [full JSON](https://data.orchid-project.org/phases/systems/MO-PD.json) · [Mo–Pd system page](https://data.orchid-project.org/systems/MO-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Pd system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-pd-bcc-a2); _phase:mo-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2901.01 K, x(Pd) 0–0.04805 | 7 | 1 |
| [FCC_A1](#phase-mo-pd-fcc-a1); _phase:mo-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2028.73 K, x(Pd) 0.55905–1 | 41 | 1 |
| [HCP_A3](#phase-mo-pd-hcp-a3); _phase:mo-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1654.34–2000.93 K, x(Pd) 0.50157–0.53788 | 9 | 1 |
| [LIQUID](#phase-mo-pd-liquid); _phase:mo-pd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1828–4000 K, x(Pd) 0–1 | 7 | 1 |

## BCC_A2 (Mo–Pd)

- Id: `phase:mo-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2901.01 K, x(Pd) 0–0.04805
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pd:bcc-a2)

Names (3): _corpus: _corpus:phase:mo-pd:bcc-a2  
_paper: _paper:10.1361/105497100770340390:(Mo)  
_tdb: _tdb:MoPd-00Gho.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MoPd-00Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPd-00Gho.tdb): BCC_A2, type code %B, sha256 `fe2b737fc07909c4…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MO% PD : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390) G. Ghosh, G. B. Olson, Thermodynamic modeling of the Cr-Pd and Mo-Pd systems, JPE 21, 32-39 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90424-8](https://doi.org/10.1016/0022-3115%2889%2990424-8) H. Kleykamp, Constitution and thermodynamics of the Mo-Ru, Mo-Pd, Ru-Pd and Mo-Ru-Pd systems, Journal of Nuclear Materials 167, 49-63 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90009-8](https://doi.org/10.1016/0022-5088%2864%2990009-8) E. Anderson, The equilibrium diagram of the system molybdenum-palladium, Journal of the Less Common Metals 6, 81-84 (1964).  
_cited as the source of values for this phase_

## FCC_A1 (Mo–Pd)

- Id: `phase:mo-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2028.73 K, x(Pd) 0.55905–1
- Literature: 41 values (41 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pd:fcc-a1)

Names (4): _corpus: _corpus:phase:mo-pd:fcc-a1  
_paper: _paper:10.1361/105497100770340390:(Pd), paper:10.1361/105497100770340390:fcc  
_tdb: _tdb:MoPd-00Gho.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MoPd-00Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPd-00Gho.tdb): FCC_A1, type code %A, sha256 `fe2b737fc07909c4…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MO PD% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390) G. Ghosh, G. B. Olson, Thermodynamic modeling of the Cr-Pd and Mo-Pd systems, JPE 21, 32-39 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90424-8](https://doi.org/10.1016/0022-3115%2889%2990424-8) H. Kleykamp, Constitution and thermodynamics of the Mo-Ru, Mo-Pd, Ru-Pd and Mo-Ru-Pd systems, Journal of Nuclear Materials 167, 49-63 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90009-8](https://doi.org/10.1016/0022-5088%2864%2990009-8) E. Anderson, The equilibrium diagram of the system molybdenum-palladium, Journal of the Less Common Metals 6, 81-84 (1964).  
_cited as the source of values for this phase_

## HCP_A3 (Mo–Pd)

- Id: `phase:mo-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1654.34–2000.93 K, x(Pd) 0.50157–0.53788
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pd:hcp-a3)

Names (4): _corpus: _corpus:phase:mo-pd:hcp-a3  
_paper: _paper:10.1361/105497100770340390:ε  
_system_alias: _system_alias:mo-pd:epsilon  
_tdb: _tdb:MoPd-00Gho.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MoPd-00Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPd-00Gho.tdb): HCP_A3, type code %A, sha256 `fe2b737fc07909c4…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MO PD : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390) G. Ghosh, G. B. Olson, Thermodynamic modeling of the Cr-Pd and Mo-Pd systems, JPE 21, 32-39 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90424-8](https://doi.org/10.1016/0022-3115%2889%2990424-8) H. Kleykamp, Constitution and thermodynamics of the Mo-Ru, Mo-Pd, Ru-Pd and Mo-Ru-Pd systems, Journal of Nuclear Materials 167, 49-63 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90009-8](https://doi.org/10.1016/0022-5088%2864%2990009-8) E. Anderson, The equilibrium diagram of the system molybdenum-palladium, Journal of the Less Common Metals 6, 81-84 (1964).  
_cited as the source of values for this phase_

## LIQUID (Mo–Pd)

- Id: `phase:mo-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1828–4000 K, x(Pd) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pd:liquid)

Names (3): _corpus: _corpus:phase:mo-pd:liquid  
_paper: _paper:10.1361/105497100770340390:L  
_tdb: _tdb:MoPd-00Gho.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MoPd-00Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPd-00Gho.tdb): LIQUID, type code %, sha256 `fe2b737fc07909c4…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MO PD : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390) G. Ghosh, G. B. Olson, Thermodynamic modeling of the Cr-Pd and Mo-Pd systems, JPE 21, 32-39 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(64)90009-8](https://doi.org/10.1016/0022-5088%2864%2990009-8) E. Anderson, The equilibrium diagram of the system molybdenum-palladium, Journal of the Less Common Metals 6, 81-84 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(89)90424-8](https://doi.org/10.1016/0022-3115%2889%2990424-8) H. Kleykamp, Constitution and thermodynamics of the Mo-Ru, Mo-Pd, Ru-Pd and Mo-Ru-Pd systems, Journal of Nuclear Materials 167, 49-63 (1989).  
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
