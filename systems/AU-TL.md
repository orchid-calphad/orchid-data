# Au–Tl system

> Au–Tl system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-TL.html · Markdown: https://data.orchid-project.org/systems/AU-TL.md

5 accepted literature values from 1 paper(s) (experimental 3, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-TL.json) · [CSV](https://data.orchid-project.org/systems/AU-TL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-TL) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-TL/AuTl-89Che-LB.json) · [Markdown](https://data.orchid-project.org/systems/AU-TL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuTl-89Che-LB.tdb | P.-Y. Chevalier, Thermochim. Acta, 155, 211-25(1989). [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3) | `ae98194a9b82354076ee3ec20f96b2f8db8c13adfe018b8be0f7b83cecdd2108` | [viewer](https://orchid-project.org/phase-diagrams/#AU-TL/AuTl-89Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuTl-89Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuTl-89Che-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuTl-89Che-LB.tdb | 508.76 | LIQUID (x(Tl) 0.89429) + HCP_A3 (x(Tl) 0.99936) + BCC_A2 (x(Tl) 0.99966) |
| AuTl-89Che-LB.tdb | 415.44 | FCC_A1 (x(Tl) 0.00112) + LIQUID (x(Tl) 0.72338) + HCP_A3 (x(Tl) 0.99906) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-TL.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-TL.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Tl system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 418 | eutectic |  | model | [1] Chevalier 1989 | p. 10 | “The agreement is better for the eutectic temperature in the second case: T = 418 K, xrl = 0.722, for (a); T = 409 K, xn = 0.719, for (b), compared with T = 404 K \[25\] and T = 415 K \[27\].” |
| 415 | eutectic |  | experimental | [1] Chevalier 1989; _cites ref. 27_ | p. 4 | “There is eutectic reaction liquid (L) e f.c.c. + Tl h.c.p. and the eutectic point was located by Hajicek \[27\] at T = 415 K and xri = 0.708.” |
| 415 | eutectic |  | experimental | [1] Chevalier 1989; _cites ref. 27_ | p. 10 | “The agreement is better for the eutectic temperature in the second case: T = 418 K, xrl = 0.722, for (a); T = 409 K, xn = 0.719, for (b), compared with T = 404 K \[25\] and T = 415 K \[27\].” |
| 409 | eutectic |  | model | [1] Chevalier 1989 | p. 10 | “The agreement is better for the eutectic temperature in the second case: T = 418 K, xrl = 0.722, for (a); T = 409 K, xn = 0.719, for (b), compared with T = 404 K \[25\] and T = 415 K \[27\].” |
| 404 | eutectic |  | experimental | [1] Chevalier 1989; _cites Levin 1905_ [doi](https://doi.org/10.1002/zaac.19050450105) | p. 10 | “The agreement is better for the eutectic temperature in the second case: T = 418 K, xrl = 0.722, for (a); T = 409 K, xn = 0.719, for (b), compared with T = 404 K \[25\] and T = 415 K \[27\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Pierre-Yves Chevalier, A thermodynamic evaluation of the Au-Sb and Au-Tl systems, Thermochimica Acta 155, 211-225 (1989). [doi:10.1016/0040-6031(89)87147-3](https://doi.org/10.1016/0040-6031%2889%2987147-3)

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
