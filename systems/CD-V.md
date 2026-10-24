# Cd–V system

> Cd–V system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-V.html · Markdown: https://data.orchid-project.org/systems/CD-V.md

2 accepted literature values from 1 paper(s) (model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-V.json) · [CSV](https://data.orchid-project.org/systems/CD-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-V/CdV-13Zha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CD-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-V.html) · [Markdown](https://data.orchid-project.org/systems/CD-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdV-13Zha.tdb | C. Zhang, K. Cheng, W. Wang, X. Li, B. Hu, S. Liu, Y. Du, Calphad, 42, 6-12(2013). [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) | `453f03e1bb4572279d49fc69c621ff1f9c61a0458e1e8b97b9e28d734b145d08` | [viewer](https://orchid-project.org/phase-diagrams/#CD-V/CdV-13Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdV-13Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdV-13Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdV-13Zha.tdb | 2167.76 | LIQUID#2 (x(V) 0.00864) + LIQUID (x(V) 0.99136) + BCC_A2 (x(V) 1) |
| CdV-13Zha.tdb | 2167.76 | LIQUID (x(V) 0.00864) + LIQUID#2 (x(V) 0.99136) + BCC_A2 (x(V) 1) |
| CdV-13Zha.tdb | 594.22 | HCP_A3 (x(V) 0) + LIQUID (x(V) 0) + BCC_A2 (x(V) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–V system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1039.55 | Gas+(V) -> Liquid(Cd) | Gas: Cd 1; (V): Cd 0; Liquid(Cd): Cd 1 | model | [1] Zhang 2013 | Table 4, p. 5, row 31 |  |
| 594.25 | Liquid(Cd) -> (V)+(Cd) | Liquid(Cd): Cd 1; (V): Cd 0; (Cd): Cd 1 | model | [1] Zhang 2013 | Table 4, p. 5, row 30 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013). [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
