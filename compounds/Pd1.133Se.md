# Pd1.133Se: enthalpy of formation

> Enthalpy of formation of Pd1.133Se: 3 literature value(s) with sources, pages and quotes, from ORCHID.

HTML: https://data.orchid-project.org/compounds/Pd1.133Se.html · Markdown: https://data.orchid-project.org/compounds/Pd1.133Se.md

3 accepted literature formation-enthalpy value(s) (experimental 1, model 2).

Systems: [Pd–Se](https://data.orchid-project.org/systems/PD-SE.html)

## Literature values

Table: Enthalpy of formation of Pd1.133Se reported in the literature (3)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -72.68 kJ/mol (basis unstated) ± 0.82 | Pd1.133Se (i.e. Pd17Se15) | 298.15 | experimental |  | [Pd–Se](https://data.orchid-project.org/systems/PD-SE.html) | [1] Bordier 2014; _cites Stolyarova 2011_ [doi](https://doi.org/10.1134/s0016702911030098) | Table 2, p. 3, row 3; `ORC-CRYG5DNRFE.9624a3` |  |
| -72.68 kJ/mol (basis unstated) ± 0.82 | Pd1.133Se | 298.15 | model |  | [Pd–Se](https://data.orchid-project.org/systems/PD-SE.html) | [1] Bordier 2014; _cites Stolyarova 2011_ [doi](https://doi.org/10.1134/s0016702911030098) | Table 3, p. 7, row 9; `ORC-UXEK7KXI32.2d22a7` |  |
| -72.17 kJ/mol (basis unstated) | Pd1.133Se | 298.15 | model |  | [Pd–Se](https://data.orchid-project.org/systems/PD-SE.html) | [1] Bordier 2014 | Table 3, p. 7, row 10; `ORC-NJHWKGGJY7.fb1e59` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of Pd1.133Se

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -72.68 | kJ/mol (basis unstated) | 0.82 | 0.005 | 38.5 (unknown, calibrated) |  |  |  | 38.5 |
| -72.68 | kJ/mol (basis unstated) | 0.82 | 0.005 | 42.9 (model_calculated, calibrated) |  |  |  | 42.9 |
| -72.17 | kJ/mol (basis unstated) |  | 0.005 | 42.9 (model_calculated, calibrated) |  |  |  | 42.9 |

## Sources

1. S. Bordier, A. Chocard, S. Gossé, Thermodynamic assessment of the palladium–selenium (Pd–Se) system, Journal of Nuclear Materials 451, 120-129 (2014). [doi:10.1016/j.jnucmat.2014.03.044](https://doi.org/10.1016/j.jnucmat.2014.03.044)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-dft-benchmark
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162, https://doi.org/10.1038/sdata.2017.162; B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

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

@misc{orchid_dft_benchmark_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-dft-benchmark},
  url       = {https://doi.org/10.5281/zenodo.PENDING-dft-benchmark},
  note      = {Version 1, machine-extracted}
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
