# Co–H system

> Co–H system: 1 accepted literature values (other property 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-H.html · Markdown: https://data.orchid-project.org/systems/CO-H.md

1 accepted literature values from 1 paper(s) (model 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-H.json) · [CSV](https://data.orchid-project.org/systems/CO-H.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-H) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-H/CoH-12Kim.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CO-H.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CO-H.html) · [Markdown](https://data.orchid-project.org/systems/CO-H.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoH-12Kim.tdb | K.-H. Kim, J.-H. Shim, B.-J. Lee, Int. J. Hydrogen Energy, 37, 7836-47(2012). [doi:10.1016/j.ijhydene.2012.01.117](https://doi.org/10.1016/j.ijhydene.2012.01.117) | `25f2231073fd723cb3e90e253c73c39ec85beecbe4757343ac6fdeeea81cfd72` | [viewer](https://orchid-project.org/phase-diagrams/#CO-H/CoH-12Kim.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoH-12Kim.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoH-12Kim.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoH-12Kim.tdb | 1767.48 | FCC_A1 (x(H) 3.500e-4) + LIQUID (x(H) 6.700e-4) + GAS (x(H) 1) |
| CoH-12Kim.tdb | 1767.48 | FCC_A1 (x(H) 3.500e-4) + LIQUID (x(H) 6.700e-4) + GAS (x(H) 1) |
| CoH-12Kim.tdb | 695.14 | FCC_A1 (x(H) 5.000e-5) + HCP_A3 (x(H) 6.000e-5) + GAS (x(H) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-H.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-H.json)

## Other properties

### Other property (1)

Table: Other property, Co–H system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: heat of melting_ | 16200 J/mol | 1768 |  | model | [1] Kim 2012; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | p. 6; `ORC-UFHBM3TSFD` | “Considering that Co and Ni are close to each other in the periodic table and assuming that fundamental thermodynamic properties may be similar to each other (the melting point of Ni and Co, and heat of melting of the two elements are 1728 K, 1768 K and 17,480 J/mol, 16,200 J/mol, respectively \[50\]), the value for the heat of formation of CoH6 was taken from the value for NiH6.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Ki-Hyun Kim, Jae-Hyeok Shim, Byeong-Joo Lee, Effect of alloying elements (Al, Co, Fe, Ni) on the solubility of hydrogen in vanadium: A thermodynamic calculation, International Journal of Hydrogen Energy 37, 7836-7847 (2012). [doi:10.1016/j.ijhydene.2012.01.117](https://doi.org/10.1016/j.ijhydene.2012.01.117)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
