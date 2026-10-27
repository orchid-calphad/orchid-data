# K system

> K system: 5 accepted literature values (crystal structure 4, formation 1) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/K.html · Markdown: https://data.orchid-project.org/systems/K.md

5 accepted literature values from 2 paper(s) (experimental 1, model 1, DFT 2, unspecified 1); 0 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/K.json) · [CSV](https://data.orchid-project.org/systems/K.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#K) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/K.html) · [Markdown](https://data.orchid-project.org/systems/K.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |
| DFT | 2 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 1 |
| crystal structure | 4 |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, K system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| K |  | 0 kJ/mol-atom | 298.15 | DFT |  |  | [1] Zhang 2006 | Table 2, p. 3, row 22; `ORC-ELWX2PIYGP.739f2a` |  |

## Other properties

### Crystal structure (4)

Table: Crystal structure, K system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 5.29 Å |  | (K); _alloy: K 1_ | unspecified | [2] Wang 2012 | Table 1, p. 3, row 12; `ORC-A532IXHNV3` |  |
| Lattice a | 5.32 Å | 298.15 | (K); _alloy: K 1_ | model | [2] Wang 2012; _cites King 1981_ [doi](https://doi.org/10.1007/bf02868307) | Table 1, p. 3, row 11; `ORC-CPVQKWDAQE` |  |
| Lattice a; _printed: Lattice constant a_ | 5.271 Å | 298.15 | K; _alloy: K 1_ | DFT | [1] Zhang 2006 | Table 2, p. 3, row 22; `ORC-2LHXAL4KTU` |  |
| Lattice a; _printed: Lattice constant a_ | 5.328 Å | 298.15 | K; _alloy: K 1_ | experimental | [1] Zhang 2006; _cites Liu 1986_ [doi](https://doi.org/10.1016/0022-3697%2886%2990073-9) | Table 2, p. 3, row 23; `ORC-XQNDRTQUW4` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006). [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037)
2. Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012). [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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
