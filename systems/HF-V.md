# Hf–V system

> Hf–V system: 24 accepted literature values (invariant reaction 12, formation 4, mixing / partial 4, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-V.html · Markdown: https://data.orchid-project.org/systems/HF-V.md

24 accepted literature values from 1 paper(s) (experimental 8, model 16); 1 calculated phase diagram(s). 15 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-V.json) · [CSV](https://data.orchid-project.org/systems/HF-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-V/HfV-05Ser.json) · [phases (5)](https://data.orchid-project.org/phases/pages/HF-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HF-V.html) · [Markdown](https://data.orchid-project.org/systems/HF-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 16 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 4 |
| formation | 4 |
| mixing / partial | 4 |

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

Table: Invariant reactions reported in the literature for the Hf–V system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2266.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 3, p. 3, row 15; `ORC-ULYMJRGWAE` |  |
| 1808.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 3, p. 3, row 5; `ORC-BDLVB33T7V` |  |
| 1804.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 2, p. 3, row 6; `ORC-LV434AGVKP` |  |
| 1793.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 3, p. 3, row 7; `ORC-3G73AJRGW2` |  |
| 1793.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 8; `ORC-HRCGT35BXK` |  |
| 1733.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 3, p. 3, row 9; `ORC-CGT2S2IPDK` |  |
| 1731.15 | eutectic: L -> bcc_A2 + C15-Laves |  | model | [1] Servant 2005 | Table 2, p. 3, row 10; `ORC-CJRPIXGBRC` |  |
| 1729.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 12; `ORC-FPTWLCXDMG` |  |
| 1726.15 | eutectic: L -> bcc_A2 + C15-Laves |  | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 2, p. 3, row 11; `ORC-NPQGJJSIY3` |  |
| 1473.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | model | [1] Servant 2005 | Table 3, p. 3, row 14; `ORC-H4HY336G33` |  |
| 1466.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | model | [1] Servant 2005 | Table 3, p. 3, row 13; `ORC-KVRKMVZQUP` |  |
| 1463.15 | eutectoid: bcc_A2 -> C15-Laves + cph_A3 |  | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 16; `ORC-2IX5X7Y3EI` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Hf–V system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Laves |  | -3.344 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Servant 2005 | Table 1, p. 2, row 2; `ORC-7BVLHTVAN2.1e70f9` |  |
| Laves |  | -3.204 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Servant 2005 | Table 1, p. 2, row 4; `ORC-FNPVDX2U5V.040967` |  |
| Laves phase |  | -3.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Servant 2005 | Table 1, p. 2, row 3; `ORC-HH4D75SPXZ.3f50c8` |  |
| Laves phase |  | -2.813 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Servant 2005 | Table 1, p. 2, row 5; `ORC-NKIM2CP5YX.6c0590` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Hf–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1805.65 K | 1805.65 | congruent melting: L -> C15 Laves | model | [1] Servant 2005 | Table 3, p. 3, row 2; `ORC-L3XCVYIOSY` |  |
| Phase transition | 1809.15 K | 1809.15 | congruent melting: L -> C15 Laves | model | [1] Servant 2005 | Table 3, p. 3, row 1; `ORC-4IK4OX7EUJ` |  |
| Phase transition | 1823.15 K | 1823.15 | congruent melting: L -> C15 Laves | experimental | [1] Servant 2005; _cites Smith 1990_ | Table 3, p. 3, row 4; `ORC-ERC4LMJTDP` |  |
| Phase transition | 1825.15 K | 1825.15 | congruent melting: L -> C15 Laves | experimental | [1] Servant 2005; _cites Rudy 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990003-9) | Table 3, p. 3, row 3; `ORC-QJFT5ZQRXW` |  |

### Mixing / partial (4)

Table: Mixing / partial, Hf–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔHmelting_ | -5.528 kJ/mol (basis unstated) | 298.15 | liquid; _alloy: Hf 0.5, V 0.5_ | model | [1] Servant 2005 | Table 1, p. 2, row 2; `ORC-7BVLHTVAN2.638e87` |  |
| Enthalpy of mixing; _printed: ΔHmelting_ | -4.67 kJ/mol (basis unstated) | 298.15 | liquid; _alloy: Hf 0.5, V 0.5_ | model | [1] Servant 2005 | Table 1, p. 2, row 4; `ORC-FNPVDX2U5V.d81635` |  |
| Enthalpy of mixing; _printed: ΔHmelting_ | -4.42 kJ/mol (basis unstated) | 298.15 | liquid; _alloy: Hf 0.5, V 0.5_ | model | [1] Servant 2005 | Table 1, p. 2, row 3; `ORC-HH4D75SPXZ.614cc1` |  |
| Enthalpy of mixing; _printed: ΔHmelting_ | -4.692 kJ/mol (basis unstated) | 298.15 | liquid; _alloy: Hf 0.5, V 0.5_ | model | [1] Servant 2005 | Table 1, p. 2, row 5; `ORC-NKIM2CP5YX.975a96` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005). [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
