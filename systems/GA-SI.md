# Ga–Si system

> Ga–Si system: 24 accepted literature values (crystal structure 12, phase equilibrium 11, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-SI.html · Markdown: https://data.orchid-project.org/systems/GA-SI.md

24 accepted literature values from 1 paper(s) (experimental 20, unspecified 4); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-SI.json) · [CSV](https://data.orchid-project.org/systems/GA-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-SI/GaSi-05Fra-LB.json) · [phases (6)](https://data.orchid-project.org/phases/pages/GA-SI.html) · [Markdown](https://data.orchid-project.org/systems/GA-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 20 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase equilibrium | 11 |
| crystal structure | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaSi-05Fra-LB.tdb | P. Franke, unpublished, 2005. | `90a1f15279062a1cdf52ee06ec44d185d1191130296d3a7cacc6e4191c9e7066` | [viewer](https://orchid-project.org/phase-diagrams/#GA-SI/GaSi-05Fra-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaSi-05Fra-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaSi-05Fra-LB.json) |
| GaSi-85Ole.tdb | R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 362-64(1095). [doi:10.1007/BF02880523](https://doi.org/10.1007/BF02880523) | `fab542640f16379f390f04bfcd35a85b2551b4df6a8904e364fc898fda7208f8` | [viewer](https://orchid-project.org/phase-diagrams/#GA-SI/GaSi-85Ole.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaSi-85Ole.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaSi-85Ole.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaSi-05Fra-LB.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Si) 0) + LIQUID (x(Si) 0) + DIAMOND_A4 (x(Si) 1) |
| GaSi-85Ole.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Si) 0) + LIQUID (x(Si) 0) + DIAMOND_A4 (x(Si) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-SI.json) · [CALPHAD hull GaSi-85Ole](https://data.orchid-project.org/hulls/calphad-sgte/GA/GA-SI--GaSi-85Ole.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ga–Si system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 293.15 | eutectic |  | experimental | [1] Olesinski 1985; _cites ref. 58Sav_ | p. 1 | “The temperature-composition coordinates of the liquidus listed in Table 1 have been taken from \[48Kle\], \[53Kec\], and \[77Girl; the data of \[58Sav\] seem to be questionable (the authors claimed the eutectic point to be at 20 ~ and 1.2 at.% Si).” |

## Other properties

### Phase equilibrium (11)

Table: Phase equilibrium, Ga–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 578.15 | Liquid + L; _Liquid: Ga 0.9999, Si 1.000e-4; L: Ga 0.9999, Si 1.000e-4_ | experimental | [1] Olesinski 1985; _cites Keck 1953_ | Table 1, p. 1, row 11 |  |
| Phase composition |  | 753.15 | Liquid + L; _Liquid: Ga 0.998, Si 0.002; L: Ga 0.998, Si 0.002_ | experimental | [1] Olesinski 1985; _cites Girault 1977_ | Table 1, p. 1, row 10 |  |
| Phase composition |  | 773.15 | Liquid + L; _Liquid: Ga 0.9974, Si 0.0026; L: Ga 0.9974, Si 0.0026_ | experimental | [1] Olesinski 1985; _cites Keck 1953_ | Table 1, p. 1, row 9 |  |
| Phase composition |  | 883.15 | Liquid + L; _Liquid: Ga 0.993, Si 0.007; L: Ga 0.993, Si 0.007_ | experimental | [1] Olesinski 1985; _cites Girault 1977_ | Table 1, p. 1, row 8 |  |
| Phase composition |  | 973.15 | Liquid + L; _Liquid: Ga 0.98, Si 0.02; L: Ga 0.98, Si 0.02_ | experimental | [1] Olesinski 1985; _cites Girault 1977_ | Table 1, p. 1, row 7 |  |
| Phase composition |  | 1023.15 | Liquid + L; _Liquid: Ga 0.95, Si 0.05; L: Ga 0.95, Si 0.05_ | experimental | [1] Olesinski 1985; _cites ref. 48Kle_ | Table 1, p. 1, row 6 |  |
| Phase composition |  | 1028.15 | Liquid + L; _Liquid: Ga 0.965, Si 0.035; L: Ga 0.965, Si 0.035_ | experimental | [1] Olesinski 1985; _cites Keck 1953_ | Table 1, p. 1, row 5 |  |
| Phase composition |  | 1073.15 | Liquid + L; _Liquid: Ga 0.95, Si 0.05; L: Ga 0.95, Si 0.05_ | experimental | [1] Olesinski 1985; _cites Girault 1977_ | Table 1, p. 1, row 4 |  |
| Phase composition |  | 1173.15 | Liquid + L; _Liquid: Ga 0.9, Si 0.1; L: Ga 0.9, Si 0.1_ | experimental | [1] Olesinski 1985; _cites ref. 48Kle_ | Table 1, p. 1, row 3 |  |
| Phase composition |  | 1273.15 | Liquid + L; _Liquid: Ga 0.8, Si 0.2; L: Ga 0.8, Si 0.2_ | experimental | [1] Olesinski 1985; _cites ref. 48Kle_ | Table 1, p. 1, row 2 |  |
| Phase composition |  | 1423.15 | Liquid + L; _Liquid: Ga 0.6, Si 0.4; L: Ga 0.6, Si 0.4_ | experimental | [1] Olesinski 1985; _cites ref. 48Kle_ | Table 1, p. 1, row 1 |  |

### Crystal structure (12)

Table: Crystal structure, Ga–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 1.0593 nm | 237.15 | (γGa); _(γGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 4 |  |
| Lattice a | 0.27713 nm | 250.15 | (βGa); _(βGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 3 |  |
| Lattice a | 0.909 nm | 254.15 | (δGa); _(δGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 5 |  |
| Lattice a | 0.54306 nm | 298.15 | (Si); _(Si): Ga 0.001, Si 0.999_ | unspecified | [1] Olesinski 1985; _cites ref. 1_ | Table 4, p. 2, row 1 |  |
| Lattice a | 0.45192 nm | 298.15 | (αGaI); _(αGaI): Ga 1, Si 0_ | unspecified | [1] Olesinski 1985; _cites ref. 1_ | Table 4, p. 2, row 2 |  |
| Lattice b | 1.3523 nm | 237.15 | (γGa); _(γGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 4 |  |
| Lattice b | 0.80606 nm | 250.15 | (βGa); _(βGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 3 |  |
| Lattice b | 0.76586 nm | 298.15 | (αGaI); _(αGaI): Ga 1, Si 0_ | unspecified | [1] Olesinski 1985; _cites ref. 1_ | Table 4, p. 2, row 2 |  |
| Lattice c | 0.5203 nm | 237.15 | (γGa); _(γGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 4 |  |
| Lattice c | 0.33314 nm | 250.15 | (βGa); _(βGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 3 |  |
| Lattice c | 1.702 nm | 254.15 | (δGa); _(δGa): Ga 1, Si 0_ | experimental | [1] Olesinski 1985; _cites Defrain 1977_ [doi](https://doi.org/10.1051/jcp/1977740851) | Table 4, p. 2, row 5 |  |
| Lattice c | 0.45258 nm | 298.15 | (αGaI); _(αGaI): Ga 1, Si 0_ | unspecified | [1] Olesinski 1985; _cites ref. 1_ | Table 4, p. 2, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. R. W. Olesinski, N. Kanani, G. J. Abbaschian, The Ga−Si (Gallium-Silicon) system, Bulletin of Alloy Phase Diagrams 6, 362-364 (1985). [doi:10.1007/bf02880523](https://doi.org/10.1007/bf02880523)

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
