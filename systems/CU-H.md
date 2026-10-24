# Cu–H system

> Cu–H system: 3 accepted literature values (formation 1, invariant reaction 1, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-H.html · Markdown: https://data.orchid-project.org/systems/CU-H.md

3 accepted literature values from 2 paper(s) (experimental 1, model 1, DFT 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-H.json) · [CSV](https://data.orchid-project.org/systems/CU-H.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-H) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-H/CuH-07Hua.json) · [phases (7)](https://data.orchid-project.org/phases/pages/CU-H.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CU-H.html) · [Markdown](https://data.orchid-project.org/systems/CU-H.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |
| DFT | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 1 |
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuH-07Hua.tdb | W. Huang, S.M. Opalka, D. Wang, T.B. Flanagan, Calphad, 31, 315-29(2007). [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) | `49646b7ec4a6535d616405ccf5bce8288d47239cace684665767942e4930c787` | [viewer](https://orchid-project.org/phase-diagrams/#CU-H/CuH-07Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuH-07Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuH-07Hua.json) |
| CuH-14Mag.tdb | H. Magnusson, K. Frisk, Calphad, 47, 148-60(2014). [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) | `631979327e19b67c8b99ea9c851020b231d3850f6fbf8ef19835cd6ee5e7a917` | [viewer](https://orchid-project.org/phase-diagrams/#CU-H/CuH-14Mag.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuH-14Mag.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuH-07Hua.tdb | 1357.59 | FCC_A1 (x(H) 1.000e-4) + LIQUID (x(H) 2.600e-4) + GAS (x(H) 1) |
| CuH-14Mag.tdb | 1357.53 | FCC_A1 (x(H) 9.000e-5) + LIQUID (x(H) 3.000e-4) + GAS (x(H) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-H.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-H.json) · [CALPHAD hull CuH-07Hua](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-H--CuH-07Hua.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–H system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1348.15 | eutectic: L = H2 + (Cu) |  | experimental | [1] Huang 2007; _cites Massalski 1990_ | p. 3 | “The Cu-H phase diagram has a simple eutectic L = H2 + (Cu) at 1075 ◦ C with ∼0.2 at.%H in fcc and ∼0.6 at.%H in the liquid at 50 MPa, as shown in Fig. 4.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cu–H system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CuH bcc |  | 12.08 kJ/mol-atom | 298.15 | DFT |  |  | [1] Huang 2007 | Table 2, p. 6, row 2 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Cu–H system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1357 K | 1357 | other | model | [2] Magnusson 2014; _cites Lyman 1973_ | p. 3 | “This solubility increases with temperature and reaches a maximum at the liquidus of 0.01 at% at 1357 K \[28\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007). [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002)
2. Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014). [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004)

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
