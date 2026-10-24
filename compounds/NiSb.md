# NiSb: enthalpy of formation

> Enthalpy of formation of NiSb: 4 literature value(s) with sources, pages and quotes, from ORCHID.

HTML: https://data.orchid-project.org/compounds/NiSb.html · Markdown: https://data.orchid-project.org/compounds/NiSb.md

4 accepted literature formation-enthalpy value(s) (experimental 2, model 2).

Systems: [Ni–Sb](https://data.orchid-project.org/systems/NI-SB.html)

## Literature values

Table: Enthalpy of formation of NiSb reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -33.472 kJ/mol (basis unstated) | ζ(NiSb) | 298.15 | experimental |  | [Ni–Sb](https://data.orchid-project.org/systems/NI-SB.html) | [1] Cao 2013; _cites Korber 1937_ | Table IV, p. 9, row 1; `ORC-ABDJTH4LAW` |  |
| -32.543 kJ/mol (basis unstated) ± 0.494 | ζ(NiSb) | 1060 | experimental |  | [Ni–Sb](https://data.orchid-project.org/systems/NI-SB.html) | [1] Cao 2013; _cites Predel 1978_ [doi](https://doi.org/10.1016/0040-6031%2878%2985146-6) | Table IV, p. 9, row 3; `ORC-64UDB5YW55.8b29a9` |  |
| -32.659 kJ/mol (basis unstated) | ζ(NiSb) | 1060 | model |  | [Ni–Sb](https://data.orchid-project.org/systems/NI-SB.html) | [1] Cao 2013 | Table IV, p. 9, row 4; `ORC-QBMBSSVL7S` |  |
| -32.171 kJ/mol (basis unstated) | ζ(NiSb) | 298.15 | model |  | [Ni–Sb](https://data.orchid-project.org/systems/NI-SB.html) | [1] Cao 2013 | Table IV, p. 9, row 2; `ORC-GQGFCXOC6L` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of NiSb

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -33.472 | kJ/mol (basis unstated) |  | 5.000e-4 | 7 (unknown, calibrated) |  |  |  | 7 |
| -32.543 | kJ/mol (basis unstated) | 0.494 | 5.000e-4 | 7 (unknown, calibrated) |  |  |  | 7 |
| -32.659 | kJ/mol (basis unstated) |  | 5.000e-4 | 6.8 (model_calculated, calibrated) |  |  |  | 6.8 |
| -32.171 | kJ/mol (basis unstated) |  | 5.000e-4 | 6.8 (model_calculated, calibrated) |  |  |  | 6.8 |

## Sources

1. Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013). [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID DFT-vs-experiment formation-enthalpy benchmark (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-dft-benchmark
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162, https://doi.org/10.1038/sdata.2017.162; B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_dft_benchmark_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID DFT-vs-experiment formation-enthalpy benchmark}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-dft-benchmark},
  url       = {https://doi.org/10.5281/zenodo.PENDING-dft-benchmark},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
