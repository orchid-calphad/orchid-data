# Cr–Ta system

> Cr–Ta system: 8 accepted literature values (formation 8) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-TA.html · Markdown: https://data.orchid-project.org/systems/CR-TA.md

8 accepted literature values from 2 paper(s) (experimental 2, model 3, DFT 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-TA.json) · [CSV](https://data.orchid-project.org/systems/CR-TA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-TA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-TA/CrTa-09Pav.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CR-TA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-TA.html) · [Markdown](https://data.orchid-project.org/systems/CR-TA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 3 |
| DFT | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrTa-09Pav.tdb | J. Pavlu, J. Vrestal, M. Sob, Calphad, 33, 179-86(2009). [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) | `9b511b195240080dd54955ff86b4c3e0c6419399a440f142a5b6046124109a8f` | [viewer](https://orchid-project.org/phase-diagrams/#CR-TA/CrTa-09Pav.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrTa-09Pav.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrTa-09Pav.json) |
| CrTa-93Dup-LB.tdb | N. Dupin, I. Ansara, J. Phase Equilib., 14, 451-56(1993), addendum, ibid, 15, 135(1994). [doi:10.1007/BF02671963](https://doi.org/10.1007/BF02671963) | `4ebec6dec118a81cac200c624e314a88f5c149eda56c0325e24c3d90526e0846` | [viewer](https://orchid-project.org/phase-diagrams/#CR-TA/CrTa-93Dup-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrTa-93Dup-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrTa-93Dup-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrTa-09Pav.tdb | 2238.61 | C14_LAVES (x(Ta) 0.37862) + LIQUID (x(Ta) 0.5011) + BCC_A2 (x(Ta) 0.73492) |
| CrTa-09Pav.tdb | 2065.68 | BCC_A2 (x(Ta) 0.03968) + LIQUID (x(Ta) 0.09906) + C14_LAVES (x(Ta) 0.30654) |
| CrTa-09Pav.tdb | 1991.39 | C14_LAVES (x(Ta) 0.37308) + C15_LAVES (x(Ta) 0.37408) + BCC_A2 (x(Ta) 0.84827) |
| CrTa-09Pav.tdb | 1903.36 | BCC_A2 (x(Ta) 0.01899) + C14_LAVES (x(Ta) 0.30973) + C15_LAVES (x(Ta) 0.3111) |
| CrTa-93Dup-LB.tdb | 2223.57 | C14_LAVES (x(Ta) 0.38351) + LIQUID (x(Ta) 0.49523) + BCC_A2 (x(Ta) 0.72858) |
| CrTa-93Dup-LB.tdb | 2043.56 | BCC_A2 (x(Ta) 0.04661) + LIQUID (x(Ta) 0.11701) + C14_LAVES (x(Ta) 0.30232) |
| CrTa-93Dup-LB.tdb | 1989.79 | C14_LAVES (x(Ta) 0.35387) + C15_LAVES (x(Ta) 0.35904) + BCC_A2 (x(Ta) 0.80496) |
| CrTa-93Dup-LB.tdb | 1915.8 | BCC_A2 (x(Ta) 0.02889) + C14_LAVES (x(Ta) 0.31195) + C15_LAVES (x(Ta) 0.32526) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-TA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-TA.json) · [CALPHAD hull CrTa-93Dup-LB](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-TA--CrTa-93Dup-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cr–Ta system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Cr2Ta (LT) | [Cr2Ta](https://data.orchid-project.org/compounds/Cr2Ta.html) | -8.93 kJ/mol-atom |  | model | -11.01 (mp-aaaaadnt) | -12.142 (oqmd-18299) | [1] Dupin 1993 | Table 4, p. 5, row 3 |  |
| Cr2Ta (LT) | [Cr2Ta](https://data.orchid-project.org/compounds/Cr2Ta.html) | -8.596 kJ/mol-atom |  | model | -11.01 (mp-aaaaadnt) | -12.142 (oqmd-18299) | [1] Dupin 1993 | Table 4, p. 5, row 4 |  |
| Cr2Ta (LT) | [Cr2Ta](https://data.orchid-project.org/compounds/Cr2Ta.html) | -8.5 kJ/mol-atom ± 0.5 | 1693 | experimental | -11.01 (mp-aaaaadnt) | -12.142 (oqmd-18299) | [1] Dupin 1993; _cites Feschotte 1964_ [doi](https://doi.org/10.1039/tf9646001941) | Table 4, p. 5, row 1 |  |
| Cr2Ta (LT) | [Cr2Ta](https://data.orchid-project.org/compounds/Cr2Ta.html) | -5 kJ/mol-atom | 1693 | model | -11.01 (mp-aaaaadnt) | -12.142 (oqmd-18299) | [1] Dupin 1993; _cites Kaufman 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990032-f) | Table 4, p. 5, row 2 |  |
| Cr2Ta C14 |  | -8.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Pavlů 2009; _cites Feschotte 1964_ | Table 4, p. 4, row 5 |  |
| CrTa2 (C14) |  | 76.35 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Pavlů 2009 | Table 5, p. 4, row 2 |  |
| CrTa2 (C15) |  | 74.39 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Pavlů 2009 | Table 5, p. 4, row 4 |  |
| CrTa2 (C36) |  | 75.34 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Pavlů 2009 | Table 5, p. 4, row 6 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. N. Dupin, I. Ansara, Thermodynamic assessment of the Cr-Ta system, JPE 14, 451-456 (1993). [doi:10.1007/bf02671963](https://doi.org/10.1007/bf02671963)
2. J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009). [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006)

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
