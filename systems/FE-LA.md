# Fe–La system

> Fe–La system: 5 accepted literature values (phase transition 3, invariant reaction 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-LA.html · Markdown: https://data.orchid-project.org/systems/FE-LA.md

5 accepted literature values from 1 paper(s) (model 5); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-LA.json) · [CSV](https://data.orchid-project.org/systems/FE-LA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-LA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-LA/FeLa-09Pov.json) · [Markdown](https://data.orchid-project.org/systems/FE-LA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FeLa-09Pov.tdb | E. Povoden-Karadeniz, A.N. Grundy, M. Chen, T. Ivas, L.J. Gauckler, J. Phase Equilib. Diffus., 30, 351-66(2009). [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) | `93c713b8df680ffc2a6e483c568e88db56d841f5c4839e0b7f81a83cd305339f` | [viewer](https://orchid-project.org/phase-diagrams/#FE-LA/FeLa-09Pov.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FeLa-09Pov.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FeLa-09Pov.json) |
| FeLa-23Su.tdb | D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023). [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) | `825f2df5101d7cd0ffc67189cdf39deafb558ee98683104161a1685df56125e3` | [viewer](https://orchid-project.org/phase-diagrams/#FE-LA/FeLa-23Su.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FeLa-23Su.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FeLa-23Su.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FeLa-09Pov.tdb | 1650.03 | FCC_A1 (x(La) 0.00184) + BCC_A2 (x(La) 0.00247) + LIQUID (x(La) 0.10448) |
| FeLa-09Pov.tdb | 1188.34 | FCC_A1 (x(La) 0.00173) + BCC_A2 (x(La) 0.00204) + LIQUID (x(La) 0.82978) |
| FeLa-09Pov.tdb | 1133.15 | LIQUID (x(La) 0.96239) + BCC_A2 (x(La) 0.99906) + FCC_A1 (x(La) 0.99931) |
| FeLa-09Pov.tdb | 1078.1 | BCC_A2 (x(La) 0.00143) + LIQUID (x(La) 0.88645) + FCC_A1 (x(La) 0.99865) |
| FeLa-09Pov.tdb | 549.89 | BCC_A2 (x(La) 1.000e-5) + FCC_A1 (x(La) 0.99998) + DHCP (x(La) 1) |
| FeLa-23Su.tdb | 1670.01 | FCC_A1 (x(La) 0.02293) + BCC_A2 (x(La) 0.02294) + LIQUID (x(La) 0.40043) |
| FeLa-23Su.tdb | 1199.99 | FCC_A1 (x(La) 0.00707) + BCC_A2 (x(La) 0.0084) + LIQUID (x(La) 0.81532) |
| FeLa-23Su.tdb | 1130.58 | LIQUID (x(La) 0.95722) + BCC_A2 (x(La) 0.99668) + FCC_A1 (x(La) 0.9977) |
| FeLa-23Su.tdb | 1070.01 | BCC_A2 (x(La) 0.00454) + LIQUID (x(La) 0.87947) + FCC_A1 (x(La) 0.99618) |
| FeLa-23Su.tdb | 549.98 | BCC_A2 (x(La) 1.000e-5) + DHCP (x(La) 1) + FCC_A1 (x(La) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-LA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-LA.json) · [CALPHAD hull FeLa-09Pov](https://data.orchid-project.org/hulls/calphad-sgte/FE/FE-LA--FeLa-09Pov.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Fe–La system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2077 | eutectic |  | model | [1] Povoden-Karadeniz 2009 | p. 12 | “The calculated eutectic at the LaO1.5-rich side changes from T = 2055 K and 32.0 cat.% Fe in air (Fig. 10b) to 2077 K and 30.9 cat.% in pure oxygen; for the eutectic at the Fe-rich side T = 1704 K and 88.8 cat.% Fe in pure oxygen, and 1701 K and 88.5 cat.% Fe in air are calculated.” |
| 2055 | eutectic |  | model | [1] Povoden-Karadeniz 2009 | p. 12 | “The calculated eutectic at the LaO1.5-rich side changes from T = 2055 K and 32.0 cat.% Fe in air (Fig. 10b) to 2077 K and 30.9 cat.% in pure oxygen; for the eutectic at the Fe-rich side T = 1704 K and 88.8 cat.% Fe in pure oxygen, and 1701 K and 88.5 cat.% Fe in air are calculated.” |

## Other properties

### Phase transition (3)

Table: Phase transition, Fe–La system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 740 K | 740 | magnetic | model | [1] Povoden-Karadeniz 2009 | p. 9 | “A peak with broad shoulders calculated to be present at 740 K is caused by a magnetic order-disorder transition.\[25\]” |
| Phase transition | 2136 K | 2136 |  | model | [1] Povoden-Karadeniz 2009 | p. 12 | “r-La1±xFe1±yO3d melts at 2176 K at pO2 1⁄4 105 Pa; 2136 K is calculated in air.” |
| Phase transition | 2176 K | 2176 |  | model | [1] Povoden-Karadeniz 2009 | p. 12 | “r-La1±xFe1±yO3d melts at 2176 K at pO2 1⁄4 105 Pa; 2136 K is calculated in air.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009). [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
