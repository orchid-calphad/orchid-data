# Mn–V system

> Mn–V system: 4 accepted literature values (phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MN-V.html · Markdown: https://data.orchid-project.org/systems/MN-V.md

4 accepted literature values from 1 paper(s) (experimental 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MN-V.json) · [CSV](https://data.orchid-project.org/systems/MN-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MN-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MN-V/MnV-91Hua-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/MN-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MN-V.html) · [Markdown](https://data.orchid-project.org/systems/MN-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MnV-91Hua-LB.tdb | W. Huang, Calphad, 15, 195-208(1991). [doi:10.1016/0364-5916(91)90018-F](https://doi.org/10.1016/0364-5916%2891%2990018-F) | `a91ef616c206517388d3c85bf5c3e55ddf6838cb37cc2ad03e9621a84df45f8b` | [viewer](https://orchid-project.org/phase-diagrams/#MN-V/MnV-91Hua-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnV-91Hua-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnV-91Hua-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MnV-91Hua-LB.tdb | 1377.57 | FCC_A1 (x(V) 0.00377) + CUB_A13 (x(V) 0.00615) + BCC_A2 (x(V) 0.00754) |
| MnV-91Hua-LB.tdb | 1277.07 | CUB_A13 (x(V) 0.07806) + BCC_A2 (x(V) 0.10325) + SIGMA_D8B (x(V) 0.15934) |
| MnV-91Hua-LB.tdb | 1162.73 | CUB_A13 (x(V) 0.05694) + CBCC_A12 (x(V) 0.08481) + SIGMA_D8B (x(V) 0.1488) |
| MnV-91Hua-LB.tdb | 1016.67 | CBCC_A12 (x(V) 0.06636) + SIGMA_OLD (x(V) 0.1415) + SIGMA_D8B (x(V) 0.14195) |
| MnV-91Hua-LB.tdb | 479.35 | SIGMA_OLD (x(V) 0.35057) + SIGMA_D8B (x(V) 0.35569) + BCC_A2 (x(V) 0.65686) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MN/MN-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MN/MN-V.json)

## Other properties

### Phase transition (4)

Table: Phase transition, Mn–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1183 K | 1183 | @-a | experimental | [1] Huang 1991; _cites ref. 9_ | p. 4 | “The phase equilibrium data, including yt6=p at 1380 K and &=pto at 1293 K by Hellawell and Hume-Rothery (B), and @-a at 1183 K and the 6=c congruent (9) were selected. To transformation at 1323 K, 75 at% Mn by Waterstrat” |
| Phase transition | 1293 K | 1293 | &=pto | experimental | [1] Huang 1991; _cites ref. 8_ | p. 4 | “The phase equilibrium data, including yt6=p at 1380 K and &=pto at 1293 K by Hellawell and Hume-Rothery (B), and @-a at 1183 K and the 6=c congruent (9) were selected. To transformation at 1323 K, 75 at% Mn by Waterstrat” |
| Phase transition | 1323 K | 1323 | congruent transformation | experimental | [1] Huang 1991; _cites ref. 9_ | p. 4 | “The phase equilibrium data, including yt6=p at 1380 K and &=pto at 1293 K by Hellawell and Hume-Rothery (B), and @-a at 1183 K and the 6=c congruent (9) were selected. To transformation at 1323 K, 75 at% Mn by Waterstrat” |
| Phase transition | 1380 K | 1380 | yt6=p | experimental | [1] Huang 1991; _cites ref. 8_ | p. 4 | “The phase equilibrium data, including yt6=p at 1380 K and &=pto at 1293 K by Hellawell and Hume-Rothery (B), and @-a at 1183 K and the 6=c congruent (9) were selected. To transformation at 1323 K, 75 at% Mn by Waterstrat” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Weiming Huang, A Thermodynamic Analysis of the Mn-V And Fe-Mn-V Systems, Calphad 15, 195-208 (1991). [doi:10.1016/0364-5916(91)90018-f](https://doi.org/10.1016/0364-5916%2891%2990018-f)

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
