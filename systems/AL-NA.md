# Al–Na system

> Al–Na system: 8 accepted literature values (invariant reaction 8) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-NA.html · Markdown: https://data.orchid-project.org/systems/AL-NA.md

8 accepted literature values from 1 paper(s) (experimental 4, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-NA.json) · [CSV](https://data.orchid-project.org/systems/AL-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-NA/AlNa-06Zha.json) · [Markdown](https://data.orchid-project.org/systems/AL-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlNa-06Zha.tdb | S. Zhang, Q. Han, Z.-K. Liu, J. Alloys Compd., 419, 91-97(2006). [doi:10.1016/j.jallcom.2005.10.002](https://doi.org/10.1016/j.jallcom.2005.10.002) | `e3af44669614f4fe1012baee8b21f8a53d85adc328a1487b27d7cece28558c00` | [viewer](https://orchid-project.org/phase-diagrams/#AL-NA/AlNa-06Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlNa-06Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlNa-06Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlNa-06Zha.tdb | 933.47 | FCC_A1 (x(Na) 0) + LIQUID#2 (x(Na) 0) + LIQUID (x(Na) 1) |
| AlNa-06Zha.tdb | 932.28 | FCC_A1 (x(Na) 2.000e-5) + LIQUID#2 (x(Na) 0.00146) + LIQUID (x(Na) 1) |
| AlNa-06Zha.tdb | 932.27 | FCC_A1 (x(Na) 2.000e-5) + LIQUID#2 (x(Na) 0.00142) + LIQUID (x(Na) 1) |
| AlNa-06Zha.tdb | 370.92 | FCC_A1 (x(Na) 0) + BCC_A2 (x(Na) 0.9999) + LIQUID (x(Na) 1) |
| AlNa-06Zha.tdb | 370.92 | FCC_A1 (x(Na) 0) + BCC_A2 (x(Na) 0.9999) + LIQUID (x(Na) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Na system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1157 | Gas -> liquid1 + liquid2 | Gas: Na 1; liquid1: Na 0.00238; liquid2: Na 1 | model | [1] Zhang 2006 | Table 2, p. 4, row 1 |  |
| 932 | Liquid1 -> fcc(Al) + liquid2 | Liquid1: Na 0.0014; fcc(Al): Na 2.000e-5 | experimental | [1] Zhang 2006; _cites Ransley 1950_ | Table 2, p. 4, row 6 |  |
| 932 | Liquid1 -> fcc(Al) + liquid2 | Liquid1: Na 0.0014; fcc(Al): Na 2.000e-5; liquid2: Na 1 | model | [1] Zhang 2006 | Table 2, p. 4, row 2 |  |
| 932 | Liquid1 -> fcc(Al) + liquid2 | Liquid1: Na 0.0018; fcc(Al): Na 2.300e-5 | model | [1] Zhang 2006; _cites Murray 1983_ [doi](https://doi.org/10.1007/bf02868094) | Table 2, p. 4, row 3 |  |
| 932 | Liquid1 -> fcc(Al) + liquid2 | Liquid1: Na 0.0018 | experimental | [1] Zhang 2006; _cites Fink 1948_ | Table 2, p. 4, row 5 |  |
| 930 | Liquid1 -> fcc(Al) + liquid2 |  | experimental | [1] Zhang 2006; _cites Mathewson 1906_ | Table 2, p. 4, row 4 |  |
| 371 | Liquid2 -> fcc(Al) + bcc(Na) | Liquid2: Na 0.9999; fcc(Al): Na 0; bcc(Na): Na 1 | model | [1] Zhang 2006 | Table 2, p. 4, row 7 |  |
| 371 | Liquid2 -> fcc(Al) + bcc(Na) |  | experimental | [1] Zhang 2006; _cites Mathewson 1906_ | Table 2, p. 4, row 8 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Qingyou Han, Zi-Kui Liu, Thermodynamic modeling of the Al–Mg–Na system, Journal of Alloys and Compounds 419, 91-97 (2006). [doi:10.1016/j.jallcom.2005.10.002](https://doi.org/10.1016/j.jallcom.2005.10.002)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
