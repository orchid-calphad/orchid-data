# Bi2Cs3: enthalpy of formation

> Enthalpy of formation of Bi2Cs3: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/Bi2Cs3.html · Markdown: https://data.orchid-project.org/compounds/Bi2Cs3.md

4 accepted literature formation-enthalpy value(s) (experimental 1, model 1, DFT 2); experimental median -40.7 kJ/mol-atom (n = 1); Materials Project -31.375 kJ/mol-atom (mp-aaabgrwc); OQMD -34.17 kJ/mol-atom (oqmd-22902).

Systems: [Bi–Cs](https://data.orchid-project.org/systems/BI-CS.html)

## Literature values

Table: Enthalpy of formation of Bi2Cs3 reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -40.7 kJ/mol-atom | Bi2Cs3 | 298.15 | experimental | EMF | [Bi–Cs](https://data.orchid-project.org/systems/BI-CS.html) | [1] Djaballah 2015; _cites Voronin 1975_ | Table 2, p. 4, row 8; `ORC-GA3QTP5BWE.2fe8a5` |  |
| -33.968 kJ/mol-atom | Bi2Cs3 |  | model | CALPHAD | [Bi–Cs](https://data.orchid-project.org/systems/BI-CS.html) | [1] Djaballah 2015 | Table 2, p. 4, row 11; `ORC-UOGIHLYDCO.1af72b` |  |
| -41.326 kJ/mol-atom | Bi2Cs3 | 0 | DFT | LDA | [Bi–Cs](https://data.orchid-project.org/systems/BI-CS.html) | [1] Djaballah 2015 | Table 2, p. 4, row 10; `ORC-UAJWV3WDJB.03b6b3` |  |
| -34.483 kJ/mol-atom | Bi2Cs3 | 0 | DFT | GGA | [Bi–Cs](https://data.orchid-project.org/systems/BI-CS.html) | [1] Djaballah 2015 | Table 2, p. 4, row 9; `ORC-XBCBTMS4J3.12d05c` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of Bi2Cs3

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -40.7 | kJ/mol-atom |  | 0.05 | 4.6 (emf, cleaned_below_threshold) |  |  |  | 4.6 |
| -33.968 | kJ/mol-atom |  | 5.000e-4 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -41.326 | kJ/mol-atom |  | 5.000e-4 | 8.243 (dft, calibrated) |  |  |  | 8.243 |
| -34.483 | kJ/mol-atom |  | 5.000e-4 | 8.243 (dft, calibrated) |  |  |  | 8.243 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of Bi2Cs3

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaabgrwc | -31.375 | -0.325176 | C2/c | 0.6155 | 0.0064 | no |
| OQMD | oqmd-22902 | -34.17 | -0.354149 | C2/c | 2.6033 | 0.027 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015). [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002)

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
