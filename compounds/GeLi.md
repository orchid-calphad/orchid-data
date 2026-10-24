# GeLi: enthalpy of formation

> Enthalpy of formation of GeLi: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/GeLi.html · Markdown: https://data.orchid-project.org/compounds/GeLi.md

4 accepted literature formation-enthalpy value(s) (experimental 1, model 2, DFT 1); experimental median -25.5 kJ/mol-atom (n = 1); Materials Project -27.093 kJ/mol-atom (mp-aaaaaorm); OQMD -27.619 kJ/mol-atom (oqmd-7668).

Systems: [Ge–Li](https://data.orchid-project.org/systems/GE-LI.html)

## Literature values

Table: Enthalpy of formation of GeLi reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -25.5 kJ/mol-atom ± 1.6 | GeLi | 298.15 | experimental | experiment | [Ge–Li](https://data.orchid-project.org/systems/GE-LI.html) | [1] Gierlotka 2022 | Table 10, p. 8, row 6 |  |
| -33.637 kJ/mol-atom | GeLi | 0 | model |  | [Ge–Li](https://data.orchid-project.org/systems/GE-LI.html) | [1] Gierlotka 2022; _cites modeled stoichiometry of the phases based on Gruttner \[23\] description whereas this work adopts ab initio findings_ | Table 10, p. 8, row 8 |  |
| -28.25 kJ/mol-atom | GeLi | 0 | model | Calphad | [Ge–Li](https://data.orchid-project.org/systems/GE-LI.html) | [1] Gierlotka 2022 | Table 10, p. 8, row 7 |  |
| -27.542 kJ/mol-atom | GeLi | 0 | DFT | ab initio | [Ge–Li](https://data.orchid-project.org/systems/GE-LI.html) | [1] Gierlotka 2022 | Table 10, p. 8, row 5 |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of GeLi

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -25.5 | kJ/mol-atom | 1.6 | 5.000e-4 | 3.8 (experimental_unspecified, calibrated) |  |  |  | 3.8 |
| -33.637 | kJ/mol-atom |  | 5.000e-4 | 3.3 (model_calculated, calibrated) |  |  |  | 3.3 |
| -28.25 | kJ/mol-atom |  | 5.000e-4 | 3.3 (model_calculated, calibrated) |  |  |  | 3.3 |
| -27.542 | kJ/mol-atom |  | 5.000e-4 | 6.28 (dft, calibrated) |  |  |  | 6.28 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of GeLi

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaaaorm | -27.093 | -0.280801 | I4_1/a | 0 | 0 | no |
| OQMD | oqmd-7668 | -27.619 | -0.286247 | I41/a | 0 | 0 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. W. Gierlotka, A. Dębski, M. Zabrocki, A. Góral, W. Gąsior, Phase diagram, thermodynamic studies, and ab-initio calculations of the Ge-Li system, The Journal of Chemical Thermodynamics 175, 106883 (2022). [doi:10.1016/j.jct.2022.106883](https://doi.org/10.1016/j.jct.2022.106883)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
