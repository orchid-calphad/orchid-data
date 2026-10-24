# Nb–Y system

> Nb–Y system: 3 accepted literature values (phase transition 2, invariant reaction 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-Y.html · Markdown: https://data.orchid-project.org/systems/NB-Y.md

3 accepted literature values from 1 paper(s) (model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NB-Y.json) · [CSV](https://data.orchid-project.org/systems/NB-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NB-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-Y/NbY-08Mat.json) · [phases (4)](https://data.orchid-project.org/phases/pages/NB-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NB-Y.html) · [Markdown](https://data.orchid-project.org/systems/NB-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NbY-08Mat.tdb | N. Mattern, M. Zinkevich, W. Loeser, G. Behr, J. Acker, J. Phase Equilib. Diffus., 29, 141-55(2008). [doi:10.1007/s11669-007-9243-2](https://doi.org/10.1007/s11669-007-9243-2) | `5eb6de94dbc7d3b27579ebe91ad5a8b0a8bf269693625822ab42f0562eaff676` | [viewer](https://orchid-project.org/phase-diagrams/#NB-Y/NbY-08Mat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbY-08Mat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbY-08Mat.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NbY-08Mat.tdb | 2683.02 | BCC_A2 (x(Y) 3.900e-4) + LIQUID#2 (x(Y) 0.04371) + LIQUID (x(Y) 0.53858) |
| NbY-08Mat.tdb | 1751.07 | LIQUID (x(Y) 0.982) + BCC_A2 (x(Y) 0.99998) + HCP_A3 (x(Y) 0.99999) |
| NbY-08Mat.tdb | 1741.32 | BCC_A2 (x(Y) 3.000e-5) + LIQUID (x(Y) 0.9765) + HCP_A3 (x(Y) 0.99999) |
| NbY-08Mat.tdb | 1741.32 | BCC_A2 (x(Y) 3.000e-5) + LIQUID (x(Y) 0.9765) + HCP_A3 (x(Y) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NB/NB-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NB/NB-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nb–Y system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1743.15 | eutectic |  | model | [1] Mattern 2008; _cites Palenzona 1991_ [doi](https://doi.org/10.1007/bf02645717) | p. 7; `ORC-2XETEZWOYC.516897` | “Using regular and subregular interaction parameters for the liquid phase, it was possible to obtain a good fit of the eutectic and monotectic temperatures, 1470 ± 10 C and 2400 C, respectively.\[16\]” |

## Other properties

### Phase transition (2)

Table: Phase transition, Nb–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1751.15 K | 1751.15 | polymorphic | model | [1] Mattern 2008; _cites Palenzona 1991_ [doi](https://doi.org/10.1007/bf02645717) | p. 7; `ORC-TIJAPKI4MF` | “The calculated solid solubilities of Y in Nb and vice versa are around 0.1 at.% in agreement with experimental reports,\[16\] while niobium has virtually no effect on the temperature of polymorphic cph M bcc transformation in yttrium metal (1478 C).” |
| Phase transition | 2673.15 K | 2673.15 | other | model | [1] Mattern 2008; _cites Palenzona 1991_ [doi](https://doi.org/10.1007/bf02645717) | p. 7; `ORC-2XETEZWOYC.af8ae2` | “Using regular and subregular interaction parameters for the liquid phase, it was possible to obtain a good fit of the eutectic and monotectic temperatures, 1470 ± 10 C and 2400 C, respectively.\[16\]” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. N. Mattern, M. Zinkevich, W. Löser, G. Behr, J. Acker, Experimental and Thermodynamic Assessment of the Nb-Ni-Y System, J Phs Eqil and Diff 29, 141-155 (2008). [doi:10.1007/s11669-007-9243-2](https://doi.org/10.1007/s11669-007-9243-2)

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
