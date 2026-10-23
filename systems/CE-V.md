# Ce–V system

> Ce–V system: 12 accepted literature values (invariant reaction 12) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-V.html · Markdown: https://data.orchid-project.org/systems/CE-V.md

12 accepted literature values from 1 paper(s) (model 4, unspecified 8); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-V.json) · [CSV](https://data.orchid-project.org/systems/CE-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-V/CeV-10Cha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CE-V.html) · [Markdown](https://data.orchid-project.org/systems/CE-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 4 |
| unspecified | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeV-10Cha.tdb | W. Chan, M.C. Gao, O.N. Dogan, P. King, J. Phase Equilib. Diffus., 31, 425-32(2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4) | `94a5599f614a500403ac63347850b09d3afcd53c7a3d13859831d8d6d4f735cc` | [viewer](https://orchid-project.org/phase-diagrams/#CE-V/CeV-10Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeV-10Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeV-10Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeV-10Cha.tdb | 2154.41 | LIQUID (x(V) 0.01731) + LIQUID#2 (x(V) 0.98269) + BCC_A2 (x(V) 0.99949) |
| CeV-10Cha.tdb | 1072.12 | LIQUID (x(V) 4.000e-5) + BCC_A2#2 (x(V) 1.100e-4) + BCC_A2 (x(V) 1) |
| CeV-10Cha.tdb | 999.84 | FCC_A1 (x(V) 0) + BCC_A2#2 (x(V) 6.000e-5) + BCC_A2 (x(V) 1) |
| CeV-10Cha.tdb | 999.84 | FCC_A1 (x(V) 0) + BCC_A2#2 (x(V) 6.000e-5) + BCC_A2 (x(V) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–V system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2180.15 | L2 \<-> L1 + V | L2: V 0.99; L1: V 0.0169; V: V 0.994 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 2 |  |
| 2158.15 | L2 \<-> L1 + V | L2: V 0.999; L1: V 0.016; V: V 0.9995 | unspecified | [1] Chan 2010; _cites Efimov 2010_ | Table 2, p. 4, row 1 |  |
| 2154.15 | L2 \<-> L1 + V | L2: V 0.9827; L1: V 0.0173; V: V 0.9995 | model | [1] Chan 2010 | Table 2, p. 4, row 3 |  |
| 1083.15 | L + V \<-> δCe |  | unspecified | [1] Chan 2010; _cites Efimov 2010_ | Table 2, p. 4, row 4 |  |
| 1074.15 | L + V \<-> δCe | L: V 4.000e-5; δCe: V 1.100e-4 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 5 |  |
| 1072.15 | L + V \<-> δCe | L: V 4.000e-5; V: V 1; δCe: V 1.100e-4 | model | [1] Chan 2010 | Table 2, p. 4, row 6 |  |
| 999.85 | δCe \<-> V + γCe | δCe: V 0; V: V 1; γCe: V 0 | model | [1] Chan 2010 | Table 2, p. 4, row 9 |  |
| 999.15 | δCe \<-> V + γCe |  | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 8 |  |
| 978.15 | δCe \<-> V + γCe |  | unspecified | [1] Chan 2010; _cites Efimov 2010_ | Table 2, p. 4, row 7 |  |
| 334.15 | γCe \<-> V + βCe |  | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 10 |  |
| 283.15 | γCe \<-> V + βCe |  | unspecified | [1] Chan 2010; _cites Gschneidner 1999_ [doi](https://doi.org/10.1361/105497199770340590) | Table 2, p. 4, row 11 |  |
| 283 | γCe \<-> V + βCe | γCe: V 0; V: V 1; βCe: V 0 | model | [1] Chan 2010 | Table 2, p. 4, row 12 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Thermodynamic Assessment of V-Rare Earth Systems, J. Phase Equilib. Diffus. 31, 425-432 (2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4)

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
