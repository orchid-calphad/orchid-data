# Mg–Tl system

> Mg–Tl system: 15 accepted literature values (invariant reaction 10, phase transition 4, formation 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-TL.html · Markdown: https://data.orchid-project.org/systems/MG-TL.md

15 accepted literature values from 1 paper(s) (experimental 8, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-TL.json) · [CSV](https://data.orchid-project.org/systems/MG-TL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-TL) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-TL/MgTl-08Liu.json) · [phases (7)](https://data.orchid-project.org/phases/pages/MG-TL.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MG-TL.html) · [Markdown](https://data.orchid-project.org/systems/MG-TL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 4 |
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgTl-08Liu.tdb | Y. Liu, D. Liang, J. Alloys Compd., 459, 286-90(2008). [doi:10.1016/j.jallcom.2007.04.031](https://doi.org/10.1016/j.jallcom.2007.04.031) | `e8378fccc52d0d12f2313e676963dcfd08817b258db84355a4d93ff1bc732475` | [viewer](https://orchid-project.org/phase-diagrams/#MG-TL/MgTl-08Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgTl-08Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgTl-08Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MgTl-08Liu.tdb | 678.52 | HCP_A3 (x(Tl) 0.16108) + LIQUID (x(Tl) 0.24224) + MG5TL2_D8G (x(Tl) 0.28571) |
| MgTl-08Liu.tdb | 678.52 | HCP_A3 (x(Tl) 0.16107) + LIQUID (x(Tl) 0.24223) + MG5TL2_D8G (x(Tl) 0.28571) |
| MgTl-08Liu.tdb | 664.5 | MG5TL2_D8G (x(Tl) 0.28571) + MG2TL_C22 (x(Tl) 0.33333) + LIQUID (x(Tl) 0.36046) |
| MgTl-08Liu.tdb | 664.5 | MG5TL2_D8G (x(Tl) 0.28571) + MG2TL_C22 (x(Tl) 0.33333) + LIQUID (x(Tl) 0.36042) |
| MgTl-08Liu.tdb | 624.83 | MG2TL_C22 (x(Tl) 0.33333) + LIQUID (x(Tl) 0.44832) + MGTL_B2 (x(Tl) 0.5) |
| MgTl-08Liu.tdb | 624.83 | MG2TL_C22 (x(Tl) 0.33333) + LIQUID (x(Tl) 0.44805) + MGTL_B2 (x(Tl) 0.5) |
| MgTl-08Liu.tdb | 624.83 | MG2TL_C22 (x(Tl) 0.33333) + LIQUID (x(Tl) 0.44871) + MGTL_B2 (x(Tl) 0.5) |
| MgTl-08Liu.tdb | 545.12 | LIQUID (x(Tl) 0.94831) + HCP_A3 (x(Tl) 0.99287) + BCC_A2 (x(Tl) 0.99975) |
| MgTl-08Liu.tdb | 474.84 | MGTL_B2 (x(Tl) 0.5) + LIQUID (x(Tl) 0.81635) + HCP_A3 (x(Tl) 0.9682) |
| MgTl-08Liu.tdb | 474.84 | MGTL_B2 (x(Tl) 0.5) + LIQUID (x(Tl) 0.81616) + HCP_A3 (x(Tl) 0.96815) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MG/MG-TL.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-TL.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mg–Tl system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 678.5 | eutectic: Liquid -> hcp + Mg5Tl2 | Liquid: Tl 0.242; hcp: Tl 0.161; Mg5Tl2: Tl 0.285714 | model | [1] Liu 2008 | Table 2, p. 4, row 1; `ORC-VTLMXLNWCA` |  |
| 678.3 | eutectic: Liquid -> hcp + Mg5Tl2 | Liquid: Tl 0.25; hcp: Tl 0.154; Mg5Tl2: Tl 0.285714 | experimental | [1] Liu 2008; _cites Hume-Rothery 1938_ | Table 2, p. 4, row 2; `ORC-65E6743DSU` |  |
| 665 | Liquid + Mg5Tl2 -> Mg2Tl | Liquid: Tl 0.343; Mg5Tl2: Tl 0.285714; Mg2Tl: Tl 0.333333 | experimental | [1] Liu 2008; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.19340400213) | Table 2, p. 4, row 6; `ORC-QEEJS66DAT` |  |
| 664.5 | Liquid + Mg5Tl2 -> Mg2Tl | Liquid: Tl 0.361; Mg5Tl2: Tl 0.285714; Mg2Tl: Tl 0.333333 | model | [1] Liu 2008 | Table 2, p. 4, row 5; `ORC-5F7XKXR5Y6` |  |
| 626 | eutectic: Liquid -> Mg2Tl + MgTl | Liquid: Tl 0.425; Mg2Tl: Tl 0.333333; MgTl: Tl 0.5 | experimental | [1] Liu 2008; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.19340400213) | Table 2, p. 4, row 8; `ORC-UQYJNC7XHV` |  |
| 624.8 | eutectic: Liquid -> Mg2Tl + MgTl | Liquid: Tl 0.448; Mg2Tl: Tl 0.333333; MgTl: Tl 0.5 | model | [1] Liu 2008 | Table 2, p. 4, row 7; `ORC-QN3E2HU5GX` |  |
| 477.4 | eutectic: Liquid -> MgTl + bcc | Liquid: Tl 0.813; MgTl: Tl 0.5; bcc: Tl 0.959 | model | [1] Liu 2008 | Table 2, p. 4, row 11; `ORC-WAPK2DALS6` |  |
| 475 | eutectic: Liquid -> MgTl + bcc | Liquid: Tl 0.8; MgTl: Tl 0.5; bcc: Tl 0.952 | experimental | [1] Liu 2008; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.19340400213) | Table 2, p. 4, row 12; `ORC-XCLW642NPM` |  |
| 433 | bcc -> MgTl + hcp | bcc: Tl 0.95; MgTl: Tl 0.5; hcp: Tl 0.97 | experimental | [1] Liu 2008; _cites Grube 1905_ | Table 2, p. 4, row 14; `ORC-7UCAOOIHZJ` |  |
| 432.2 | bcc -> MgTl + hcp | bcc: Tl 0.971; MgTl: Tl 0.5; hcp: Tl 0.979 | model | [1] Liu 2008 | Table 2, p. 4, row 13; `ORC-3SX7WBH7I5` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Mg–Tl system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| MgTl |  | -24.3 unspecified ± 4.2 | 600 | experimental |  |  | [1] Liu 2008; _cites Kubaschewski 1941_ | p. 2; `ORC-IRPNLJYZSC` | “The only value reported for the enthalpy of formation of MgTl is -24.3 ± 4.2 kJ/mol atoms \[11\], which was determined at 600 K by an adiabatic high-temperature calorimeter with all the starting materials having a purity of 99.96%.” |

