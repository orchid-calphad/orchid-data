# Mg–H system

> Mg–H system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-H.html · Markdown: https://data.orchid-project.org/systems/MG-H.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-H/MgH-07Pal.json) · [Markdown](https://data.orchid-project.org/systems/MG-H.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgH-07Pal.tdb | M. Palumbo, F.J. Torres, J.R. Ares, C. Pisani, J.F. Fernandez, M. Baricco, Calphad, 31, 457-67(2007). [doi:10.1016/j.calphad.2007.04.005](https://doi.org/10.1016/j.calphad.2007.04.005) | `8871b1dc6e5850f79984cd38316758cefba2697ac60c408204c4582ec43d76df` | [viewer](https://orchid-project.org/phase-diagrams/#MG-H/MgH-07Pal.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgH-07Pal.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgH-07Pal.json) |
| MgH-99Zen.tdb | K. Zeng, T. Klassen, W. Oelerich, R. Bormann, Int. J. Hydrogen Energy, 24, 989-1004(1999). [doi:10.1016/S0360-3199(98)00132-3](https://doi.org/10.1016/S0360-3199%2898%2900132-3) | `7133dff29673a4f119f1c857d0fdcf297f9f1524b17519bd9681899f27f01f87` | [viewer](https://orchid-project.org/phase-diagrams/#MG-H/MgH-99Zen.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgH-99Zen.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgH-99Zen.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MgH-07Pal.tdb | 922.77 | HCP_A3 (x(H) 7.200e-4) + LIQUID (x(H) 0.001) + GAS (x(H) 0.99808) |
| MgH-07Pal.tdb | 561.18 | HCP_A3 (x(H) 1.600e-4) + MGH2_C4 (x(H) 0.66667) + GAS (x(H) 1) |
| MgH-07Pal.tdb | 561.18 | HCP_A3 (x(H) 1.600e-4) + MGH2_C4 (x(H) 0.66667) + GAS (x(H) 1) |
| MgH-99Zen.tdb | 922.82 | HCP_A3 (x(H) 7.200e-4) + LIQUID (x(H) 9.400e-4) + GAS (x(H) 0.99808) |
| MgH-99Zen.tdb | 561.44 | HCP_A3 (x(H) 1.600e-4) + MGH2_C4 (x(H) 0.66667) + GAS (x(H) 1) |
| MgH-99Zen.tdb | 561.44 | HCP_A3 (x(H) 1.600e-4) + MGH2_C4 (x(H) 0.66667) + GAS (x(H) 1) |

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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
