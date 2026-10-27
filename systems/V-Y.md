# V–Y system

> V–Y system: 7 accepted literature values (invariant reaction 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/V-Y.html · Markdown: https://data.orchid-project.org/systems/V-Y.md

7 accepted literature values from 1 paper(s) (experimental 3, model 2, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/V-Y.json) · [CSV](https://data.orchid-project.org/systems/V-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#V-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#V-Y/VY-10Cha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/V-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/V-Y.html) · [Markdown](https://data.orchid-project.org/systems/V-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 2 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| VY-10Cha.tdb | W. Chan, M.C. Gao, O.N. Dogan, P. King, J. Phase Equilib. Diffus., 31, 425-32(2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4) | `0df5652586b3c536e5e0639134b9ead6b19afdca15c8cd8d9baa0e7fe1559422` | [viewer](https://orchid-project.org/phase-diagrams/#V-Y/VY-10Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/VY-10Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/VY-10Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| VY-10Cha.tdb | 2176.56 | BCC_A2 (x(Y) 5.700e-4) + LIQUID#2 (x(Y) 0.0043) + LIQUID (x(Y) 0.81939) |
| VY-10Cha.tdb | 1758.47 | LIQUID (x(Y) 0.98206) + HCP_A3 (x(Y) 0.99796) + BCC_A2 (x(Y) 0.99937) |
| VY-10Cha.tdb | 1719.26 | BCC_A2 (x(Y) 1.100e-4) + LIQUID (x(Y) 0.94191) + HCP_A3 (x(Y) 0.99564) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/V/V-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/V/V-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the V–Y system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2181.15 | monotectic: L1 \<-> L2 + V | L1: Y 1.000e-5; L2: Y 0.82; V: Y 1.000e-6 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 7, row 2; `ORC-77LWXIDHCN` |  |
| 2176.15 | monotectic: L1 \<-> L2 + V | L1: Y 0.0043; L2: Y 0.8194; V: Y 6.000e-4 | model | [1] Chan 2010 | Table 4, p. 7, row 3; `ORC-7WLZSVAREP` |  |
| 2173.15 | monotectic: L1 \<-> L2 + V | L1: Y 6.000e-4; L2: Y 0.852 | experimental | [1] Chan 2010; _cites Lundin 1962_ | Table 4, p. 7, row 1; `ORC-C3GLBXS5N6` |  |
| 1763.15 | L + βY \<-> αY |  | experimental | [1] Chan 2010; _cites Lundin 1962_ | Table 4, p. 7, row 4; `ORC-WQBLFI47SK` |  |
| 1728.15 | eutectic: L \<-> V + αY | L: Y 0.8839; V: Y 0; αY: Y 0.9965 | experimental | [1] Chan 2010; _cites Lundin 1962_ | Table 4, p. 7, row 7; `ORC-2BALGCYXNG` |  |
| 1723.15 | eutectic: L \<-> V + αY | L: Y 0.9419; V: Y 0; αY: Y 0.9956 | model | [1] Chan 2010 | Table 4, p. 7, row 9; `ORC-EJOKYP3OHC` |  |
| 1723.15 | eutectic: L \<-> V + αY | L: Y 0.93; V: Y 0; αY: Y 0.999 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 7, row 8; `ORC-QZOMH2A4HD` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Thermodynamic Assessment of V-Rare Earth Systems, J. Phase Equilib. Diffus. 31, 425-432 (2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
