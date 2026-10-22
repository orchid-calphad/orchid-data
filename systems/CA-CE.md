# Ca–Ce system

> Ca–Ce system: 40 accepted literature values (invariant reaction 14, mixing / partial 12, crystal structure 11, phase transition 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-CE.html · Markdown: https://data.orchid-project.org/systems/CA-CE.md

40 accepted literature values from 2 paper(s) (experimental 11, model 11, DFT 18); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-CE.json) · [CSV](https://data.orchid-project.org/systems/CA-CE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-CE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-CE/CaCe-07Ham.json) · [Markdown](https://data.orchid-project.org/systems/CA-CE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 11 |
| DFT | 18 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |
| phase transition | 3 |
| mixing / partial | 12 |
| crystal structure | 11 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaCe-07Ham.tdb | M. Hampl, J. Groebner, R. Schmid-Fetzer, J. Mater. Sci., 42, 10023-31(2007). [doi:10.1007/s10853-007-2002-2](https://doi.org/10.1007/s10853-007-2002-2) | `c783a715a2b1db9f1e667cd9cd9858db3086dd2c0a2c66fa74898e1cbeabe0e7` | [viewer](https://orchid-project.org/phase-diagrams/#CA-CE/CaCe-07Ham.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaCe-07Ham.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaCe-07Ham.json) |
| CaCe-08Zha.tdb | H. Zhang, Y. Wang, S. Shang, L.-Q. Chen, Z.-K. Liu, J. Alloys Compd., 463, 294-301(2008). [doi:10.1016/j.jallcom.2007.09.020](https://doi.org/10.1016/j.jallcom.2007.09.020) | `e5b5b58aa607f94b67a4cff28f58070d8665ea36dfb6451561fb51e2bb899fc4` | [viewer](https://orchid-project.org/phase-diagrams/#CA-CE/CaCe-08Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaCe-08Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaCe-08Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaCe-07Ham.tdb | 1123.38 | LIQUID#2 (x(Ce) 0.01968) + BCC_A2 (x(Ce) 0.02761) + LIQUID (x(Ce) 0.98032) |
| CaCe-07Ham.tdb | 1084.67 | BCC_A2 (x(Ce) 0.02431) + BCC_A2#2 (x(Ce) 0.97569) + LIQUID (x(Ce) 0.98387) |
| CaCe-07Ham.tdb | 993.34 | BCC_A2#2 (x(Ce) 0.01631) + BCC_A2 (x(Ce) 0.98369) + FCC_A1 (x(Ce) 0.98638) |
| CaCe-07Ham.tdb | 715.65 | FCC_A1#2 (x(Ce) 0.00242) + BCC_A2 (x(Ce) 0.00251) + FCC_A1 (x(Ce) 0.99758) |
| CaCe-08Zha.tdb | 1105.66 | BCC_A2 (x(Ce) 9.000e-5) + LIQUID#2 (x(Ce) 0.00821) + LIQUID (x(Ce) 0.99179) |
| CaCe-08Zha.tdb | 1105.66 | BCC_A2 (x(Ce) 9.000e-5) + LIQUID (x(Ce) 0.00821) + LIQUID#2 (x(Ce) 0.99179) |
| CaCe-08Zha.tdb | 1061.45 | BCC_A2#2 (x(Ce) 6.000e-5) + LIQUID (x(Ce) 0.99366) + BCC_A2 (x(Ce) 0.99994) |
| CaCe-08Zha.tdb | 1061.45 | BCC_A2 (x(Ce) 6.000e-5) + LIQUID (x(Ce) 0.99366) + BCC_A2#2 (x(Ce) 0.99994) |
| CaCe-08Zha.tdb | 1000 | BCC_A2 (x(Ce) 4.000e-5) + BCC_A2#2 (x(Ce) 0.99996) + FCC_A1 (x(Ce) 0.99997) |
| CaCe-08Zha.tdb | 716.03 | BCC_A2 (x(Ce) 0) + FCC_A1 (x(Ce) 0) + FCC_A1#2 (x(Ce) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-CE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-CE.json) · [CALPHAD hull CaCe-07Ham](https://data.orchid-project.org/hulls/calphad-sgte/CA/CA-CE--CaCe-07Ham.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Ce system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1123.15 | L′ + L″ = βCa |  | model | [1] Hampl 2007 | Table 3, p. 5, row 1 |  |
| 1122.15 | L′ + L″ = βCa |  | experimental | [1] Hampl 2007 | Table 3, p. 5, row 2 |  |
| 1108 | Liquid 1 -> bcc(Ca) + liquid 2 | Liquid 1: Ce 0.002 | experimental | [2] Zhang 2008; _cites Gschneider 1961_ | Table 5, p. 4, row 3 |  |
| 1105.8 | Liquid 1 -> bcc(Ca) + liquid 2 | Liquid 1: Ce 0.0027; bcc(Ca): Ce 2.300e-4; liquid 2: Ce 0.9997 | model | [2] Zhang 2008 | Table 5, p. 4, row 4 |  |
| 1079.15 | L″ + βCa = βCe |  | model | [1] Hampl 2007 | Table 3, p. 5, row 3 |  |
| 1078.15 | L″ + βCa = βCe |  | experimental | [1] Hampl 2007 | Table 3, p. 5, row 4 |  |
| 1068 | Liquid 1 -> bcc(Ce) + bcc(Ca) | Liquid 1: Ce 0.997 | experimental | [2] Zhang 2008; _cites Gschneider 1961_ | Table 5, p. 4, row 1 |  |
| 1061.7 | Liquid 1 -> bcc(Ce) + bcc(Ca) | Liquid 1: Ce 0.998; bcc(Ce): Ce 0.9998; bcc(Ca): Ce 1.500e-5 | model | [2] Zhang 2008 | Table 5, p. 4, row 2 |  |
| 993.15 | βCe = αCe + βCa |  | model | [1] Hampl 2007 | Table 3, p. 5, row 5 |  |
| 993.15 | βCe = αCe + βCa |  | experimental | [1] Hampl 2007 | Table 3, p. 5, row 6 |  |
| 787.15 | eutectic |  | model | [1] Hampl 2007 | p. 7 | “This eutectic matrix, corresponding to reaction E2 at 514 °C, consists mainly of (Mg) and CaMg2 with a small amount of CeMg12 and a calculated overall composition of 10 at.% Ca and 0.45 at.% Ce.” |
| 787.15 | eutectic |  | model | [1] Hampl 2007 | p. 7 | “Under Scheil conditions a solid phase cannot be consumed; all of the Ce5Mg41 is frozen-in and solidification proceeds along the monovariant eutectic L = CaMg2 + CeMg12 until the ternary eutectic E2 at 514 °C is reached with a large amount (30%) of residual liquid, 10 times more than in the equilibrium case.” |
| 727.15 | βCa = αCa (+αCe) |  | experimental | [1] Hampl 2007 | Table 3, p. 5, row 8 |  |
| 715.15 | βCa = αCa (+αCe) |  | model | [1] Hampl 2007 | Table 3, p. 5, row 7 |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Ca–Ce system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 855.15 K | 855.15 | other | model | [1] Hampl 2007 | p. 7 | “So far the Scheil and equilibrium calculations for this alloy are essentially the same until reaction U5 at 582 °C is reached.” |
| Phase transition | 884.15 K | 884.15 | other | model | [1] Hampl 2007 | p. 4 | “The seemingly similar reaction U4 at 611 °C is not degenerate, even though the liquid contains only 0.02 at.% Ca.” |
| Phase transition | 1123.15 K | 1123.15 | other | model | [1] Hampl 2007 | p. 6 | “It is noted that the invariant reaction at 850 °C is not a monotectic but a syntectic one, due to the solid solubility.” |

### Mixing / partial (12)

Table: Mixing / partial, Ca–Ce system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing | 22.719 kJ/mol (basis unstated) | 0 | Ca0.25Ce0.75; _alloy: Ce 0.75_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 7 |  |
| Enthalpy of mixing | 18.208 kJ/mol (basis unstated) | 0 | Ca0.25Ce0.75 (with magnetic); _alloy: Ce 0.75_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 10 |  |
| Enthalpy of mixing | 21.928 kJ/mol (basis unstated) | 0 | Ca0.50Ce0.50; _alloy: Ce 0.5_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 8 |  |
| Enthalpy of mixing | 20.989 kJ/mol (basis unstated) | 0 | Ca0.50Ce0.50 (with magnetic); _alloy: Ce 0.5_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 11 |  |
| Enthalpy of mixing | 16.488 kJ/mol (basis unstated) | 0 | Ca0.75Ce0.25; _alloy: Ce 0.25_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 9 |  |
| Enthalpy of mixing | 15.827 kJ/mol (basis unstated) | 0 | Ca0.75Ce0.25 (with magnetic); _alloy: Ce 0.25_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 12 |  |
| Enthalpy of mixing | 15.827 kJ/mol (basis unstated) | 0 | bcc; _alloy: Ce 0.25_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 12 |  |
| Enthalpy of mixing | 22.719 kJ/mol (basis unstated) | 0 | bcc; _alloy: Ce 0.75_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 7 |  |
| Enthalpy of mixing | 20.989 kJ/mol (basis unstated) | 0 | bcc; _alloy: Ce 0.5_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 11 |  |
| Enthalpy of mixing | 21.928 kJ/mol (basis unstated) | 0 | bcc; _alloy: Ce 0.5_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 8 |  |
| Enthalpy of mixing | 18.208 kJ/mol (basis unstated) | 0 | bcc; _alloy: Ce 0.75_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 10 |  |
| Enthalpy of mixing | 16.488 kJ/mol (basis unstated) | 0 | bcc; _alloy: Ce 0.25_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 9 |  |

### Crystal structure (11)

Table: Crystal structure, Ca–Ce system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice unspecified axis; _printed: Lattice parameter_ | 4.5 Å |  | Ca; _alloy: Ce 0_ | experimental | [2] Zhang 2008; _cites Lide 2002_ | Table 1, p. 2, row 2 |  |
| lattice unspecified axis; _printed: Lattice parameter_ | 4.4 Å | 0 | Ca; _alloy: Ce 0_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 1 |  |
| lattice unspecified axis; _printed: Lattice parameter_ | 4.5 Å |  | bcc; _alloy: Ce 0_ | experimental | [2] Zhang 2008; _cites Lide 2002_ | Table 1, p. 2, row 2 |  |
| lattice unspecified axis; _printed: Calculated lattice parameter_ | 4.4 Å | 0 | bcc; _alloy: Ce 0_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 1 |  |
| lattice unspecified axis; _printed: Lattice parameter_ | 3.756 Å | 1041 | Ce; _alloy: Ce 1_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 3 |  |
| lattice unspecified axis; _printed: Lattice parameter_ | 4.11 Å | 1041 | Ce; _alloy: Ce 1_ | experimental | [2] Zhang 2008; _cites Koskenmaki 1981_ | Table 1, p. 2, row 4 |  |
| lattice unspecified axis; _printed: Lattice parameter_ | 4.11 Å | 1041 | Ce (with magnetic); _alloy: Ce 1_ | experimental | [2] Zhang 2008; _cites Koskenmaki 1981_ | Table 1, p. 2, row 6 |  |
| lattice unspecified axis; _printed: Lattice parameter_ | 3.759 Å | 1041 | Ce (with magnetic); _alloy: Ce 1_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 5 |  |
| lattice unspecified axis; _printed: Calculated lattice parameter_ | 3.756 Å | 1041 | bcc; _alloy: Ce 1_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 3 |  |
| lattice unspecified axis; _printed: Lattice parameter_ | 4.11 Å | 1041 | bcc; _alloy: Ce 1_ | experimental | [2] Zhang 2008; _cites Koskenmaki 1981_ | Table 1, p. 2, row 6 |  |
| lattice unspecified axis; _printed: Calculated lattice parameter_ | 3.759 Å | 1041 | bcc; _alloy: Ce 1_ | DFT | [2] Zhang 2008 | Table 1, p. 2, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Milan Hampl, Joachim Gröbner, Rainer Schmid-Fetzer, Experimental study of phase equilibria and solidification microstructures of Mg–Ca–Ce alloys combined with thermodynamic modeling, J Mater Sci 42, 10023-10031 (2007). [doi:10.1007/s10853-007-2002-2](https://doi.org/10.1007/s10853-007-2002-2)
2. Hui Zhang, Yi Wang, Shunli Shang, Long-Qing Chen, Zi-Kui Liu, Thermodynamic modeling of Mg–Ca–Ce system by combining first-principles and CALPHAD method, Journal of Alloys and Compounds 463, 294-301 (2008). [doi:10.1016/j.jallcom.2007.09.020](https://doi.org/10.1016/j.jallcom.2007.09.020)

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
