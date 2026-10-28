# Sr–Te system

> Sr–Te system: 15 accepted literature values (invariant reaction 8, formation 5, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SR-TE.html · Markdown: https://data.orchid-project.org/systems/SR-TE.md

15 accepted literature values from 1 paper(s) (experimental 5, model 6, DFT 4); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SR-TE.json) · [CSV](https://data.orchid-project.org/systems/SR-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SR-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SR-TE/SrTe-22Yu.json) · [phases (8)](https://data.orchid-project.org/phases/pages/SR-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SR-TE.html) · [Markdown](https://data.orchid-project.org/systems/SR-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 6 |
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 2 |
| formation | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SrTe-22Yu.tdb | S. Yu, J. Wang, D. Cui, S. Chen, Q. Wu, Y. Du, J. Phase Equilib. Diffus., 43, 193-213(2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) | `e40e229b044ae412f8e7db991c209295d17f983523c19df4efbed2876640956d` | [viewer](https://orchid-project.org/phase-diagrams/#SR-TE/SrTe-22Yu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SrTe-22Yu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98261) |
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98272) |
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98254) |
| SrTe-22Yu.tdb | 1123.15 | SR2TE3 (x(Te) 0.6) + SRTE2 (x(Te) 0.66667) + LIQUID (x(Te) 0.99695) |
| SrTe-22Yu.tdb | 1123.15 | SR2TE3 (x(Te) 0.6) + SRTE2 (x(Te) 0.66667) + LIQUID (x(Te) 0.99696) |
| SrTe-22Yu.tdb | 1032.08 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.01324) + SRTE_B1 (x(Te) 0.5) |
| SrTe-22Yu.tdb | 820 | BCC_A2 (x(Te) 0) + FCC_A1 (x(Te) 0) + SRTE_B1 (x(Te) 0.5) |
| SrTe-22Yu.tdb | 722.66 | SRTE2 (x(Te) 0.66667) + HEXAGONAL_A8 (x(Te) 1) + LIQUID (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SR/SR-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SR/SR-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sr–Te system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1193.2 | L + SrTe -> Sr2Te3 | L: Te 0.982; SrTe: Te 0.5; Sr2Te3: Te 0.6 | model | [1] Yu 2022 | Table 7, p. 18, row 3; `ORC-MG4N4JJWFO` |  |
| 1193 | L + SrTe -> Sr2Te3 | L: Te 0.982; SrTe: Te 0.5; Sr2Te3: Te 0.6 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 4; `ORC-CWT5Z2JQZU` |  |
| 1123 | L + Sr2Te3 -> SrTe2 | L: Te 0.988; Sr2Te3: Te 0.6; SrTe2: Te 0.666 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 6; `ORC-5SRN4PLCQS` |  |
| 1123 | L + Sr2Te3 -> SrTe2 | L: Te 0.997; Sr2Te3: Te 0.6; SrTe2: Te 0.666 | model | [1] Yu 2022 | Table 7, p. 18, row 5; `ORC-EKU2Z7XB3A` |  |
| 1033 | eutectic: L -> (Sr) + SrTe | L: Te 0; (Sr): Te 0; SrTe: Te 0.5 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 2; `ORC-3UW5R2CU5H` |  |
| 1032.1 | eutectic: L -> (Sr) + SrTe | L: Te 0.013; (Sr): Te 0; SrTe: Te 0.5 | model | [1] Yu 2022 | Table 7, p. 18, row 1; `ORC-HQGOAG7FEM` |  |
| 722.7 | eutectic: L -> SrTe2 + (Te) | L: Te 1; SrTe2: Te 0.666; (Te): Te 1 | model | [1] Yu 2022 | Table 7, p. 18, row 7; `ORC-UN37H52B3H` |  |
| 722 | eutectic: L -> SrTe2 + (Te) | L: Te 1; SrTe2: Te 0.666; (Te): Te 1 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 8; `ORC-OWZS5ZBQPW` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Sr–Te system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| SrTe |  | -187.88 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022; _cites Jain 2013_ [doi](https://doi.org/10.1063/1.4812323) | Table 2, p. 5, row 22; `ORC-WCUTKKVVE2` |  |
| SrTe |  | -174 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022; _cites Labidi 2008_ | Table 2, p. 5, row 20; `ORC-AMQQ2ERCC5` |  |
| SrTe | [SrTe](https://data.orchid-project.org/compounds/SrTe.html) | -168 kJ/mol-atom | 298.15 | model | -188.541 (mp-aaaaacxi) | -168.527 (oqmd-656717) | [1] Yu 2022 | Table 2, p. 5, row 23; `ORC-RB7CJ7X7UV` |  |
| SrTe |  | -167.98 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022 | Table 2, p. 5, row 19; `ORC-ZGM6VXBR7V` |  |
| SrTe |  | -167.97 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022; _cites Saal 2013_ [doi](https://doi.org/10.1007/s11837-013-0755-4) | Table 2, p. 5, row 21; `ORC-W6B74HU54M` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Sr–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1763 K | 1763 | L -> SrTe; _L: Te 0.5; SrTe: Te 0.5_ | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 10; `ORC-RC3O4W4YLK` |  |
| Phase transition | 1764 K | 1764 | L -> SrTe; _L: Te 0.5; SrTe: Te 0.5_ | model | [1] Yu 2022 | Table 7, p. 18, row 9; `ORC-RCMSIU7NLK` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z)

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
