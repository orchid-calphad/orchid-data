# Ir–W system

> Ir–W system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IR-W.html · Markdown: https://data.orchid-project.org/systems/IR-W.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IR-W.json) · [CSV](https://data.orchid-project.org/systems/IR-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IR-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IR-W/IrW-20Hua.json) · [phases (8)](https://data.orchid-project.org/phases/pages/IR-W.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/IR-W.html) · [Markdown](https://data.orchid-project.org/systems/IR-W.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| IrW-20Hua.tdb | Y.-Y. Huang, B. Wu, F. Li, L.-L. Chen, Z.-X. Deng, K. Chang, J. Mining Metall. B, 56, 109-18(2020). [doi:10.2298/JMMB190211001H](https://doi.org/10.2298/JMMB190211001H) | `ad9a9f3cc83e11548f4603d7e9aae44dda1aabfcb1ed6e17153220c5bd37a338` | [viewer](https://orchid-project.org/phase-diagrams/#IR-W/IrW-20Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/IrW-20Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/IrW-20Hua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| IrW-20Hua.tdb | 2846.18 | LIQUID (x(W) 0.70735) + IRW3_D8B (x(W) 0.7995) + BCC_A2 (x(W) 0.93883) |
| IrW-20Hua.tdb | 2728.42 | IRW_A3 (x(W) 0.60218) + LIQUID (x(W) 0.64827) + IRW3_D8B (x(W) 0.75481) |
| IrW-20Hua.tdb | 2579.39 | FCC_A1 (x(W) 0.19061) + LIQUID (x(W) 0.22053) + IRW_A3 (x(W) 0.23656) |
| IrW-20Hua.tdb | 2074.88 | IRW_A3 (x(W) 0.56273) + IRW3_D8B (x(W) 0.75184) + BCC_A2 (x(W) 0.95018) |
| IrW-20Hua.tdb | 1921.14 | FCC_A1 (x(W) 0.20837) + IR3W_D019 (x(W) 0.23331) + IRW_A3 (x(W) 0.2404) |
| IrW-20Hua.tdb | 1847.89 | IRW_B19 (x(W) 0.49767) + IRW_A3 (x(W) 0.54313) + BCC_A2 (x(W) 0.96487) |
| IrW-20Hua.tdb | 1507.94 | IR3W_D019 (x(W) 0.33617) + IRW_A3 (x(W) 0.37392) + IRW_B19 (x(W) 0.47839) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IR/IR-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IR/IR-W.json)

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
