# Li–Mg system

> Li–Mg system: 2 accepted literature values (invariant reaction 1, phase transition 1) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-MG.html · Markdown: https://data.orchid-project.org/systems/LI-MG.md

2 accepted literature values from 1 paper(s) (model 2); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-MG.json) · [CSV](https://data.orchid-project.org/systems/LI-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-MG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-00Bra.json) · [phases (4)](https://data.orchid-project.org/phases/pages/LI-MG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LI-MG.html) · [Markdown](https://data.orchid-project.org/systems/LI-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiMg-00Bra.tdb | M.H. Braga, L.F. Malheiros, M. Hamalainen, Thermochim. Acta, 344, 47-54(2000). [doi:10.1016/S0040-6031(99)00325-1](https://doi.org/10.1016/S0040-6031%2899%2900325-1) | `0c400e6056a51a6bf88f3ae0586285757eb9cd86759baad1e4013fb1d65d78a9` | [viewer](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-00Bra.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiMg-00Bra.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiMg-00Bra.json) |
| LiMg-11Wan.tdb | P. Wang, Y. Du, S. Liu, Calphad, 35, 523-32(2011). [doi:10.1016/j.calphad.2011.09.003](https://doi.org/10.1016/j.calphad.2011.09.003) | `7acf87c1787c5e807a313d0522c3d48367d3fb58f32e396f934ae580563feac5` | [viewer](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiMg-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiMg-11Wan.json) |
| LiMg-90Sau-LB.tdb | N. Saunders, Calphad, 14, 61-70 (1990). [doi:10.1016/0364-5916(90)90040-7](https://doi.org/10.1016/0364-5916%2890%2990040-7) | `ad16964d3d8f07a594977b9dd2f2a2cc274a1d4825e314c1fe8e719f5e6bf9f8` | [viewer](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-90Sau-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiMg-90Sau-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiMg-90Sau-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiMg-00Bra.tdb | 862.06 | BCC_A2 (x(Mg) 0.72385) + LIQUID (x(Mg) 0.7481) + HCP_A3 (x(Mg) 0.84636) |
| LiMg-11Wan.tdb | 859.65 | BCC_A2 (x(Mg) 0.75114) + LIQUID (x(Mg) 0.76946) + HCP_A3 (x(Mg) 0.8261) |
| LiMg-90Sau-LB.tdb | 865.16 | BCC_A2 (x(Mg) 0.76028) + LIQUID (x(Mg) 0.77423) + HCP_A3 (x(Mg) 0.83416) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-MG.json) · [CALPHAD hull LiMg-00Bra](https://data.orchid-project.org/hulls/calphad-sgte/LI/LI-MG--LiMg-00Bra.json) · [CALPHAD hull LiMg-90Sau-LB](https://data.orchid-project.org/hulls/calphad-sgte/LI/LI-MG--LiMg-90Sau-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Mg system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 865.2 | eutectic: Liquid -> bcc-A2 + hcp-A3 | L: Mg 0.774; bcc-A2: Mg 0.76; hcp-A3: Mg 0.834 | model | [1] (ed.) 1998 | Table I, p. 228, row 1; `ORC-IYZ2LDMQP3` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Li–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 867.4 K | 867.4 | other: Liquid -> bcc-A2; _L: Mg 0.727; bcc-A2: Mg 0.727_ | model | [1] (ed.) 1998 | Table I, p. 228, row 2; `ORC-FUOQGYJQO2` |  |

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
