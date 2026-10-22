# Fe–Pd system

> Fe–Pd system: 27 accepted literature values (invariant reaction 21, formation 4, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-PD.html · Markdown: https://data.orchid-project.org/systems/FE-PD.md

27 accepted literature values from 1 paper(s) (experimental 15, model 12); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-PD.json) · [CSV](https://data.orchid-project.org/systems/FE-PD.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-PD) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-PD/FePd-99Gho-LB.json) · [Markdown](https://data.orchid-project.org/systems/FE-PD.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 15 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 21 |
| phase transition | 2 |
| formation | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FePd-99Gho-LB.tdb | G. Ghosh, C. Kantner, G.B. Olson, J. Phase Equilib., 20, 295-308(1999). [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) | `44714d50700b1a28a8ad1b6936558770de176bbf6f8c72c21311a0c71ec9cd02` | [viewer](https://orchid-project.org/phase-diagrams/#FE-PD/FePd-99Gho-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FePd-99Gho-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FePd-99Gho-LB.tdb | 1753.43 | BCC_A2 (x(Pd) 0.03877) + FCC_A1 (x(Pd) 0.04336) + LIQUID (x(Pd) 0.07577) |
| FePd-99Gho-LB.tdb | 1087.42 | BCC_A2 (x(Pd) 0.02566) + FCC_A1#2 (x(Pd) 0.05963) + FCC_A1 (x(Pd) 0.24012) |
| FePd-99Gho-LB.tdb | 1037.12 | FEPD_L10 (x(Pd) 0.62224) + FCC_A1 (x(Pd) 0.64422) + FEPD3_L12 (x(Pd) 0.6833) |
| FePd-99Gho-LB.tdb | 898.04 | BCC_A2 (x(Pd) 0.00603) + FCC_A1 (x(Pd) 0.39972) + FEPD_L10 (x(Pd) 0.48925) |
| FePd-99Gho-LB.tdb | 322.8 | FEPD3_L12 (x(Pd) 0.84322) + FEPD3_L12#2 (x(Pd) 0.88493) + FCC_A1 (x(Pd) 0.9472) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-PD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-PD.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Fe–Pd system (21)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1753 | L + (δFe) -> (γFe) | L: Pd 0.0757; (δFe): Pd 0.0387; (γFe): Pd 0.0433 | model | [1] Ghosh 1999 | Table 1, p. 5, row 2 |  |
| 1751 | L + (δFe) -> (γFe) | L: Pd 0.065; (δFe): Pd 0.033; (γFe): Pd 0.037 | experimental | [1] Ghosh 1999; _cites Gibson 1958_ | Table 1, p. 5, row 1 |  |
| 1583 | L -> γ | L: Pd 0.5; γ: Pd 0.5 | experimental | [1] Ghosh 1999; _cites Kubaschewski 1982_ | Table 1, p. 5, row 11 |  |
| 1582 | L -> γ | L: Pd 0.4971; γ: Pd 0.4971 | model | [1] Ghosh 1999 | Table 1, p. 5, row 12 |  |
| 1173 | γ -> γ1 + γ2 |  | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 13 |  |
| 1147 | γ -> γ1 + γ2 | γ: Pd 0.1406 | model | [1] Ghosh 1999 | Table 1, p. 5, row 14 |  |
| 1094 | γ -> FePd3 | γ: Pd 0.7305; FePd3: Fe 0.25, Pd 0.75 | model | [1] Ghosh 1999 | Table 1, p. 5, row 21 |  |
| 1093 | γ -> FePd3 | γ: Fe 0.25, Pd 0.75; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 19 |  |
| 1088 | γ1 -> (αFe) + γ2 | γ1: Pd 0.07; (αFe): Pd 0.0348; γ2: Pd 0.2348 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 4 |  |
| 1087 | γ1 -> (αFe) + γ2 | γ1: Pd 0.0597; (αFe): Pd 0.0257; γ2: Pd 0.2401 | model | [1] Ghosh 1999 | Table 1, p. 5, row 5 |  |
| 1083 | γ -> FePd3 | γ: Pd 0.6596; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Takezawa 1987_ [doi](https://doi.org/10.2320/jinstmet1952.51.4_285) | Table 1, p. 5, row 20 |  |
| 1073 | γ1 -> (αFe) + γ2 |  | experimental | [1] Ghosh 1999; _cites Kussman 1963_ | Table 1, p. 5, row 3 |  |
| 1073 | γ -> FePd3 | γ: Pd 0.65; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Kussman 1963_ | Table 1, p. 5, row 18 |  |
| 1063 | γ -> FePd | γ: Fe 0.5, Pd 0.5; FePd: Fe 0.5, Pd 0.5 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 15 |  |
| 1060 | γ -> FePd | γ: Pd 0.5808; FePd: Fe 0.5, Pd 0.5 | model | [1] Ghosh 1999 | Table 1, p. 5, row 17 |  |
| 1056 | γ -> FePd | γ: Pd 0.5792; FePd: Fe 0.5, Pd 0.5 | experimental | [1] Ghosh 1999; _cites Takezawa 1987_ [doi](https://doi.org/10.2320/jinstmet1952.51.4_285) | Table 1, p. 5, row 16 |  |
| 1037 | γ -> FePd + FePd3 | γ: Pd 0.6443; FePd: Pd 0.6222; FePd3: Pd 0.6833 | model | [1] Ghosh 1999 | Table 1, p. 5, row 10 |  |
| 1033 | γ -> FePd + FePd3 | γ: Pd 0.615; FePd: Fe 0.5, Pd 0.5; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 9 |  |
| 898 | γ -> (αFe) + FePd | γ: Pd 0.3998; (αFe): Pd 0.0061; FePd: Pd 0.4893 | model | [1] Ghosh 1999 | Table 1, p. 5, row 8 |  |
| 878 | γ -> (αFe) + FePd | γ: Pd 0.46; FePd: Pd 0.4833 | experimental | [1] Ghosh 1999; _cites Kussman 1963_ | Table 1, p. 5, row 6 |  |
| 873 | γ -> (αFe) + FePd | γ: Pd 0.43; (αFe): Pd 0.0087; FePd: Pd 0.4696 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 7 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Fe–Pd system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| FePd | [FePd](https://data.orchid-project.org/compounds/FePd.html) | -13.735 kJ/mol-atom | 298.15 | model | -6.145 (mp-aaaaaeex) | -6.376 (oqmd-116604) | [1] Ghosh 1999 | Table 2, p. 7, row 1 |  |
| FePd | [FePd](https://data.orchid-project.org/compounds/FePd.html) | -6 kJ/mol-atom | 298.15 | model | -6.145 (mp-aaaaaeex) | -6.376 (oqmd-116604) | [1] Ghosh 1999; _cites F 1988_ | Table 2, p. 7, row 2 |  |
| FePd3 | [FePd3](https://data.orchid-project.org/compounds/FePd3.html) | -22.01 kJ/mol-atom | 298.15 | model | -10.445 (mp-aaaabgif) | -10.694 (oqmd-2169161) | [1] Ghosh 1999 | Table 2, p. 7, row 3 |  |
| FePd3 | [FePd3](https://data.orchid-project.org/compounds/FePd3.html) | -4 kJ/mol-atom | 298.15 | model | -10.445 (mp-aaaabgif) | -10.694 (oqmd-2169161) | [1] Ghosh 1999; _cites F 1988_ | Table 2, p. 7, row 4 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Fe–Pd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1063 K | 1063 | congruent | experimental | [1] Ghosh 1999; _cites Takezawa 1987_ [doi](https://doi.org/10.2320/jinstmet1952.51.4_285) | p. 2 | “More importantly, they exhibit congruent ordering at highly off-stoichiometric compositions, for example, FePd around 59 at.% Pd (Ref 37) at 1063 ± 20 K, and FePd3 around 66 at.% Pd (Ref 37) at 1093 ± 20 K.” |
| Phase transition | 1093 K | 1093 | congruent | experimental | [1] Ghosh 1999; _cites Takezawa 1987_ [doi](https://doi.org/10.2320/jinstmet1952.51.4_285) | p. 2 | “More importantly, they exhibit congruent ordering at highly off-stoichiometric compositions, for example, FePd around 59 at.% Pd (Ref 37) at 1063 ± 20 K, and FePd3 around 66 at.% Pd (Ref 37) at 1093 ± 20 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999). [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
