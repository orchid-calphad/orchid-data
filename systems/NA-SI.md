# Na–Si system

> Na–Si system: 7 accepted literature values (crystal structure 6, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NA-SI.html · Markdown: https://data.orchid-project.org/systems/NA-SI.md

7 accepted literature values from 1 paper(s) (experimental 3, model 1, DFT 3); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/NA-SI.json) · [CSV](https://data.orchid-project.org/systems/NA-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NA-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NA-SI/NaSi-12Hao.json) · [phases (7)](https://data.orchid-project.org/phases/pages/NA-SI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NA-SI.html) · [Markdown](https://data.orchid-project.org/systems/NA-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 1 |
| DFT | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NaSi-12Hao.tdb | D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang, B. Hu, Y. Du, J. Mining Metall. B, 48, 273-82(2012). [doi:10.2298/JMMB120113024H](https://doi.org/10.2298/JMMB120113024H) | `fded76f9bf76e977f01f37f7a5ef879425f4f4369342b94764352735aab1d9f4` | [viewer](https://orchid-project.org/phase-diagrams/#NA-SI/NaSi-12Hao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaSi-12Hao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaSi-12Hao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NaSi-12Hao.tdb | 1024.28 | NASI_HT (x(Si) 0.5) + LIQUID (x(Si) 0.58895) + DIAMOND_A4 (x(Si) 1) |
| NaSi-12Hao.tdb | 1024.28 | NASI_HT (x(Si) 0.5) + LIQUID (x(Si) 0.58907) + DIAMOND_A4 (x(Si) 1) |
| NaSi-12Hao.tdb | 952.66 | LIQUID#2 (x(Si) 0.05282) + LIQUID (x(Si) 0.25525) + NASI_HT (x(Si) 0.5) |
| NaSi-12Hao.tdb | 884.98 | NASI_HT (x(Si) 0.5) + NASI_LT (x(Si) 0.5) + DIAMOND_A4 (x(Si) 1) |
| NaSi-12Hao.tdb | 884.98 | LIQUID (x(Si) 0.02251) + NASI_LT (x(Si) 0.5) + NASI_HT (x(Si) 0.5) |
| NaSi-12Hao.tdb | 370.87 | LIQUID (x(Si) 0) + BCC_A2 (x(Si) 0) + NASI_LT (x(Si) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NA/NA-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NA/NA-SI.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Na–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 885.15 K | 885.15 | LT-NaSi + HT-NaSi | model | [1] Hao 2012 | p. 5; `ORC-3LFZFS6N6S` | “The Gibbs energy of the HT-NaSi phase is equal to that of the LT-NaSi phase at the transition temperature of 612 °C.” |

### Crystal structure (6)

Table: Crystal structure, Na–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 12.083 Å |  | LT-NaSi; _alloy: Na 0.5, Si 0.5_ | DFT | [1] Hao 2012 | Table 1, p. 5, row 6; `ORC-X4KAZAK4O4.f873ba` |  |
| Lattice a | 12.19 Å | 298.15 | LT-NaSi; _alloy: Na 0.5, Si 0.5_ | experimental | [1] Hao 2012; _cites Hohmann 1948_ | Table 1, p. 5, row 5; `ORC-I7K54ROIMN.18206b` |  |
| Lattice b | 6.553 Å |  | LT-NaSi; _alloy: Na 0.5, Si 0.5_ | DFT | [1] Hao 2012 | Table 1, p. 5, row 6; `ORC-X4KAZAK4O4.1c9277` |  |
| Lattice b | 6.55 Å | 298.15 | LT-NaSi; _alloy: Na 0.5, Si 0.5_ | experimental | [1] Hao 2012; _cites Hohmann 1948_ | Table 1, p. 5, row 5; `ORC-I7K54ROIMN.5a987a` |  |
| Lattice c | 11.03 Å |  | LT-NaSi; _alloy: Na 0.5, Si 0.5_ | DFT | [1] Hao 2012 | Table 1, p. 5, row 6; `ORC-X4KAZAK4O4.ee2c4b` |  |
| Lattice c | 11.18 Å | 298.15 | LT-NaSi; _alloy: Na 0.5, Si 0.5_ | experimental | [1] Hao 2012; _cites Hohmann 1948_ | Table 1, p. 5, row 5; `ORC-I7K54ROIMN.380749` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang et al., Thermodynamic modeling of the Na-X (X = Si, Ag, Cu, Cr) systems, J min metall B Metall 48, 273-282 (2012). [doi:10.2298/jmmb120113024h](https://doi.org/10.2298/jmmb120113024h)

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
