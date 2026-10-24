# Nb–Re system

> Nb–Re system: 50 accepted literature values (invariant reaction 27, formation 14, crystal structure 6, heat capacity / entropy / enthalpy 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-RE.html · Markdown: https://data.orchid-project.org/systems/NB-RE.md

50 accepted literature values from 2 paper(s) (experimental 17, model 26, DFT 7); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NB-RE.json) · [CSV](https://data.orchid-project.org/systems/NB-RE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NB-RE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-RE/NbRe-13Liu.json) · [phases (6)](https://data.orchid-project.org/phases/pages/NB-RE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NB-RE.html) · [Markdown](https://data.orchid-project.org/systems/NB-RE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 17 |
| model | 26 |
| DFT | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 27 |
| phase transition | 1 |
| formation | 14 |
| heat capacity / entropy / enthalpy | 2 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NbRe-13Liu.tdb | X.L. Liu, C.Z. Hargather, Z.-K. Liu, Calphad, 41, 119-27(2013). [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006) | `9127581a18abfbf796e89ef8697ff3e913d6ac69087a786efa45855308b83b12` | [viewer](https://orchid-project.org/phase-diagrams/#NB-RE/NbRe-13Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbRe-13Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbRe-13Liu.json) |
| NbRe-20Yen.tdb | S. Yen, S. Wu, M.A. Makhraja, K. Lo, A. Yeh, K. Yoshimi, C. Zhang, S. Lin, Calphad, 70, 101797(2020). [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) | `a3f16c73704aef3b4dea70b7faa4dd235462965e98bca54cc37a5d1cc7e42b6e` | [viewer](https://orchid-project.org/phase-diagrams/#NB-RE/NbRe-20Yen.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbRe-20Yen.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbRe-20Yen.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NbRe-13Liu.tdb | 2982.47 | CHI_A12 (x(Re) 0.85394) + LIQUID (x(Re) 0.86561) + HCP_A3 (x(Re) 0.97743) |
| NbRe-13Liu.tdb | 2831.78 | LIQUID (x(Re) 0.53985) + SIGMA_D8B (x(Re) 0.59992) + CHI_A12 (x(Re) 0.65735) |
| NbRe-13Liu.tdb | 2724.38 | BCC_A2 (x(Re) 0.45815) + LIQUID (x(Re) 0.46233) + SIGMA_D8B (x(Re) 0.568) |
| NbRe-13Liu.tdb | 2439.06 | BCC_A2 (x(Re) 0.46955) + SIGMA_D8B (x(Re) 0.57061) + CHI_A12 (x(Re) 0.63616) |
| NbRe-20Yen.tdb | 2990.17 | CHI_A12 (x(Re) 0.85278) + LIQUID (x(Re) 0.86135) + HCP_A3 (x(Re) 0.97513) |
| NbRe-20Yen.tdb | 2804.19 | LIQUID (x(Re) 0.53095) + SIGMA_D8B (x(Re) 0.56368) + CHI_A12 (x(Re) 0.61944) |
| NbRe-20Yen.tdb | 2703.45 | BCC_A2 (x(Re) 0.4333) + LIQUID (x(Re) 0.45597) + SIGMA_D8B (x(Re) 0.52522) |
| NbRe-20Yen.tdb | 2435.76 | BCC_A2 (x(Re) 0.45194) + SIGMA_D8B (x(Re) 0.54229) + CHI_A12 (x(Re) 0.60144) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NB/NB-RE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NB/NB-RE.json) · [CALPHAD hull NbRe-13Liu](https://data.orchid-project.org/hulls/calphad-sgte/NB/NB-RE--NbRe-13Liu.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nb–Re system (27)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 3004 | Liquid ↔ hcp + χ | L: Re 0.88 | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 4 |  |
| 3004 | eutectic: L -> χ + hcp (eutectic) | L: Re 0.88 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 8 |  |
| 3003 | eutectic: L-χ þhcp |  | experimental | [2] Liu 2013; _cites Knapton 1959_ [doi](https://doi.org/10.1016/0022-5088%2859%2990065-7) | p. 2 | “He evaluated one eutectic point at 2673 K and 53% Re (Lbcc þs) and a second one at 3003 K and 88% Re (L-χ þhcp).” |
| 2990 | Liquid ↔ hcp + χ | L: Re 0.861 | model | [1] Yen 2020 | Table VIII, p. 44, row 6 |  |
| 2982 | eutectic: L -> χ + hcp (eutectic) | L: Re 0.87 | model | [2] Liu 2013 | Table 6, p. 9, row 7 |  |
| 2982 | Liquid ↔ hcp + χ | L: Re 0.87 | DFT | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 5 |  |
| 2982 | eutectic |  | model | [2] Liu 2013 | p. 8 | “Excellent agreement is seen in the Re-rich eutectic at 86% Re and 2982 K (L-χþhcp) when compared to the experimental values of 88 70.5% Re and 3004 715 K \[7\].” |
| 2843 | Liquid + χ ↔ σ | L: Re 0.53 | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 7 |  |
| 2843 | peritectic: L + χ -> σ (peritectic) | L: Re 0.53 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 4 |  |
| 2831 | Liquid ↔ bcc + σ | L: Re 0.46 | DFT | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 2 |  |
| 2831 | Liquid + χ ↔ σ | L: Re 0.54 | DFT | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 8 |  |
| 2831 | peritectic: L + χ -> σ (peritectic) | L: Re 0.54 | model | [2] Liu 2013 | Table 6, p. 9, row 3 |  |
| 2804 | Liquid + χ ↔ σ | L: Re 0.531 | model | [1] Yen 2020 | Table VIII, p. 44, row 9 |  |
| 2793 | peritectic: L þhcp-χ |  | experimental | [2] Liu 2013; _cites Savitskii 1961_ [doi](https://doi.org/10.1007/bf01472402) | p. 2 | “A peritectic reaction forming χ, existing from 69.5% to 86.5% Re, was found at 2793 K (L þhcp-χ).” |
| 2740 | eutectic: L -> bcc + σ (eutectic) | L: Re 0.48 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 2 |  |
| 2740 | Liquid ↔ bcc + σ | L: Re 0.48 | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 1 |  |
| 2724 | eutectic |  | model | [2] Liu 2013 | p. 7 | “Starting on the Nb-rich side of the phase diagram, the present work shows a eutectic at 46% Re at a temperature of 2724 K (Lbcc þs) in close agreement with the reported 48 71% Re and” |
| 2724 | eutectic: L -> bcc + σ (eutectic) | bcc: Re 0.46 | model | [2] Liu 2013 | Table 6, p. 9, row 1 |  |
| 2723 | peritectic: L þχ-s |  | experimental | [2] Liu 2013 | p. 2 | “A peritectic point was found at 2723 K and 57% Re (L þχ-s).” |
| 2703 | Liquid ↔ bcc + σ | L: Re 0.456 | model | [1] Yen 2020 | Table VIII, p. 44, row 3 |  |
| 2673 | eutectic: Lbcc þs |  | experimental | [2] Liu 2013; _cites Knapton 1959_ [doi](https://doi.org/10.1016/0022-5088%2859%2990065-7) | p. 2 | “He evaluated one eutectic point at 2673 K and 53% Re (Lbcc þs) and a second one at 3003 K and 88% Re (L-χ þhcp).” |
| 2613 | eutectic: L-bcc þχ |  | experimental | [2] Liu 2013 | p. 2 | “At 2613 K, a eutectic reaction exists with the composition of 50-51% Re (L-bcc þχ).” |
| 2460 | σ ↔ bcc + χ |  | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 10 |  |
| 2460 | eutectoid: σ -> bcc + χ (eutectoid) | σ: Re 0.54 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 6 |  |
| 2441 | eutectoid: σ -> bcc + χ (eutectoid) | σ: Re 0.57 | model | [2] Liu 2013 | Table 6, p. 9, row 5 |  |
| 2441 | σ ↔ bcc + χ |  | DFT | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 11 |  |
| 2436 | σ ↔ bcc + χ |  | model | [1] Yen 2020 | Table VIII, p. 44, row 12 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Nb–Re system (6)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -13.542 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | p. 4 | “Table 3 depicts that the ΔfH for χ-(Re)24(Nb)10(Re)24 calculated with the Debye-Grüneisen model at 298 K in this work is -13.542 kJ/mol atom.” |
| (σ) |  | -13.588 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 2 |  |
| (σ) |  | -2.247 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 1 |  |
| (χ) |  | -13.542 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 4 |  |
| (χ) |  | -10.519 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 6 |  |
| (χ) |  | 4.359 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 5 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 3073 K | 3073 | congruent transformation | experimental | [2] Liu 2013; _cites Knapton 1959_ [doi](https://doi.org/10.1016/0022-5088%2859%2990065-7) | p. 2 | “Knapton also noted the congruent melting of χ at 3073 K \[6\].” |

### Formation (8)

Table: Formation, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔfS_ | -2.033 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 1 |  |
| Entropy of formation; _printed: ΔfS_ | -0.068 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 1 |  |
| Entropy of formation; _printed: ΔfS_ | -0.692 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 2 |  |
| Entropy of formation; _printed: ΔfS_ | -0.023 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 2 |  |
| Entropy of formation; _printed: ΔfS_ | 0.88 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 5 |  |
| Entropy of formation; _printed: ΔfS_ | 0.492 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 4 |  |
| Entropy of formation; _printed: ΔfS_ | 0.237 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 6 |  |
| Entropy of formation; _printed: ΔfS_ | 13.751 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 6 |  |

### Heat capacity / entropy / enthalpy (2)

Table: Heat capacity / entropy / enthalpy, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: ΔfS_ | 51.029 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 5 |  |
| Entropy; _printed: ΔfS_ | 28.528 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 4 |  |

### Crystal structure (6)

Table: Crystal structure, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 9.676 Å |  | UNKNOWN | experimental | [2] Liu 2013; _cites Joubert 2009_ [doi](https://doi.org/10.1016/j.pmatsci.2009.04.002) | Table 1, p. 4, row 10 |  |
| Lattice a | 9.782 Å |  | UNKNOWN | experimental | [2] Liu 2013; _cites Joubert 2008_ [doi](https://doi.org/10.1016/j.pmatsci.2007.04.001) | Table 1, p. 4, row 8 |  |
| Lattice a | 9.677 Å | 0 | UNKNOWN | DFT | [2] Liu 2013 | Table 1, p. 4, row 9 |  |
| Lattice a | 9.779 Å | 0 | UNKNOWN | DFT | [2] Liu 2013 | Table 1, p. 4, row 7 |  |
| lattice c a | 0.521 not_printed |  | UNKNOWN | experimental | [2] Liu 2013; _cites Joubert 2008_ [doi](https://doi.org/10.1016/j.pmatsci.2007.04.001) | Table 1, p. 4, row 8 |  |
| lattice c a | 0.523 not_printed | 0 | UNKNOWN | DFT | [2] Liu 2013 | Table 1, p. 4, row 7 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020). [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797)
2. Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013). [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
