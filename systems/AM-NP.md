# Am–Np system

> Am–Np system: 1 accepted literature values (invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AM-NP.html · Markdown: https://data.orchid-project.org/systems/AM-NP.md

1 accepted literature values from 1 paper(s) (experimental 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AM-NP.json) · [CSV](https://data.orchid-project.org/systems/AM-NP.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AM-NP) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AM-NP/AmNp-10Kur.json) · [phases (7)](https://data.orchid-project.org/phases/pages/AM-NP.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AM-NP.html) · [Markdown](https://data.orchid-project.org/systems/AM-NP.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AmNp-10Kur.tdb | M. Kurata, IOP Conf. Ser.: Mater. Sci. Eng., 9, 012023(2010). | `2a5ba036840cfb6c59a6f5f5f8ea9dd828ed606d973bc361614d26fa5548f273` | [viewer](https://orchid-project.org/phase-diagrams/#AM-NP/AmNp-10Kur.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AmNp-10Kur.json) |
| AmNp-93Oga.tdb | T. Ogawa, J. Alloys Compd., 194, 1-7(1993). [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) | `cfa44b10057e67b3e1a0e537dec78e40930acfe402fe4bdcbabdbb27ab076aeb` | [viewer](https://orchid-project.org/phase-diagrams/#AM-NP/AmNp-93Oga.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AmNp-93Oga.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AmNp-10Kur.tdb | 1255.61 | FCC_A1 (x(Np) 0.01242) + BCC_A2 (x(Np) 0.05844) + LIQUID (x(Np) 0.62324) |
| AmNp-10Kur.tdb | 1041.98 | FCC_A1 (x(Np) 0.00653) + DHCP (x(Np) 0.00653) + LIQUID (x(Np) 0.92403) |
| AmNp-10Kur.tdb | 882.99 | DHCP (x(Np) 0.00292) + LIQUID (x(Np) 0.97248) + BCC_A2 (x(Np) 0.98901) |
| AmNp-10Kur.tdb | 844.56 | DHCP (x(Np) 0.00223) + BCC_A2 (x(Np) 0.99179) + TETRAG_AD (x(Np) 0.99776) |
| AmNp-10Kur.tdb | 555.03 | DHCP (x(Np) 7.000e-5) + TETRAG_AD (x(Np) 0.99991) + ORTHO_AC (x(Np) 0.99991) |
| AmNp-93Oga.tdb | 1215.18 | FCC_A1 (x(Np) 0.13302) + BCC_A2 (x(Np) 0.21555) + LIQUID (x(Np) 0.88326) |
| AmNp-93Oga.tdb | 941.32 | FCC_A1 (x(Np) 0.08507) + BCC_A2 (x(Np) 0.96373) + LIQUID (x(Np) 0.97839) |
| AmNp-93Oga.tdb | 823.05 | FCC_A1 (x(Np) 0.05622) + BCC_A2 (x(Np) 0.98132) + TETRAG_AD (x(Np) 1) |
| AmNp-93Oga.tdb | 823.05 | FCC_A1 (x(Np) 0.05617) + BCC_A2 (x(Np) 0.98134) + TETRAG_AD (x(Np) 1) |
| AmNp-93Oga.tdb | 787.47 | DHCP (x(Np) 0) + FCC_A1 (x(Np) 0.04719) + TETRAG_AD (x(Np) 1) |
| AmNp-93Oga.tdb | 787.47 | DHCP (x(Np) 0) + FCC_A1 (x(Np) 0.0471) + TETRAG_AD (x(Np) 1) |
| AmNp-93Oga.tdb | 555.03 | DHCP (x(Np) 0) + ORTHO_AC (x(Np) 1) + TETRAG_AD (x(Np) 1) |

Convex hulls: [CALPHAD hull AmNp-93Oga](https://data.orchid-project.org/hulls/calphad-sgte/AM/AM-NP--AmNp-93Oga.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Am–Np system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1250 | peritectic |  | experimental | [1] Kurata 2010; _cites Gibson 1992_ | p. 4 | “The thermal analysis data suggest a peritectic reaction among BCC, FCC, and liquid at around 1250 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M Kurata, Thermodynamic database on U-Pu-Zr-Np-Am-Fe alloy system II — Evaluation of Np, Am, and Fe containing systems-, IOP Conf. Ser.: Mater. Sci. Eng. 9, 012023 (2010). [doi:10.1088/1757-899x/9/1/012023](https://doi.org/10.1088/1757-899x/9/1/012023)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
