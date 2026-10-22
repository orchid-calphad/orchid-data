# Hg–Te system

> Hg–Te system: 36 accepted literature values (phase equilibrium 12, invariant reaction 10, formation 8, phase transition 6) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HG-TE.html · Markdown: https://data.orchid-project.org/systems/HG-TE.md

36 accepted literature values from 2 paper(s) (experimental 22, model 11, unspecified 3); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HG-TE.json) · [CSV](https://data.orchid-project.org/systems/HG-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HG-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HG-TE/HgTe-10Gie.json) · [Markdown](https://data.orchid-project.org/systems/HG-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 22 |
| model | 11 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 6 |
| phase equilibrium | 12 |
| formation | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HgTe-10Gie.tdb | W. Gierlotka, J. Alloys Compd., 494, 102-8(2010). [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) | `c1efc80be4426d7d90ed54d3813099f9aefae229ba3411c64d411a6e9c9ecdca` | [viewer](https://orchid-project.org/phase-diagrams/#HG-TE/HgTe-10Gie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgTe-10Gie.json) |
| HgTe-95Yan-LB.tdb | J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995). [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) | `d35628e6d9da010c601e3659dc676c9d84d2543881647cac6ce6fc7d5612f0bf` | [viewer](https://orchid-project.org/phase-diagrams/#HG-TE/HgTe-95Yan-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgTe-95Yan-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HgTe-10Gie.tdb | 940.55 | ZINCBLENDE_B3 (x(Te) 0.5) + LIQUID (x(Te) 0.52155) + ION (x(Te) 0.52677) |
| HgTe-10Gie.tdb | 762.92 | ION (x(Te) 0.09121) + LIQUID (x(Te) 0.09145) + ZINCBLENDE_B3 (x(Te) 0.5) |
| HgTe-10Gie.tdb | 682.81 | ZINCBLENDE_B3 (x(Te) 0.5) + ION (x(Te) 0.84299) + HEXAGONAL_A8 (x(Te) 1) |
| HgTe-95Yan-LB.tdb | 686.29 | ZINCBLENDE_B3 (x(Te) 0.5) + LIQUID (x(Te) 0.85286) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HG/HG-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HG/HG-TE.json) · [CALPHAD hull HgTe-95Yan-LB](https://data.orchid-project.org/hulls/calphad-sgte/HG/HG-TE--HgTe-95Yan-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hg–Te system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 684 | HgTe + Te = L | HgTe: Te 0.5; Te: Te 1 | experimental | [1] Gierlotka 2010; _cites Massalski 1986_ | Table 3, p. 4, row 9 |  |
| 684 | eutectic |  | experimental | [1] Gierlotka 2010 | p. 2 | “The system shows 2 invariant reactions: eutectic reaction between liquid, solid Hg and intermetallic compound HgTe at temperature 233 K and another eutectic between liquid, solid tellurium and intermetallic compound at 684 K.” |
| 683 | HgTe + Te = L | HgTe: Te 0.5; Te: Te 1 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 11 |  |
| 683 | HgTe + Te = L | HgTe: Te 0.5; Te: Te 1 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 10 |  |
| 675 | HgTe + Te = L | HgTe: Te 0.5; Te: Te 1 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 12 |  |
| 234 | Hg + HgTe = L | Hg: Te 0; HgTe: Te 0.5 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 2 |  |
| 234 | Hg + HgTe = L | Hg: Te 0; HgTe: Te 0.5 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 3 |  |
| 233 | eutectic |  | experimental | [1] Gierlotka 2010 | p. 2 | “The system shows 2 invariant reactions: eutectic reaction between liquid, solid Hg and intermetallic compound HgTe at temperature 233 K and another eutectic between liquid, solid tellurium and intermetallic compound at 684 K.” |
| 233 | Hg + HgTe = L | Hg: Te 0; HgTe: Te 0.5 | experimental | [1] Gierlotka 2010; _cites Massalski 1986_ | Table 3, p. 4, row 1 |  |
| 233 | Hg + HgTe = L | Hg: Te 0; HgTe: Te 0.5 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 4 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Hg–Te system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| HgTe |  | -44.02 kJ/mol (basis unstated) | 298 | model |  |  | [1] Gierlotka 2010; _cites Yang 1995_ [doi](https://doi.org/10.1016/0364-5916%2895%2900039-h) | Table 4, p. 4, row 7 |  |
| HgTe |  | -43.802 kJ/mol (basis unstated) | 298 | unspecified |  |  | [1] Gierlotka 2010; _cites Su 1981_ | Table 4, p. 4, row 4 |  |
| HgTe |  | -43.69 kJ/mol (basis unstated) | 298 | unspecified |  |  | [1] Gierlotka 2010; _cites Brebrick 1991_ | Table 4, p. 4, row 6 |  |
| HgTe |  | -43.648 kJ/mol (basis unstated) | 298 | model |  |  | [1] Gierlotka 2010 | Table 4, p. 4, row 8 |  |
| HgTe |  | -41.2 kJ/mol (basis unstated) | 298 | unspecified |  |  | [1] Gierlotka 2010; _cites Sha 1989_ [doi](https://doi.org/10.1149/1.2096558) | Table 4, p. 4, row 3 |  |
| HgTe |  | -36.5 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Gierlotka 2010; _cites Nasar 1990_ [doi](https://doi.org/10.1016/0022-5088%2890%2990316-c) | Table 4, p. 4, row 5 |  |
| HgTe |  | -33.9 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Gierlotka 2010; _cites Ratajczak 1969_ | Table 4, p. 4, row 1 |  |
| HgTe |  | -31.8 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Gierlotka 2010; _cites Mills 1974_ | Table 4, p. 4, row 2 |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Hg–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 942 K | 942 | L = HgTe; _L: Te 0.5; HgTe: Te 0.5_ | model | [1] Gierlotka 2010 | Table 3, p. 4, row 8 |  |
| Phase transition | 942.65 K | 942.65 | HgTe | experimental | [2] Jianrong 1995; _cites ref. 31_ | p. 2 | “The melting point of HgTe has been measured by Strauss (3 1) Asadov (34) Delves and Lewis (36) Vanyukov et al. (32), Harman (35) Levitskaya et al. (37) Steininger (38) Blair and New&m (39), Ray and Spencer (26), Szofran and Lehoczky (40), Harman and Strauss (41), Tung et al.. (5)and Gromakov et al. (42) with general agreement and a mean value of 669.5"C.” |
| Phase transition | 943 K | 943 | L = HgTe; _L: Te 0.5; HgTe: Te 0.5_ | experimental | [1] Gierlotka 2010; _cites Massalski 1986_ | Table 3, p. 4, row 5 |  |
| Phase transition | 943 K | 943 | congruent | experimental | [1] Gierlotka 2010 | p. 2 | “Temperature of congruent melting of HgTe intermetallic compound is 943 K.” |
| Phase transition | 944 K | 944 | L = HgTe; _L: Te 0.5; HgTe: Te 0.5_ | model | [1] Gierlotka 2010 | Table 3, p. 4, row 6 |  |
| Phase transition | 944 K | 944 | L = HgTe; _L: Te 0.5; HgTe: Te 0.5_ | model | [1] Gierlotka 2010 | Table 3, p. 4, row 7 |  |

### Phase equilibrium (12)

Table: Phase equilibrium, Hg–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 936.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 32_ | Table 1B, p. 4, row 5 |  |
| Phase composition |  | 936.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 32_ | Table 1B, p. 4, row 3 |  |
| Phase composition |  | 940.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 5_ | Table 1B, p. 4, row 6 |  |
| Phase composition |  | 941.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 38_ | Table 1B, p. 4, row 11 |  |
| Phase composition |  | 941.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 37_ | Table 1B, p. 4, row 12 |  |
| Phase composition |  | 942.65 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 39_ | Table 1B, p. 4, row 7 |  |
| Phase composition |  | 943.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 32_ | Table 1B, p. 4, row 4 |  |
| Phase composition |  | 943.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 36_ | Table 1B, p. 4, row 9 |  |
| Phase composition |  | 943.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 26_ | Table 1B, p. 4, row 8 |  |
| Phase composition |  | 943.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 34_ | Table 1B, p. 4, row 2 |  |
| Phase composition |  | 943.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 31_ | Table 1B, p. 4, row 1 |  |
| Phase composition |  | 958.15 | liquidus: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 42_ | Table 1B, p. 4, row 10 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010). [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003)
2. Yang Jianrong, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Thermodynamic and phase diagram assessment of the Cd-Te and Hg-Te systems, Calphad 19, 399-414 (1995). [doi:10.1016/0364-5916(95)00038-g](https://doi.org/10.1016/0364-5916%2895%2900038-g)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
