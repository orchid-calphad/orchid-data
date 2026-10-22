# Bi–Co system

> Bi–Co system: 1 accepted literature values (invariant reaction 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-CO.html · Markdown: https://data.orchid-project.org/systems/BI-CO.md

1 accepted literature values from 1 paper(s) (experimental 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-CO.json) · [CSV](https://data.orchid-project.org/systems/BI-CO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-CO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-CO/BiCo-22Hu.json) · [Markdown](https://data.orchid-project.org/systems/BI-CO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiCo-22Hu.tdb | J. Hu, N. Su, X. Wang, F. Yin, X. Ouyang, Calphad, 77, 102404(2022). [doi:10.1016/j.calphad.2022.102404](https://doi.org/10.1016/j.calphad.2022.102404) | `02a7f22b117ad02f65c0850aeadcd1a9aaec5bed554c41c44f4396f17ee49c44` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CO/BiCo-22Hu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCo-22Hu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCo-22Hu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiCo-22Hu.tdb | 1639.73 | LIQUID (x(Co) 0.01782) + LIQUID#2 (x(Co) 0.88244) + FCC_A1 (x(Co) 0.99571) |
| BiCo-22Hu.tdb | 694.99 | LIQUID (x(Co) 0) + HCP_A3 (x(Co) 1) + FCC_A1 (x(Co) 1) |
| BiCo-22Hu.tdb | 694.83 | LIQUID (x(Co) 0) + FCC_A1 (x(Co) 0.99998) + HCP_A3 (x(Co) 1) |
| BiCo-22Hu.tdb | 544.55 | LIQUID (x(Co) 0) + RHOMBOHEDRAL_A7 (x(Co) 0) + HCP_A3 (x(Co) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-CO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-CO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Co system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 544.59 | eutectic |  | experimental | [1] Hu 2022 | p. 15 | “Except for the eutectic reaction temperature of 271.44 °C, the rest are dotted lines that indicating uncertain regions.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jingxian Hu, Na Su, Xinming Wang, Fucheng Yin, Xuemei Ouyang, Experimental investigation and thermodynamic calculation of the Co–Sn–Bi ternary system, Calphad 77, 102404 (2022). [doi:10.1016/j.calphad.2022.102404](https://doi.org/10.1016/j.calphad.2022.102404)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
