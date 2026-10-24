# Ag–Hg system

> Ag–Hg system: 6 accepted literature values (invariant reaction 5, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-HG.html · Markdown: https://data.orchid-project.org/systems/AG-HG.md

6 accepted literature values from 1 paper(s) (experimental 2, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-HG.json) · [CSV](https://data.orchid-project.org/systems/AG-HG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-HG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-HG/AgHg-12Liu.json) · [phases (7)](https://data.orchid-project.org/phases/pages/AG-HG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-HG.html) · [Markdown](https://data.orchid-project.org/systems/AG-HG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgHg-12Liu.tdb | Y. Liu, G. Wang, J. Wang, Y. Chen, Z. Long, Thermochim. Acta, 547, 83-88(2012). [doi:10.1016/j.tca.2012.08.004](https://doi.org/10.1016/j.tca.2012.08.004) | `39dc2bfee53e4124e77e582f6086c935e385083010df60383363770af64ac169` | [viewer](https://orchid-project.org/phase-diagrams/#AG-HG/AgHg-12Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgHg-12Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgHg-12Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgHg-12Liu.tdb | 548.23 | FCC_A1 (x(Hg) 0.37508) + AG11HG9_A3 (x(Hg) 0.45) + LIQUID (x(Hg) 0.95128) |
| AgHg-12Liu.tdb | 548.23 | FCC_A1 (x(Hg) 0.37505) + AG11HG9_A3 (x(Hg) 0.45) + LIQUID (x(Hg) 0.9512) |
| AgHg-12Liu.tdb | 399.22 | AG11HG9_A3 (x(Hg) 0.45) + AG11HG15 (x(Hg) 0.57692) + LIQUID (x(Hg) 0.99168) |
| AgHg-12Liu.tdb | 399.22 | AG11HG9_A3 (x(Hg) 0.45) + AG11HG15 (x(Hg) 0.57692) + LIQUID (x(Hg) 0.99166) |
| AgHg-12Liu.tdb | 399.22 | AG11HG9_A3 (x(Hg) 0.45) + AG11HG15 (x(Hg) 0.57692) + LIQUID (x(Hg) 0.9917) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-HG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-HG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Hg system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 549 | fcc + liq ↔ Ag11Hg9 | Ag11Hg9: Hg 0.45 | experimental | [1] Liu 2012; _cites Murphy 1931_ | Table 2, p. 4, row 2; `ORC-LHYCJ2G24M` |  |
| 549 | peritectic: fcc + liquid -> Ag11Hg9 |  | experimental | [1] Liu 2012; _cites Murphy 1931_ | p. 4; `ORC-T6KJLGLKYN` | “the peritectic reaction between fcc and liquid to form Ag11 Hg9 , the temperature of which was identified at 549.0 K by Murphy \[5\].” |
| 548.23 | fcc + liq ↔ Ag11Hg9 | fcc: Hg 0.375; liq: Hg 0.9512; Ag11Hg9: Hg 0.45 | model | [1] Liu 2012 | Table 2, p. 4, row 1; `ORC-B5WRW54UZG` |  |
| 399.22 | Ag11Hg9 + liq ↔ Ag11Hg15 | Ag11Hg9: Hg 0.9917; Ag11Hg15: Hg 0.576923 | model | [1] Liu 2012 | Table 2, p. 4, row 3; `ORC-WWUHWUCDF5` |  |
| 234.29 | liq ↔ Ag11Hg15 + (Hg) | Ag11Hg15: Hg 0.576923; (Hg): Hg 0.999868 | model | [1] Liu 2012 | Table 2, p. 4, row 4; `ORC-PBWOAB2N6H` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ag–Hg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 544.23 K | 544.23 | fcc + liquid -> Ag11Hg9 | model | [1] Liu 2012 | p. 4; `ORC-ET32T33BLQ` | “As noted, the calculated temperature for this invariant reaction, i.e. 544.23 K, is very close to the value proposed by Murphy \[5\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Guan Wang, Jiang Wang, Yang Chen, Zhaohui Long, Phase equilibria and thermodynamic functions for Ag–Hg and Cu–Hg binary systems, Thermochimica Acta 547, 83-88 (2012). [doi:10.1016/j.tca.2012.08.004](https://doi.org/10.1016/j.tca.2012.08.004)

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
