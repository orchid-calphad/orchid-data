# Pb–Zn phases

> Pb–Zn system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/PB-ZN.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/PB-ZN.json) · [Pb–Zn system page](https://data.orchid-project.org/systems/PB-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Zn system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pb-zn-bcc-a2); _phase:pb-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-pb-zn-fcc-a1); _phase:pb-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–600.61 K, x(Zn) 0–0.00265 | 8 | 4 |
| [HCP_A3](#phase-pb-zn-hcp-a3); _phase:pb-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–693.48 K, x(Zn) 0.99595–1 | 13 | 4 |
| [LIQUID](#phase-pb-zn-liquid); _phase:pb-zn:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 590.91–2500 K, x(Zn) 0–1 | 13 | 4 |

## BCC_A2 (Pb–Zn)

- Id: `phase:pb-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zn:bcc-a2)

Names (5): _corpus: _corpus:phase:pb-zn:bcc-a2  
_tdb: _tdb:PbZn-03Dav.tdb:BCC_A2, tdb:PbZn-03Kim.tdb:BCC_A2, tdb:PbZn-93Sri-LB.tdb:BCC_A2, tdb:PbZn-98Jan.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[PbZn-03Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Dav.tdb): BCC_A2, type code %B, sha256 `4d620daf5b35e9d9…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PB ZN : VA : !
~~~~

[PbZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Kim.tdb): BCC_A2, type code %B, sha256 `dc3fde6733831cf6…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : PB ZN : VA : !
~~~~

[PbZn-93Sri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-93Sri-LB.tdb): BCC_A2, type code %B, sha256 `7baa1c24737eb726…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : PB ZN : VA : !
~~~~

[PbZn-98Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-98Jan.tdb): BCC_A2, type code %B, sha256 `a00fd87820c8ecde…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PB ZN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00040-6](https://doi.org/10.1016/S0364-5916%2898%2900040-6) T. Jantzen, P.J. Spencer, Calphad, 22, 417-34(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_
- [doi:10.3139/146.030008](https://doi.org/10.3139/146.030008) N. David, J. Hertz, J.-M. Fiorani, Z. Metallkd., 94, 8-11(2003).  
_assessment that models this phase_

## FCC_A1 (Pb–Zn)

- Id: `phase:pb-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–600.61 K, x(Zn) 0–0.00265
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zn:fcc-a1)

Names (6): _corpus: _corpus:phase:pb-zn:fcc-a1  
_paper: _paper:10.1007/bf02667882:(Pb)  
_tdb: _tdb:PbZn-03Dav.tdb:FCC_A1, tdb:PbZn-03Kim.tdb:FCC_A1, tdb:PbZn-93Sri-LB.tdb:FCC_A1, tdb:PbZn-98Jan.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[PbZn-03Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Dav.tdb): FCC_A1, type code %A, sha256 `4d620daf5b35e9d9…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PB% ZN : VA : !
~~~~

[PbZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Kim.tdb): FCC_A1, type code %A, sha256 `dc3fde6733831cf6…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : PB% ZN : VA : !
~~~~

[PbZn-93Sri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-93Sri-LB.tdb): FCC_A1, type code %A, sha256 `7baa1c24737eb726…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : PB% ZN : VA : !
~~~~

[PbZn-98Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-98Jan.tdb): FCC_A1, type code %A, sha256 `a00fd87820c8ecde…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PB% ZN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00040-6](https://doi.org/10.1016/S0364-5916%2898%2900040-6) T. Jantzen, P.J. Spencer, Calphad, 22, 417-34(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_
- [doi:10.3139/146.030008](https://doi.org/10.3139/146.030008) N. David, J. Hertz, J.-M. Fiorani, Z. Metallkd., 94, 8-11(2003).  
_assessment that models this phase_

## HCP_A3 (Pb–Zn)

- Id: `phase:pb-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–693.48 K, x(Zn) 0.99595–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zn:hcp-a3)

Names (6): _corpus: _corpus:phase:pb-zn:hcp-a3  
_paper: _paper:10.1007/bf02667882:(Zn)  
_tdb: _tdb:PbZn-03Dav.tdb:HCP_A3, tdb:PbZn-03Kim.tdb:HCP_A3, tdb:PbZn-93Sri-LB.tdb:HCP_A3, tdb:PbZn-98Jan.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[PbZn-03Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Dav.tdb): HCP_A3, type code %A, sha256 `4d620daf5b35e9d9…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PB ZN% : VA : !
~~~~

[PbZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Kim.tdb): HCP_A3, type code %A, sha256 `dc3fde6733831cf6…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : PB ZN% : VA : !
~~~~

[PbZn-93Sri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-93Sri-LB.tdb): HCP_A3, type code %A, sha256 `7baa1c24737eb726…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : PB ZN% : VA : !
~~~~

[PbZn-98Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-98Jan.tdb): HCP_A3, type code %A, sha256 `a00fd87820c8ecde…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PB ZN% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00040-6](https://doi.org/10.1016/S0364-5916%2898%2900040-6) T. Jantzen, P.J. Spencer, Calphad, 22, 417-34(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_
- [doi:10.3139/146.030008](https://doi.org/10.3139/146.030008) N. David, J. Hertz, J.-M. Fiorani, Z. Metallkd., 94, 8-11(2003).  
_assessment that models this phase_

## LIQUID (Pb–Zn)

- Id: `phase:pb-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 590.91–2500 K, x(Zn) 0–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zn:liquid)

Names (7): _corpus: _corpus:phase:pb-zn:liquid  
_paper: _paper:10.1007/bf02667882:L1, paper:10.1007/bf02667882:L2  
_tdb: _tdb:PbZn-03Dav.tdb:LIQUID, tdb:PbZn-03Kim.tdb:LIQUID, tdb:PbZn-93Sri-LB.tdb:LIQUID, tdb:PbZn-98Jan.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[PbZn-03Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Dav.tdb): LIQUID, type code %, sha256 `4d620daf5b35e9d9…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PB ZN : !
~~~~

[PbZn-03Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-03Kim.tdb): LIQUID, type code %, sha256 `dc3fde6733831cf6…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : PB ZN : !
~~~~

[PbZn-93Sri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-93Sri-LB.tdb): LIQUID, type code %, sha256 `7baa1c24737eb726…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : PB ZN : !
~~~~

[PbZn-98Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZn-98Jan.tdb): LIQUID, type code %, sha256 `a00fd87820c8ecde…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PB ZN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00040-6](https://doi.org/10.1016/S0364-5916%2898%2900040-6) T. Jantzen, P.J. Spencer, Calphad, 22, 417-34(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2003-0070](https://doi.org/10.1515/ijmr-2003-0070) S.S. Kim, T.H. Sanders, Jr., Z. Metallkd., 94, 390-95(2003).  
_assessment that models this phase_
- [doi:10.3139/146.030008](https://doi.org/10.3139/146.030008) N. David, J. Hertz, J.-M. Fiorani, Z. Metallkd., 94, 8-11(2003).  
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
