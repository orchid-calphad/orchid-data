# Co–In system

> Co–In system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-IN.html · Markdown: https://data.orchid-project.org/systems/CO-IN.md

10 accepted literature values from 1 paper(s) (experimental 5, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-IN.json) · [CSV](https://data.orchid-project.org/systems/CO-IN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-IN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-IN/CoIn-01Boa-LB.json) · [phases (7)](https://data.orchid-project.org/phases/pages/CO-IN.html) · [Markdown](https://data.orchid-project.org/systems/CO-IN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoIn-01Boa-LB.tdb | D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001). [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) | `7b7830ea54945b1a2bbabec1211bb2d7cfacd42bc1795986f3e3d08861026762` | [viewer](https://orchid-project.org/phase-diagrams/#CO-IN/CoIn-01Boa-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoIn-01Boa-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoIn-01Boa-LB.tdb | 1558.24 | FCC_A1 (x(In) 4.000e-5) + LIQUID#2 (x(In) 0.23215) + LIQUID (x(In) 0.91941) |
| CoIn-01Boa-LB.tdb | 824.26 | FCC_A1 (x(In) 0) + COIN2_CB (x(In) 0.66667) + LIQUID (x(In) 0.99858) |
| CoIn-01Boa-LB.tdb | 824.26 | FCC_A1 (x(In) 0) + COIN2_CB (x(In) 0.66667) + LIQUID (x(In) 0.99858) |
| CoIn-01Boa-LB.tdb | 765.21 | COIN2_CB (x(In) 0.66667) + COIN3 (x(In) 0.75) + LIQUID (x(In) 0.99933) |
| CoIn-01Boa-LB.tdb | 765.21 | COIN2_CB (x(In) 0.66667) + COIN3 (x(In) 0.75) + LIQUID (x(In) 0.99933) |
| CoIn-01Boa-LB.tdb | 765.21 | COIN2_CB (x(In) 0.66667) + COIN3 (x(In) 0.75) + LIQUID (x(In) 0.99933) |
| CoIn-01Boa-LB.tdb | 695 | FCC_A1 (x(In) 0) + HCP_A3 (x(In) 0) + COIN2_CB (x(In) 0.66667) |
| CoIn-01Boa-LB.tdb | 429.75 | COIN3 (x(In) 0.75) + TETRAGONAL_A6 (x(In) 1) + LIQUID (x(In) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-IN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-IN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Co–In system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1776.5 | critical point: liq -> liq1 + liq2 | liq1: In 0.7 | model | [1] Boa 2001 | Table 4, p. 4, row 2 |  |
| 1770 | critical point: liq -> liq1 + liq2 | liq1: In 0.65 | experimental | [1] Boa 2001; _cites Bros 1996_ [doi](https://doi.org/10.1016/0925-8388%2895%2901948-0) | Table 4, p. 4, row 1 |  |
| 1559.15 | monotectic: liq1 -> (αCo) + liq2 | liq1: In 0.23 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 3 |  |
| 1558.2 | monotectic: liq1 -> (αCo) + liq2 | liq1: In 0.232 | model | [1] Boa 2001 | Table 4, p. 4, row 4 |  |
| 824.31 | peritectic: (αCo) + liq2 -> CoIn2 | liq2: In 0.986; CoIn2: In 0.666667 | model | [1] Boa 2001 | Table 4, p. 4, row 6 |  |
| 823 | peritectic: (αCo) + liq2 -> CoIn2 | CoIn2: In 0.666667 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 5 |  |
| 764.78 | peritectic: CoIn2 + liq2 -> CoIn3 | CoIn2: In 0.666667; liq2: In 0.9993; CoIn3: In 0.75 | model | [1] Boa 2001 | Table 4, p. 4, row 8 |  |
| 763.15 | peritectic: CoIn2 + liq2 -> CoIn3 | CoIn2: In 0.666667; CoIn3: In 0.75 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 7 |  |
| 429.78 | eutectic: liq2 -> CoIn3 + In | liq2: In 0.9999; CoIn3: In 0.75; In: In 1 | model | [1] Boa 2001 | Table 4, p. 4, row 10 |  |
| 429.15 | eutectic: liq2 -> CoIn3 + In | CoIn3: In 0.75; In: In 1 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 9 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Boa, B.K. Dongui, I. Ansara, Thermodynamic evaluation of the Co-In system, Calphad 25, 645-650 (2001). [doi:10.1016/s0364-5916(02)00014-7](https://doi.org/10.1016/s0364-5916%2802%2900014-7)

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
