# ReSi2: enthalpy of formation

> Enthalpy of formation of ReSi2: 5 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/ReSi2.html · Markdown: https://data.orchid-project.org/compounds/ReSi2.md

5 accepted literature formation-enthalpy value(s) (experimental 1, model 4); experimental median -28.8 kJ/mol-atom (n = 1); Materials Project -14.277 kJ/mol-atom (mp-aaaaasqv); OQMD -17.558 kJ/mol-atom (oqmd-6973).

Systems: [Re–Si](https://data.orchid-project.org/systems/RE-SI.html)

## Literature values

Table: Enthalpy of formation of ReSi2 reported in the literature (5)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -28.8 kJ/mol-atom | ReSi2 | 298.15 | experimental | Elemental effusion | [Re–Si](https://data.orchid-project.org/systems/RE-SI.html) | [1] Yang 2010; _cites Searcy 1962_ | Table 2, p. 3, row 12; `ORC-5SVXSDJRSO` |  |
| -33.445 kJ/mol-atom | ReSi2 |  | model | This work | [Re–Si](https://data.orchid-project.org/systems/RE-SI.html) | [1] Yang 2010 | Table 2, p. 3, row 16; `ORC-DNWART47JX` |  |
| -31.2 kJ/mol-atom | ReSi2 |  | model | Assessment | [Re–Si](https://data.orchid-project.org/systems/RE-SI.html) | [1] Yang 2010; _cites Shao 2001_ [doi](https://doi.org/10.1016/s0966-9795%2801%2900110-8) | Table 2, p. 3, row 15; `ORC-Y3BK47ZJYE` |  |
| -30.1 kJ/mol-atom | ReSi2 |  | model | Estimation | [Re–Si](https://data.orchid-project.org/systems/RE-SI.html) | [1] Yang 2010; _cites Chart 1973_ | Table 2, p. 3, row 13; `ORC-GYLPB3ZT5U` |  |
| -10 kJ/mol-atom | ReSi2 |  | model | Assessment | [Re–Si](https://data.orchid-project.org/systems/RE-SI.html) | [1] Yang 2010; _cites Boer 1989_ | Table 2, p. 3, row 14; `ORC-D26X5KQGPV` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of ReSi2

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -28.8 | kJ/mol-atom |  | 0.05 | 4.2 (kems_vapour, calibrated) |  |  |  | 4.2 |
| -33.445 | kJ/mol-atom |  | 5.000e-4 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -31.2 | kJ/mol-atom |  | 0.05 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -30.1 | kJ/mol-atom |  | 0.05 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -10 | kJ/mol-atom |  | 0.5 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of ReSi2

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaaasqv | -14.277 | -0.147972 | I4/mmm | 19.1322 | 0.1983 | no |
| OQMD | oqmd-6973 | -17.558 | -0.181979 | Immm | 18.5538 | 0.1923 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010). [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003)

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
