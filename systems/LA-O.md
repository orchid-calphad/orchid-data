# La–O system

> La–O system: 37 accepted literature values (formation 17, phase transition 13, heat capacity / entropy / enthalpy 7) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-O.html · Markdown: https://data.orchid-project.org/systems/LA-O.md

37 accepted literature values from 2 paper(s) (experimental 24, model 11, unspecified 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LA-O.json) · [CSV](https://data.orchid-project.org/systems/LA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-O/LaO-01Gru.json) · [phases (15)](https://data.orchid-project.org/phases/pages/LA-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LA-O.html) · [Markdown](https://data.orchid-project.org/systems/LA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 24 |
| model | 11 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 13 |
| formation | 17 |
| heat capacity / entropy / enthalpy | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LaO-01Gru.tdb | A.N. Grundy, B. Hallstedt, L.J. Gauckler, J. Phase Equilib., 22, 105-13(2001). [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) | `dd70787d0d64865c3636a46845bb2dbeccb575b1c515332d2b933a3966b68600` | [viewer](https://orchid-project.org/phase-diagrams/#LA-O/LaO-01Gru.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaO-01Gru.json) |
| LaO-07Zin.tdb | M. Zinkevich, Prog. Mater. Sci., 52, 597-647(2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) | `c8176e51a3d7e85115b4fd78fdd64e381a6d1011fab606a5a355fc028a9bf5f9` | [viewer](https://orchid-project.org/phase-diagrams/#LA-O/LaO-07Zin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaO-07Zin.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LaO-01Gru.tdb | 2382.84 | ION (x(O) 0.516) + X_LA2O3 (x(O) 0.58852) + H_LA2O3 (x(O) 0.58852) |
| LaO-01Gru.tdb | 2382.84 | H_LA2O3 (x(O) 0.59997) + X_LA2O3 (x(O) 0.59997) + GAS (x(O) 1) |
| LaO-01Gru.tdb | 2312.72 | ION (x(O) 0.49292) + H_LA2O3 (x(O) 0.58814) + A_LA2O3_D52 (x(O) 0.58814) |
| LaO-01Gru.tdb | 2312.72 | A_LA2O3_D52 (x(O) 0.59998) + H_LA2O3 (x(O) 0.59998) + GAS (x(O) 1) |
| LaO-01Gru.tdb | 1169.18 | BCC_A2 (x(O) 0.0673) + ION (x(O) 0.07877) + A_LA2O3_D52 (x(O) 0.59417) |
| LaO-01Gru.tdb | 1137.66 | BCC_A2 (x(O) 0.06302) + FCC_A1 (x(O) 0.06323) + A_LA2O3_D52 (x(O) 0.5945) |
| LaO-01Gru.tdb | 552.91 | FCC_A1 (x(O) 0.00403) + DHCP (x(O) 0.00443) + A_LA2O3_D52 (x(O) 0.59953) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LA/LA-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LA/LA-O.json) · [CALPHAD hull LaO-01Gru](https://data.orchid-project.org/hulls/calphad-sgte/LA/LA-O--LaO-01Gru.json) · [CALPHAD hull LaO-05Che](https://data.orchid-project.org/hulls/calphad-sgte/LA/LA-O--LaO-05Che.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, La–O system (17)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| A-La2O3 | [La2O3](https://data.orchid-project.org/compounds/La2O3.html) | -358.32 kJ/mol-atom | 298.15 | model | -373.797 (mp-aaaaadke) | -358.204 (oqmd-30652) | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 13 |  |
| La2O3 |  | -2255.2 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Roth 1940_ | Table 3, p. 3, row 11 |  |
| La2O3 |  | -2255.2 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Roth 1940_ | Table 3, p. 3, row 3 |  |
| La2O3 |  | -1907.4 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Moose 1932_ | Table 3, p. 3, row 10 |  |
| La2O3 |  | -1907.4 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Moose 1932_ | Table 3, p. 3, row 2 |  |
| La2O3 |  | -1866.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Von 1959_ | Table 3, p. 3, row 5 |  |
| La2O3 |  | -1866.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Von 1959_ | Table 3, p. 3, row 13 |  |
| La2O3 |  | -1862.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Muthmann 1904_ [doi](https://doi.org/10.1002/jlac.19043310102) | Table 3, p. 3, row 1 |  |
| La2O3 |  | -1862.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Muthmann 1904_ [doi](https://doi.org/10.1002/jlac.19043310102) | Table 3, p. 3, row 9 |  |
| La2O3 |  | -1797.9 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Gvelesiani 1967_ | Table 3, p. 3, row 15 |  |
| La2O3 |  | -1797.9 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Gvelesiani 1967_ | Table 3, p. 3, row 7 |  |
| La2O3 |  | -1795.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Grundy 2001 | Table 3, p. 3, row 8 |  |
| La2O3 |  | -1795.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Grundy 2001 | Table 3, p. 3, row 16 |  |
| La2O3 |  | -1794.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Fitzgibbon 1965_ [doi](https://doi.org/10.1021/j100891a504) | Table 3, p. 3, row 14 |  |
| La2O3 |  | -1794.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Fitzgibbon 1965_ [doi](https://doi.org/10.1021/j100891a504) | Table 3, p. 3, row 6 |  |
| La2O3 |  | -1793.3 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Huber 1953_ [doi](https://doi.org/10.1021/ja01110a511) | Table 3, p. 3, row 12 |  |
| La2O3 |  | -1793.3 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Huber 1953_ [doi](https://doi.org/10.1021/ja01110a511) | Table 3, p. 3, row 4 |  |

## Other properties

### Phase transition (13)

Table: Phase transition, La–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2113 K | 2113 | other: \[1913Ruf\] | experimental | [2] Grundy 2001; _cites Ruff 1913_ [doi](https://doi.org/10.1002/zaac.19130820131) | Table 1, p. 2, row 1 |  |
| Phase transition | 2313 K | 2313 | A-La2O3 -> H-La2O3 | model | [2] Grundy 2001 | p. 1 | “Neutron diffraction \[1979Ald\] and x-ray diffraction \[1966Foe\] studies at very high temperatures and analysis of cooling curves \[1965Foe\] show that A-La2O3 transforms to partially ordered hexagonal H-La2O3 at 2313 K, then to cubic X-La2O3 at 2383 K.” |
| Phase transition | 2313 K | 2313 | polymorphic | experimental | [2] Grundy 2001; _cites ref. 1965Foe_ | p. 4 | “A first indication of these three polymorphic phases was given when Foëx \[1965Foe\] found three distinctive steps in the cooling curves of molten lanthanum oxide, one at 2583 K corresponding to the solidification and two more at 2383 and 2313 K corresponding to the X → H and H → A transitions, respectively.” |
| Phase transition | 2383 K | 2383 | H-La2O3 -> X-La2O3 | model | [2] Grundy 2001 | p. 1 | “Neutron diffraction \[1979Ald\] and x-ray diffraction \[1966Foe\] studies at very high temperatures and analysis of cooling curves \[1965Foe\] show that A-La2O3 transforms to partially ordered hexagonal H-La2O3 at 2313 K, then to cubic X-La2O3 at 2383 K.” |
| Phase transition | 2383 K | 2383 | polymorphic | experimental | [2] Grundy 2001; _cites ref. 1965Foe_ | p. 4 | “A first indication of these three polymorphic phases was given when Foëx \[1965Foe\] found three distinctive steps in the cooling curves of molten lanthanum oxide, one at 2583 K corresponding to the solidification and two more at 2383 and 2313 K corresponding to the X → H and H → A transitions, respectively.” |
| Phase transition | 2490 K | 2490 | other: \[1967Mor\] | experimental | [2] Grundy 2001; _cites Mordovin 1967_ | Table 1, p. 2, row 4 |  |
| Phase transition | 2529 K | 2529 | other: \[1967Nog\] | experimental | [2] Grundy 2001; _cites Noguchi 1968_ | Table 1, p. 2, row 5 |  |
| Phase transition | 2577 K | 2577 | other: \[1966Sat\] | experimental | [2] Grundy 2001; _cites Sata 1966_ | Table 1, p. 2, row 3 |  |
| Phase transition | 2583 K | 2583 |  | experimental | [2] Grundy 2001; _cites ref. 1965Foe_ | p. 4 | “A first indication of these three polymorphic phases was given when Foëx \[1965Foe\] found three distinctive steps in the cooling curves of molten lanthanum oxide, one at 2583 K corresponding to the solidification and two more at 2383 and 2313 K corresponding to the X → H and H → A transitions, respectively.” |
| Phase transition | 2586 K | 2586 |  | model | [2] Grundy 2001 | p. 1 | “The average of these three measurements is 2586 K. This is the value adopted by the SGTE substance database \[1997SGT\] and is used for this study.” |
| Phase transition | 2586 K | 2586 | other: \[1997SGT\], this study | unspecified | [2] Grundy 2001 | Table 1, p. 2, row 7 |  |
| Phase transition | 2588 K | 2588 | other: \[1932War\] | unspecified | [2] Grundy 2001; _cites ref. 1932War_ | Table 1, p. 2, row 2 |  |
| Phase transition | 2593 K | 2593 | other: \[1975Cou\] | experimental | [2] Grundy 2001; _cites Coutures 1975_ | Table 1, p. 2, row 6 |  |

### Heat capacity / entropy / enthalpy (7)

Table: Heat capacity / entropy / enthalpy, La–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: -ΔS298.15_ | -292.88 J/mol·K | 298.15 | La2O3; _alloy: O 0.6_ | experimental | [2] Grundy 2001; _cites Justice 1963_ [doi](https://doi.org/10.1021/j100796a031) | Table 4, p. 4, row 2 |  |
| Entropy; _printed: S298.15_ | 25.464 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001; _cites Justice 1963_ [doi](https://doi.org/10.1021/j100796a031) | Table 2, p. 3, row 1 |  |
| Entropy; _printed: S298.15_ | 25.468 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001 | Table 2, p. 3, row 4 |  |
| Entropy; _printed: S298.15_ | 25.59 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001; _cites Goldstein 1959_ [doi](https://doi.org/10.1021/j150579a028) | Table 2, p. 3, row 2 |  |
| Entropy; _printed: -ΔS298.15_ | -294.02 J/mol·K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001 | Table 4, p. 4, row 3 |  |
| Entropy; _printed: S298.15_ | 25.714 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001; _cites King 1961_ | Table 2, p. 3, row 3 |  |
| Entropy; _printed: -ΔS298.15_ | -294.56 J/mol·K | 298.15 | La2O3; _alloy: O 0.6_ | experimental | [2] Grundy 2001; _cites King 1961_ | Table 4, p. 4, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)
2. A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001). [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950)

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
