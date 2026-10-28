# Si–Zn system

> Si–Zn system: 4 accepted literature values (invariant reaction 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SI-ZN.html · Markdown: https://data.orchid-project.org/systems/SI-ZN.md

4 accepted literature values from 2 paper(s) (model 4); 2 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SI-ZN.json) · [CSV](https://data.orchid-project.org/systems/SI-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SI-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SI-ZN/SiZn-86Mey.json) · [phases (5)](https://data.orchid-project.org/phases/pages/SI-ZN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SI-ZN.html) · [Markdown](https://data.orchid-project.org/systems/SI-ZN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SiZn-86Mey.tdb | S. an Mey, K. Hack, Z. Metallkd., 77, 454-59(1986). | `a01184415c4bd4f99e25fbde482fef0f507ce350e3387cc3db04d1414fe98de9` | [viewer](https://orchid-project.org/phase-diagrams/#SI-ZN/SiZn-86Mey.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiZn-86Mey.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiZn-86Mey.json) |
| SiZn-96Jac-LB.tdb | M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996). [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) | `56568b4c0531129d6f49218ad42ac6a8848e4ef5d82ed01d49b1ba4fd297b93e` | [viewer](https://orchid-project.org/phase-diagrams/#SI-ZN/SiZn-96Jac-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiZn-96Jac-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiZn-96Jac-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SiZn-86Mey.tdb | 692.42 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99953) + HCP_A3 (x(Zn) 1) |
| SiZn-86Mey.tdb | 692.42 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99953) + HCP_A3 (x(Zn) 1) |
| SiZn-86Mey.tdb | 692.42 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99953) + HCP_A3 (x(Zn) 1) |
| SiZn-96Jac-LB.tdb | 692.17 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99906) + HCP_A3 (x(Zn) 1) |
| SiZn-96Jac-LB.tdb | 692.17 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99906) + HCP_A3 (x(Zn) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SI/SI-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SI/SI-ZN.json) · [CALPHAD hull SiZn-86Mey](https://data.orchid-project.org/hulls/calphad-sgte/SI/SI-ZN--SiZn-86Mey.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Si–Zn system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1675 | eutectic: \<Si>-Liq- Vap | Liq: Zn 0.0251 | model | [1] Jacobs 1996 | Table 1, p. 3, row 1; `ORC-FXYPBGXWSJ` |  |
| 1189.29 | eutectic: \<Si>-Liq- Vap | Liq: Zn 0.8985 | model | [1] Jacobs 1996 | Table 1, p. 3, row 2; `ORC-TLB2UTKZCU` |  |
| 692.17 | eutectic: \<Si>-Liq-\<Zn> | Liq: Zn 0.9991 | model | [1] Jacobs 1996 | Table 1, p. 3, row 3; `ORC-ILG6D6JEGL` |  |
| 692.1 | other: Liquid -> diamond + hcp-Zn | L: Zn 1; diamond: Zn 0; hcp-Zn: Zn 1 | model | [2] (ed.) 1998 | Table I, p. 295, row 1; `ORC-ENHV2Z6RFU` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M.H.G. Jacobs, P.J. Spencer, A critical thermodynamic evaluation of the systems SiZn and AlSiZn, Calphad 20, 307-320 (1996). [doi:10.1016/s0364-5916(96)00033-8](https://doi.org/10.1016/s0364-5916%2896%2900033-8)
2. I. Ansara, A. T. Dinsdale, M. H. Rand (eds.), COST 507: Thermochemical database for light metal alloys, Volume 2, EUR 18499 EN, Office for Official Publications of the European Communities, Luxembourg (1998), ISBN 92-828-3902-8.

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
