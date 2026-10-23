# Cr–Pb system

> Cr–Pb system: 2 accepted literature values (invariant reaction 1, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-PB.html · Markdown: https://data.orchid-project.org/systems/CR-PB.md

2 accepted literature values from 1 paper(s) (model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-PB.json) · [CSV](https://data.orchid-project.org/systems/CR-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-PB/CrPb-14Gos.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CR-PB.html) · [Markdown](https://data.orchid-project.org/systems/CR-PB.md)

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
| CrPb-14Gos.tdb | S. Gosse, J. Nucl. Mater., 449, 122-31(2014). [doi:10.1016/j.jnucmat.2014.03.011](https://doi.org/10.1016/j.jnucmat.2014.03.011) | `8d21769668212f9e46a9965b2ae00beb101675a27c350a76d348693466ec5acb` | [viewer](https://orchid-project.org/phase-diagrams/#CR-PB/CrPb-14Gos.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrPb-14Gos.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrPb-14Gos.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrPb-14Gos.tdb | 2007.97 | BCC_A2 (x(Pb) 0.00115) + LIQUID#2 (x(Pb) 0.14523) + LIQUID (x(Pb) 0.85477) |
| CrPb-14Gos.tdb | 601.02 | BCC_A2 (x(Pb) 0) + FCC_A1 (x(Pb) 0.99935) + LIQUID (x(Pb) 1) |
| CrPb-14Gos.tdb | 601.02 | BCC_A2 (x(Pb) 0) + FCC_A1 (x(Pb) 0.99935) + LIQUID (x(Pb) 1) |
| CrPb-14Gos.tdb | 601.02 | BCC_A2 (x(Pb) 0) + FCC_A1 (x(Pb) 0.99935) + LIQUID (x(Pb) 1) |
| CrPb-14Gos.tdb | 600.61 | BCC_A2 (x(Pb) 0) + LIQUID (x(Pb) 1) + FCC_A1 (x(Pb) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-PB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–Pb system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2008 | monotectic |  | model | [1] Gossé 2014 | p. 4 | “The monotectic reaction is calculated at 2008 K and the critical point of the liquid miscibility gap is 2186 K for a 50 at.% Cr composition (Fig. 3(a)).” |

## Other properties

### Phase transition (1)

Table: Phase transition, Cr–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2186 K | 2186 | other | model | [1] Gossé 2014 | p. 4 | “The monotectic reaction is calculated at 2008 K and the critical point of the liquid miscibility gap is 2186 K for a 50 at.% Cr composition (Fig. 3(a)).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Stéphane Gossé, Thermodynamic assessment of solubility and activity of iron, chromium, and nickel in lead bismuth eutectic, Journal of Nuclear Materials 449, 122-131 (2014). [doi:10.1016/j.jnucmat.2014.03.011](https://doi.org/10.1016/j.jnucmat.2014.03.011)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
