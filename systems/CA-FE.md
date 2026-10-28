# Ca–Fe system

> Ca–Fe system: 3 accepted literature values (activity / EMF / Gibbs energy 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-FE.html · Markdown: https://data.orchid-project.org/systems/CA-FE.md

3 accepted literature values from 1 paper(s) (experimental 1, model 2); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-FE.json) · [CSV](https://data.orchid-project.org/systems/CA-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-FE/CaFe-13Sel.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CA-FE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CA-FE.html) · [Markdown](https://data.orchid-project.org/systems/CA-FE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| activity / EMF / Gibbs energy | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaFe-13Sel.tdb | M. Selleby, unpublished, 2013. | `db0b56bc202113e490ef6012428a042966c530803984a7745a04fb85e86abdcf` | [viewer](https://orchid-project.org/phase-diagrams/#CA-FE/CaFe-13Sel.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaFe-13Sel.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaFe-13Sel.json) |
| CaFe-90Hil.tdb | M. Hillert, M. Selleby, B. Sundman, Metall. Trans. A, 21A, 2759-76(1990). [doi:10.1007/BF02646071](https://doi.org/10.1007/BF02646071) | `3262e162a4465f4a419cf52babb99ac97015a897a38abb9db800a85aaa01871b` | [viewer](https://orchid-project.org/phase-diagrams/#CA-FE/CaFe-90Hil.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaFe-90Hil.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaFe-90Hil.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaFe-13Sel.tdb | 1810.83 | LIQUID#2 (x(Fe) 2.800e-4) + LIQUID (x(Fe) 0.99972) + BCC_A2 (x(Fe) 0.99978) |
| CaFe-13Sel.tdb | 1667.31 | LIQUID (x(Fe) 9.000e-5) + BCC_A2 (x(Fe) 0.99993) + FCC_A1 (x(Fe) 0.99993) |
| CaFe-13Sel.tdb | 1667.31 | LIQUID (x(Fe) 9.000e-5) + FCC_A1 (x(Fe) 0.99993) + BCC_A2 (x(Fe) 0.99993) |
| CaFe-13Sel.tdb | 1184.81 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| CaFe-13Sel.tdb | 1184.81 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| CaFe-13Sel.tdb | 1115 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 0) + BCC_A2#2 (x(Fe) 1) |
| CaFe-13Sel.tdb | 716.03 | BCC_A2#2 (x(Fe) 0) + FCC_A1 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |
| CaFe-90Hil.tdb | 1810.81 | LIQUID#2 (x(Fe) 3.300e-4) + LIQUID (x(Fe) 0.99967) + BCC_A2 (x(Fe) 0.99974) |
| CaFe-90Hil.tdb | 1667.19 | LIQUID (x(Fe) 1.500e-4) + BCC_A2 (x(Fe) 0.99987) + FCC_A1 (x(Fe) 0.99988) |
| CaFe-90Hil.tdb | 1667.19 | LIQUID (x(Fe) 1.500e-4) + BCC_A2 (x(Fe) 0.99987) + FCC_A1 (x(Fe) 0.99988) |
| CaFe-90Hil.tdb | 1184.81 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| CaFe-90Hil.tdb | 1184.81 | LIQUID (x(Fe) 0) + FCC_A1 (x(Fe) 1) + BCC_A2 (x(Fe) 1) |
| CaFe-90Hil.tdb | 1115 | LIQUID (x(Fe) 0) + BCC_A2#2 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |
| CaFe-90Hil.tdb | 716.03 | FCC_A1 (x(Fe) 0) + BCC_A2#2 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-FE.json) · [CALPHAD hull CaFe-90Hil](https://data.orchid-project.org/hulls/calphad-sgte/CA/CA-FE--CaFe-90Hil.json)

## Other properties

### Activity / EMF / Gibbs energy (3)

Table: Activity / EMF / Gibbs energy, Ca–Fe system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Chemical potential; _printed: oxygen potential_ | -63.4 kcal/mole O2 | 1273.15 |  | experimental | [1] Hillert 1990 | p. 9; `ORC-F6BWLC5XH7` | “Edstrrm E4mdetermined one point on line X at 1000 ~ to be -63.4 kcal/mole 02 and Reeve and Gregoryc2s\] determined two more points on the line.” |
| Chemical potential; _printed: oxygen potential_ | -74.2 kcal/mole O2 | 1372.15 |  | model | [1] Hillert 1990 | p. 9; `ORC-73Y7CB2KXF` | “The present assessment yields 1099 ~ and -74.2 kcal/mole 02 but predicts that this invariant equilibrium is metastable.” |
| Chemical potential; _printed: oxygen potential_ | -75.1 kcal/mole O2 | 1383.15 |  | model | [1] Hillert 1990 | p. 9; `ORC-2BD6K4HVS5` | “Turkdogant3~ predicted that the univariant lines S, T, and U should intersect at an invariant point X at 1110 ~ and -75.1 kcal/mole 02 and represent a stable equilibrium.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Mats Hillert, Malin Selleby, Bo Sundman, An assessment of the Ca-Fe-O system, Metall Trans A 21, 2759-2776 (1990). [doi:10.1007/bf02646071](https://doi.org/10.1007/bf02646071)

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
