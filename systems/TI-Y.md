# Ti–Y system

> Ti–Y system: 1 accepted literature values (phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TI-Y.html · Markdown: https://data.orchid-project.org/systems/TI-Y.md

1 accepted literature values from 1 paper(s) (experimental 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/TI-Y.json) · [CSV](https://data.orchid-project.org/systems/TI-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#TI-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#TI-Y/TiY-18Yao.json) · [Markdown](https://data.orchid-project.org/systems/TI-Y.md)

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
| TiY-18Yao.tdb | B. Yao, B. Hu, A. Zhang, J. Zhao, J. Wang, J. Phase Equilib. Diffus., 39, 44-50(2018). [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) | `0fcdc76cbe30b604149dd1bd2af5122cdce31995b408a83403391a805bd4d7a0` | [viewer](https://orchid-project.org/phase-diagrams/#TI-Y/TiY-18Yao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/TiY-18Yao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/TiY-18Yao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| TiY-18Yao.tdb | 1728.02 | LIQUID (x(Y) 0.9532) + BCC_A2 (x(Y) 0.98666) + HCP_A3 (x(Y) 0.99146) |
| TiY-18Yao.tdb | 1643.2 | BCC_A2 (x(Y) 0.01915) + LIQUID#2 (x(Y) 0.29021) + LIQUID (x(Y) 0.77939) |
| TiY-18Yao.tdb | 1630.27 | BCC_A2 (x(Y) 0.0187) + LIQUID (x(Y) 0.80046) + HCP_A3 (x(Y) 0.98234) |
| TiY-18Yao.tdb | 1152.05 | HCP_A3 (x(Y) 0.00137) + BCC_A2 (x(Y) 0.0025) + HCP_A3#2 (x(Y) 0.99665) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/TI/TI-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/TI/TI-Y.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Ti–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1763.15 K | 1763.15 |  | experimental | [1] Bu 2010; _cites Bare 1961_ | p. 4 | “However, it was reported by Bare and Carlson \[13\] that the allotropic transition of Ti occurring at 1490 ±15 °C in the Ti-Y system was a peritectoid reaction rather than the metatectic reaction, according to the results from the microscopic and thermal analysis and from the resistometric measurements.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M.J. Bu, P.S. Wang, H.H. Xu, S.H. Liu, C.S. Sha, Y. Du et al., Experimental investigation and thermodynamic modeling of the Zr-Y system, J min metall B Metall 46, 181-192 (2010). [doi:10.2298/jmmb1002181b](https://doi.org/10.2298/jmmb1002181b)

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
