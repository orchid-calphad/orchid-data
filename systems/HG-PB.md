# Hg–Pb system

> Hg–Pb system: 24 accepted literature values (phase equilibrium 13, phase transition 11) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HG-PB.html · Markdown: https://data.orchid-project.org/systems/HG-PB.md

24 accepted literature values from 1 paper(s) (experimental 20, model 4); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HG-PB.json) · [CSV](https://data.orchid-project.org/systems/HG-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HG-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HG-PB/HgPb-02Mai-LB.json) · [phases (6)](https://data.orchid-project.org/phases/pages/HG-PB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HG-PB.html) · [Markdown](https://data.orchid-project.org/systems/HG-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 20 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 11 |
| phase equilibrium | 13 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HgPb-02Mai-LB.tdb | A. Maitre, J.M. Fiorani, M. Vilasi, J. Phase Equilib., 23, 329-38(2002). [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) | `7e9650b9546b0f1f27d1694d8941a33904617de48101e6aada19029edc26b6f6` | [viewer](https://orchid-project.org/phase-diagrams/#HG-PB/HgPb-02Mai-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgPb-02Mai-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HgPb-02Mai-LB.tdb | 429.07 | LIQUID (x(Pb) 0.48553) + HGPB2_L10 (x(Pb) 0.66667) + FCC_A1 (x(Pb) 0.69489) |
| HgPb-02Mai-LB.tdb | 429.07 | LIQUID (x(Pb) 0.48601) + HGPB2_L10 (x(Pb) 0.66667) + FCC_A1 (x(Pb) 0.69512) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HG/HG-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HG/HG-PB.json)

## Other properties

### Phase transition (11)

Table: Phase transition, Hg–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 235.6 K | 235.6 | peritectic: Liq + Pb2Hg ↔ rhombo_A10(Hg); _alloy: Pb 0.666667_ | model | [1] Maitre 2002 | Table 2, p. 4, row 21; `ORC-6O3XWT2A3U` |  |
| Phase transition | 427.3 K | 427.3 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.32, Pb 0.68_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 14; `ORC-6YEYBIPW2J` |  |
| Phase transition | 428.6 K | 428.6 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.31, Pb 0.69_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 12; `ORC-HR6WHYOBQ7` |  |
| Phase transition | 428.7 K | 428.7 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.28, Pb 0.72_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 10; `ORC-GIMCLQ52WL` |  |
| Phase transition | 429 K | 429 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Pb 1_ | model | [1] Maitre 2002 | Table 2, p. 4, row 22; `ORC-32VQYHFRT7` |  |
| Phase transition | 429.3 K | 429.3 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.4, Pb 0.6_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 18; `ORC-ACKOV7WDEJ` |  |
| Phase transition | 429.4 K | 429.4 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.35, Pb 0.65_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 16; `ORC-Y5H6VQ6WEJ` |  |
| Phase transition | 453.2 K | 453.2 | other: 25 at.% Hg; _alloy: Hg 0.25, Pb 0.75_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 8; `ORC-XYAAVDIDC2` |  |
| Phase transition | 490 K | 490 | other: 21 at.% Hg; _alloy: Hg 0.21, Pb 0.79_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 6; `ORC-YC6OJNSHPO` |  |
| Phase transition | 513 K | 513 | other: 15 at.% Hg; _alloy: Hg 0.15, Pb 0.85_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 4; `ORC-FWEKSNWAIM` |  |
| Phase transition | 536 K | 536 | other: 10 at.% Hg; _alloy: Hg 0.1, Pb 0.9_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 2; `ORC-NMHNJFVF3P` |  |

### Phase equilibrium (13)

Table: Phase equilibrium, Hg–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 235.6 | Liquid + Rhombo_A10(Hg) + Pb2Hg; _Liquid: Hg 0.996, Pb 0.004; Rhombo_A10(Hg): Hg 0.994, Pb 0.006; Pb2Hg: Hg 0.326, Pb 0.674_ | model | [1] Maitre 2002 | Table 3, p. 4, row 1; `ORC-M4V3VXWBLF` |  |
| Phase composition |  | 378.7 | other: 80 at.% Hg; _liquid: Hg 0.8, Pb 0.2_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 20; `ORC-BVNQJAJL75` |  |
| Phase composition |  | 410.7 | other: 60 at.% Hg; _liquid: Hg 0.6, Pb 0.4_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 19; `ORC-HFWFY5L47W` |  |
| Phase composition |  | 429 | Liquid + Fcc(Pb) + Pb2Hg; _Liquid: Hg 0.506, Pb 0.494; Fcc(Pb): Hg 0.298, Pb 0.702; Pb2Hg: Hg 0.326, Pb 0.674_ | model | [1] Maitre 2002 | Table 3, p. 4, row 2; `ORC-E553KV47S2` |  |
| Phase composition |  | 457.7 | other: 40 at.% Hg; _liquid: Hg 0.4, Pb 0.6_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 17; `ORC-A6LFHEHGSH` |  |
| Phase composition |  | 478.7 | other: 35 at.% Hg; _liquid: Hg 0.35, Pb 0.65_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 15; `ORC-AHTHLU77SU` |  |
| Phase composition |  | 489.7 | other: 32 at.% Hg; _liquid: Hg 0.32, Pb 0.68_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 13; `ORC-2YSUKG7LWA` |  |
| Phase composition |  | 491.8 | other: 31 at.% Hg; _liquid: Hg 0.31, Pb 0.69_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 11; `ORC-4UWUHD3BP5` |  |
| Phase composition |  | 491.9 | other: 28 at.% Hg; _liquid: Hg 0.28, Pb 0.72_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 9; `ORC-N3U425XWOA` |  |
| Phase composition |  | 508.4 | other: 25 at.% Hg; _liquid: Hg 0.25, Pb 0.75_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 7; `ORC-UHRTCU4K3T` |  |
| Phase composition |  | 527.9 | other: 21 at.% Hg; _liquid: Hg 0.21, Pb 0.79_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 5; `ORC-OMGDHKJMHL` |  |
| Phase composition |  | 543.7 | other: 15 at.% Hg; _liquid: Hg 0.15, Pb 0.85_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 3; `ORC-74REEDCFGI` |  |
| Phase composition |  | 566.9 | other: 10 at.% Hg; _liquid: Hg 0.1, Pb 0.9_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 1; `ORC-WVZ5G2HJMC` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002). [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
