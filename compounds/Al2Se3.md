# Al2Se3: enthalpy of formation

> Enthalpy of formation of Al2Se3: 5 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/Al2Se3.html · Markdown: https://data.orchid-project.org/compounds/Al2Se3.md

5 accepted literature formation-enthalpy value(s) (experimental 2, model 1, DFT 2); experimental median -110.95 kJ/mol-atom (n = 2); Materials Project -108.385 kJ/mol-atom (mp-aaaaarha); OQMD -82.526 kJ/mol-atom (oqmd-1376246).

Systems: [Al–Se](https://data.orchid-project.org/systems/AL-SE.html)

## Literature values

Table: Enthalpy of formation of Al2Se3 reported in the literature (5)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -113.4 kJ/mol-atom | Al2Se3 | 298.15 | experimental | Direct synthesis calorimetry | [Al–Se](https://data.orchid-project.org/systems/AL-SE.html) | [1] Shi 2019; _cites Kapustinskii 1951_ | Table 3, p. 3, row 10 |  |
| -108.5 kJ/mol-atom | Al2Se3 | 298.15 | experimental | Combustion calorimetry | [Al–Se](https://data.orchid-project.org/systems/AL-SE.html) | [1] Shi 2019; _cites Schneider 1954_ [doi](https://doi.org/10.1002/zaac.19542770107) | Table 3, p. 3, row 11 |  |
| -107.7 kJ/mol-atom | Al2Se3 | 298.15 | model | CALPHAD | [Al–Se](https://data.orchid-project.org/systems/AL-SE.html) | [1] Shi 2019 | Table 3, p. 3, row 14 |  |
| -81.72 kJ/mol-atom | Al2Se3 | 0 | DFT | DFT | [Al–Se](https://data.orchid-project.org/systems/AL-SE.html) | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 12 |  |
| -81.24 kJ/mol-atom | Al2Se3 | 0 | DFT | DFT | [Al–Se](https://data.orchid-project.org/systems/AL-SE.html) | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 13 |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of Al2Se3

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -113.4 | kJ/mol-atom |  | 0.05 | 3.5 (solution_reaction_calorimetry, calibrated) |  |  |  | 3.5 |
| -108.5 | kJ/mol-atom |  | 0.05 | 1 (combustion_calorimetry, cleaned_below_threshold) |  |  |  | 1 |
| -107.7 | kJ/mol-atom |  | 0.05 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |
| -81.72 | kJ/mol-atom |  | 0.005 | 10.19 (dft, calibrated) |  |  |  | 10.19 |
| -81.24 | kJ/mol-atom |  | 0.005 | 10.19 (dft, calibrated) |  |  |  | 10.19 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of Al2Se3

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaaarha | -108.385 | -1.12333 | Cc | 0 | 0 | no |
| OQMD | oqmd-1376246 | -82.526 | -0.85532 | I41md | 0 | 0 | yes |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z)

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
