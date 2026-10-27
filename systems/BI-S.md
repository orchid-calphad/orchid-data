# Bi–S system

> Bi–S system: 9 accepted literature values (heat capacity / entropy / enthalpy 3, phase transition 3, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-S.html · Markdown: https://data.orchid-project.org/systems/BI-S.md

9 accepted literature values from 1 paper(s) (experimental 2, model 5, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-S.json) · [CSV](https://data.orchid-project.org/systems/BI-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-S/BiS-14Hua.json) · [phases (8)](https://data.orchid-project.org/phases/pages/BI-S.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-S.html) · [Markdown](https://data.orchid-project.org/systems/BI-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 5 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 3 |
| heat capacity / entropy / enthalpy | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiS-14Hua.tdb | S. Huang, Y. Liu, Y. Chen, Z. Kang, J. Electron. Mater., 43, 1237-43(2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) | `5bb6b53163e5d5991b79bf7ccdc3e1355f3c9da7d5346ea5a7fd000df556009a` | [viewer](https://orchid-project.org/phase-diagrams/#BI-S/BiS-14Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiS-14Hua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiS-14Hua.tdb | 1042.41 | BI2S3_D58 (x(S) 0.6) + LIQUID (x(S) 0.60013) + LIQUID#2 (x(S) 0.62853) |
| BiS-14Hua.tdb | 995.75 | BI2S3_D58 (x(S) 0.6) + LIQUID (x(S) 0.70511) + LIQUID#2 (x(S) 0.95897) |
| BiS-14Hua.tdb | 544.52 | RHOMBOHEDRAL_A7 (x(S) 0) + LIQUID (x(S) 3.200e-4) + BI2S3_D58 (x(S) 0.6) |
| BiS-14Hua.tdb | 384.34 | BI2S3_D58 (x(S) 0.6) + ORTHORHOMBIC_A16 (x(S) 1) + LIQUID (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–S system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 996 | monotectic: liq1 -> Bi2S3 + liq2 | Bi2S3: Bi 0.4, S 0.6; liq1: S 0.703; liq2: S 0.962 | model | [1] Huang 2014 | Table VII, p. 6, row 2; `ORC-OIFBIGHNZZ` |  |
| 544.5 | eutectic: liq -> Rho_Bi + Bi2S3 | Bi2S3: Bi 0.4, S 0.6 | model | [1] Huang 2014 | Table VII, p. 6, row 1; `ORC-XRY7Q3TNUR` |  |
| 388.2 | eutectic: liq2 -> Bi2S3 + Ort_S | Bi2S3: Bi 0.4, S 0.6 | model | [1] Huang 2014 | Table VII, p. 6, row 3; `ORC-JKHHGJP3IA` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Bi–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1036 K | 1036 | congruent transformation | experimental | [1] Huang 2014; _cites Glatz 1966_ [doi](https://doi.org/10.1021/j100883a513) | Table VI, p. 6, row 3; `ORC-OXKRFLCFJQ` |  |
| Phase transition | 1043 K | 1043 | congruent transformation | model | [1] Huang 2014 | Table VI, p. 6, row 1; `ORC-YOGBSIZEHI` |  |
| Phase transition | 1048 K | 1048 | congruent transformation | unspecified | [1] Huang 2014; _cites ref. 32_ | Table VI, p. 6, row 2; `ORC-ZT2MVI3ET7` |  |

### Heat capacity / entropy / enthalpy (3)

Table: Heat capacity / entropy / enthalpy, Bi–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Entropy of Melting_ | 38 J/mol (basis unstated)/K |  | UNKNOWN | experimental | [1] Huang 2014; _cites Itagaki 1985_ [doi](https://doi.org/10.1016/0040-6031%2885%2985439-3) | Table III, p. 5, row 3; `ORC-JBLMBCG6C6` |  |
| Entropy; _printed: Entropy of Melting_ | 49.4 J/mol (basis unstated)/K |  | UNKNOWN | unspecified | [1] Huang 2014; _cites Shamsuddin 1981_ | Table III, p. 5, row 2; `ORC-KPZJ42RVEJ` |  |
| Entropy; _printed: Entropy of Melting_ | 55.1 J/mol (basis unstated)/K |  | UNKNOWN | model | [1] Huang 2014 | Table III, p. 5, row 1; `ORC-Z7IMWLN4LN` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x)

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
