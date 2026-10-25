# Cr–Pd system

> Cr–Pd system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-PD.html · Markdown: https://data.orchid-project.org/systems/CR-PD.md

6 accepted literature values from 1 paper(s) (experimental 3, model 3); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-PD.json) · [CSV](https://data.orchid-project.org/systems/CR-PD.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-PD) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-PD/CrPd-00Gho-LB.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CR-PD.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-PD.html) · [Markdown](https://data.orchid-project.org/systems/CR-PD.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrPd-00Gho-LB.tdb | G. Ghosh, G.B. Olson, J. Phase Equilib., 21, 32-39(2000). [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390) | `a3ff7860baad43f02ef3bf075df86e448927cb42388ebc576c49e3f682c5b9b3` | [viewer](https://orchid-project.org/phase-diagrams/#CR-PD/CrPd-00Gho-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrPd-00Gho-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrPd-00Gho-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrPd-00Gho-LB.tdb | 1576.87 | BCC_A2 (x(Pd) 0.01508) + LIQUID (x(Pd) 0.40437) + FCC_A1 (x(Pd) 0.49667) |
| CrPd-00Gho-LB.tdb | 842.96 | BCC_A2 (x(Pd) 0.00564) + CRPD_L10 (x(Pd) 0.5) + FCC_A1 (x(Pd) 0.63224) |
| CrPd-00Gho-LB.tdb | 842.96 | BCC_A2 (x(Pd) 0.00564) + CRPD_L10 (x(Pd) 0.5) + FCC_A1 (x(Pd) 0.63224) |
| CrPd-00Gho-LB.tdb | 778.66 | CRPD_L10 (x(Pd) 0.5) + CR2PD3_L12 (x(Pd) 0.6) + FCC_A1 (x(Pd) 0.65322) |
| CrPd-00Gho-LB.tdb | 778.66 | CRPD_L10 (x(Pd) 0.5) + CR2PD3_L12 (x(Pd) 0.6) + FCC_A1 (x(Pd) 0.65307) |
| CrPd-00Gho-LB.tdb | 778.66 | CRPD_L10 (x(Pd) 0.5) + CR2PD3_L12 (x(Pd) 0.6) + FCC_A1 (x(Pd) 0.65322) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-PD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-PD.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–Pd system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1586 | L \<-> (Cr) + (Pd) | L: Pd 0.44; (Cr): Pd 0.02; (Pd): Pd 0.495 | experimental | [1] Ghosh 2000; _cites Raub 1954_ | Table 1, p. 5, row 1; `ORC-2IXWLE2PAR` |  |
| 1577 | L \<-> (Cr) + (Pd) | L: Pd 0.4034; (Cr): Pd 0.0132; (Pd): Pd 0.4956 | model | [1] Ghosh 2000 | Table 1, p. 5, row 2; `ORC-EMT4VYGIFV` |  |
| 843 | (Cr) + (Pd) \<-> CrPd | (Cr): Pd 0.004; (Pd): Pd 0.628; CrPd: Pd 0.5 | experimental | [1] Ghosh 2000; _cites Raub 1967_ | Table 1, p. 5, row 3; `ORC-7YESCKYGRM` |  |
| 843 | (Cr) + (Pd) \<-> CrPd | (Cr): Pd 0.0044; (Pd): Pd 0.6321; CrPd: Pd 0.5 | model | [1] Ghosh 2000 | Table 1, p. 5, row 4; `ORC-ZODNDQORZE` |  |
| 778 | CrPd + (Pd) \<-> Cr2Pd3 | CrPd: Pd 0.5; (Pd): Pd 0.6532; Cr2Pd3: Pd 0.6 | model | [1] Ghosh 2000 | Table 1, p. 5, row 6; `ORC-E7CQMAMM65` |  |
| 778 | CrPd + (Pd) \<-> Cr2Pd3 | CrPd: Pd 0.52; (Pd): Pd 0.66; Cr2Pd3: Pd 0.61 | experimental | [1] Ghosh 2000; _cites Raub 1967_ | Table 1, p. 5, row 5; `ORC-PTA6LLQCYW` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. G. Ghosh, G. B. Olson, Thermodynamic modeling of the Cr-Pd and Mo-Pd systems, JPE 21, 32-39 (2000). [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390)

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
