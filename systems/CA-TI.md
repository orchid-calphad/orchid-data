# Ca–Ti system

> Ca–Ti system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-TI.html · Markdown: https://data.orchid-project.org/systems/CA-TI.md

4 accepted literature values from 1 paper(s) (model 4); 1 calculated phase diagram(s). 8 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-TI.json) · [CSV](https://data.orchid-project.org/systems/CA-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-TI/CaTi-15Ham.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CA-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CA-TI.html) · [Markdown](https://data.orchid-project.org/systems/CA-TI.md)

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
| CaTi-15Ham.tdb | M. Hampl, R. Schmid-Fetzer, J. Mater. Sci., 50, 5822-32(2015). [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x) | `3a0af4e503124843d15f19ba39b9f2bb731c172b26a29ec11c19db18c0c00436` | [viewer](https://orchid-project.org/phase-diagrams/#CA-TI/CaTi-15Ham.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaTi-15Ham.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaTi-15Ham.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaTi-15Ham.tdb | 1938.56 | LIQUID (x(Ti) 0.00423) + LIQUID#2 (x(Ti) 0.99577) + BCC_A2 (x(Ti) 0.99691) |
| CaTi-15Ham.tdb | 1156.02 | LIQUID (x(Ti) 3.200e-4) + HCP_A3 (x(Ti) 0.99953) + BCC_A2 (x(Ti) 0.99992) |
| CaTi-15Ham.tdb | 1114.76 | BCC_A2 (x(Ti) 6.000e-5) + LIQUID (x(Ti) 2.600e-4) + HCP_A3 (x(Ti) 0.99963) |
| CaTi-15Ham.tdb | 716.03 | BCC_A2 (x(Ti) 0) + FCC_A1 (x(Ti) 0) + HCP_A3 (x(Ti) 0.99999) |
| CaTi-15Ham.tdb | 716.03 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0) + HCP_A3 (x(Ti) 0.99999) |
| CaTi-15Ham.tdb | 716.03 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0) + HCP_A3 (x(Ti) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Ti system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1938.15 | L'' = L' + βTi | L'': Ti 0.99577; L': Ti 0.00423; βTi: Ti 0.99691 | model | [1] Hampl 2015 | Table 3, p. 5, row 1; `ORC-DB4CHVBPYB` |  |
| 1156.15 | L' + βTi = αTi | L': Ti 3.200e-4; βTi: Ti 0.99992 | model | [1] Hampl 2015 | Table 3, p. 5, row 2; `ORC-ICEYYVA3IO` |  |
| 1115.15 | L' = βCa + αTi | L': Ti 2.600e-4; βCa: Ti 6.000e-5; αTi: Ti 0.99963 | model | [1] Hampl 2015 | Table 3, p. 5, row 3; `ORC-4ER4RGW7YR` |  |
| 716.15 | eutectic: βCa = αCa (+αTi) | αTi: Ti 0.99999 | model | [1] Hampl 2015 | Table 3, p. 5, row 4; `ORC-3ULKGJMJQ4` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Milan Hampl, Rainer Schmid-Fetzer, Experimental investigation and thermodynamic assessment of the Al–Ca–Ti system, J Mater Sci 50, 5822-5832 (2015). [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x)

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
