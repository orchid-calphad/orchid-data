# Gd–H system

> Gd–H system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GD-H.html · Markdown: https://data.orchid-project.org/systems/GD-H.md

2 accepted literature values from 1 paper(s) (model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GD-H.json) · [CSV](https://data.orchid-project.org/systems/GD-H.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GD-H) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GD-H/GdH-16Fu.json) · [phases (5)](https://data.orchid-project.org/phases/pages/GD-H.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GD-H.html) · [Markdown](https://data.orchid-project.org/systems/GD-H.md)

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
| GdH-16Fu.tdb | K. Fu, G. Li, J. Li, Y. Liu, W. Tian, J. Zheng, X. Li, J. Alloys Compd., 673, 131-37(2016). [doi:10.1016/j.jallcom.2016.02.201](https://doi.org/10.1016/j.jallcom.2016.02.201) | `aaac49e5806f315ddff81d94cb03e458f1efda6d43031920b4c484b37238d497` | [viewer](https://orchid-project.org/phase-diagrams/#GD-H/GdH-16Fu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdH-16Fu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdH-16Fu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GdH-16Fu.tdb | 1916.51 | LIQUID (x(H) 0.00488) + HCP_A3 (x(H) 0.14911) + GAS (x(H) 1) |
| GdH-16Fu.tdb | 1586.6 | LIQUID (x(H) 1.100e-4) + BCC_A2 (x(H) 3.300e-4) + HCP_A3 (x(H) 0.01384) |
| GdH-16Fu.tdb | 1468.03 | HCP_A3 (x(H) 0.39695) + FCC_A1 (x(H) 0.52934) + GAS (x(H) 1) |
| GdH-16Fu.tdb | 623.77 | FCC_A1 (x(H) 0.70081) + HCP_A3 (x(H) 0.7496) + GAS (x(H) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GD/GD-H.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GD/GD-H.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Gd–H system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1466.75 | Hcp(Gd) +Gas(H2)→β-GdH2 | Hcp(Gd): H 0.397; Gas(H2): H 1; β-GdH2: H 0.53 | model | [1] Fu 2016 | Table 3, p. 5, row 2; `ORC-KEN7ZREPFM` |  |
| 623.35 | β-GdH2+Gas(H2)→γ-GdH3 | β-GdH2: H 0.701; Gas(H2): H 1; γ-GdH3: H 0.75 | model | [1] Fu 2016 | Table 3, p. 5, row 1; `ORC-IMWNY4WA5G` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Kai Fu, Guoling Li, Jigang Li, Yang Liu, Wenhuai Tian, Jie Zheng et al., Study on the thermodynamics of the gadolinium-hydrogen binary system (H/Gd = 0.0–2.0) and implications to metallic gadolinium purification, Journal of Alloys and Compounds 673, 131-137 (2016). [doi:10.1016/j.jallcom.2016.02.201](https://doi.org/10.1016/j.jallcom.2016.02.201)

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
