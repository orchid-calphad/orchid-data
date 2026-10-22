# Hf–V system

> Hf–V system: 21 accepted literature values (invariant reaction 14, phase transition 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-V.html · Markdown: https://data.orchid-project.org/systems/HF-V.md

21 accepted literature values from 1 paper(s) (experimental 12, model 9); 1 calculated phase diagram(s). 10 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-V.json) · [CSV](https://data.orchid-project.org/systems/HF-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-V/HfV-05Ser.json) · [Markdown](https://data.orchid-project.org/systems/HF-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |
| phase transition | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfV-05Ser.tdb | C. Servant, J. Phase Equilib. Diffus., 26, 39-49(2005). [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) | `5eb8c7c45b64d39e5506d60ca92a8105b8ab1252eeccf8f392652a2363f392fc` | [viewer](https://orchid-project.org/phase-diagrams/#HF-V/HfV-05Ser.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfV-05Ser.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfV-05Ser.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfV-05Ser.tdb | 1807.52 | C15_LAVES (x(V) 0.67472) + LIQUID (x(V) 0.6923) + BCC_A2 (x(V) 0.97334) |
| HfV-05Ser.tdb | 1733.12 | BCC_A2 (x(V) 0.24261) + LIQUID (x(V) 0.46083) + C15_LAVES (x(V) 0.64035) |
| HfV-05Ser.tdb | 1466.17 | HCP_A3 (x(V) 0.02651) + BCC_A2 (x(V) 0.18619) + C15_LAVES (x(V) 0.64465) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hf–V system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2266.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 3, p. 3, row 15 |  |
| 1819.15 | peritectic |  | experimental | [1] Servant 2005; _cites Guzei 1968_ | p. 1 | “Conflicting information is provided in Ref 19 and 20, studies in which the Laves phase formation was reported to occur as result of a peritectic reaction at either 1546 °C (Ref 19) or 1490 °C (Ref 20).” |
| 1808.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 3, p. 3, row 5 |  |
| 1804.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 2, p. 3, row 6 |  |
| 1793.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 3, p. 3, row 7 |  |
| 1793.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 8 |  |
| 1763.15 | peritectic |  | experimental | [1] Servant 2005; _cites Cunnigham 1963_ | p. 1 | “Conflicting information is provided in Ref 19 and 20, studies in which the Laves phase formation was reported to occur as result of a peritectic reaction at either 1546 °C (Ref 19) or 1490 °C (Ref 20).” |
| 1733.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 3, p. 3, row 9 |  |
| 1731.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 2, p. 3, row 10 |  |
| 1729.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 12 |  |
| 1726.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 2, p. 3, row 11 |  |
| 1473.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | model | [1] Servant 2005 | Table 3, p. 3, row 14 |  |
| 1466.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | model | [1] Servant 2005 | Table 3, p. 3, row 13 |  |
| 1463.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 16 |  |

## Other properties

### Phase transition (7)

Table: Phase transition, Hf–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1805.65 K | 1805.65 | congruent melting: L -> C15 Laves | model | [1] Servant 2005 | Table 3, p. 3, row 2 |  |
| Phase transition | 1809.15 K | 1809.15 | congruent melting: L -> C15 Laves | model | [1] Servant 2005 | Table 3, p. 3, row 1 |  |
| Phase transition | 1823.15 K | 1823.15 | congruent melting: L -> C15 Laves | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 4 |  |
| Phase transition | 1823.15 K | 1823.15 | congruent transformation | model | [1] Servant 2005; _cites Smith 1990_ | p. 1 | “The C15-Laves phase melts congruently at a temperature of 1552 °C (Ref 16) and 1550 °C (Ref 17), and has a homogeneity range.” |
| Phase transition | 1825.15 K | 1825.15 | congruent melting: L -> C15 Laves | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 3, p. 3, row 3 |  |
| Phase transition | 1825.15 K | 1825.15 | congruent transformation | experimental | [1] Servant 2005; _cites Rudy 1968_ | p. 1 | “The C15-Laves phase melts congruently at a temperature of 1552 °C (Ref 16) and 1550 °C (Ref 17), and has a homogeneity range.” |
| Phase transition | 2446.15 K | 2446.15 |  | experimental | [1] Servant 2005; _cites Komjathy 1961_ | p. 1 | “On the other hand, according to Komjathy (Ref 18), its melting point is higher (2173 °C) and the phase is stoichiometric.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005). [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464)

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
