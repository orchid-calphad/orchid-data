# Al–Ga phases

> Al–Ga system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-GA.html · Markdown: https://data.orchid-project.org/phases/pages/AL-GA.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-GA) · [full JSON](https://data.orchid-project.org/phases/systems/AL-GA.json) · [Al–Ga system page](https://data.orchid-project.org/systems/AL-GA.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Ga system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-al-ga-a11-orthorhombic); _phase:al-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 298.77–302.91 K, x(Ga) 1–1 | 0 | 3 |
| [BCC_A2](#phase-al-ga-bcc-a2); _phase:al-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-al-ga-fcc-a1); _phase:al-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–940 K, x(Ga) 0–0.09389 | 0 | 3 |
| [HCP_A3](#phase-al-ga-hcp-a3); _phase:al-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-al-ga-liquid); _phase:al-ga:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 298.77–2500 K, x(Ga) 0–1 | 0 | 3 |

## ORTHORHOMBIC_A11 (Al–Ga)

- Id: `phase:al-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 298.77–302.91 K, x(Ga) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ga:a11-orthorhombic)

Names (4): _corpus: _corpus:phase:al-ga:a11-orthorhombic  
_tdb: _tdb:AlGa-00Mat.tdb:ORTHORHOMBIC_A11, tdb:AlGa-78Ans.tdb:ORTHORHOMBIC_A11, tdb:AlGa-92Wat-LB.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (3): PHASE and CONSTITUENT statements as written

[AlGa-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-00Mat.tdb): ORTHORHOMBIC_A11, type code %, sha256 `4a1c4e2938a4b653…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[AlGa-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-78Ans.tdb): ORTHORHOMBIC_A11, type code %, sha256 `381170fa980b47b3…`

~~~~text
44: PHASE ORTHORHOMBIC_A11 % 1 1 !
45: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[AlGa-92Wat-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-92Wat-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `063ea10dc1895078…`

~~~~text
40: PHASE ORTHORHOMBIC_A11 % 1 1 !
41: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90009-M](https://doi.org/10.1016/0364-5916%2892%2990009-M) A. Watson, Calphad, 16, 207-17(1992).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## BCC_A2 (Al–Ga)

- Id: `phase:al-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ga:bcc-a2)

Names (4): _corpus: _corpus:phase:al-ga:bcc-a2  
_tdb: _tdb:AlGa-00Mat.tdb:BCC_A2, tdb:AlGa-78Ans.tdb:BCC_A2, tdb:AlGa-92Wat-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlGa-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-00Mat.tdb): BCC_A2, type code %B, sha256 `4a1c4e2938a4b653…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL GA : VA : !
~~~~

[AlGa-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-78Ans.tdb): BCC_A2, type code %B, sha256 `381170fa980b47b3…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL : VA : !
~~~~

[AlGa-92Wat-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-92Wat-LB.tdb): BCC_A2, type code %B, sha256 `063ea10dc1895078…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL GA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90009-M](https://doi.org/10.1016/0364-5916%2892%2990009-M) A. Watson, Calphad, 16, 207-17(1992).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## FCC_A1 (Al–Ga)

- Id: `phase:al-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–940 K, x(Ga) 0–0.09389
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ga:fcc-a1)

Names (4): _corpus: _corpus:phase:al-ga:fcc-a1  
_tdb: _tdb:AlGa-00Mat.tdb:FCC_A1, tdb:AlGa-78Ans.tdb:FCC_A1, tdb:AlGa-92Wat-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlGa-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-00Mat.tdb): FCC_A1, type code %A, sha256 `4a1c4e2938a4b653…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL GA : VA : !
~~~~

[AlGa-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-78Ans.tdb): FCC_A1, type code %A, sha256 `381170fa980b47b3…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL GA : VA : !
~~~~

[AlGa-92Wat-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-92Wat-LB.tdb): FCC_A1, type code %A, sha256 `063ea10dc1895078…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL GA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90009-M](https://doi.org/10.1016/0364-5916%2892%2990009-M) A. Watson, Calphad, 16, 207-17(1992).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## HCP_A3 (Al–Ga)

- Id: `phase:al-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ga:hcp-a3)

Names (4): _corpus: _corpus:phase:al-ga:hcp-a3  
_tdb: _tdb:AlGa-00Mat.tdb:HCP_A3, tdb:AlGa-78Ans.tdb:HCP_A3, tdb:AlGa-92Wat-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlGa-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-00Mat.tdb): HCP_A3, type code %A, sha256 `4a1c4e2938a4b653…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL GA : VA : !
~~~~

[AlGa-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-78Ans.tdb): HCP_A3, type code %A, sha256 `381170fa980b47b3…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL : VA : !
~~~~

[AlGa-92Wat-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-92Wat-LB.tdb): HCP_A3, type code %A, sha256 `063ea10dc1895078…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL GA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90009-M](https://doi.org/10.1016/0364-5916%2892%2990009-M) A. Watson, Calphad, 16, 207-17(1992).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## LIQUID (Al–Ga)

- Id: `phase:al-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 298.77–2500 K, x(Ga) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ga:liquid)

Names (4): _corpus: _corpus:phase:al-ga:liquid  
_tdb: _tdb:AlGa-00Mat.tdb:LIQUID, tdb:AlGa-78Ans.tdb:LIQUID, tdb:AlGa-92Wat-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlGa-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-00Mat.tdb): LIQUID, type code %, sha256 `4a1c4e2938a4b653…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL GA : !
~~~~

[AlGa-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-78Ans.tdb): LIQUID, type code %, sha256 `381170fa980b47b3…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL GA : !
~~~~

[AlGa-92Wat-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGa-92Wat-LB.tdb): LIQUID, type code %, sha256 `063ea10dc1895078…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90009-M](https://doi.org/10.1016/0364-5916%2892%2990009-M) A. Watson, Calphad, 16, 207-17(1992).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
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
