# Hg–Zn system

> Hg–Zn system: 5 accepted literature values (phase equilibrium 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HG-ZN.html · Markdown: https://data.orchid-project.org/systems/HG-ZN.md

5 accepted literature values from 1 paper(s) (experimental 5); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HG-ZN.json) · [CSV](https://data.orchid-project.org/systems/HG-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HG-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HG-ZN/HgZn-98Han-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/HG-ZN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HG-ZN.html) · [Markdown](https://data.orchid-project.org/systems/HG-ZN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase equilibrium | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HgZn-98Han-LB.tdb | S.C. Hansen, Calphad, 22, 359-73(1998). [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) | `bc1b12ff7603ad23ddefe7c854e775e5ca4f45cc79ff492b2c4791284c2b6beb` | [viewer](https://orchid-project.org/phase-diagrams/#HG-ZN/HgZn-98Han-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgZn-98Han-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HgZn-98Han-LB.tdb | 315.63 | LIQUID (x(Zn) 0.08948) + HGZN3 (x(Zn) 0.75) + HCP_A3 (x(Zn) 0.97978) |
| HgZn-98Han-LB.tdb | 315.63 | LIQUID (x(Zn) 0.08979) + HGZN3 (x(Zn) 0.75) + HCP_A3 (x(Zn) 0.97974) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HG/HG-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HG/HG-ZN.json)

## Other properties

### Phase equilibrium (5)

Table: Phase equilibrium, Hg–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  |  | (Zn); _(Zn): Hg 0.02, Zn 0.98_ | experimental | [1] Hansen 1998; _cites ref. 30_ | Table II, p. 5, row 4; `ORC-KNJ5ZEPQT2` |  |
| Phase composition |  | 285.25 | (Zn); _(Zn): Hg 0.013, Zn 0.987_ | experimental | [1] Hansen 1998; _cites ref. 18_ | Table II, p. 5, row 1; `ORC-S6GZUAQQ46` |  |
| Phase composition |  | 293.15 | (Zn); _(Zn): Hg 0.008, Zn 0.992_ | experimental | [1] Hansen 1998; _cites ref. 31_ | Table II, p. 5, row 5; `ORC-247VUQV5UZ` |  |
| Phase composition |  | 293.15 | (Zn); _(Zn): Hg 0.017, Zn 0.983_ | experimental | [1] Hansen 1998; _cites ref. 29_ | Table II, p. 5, row 3; `ORC-XZPOBR2ZJD` |  |
| Phase composition |  | 308.15 | (Zn); _(Zn): Hg 0.02, Zn 0.98_ | experimental | [1] Hansen 1998; _cites ref. 18_ | Table II, p. 5, row 2; `ORC-DRU2K3KUOF` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.C. Hansen, Thermodynamic assessment of binary Zn-Hg, Cd-Hg, AND In-Hg amalgams, Calphad 22, 359-373 (1998). [doi:10.1016/s0364-5916(98)00036-4](https://doi.org/10.1016/s0364-5916%2898%2900036-4)

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
