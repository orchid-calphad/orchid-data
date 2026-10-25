# HfNi: enthalpy of formation

> Enthalpy of formation of HfNi: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/HfNi.html · Markdown: https://data.orchid-project.org/compounds/HfNi.md

4 accepted literature formation-enthalpy value(s) (model 3, DFT 1); Materials Project -50.09 kJ/mol-atom (mp-aaacfyaa); OQMD -50.079 kJ/mol-atom (oqmd-30515).

Systems: [Hf–Ni](https://data.orchid-project.org/systems/HF-NI.html)

## Literature values

Table: Enthalpy of formation of HfNi reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -50.06 kJ/mol-atom | NiHf(B33) | 298.15 | model |  | [Hf–Ni](https://data.orchid-project.org/systems/HF-NI.html) | [1] Ross 2018; _cites Berche 2016_ [doi](https://doi.org/10.1016/j.commatsci.2016.08.042) | Table 1, p. 4, row 9; `ORC-OFNCAV2ZOM.953f73` |  |
| -50 kJ/mol-atom | NiHf(B33) | 298.15 | model |  | [Hf–Ni](https://data.orchid-project.org/systems/HF-NI.html) | [1] Ross 2018 | Table 1, p. 4, row 8; `ORC-2V6MMT6W3Q.b18886` |  |
| -41.77 kJ/mol-atom | NiHf(B2) | 298.15 | model |  | [Hf–Ni](https://data.orchid-project.org/systems/HF-NI.html) | [1] Ross 2018 | Table 1, p. 4, row 10; `ORC-SMDYQTNVJ5.a51ff8` |  |
| -50.06 kJ/mol (basis unstated) | B33-HfNi | 0 | DFT | DFT | [Hf–Ni](https://data.orchid-project.org/systems/HF-NI.html) | [2] Berche 2016 | Table 2, p. 4, row 5; `ORC-SWSJNQ2BTR.6e34ee` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of HfNi

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -50.06 | kJ/mol-atom |  | 0.005 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |
| -50 | kJ/mol-atom |  | 0.05 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |
| -41.77 | kJ/mol-atom |  | 0.005 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |
| -50.06 | kJ/mol (basis unstated) |  | 0.005 | 8.332 (dft, calibrated) |  |  |  | 8.332 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of HfNi

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaacfyaa | -50.09 | -0.519151 | Cmcm | 0 | 0 | no |
| OQMD | oqmd-30515 | -50.079 | -0.519031 | Cmcm | 0 | 0 | no |
| OQMD | oqmd-305271 | -41.908 | -0.434345 | Pm-3m | 8.1709 | 0.0847 | yes |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. A.J. Ross, T. Gheno, P.K. Ray, M.J. Kramer, X.L. Liu, G. Lindwall et al., A first-principles based description of the Hf-Ni system supported by high-temperature synchrotron experiments, Thermochimica Acta 668, 142-151 (2018). [doi:10.1016/j.tca.2018.08.011](https://doi.org/10.1016/j.tca.2018.08.011)
2. A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016). [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042)

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
