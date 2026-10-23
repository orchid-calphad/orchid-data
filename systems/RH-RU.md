# Rh–Ru system

> Rh–Ru system: 1 accepted literature values (invariant reaction 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RH-RU.html · Markdown: https://data.orchid-project.org/systems/RH-RU.md

1 accepted literature values from 1 paper(s) (model 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/RH-RU.json) · [CSV](https://data.orchid-project.org/systems/RH-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RH-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RH-RU/RhRu-16Gos.json) · [phases (4)](https://data.orchid-project.org/phases/pages/RH-RU.html) · [Markdown](https://data.orchid-project.org/systems/RH-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| RhRu-16Gos.tdb | S. Gosse, N. Dupin, C. Gueneau, J.-C. Crivello, J.-M. Joubert, J. Nucl. Mater., 474, 163-73(2016). [doi:10.1016/j.jnucmat.2016.03.025](https://doi.org/10.1016/j.jnucmat.2016.03.025) | `6d3f3a5adc97d335c9cf0deee0ddf77953e6239172178f20ab296ffce67efb6e` | [viewer](https://orchid-project.org/phase-diagrams/#RH-RU/RhRu-16Gos.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/RhRu-16Gos.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/RhRu-16Gos.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| RhRu-16Gos.tdb | 2359.87 | LIQUID (x(Ru) 0.37848) + FCC_A1 (x(Ru) 0.40085) + HCP_A3 (x(Ru) 0.48194) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RH/RH-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RH/RH-RU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Rh–Ru system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2360 | peritectic |  | model | [1] Gossé 2016 | p. 6 | “The invariant compositions are respectively: 40.1 at.% Ru, 48.2 at.% Ru, 37.8 at.% Ru at the peritectic reaction calculated at 2360 K (Fig. 7).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. Gossé, N. Dupin, C. Guéneau, J.-C. Crivello, J.-M. Joubert, Thermodynamic assessment of the Pd Rh Ru system using calphad and first-principles methods, Journal of Nuclear Materials 474, 163-173 (2016). [doi:10.1016/j.jnucmat.2016.03.025](https://doi.org/10.1016/j.jnucmat.2016.03.025)

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
