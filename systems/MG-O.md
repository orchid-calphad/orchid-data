# Mg–O system

> Mg–O system: 35 accepted literature values (phase equilibrium 26, formation 5, heat capacity / entropy / enthalpy 3, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-O.html · Markdown: https://data.orchid-project.org/systems/MG-O.md

35 accepted literature values from 3 paper(s) (experimental 8, model 20, DFT 3, unspecified 4); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-O.json) · [CSV](https://data.orchid-project.org/systems/MG-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-O/MgO-18Lia.json) · [phases (8)](https://data.orchid-project.org/phases/pages/MG-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MG-O.html) · [Markdown](https://data.orchid-project.org/systems/MG-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 20 |
| DFT | 3 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| phase equilibrium | 26 |
| formation | 5 |
| heat capacity / entropy / enthalpy | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgO-18Lia.tdb | S.-M. Liang, R. Schmid-Fetzer, J. Eur. Ceram. Soc., 38, 4768-85(2018). [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | `28bd068049e41b579b0e2a29e75feb9e8ac64c72b5b2fa8daa7bfae24147c334` | [viewer](https://orchid-project.org/phase-diagrams/#MG-O/MgO-18Lia.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgO-18Lia.json) |
| MgO-23Li.tdb | X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023). [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) | `d795b07d34aedd0d85468125fa5ec66c6e7f72b88dcc68b79c61adaf4cfbbb95` | [viewer](https://orchid-project.org/phase-diagrams/#MG-O/MgO-23Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgO-23Li.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MG/MG-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-O.json) · [CALPHAD hull MgO-18Lia](https://data.orchid-project.org/hulls/calphad-sgte/MG/MG-O--MgO-18Lia.json) · [CALPHAD hull MgO-93Hal-LB](https://data.orchid-project.org/hulls/calphad-sgte/MG/MG-O--MgO-93Hal-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Mg–O system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| MgO |  | -602 kJ/(mol 0) | 298.15 | experimental |  |  | [1] Hallstedt 1993; _cites Fikner_ | p. 5; `ORC-HACIS2G7EH` | “However, Fikner \[5J and Otsuka and Kozuka \[6J have found correlations between the enthalpy and entropy of dissolution of 0 into liquid metals and the enthalpy of formation of the oxide at 298 K. Using the expressions provided by Fitzner I5J with the enthalpy of formation of MgO (A?&s = -602 kJ/(mol 0)) gives A"G = -500000 + 90T J/mol for dissolution of 0 in liquid Mg (1 mol-W standard state).” |
| MgO | [MgO](https://data.orchid-project.org/compounds/MgO.html) | -300.62 kJ/mol-atom |  | model | -294.608 (mp-aaaaabwr) | -284.268 (oqmd-1443261) | [2] Li 2023 | Table 5, p. 6, row 1; `ORC-XV5TPNSVBM.04345a` |  |
| MgO |  | -282.82 kJ/mol-atom |  | DFT |  |  | [2] Li 2023 | Table 3, p. 5, row 2; `ORC-FD66XG5EMK` |  |
| MgO |  | -281.86 kJ/mol-atom | 0 | DFT |  |  | [2] Li 2023 | Table 3, p. 5, row 1; `ORC-HM2EPURU2E` |  |
| MgO |  | -263.71 kJ/mol-atom |  | DFT |  |  | [2] Li 2023 | Table 3, p. 5, row 3; `ORC-DAWTDSHCJ3` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Mg–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 3249.6 K | 3249.6 | congruent transformation | model | [3] Liang 2018 | p. 11; `ORC-YZVMY6AYNL` | “This stable range of liquid oxide extends from 49.98 to 50.01 at.% O at 1 bar with a calculated congruent melting point of MgO at 3249.6 K.” |

### Phase equilibrium (26)

Table: Phase equilibrium, Mg–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 923 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 2; `ORC-7G2QWL3JRK` |  |
| Phase composition |  | 923 | liquid Mg; _liquid Mg: Mg 1, O 0_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 1; `ORC-7RPPKQGVCL` |  |
| Phase composition |  | 923 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1981_ | Table 2, p. 6, row 3; `ORC-KXXLUEI3VQ` |  |
| Phase composition |  | 1000 | liquid Mg; _liquid Mg: Mg 1, O 0_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 4; `ORC-5RDB7BDIH2` |  |
| Phase composition |  | 1000 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1981_ | Table 2, p. 6, row 6; `ORC-G6NIPKGDTK` |  |
| Phase composition |  | 1000 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 5; `ORC-NECKUB7CTM` |  |
| Phase composition |  | 1200 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1981_ | Table 2, p. 6, row 9; `ORC-GDZ4JZ4DNZ` |  |
| Phase composition |  | 1200 | liquid Mg; _liquid Mg: Mg 0.999996, O 4.000e-6_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 8; `ORC-P3NPFYMKZE` |  |
| Phase composition |  | 1200 | liquid Mg; _liquid Mg: Mg 1, O 0_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 7; `ORC-YC22QEPNP3` |  |
| Phase composition |  | 1373 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1981_ | Table 2, p. 6, row 12; `ORC-43E2NYRT75` |  |
| Phase composition |  | 1373 | liquid Mg; _liquid Mg: Mg 0.999998, O 2.000e-6_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 10; `ORC-73JE4FMD7G` |  |
| Phase composition |  | 1373 | liquid Mg; _liquid Mg: Mg 0.999986, O 1.400e-5_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 11; `ORC-WVHJOZG7XS` |  |
| Phase composition |  | 2647.5 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [3] Liang 2018; _cites Ruff 1913_ [doi](https://doi.org/10.1002/zaac.19130820131) | Table 4, p. 8, row 1; `ORC-TKFRYFP4L4` |  |
| Phase composition |  | 3073 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [3] Liang 2018; _cites Riley 1966_ | Table 4, p. 8, row 4; `ORC-3WKU277YLT` |  |
| Phase composition |  | 3073 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [3] Liang 2018; _cites Kanolt 1913_ | Table 4, p. 8, row 2; `ORC-GIK4GT2IHC` |  |
| Phase composition |  | 3096 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [3] Liang 2018; _cites Panek 1979_ | Table 4, p. 8, row 5; `ORC-UFUWF53JJ7` |  |
| Phase composition |  | 3098 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [3] Liang 2018; _cites McNally 1961_ | Table 4, p. 8, row 3; `ORC-2YCTTIPCLS` |  |
| Phase composition |  | 3098 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [3] Liang 2018; _cites Factsage 2017_ | Table 4, p. 8, row 12; `ORC-T4TGQPVCHM` |  |
| Phase composition |  | 3099 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [3] Liang 2018; _cites Hlavac 1982_ [doi](https://doi.org/10.1351/pac198254030681) | Table 4, p. 8, row 8; `ORC-LYKBGPPGOB` |  |
| Phase composition |  | 3100 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [3] Liang 2018; _cites SGTE 2013_ | Table 4, p. 8, row 13; `ORC-3IPRASD7EL` |  |
| Phase composition |  | 3100 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [3] Liang 2018; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874914) | Table 4, p. 8, row 9; `ORC-GJ5ZPRZD5D` |  |
| Phase composition |  | 3105 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [3] Liang 2018; _cites Chase 1998_ | Table 4, p. 8, row 11; `ORC-BAW3YNBM5R` |  |
| Phase composition |  | 3105 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [3] Liang 2018; _cites Kubaschewski 1993_ | Table 4, p. 8, row 10; `ORC-PIZL5ZU6S2` |  |
| Phase composition |  | 3215 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [3] Liang 2018; _cites Chernyshev 1993_ [doi](https://doi.org/10.1016/0040-6031%2893%2980422-7) | Table 4, p. 8, row 6; `ORC-RKBKCJUSWY` |  |
| Phase composition |  | 3250 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [3] Liang 2018; _cites Ronchi 2001_ [doi](https://doi.org/10.1063/1.1398069) | Table 4, p. 8, row 7; `ORC-EGWQ3OYD72` |  |
| Phase composition |  | 3250 | congruent melting: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [3] Liang 2018 | Table 4, p. 8, row 14; `ORC-L7IGD3VFZX` |  |

### Heat capacity / entropy / enthalpy (3)

Table: Heat capacity / entropy / enthalpy, Mg–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Standard entropy_ | 28.1 J/mol (basis unstated)/K |  | MgO; _alloy: Mg 0.5, O 0.5_ | model | [2] Li 2023 | Table 5, p. 6, row 1; `ORC-XV5TPNSVBM.278992` |  |
| Heat capacity; _printed: Heat capacity of the liquid oxide_ | 33.47 J/mol-atom/K |  | liquid oxide; _alloy: Mg 0.5, O 0.5_ | model | [2] Li 2023 | Table 5, p. 6, row 1; `ORC-XV5TPNSVBM.5a74b6` |  |
| Heat capacity; _printed: Heat capacity at 298.15 K_ | 18.65 J/mol-atom/K | 298.15 | MgO; _alloy: Mg 0.5, O 0.5_ | model | [2] Li 2023 | Table 5, p. 6, row 1; `ORC-XV5TPNSVBM.5c0a66` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Bengt Hallstedt, The Magnesium — Oxygen system, Calphad 17, 281-286 (1993). [doi:10.1016/0364-5916(93)90006-w](https://doi.org/10.1016/0364-5916%2893%2990006-w)
2. X.-J. Li, S.-H. Liu, Thermodynamic description of the Mg-O and Al-O systems, J min metall B Metall 59, 395-405 (2023). [doi:10.2298/jmmb230621034l](https://doi.org/10.2298/jmmb230621034l)
3. Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018). [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
