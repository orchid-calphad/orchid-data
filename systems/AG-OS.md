# Ag–Os system

> Ag–Os system: 1 accepted literature values (phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-OS.html · Markdown: https://data.orchid-project.org/systems/AG-OS.md

1 accepted literature values from 1 paper(s) (experimental 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-OS.json) · [CSV](https://data.orchid-project.org/systems/AG-OS.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-OS) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-OS/AgOs-86Kar-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AG-OS.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-OS.html) · [Markdown](https://data.orchid-project.org/systems/AG-OS.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgOs-86Kar-LB.tdb | I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 7, 360-62(1986). [doi:10.1007/BF02873022](https://doi.org/10.1007/BF02873022) | `575874308ce082e522536fdf72947bd50f6f4e0c9344f445095a407f290cc906` | [viewer](https://orchid-project.org/phase-diagrams/#AG-OS/AgOs-86Kar-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgOs-86Kar-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgOs-86Kar-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgOs-86Kar-LB.tdb | 3107.11 | LIQUID (x(Os) 0.29634) + LIQUID#2 (x(Os) 0.77444) + HCP_A3 (x(Os) 0.99997) |
| AgOs-86Kar-LB.tdb | 1234.43 | FCC_A1 (x(Os) 3.000e-5) + LIQUID (x(Os) 4.700e-4) + HCP_A3 (x(Os) 0.99994) |
| AgOs-86Kar-LB.tdb | 1234.43 | FCC_A1 (x(Os) 3.000e-5) + LIQUID (x(Os) 4.700e-4) + HCP_A3 (x(Os) 0.99994) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-OS.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-OS.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Ag–Os system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2173.15 K | 2173.15 | other | experimental | [1] Karakaya 1986; _cites ref. 59Rud_ | p. 3 | “A monotectic reaction was reported at about 1900 ~ and near 20 at.% Ag \[59Rud\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Karakaya, W. T. Thompson, The Ag−Os (Silver-Osmium) system, Bulletin of Alloy Phase Diagrams 7, 360-362 (1986). [doi:10.1007/bf02873022](https://doi.org/10.1007/bf02873022)

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
