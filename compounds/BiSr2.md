# BiSr2: enthalpy of formation

> Enthalpy of formation of BiSr2: 3 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/BiSr2.html · Markdown: https://data.orchid-project.org/compounds/BiSr2.md

3 accepted literature formation-enthalpy value(s) (experimental 1, model 1, DFT 1); experimental median -104 kJ/mol-atom (n = 1); Materials Project -72.467 kJ/mol-atom (mp-aaaabrvf); OQMD -74.05 kJ/mol-atom (oqmd-7610).

Systems: [Bi–Sr](https://data.orchid-project.org/systems/BI-SR.html)

## Literature values

Table: Enthalpy of formation of BiSr2 reported in the literature (3)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -104 kJ/mol-atom ± 1.67 | Sr2Bi | 298.15 | experimental |  | [Bi–Sr](https://data.orchid-project.org/systems/BI-SR.html) | [1] Wang 2014; _cites Shukarev 1956_ | Table 2, p. 3, row 22 |  |
| -76.47 kJ/mol-atom | Sr2Bi | 298.15 | model | CALPHAD | [Bi–Sr](https://data.orchid-project.org/systems/BI-SR.html) | [1] Wang 2014 | Table 2, p. 3, row 24 |  |
| -73.23 kJ/mol-atom | Sr2Bi | 298.15 | DFT | First-principles calculations | [Bi–Sr](https://data.orchid-project.org/systems/BI-SR.html) | [1] Wang 2014 | Table 2, p. 3, row 23 |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of BiSr2

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -104 | kJ/mol-atom | 1.67 | 0.05 | 3.5 (unknown, calibrated) |  |  |  | 3.5 |
| -76.47 | kJ/mol-atom |  | 0.005 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |
| -73.23 | kJ/mol-atom |  | 0.005 | 8.472 (dft, calibrated) |  |  |  | 8.472 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of BiSr2

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaabrvf | -72.467 | -0.751074 | I4/mmm | 2.4298 | 0.0252 | no |
| OQMD | oqmd-7610 | -74.05 | -0.767472 | I4/mmm | 1.9747 | 0.0205 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Yao Wang, Jinghua Xin, Chong Chen, Shuhong Liu, Biao Hu, Yong Du, Thermodynamic assessment of the Sr–In and Sr–Bi systems supported by first-principles calculations, Calphad 45, 49-54 (2014). [doi:10.1016/j.calphad.2013.12.001](https://doi.org/10.1016/j.calphad.2013.12.001)

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
