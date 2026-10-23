# Fe–W phases

> Fe–W system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-W.html · Markdown: https://data.orchid-project.org/phases/pages/FE-W.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-W) · [full JSON](https://data.orchid-project.org/phases/systems/FE-W.json) · [Fe–W system page](https://data.orchid-project.org/systems/FE-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–W system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-w-bcc-a2); _phase:fe-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.9 K, x(W) 0–1 | 0 | 3 |
| [C14_LAVES](#phase-fe-w-c14-laves); _phase:fe-w:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1335.45 K, x(W) 0.32844–0.33333 | 0 | 3 |
| [MU_D85](#phase-fe-w-d85-mu); _phase:fe-w:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1914.37 K, x(W) 0.39185–0.46154 | 0 | 3 |
| [FCC_A1](#phase-fe-w-fcc-a1); _phase:fe-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 873.57–1832.32 K, x(W) 0–0.01357 | 0 | 3 |
| [HCP_A3](#phase-fe-w-hcp-a3); _phase:fe-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-fe-w-liquid); _phase:fe-w:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1805.91–4000 K, x(W) 0–1 | 0 | 3 |

## BCC_A2 (Fe–W)

- Id: `phase:fe-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.9 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-w:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-w:bcc-a2  
_tdb: _tdb:FeW-15Jac-phonon.tdb:BCC_A2, tdb:FeW-15Jac-static.tdb:BCC_A2, tdb:FeW-87Gus-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[FeW-15Jac-phonon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-phonon.tdb): BCC_A2, type code %B, sha256 `3c044c4de34afca7…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : FE W : VA : !
~~~~

[FeW-15Jac-static.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-static.tdb): BCC_A2, type code %B, sha256 `40556b11f6faf2f1…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : FE W : VA : !
~~~~

[FeW-87Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-87Gus-LB.tdb): BCC_A2, type code %B, sha256 `0f42cbd0e7a82e6e…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02825699](https://doi.org/10.1007/BF02825699) P. Gustafson, Metall. Trans. A, 18A, 175-88 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.010](https://doi.org/10.1016/j.calphad.2015.04.010) A. Jacob, C. Schmetterer, L. Singheiser, A. Gray-Weale, B. Hallstedt, A. Watson, Calphad, 50, 92-104(2015).  
_assessment that models this phase_

## C14_LAVES (Fe–W)

- Id: `phase:fe-w:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeW-15Jac-phonon.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeW-15Jac-static.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeW-87Gus-LB.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1335.45 K, x(W) 0.32844–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-w:c14-laves)

Names (4): _corpus: _corpus:phase:fe-w:c14-laves  
_tdb: _tdb:FeW-15Jac-phonon.tdb:C14_LAVES, tdb:FeW-15Jac-static.tdb:C14_LAVES, tdb:FeW-87Gus-LB.tdb:C14_LAVES  


### TDB models of C14_LAVES (3): PHASE and CONSTITUENT statements as written

[FeW-15Jac-phonon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-phonon.tdb): C14_LAVES, type code %, sha256 `3c044c4de34afca7…`

~~~~text
41: PHASE C14_LAVES % 2 2 1 !
42: CONST C14_LAVES : FE W : FE W : !
~~~~

[FeW-15Jac-static.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-static.tdb): C14_LAVES, type code %, sha256 `40556b11f6faf2f1…`

~~~~text
41: PHASE C14_LAVES % 2 2 1 !
42: CONST C14_LAVES : FE W : FE W : !
~~~~

[FeW-87Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-87Gus-LB.tdb): C14_LAVES, type code %, sha256 `0f42cbd0e7a82e6e…`

~~~~text
45: PHASE C14_LAVES % 2 2 1 !
46: CONST C14_LAVES : FE% W : FE W% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02825699](https://doi.org/10.1007/BF02825699) P. Gustafson, Metall. Trans. A, 18A, 175-88 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.010](https://doi.org/10.1016/j.calphad.2015.04.010) A. Jacob, C. Schmetterer, L. Singheiser, A. Gray-Weale, B. Hallstedt, A. Watson, Calphad, 50, 92-104(2015).  
_assessment that models this phase_

## MU_D85 (Fe–W)

- Id: `phase:fe-w:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeW-15Jac-phonon.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeW-15Jac-static.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1914.37 K, x(W) 0.39185–0.46154
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-w:d85-mu)

Names (4): _corpus: _corpus:phase:fe-w:d85-mu  
_tdb: _tdb:FeW-15Jac-phonon.tdb:MU_D85, tdb:FeW-15Jac-static.tdb:MU_D85, tdb:FeW-87Gus-LB.tdb:MU_D85  


### TDB models of MU_D85 (3): PHASE and CONSTITUENT statements as written

[FeW-15Jac-phonon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-phonon.tdb): MU_D85, type code %, sha256 `3c044c4de34afca7…`

~~~~text
46: PHASE MU_D85 % 4 1 4 2 6 !
47: CONST MU_D85 : FE W : W : FE W : FE W : !
~~~~

[FeW-15Jac-static.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-static.tdb): MU_D85, type code %, sha256 `40556b11f6faf2f1…`

~~~~text
46: PHASE MU_D85 % 4 1 4 2 6 !
47: CONST MU_D85 : FE W : W : FE W : FE W : !
~~~~

[FeW-87Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-87Gus-LB.tdb): MU_D85, type code %, sha256 `0f42cbd0e7a82e6e…`

~~~~text
50: PHASE MU_D85 % 3 7 2 4 !
51: CONST MU_D85 : FE : W : FE W% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02825699](https://doi.org/10.1007/BF02825699) P. Gustafson, Metall. Trans. A, 18A, 175-88 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.010](https://doi.org/10.1016/j.calphad.2015.04.010) A. Jacob, C. Schmetterer, L. Singheiser, A. Gray-Weale, B. Hallstedt, A. Watson, Calphad, 50, 92-104(2015).  
_assessment that models this phase_

## FCC_A1 (Fe–W)

- Id: `phase:fe-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 873.57–1832.32 K, x(W) 0–0.01357
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-w:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-w:fcc-a1  
_tdb: _tdb:FeW-15Jac-phonon.tdb:FCC_A1, tdb:FeW-15Jac-static.tdb:FCC_A1, tdb:FeW-87Gus-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[FeW-15Jac-phonon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-phonon.tdb): FCC_A1, type code %A, sha256 `3c044c4de34afca7…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : FE W : VA : !
~~~~

[FeW-15Jac-static.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-static.tdb): FCC_A1, type code %A, sha256 `40556b11f6faf2f1…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : FE W : VA : !
~~~~

[FeW-87Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-87Gus-LB.tdb): FCC_A1, type code %A, sha256 `0f42cbd0e7a82e6e…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02825699](https://doi.org/10.1007/BF02825699) P. Gustafson, Metall. Trans. A, 18A, 175-88 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.010](https://doi.org/10.1016/j.calphad.2015.04.010) A. Jacob, C. Schmetterer, L. Singheiser, A. Gray-Weale, B. Hallstedt, A. Watson, Calphad, 50, 92-104(2015).  
_assessment that models this phase_

## HCP_A3 (Fe–W)

- Id: `phase:fe-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-w:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-w:hcp-a3  
_tdb: _tdb:FeW-15Jac-phonon.tdb:HCP_A3, tdb:FeW-15Jac-static.tdb:HCP_A3, tdb:FeW-87Gus-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[FeW-15Jac-phonon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-phonon.tdb): HCP_A3, type code %, sha256 `3c044c4de34afca7…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : FE W : VA : !
~~~~

[FeW-15Jac-static.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-static.tdb): HCP_A3, type code %, sha256 `40556b11f6faf2f1…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : FE W : VA : !
~~~~

[FeW-87Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-87Gus-LB.tdb): HCP_A3, type code %, sha256 `0f42cbd0e7a82e6e…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : FE W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02825699](https://doi.org/10.1007/BF02825699) P. Gustafson, Metall. Trans. A, 18A, 175-88 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.010](https://doi.org/10.1016/j.calphad.2015.04.010) A. Jacob, C. Schmetterer, L. Singheiser, A. Gray-Weale, B. Hallstedt, A. Watson, Calphad, 50, 92-104(2015).  
_assessment that models this phase_

## LIQUID (Fe–W)

- Id: `phase:fe-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1805.91–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-w:liquid)

Names (4): _corpus: _corpus:phase:fe-w:liquid  
_tdb: _tdb:FeW-15Jac-phonon.tdb:LIQUID, tdb:FeW-15Jac-static.tdb:LIQUID, tdb:FeW-87Gus-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[FeW-15Jac-phonon.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-phonon.tdb): LIQUID, type code %, sha256 `3c044c4de34afca7…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : FE W : !
~~~~

[FeW-15Jac-static.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-15Jac-static.tdb): LIQUID, type code %, sha256 `40556b11f6faf2f1…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : FE W : !
~~~~

[FeW-87Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeW-87Gus-LB.tdb): LIQUID, type code %, sha256 `0f42cbd0e7a82e6e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02825699](https://doi.org/10.1007/BF02825699) P. Gustafson, Metall. Trans. A, 18A, 175-88 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.010](https://doi.org/10.1016/j.calphad.2015.04.010) A. Jacob, C. Schmetterer, L. Singheiser, A. Gray-Weale, B. Hallstedt, A. Watson, Calphad, 50, 92-104(2015).  
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
