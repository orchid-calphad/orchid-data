# Ni2Si: enthalpy of formation

> Enthalpy of formation of Ni2Si: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/Ni2Si.html · Markdown: https://data.orchid-project.org/compounds/Ni2Si.md

4 accepted literature formation-enthalpy value(s) (experimental 2, model 2); experimental median -48.75 kJ/mol-atom (n = 2); Materials Project -53.015 kJ/mol-atom (mp-aaaaabra); OQMD -53.941 kJ/mol-atom (oqmd-4675).

Systems: [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html)

## Literature values

Table: Enthalpy of formation of Ni2Si reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -50.6 kJ/mol-atom | Ni2Si(δ) | 298.15 | experimental |  | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [1] Tokunaga 2003; _cites Meschel 1998_ [doi](https://doi.org/10.1016/s0925-8388%2897%2900528-8) | Table 4, p. 7, row 3; `ORC-ATSWCPLHI3.ae4c69` |  |
| -46.9 kJ/mol-atom | Ni2Si(δ) | 298.15 | experimental |  | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [1] Tokunaga 2003; _cites Oelson 1936_ | Table 4, p. 7, row 1; `ORC-DYBIVMPQDE.730676` |  |
| -47.6 kJ/mol-atom | Ni2Si(δ) |  | model | CALPHAD assessment | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [1] Tokunaga 2003 | Table 4, p. 7, row 5; `ORC-ZNDNRTOJKZ.ebb93b` |  |
| -41.7 kJ/mol-atom | Ni2Si(δ) |  | model |  | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [1] Tokunaga 2003; _cites Lindholm 1996_ [doi](https://doi.org/10.1007/bf02663838) | Table 4, p. 7, row 6; `ORC-CRPUQ55THO.c6799f` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of Ni2Si

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -50.6 | kJ/mol-atom |  | 0.05 | 3.5 (unknown, calibrated) |  |  |  | 3.5 |
| -46.9 | kJ/mol-atom |  | 0.05 | 3.5 (unknown, calibrated) |  |  |  | 3.5 |
| -47.6 | kJ/mol-atom |  | 0.05 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |
| -41.7 | kJ/mol-atom |  | 0.05 | 3.4 (model_calculated, calibrated) |  |  |  | 3.4 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of Ni2Si

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaaabra | -53.015 | -0.549459 | Pnma | 0 | 0 | no |
| OQMD | oqmd-4675 | -53.941 | -0.559065 | Pnma | 0 | 0 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic assessment of the Ni–Si system by incorporating ab initio energetic calculations into the CALPHAD approach, Calphad 27, 161-168 (2003). [doi:10.1016/s0364-5916(03)00049-x](https://doi.org/10.1016/s0364-5916%2803%2900049-x)

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
