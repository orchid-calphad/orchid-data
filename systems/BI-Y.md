# Bi–Y system

> Bi–Y system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-Y.html · Markdown: https://data.orchid-project.org/systems/BI-Y.md

10 accepted literature values from 1 paper(s) (experimental 6, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-Y.json) · [CSV](https://data.orchid-project.org/systems/BI-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-Y/BiY-11Wan.json) · [phases (7)](https://data.orchid-project.org/phases/pages/BI-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-Y.html) · [Markdown](https://data.orchid-project.org/systems/BI-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiY-11Wan.tdb | S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 32, 441-46(2011). [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) | `ac3d63c817a8399a6b4a113fd2c037e46b0c7d1b3a9c872f978c765786aed982` | [viewer](https://orchid-project.org/phase-diagrams/#BI-Y/BiY-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiY-11Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiY-11Wan.tdb | 1804.07 | BIY_B1 (x(Y) 0.5) + BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.67558) |
| BiY-11Wan.tdb | 1804.06 | BIY_B1 (x(Y) 0.5) + BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.67578) |
| BiY-11Wan.tdb | 1804.06 | BIY_B1 (x(Y) 0.5) + BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.67581) |
| BiY-11Wan.tdb | 1751.97 | LIQUID (x(Y) 0.9736) + HCP_A3 (x(Y) 0.99984) + BCC_A2 (x(Y) 1) |
| BiY-11Wan.tdb | 1751.97 | LIQUID (x(Y) 0.97362) + HCP_A3 (x(Y) 0.99984) + BCC_A2 (x(Y) 1) |
| BiY-11Wan.tdb | 1417.65 | BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.81825) + HCP_A3 (x(Y) 0.99795) |
| BiY-11Wan.tdb | 1417.65 | BI3Y5 (x(Y) 0.625) + LIQUID (x(Y) 0.81825) + HCP_A3 (x(Y) 0.99795) |
| BiY-11Wan.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(Y) 0) + LIQUID (x(Y) 1.000e-5) + BIY_B1 (x(Y) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Y system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2293.15 | congruent melting: L -> BiY | L: Y 0.5; BiY: Y 0.5 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 3 |  |
| 2292.65 | congruent melting: L -> BiY | L: Y 0.5; BiY: Y 0.5 | model | [1] Wang 2011 | Table 4, p. 5, row 4 |  |
| 1804.05 | peritectic: L + BiY -> Bi3Y5 | L: Y 0.676; BiY: Y 0.5; Bi3Y5: Y 0.625 | model | [1] Wang 2011 | Table 4, p. 5, row 6 |  |
| 1803.15 | peritectic: L + BiY -> Bi3Y5 | BiY: Y 0.5; Bi3Y5: Y 0.625 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 5 |  |
| 1418.15 | eutectic: L -> Bi3Y5 + (αY) | L: Y 0.815; Bi3Y5: Y 0.625; (αY): Y 1 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 7 |  |
| 1418.15 | eutectic: L (81.5 at.% Y) M aY + Bi3Y5 |  | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | p. 2 | “Schmidt et al.\[18\] also determined two eutectic reactions: L (\<0.1 at.% Y) M (Bi) + BiY at 269 C and L (81.5 at.% Y) M aY + Bi3Y5 at 1145 C.” |
| 1417.65 | eutectic: L -> Bi3Y5 + (αY) | L: Y 0.818; Bi3Y5: Y 0.625; (αY): Y 0.998 | model | [1] Wang 2011 | Table 4, p. 5, row 8 |  |
| 544.55 | eutectic: L -> (Bi) + BiY | L: Y 0; (Bi): Y 0; BiY: Y 0.5 | model | [1] Wang 2011 | Table 4, p. 5, row 2 |  |
| 542.15 | eutectic: L -> (Bi) + BiY | (Bi): Y 0; BiY: Y 0.5 | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | Table 4, p. 5, row 1 |  |
| 542.15 | eutectic: L (\<0.1 at.% Y) M (Bi) + BiY |  | experimental | [1] Wang 2011; _cites Schmidt 1969_ [doi](https://doi.org/10.1016/0022-5088%2869%2990159-3) | p. 2 | “Schmidt et al.\[18\] also determined two eutectic reactions: L (\<0.1 at.% Y) M (Bi) + BiY at 269 C and L (81.5 at.% Y) M aY + Bi3Y5 at 1145 C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011). [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1)

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
