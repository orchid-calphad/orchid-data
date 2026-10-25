# Cr–Sc system

> Cr–Sc system: 4 accepted literature values (mixing / partial 2, invariant reaction 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-SC.html · Markdown: https://data.orchid-project.org/systems/CR-SC.md

4 accepted literature values from 1 paper(s) (experimental 1, model 3); 2 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-SC.json) · [CSV](https://data.orchid-project.org/systems/CR-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-SC) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-SC/CrSc-12Bu.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CR-SC.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-SC.html) · [Markdown](https://data.orchid-project.org/systems/CR-SC.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| mixing / partial | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrSc-12Bu.tdb | M.J. Bu, Y.B. Peng, M. Wang, Y. Du, H.H. Xu, D.D. Zhao, C.S. Sha, J. Phase Equilib. Diffus., 33, 40-45(2012). [doi:10.1007/s11669-011-9978-7](https://doi.org/10.1007/s11669-011-9978-7) | `255c2195d566a2929e7470af4ce93837a83ebe40e63894a80057222163a3289c` | [viewer](https://orchid-project.org/phase-diagrams/#CR-SC/CrSc-12Bu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrSc-12Bu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrSc-12Bu.json) |
| CrSc-15Wan.tdb | S.L. Wang, L.J. Zhou, Y. Ye, X.H. Wang, Y.H. Lin, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 36, 3-9(2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) | `a5b5b3689bf2cb9849c8644e9ec276fc33324f156c9246cca4fc702a7121e407` | [viewer](https://orchid-project.org/phase-diagrams/#CR-SC/CrSc-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrSc-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrSc-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrSc-12Bu.tdb | 1367.78 | BCC_A2 (x(Sc) 0.01323) + LIQUID (x(Sc) 0.65074) + BCC_A2#2 (x(Sc) 0.90507) |
| CrSc-12Bu.tdb | 1265.05 | BCC_A2 (x(Sc) 0.00914) + BCC_A2#2 (x(Sc) 0.92353) + HCP_A3 (x(Sc) 0.98822) |
| CrSc-15Wan.tdb | 1363.17 | BCC_A2 (x(Sc) 9.800e-4) + LIQUID (x(Sc) 0.6515) + BCC_A2#2 (x(Sc) 0.92319) |
| CrSc-15Wan.tdb | 1263.22 | BCC_A2 (x(Sc) 5.900e-4) + BCC_A2#2 (x(Sc) 0.93392) + HCP_A3 (x(Sc) 0.98615) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-SC.json) · [CALPHAD hull CrSc-12Bu](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-SC--CrSc-12Bu.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–Sc system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1263.25 | βSc -> (Cr) + αSc | βSc: Sc 0.934; (Cr): Sc 0; αSc: Sc 0.9862 | model | [1] Wang 2015 | Table 1, p. 3, row 6; `ORC-LV3AS346S5` |  |
| 1263.15 | βSc -> (Cr) + αSc |  | experimental | [1] Wang 2015; _cites Svechnikov 1972_ | Table 1, p. 3, row 5; `ORC-NEICK5WMN5` |  |

## Other properties

### Mixing / partial (2)

Table: Mixing / partial, Cr–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 1 kJ/mol (basis unstated) | 2273.15 | liquid; _alloy: Cr 0.5, Sc 0.5_ | model | [1] Wang 2015; _cites F 1988_ | Table 3, p. 3, row 1; `ORC-KNYKAU2W5D` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 0.975 kJ/mol (basis unstated) | 2273.15 | liquid; _alloy: Cr 0.5, Sc 0.5_ | model | [1] Wang 2015 | Table 3, p. 3, row 2; `ORC-RBIU7EBWFI` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8)

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
