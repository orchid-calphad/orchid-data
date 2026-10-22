# Dy–C system

> Dy–C system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/DY-C.html · Markdown: https://data.orchid-project.org/systems/DY-C.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#DY-C/DyC-20Xu.json) · [Markdown](https://data.orchid-project.org/systems/DY-C.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| DyC-20Xu.tdb | K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020). [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) | `773f0d8f1049a3a6009833cb6c456b7b5c7a391888fb9a5d1e84df1b39940f7c` | [viewer](https://orchid-project.org/phase-diagrams/#DY-C/DyC-20Xu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/DyC-20Xu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| DyC-20Xu.tdb | 2543.94 | DYC2_C1 (x(C) 0.66667) + LIQUID (x(C) 0.6901) + GRAPHITE (x(C) 1) |
| DyC-20Xu.tdb | 2543.93 | DYC2_C1 (x(C) 0.66667) + LIQUID (x(C) 0.68979) + GRAPHITE (x(C) 1) |
| DyC-20Xu.tdb | 2543.93 | DYC2_C1 (x(C) 0.66667) + LIQUID (x(C) 0.68982) + GRAPHITE (x(C) 1) |
| DyC-20Xu.tdb | 1895.03 | LIQUID (x(C) 0.5077) + DY2C3_D5C (x(C) 0.6) + DYC2_C1 (x(C) 0.66667) |
| DyC-20Xu.tdb | 1895.03 | LIQUID (x(C) 0.50766) + DY2C3_D5C (x(C) 0.6) + DYC2_C1 (x(C) 0.66667) |
| DyC-20Xu.tdb | 1654.13 | HCP_A3 (x(C) 0) + BCC_A2 (x(C) 0) + LIQUID (x(C) 0.01623) |
| DyC-20Xu.tdb | 1568.63 | DY2C3_D5C (x(C) 0.6) + DYC2_C1 (x(C) 0.66667) + DYC2_C11A (x(C) 0.66667) |
| DyC-20Xu.tdb | 1568.63 | DYC2_C11A (x(C) 0.66667) + DYC2_C1 (x(C) 0.66667) + GRAPHITE (x(C) 1) |
| DyC-20Xu.tdb | 1212.54 | HCP_A3 (x(C) 0) + LIQUID (x(C) 0.27241) + DY2C3_D5C (x(C) 0.6) |
| DyC-20Xu.tdb | 1212.54 | HCP_A3 (x(C) 0) + LIQUID (x(C) 0.27238) + DY2C3_D5C (x(C) 0.6) |

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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
