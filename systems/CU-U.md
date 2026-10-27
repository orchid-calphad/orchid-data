# Cu–U system

> Cu–U system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-U.html · Markdown: https://data.orchid-project.org/systems/CU-U.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-U/CuU-19Sol.json) · [phases (7)](https://data.orchid-project.org/phases/pages/CU-U.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CU-U.html) · [Markdown](https://data.orchid-project.org/systems/CU-U.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuU-19Sol.tdb | L. Soldi, S. Gosse, A. Laplace, P. Bonnaillie, J. Schorne-Pinto, M. Roskosz, J. Alloys Compd., 799, 239-46(2019). [doi:10.1016/j.jallcom.2019.05.294](https://doi.org/10.1016/j.jallcom.2019.05.294) | `59e1b140f2a16d267dfc5650914fee9a772bb1fbb309a93375961b163601763b` | [viewer](https://orchid-project.org/phase-diagrams/#CU-U/CuU-19Sol.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuU-19Sol.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuU-19Sol.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuU-19Sol.tdb | 1353.39 | LIQUID (x(U) 0.18009) + LIQUID#2 (x(U) 0.95535) + BCC_A2 (x(U) 0.97899) |
| CuU-19Sol.tdb | 1320 | CU5U_C15B (x(U) 0.16667) + LIQUID (x(U) 0.17133) + BCC_A2 (x(U) 0.9799) |
| CuU-19Sol.tdb | 1320 | CU5U_C15B (x(U) 0.16667) + LIQUID (x(U) 0.17131) + BCC_A2 (x(U) 0.9799) |
| CuU-19Sol.tdb | 1213.61 | FCC_A1 (x(U) 0) + LIQUID (x(U) 0.06945) + CU5U_C15B (x(U) 0.16667) |
| CuU-19Sol.tdb | 1213.61 | FCC_A1 (x(U) 0) + LIQUID (x(U) 0.06944) + CU5U_C15B (x(U) 0.16667) |
| CuU-19Sol.tdb | 1050.92 | CU5U_C15B (x(U) 0.16667) + TETRAGONAL_U (x(U) 0.99191) + BCC_A2 (x(U) 0.99294) |
| CuU-19Sol.tdb | 930.66 | CU5U_C15B (x(U) 0.16667) + TETRAGONAL_U (x(U) 0.99548) + ORTHORHOMBIC_A20 (x(U) 1) |
| CuU-19Sol.tdb | 930.66 | CU5U_C15B (x(U) 0.16667) + TETRAGONAL_U (x(U) 0.99552) + ORTHORHOMBIC_A20 (x(U) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-U.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-U.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
