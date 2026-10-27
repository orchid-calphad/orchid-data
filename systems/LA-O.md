# La–O system

> La–O system: 47 accepted literature values (phase transition 19, formation 17, heat capacity / entropy / enthalpy 8, crystal structure 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-O.html · Markdown: https://data.orchid-project.org/systems/LA-O.md

47 accepted literature values from 2 paper(s) (experimental 31, model 14, unspecified 2); 2 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/LA-O.json) · [CSV](https://data.orchid-project.org/systems/LA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-O/LaO-01Gru.json) · [phases (15)](https://data.orchid-project.org/phases/pages/LA-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LA-O.html) · [Markdown](https://data.orchid-project.org/systems/LA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 31 |
| model | 14 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 19 |
| formation | 17 |
| heat capacity / entropy / enthalpy | 8 |
| crystal structure | 3 |

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
| A-La2O3 | [La2O3](https://data.orchid-project.org/compounds/La2O3.html) | -358.32 kJ/mol-atom | 298.15 | model | -373.797 (mp-aaaaadke) | -358.204 (oqmd-30652) | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 13; `ORC-R5Z7F2ZFHA.25c306` |  |
| La2O3 |  | -2255.2 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Roth 1940_ | Table 3, p. 3, row 11; `ORC-7HVF4JYGKC` |  |
| La2O3 |  | -2255.2 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Roth 1940_ | Table 3, p. 3, row 3; `ORC-YFLPG2T5CJ` |  |
| La2O3 |  | -1907.4 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Moose 1932_ | Table 3, p. 3, row 10; `ORC-VTONN5KR2B` |  |
| La2O3 |  | -1907.4 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Moose 1932_ | Table 3, p. 3, row 2; `ORC-WODDK3PHVQ` |  |
| La2O3 |  | -1866.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Von 1959_ | Table 3, p. 3, row 5; `ORC-N2BINSDHMC` |  |
| La2O3 |  | -1866.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Von 1959_ | Table 3, p. 3, row 13; `ORC-SNQD26D234` |  |
| La2O3 |  | -1862.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Muthmann 1904_ [doi](https://doi.org/10.1002/jlac.19043310102) | Table 3, p. 3, row 1; `ORC-MZVN67SSDB` |  |
| La2O3 |  | -1862.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Muthmann 1904_ [doi](https://doi.org/10.1002/jlac.19043310102) | Table 3, p. 3, row 9; `ORC-YGURYXCQZ3` |  |
| La2O3 |  | -1797.9 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Gvelesiani 1967_ | Table 3, p. 3, row 15; `ORC-5IIOJL5L26` |  |
| La2O3 |  | -1797.9 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Gvelesiani 1967_ | Table 3, p. 3, row 7; `ORC-O42ENWTUDL` |  |
| La2O3 |  | -1795.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Grundy 2001 | Table 3, p. 3, row 8; `ORC-TJJQJSMBNO` |  |
| La2O3 |  | -1795.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Grundy 2001 | Table 3, p. 3, row 16; `ORC-WDJW24J6FZ` |  |
| La2O3 |  | -1794.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Fitzgibbon 1965_ [doi](https://doi.org/10.1021/j100891a504) | Table 3, p. 3, row 14; `ORC-5GOJNYDWQX` |  |
| La2O3 |  | -1794.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Fitzgibbon 1965_ [doi](https://doi.org/10.1021/j100891a504) | Table 3, p. 3, row 6; `ORC-NJY6NALODN` |  |
| La2O3 |  | -1793.3 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Huber 1953_ [doi](https://doi.org/10.1021/ja01110a511) | Table 3, p. 3, row 12; `ORC-DMGNH64DQO` |  |
| La2O3 |  | -1793.3 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Grundy 2001; _cites Huber 1953_ [doi](https://doi.org/10.1021/ja01110a511) | Table 3, p. 3, row 4; `ORC-LZHJ3DOIB7` |  |

## Other properties

### Phase transition (19)

Table: Phase transition, La–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2113 K | 2113 | other: \[1913Ruf\] | experimental | [2] Grundy 2001; _cites Ruff 1913_ [doi](https://doi.org/10.1002/zaac.19130820131) | Table 1, p. 2, row 1; `ORC-MVNC3YU6GD` |  |
| Phase transition | 2303 K | 2303 | polymorphic: A ⟺ H; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 6, row 17; `ORC-PYAPMTFHGZ` |  |
| Phase transition | 2313 K | 2313 | polymorphic: A \<=> H; _alloy: La 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 10; `ORC-MF3RAQWG2I` |  |
| Phase transition | 2313 K | 2313 | polymorphic: A ⟺ H; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 6, row 13; `ORC-3ASW63ZSKL` |  |
| Phase transition | 2313 K | 2313 | polymorphic: A ⟺ H; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Molodkin 1982_ | Table 2.1, p. 6, row 19; `ORC-MFLU6J3IPY` |  |
| Phase transition | 2313 K | 2313 | polymorphic: A ⟺ H; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 11; `ORC-QYEQSIWOO3` |  |
| Phase transition | 2323 K | 2323 | polymorphic: A ⟺ H; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 6, row 15; `ORC-N2RWVNNDDA` |  |
| Phase transition | 2363 K | 2363 | polymorphic: H ⟺ X; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Molodkin 1982_ | Table 2.1, p. 6, row 20; `ORC-FMFWDVQKMG` |  |
| Phase transition | 2373 K | 2373 | polymorphic: H \<=> X; _alloy: La 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 24; `ORC-PAVKTIBCHT` |  |
| Phase transition | 2373 K | 2373 | polymorphic: H ⟺ X; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 6, row 14; `ORC-F3K2VHKS46` |  |
| Phase transition | 2373 K | 2373 | polymorphic: H ⟺ X; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 6, row 18; `ORC-NXEEMXM73I` |  |
| Phase transition | 2383 K | 2383 | polymorphic: H ⟺ X; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 12; `ORC-ZS4HHIIL64` |  |
| Phase transition | 2413 K | 2413 | polymorphic: H ⟺ X; _alloy: La 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 6, row 16; `ORC-H26XJKV6VC` |  |
| Phase transition | 2490 K | 2490 | other: \[1967Mor\] | experimental | [2] Grundy 2001; _cites Mordovin 1967_ | Table 1, p. 2, row 4; `ORC-6R32EVWYOC` |  |
| Phase transition | 2529 K | 2529 | other: \[1967Nog\] | experimental | [2] Grundy 2001; _cites Noguchi 1968_ | Table 1, p. 2, row 5; `ORC-L6E3ZVYAH7` |  |
| Phase transition | 2577 K | 2577 | other: \[1966Sat\] | experimental | [2] Grundy 2001; _cites Sata 1966_ | Table 1, p. 2, row 3; `ORC-UY72IKXCSB` |  |
| Phase transition | 2586 K | 2586 | other: \[1997SGT\], this study | unspecified | [2] Grundy 2001 | Table 1, p. 2, row 7; `ORC-DEVXRI5KWB` |  |
| Phase transition | 2588 K | 2588 | other: \[1932War\] | unspecified | [2] Grundy 2001; _cites ref. 1932War_ | Table 1, p. 2, row 2; `ORC-GCXUEW4SS2` |  |
| Phase transition | 2593 K | 2593 | other: \[1975Cou\] | experimental | [2] Grundy 2001; _cites Coutures 1975_ | Table 1, p. 2, row 6; `ORC-DHXCMV7LWD` |  |

### Heat capacity / entropy / enthalpy (8)

Table: Heat capacity / entropy / enthalpy, La–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: °S_ | 127.38 unknown | 298.15 | A-La2O3; _alloy: La 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 13; `ORC-R5Z7F2ZFHA.7ae51e` |  |
| Entropy; _printed: -ΔS298.15_ | -292.88 J/mol·K | 298.15 | La2O3; _alloy: O 0.6_ | experimental | [2] Grundy 2001; _cites Justice 1963_ [doi](https://doi.org/10.1021/j100796a031) | Table 4, p. 4, row 2; `ORC-FOGZE2XMGN` |  |
| Entropy; _printed: S298.15_ | 25.464 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001; _cites Justice 1963_ [doi](https://doi.org/10.1021/j100796a031) | Table 2, p. 3, row 1; `ORC-JNVTUXQCPD` |  |
| Entropy; _printed: S298.15_ | 25.468 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001 | Table 2, p. 3, row 4; `ORC-MOGBDVKS4N` |  |
| Entropy; _printed: S298.15_ | 25.59 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001; _cites Goldstein 1959_ [doi](https://doi.org/10.1021/j150579a028) | Table 2, p. 3, row 2; `ORC-MW3FCHNXUD` |  |
| Entropy; _printed: -ΔS298.15_ | -294.02 J/mol·K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001 | Table 4, p. 4, row 3; `ORC-O6NCUQ65FX` |  |
| Entropy; _printed: S298.15_ | 25.714 J/mol-atom/K | 298.15 | La2O3; _alloy: O 0.6_ | model | [2] Grundy 2001; _cites King 1961_ | Table 2, p. 3, row 3; `ORC-VQORFOQAX6` |  |
| Entropy; _printed: -ΔS298.15_ | -294.56 J/mol·K | 298.15 | La2O3; _alloy: O 0.6_ | experimental | [2] Grundy 2001; _cites King 1961_ | Table 4, p. 4, row 1; `ORC-VSCIOHTF62` |  |

### Crystal structure (3)

Table: Crystal structure, La–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 49.627 cm3 mol-1 | 298.15 | La2O3 (A-type); _alloy: La 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 3; `ORC-CZLPQCEH7L.b76c59` |  |
| lattice molar volume | 50.748 cm3 mol-1 | 298.15 | La2O3 (B-type); _alloy: La 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 3; `ORC-CZLPQCEH7L.5a2e7c` |  |
| lattice molar volume | 55.442 cm3 mol-1 | 298.15 | La2O3 (C-type); _alloy: La 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 3; `ORC-CZLPQCEH7L.428457` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)
2. A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001). [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
