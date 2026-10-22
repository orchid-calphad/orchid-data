# Mg–Na system

> Mg–Na system: 9 accepted literature values (invariant reaction 8, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-NA.html · Markdown: https://data.orchid-project.org/systems/MG-NA.md

9 accepted literature values from 1 paper(s) (experimental 5, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-NA.json) · [CSV](https://data.orchid-project.org/systems/MG-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-NA/MgNa-06Zha.json) · [Markdown](https://data.orchid-project.org/systems/MG-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgNa-06Zha.tdb | S. Zhang, Q. Han, Z.-K. Liu, J. Alloys Compd., 419, 91-97(2006). [doi:10.1016/j.jallcom.2005.10.002](https://doi.org/10.1016/j.jallcom.2005.10.002) | `715512f518dab4d902ed3b116783dae6ee3550b790c9a1e4fb11a8a8f8e96e20` | [viewer](https://orchid-project.org/phase-diagrams/#MG-NA/MgNa-06Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgNa-06Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgNa-06Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MgNa-06Zha.tdb | 910 | HCP_A3 (x(Na) 0.00326) + LIQUID#2 (x(Na) 0.021) + LIQUID (x(Na) 0.92704) |
| MgNa-06Zha.tdb | 370.8 | HCP_A3 (x(Na) 0) + LIQUID (x(Na) 0.99982) + BCC_A2 (x(Na) 0.99997) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MG/MG-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mg–Na system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1159 | Gas -> liquid1 + liquid2 | Gas: Na 0.8407; liquid1: Na 0.0593; liquid2: Na 0.8858 | model | [1] Zhang 2006 | Table 4, p. 5, row 1 |  |
| 911 | Liquid1 -> hcp(Mg) + liquid2 | Liquid1: Na 0.02 | experimental | [1] Zhang 2006; _cites Mathewson 1906_ | Table 4, p. 5, row 4 |  |
| 911 | Liquid1 -> hcp(Mg) + liquid2 | Liquid1: Na 0.021; liquid2: Na 0.986 | experimental | [1] Zhang 2006; _cites Lantratov 1973_ | Table 4, p. 5, row 5 |  |
| 910 | Liquid1 -> hcp(Mg) + liquid2 | Liquid1: Na 0.016; liquid2: Na 0.927 | experimental | [1] Zhang 2006; _cites Klemm 1967_ | Table 4, p. 5, row 6 |  |
| 910 | Liquid1 -> hcp(Mg) + liquid2 | Liquid1: Na 0.021; hcp(Mg): Na 3.300e-4; liquid2: Na 0.927 | model | [1] Zhang 2006 | Table 4, p. 5, row 3 |  |
| 371 | Liquid2 -> hcp(Mg) + bcc(Na) | Liquid2: Na 0.9998; hcp(Mg): Na 4.150e-6; bcc(Na): Na 1 | model | [1] Zhang 2006 | Table 4, p. 5, row 7 |  |
| 371 | Liquid2 -> hcp(Mg) + bcc(Na) |  | experimental | [1] Zhang 2006; _cites Klemm 1967_ | Table 4, p. 5, row 9 |  |
| 371 | Liquid2 -> hcp(Mg) + bcc(Na) |  | experimental | [1] Zhang 2006; _cites Mathewson 1906_ | Table 4, p. 5, row 8 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Mg–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1157 K | 1157 | Gas -> liquid2; _Gas: Na 0.97016_ | model | [1] Zhang 2006 | Table 4, p. 5, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Qingyou Han, Zi-Kui Liu, Thermodynamic modeling of the Al–Mg–Na system, Journal of Alloys and Compounds 419, 91-97 (2006). [doi:10.1016/j.jallcom.2005.10.002](https://doi.org/10.1016/j.jallcom.2005.10.002)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
