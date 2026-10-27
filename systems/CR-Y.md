# Cr–Y system

> Cr–Y system: 11 accepted literature values (invariant reaction 11) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-Y.html · Markdown: https://data.orchid-project.org/systems/CR-Y.md

11 accepted literature values from 1 paper(s) (experimental 5, model 3, unspecified 3); 2 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-Y.json) · [CSV](https://data.orchid-project.org/systems/CR-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-Y/CrY-09Cha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CR-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-Y.html) · [Markdown](https://data.orchid-project.org/systems/CR-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 3 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 11 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrY-09Cha.tdb | W. Chan, C. Gao, O.N. Dogan, P. King, A.D. Rollett, J. Phase Equilib. Diffus., 30, 578-86(2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) | `eae96d9642ae594d246dbab4f8f3bccd289347bab2fc73e41913e0f1515da413` | [viewer](https://orchid-project.org/phase-diagrams/#CR-Y/CrY-09Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrY-09Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrY-09Cha.json) |
| CrY-21Wan.tdb | Y. Wang, M. Ostrowska, G. Cacciamani, Calphad, 72, 102214(2021). [doi:10.1016/j.calphad.2020.102214](https://doi.org/10.1016/j.calphad.2020.102214) | `2261a8ac56309484f932c652e6f549213589c0a5d32ad679a580df3993c1ef01` | [viewer](https://orchid-project.org/phase-diagrams/#CR-Y/CrY-21Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrY-21Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrY-21Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrY-09Cha.tdb | 2019.68 | BCC_A2 (x(Y) 0.00498) + LIQUID#2 (x(Y) 0.18466) + LIQUID (x(Y) 0.55191) |
| CrY-09Cha.tdb | 1737.93 | LIQUID (x(Y) 0.97094) + BCC_A2 (x(Y) 0.99553) + HCP_A3 (x(Y) 0.99811) |
| CrY-09Cha.tdb | 1602.37 | BCC_A2 (x(Y) 0.00196) + LIQUID (x(Y) 0.87102) + HCP_A3 (x(Y) 0.99326) |
| CrY-21Wan.tdb | 2021.37 | BCC_A2 (x(Y) 0.0064) + LIQUID#2 (x(Y) 0.1855) + LIQUID (x(Y) 0.55072) |
| CrY-21Wan.tdb | 1744.58 | LIQUID (x(Y) 0.97541) + BCC_A2 (x(Y) 0.99712) + HCP_A3 (x(Y) 0.99839) |
| CrY-21Wan.tdb | 1602.47 | BCC_A2 (x(Y) 0.00266) + LIQUID (x(Y) 0.8711) + HCP_A3 (x(Y) 0.99327) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-Y.json) · [CALPHAD hull CrY-09Cha](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-Y--CrY-09Cha.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–Y system (11)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2033.15 | monotectic: L1 -> L2 + Cr | L1: Y 0.0936; L2: Y 0.5771 | experimental | [1] Chan 2009; _cites Terekhova 1961_ | Table 4, p. 9, row 1; `ORC-IRQIVRHLJA` |  |
| 2033.15 | monotectic: L1 -> L2 + Cr | L1: Y 0.09; L2: Y 0.58 | unspecified | [1] Chan 2009; _cites Venkatraman 1985_ [doi](https://doi.org/10.1007/bf02869503) | Table 4, p. 9, row 2; `ORC-PWFB36X4OG` |  |
| 2020.15 | monotectic: L1 -> L2 + Cr | L1: Y 0.185; L2: Y 0.552; Cr: Y 5.000e-4 | model | [1] Chan 2009 | Table 4, p. 9, row 4; `ORC-F5QK6DPJUQ` |  |
| 2013.15 | monotectic: L1 -> L2 + Cr | L1: Y 0.109; L2: Y 0.611 | experimental | [1] Chan 2009; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02645392) | Table 4, p. 9, row 3; `ORC-LS3BHMGEFG` |  |
| 1751.15 | βY -> L2 + αY | L2: Y 0.981 | experimental | [1] Chan 2009; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02645392) | Table 4, p. 9, row 5; `ORC-ETJESYUL5C` |  |
| 1738.15 | βY -> L2 + αY | βY: Y 0.998; L2: Y 0.971; αY: Y 0.996 | model | [1] Chan 2009 | Table 4, p. 9, row 6; `ORC-XCHGBHC225` |  |
| 1603.15 | eutectic: L2 -> Cr + αY | L2: Y 0.8 | unspecified | [1] Chan 2009; _cites Venkatraman 1985_ [doi](https://doi.org/10.1007/bf02869503) | Table 4, p. 9, row 8; `ORC-MFV22D4RNS` |  |
| 1602.15 | eutectic: L2 -> Cr + αY | L2: Y 0.871; Cr: Y 2.000e-4; αY: Y 0.993 | model | [1] Chan 2009 | Table 4, p. 9, row 11; `ORC-O6G33XSFZM` |  |
| 1588.15 | eutectic: L2 -> Cr + αY | L2: Y 0.7965 | experimental | [1] Chan 2009; _cites Terekhova 1961_ | Table 4, p. 9, row 7; `ORC-Z3IVAWCYJC` |  |
| 1573.15 | eutectic: L2 -> Cr + αY | L2: Y 0.859 | experimental | [1] Chan 2009; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02645392) | Table 4, p. 9, row 10; `ORC-CU4GS335HG` |  |
| 1510.15 | eutectic: L2 -> Cr + αY | L2: Y 0.84633 | unspecified | [1] Chan 2009; _cites Terekhova 1990_ | Table 4, p. 9, row 9; `ORC-ZKYQMEAYQS` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3)

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
