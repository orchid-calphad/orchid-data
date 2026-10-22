# Pb–Sc system

> Pb–Sc system: 4 accepted literature values (invariant reaction 2, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-SC.html · Markdown: https://data.orchid-project.org/systems/PB-SC.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-SC.json) · [CSV](https://data.orchid-project.org/systems/PB-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-SC) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-SC/PbSc-14Idd.json) · [Markdown](https://data.orchid-project.org/systems/PB-SC.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbSc-14Idd.tdb | A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, J. Alloys Compd., 589, 192-99(2014). [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) | `f09786a7a2f576ea9ca5b405f1830a5a334cdd6db912f4a018e17f08976b9d4b` | [viewer](https://orchid-project.org/phase-diagrams/#PB-SC/PbSc-14Idd.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbSc-14Idd.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbSc-14Idd.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbSc-14Idd.tdb | 1561.98 | LIQUID (x(Sc) 0.4046) + PB5SC6 (x(Sc) 0.54545) + PB3SC5_D88 (x(Sc) 0.625) |
| PbSc-14Idd.tdb | 1561.98 | LIQUID (x(Sc) 0.40454) + PB5SC6 (x(Sc) 0.54545) + PB3SC5_D88 (x(Sc) 0.625) |
| PbSc-14Idd.tdb | 1561.98 | LIQUID (x(Sc) 0.40469) + PB5SC6 (x(Sc) 0.54545) + PB3SC5_D88 (x(Sc) 0.625) |
| PbSc-14Idd.tdb | 1544.86 | LIQUID (x(Sc) 0.88492) + BCC_A2 (x(Sc) 0.98191) + HCP_A3 (x(Sc) 0.99225) |
| PbSc-14Idd.tdb | 1468.85 | PB3SC5_D88 (x(Sc) 0.625) + LIQUID (x(Sc) 0.86409) + HCP_A3 (x(Sc) 0.98999) |
| PbSc-14Idd.tdb | 1468.85 | PB3SC5_D88 (x(Sc) 0.625) + LIQUID (x(Sc) 0.86402) + HCP_A3 (x(Sc) 0.98998) |
| PbSc-14Idd.tdb | 600.54 | FCC_A1 (x(Sc) 0) + LIQUID (x(Sc) 1.100e-4) + PB5SC6 (x(Sc) 0.54545) |
| PbSc-14Idd.tdb | 600.54 | FCC_A1 (x(Sc) 0) + LIQUID (x(Sc) 1.100e-4) + PB5SC6 (x(Sc) 0.54545) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-SC.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pb–Sc system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1563.15 | peritectic |  | experimental | [1] Iddaoudi 2014; _cites Palenzona 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906014-2) | p. 2 | “For the Sc5Pb3 compound a congruent melting was determined at 1700 °C, while for the Sc6Pb5 compound a peritectic formation was reported, at 1290 °C.” |
| 1469.15 | eutectic: Liq M Sc5Pb3 + (aSc) |  | model | [1] Iddaoudi 2014 | p. 5 | “For the Sc-rich part of this system we suggested the eutectic reaction of Liq M Sc5Pb3 + (aSc) at 1196 °C and the catatectic reaction Liq + aSc) M (bSc) at 1272 °C according to the literature data of Dy-rich part of Dy-Pb system and presented in Fig. 5.” |

## Other properties

### Phase transition (2)

Table: Phase transition, Pb–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1545.15 K | 1545.15 | other: Liq + aSc) M (bSc) | model | [1] Iddaoudi 2014 | p. 5 | “For the Sc-rich part of this system we suggested the eutectic reaction of Liq M Sc5Pb3 + (aSc) at 1196 °C and the catatectic reaction Liq + aSc) M (bSc) at 1272 °C according to the literature data of Dy-rich part of Dy-Pb system and presented in Fig. 5.” |
| Phase transition | 1973.15 K | 1973.15 | congruent | experimental | [1] Iddaoudi 2014; _cites Palenzona 1995_ [doi](https://doi.org/10.1016/0925-8388%2894%2906014-2) | p. 2 | “For the Sc5Pb3 compound a congruent melting was determined at 1700 °C, while for the Sc6Pb5 compound a peritectic formation was reported, at 1290 °C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014). [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
