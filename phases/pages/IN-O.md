# In–O phases

> In–O system: 8 phases (tier A 5, liquid 1, gas 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-O.html · Markdown: https://data.orchid-project.org/phases/pages/IN-O.md

8 phases (tier A 5, liquid 1, gas 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-O) · [full JSON](https://data.orchid-project.org/phases/systems/IN-O.json) · [In–O system page](https://data.orchid-project.org/systems/IN-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–O system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-o-a6-tetragonal); _phase:in-o:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–303 K, x(O) 0–0 | 0 | 1 |
| [BCC_A2](#phase-in-o-bcc-a2); _phase:in-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-in-o-fcc-a1); _phase:in-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-in-o-gas); _phase:in-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1658.66–2293.05 K, x(O) 0.0002–0.33238 | 0 | 1 |
| [HCP_A3](#phase-in-o-hcp-a3); _phase:in-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [IN2O3_D53](#phase-in-o-in2o3-d53); _phase:in-o:in2o3-d53_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–715 K, x(O) 0.6–0.6 | 0 | 1 |
| [ION](#phase-in-o-ion); _phase:in-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1658.66–2293.05 K, x(O) 0–0.0761 | 0 | 1 |
| [O2GAS](#phase-in-o-o2gas); _phase:in-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–715 K, x(O) 1–1 | 0 | 1 |

## TETRAGONAL_A6 (In–O)

- Id: `phase:in-o:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–303 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-o:a6-tetragonal  
_tdb: _tdb:InO-06Iso.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): TETRAGONAL_A6, type code %, sha256 `0a94a17909d2d28d…`

~~~~text
59: PHASE TETRAGONAL_A6 % 1 1 !
60: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

## BCC_A2 (In–O)

- Id: `phase:in-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:bcc-a2)

Names (2): _corpus: _corpus:phase:in-o:bcc-a2  
_tdb: _tdb:InO-06Iso.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): BCC_A2, type code %B, sha256 `0a94a17909d2d28d…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : IN : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

## FCC_A1 (In–O)

- Id: `phase:in-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:fcc-a1)

Names (2): _corpus: _corpus:phase:in-o:fcc-a1  
_tdb: _tdb:InO-06Iso.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): FCC_A1, type code %A, sha256 `0a94a17909d2d28d…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : IN : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

## GAS (In–O)

- Id: `phase:in-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1658.66–2293.05 K, x(O) 0.0002–0.33238
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:gas)

Names (2): _corpus: _corpus:phase:in-o:gas  
_tdb: _tdb:InO-06Iso.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): GAS, type code %, sha256 `0a94a17909d2d28d…`

~~~~text
67: PHASE GAS:G % 1 1 !
68: CONST GAS:G : IN IN2 INO IN2O O O2% O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

## HCP_A3 (In–O)

- Id: `phase:in-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:hcp-a3)

Names (2): _corpus: _corpus:phase:in-o:hcp-a3  
_tdb: _tdb:InO-06Iso.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): HCP_A3, type code %A, sha256 `0a94a17909d2d28d…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : IN : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

## IN2O3_D53 (In–O)

- Id: `phase:in-o:in2o3-d53`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–715 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:in2o3-d53)

Names (2): _corpus: _corpus:phase:in-o:in2o3-d53  
_tdb: _tdb:InO-06Iso.tdb:IN2O3_D53  


### TDB models of IN2O3_D53 (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): IN2O3_D53, type code %, sha256 `0a94a17909d2d28d…`

~~~~text
64: PHASE IN2O3_D53:I % 2 2 3 !
65: CONST IN2O3_D53:I : IN+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

## ION (In–O)

- Id: `phase:in-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1658.66–2293.05 K, x(O) 0–0.0761
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:ion)

Names (2): _corpus: _corpus:phase:in-o:ion  
_tdb: _tdb:InO-06Iso.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): ION, type code %, sha256 `0a94a17909d2d28d…`

~~~~text
39: PHASE ION:Y % 2 1 1 !
40: CONST ION:Y : IN+3 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

## O2GAS (In–O)

- Id: `phase:in-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–715 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-o:o2gas)

Names (2): _corpus: _corpus:phase:in-o:o2gas  
_tdb: _tdb:InO-06Iso.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[InO-06Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/InO-06Iso.tdb): O2GAS, type code %, sha256 `0a94a17909d2d28d…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.11.083](https://doi.org/10.1016/j.jallcom.2005.11.083) I. Isomaeki, M. Haemaelaeinen, W. Gierlotka, B. Onderka, K. Fitzner, J. Alloys Compd., 422, 173-77(2006).  
_assessment that models this phase_

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
