# Be–Si phases

> Be–Si system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BE-SI.html · Markdown: https://data.orchid-project.org/phases/pages/BE-SI.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BE-SI) · [full JSON](https://data.orchid-project.org/phases/systems/BE-SI.json) · [Be–Si system page](https://data.orchid-project.org/systems/BE-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/BE-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Be–Si system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-be-si-a4-diamond); _phase:be-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 1–1 | 0 | 2 |
| [BCC_A2](#phase-be-si-bcc-a2); _phase:be-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1526.52–1560 K, x(Si) 0–0.00054 | 0 | 2 |
| [FCC_A1](#phase-be-si-fcc-a1); _phase:be-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-be-si-hcp-a3); _phase:be-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1526.58 K, x(Si) 0–0.00095 | 0 | 2 |
| [LIQUID](#phase-be-si-liquid); _phase:be-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1357.8–2500 K, x(Si) 0–1 | 0 | 2 |

## DIAMOND_A4 (Be–Si)

- Id: `phase:be-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-si:a4-diamond)

Names (3): _corpus: _corpus:phase:be-si:a4-diamond  
_tdb: _tdb:BeSi-05Pan.tdb:DIAMOND_A4, tdb:BeSi-21Liu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[BeSi-05Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-05Pan.tdb): DIAMOND_A4, type code %, sha256 `11c4d80c4618b0da…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[BeSi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-21Liu.tdb): DIAMOND_A4, type code %, sha256 `10357ee109dbbac4…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00917-6](https://doi.org/10.1007/s11669-021-00917-6) Kun Liu, Peisheng Wang, Xiaozhong Huang, Haitang Yang, Yong Du, Experimental Investigation and Thermodynamic Calculation of the Be-C-Si System, J. Phase Equilib. Diffus. 42, 515-523 (2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2005-0227](https://doi.org/10.1515/ijmr-2005-0227) Z. Pan, Y. Du, B. Huang, Z. Metallkd., 96, 1301-7(2005).  
_assessment that models this phase_

## BCC_A2 (Be–Si)

- Id: `phase:be-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1526.52–1560 K, x(Si) 0–0.00054
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-si:bcc-a2)

Names (3): _corpus: _corpus:phase:be-si:bcc-a2  
_tdb: _tdb:BeSi-05Pan.tdb:BCC_A2, tdb:BeSi-21Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BeSi-05Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-05Pan.tdb): BCC_A2, type code %B, sha256 `11c4d80c4618b0da…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BE% SI : VA : !
~~~~

[BeSi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-21Liu.tdb): BCC_A2, type code %B, sha256 `10357ee109dbbac4…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : BE% SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00917-6](https://doi.org/10.1007/s11669-021-00917-6) Kun Liu, Peisheng Wang, Xiaozhong Huang, Haitang Yang, Yong Du, Experimental Investigation and Thermodynamic Calculation of the Be-C-Si System, J. Phase Equilib. Diffus. 42, 515-523 (2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2005-0227](https://doi.org/10.1515/ijmr-2005-0227) Z. Pan, Y. Du, B. Huang, Z. Metallkd., 96, 1301-7(2005).  
_assessment that models this phase_

## FCC_A1 (Be–Si)

- Id: `phase:be-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-si:fcc-a1)

Names (3): _corpus: _corpus:phase:be-si:fcc-a1  
_tdb: _tdb:BeSi-05Pan.tdb:FCC_A1, tdb:BeSi-21Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BeSi-05Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-05Pan.tdb): FCC_A1, type code %A, sha256 `11c4d80c4618b0da…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BE SI : VA : !
~~~~

[BeSi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-21Liu.tdb): FCC_A1, type code %A, sha256 `10357ee109dbbac4…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : BE SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00917-6](https://doi.org/10.1007/s11669-021-00917-6) Kun Liu, Peisheng Wang, Xiaozhong Huang, Haitang Yang, Yong Du, Experimental Investigation and Thermodynamic Calculation of the Be-C-Si System, J. Phase Equilib. Diffus. 42, 515-523 (2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2005-0227](https://doi.org/10.1515/ijmr-2005-0227) Z. Pan, Y. Du, B. Huang, Z. Metallkd., 96, 1301-7(2005).  
_assessment that models this phase_

## HCP_A3 (Be–Si)

- Id: `phase:be-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1526.58 K, x(Si) 0–0.00095
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-si:hcp-a3)

Names (3): _corpus: _corpus:phase:be-si:hcp-a3  
_tdb: _tdb:BeSi-05Pan.tdb:HCP_A3, tdb:BeSi-21Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BeSi-05Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-05Pan.tdb): HCP_A3, type code %A, sha256 `11c4d80c4618b0da…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BE% SI : VA : !
~~~~

[BeSi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-21Liu.tdb): HCP_A3, type code %A, sha256 `10357ee109dbbac4…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : BE% SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00917-6](https://doi.org/10.1007/s11669-021-00917-6) Kun Liu, Peisheng Wang, Xiaozhong Huang, Haitang Yang, Yong Du, Experimental Investigation and Thermodynamic Calculation of the Be-C-Si System, J. Phase Equilib. Diffus. 42, 515-523 (2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2005-0227](https://doi.org/10.1515/ijmr-2005-0227) Z. Pan, Y. Du, B. Huang, Z. Metallkd., 96, 1301-7(2005).  
_assessment that models this phase_

## LIQUID (Be–Si)

- Id: `phase:be-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1357.8–2500 K, x(Si) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-si:liquid)

Names (3): _corpus: _corpus:phase:be-si:liquid  
_tdb: _tdb:BeSi-05Pan.tdb:LIQUID, tdb:BeSi-21Liu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BeSi-05Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-05Pan.tdb): LIQUID, type code %, sha256 `11c4d80c4618b0da…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BE SI : !
~~~~

[BeSi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BeSi-21Liu.tdb): LIQUID, type code %, sha256 `10357ee109dbbac4…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : BE SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00917-6](https://doi.org/10.1007/s11669-021-00917-6) Kun Liu, Peisheng Wang, Xiaozhong Huang, Haitang Yang, Yong Du, Experimental Investigation and Thermodynamic Calculation of the Be-C-Si System, J. Phase Equilib. Diffus. 42, 515-523 (2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2005-0227](https://doi.org/10.1515/ijmr-2005-0227) Z. Pan, Y. Du, B. Huang, Z. Metallkd., 96, 1301-7(2005).  
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
