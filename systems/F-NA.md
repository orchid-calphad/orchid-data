# F–Na system

> F–Na system: 10 accepted literature values (invariant reaction 5, crystal structure 2, formation 2, phase transition 1) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/F-NA.html · Markdown: https://data.orchid-project.org/systems/F-NA.md

10 accepted literature values from 1 paper(s) (experimental 4, model 4, DFT 2); 0 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/F-NA.json) · [CSV](https://data.orchid-project.org/systems/F-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#F-NA) · [phases (7)](https://data.orchid-project.org/phases/pages/F-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/F-NA.html) · [Markdown](https://data.orchid-project.org/systems/F-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 4 |
| DFT | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 1 |
| formation | 2 |
| crystal structure | 2 |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/F/F-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/F/F-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the F–Na system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2556 | Gas (P = 10 bar) = liquid | Gas: F 0.5; liquid: F 0.5 | model | [1] Zhang 2006 | Table 4, p. 9, row 1; `ORC-RGFXLU6XDJ` |  |
| 1269 | Gas (P = 10 bar) = liquid + NaF | Gas: F 0.999967; liquid: F 0.5; NaF: F 0.5 | model | [1] Zhang 2006 | Table 4, p. 9, row 2; `ORC-Z3EPAZMNA4` |  |
| 1263 | monotectic: Liquid 1 = liquid 2 + NaF | Liquid 1: F 0.495; liquid 2: F 0.145; NaF: F 0.497 | experimental | [1] Zhang 2006; _cites Bredig 1955_ [doi](https://doi.org/10.1021/ja01607a016) | Table 4, p. 9, row 4; `ORC-HQ46UVIJFA` |  |
| 1254 | monotectic: Liquid 1 = liquid 2 + NaF | Liquid 1: F 0.488; liquid 2: F 0.142; NaF: F 0.5 | model | [1] Zhang 2006 | Table 4, p. 9, row 3; `ORC-KRGWFS3XQU` |  |
| 371 | eutectic: Liquid = bcc + NaF | Liquid: F 0; bcc: F 0; NaF: F 0.5 | model | [1] Zhang 2006 | Table 4, p. 9, row 5; `ORC-O4AU7OZKTJ` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, F–Na system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| NaF | [NaF](https://data.orchid-project.org/compounds/NaF.html) | -287.69 kJ/mol-atom | 298.15 | experimental | -283.373 (mp-aaaaabag) | -286.946 (oqmd-5686) | [1] Zhang 2006; _cites Chase 1998_ | Table 2, p. 3, row 29; `ORC-WVH7P6YN7T.8d45dd` |  |
| NaF |  | -269.597 kJ/mol-atom | 0 | DFT |  |  | [1] Zhang 2006 | Table 2, p. 3, row 28; `ORC-B4XZ4YWAI5.2088f8` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, F–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1373 K | 1373 | other | experimental | [1] Zhang 2006 | p. 2; `ORC-IZ7G5HZB23` | “The composition of the consolute point in the liquid was estimated to be 23.1 at.% F at 1373 K by extrapolation.” |

### Crystal structure (2)

Table: Crystal structure, F–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: Lattice constant a_ | 4.5 Å | 0 | NaF; _alloy: Na 0.5_ | DFT | [1] Zhang 2006 | Table 2, p. 3, row 28; `ORC-3IUSPOMF62` |  |
| Lattice a; _printed: Lattice constant a_ | 4.62 Å ± 0.004 |  | NaF; _alloy: Na 0.5_ | experimental | [1] Zhang 2006; _cites Davey 1923_ [doi](https://doi.org/10.1103/physrev.21.143) | Table 2, p. 3, row 11; `ORC-ZYLR5O2YMQ` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006). [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037)

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
