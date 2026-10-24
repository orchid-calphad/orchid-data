# Cd–Zn system

> Cd–Zn system: 4 accepted literature values (invariant reaction 3, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-ZN.html · Markdown: https://data.orchid-project.org/systems/CD-ZN.md

4 accepted literature values from 1 paper(s) (experimental 3, model 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-ZN.json) · [CSV](https://data.orchid-project.org/systems/CD-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-ZN/CdZn-93Zab.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CD-ZN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-ZN.html) · [Markdown](https://data.orchid-project.org/systems/CD-ZN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdZn-93Zab.tdb | L.A. Zabdyr, W. Zakulski, Arch. Metall., 38, 3-18(1993). | `dfa8770557cf58af574a6687ea7c8bd331b6d53f21575109a35334ceb42c46c3` | [viewer](https://orchid-project.org/phase-diagrams/#CD-ZN/CdZn-93Zab.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdZn-93Zab.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdZn-93Zab.json) |
| CdZn-97Zab-LB.tdb | L.A. Zabdyr, Calphad, 21, 349-58(1997). [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) | `be5c0e38c1191905f989fb320942404c54a19220a6c53a6ad067a6484a3792c9` | [viewer](https://orchid-project.org/phase-diagrams/#CD-ZN/CdZn-97Zab-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdZn-97Zab-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdZn-97Zab-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdZn-93Zab.tdb | 540.24 | HCP_A3 (x(Zn) 0.0439) + LIQUID (x(Zn) 0.24371) + HCP_A3#2 (x(Zn) 0.98778) |
| CdZn-97Zab-LB.tdb | 538.16 | HCP_A3 (x(Zn) 0.0453) + LIQUID (x(Zn) 0.25957) + HCP_A3#2 (x(Zn) 0.9885) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-ZN.json) · [CALPHAD hull CdZn-93Zab](https://data.orchid-project.org/hulls/calphad-sgte/CD/CD-ZN--CdZn-93Zab.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Zn system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 539 | L \<-> (Zn) + (Cd) |  | experimental | [1] Liu 2009; _cites Record 2003_ [doi](https://doi.org/10.1016/s0966-9795%2803%2900157-2) | Table 6, p. 5, row 4 |  |
| 538 | L \<-> (Zn) + (Cd) | L: Zn 0.2596; (Zn): Zn 0.9885; (Cd): Zn 0.0453 | experimental | [1] Liu 2009; _cites Adjadj 2007_ [doi](https://doi.org/10.1016/j.jallcom.2006.04.051) | Table 6, p. 5, row 3 |  |
| 537.54 | L \<-> (Zn) + (Cd) | L: Zn 0.2585; (Zn): Zn 0.9905; (Cd): Zn 0.0418 | model | [1] Liu 2009 | Table 6, p. 5, row 5 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Cd–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 594.11 K | 594.11 | congruent melting: L \<-> (Cd); _L: Zn 0; (Cd): Zn 0_ | experimental | [1] Liu 2009; _cites Adjadj 2007_ [doi](https://doi.org/10.1016/j.jallcom.2006.04.051) | Table 6, p. 5, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009). [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006)

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
