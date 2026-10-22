# Al–Be system

> Al–Be system: 5 accepted literature values (activity / EMF / Gibbs energy 3, invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-BE.html · Markdown: https://data.orchid-project.org/systems/AL-BE.md

5 accepted literature values from 1 paper(s) (experimental 4, model 1); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-BE.json) · [CSV](https://data.orchid-project.org/systems/AL-BE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-BE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-BE/AlBe-04Pan-LB.json) · [Markdown](https://data.orchid-project.org/systems/AL-BE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
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

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Be system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 920.15 | eutectic |  | experimental | [1] Pan 2004; _cites Haas 1930_ | p. 3 | “By means of thermal analysis and optical microscopy, Kroll \[13\] as well as Haas and Uno \[14\] reported the eutectic point to be at 640 ◦ C and 4.1 at.% Be, and at 647 ◦ C and 4.1 at.% Be, respectively.” |
| 913.15 | eutectic |  | experimental | [1] Pan 2004; _cites Kroll 1926_ | p. 3 | “By means of thermal analysis and optical microscopy, Kroll \[13\] as well as Haas and Uno \[14\] reported the eutectic point to be at 640 ◦ C and 4.1 at.% Be, and at 647 ◦ C and 4.1 at.% Be, respectively.” |

## Other properties

### Activity / EMF / Gibbs energy (3)

Table: Activity / EMF / Gibbs energy, Al–Be system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity coefficient; _printed: activity coefficient_ | 4.64 unspecified | 1600 |  | experimental | [1] Pan 2004; _cites Bienvenu 1967_ | p. 6 | “In accordance with the parameters obtained in the present work, the calculated activity coefficient for Al in a dilute solution of liquid Be at 1600 K is 5.2, which agrees with the measured value of 4.64 \[32\].” |
| Activity coefficient; _printed: activity coefficient_ | 5.2 unspecified | 1600 |  | model | [1] Pan 2004 | p. 6 | “In accordance with the parameters obtained in the present work, the calculated activity coefficient for Al in a dilute solution of liquid Be at 1600 K is 5.2, which agrees with the measured value of 4.64 \[32\].” |
| Activity coefficient; _printed: activity coefficient_ | 4.64 unspecified | 1600 |  | experimental | [1] Pan 2004; _cites Bienvenu 1967_ | p. 3 | “Using the distribution method, Bienvenu et al. \[32\] reported the activity coefficient for Al in a dilute solution of liquid Be as 4.64 at 1600 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zhu Pan, Yong Du, B.Y. Huang, Yong Liu, R.C. Wang, A thermodynamic description of the Al–Be system: Modeling and experiment, Calphad 28, 371-378 (2004). [doi:10.1016/j.calphad.2004.12.003](https://doi.org/10.1016/j.calphad.2004.12.003)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
