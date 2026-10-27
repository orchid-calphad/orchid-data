# N–O phases

> N–O system: 4 phases (liquid 1, gas 3); 1 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-O.html · Markdown: https://data.orchid-project.org/phases/pages/N-O.md

4 phases (liquid 1, gas 3); 1 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-O) · [full JSON](https://data.orchid-project.org/phases/systems/N-O.json) · [N–O system page](https://data.orchid-project.org/systems/N-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–O system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [GAS](#phase-n-o-gas); _phase:n-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0–1 | 0 | 1 |
| [LIQUID](#phase-n-o-liquid); _phase:n-o:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |
| [N2GAS](#phase-n-o-n2gas); _phase:n-o:n2gas_ | gas | gas | not stable in 1 calculated diagram(s) | 0 | 1 |
| [O2GAS](#phase-n-o-o2gas); _phase:n-o:o2gas_ | gas | gas | not stable in 1 calculated diagram(s) | 0 | 1 |

## GAS (N–O)

- Id: `phase:n-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-o:gas)

Names (2): _corpus: _corpus:phase:n-o:gas  
_tdb: _tdb:NO-97SUB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[NO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/NO-97SUB.tdb): GAS, type code %, sha256 `f4b2b9114b30b23e…`

~~~~text
36: PHASE GAS:G % 1 1 !
37: CONST GAS:G : N N2 N3 NO NO2 NO3 N2O N2O3 N2O4 N2O5 O O2% O3 : !
~~~~

## LIQUID (N–O)

- Id: `phase:n-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: N 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-o:liquid)

Names (2): _corpus: _corpus:phase:n-o:liquid  
_tdb: _tdb:NO-97SUB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/NO-97SUB.tdb): LIQUID, type code %, sha256 `f4b2b9114b30b23e…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : N : !
~~~~

## N2GAS (N–O)

- Id: `phase:n-o:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-o:n2gas)

Names (2): _corpus: _corpus:phase:n-o:n2gas  
_tdb: _tdb:NO-97SUB.tdb:N2GAS  


### TDB models of N2GAS (1): PHASE and CONSTITUENT statements as written

[NO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/NO-97SUB.tdb): N2GAS, type code %, sha256 `f4b2b9114b30b23e…`

~~~~text
39: PHASE N2GAS % 1 1 !
40: CONST N2GAS : N2 : !
~~~~

## O2GAS (N–O)

- Id: `phase:n-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-o:o2gas)

Names (2): _corpus: _corpus:phase:n-o:o2gas  
_tdb: _tdb:NO-97SUB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[NO-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/NO-97SUB.tdb): O2GAS, type code %, sha256 `f4b2b9114b30b23e…`

~~~~text
42: PHASE O2GAS % 1 1 !
43: CONST O2GAS : O2 : !
~~~~

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
