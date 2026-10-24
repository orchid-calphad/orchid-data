# Ce–Ti system

> Ce–Ti system: 4 accepted literature values (invariant reaction 2, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-TI.html · Markdown: https://data.orchid-project.org/systems/CE-TI.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-TI.json) · [CSV](https://data.orchid-project.org/systems/CE-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-TI/CeTi-18Yao.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CE-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CE-TI.html) · [Markdown](https://data.orchid-project.org/systems/CE-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeTi-18Yao.tdb | B. Yao, B. Hu, A. Zhang, J. Zhao, J. Wang, J. Phase Equilib. Diffus., 39, 44-50(2018). [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) | `775e4e88db0a29576be41201035738a09dc9f683db6b7aabe256f17d7ab525ab` | [viewer](https://orchid-project.org/phase-diagrams/#CE-TI/CeTi-18Yao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeTi-18Yao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeTi-18Yao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeTi-18Yao.tdb | 1724.89 | LIQUID (x(Ti) 0.24733) + LIQUID#2 (x(Ti) 0.78708) + BCC_A2 (x(Ti) 0.97985) |
| CeTi-18Yao.tdb | 1178.94 | LIQUID (x(Ti) 0.02344) + HCP_A3 (x(Ti) 0.9857) + BCC_A2 (x(Ti) 0.99502) |
| CeTi-18Yao.tdb | 1060.03 | BCC_A2 (x(Ti) 0.00508) + LIQUID (x(Ti) 0.01251) + HCP_A3 (x(Ti) 0.99068) |
| CeTi-18Yao.tdb | 990.76 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0.00341) + HCP_A3 (x(Ti) 0.99339) |
| CeTi-18Yao.tdb | 990.76 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0.0034) + HCP_A3 (x(Ti) 0.9934) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–Ti system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1063.15 | eutectic: Liquid#1 $ (dCe) ? (aTi) |  | experimental | [1] Yao 2018 | p. 6; `ORC-KSDAWGYXBB.d4772c` | “The temperatures of peritectic reaction Liquid#1 ? (bTi) $ (aTi) and eutectic reaction Liquid#1 $ (dCe) ? (aTi) are calculated to be 906 and 787 °C, which are consistent with the experimental ones 910 ± 10 and 790 ± 20 °C, respectively.” |
| 1060.15 | eutectic: Liquid#1 $ (dCe) ? (aTi) |  | model | [1] Yao 2018 | p. 6; `ORC-KSDAWGYXBB.35eefe` | “The temperatures of peritectic reaction Liquid#1 ? (bTi) $ (aTi) and eutectic reaction Liquid#1 $ (dCe) ? (aTi) are calculated to be 906 and 787 °C, which are consistent with the experimental ones 910 ± 10 and 790 ± 20 °C, respectively.” |

## Other properties

### Phase transition (2)

Table: Phase transition, Ce–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 983.15 K | 983.15 | other: (dCe) $ (cCe) ? (aTi) | experimental | [1] Yao 2018 | p. 6; `ORC-OCHD7HTFMF.1c6440` | “The calculated temperature of the eutectoid reaction (dCe) $ (cCe) ? (aTi) is to be 718 °C, which also agree well with the experimental one 710 ± 20 °C.” |
| Phase transition | 991.15 K | 991.15 | other: (dCe) $ (cCe) ? (aTi) | model | [1] Yao 2018 | p. 6; `ORC-OCHD7HTFMF.ae0e8e` | “The calculated temperature of the eutectoid reaction (dCe) $ (cCe) ? (aTi) is to be 718 °C, which also agree well with the experimental one 710 ± 20 °C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Bin Yao, Biao Hu, Anan Zhang, Jingrui Zhao, Jiong Wang, Yong Du, Thermodynamic Assessment of the Ti-RE (RE = Ce, Er, Tm, Y) Binary Systems, J. Phase Equilib. Diffus. 39, 44-50 (2018). [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0)

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
