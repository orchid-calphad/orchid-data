# In–N system

> In–N system: 33 accepted literature values (phase transition 23, formation 9, heat capacity / entropy / enthalpy 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-N.html · Markdown: https://data.orchid-project.org/systems/IN-N.md

33 accepted literature values from 2 paper(s) (experimental 28, model 5); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-N.json) · [CSV](https://data.orchid-project.org/systems/IN-N.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-N) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-N/InN-02Ond.json) · [Markdown](https://data.orchid-project.org/systems/IN-N.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 28 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 23 |
| formation | 9 |
| heat capacity / entropy / enthalpy | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InN-02Ond.tdb | B. Onderka, J. Unland, R. Schmid-Fetzer, J. Mater. Res., 17, 3065-83(2002). [doi:10.1557/JMR](https://doi.org/10.1557/JMR) | `1390e31379d591aaa398d0e7e5bcc28cd39443a1232bfcf05b852ced52672411` | [viewer](https://orchid-project.org/phase-diagrams/#IN-N/InN-02Ond.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InN-02Ond.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InN-02Ond.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InN-02Ond.tdb | 429.75 | LIQUID (x(N) 0) + TETRAGONAL_A6 (x(N) 0) + GAS (x(N) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-N.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-N.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, In–N system (9)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| InN |  | -143.5 per formula unit | 298.15 | experimental |  |  | [1] F 2010; _cites MacChesney 1970_ | Table III, p. 10, row 2 |  |
| InN |  | -136.4 per formula unit ± 19 | 298.15 | experimental |  |  | [1] F 2010; _cites Vorobev 1973_ | Table III, p. 10, row 5 |  |
| InN |  | -132.6 per formula unit ± 6 | 298.15 | experimental |  |  | [1] F 2010; _cites Vorobev 1971_ | Table III, p. 10, row 4 |  |
| InN |  | -131.4 per formula unit ± 7 | 298.15 | experimental |  |  | [1] F 2010; _cites Jones 1987_ | Table III, p. 10, row 7 |  |
| InN |  | -127.6 per formula unit ± 3 | 298.15 | experimental |  |  | [1] F 2010; _cites Gordienko 1977_ | Table III, p. 10, row 6 |  |
| InN |  | -113 per formula unit ± 42 | 298.15 | experimental |  |  | [1] F 2010; _cites Vorobev 1971_ | Table III, p. 10, row 3 |  |
| InN |  | -96.5 per formula unit | 298.15 | model |  |  | [1] F 2010 | Table III, p. 10, row 11 |  |
| InN |  | -28.6 per formula unit ± 9.2 | 298.15 | experimental |  |  | [1] F 2010; _cites Ranade 2001_ | Table III, p. 10, row 8 |  |
| InN |  | -19.2 per formula unit ± 2 | 298.15 | experimental |  |  | [1] F 2010; _cites Hahn 1940_ | Table III, p. 10, row 10 |  |

## Other properties

### Phase transition (23)

Table: Phase transition, In–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 234 K | 234 | other | model | [2] Onderka 2002 | p. 15 | “The consequence of selecting that value together with S°298(InN) derived from experimental Cp data is a value of T LSG ⳱ 234 K at 1 bar as given in Table VI.” |
| Phase transition | 773 K | 773 | Decomposition of InN (+In) powder, TGA, DTA, high resolution TGA in isothermal steps, XRD; _alloy: N 0.5_ | experimental | [1] F 2010 | Table V, p. 14, row 12 |  |
| Phase transition | 773 K | 773 | Thin film InN decomposition; _alloy: N 0.5_ | experimental | [1] F 2010; _cites Trainor 1974_ | Table V, p. 14, row 3 |  |
| Phase transition | 773 K | 773 | other | model | [2] Onderka 2002 | p. 11 | “Assuming that the start of InN decomposition corresponds to T LSG, the value of 773 K is assessed based on the present experimental data, which are well supported by literature data.” |
| Phase transition | 773 K | 773 | other: Isothermal stepping TGA, sample 2 | experimental | [1] F 2010 | Table II, p. 6, row 6 |  |
| Phase transition | 773 K | 773 | other: Isothermal stepping TGA, samples 1, 3, 4, assessed value | experimental | [1] F 2010 | Table II, p. 6, row 7 |  |
| Phase transition | 773 K | 773 | other: Mechanical mixture InN + In (3:1 by mass), first heating up to 1073 K | experimental | [1] F 2010 | Table II, p. 6, row 3 |  |
| Phase transition | 775 K | 775 | Thin InN (+In) film decomposition, optical microscopy; _alloy: N 0.5_ | experimental | [1] F 2010 | Table V, p. 14, row 13 |  |
| Phase transition | 783 K | 783 | other: InN, first heating up to 1073 K; _alloy: N 0.5_ | experimental | [1] F 2010 | Table II, p. 6, row 1 |  |
| Phase transition | 793 K | 793 | other: InN, first heating up to 1073 K; _alloy: N 0.5_ | experimental | [1] F 2010 | Table II, p. 6, row 2 |  |
| Phase transition | 795 K | 795 | Decomposition of InN (+In) powders, high pressure autoclave 1–1000 bar, XRD; _alloy: N 0.5_ | experimental | [1] F 2010; _cites MacChesney 1970_ | Table V, p. 14, row 1 |  |
| Phase transition | 798 K | 798 | other: InN, dynamic oscillation TGA, first heating cycle; _alloy: N 0.5_ | experimental | [1] F 2010 | Table II, p. 6, row 4 |  |
| Phase transition | 823 K | 823 | Thin film InN monocrystal decomposition, RHEED, XPS, optical microscopy; _alloy: N 0.5_ | experimental | [1] F 2010; _cites Guo 1993_ | Table V, p. 14, row 4 |  |
| Phase transition | 831 K | 831 |  | model | [2] Onderka 2002; _cites Van 1973_ | p. 15 | “If a much lower melting point of InN was assumed, like the value 831 K from van Vechten's model,39 a resulting curve, not shown in Fig. 16, would show a temperature maximum at that limit, irrespective of the pressure level, and then extend to higher pressure with decreasing temperature and nitrogen-rich liquid.” |
| Phase transition | 843 K | 843 | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] F 2010; _cites Grzegory 1994_ | Table V, p. 14, row 5 |  |
| Phase transition | 873 K | 873 (\<) | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] F 2010; _cites Grzegory 1994_ | Table V, p. 14, row 6 |  |
| Phase transition | 903 K | 903 | Thin film InN decomposition, mass-spectrometer. Only upper limit of P(N2) given; _alloy: N 0_ | experimental | [1] F 2010; _cites Ambacher 1996_ | Table V, p. 14, row 9 |  |
| Phase transition | 933 K | 933 | Decomposition of InN crystallites (10–50 μm) under high pressure, XRD; _alloy: N 0.5_ | experimental | [1] F 2010; _cites Krukowski 1998_ | Table V, p. 14, row 10 |  |
| Phase transition | 945 K | 945 | Decomposition of InN (+In) powders, high pressure autoclave 1–1000 bar, XRD; _alloy: N 0.5_ | experimental | [1] F 2010; _cites MacChesney 1970_ | Table V, p. 14, row 2 |  |
| Phase transition | 973 K | 973 | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] F 2010; _cites Grzegory 1994_ | Table V, p. 14, row 7 |  |
| Phase transition | 973 K | 973 (>) | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] F 2010; _cites Grzegory 1994_ | Table V, p. 14, row 8 |  |
| Phase transition | 983 K | 983 | Decomposition of InN crystallites (10–50 μm) under high pressure, XRD; _alloy: N 0.5_ | experimental | [1] F 2010; _cites Krukowski 1998_ | Table V, p. 14, row 11 |  |
| Phase transition | 1714 K | 1714 |  | model | [2] Onderka 2002 | p. 10 | “The present estimation of Tm(InN) ⳱ 1714 K was made on the basis of the trend line given in Fig. 11.” |

### Heat capacity / entropy / enthalpy (1)

Table: Heat capacity / entropy / enthalpy, In–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Heat capacity; _printed: Cp_ | 38.65 J/mol-formula K | 293 | InN | experimental | [2] Onderka 2002; _cites Krukowski 1999_ | p. 8 | “calorimetry (DSC) on crystallites 10-50 ␮m in size in the temperature range 153-293 K as given in Fig. 9 from the tabulated data of Ref. 25, where Cp (293 K) ⳱ 38.65 J/ mol-formula K is reported.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. F. Gao, C. Wang, X. Liu, J. Mater. Res., 25, 576-86(2010). [doi:10.1557/jmr](https://doi.org/10.1557/jmr)
2. B. Onderka, J. Unland, R. Schmid-Fetzer, Thermodynamics and phase stability in the In–N system, J. Mater. Res. 17, 3065-3083 (2002). [doi:10.1557/jmr.2002.0445](https://doi.org/10.1557/jmr.2002.0445)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
