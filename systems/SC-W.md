# Sc–W system

> Sc–W system: 2 accepted literature values (mixing / partial 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SC-W.html · Markdown: https://data.orchid-project.org/systems/SC-W.md

2 accepted literature values from 1 paper(s) (model 2); 2 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SC-W.json) · [CSV](https://data.orchid-project.org/systems/SC-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SC-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SC-W/ScW-00Kri.json) · [phases (4)](https://data.orchid-project.org/phases/pages/SC-W.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SC-W.html) · [Markdown](https://data.orchid-project.org/systems/SC-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| mixing / partial | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ScW-00Kri.tdb | N. Krishnamurthy, T. Kundu, A. Awasthi, S.P. Garg, Z. Metallkd., 91, 234-40(2000). [doi:10.1515/ijmr-2000-910311](https://doi.org/10.1515/ijmr-2000-910311) | `e3aea447947d7bfa9b72af12ba3173936cc7388f2bfd213b402737aab321909a` | [viewer](https://orchid-project.org/phase-diagrams/#SC-W/ScW-00Kri.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScW-00Kri.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScW-00Kri.json) |
| ScW-15Wan.tdb | S.L. Wang, L.J. Zhou, Y. Ye, X.H. Wang, Y.H. Lin, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 36, 3-9(2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) | `478e3612800b19c0d86215b3b3d12b643ca402ec3d3f86de0526805f610bb21a` | [viewer](https://orchid-project.org/phase-diagrams/#SC-W/ScW-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScW-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScW-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ScW-00Kri.tdb | 1790.65 | BCC_A2 (x(W) 0.00123) + LIQUID (x(W) 0.01379) + BCC_A2#2 (x(W) 0.99877) |
| ScW-00Kri.tdb | 1605.98 | HCP_A3 (x(W) 1.900e-4) + BCC_A2#2 (x(W) 5.600e-4) + BCC_A2 (x(W) 0.99944) |
| ScW-15Wan.tdb | 1783.59 | BCC_A2 (x(W) 8.000e-5) + LIQUID (x(W) 0.01652) + BCC_A2#2 (x(W) 0.99992) |
| ScW-15Wan.tdb | 1783.59 | BCC_A2#2 (x(W) 8.000e-5) + LIQUID (x(W) 0.01652) + BCC_A2 (x(W) 0.99992) |
| ScW-15Wan.tdb | 1612.81 | BCC_A2 (x(W) 3.000e-5) + HCP_A3 (x(W) 9.300e-4) + BCC_A2#2 (x(W) 0.99997) |
| ScW-15Wan.tdb | 1612.81 | BCC_A2#2 (x(W) 3.000e-5) + HCP_A3 (x(W) 9.300e-4) + BCC_A2 (x(W) 0.99997) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SC/SC-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SC/SC-W.json) · [CALPHAD hull ScW-00Kri](https://data.orchid-project.org/hulls/calphad-sgte/SC/SC-W--ScW-00Kri.json)

## Other properties

### Mixing / partial (2)

Table: Mixing / partial, Sc–W system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 8.75 kJ/mol (basis unstated) | 3773.15 | liquid; _alloy: Sc 0.5, W 0.5_ | model | [1] Wang 2015 | Table 3, p. 3, row 8; `ORC-2NKS3HIJYT` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 9 kJ/mol (basis unstated) | 3773.15 | liquid; _alloy: Sc 0.5, W 0.5_ | model | [1] Wang 2015; _cites F 1988_ | Table 3, p. 3, row 7; `ORC-PH6OBPTHYD` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
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

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
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
