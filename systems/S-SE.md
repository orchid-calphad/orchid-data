# S–Se system

> S–Se system: 60 accepted literature values (other property 22, crystal structure 21, phase transition 9, invariant reaction 8) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/S-SE.html · Markdown: https://data.orchid-project.org/systems/S-SE.md

60 accepted literature values from 1 paper(s) (experimental 17, model 6, DFT 37); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/S-SE.json) · [CSV](https://data.orchid-project.org/systems/S-SE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#S-SE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#S-SE/SSe-17Gua.json) · [phases (6)](https://data.orchid-project.org/phases/pages/S-SE.html) · [Markdown](https://data.orchid-project.org/systems/S-SE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 17 |
| model | 6 |
| DFT | 37 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 9 |
| crystal structure | 21 |
| other property | 22 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SSe-17Gua.tdb | P.-W. Guan, S.-L. Shang, G. Lindwall, T. Anderson, Z.-K. Liu, J. Alloys Compd., 694, 510-21(2017). [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037) | `69fc3205ab133df26feeb5e181d219ea07fb4c0818bac6b1455f118c2441b6ac` | [viewer](https://orchid-project.org/phase-diagrams/#S-SE/SSe-17Gua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SSe-17Gua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SSe-17Gua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SSe-17Gua.tdb | 433.11 | LIQUID (x(Se) 0.72538) + SSE (x(Se) 0.83001) + HEXAGONAL_A8 (x(Se) 0.90441) |
| SSe-17Gua.tdb | 356.72 | ORTHORHOMBIC_A16 (x(Se) 0.15751) + LIQUID (x(Se) 0.23473) + SSE (x(Se) 0.39186) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/S/S-SE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/S/S-SE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the S–Se system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 433.16 | peritectic |  | experimental | [1] Guan 2017; _cites Ringer 1902_ [doi](https://doi.org/10.1002/zaac.19020320126) | p. 8 | “The peritectic reaction temperature predicted by this assessment is 433.1 K, which is in excellent agreement with the value observed by Ringer \[13\] (433.16 K).” |
| 433.15 | peritectic: L + d = X |  | experimental | [1] Guan 2017; _cites Ringer 1902_ [doi](https://doi.org/10.1002/zaac.19020320126) | p. 2 | “For the peritectic reaction (L þ d 1⁄4 X), Ringer \[13\] reported a temperature of 160 C and compositions 73.5, 83.0 and 87.0 at.% Se for the L, X and d phases, respectively.” |
| 433.1 | peritectic |  | model | [1] Guan 2017 | p. 8 | “The peritectic reaction temperature predicted by this assessment is 433.1 K, which is in excellent agreement with the value observed by Ringer \[13\] (433.16 K).” |
| 378.16 | eutectic |  | experimental | [1] Guan 2017; _cites Ringer 1902_ [doi](https://doi.org/10.1002/zaac.19020320126) | p. 8 | “The predicted eutectic reaction temperature, 372.3 K, is slightly lower than the values reported by Ringer \[13\] (378.16 K) and by Boctor and Kullerud \[16\] (375.16 ± 1 K).” |
| 378.15 | eutectic: L = b + X |  | experimental | [1] Guan 2017; _cites Ringer 1902_ [doi](https://doi.org/10.1002/zaac.19020320126) | p. 2 | “Ringer \[13\] also investigated the eutectic reaction (L 1⁄4 b þ X) and reported an invariant temperature of 105 C and compositions of 29.0, 40.0 and 48.7 at.% Se of b, L and X, respectively.” |
| 372.3 | eutectic |  | model | [1] Guan 2017 | p. 8 | “The predicted eutectic reaction temperature, 372.3 K, is slightly lower than the values reported by Ringer \[13\] (378.16 K) and by Boctor and Kullerud \[16\] (375.16 ± 1 K).” |
| 348.16 | eutectoid |  | experimental | [1] Guan 2017; _cites Ringer 1902_ [doi](https://doi.org/10.1002/zaac.19020320126) | p. 8 | “The predicted eutectoid reaction temperature, 337.7 K, is lower than that observed by Ringer \[13\] (348.16 K).” |
| 337.7 | eutectoid |  | model | [1] Guan 2017 | p. 8 | “The predicted eutectoid reaction temperature, 337.7 K, is lower than that observed by Ringer \[13\] (348.16 K).” |

## Other properties

### Phase transition (9)

Table: Phase transition, S–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 198 K | 198 | other | experimental | [1] Guan 2017; _cites Goldsmith 1977_ [doi](https://doi.org/10.1021/ja00465a029) | p. 2 | “the monoclinic b phase (ordered \[17\] below 198 K with space group P21 and disordered \[17,18\] above 198 K with space group P2/c) on the S-rich side, the hexagonal d phase with space group P3121 on the Se-rich side, and an intermediate X phase with an unknown structure.” |
| Phase transition | 198 K | 198 | other | experimental | [1] Guan 2017; _cites Goldsmith 1977_ [doi](https://doi.org/10.1021/ja00465a029) | p. 3 | “It was reported that there is an order-disorder transition at about 198 K \[17,18,46\].” |
| Phase transition | 348.15 K | 348.15 | b = a + X | experimental | [1] Guan 2017; _cites Ringer 1902_ [doi](https://doi.org/10.1002/zaac.19020320126) | p. 2 | “In the case of the eutectoid reaction (b 1⁄4 a þ X), Ringer \[13\] reported a temperature of 75 C and compositions of 12.0, 16.5, and 50.0 at.% Se of a, b and X, respectively, whereas the results by” |
| Phase transition | 369 K | 369 |  | experimental | [1] Guan 2017 | p. 1 | “The prediction of the transition temperature between a-S and b-S (428 K) is close to the experimental value (369 K).” |
| Phase transition | 369 K | 369 |  | experimental | [1] Guan 2017; _cites Hampton 1974_ [doi](https://doi.org/10.1080/14786437408222069) | p. 5 | “The a-S/b-S transition temperature is predicted to be 428 K, which is reasonably close to the experimental value, 369 K \[74\].” |
| Phase transition | 388 K | 388 |  | experimental | [1] Guan 2017 | p. 5 | “The agreement for TEC \[73\] in the low-temperature range is also good, but deviates in the high-temperature range (above 300 K, note that the melting temperature of sulfur is 388 K).” |
| Phase transition | 428 K | 428 |  | model | [1] Guan 2017 | p. 1 | “The prediction of the transition temperature between a-S and b-S (428 K) is close to the experimental value (369 K).” |
| Phase transition | 428 K | 428 |  | model | [1] Guan 2017 | p. 5 | “The a-S/b-S transition temperature is predicted to be 428 K, which is reasonably close to the experimental value, 369 K \[74\].” |
| Phase transition | 1029 K | 1029 | congruent transformation | model | [1] Guan 2017 | p. 8 | “The present assessment indicates a congruent volatilization temperature at 1029 K and composition 76 at.% Se at 1 bar, which is suitable for experimental verification as well as evaluating the accuracy of the present description of the gas phase.” |

### Crystal structure (21)

Table: Crystal structure, S–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| volume; _printed: Volume_ | 25.76 Å3/atom | 0 | α-S; _alloy: Se 0_ | experimental | [1] Guan 2017; _cites Rettig 1987_ [doi](https://doi.org/10.1107/s0108270187088152) | Table 1, p. 5, row 1 |  |
| volume; _printed: Volume_ | 23.51 Å3/atom | 0 | α-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 3 |  |
| volume; _printed: Volume_ | 27.29 Å3/atom | 0 | α-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 2 |  |
| volume; _printed: Volume_ | 28.19 Å3/atom | 0 | α-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 13 |  |
| volume; _printed: Volume_ | 32.13 Å3/atom | 0 | α-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 12 |  |
| volume; _printed: Volume_ | 23.66 Å3/atom | 0 | α′-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 11 |  |
| volume; _printed: Volume_ | 27.49 Å3/atom | 0 | α′-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 10 |  |
| volume; _printed: Volume_ | 31.49 Å3/atom | 0 | α′-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 20 |  |
| volume; _printed: Volume_ | 26.68 Å3/atom | 0 | α′-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 21 |  |
| volume; _printed: Volume_ | 29.78 Å3/atom | 0 | α′-Se; _alloy: Se 1_ | experimental | [1] Guan 2017; _cites Gattow 1964_ [doi](https://doi.org/10.1002/zaac.19643310504) | Table 1, p. 5, row 19 |  |
| volume; _printed: Volume_ | 27.74 Å3/atom | 0 | β-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 15 |  |
| volume; _printed: Volume_ | 32.52 Å3/atom | 0 | β-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 14 |  |
| volume; _printed: Volume_ | 27.81 Å3/atom | 0 | β1-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 5 |  |
| volume; _printed: Volume_ | 25.5 Å3/atom | 0 | β1-S; _alloy: Se 0_ | experimental | [1] Guan 2017; _cites Lewis 1911_ [doi](https://doi.org/10.1021/ja02217a005) | Table 1, p. 5, row 4 |  |
| volume; _printed: Volume_ | 24.22 Å3/atom | 0 | β1-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 6 |  |
| volume; _printed: Volume_ | 24.35 Å3/atom | 0 | β2-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 7 |  |
| volume; _printed: Volume_ | 26.86 Å3/atom | 0 | δ-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 8 |  |
| volume; _printed: Volume_ | 22.2 Å3/atom | 0 | δ-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 9 |  |
| volume; _printed: Volume_ | 23.08 Å3/atom | 0 | δ-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 18 |  |
| volume; _printed: Volume_ | 25.99 Å3/atom | 0 | δ-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 17 |  |
| volume; _printed: Volume_ | 26.57 Å3/atom | 0 | δ-Se; _alloy: Se 1_ | experimental | [1] Guan 2017; _cites Hamilton 1974_ [doi](https://doi.org/10.1016/s0022-3697%2874%2980126-5) | Table 1, p. 5, row 16 |  |

### Other property (22)

Table: Other property, S–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| bulk modulus; _printed: B0_ | 11.096 GPa (range 7.692 to 14.5) | 0 | α-S; _alloy: Se 0_ | experimental | [1] Guan 2017; _cites Rettig 1987_ [doi](https://doi.org/10.1107/s0108270187088152) | Table 1, p. 5, row 1 |  |
| bulk modulus; _printed: B0_ | 12.242 GPa | 0 | α-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 3 |  |
| bulk modulus; _printed: B0_ | 5.804 GPa | 0 | α-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 2 |  |
| bulk modulus; _printed: B0_ | 15.142 GPa | 0 | α-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 13 |  |
| bulk modulus; _printed: B0_ | 9.058 GPa | 0 | α-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 12 |  |
| bulk modulus; _printed: B0_ | 10.265 GPa | 0 | α′-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 11 |  |
| bulk modulus; _printed: B0_ | 6.383 GPa | 0 | α′-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 10 |  |
| bulk modulus; _printed: B0_ | 7.737 GPa | 0 | α′-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 20 |  |
| bulk modulus; _printed: B0_ | 13.342 GPa | 0 | α′-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 21 |  |
| bulk modulus; _printed: B0_ | 14.033 GPa | 0 | β-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 15 |  |
| bulk modulus; _printed: B0_ | 8.393 GPa | 0 | β-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 14 |  |
| bulk modulus; _printed: B0_ | 7.046 GPa | 0 | β1-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 5 |  |
| bulk modulus; _printed: B0_ | 10.867 GPa | 0 | β1-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 6 |  |
| bulk modulus; _printed: B0_ | 10.393 GPa | 0 | β2-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 7 |  |
| bulk modulus; _printed: B0_ | 7.252 GPa | 0 | δ-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 8 |  |
| bulk modulus; _printed: B0_ | 9.349 GPa | 0 | δ-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 9 |  |
| bulk modulus; _printed: B0_ | 34.163 GPa | 0 | δ-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 18 |  |
| bulk modulus; _printed: B0_ | 14.359 GPa | 0 | δ-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 17 |  |
| bulk modulus; _printed: B0_ | 10.9925 GPa (range 7.085 to 14.9) | 0 | δ-Se; _alloy: Se 1_ | experimental | [1] Guan 2017; _cites Hamilton 1974_ [doi](https://doi.org/10.1016/s0022-3697%2874%2980126-5) | Table 1, p. 5, row 16 |  |
| deviation from experiment; _printed: %Error_ | 5.9 % | 0 | α-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 2 |  |
| deviation from experiment; _printed: %Error_ | 5.7 % | 0 | α′-Se; _alloy: Se 1_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 20 |  |
| deviation from experiment; _printed: %Error_ | 9.1 % | 0 | β1-S; _alloy: Se 0_ | DFT | [1] Guan 2017 | Table 1, p. 5, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Pin-Wen Guan, Shun-Li Shang, Greta Lindwall, Tim Anderson, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the S-Se system and implications for chalcogenide alloys, Journal of Alloys and Compounds 694, 510-521 (2017). [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037)

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
