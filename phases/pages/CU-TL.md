# Cu–Tl phases

> Cu–Tl system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-TL.html · Markdown: https://data.orchid-project.org/phases/pages/CU-TL.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-TL) · [full JSON](https://data.orchid-project.org/phases/systems/CU-TL.json) · [Cu–Tl system page](https://data.orchid-project.org/systems/CU-TL.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-TL.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Tl system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-tl-bcc-a2); _phase:cu-tl:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300.75–2499.5 K, x(Tl) 0.99999–1 | 0 | 2 |
| [FCC_A1](#phase-cu-tl-fcc-a1); _phase:cu-tl:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1366.77 K, x(Tl) 0–0.00264 | 0 | 2 |
| [HCP_A3](#phase-cu-tl-hcp-a3); _phase:cu-tl:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–507 K, x(Tl) 1–1 | 0 | 2 |
| [LIQUID](#phase-cu-tl-liquid); _phase:cu-tl:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 576.5–2500 K, x(Tl) 0–1 | 103 | 2 |

## BCC_A2 (Cu–Tl)

- Id: `phase:cu-tl:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.75–2499.5 K, x(Tl) 0.99999–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tl:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-tl:bcc-a2  
_tdb: _tdb:CuTl-04Che-LB.tdb:BCC_A2, tdb:CuTl-89Che.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuTl-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-04Che-LB.tdb): BCC_A2, type code %B, sha256 `83fa28481f84d4bf…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CU TL% : VA : !
~~~~

[CuTl-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-89Che.tdb): BCC_A2, type code %B, sha256 `d1f4279261a86a0f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CU TL% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(89)87205-3](https://doi.org/10.1016/0040-6031%2889%2987205-3) P.-Y. Chevalier, A thermodynamic evaluation of the Cu-TI system, Thermochimica Acta 156, 383-392 (1989).  
_assessment that models this phase_

## FCC_A1 (Cu–Tl)

- Id: `phase:cu-tl:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1366.77 K, x(Tl) 0–0.00264
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tl:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-tl:fcc-a1  
_tdb: _tdb:CuTl-04Che-LB.tdb:FCC_A1, tdb:CuTl-89Che.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuTl-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-04Che-LB.tdb): FCC_A1, type code %A, sha256 `83fa28481f84d4bf…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CU% TL : VA : !
~~~~

[CuTl-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-89Che.tdb): FCC_A1, type code %A, sha256 `d1f4279261a86a0f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CU% TL : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(89)87205-3](https://doi.org/10.1016/0040-6031%2889%2987205-3) P.-Y. Chevalier, A thermodynamic evaluation of the Cu-TI system, Thermochimica Acta 156, 383-392 (1989).  
_assessment that models this phase_

## HCP_A3 (Cu–Tl)

- Id: `phase:cu-tl:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–507 K, x(Tl) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tl:hcp-a3)

Names (3): _corpus: _corpus:phase:cu-tl:hcp-a3  
_tdb: _tdb:CuTl-04Che-LB.tdb:HCP_A3, tdb:CuTl-89Che.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuTl-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-04Che-LB.tdb): HCP_A3, type code %A, sha256 `83fa28481f84d4bf…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CU TL% : VA : !
~~~~

[CuTl-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-89Che.tdb): HCP_A3, type code %A, sha256 `d1f4279261a86a0f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CU TL% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(89)87205-3](https://doi.org/10.1016/0040-6031%2889%2987205-3) P.-Y. Chevalier, A thermodynamic evaluation of the Cu-TI system, Thermochimica Acta 156, 383-392 (1989).  
_assessment that models this phase_

## LIQUID (Cu–Tl)

- Id: `phase:cu-tl:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 576.5–2500 K, x(Tl) 0–1
- Literature: 103 values (103 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-tl:liquid)

Names (6): _corpus: _corpus:phase:cu-tl:liquid  
_paper: _paper:10.1016/0040-6031(89)87205-3:L1, paper:10.1016/0040-6031(89)87205-3:L2, paper:10.1016/0040-6031(89)87205-3:liquid  
_tdb: _tdb:CuTl-04Che-LB.tdb:LIQUID, tdb:CuTl-89Che.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuTl-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-04Che-LB.tdb): LIQUID, type code %, sha256 `83fa28481f84d4bf…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CU TL : !
~~~~

[CuTl-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuTl-89Che.tdb): LIQUID, type code %, sha256 `d1f4279261a86a0f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CU TL : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0040-6031(89)87205-3](https://doi.org/10.1016/0040-6031%2889%2987205-3) P.-Y. Chevalier, A thermodynamic evaluation of the Cu-TI system, Thermochimica Acta 156, 383-392 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0025-5416(69)90038-x](https://doi.org/10.1016/0025-5416%2869%2990038-x) Bruno Predel, Hartmut Sandig, Thermodynamische untersuchungen der systeme aluminium-wismut, aluminium-indium und kupfer-thallium, Materials Science and Engineering 4, 49-57 (1969).  
_cited as the source of values for this phase_
- [doi:10.1021/ja01143a066](https://doi.org/10.1021/ja01143a066) O. J. Kleppa, A Thermodynamic Study of Liquid Metallic Solutions. IV. Approximate Thermodynamic Data from the Phase Diagram for the Systems Copper—Bismuth, Copper—Lead and Copper—Thallium, J. Am. Chem. Soc. 74, 6047-6051 (1952).  
_cited as the source of values for this phase_

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
