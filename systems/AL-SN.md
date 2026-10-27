# Al–Sn system

> Al–Sn system: 1 accepted literature values (invariant reaction 1) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-SN.html · Markdown: https://data.orchid-project.org/systems/AL-SN.md

1 accepted literature values from 1 paper(s) (model 1); 3 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-SN.json) · [CSV](https://data.orchid-project.org/systems/AL-SN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-SN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-SN/AlSn-19Che.json) · [phases (6)](https://data.orchid-project.org/phases/pages/AL-SN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-SN.html) · [Markdown](https://data.orchid-project.org/systems/AL-SN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlSn-19Che.tdb | T. Cheng, Y. Tang, L. Zhang, Calphad, 64, 354-63(2019). [doi:10.1016/j.calphad.2019.01.005](https://doi.org/10.1016/j.calphad.2019.01.005) | `434b627f2d64558bc572370bd0cb6054490d9e243e86619752ca22a8a0587ac4` | [viewer](https://orchid-project.org/phase-diagrams/#AL-SN/AlSn-19Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlSn-19Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlSn-19Che.json) |
| AlSn-79Ans.tdb | I. Ansara, J.P. Bros, M. Gambino, Calphad, 3, 225-233(1979). [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) | `72b5c10a35428d7ea27f11f1f90d601fc9e97fee06d5b38a2a324fbe085684db` | [viewer](https://orchid-project.org/phase-diagrams/#AL-SN/AlSn-79Ans.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlSn-79Ans.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlSn-79Ans.json) |
| AlSn-98Fri-LB.tdb | S.G. Fries, H.L. Lukas, COST 507, Final report round 2, 1998. | `1102d78dab680fb9b35f8765a3a3548a2cc11363bd3c3db481a8799ee1dd3f6d` | [viewer](https://orchid-project.org/phase-diagrams/#AL-SN/AlSn-98Fri-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlSn-98Fri-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlSn-98Fri-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlSn-19Che.tdb | 502.73 | FCC_A1 (x(Sn) 0) + LIQUID (x(Sn) 0.98113) + BCT_A5 (x(Sn) 0.98955) |
| AlSn-19Che.tdb | 502.73 | FCC_A1 (x(Sn) 0) + LIQUID (x(Sn) 0.98095) + BCT_A5 (x(Sn) 0.98945) |
| AlSn-79Ans.tdb | 499.85 | FCC_A1 (x(Sn) 0) + LIQUID (x(Sn) 0.98187) + BCT_A5 (x(Sn) 1) |
| AlSn-79Ans.tdb | 499.85 | FCC_A1 (x(Sn) 0) + LIQUID (x(Sn) 0.98187) + BCT_A5 (x(Sn) 1) |
| AlSn-79Ans.tdb | 499.85 | FCC_A1 (x(Sn) 0) + LIQUID (x(Sn) 0.98187) + BCT_A5 (x(Sn) 1) |
| AlSn-98Fri-LB.tdb | 502.38 | FCC_A1 (x(Sn) 0) + LIQUID (x(Sn) 0.98037) + BCT_A5 (x(Sn) 0.98991) |
| AlSn-98Fri-LB.tdb | 502.38 | FCC_A1 (x(Sn) 0) + LIQUID (x(Sn) 0.98037) + BCT_A5 (x(Sn) 0.98991) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-SN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-SN.json) · [CALPHAD hull AlSn-79Ans](https://data.orchid-project.org/hulls/calphad-sgte/AL/AL-SN--AlSn-79Ans.json) · [CALPHAD hull AlSn-98Fri-LB](https://data.orchid-project.org/hulls/calphad-sgte/AL/AL-SN--AlSn-98Fri-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Sn system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 502.4 | eutectic: Liquid -> fcc-A1 + bct-A5 | Liquid: Sn 0.98; fcc-A1: Sn 0; bct-A5: Sn 0.99 | model | [1] (ed.) 1998 | Table I, p. 98, row 1; `ORC-DJW2DK3FQA` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Ansara, A. T. Dinsdale, M. H. Rand (eds.), COST 507: Thermochemical database for light metal alloys, Volume 2, EUR 18499 EN, Office for Official Publications of the European Communities, Luxembourg (1998), ISBN 92-828-3902-8.

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
