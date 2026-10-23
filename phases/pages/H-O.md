# H–O phases

> H–O system: 4 phases (liquid 1, gas 3); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-O.html · Markdown: https://data.orchid-project.org/phases/pages/H-O.md

4 phases (liquid 1, gas 3); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-O) · [full JSON](https://data.orchid-project.org/phases/systems/H-O.json) · [H–O system page](https://data.orchid-project.org/systems/H-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–O system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [GAS](#phase-h-o-gas); _phase:h-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0–1 | 0 | 1 |
| [H2GAS](#phase-h-o-h2gas); _phase:h-o:h2gas_ | gas | gas | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-h-o-liquid); _phase:h-o:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–373.44 K, x(O) 0.33333–0.33333 | 0 | 1 |
| [O2GAS](#phase-h-o-o2gas); _phase:h-o:o2gas_ | gas | gas | not stable in 1 calculated diagram(s) | 0 | 1 |

## GAS (H–O)

- Id: `phase:h-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-o:gas)

Names (2): _corpus: _corpus:phase:h-o:gas  
_tdb: _tdb:HO-97SUB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[HO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/HO-97SUB.tdb): GAS, type code %, sha256 `b481d8010be99a89…`

~~~~text
32: PHASE GAS:G % 1 1 !
33: CONST GAS:G : H H2 H1O1 H1O2 H2O H2O2 O O2% O3 : !
~~~~

## H2GAS (H–O)

- Id: `phase:h-o:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-o:h2gas)

Names (2): _corpus: _corpus:phase:h-o:h2gas  
_tdb: _tdb:HO-97SUB.tdb:H2GAS  


### TDB models of H2GAS (1): PHASE and CONSTITUENT statements as written

[HO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/HO-97SUB.tdb): H2GAS, type code %, sha256 `b481d8010be99a89…`

~~~~text
35: PHASE H2GAS % 1 1 !
36: CONST H2GAS : H2 : !
~~~~

## LIQUID (H–O)

- Id: `phase:h-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–373.44 K, x(O) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-o:liquid)

Names (2): _corpus: _corpus:phase:h-o:liquid  
_tdb: _tdb:HO-97SUB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/HO-97SUB.tdb): LIQUID, type code %, sha256 `b481d8010be99a89…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : H2O : !
~~~~

## O2GAS (H–O)

- Id: `phase:h-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-o:o2gas)

Names (2): _corpus: _corpus:phase:h-o:o2gas  
_tdb: _tdb:HO-97SUB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[HO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/HO-97SUB.tdb): O2GAS, type code %, sha256 `b481d8010be99a89…`

~~~~text
38: PHASE O2GAS % 1 1 !
39: CONST O2GAS : O2 : !
~~~~

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
