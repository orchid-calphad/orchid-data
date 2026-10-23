# C–Cu phases

> C–Cu system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-CU.html · Markdown: https://data.orchid-project.org/phases/pages/C-CU.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-CU) · [full JSON](https://data.orchid-project.org/phases/systems/C-CU.json) · [Markdown](https://data.orchid-project.org/phases/pages/C-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Cu system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-cu-a4-diamond); _phase:c-cu:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GRAPHITE_A9](#phase-c-cu-a9-graphite); _phase:c-cu:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 2 |
| [BCC_A2](#phase-c-cu-bcc-a2); _phase:c-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-c-cu-fcc-a1); _phase:c-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1357.86 K, x(C) 0–8e-05 | 0 | 2 |
| [HCP_A3](#phase-c-cu-hcp-a3); _phase:c-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-c-cu-liquid); _phase:c-cu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1357.78–4000 K, x(C) 0–0.62095 | 0 | 2 |

## DIAMOND_A4 (C–Cu)

- Id: `phase:c-cu:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cu:a4-diamond)

Names (3): _corpus: _corpus:phase:c-cu:a4-diamond  
_tdb: _tdb:CuC-04Din-LB.tdb:DIAMOND_A4, tdb:CuC-19Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[CuC-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-04Din-LB.tdb): DIAMOND_A4, type code %, sha256 `f57d45db59a47b95…`

~~~~text
63: PHASE DIAMOND_A4 % 1 1 !
64: CONST DIAMOND_A4 : C : !
~~~~

[CuC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-19Che.tdb): DIAMOND_A4, type code %, sha256 `0faa62cdae2d922d…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Cu)

- Id: `phase:c-cu:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cu:a9-graphite)

Names (3): _corpus: _corpus:phase:c-cu:a9-graphite  
_tdb: _tdb:CuC-04Din-LB.tdb:GRAPHITE_A9, tdb:CuC-19Che.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (2): PHASE and CONSTITUENT statements as written

[CuC-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-04Din-LB.tdb): GRAPHITE_A9, type code %, sha256 `f57d45db59a47b95…`

~~~~text
68: PHASE GRAPHITE_A9 % 1 1 !
69: CONST GRAPHITE_A9 : C : !
~~~~

[CuC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-19Che.tdb): GRAPHITE_A9, type code %, sha256 `0faa62cdae2d922d…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_

## BCC_A2 (C–Cu)

- Id: `phase:c-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cu:bcc-a2)

Names (3): _corpus: _corpus:phase:c-cu:bcc-a2  
_tdb: _tdb:CuC-04Din-LB.tdb:BCC_A2, tdb:CuC-19Che.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuC-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-04Din-LB.tdb): BCC_A2, type code %B, sha256 `f57d45db59a47b95…`

~~~~text
53: PHASE BCC_A2 %B 2 1 3 !
54: CONST BCC_A2 : CU : C VA% : !
~~~~

[CuC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-19Che.tdb): BCC_A2, type code %B, sha256 `0faa62cdae2d922d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_

## FCC_A1 (C–Cu)

- Id: `phase:c-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1357.86 K, x(C) 0–8e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cu:fcc-a1)

Names (3): _corpus: _corpus:phase:c-cu:fcc-a1  
_tdb: _tdb:CuC-04Din-LB.tdb:FCC_A1, tdb:CuC-19Che.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuC-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-04Din-LB.tdb): FCC_A1, type code %A, sha256 `f57d45db59a47b95…`

~~~~text
48: PHASE FCC_A1 %A 2 1 1 !
49: CONST FCC_A1 : CU : C VA% : !
~~~~

[CuC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-19Che.tdb): FCC_A1, type code %A, sha256 `0faa62cdae2d922d…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_

## HCP_A3 (C–Cu)

- Id: `phase:c-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:c-cu:hcp-a3  
_tdb: _tdb:CuC-04Din-LB.tdb:HCP_A3, tdb:CuC-19Che.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuC-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-04Din-LB.tdb): HCP_A3, type code %A, sha256 `f57d45db59a47b95…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : CU : C VA% : !
~~~~

[CuC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-19Che.tdb): HCP_A3, type code %A, sha256 `0faa62cdae2d922d…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
_assessment that models this phase_

## LIQUID (C–Cu)

- Id: `phase:c-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1357.78–4000 K, x(C) 0–0.62095
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-cu:liquid)

Names (3): _corpus: _corpus:phase:c-cu:liquid  
_tdb: _tdb:CuC-04Din-LB.tdb:LIQUID, tdb:CuC-19Che.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuC-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-04Din-LB.tdb): LIQUID, type code %, sha256 `f57d45db59a47b95…`

~~~~text
43: PHASE LIQUID:L % 1 1 !
44: CONST LIQUID:L : C CU : !
~~~~

[CuC-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuC-19Che.tdb): LIQUID, type code %, sha256 `0faa62cdae2d922d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.12.001](https://doi.org/10.1016/j.calphad.2018.12.001) L. Chen, Z. Zhang, Y. Huang, J. Cui, Z. Deng, H. Zou, K. Chang, Calphad, 64, 225-35(2019).  
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
