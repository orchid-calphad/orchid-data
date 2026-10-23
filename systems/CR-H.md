# Cr–H system

> Cr–H system: 1 accepted literature values (other property 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-H.html · Markdown: https://data.orchid-project.org/systems/CR-H.md

1 accepted literature values from 1 paper(s) (experimental 1); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-H.json) · [CSV](https://data.orchid-project.org/systems/CR-H.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-H) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-H/CrH-22Dot.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CR-H.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-H.html) · [Markdown](https://data.orchid-project.org/systems/CR-H.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrH-22Dot.tdb | M. Dottor, J.-C. Crivello, J.-M. Joubert, Int. J. Hydrogen Energy, 47, 23293-309(2022). [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245) | `f1aa3481524abf0bf18221ba2f8c6c7abf0b84185e3761d3c75396c9a94ef94a` | [viewer](https://orchid-project.org/phase-diagrams/#CR-H/CrH-22Dot.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrH-22Dot.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrH-22Dot.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrH-22Dot.tdb | 2175.93 | BCC_A2 (x(H) 6.200e-4) + LIQUID (x(H) 0.00276) + GAS (x(H) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-H.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-H.json)

## Other properties

### Other property (1)

Table: Other property, Cr–H system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: enthalpy of desorption_ | 8.01 kJ/moleH | 298 | hexagonal monohydride | experimental | [1] Dottor 2022; _cites Randzio 1974_ | p. 4 | “The enthalpy of desorption at 298 K has been measured using calorimetry by Sieverts and Gotta \[62\] and Randzio and Bojarski \[63\] for the hexagonal monohydride. They found respectively 7.95 kJ/moleH for ~ CrH0.22 and an average value of 8.01 kJ/moleH for hydrides ranging from CrH0.37 to CrH0.49.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modeling of Cr and Cr–H systems up to high temperatures and high pressures, International Journal of Hydrogen Energy 47, 23293-23309 (2022). [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245)

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
