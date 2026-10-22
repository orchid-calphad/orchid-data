# Ca–Ti system

> Ca–Ti system: 11 accepted literature values (invariant reaction 7, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-TI.html · Markdown: https://data.orchid-project.org/systems/CA-TI.md

11 accepted literature values from 1 paper(s) (experimental 1, model 10); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-TI.json) · [CSV](https://data.orchid-project.org/systems/CA-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-TI/CaTi-15Ham.json) · [Markdown](https://data.orchid-project.org/systems/CA-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaTi-15Ham.tdb | M. Hampl, R. Schmid-Fetzer, J. Mater. Sci., 50, 5822-32(2015). [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x) | `3a0af4e503124843d15f19ba39b9f2bb731c172b26a29ec11c19db18c0c00436` | [viewer](https://orchid-project.org/phase-diagrams/#CA-TI/CaTi-15Ham.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaTi-15Ham.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaTi-15Ham.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaTi-15Ham.tdb | 1938.56 | LIQUID (x(Ti) 0.00423) + LIQUID#2 (x(Ti) 0.99577) + BCC_A2 (x(Ti) 0.99691) |
| CaTi-15Ham.tdb | 1156.02 | LIQUID (x(Ti) 3.200e-4) + HCP_A3 (x(Ti) 0.99953) + BCC_A2 (x(Ti) 0.99992) |
| CaTi-15Ham.tdb | 1114.76 | BCC_A2 (x(Ti) 6.000e-5) + LIQUID (x(Ti) 2.600e-4) + HCP_A3 (x(Ti) 0.99963) |
| CaTi-15Ham.tdb | 716.03 | BCC_A2 (x(Ti) 0) + FCC_A1 (x(Ti) 0) + HCP_A3 (x(Ti) 0.99999) |
| CaTi-15Ham.tdb | 716.03 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0) + HCP_A3 (x(Ti) 0.99999) |
| CaTi-15Ham.tdb | 716.03 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0) + HCP_A3 (x(Ti) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Ti system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1938.15 | monotectic: Liquid'' = Liquid' + bTi |  | model | [1] Hampl 2015 | p. 5 | “The monotectic reaction Liquid00 = Liquid0 ? bTi calculated at 1665 °C will therefore not occur at a pressure of 1 bar; instead, at 1500 °C the reaction Gas (10-5 at.% Ti) ? bTi = Liquid (0.29 at.% Ti) occurs at 1 bar, and the two-phase equilibrium Gas ? bTi is adjoining from 1500 to 1666 °C.” |
| 1938.15 | L'' = L' + βTi | L'': Ti 0.99577; L': Ti 0.00423; βTi: Ti 0.99691 | model | [1] Hampl 2015 | Table 3, p. 5, row 1 |  |
| 1156.15 | L' + βTi = αTi | L': Ti 3.200e-4; βTi: Ti 0.99992 | model | [1] Hampl 2015 | Table 3, p. 5, row 2 |  |
| 1156.15 | peritectic: L0 + bTi = aTi |  | model | [1] Hampl 2015 | p. 5 | “The Ca solubility in aTi is higher than in bTi, producing the peritectic transformation type, L0 ? bTi = aTi, at 883 °C.” |
| 1115.15 | L' = βCa + αTi | L': Ti 2.600e-4; βCa: Ti 6.000e-5; αTi: Ti 0.99963 | model | [1] Hampl 2015 | Table 3, p. 5, row 3 |  |
| 1115.15 | eutectic |  | model | [1] Hampl 2015 | p. 5 | “Using a simplified, temperature independent, interaction = 75,000 J/mol, produces essentially parameter, L0;liquid Ca;Ti the same calculated solubility values from the eutectic at 842 °C up to about 900 °C, also reproducing the experimental data from \[6\] in that range.” |
| 716.15 | eutectic: βCa = αCa (+αTi) | αTi: Ti 0.99999 | model | [1] Hampl 2015 | Table 3, p. 5, row 4 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Ca–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1773.15 K | 1773.15 | Gas + bTi = Liquid | model | [1] Hampl 2015 | p. 5 | “The monotectic reaction Liquid00 = Liquid0 ? bTi calculated at 1665 °C will therefore not occur at a pressure of 1 bar; instead, at 1500 °C the reaction Gas (10-5 at.% Ti) ? bTi = Liquid (0.29 at.% Ti) occurs at 1 bar, and the two-phase equilibrium Gas ? bTi is adjoining from 1500 to 1666 °C.” |
| Phase transition | 1926.15 K | 1926.15 | other | model | [1] Hampl 2015 | p. 5 | “For that parameter setting, the monotectic temperature is lower, 1653 °C, compared to the value of 1665 °C in the finally assessed diagram using the value of L0;liquid = (50,000 ? 20T) J/mol.” |
| Phase transition | 1938.15 K | 1938.15 | other | model | [1] Hampl 2015 | p. 5 | “For that parameter setting, the monotectic temperature is lower, 1653 °C, compared to the value of 1665 °C in the finally assessed diagram using the value of L0;liquid = (50,000 ? 20T) J/mol.” |
| Phase transition | 1941.15 K | 1941.15 |  | experimental | [1] Hampl 2015 | p. 10 | “The consistent thermodynamic calculation reveals that a wide liquid miscibility gap must exist between Ca- and Ti-rich melts above the monotectic reaction, close to the melting point of Ti at 1668 °C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Milan Hampl, Rainer Schmid-Fetzer, Experimental investigation and thermodynamic assessment of the Al–Ca–Ti system, J Mater Sci 50, 5822-5832 (2015). [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x)

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
