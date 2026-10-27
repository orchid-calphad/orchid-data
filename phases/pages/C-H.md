# C–H phases

> C–H system: 4 phases (tier A 1, liquid 1, gas 2); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-H.html · Markdown: https://data.orchid-project.org/phases/pages/C-H.md

4 phases (tier A 1, liquid 1, gas 2); 2 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-H) · [full JSON](https://data.orchid-project.org/phases/systems/C-H.json) · [C–H system page](https://data.orchid-project.org/systems/C-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–H system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [GRAPHITE_A9](#phase-c-h-a9-graphite); _phase:c-h:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3974.5 K, x(H) 0–0 | 0 | 1 |
| [GAS](#phase-c-h-gas); _phase:c-h:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–3974.5 K, x(H) 0–0.99941 | 0 | 1 |
| [H2GAS](#phase-c-h-h2gas); _phase:c-h:h2gas_ | gas | gas | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-c-h-liquid); _phase:c-h:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |

## GRAPHITE_A9 (C–H)

- Id: `phase:c-h:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–3974.5 K, x(H) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-h:a9-graphite)

Names (2): _corpus: _corpus:phase:c-h:a9-graphite  
_tdb: _tdb:CH-97SUB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (1): PHASE and CONSTITUENT statements as written

[CH-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/CH-97SUB.tdb): GRAPHITE_A9, type code %, sha256 `963d51b236f0d482…`

~~~~text
46: PHASE GRAPHITE_A9 % 1 1 !
47: CONST GRAPHITE_A9 : C : !
~~~~

## GAS (C–H)

- Id: `phase:c-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3974.5 K, x(H) 0–0.99941
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-h:gas)

Names (2): _corpus: _corpus:phase:c-h:gas  
_tdb: _tdb:CH-97SUB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CH-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/CH-97SUB.tdb): GAS, type code %, sha256 `963d51b236f0d482…`

~~~~text
49: PHASE GAS:G % 1 1 !
50: CONST GAS:G : C C2 C3 C4 C5 C60 CH3 CH4 C2H2 C2H3 C2H4 C2H5 C2H6 C3H6 C3H8
               C4H8 C4H10 C6H6 H H2 : !
~~~~

## H2GAS (C–H)

- Id: `phase:c-h:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-h:h2gas)

Names (2): _corpus: _corpus:phase:c-h:h2gas  
_tdb: _tdb:CH-97SUB.tdb:H2GAS  


### TDB models of H2GAS (1): PHASE and CONSTITUENT statements as written

[CH-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/CH-97SUB.tdb): H2GAS, type code %, sha256 `963d51b236f0d482…`

~~~~text
53: PHASE H2GAS % 1 1 !
54: CONST H2GAS : H2 : !
~~~~

## LIQUID (C–H)

- Id: `phase:c-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-h:liquid)

Names (2): _corpus: _corpus:phase:c-h:liquid  
_tdb: _tdb:CH-97SUB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CH-97SUB.tdb](https://orchid-project.org/data/databases/sgte-binary/CH-97SUB.tdb): LIQUID, type code %, sha256 `963d51b236f0d482…`

~~~~text
41: PHASE LIQUID:L % 1 1 !
42: CONST LIQUID:L : C H : !
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
