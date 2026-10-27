# Te–Yb system

> Te–Yb system: 6 accepted literature values (invariant reaction 4, phase transition 2) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TE-YB.html · Markdown: https://data.orchid-project.org/systems/TE-YB.md

6 accepted literature values from 1 paper(s) (experimental 3, model 3); 0 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/TE-YB.json) · [CSV](https://data.orchid-project.org/systems/TE-YB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#TE-YB) · [phases (6)](https://data.orchid-project.org/phases/pages/TE-YB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/TE-YB.html) · [Markdown](https://data.orchid-project.org/systems/TE-YB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 2 |

Convex hulls: [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/TE/TE-YB.json) · [CALPHAD hull YbTe-15Wan](https://data.orchid-project.org/hulls/calphad-sgte/TE/TE-YB--YbTe-15Wan.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Te–Yb system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1093 | eutectic: Liq -> (γYb) + TeYb | (γYb): Te 0; TeYb: Te 0.5 | experimental | [1] Ghamri 2015; _cites Kh 1970_ | Table 5, p. 6, row 5; `ORC-TOSSOPGGYT` |  |
| 1090 | eutectic: Liq -> (γYb) + TeYb | L: Te 0.005; (γYb): Te 0; TeYb: Te 0.5 | model | [1] Ghamri 2015 | Table 5, p. 6, row 6; `ORC-LS5LBW26TA` |  |
| 726 | eutectic: Liq -> (Te) + TeYb | (Te): Te 1; TeYb: Te 0.5 | experimental | [1] Ghamri 2015; _cites Kh 1970_ | Table 5, p. 6, row 1; `ORC-4R67FNHY4U` |  |
| 721.7 | eutectic: Liq -> (Te) + TeYb | L: Te 0.9967; (Te): Te 1; TeYb: Te 0.5 | model | [1] Ghamri 2015 | Table 5, p. 6, row 2; `ORC-ICVRHJXPBF` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Te–Yb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2003 K | 2003 | congruent melting: Liq -> TeYb; _L: Te 0.5; TeYb: Te 0.5_ | experimental | [1] Ghamri 2015; _cites Kh 1970_ | Table 5, p. 6, row 3; `ORC-NC54NZTUNU` |  |
| Phase transition | 2003.46 K | 2003.46 | congruent melting: Liq -> TeYb; _L: Te 0.5; TeYb: Te 0.5_ | model | [1] Ghamri 2015 | Table 5, p. 6, row 4; `ORC-I5VFHQNYDG` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015). [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

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
