# Hf–N system

> Hf–N system: 7 accepted literature values (phase transition 3, invariant reaction 2, formation 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-N.html · Markdown: https://data.orchid-project.org/systems/HF-N.md

7 accepted literature values from 1 paper(s) (experimental 5, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-N.json) · [CSV](https://data.orchid-project.org/systems/HF-N.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-N) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-N/HfN-18Pan.json) · [Markdown](https://data.orchid-project.org/systems/HF-N.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 3 |
| formation | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfN-18Pan.tdb | M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018). [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) | `e62247a157b146a136b12ccfa9ecf9f956b7458ba581bf6b57403474d3c50992` | [viewer](https://orchid-project.org/phase-diagrams/#HF-N/HfN-18Pan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfN-18Pan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfN-18Pan.tdb | 3650.81 | LIQUID (x(N) 0.26474) + FCC_A1 (x(N) 0.42525) + GAS (x(N) 0.9989) |
| HfN-18Pan.tdb | 3187.99 | LIQUID (x(N) 0.19761) + HCP_A3 (x(N) 0.25325) + FCC_A1 (x(N) 0.37756) |
| HfN-18Pan.tdb | 2542.71 | HCP_A3 (x(N) 0.2704) + FCC_A1 (x(N) 0.41203) + HF4N3 (x(N) 0.42857) |
| HfN-18Pan.tdb | 2478.01 | BCC_A2 (x(N) 0) + LIQUID (x(N) 0.01199) + HCP_A3 (x(N) 0.03726) |
| HfN-18Pan.tdb | 2245.01 | HCP_A3 (x(N) 0.27426) + HF3N2 (x(N) 0.4) + HF4N3 (x(N) 0.42857) |
| HfN-18Pan.tdb | 353.56 | HF3N2 (x(N) 0.4) + HF4N3 (x(N) 0.42857) + FCC_A1 (x(N) 0.49986) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-N.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-N.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hf–N system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 3184.15 | peritectic |  | experimental | [1] Pang 2018; _cites Booker 1969_ | p. 1 | “The Hcp solid solution with about 28 at. % N peritectically melts to form liquid plus Fcc phases at 2911 oC \[22\].” |
| 2463.15 | eutectic |  | experimental | [1] Pang 2018; _cites Booker 1969_ | p. 2 | “The temperature of the eutectic reaction among liquid, Hcp and Bcc phases is 2190 oC \[22\].” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Hf–N system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -187.23 unspecified | 298 | model |  |  | [1] Pang 2018; _cites Mulokozi 1981_ | p. 3 | “The enthalpy of formation for HfN1.0 at 298 K calculated by Mulokozi \[39\] was -187.23 kJ/mol-atoms.” |
| — |  | 184.6 unspecified ± 0.7 | 298 | experimental |  |  | [1] Pang 2018; _cites Humphrey 1953_ | p. 3 | “Humphrey \[38\] determined the heat of formation for hafnium mononitride at 298 K to be 184.6±0.7 kJ/mol-atoms by combustion calorimetry.” |

## Other properties

### Phase transition (3)

Table: Phase transition, Hf–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 3273.15 K | 3273.15 |  | experimental | [1] Pang 2018; _cites Nowotny 1960_ | p. 2 | “The melting point of Fcc phase is 3000 oC according to Nowotny et al. \[24\].” |
| Phase transition | 3639 K | 3639 |  | model | [1] Pang 2018 | p. 5 | “The calculated melting point of Fcc phase at 1 bar N2 pressure is 3639 K, which is 21 K lower than the experimental value reported by Booker and Brukl \[22\].” |
| Phase transition | 3660.15 K | 3660.15 | congruent | experimental | [1] Pang 2018; _cites Booker 1969_ | p. 2 | “However, Booker and Brukl \[22\] reported that the congruent melting point of Fcc phase is 3387 oC at 49 at. % N under 2 bar pressure of Ar.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. Pang, Y. Peng, P. Zhou, Y. Du, Thermodynamic modeling of the Hf-N system, J min metall B Metall 54, 111-118 (2018). [doi:10.2298/jmmb170520055p](https://doi.org/10.2298/jmmb170520055p)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
