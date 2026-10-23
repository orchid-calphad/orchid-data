# H–Na phases

> H–Na system: 6 phases (tier A 4, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-NA.html · Markdown: https://data.orchid-project.org/phases/pages/H-NA.md

6 phases (tier A 4, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-NA) · [full JSON](https://data.orchid-project.org/phases/systems/H-NA.json) · [Markdown](https://data.orchid-project.org/phases/pages/H-NA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Na system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-na-bcc-a2); _phase:h-na:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–370.87 K, x(H) 0–0 | 0 | 2 |
| [FCC_A1](#phase-h-na-fcc-a1); _phase:h-na:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-h-na-gas); _phase:h-na:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1 | 0 | 2 |
| [HCP_A3](#phase-h-na-hcp-a3); _phase:h-na:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-h-na-liquid); _phase:h-na:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 370.87–1158.44 K, x(H) 0–0.00334 | 0 | 2 |
| [NAH_B1](#phase-h-na-nah-b1); _phase:h-na:nah-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–699.54 K, x(H) 0.5–0.5 | 0 | 2 |

## BCC_A2 (H–Na)

- Id: `phase:h-na:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–370.87 K, x(H) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-na:bcc-a2)

Names (3): _corpus: _corpus:phase:h-na:bcc-a2  
_tdb: _tdb:NaH-06Qiu.tdb:BCC_A2, tdb:NaH-93Pel.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NaH-06Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-06Qiu.tdb): BCC_A2, type code %B, sha256 `450ff68ec5e0694f…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : NA : H VA% : !
~~~~

[NaH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-93Pel.tdb): BCC_A2, type code %B, sha256 `efda4119d6909c2f…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0136](https://doi.org/10.3139/ijmr-2006-0136) C. Qiu, S.M. Opalka, G.B. Olson, D.L. Anton, Int. J. Mater. Res., 97, 845-53(2006).  
_assessment that models this phase_

## FCC_A1 (H–Na)

- Id: `phase:h-na:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-na:fcc-a1)

Names (3): _corpus: _corpus:phase:h-na:fcc-a1  
_tdb: _tdb:NaH-06Qiu.tdb:FCC_A1, tdb:NaH-93Pel.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NaH-06Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-06Qiu.tdb): FCC_A1, type code %A, sha256 `450ff68ec5e0694f…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : NA : VA : !
~~~~

[NaH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-93Pel.tdb): FCC_A1, type code %A, sha256 `efda4119d6909c2f…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0136](https://doi.org/10.3139/ijmr-2006-0136) C. Qiu, S.M. Opalka, G.B. Olson, D.L. Anton, Int. J. Mater. Res., 97, 845-53(2006).  
_assessment that models this phase_

## GAS (H–Na)

- Id: `phase:h-na:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-na:gas)

Names (3): _corpus: _corpus:phase:h-na:gas  
_tdb: _tdb:NaH-06Qiu.tdb:GAS, tdb:NaH-93Pel.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[NaH-06Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-06Qiu.tdb): GAS, type code %, sha256 `450ff68ec5e0694f…`

~~~~text
57: PHASE GAS:G % 1 1 !
58: CONST GAS:G : H H2 NA NA2 NAH : !
~~~~

[NaH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-93Pel.tdb): GAS, type code %, sha256 `efda4119d6909c2f…`

~~~~text
51: PHASE GAS:G % 1 1 !
52: CONST GAS:G : H H2 NA NA2 NAH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0136](https://doi.org/10.3139/ijmr-2006-0136) C. Qiu, S.M. Opalka, G.B. Olson, D.L. Anton, Int. J. Mater. Res., 97, 845-53(2006).  
_assessment that models this phase_

## HCP_A3 (H–Na)

- Id: `phase:h-na:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-na:hcp-a3)

Names (3): _corpus: _corpus:phase:h-na:hcp-a3  
_tdb: _tdb:NaH-06Qiu.tdb:HCP_A3, tdb:NaH-93Pel.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NaH-06Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-06Qiu.tdb): HCP_A3, type code %A, sha256 `450ff68ec5e0694f…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : NA : VA : !
~~~~

[NaH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-93Pel.tdb): HCP_A3, type code %A, sha256 `efda4119d6909c2f…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : NA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0136](https://doi.org/10.3139/ijmr-2006-0136) C. Qiu, S.M. Opalka, G.B. Olson, D.L. Anton, Int. J. Mater. Res., 97, 845-53(2006).  
_assessment that models this phase_

## LIQUID (H–Na)

- Id: `phase:h-na:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 370.87–1158.44 K, x(H) 0–0.00334
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-na:liquid)

Names (3): _corpus: _corpus:phase:h-na:liquid  
_tdb: _tdb:NaH-06Qiu.tdb:LIQUID, tdb:NaH-93Pel.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NaH-06Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-06Qiu.tdb): LIQUID, type code %, sha256 `450ff68ec5e0694f…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : H NA : !
~~~~

[NaH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-93Pel.tdb): LIQUID, type code %, sha256 `efda4119d6909c2f…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : NA NAH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0136](https://doi.org/10.3139/ijmr-2006-0136) C. Qiu, S.M. Opalka, G.B. Olson, D.L. Anton, Int. J. Mater. Res., 97, 845-53(2006).  
_assessment that models this phase_

## NAH_B1 (H–Na)

- Id: `phase:h-na:nah-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabjic and oqmd-642654, space group 225
- Stoichiometry: H 0.5000, Na 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–699.54 K, x(H) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-na:nah-b1)

Names (5): _corpus: _corpus:phase:h-na:nah-b1  
_mp: _mp:mp-aaaabjic  
_oqmd: _oqmd:oqmd-642654  
_tdb: _tdb:NaH-06Qiu.tdb:NAH_B1, tdb:NaH-93Pel.tdb:NAH_B1  


### TDB models of NAH_B1 (2): PHASE and CONSTITUENT statements as written

[NaH-06Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-06Qiu.tdb): NAH_B1, type code %, sha256 `450ff68ec5e0694f…`

~~~~text
54: PHASE NAH_B1 % 2 1 1 !
55: CONST NAH_B1 : NA : H : !
~~~~

[NaH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/NaH-93Pel.tdb): NAH_B1, type code %, sha256 `efda4119d6909c2f…`

~~~~text
48: PHASE NAH_B1 % 2 1 1 !
49: CONST NAH_B1 : NA : H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2006-0136](https://doi.org/10.3139/ijmr-2006-0136) C. Qiu, S.M. Opalka, G.B. Olson, D.L. Anton, Int. J. Mater. Res., 97, 845-53(2006).  
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
