# Dy–H system

> Dy–H system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/DY-H.html · Markdown: https://data.orchid-project.org/systems/DY-H.md

2 accepted literature values from 1 paper(s) (model 2); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/DY-H.json) · [CSV](https://data.orchid-project.org/systems/DY-H.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#DY-H) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#DY-H/DyH-17Fu.json) · [phases (5)](https://data.orchid-project.org/phases/pages/DY-H.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/DY-H.html) · [Markdown](https://data.orchid-project.org/systems/DY-H.md)

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
| DyH-17Fu.tdb | K. Fu, G. Li, J. Li, Y. Liu, W. Tian, X. Li, J. Alloys Compd., 696, 60-66(2017). [doi:10.1016/j.jallcom.2016.11.182](https://doi.org/10.1016/j.jallcom.2016.11.182) | `ea03b6bab2ca6e277e6679210ee606a57ef95b56995a598cb8fddac4fd43b379` | [viewer](https://orchid-project.org/phase-diagrams/#DY-H/DyH-17Fu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/DyH-17Fu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/DyH-17Fu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| DyH-17Fu.tdb | 2048.53 | LIQUID (x(H) 0.00496) + HCP_A3 (x(H) 0.16639) + GAS (x(H) 1) |
| DyH-17Fu.tdb | 1685.26 | LIQUID (x(H) 4.000e-5) + BCC_A2 (x(H) 9.000e-5) + HCP_A3 (x(H) 0.00628) |
| DyH-17Fu.tdb | 1563.07 | HCP_A3 (x(H) 0.40757) + FCC_A1 (x(H) 0.51095) + GAS (x(H) 1) |
| DyH-17Fu.tdb | 649.57 | FCC_A1 (x(H) 0.68918) + HCP_A3 (x(H) 0.7499) + GAS (x(H) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/DY/DY-H.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/DY/DY-H.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Dy–H system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1625.75 | Hcp(Dy) +Gas(H2)→β-DyH2 | Hcp(Dy): H 0.367; Gas(H2): H 1; β-DyH2: H 0.458 | model | [1] Fu 2017 | Table 2, p. 6, row 2; `ORC-V2CWRMLR2S` |  |
| 641.05 | β-DyH2+Gas(H2)→γ-DyH3 | β-DyH2: H 0.694; Gas(H2): H 1; γ-DyH3: H 0.747 | model | [1] Fu 2017 | Table 2, p. 6, row 1; `ORC-223LPPM4CU` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Kai Fu, Guoling Li, Jigang Li, Yang Liu, Wenhuai Tian, Xingguo Li, Experimental study and thermodynamic assessment of the dysprosium-hydrogen binary system, Journal of Alloys and Compounds 696, 60-66 (2017). [doi:10.1016/j.jallcom.2016.11.182](https://doi.org/10.1016/j.jallcom.2016.11.182)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

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
