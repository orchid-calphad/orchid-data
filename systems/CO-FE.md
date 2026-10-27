# Co–Fe system

> Co–Fe system: 10 accepted literature values (phase equilibrium 9, mixing / partial 1) and 4 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-FE.html · Markdown: https://data.orchid-project.org/systems/CO-FE.md

10 accepted literature values from 2 paper(s) (experimental 9, DFT 1); 4 calculated phase diagram(s). 7 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-FE.json) · [CSV](https://data.orchid-project.org/systems/CO-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-FE/CoFe-02Ohn.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CO-FE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CO-FE.html) · [Markdown](https://data.orchid-project.org/systems/CO-FE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| DFT | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase equilibrium | 9 |
| mixing / partial | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoFe-02Ohn.tdb | I. Ohnuma, H. Enoki, O. Ikeda, R. Kainuma, H. Ohtani, B. Sundman, K. Ishida, Acta Mater., 50, 379-93(2002). [doi:10.1016/S1359-6454(01)00337-8](https://doi.org/10.1016/S1359-6454%2801%2900337-8) | `4ed3ddb5c0d6db77898f57a5a2707ccc16fd3166452d716e97b56d4ca23af9cd` | [viewer](https://orchid-project.org/phase-diagrams/#CO-FE/CoFe-02Ohn.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoFe-02Ohn.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoFe-02Ohn.json) |
| CoFe-15Rod.tdb | J.E. Rodriguez, D.M. Matson, Calphad, 49, 87-100(2015). [doi:10.1016/j.calphad.2015.03.001](https://doi.org/10.1016/j.calphad.2015.03.001) | `b439f24ad16996c6d1c9de95859f4110298fffc3cd6c3ddbc92f172b29ca73d0` | [viewer](https://orchid-project.org/phase-diagrams/#CO-FE/CoFe-15Rod.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoFe-15Rod.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoFe-15Rod.json) |
| CoFe-17Wan.tdb | J. Wang, X.-G. Lu, N. Zhu, W. Zheng, Calphad, 58, 82-100(2017). [doi:10.1016/j.calphad.2017.06.001](https://doi.org/10.1016/j.calphad.2017.06.001) | `324b5028ec03d3950620d131235ecd322f2ccf53b9d5022dd55cc6a8ed415d2b` | [viewer](https://orchid-project.org/phase-diagrams/#CO-FE/CoFe-17Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoFe-17Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoFe-17Wan.json) |
| CoFe-87Fer-LB.tdb | A. Fernandez Guillermet, High Temp. High Press., 19, 477-99(1987). | `edf9a6fc99f8e55aa8aaac8e3e08ec3e93110f4e674052dcc424377b29b1a21f` | [viewer](https://orchid-project.org/phase-diagrams/#CO-FE/CoFe-87Fer-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoFe-87Fer-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoFe-87Fer-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoFe-02Ohn.tdb | 1771.95 | LIQUID (x(Fe) 0.82085) + FCC_A1 (x(Fe) 0.82868) + B2_BCC (x(Fe) 0.83543) |
| CoFe-02Ohn.tdb | 494.23 | HCP_A3 (x(Fe) 0.02252) + FCC_A1 (x(Fe) 0.05029) + B2_BCC (x(Fe) 0.24766) |
| CoFe-15Rod.tdb | 1769.67 | LIQUID (x(Fe) 0.78298) + FCC_A1 (x(Fe) 0.79081) + BCC_A2 (x(Fe) 0.79601) |
| CoFe-15Rod.tdb | 406.16 | HCP_A3 (x(Fe) 0.03623) + FCC_A1 (x(Fe) 0.06146) + BCC_A2 (x(Fe) 0.18484) |
| CoFe-17Wan.tdb | 1773.69 | LIQUID (x(Fe) 0.8104) + FCC_A1 (x(Fe) 0.81941) + BCC_A2 (x(Fe) 0.82638) |
| CoFe-17Wan.tdb | 1773.69 | LIQUID (x(Fe) 0.8104) + FCC_A1 (x(Fe) 0.81941) + B2_BCC (x(Fe) 0.82638) |
| CoFe-17Wan.tdb | 450.81 | HCP_A3 (x(Fe) 0.01972) + FCC_A1 (x(Fe) 0.05103) + B2_BCC (x(Fe) 0.23523) |
| CoFe-87Fer-LB.tdb | 1777.77 | LIQUID (x(Fe) 0.83052) + FCC_A1 (x(Fe) 0.83904) + BCC_A2 (x(Fe) 0.8475) |
| CoFe-87Fer-LB.tdb | 435.23 | HCP_A3 (x(Fe) 0.03266) + FCC_A1 (x(Fe) 0.05824) + BCC_A2 (x(Fe) 0.20502) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-FE.json) · [CALPHAD hull CoFe-02Ohn](https://data.orchid-project.org/hulls/calphad-sgte/CO/CO-FE--CoFe-02Ohn.json) · [CALPHAD hull CoFe-15Rod](https://data.orchid-project.org/hulls/calphad-sgte/CO/CO-FE--CoFe-15Rod.json) · [CALPHAD hull CoFe-87Fer-LB](https://data.orchid-project.org/hulls/calphad-sgte/CO/CO-FE--CoFe-87Fer-LB.json)

## Other properties

### Phase equilibrium (9)

Table: Phase equilibrium, Co–Fe system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 673.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.704, Fe 0.296; f.c.c.: Co 0.927, Fe 0.073_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 8; `ORC-N3J6QDVUI4` |  |
| Phase composition |  | 723.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.709, Fe 0.291; f.c.c.: Co 0.908, Fe 0.092_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 7; `ORC-C5FZORTTB3` |  |
| Phase composition |  | 773.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.737, Fe 0.263; f.c.c.: Co 0.904, Fe 0.096_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 6; `ORC-KVB4F4CCD6` |  |
| Phase composition |  | 823.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.739, Fe 0.261; f.c.c.: Co 0.891, Fe 0.109_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 5; `ORC-HZGH2EA7ZC` |  |
| Phase composition |  | 873.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.747, Fe 0.253; f.c.c.: Co 0.891, Fe 0.109_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 4; `ORC-MAAWS4VH67` |  |
| Phase composition |  | 973.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.74, Fe 0.26; f.c.c.: Co 0.849, Fe 0.151_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 3; `ORC-B4M2Y5YMJP` |  |
| Phase composition |  | 973.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.745, Fe 0.255; f.c.c.: Co 0.851, Fe 0.149_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 2; `ORC-L7ECB5RIAN` |  |
| Phase composition |  | 1073.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.736, Fe 0.264; f.c.c.: Co 0.804, Fe 0.196_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 1; `ORC-2ACYPXXJ45` |  |
| Phase composition |  | 1073.15 | b.c.c. + f.c.c.; _b.c.c.: Co 0.736, Fe 0.264; f.c.c.: Co 0.804, Fe 0.196_ | experimental | [1] Ohnuma 2002 | Table 1, p. 6, row 9; `ORC-E75QMHH2YI` |  |

### Mixing / partial (1)

Table: Mixing / partial, Co–Fe system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔmixH^SQS_ | -3.392 kJ/mol-atom |  | fcc; _alloy: Co 0.5, Fe 0.5_ | DFT | [2] Bracq 2021 | Table 1, p. 4, row 2; `ORC-HLNK5SU4RE.f4313f` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Ikuo Ohnuma, Hirotoshi Enoki, Osamu Ikeda, Ryosuke Kainuma, Hiroshi Ohtani, Bo Sundman et al., Phase equilibria in the Fe–Co binary system, Acta Materialia 50, 379-393 (2002). [doi:10.1016/s1359-6454(01)00337-8](https://doi.org/10.1016/s1359-6454%2801%2900337-8)
2. Guillaume Bracq, Jean-Claude Crivello, Mathilde Laurent-Brocq, Jean-Marc Joubert, Ivan Guillot, What is the Enthalpy Contribution to the Stabilization of the Co–Cr–Fe–Mn–Ni Faced-centered Cubic Solid Solution?, J. Phase Equilib. Diffus. 42, 561-570 (2021). [doi:10.1007/s11669-021-00922-9](https://doi.org/10.1007/s11669-021-00922-9)

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
