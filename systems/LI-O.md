# Li–O system

> Li–O system: 24 accepted literature values (formation 9, invariant reaction 9, heat capacity / entropy / enthalpy 4, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-O.html · Markdown: https://data.orchid-project.org/systems/LI-O.md

24 accepted literature values from 1 paper(s) (experimental 12, model 12); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-O.json) · [CSV](https://data.orchid-project.org/systems/LI-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-O/LiO-11Cha.json) · [Markdown](https://data.orchid-project.org/systems/LI-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |
| phase transition | 2 |
| formation | 9 |
| heat capacity / entropy / enthalpy | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiO-11Cha.tdb | K. Chang, B. Hallstedt, Calphad, 35, 160-64(2011). [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) | `6943f8b9e741020b0a26232e445ee2b98737e8f64608bbda37a7396be76d8128` | [viewer](https://orchid-project.org/phase-diagrams/#LI-O/LiO-11Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiO-11Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiO-11Cha.tdb | 613.65 | LI2O_C1 (x(O) 0.33333) + LI2O2 (x(O) 0.5) + O2GAS (x(O) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–O system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2673 | L -> Gas | L: O 0.3333; Gas: O 0.3333 | model | [1] Chang 2011 | Table 3, p. 4, row 6 |  |
| 2600 | L -> Gas | L: O 0.3333; Gas: O 0.3333 | experimental | [1] Chang 2011; _cites Brewer 1953_ [doi](https://doi.org/10.1021/cr60161a001) | Table 3, p. 4, row 5 |  |
| 1711 | L -> Li2O | L: O 0.3333; Li2O: O 0.3333 | experimental | [1] Chang 2011; _cites Ortman 1983_ | Table 3, p. 4, row 3 |  |
| 1711 | L -> Li2O | L: O 0.3333; Li2O: O 0.3333 | model | [1] Chang 2011 | Table 3, p. 4, row 4 |  |
| 613.2 | Li2O2 -> Li2O + Gas |  | model | [1] Chang 2011 | Table 3, p. 4, row 8 |  |
| 613 | Li2O2 -> Li2O + Gas |  | experimental | [1] Chang 2011; _cites Yu 2009_ | Table 3, p. 4, row 7 |  |
| 453.6 | L -> (Li) + Li2O | L: O 2.000e-6 | experimental | [1] Chang 2011; _cites Sangster 1992_ [doi](https://doi.org/10.1007/bf02667558) | Table 3, p. 4, row 1 |  |
| 453.6 | L -> (Li) + Li2O | L: O 2.000e-6 | model | [1] Chang 2011 | Table 3, p. 4, row 2 |  |
| 453.6 | eutectic |  | experimental | [1] Chang 2011; _cites Sangster 1992_ [doi](https://doi.org/10.1007/bf02667558) | p. 1 | “Sangster and Pelton \[1\] reviewed the solubility data from Refs. \[2-5\] and reported an eutectic reaction involving (Li), Li2 O and liquid at 453.6 K with a eutectic composition of 2 × 10-4 at.% O.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Li–O system (9)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199.577 kJ/mol-atom ± 0.7 | 298.15 | model | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites This_ | Table 4, p. 5, row 4 |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199.301 kJ/mol-atom ± 0.092 | 298.15 | experimental | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites ref. 21_ | Table 4, p. 5, row 2 |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199.16 kJ/mol-atom ± 0.433333 | 298.15 | experimental | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites ref. 20_ | Table 4, p. 5, row 1 |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199 kJ/mol-atom | 298.15 | model | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011 | Table 4, p. 5, row 5 |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -198.833 kJ/mol-atom ± 0.223333 | 298.15 | experimental | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites ref. 22_ | Table 4, p. 5, row 3 |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -161.07 kJ/mol-atom | 298.15 | model | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011 | Table 4, p. 5, row 9 |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -158.155 kJ/mol-atom ± 2.1 | 298.15 | model | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011; _cites This_ | Table 4, p. 5, row 8 |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -158.155 kJ/mol-atom | 298.15 | experimental | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011; _cites ref. 28_ | Table 4, p. 5, row 7 |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -151.475 kJ/mol-atom | 298.15 | experimental | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011; _cites ref. 15_ | Table 4, p. 5, row 6 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Li–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1843 K | 1843 |  | experimental | [1] Chang 2011; _cites A 1953_ | p. 1 | “Van Arkel et al. \[7\] observed that Li2 O melts quite sharply at 1843 K.” |
| Phase transition | 1973 K | 1973 |  | model | [1] Chang 2011; _cites Conclusions 2011_ | p. 1 | “Jaeger and van Klooster \[6\] assumed that the melting point is around 1973 K because they were unable to melt Li2 O despite heating it up to 1898 K.” |

### Heat capacity / entropy / enthalpy (4)

Table: Heat capacity / entropy / enthalpy, Li–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S298.15_ | 37.89 J/mol (basis unstated)/K | 298.15 | Li2O; _alloy: O 0.333333_ | experimental | [1] Chang 2011; _cites This_ | Table 5, p. 5, row 1 |  |
| Entropy; _printed: S298.15_ | 36.5 J/mol (basis unstated)/K | 298.15 | Li2O; _alloy: O 0.333333_ | model | [1] Chang 2011 | Table 5, p. 5, row 2 |  |
| Entropy; _printed: S298.15_ | 60.83 J/mol (basis unstated)/K | 298.15 | Li2O2; _alloy: O 0.5_ | model | [1] Chang 2011 | Table 5, p. 5, row 4 |  |
| Entropy; _printed: S298.15_ | 56.484 unknown ± 4.2 | 298.15 | Li2O2; _alloy: O 0.5_ | model | [1] Chang 2011; _cites This_ | Table 5, p. 5, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011). [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
