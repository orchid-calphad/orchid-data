# C–Pd phases

> C–Pd system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-PD.html · Markdown: https://data.orchid-project.org/phases/pages/C-PD.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-PD) · [full JSON](https://data.orchid-project.org/phases/systems/C-PD.json) · [C–Pd system page](https://data.orchid-project.org/systems/C-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Pd system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-pd-a4-diamond); _phase:c-pd:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GRAPHITE_A9](#phase-c-pd-a9-graphite); _phase:c-pd:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 0.99961–1 | 2 | 3 |
| [BCC_A2](#phase-c-pd-bcc-a2); _phase:c-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-c-pd-fcc-a1); _phase:c-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1828.77 K, x(C) 0–0.08565 | 2 | 3 |
| [HCP_A3](#phase-c-pd-hcp-a3); _phase:c-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-c-pd-liquid); _phase:c-pd:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1765.16–4000 K, x(C) 0–0.62447 | 2 | 3 |

## DIAMOND_A4 (C–Pd)

- Id: `phase:c-pd:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pd:a4-diamond)

Names (4): _corpus: _corpus:phase:c-pd:a4-diamond  
_tdb: _tdb:PdC-04Kor-LB.tdb:DIAMOND_A4, tdb:PdC-06Du.tdb:DIAMOND_A4, tdb:PdC-20Jia.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[PdC-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-04Kor-LB.tdb): DIAMOND_A4, type code %, sha256 `f28cef69e245166a…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : C : !
~~~~

[PdC-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-06Du.tdb): DIAMOND_A4, type code %, sha256 `53286c4307480550…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C% PD : !
~~~~

[PdC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-20Jia.tdb): DIAMOND_A4, type code %, sha256 `321588b3daac71cd…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Pd)

- Id: `phase:c-pd:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 0.99961–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pd:a9-graphite)

Names (5): _corpus: _corpus:phase:c-pd:a9-graphite  
_paper: _paper:10.1016/j.intermet.2005.09.008:graphite(C)  
_tdb: _tdb:PdC-04Kor-LB.tdb:GRAPHITE_A9, tdb:PdC-06Du.tdb:GRAPHITE_A9, tdb:PdC-20Jia.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (3): PHASE and CONSTITUENT statements as written

[PdC-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-04Kor-LB.tdb): GRAPHITE_A9, type code %, sha256 `f28cef69e245166a…`

~~~~text
47: PHASE GRAPHITE_A9 % 1 1 !
48: CONST GRAPHITE_A9 : C : !
~~~~

[PdC-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-06Du.tdb): GRAPHITE_A9, type code %, sha256 `53286c4307480550…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C% PD : !
~~~~

[PdC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-20Jia.tdb): GRAPHITE_A9, type code %, sha256 `321588b3daac71cd…`

~~~~text
44: PHASE GRAPHITE_A9 % 1 1 !
45: CONST GRAPHITE_A9 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1021/j100839a028](https://doi.org/10.1021/j100839a028) M. R. Nadler, Charles P. Kempter, SOME SOLIDUS TEMPERATURES IN SEVERAL METAL—CARBON SYSTEMS, J. Phys. Chem. 64, 1468-1471 (1960).  
_cited as the source of values for this phase_

## BCC_A2 (C–Pd)

- Id: `phase:c-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pd:bcc-a2)

Names (4): _corpus: _corpus:phase:c-pd:bcc-a2  
_tdb: _tdb:PdC-04Kor-LB.tdb:BCC_A2, tdb:PdC-06Du.tdb:BCC_A2, tdb:PdC-20Jia.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[PdC-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-04Kor-LB.tdb): BCC_A2, type code %B, sha256 `f28cef69e245166a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PD : C VA% : !
~~~~

[PdC-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-06Du.tdb): BCC_A2, type code %B, sha256 `53286c4307480550…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : PD : C VA% : !
~~~~

[PdC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-20Jia.tdb): BCC_A2, type code %B, sha256 `321588b3daac71cd…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : PD : C VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase_

## FCC_A1 (C–Pd)

- Id: `phase:c-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1828.77 K, x(C) 0–0.08565
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pd:fcc-a1)

Names (5): _corpus: _corpus:phase:c-pd:fcc-a1  
_paper: _paper:10.1016/j.intermet.2005.09.008:fcc(Pd)  
_tdb: _tdb:PdC-04Kor-LB.tdb:FCC_A1, tdb:PdC-06Du.tdb:FCC_A1, tdb:PdC-20Jia.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[PdC-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-04Kor-LB.tdb): FCC_A1, type code %A, sha256 `f28cef69e245166a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PD : C VA% : !
~~~~

[PdC-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-06Du.tdb): FCC_A1, type code %A, sha256 `53286c4307480550…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : C PD% : VA : !
~~~~

[PdC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-20Jia.tdb): FCC_A1, type code %A, sha256 `321588b3daac71cd…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : PD : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1021/j100839a028](https://doi.org/10.1021/j100839a028) M. R. Nadler, Charles P. Kempter, SOME SOLIDUS TEMPERATURES IN SEVERAL METAL—CARBON SYSTEMS, J. Phys. Chem. 64, 1468-1471 (1960).  
_cited as the source of values for this phase_

## HCP_A3 (C–Pd)

- Id: `phase:c-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pd:hcp-a3)

Names (4): _corpus: _corpus:phase:c-pd:hcp-a3  
_tdb: _tdb:PdC-04Kor-LB.tdb:HCP_A3, tdb:PdC-06Du.tdb:HCP_A3, tdb:PdC-20Jia.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[PdC-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-04Kor-LB.tdb): HCP_A3, type code %A, sha256 `f28cef69e245166a…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PD : C VA% : !
~~~~

[PdC-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-06Du.tdb): HCP_A3, type code %A, sha256 `53286c4307480550…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : PD : C VA% : !
~~~~

[PdC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-20Jia.tdb): HCP_A3, type code %A, sha256 `321588b3daac71cd…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : PD : C VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase_

## LIQUID (C–Pd)

- Id: `phase:c-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1765.16–4000 K, x(C) 0–0.62447
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pd:liquid)

Names (5): _corpus: _corpus:phase:c-pd:liquid  
_paper: _paper:10.1016/j.intermet.2005.09.008:L  
_tdb: _tdb:PdC-04Kor-LB.tdb:LIQUID, tdb:PdC-06Du.tdb:LIQUID, tdb:PdC-20Jia.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[PdC-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-04Kor-LB.tdb): LIQUID, type code %, sha256 `f28cef69e245166a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : C PD : !
~~~~

[PdC-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-06Du.tdb): LIQUID, type code %, sha256 `53286c4307480550…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C PD : !
~~~~

[PdC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdC-20Jia.tdb): LIQUID, type code %, sha256 `321588b3daac71cd…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : C PD : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1021/j100839a028](https://doi.org/10.1021/j100839a028) M. R. Nadler, Charles P. Kempter, SOME SOLIDUS TEMPERATURES IN SEVERAL METAL—CARBON SYSTEMS, J. Phys. Chem. 64, 1468-1471 (1960).  
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
