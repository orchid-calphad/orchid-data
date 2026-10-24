# AlAs: enthalpy of formation

> Enthalpy of formation of AlAs: 4 literature value(s) with sources, pages and quotes, from ORCHID.

HTML: https://data.orchid-project.org/compounds/AlAs.html · Markdown: https://data.orchid-project.org/compounds/AlAs.md

4 accepted literature formation-enthalpy value(s) (experimental 4).

Systems: [Al–As](https://data.orchid-project.org/systems/AL-AS.html)

## Literature values

Table: Enthalpy of formation of AlAs reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -74.1 kJ/mol (basis unstated) ± 6.5 | Al0.5As0.5(c) | 298.15 | experimental | solution calorimetry | [Al–As](https://data.orchid-project.org/systems/AL-AS.html) | [1] Ansara 1984; _cites ref. 40_ | Table V, p. 8, row 1; `ORC-TPCHL4IPZ3.12ad36` |  |
| -60.37 kJ/mol (basis unstated) ± 0.63 | Al0.5As0.5(c) | 298.15 | experimental | Mass spectrometry | [Al–As](https://data.orchid-project.org/systems/AL-AS.html) | [1] Ansara 1984; _cites ref. 14_ | Table V, p. 8, row 3; `ORC-IFH5NT34DE.3c3c1e` |  |
| -58.2 kJ/mol (basis unstated) ± 1.2 | Al0.5As0.5(c) | 298.15 | experimental | Sn solution calorimetry | [Al–As](https://data.orchid-project.org/systems/AL-AS.html) | [1] Ansara 1984; _cites ref. 38_ | Table V, p. 8, row 2; `ORC-7IUYZXQGF3.1efe92` |  |
| -31 kJ/mol (basis unstated) ± 3.5 | Al0.5As0.5(c) | 298.15 | experimental | Mass spectrometry and Knudsen effusion | [Al–As](https://data.orchid-project.org/systems/AL-AS.html) | [1] Ansara 1984; _cites ref. 41_ | Table V, p. 8, row 4; `ORC-3LBVASEB5P.33b988` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of AlAs

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -74.1 | kJ/mol (basis unstated) | 6.5 | 0.05 | 7 (solution_reaction_calorimetry, calibrated) |  |  |  | 7 |
| -60.37 | kJ/mol (basis unstated) | 0.63 | 0.005 | 11.2 (kems_vapour, cleaned_below_threshold) |  |  |  | 11.2 |
| -58.2 | kJ/mol (basis unstated) | 1.2 | 0.05 | 7 (solution_reaction_calorimetry, calibrated) |  |  |  | 7 |
| -31 | kJ/mol (basis unstated) | 3.5 | 0.5 | 11.2 (kems_vapour, cleaned_below_threshold) |  |  |  | 11.2 |

## Sources

1. I. Ansara, D. Dutartre, Thermodynamic study of the Al-Ga-As-Ge system, Calphad 8, 323-342 (1984). [doi:10.1016/0364-5916(84)90035-x](https://doi.org/10.1016/0364-5916%2884%2990035-x)

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
