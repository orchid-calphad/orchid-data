# Fe–In system

> Fe–In system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-IN.html · Markdown: https://data.orchid-project.org/systems/FE-IN.md

5 accepted literature values from 1 paper(s) (model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-IN.json) · [CSV](https://data.orchid-project.org/systems/FE-IN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-IN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-IN/FeIn-09Ohn.json) · [phases (5)](https://data.orchid-project.org/phases/pages/FE-IN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/FE-IN.html) · [Markdown](https://data.orchid-project.org/systems/FE-IN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FeIn-09Ohn.tdb | M. Ohno, K. Yoh, Mater. Trans. (JIM), 50, 1202-7(2009). [doi:10.2320/matertrans.MER2008437](https://doi.org/10.2320/matertrans.MER2008437) | `199a9d26cb33c1fc19d83bc5c712bdf033e7b64d1203820594afb3c0b4d1381b` | [viewer](https://orchid-project.org/phase-diagrams/#FE-IN/FeIn-09Ohn.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FeIn-09Ohn.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FeIn-09Ohn.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FeIn-09Ohn.tdb | 1744.39 | BCC_A2 (x(In) 0.00919) + LIQUID#2 (x(In) 0.05237) + LIQUID (x(In) 0.90297) |
| FeIn-09Ohn.tdb | 1611.67 | FCC_A1 (x(In) 0.00645) + BCC_A2 (x(In) 0.00846) + LIQUID (x(In) 0.93999) |
| FeIn-09Ohn.tdb | 1196.58 | FCC_A1 (x(In) 0.00389) + BCC_A2 (x(In) 0.0049) + LIQUID (x(In) 0.99033) |
| FeIn-09Ohn.tdb | 429.75 | BCC_A2 (x(In) 4.000e-5) + LIQUID (x(In) 1) + TETRAGONAL_A6 (x(In) 1) |
| FeIn-09Ohn.tdb | 429.75 | BCC_A2 (x(In) 4.000e-5) + TETRAGONAL_A6 (x(In) 1) + LIQUID (x(In) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-IN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-IN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Fe–In system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2423 | L ↔ L1 + L2 | L: In 0.4258 | model | [1] Ohno 2009 | Table 3, p. 3, row 1; `ORC-SJFW3K56KZ` |  |
| 1744 | L1 ↔ (δFe) + L2 | L1: In 0.0523; (δFe): In 0.0092; L2: In 0.903 | model | [1] Ohno 2009 | Table 3, p. 3, row 2; `ORC-XSRC4MOOP2` |  |
| 1617 | (δFe) ↔ (γFe) + L2 | (δFe): In 0.0085; (γFe): In 0.0067; L2: In 0.9388 | model | [1] Ohno 2009 | Table 3, p. 3, row 3; `ORC-WOHMOLRJVA` |  |
| 1195 | (γFe) + L2 ↔ (αFe) | (γFe): In 0.004; L2: In 0.9904; (αFe): In 0.0049 | model | [1] Ohno 2009 | Table 3, p. 3, row 4; `ORC-RWQCMY5AUV` |  |
| 429 | L2 ↔ (αFe) + In | L2: In 1; (αFe): In 0; In: In 1 | model | [1] Ohno 2009 | Table 3, p. 3, row 5; `ORC-CFS5PLYOH3` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Munekazu Ohno, Kanji Yoh, Thermodynamic Calculation of Phase Equilibria in As-Fe-In Ternary System Based on CALPHAD Approach, Mater. Trans. 50, 1202-1207 (2009). [doi:10.2320/matertrans.mer2008437](https://doi.org/10.2320/matertrans.mer2008437)

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
