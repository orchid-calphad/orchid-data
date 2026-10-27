# Ag–B system

> Ag–B system: 4 accepted literature values (invariant reaction 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-B.html · Markdown: https://data.orchid-project.org/systems/AG-B.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-B.json) · [CSV](https://data.orchid-project.org/systems/AG-B.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-B) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-B/AgB-04Kor-LB.json) · [phases (6)](https://data.orchid-project.org/phases/pages/AG-B.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-B.html) · [Markdown](https://data.orchid-project.org/systems/AG-B.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgB-04Kor-LB.tdb | J. Korb, unpublished, GTT, 2004. | `433d8df8e0788ba9ae093336f87453eeec4328f893d74a5d1b0cbe1ebd058f90` | [viewer](https://orchid-project.org/phase-diagrams/#AG-B/AgB-04Kor-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgB-04Kor-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgB-04Kor-LB.json) |
| AgB-20Zho.tdb | J. Zhou, B. Hu, Y. Jiang, C. Qiu, Y. Du, H. Yin, J. Phase Equilib. Diffus., 41, 257-68(2020). [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) | `95c088f2f369a16b9a2d202fe7a6f187d294196dd63c43f6201f7bebb7a7e862` | [viewer](https://orchid-project.org/phase-diagrams/#AG-B/AgB-20Zho.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgB-20Zho.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgB-04Kor-LB.tdb | 2346.91 | LIQUID#2 (x(B) 0.02996) + LIQUID (x(B) 0.99879) + BETA_RHOMBO_B (x(B) 1) |
| AgB-04Kor-LB.tdb | 2346.91 | LIQUID#2 (x(B) 0.02997) + LIQUID (x(B) 0.99879) + BETA_RHOMBO_B (x(B) 1) |
| AgB-04Kor-LB.tdb | 1234.92 | FCC_A1 (x(B) 1.100e-4) + LIQUID (x(B) 1.200e-4) + BETA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 2342.17 | LIQUID#2 (x(B) 0.0066) + LIQUID (x(B) 0.9934) + BETA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1388 | LIQUID (x(B) 0) + ALPHA_RHOMBO_B (x(B) 1) + BETA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1235.48 | LIQUID (x(B) 0) + FCC_A1 (x(B) 4.900e-4) + ALPHA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1235.48 | LIQUID (x(B) 0) + FCC_A1 (x(B) 4.900e-4) + ALPHA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1234.93 | LIQUID (x(B) 0) + FCC_A1 (x(B) 0) + ALPHA_RHOMBO_B (x(B) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-B.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-B.json) · [CALPHAD hull AgB-04Kor-LB](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-B--AgB-04Kor-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–B system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2348.15 | monotectic: Liquid# 2 -> Liquid#1 + (βB) | (βB): B 1 | experimental | [1] Zhou 2020; _cites Wald 1970_ | Table 4, p. 7, row 2; `ORC-RBDMU3DBSM` |  |
| 2342.15 | monotectic: Liquid# 2 -> Liquid#1 + (βB) | Liquid# 2: B 0.9934; Liquid#1: B 0.0066; (βB): B 1 | model | [1] Zhou 2020 | Table 4, p. 7, row 1; `ORC-WCIG7F4BOI` |  |
| 1237.15 | eutectic: Liquid#1 -> (Ag) + (βB) | Liquid#1: B 0.0015; (Ag): B 0; (βB): B 1 | model | [1] Zhou 2020 | Table 4, p. 7, row 3; `ORC-MBWMSK2T7T` |  |
| 1235.15 | eutectic: Liquid#1 -> (Ag) + (βB) | (Ag): B 0; (βB): B 1 | experimental | [1] Zhou 2020; _cites Wald 1970_ | Table 4, p. 7, row 4; `ORC-VFK2VLNOGP` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020). [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5)

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
