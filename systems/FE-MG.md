# Fe–Mg system

> Fe–Mg system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-MG.html · Markdown: https://data.orchid-project.org/systems/FE-MG.md

4 accepted literature values from 1 paper(s) (model 4); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-MG.json) · [CSV](https://data.orchid-project.org/systems/FE-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-MG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-MG/FeMg-98Tib-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/FE-MG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/FE-MG.html) · [Markdown](https://data.orchid-project.org/systems/FE-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FeMg-98Tib-LB.tdb | J. Tibballs, COST 507, Final report round 2, 1998. | `92473e5981422ab67f97cbb9d39cc6e3338f426a7b1c5fc5a6f89489ae344d43` | [viewer](https://orchid-project.org/phase-diagrams/#FE-MG/FeMg-98Tib-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FeMg-98Tib-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FeMg-98Tib-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FeMg-98Tib-LB.tdb | 1791.38 | BCC_A2 (x(Mg) 0.0076) + LIQUID#2 (x(Mg) 0.01847) + LIQUID (x(Mg) 0.98743) |
| FeMg-98Tib-LB.tdb | 1661.61 | FCC_A1 (x(Mg) 0.0052) + BCC_A2 (x(Mg) 0.00542) + LIQUID (x(Mg) 0.99192) |
| FeMg-98Tib-LB.tdb | 1183.42 | BCC_A2 (x(Mg) 7.700e-4) + FCC_A1 (x(Mg) 9.000e-4) + LIQUID (x(Mg) 0.99922) |
| FeMg-98Tib-LB.tdb | 922.94 | BCC_A2 (x(Mg) 8.000e-5) + LIQUID (x(Mg) 0.99992) + HCP_A3 (x(Mg) 1) |
| FeMg-98Tib-LB.tdb | 922.94 | BCC_A2 (x(Mg) 8.000e-5) + LIQUID (x(Mg) 0.99992) + HCP_A3 (x(Mg) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-MG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Fe–Mg system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1791.4 | monotectic: Liquid' -> bcc-A2 + Liquid" | Liquid': Mg 0.018; bcc-A2: Mg 0.008; Liquid": Mg 0.987 | model | [1] (ed.) 1998 | Table I, p. 212, row 1; `ORC-52P5DK6O3T` |  |
| 1661.6 | other: Liquid" + bcc-A2 -> fcc-A1 | Liquid": Mg 0.992; bcc-A2: Mg 0.005; fcc-A1: Mg 0.005 | model | [1] (ed.) 1998 | Table I, p. 212, row 2; `ORC-EGOFOXIDUR` |  |
| 1183.4 | other: Liquid" + bcc-A2 -> fcc-A1 | Liquid": Mg 0.999; bcc-A2: Mg 0.001; fcc-A1: Mg 0.001 | model | [1] (ed.) 1998 | Table I, p. 212, row 3; `ORC-754AJQSESZ` |  |
| 922.9 | other: Liquid" +bcc-A2 -> hcp-A3 | Liquid": Mg 1; bcc-A2: Mg 0; hcp-A3: Mg 1 | model | [1] (ed.) 1998 | Table I, p. 212, row 4; `ORC-PRMKGLNXKL` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Ansara, A. T. Dinsdale, M. H. Rand (eds.), COST 507: Thermochemical database for light metal alloys, Volume 2, EUR 18499 EN, Office for Official Publications of the European Communities, Luxembourg (1998), ISBN 92-828-3902-8.

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
