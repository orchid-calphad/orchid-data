# In–Zn phases

> In–Zn system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/IN-ZN.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/IN-ZN.json) · [In–Zn system page](https://data.orchid-project.org/systems/IN-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Zn system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-zn-a6-tetragonal); _phase:in-zn:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Zn) 0–0.01037 | 0 | 1 |
| [BCC_A2](#phase-in-zn-bcc-a2); _phase:in-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-in-zn-fcc-a1); _phase:in-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-in-zn-hcp-a3); _phase:in-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–692.68 K, x(Zn) 0.99324–1 | 0 | 1 |
| [LIQUID](#phase-in-zn-liquid); _phase:in-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 416.75–2500 K, x(Zn) 0–1 | 0 | 1 |

## TETRAGONAL_A6 (In–Zn)

- Id: `phase:in-zn:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Zn) 0–0.01037
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-zn:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-zn:a6-tetragonal  
_tdb: _tdb:InZn-96Lee-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InZn-96Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InZn-96Lee-LB.tdb): TETRAGONAL_A6, type code %, sha256 `d5b7b63e5300ab66…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : IN% ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_

## BCC_A2 (In–Zn)

- Id: `phase:in-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-zn:bcc-a2)

Names (2): _corpus: _corpus:phase:in-zn:bcc-a2  
_tdb: _tdb:InZn-96Lee-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InZn-96Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InZn-96Lee-LB.tdb): BCC_A2, type code %B, sha256 `d5b7b63e5300ab66…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : IN ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_

## FCC_A1 (In–Zn)

- Id: `phase:in-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-zn:fcc-a1)

Names (2): _corpus: _corpus:phase:in-zn:fcc-a1  
_tdb: _tdb:InZn-96Lee-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InZn-96Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InZn-96Lee-LB.tdb): FCC_A1, type code %A, sha256 `d5b7b63e5300ab66…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : IN ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_

## HCP_A3 (In–Zn)

- Id: `phase:in-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–692.68 K, x(Zn) 0.99324–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-zn:hcp-a3)

Names (2): _corpus: _corpus:phase:in-zn:hcp-a3  
_tdb: _tdb:InZn-96Lee-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InZn-96Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InZn-96Lee-LB.tdb): HCP_A3, type code %A, sha256 `d5b7b63e5300ab66…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : IN ZN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_

## LIQUID (In–Zn)

- Id: `phase:in-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 416.75–2500 K, x(Zn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-zn:liquid)

Names (2): _corpus: _corpus:phase:in-zn:liquid  
_tdb: _tdb:InZn-96Lee-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InZn-96Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InZn-96Lee-LB.tdb): LIQUID, type code %, sha256 `d5b7b63e5300ab66…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : IN ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
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
