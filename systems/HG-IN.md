# Hg–In system

> Hg–In system: 15 accepted literature values (invariant reaction 14, activity / EMF / Gibbs energy 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HG-IN.html · Markdown: https://data.orchid-project.org/systems/HG-IN.md

15 accepted literature values from 1 paper(s) (experimental 8, model 7); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HG-IN.json) · [CSV](https://data.orchid-project.org/systems/HG-IN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HG-IN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HG-IN/HgIn-09Gie.json) · [phases (9)](https://data.orchid-project.org/phases/pages/HG-IN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HG-IN.html) · [Markdown](https://data.orchid-project.org/systems/HG-IN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |
| activity / EMF / Gibbs energy | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HgIn-09Gie.tdb | W. Gierlotka, P. Jarosz, S.-W. Chen, Thermochim. Acta, 491, 29-34(2009). [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) | `6cbb48c284a17292d7463f9763dd9d558f02b687e79ed2dd78cb427988dfe7f6` | [viewer](https://orchid-project.org/phase-diagrams/#HG-IN/HgIn-09Gie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgIn-09Gie.json) |
| HgIn-98Han.tdb | S.C. Hansen, Calphad, 22, 359-73(1998). [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) | `0316d13b9f5f843aa316abf935f3d8a7c61d8d92285a8f9727844fc466717101` | [viewer](https://orchid-project.org/phase-diagrams/#HG-IN/HgIn-98Han.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgIn-98Han.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HgIn-09Gie.tdb | 366.84 | LIQUID (x(In) 0.83309) + FCC_A1 (x(In) 0.92928) + TETRAGONAL_A6 (x(In) 0.94442) |
| HgIn-98Han.tdb | 380.72 | LIQUID (x(In) 0.86366) + FCC_A1 (x(In) 0.93234) + TETRAGONAL_A6 (x(In) 0.9492) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HG/HG-IN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HG/HG-IN.json) · [CALPHAD hull HgIn-98Han](https://data.orchid-project.org/hulls/calphad-sgte/HG/HG-IN--HgIn-98Han.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hg–In system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 381 | L + Tetra -> FCC_A1 |  | experimental | [1] Gierlotka 2009; _cites ref. 21_ | Table 4, p. 6, row 9; `ORC-QX6SR2LQ6W` |  |
| 380.8 | L + Tetra -> FCC_A1 |  | model | [1] Gierlotka 2009 | Table 4, p. 6, row 10; `ORC-PHCHY4C5F5` |  |
| 254 | congruent melting: L -> HgIn | L: Hg 0.5, In 0.5; HgIn: Hg 0.5, In 0.5 | experimental | [1] Gierlotka 2009; _cites ref. 21_ | Table 4, p. 6, row 13; `ORC-DO77TKGQOG` |  |
| 253.6 | L + Rhombo -> FCO |  | model | [1] Gierlotka 2009 | Table 4, p. 6, row 2; `ORC-FGAK2SFND5` |  |
| 253 | L + Rhombo -> FCO |  | experimental | [1] Gierlotka 2009; _cites ref. 21_ | Table 4, p. 6, row 1; `ORC-3EABSWA23J` |  |
| 252.6 | congruent melting: L -> HgIn | L: Hg 0.5, In 0.5; HgIn: Hg 0.5, In 0.5 | model | [1] Gierlotka 2009 | Table 4, p. 6, row 14; `ORC-HLCDRWXIZ7` |  |
| 243.7 | eutectic: L -> HgIn + FCC_A1 | HgIn: Hg 0.5, In 0.5 | model | [1] Gierlotka 2009 | Table 4, p. 6, row 8; `ORC-IT7MZ633YQ` |  |
| 243 | eutectic: L -> HgIn + FCC_A1 | HgIn: Hg 0.5, In 0.5 | experimental | [1] Gierlotka 2009; _cites ref. 21_ | Table 4, p. 6, row 7; `ORC-BPO56FDGSB` |  |
| 236 | congruent melting: L -> Rhombo |  | experimental | [1] Gierlotka 2009; _cites ref. 21_ | Table 4, p. 6, row 11; `ORC-FMQS3POAF5` |  |
| 236 | eutectic: L -> FCO + HgIn | HgIn: Hg 0.5, In 0.5 | experimental | [1] Gierlotka 2009; _cites ref. 21_ | Table 4, p. 6, row 3; `ORC-UGVR7HGTAC` |  |
| 235.6 | eutectic: L -> FCO + HgIn | HgIn: Hg 0.5, In 0.5 | model | [1] Gierlotka 2009 | Table 4, p. 6, row 4; `ORC-FB2I3XSO6O` |  |
| 235.6 | congruent melting: L -> Rhombo |  | model | [1] Gierlotka 2009 | Table 4, p. 6, row 12; `ORC-SE6C2M3TR3` |  |
| 218 | HgIn + FCC_A1 -> HgIn2 | HgIn: Hg 0.5, In 0.5; HgIn2: Hg 0.333333, In 0.666667 | model | [1] Gierlotka 2009 | Table 4, p. 6, row 6; `ORC-BEA74KBOUN` |  |
| 218 | HgIn + FCC_A1 -> HgIn2 | HgIn: Hg 0.5, In 0.5; HgIn2: Hg 0.333333, In 0.666667 | experimental | [1] Gierlotka 2009; _cites ref. 21_ | Table 4, p. 6, row 5; `ORC-MUTX6Y2IQS` |  |

## Other properties

### Activity / EMF / Gibbs energy (1)

Table: Activity / EMF / Gibbs energy, Hg–In system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Vapour pressure; _printed: pressure_ | 4.070e-6 hPa | 900 |  | experimental | [1] Gierlotka 2009; _cites Kozin 1961_ | p. 3; `ORC-AXGJYRJBFR` | “The pressure of indium is negligible at experiment temperatures and equal 4.07E - 6 hPa at 900 K \[9\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009). [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020)

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
