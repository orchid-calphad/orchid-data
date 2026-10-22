# Ni–Ru system

> Ni–Ru system: 5 accepted literature values (formation 4, invariant reaction 1) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NI-RU.html · Markdown: https://data.orchid-project.org/systems/NI-RU.md

5 accepted literature values from 2 paper(s) (experimental 1, DFT 4); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NI-RU.json) · [CSV](https://data.orchid-project.org/systems/NI-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NI-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-01Che-LB.json) · [Markdown](https://data.orchid-project.org/systems/NI-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| formation | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NiRu-01Che-LB.tdb | P.-Y. Chevalier, E. Fischer, unpublished, 2001. | `cfb9ea78cdca6ee26eeea2aa7b91d55a78c4d5f2636678699421a39d1aa6e072` | [viewer](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-01Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiRu-01Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiRu-01Che-LB.json) |
| NiRu-04Hal.tdb | S. Hallstroem, J. Phase Equilib. Diffus., 25, 252-54(2004). [doi:10.1361/15477030419504](https://doi.org/10.1361/15477030419504) | `d86ac6781c062de73ce0afb651fbf2d80fb33fda4b6c3e6d0e37fc7b079999e9` | [viewer](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-04Hal.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiRu-04Hal.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiRu-04Hal.json) |
| NiRu-08Hal.tdb | S. Hallstroem, D. Andersson, A. Ruban, J. Agren, Acta Mater., 56, 4062-69(2008). [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028) | `b00a907636215ffed49ea53e7ca32d80c1236b024aecb2308df2c9ad79e97f61` | [viewer](https://orchid-project.org/phase-diagrams/#NI-RU/NiRu-08Hal.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiRu-08Hal.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiRu-08Hal.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NiRu-01Che-LB.tdb | 1807.84 | LIQUID (x(Ru) 0.26144) + FCC_A1 (x(Ru) 0.31942) + HCP_A3 (x(Ru) 0.5053) |
| NiRu-04Hal.tdb | 1836.9 | LIQUID (x(Ru) 0.29256) + FCC_A1 (x(Ru) 0.34142) + HCP_A3 (x(Ru) 0.52632) |
| NiRu-08Hal.tdb | 1801.84 | LIQUID (x(Ru) 0.25525) + FCC_A1 (x(Ru) 0.31029) + HCP_A3 (x(Ru) 0.51555) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NI/NI-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NI/NI-RU.json) · [CALPHAD hull NiRu-01Che-LB](https://data.orchid-project.org/hulls/calphad-sgte/NI/NI-RU--NiRu-01Che-LB.json) · [CALPHAD hull NiRu-04Hal](https://data.orchid-project.org/hulls/calphad-sgte/NI/NI-RU--NiRu-04Hal.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ni–Ru system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1763.15 | peritectic |  | experimental | [1] Hallström 2004; _cites Raub 1961_ | p. 1 | “Raub and Menzel\[7\] reported the peritectic temperature to be 1490 °C, whereas Kornilov and Myasnikova\[8\] reported 1550 ± 10 °C.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ni–Ru system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ni2Ru2 |  | 14.6 kJ/mol-atom | 0 | DFT |  |  | [2] Hallström 2008 | Table A.1, p. 7, row 3 |  |
| Ni3Ru |  | 17.56 kJ/mol-atom | 0 | DFT |  |  | [2] Hallström 2008 | Table A.1, p. 7, row 2 |  |
| NiRu |  | 25.35 kJ/mol-atom | 0 | DFT |  |  | [2] Hallström 2008 | Table A.1, p. 7, row 5 |  |
| NiRu3 |  | 13.8 kJ/mol-atom | 0 | DFT |  |  | [2] Hallström 2008 | Table A.1, p. 7, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Samuel Hallström, Thermodynamic Assessment of the Ni-Ru System, Journal of Phase Equilibria &amp; Diffusion 25, 252-254 (2004). [doi:10.1361/15477030419504](https://doi.org/10.1361/15477030419504)
2. Samuel Hallström, David Andersson, Andrei Ruban, John Ågren, Thermodynamic reassessment of the Ni–Ru system and assessment of the Al–Ni–Ru system at 1273–1523 K using ab initio calculations, Acta Materialia 56, 4062-4069 (2008). [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
