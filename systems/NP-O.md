# Np–O system

> Np–O system: 45 accepted literature values (formation 14, heat capacity / entropy / enthalpy 11, invariant reaction 7, phase transition 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NP-O.html · Markdown: https://data.orchid-project.org/systems/NP-O.md

45 accepted literature values from 1 paper(s) (experimental 3, model 29, unspecified 13); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/NP-O.json) · [CSV](https://data.orchid-project.org/systems/NP-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NP-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NP-O/NpO-16Smi.json) · [phases (9)](https://data.orchid-project.org/phases/pages/NP-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NP-O.html) · [Markdown](https://data.orchid-project.org/systems/NP-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 29 |
| unspecified | 13 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase transition | 6 |
| formation | 14 |
| heat capacity / entropy / enthalpy | 11 |
| crystal structure | 4 |
| other property | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NpO-16Smi.tdb | A.L. Smith, J.-Y. Colle, O. Benes, R.J.M. Konings, B. Sundman, C. Gueneau, J. Chem. Thermodyn., 103, 257-75(2016). [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040) | `f83f0e3f59b5ca9526ff567a1d28354abc1a3dcc0c99f14a83021650bd6be3b1` | [viewer](https://orchid-project.org/phase-diagrams/#NP-O/NpO-16Smi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NpO-16Smi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NpO-16Smi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NpO-16Smi.tdb | 1116.83 | ION (x(O) 5.500e-4) + ION#2 (x(O) 0.41177) + NPO2_C1 (x(O) 0.66642) |
| NpO-16Smi.tdb | 916.84 | BCC_A2 (x(O) 0) + ION (x(O) 0) + NPO2_C1 (x(O) 0.66664) |
| NpO-16Smi.tdb | 916.84 | BCC_A2 (x(O) 0) + ION (x(O) 0) + NPO2_C1 (x(O) 0.66664) |
| NpO-16Smi.tdb | 855.95 | TETRAG_AD (x(O) 0) + BCC_A2 (x(O) 0) + NPO2_C1 (x(O) 0.66666) |
| NpO-16Smi.tdb | 702.28 | NPO2_C1 (x(O) 0.66667) + NP2O5 (x(O) 0.71429) + GAS (x(O) 1) |
| NpO-16Smi.tdb | 702.28 | NPO2_C1 (x(O) 0.66667) + NP2O5 (x(O) 0.71429) + O2GAS (x(O) 1) |
| NpO-16Smi.tdb | 555.03 | TETRAG_AD (x(O) 0) + ORTHO_AC (x(O) 0) + NPO2_C1 (x(O) 0.66667) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NP/NP-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NP/NP-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Np–O system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 3070 | NpO2-x = L | NpO2-x: O 0.66667; L: O 0.66667 | unspecified | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 7, p. 10, row 7; `ORC-LNUSDKLIZM` |  |
| 3069.5 | NpO1.90 = L | NpO1.90: O 0.6549; L: O 0.6549 | model | [1] Smith 2016 | Table 7, p. 10, row 5; `ORC-E323HEQGWT` |  |
| 2879 | NpO2-x + G = L | NpO2-x: O 0.6633; L: O 0.672 | model | [1] Smith 2016 | Table 7, p. 10, row 6; `ORC-CG5TRVCYWC` |  |
| 1117 | L1 + L2 = NpO2-x | L1: O 5.500e-4; NpO2-x: O 0.412 | model | [1] Smith 2016 | Table 7, p. 10, row 2; `ORC-7KSJBSWI6T` |  |
| 913 | L1 = NpO2-x + γ-Np | NpO2-x: O 0.66667; γ-Np: O 0 | model | [1] Smith 2016 | Table 7, p. 10, row 1; `ORC-KBXM2K6JWI` |  |
| 700 | Np2O5 = 2NpO2 + 1/2O2 | Np2O5: O 0.71428; NpO2: Np 0.333333, O 0.666667 | unspecified | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 7, p. 10, row 4; `ORC-7W5Z67OINR` |  |
| 700 | Np2O5 = 2NpO2 + 1/2O2 | Np2O5: O 0.71428; NpO2: Np 0.333333, O 0.666667 | model | [1] Smith 2016 | Table 7, p. 10, row 3; `ORC-OL3XCXZOGY` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Np–O system (14)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Np(g) |  | 470 kJ/mol (basis unstated) ± 5 | 298.15 | model |  |  | [1] Smith 2016; _cites Konings 2010_ [doi](https://doi.org/10.1063/1.3474238) | Table 11, p. 14, row 1; `ORC-26LE6HRVKA.67ad21` |  |
| Np2O5(cr) | [Np2O5](https://data.orchid-project.org/compounds/Np2O5.html) | -310.286 kJ/mol-atom | 298.15 | model | -332.73 (mp-aaabfope) | -307.97 (oqmd-113840) | [1] Smith 2016 | Table 9, p. 12, row 3; `ORC-JBXVUOFGIP.854c26` |  |
| Np2O5(cr) | [Np2O5](https://data.orchid-project.org/compounds/Np2O5.html) | -308.957 kJ/mol-atom ± 1.32857 | 298.15 | unspecified | -332.73 (mp-aaabfope) | -307.97 (oqmd-113840) | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 2, p. 3, row 7; `ORC-JPU2E25EMA.b56a48` |  |
| Np2O5(cr) | [Np2O5](https://data.orchid-project.org/compounds/Np2O5.html) | -308.957 kJ/mol-atom ± 1.32857 | 298.15 | model | -332.73 (mp-aaabfope) | -307.97 (oqmd-113840) | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 9, p. 12, row 4; `ORC-NWFD2FN5QA.258f9b` |  |
| NpO(g) |  | -16.5 kJ/mol (basis unstated) ± 12.2 | 298.15 | model |  |  | [1] Smith 2016 | Table B.3, p. 17, row 4; `ORC-TQHMSO3VT6.07db6c` |  |
| NpO(g) |  | -13.3 kJ/mol (basis unstated) ± 11.5 | 298.15 | model |  |  | [1] Smith 2016 | Table B.3, p. 17, row 4; `ORC-TQHMSO3VT6.1a6a92` |  |
| NpO(g) |  | -9.8 kJ/mol (basis unstated) ± 7.8 | 298.15 | model |  |  | [1] Smith 2016 | Table 11, p. 14, row 2; `ORC-U4EO7KAALX.a5b857` |  |
| NpO(g) |  | -6.3 kJ/mol (basis unstated) ± 10.6 | 298.15 | model |  |  | [1] Smith 2016 | Table B.3, p. 17, row 3; `ORC-N3LQBPBIG7.780ae6` |  |
| NpO(g) |  | -2 kJ/mol (basis unstated) ± 11.4 | 298.15 | model |  |  | [1] Smith 2016 | Table B.3, p. 17, row 3; `ORC-N3LQBPBIG7.8310cd` |  |
| NpO2(cr) | [NpO2](https://data.orchid-project.org/compounds/NpO2.html) | -359.5 kJ/mol-atom ± 0.9 | 298.15 | model | -347.462 (mp-aaaaadwq) | -357.999 (oqmd-30883) | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 9, p. 12, row 2; `ORC-BFPKHAMK57.63ecea` |  |
| NpO2(cr) | [NpO2](https://data.orchid-project.org/compounds/NpO2.html) | -359.5 kJ/mol-atom ± 0.9 | 298.15 | unspecified | -347.462 (mp-aaaaadwq) | -357.999 (oqmd-30883) | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 2, p. 3, row 5; `ORC-OUZO3RGPQY.6dbca4` |  |
| NpO2(cr) | [NpO2](https://data.orchid-project.org/compounds/NpO2.html) | -358.933 kJ/mol-atom | 298.15 | model | -347.462 (mp-aaaaadwq) | -357.999 (oqmd-30883) | [1] Smith 2016 | Table 9, p. 12, row 1; `ORC-RGFB4RVHHS.c47128` |  |
| NpO2(g) |  | -471.7 kJ/mol (basis unstated) ± 3.3 | 298.15 | model |  |  | [1] Smith 2016 | Table 11, p. 14, row 3; `ORC-V3R5BIDQHV.1c7824` |  |
| α-Np(cr) |  | 0 kJ/mol-atom | 298.15 | unspecified |  |  | [1] Smith 2016; _cites Konings 2010_ [doi](https://doi.org/10.1063/1.3474238) | Table 2, p. 3, row 1; `ORC-4WOUHONCTY.0f3f6c` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Np–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1117 K | 1117 | other | model | [1] Smith 2016 | p. 18; `ORC-IDKB22L3TC` | “Yet, the temperature of the monotectic reaction as optimized herein, i.e., 1117 K, is much lower than suggested by \[12\].” |
| Phase transition | 1117 K | 1117 | other | model | [1] Smith 2016 | p. 10; `ORC-PUHRBVRTNB.195c93` | “One major difference, however, concerns the temperature of the monotectic reaction, calculated here at 1117 K, while Richter and Sari \[12\] reported it around 2450 K.” |
| Phase transition | 2450 K | 2450 | other | experimental | [1] Smith 2016 | p. 2; `ORC-3Z2Q5HAEIH` | “Richter and Sari have suggested 2450 K for the monotectic equilibrium temperature, and an oxygen-to-metal ratio O/Np = 1.8 for the lower oxygen composition of the monophasic domain NpO2x at 2450 K, by extrapolation of the phase boundary curve from 2300 K.” |
| Phase transition | 2450 K | 2450 | other | model | [1] Smith 2016; _cites Kinoshita 2003_ [doi](https://doi.org/10.1016/s0021-9614%2803%2900002-8) | p. 10; `ORC-K3Z3VSNFUS` | “The CALPHAD assessment presented by Kinoshita et al. \[23\] exemplifies this inconsistency, where the monotectic reaction is well-reproduced at 2450 K as well as the oxygen potential curves, but where the hypostoichiometric homogeneity range is far too extended.” |
| Phase transition | 2450 K | 2450 | other | experimental | [1] Smith 2016; _cites Richter 1987_ [doi](https://doi.org/10.1016/0022-3115%2887%2990019-5) | p. 10; `ORC-PUHRBVRTNB.6e73cc` | “One major difference, however, concerns the temperature of the monotectic reaction, calculated here at 1117 K, while Richter and Sari \[12\] reported it around 2450 K.” |
| Phase transition | 3069.5 K | 3069.5 | congruent transformation | model | [1] Smith 2016 | p. 10; `ORC-IYDRGULGUP` | “In addition, the melting point of neptunium dioxide is calculated at T fus = 3069.5 K for congruently melting NpO1:90 , which is consistent with the recommended value at T fus 1⁄4 ð3070 62Þ K \[14,22\].” |

### Heat capacity / entropy / enthalpy (11)

Table: Heat capacity / entropy / enthalpy, Np–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S_m^o_ | 197.72 unknown ± 0.1 | 298.15 | Np(g); _alloy: O 0_ | model | [1] Smith 2016; _cites Konings 2010_ [doi](https://doi.org/10.1063/1.3474238) | Table 11, p. 14, row 1; `ORC-26LE6HRVKA.050900` |  |
| Entropy; _printed: S°m (298.15 K)_ | 34.6286 J/mol-atom/K | 298.15 | Np2O5(cr); _alloy: O 0.714286_ | model | [1] Smith 2016 | Table 9, p. 12, row 3; `ORC-JBXVUOFGIP.153663` |  |
| Entropy; _printed: S°m(298.15 K)_ | 26.5714 J/mol-atom/K ± 2.14286 | 298.15 | Np2O5(cr); _alloy: O 0.714286_ | unspecified | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 2, p. 3, row 7; `ORC-JPU2E25EMA.96a25c` |  |
| Entropy; _printed: S°m (298.15 K)_ | 26.5714 J/mol-atom/K ± 2.14286 | 298.15 | Np2O5(cr); _alloy: O 0.714286_ | model | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 9, p. 12, row 4; `ORC-NWFD2FN5QA.6d1e7c` |  |
| Entropy; _printed: S_m^o_ | 253.06 unknown ± 4 | 298.15 | NpO(g); _alloy: O 0.5_ | model | [1] Smith 2016 | Table 11, p. 14, row 2; `ORC-U4EO7KAALX.052477` |  |
| Entropy; _printed: S°m (298.15 K)_ | 26.7667 J/mol-atom/K ± 0.133333 | 298.15 | NpO2(cr); _alloy: O 0.666667_ | model | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 9, p. 12, row 2; `ORC-BFPKHAMK57.7412b9` |  |
| Entropy; _printed: S°m_ | 26.7667 J/mol-atom/K ± 0.133333 | 298.15 | NpO2(cr); _alloy: O 0.666667_ | unspecified | [1] Smith 2016; _cites Konings 2014_ [doi](https://doi.org/10.1063/1.4825256) | Table 2, p. 3, row 5; `ORC-OUZO3RGPQY.1007b5` |  |
| Entropy; _printed: S°m (298.15 K)_ | 26.7667 J/mol-atom/K | 298.15 | NpO2(cr); _alloy: O 0.666667_ | model | [1] Smith 2016 | Table 9, p. 12, row 1; `ORC-RGFB4RVHHS.62ee3d` |  |
| Entropy; _printed: S_m^o_ | 269.892 unknown ± 6 | 298.15 | NpO2(g); _alloy: O 0.666667_ | model | [1] Smith 2016 | Table 11, p. 14, row 3; `ORC-V3R5BIDQHV.91e0a1` |  |
| Entropy; _printed: S°m(298.15 K)_ | 50.45 J/mol-atom/K ± 0.4 | 298.15 | α-Np(cr); _alloy: O 0_ | unspecified | [1] Smith 2016; _cites Konings 2010_ [doi](https://doi.org/10.1063/1.3474238) | Table 2, p. 3, row 1; `ORC-4WOUHONCTY.496f53` |  |
| Entropy; _printed: S°m_ | 50.45 J/mol-atom/K ± 0.4 | 298.15 | α-Np(cr); _alloy: O 0_ | unspecified | [1] Smith 2016; _cites Konings 2010_ [doi](https://doi.org/10.1063/1.3474238) | Table 2, p. 3, row 1; `ORC-4WOUHONCTY.5e9ed9` |  |

### Crystal structure (4)

Table: Crystal structure, Np–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.188 Å | 298.15 | Np2O5; _alloy: O 0.714286_ | unspecified | [1] Smith 2016; _cites Lemire 2001_ | Table 1, p. 2, row 5; `ORC-J62KDJADTG.b7de4f` |  |
| Lattice a | 5.434 Å | 298.15 | NpO2; _alloy: O 0.666667_ | unspecified | [1] Smith 2016; _cites Lemire 2001_ | Table 1, p. 2, row 4; `ORC-LKUTSTUH7B` |  |
| Lattice b | 6.592 Å | 298.15 | Np2O5; _alloy: O 0.714286_ | unspecified | [1] Smith 2016; _cites Lemire 2001_ | Table 1, p. 2, row 5; `ORC-J62KDJADTG.2a6767` |  |
| Lattice c | 4.09 Å | 298.15 | Np2O5; _alloy: O 0.714286_ | unspecified | [1] Smith 2016; _cites Lemire 2001_ | Table 1, p. 2, row 5; `ORC-J62KDJADTG.d2402a` |  |

### Other property (3)

Table: Other property, Np–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: O/Np_ | 1.92 unspecified ± 0.011 | 2260 |  | model | [1] Smith 2016 | p. 15; `ORC-JLJLRYANBJ` | “Nevertheless, based on the present experimental results and CALPHAD model, we can estimate the composition at congruent vapourization at 2260 K as (O/Np) = (1.92 ± 0.011).” |
| Other; _printed: fraction NpO2(g)_ | 93.2 % | 2260 |  | model | [1] Smith 2016 | p. 12; `ORC-XJFHLNINJJ` | “The calculated azeotropic vapour composition at 2260 K is: 93.2% NpO2(g), 6.1% NpO(g), and 0.7% O(g), which corresponds to an oxygen-to-metal ratio ðO=NpÞazeotropic = (1.945 ± 0.0031) at 2260 K.” |
| Other; _printed: (O/Np)gas_ | 1.939 unspecified | 2260 | gas | experimental | [1] Smith 2016; _cites Gotcu-Freis 2011_ [doi](https://doi.org/10.1016/j.jnucmat.2011.05.014) | p. 4; `ORC-47C646DJII` | “The authors reported a vapour made of 93% NpO2(g), 6% NpO(g), and 1% Np(g) at 2260 K under vacuum, with an overall gaseous composition (O/Np)gas = 1.939 \[11\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A.L. Smith, J.-Y. Colle, O. Beneš, R.J.M. Konings, B. Sundman, C. Guéneau, Thermodynamic assessment of the neptunium–oxygen system: Mass spectrometric studies and thermodynamic modelling, The Journal of Chemical Thermodynamics 103, 257-275 (2016). [doi:10.1016/j.jct.2016.07.040](https://doi.org/10.1016/j.jct.2016.07.040)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
