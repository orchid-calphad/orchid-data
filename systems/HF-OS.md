# Hf–Os system

> Hf–Os system: 14 accepted literature values (invariant reaction 10, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-OS.html · Markdown: https://data.orchid-project.org/systems/HF-OS.md

14 accepted literature values from 1 paper(s) (experimental 7, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-OS.json) · [CSV](https://data.orchid-project.org/systems/HF-OS.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-OS) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-OS/HfOs-06Guo.json) · [Markdown](https://data.orchid-project.org/systems/HF-OS.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfOs-06Guo.tdb | C. Guo, Z. Du, J. Alloys Compd., 407, 188-92(2006). [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) | `a62b29616d7b427062c78afbe012638e4ddeabc91efea1d18c496415e9d6cee1` | [viewer](https://orchid-project.org/phase-diagrams/#HF-OS/HfOs-06Guo.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfOs-06Guo.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfOs-06Guo.tdb | 2823.29 | B2_BCC (x(Os) 0.49951) + LIQUID (x(Os) 0.55754) + HFOS2_C14 (x(Os) 0.6516) |
| HfOs-06Guo.tdb | 2797.94 | HFOS2_C14 (x(Os) 0.67149) + LIQUID (x(Os) 0.77793) + HCP_A3 (x(Os) 0.94873) |
| HfOs-06Guo.tdb | 1893.22 | LIQUID (x(Os) 0.22572) + HF54OS17 (x(Os) 0.23944) + B2_BCC (x(Os) 0.45842) |
| HfOs-06Guo.tdb | 1872.91 | B2_BCC (x(Os) 0.13513) + LIQUID (x(Os) 0.20147) + HF54OS17 (x(Os) 0.23944) |
| HfOs-06Guo.tdb | 1872.91 | B2_BCC (x(Os) 0.1351) + LIQUID (x(Os) 0.20145) + HF54OS17 (x(Os) 0.23944) |
| HfOs-06Guo.tdb | 1492.96 | HCP_A3 (x(Os) 0.00415) + B2_BCC (x(Os) 0.09224) + HF54OS17 (x(Os) 0.23944) |
| HfOs-06Guo.tdb | 1492.96 | HCP_A3 (x(Os) 0.00415) + B2_BCC (x(Os) 0.09223) + HF54OS17 (x(Os) 0.23944) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-OS.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-OS.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hf–Os system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2823 | liq. -> HfOs + HfOs2 | L: Os 0.536; HfOs: Os 0.51; HfOs2: Os 0.64 | experimental | [1] Guo 2006; _cites Eremenko 1993_ | Table 2, p. 4, row 10 |  |
| 2823 | liq. -> HfOs + HfOs2 | L: Os 0.5576; HfOs: Os 0.4995; HfOs2: Os 0.6518 | model | [1] Guo 2006 | Table 2, p. 4, row 9 |  |
| 2798 | liq. -> HfOs2 + hcp(Os) | L: Os 0.7779; HfOs2: Os 0.6715; hcp(Os): Os 0.9487 | model | [1] Guo 2006 | Table 2, p. 4, row 13 |  |
| 2798 | liq. -> HfOs2 + hcp(Os) | L: Os 0.793; HfOs2: Os 0.68; hcp(Os): Os 0.952 | experimental | [1] Guo 2006; _cites Eremenko 1993_ | Table 2, p. 4, row 14 |  |
| 1893 | liq. + HfOs -> Hf54Os17 | L: Os 0.2257; HfOs: Os 0.4584; Hf54Os17: Os 0.239437 | model | [1] Guo 2006 | Table 2, p. 4, row 5 |  |
| 1893 | liq. + HfOs -> Hf54Os17 | L: Os 0.23; HfOs: Os 0.47; Hf54Os17: Os 0.239437 | experimental | [1] Guo 2006; _cites Eremenko 1993_ | Table 2, p. 4, row 6 |  |
| 1873 | liq. -> bcc(Hf) + Hf54Os17 | L: Os 0.2015; bcc(Hf): Os 0.1351; Hf54Os17: Os 0.239437 | model | [1] Guo 2006 | Table 2, p. 4, row 1 |  |
| 1873 | liq. -> bcc(Hf) + Hf54Os17 | L: Os 0.201; bcc(Hf): Os 0.13; Hf54Os17: Os 0.239437 | experimental | [1] Guo 2006; _cites Eremenko 1993_ | Table 2, p. 4, row 2 |  |
| 1493 | bcc(Hf) -> hcp(Hf) + Hf54Os17 | bcc(Hf): Os 0.098; hcp(Hf): Os 0.011; Hf54Os17: Os 0.239437 | experimental | [1] Guo 2006; _cites Eremenko 1993_ | Table 2, p. 4, row 4 |  |
| 1493 | bcc(Hf) -> hcp(Hf) + Hf54Os17 | bcc(Hf): Os 0.0922; hcp(Hf): Os 0.0041; Hf54Os17: Os 0.239437 | model | [1] Guo 2006 | Table 2, p. 4, row 3 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Hf–Os system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2868 K | 2868 | liq. -> HfOs; _L: Os 0.4918; HfOs: Os 0.4918_ | model | [1] Guo 2006 | Table 2, p. 4, row 7 |  |
| Phase transition | 2868 K | 2868 | liq. -> HfOs; _L: Os 0.495; HfOs: Os 0.495_ | experimental | [1] Guo 2006; _cites Eremenko 1993_ | Table 2, p. 4, row 8 |  |
| Phase transition | 2953 K | 2953 | liq. -> HfOs2; _L: Os 0.6623; HfOs2: Os 0.6623_ | model | [1] Guo 2006 | Table 2, p. 4, row 11 |  |
| Phase transition | 2953 K | 2953 | liq. -> HfOs2; _L: Os 0.667; HfOs2: Os 0.667_ | experimental | [1] Guo 2006; _cites Eremenko 1993_ | Table 2, p. 4, row 12 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006). [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
