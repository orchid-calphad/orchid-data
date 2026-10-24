# Gd–Li system

> Gd–Li system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GD-LI.html · Markdown: https://data.orchid-project.org/systems/GD-LI.md

5 accepted literature values from 1 paper(s) (experimental 2, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GD-LI.json) · [CSV](https://data.orchid-project.org/systems/GD-LI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GD-LI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GD-LI/GdLi-01Kev-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/GD-LI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GD-LI.html) · [Markdown](https://data.orchid-project.org/systems/GD-LI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GdLi-01Kev-LB.tdb | D.G. Kevorkov, J. Groebner, R. Schmid-Fetzer, V.V. Pavlyuk, G.S. Dmytriv, O.I. Bodak, J. Phase Equilib., 22, 34-42(2001). [doi:10.1361/105497101770339274](https://doi.org/10.1361/105497101770339274) | `372dc79e5d5f91b9c687b80166f81b779729407479ab7d3e058d7dc308528e03` | [viewer](https://orchid-project.org/phase-diagrams/#GD-LI/GdLi-01Kev-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdLi-01Kev-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdLi-01Kev-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GdLi-01Kev-LB.tdb | 1491.46 | HCP_A3 (x(Li) 0.00354) + BCC_A2 (x(Li) 0.00674) + LIQUID (x(Li) 0.05069) |
| GdLi-01Kev-LB.tdb | 1174.56 | HCP_A3 (x(Li) 0.01441) + LIQUID#2 (x(Li) 0.32855) + LIQUID (x(Li) 0.94132) |
| GdLi-01Kev-LB.tdb | 453.69 | HCP_A3 (x(Li) 7.000e-5) + BCC_A2 (x(Li) 0.99981) + LIQUID (x(Li) 0.99997) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GD/GD-LI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GD/GD-LI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Gd–Li system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1524.15 | (βGd) = (αGd) + L | (βGd): Li 0.0043; (αGd): Li 0.002; L: Li 0.0333 | model | [1] Kevorkov 2001 | Table 1, p. 2, row 1 |  |
| 1181.15 | L = (αGd) + L' | L: Li 0.3565 | experimental | [1] Kevorkov 2001; _cites Ganiev 1998_ | Table 1, p. 2, row 2 |  |
| 1175.15 | L = (αGd) + L' | L: Li 0.3307; (αGd): Li 0.0145; L': Li 0.9456 | model | [1] Kevorkov 2001 | Table 1, p. 2, row 3 |  |
| 453.15 | L' = (αGd) + Li | L': Li 0.9998; (αGd): Li 0; Li: Li 0.9999 | model | [1] Kevorkov 2001 | Table 1, p. 2, row 5 |  |
| 450.15 | L' = (αGd) + Li | L': Li 0.9974 | experimental | [1] Kevorkov 2001; _cites Ganiev 1998_ | Table 1, p. 2, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. G. Kevorkov, J. Gröbner, R. Schmid-Fetzer, V. V. Pavlyuk, G. S. Dmytriv, O. I. Bodak, The ternary Gd-Li-Mg system: Phase diagram study and computational evaluation, JPE 22, 34-42 (2001). [doi:10.1361/105497101770339274](https://doi.org/10.1361/105497101770339274)

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
