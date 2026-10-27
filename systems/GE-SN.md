# Ge–Sn system

> Ge–Sn system: 10 accepted literature values (mixing / partial 10) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-SN.html · Markdown: https://data.orchid-project.org/systems/GE-SN.md

10 accepted literature values from 3 paper(s) (experimental 9, model 1); 2 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-SN.json) · [CSV](https://data.orchid-project.org/systems/GE-SN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-SN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-SN/GeSn-79Ans.json) · [phases (6)](https://data.orchid-project.org/phases/pages/GE-SN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GE-SN.html) · [Markdown](https://data.orchid-project.org/systems/GE-SN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| mixing / partial | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeSn-79Ans.tdb | I. Ansara, J.P. Bros, M. Gambino, Calphad, 3, 225-233(1979). [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) | `e5c9457371c4b038dc9e341e04bff8bfa0ea6fb59f4d71e8a0ad94e456f90bc4` | [viewer](https://orchid-project.org/phase-diagrams/#GE-SN/GeSn-79Ans.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeSn-79Ans.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeSn-79Ans.json) |
| GeSn-96Feu-LB.tdb | Y. Feutelais, B. Legendre, S.G. Fries, Calphad, 20, 109-23(1996). [doi:10.1016/0364-5916(96)00018-1](https://doi.org/10.1016/0364-5916%2896%2900018-1) | `5b1370f2e9cad0c7fea42f48a3f7a068dfa6aaa7d457335e9a8be096fbeb4a06` | [viewer](https://orchid-project.org/phase-diagrams/#GE-SN/GeSn-96Feu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeSn-96Feu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeSn-96Feu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeSn-79Ans.tdb | 504.12 | DIAMOND_A4 (x(Sn) 5.000e-5) + LIQUID (x(Sn) 0.99682) + BCT_A5 (x(Sn) 1) |
| GeSn-79Ans.tdb | 504.12 | DIAMOND_A4 (x(Sn) 5.000e-5) + LIQUID (x(Sn) 0.9968) + BCT_A5 (x(Sn) 1) |
| GeSn-79Ans.tdb | 504.12 | DIAMOND_A4 (x(Sn) 5.000e-5) + LIQUID (x(Sn) 0.9968) + BCT_A5 (x(Sn) 1) |
| GeSn-96Feu-LB.tdb | 504.21 | DIAMOND_A4 (x(Sn) 0.00639) + LIQUID (x(Sn) 0.99712) + BCT_A5 (x(Sn) 0.99999) |
| GeSn-96Feu-LB.tdb | 504.21 | DIAMOND_A4 (x(Sn) 0.00639) + LIQUID (x(Sn) 0.99711) + BCT_A5 (x(Sn) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-SN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-SN.json) · [CALPHAD hull GeSn-79Ans](https://data.orchid-project.org/hulls/calphad-sgte/GE/GE-SN--GeSn-79Ans.json)

## Other properties

### Mixing / partial (10)

Table: Mixing / partial, Ge–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 40.1004 kJ/mol (basis unstated) |  | liquid | model | [1] Feutelais 1996 | Table 4, p. 7, row 5; `ORC-7DADQ36DNV` |  |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 41.7145 kJ/mol (basis unstated) | 623 | liquid | experimental | [1] Feutelais 1996; _cites ref. 66_ | Table 4, p. 7, row 2; `ORC-PR2XJO4YUO` |  |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 41.7145 kJ/mol (basis unstated) | 623 | liquid | experimental | [1] Feutelais 1996; _cites ref. 62_ | Table 4, p. 7, row 1; `ORC-SR2B7XUW4G` |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 3.35 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 3; `ORC-CDRKPRLCTJ.af1deb` |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 3.65 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 1; `ORC-DCI5CZ3B74.14e4db` |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 3.1 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 4; `ORC-PBFHC2AQZZ.5326bb` |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 2.86 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 2; `ORC-U3M7BV3TFW.44cbf7` |  |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 40.1538 kJ/mol (basis unstated) | 963.5 | liquid | experimental | [1] Feutelais 1996; _cites ref. 66_ | Table 4, p. 7, row 3; `ORC-RTUHPVTOBT` |  |
| Partial enthalpy; _printed: heat of solution_ | 3.21 kJ/mol (basis unstated) | 973 |  | experimental | [3] Ansara 1979; _cites SCHMIEDL 1973_ | p. 4; `ORC-FTW76RPS7P` | “MATHIEU (25) has measured the heat of solution of Ge in liquid tin at infinite dilution at973K and obtaineda value of 3210 J.mol'1 if the liquid elmentsare taken as reference state.” |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 40.3338 kJ/mol (basis unstated) | 1083 | liquid | experimental | [1] Feutelais 1996; _cites ref. 79_ | Table 4, p. 7, row 4; `ORC-3GYEMUWXL6` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Y. Feutelais, B. Legendre, S.G. Fries, Thermodynamic evaluation of the system germanium — tin, Calphad 20, 109-123 (1996). [doi:10.1016/0364-5916(96)00018-1](https://doi.org/10.1016/0364-5916%2896%2900018-1)
2. W. Gierlotka, A. Dębski, M. Zabrocki, A. Góral, W. Gąsior, Phase diagram, thermodynamic studies, and ab-initio calculations of the Ge-Li system, The Journal of Chemical Thermodynamics 175, 106883 (2022). [doi:10.1016/j.jct.2022.106883](https://doi.org/10.1016/j.jct.2022.106883)
3. I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979). [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
