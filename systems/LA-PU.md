# La–Pu system

> La–Pu system: 23 accepted literature values (invariant reaction 23) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-PU.html · Markdown: https://data.orchid-project.org/systems/LA-PU.md

23 accepted literature values from 1 paper(s) (experimental 15, model 8); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/LA-PU.json) · [CSV](https://data.orchid-project.org/systems/LA-PU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LA-PU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-PU/LaPu-14Liu.json) · [phases (9)](https://data.orchid-project.org/phases/pages/LA-PU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LA-PU.html) · [Markdown](https://data.orchid-project.org/systems/LA-PU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 15 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 23 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LaPu-14Liu.tdb | X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia, C.P. Wang, J. Nucl. Mater., 453, 169-75(2014). [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) | `b876dfcc548ef4193b191505108fb9e294a09ae6367251ff5d277ea87baf5279` | [viewer](https://orchid-project.org/phase-diagrams/#LA-PU/LaPu-14Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaPu-14Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LaPu-14Liu.tdb | 1123.18 | BCC_A2 (x(Pu) 0.20428) + LIQUID#2 (x(Pu) 0.22925) + LIQUID (x(Pu) 0.95607) |
| LaPu-14Liu.tdb | 1108.2 | FCC_A1 (x(Pu) 0.19352) + BCC_A2 (x(Pu) 0.19695) + LIQUID (x(Pu) 0.95973) |
| LaPu-14Liu.tdb | 912.12 | FCC_A1 (x(Pu) 0.13352) + LIQUID (x(Pu) 0.98958) + BCC_A2 (x(Pu) 0.98983) |
| LaPu-14Liu.tdb | 753.89 | FCC_A1 (x(Pu) 0.07829) + BCC_A2 (x(Pu) 0.99741) + TETRAGONAL_A6 (x(Pu) 0.99815) |
| LaPu-14Liu.tdb | 736.13 | FCC_A1#2 (x(Pu) 0.07249) + FCC_A1 (x(Pu) 0.99851) + TETRAGONAL_A6 (x(Pu) 0.99852) |
| LaPu-14Liu.tdb | 592.04 | FCC_A1#2 (x(Pu) 0.03512) + FCC_A1 (x(Pu) 0.99975) + GAMMA_PU (x(Pu) 1) |
| LaPu-14Liu.tdb | 487.9 | FCC_A1 (x(Pu) 0.01688) + BETA_PU (x(Pu) 1) + GAMMA_PU (x(Pu) 1) |
| LaPu-14Liu.tdb | 472.48 | DHCP (x(Pu) 0) + FCC_A1 (x(Pu) 0.01477) + BETA_PU (x(Pu) 1) |
| LaPu-14Liu.tdb | 397.62 | DHCP (x(Pu) 0) + ALPHA_PU (x(Pu) 1) + BETA_PU (x(Pu) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LA/LA-PU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LA/LA-PU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the La–Pu system (23)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1123.15 | monotectic: L1 -> (γLa) + L2 | L1: Pu 0.229; (γLa): Pu 0.204; L2: Pu 0.956 | model | [1] Liu 2014 | Table 5, p. 6, row 4; `ORC-GEPY52ECGM` |  |
| 1123.15 | monotectic: L1 -> (γLa) + L2 | L1: Pu 0.23; (γLa): Pu 0.2 | experimental | [1] Liu 2014; _cites Ellinger 1967_ | Table 5, p. 6, row 2; `ORC-H7XBHXX2GZ` |  |
| 1123.15 | monotectic: L1 -> (γLa) + L2 | L1: Pu 0.23; (γLa): Pu 0.2; L2: Pu 0.957 | experimental | [1] Liu 2014; _cites Okamoto 2000_ | Table 5, p. 6, row 3; `ORC-MYXCBHJR27` |  |
| 1119.15 | monotectic: L1 -> (γLa) + L2 | L1: Pu 0.23; (γLa): Pu 0.2 | experimental | [1] Liu 2014; _cites Poole 1960_ | Table 5, p. 6, row 1; `ORC-BJQJ6J7T3R` |  |
| 1108.15 | metatectic/catatectic: (γLa) -> L2 + (βLa) | (γLa): Pu 0.197; L2: Pu 0.96; (βLa): Pu 0.193 | model | [1] Liu 2014 | Table 5, p. 6, row 8; `ORC-CNFH22OACM` |  |
| 1108.15 | metatectic/catatectic: (γLa) -> L2 + (βLa) | (γLa): Pu 0.2; L2: Pu 0.96; (βLa): Pu 0.191 | experimental | [1] Liu 2014; _cites Okamoto 2000_ | Table 5, p. 6, row 7; `ORC-CZXIFC2V6L` |  |
| 1108.15 | metatectic/catatectic: (γLa) -> L2 + (βLa) | (γLa): Pu 0.2; (βLa): Pu 0.19 | experimental | [1] Liu 2014; _cites Ellinger 1967_ | Table 5, p. 6, row 6; `ORC-EX4VMP5OC6` |  |
| 1106.15 | metatectic/catatectic: (γLa) -> L2 + (βLa) | (γLa): Pu 0.18; (βLa): Pu 0.16 | experimental | [1] Liu 2014; _cites Poole 1960_ | Table 5, p. 6, row 5; `ORC-SWSB5IGWGD` |  |
| 913.15 | eutectic: L2 -> (βLa) + (εPu) | L2: Pu 0.985; (βLa): Pu 0.128; (εPu): Pu 0.988 | experimental | [1] Liu 2014; _cites Okamoto 2000_ | Table 5, p. 6, row 10; `ORC-5VY6DNJNBE` |  |
| 912.15 | eutectic: L2 -> (βLa) + (εPu) | L2: Pu 0.989; (βLa): Pu 0.134; (εPu): Pu 0.99 | model | [1] Liu 2014 | Table 5, p. 6, row 11; `ORC-6N6TPEP4NH` |  |
| 905.15 | eutectic: L2 -> (βLa) + (εPu) |  | experimental | [1] Liu 2014; _cites Ellinger 1967_ | Table 5, p. 6, row 9; `ORC-35LJ2WCXDV` |  |
| 756.15 | eutectoid: (εPu) -> (βLa) + (δ'Pu) | (εPu): Pu 0.997; (βLa): Pu 0.071; (δ'Pu): Pu 0.998 | experimental | [1] Liu 2014; _cites Okamoto 2000_ | Table 5, p. 6, row 13; `ORC-6SAU74MBA7` |  |
| 754.15 | eutectoid: (εPu) -> (βLa) + (δ'Pu) | (εPu): Pu 0.997; (βLa): Pu 0.078; (δ'Pu): Pu 0.998 | model | [1] Liu 2014 | Table 5, p. 6, row 14; `ORC-YNUEPDOHGN` |  |
| 748.15 | eutectoid: (εPu) -> (βLa) + (δ'Pu) |  | experimental | [1] Liu 2014; _cites Ellinger 1967_ | Table 5, p. 6, row 12; `ORC-DWV4CG5Q2U` |  |
| 736.15 | peritectoid: (βLa) + (δ'Pu) -> (δPu) | (βLa): Pu 0.068; (δ'Pu): Pu 0.998 | experimental | [1] Liu 2014; _cites Okamoto 2000_ | Table 5, p. 6, row 22; `ORC-CKBUUPRJP2` |  |
| 736.15 | peritectoid: (βLa) + (δ'Pu) -> (δPu) | (βLa): Pu 0.072; (δ'Pu): Pu 0.998 | model | [1] Liu 2014 | Table 5, p. 6, row 23; `ORC-QVE67COCR5` |  |
| 723.15 | peritectoid: (βLa) + (δ'Pu) -> (δPu) |  | experimental | [1] Liu 2014; _cites Ellinger 1967_ | Table 5, p. 6, row 21; `ORC-F7XKFJ32SC` |  |
| 603.15 | eutectoid: (δPu) -> (βLa) + (γPu) |  | experimental | [1] Liu 2014; _cites Ellinger 1967_ | Table 5, p. 6, row 15; `ORC-LKQKPAUUZX` |  |
| 593.15 | eutectoid: (δPu) -> (βLa) + (γPu) | (δPu): Pu 1; (βLa): Pu 0.036; (γPu): Pu 1 | experimental | [1] Liu 2014; _cites Okamoto 2000_ | Table 5, p. 6, row 16; `ORC-IR7BGPI4I4` |  |
| 592.15 | eutectoid: (δPu) -> (βLa) + (γPu) | (δPu): Pu 1; (βLa): Pu 0.035; (γPu): Pu 1 | model | [1] Liu 2014 | Table 5, p. 6, row 17; `ORC-TFDUQA3EHL` |  |
| 488.15 | eutectoid: (γPu) -> (βLa) + (βPu) | (γPu): Pu 1; (βLa): Pu 0.023; (βPu): Pu 1 | experimental | [1] Liu 2014; _cites Okamoto 2000_ | Table 5, p. 6, row 18; `ORC-CCFYSC5K6H` |  |
| 488.15 | eutectoid: (γPu) -> (βLa) + (βPu) | (γPu): Pu 1; (βLa): Pu 0.017; (βPu): Pu 1 | model | [1] Liu 2014 | Table 5, p. 6, row 19; `ORC-YMWOBT24ML` |  |
| 472.15 | eutectoid: (βLa) -> (αLa) + (βPu) | (βLa): Pu 0.015; (αLa): Pu 0; (βPu): Pu 1 | model | [1] Liu 2014 | Table 5, p. 6, row 20; `ORC-IEPT3ELK3C` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014). [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
