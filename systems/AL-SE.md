# Al–Se system

> Al–Se system: 11 accepted literature values (phase transition 6, invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-SE.html · Markdown: https://data.orchid-project.org/systems/AL-SE.md

11 accepted literature values from 1 paper(s) (experimental 2, model 7, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-SE.json) · [CSV](https://data.orchid-project.org/systems/AL-SE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-SE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-SE/AlSe-19Shi.json) · [Markdown](https://data.orchid-project.org/systems/AL-SE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 7 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlSe-19Shi.tdb | C. Shi, B. Yang, B. Hu, Y. Du, S. Yao, J. Phase Equilib. Diffus., 40, 392-402(2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) | `990a49c151cafe47b8ee86155122c8030778d13fe2222d6d211fbec36f7b4128` | [viewer](https://orchid-project.org/phase-diagrams/#AL-SE/AlSe-19Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlSe-19Shi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlSe-19Shi.tdb | 903.09 | FCC_A1 (x(Se) 0) + LIQUID (x(Se) 0.03617) + AL2SE3 (x(Se) 0.6) |
| AlSe-19Shi.tdb | 903.09 | FCC_A1 (x(Se) 0) + LIQUID (x(Se) 0.03588) + AL2SE3 (x(Se) 0.6) |
| AlSe-19Shi.tdb | 903.09 | FCC_A1 (x(Se) 0) + LIQUID (x(Se) 0.03602) + AL2SE3 (x(Se) 0.6) |
| AlSe-19Shi.tdb | 494 | AL2SE3 (x(Se) 0.6) + HEXAGONAL_A8 (x(Se) 1) + LIQUID (x(Se) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-SE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-SE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Se system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 933.15 | eutectic: L -> (αAl) + Al2Se3 | (αAl): Se 0; Al2Se3: Se 0.6 | unspecified | [1] Shi 2019; _cites The 2019_ | Table 6, p. 9, row 1 |  |
| 929.25 | eutectic: L -> (αAl) + Al2Se3 | L: Se 0; (αAl): Se 0; Al2Se3: Se 0.6 | model | [1] Shi 2019 | Table 6, p. 9, row 3 |  |
| 924.25 | eutectic: L -> (αAl) + Al2Se3 | L: Se 0.001; (αAl): Se 0; Al2Se3: Se 0.6 | model | [1] Shi 2019 | Table 6, p. 9, row 2 |  |
| 494.05 | eutectic: L -> (Se) + Al2Se3 | L: Se 1; (Se): Se 0; Al2Se3: Se 0.6 | model | [1] Shi 2019 | Table 6, p. 9, row 5 |  |
| 493.15 | eutectic: L -> (Se) + Al2Se3 | (Se): Se 0; Al2Se3: Se 0.6 | unspecified | [1] Shi 2019; _cites The 2019_ | Table 6, p. 9, row 4 |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Al–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 493.15 K | 493.15 | L ? (Se) ? Al3Se4 | experimental | [1] Shi 2019 | p. 4 | “L ? (aAl) ? Al3Se4 and L ? (Se) ? Al3Se4, were determined to occur at about 660 C and 0.1 at.% Se and about 220 C and 99.9 at.% Se.” |
| Phase transition | 494.05 K | 494.05 | L ? Al2Se3 ? (Se) | model | [1] Shi 2019 | p. 7 | “In Fig. 5, the calculated invariant reactions L ? (Al) ? aAl2Se3 and L ? Al2Se3 ? (Se) lie at 651.1 C and 0.1 at.% Se and at 220.9 C and close to 100 at.% Se, respectively.” |
| Phase transition | 924.25 K | 924.25 | L ? (Al) ? aAl2Se3 | model | [1] Shi 2019 | p. 7 | “In Fig. 5, the calculated invariant reactions L ? (Al) ? aAl2Se3 and L ? Al2Se3 ? (Se) lie at 651.1 C and 0.1 at.% Se and at 220.9 C and close to 100 at.% Se, respectively.” |
| Phase transition | 933.15 K | 933.15 | L ? (aAl) ? Al3Se4 | experimental | [1] Shi 2019 | p. 4 | “L ? (aAl) ? Al3Se4 and L ? (Se) ? Al3Se4, were determined to occur at about 660 C and 0.1 at.% Se and about 220 C and 99.9 at.% Se.” |
| Phase transition | 1212.85 K | 1212.85 |  | model | [1] Shi 2019 | p. 7 | “The calculated melting temperature of Al2Se3 is 939.7 C.” |
| Phase transition | 1213.15 K | 1213.15 |  | model | [1] Shi 2019 | p. 7 | “In Fig. 6, the calculated melting temperature of Al2Se3 is 940.0 C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
