# O–Pr system

> O–Pr system: 1 accepted literature values (formation 1) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/O-PR.html · Markdown: https://data.orchid-project.org/systems/O-PR.md

1 accepted literature values from 1 paper(s) (model 1); 0 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/O-PR.json) · [CSV](https://data.orchid-project.org/systems/O-PR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#O-PR) · [phases (15)](https://data.orchid-project.org/phases/pages/O-PR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/O-PR.html) · [Markdown](https://data.orchid-project.org/systems/O-PR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 1 |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/O/O-PR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/O/O-PR.json) · [CALPHAD hull PrO-16McM](https://data.orchid-project.org/hulls/calphad-sgte/O/O-PR--PrO-16McM.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, O–Pr system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| A-Pr2O3 | [Pr2O3](https://data.orchid-project.org/compounds/Pr2O3.html) | -361.98 kJ/mol-atom | 298.15 | model | -360.381 (mp-aaaaaysn) | -345.037 (oqmd-16545) | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 25 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

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

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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
