# Tl–Se system

> Tl–Se system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TL-SE.html · Markdown: https://data.orchid-project.org/systems/TL-SE.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#TL-SE/TlSe-00Roe-LB.json) · [Markdown](https://data.orchid-project.org/systems/TL-SE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| TlSe-00Roe-LB.tdb | F. Roemermann, Y. Feutelais, S.G. Fries, R. Blachnik, Intermetallics, 8, 53-65(2000). | `8323ab45605996cf7b41f68f90d6e7f108d7e4f8b62a49b4ec8dbf3313ba8ecb` | [viewer](https://orchid-project.org/phase-diagrams/#TL-SE/TlSe-00Roe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/TlSe-00Roe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/TlSe-00Roe-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| TlSe-00Roe-LB.tdb | 646.4 | LIQUID#2 (x(Se) 0.01198) + LIQUID (x(Se) 0.32503) + TL5SE3 (x(Se) 0.33347) |
| TlSe-00Roe-LB.tdb | 587.32 | TL5SE3 (x(Se) 0.37197) + LIQUID (x(Se) 0.42431) + TLSE_BETA (x(Se) 0.5) |
| TlSe-00Roe-LB.tdb | 574.33 | BCC_A2 (x(Se) 0) + LIQUID (x(Se) 0.00415) + TL5SE3 (x(Se) 0.33347) |
| TlSe-00Roe-LB.tdb | 519.76 | BCC_A2 (x(Se) 0) + TL2SE (x(Se) 0.33333) + TL5SE3 (x(Se) 0.33393) |
| TlSe-00Roe-LB.tdb | 519.76 | BCC_A2 (x(Se) 0) + TL2SE (x(Se) 0.33333) + TL5SE3 (x(Se) 0.33394) |
| TlSe-00Roe-LB.tdb | 507 | HCP_A3 (x(Se) 0) + BCC_A2 (x(Se) 0) + TL2SE (x(Se) 0.33333) |
| TlSe-00Roe-LB.tdb | 492.76 | LIQUID (x(Se) 0.76122) + LIQUID#2 (x(Se) 0.99046) + HEXAGONAL_A8 (x(Se) 1) |
| TlSe-00Roe-LB.tdb | 475.38 | TLSE_BETA (x(Se) 0.5) + LIQUID (x(Se) 0.73142) + HEXAGONAL_A8 (x(Se) 1) |
| TlSe-00Roe-LB.tdb | 465.66 | TLSE_B37 (x(Se) 0.5) + TLSE_BETA (x(Se) 0.5) + HEXAGONAL_A8 (x(Se) 1) |
| TlSe-00Roe-LB.tdb | 465.66 | TL5SE3 (x(Se) 0.37201) + TLSE_B37 (x(Se) 0.5) + TLSE_BETA (x(Se) 0.5) |

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
