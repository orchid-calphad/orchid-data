# Cd–Hg system

> Cd–Hg system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-HG.html · Markdown: https://data.orchid-project.org/systems/CD-HG.md

6 accepted literature values from 2 paper(s) (experimental 4, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-HG.json) · [CSV](https://data.orchid-project.org/systems/CD-HG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-HG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-HG/CdHg-95Yan-LB.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CD-HG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-HG.html) · [Markdown](https://data.orchid-project.org/systems/CD-HG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdHg-95Yan-LB.tdb | J. Yang, N.J. Silk, A. Watson, A.W. Bryant, T.G. Chart, B.B. Argent, Calphad, 19, 415-30(1995). [doi:10.1016/0364-5916(95)00039-H](https://doi.org/10.1016/0364-5916%2895%2900039-H) | `284289a9e34cef691c30bc763223c7a65862b588ea6f7fc050d5c8ff67fc3d46` | [viewer](https://orchid-project.org/phase-diagrams/#CD-HG/CdHg-95Yan-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdHg-95Yan-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdHg-95Yan-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdHg-95Yan-LB.tdb | 459.18 | HCP_A3 (x(Hg) 0.26036) + TETRAGONAL_A6 (x(Hg) 0.29794) + LIQUID (x(Hg) 0.36641) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-HG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-HG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Hg system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 461.15 | peritectic |  | experimental | [1] Yang 1995 | p. 3 | “A high temperature peritectic reaction is generally agreed to occur at 188°C between 27 and 36 at% Hg.” |
| 461.15 | ℓ + hcp -> ω | L: Hg 0.36; hcp: Hg 0.25; ω: Hg 0.29 | experimental | [2] Hansen 1998 | Table A2, p. 14, row 1 |  |
| 460.15 | ℓ + hcp -> ω | L: Hg 0.36; hcp: Hg 0.23; ω: Hg 0.29 | model | [2] Hansen 1998 | Table A2, p. 14, row 2 |  |
| 240.15 | ℓ + ω -> rhom | L: Hg 0.983; ω: Hg 0.88; rhom: Hg 0.961 | model | [2] Hansen 1998 | Table A2, p. 14, row 4 |  |
| 239.15 | peritectic |  | experimental | [1] Yang 1995; _cites Mehl 1930_ | p. 3 | “In 1930 Mehl et al. (5) extended investigations to higher Hg concentrations and using X-ray and thermal analysis methods discovered the presence of the rhombohedral primary solid solution and a peritectic reaction at -34°C from 88-97 at'/0Hg.” |
| 239.15 | ℓ + ω -> rhom | L: Hg 0.987; ω: Hg 0.88; rhom: Hg 0.965 | experimental | [2] Hansen 1998 | Table A2, p. 14, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Yang, N.J. Silk, A. Watson, A.W. Bryant, T.G. Chart, B.B. Argent, The thermodynamics and phase diagrams of the Cd-Hg and Cd-Hg-Te systems, Calphad 19, 415-430 (1995). [doi:10.1016/0364-5916(95)00039-h](https://doi.org/10.1016/0364-5916%2895%2900039-h)
2. S.C. Hansen, Thermodynamic assessment of binary Zn-Hg, Cd-Hg, AND In-Hg amalgams, Calphad 22, 359-373 (1998). [doi:10.1016/s0364-5916(98)00036-4](https://doi.org/10.1016/s0364-5916%2898%2900036-4)

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
