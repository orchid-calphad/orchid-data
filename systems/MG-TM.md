# Mg–Tm system

> Mg–Tm system: 12 accepted literature values (invariant reaction 12) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-TM.html · Markdown: https://data.orchid-project.org/systems/MG-TM.md

12 accepted literature values from 1 paper(s) (experimental 6, model 6); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-TM.json) · [CSV](https://data.orchid-project.org/systems/MG-TM.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-TM) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-TM/MgTm-04Du-LB.json) · [phases (7)](https://data.orchid-project.org/phases/pages/MG-TM.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MG-TM.html) · [Markdown](https://data.orchid-project.org/systems/MG-TM.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgTm-04Du-LB.tdb | Z. Du, H. Liu, G. Ling, J. Alloys Compd., 373, 151-55(2004). [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) | `8bc07bc38ca74452f239e4114172e09b8deed648a761aabdf5fbefc59765fa56` | [viewer](https://orchid-project.org/phase-diagrams/#MG-TM/MgTm-04Du-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgTm-04Du-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MgTm-04Du-LB.tdb | 1473.23 | LIQUID (x(Tm) 0.70008) + BCC_A2 (x(Tm) 0.75122) + HCP_A3 (x(Tm) 0.88076) |
| MgTm-04Du-LB.tdb | 1033.21 | LIQUID (x(Tm) 0.3351) + MGTM_B2 (x(Tm) 0.48967) + BCC_A2 (x(Tm) 0.55888) |
| MgTm-04Du-LB.tdb | 943.44 | MGTM_B2 (x(Tm) 0.51639) + BCC_A2 (x(Tm) 0.65883) + HCP_A3 (x(Tm) 0.85355) |
| MgTm-04Du-LB.tdb | 903.04 | LIQUID (x(Tm) 0.19656) + MG2TM_C14 (x(Tm) 0.33333) + MGTM_B2 (x(Tm) 0.41162) |
| MgTm-04Du-LB.tdb | 863.07 | LIQUID (x(Tm) 0.15097) + MG24TM5_A12 (x(Tm) 0.17241) + MG2TM_C14 (x(Tm) 0.33333) |
| MgTm-04Du-LB.tdb | 863.07 | LIQUID (x(Tm) 0.15122) + MG24TM5_A12 (x(Tm) 0.17241) + MG2TM_C14 (x(Tm) 0.33333) |
| MgTm-04Du-LB.tdb | 863.07 | LIQUID (x(Tm) 0.15081) + MG24TM5_A12 (x(Tm) 0.17241) + MG2TM_C14 (x(Tm) 0.33333) |
| MgTm-04Du-LB.tdb | 847.99 | HCP_A3 (x(Tm) 0.04441) + LIQUID (x(Tm) 0.10914) + MG24TM5_A12 (x(Tm) 0.17241) |
| MgTm-04Du-LB.tdb | 847.99 | HCP_A3 (x(Tm) 0.04431) + LIQUID (x(Tm) 0.10882) + MG24TM5_A12 (x(Tm) 0.17241) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MG/MG-TM.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-TM.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mg–Tm system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1473 | liquid + hcp(Tm) -> bcc | liquid: Tm 0.69; hcp(Tm): Tm 0.88; bcc: Tm 0.81 | experimental | [1] Du 2004; _cites Saccone 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906023-1) | Table 2, p. 4, row 10; `ORC-C5VPMUDM5V` |  |
| 1473 | liquid + hcp(Tm) -> bcc | liquid: Tm 0.7001; hcp(Tm): Tm 0.8808; bcc: Tm 0.7512 | model | [1] Du 2004 | Table 2, p. 4, row 9; `ORC-IY2Z4OTWTX` |  |
| 1033 | liquid + bcc -> MgTm | liquid: Tm 0.3351; bcc: Tm 0.5589; MgTm: Tm 0.4897 | model | [1] Du 2004 | Table 2, p. 4, row 7; `ORC-2WZYXAWMAA` |  |
| 1033 | liquid + bcc -> MgTm | liquid: Tm 0.32; bcc: Tm 0.57; MgTm: Tm 0.5 | experimental | [1] Du 2004; _cites Saccone 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906023-1) | Table 2, p. 4, row 8; `ORC-EJVY27LGMZ` |  |
| 943 | bcc -> MgTm + hcp(Tm) | bcc: Tm 0.7; MgTm: Tm 0.52; hcp(Tm): Tm 0.87 | experimental | [1] Du 2004; _cites Saccone 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906023-1) | Table 2, p. 4, row 12; `ORC-B5KTIEUM4G` |  |
| 943 | bcc -> MgTm + hcp(Tm) | bcc: Tm 0.6588; MgTm: Tm 0.5164; hcp(Tm): Tm 0.8536 | model | [1] Du 2004 | Table 2, p. 4, row 11; `ORC-TNPKOTOQCO` |  |
| 903 | liquid + MgTm -> Mg2Tm | liquid: Tm 0.1966; MgTm: Tm 0.4116; Mg2Tm: Tm 0.333333 | model | [1] Du 2004 | Table 2, p. 4, row 5; `ORC-3RYKO4WCXR` |  |
| 903 | liquid + MgTm -> Mg2Tm | liquid: Tm 0.18; MgTm: Tm 0.42; Mg2Tm: Tm 0.333333 | experimental | [1] Du 2004; _cites Saccone 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906023-1) | Table 2, p. 4, row 6; `ORC-BPPWOXTJ5A` |  |
| 863 | liquid +Mg2Tm -> Mg24Tm5 | liquid: Tm 0.151; Mg2Tm: Tm 0.333333; Mg24Tm5: Tm 0.172414 | model | [1] Du 2004 | Table 2, p. 4, row 3; `ORC-7O435JLSXH` |  |
| 863 | liquid +Mg2Tm -> Mg24Tm5 | liquid: Tm 0.13; Mg2Tm: Tm 0.333333; Mg24Tm5: Tm 0.172414 | experimental | [1] Du 2004; _cites Saccone 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906023-1) | Table 2, p. 4, row 4; `ORC-NJAVRCS2NH` |  |
| 848 | eutectic: liquid -> hcp(Mg)+Mg24Tm5 | liquid: Tm 0.11; hcp(Mg): Tm 0.06; Mg24Tm5: Tm 0.172414 | experimental | [1] Du 2004; _cites Saccone 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906023-1) | Table 2, p. 4, row 2; `ORC-2B2KI7D33D` |  |
| 848 | eutectic: liquid -> hcp(Mg)+Mg24Tm5 | liquid: Tm 0.1088; hcp(Mg): Tm 0.0443; Mg24Tm5: Tm 0.172414 | model | [1] Du 2004 | Table 2, p. 4, row 1; `ORC-B5U37CCRPB` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004). [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033)

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
