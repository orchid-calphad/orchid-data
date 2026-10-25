# Cu–Li phases

> Cu–Li system: 5 phases (tier A 3, liquid 1, unresolved_no_candidates 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-LI.html · Markdown: https://data.orchid-project.org/phases/pages/CU-LI.md

5 phases (tier A 3, liquid 1, unresolved_no_candidates 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-LI) · [full JSON](https://data.orchid-project.org/phases/systems/CU-LI.json) · [Cu–Li system page](https://data.orchid-project.org/systems/CU-LI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-LI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Li system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-li-bcc-a2); _phase:cu-li:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.85 K, x(Li) 0.99991–1 | 1 | 3 |
| [CU2LI3](#phase-cu-li-cu2li3); _phase:cu-li:cu2li3_ |  | unresolved_no_candidates | not stable in 1 calculated diagram(s) | 1 | 1 |
| [FCC_A1](#phase-cu-li-fcc-a1); _phase:cu-li:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Li) 0–0.83237 | 39 | 3 |
| [HCP_A3](#phase-cu-li-hcp-a3); _phase:cu-li:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-cu-li-liquid); _phase:cu-li:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 453.56–2500 K, x(Li) 0–1 | 18 | 3 |

## BCC_A2 (Cu–Li)

- Id: `phase:cu-li:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.85 K, x(Li) 0.99991–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-li:bcc-a2)

Names (5): _corpus: _corpus:phase:cu-li:bcc-a2  
_paper: _paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:CuLi-09Gas.tdb:BCC_A2, tdb:CuLi-16Li.tdb:BCC_A2, tdb:CuLi-98Sau-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CuLi-09Gas.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-09Gas.tdb): BCC_A2, type code %B, sha256 `1b32f2fc93785070…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CU LI% : VA : !
~~~~

[CuLi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-16Li.tdb): BCC_A2, type code %B, sha256 `f42782ad44b9e515…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CU LI% : VA : !
~~~~

[CuLi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-98Sau-LB.tdb): BCC_A2, type code %B, sha256 `d46bb41de43190bd…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CU LI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.10.006](https://doi.org/10.1016/j.calphad.2008.10.006) W. Gąsior, B. Onderka, Z. Moser, A. Dębski, T. Gancarz, Thermodynamic evaluation of Cu–Li phase diagram from EMF measurements and DTA study, Calphad 33, 215-220 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.003](https://doi.org/10.1016/j.calphad.2016.04.003) D. Li, S. Fuertauer, H. Flandorfer, D.M. Cupid, Calphad, 53, 105-15(2016).  
_assessment that models this phase_

## CU2LI3 (Cu–Li)

- Id: `phase:cu-li:cu2li3`; status `unresolved_no_candidates`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Stoichiometry: Cu 0.4000, Li 0.6000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-li:cu2li3)

Names (3): _corpus: _corpus:phase:cu-li:cu2li3  
_paper: _paper:10.1016/j.calphad.2008.10.006:Cu2Li3  
_tdb: _tdb:CuLi-09Gas.tdb:CU2LI3  


### TDB models of CU2LI3 (1): PHASE and CONSTITUENT statements as written

[CuLi-09Gas.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-09Gas.tdb): CU2LI3, type code %, sha256 `1b32f2fc93785070…`

~~~~text
49: PHASE CU2LI3 % 2 2 3 !
50: CONST CU2LI3 : CU : LI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.10.006](https://doi.org/10.1016/j.calphad.2008.10.006) W. Gąsior, B. Onderka, Z. Moser, A. Dębski, T. Gancarz, Thermodynamic evaluation of Cu–Li phase diagram from EMF measurements and DTA study, Calphad 33, 215-220 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cu–Li)

- Id: `phase:cu-li:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Li) 0–0.83237
- Literature: 39 values (39 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-li:fcc-a1)

Names (6): _corpus: _corpus:phase:cu-li:fcc-a1  
_paper: _paper:10.1016/j.calphad.2008.10.006:fcc-(Cu), paper:sha256-85fd53a1a176b694:fcc-A1  
_tdb: _tdb:CuLi-09Gas.tdb:FCC_A1, tdb:CuLi-16Li.tdb:FCC_A1, tdb:CuLi-98Sau-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CuLi-09Gas.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-09Gas.tdb): FCC_A1, type code %A, sha256 `1b32f2fc93785070…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CU% LI : VA : !
~~~~

[CuLi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-16Li.tdb): FCC_A1, type code %A, sha256 `f42782ad44b9e515…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CU% LI : VA : !
~~~~

[CuLi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-98Sau-LB.tdb): FCC_A1, type code %A, sha256 `d46bb41de43190bd…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CU% LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.10.006](https://doi.org/10.1016/j.calphad.2008.10.006) W. Gąsior, B. Onderka, Z. Moser, A. Dębski, T. Gancarz, Thermodynamic evaluation of Cu–Li phase diagram from EMF measurements and DTA study, Calphad 33, 215-220 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.04.003](https://doi.org/10.1016/j.calphad.2016.04.003) D. Li, S. Fuertauer, H. Flandorfer, D.M. Cupid, Calphad, 53, 105-15(2016).  
_assessment that models this phase_

## HCP_A3 (Cu–Li)

- Id: `phase:cu-li:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-li:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-li:hcp-a3  
_tdb: _tdb:CuLi-09Gas.tdb:HCP_A3, tdb:CuLi-16Li.tdb:HCP_A3, tdb:CuLi-98Sau-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CuLi-09Gas.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-09Gas.tdb): HCP_A3, type code %A, sha256 `1b32f2fc93785070…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CU LI : VA: !
~~~~

[CuLi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-16Li.tdb): HCP_A3, type code %A, sha256 `f42782ad44b9e515…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CU LI : VA: !
~~~~

[CuLi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-98Sau-LB.tdb): HCP_A3, type code %A, sha256 `d46bb41de43190bd…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CU LI : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.10.006](https://doi.org/10.1016/j.calphad.2008.10.006) W. Gąsior, B. Onderka, Z. Moser, A. Dębski, T. Gancarz, Thermodynamic evaluation of Cu–Li phase diagram from EMF measurements and DTA study, Calphad 33, 215-220 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.003](https://doi.org/10.1016/j.calphad.2016.04.003) D. Li, S. Fuertauer, H. Flandorfer, D.M. Cupid, Calphad, 53, 105-15(2016).  
_assessment that models this phase_

## LIQUID (Cu–Li)

- Id: `phase:cu-li:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 453.56–2500 K, x(Li) 0–1
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-li:liquid)

Names (6): _corpus: _corpus:phase:cu-li:liquid  
_paper: _paper:10.1016/j.calphad.2008.10.006:liquid, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:CuLi-09Gas.tdb:LIQUID, tdb:CuLi-16Li.tdb:LIQUID, tdb:CuLi-98Sau-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CuLi-09Gas.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-09Gas.tdb): LIQUID, type code %, sha256 `1b32f2fc93785070…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CU LI : !
~~~~

[CuLi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-16Li.tdb): LIQUID, type code %, sha256 `f42782ad44b9e515…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CU LI : !
~~~~

[CuLi-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuLi-98Sau-LB.tdb): LIQUID, type code %, sha256 `d46bb41de43190bd…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CU LI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.10.006](https://doi.org/10.1016/j.calphad.2008.10.006) W. Gąsior, B. Onderka, Z. Moser, A. Dębski, T. Gancarz, Thermodynamic evaluation of Cu–Li phase diagram from EMF measurements and DTA study, Calphad 33, 215-220 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.04.003](https://doi.org/10.1016/j.calphad.2016.04.003) D. Li, S. Fuertauer, H. Flandorfer, D.M. Cupid, Calphad, 53, 105-15(2016).  
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
