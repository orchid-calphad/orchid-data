# Cr–U system

> Cr–U system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-U.html · Markdown: https://data.orchid-project.org/systems/CR-U.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-U.json) · [CSV](https://data.orchid-project.org/systems/CR-U.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-U) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-U/CrU-11Ber.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CR-U.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-U.html) · [Markdown](https://data.orchid-project.org/systems/CR-U.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrU-11Ber.tdb | A. Berche, N. Dupin, C. Gueneau, C. Rado, B. Sundman, J.C. Dumas, J. Nucl. Mater., 411, 131-43(2011). [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) | `0603e4a72229dc3b6650a80b725fabe4e6a121fb2f21b45beaeb2659e3be4b44` | [viewer](https://orchid-project.org/phase-diagrams/#CR-U/CrU-11Ber.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrU-11Ber.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrU-11Ber.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrU-11Ber.tdb | 1133.4 | BCC_A2 (x(U) 2.000e-5) + LIQUID (x(U) 0.81199) + BCC_A2#2 (x(U) 0.95764) |
| CrU-11Ber.tdb | 1133.4 | BCC_A2#2 (x(U) 2.000e-5) + LIQUID (x(U) 0.81198) + BCC_A2 (x(U) 0.95764) |
| CrU-11Ber.tdb | 1012.5 | BCC_A2 (x(U) 1.000e-5) + BCC_A2#2 (x(U) 0.96797) + TETRAGONAL_U (x(U) 0.98379) |
| CrU-11Ber.tdb | 912.09 | BCC_A2 (x(U) 0) + TETRAGONAL_U (x(U) 0.98894) + ORTHORHOMBIC_A20 (x(U) 1) |
| CrU-11Ber.tdb | 912.09 | BCC_A2 (x(U) 0) + TETRAGONAL_U (x(U) 0.98893) + ORTHORHOMBIC_A20 (x(U) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-U.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-U.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–U system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1133 | Liquid -> (Cr) + (γ-U) |  | model | [1] Berche 2011 | Table 4, p. 8, row 1; `ORC-3OY3SY64DB` |  |
| 1133 | Liquid -> (Cr) + (γ-U) |  | experimental | [1] Berche 2011; _cites Venkatraman 1980_ | Table 4, p. 8, row 2; `ORC-ZBQJHCHKY3` |  |
| 912 | (β-U) -> (Cr) + (α-U) |  | model | [1] Berche 2011 | Table 4, p. 8, row 5; `ORC-CM24P3E2ZP` |  |
| 903 | (β-U) -> (Cr) + (α-U) |  | experimental | [1] Berche 2011; _cites Venkatraman 1980_ | Table 4, p. 8, row 6; `ORC-OZJS4YC2HM` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011). [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043)

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
