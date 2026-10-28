# Ni–Ru system

> Ni–Ru system: 4 accepted literature values (formation 4) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NI-RU.html · Markdown: https://data.orchid-project.org/systems/NI-RU.md

4 accepted literature values from 1 paper(s) (DFT 4); 3 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/NI-RU.json) · [CSV](https://data.orchid-project.org/systems/NI-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NI-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-01Che-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/NI-RU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NI-RU.html) · [Markdown](https://data.orchid-project.org/systems/NI-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NiRu-01Che-LB.tdb | P.-Y. Chevalier, E. Fischer, unpublished, 2001. | `cfb9ea78cdca6ee26eeea2aa7b91d55a78c4d5f2636678699421a39d1aa6e072` | [viewer](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-01Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiRu-01Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiRu-01Che-LB.json) |
| NiRu-04Hal.tdb | S. Hallstroem, J. Phase Equilib. Diffus., 25, 252-54(2004). [doi:10.1361/15477030419504](https://doi.org/10.1361/15477030419504) | `d86ac6781c062de73ce0afb651fbf2d80fb33fda4b6c3e6d0e37fc7b079999e9` | [viewer](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-04Hal.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiRu-04Hal.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiRu-04Hal.json) |
| NiRu-08Hal.tdb | S. Hallstroem, D. Andersson, A. Ruban, J. Agren, Acta Mater., 56, 4062-69(2008). [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028) | `b00a907636215ffed49ea53e7ca32d80c1236b024aecb2308df2c9ad79e97f61` | [viewer](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-08Hal.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiRu-08Hal.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiRu-08Hal.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NiRu-01Che-LB.tdb | 1807.84 | LIQUID (x(Ru) 0.26144) + FCC_A1 (x(Ru) 0.31942) + HCP_A3 (x(Ru) 0.5053) |
| NiRu-04Hal.tdb | 1836.9 | LIQUID (x(Ru) 0.29256) + FCC_A1 (x(Ru) 0.34142) + HCP_A3 (x(Ru) 0.52632) |
| NiRu-08Hal.tdb | 1801.84 | LIQUID (x(Ru) 0.25525) + FCC_A1 (x(Ru) 0.31029) + HCP_A3 (x(Ru) 0.51555) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NI/NI-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NI/NI-RU.json) · [CALPHAD hull NiRu-01Che-LB](https://data.orchid-project.org/hulls/calphad-sgte/NI/NI-RU--NiRu-01Che-LB.json) · [CALPHAD hull NiRu-04Hal](https://data.orchid-project.org/hulls/calphad-sgte/NI/NI-RU--NiRu-04Hal.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ni–Ru system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ni2Ru2 |  | 14.6 kJ/mol-atom | 0 | DFT |  |  | [1] Hallström 2008 | Table A.1, p. 7, row 4; `ORC-UKEBJMLR64` |  |
| Ni3Ru |  | 17.56 kJ/mol-atom | 0 | DFT |  |  | [1] Hallström 2008 | Table A.1, p. 7, row 3; `ORC-EEJVYGIGY3` |  |
| NiRu |  | 25.35 kJ/mol-atom | 0 | DFT |  |  | [1] Hallström 2008 | Table A.1, p. 7, row 6; `ORC-22FCDAQURR` |  |
| NiRu3 |  | 13.8 kJ/mol-atom | 0 | DFT |  |  | [1] Hallström 2008 | Table A.1, p. 7, row 5; `ORC-ZC5QIC3EQM` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Samuel Hallström, David Andersson, Andrei Ruban, John Ågren, Thermodynamic reassessment of the Ni–Ru system and assessment of the Al–Ni–Ru system at 1273–1523 K using ab initio calculations, Acta Materialia 56, 4062-4069 (2008). [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028)

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
