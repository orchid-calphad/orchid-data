# Pd–Ru system

> Pd–Ru system: 10 accepted literature values (invariant reaction 8, activity / EMF / Gibbs energy 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PD-RU.html · Markdown: https://data.orchid-project.org/systems/PD-RU.md

10 accepted literature values from 1 paper(s) (experimental 6, model 4); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PD-RU.json) · [CSV](https://data.orchid-project.org/systems/PD-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PD-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PD-RU/PdRu-16Gos.json) · [phases (4)](https://data.orchid-project.org/phases/pages/PD-RU.html) · [Markdown](https://data.orchid-project.org/systems/PD-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| activity / EMF / Gibbs energy | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PdRu-16Gos.tdb | S. Gosse, N. Dupin, C. Gueneau, J.-C. Crivello, J.-M. Joubert, J. Nucl. Mater., 474, 163-73(2016). [doi:10.1016/j.jnucmat.2016.03.025](https://doi.org/10.1016/j.jnucmat.2016.03.025) | `9a1ab65f3ae856616c7ac1cb262015b0a128cfacdc8c2f044266e07d26bd8bb2` | [viewer](https://orchid-project.org/phase-diagrams/#PD-RU/PdRu-16Gos.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PdRu-16Gos.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PdRu-16Gos.json) |
| PdRu-98Spe-LB.tdb | P.J. Spencer, unpublished work, 1998. | `3c7dd4a8054f74f4a50db24955ec681543429e9b4c8f907613601d85768e5112` | [viewer](https://orchid-project.org/phase-diagrams/#PD-RU/PdRu-98Spe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PdRu-98Spe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PdRu-98Spe-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PdRu-16Gos.tdb | 1867.28 | LIQUID (x(Ru) 0.13748) + FCC_A1 (x(Ru) 0.19156) + HCP_A3 (x(Ru) 0.93942) |
| PdRu-98Spe-LB.tdb | 1856.22 | LIQUID (x(Ru) 0.14566) + FCC_A1 (x(Ru) 0.17302) + HCP_A3 (x(Ru) 0.82653) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PD/PD-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PD/PD-RU.json) · [CALPHAD hull PdRu-98Spe-LB](https://data.orchid-project.org/hulls/calphad-sgte/PD/PD-RU--PdRu-98Spe-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pd–Ru system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1867 | peritectic: peritectic reaction | FCC: Ru 0.21 | experimental | [1] Gossé 2016; _cites Tripathi 1993_ | Table 1, p. 3, row 6 |  |
| 1867 | peritectic |  | model | [1] Gossé 2016 | p. 5 | “The peritectic reaction is calculated at 1867 K where the maximum solubilities are 19.2 at.% Ru in the FCC and 93.9 at.% Pd in the HCP solid solutions and the liquid composition is 13.7 at.% Ru.” |
| 1867 | peritectic: peritectic reaction | L: Ru 0.12; FCC: Ru 0.19; HCP: Ru 0.923 | experimental | [1] Gossé 2016; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 1, p. 3, row 2 |  |
| 1866 | peritectic: peritectic reaction | L: Ru 0.02; FCC: Ru 0.18; HCP: Ru 0.71 | experimental | [1] Gossé 2016; _cites Rudnitskii 1959_ | Table 1, p. 3, row 5 |  |
| 1866 | peritectic: peritectic reaction | L: Ru 0.1; FCC: Ru 0.185; HCP: Ru 0.923 | model | [1] Gossé 2016; _cites Gurler 1993_ [doi](https://doi.org/10.1016/0925-8388%2893%2990291-t) | Table 1, p. 3, row 7 |  |
| 1858 | peritectic: peritectic reaction | L: Ru 0.09; FCC: Ru 0.16; HCP: Ru 0.7 | experimental | [1] Gossé 2016; _cites Obrowski 1962_ | Table 1, p. 3, row 3 |  |
| 1856 | peritectic: peritectic reaction |  | experimental | [1] Gossé 2016; _cites Okamoto 1990_ | Table 1, p. 3, row 4 |  |
| 1852 | peritectic: peritectic reaction | FCC: Ru 0.18; HCP: Ru 0.83 | experimental | [1] Gossé 2016; _cites Darling 1960_ [doi](https://doi.org/10.1595/003214060x43104110) | Table 1, p. 3, row 1 |  |

## Other properties

### Activity / EMF / Gibbs energy (2)

Table: Activity / EMF / Gibbs energy, Pd–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity; _printed: activity_ | 0.99 unspecified | 1100 |  | model | [1] Gossé 2016 | p. 5 | “The calculated activity of Ru at 1100 K and 1200 K are about 0.99 while Kleykamp \[34\] reported an experimental value of 0.53.” |
| Activity; _printed: activity_ | 0.99 unspecified | 1200 |  | model | [1] Gossé 2016 | p. 5 | “The calculated activity of Ru at 1100 K and 1200 K are about 0.99 while Kleykamp \[34\] reported an experimental value of 0.53.” |

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
