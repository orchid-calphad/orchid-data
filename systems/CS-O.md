# Cs–O system

> Cs–O system: 256 accepted literature values (heat capacity / entropy / enthalpy 100, formation 74, crystal structure 68, phase transition 11) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CS-O.html · Markdown: https://data.orchid-project.org/systems/CS-O.md

256 accepted literature values from 1 paper(s) (experimental 63, model 67, DFT 102, unspecified 24); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CS-O.json) · [CSV](https://data.orchid-project.org/systems/CS-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CS-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CS-O/CsO-15Gue.json) · [phases (15)](https://data.orchid-project.org/phases/pages/CS-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CS-O.html) · [Markdown](https://data.orchid-project.org/systems/CS-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 63 |
| model | 67 |
| DFT | 102 |
| unspecified | 24 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 11 |
| formation | 74 |
| heat capacity / entropy / enthalpy | 100 |
| crystal structure | 68 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CsO-15Gue.tdb | C. Gueneau, J.-L. Fleche, Calphad, 49, 67-78(2015). [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002) | `5219d7e34c2f9d747da82c88e4744644fccf0b1155da2778af483725a55b4ebe` | [viewer](https://orchid-project.org/phase-diagrams/#CS-O/CsO-15Gue.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CsO-15Gue.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CsO-15Gue.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CsO-15Gue.tdb | 325.17 | ION (x(O) 0.19439) + CS4O (x(O) 0.2) + CS3O (x(O) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CS/CS-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CS/CS-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cs–O system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 271 | eutectic: liquid = Cs bcc + Cs7O |  | experimental | [1] Guéneau 2015; _cites Brauer 1947_ [doi](https://doi.org/10.1002/zaac.19472550110) | p. 2 | “In the Cs-Cs2O part, an eutectic reaction (liquid1⁄4 Cs bccþ Cs7O) was measured by Brauer \[10\] at 271 K and the compound Cs7O was found to melt congruently at 276 K.” |
| 262.7 | peritectic: Cs7O2 = Cs7O + Cs3O |  | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | p. 2 | “Their observation of a transition at 262.7 K between 20 and 25 at% O implies that Cs7O2 decomposes by a peritectic reaction into Cs7O and Cs3O.” |
| 262 | eutectic: liquid = Cs7O + Cs4O |  | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | p. 2 | “An eutectic reaction (liquid1⁄4Cs7OþCs4O) was measured by Knights and Phillips \[11\] at 262 K.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cs–O system (74)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Cs2O |  | -122.367 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 10 |  |
| Cs2O |  | -117.4 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 12 |  |
| Cs2O |  | -116.933 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 11 |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -116.133 kJ/mol-atom | 298.15 | experimental | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 18 |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | unspecified | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 16 |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | model | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015 | Table 5, p. 7, row 19 |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | unspecified | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 14 |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | model | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15 |  |
| Cs2O | [Cs2O](https://data.orchid-project.org/compounds/Cs2O.html) | -115.333 kJ/mol-atom | 298.15 | experimental | -114.685 (mp-aaaaalvg) | -107.286 (oqmd-1343720) | [1] Guéneau 2015; _cites Settle 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990179-7) | Table 5, p. 7, row 17 |  |
| Cs2O2 |  | -131.025 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 21 |  |
| Cs2O2 |  | -129.05 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 22 |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -124.4 kJ/mol-atom | 298.15 | unspecified | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 25 |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -110 kJ/mol-atom | 298.15 | model | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24 |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -110 kJ/mol-atom | 298.15 | unspecified | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 23 |  |
| Cs2O2 |  | -97.95 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 20 |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -97.5 kJ/mol-atom | 298.15 | model | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015 | Table 5, p. 7, row 27 |  |
| Cs2O2 | [CsO](https://data.orchid-project.org/compounds/CsO.html) | -96.625 kJ/mol-atom | 298.15 | experimental | -118.726 (mp-aaaaalrs) | -117.021 (oqmd-4779) | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 26 |  |
| Cs3O |  | -92.575 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 8 |  |
| Cs3O | [Cs3O](https://data.orchid-project.org/compounds/Cs3O.html) | -85.475 kJ/mol-atom | 298.15 | model | -89.555 (mp-aaabdavm) | -85.555 (oqmd-2013713) | [1] Guéneau 2015 | Table 5, p. 7, row 9 |  |
| Cs3O |  | -74.125 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 7 |  |
| Cs4O |  | -67.84 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 4 |  |
| Cs4O |  | -59.64 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 3 |  |
| Cs7O | [Cs7O](https://data.orchid-project.org/compounds/Cs7O.html) | -42.5625 kJ/mol-atom | 298.15 | model | -44.374 (mp-aaabfyzf) | -43.119 (oqmd-1632) | [1] Guéneau 2015 | Table 5, p. 7, row 2 |  |
| Cs7O |  | -37.475 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 1 |  |
| Cs7O2 |  | -75.8111 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 6 |  |
| Cs7O2 |  | -64 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 5 |  |
| CsO2 |  | -129.533 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 29 |  |
| CsO2 |  | -117.067 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 30 |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -95.4 kJ/mol-atom | 298.15 | model | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32 |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -95.4 kJ/mol-atom | 298.15 | unspecified | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 33 |  |
| CsO2 |  | -84.2667 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 28 |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -80.4667 kJ/mol-atom | 298.15 | model | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015 | Table 5, p. 7, row 35 |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -78.3 kJ/mol-atom | 298.15 | experimental | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 34 |  |
| CsO2 | [CsO2](https://data.orchid-project.org/compounds/CsO2.html) | -77.7 kJ/mol-atom | 298.15 | unspecified | -94.541 (mp-aaaaacdl) | -103.292 (oqmd-6963) | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 31 |  |
| CsO3 |  | -71 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 36 |  |
| CsO3 | [CsO3](https://data.orchid-project.org/compounds/CsO3.html) | -68.15 kJ/mol-atom | 298.15 | model | -62.92 (mp-aaacprqh) | -84.786 (oqmd-6357) | [1] Guéneau 2015 | Table 5, p. 7, row 38 |  |
| CsO3 |  | -50.175 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 37 |  |
| UNKNOWN |  | -682.3 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 6 |  |
| UNKNOWN |  | -576 kJ/mol (basis unstated) | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 5 |  |
| UNKNOWN |  | -131.025 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 21 |  |
| UNKNOWN |  | -129.533 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 29 |  |
| UNKNOWN |  | -129.05 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 22 |  |
| UNKNOWN |  | -124.4 kJ/mol-atom | 298.15 | unspecified |  |  | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 25 |  |
| UNKNOWN |  | -122.367 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 10 |  |
| UNKNOWN |  | -117.4 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 12 |  |
| UNKNOWN |  | -117.067 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Brillant 2009_ | Table 5, p. 7, row 30 |  |
| UNKNOWN |  | -116.933 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 11 |  |
| UNKNOWN |  | -116.133 kJ/mol-atom | 298.15 | experimental |  |  | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 18 |  |
| UNKNOWN |  | -115.333 kJ/mol-atom | 298.15 | unspecified |  |  | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 16 |  |
| UNKNOWN |  | -115.333 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 19 |  |
| UNKNOWN |  | -115.333 kJ/mol-atom | 298.15 | unspecified |  |  | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 14 |  |
| UNKNOWN |  | -115.333 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15 |  |
| UNKNOWN |  | -115.333 kJ/mol-atom | 298.15 | experimental |  |  | [1] Guéneau 2015; _cites Settle 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990179-7) | Table 5, p. 7, row 17 |  |
| UNKNOWN |  | -110 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24 |  |
| UNKNOWN |  | -110 kJ/mol-atom | 298.15 | unspecified |  |  | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 23 |  |
| UNKNOWN |  | -97.95 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 20 |  |
| UNKNOWN |  | -97.5 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 27 |  |
| UNKNOWN |  | -96.625 kJ/mol-atom | 298.15 | experimental |  |  | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 26 |  |
| UNKNOWN |  | -95.4 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32 |  |
| UNKNOWN |  | -95.4 kJ/mol-atom | 298.15 | unspecified |  |  | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 33 |  |
| UNKNOWN |  | -92.575 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 8 |  |
| UNKNOWN |  | -85.475 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 9 |  |
| UNKNOWN |  | -84.2667 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 28 |  |
| UNKNOWN |  | -80.4667 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 35 |  |
| UNKNOWN |  | -78.3 kJ/mol-atom | 298.15 | experimental |  |  | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 34 |  |
| UNKNOWN |  | -77.7 kJ/mol-atom | 298.15 | unspecified |  |  | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 31 |  |
| UNKNOWN |  | -74.125 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 7 |  |
| UNKNOWN |  | -71 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 36 |  |
| UNKNOWN |  | -68.15 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 38 |  |
| UNKNOWN |  | -67.84 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 4 |  |
| UNKNOWN |  | -59.64 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 3 |  |
| UNKNOWN |  | -50.175 kJ/mol-atom | 0 | DFT |  |  | [1] Guéneau 2015; _cites Jain 2010_ [doi](https://doi.org/10.1016/j.ces.2010.01.024) | Table 5, p. 7, row 37 |  |
| UNKNOWN |  | -42.5625 kJ/mol-atom | 298.15 | model |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 2 |  |
| UNKNOWN |  | -37.475 kJ/mol-atom | 298.15 | DFT |  |  | [1] Guéneau 2015 | Table 5, p. 7, row 1 |  |

## Other properties

### Phase transition (11)

Table: Phase transition, Cs–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 276 K | 276 | congruent transformation | experimental | [1] Guéneau 2015; _cites Brauer 1947_ [doi](https://doi.org/10.1002/zaac.19472550110) | p. 2 | “In the Cs-Cs2O part, an eutectic reaction (liquid1⁄4 Cs bccþ Cs7O) was measured by Brauer \[10\] at 271 K and the compound Cs7O was found to melt congruently at 276 K.” |
| Phase transition | 300 K | 300 |  | model | [1] Guéneau 2015; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | p. 5 | “In case of cesium with a low melting point at 300 K, the SGTE function from Dinsdale \[36\] used in our CALPHAD model is valid for T4 200 K.” |
| Phase transition | 326 K | 326 | Cs4O = liquid + Cs3O | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | p. 2 | “Cs4O was found to decompose at 326 K into liquid and Cs3O.” |
| Phase transition | 343 K | 343 | other | experimental | [1] Guéneau 2015; _cites Cordfunke 1990_ | p. 2 | “The largest uncertainties were on both the melting point of Cs2O2 (863 K) and the decomposition of CsO3 (343 K), which were reported on the phase diagrams successively by Knights and Phillips \[11\], Cordfunke and Konings \[8\].” |
| Phase transition | 437 K | 437 | Cs3O = liquid + Cs2O | experimental | [1] Guéneau 2015 | p. 2 | “And Cs3O was observed to decompose into liquid and Cs2O at 437 K.” |
| Phase transition | 705 K | 705 | CsO2 | experimental | [1] Guéneau 2015; _cites Blumenthal 1933_ | p. 2 | “The melting point of CsO2 was estimated at 705 K by Blumenthal and Centerszwer \[12\] and later reported as 723 K by Vol'nov \[13\].” |
| Phase transition | 723 K | 723 | CsO2 | experimental | [1] Guéneau 2015; _cites Volnov 1967_ | p. 2 | “The melting point of CsO2 was estimated at 705 K by Blumenthal and Centerszwer \[12\] and later reported as 723 K by Vol'nov \[13\].” |
| Phase transition | 723 K | 723 | CsO2 | experimental | [1] Guéneau 2015; _cites Volnov 1967_ | p. 2 | “CsO2 was observed to start to melt at 723 K in agreement with Vol'nov \[13\].” |
| Phase transition | 768 K | 768 | Cs2O | experimental | [1] Guéneau 2015; _cites Touzain 1976_ [doi](https://doi.org/10.1007/bf01909410) | p. 2 | “The melting point of Cs2O was found at 768 K by Touzain \[14\] using DTA.” |
| Phase transition | 863 K | 863 |  | experimental | [1] Guéneau 2015 | p. 8 | “In the assessment, it was not possible to reproduce the melting point of Cs2O2 (863 K).” |
| Phase transition | 863 K | 863 | Cs2O2 | experimental | [1] Guéneau 2015; _cites Cordfunke 1990_ | p. 2 | “The largest uncertainties were on both the melting point of Cs2O2 (863 K) and the decomposition of CsO3 (343 K), which were reported on the phase diagrams successively by Knights and Phillips \[11\], Cordfunke and Konings \[8\].” |

### Heat capacity / entropy / enthalpy (100)

Table: Heat capacity / entropy / enthalpy, Cs–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 16 |  |
| Entropy; _printed: S0 298.15 K_ | 38.2 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 18 |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 19 |  |
| Entropy; _printed: S0 298.15 K_ | 52.4333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 10 |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 14 |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Flotow 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990256-0) | Table 5, p. 7, row 13 |  |
| Entropy; _printed: S0 298.15 K_ | 48.9667 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15 |  |
| Entropy; _printed: S0 298.15 K_ | 48.9 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Settle 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990179-7) | Table 5, p. 7, row 17 |  |
| Entropy; _printed: S0 298.15 K_ | 45 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24 |  |
| Entropy; _printed: S0 298.15 K_ | 36.075 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 25 |  |
| Entropy; _printed: S0 298.15 K_ | 53.85 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 27 |  |
| Entropy; _printed: S0 298.15 K_ | 43.4 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 23 |  |
| Entropy; _printed: S0 298.15 K_ | 53.325 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 26 |  |
| Entropy; _printed: S0 298.15 K_ | 40.925 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 20 |  |
| Entropy; _printed: S0 298.15 K_ | 65.45 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 9 |  |
| Entropy; _printed: S0 298.15 K_ | 59.25 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 7 |  |
| Entropy; _printed: S0 298.15 K_ | 60.86 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 3 |  |
| Entropy; _printed: S0 298.15 K_ | 72.84 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 4 |  |
| Entropy; _printed: S0 298.15 K_ | 78.075 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 2 |  |
| Entropy; _printed: S0 298.15 K_ | 77.1625 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 1 |  |
| Entropy; _printed: S0 298.15 K_ | 69.0444 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 6 |  |
| Entropy; _printed: S0 298.15 K_ | 60.5556 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5 |  |
| Entropy; _printed: S0 298.15 K_ | 57.0667 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 34 |  |
| Entropy; _printed: S0 298.15 K_ | 54.4 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 35 |  |
| Entropy; _printed: S0 298.15 K_ | 47.3333 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32 |  |
| Entropy; _printed: S0 298.15 K_ | 49.1667 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 28 |  |
| Entropy; _printed: S0 298.15 K_ | 46.6 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 33 |  |
| Entropy; _printed: S0 298.15 K_ | 45.5 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 31 |  |
| Entropy; _printed: S0 298.15 K_ | 36.175 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 36 |  |
| Entropy; _printed: S0 298.15 K_ | 42.15 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 38 |  |
| Entropy; _printed: S0_ | 48.9667 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 16 |  |
| Entropy; _printed: S0_ | 38.2 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 18 |  |
| Entropy; _printed: S0_ | 45 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24 |  |
| Entropy; _printed: S0_ | 36.075 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 25 |  |
| Entropy; _printed: S0_ | 48.9667 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 19 |  |
| Entropy; _printed: S0_ | 621.4 J/mol (basis unstated)/K | 298.15 | UNKNOWN | model | [1] Guéneau 2015 | Table 5, p. 7, row 6 |  |
| Entropy; _printed: S0_ | 57.0667 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 34 |  |
| Entropy; _printed: S0_ | 78.075 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.125_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 2 |  |
| Entropy; _printed: S0_ | 54.4 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 35 |  |
| Entropy; _printed: S0_ | 52.4333 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 10 |  |
| Entropy; _printed: S0_ | 47.3333 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32 |  |
| Entropy; _printed: S0_ | 60.86 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 3 |  |
| Entropy; _printed: S0_ | 48.9667 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 14 |  |
| Entropy; _printed: S0_ | 48.9667 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Flotow 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990256-0) | Table 5, p. 7, row 13 |  |
| Entropy; _printed: S0_ | 53.85 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 27 |  |
| Entropy; _printed: S0_ | 77.1625 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 1 |  |
| Entropy; _printed: S0_ | 65.45 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.25_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 9 |  |
| Entropy; _printed: S0_ | 43.4 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 23 |  |
| Entropy; _printed: S0_ | 36.175 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 36 |  |
| Entropy; _printed: S0_ | 48.9667 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15 |  |
| Entropy; _printed: S0_ | 53.325 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Knights 1979_ [doi](https://doi.org/10.1016/0022-3115%2879%2990163-6) | Table 5, p. 7, row 26 |  |
| Entropy; _printed: S0_ | 49.1667 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 28 |  |
| Entropy; _printed: S0_ | 545 J/mol (basis unstated)/K | 298.15 | UNKNOWN | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5 |  |
| Entropy; _printed: S0_ | 46.6 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | unspecified | [1] Guéneau 2015; _cites Lamoreaux 1984_ [doi](https://doi.org/10.1063/1.555706) | Table 5, p. 7, row 33 |  |
| Entropy; _printed: S0_ | 59.25 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 7 |  |
| Entropy; _printed: S0_ | 40.925 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 20 |  |
| Entropy; _printed: S0_ | 48.9 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Settle 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990179-7) | Table 5, p. 7, row 17 |  |
| Entropy; _printed: S0_ | 42.15 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.75_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 38 |  |
| Entropy; _printed: S0_ | 72.84 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.2_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 4 |  |
| Entropy; _printed: S0_ | 45.5 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | unspecified | [1] Guéneau 2015; _cites Cordfunke 1990_ | Table 5, p. 7, row 31 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.2333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 19 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 24.9333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 10 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.3333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Flotow 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990256-0) | Table 5, p. 7, row 13 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.3333 J/mol-atom/K | 298.15 | Cs2O; _alloy: O 0.333333_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 23.75 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 23.375 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 27 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 27.75 J/mol-atom/K | 298.15 | Cs2O2; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 20 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.675 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 9 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.7 J/mol-atom/K | 298.15 | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 7 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 27.28 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 3 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.74 J/mol-atom/K | 298.15 | Cs4O; _alloy: O 0.2_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 4 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.3 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 2 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.3125 J/mol-atom/K | 298.15 | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 1 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.6778 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 6 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 25.6889 J/mol-atom/K | 298.15 | Cs7O2; _alloy: O 0.222222_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 22.8167 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 35 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 26.3 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 22.7333 J/mol-atom/K | 298.15 | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 28 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 21.075 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 36 |  |
| Heat capacity; _printed: Cp0 298.15 K_ | 21.05 J/mol-atom/K | 298.15 | CsO3; _alloy: O 0.75_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 38 |  |
| Heat capacity; _printed: Cp0_ | 23.75 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 24 |  |
| Heat capacity; _printed: Cp0_ | 25.2333 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 19 |  |
| Heat capacity; _printed: Cp0_ | 231.1 J/mol (basis unstated)/K | 298.15 | UNKNOWN | model | [1] Guéneau 2015 | Table 5, p. 7, row 6 |  |
| Heat capacity; _printed: Cp0_ | 26.3 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.125_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 2 |  |
| Heat capacity; _printed: Cp0_ | 22.8167 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 35 |  |
| Heat capacity; _printed: Cp0_ | 24.9333 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 10 |  |
| Heat capacity; _printed: Cp0_ | 26.3 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 32 |  |
| Heat capacity; _printed: Cp0_ | 27.28 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 3 |  |
| Heat capacity; _printed: Cp0_ | 25.3333 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Flotow 1974_ [doi](https://doi.org/10.1016/0021-9614%2874%2990256-0) | Table 5, p. 7, row 13 |  |
| Heat capacity; _printed: Cp0_ | 23.375 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 27 |  |
| Heat capacity; _printed: Cp0_ | 26.3125 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 1 |  |
| Heat capacity; _printed: Cp0_ | 25.675 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.25_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 9 |  |
| Heat capacity; _printed: Cp0_ | 21.075 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 36 |  |
| Heat capacity; _printed: Cp0_ | 25.3333 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.333333_ | model | [1] Guéneau 2015; _cites SGTE_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 5, p. 7, row 15 |  |
| Heat capacity; _printed: Cp0_ | 22.7333 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 28 |  |
| Heat capacity; _printed: Cp0_ | 231.2 J/mol (basis unstated)/K | 298.15 | UNKNOWN | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 5 |  |
| Heat capacity; _printed: Cp0_ | 26.7 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 7 |  |
| Heat capacity; _printed: Cp0_ | 27.75 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 5, p. 7, row 20 |  |
| Heat capacity; _printed: Cp0_ | 21.05 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.75_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 38 |  |
| Heat capacity; _printed: Cp0_ | 25.74 J/mol-atom/K | 298.15 | UNKNOWN; _alloy: O 0.2_ | model | [1] Guéneau 2015 | Table 5, p. 7, row 4 |  |

### Crystal structure (68)

Table: Crystal structure, Cs–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 17.88 Å |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6 |  |
| Lattice a | 4.33 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 10 |  |
| Lattice a | 4.232 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 11 |  |
| Lattice a | 8.899 Å |  | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 8 |  |
| Lattice a | 16.414 Å |  | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 2 |  |
| Lattice a | 4.46 Å |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13 |  |
| Lattice a | 9.031 Å |  | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 15 |  |
| Lattice a | 6.836 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18 |  |
| Lattice a | 7.008 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17 |  |
| Lattice a | 17.027 Å |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4 |  |
| Lattice a | 17.61 Å | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5 |  |
| Lattice a | 4.269 Å | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 9 |  |
| Lattice a | 8.78 Å | 298.15 | Cs3O; _alloy: O 0.25_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 7 |  |
| Lattice a | 16.393 Å | 298.15 | Cs7O; _alloy: O 0.125_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 1 |  |
| Lattice a | 4.322 Å | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12 |  |
| Lattice a | 8.924 Å | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 14 |  |
| Lattice a | 6.709 Å | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16 |  |
| Lattice a | 16.833 Å | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3 |  |
| Lattice b | 9.377 Å |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6 |  |
| Lattice b | 7.644 Å |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13 |  |
| Lattice b | 6.358 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18 |  |
| Lattice b | 6.556 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17 |  |
| Lattice b | 20.882 Å |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4 |  |
| Lattice b | 9.218 Å | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5 |  |
| Lattice b | 7.517 Å | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12 |  |
| Lattice b | 6.244 Å | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16 |  |
| Lattice b | 20.569 Å | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3 |  |
| Lattice c | 24.466 Å |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6 |  |
| Lattice c | 22.491 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 10 |  |
| Lattice c | 18.74 Å |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 11 |  |
| Lattice c | 7.627 Å |  | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 8 |  |
| Lattice c | 9.357 Å |  | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 2 |  |
| Lattice c | 6.495 Å |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13 |  |
| Lattice c | 14.906 Å |  | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 15 |  |
| Lattice c | 9.231 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18 |  |
| Lattice c | 9.42 Å |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17 |  |
| Lattice c | 12.643 Å |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4 |  |
| Lattice c | 24.047 Å | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5 |  |
| Lattice c | 18.82 Å | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 9 |  |
| Lattice c | 7.52 Å | 298.15 | Cs3O; _alloy: O 0.25_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 7 |  |
| Lattice c | 9.193 Å | 298.15 | Cs7O; _alloy: O 0.125_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 1 |  |
| Lattice c | 6.43 Å | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12 |  |
| Lattice c | 14.652 Å | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 14 |  |
| Lattice c | 8.997 Å | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16 |  |
| Lattice c | 12.4 Å | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3 |  |
| lattice beta | 100.29 not_printed |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6 |  |
| lattice beta | 122.41 not_printed |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18 |  |
| lattice beta | 123.61 not_printed |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17 |  |
| lattice beta | 100.14 not_printed | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5 |  |
| lattice beta | 120.85 not_printed | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16 |  |
| lattice v | 4035.98 Å³ |  | Cs11O3; _alloy: O 0.214286_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 6 |  |
| lattice v | 365.2 Å³ |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 10 |  |
| lattice v | 290.57 Å³ |  | Cs2O; _alloy: O 0.333333_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 11 |  |
| lattice v | 523.17 Å³ |  | Cs3O; _alloy: O 0.25_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 8 |  |
| lattice v | 2183.46 Å³ |  | Cs7O; _alloy: O 0.125_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 2 |  |
| lattice v | 221.43 Å³ |  | CsO; _alloy: O 0.5_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 13 |  |
| lattice v | 1215.72 Å³ |  | CsO2; _alloy: O 0.666667_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 15 |  |
| lattice v | 338.7 Å³ |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 18 |  |
| lattice v | 360.51 Å³ |  | CsO3; _alloy: O 0.75_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 17 |  |
| lattice v | 4496.23 Å³ |  | UNKNOWN; _alloy: O 0.2_ | DFT | [1] Guéneau 2015 | Table 2, p. 4, row 4 |  |
| lattice v | 3842.55 Å³ | 298.15 | Cs11O3; _alloy: O 0.214286_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 5 |  |
| lattice v | 297.03 Å³ | 298.15 | Cs2O; _alloy: O 0.333333_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 9 |  |
| lattice v | 502.04 Å³ | 298.15 | Cs3O; _alloy: O 0.25_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 7 |  |
| lattice v | 2139.46 Å³ | 298.15 | Cs7O; _alloy: O 0.125_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 1 |  |
| lattice v | 208.9 Å³ | 298.15 | CsO; _alloy: O 0.5_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 12 |  |
| lattice v | 1166.85 Å³ | 298.15 | CsO2; _alloy: O 0.666667_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 14 |  |
| lattice v | 323.56 Å³ | 298.15 | CsO3; _alloy: O 0.75_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 16 |  |
| lattice v | 4293.35 Å³ | 298.15 | UNKNOWN; _alloy: O 0.2_ | experimental | [1] Guéneau 2015; _cites Villars 2014_ | Table 2, p. 4, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C. Guéneau, J.-L. Flèche, Thermodynamic assessment of the cesium–oxygen system by coupling density functional theory and CALPHAD approaches, Calphad 49, 67-78 (2015). [doi:10.1016/j.calphad.2015.02.002](https://doi.org/10.1016/j.calphad.2015.02.002)

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
