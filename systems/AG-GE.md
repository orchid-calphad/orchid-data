# Ag–Ge system

> Ag–Ge system: 22 accepted literature values (invariant reaction 13, phase transition 6, phase equilibrium 3) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-GE.html · Markdown: https://data.orchid-project.org/systems/AG-GE.md

22 accepted literature values from 4 paper(s) (experimental 19, model 3); 3 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-GE.json) · [CSV](https://data.orchid-project.org/systems/AG-GE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-GE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-11Wan.json) · [phases (5)](https://data.orchid-project.org/phases/pages/AG-GE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-GE.html) · [Markdown](https://data.orchid-project.org/systems/AG-GE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 6 |
| phase equilibrium | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgGe-11Wan.tdb | J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermochim. Acta, 512, 240-46(2011). [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003) | `ee980cd7d96cd65640c7356ecc0c7ac3684d5e0d6c9e6bea9532f66373f24559` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGe-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGe-11Wan.json) |
| AgGe-18Raj.tdb | V.B. Rajkumar, S.-W. Chen, J. Electron. Mater., 47, 3666-77(2018). [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7) | `76195dd4c052f435fdc403917b36910abbc5b680653b5b13f0cd57b30ded5082` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-18Raj.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGe-18Raj.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGe-18Raj.json) |
| AgGe-88Che-LB.tdb | P.-Y. Chevalier, Thermochim. Acta, 130, 25-32(1988). [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3) | `30d36f0532b3185255f40b154c857353e3d92c9a8fb851b4f3c3340f0eafbb50` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-88Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGe-88Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGe-88Che-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgGe-11Wan.tdb | 920.27 | FCC_A1 (x(Ge) 0.09978) + LIQUID (x(Ge) 0.24907) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-11Wan.tdb | 920.27 | FCC_A1 (x(Ge) 0.09978) + LIQUID (x(Ge) 0.24906) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-18Raj.tdb | 924.77 | FCC_A1 (x(Ge) 0.09584) + LIQUID (x(Ge) 0.25453) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-18Raj.tdb | 924.77 | FCC_A1 (x(Ge) 0.09579) + LIQUID (x(Ge) 0.25439) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-88Che-LB.tdb | 923.22 | FCC_A1 (x(Ge) 0.09603) + LIQUID (x(Ge) 0.24891) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-88Che-LB.tdb | 923.22 | FCC_A1 (x(Ge) 0.09597) + LIQUID (x(Ge) 0.2488) + DIAMOND_A4 (x(Ge) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-GE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-GE.json) · [CALPHAD hull AgGe-11Wan](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-GE--AgGe-11Wan.json) · [CALPHAD hull AgGe-88Che-LB](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-GE--AgGe-88Che-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Ge system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 924 | eutectic: L -> fcc + dia | fcc: Ge 0.096 | experimental | [1] Chevalier 1988; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | Table 2, p. 5, row 5; `ORC-RGUQBOFASQ` |  |
| 924 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | diamond_A4(Ge): Ge 1 | experimental | [2] Wang 2011; _cites Hume-Rothery 1940_ | Table 1, p. 2, row 3; `ORC-W4VMSWLYC4` |  |
| 923.5 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.24; diamond_A4(Ge): Ge 1 | experimental | [2] Wang 2011; _cites Hassam 1988_ [doi](https://doi.org/10.1007/bf02649254) | Table 1, p. 2, row 5; `ORC-2ZKPDIOD74` |  |
| 923.4 | eutectic: L -> fcc + dia | L: Ge 0.249; fcc: Ge 0.096 | model | [1] Chevalier 1988 | Table 2, p. 5, row 1; `ORC-DUPVSJFGSS` |  |
| 923.4 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.249; diamond_A4(Ge): Ge 1 | model | [2] Wang 2011; _cites Chevalier 1988_ [doi](https://doi.org/10.1016/0040-6031%2888%2987047-3) | Table 1, p. 2, row 6; `ORC-KA5DUCQ6EB` |  |
| 923 | eutectic: L -> fcc + dia | L: Ge 0.26; fcc: Ge 0.065 | experimental | [1] Chevalier 1988; _cites Bull 1980_ | Table 2, p. 5, row 2; `ORC-AJ2QWRHXXG` |  |
| 923 | eutectic: L -> fcc + dia | fcc: Ge 0.081 | experimental | [1] Chevalier 1988; _cites Owen 1940_ | Table 2, p. 5, row 6; `ORC-E2QDAEEZRY` |  |
| 923 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.26; diamond_A4(Ge): Ge 1 | experimental | [2] Wang 2011; _cites Briggs 1929_ [doi](https://doi.org/10.1021/j150301a010) | Table 1, p. 2, row 1; `ORC-T4775PDIM5` |  |
| 923 | eutectic: L -> fcc + dia | L: Ge 0.24 | experimental | [1] Chevalier 1988; _cites Maucher 1936_ | Table 2, p. 5, row 4; `ORC-UVROGFCC4W` |  |
| 923 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.24; diamond_A4(Ge): Ge 1 | experimental | [2] Wang 2011; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | Table 1, p. 2, row 4; `ORC-Z4APIJHMNQ` |  |
| 922 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.241; diamond_A4(Ge): Ge 1 | experimental | [2] Wang 2011; _cites Maucher 1936_ | Table 1, p. 2, row 2; `ORC-6DFXWHXESF` |  |
| 922 | eutectic: L -> fcc + dia | L: Ge 0.241; fcc: Ge 0.079 | experimental | [1] Chevalier 1988; _cites Briggs 1929_ [doi](https://doi.org/10.1021/j150301a010) | Table 2, p. 5, row 3; `ORC-Q4XYHVNJYA` |  |
| 921 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.249; diamond_A4(Ge): Ge 1 | model | [2] Wang 2011 | Table 1, p. 2, row 7; `ORC-TIYKRVUQSM` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Ag–Ge system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 922 K | 922 | eutectic | experimental | [3] Hassam 1988; _cites Maucher 1936_ | Table I, p. 2, row 2; `ORC-NDFFPOWSWH` |  |
| Phase transition | 923 K | 923 | eutectic | experimental | [3] Hassam 1988; _cites Briggs 1929_ [doi](https://doi.org/10.1021/j150301a010) | Table I, p. 2, row 1; `ORC-IYMUBV5HCS` |  |
| Phase transition | 924 K | 924 | eutectic | experimental | [3] Hassam 1988; _cites Martin-Garin 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990094-6) | Table I, p. 2, row 3; `ORC-N7RSDZENUR` |  |
| Phase transition | 1028 K | 1028 (>) | other: 7.49 ± 0.742 at.% Ge solidus; _alloy: Ag 0.9251, Ge 0.0749_ | experimental | [4] Rajkumar 2018 | Table III, p. 5, row 6; `ORC-473KEK7CHH` |  |
| Phase transition | 1073 K | 1073 (>) | other: 5.51 ± 0.748 at.% Ge solidus; _alloy: Ag 0.9449, Ge 0.0551_ | experimental | [4] Rajkumar 2018 | Table III, p. 5, row 4; `ORC-2X7M7LMCA7` |  |
| Phase transition | 1132 K | 1132 (>) | other: 3.67 ± 0.649 at.% Ge solidus; _alloy: Ag 0.9633, Ge 0.0367_ | experimental | [4] Rajkumar 2018 | Table III, p. 5, row 2; `ORC-RH4BN57FUE` |  |

### Phase equilibrium (3)

Table: Phase equilibrium, Ag–Ge system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1154 | other: 7.49 ± 0.742 at.% Ge liquidus; _liquid: Ag 0.9251, Ge 0.0749_ | experimental | [4] Rajkumar 2018 | Table III, p. 5, row 5; `ORC-N7AOC2ESTH` |  |
| Phase composition |  | 1178 | other: 5.51 ± 0.748 at.% Ge liquidus; _liquid: Ag 0.9449, Ge 0.0551_ | experimental | [4] Rajkumar 2018 | Table III, p. 5, row 3; `ORC-OWMBOIIDGG` |  |
| Phase composition |  | 1201 | other: 3.67 ± 0.649 at.% Ge liquidus; _liquid: Ag 0.9633, Ge 0.0367_ | experimental | [4] Rajkumar 2018 | Table III, p. 5, row 1; `ORC-TNMKX2HEUB` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. P.-Y. Chevalier, Critical assessment of thermodynamic data for the Ag-Ge system, Thermochimica Acta 130, 25-32 (1988). [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3)
2. J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic description of the Au–Ag–Ge ternary system, Thermochimica Acta 512, 240-246 (2011). [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003)
3. S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988). [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254)
4. V. B. Rajkumar, Sinn-Wen Chen, Phase Equilibria and Thermodynamic Descriptions of Ag-Ge and Ag-Ge-Ni Systems, Journal of Elec Materi 47, 3666-3677 (2018). [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7)

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
