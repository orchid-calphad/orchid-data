# Au–Te system

> Au–Te system: 49 accepted literature values (phase transition 22, crystal structure 12, invariant reaction 10, formation 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-TE.html · Markdown: https://data.orchid-project.org/systems/AU-TE.md

49 accepted literature values from 2 paper(s) (experimental 46, model 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-TE.json) · [CSV](https://data.orchid-project.org/systems/AU-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-TE/AuTe-06Wan.json) · [phases (6)](https://data.orchid-project.org/phases/pages/AU-TE.html) · [Markdown](https://data.orchid-project.org/systems/AU-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 46 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 22 |
| formation | 4 |
| crystal structure | 12 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuTe-06Wan.tdb | J. Wang, X.-G. Lu, B. Sundman, X. Su, J. Alloys Compd., 407, 106-11(2006). [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038) | `03172f4e43a2f653f818fbbdcc7f41e60472fa03e9582242975439feab85d909` | [viewer](https://orchid-project.org/phase-diagrams/#AU-TE/AuTe-06Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuTe-06Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuTe-06Wan.json) |
| AuTe-94Feu-LB.tdb | Y. Feutelais, D. Mouani, J.R. Didry, B. Legendre, J. Phase Equilib., 15, 380-85(1994). [doi:10.1007/BF02647557](https://doi.org/10.1007/BF02647557) | `92fa89b9beed51a93a85bd15ff5130e9d40e9174624824aa1afbe8656d77bd8b` | [viewer](https://orchid-project.org/phase-diagrams/#AU-TE/AuTe-94Feu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuTe-94Feu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuTe-94Feu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuTe-06Wan.tdb | 718.44 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.53882) + AUTE2_C34 (x(Te) 0.66667) |
| AuTe-06Wan.tdb | 718.43 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.53953) + AUTE2_C34 (x(Te) 0.66667) |
| AuTe-06Wan.tdb | 718.43 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.53942) + AUTE2_C34 (x(Te) 0.66667) |
| AuTe-06Wan.tdb | 689.88 | AUTE2_C34 (x(Te) 0.66667) + LIQUID (x(Te) 0.87066) + HEXAGONAL_A8 (x(Te) 1) |
| AuTe-06Wan.tdb | 689.88 | AUTE2_C34 (x(Te) 0.66667) + LIQUID (x(Te) 0.87069) + HEXAGONAL_A8 (x(Te) 1) |
| AuTe-94Feu-LB.tdb | 719.88 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.54578) + AUTE2_C34 (x(Te) 0.66667) |
| AuTe-94Feu-LB.tdb | 719.88 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.54553) + AUTE2_C34 (x(Te) 0.66667) |
| AuTe-94Feu-LB.tdb | 688.82 | AUTE2_C34 (x(Te) 0.66667) + LIQUID (x(Te) 0.87187) + HEXAGONAL_A8 (x(Te) 1) |
| AuTe-94Feu-LB.tdb | 315.22 | FCC_A1 (x(Te) 0) + AUTE2_C34 (x(Te) 0.66667) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-TE.json) · [CALPHAD hull AuTe-94Feu-LB](https://data.orchid-project.org/hulls/calphad-sgte/AU/AU-TE--AuTe-94Feu-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Te system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 725 | eutectic: Liquid = fcc (Au) + AuTe2 | fcc (Au): Te 0; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Pelabon 1909_ | Table 2, p. 3, row 4 |  |
| 721 | eutectic: Liquid = fcc (Au) + AuTe2 | fcc (Au): Te 0; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Bergman 1977_ [doi](https://doi.org/10.1002/bbpc.19770811024) | Table 2, p. 3, row 3 |  |
| 720 | eutectic: Liquid = fcc (Au) + AuTe2 | fcc (Au): Te 0; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Pellini 1910_ | Table 2, p. 3, row 2 |  |
| 718.4 | eutectic: Liquid = fcc (Au) + AuTe2 | fcc (Au): Te 0; AuTe2: Te 0.666667 | model | [1] Wang 2006 | Table 2, p. 3, row 5 |  |
| 705 | eutectic: Liquid = fcc (Au) + AuTe2 | fcc (Au): Te 0; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Rose 1908_ | Table 2, p. 3, row 1 |  |
| 690 | eutectic: Liquid = hex (Te) + AuTe2 | hex (Te): Te 1; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Bergman 1977_ [doi](https://doi.org/10.1002/bbpc.19770811024) | Table 2, p. 3, row 9 |  |
| 689.9 | eutectic: Liquid = hex (Te) + AuTe2 | hex (Te): Te 1; AuTe2: Te 0.666667 | model | [1] Wang 2006 | Table 2, p. 3, row 10 |  |
| 689 | eutectic: Liquid = hex (Te) + AuTe2 | hex (Te): Te 1; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Pellini 1910_ | Table 2, p. 3, row 8 |  |
| 688 | eutectic: Liquid = hex (Te) + AuTe2 | hex (Te): Te 1; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Pelabon 1909_ | Table 2, p. 3, row 7 |  |
| 670 | eutectic: Liquid = hex (Te) + AuTe2 | hex (Te): Te 1; AuTe2: Te 0.666667 | experimental | [1] Wang 2006; _cites Rose 1908_ | Table 2, p. 3, row 6 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Au–Te system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -4.74 kJ/mol-atom | 298 | experimental |  |  | [1] Wang 2006; _cites Andon 1971_ [doi](https://doi.org/10.1039/j19710001788) | p. 3 | “The data for enthalpy of formation of AuTe2 obtained from vapor pressure measurements by Andon et al. \[21\] and Veale and Barrett \[13\] are -4.74 and -3.91 kJ per mole atoms, respectively, at 298 K.” |
| — |  | -3.91 kJ/mol-atom | 298 | experimental |  |  | [1] Wang 2006; _cites Veale 1967_ [doi](https://doi.org/10.1016/0022-5088%2867%2990110-5) | p. 3 | “The data for enthalpy of formation of AuTe2 obtained from vapor pressure measurements by Andon et al. \[21\] and Veale and Barrett \[13\] are -4.74 and -3.91 kJ per mole atoms, respectively, at 298 K.” |
| — |  | -3 kJ/mol-atom | 298 | experimental |  |  | [1] Wang 2006 | p. 3 | “They obtained the enthalpy of formation of AuTe2 compound at 298 K (-3.0 kJ per mole of atoms) and the enthalpy of fusion (19.1 kJ per mole of atoms).” |
| — |  | -2.5 kJ/mol-atom | 728 | experimental |  |  | [1] Wang 2006; _cites Bergman 1977_ [doi](https://doi.org/10.1002/bbpc.19770811024) | p. 3 | “The enthalpy of formation of AuTe2 compound at 728 K is -2.5 kJ per mole of atoms and the enthalpy of fusion at 737 K is 18.6 kJ per mole of atoms, which were measured by direct reaction calorimetry \[3\].” |

## Other properties

### Phase transition (22)

Table: Phase transition, Au–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 690.25 K | 690.25 | other: 97 at.% Te; _alloy: Au 0.03, Te 0.97_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 32 |  |
| Phase transition | 690.35 K | 690.35 | other: 70 at.% Te; _alloy: Au 0.3, Te 0.7_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 28 |  |
| Phase transition | 690.45 K | 690.45 | other: 88 at.% Te; _alloy: Au 0.12, Te 0.88_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 30 |  |
| Phase transition | 690.45 K | 690.45 | other: 93 at.% Te; _alloy: Au 0.07, Te 0.93_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 31 |  |
| Phase transition | 690.65 K | 690.65 | other: 80 at.% Te; _alloy: Au 0.2, Te 0.8_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 29 |  |
| Phase transition | 708.15 K | 708.15 | AuTe2 | experimental | [2] Feutelais 1994; _cites Winkler 1994_ | p. 2 | “Later, \[64Win\] pointed out a crystalline transformation of the AuTe 2 compound at 435 ~” |
| Phase transition | 717.15 K | 717.15 | AuTe2 | experimental | [2] Feutelais 1994; _cites ref. 65Cab_ | p. 2 | “On the same compound, using high temperature X-ray powder diffraction, \[65Cab\] found at 444 ~ on only one occasion a diffraction pattern different from this one obtained at room temperature.” |
| Phase transition | 720.85 K | 720.85 | other: 38 at.% Te; _alloy: Au 0.62, Te 0.38_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 18 |  |
| Phase transition | 720.95 K | 720.95 | other: 43 at.% Te; _alloy: Au 0.57, Te 0.43_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 19 |  |
| Phase transition | 720.95 K | 720.95 | other: 54 at.% Te; _alloy: Au 0.46, Te 0.54_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 22 |  |
| Phase transition | 721.05 K | 721.05 | other: 50 at.% Te; _alloy: Au 0.5, Te 0.5_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 20 |  |
| Phase transition | 721.05 K | 721.05 | other: 53 at.% Te; _alloy: Au 0.47, Te 0.53_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 21 |  |
| Phase transition | 721.15 K | 721.15 | other: 55 at.% Te; _alloy: Au 0.45, Te 0.55_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 23 |  |
| Phase transition | 721.15 K | 721.15 | other: 60 at.% Te; _alloy: Au 0.4, Te 0.6_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 25 |  |
| Phase transition | 721.15 K | 721.15 | other: 63 at.% Te; _alloy: Au 0.37, Te 0.63_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 26 |  |
| Phase transition | 721.25 K | 721.25 | other: 57 at.% Te; _alloy: Au 0.43, Te 0.57_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 24 |  |
| Phase transition | 725 K | 725 | congruent melting: Liquid = AuTe2; _L: Te 0.666667; AuTe2: Te 0.666667_ | experimental | [1] Wang 2006; _cites Rose 1908_ | Table 2, p. 3, row 12 |  |
| Phase transition | 736 K | 736 | congruent melting: Liquid = AuTe2; _L: Te 0.666667; AuTe2: Te 0.666667_ | experimental | [1] Wang 2006; _cites Bergman 1977_ [doi](https://doi.org/10.1002/bbpc.19770811024) | Table 2, p. 3, row 13 |  |
| Phase transition | 736.75 K | 736.75 | congruent transformation | experimental | [2] Feutelais 1994 | p. 2 | “Auo.333Te0.667 a congruent melting point at 463.6 ~” |
| Phase transition | 736.75 K | 736.75 | congruent transformation: 66.67 at.% Te; _alloy: Au 0.3333, Te 0.6667_ | experimental | [2] Feutelais 1994 | Table I, p. 1, row 27 |  |
| Phase transition | 737 K | 737 | congruent melting: Liquid = AuTe2; _L: Te 0.666667; AuTe2: Te 0.666667_ | experimental | [1] Wang 2006; _cites Pellini 1910_ | Table 2, p. 3, row 11 |  |
| Phase transition | 738.4 K | 738.4 | congruent melting: Liquid = AuTe2; _L: Te 0.666667; AuTe2: Te 0.666667_ | model | [1] Wang 2006 | Table 2, p. 3, row 14 |  |

### Crystal structure (12)

Table: Crystal structure, Au–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.409 nm | 298.15 | Au; _alloy: Te 0_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 5 |  |
| Lattice a | 0.4093 nm | 298.15 | Au; _alloy: Te 0_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 1 |  |
| Lattice a | 0.4086 nm | 298.15 | Au; _alloy: Te 0_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 9 |  |
| Lattice a | 0.4089 nm | 298.15 | Au; _alloy: Te 0_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 11 |  |
| Lattice a | 0.4087 nm | 298.15 | Au; _alloy: Te 0_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 3 |  |
| Lattice a | 0.409 nm | 298.15 | Au; _alloy: Te 0_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 7 |  |
| Lattice a | 0.4098 nm | 298.15 | Au0.500Te0.500; _alloy: Te 0.5_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 4 |  |
| Lattice a | 0.4108 nm | 298.15 | Au0.500Te0.500; _alloy: Te 0.5_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 2 |  |
| Lattice a | 0.4095 nm | 298.15 | Au0.500Te0.500; _alloy: Te 0.5_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 8 |  |
| Lattice a | 0.4091 nm | 298.15 | Au0.500Te0.500; _alloy: Te 0.5_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 10 |  |
| Lattice a | 0.4097 nm | 298.15 | Au0.500Te0.500; _alloy: Te 0.5_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 12 |  |
| Lattice a | 0.4099 nm | 298.15 | Au0.500Te0.500; _alloy: Te 0.5_ | experimental | [2] Feutelais 1994 | Table 3, p. 2, row 6 |  |

### Other property (1)

Table: Other property, Au–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: enthalpy of fusion_ | 18.6 kJ per mole of atoms | 737 |  | experimental | [1] Wang 2006; _cites Bergman 1977_ [doi](https://doi.org/10.1002/bbpc.19770811024) | p. 3 | “The enthalpy of formation of AuTe2 compound at 728 K is -2.5 kJ per mole of atoms and the enthalpy of fusion at 737 K is 18.6 kJ per mole of atoms, which were measured by direct reaction calorimetry \[3\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jianhua Wang, Xiao-gang Lu, Bo Sundman, Xuping Su, Thermodynamic reassessment of the Au–Te system, Journal of Alloys and Compounds 407, 106-111 (2006). [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038)
2. Y. Feutelais, D. Mouani, J. R. Didry, B. Legendre, The gold-tellurium system, JPE 15, 380-385 (1994). [doi:10.1007/bf02647557](https://doi.org/10.1007/bf02647557)

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
