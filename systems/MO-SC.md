# Mo–Sc system

> Mo–Sc system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-SC.html · Markdown: https://data.orchid-project.org/systems/MO-SC.md

2 accepted literature values from 1 paper(s) (model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-SC.json) · [CSV](https://data.orchid-project.org/systems/MO-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-SC) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-SC/MoSc-15Wan.json) · [phases (4)](https://data.orchid-project.org/phases/pages/MO-SC.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MO-SC.html) · [Markdown](https://data.orchid-project.org/systems/MO-SC.md)

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
| MoSc-15Wan.tdb | S.L. Wang, L.J. Zhou, Y. Ye, X.H. Wang, Y.H. Lin, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 36, 3-9(2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) | `0ab14e8c45e527af01d3c1fdc91fc7086399f223270dc4bf2141de78be1b15c5` | [viewer](https://orchid-project.org/phase-diagrams/#MO-SC/MoSc-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoSc-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoSc-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoSc-15Wan.tdb | 1643.17 | BCC_A2 (x(Sc) 0.00235) + LIQUID (x(Sc) 0.89551) + BCC_A2#2 (x(Sc) 0.9834) |
| MoSc-15Wan.tdb | 1603.08 | BCC_A2 (x(Sc) 0.00201) + BCC_A2#2 (x(Sc) 0.98513) + HCP_A3 (x(Sc) 0.98587) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-SC.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mo–Sc system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1643.15 | eutectic: L -> (Mo) + bSc |  | model | [1] Wang 2015; _cites Massalski 1996_ | p. 2 | “The Sc-Mo phase diagram consisted of three solid solution phases ((Mo), aSc and bSc phases) is mainly based on the work of Massalski,\[15\] who indicated a eutectic reaction (L (89.5 at.% Sc) M (Mo) (0.2 at.% Sc) + bSc (98.5 at.% Sc) at 1370 ± 50 °C) and a eutectoid reaction (bSc (98.5 at.% Sc) M (Cr) (0.2 at.% Sc) + aSc (99.5 at.% Sc) at 1330 °C).” |
| 1603.15 | eutectoid: bSc -> (Cr) + aSc |  | model | [1] Wang 2015; _cites Massalski 1996_ | p. 2 | “The Sc-Mo phase diagram consisted of three solid solution phases ((Mo), aSc and bSc phases) is mainly based on the work of Massalski,\[15\] who indicated a eutectic reaction (L (89.5 at.% Sc) M (Mo) (0.2 at.% Sc) + bSc (98.5 at.% Sc) at 1370 ± 50 °C) and a eutectoid reaction (bSc (98.5 at.% Sc) M (Cr) (0.2 at.% Sc) + aSc (99.5 at.% Sc) at 1330 °C).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8)

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
