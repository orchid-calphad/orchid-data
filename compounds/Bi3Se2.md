# Bi3Se2: enthalpy of formation

> Enthalpy of formation of Bi3Se2: 3 literature value(s) with sources, pages and quotes, from ORCHID.

HTML: https://data.orchid-project.org/compounds/Bi3Se2.html · Markdown: https://data.orchid-project.org/compounds/Bi3Se2.md

3 accepted literature formation-enthalpy value(s) (experimental 1, model 1, DFT 1); experimental median -26.4 kJ/mol-atom (n = 1).

Systems: [Bi–Se](https://data.orchid-project.org/systems/BI-SE.html)

## Literature values

Table: Enthalpy of formation of Bi3Se2 reported in the literature (3)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -26.4 kJ/mol-atom | Bi3Se2 | 298.15 | experimental | EMF | [Bi–Se](https://data.orchid-project.org/systems/BI-SE.html) | [1] Zhou 2024; _cites Hasanova 2021_ [doi](https://doi.org/10.1007/s11837-021-04621-1) | Table 3, p. 5, row 62; `ORC-CCJTFOHABK` |  |
| -26.405 kJ/mol-atom | Bi3Se2 | 298.15 | model | CALPHAD | [Bi–Se](https://data.orchid-project.org/systems/BI-SE.html) | [1] Zhou 2024 | Table 3, p. 5, row 64; `ORC-BVZNK33RJI` |  |
| -24.893 kJ/mol-atom | Bi3Se2 | 0 | DFT | First-principles | [Bi–Se](https://data.orchid-project.org/systems/BI-SE.html) | [1] Zhou 2024; _cites Saal 2013_ [doi](https://doi.org/10.1007/s11837-013-0755-4) | Table 3, p. 5, row 63; `ORC-REKUR5QNIQ` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of Bi3Se2

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -26.4 | kJ/mol-atom |  | 5.000e-5 | 4.6 (emf, cleaned_below_threshold) |  |  |  | 4.6 |
| -26.405 | kJ/mol-atom |  | 5.000e-5 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |
| -24.893 | kJ/mol-atom |  | 5.000e-5 | 10.01 (dft, calibrated) |  |  |  | 10.01 |

## Sources

1. Jiaqiang Zhou, Jiong Wang, Biao Hu, Dongyu Cui, Thermodynamic Modeling of the Bi-Se and Bi-Te Binary Systems, J. Phase Equilib. Diffus. 45, 89-113 (2024). [doi:10.1007/s11669-024-01093-z](https://doi.org/10.1007/s11669-024-01093-z)

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
