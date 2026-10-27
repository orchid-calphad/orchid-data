# Al–Be system

> Al–Be system: 3 accepted literature values (activity / EMF / Gibbs energy 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-BE.html · Markdown: https://data.orchid-project.org/systems/AL-BE.md

3 accepted literature values from 1 paper(s) (experimental 2, model 1); 1 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-BE.json) · [CSV](https://data.orchid-project.org/systems/AL-BE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-BE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-BE/AlBe-04Pan-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AL-BE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-BE.html) · [Markdown](https://data.orchid-project.org/systems/AL-BE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| activity / EMF / Gibbs energy | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlBe-04Pan-LB.tdb | Z. Pan, Y. Du, B.Y. Huang, Y. Liu, R.C. Wang, Calphad, 28, 371-78(2004). [doi:10.1016/j.calphad.2004.12.003](https://doi.org/10.1016/j.calphad.2004.12.003) | `3a0e89b35a3ffb8e181601d2178da2ed6ba592c8637a714b2a1743c58a975e63` | [viewer](https://orchid-project.org/phase-diagrams/#AL-BE/AlBe-04Pan-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlBe-04Pan-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlBe-04Pan-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlBe-04Pan-LB.tdb | 1527 | LIQUID (x(Be) 0.98587) + HCP_A3 (x(Be) 0.99964) + BCC_A2 (x(Be) 0.99964) |
| AlBe-04Pan-LB.tdb | 1429.99 | LIQUID#2 (x(Be) 0.63429) + LIQUID (x(Be) 0.77704) + HCP_A3 (x(Be) 0.99822) |
| AlBe-04Pan-LB.tdb | 916.52 | FCC_A1 (x(Be) 0.00134) + LIQUID (x(Be) 0.0268) + HCP_A3 (x(Be) 0.99977) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-BE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-BE.json)

## Other properties

### Activity / EMF / Gibbs energy (3)

Table: Activity / EMF / Gibbs energy, Al–Be system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity coefficient; _printed: activity coefficient_ | 4.64 unspecified | 1600 |  | experimental | [1] Pan 2004; _cites Bienvenu 1967_ | p. 6; `ORC-KUIXL72UYP.0cc620` | “In accordance with the parameters obtained in the present work, the calculated activity coefficient for Al in a dilute solution of liquid Be at 1600 K is 5.2, which agrees with the measured value of 4.64 \[32\].” |
| Activity coefficient; _printed: activity coefficient_ | 5.2 unspecified | 1600 |  | model | [1] Pan 2004 | p. 6; `ORC-KUIXL72UYP.358b91` | “In accordance with the parameters obtained in the present work, the calculated activity coefficient for Al in a dilute solution of liquid Be at 1600 K is 5.2, which agrees with the measured value of 4.64 \[32\].” |
| Activity coefficient; _printed: activity coefficient_ | 4.64 unspecified | 1600 |  | experimental | [1] Pan 2004; _cites Bienvenu 1967_ | p. 3; `ORC-LFW4GN5WCE` | “Using the distribution method, Bienvenu et al. \[32\] reported the activity coefficient for Al in a dilute solution of liquid Be as 4.64 at 1600 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zhu Pan, Yong Du, B.Y. Huang, Yong Liu, R.C. Wang, A thermodynamic description of the Al–Be system: Modeling and experiment, Calphad 28, 371-378 (2004). [doi:10.1016/j.calphad.2004.12.003](https://doi.org/10.1016/j.calphad.2004.12.003)

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
