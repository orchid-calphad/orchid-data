# Nb–Re system

> Nb–Re system: 42 accepted literature values (invariant reaction 20, formation 13, crystal structure 6, heat capacity / entropy / enthalpy 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-RE.html · Markdown: https://data.orchid-project.org/systems/NB-RE.md

42 accepted literature values from 2 paper(s) (experimental 12, model 24, DFT 6); 2 calculated phase diagram(s). 8 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/NB-RE.json) · [CSV](https://data.orchid-project.org/systems/NB-RE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NB-RE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-RE/NbRe-13Liu.json) · [phases (6)](https://data.orchid-project.org/phases/pages/NB-RE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NB-RE.html) · [Markdown](https://data.orchid-project.org/systems/NB-RE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 24 |
| DFT | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 20 |
| phase transition | 1 |
| formation | 13 |
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

Table: Invariant reactions reported in the literature for the Nb–Re system (20)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 3004 | Liquid ↔ hcp + χ | L: Re 0.88 | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 4; `ORC-6OOI4WDRRE` |  |
| 3004 | eutectic: L -> χ + hcp (eutectic) | L: Re 0.88 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 8; `ORC-7XWYXZW7PP` |  |
| 2990 | Liquid ↔ hcp + χ | L: Re 0.861 | model | [1] Yen 2020 | Table VIII, p. 44, row 6; `ORC-NW4V5CUWLM` |  |
| 2982 | eutectic: L -> χ + hcp (eutectic) | L: Re 0.87 | model | [2] Liu 2013 | Table 6, p. 9, row 7; `ORC-F3NZHTIXZ3` |  |
| 2982 | Liquid ↔ hcp + χ | L: Re 0.87 | DFT | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 5; `ORC-UCHRGRMVDG` |  |
| 2843 | Liquid + χ ↔ σ | L: Re 0.53 | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 7; `ORC-6JF6Y3MMIG` |  |
| 2843 | peritectic: L + χ -> σ (peritectic) | L: Re 0.53 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 4; `ORC-L62WHNUIWH` |  |
| 2831 | Liquid ↔ bcc + σ | L: Re 0.46 | DFT | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 2; `ORC-33EEZMH2GS` |  |
| 2831 | Liquid + χ ↔ σ | L: Re 0.54 | DFT | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 8; `ORC-5QA7S7J6AF` |  |
| 2831 | peritectic: L + χ -> σ (peritectic) | L: Re 0.54 | model | [2] Liu 2013 | Table 6, p. 9, row 3; `ORC-TH3MP5QHWA` |  |
| 2804 | Liquid + χ ↔ σ | L: Re 0.531 | model | [1] Yen 2020 | Table VIII, p. 44, row 9; `ORC-7QAJT7ZNJT` |  |
| 2740 | eutectic: L -> bcc + σ (eutectic) | L: Re 0.48 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 2; `ORC-25V73YGVHI` |  |
| 2740 | Liquid ↔ bcc + σ | L: Re 0.48 | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 1; `ORC-HHFTH2FIN7` |  |
| 2724 | eutectic: L -> bcc + σ (eutectic) | bcc: Re 0.46 | model | [2] Liu 2013 | Table 6, p. 9, row 1; `ORC-XQIUK4ED5G` |  |
| 2703 | Liquid ↔ bcc + σ | L: Re 0.456 | model | [1] Yen 2020 | Table VIII, p. 44, row 3; `ORC-BUDBODJQLT` |  |
| 2460 | σ ↔ bcc + χ |  | experimental | [1] Yen 2020; _cites Giessen 1961_ | Table VIII, p. 44, row 10; `ORC-S2CH6VXKE3` |  |
| 2460 | eutectoid: σ -> bcc + χ (eutectoid) | σ: Re 0.54 | experimental | [2] Liu 2013; _cites Giessen 1961_ | Table 6, p. 9, row 6; `ORC-ZE5UC6CEE2` |  |
| 2441 | eutectoid: σ -> bcc + χ (eutectoid) | σ: Re 0.57 | model | [2] Liu 2013 | Table 6, p. 9, row 5; `ORC-ELMWBCFUHN` |  |
| 2441 | σ ↔ bcc + χ |  | model | [1] Yen 2020; _cites Liu 2013_ | Table VIII, p. 44, row 11; `ORC-IQQB4KEKAF` |  |
| 2436 | σ ↔ bcc + χ |  | model | [1] Yen 2020 | Table VIII, p. 44, row 12; `ORC-XMPUKZ7J46` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Nb–Re system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| (σ) |  | -13.588 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 2; `ORC-Z4GXLV2562.2b896f` |  |
| (σ) |  | -2.247 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 1; `ORC-NQ66MRC6SE.c4e5d8` |  |
| (χ) |  | -13.542 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 4; `ORC-IENEGXBQ4W.2a06f8` |  |
| (χ) |  | -10.519 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 6; `ORC-PMML277PUB.61264f` |  |
| (χ) |  | 4.359 kJ/mol-atom | 298.15 | model |  |  | [2] Liu 2013 | Table 3, p. 5, row 5; `ORC-A2SYWB6OSF.13962f` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 3073 K | 3073 | congruent transformation | experimental | [2] Liu 2013; _cites Knapton 1959_ [doi](https://doi.org/10.1016/0022-5088%2859%2990065-7) | p. 2; `ORC-YZKCOR6Y7Y` | “Knapton also noted the congruent melting of χ at 3073 K \[6\].” |

### Formation (8)

Table: Formation, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔfS_ | -2.033 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 1; `ORC-NQ66MRC6SE.7a84f5` |  |
| Entropy of formation; _printed: ΔfS_ | -0.068 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 1; `ORC-NQ66MRC6SE.d1dcaa` |  |
| Entropy of formation; _printed: ΔfS_ | -0.692 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 2; `ORC-Z4GXLV2562.e27537` |  |
| Entropy of formation; _printed: ΔfS_ | -0.023 J/mol-atom/K | 298.15 | (σ) | model | [2] Liu 2013 | Table 3, p. 5, row 2; `ORC-Z4GXLV2562.efaf4c` |  |
| Entropy of formation; _printed: ΔfS_ | 0.88 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 5; `ORC-A2SYWB6OSF.dedd51` |  |
| Entropy of formation; _printed: ΔfS_ | 0.492 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 4; `ORC-IENEGXBQ4W.9efd1d` |  |
| Entropy of formation; _printed: ΔfS_ | 0.237 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 6; `ORC-PMML277PUB.660c36` |  |
| Entropy of formation; _printed: ΔfS_ | 13.751 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 6; `ORC-PMML277PUB.9b75b8` |  |

### Heat capacity / entropy / enthalpy (2)

Table: Heat capacity / entropy / enthalpy, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: ΔfS_ | 51.029 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 5; `ORC-A2SYWB6OSF.2d1b6a` |  |
| Entropy; _printed: ΔfS_ | 28.528 J/mol-atom/K | 298.15 | (χ) | model | [2] Liu 2013 | Table 3, p. 5, row 4; `ORC-IENEGXBQ4W.4b90e8` |  |

### Crystal structure (6)

Table: Crystal structure, Nb–Re system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 9.782 Å |  | σ | experimental | [2] Liu 2013; _cites Joubert 2008_ [doi](https://doi.org/10.1016/j.pmatsci.2007.04.001) | Table 1, p. 4, row 8; `ORC-EXG7IJEDXY.64d753` |  |
| Lattice a | 9.779 Å | 0 | σ-(Re)10(Nb)4(Nb)16 | DFT | [2] Liu 2013 | Table 1, p. 4, row 7; `ORC-IKPKSWE2LY.74b2f5` |  |
| Lattice a | 9.676 Å |  | χ | experimental | [2] Liu 2013; _cites Joubert 2009_ [doi](https://doi.org/10.1016/j.pmatsci.2009.04.002) | Table 1, p. 4, row 10; `ORC-EHOAWE4CFE` |  |
| Lattice a | 9.677 Å | 0 | χ-(Re)24(Nb)10(Re)24 | DFT | [2] Liu 2013 | Table 1, p. 4, row 9; `ORC-FF32EHOQDS` |  |
| lattice c a | 0.521 not_printed |  | σ | experimental | [2] Liu 2013; _cites Joubert 2008_ [doi](https://doi.org/10.1016/j.pmatsci.2007.04.001) | Table 1, p. 4, row 8; `ORC-EXG7IJEDXY.adb6d8` |  |
| lattice c a | 0.523 not_printed | 0 | σ-(Re)10(Nb)4(Nb)16 | DFT | [2] Liu 2013 | Table 1, p. 4, row 7; `ORC-IKPKSWE2LY.e61b0c` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020). [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797)
2. Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013). [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006)

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
