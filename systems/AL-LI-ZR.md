# Al–Li–Zr system

> Al–Li–Zr system: 7 accepted literature values (crystal structure 5, formation 2) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-LI-ZR.html · Markdown: https://data.orchid-project.org/systems/AL-LI-ZR.md

7 accepted literature values from 1 paper(s) (model 3, DFT 1, unspecified 3); 0 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-LI-ZR.json) · [CSV](https://data.orchid-project.org/systems/AL-LI-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-LI-ZR) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-LI-ZR.html) · [Markdown](https://data.orchid-project.org/systems/AL-LI-ZR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 3 |
| DFT | 1 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 2 |
| crystal structure | 5 |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–Li–Zr system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| AlLi2Zr |  | -3.8946 kJ/mol (basis unstated) |  | model |  |  | [1] Long 2020 | Table 6, p. 15, row 1; `ORC-7CHFBJN2T2.f88881` |  |
| AlLi2Zr |  | -3.4662 kJ/mol (basis unstated) |  | DFT |  |  | [1] Long 2020 | Table 6, p. 15, row 1; `ORC-7CHFBJN2T2.3bb404` |  |

## Other properties

### Crystal structure (5)

Table: Crystal structure, Al–Li–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 6.633 Å |  | AlLi2Zr; _alloy: Li 0.5, Zr 0.25_ | model | [1] Long 2020; _cites Zatorska 2002_ [doi](https://doi.org/10.1016/s0925-8388%2801%2901700-5) | Table 6, p. 15, row 2; `ORC-35TXJ35NS6` |  |
| Lattice a; _printed: a_ | 6.598 Å |  | AlLi2Zr; _alloy: Li 0.5, Zr 0.25_ | model | [1] Long 2020 | Table 6, p. 15, row 1; `ORC-DYDG6BAIUF` |  |
| Lattice a | 8.1336 Å | 298.15 | Al3Lix+yZr5-x | unspecified | [1] Long 2020 | Table 1, p. 2, row 19; `ORC-7NTRVVT3Z6.4e3caa` |  |
| Lattice a | 6.633 Å | 298.15 | AlLi2Zr; _alloy: Li 0.5, Zr 0.25_ | unspecified | [1] Long 2020 | Table 1, p. 2, row 18; `ORC-7XFMYO7ZEE` |  |
| Lattice c | 5.7029 Å | 298.15 | Al3Lix+yZr5-x | unspecified | [1] Long 2020 | Table 1, p. 2, row 19; `ORC-7NTRVVT3Z6.544da4` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020). [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
