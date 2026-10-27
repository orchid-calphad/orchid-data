# F–K system

> F–K system: 10 accepted literature values (invariant reaction 6, crystal structure 2, formation 2) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/F-K.html · Markdown: https://data.orchid-project.org/systems/F-K.md

10 accepted literature values from 1 paper(s) (experimental 4, model 4, DFT 2); 0 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/F-K.json) · [CSV](https://data.orchid-project.org/systems/F-K.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#F-K) · [phases (7)](https://data.orchid-project.org/phases/pages/F-K.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/F-K.html) · [Markdown](https://data.orchid-project.org/systems/F-K.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 4 |
| DFT | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| formation | 2 |
| crystal structure | 2 |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/F/F-K.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/F/F-K.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the F–K system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1964 | Gas (P = 3 bar) = liquid | Gas (P = 3 bar): F 0.489; liquid: F 0.489 | model | [1] Zhang 2006 | Table 5, p. 9, row 1; `ORC-QFATTPAJGS` |  |
| 1131 | Gas (P = 3 bar) = liquid + KF | Gas (P = 3 bar): F 0.9998; liquid: F 0.5; KF: F 0.5 | model | [1] Zhang 2006 | Table 5, p. 9, row 2; `ORC-OFVWQG7PPB` |  |
| 1122 | Liquid 1 = liquid 2 + KF | Liquid 1: F 0.489; liquid 2: F 0.315; KF: F 0.5; L1: F 0.489; L2: F 0.315 | experimental | [1] Zhang 2006; _cites Johnson 1958_ | Table 5, p. 9, row 5; `ORC-V7PNEYH26N` |  |
| 1122 | Liquid 1 = liquid 2 + KF | KF: F 0.5, K 0.5 | experimental | [1] Zhang 2006; _cites Bredig 1955_ [doi](https://doi.org/10.1021/ja01607a016) | Table 5, p. 9, row 4; `ORC-WRTDGSWCPD` |  |
| 1120 | Liquid 1 = liquid 2 + KF | Liquid 1: F 0.49; liquid 2: F 0.322; KF: F 0.5; L1: F 0.49; L2: F 0.322 | model | [1] Zhang 2006 | Table 5, p. 9, row 3; `ORC-EGBSTUQSCC` |  |
| 337 | Liquid = bcc + KF | Liquid: F 2.500e-5; bcc: F 2.500e-5; KF: F 0.5 | model | [1] Zhang 2006 | Table 5, p. 9, row 6; `ORC-54ENQABX2V` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, F–K system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| KF | [KF](https://data.orchid-project.org/compounds/KF.html) | -284.305 kJ/mol-atom | 298.15 | experimental | -283.123 (mp-aaaaaarv) | -281.083 (oqmd-1442813) | [1] Zhang 2006; _cites Chase 1998_ | Table 2, p. 3, row 27; `ORC-XB6YM2SOGE.710880` |  |
| KF |  | -264.865 kJ/mol-atom | 0 | DFT |  |  | [1] Zhang 2006 | Table 2, p. 3, row 26; `ORC-QY2GREQUEJ.892b97` |  |

## Other properties

### Crystal structure (2)

Table: Crystal structure, F–K system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: Lattice constant a_ | 5.333 Å |  | KF; _alloy: K 0.5_ | experimental | [1] Zhang 2006; _cites Broch 1929_ [doi](https://doi.org/10.1515/zpch-1929-0314) | Table 2, p. 3, row 8; `ORC-56OEO6T4EJ` |  |
| Lattice a; _printed: Lattice constant a_ | 5.178 Å | 0 | KF; _alloy: K 0.5_ | DFT | [1] Zhang 2006 | Table 2, p. 3, row 26; `ORC-ZKA2TVPO7R` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006). [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

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

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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
