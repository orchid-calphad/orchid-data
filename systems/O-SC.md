# O–Sc system

> O–Sc system: 7 accepted literature values (crystal structure 3, phase transition 2, formation 1, heat capacity / entropy / enthalpy 1) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/O-SC.html · Markdown: https://data.orchid-project.org/systems/O-SC.md

7 accepted literature values from 1 paper(s) (experimental 1, model 5, unspecified 1); 0 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/O-SC.json) · [CSV](https://data.orchid-project.org/systems/O-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#O-SC) · [phases (6)](https://data.orchid-project.org/phases/pages/O-SC.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/O-SC.html) · [Markdown](https://data.orchid-project.org/systems/O-SC.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 5 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 2 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 1 |
| crystal structure | 3 |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/O/O-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/O/O-SC.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, O–Sc system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| C-Sc2O3 | [Sc2O3](https://data.orchid-project.org/compounds/Sc2O3.html) | -381.715 kJ/mol-atom | 298.15 | model | -382.923 (mp-aaaaaaii) | -367.356 (oqmd-4555) | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 1; `ORC-4ZKH5RH67R.0afd30` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, O–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 298.15 K | 298.15 | polymorphic: C ⇒ A; _alloy: O 0.6, Sc 0.4_ | unspecified | [1] ZINKEVICH 2007; _cites Atou 1994_ | Table 2.3, p. 10, row 2; `ORC-5UWAGDJNTI` |  |
| Phase transition | 1273 K | 1273 | polymorphic: C ⇒ B; _alloy: O 0.6, Sc 0.4_ | experimental | [1] ZINKEVICH 2007; _cites Reid 1969_ | Table 2.3, p. 10, row 1; `ORC-O32YOI4ZS5` |  |

### Heat capacity / entropy / enthalpy (1)

Table: Heat capacity / entropy / enthalpy, O–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: °S_ | 77 unknown | 298.15 | C-Sc2O3; _alloy: O 0.6, Sc 0.4_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 1; `ORC-4ZKH5RH67R.6864ad` |  |

### Crystal structure (3)

Table: Crystal structure, O–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 31.781 cm3 mol-1 | 298.15 | Sc2O3 (A-type); _alloy: O 0.6, Sc 0.4_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 1; `ORC-DI2XNZRC2C.8fc252` |  |
| lattice molar volume | 33.129 cm3 mol-1 | 298.15 | Sc2O3 (B-type); _alloy: O 0.6, Sc 0.4_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 1; `ORC-DI2XNZRC2C.48d7ec` |  |
| lattice molar volume | 35.911 cm3 mol-1 | 298.15 | Sc2O3 (C-type); _alloy: O 0.6, Sc 0.4_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 1; `ORC-DI2XNZRC2C.33681f` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
