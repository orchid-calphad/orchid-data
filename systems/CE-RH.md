# Ce–Rh system

> Ce–Rh system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-RH.html · Markdown: https://data.orchid-project.org/systems/CE-RH.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-RH/CeRh-24Bou.json) · [phases (11)](https://data.orchid-project.org/phases/pages/CE-RH.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CE-RH.html) · [Markdown](https://data.orchid-project.org/systems/CE-RH.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeRh-24Bou.tdb | H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024). [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) | `4df20ec37e9a29927289e46464b4f006e23185f4a0a0541ba49a661551ca4eea` | [viewer](https://orchid-project.org/phase-diagrams/#CE-RH/CeRh-24Bou.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeRh-24Bou.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeRh-24Bou.tdb | 1695.78 | CERH3_L12 (x(Rh) 0.75) + LIQUID (x(Rh) 0.82709) + FCC_A1 (x(Rh) 1) |
| CeRh-24Bou.tdb | 1670.15 | CERH2_C15 (x(Rh) 0.66667) + LIQUID (x(Rh) 0.69004) + CERH3_L12 (x(Rh) 0.75) |
| CeRh-24Bou.tdb | 1229.18 | LIQUID (x(Rh) 0.42101) + CE5RH4 (x(Rh) 0.44444) + CERH_B33 (x(Rh) 0.5) |
| CeRh-24Bou.tdb | 1189.27 | CERH_B33 (x(Rh) 0.5) + LIQUID (x(Rh) 0.58229) + CERH2_C15 (x(Rh) 0.66667) |
| CeRh-24Bou.tdb | 1082.66 | LIQUID (x(Rh) 0.37378) + CE3RH2 (x(Rh) 0.4) + CE5RH4 (x(Rh) 0.44444) |
| CeRh-24Bou.tdb | 1000 | FCC_A1 (x(Rh) 0) + BCC_A2 (x(Rh) 0) + LIQUID (x(Rh) 0.04978) |
| CeRh-24Bou.tdb | 993.98 | LIQUID (x(Rh) 0.35012) + CE5RH3 (x(Rh) 0.375) + CE3RH2 (x(Rh) 0.4) |
| CeRh-24Bou.tdb | 979.38 | CE7RH3_D102 (x(Rh) 0.3) + LIQUID (x(Rh) 0.34299) + CE5RH3 (x(Rh) 0.375) |
| CeRh-24Bou.tdb | 892.47 | FCC_A1 (x(Rh) 0) + LIQUID (x(Rh) 0.15683) + CE7RH3_D102 (x(Rh) 0.3) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-RH.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-RH.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
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
