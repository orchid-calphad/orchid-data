# Bi–Cr system

> Bi–Cr system: 2 accepted literature values (invariant reaction 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-CR.html · Markdown: https://data.orchid-project.org/systems/BI-CR.md

2 accepted literature values from 1 paper(s) (experimental 1, model 1); 2 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-CR.json) · [CSV](https://data.orchid-project.org/systems/BI-CR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-CR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-CR/BiCr-13Cao.json) · [phases (5)](https://data.orchid-project.org/phases/pages/BI-CR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-CR.html) · [Markdown](https://data.orchid-project.org/systems/BI-CR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiCr-13Cao.tdb | Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013). [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) | `29ce6447bfe477c23626e12b83f63dfb13455691fd22a8dfbe548c134c5384c6` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CR/BiCr-13Cao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCr-13Cao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCr-13Cao.json) |
| BiCr-14Gos.tdb | S. Gosse, J. Nucl. Mater., 449, 122-31(2014). [doi:10.1016/j.jnucmat.2014.03.011](https://doi.org/10.1016/j.jnucmat.2014.03.011) | `836782b2e86fed0fbfd21aaa358ac16d69b07e6c3f9e13acc3421347434a198f` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CR/BiCr-14Gos.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCr-14Gos.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCr-14Gos.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiCr-13Cao.tdb | 1832.11 | LIQUID (x(Cr) 0.06217) + LIQUID#2 (x(Cr) 0.84962) + BCC_A2 (x(Cr) 0.99988) |
| BiCr-13Cao.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(Cr) 0) + LIQUID (x(Cr) 0) + BCC_A2 (x(Cr) 1) |
| BiCr-13Cao.tdb | 544.55 | LIQUID (x(Cr) 0) + RHOMBOHEDRAL_A7 (x(Cr) 0) + BCC_A2 (x(Cr) 1) |
| BiCr-14Gos.tdb | 2095.46 | LIQUID (x(Cr) 0.21948) + LIQUID#2 (x(Cr) 0.93275) + BCC_A2 (x(Cr) 0.9962) |
| BiCr-14Gos.tdb | 2095.46 | LIQUID#2 (x(Cr) 0.21948) + LIQUID (x(Cr) 0.93275) + BCC_A2 (x(Cr) 0.9962) |
| BiCr-14Gos.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(Cr) 0) + LIQUID (x(Cr) 0) + BCC_A2 (x(Cr) 1) |
| BiCr-14Gos.tdb | 544.55 | LIQUID (x(Cr) 0) + RHOMBOHEDRAL_A7 (x(Cr) 0) + BCC_A2 (x(Cr) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-CR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-CR.json) · [CALPHAD hull BiCr-13Cao](https://data.orchid-project.org/hulls/calphad-sgte/BI/BI-CR--BiCr-13Cao.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Cr system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 544.55 | Liquid#2=(Cr)+(Bi) | Liquid#2: Bi 0.999; (Cr): Bi 0; (Bi): Bi 1 | model | [1] Cao 2013 | Table 3, p. 5, row 19; `ORC-ADHC4G744P` |  |
| 544.15 | Liquid#2=(Cr)+(Bi) | Liquid#2: Bi 1; (Cr): Bi 0; (Bi): Bi 1 | experimental | [1] Cao 2013; _cites Williams 1907_ | Table 3, p. 5, row 18; `ORC-QGF3SKU55U` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang et al., Thermodynamic modeling of the Bi-M (M = Ti, Cr, V) systems, J min metall B Metall 49, 307-313 (2013). [doi:10.2298/jmmb130127033c](https://doi.org/10.2298/jmmb130127033c)

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
