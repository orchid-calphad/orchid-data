# Na–Sb system

> Na–Sb system: 61 accepted literature values (formation 30, phase transition 14, heat capacity / entropy / enthalpy 12, invariant reaction 5) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NA-SB.html · Markdown: https://data.orchid-project.org/systems/NA-SB.md

61 accepted literature values from 2 paper(s) (experimental 32, model 29); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/NA-SB.json) · [CSV](https://data.orchid-project.org/systems/NA-SB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NA-SB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NA-SB/NaSb-13Liu.json) · [phases (7)](https://data.orchid-project.org/phases/pages/NA-SB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NA-SB.html) · [Markdown](https://data.orchid-project.org/systems/NA-SB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 32 |
| model | 29 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 14 |
| formation | 30 |
| heat capacity / entropy / enthalpy | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NaSb-13Liu.tdb | Y. Liu, J. Xu, Z. Kang, J. Wang, Thermochim. Acta, 569, 119-26(2013). [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) | `35a80346e37417b2fe1442e0cd7a587a6a7cb3ae875da4a68fa196b95c200c48` | [viewer](https://orchid-project.org/phase-diagrams/#NA-SB/NaSb-13Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaSb-13Liu.json) |
| NaSb-17Dre.tdb | L. Dreval, M. Zschornak, W. Muenchgesang, O. Fabrichnaya, D. Rafaja, M.L. Martine, L. Giebeler, M. Motylenko, J. Alloys Compd., 695, 1725-42(2017). [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) | `b4cfe0c128f39fbc7ccc8abc05b0637258cbe77f32c8c1c9b7c8c63a8070a228` | [viewer](https://orchid-project.org/phase-diagrams/#NA-SB/NaSb-17Dre.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaSb-17Dre.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NaSb-13Liu.tdb | 710.44 | NA3SB_D018 (x(Sb) 0.25) + LIQUID (x(Sb) 0.44241) + NASB (x(Sb) 0.5) |
| NaSb-13Liu.tdb | 671.9 | NASB (x(Sb) 0.5) + LIQUID (x(Sb) 0.59703) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| NaSb-13Liu.tdb | 370.87 | BCC_A2 (x(Sb) 0) + LIQUID (x(Sb) 0) + NA3SB_D018 (x(Sb) 0.25) |
| NaSb-17Dre.tdb | 707.91 | NA3SB_D018 (x(Sb) 0.25) + LIQUID (x(Sb) 0.44004) + NASB (x(Sb) 0.5) |
| NaSb-17Dre.tdb | 672.97 | NASB (x(Sb) 0.5) + LIQUID (x(Sb) 0.60334) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| NaSb-17Dre.tdb | 370.87 | BCC_A2 (x(Sb) 0) + LIQUID (x(Sb) 0) + NA3SB_D018 (x(Sb) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NA/NA-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NA/NA-SB.json) · [CALPHAD hull NaSb-13Liu](https://data.orchid-project.org/hulls/calphad-sgte/NA/NA-SB--NaSb-13Liu.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Na–Sb system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 710 | liq -> Na3Sb + NaSb | liq: Sb 0.45; Na3Sb: Sb 0.25; NaSb: Sb 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 6 |  |
| 708 | liq -> Na3Sb + NaSb | liq: Sb 0.45; Na3Sb: Sb 0.25; NaSb: Sb 0.5 | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 3, p. 5, row 7 |  |
| 672 | liq -> NaSb + Sb | liq: Sb 0.6; NaSb: Sb 0.5; Sb: Sb 1 | model | [1] Liu 2013 | Table 3, p. 5, row 11 |  |
| 370.9 | liq -> Na + Na3Sb | Na3Sb: Sb 0.25 | model | [1] Liu 2013 | Table 3, p. 5, row 1 |  |
| 370.8 | liq -> Na + Na3Sb | Na3Sb: Sb 0.25 | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 3, p. 5, row 2 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Na–Sb system (18)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Na3Sb(s) | [Na3Sb](https://data.orchid-project.org/compounds/Na3Sb.html) | -58.5 kJ/mol-atom | 298.15 | experimental | -45.951 (mp-aaaaalua) | -50.428 (oqmd-5156) | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 2 |  |
| Na3Sb(s) | [Na3Sb](https://data.orchid-project.org/compounds/Na3Sb.html) | -56.75 kJ/mol-atom | 298.15 | experimental | -45.951 (mp-aaaaalua) | -50.428 (oqmd-5156) | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 3 |  |
| Na3Sb(s) | [Na3Sb](https://data.orchid-project.org/compounds/Na3Sb.html) | -56.5 kJ/mol-atom |  | model | -45.951 (mp-aaaaalua) | -50.428 (oqmd-5156) | [1] Liu 2013 | Table 2, p. 4, row 1 |  |
| Na3Sb(s) | [Na3Sb](https://data.orchid-project.org/compounds/Na3Sb.html) | -53.25 kJ/mol-atom | 298.15 | experimental | -45.951 (mp-aaaaalua) | -50.428 (oqmd-5156) | [1] Liu 2013; _cites Morozova 1959_ | Table 2, p. 4, row 4 |  |
| Na3Sb(s) | [Na3Sb](https://data.orchid-project.org/compounds/Na3Sb.html) | -49.25 kJ/mol-atom | 298.15 | experimental | -45.951 (mp-aaaaalua) | -50.428 (oqmd-5156) | [1] Liu 2013; _cites Kubaschewski 1938_ | Table 2, p. 4, row 5 |  |
| NaSb(s) | [NaSb](https://data.orchid-project.org/compounds/NaSb.html) | -37.5 kJ/mol-atom |  | model | -40.415 (mp-aaaaalto) | -37.498 (oqmd-5018) | [1] Liu 2013 | Table 2, p. 4, row 6 |  |
| NaSb(s) | [NaSb](https://data.orchid-project.org/compounds/NaSb.html) | -36 kJ/mol-atom | 298.15 | experimental | -40.415 (mp-aaaaalto) | -37.498 (oqmd-5018) | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 8 |  |
| NaSb(s) | [NaSb](https://data.orchid-project.org/compounds/NaSb.html) | -35 kJ/mol-atom | 298.15 | experimental | -40.415 (mp-aaaaalto) | -37.498 (oqmd-5018) | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 7 |  |
| NaSb(s) | [NaSb](https://data.orchid-project.org/compounds/NaSb.html) | -33 kJ/mol-atom | 298.15 | experimental | -40.415 (mp-aaaaalto) | -37.498 (oqmd-5018) | [1] Liu 2013; _cites Kubaschewski 1938_ | Table 2, p. 4, row 9 |  |
| UNKNOWN |  | -234 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 2 |  |
| UNKNOWN |  | -227 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 3 |  |
| UNKNOWN |  | -226 kJ/mol (basis unstated) |  | model |  |  | [1] Liu 2013 | Table 2, p. 4, row 1 |  |
| UNKNOWN |  | -213 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Morozova 1959_ | Table 2, p. 4, row 4 |  |
| UNKNOWN |  | -197 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Kubaschewski 1938_ | Table 2, p. 4, row 5 |  |
| UNKNOWN |  | -75 kJ/mol (basis unstated) |  | model |  |  | [1] Liu 2013 | Table 2, p. 4, row 6 |  |
| UNKNOWN |  | -72 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 8 |  |
| UNKNOWN |  | -70 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 7 |  |
| UNKNOWN |  | -66 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Kubaschewski 1938_ | Table 2, p. 4, row 9 |  |

## Other properties

### Phase transition (14)

Table: Phase transition, Na–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 723 K | 723 | NaSb | experimental | [1] Liu 2013; _cites Redslob 1982_ [doi](https://doi.org/10.1515/zna-1982-0612) | p. 2 | “In addition, the melting temperature of NaSb was also reported by Redslob et al. \[10\] as 723 K, who utilized electrical conductivity measurements.” |
| Phase transition | 723 K | 723 | congruent transformation | experimental | [2] Dreval 2017; _cites Redslob 1982_ | p. 9 | “In the course of the optimization, it also became clear that the value of 723 K reported in Ref. \[30\] for the congruent melting of NaSb compound is not reliable, since a better fit to this temperature simultaneously results in a worse description of the conjugated invariant reactions.” |
| Phase transition | 723 K | 723 | liq -> NaSb; _liq: Sb 0.5; NaSb: Sb 0.5_ | experimental | [1] Liu 2013; _cites Redslob 1982_ [doi](https://doi.org/10.1515/zna-1982-0612) | Table 3, p. 5, row 10 |  |
| Phase transition | 738 K | 738 | congruent transformation | model | [1] Liu 2013; _cites Sangster 1993_ [doi](https://doi.org/10.1007/bf02667822) | p. 1 | “According to the assessed phase diagram, two intermetallic phases can be identified, i.e. Na3 Sb and NaSb. Such two intermetallics melt congruently around 1130 and 738 K, respectively.” |
| Phase transition | 738 K | 738 | congruent transformation | experimental | [1] Liu 2013; _cites Ugai 1961_ | p. 2 | “The congruent melting temperatures of Na3 Sb and NaSb were measured by Ugai \[9\] with thermal analysis, the results of which are 1132 and 738 K, respectively.” |
| Phase transition | 738 K | 738 | liq -> NaSb; _liq: Sb 0.5; NaSb: Sb 0.5_ | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 3, p. 5, row 9 |  |
| Phase transition | 739 K | 739 | congruent transformation | model | [2] Dreval 2017 | p. 9 | “According to our calculations, the congruent melting point of the NaSb compound is 739 K, which is only by 1 K higher than the value reported in Refs. \[27,28\].” |
| Phase transition | 739 K | 739 | liq -> NaSb; _liq: Sb 0.5; NaSb: Sb 0.5_ | model | [1] Liu 2013 | Table 3, p. 5, row 8 |  |
| Phase transition | 745 K | 745 |  | model | [2] Dreval 2017; _cites Liu 2017_ | p. 9 | “The temperature calculated by Liu et al. \[10\] is equal to 745 K.” |
| Phase transition | 1130 K | 1130 | congruent transformation | model | [1] Liu 2013; _cites Sangster 1993_ [doi](https://doi.org/10.1007/bf02667822) | p. 1 | “According to the assessed phase diagram, two intermetallic phases can be identified, i.e. Na3 Sb and NaSb. Such two intermetallics melt congruently around 1130 and 738 K, respectively.” |
| Phase transition | 1130 K | 1130 | liq -> Na3Sb; _liq: Sb 0.25; Na3Sb: Sb 0.25_ | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 3, p. 5, row 4 |  |
| Phase transition | 1131 K | 1131 | liq -> Na3Sb; _liq: Sb 0.25; Na3Sb: Sb 0.25_ | model | [1] Liu 2013 | Table 3, p. 5, row 3 |  |
| Phase transition | 1132 K | 1132 | congruent transformation | experimental | [1] Liu 2013; _cites Ugai 1961_ | p. 2 | “The congruent melting temperatures of Na3 Sb and NaSb were measured by Ugai \[9\] with thermal analysis, the results of which are 1132 and 738 K, respectively.” |
| Phase transition | 1132 K | 1132 | liq -> Na3Sb; _liq: Sb 0.25; Na3Sb: Sb 0.25_ | experimental | [1] Liu 2013; _cites Ugai 1961_ | Table 3, p. 5, row 5 |  |

### Formation (12)

Table: Formation, Na–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropies of formation_ | -9.775 J/mol-atom/K |  | Na3Sb(s); _alloy: Sb 0.25_ | model | [1] Liu 2013 | Table 2, p. 4, row 1 |  |
| Entropy of formation; _printed: Entropies of formation_ | -2.315 J/mol-atom/K |  | NaSb(s); _alloy: Sb 0.5_ | model | [1] Liu 2013 | Table 2, p. 4, row 6 |  |
| Entropy of formation; _printed: Entropies of formation_ | -4.63 J/mol (basis unstated)/K |  | UNKNOWN | model | [1] Liu 2013 | Table 2, p. 4, row 6 |  |
| Entropy of formation; _printed: Entropies of formation_ | -39.1 J/mol (basis unstated)/K |  | UNKNOWN | model | [1] Liu 2013 | Table 2, p. 4, row 1 |  |
| Entropy of formation; _printed: Entropies of formation_ | -23 J/mol-atom/K | 298.15 | Na3Sb(s); _alloy: Sb 0.25_ | experimental | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 2 |  |
| Entropy of formation; _printed: Entropies of formation_ | -15 J/mol-atom/K | 298.15 | Na3Sb(s); _alloy: Sb 0.25_ | experimental | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 3 |  |
| Entropy of formation; _printed: Entropies of formation_ | -8.5 J/mol-atom/K | 298.15 | NaSb(s); _alloy: Sb 0.5_ | experimental | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 8 |  |
| Entropy of formation; _printed: Entropies of formation_ | -3.5 J/mol-atom/K | 298.15 | NaSb(s); _alloy: Sb 0.5_ | experimental | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 7 |  |
| Entropy of formation; _printed: Entropies of formation_ | -92 J/mol (basis unstated)/K | 298.15 | UNKNOWN | experimental | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 2 |  |
| Entropy of formation; _printed: Entropies of formation_ | -60 J/mol (basis unstated)/K | 298.15 | UNKNOWN | experimental | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 3 |  |
| Entropy of formation; _printed: Entropies of formation_ | -17 J/mol (basis unstated)/K | 298.15 | UNKNOWN | experimental | [1] Liu 2013; _cites Voronin 1987_ | Table 2, p. 4, row 8 |  |
| Entropy of formation; _printed: Entropies of formation_ | -7 J/mol (basis unstated)/K | 298.15 | UNKNOWN | experimental | [1] Liu 2013; _cites Voronin 1967_ | Table 2, p. 4, row 7 |  |

### Heat capacity / entropy / enthalpy (12)

Table: Heat capacity / entropy / enthalpy, Na–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Heat capacity; _printed: Cp_ | 51.9 J/mol (basis unstated)/K | 298.15 | Na3Sb; _alloy: Sb 0.25_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 1 |  |
| Heat capacity; _printed: Cp_ | 103.69 J/mol (basis unstated)/K | 298.15 | NaSb; _alloy: Sb 0.5_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 7 |  |
| Heat capacity; _printed: Cp_ | 51.94 J/mol (basis unstated)/K | 300 | Na3Sb; _alloy: Sb 0.25_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 2 |  |
| Heat capacity; _printed: Cp_ | 53.94 J/mol (basis unstated)/K | 400 | Na3Sb; _alloy: Sb 0.25_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 3 |  |
| Heat capacity; _printed: Cp_ | 105.84 J/mol (basis unstated)/K | 400 | NaSb; _alloy: Sb 0.5_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 8 |  |
| Heat capacity; _printed: Cp_ | 55.94 J/mol (basis unstated)/K | 500 | Na3Sb; _alloy: Sb 0.25_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 4 |  |
| Heat capacity; _printed: Cp_ | 57.94 J/mol (basis unstated)/K | 600 | Na3Sb; _alloy: Sb 0.25_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 5 |  |
| Heat capacity; _printed: Cp_ | 110.06 J/mol (basis unstated)/K | 600 | NaSb; _alloy: Sb 0.5_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 9 |  |
| Heat capacity; _printed: Cp_ | 59.94 J/mol (basis unstated)/K | 700 | Na3Sb; _alloy: Sb 0.25_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 6 |  |
| Heat capacity; _printed: Cp_ | 114.27 J/mol (basis unstated)/K | 800 | NaSb; _alloy: Sb 0.5_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 10 |  |
| Heat capacity; _printed: Cp_ | 118.49 J/mol (basis unstated)/K | 1000 | NaSb; _alloy: Sb 0.5_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 11 |  |
| Heat capacity; _printed: Cp_ | 120.6 J/mol (basis unstated)/K | 1100 | NaSb; _alloy: Sb 0.5_ | model | [2] Dreval 2017; _cites Thermo-calc 2015_ | Table 7, p. 11, row 12 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013). [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009)
2. Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017). [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003)

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
