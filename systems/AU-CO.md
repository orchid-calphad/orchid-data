# Au–Co system

> Au–Co system: 4 accepted literature values (invariant reaction 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-CO.html · Markdown: https://data.orchid-project.org/systems/AU-CO.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-CO.json) · [CSV](https://data.orchid-project.org/systems/AU-CO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-CO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-CO/AuCo-04Kor-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AU-CO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AU-CO.html) · [Markdown](https://data.orchid-project.org/systems/AU-CO.md)

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
| AuCo-04Kor-LB.tdb | J. Korb, unpublished, GTT, 2004. | `fe460222ed545fd85ed596cd8750d71d69618b1e3001e7f44bf234a6f8948df0` | [viewer](https://orchid-project.org/phase-diagrams/#AU-CO/AuCo-04Kor-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuCo-04Kor-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuCo-04Kor-LB.json) |
| AuCo-09Don.tdb | H.Q. Dong, S. Jin, L.G. Zhang, J.S. Wang, X.M. Tao, H.S. Liu, Z.P. Jin, J. Electron. Mater., 38, 2158-69(2009). [doi:10.1007/s11664-009-0874-4](https://doi.org/10.1007/s11664-009-0874-4) | `bf5afe9f855266c50a3685830a98ff6f614484d33a960e92ab499fbb5e626ce1` | [viewer](https://orchid-project.org/phase-diagrams/#AU-CO/AuCo-09Don.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuCo-09Don.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuCo-09Don.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuCo-04Kor-LB.tdb | 1270.51 | FCC_A1#2 (x(Co) 0.22225) + LIQUID (x(Co) 0.28355) + FCC_A1 (x(Co) 0.98067) |
| AuCo-04Kor-LB.tdb | 695.15 | FCC_A1 (x(Co) 6.600e-4) + HCP_A3 (x(Co) 0.99886) + FCC_A1#2 (x(Co) 0.99888) |
| AuCo-09Don.tdb | 1270.61 | FCC_A1#2 (x(Co) 0.20778) + LIQUID (x(Co) 0.2619) + FCC_A1 (x(Co) 0.97723) |
| AuCo-09Don.tdb | 697.61 | FCC_A1#2 (x(Co) 0.01035) + HCP_A3 (x(Co) 0.99865) + FCC_A1 (x(Co) 0.99893) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-CO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-CO.json) · [CALPHAD hull AuCo-04Kor-LB](https://data.orchid-project.org/hulls/calphad-sgte/AU/AU-CO--AuCo-04Kor-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Co system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1270.4 | eutectic: L -> Au + αCo | L: Co 0.262; Au: Co 0.208; αCo: Co 0.977 | model | [1] Dong 2009 | Table I, p. 2, row 2; `ORC-XIWE5MLPPT` |  |
| 1269.5 | eutectic: L -> Au + αCo | L: Co 0.248; Au: Co 0.23; αCo: Co 0.981 | experimental | [1] Dong 2009; _cites Okamoto 1985_ [doi](https://doi.org/10.1007/bf02869509) | Table I, p. 2, row 1; `ORC-DT6F2PSNTN` |  |
| 695 | eutectoid: αCo -> Au + εCo | αCo: Co 0.9995; Au: Co 0.002 | experimental | [1] Dong 2009; _cites Okamoto 1985_ [doi](https://doi.org/10.1007/bf02869509) | Table I, p. 2, row 3; `ORC-WFREF5GXLC` |  |
| 694 | eutectoid: αCo -> Au + εCo | αCo: Co 0.999; Au: Co 0.009; εCo: Co 0.9993 | model | [1] Dong 2009 | Table I, p. 2, row 4; `ORC-7PGOOGQPD2` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. H. Q. Dong, S. Jin, L. G. Zhang, J. S. Wang, X. M. Tao, H. S. Liu et al., Thermodynamic Assessment of the Au-Co-Sn Ternary System, Journal of Elec Materi 38, 2158-2169 (2009). [doi:10.1007/s11664-009-0874-4](https://doi.org/10.1007/s11664-009-0874-4)

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
