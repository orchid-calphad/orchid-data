# Ag–Mn system

> Ag–Mn system: 18 accepted literature values (crystal structure 12, invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-MN.html · Markdown: https://data.orchid-project.org/systems/AG-MN.md

18 accepted literature values from 1 paper(s) (model 6, unspecified 12); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-MN.json) · [CSV](https://data.orchid-project.org/systems/AG-MN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-MN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-MN/AgMn-90Kar.json) · [phases (6)](https://data.orchid-project.org/phases/pages/AG-MN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-MN.html) · [Markdown](https://data.orchid-project.org/systems/AG-MN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 6 |
| unspecified | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| crystal structure | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgMn-90Kar.tdb | I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 11, 480-86(1990). [doi:10.1007/BF02898263](https://doi.org/10.1007/BF02898263) | `0d7140384c10ff2293fb524cc17b5a5f54529203283c9e9c9729f038a64396ae` | [viewer](https://orchid-project.org/phase-diagrams/#AG-MN/AgMn-90Kar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgMn-90Kar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgMn-90Kar.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgMn-90Kar.tdb | 1480.56 | LIQUID (x(Mn) 0.52451) + LIQUID#2 (x(Mn) 0.94758) + BCC_A2 (x(Mn) 0.98905) |
| AgMn-90Kar.tdb | 1402.67 | LIQUID (x(Mn) 0.46195) + BCC_A2 (x(Mn) 0.9921) + FCC_A1 (x(Mn) 0.99242) |
| AgMn-90Kar.tdb | 1348.76 | LIQUID (x(Mn) 0.42672) + FCC_A1 (x(Mn) 0.99344) + CUB_A13 (x(Mn) 0.99562) |
| AgMn-90Kar.tdb | 1269.5 | LIQUID (x(Mn) 0.3808) + FCC_A1 (x(Mn) 0.43796) + CUB_A13 (x(Mn) 0.99628) |
| AgMn-90Kar.tdb | 976.4 | FCC_A1 (x(Mn) 0.30088) + CUB_A13 (x(Mn) 0.99897) + CBCC_A12 (x(Mn) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-MN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-MN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Mn system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1480.15 | monotectic: L2 -> L1 + (δMn) | L2: Mn 0.948; L1: Mn 0.524; (δMn): Mn 0.988 | model | [1] Karakaya 1990 | Table I, p. 3, row 6; `ORC-OXFQVXMHFJ` |  |
| 1401.15 | metatectic/catatectic: (δMn) -> L1 + (γMn) | (δMn): Mn 0.991; L1: Mn 0.463; (γMn): Mn 0.993 | model | [1] Karakaya 1990 | Table I, p. 3, row 5; `ORC-XIB3RSBWO6` |  |
| 1342.15 | metatectic/catatectic: (γMn) -> L1 + (βMn) | (γMn): Mn 0.994; L1: Mn 0.426; (βMn): Mn 0.996 | model | [1] Karakaya 1990 | Table I, p. 3, row 4; `ORC-GR4XMKVENV` |  |
| 1262.15 | peritectic: L1 -> (Ag) + (βMn) | L1: Mn 0.38; (Ag): Mn 0.436; (βMn): Mn 0.996 | model | [1] Karakaya 1990 | Table I, p. 3, row 3; `ORC-I6VQ2LDJS2` |  |
| 1235.08 | congruent melting: L -> Ag | L: Mn 0; Ag: Mn 0 | model | [1] Karakaya 1990 | Table I, p. 3, row 1; `ORC-XCAMRXOPF6` |  |
| 997.15 | eutectoid: (βMn) -> (Ag) + (αMn) | (βMn): Mn 0.999; (Ag): Mn 0.317; (αMn): Mn 1 | model | [1] Karakaya 1990 | Table I, p. 3, row 2; `ORC-LCZH7TXOAF` |  |

## Other properties

### Crystal structure (12)

Table: Crystal structure, Ag–Mn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.08606 Å | 848.15 | (Ag); _(Ag): Ag 0.9792, Mn 0.0208_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 4; `ORC-EDKIMJE3BJ.87a45c` |  |
| Lattice a | 4.08602 Å | 848.15 | (Ag); _(Ag): Ag 0.9541, Mn 0.0459_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 5; `ORC-M3FWOPTKJL.104894` |  |
| Lattice a | 4.08606 Å | 848.15 | (Ag); _(Ag): Ag 0.9511, Mn 0.0489_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 6; `ORC-UMQCX4AYSU.d97ff3` |  |
| Lattice a | 4.078 Å | 1173.15 | (Ag); _(Ag): Ag 0.925, Mn 0.075_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 7; `ORC-KANLZLMGBF.301610` |  |
| Lattice a | 4.08605 Å | 1173.15 | (Ag); _(Ag): Ag 0.9819, Mn 0.0181_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 3; `ORC-LIXYLGEXQC.57717c` |  |
| Lattice a | 4.073 Å | 1173.15 | (Ag); _(Ag): Ag 0.85, Mn 0.15_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 8; `ORC-Y4LFZRT4I7.82f0c6` |  |
| lattice unspecified axis | 4.08606 Å | 848.15 | (Ag); _(Ag): Ag 0.9792, Mn 0.0208_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 4; `ORC-EDKIMJE3BJ.b71619` |  |
| lattice unspecified axis | 4.08602 Å | 848.15 | (Ag); _(Ag): Ag 0.9541, Mn 0.0459_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 5; `ORC-M3FWOPTKJL.b3eb0e` |  |
| lattice unspecified axis | 4.08606 Å | 848.15 | (Ag); _(Ag): Ag 0.9511, Mn 0.0489_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 6; `ORC-UMQCX4AYSU.717d86` |  |
| lattice unspecified axis | 4.078 Å | 1173.15 | (Ag); _(Ag): Ag 0.925, Mn 0.075_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 7; `ORC-KANLZLMGBF.c82917` |  |
| lattice unspecified axis | 4.08605 Å | 1173.15 | (Ag); _(Ag): Ag 0.9819, Mn 0.0181_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 3; `ORC-LIXYLGEXQC.296d45` |  |
| lattice unspecified axis | 4.073 Å | 1173.15 | (Ag); _(Ag): Ag 0.85, Mn 0.15_ | unspecified | [1] Karakaya 1990 | Table 3, p. 5, row 8; `ORC-Y4LFZRT4I7.879ccb` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Karakaya, W. T. Thompson, The Ag-Mn (Silver-Manganese) system, Bulletin of Alloy Phase Diagrams 11, 480-486 (1990). [doi:10.1007/bf02898263](https://doi.org/10.1007/bf02898263)

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
