# Cu–Ni system

> Cu–Ni system: 37 accepted literature values (activity / EMF / Gibbs energy 28, mixing / partial 3, phase transition 3, invariant reaction 2) and 4 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-NI.html · Markdown: https://data.orchid-project.org/systems/CU-NI.md

37 accepted literature values from 2 paper(s) (experimental 33, model 4); 4 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-NI.json) · [CSV](https://data.orchid-project.org/systems/CU-NI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-NI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-NI/CuNi-07Tur.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CU-NI.html) · [Markdown](https://data.orchid-project.org/systems/CU-NI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 33 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 3 |
| formation | 1 |
| mixing / partial | 3 |
| activity / EMF / Gibbs energy | 28 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuNi-07Tur.tdb | M.A. Turchanin, P.G. Agraval, A.R. Abdulov, Powder Metall. Met. Ceram., 46, 467-77(2007). [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9) | `10031ba89321cab1e44115d6fa90ffa375b8daa4c4ee8d4c0bf0b9f027b1c488` | [viewer](https://orchid-project.org/phase-diagrams/#CU-NI/CuNi-07Tur.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuNi-07Tur.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuNi-07Tur.json) |
| CuNi-87Jan.tdb | A. Jansson, TRITA-MAC 340, KTH, Stockholm 1987. | `c378a4dea0f2dadf130df3dbfd46ff643d92c32242bb19a0a743b2d29d1f2d59` | [viewer](https://orchid-project.org/phase-diagrams/#CU-NI/CuNi-87Jan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuNi-87Jan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuNi-87Jan.json) |
| CuNi-89Sri.tdb | S. Srikanth, K.T. Jacob, Mater. Sci. Technol., 5, 427-34(1989). [doi:10.1179/mst.1989.5.5.427](https://doi.org/10.1179/mst.1989.5.5.427) | `39b018ea8c7d3c13c313c0275c736b6516c8bfc5c0d2efaf0cf5b4a3963fc3f7` | [viewer](https://orchid-project.org/phase-diagrams/#CU-NI/CuNi-89Sri.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuNi-89Sri.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuNi-89Sri.json) |
| CuNi-92Mey-LB.tdb | S. an Mey, Calphad 16, 255-60(1992). | `7e52adda858e302168ae26b5abfe17f4726ccbfaaff0880abcad5b38e3f559e1` | [viewer](https://orchid-project.org/phase-diagrams/#CU-NI/CuNi-92Mey-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuNi-92Mey-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuNi-92Mey-LB.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-NI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-NI.json) · [CALPHAD hull CuNi-87Jan](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-NI--CuNi-87Jan.json) · [CALPHAD hull CuNi-89Sri](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-NI--CuNi-89Sri.json) · [CALPHAD hull CuNi-92Mey-LB](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-NI--CuNi-92Mey-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–Ni system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1386 | peritectic |  | model | [1] Turchanin 2007 | p. 10 | “The peritectic temperature that we calculated is 1386 K, which practically coincides with the data from \[27, 28\].” |
| 1385 | peritectic |  | experimental | [1] Turchanin 2007; _cites ref. 27_ | p. 5 | “The peritectic temperature of 1385 K found in \[27\] completely agrees with the value from \[28\].” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cu–Ni system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | 2.26 kJ/mol (basis unstated) | 1000 | experimental |  |  | [2] Srikanth 1989 | p. 2 | “Kubaschewski et al.ll obtained a value of 2260 J mol-1 for the enthalpy of formation of equiatomic Cu-Ni solution at 1000 K by means of an adiabatic reaction calorimeter.” |

## Other properties

### Phase transition (3)

Table: Phase transition, Cu–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 690 K | 690 | other | model | [2] Srikanth 1989 | p. 9 | “The critical point in the present evaluation is located at XNi = 0·67 and T;; = 690 K.” |
| Phase transition | 698 K | 698 | other | model | [1] Turchanin 2007 | p. 9 | “According to our calculations, this is a peritectoid transformation that occurs at 698 K.” |
| Phase transition | 714 K | 714 |  | model | [1] Turchanin 2007; _cites ref. 12_ | p. 7 | “In particular, the transformation temperature is 714 K, as reported in \[12\].” |

### Mixing / partial (3)

Table: Mixing / partial, Cu–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 1.59 kJ/mol (basis unstated) | 1113 |  | experimental | [2] Srikanth 1989; _cites ref. 10_ | p. 2 | “Oriani and Murphy10 used a differential solution calorimeter using liquid tin as the solvent to measure enthalpy of mixing in solid Cu-Ni alloys at 1113 K. Their study gives a maximum value of 1590 J mol-1 at XNi '" 0·7.” |
| Enthalpy of mixing; _printed: ~Hmax_ | 8 kJ/mol (basis unstated) | 1773 |  | experimental | [2] Srikanth 1989; _cites EL'KHASAN 1966_ | p. 7 | “El'Khasan et ai.39 report high exothermic values for the enthalpy of mixing (~Hmax= 8 kJ mol-1) at 1773 K and their results are not compatible with other calorimetric studies.” |
| Partial enthalpy; _printed: ∞ ΔH Co_ | 42 kJ/mol (basis unstated) ± 2.4 | 1385 |  | experimental | [1] Turchanin 2007; _cites ref. 19_ | p. 2 | “The above results are in agreement with \[19\], which established the first enthalpy of cobalt mixing ∞ ΔH Co = 42.0 ± 2.4 kJ/mole at 1385 K using a high-temperature Tian-Calvet calorimeter.” |

### Activity / EMF / Gibbs energy (28)

Table: Activity / EMF / Gibbs energy, Cu–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity Cu; _printed: aCu_ | 0.5141 1 | 1000 | UNKNOWN; _alloy: Cu 0.2, Ni 0.8_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 8 |  |
| Activity Cu; _printed: aCu_ | 0.7926 1 | 1000 | UNKNOWN; _alloy: Cu 0.7, Ni 0.3_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 3 |  |
| Activity Cu; _printed: aCu_ | 0.8463 1 | 1000 | UNKNOWN; _alloy: Cu 0.8, Ni 0.2_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 2 |  |
| Activity Cu; _printed: aCu_ | 0.9128 1 | 1000 | UNKNOWN; _alloy: Cu 0.9, Ni 0.1_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 1 |  |
| Activity Cu; _printed: aCu_ | 0.5873 1 | 1000 | UNKNOWN; _alloy: Cu 0.3, Ni 0.7_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 7 |  |
| Activity Cu; _printed: aCu_ | 0.6391 1 | 1000 | UNKNOWN; _alloy: Cu 0.4, Ni 0.6_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 6 |  |
| Activity Cu; _printed: aCu_ | 0.3649 1 | 1000 | UNKNOWN; _alloy: Cu 0.1, Ni 0.9_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 9 |  |
| Activity Cu; _printed: aCu_ | 0.6856 1 | 1000 | UNKNOWN; _alloy: Cu 0.5, Ni 0.5_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 5 |  |
| Activity Cu; _printed: aCu_ | 0.7376 1 | 1000 | UNKNOWN; _alloy: Cu 0.6, Ni 0.4_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 4 |  |
| Activity Ni; _printed: aNi_ | 0.8686 1 | 1000 | UNKNOWN; _alloy: Cu 0.2, Ni 0.8_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 8 |  |
| Activity Ni; _printed: aNi_ | 0.5985 1 | 1000 | UNKNOWN; _alloy: Cu 0.7, Ni 0.3_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 3 |  |
| Activity Ni; _printed: aNi_ | 0.4894 1 | 1000 | UNKNOWN; _alloy: Cu 0.8, Ni 0.2_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 2 |  |
| Activity Ni; _printed: aNi_ | 0.3103 1 | 1000 | UNKNOWN; _alloy: Cu 0.9, Ni 0.1_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 1 |  |
| Activity Ni; _printed: aNi_ | 0.8322 1 | 1000 | UNKNOWN; _alloy: Cu 0.3, Ni 0.7_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 7 |  |
| Activity Ni; _printed: aNi_ | 0.7953 1 | 1000 | UNKNOWN; _alloy: Cu 0.4, Ni 0.6_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 6 |  |
| Activity Ni; _printed: aNi_ | 0.9185 1 | 1000 | UNKNOWN; _alloy: Cu 0.1, Ni 0.9_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 9 |  |
| Activity Ni; _printed: aNi_ | 0.7506 1 | 1000 | UNKNOWN; _alloy: Cu 0.5, Ni 0.5_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 5 |  |
| Activity Ni; _printed: aNi_ | 0.6856 1 | 1000 | UNKNOWN; _alloy: Cu 0.6, Ni 0.4_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 4 |  |
| EMF; _printed: E_ | 6.1 mV | 1000 | UNKNOWN; _alloy: Cu 0.2, Ni 0.8_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 8 |  |
| EMF; _printed: E_ | 22.1 mV | 1000 | UNKNOWN; _alloy: Cu 0.7, Ni 0.3_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 3 |  |
| EMF; _printed: E_ | 30.8 mV | 1000 | UNKNOWN; _alloy: Cu 0.8, Ni 0.2_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 2 |  |
| EMF; _printed: E_ | 50.5 mV | 1000 | UNKNOWN; _alloy: Cu 0.9, Ni 0.1_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 1 |  |
| EMF; _printed: E_ | 7.9 mV | 1000 | UNKNOWN; _alloy: Cu 0.3, Ni 0.7_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 7 |  |
| EMF; _printed: E_ | 9.9 mV | 1000 | UNKNOWN; _alloy: Cu 0.4, Ni 0.6_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 6 |  |
| EMF; _printed: E_ | 3.7 mV | 1000 | UNKNOWN; _alloy: Cu 0.1, Ni 0.9_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 9 |  |
| EMF; _printed: E_ | 12.4 mV | 1000 | UNKNOWN; _alloy: Cu 0.5, Ni 0.5_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 5 |  |
| EMF; _printed: E_ | 16.3 mV | 1000 | UNKNOWN; _alloy: Cu 0.6, Ni 0.4_ | experimental | [2] Srikanth 1989 | Table 1, p. 4, row 4 |  |
| Gibbs energy; _printed: ΔfG°(CuI) - ΔfG°(0.5NiI2)_ | 39 kJ mol-1 | 1000 |  | experimental | [2] Srikanth 1989; _cites KUBASCHEWSKI 1979_ | p. 6 | “Since the standard Gibbs' energies of formation of CuI and 0'5NiI2 differ by only 39 kJ mol-1 (Ref. 30) at 1000 K, it is possible that their measurements may be affected by the displacement reaction Ni(alloy) + 2Cu + ~ Nj2+ + 2Cu(alloy)” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. A. Turchanin, P. G. Agraval, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. V. Copper-cobalt system, Powder Metall Met Ceram 46, 77-89 (2007). [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9)
2. S. Srikanth, K. T. Jacob, Thermodynamic properties of Cu–Ni alloys: measurements and assessment, Materials Science and Technology 5, 427-434 (1989). [doi:10.1179/mst.1989.5.5.427](https://doi.org/10.1179/mst.1989.5.5.427)

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
