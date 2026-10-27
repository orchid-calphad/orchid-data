# Se–Te phases

> Se–Te system: 3 phases (tier A 1, liquid 1, gas 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SE-TE.html · Markdown: https://data.orchid-project.org/phases/pages/SE-TE.md

3 phases (tier A 1, liquid 1, gas 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SE-TE) · [full JSON](https://data.orchid-project.org/phases/systems/SE-TE.json) · [Se–Te system page](https://data.orchid-project.org/systems/SE-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/SE-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Se–Te system (3)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-se-te-a8-hexagonal); _phase:se-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–722.66 K, x(Te) 0–1 | 0 | 3 |
| [GAS](#phase-se-te-gas); _phase:se-te:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 413.87–2500 K, x(Te) 0–1 | 0 | 1 |
| [LIQUID](#phase-se-te-liquid); _phase:se-te:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 493.97–2500 K, x(Te) 0–1 | 0 | 3 |

## HEXAGONAL_A8 (Se–Te)

- Id: `phase:se-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–722.66 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:se-te:a8-hexagonal  
_tdb: _tdb:SeTe-12Gie.tdb:HEXAGONAL_A8, tdb:SeTe-21Fik.tdb:HEXAGONAL_A8, tdb:SeTe-88Gho-LB.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (3): PHASE and CONSTITUENT statements as written

[SeTe-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SeTe-12Gie.tdb): HEXAGONAL_A8, type code %, sha256 `5ab5c2c49c0744c2…`

~~~~text
28: PHASE HEXAGONAL_A8 % 1 1 !
29: CONST HEXAGONAL_A8 : SE TE : !
~~~~

[SeTe-21Fik.tdb](https://orchid-project.org/data/databases/sgte-binary/SeTe-21Fik.tdb): HEXAGONAL_A8, type code %, sha256 `5d5099e229e71305…`

~~~~text
35: PHASE HEXAGONAL_A8 % 1 1 !
36: CONST HEXAGONAL_A8 : SE TE : !
~~~~

[SeTe-88Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SeTe-88Gho-LB.tdb): HEXAGONAL_A8, type code %, sha256 `a880e2b8c9d01444…`

~~~~text
48: PHASE HEXAGONAL_A8 % 1 1 !
49: CONST HEXAGONAL_A8 : SE TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(88)90010-7](https://doi.org/10.1016/0364-5916%2888%2990010-7) G. Ghosh, H.L. Lukas, L. Delaey, Calphad, 12, 295-99(1988).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102309](https://doi.org/10.1016/j.calphad.2021.102309) O. Fikar, J. Vrestal, A. Kroupa, S.-W. Chen, Calphad, 74, 102309(2021).  
_assessment that models this phase_
- [doi:10.3139/146.110677](https://doi.org/10.3139/146.110677) W. Gierlotka, W.-H. Wu, Int. J. Mater. Res., 103, 698-701(2012).  
_assessment that models this phase_

## GAS (Se–Te)

- Id: `phase:se-te:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 413.87–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-te:gas)

Names (2): _corpus: _corpus:phase:se-te:gas  
_tdb: _tdb:SeTe-88Gho-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SeTe-88Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SeTe-88Gho-LB.tdb): GAS, type code %, sha256 `a880e2b8c9d01444…`

~~~~text
51: PHASE GAS:G % 1 1 !
52: CONST GAS:G : SE SE2 SE3 SE4 SE5 SE6 SE7 SE8 TE TE2 TE3 TE4 TE5 TE6 TE7 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90010-7](https://doi.org/10.1016/0364-5916%2888%2990010-7) G. Ghosh, H.L. Lukas, L. Delaey, Calphad, 12, 295-99(1988).  
_assessment that models this phase_

## LIQUID (Se–Te)

- Id: `phase:se-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 493.97–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-te:liquid)

Names (4): _corpus: _corpus:phase:se-te:liquid  
_tdb: _tdb:SeTe-12Gie.tdb:LIQUID, tdb:SeTe-21Fik.tdb:LIQUID, tdb:SeTe-88Gho-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[SeTe-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/SeTe-12Gie.tdb): LIQUID, type code %, sha256 `5ab5c2c49c0744c2…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SE TE : !
~~~~

[SeTe-21Fik.tdb](https://orchid-project.org/data/databases/sgte-binary/SeTe-21Fik.tdb): LIQUID, type code %, sha256 `5d5099e229e71305…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : SE SETE TE : !
~~~~

[SeTe-88Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SeTe-88Gho-LB.tdb): LIQUID, type code %, sha256 `a880e2b8c9d01444…`

~~~~text
43: PHASE LIQUID:L % 1 1 !
44: CONST LIQUID:L : SE TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(88)90010-7](https://doi.org/10.1016/0364-5916%2888%2990010-7) G. Ghosh, H.L. Lukas, L. Delaey, Calphad, 12, 295-99(1988).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102309](https://doi.org/10.1016/j.calphad.2021.102309) O. Fikar, J. Vrestal, A. Kroupa, S.-W. Chen, Calphad, 74, 102309(2021).  
_assessment that models this phase_
- [doi:10.3139/146.110677](https://doi.org/10.3139/146.110677) W. Gierlotka, W.-H. Wu, Int. J. Mater. Res., 103, 698-701(2012).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