## Other properties

### Phase transition (4)

Table: Phase transition, Mg–Tl system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 631 K | 631 | Liquid -> MgTl; _Liquid: Tl 0.5; MgTl: Tl 0.5_ | experimental | [1] Liu 2008; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.19340400213) | Table 2, p. 4, row 10; `ORC-VJLJP7RKDF` |  |
| Phase transition | 631.9 K | 631.9 | Liquid -> MgTl; _Liquid: Tl 0.5; MgTl: Tl 0.5_ | model | [1] Liu 2008 | Table 2, p. 4, row 9; `ORC-ROX3BABETO` |  |
| Phase transition | 686 K | 686 | Mg5Tl2 -> liquid; _Mg5Tl2: Tl 0.285714; liquid: Tl 0.285714_ | experimental | [1] Liu 2008; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.19340400213) | Table 2, p. 4, row 4; `ORC-IVQFK3G3GP` |  |
| Phase transition | 687.5 K | 687.5 | Mg5Tl2 -> liquid; _Mg5Tl2: Tl 0.285714; liquid: Tl 0.285714_ | model | [1] Liu 2008 | Table 2, p. 4, row 3; `ORC-DI7XODJH4J` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Dong Liang, Thermodynamic reevaluation of the Mg–Tl system, Journal of Alloys and Compounds 459, 286-290 (2008). [doi:10.1016/j.jallcom.2007.04.031](https://doi.org/10.1016/j.jallcom.2007.04.031)

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
