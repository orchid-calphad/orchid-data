# Pu–Th system

> Pu–Th system: 2 accepted literature values (heat capacity / entropy / enthalpy 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PU-TH.html · Markdown: https://data.orchid-project.org/systems/PU-TH.md

2 accepted literature values from 1 paper(s) (model 2); 1 calculated phase diagram(s). 8 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/PU-TH.json) · [CSV](https://data.orchid-project.org/systems/PU-TH.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PU-TH) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PU-TH/PuTh-14Ben.json) · [phases (9)](https://data.orchid-project.org/phases/pages/PU-TH.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PU-TH.html) · [Markdown](https://data.orchid-project.org/systems/PU-TH.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| heat capacity / entropy / enthalpy | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PuTh-14Ben.tdb | O. Benes, D. Manara, R.J.M. Konings, J. Nucl. Mater., 449, 15-22(2014). [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) | `90a9babb3ad9d9a5ead38ddc3fa242a8cbcef026badac6dd6eee78f4b3a85731` | [viewer](https://orchid-project.org/phase-diagrams/#PU-TH/PuTh-14Ben.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PuTh-14Ben.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PuTh-14Ben.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PuTh-14Ben.tdb | 1337.39 | LIQUID (x(Th) 0.59775) + BCC_TH (x(Th) 0.81603) + FCC_A1 (x(Th) 0.87422) |
| PuTh-14Ben.tdb | 1108.96 | LIQUID (x(Th) 0.38969) + BCC_TH (x(Th) 0.65373) + FCC_A1 (x(Th) 0.76283) |
| PuTh-14Ben.tdb | 883 | LIQUID (x(Th) 0.13683) + PU7TH3 (x(Th) 0.3) + BCC_TH (x(Th) 0.46549) |
| PuTh-14Ben.tdb | 877.78 | PU7TH3 (x(Th) 0.3) + BCC_TH (x(Th) 0.47478) + FCC_A1 (x(Th) 0.60647) |
| PuTh-14Ben.tdb | 838.82 | BCC_PU (x(Th) 0.03412) + LIQUID (x(Th) 0.06543) + PU7TH3 (x(Th) 0.3) |
| PuTh-14Ben.tdb | 777.27 | BCC_PU (x(Th) 0.01823) + FCC_A1 (x(Th) 0.02979) + PU7TH3 (x(Th) 0.3) |
| PuTh-14Ben.tdb | 764.1 | BCC_PU (x(Th) 0.00815) + TETRAGONAL_A6 (x(Th) 0.01149) + FCC_A1 (x(Th) 0.01229) |
| PuTh-14Ben.tdb | 578.55 | GAMMA_PU (x(Th) 0) + FCC_A1 (x(Th) 0.00372) + PU7TH3 (x(Th) 0.3) |
| PuTh-14Ben.tdb | 578.55 | GAMMA_PU (x(Th) 0) + FCC_A1 (x(Th) 0.00373) + PU7TH3 (x(Th) 0.3) |
| PuTh-14Ben.tdb | 487.9 | BETA_PU (x(Th) 0) + GAMMA_PU (x(Th) 0) + PU7TH3 (x(Th) 0.3) |
| PuTh-14Ben.tdb | 397.62 | BETA_PU (x(Th) 0) + ALPHA_PU (x(Th) 0) + PU7TH3 (x(Th) 0.3) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PU/PU-TH.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PU/PU-TH.json)

## Other properties

### Heat capacity / entropy / enthalpy (2)

Table: Heat capacity / entropy / enthalpy, Pu–Th system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S0(298.15)_ | 53.6618 J/mol-atom/K | 298.15 | Th3Pu7; _alloy: Th 0.3_ | model | [1] Beneš 2014 | Table 1, p. 2, row 37; `ORC-RGH2U3SM2J.e1026c` |  |
| Entropy; _printed: S0(298.15)_ | 53.6618 J/mol-atom/K | 298.15 | Th3Pu7; _alloy: Th 0.3_ | model | [1] Beneš 2014 | Table 1, p. 2, row 38; `ORC-YG6EXYMDXI` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. O. Beneš, D. Manara, R.J.M. Konings, Thermodynamic assessment of the Th–U–Pu system, Journal of Nuclear Materials 449, 15-22 (2014). [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001)

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
