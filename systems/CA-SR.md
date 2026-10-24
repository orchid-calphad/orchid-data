# Ca–Sr system

> Ca–Sr system: 7 accepted literature values (crystal structure 4, formation 2, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-SR.html · Markdown: https://data.orchid-project.org/systems/CA-SR.md

7 accepted literature values from 2 paper(s) (experimental 1, unspecified 6); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-SR.json) · [CSV](https://data.orchid-project.org/systems/CA-SR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-SR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-SR/CaSr-03Zho.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CA-SR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CA-SR.html) · [Markdown](https://data.orchid-project.org/systems/CA-SR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| unspecified | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| formation | 2 |
| crystal structure | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaSr-03Zho.tdb | Y. Zhong, K. Ozturk, Z.-K. Liu, J. Phase Equilib., 24, 340-46(2003). [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) | `b8538512e55eacb5ee55ac97cd448e519b93b12ac6c87b4a46455267c73148e8` | [viewer](https://orchid-project.org/phase-diagrams/#CA-SR/CaSr-03Zho.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaSr-03Zho.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaSr-03Zho.json) |
| CaSr-07Shi.tdb | D. Shin, PhD Thesis, 2007. | `11fdb0087a5341fa0ad0c00120fa6d79ccee69e656b6ee63c2f1c786713e0ee1` | [viewer](https://orchid-project.org/phase-diagrams/#CA-SR/CaSr-07Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaSr-07Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaSr-07Shi.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-SR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-SR.json) · [CALPHAD hull CaSr-03Zho](https://data.orchid-project.org/hulls/calphad-sgte/CA/CA-SR--CaSr-03Zho.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ca–Sr system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ca2Sr-C14 | [Ca2Sr](https://data.orchid-project.org/compounds/Ca2Sr.html) | 2.5445 kJ/mol-atom | 0 | unspecified |  | 1.213 (oqmd-1450029) | [1] Zhong 2006 | Table 2, p. 4, row 18 |  |
| Sr2Ca-C14 | [CaSr2](https://data.orchid-project.org/compounds/CaSr2.html) | 15.7965 kJ/mol-atom | 0 | unspecified |  | 2.047 (oqmd-1449632) | [1] Zhong 2006 | Table 2, p. 4, row 20 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ca–Sr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1011.15 K | 1011.15 | other | experimental | [2] Zhong 2003; _cites Schottmiller 1958_ [doi](https://doi.org/10.1021/j150569a024) | p. 1 | “Schottmiller et al. \[1958Sch\] determined the liquidus and solidus by thermal analysis with an uncertainty about ±2 °C. They prepared alloys from 99.8 wt.% Ca and doubly distilled 99.7 wt.% Sr in Fe crucibles in an argon atmosphere. The liquidus has a minimum at about 738 °C and 62 at.% Sr.” |

### Crystal structure (4)

Table: Crystal structure, Ca–Sr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 7.347 Å | 0 | Ca2Sr-C14; _alloy: Sr 0.333333_ | unspecified | [1] Zhong 2006 | Table 2, p. 4, row 18 |  |
| Lattice a; _printed: a_ | 7.649 Å | 0 | Sr2Ca-C14; _alloy: Sr 0.666667_ | unspecified | [1] Zhong 2006 | Table 2, p. 4, row 20 |  |
| Lattice c; _printed: c_ | 12.124 Å | 0 | Ca2Sr-C14; _alloy: Sr 0.333333_ | unspecified | [1] Zhong 2006 | Table 2, p. 4, row 18 |  |
| Lattice c; _printed: c_ | 12.378 Å | 0 | Sr2Ca-C14; _alloy: Sr 0.666667_ | unspecified | [1] Zhong 2006 | Table 2, p. 4, row 20 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006). [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076)
2. Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003). [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325)

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
