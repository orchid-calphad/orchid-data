# Hf–N system

> Hf–N system: 1 accepted literature values (formation 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-N.html · Markdown: https://data.orchid-project.org/systems/HF-N.md

1 accepted literature values from 1 paper(s) (model 1); 1 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-N.json) · [CSV](https://data.orchid-project.org/systems/HF-N.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-N) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-N/HfN-18Pan.json) · [phases (8)](https://data.orchid-project.org/phases/pages/HF-N.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HF-N.html) · [Markdown](https://data.orchid-project.org/systems/HF-N.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfN-18Pan.tdb | M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018). [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) | `e62247a157b146a136b12ccfa9ecf9f956b7458ba581bf6b57403474d3c50992` | [viewer](https://orchid-project.org/phase-diagrams/#HF-N/HfN-18Pan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfN-18Pan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfN-18Pan.tdb | 3650.81 | LIQUID (x(N) 0.26474) + FCC_A1 (x(N) 0.42525) + GAS (x(N) 0.9989) |
| HfN-18Pan.tdb | 3187.99 | LIQUID (x(N) 0.19761) + HCP_A3 (x(N) 0.25325) + FCC_A1 (x(N) 0.37756) |
| HfN-18Pan.tdb | 2542.71 | HCP_A3 (x(N) 0.2704) + FCC_A1 (x(N) 0.41203) + HF4N3 (x(N) 0.42857) |
| HfN-18Pan.tdb | 2478.01 | BCC_A2 (x(N) 0) + LIQUID (x(N) 0.01199) + HCP_A3 (x(N) 0.03726) |
| HfN-18Pan.tdb | 2245.01 | HCP_A3 (x(N) 0.27426) + HF3N2 (x(N) 0.4) + HF4N3 (x(N) 0.42857) |
| HfN-18Pan.tdb | 353.56 | HF3N2 (x(N) 0.4) + HF4N3 (x(N) 0.42857) + FCC_A1 (x(N) 0.49986) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-N.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-N.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Hf–N system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| HfN1.0 |  | -187.23 unspecified | 298.15 | model |  |  | [1] Pang 2018; _cites Mulokozi 1981_ | p. 3; `ORC-AL6GLWJ52P` | “The enthalpy of formation for HfN1.0 at 298 K calculated by Mulokozi \[39\] was -187.23 kJ/mol-atoms.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. Pang, Y. Peng, P. Zhou, Y. Du, Thermodynamic modeling of the Hf-N system, J min metall B Metall 54, 111-118 (2018). [doi:10.2298/jmmb170520055p](https://doi.org/10.2298/jmmb170520055p)

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
