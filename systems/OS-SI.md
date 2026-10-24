# Os–Si system

> Os–Si system: 18 accepted literature values (invariant reaction 17, phase equilibrium 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/OS-SI.html · Markdown: https://data.orchid-project.org/systems/OS-SI.md

18 accepted literature values from 1 paper(s) (experimental 13, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/OS-SI.json) · [CSV](https://data.orchid-project.org/systems/OS-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#OS-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#OS-SI/OsSi-01Liu-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/OS-SI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/OS-SI.html) · [Markdown](https://data.orchid-project.org/systems/OS-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 13 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase equilibrium | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| OsSi-01Liu-LB.tdb | Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001). [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) | `661081800c525b84650d894af942f1a36a9a98bddd7f6dc44ddd1d32320c9649` | [viewer](https://orchid-project.org/phase-diagrams/#OS-SI/OsSi-01Liu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/OsSi-01Liu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| OsSi-01Liu-LB.tdb | 2013.01 | LIQUID (x(Si) 0.4572) + MSI_B20 (x(Si) 0.5) + OS2SI3 (x(Si) 0.6) |
| OsSi-01Liu-LB.tdb | 2013.01 | LIQUID (x(Si) 0.45739) + MSI_B20 (x(Si) 0.5) + OS2SI3 (x(Si) 0.6) |
| OsSi-01Liu-LB.tdb | 2013.01 | LIQUID (x(Si) 0.45698) + MSI_B20 (x(Si) 0.5) + OS2SI3 (x(Si) 0.6) |
| OsSi-01Liu-LB.tdb | 1990.3 | HCP_A3 (x(Si) 0) + LIQUID (x(Si) 0.41952) + MSI_B20 (x(Si) 0.5) |
| OsSi-01Liu-LB.tdb | 1990.3 | HCP_A3 (x(Si) 0) + LIQUID (x(Si) 0.41947) + MSI_B20 (x(Si) 0.5) |
| OsSi-01Liu-LB.tdb | 1990.3 | HCP_A3 (x(Si) 0) + LIQUID (x(Si) 0.41939) + MSI_B20 (x(Si) 0.5) |
| OsSi-01Liu-LB.tdb | 1990.3 | HCP_A3 (x(Si) 0) + LIQUID (x(Si) 0.41938) + MSI_B20 (x(Si) 0.5) |
| OsSi-01Liu-LB.tdb | 1922.11 | OS2SI3 (x(Si) 0.6) + OSSI2 (x(Si) 0.66667) + LIQUID (x(Si) 0.78483) |
| OsSi-01Liu-LB.tdb | 1922.11 | OS2SI3 (x(Si) 0.6) + OSSI2 (x(Si) 0.66667) + LIQUID (x(Si) 0.7846) |
| OsSi-01Liu-LB.tdb | 1616.01 | OSSI2 (x(Si) 0.66667) + LIQUID (x(Si) 0.9088) + DIAMOND_A4 (x(Si) 1) |
| OsSi-01Liu-LB.tdb | 1616.01 | OSSI2 (x(Si) 0.66667) + LIQUID (x(Si) 0.90893) + DIAMOND_A4 (x(Si) 1) |
| OsSi-01Liu-LB.tdb | 1616.01 | OSSI2 (x(Si) 0.66667) + LIQUID (x(Si) 0.909) + DIAMOND_A4 (x(Si) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/OS/OS-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/OS/OS-SI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Os–Si system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2113 | liquid = Os2Si3 | liquid: Os 0.4, Si 0.6; Os2Si3: Os 0.4, Si 0.6 | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | Table 4, p. 8, row 1; `ORC-MVG7E3UUNR` |  |
| 2102 | liquid = Os2Si3 | liquid: Os 0.4, Si 0.6; Os2Si3: Os 0.4, Si 0.6 | model | [1] Liu 2001 | Table 4, p. 8, row 2; `ORC-ZRNRLMCK2I` |  |
| 2011 | liquid + Os2Si3 = OsSi | liquid: Si 0.46; Os2Si3: Si 0.6; OsSi: Si 0.5 | model | [1] Liu 2001 | Table 4, p. 8, row 10; `ORC-GQRTUDA6JZ` |  |
| 2003 | peritectic: liquid + Os2Si3 -> OsSi |  | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | p. 3; `ORC-WFOHTHAHNT.6e5950` | “Two eutectic and two peritectic transformations were identified: E1: liquid5(Si)1OsSi 2 at 1633 K, consistent with the results of \[8,23\]. E2: liquid5(Os)1OsSi at 1993 K. P1: liquid1Os 2 Si 3 5OsSi at 2003 K. P2: liquid1Os 2 Si 3 5OsSi 2 at 1913 K.” |
| 2003 | liquid + Os2Si3 = OsSi | Os2Si3: Si 0.6; OsSi: Si 0.5 | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | Table 4, p. 8, row 9; `ORC-XU4UXXJR66` |  |
| 1993 | liquid = OsSi + (Os) | liquid: Si 0.45; OsSi: Si 0.5; (Os): Si 0 | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | Table 4, p. 8, row 11; `ORC-7TTIL6NALG` |  |
| 1993 | eutectic: liquid -> (Os) + OsSi |  | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | p. 3; `ORC-WFOHTHAHNT.093aca` | “Two eutectic and two peritectic transformations were identified: E1: liquid5(Si)1OsSi 2 at 1633 K, consistent with the results of \[8,23\]. E2: liquid5(Os)1OsSi at 1993 K. P1: liquid1Os 2 Si 3 5OsSi at 2003 K. P2: liquid1Os 2 Si 3 5OsSi 2 at 1913 K.” |
| 1988 | liquid = OsSi + (Os) | liquid: Si 0.42; OsSi: Si 0.5; (Os): Si 0 | model | [1] Liu 2001 | Table 4, p. 8, row 12; `ORC-ZQESTJNF5P` |  |
| 1921 | liquid + Os2Si3 = OsSi2 | liquid: Si 0.78; Os2Si3: Si 0.6; OsSi2: Si 0.667 | model | [1] Liu 2001 | Table 4, p. 8, row 4; `ORC-BJXOFLWO3Z` |  |
| 1913 | liquid + Os2Si3 = OsSi2 | liquid: Si 0.72; Os2Si3: Si 0.6; OsSi2: Si 0.667 | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | Table 4, p. 8, row 3; `ORC-R4KMKVOKBP` |  |
| 1913 | peritectic: liquid + Os2Si3 -> OsSi2 |  | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | p. 3; `ORC-WFOHTHAHNT.4cad16` | “Two eutectic and two peritectic transformations were identified: E1: liquid5(Si)1OsSi 2 at 1633 K, consistent with the results of \[8,23\]. E2: liquid5(Os)1OsSi at 1993 K. P1: liquid1Os 2 Si 3 5OsSi at 2003 K. P2: liquid1Os 2 Si 3 5OsSi 2 at 1913 K.” |
| 1633 | liquid = OsSi2 + Diamond | OsSi2: Os 0.333333, Si 0.666667 | experimental | [1] Liu 2001; _cites Finnie 1962_ [doi](https://doi.org/10.1016/0022-5088%2862%2990055-3) | Table 4, p. 8, row 7; `ORC-4MZZYX3CG3` |  |
| 1633 | liquid = OsSi2 + Diamond | liquid: Si 0.88; OsSi2: Si 0.667; Diamond: Si 1 | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | Table 4, p. 8, row 5; `ORC-MZYWJVD4DQ` |  |
| 1633 | eutectic: liquid -> (Si) + OsSi2 |  | experimental | [1] Liu 2001; _cites Schellenberg 1988_ [doi](https://doi.org/10.1016/0022-5088%2888%2990148-8) | p. 3; `ORC-WFOHTHAHNT.504cde` | “Two eutectic and two peritectic transformations were identified: E1: liquid5(Si)1OsSi 2 at 1633 K, consistent with the results of \[8,23\]. E2: liquid5(Os)1OsSi at 1993 K. P1: liquid1Os 2 Si 3 5OsSi at 2003 K. P2: liquid1Os 2 Si 3 5OsSi 2 at 1913 K.” |
| 1630 | liquid = OsSi2 + Diamond | liquid: Si 0.9; OsSi2: Os 0.333333, Si 0.666667 | experimental | [1] Liu 2001; _cites Mason 1983_ [doi](https://doi.org/10.1016/0022-0248%2883%2990424-4) | Table 4, p. 8, row 6; `ORC-IZS7SVSTOR` |  |
| 1630 | eutectic |  | experimental | [1] Liu 2001; _cites Mason 1983_ [doi](https://doi.org/10.1016/0022-0248%2883%2990424-4) | p. 3; `ORC-UE3X4OM5AN` | “On slow cooling, OsSi 2 crystallized until the eutectic temperature was reached at 1630 K.” |
| 1615 | liquid = OsSi2 + Diamond | liquid: Si 0.9; OsSi2: Si 0.667; Diamond: Si 1 | model | [1] Liu 2001 | Table 4, p. 8, row 8; `ORC-U4KR7A3ZUJ` |  |

## Other properties

### Phase equilibrium (1)

Table: Phase equilibrium, Os–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  | 1730 | liquid; _alloy: Os 0.15, Si 0.85_ | experimental | [1] Liu 2001; _cites Mason 1983_ [doi](https://doi.org/10.1016/0022-0248%2883%2990424-4) | p. 3; `ORC-VH3LZCUGMT` | “It was found that the mixture of 15 at.% Os and 85 at.% Si was completely liquid at 1730 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Y.Q. Liu, G. Shao, K.P. Homewood, Thermodynamic assessment of the Ru–Si and Os–Si systems, Journal of Alloys and Compounds 320, 72-79 (2001). [doi:10.1016/s0925-8388(01)00931-8](https://doi.org/10.1016/s0925-8388%2801%2900931-8)

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
