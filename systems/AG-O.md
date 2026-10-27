# Ag–O system

> Ag–O system: 58 accepted literature values (model expression 19, invariant reaction 16, formation 9, heat capacity / entropy / enthalpy 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-O.html · Markdown: https://data.orchid-project.org/systems/AG-O.md

58 accepted literature values from 1 paper(s) (experimental 35, model 23); 1 calculated phase diagram(s). 9 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-O.json) · [CSV](https://data.orchid-project.org/systems/AG-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-O/AgO-97Ass-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/AG-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-O.html) · [Markdown](https://data.orchid-project.org/systems/AG-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 35 |
| model | 23 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |
| phase transition | 2 |
| formation | 9 |
| heat capacity / entropy / enthalpy | 7 |
| activity / EMF / Gibbs energy | 5 |
| model expression | 19 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgO-97Ass-LB.tdb | J. Assal, B. Hallstedt and L.J. Gauckler, J. Am. Ceram. Soc., 80, 3054-60(1997) [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) | `9f608fb28b4b4e31cd84c13d6756c0fd284a4dd09fe677a8805bdc771e6bc22d` | [viewer](https://orchid-project.org/phase-diagrams/#AG-O/AgO-97Ass-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgO-97Ass-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgO-97Ass-LB.tdb | 1211.42 | FCC_A1 (x(O) 5.700e-4) + ION (x(O) 0.02078) + GAS (x(O) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–O system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1228 | L + O2 -> Ag (in O2) | L: O 0.0204 | experimental | [1] Assal 1997; _cites Sieverts 1909_ | Table III, p. 3, row 11; `ORC-F6IUO2B5VU` |  |
| 1226 | L + O2 -> Ag (in air) | L: O 0.0097 | model | [1] Assal 1997; _cites Karakaya 1992_ [doi](https://doi.org/10.1007/bf02667476) | Table III, p. 3, row 9; `ORC-VKPKKR42WR` |  |
| 1224.2 | L + O2 -> Ag (in air) | L: O 0.00981 | model | [1] Assal 1997 | Table III, p. 3, row 10; `ORC-OH7QH2WGSY` |  |
| 1224 | L + O2 -> Ag (in air) |  | experimental | [1] Assal 1997; _cites Allen 1932_ | Table III, p. 3, row 5; `ORC-6GXPR7TBKN` |  |
| 1223 | L + O2 -> Ag (in air) | L: O 0.0087 | experimental | [1] Assal 1997; _cites Knacke 1968_ [doi](https://doi.org/10.1515/ijmr-1968-590204) | Table III, p. 3, row 8; `ORC-W4X43AJRXR` |  |
| 1223 | L + O2 -> Ag (in air) |  | experimental | [1] Assal 1997; _cites Baker 1965_ [doi](https://doi.org/10.1038/205065a0) | Table III, p. 3, row 6; `ORC-ZCXGXWZS5L` |  |
| 1219 | L + O2 -> Ag (in air) | L: O 0.0099 | experimental | [1] Assal 1997; _cites Besson 1966_ | Table III, p. 3, row 7; `ORC-FPWYQBIGR4` |  |
| 1212 | L + O2 -> Ag (in O2) | L: O 0.0209 | model | [1] Assal 1997; _cites Karakaya 1992_ [doi](https://doi.org/10.1007/bf02667476) | Table III, p. 3, row 16; `ORC-7KKXF6IX5Z` |  |
| 1212 | L + O2 -> Ag (in O2) | L: O 0.0195 | experimental | [1] Assal 1997; _cites Knacke 1968_ [doi](https://doi.org/10.1515/ijmr-1968-590204) | Table III, p. 3, row 15; `ORC-DAIJP43ORV` |  |
| 1212 | L + O2 -> Ag (in O2) | L: O 0.021 | experimental | [1] Assal 1997; _cites Shah 1967_ | Table III, p. 3, row 14; `ORC-PIS6I7MV6L` |  |
| 1211.8 | L + O2 -> Ag (in O2) | L: O 0.02053 | model | [1] Assal 1997 | Table III, p. 3, row 17; `ORC-NV662NNW2E` |  |
| 1211 | L + O2 -> Ag (in O2) |  | experimental | [1] Assal 1997; _cites Allen 1932_ | Table III, p. 3, row 12; `ORC-MJIIYEH5ZZ` |  |
| 1210 | L + O2 -> Ag (in O2) |  | experimental | [1] Assal 1997; _cites Baker 1965_ [doi](https://doi.org/10.1038/205065a0) | Table III, p. 3, row 13; `ORC-Q4E3CV2KMG` |  |
| 803.5 | eutectic: L -> Ag + Ag2O (eutectic) | L: O 0.2514 | model | [1] Assal 1997 | Table III, p. 3, row 3; `ORC-JVZSJNU2IW` |  |
| 803 | eutectic: L -> Ag + Ag2O (eutectic) | L: O 0.22 | experimental | [1] Assal 1997; _cites Baker 1968_ | Table III, p. 3, row 2; `ORC-NNER7NVWN7` |  |
| 780 | eutectic: L -> Ag + Ag2O (eutectic) |  | experimental | [1] Assal 1997; _cites Allen 1932_ | Table III, p. 3, row 1; `ORC-35Q7E7K4SK` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ag–O system (9)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ag2O |  | -31.1 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Assal 1997; _cites Kubaschewski 1993_ | Table V, p. 6, row 4; `ORC-YKHQTP4PHB` |  |
| Ag2O |  | -30.68 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 6; `ORC-B54EZ7YTTE` |  |
| Ag2O |  | -30.54 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Assal 1997; _cites Pitzer 1937_ | Table V, p. 6, row 3; `ORC-GTVWBTH2DK` |  |
| Ag2O |  | -29.99 kJ/mol (basis unstated) | 773 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 7; `ORC-CQ2UMNQX5Z.83cf17` |  |
| Ag2O |  | -29.44 kJ/mol (basis unstated) | 609.5 | model |  |  | [1] Assal 1997; _cites Pitzer 1937_ | Table V, p. 6, row 5; `ORC-YQ7XUB3RNX` |  |
| Ag2O |  | -26.53 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Assal 1997; _cites Lewis 1906_ | Table V, p. 6, row 1; `ORC-QPT5LPZO7I` |  |
| Ag2O |  | -25.81 kJ/mol (basis unstated) | 773 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 7; `ORC-CQ2UMNQX5Z.b6af84` |  |
| Ag2O |  | -25.81 kJ/mol (basis unstated) | 773 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 8; `ORC-YIERJAQR5V` |  |
| Ag2O |  | -22.6 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Assal 1997; _cites Mixter 1911_ | Table V, p. 6, row 2; `ORC-IVQPHJSZYY` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Ag–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1060 K | 1060 | Ag2O | model | [1] Assal 1997 | p. 6; `ORC-2IP5JVUFM4` | “Below the calculated melting temperature of Ag2O (Tm 4 1060 K), stoichiometric Ag2O is described by SER °GAg2O - 2HSER = A + BT + CT ln T + DT 2 + FT -1 Ag - HO” |
| Phase transition | 1060.2 K | 1060.2 | L -> Ag2O; _L: O 0.3333_ | model | [1] Assal 1997 | Table III, p. 3, row 4; `ORC-MJNFPKLVYA` |  |

### Heat capacity / entropy / enthalpy (7)

Table: Heat capacity / entropy / enthalpy, Ag–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S_ | 40.3 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997; _cites Kubaschewski 1993_ | Table IV, p. 6, row 3; `ORC-2BIUY7EOVW.ce5055` |  |
| Entropy; _printed: S_ | 40.3 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997 | Table IV, p. 6, row 4; `ORC-3FHDF7TFKC.e1db23` |  |
| Entropy; _printed: S_ | 40.5667 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | experimental | [1] Assal 1997; _cites Pitzer 1937_ | Table IV, p. 6, row 1; `ORC-HO4PDQ4TPX.74deaa` |  |
| Heat capacity; _printed: Cp_ | 22.1 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997; _cites Kubaschewski 1993_ | Table IV, p. 6, row 3; `ORC-2BIUY7EOVW.74e78b` |  |
| Heat capacity; _printed: Cp_ | 22.1 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997 | Table IV, p. 6, row 4; `ORC-3FHDF7TFKC.fd5e06` |  |
| Heat capacity; _printed: Cp_ | 21.8667 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | experimental | [1] Assal 1997; _cites Pitzer 1937_ | Table IV, p. 6, row 1; `ORC-HO4PDQ4TPX.44338c` |  |
| Heat capacity; _printed: Cp_ | 22.2667 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | experimental | [1] Assal 1997; _cites Kobayashi 1951_ | Table IV, p. 6, row 2; `ORC-OLEMKAVMOH` |  |

### Activity / EMF / Gibbs energy (5)

Table: Activity / EMF / Gibbs energy, Ag–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy; _printed: Δ°G_ | -6887 J/mol |  | UNKNOWN | experimental | [1] Assal 1997; _cites Sieverts 1909_ | Table I, p. 2, row 1; `ORC-HE7LQKN7Y4.35385c` |  |
| Gibbs energy; _printed: Δ°G_ | -7028 J/mol |  | UNKNOWN | experimental | [1] Assal 1997; _cites Sieverts 1909_ | Table I, p. 2, row 1; `ORC-HE7LQKN7Y4.7a70f3` |  |
| Gibbs energy; _printed: Δ°G_ | -6975 J/mol | 1348 | UNKNOWN | experimental | [1] Assal 1997; _cites Donnan 1910_ | Table I, p. 2, row 2; `ORC-XB4OBER4ZF.b4bd56` |  |
| Vapour pressure; _printed: PO2_ | 5.370e7 Pa | 803 |  | model | [1] Assal 1997; _cites Keyes 1922_ | p. 1; `ORC-7HCJB5YF5G` | “Using the silver-Ag2 O equilibrium measurements from Keyes and Hara,14 they could calculate the eutectic point (i.e., the intersection of these three equilibria) and found T 4 803 K and PO2 4 5.37 × 107 Pa.” |
| Vapour pressure; _printed: PO2_ | 5.260e7 Pa | 803.6 |  | model | [1] Assal 1997 | p. 6; `ORC-VZ64O2L73O` | “The calculated eutectic point is at T 4 803.6 K, PO2 4 5.26 × 107 Pa, and xO 4 0.2514.” |

### Model expression (19)

Table: Model expression, Ag–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 5.98 J/mol/K |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Shah 1967_ | Table I, p. 2, row 6; `ORC-3657HPDZ3U.60c9f3` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -14473 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Shah 1967_ | Table I, p. 2, row 6; `ORC-3657HPDZ3U.c6db97` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -14940 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Lupis 1968_ | Table I, p. 2, row 8; `ORC-5WMBSK2UVU.2d72a2` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 21.68 J/mol/K |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Lupis 1968_ | Table I, p. 2, row 8; `ORC-5WMBSK2UVU.4685b6` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 18.04 J/mol/K |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Fischer 1966_ | Table I, p. 2, row 5; `ORC-5XFQRTEIRZ.113914` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -10463 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Fischer 1966_ | Table I, p. 2, row 5; `ORC-5XFQRTEIRZ.2fcf39` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 21.22 J/mol/K |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Diaz 1966_ | Table I, p. 2, row 4; `ORC-6L4UMH62M7.b72ffa` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -14145 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Diaz 1966_ | Table I, p. 2, row 4; `ORC-6L4UMH62M7.bf5b78` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -15004 J/mol |  | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 12; `ORC-7JQTIH33AX.286001` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 5.97 J/mol/K |  | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 12; `ORC-7JQTIH33AX.8500fb` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -13904 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Parlee 1965_ | Table I, p. 2, row 3; `ORC-CZ6ALN77AU.d31725` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 5.41 J/mol/K |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Parlee 1965_ | Table I, p. 2, row 3; `ORC-CZ6ALN77AU.fe2818` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 6.52 J/mol/K |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Otsuka 1981_ | Table I, p. 2, row 9; `ORC-EDFTECJ46X.928328` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -16140 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Otsuka 1981_ | Table I, p. 2, row 9; `ORC-EDFTECJ46X.d7b5c4` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -15614 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Magill 1988_ | Table I, p. 2, row 10; `ORC-UUKQ6CFBDO.b097cd` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 6.76 J/mol/K |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Magill 1988_ | Table I, p. 2, row 10; `ORC-UUKQ6CFBDO.e58eee` |  |
| gibbs energy expression term; _printed: Δ°G (coefficient B of A + B·T)_ | 5.79 J/mol/K |  | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 11; `ORC-VU72MJSBE6.7437a6` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -14759 J/mol |  | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 11; `ORC-VU72MJSBE6.bc9cca` |  |
| gibbs energy expression term; _printed: Δ°G (constant term A of A + B·T)_ | -17872 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Baker 1968_ | Table I, p. 2, row 7; `ORC-X6MC6VX7HL` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997). [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x)

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
