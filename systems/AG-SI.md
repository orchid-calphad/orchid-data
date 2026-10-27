# Ag–Si system

> Ag–Si system: 9 accepted literature values (invariant reaction 5, phase transition 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-SI.html · Markdown: https://data.orchid-project.org/systems/AG-SI.md

9 accepted literature values from 1 paper(s) (experimental 6, model 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-SI.json) · [CSV](https://data.orchid-project.org/systems/AG-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-SI/AgSi-85Sau.json) · [phases (5)](https://data.orchid-project.org/phases/pages/AG-SI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-SI.html) · [Markdown](https://data.orchid-project.org/systems/AG-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgSi-85Sau.tdb | N. Saunders, Calphad, 9, 297-309(1985). [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) | `7730593a39e0f7f466005466e8aeabd98fa1f7ec7845cdc7935fb5e147ac2e23` | [viewer](https://orchid-project.org/phase-diagrams/#AG-SI/AgSi-85Sau.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgSi-85Sau.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgSi-85Sau.json) |
| AgSi-88Che-LB.tdb | P.-Y. Chevalier, Thermochim. Acta, 130, 33-41(1988). [doi:10.1016/0040-6031(88)87048-5](https://doi.org/10.1016/0040-6031%2888%2987048-5) | `97dc06551f22e1b3e7315d99126e04f9ad50ab3bf175d8ee10475327d8d25f52` | [viewer](https://orchid-project.org/phase-diagrams/#AG-SI/AgSi-88Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgSi-88Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgSi-88Che-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgSi-85Sau.tdb | 1234.93 | FCC_A1 (x(Si) 0) + LIQUID (x(Si) 0) + DIAMOND_A4 (x(Si) 1) |
| AgSi-85Sau.tdb | 1123.19 | FCC_A1 (x(Si) 6.700e-4) + LIQUID (x(Si) 0.09423) + DIAMOND_A4 (x(Si) 1) |
| AgSi-85Sau.tdb | 1123.18 | FCC_A1 (x(Si) 6.700e-4) + LIQUID (x(Si) 0.09415) + DIAMOND_A4 (x(Si) 1) |
| AgSi-88Che-LB.tdb | 1110.21 | FCC_A1 (x(Si) 0) + LIQUID (x(Si) 0.10041) + DIAMOND_A4 (x(Si) 1) |
| AgSi-88Che-LB.tdb | 1110.21 | FCC_A1 (x(Si) 0) + LIQUID (x(Si) 0.1004) + DIAMOND_A4 (x(Si) 1) |
| AgSi-88Che-LB.tdb | 1110.21 | FCC_A1 (x(Si) 0) + LIQUID (x(Si) 0.1004) + DIAMOND_A4 (x(Si) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-SI.json) · [CALPHAD hull AgSi-85Sau](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-SI--AgSi-85Sau.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Si system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1128 | eutectic: liquid -> Ag(f.c.c.) + dia | L: Si 0.132 | experimental | [1] Chevalier 1988; _cites Gottardi 1957_ | Table 2, p. 5, row 7; `ORC-N4RM64ZHTO` |  |
| 1121 | eutectic: liquid -> Ag(f.c.c.) + dia | L: Si 0.107 | experimental | [1] Chevalier 1988; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | Table 2, p. 5, row 9; `ORC-QVPNN6MXNT` |  |
| 1113 | eutectic: liquid -> Ag(f.c.c.) + dia | L: Si 0.106 | experimental | [1] Chevalier 1988; _cites Hager 1948_ | Table 2, p. 5, row 8; `ORC-5PACAXB5TC` |  |
| 1110.3 | eutectic: liquid -> Ag(f.c.c.) + dia | L: Si 0.1; dia: Si 0.999998 | model | [1] Chevalier 1988 | Table 2, p. 5, row 5; `ORC-ABJD4XWU7G` |  |
| 1098 | eutectic: liquid -> Ag(f.c.c.) + dia | L: Si 0.154 | experimental | [1] Chevalier 1988; _cites Arrivaut 1908_ [doi](https://doi.org/10.1002/zaac.19080600128) | Table 2, p. 5, row 6; `ORC-X2BTKV7I6Z` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Ag–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1234 K | 1234 | Ag f.c.c. -> Ag(liq); _Ag f.c.c.: Si 0_ | experimental | [1] Chevalier 1988; _cites Hultgren 1973_ | Table 2, p. 5, row 2; `ORC-X3WIHND6XB` |  |
| Phase transition | 1235.08 K | 1235.08 | Ag f.c.c. -> Ag(liq); _Ag f.c.c.: Si 0_ | model | [1] Chevalier 1988 | Table 2, p. 5, row 1; `ORC-VPMAHSSDL6` |  |
| Phase transition | 1685 K | 1685 | Si dia -> Si(liq); _Si dia: Si 1_ | experimental | [1] Chevalier 1988; _cites Hultgren 1973_ | Table 2, p. 5, row 4; `ORC-2S7QGIYJ5I` |  |
| Phase transition | 1687 K | 1687 | Si dia -> Si(liq); _Si dia: Si 1_ | model | [1] Chevalier 1988 | Table 2, p. 5, row 3; `ORC-2GSNBREGKP` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. P.-Y. Chevalier, Thermodynamic evalution of the Ag-Si system, Thermochimica Acta 130, 33-41 (1988). [doi:10.1016/0040-6031(88)87048-5](https://doi.org/10.1016/0040-6031%2888%2987048-5)

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
