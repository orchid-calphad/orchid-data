# Sn–Se system

> Sn–Se system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SN-SE.html · Markdown: https://data.orchid-project.org/systems/SN-SE.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SN-SE/SnSe-96Feu-LB.json) · [Markdown](https://data.orchid-project.org/systems/SN-SE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SnSe-96Feu-LB.tdb | Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996). [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) | `1a2bab98ceb7b79f5ea186ba4108dd8448be44ee5721e29376f34f890a048b7e` | [viewer](https://orchid-project.org/phase-diagrams/#SN-SE/SnSe-96Feu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SnSe-96Feu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SnSe-96Feu-LB.tdb | 1104.33 | LIQUID#2 (x(Se) 0.23922) + LIQUID (x(Se) 0.42889) + SNSE_B33 (x(Se) 0.5) |
| SnSe-96Feu-LB.tdb | 904.42 | SNSE_B33 (x(Se) 0.5) + LIQUID (x(Se) 0.61104) + SNSE2_C6 (x(Se) 0.66667) |
| SnSe-96Feu-LB.tdb | 796.51 | SNSE_B16 (x(Se) 0.5) + SNSE_B33 (x(Se) 0.5) + SNSE2_C6 (x(Se) 0.66667) |
| SnSe-96Feu-LB.tdb | 796.51 | LIQUID (x(Se) 0.00805) + SNSE_B16 (x(Se) 0.5) + SNSE_B33 (x(Se) 0.5) |
| SnSe-96Feu-LB.tdb | 505.06 | BCT_A5 (x(Se) 0) + LIQUID (x(Se) 7.000e-5) + SNSE_B16 (x(Se) 0.5) |
| SnSe-96Feu-LB.tdb | 493.92 | SNSE2_C6 (x(Se) 0.66667) + LIQUID (x(Se) 0.99975) + HEXAGONAL_A8 (x(Se) 1) |

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
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
