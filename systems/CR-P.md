# Cr–P system

> Cr–P system: 3 accepted literature values (activity / EMF / Gibbs energy 2, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-P.html · Markdown: https://data.orchid-project.org/systems/CR-P.md

3 accepted literature values from 1 paper(s) (model 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-P.json) · [CSV](https://data.orchid-project.org/systems/CR-P.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-P) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-P/CrP-14Mie.json) · [Markdown](https://data.orchid-project.org/systems/CR-P.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| activity / EMF / Gibbs energy | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrP-14Mie.tdb | J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014). [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) | `13fd479377120522b9809dc36c02c00447b146c0c4c2f9c4fe1d8dc02472b5b3` | [viewer](https://orchid-project.org/phase-diagrams/#CR-P/CrP-14Mie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrP-14Mie.json) |
| CrP-99Mie-LB.tdb | J. Miettinen, Calphad, 23, 191-99(1999). [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) | `372cae8e610e58d479c7da367b4c0325402057b10dc71e3f2c77a369d4305f59` | [viewer](https://orchid-project.org/phase-diagrams/#CR-P/CrP-99Mie-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrP-99Mie-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrP-14Mie.tdb | 1784.51 | LIQUID (x(P) 0.21997) + M3P_D0E (x(P) 0.25) + M2P_C22 (x(P) 0.33333) |
| CrP-14Mie.tdb | 1784.5 | LIQUID (x(P) 0.21958) + M3P_D0E (x(P) 0.25) + M2P_C22 (x(P) 0.33333) |
| CrP-14Mie.tdb | 1784.5 | LIQUID (x(P) 0.21964) + M3P_D0E (x(P) 0.25) + M2P_C22 (x(P) 0.33333) |
| CrP-14Mie.tdb | 1644.33 | BCC_A2 (x(P) 1.000e-4) + LIQUID (x(P) 0.13387) + M3P_D0E (x(P) 0.25) |
| CrP-99Mie-LB.tdb | 1783.12 | LIQUID (x(P) 0.21756) + M3P_D0E (x(P) 0.25) + M2P_C22 (x(P) 0.33333) |
| CrP-99Mie-LB.tdb | 1783.11 | LIQUID (x(P) 0.21703) + M3P_D0E (x(P) 0.25) + M2P_C22 (x(P) 0.33333) |
| CrP-99Mie-LB.tdb | 1783.11 | LIQUID (x(P) 0.21711) + M3P_D0E (x(P) 0.25) + M2P_C22 (x(P) 0.33333) |
| CrP-99Mie-LB.tdb | 1644.99 | BCC_A2 (x(P) 1.000e-4) + LIQUID (x(P) 0.13374) + M3P_D0E (x(P) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-P.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-P.json) · [CALPHAD hull CrP-99Mie-LB](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-P--CrP-99Mie-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–P system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1645.15 | eutectic |  | model | [1] Miettinen 1999 | p. 4 | “'Gcrp = 2'Gcrbcc+ oGpwhite-p -159530+5T gave a low solubility of phosphorus in the bee phase (O.OOSwt%at Here, the bee interaction parameter, Lc,,rbCC, the calculated eutectic temperature of 1372'C) which agrees reasonably well with the "very slow" solubility suggested by experimental studies (6,7).” |

## Other properties

### Activity / EMF / Gibbs energy (2)

Table: Activity / EMF / Gibbs energy, Cr–P system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy | -150 kJ/mol | 1920.15 | Cr2P | model | [1] Miettinen 1999 | p. 4 | “After making the necessary change of reference state of pure phosphorus from gaseous phase (5) to white-P (21), a certain Gibbs energy function was obtained for Crr.ss5Pi.ro5yielding a value of about -159 kJ/mol at 1647'C (calculated melting point of Cr2P) whereas Eq.(9) yields a value of about -150 kJ/mol for Cr2P at the same temperature.” |
| Gibbs energy | -159 kJ/mol | 1920.15 | Crr.ss5Pi.ro5 | model | [1] Miettinen 1999; _cites AI 1998_ | p. 4 | “After making the necessary change of reference state of pure phosphorus from gaseous phase (5) to white-P (21), a certain Gibbs energy function was obtained for Crr.ss5Pi.ro5yielding a value of about -159 kJ/mol at 1647'C (calculated melting point of Cr2P) whereas Eq.(9) yields a value of about -150 kJ/mol for Cr2P at the same temperature.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jyrki Miettinen, Thermodynamic description of Cr-P AND Fe-Cr-P systems at low phosphorus contents, Calphad 23, 141-154 (1999). [doi:10.1016/s0364-5916(99)00019-x](https://doi.org/10.1016/s0364-5916%2899%2900019-x)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
