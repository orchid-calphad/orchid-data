# Ba–Fe system

> Ba–Fe system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-FE.html · Markdown: https://data.orchid-project.org/systems/BA-FE.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-FE/BaFe-19Hal.json) · [phases (4)](https://data.orchid-project.org/phases/pages/BA-FE.html) · [Markdown](https://data.orchid-project.org/systems/BA-FE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaFe-19Hal.tdb | B. Hallstedt, unpublished, 2019. | `87597e2245e6d340e7f34b973e99fc660918eefffc87dc993db96dc031c13466` | [viewer](https://orchid-project.org/phase-diagrams/#BA-FE/BaFe-19Hal.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaFe-19Hal.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaFe-19Hal.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaFe-19Hal.tdb | 1810.95 | LIQUID#2 (x(Fe) 0.001) + LIQUID (x(Fe) 1) + BCC_A2 (x(Fe) 1) |
| BaFe-19Hal.tdb | 1810.95 | LIQUID#2 (x(Fe) 0.001) + LIQUID (x(Fe) 1) + BCC_A2 (x(Fe) 1) |
| BaFe-19Hal.tdb | 1810.95 | LIQUID#2 (x(Fe) 0.001) + BCC_A2 (x(Fe) 1) + LIQUID (x(Fe) 1) |
| BaFe-19Hal.tdb | 1667.47 | LIQUID (x(Fe) 5.100e-4) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| BaFe-19Hal.tdb | 1667.47 | LIQUID (x(Fe) 5.100e-4) + FCC_A1 (x(Fe) 1) + BCC_A2 (x(Fe) 1) |
| BaFe-19Hal.tdb | 1184.81 | LIQUID (x(Fe) 2.000e-5) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| BaFe-19Hal.tdb | 1184.81 | LIQUID (x(Fe) 2.000e-5) + FCC_A1 (x(Fe) 1) + BCC_A2 (x(Fe) 1) |
| BaFe-19Hal.tdb | 1000 | LIQUID (x(Fe) 0) + BCC_A2#2 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |
| BaFe-19Hal.tdb | 1000 | LIQUID (x(Fe) 0) + BCC_A2#2 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-FE.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
