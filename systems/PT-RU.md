# Pt–Ru system

> Pt–Ru system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PT-RU.html · Markdown: https://data.orchid-project.org/systems/PT-RU.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PT-RU/PtRu-06Wat.json) · [Markdown](https://data.orchid-project.org/systems/PT-RU.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PtRu-06Wat.tdb | A. Watson, L.A. Cornish, R. Suess, Rare Met., 25, 597-607(2006). [doi:10.1016/S1001-0521(06)60106-X](https://doi.org/10.1016/S1001-0521%2806%2960106-X) | `bb1e1daaeffd72babe12f47a7c82ec8d31b18fa65596e893a5f9a9b0eadc3936` | [viewer](https://orchid-project.org/phase-diagrams/#PT-RU/PtRu-06Wat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PtRu-06Wat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PtRu-06Wat.json) |
| PtRu-98Spe-LB.tdb | P.J. Spencer, unpublished work, 1998. | `5097999c777fa9185197447e0a6ad1875217f7b62faa44ecabf9ba2e205d14c0` | [viewer](https://orchid-project.org/phase-diagrams/#PT-RU/PtRu-98Spe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PtRu-98Spe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PtRu-98Spe-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PtRu-06Wat.tdb | 2400.73 | FCC_A1 (x(Ru) 0.7258) + LIQUID (x(Ru) 0.73456) + HCP_A3 (x(Ru) 0.8093) |
| PtRu-98Spe-LB.tdb | 2456.5 | FCC_A1 (x(Ru) 0.70616) + LIQUID (x(Ru) 0.73441) + HCP_A3 (x(Ru) 0.79511) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PT/PT-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PT/PT-RU.json) · [CALPHAD hull PtRu-98Spe-LB](https://data.orchid-project.org/hulls/calphad-sgte/PT/PT-RU--PtRu-98Spe-LB.json)

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
