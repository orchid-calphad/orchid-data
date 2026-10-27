# F–O phases

> F–O system: 2 phases (gas 2); 1 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/F-O.html · Markdown: https://data.orchid-project.org/phases/pages/F-O.md

2 phases (gas 2); 1 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=F-O) · [full JSON](https://data.orchid-project.org/phases/systems/F-O.json) · [F–O system page](https://data.orchid-project.org/systems/F-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/F-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the F–O system (2)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [GAS](#phase-f-o-gas); _phase:f-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0–1 | 0 | 1 |
| [O2GAS](#phase-f-o-o2gas); _phase:f-o:o2gas_ | gas | gas | not stable in 1 calculated diagram(s) | 0 | 1 |

## GAS (F–O)

- Id: `phase:f-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-o:gas)

Names (2): _corpus: _corpus:phase:f-o:gas  
_tdb: _tdb:FO-97SUB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[FO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/FO-97SUB.tdb): GAS, type code %, sha256 `62071db1ae5318a6…`

~~~~text
31: PHASE GAS:G % 1 1 !
32: CONST GAS:G : F F2 FO FO2 F2O F2O2 O O2% O3 : !
~~~~

## O2GAS (F–O)

- Id: `phase:f-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-o:o2gas)

Names (2): _corpus: _corpus:phase:f-o:o2gas  
_tdb: _tdb:FO-97SUB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[FO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/FO-97SUB.tdb): O2GAS, type code %, sha256 `62071db1ae5318a6…`

~~~~text
34: PHASE O2GAS % 1 1 !
35: CONST O2GAS : O2 : !
~~~~

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
