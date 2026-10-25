# Ge3Nb5: enthalpy of formation

> Enthalpy of formation of Ge3Nb5: 4 literature value(s) with sources, pages and quotes, from ORCHID.

HTML: https://data.orchid-project.org/compounds/Ge3Nb5.html · Markdown: https://data.orchid-project.org/compounds/Ge3Nb5.md

4 accepted literature formation-enthalpy value(s) (model 2, DFT 2).

Systems: [Ge–Nb](https://data.orchid-project.org/systems/GE-NB.html)

## Literature values

Table: Enthalpy of formation of Ge3Nb5 reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -42.892 kJ/mol (basis unstated) | Nb5Ge3 | 298.15 | model | Calphad | [Ge–Nb](https://data.orchid-project.org/systems/GE-NB.html) | [1] Utton 2017 | Table 2, p. 6, row 6; `ORC-WVLZUEQFJO` |  |
| -42 kJ/mol (basis unstated) | Nb5Ge3 | 298.15 | model | Calphad | [Ge–Nb](https://data.orchid-project.org/systems/GE-NB.html) | [1] Utton 2017 | Table 2, p. 6, row 2; `ORC-HC64QSVJEY` |  |
| -46.63 kJ/mol (basis unstated) | Nb5Ge3 | 0 | DFT | ab initio | [Ge–Nb](https://data.orchid-project.org/systems/GE-NB.html) | [1] Utton 2017; _cites Papadimitriou 2015_ [doi](https://doi.org/10.1007/s11661-015-3149-0) | Table 2, p. 6, row 5; `ORC-F5XXKDLBS5` |  |
| -46.53 kJ/mol (basis unstated) | Nb5Ge3 | 0 | DFT | ab initio | [Ge–Nb](https://data.orchid-project.org/systems/GE-NB.html) | [1] Utton 2017; _cites Papadimitriou 2015_ [doi](https://doi.org/10.1007/s11661-015-3149-0) | Table 2, p. 6, row 1; `ORC-B2ED5JJWQY` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of Ge3Nb5

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -42.892 | kJ/mol (basis unstated) |  | 5.000e-4 | 27.2 (model_calculated, calibrated) |  |  |  | 27.2 |
| -42 | kJ/mol (basis unstated) |  | 0.5 | 27.2 (model_calculated, calibrated) |  |  |  | 27.2 |
| -46.63 | kJ/mol (basis unstated) |  | 0.005 | 63.7 (dft, calibrated) |  |  |  | 63.7 |
| -46.53 | kJ/mol (basis unstated) |  | 0.005 | 63.7 (dft, calibrated) |  |  |  | 63.7 |

## Sources

1. Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017). [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279)

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
