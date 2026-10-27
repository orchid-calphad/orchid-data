# Er–Zr system

> Er–Zr system: 37 accepted literature values (phase equilibrium 20, phase transition 13, invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-ZR.html · Markdown: https://data.orchid-project.org/systems/ER-ZR.md

37 accepted literature values from 1 paper(s) (experimental 35, unspecified 2); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-ZR.json) · [CSV](https://data.orchid-project.org/systems/ER-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-ZR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-ZR/ErZr-10Jou.json) · [phases (4)](https://data.orchid-project.org/phases/pages/ER-ZR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ER-ZR.html) · [Markdown](https://data.orchid-project.org/systems/ER-ZR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 35 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 13 |
| phase equilibrium | 20 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErZr-10Jou.tdb | J. Jourdan, C. Toffolon-Masclet, J.-M. Joubert, J. Nucl. Mater., 402, 102-7(2010). [doi:10.1016/j.jnucmat.2010.05.002](https://doi.org/10.1016/j.jnucmat.2010.05.002) | `9a683aa7ae003e8f80e36b9afe9946818cc13ab6e74791de33075651652a3460` | [viewer](https://orchid-project.org/phase-diagrams/#ER-ZR/ErZr-10Jou.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErZr-10Jou.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErZr-10Jou.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErZr-10Jou.tdb | 1669.86 | HCP_A3 (x(Zr) 0.31296) + LIQUID (x(Zr) 0.41574) + BCC_A2 (x(Zr) 0.45929) |
| ErZr-10Jou.tdb | 1296.15 | HCP_A3 (x(Zr) 0.21995) + HCP_A3#2 (x(Zr) 0.6821) + BCC_A2 (x(Zr) 0.7793) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-ZR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-ZR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–Zr system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1670.15 | eutectic: Liquid -> (Er) + (βZr) |  | unspecified | [1] Jourdan 2010 | Table 4, p. 5, row 2; `ORC-WFEQQPX456` |  |
| 1653.15 | eutectic: Liquid -> (Er) + (βZr) |  | experimental | [1] Jourdan 2010 | Table 4, p. 5, row 1; `ORC-H4M7N2VM7O` |  |
| 1318.15 | (Er) + (βZr) -> (αZr) |  | experimental | [1] Jourdan 2010 | Table 4, p. 5, row 3; `ORC-W3PT2TXM6X` |  |
| 1304.15 | (Er) + (βZr) -> (αZr) |  | unspecified | [1] Jourdan 2010 | Table 4, p. 5, row 4; `ORC-O4PWSETWMW` |  |

## Other properties

### Phase transition (13)

Table: Phase transition, Er–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1223.15 K | 1223.15 | other: Er20Zr80; _alloy: Er 0.2, Zr 0.8_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 5; `ORC-QE4UZPP3ET` |  |
| Phase transition | 1283.15 K | 1283.15 | other: Er25Zr75; _alloy: Er 0.25, Zr 0.75_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 7; `ORC-FR3WZJOGTU` |  |
| Phase transition | 1318.15 K | 1318.15 | peritectoid: Er25Zr75; _alloy: Er 0.25, Zr 0.75_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 6; `ORC-6TZ2AQMQU4` |  |
| Phase transition | 1323.15 K | 1323.15 | peritectoid: Er35Zr65; _alloy: Er 0.35, Zr 0.65_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 10; `ORC-U5G4RFUJBD` |  |
| Phase transition | 1648.15 K | 1648.15 | other: Er60Zr40; _alloy: Er 0.6, Zr 0.4_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 17; `ORC-NPGYZICH57` |  |
| Phase transition | 1658.15 K | 1658.15 | other: Er52Zr48; _alloy: Er 0.52, Zr 0.48_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 15; `ORC-U2DITWY36E` |  |
| Phase transition | 1663.15 K | 1663.15 | other: Er68Zr32; _alloy: Er 0.68, Zr 0.32_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 21; `ORC-QSVKQKETUB` |  |
| Phase transition | 1673.15 K | 1673.15 | other: Er45Zr55; _alloy: Er 0.45, Zr 0.55_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 13; `ORC-RFVGS4BFDS` |  |
| Phase transition | 1678.15 K | 1678.15 | other: Er66.5Zr33.5; _alloy: Er 0.665, Zr 0.335_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 19; `ORC-GAKOAAWIAQ` |  |
| Phase transition | 1693.15 K | 1693.15 | other: Er80Zr20; _alloy: Er 0.8, Zr 0.2_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 23; `ORC-5W7DCYMNFF` |  |
| Phase transition | 1723.15 K | 1723.15 | other: Er35Zr65; _alloy: Er 0.35, Zr 0.65_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 9; `ORC-KNF7SXTJ75` |  |
| Phase transition | 1733.15 K | 1733.15 | other: Er90Zr10; _alloy: Er 0.9, Zr 0.1_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 25; `ORC-TR5RA3GLV3` |  |
| Phase transition | 1823.15 K | 1823.15 | other: Er20Zr80; _alloy: Er 0.2, Zr 0.8_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 4; `ORC-F6BI7HECAK` |  |

### Phase equilibrium (20)

Table: Phase equilibrium, Er–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 773.15 | (Zr) + (Er); _(Zr): Er 0.123, Zr 0.877; (Er): Er 0.855, Zr 0.145_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 1; `ORC-3XKMQDPOVE` |  |
| Phase composition |  | 773.15 | (Zr) + (Er); _(Zr): Er 0.124, Zr 0.876; (Er): Er 0.925, Zr 0.075_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 2; `ORC-BXMMNX7D4T` |  |
| Phase composition |  | 1123.15 | (Zr) + (Er); _(Zr): Er 0.149, Zr 0.851; (Er): Er 0.887, Zr 0.113_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 3; `ORC-CNVDD4QPMP` |  |
| Phase composition |  | 1123.15 | (Zr) + (Er); _(Zr): Er 0.154, Zr 0.846; (Er): Er 0.879, Zr 0.121_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 4; `ORC-WKJFNCHST2` |  |
| Phase composition |  | 1273.15 | (Zr) + (Er); _(Zr): Er 0.253, Zr 0.747; (Er): Er 0.798, Zr 0.202_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 6; `ORC-UF4SPAQQDO` |  |
| Phase composition |  | 1273.15 | (Zr) + (Er); _(Zr): Er 0.26, Zr 0.74; (Er): Er 0.79, Zr 0.21_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 5; `ORC-YAIIUIZ7CW` |  |
| Phase composition |  | 1323.15 | (Zr) + (Er); _(Zr): Er 0.33, Zr 0.67; (Er): Er 0.756, Zr 0.244_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 7; `ORC-W3J7UUDH2A` |  |
| Phase composition |  | 1373.15 | (Zr) + (Er); _(Zr): Er 0.21, Zr 0.79; (Er): Er 0.719, Zr 0.281_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 8; `ORC-SQVF6ESEQJ` |  |
| Phase composition |  | 1373.15 | (Zr) + (Er); _(Zr): Er 0.218, Zr 0.782; (Er): Er 0.679, Zr 0.321_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 9; `ORC-YYWEB7KXQM` |  |
| Phase composition |  | 1473.15 | (Zr) + (Er); _(Zr): Er 0.346, Zr 0.654; (Er): Er 0.683, Zr 0.317_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 10; `ORC-J3FU5PHP5R` |  |
| Phase composition |  | 1473.15 | (Zr) + (Er); _(Zr): Er 0.335, Zr 0.665; (Er): Er 0.693, Zr 0.307_ | experimental | [1] Jourdan 2010 | Table 1, p. 3, row 11; `ORC-NOX3BOHHXN` |  |
| Phase composition |  | 1663.15 | other: Er60Zr40; _liquid: Er 0.6, Zr 0.4_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 16; `ORC-CB4XNUOW2N` |  |
| Phase composition |  | 1679.15 | other: Er52Zr48; _liquid: Er 0.52, Zr 0.48_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 14; `ORC-IQRRDFXYS4` |  |
| Phase composition |  | 1688.15 | other: Er66.5Zr33.5; _liquid: Er 0.665, Zr 0.335_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 18; `ORC-E4PMPAOAXF` |  |
| Phase composition |  | 1688.15 | other: Er68Zr32; _liquid: Er 0.68, Zr 0.32_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 20; `ORC-PAHWFJ3OAU` |  |
| Phase composition |  | 1703.15 | other: Er45Zr55; _liquid: Er 0.45, Zr 0.55_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 12; `ORC-G7SU5NRADU` |  |
| Phase composition |  | 1723.15 | other: Er80Zr20; _liquid: Er 0.8, Zr 0.2_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 22; `ORC-CEAIATGEUX` |  |
| Phase composition |  | 1753.15 | other: Er35Zr65; _liquid: Er 0.35, Zr 0.65_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 8; `ORC-KPQEGUHRKU` |  |
| Phase composition |  | 1763.15 | other: Er90Zr10; _liquid: Er 0.9, Zr 0.1_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 24; `ORC-4DP65G36WT` |  |
| Phase composition |  | 2113.15 | other: Zr; _liquid: Zr 1_ | experimental | [1] Jourdan 2010 | Table 2, p. 4, row 1; `ORC-RHK2J75NMI` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Jourdan, C. Toffolon-Masclet, J.-M. Joubert, Experimental re-determination and thermodynamic assessment of the erbium–zirconium system, Journal of Nuclear Materials 402, 102-107 (2010). [doi:10.1016/j.jnucmat.2010.05.002](https://doi.org/10.1016/j.jnucmat.2010.05.002)

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
