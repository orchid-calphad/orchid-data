# Hg–Sn system

> Hg–Sn system: 73 accepted literature values (phase transition 31, invariant reaction 24, crystal structure 14, activity / EMF / Gibbs energy 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HG-SN.html · Markdown: https://data.orchid-project.org/systems/HG-SN.md

73 accepted literature values from 1 paper(s) (experimental 43, model 30); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HG-SN.json) · [CSV](https://data.orchid-project.org/systems/HG-SN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HG-SN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HG-SN/HgSn-03Yen-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/HG-SN.html) · [Markdown](https://data.orchid-project.org/systems/HG-SN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 43 |
| model | 30 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 24 |
| phase transition | 31 |
| mixing / partial | 1 |
| activity / EMF / Gibbs energy | 2 |
| crystal structure | 14 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HgSn-03Yen-LB.tdb | Y.-W. Yen, J. Groebner, S.C. Hansen, R. Schmid-Fetzer, J. Phase Equilib., 24, 151-67(2003). [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) | `c2b9fce680ecdfc10123e23524d43121af4054867846ab6bed588b6155a230f4` | [viewer](https://orchid-project.org/phase-diagrams/#HG-SN/HgSn-03Yen-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgSn-03Yen-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HgSn-03Yen-LB.tdb | 497.11 | LIQUID (x(Sn) 0.97249) + HGSN38 (x(Sn) 0.97436) + BCT_A5 (x(Sn) 1) |
| HgSn-03Yen-LB.tdb | 497.11 | LIQUID (x(Sn) 0.97263) + HGSN38 (x(Sn) 0.97436) + BCT_A5 (x(Sn) 1) |
| HgSn-03Yen-LB.tdb | 484.23 | LIQUID (x(Sn) 0.90438) + HGSN12_AF (x(Sn) 0.93723) + HGSN38 (x(Sn) 0.97436) |
| HgSn-03Yen-LB.tdb | 484.23 | LIQUID (x(Sn) 0.90444) + HGSN12_AF (x(Sn) 0.93725) + HGSN38 (x(Sn) 0.97436) |
| HgSn-03Yen-LB.tdb | 472.06 | HGSN12_AF (x(Sn) 0.94493) + HGSN38 (x(Sn) 0.97436) + BCT_A5 (x(Sn) 1) |
| HgSn-03Yen-LB.tdb | 362.08 | LIQUID (x(Sn) 0.13603) + HGSN7 (x(Sn) 0.875) + HGSN12_AF (x(Sn) 0.88285) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HG/HG-SN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HG/HG-SN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hg–Sn system (24)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 497.1 | peritectic: L + βSn -> β | L: Sn 0.9726 | model | [1] Yen 2003 | Table 8, p. 9, row 2 |  |
| 496.5 | peritectic: L + βSn -> β | L: Sn 0.97 | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 8, p. 9, row 3 |  |
| 487.5 | peritectic: L + β -> γ | L: Sn 0.9177; γ: Hg 0.076923, Sn 0.923077 | model | [1] Yen 2003 | Table 8, p. 9, row 4 |  |
| 487 | peritectic: L + β -> γ | L: Sn 0.912; γ: Hg 0.076923, Sn 0.923077 | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 8, p. 9, row 6 |  |
| 484.3 | peritectic |  | model | [1] Yen 2003 | p. 13 | “Calculated temperatures and compositions of invariant reactions in Case 2 compare well with the experimental data and are listed in Table 8, except for the peritectic calculated at 484.3 K.” |
| 484.2 | peritectic: L + β -> γ | L: Sn 0.9043; γ: Hg 0.076923, Sn 0.923077 | model | [1] Yen 2003 | Table 8, p. 9, row 5 |  |
| 473.4 | eutectoid: β -> γ + βSn | γ: Hg 0.076923, Sn 0.923077 | model | [1] Yen 2003 | Table 8, p. 9, row 7 |  |
| 472.1 | eutectoid: β -> γ + βSn | γ: Hg 0.076923, Sn 0.923077 | model | [1] Yen 2003 | Table 8, p. 9, row 8 |  |
| 471.5 | eutectoid: β -> γ + βSn | γ: Hg 0.076923, Sn 0.923077 | experimental | [1] Yen 2003 | Table 8, p. 9, row 9 |  |
| 368 | peritectic |  | experimental | [1] Yen 2003; _cites Yan-Sho-Syan 1969_ | p. 5 | “Literature values for the peritectic temperature include 363 K \[1937Pry\], 364.6 K \[1963Tay\], 368 K \[1969Yan\], 358 K \[1984Elh\], and 353 K \[1985Sar1\].” |
| 364.6 | peritectic |  | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | p. 5 | “Literature values for the peritectic temperature include 363 K \[1937Pry\], 364.6 K \[1963Tay\], 368 K \[1969Yan\], 358 K \[1984Elh\], and 353 K \[1985Sar1\].” |
| 363.5 | peritectic: L + γ -> δ | L: Sn 0.1453; γ: Hg 0.076923, Sn 0.923077 | model | [1] Yen 2003 | Table 8, p. 9, row 10 |  |
| 363 | peritectic: L + γ -> δ | γ: Hg 0.076923, Sn 0.923077 | experimental | [1] Yen 2003 | Table 8, p. 9, row 11 |  |
| 363 | peritectic |  | experimental | [1] Yen 2003; _cites Prytherch 1937_ | p. 5 | “Literature values for the peritectic temperature include 363 K \[1937Pry\], 364.6 K \[1963Tay\], 368 K \[1969Yan\], 358 K \[1984Elh\], and 353 K \[1985Sar1\].” |
| 358 | peritectic |  | experimental | [1] Yen 2003; _cites El-Handary 1984_ | p. 5 | “Literature values for the peritectic temperature include 363 K \[1937Pry\], 364.6 K \[1963Tay\], 368 K \[1969Yan\], 358 K \[1984Elh\], and 353 K \[1985Sar1\].” |
| 353 | peritectic |  | experimental | [1] Yen 2003; _cites Sarkar 1985_ | p. 5 | “Literature values for the peritectic temperature include 363 K \[1937Pry\], 364.6 K \[1963Tay\], 368 K \[1969Yan\], 358 K \[1984Elh\], and 353 K \[1985Sar1\].” |
| 265.6 | metatectic/catatectic: γ -> L + αSn | γ: Sn 0.9231; L: Sn 0.0127 | model | [1] Yen 2003 | Table 8, p. 9, row 12 |  |
| 265 | metatectic/catatectic: γ -> L + αSn | γ: Sn 0.926 | experimental | [1] Yen 2003; _cites Smith 1969_ [doi](https://doi.org/10.1179/cmq.1969.8.2.127) | Table 8, p. 9, row 13 |  |
| 262.2 | eutectoid: γ -> δ + αSn | γ: Sn 0.887 | model | [1] Yen 2003 | Table 8, p. 9, row 14 |  |
| 261.1 | metatectic/catatectic: δ -> L + αSn | L: Sn 0.0111 | model | [1] Yen 2003 | Table 8, p. 9, row 15 |  |
| 238.7 | peritectic: L + αSn -> HgSn4 | HgSn4: Hg 0.2, Sn 0.8 | experimental | [1] Yen 2003 | Table 8, p. 9, row 18 |  |
| 237.8 | peritectic: L + αSn -> HgSn4 | L: Sn 0.0054; HgSn4: Hg 0.2, Sn 0.8 | model | [1] Yen 2003 | Table 8, p. 9, row 16 |  |
| 234.7 | eutectic: L -> (Hg) + HgSn4 | HgSn4: Hg 0.2, Sn 0.8 | experimental | [1] Yen 2003 | Table 8, p. 9, row 21 |  |
| 233.4 | eutectic: L -> (Hg) + HgSn4 | L: Sn 0.0046; HgSn4: Hg 0.2, Sn 0.8 | model | [1] Yen 2003 | Table 8, p. 9, row 19 |  |

## Other properties

### Phase transition (31)

Table: Phase transition, Hg–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 233 K | 233 | other: HgSn4: Formation temperature: 233.0 K (0.24-0.57 at.% Sn) (a); _alloy: Hg 0.9976, Sn 0.0024_ | experimental | [1] Yen 2003; _cites P 1961_ | Table 2, p. 4, row 67 |  |
| Phase transition | 234.321 K | 234.321 |  | experimental | [1] Yen 2003 | p. 14 | “On the other hand the lowest thermal signals of mostly Sn-rich alloys, usually interpreted as "eutectic," are in the range 234-239 K, which is higher than the melting point of pure Hg accepted today, Tm(Hg) ⳱ 234.321 K.” |
| Phase transition | 238 K | 238 | other: HgSn4: Formation temperature: 238.0 K (0.16-0.41 at.% Sn) (a); _alloy: Hg 0.9984, Sn 0.0016_ | experimental | [1] Yen 2003; _cites Petot-Ervas 1967_ | Table 2, p. 4, row 65 |  |
| Phase transition | 238.6 K | 238.6 | other: HgSn4: Formation temperature: 238.6 K (0.3-85 at.% Sn) (a); _alloy: Hg 0.15, Sn 0.85_ | experimental | [1] Yen 2003; _cites W 1904_ | Table 2, p. 4, row 63 |  |
| Phase transition | 238.7 K | 238.7 | other: HgSn4: Formation temperature: 238.7 K (10-85 at.% Sn) (a); _alloy: Hg 0.15, Sn 0.85_ | experimental | [1] Yen 2003; _cites Yan-Sho-Syan 1969_ | Table 2, p. 4, row 66 |  |
| Phase transition | 238.8 K | 238.8 | other: HgSn4: Formation temperature: 238.8 K (8.7-14.4 at.% Sn) (a); _alloy: Hg 0.913, Sn 0.087_ | experimental | [1] Yen 2003; _cites Gayler 1937_ | Table 2, p. 4, row 64 |  |
| Phase transition | 261.1 K | 261.1 | other | model | [1] Yen 2003 | p. 13 | “This shows up in Fig. 10 by a very similar decomposition temperature of ␦ (261.1 K) and ␥ (262.2 K).” |
| Phase transition | 262.2 K | 262.2 | other | model | [1] Yen 2003 | p. 13 | “In fact, recalculating Fig. 10 with the ␦ phase suspended results in a metatectic decomposition of ␥ at 262.2 K, and also the liquidus line is virtually unchanged.” |
| Phase transition | 262.2 K | 262.2 | other | model | [1] Yen 2003 | p. 13 | “This shows up in Fig. 10 by a very similar decomposition temperature of ␦ (261.1 K) and ␥ (262.2 K).” |
| Phase transition | 265 K | 265 | other: γ: Decomposition temperature: 265.00 K (91.4-94.8 at.% Sn) (a); _alloy: Hg 0.086, Sn 0.914_ | experimental | [1] Yen 2003; _cites Smith 1969_ [doi](https://doi.org/10.1179/cmq.1969.8.2.127) | Table 2, p. 4, row 53 |  |
| Phase transition | 298 K | 298 | γ: Solubility range: 88-92 at.% Sn (298 K) (b) | experimental | [1] Yen 2003; _cites Che 1991_ [doi](https://doi.org/10.1007/bf01130189) | Table 2, p. 4, row 45 |  |
| Phase transition | 310 K | 310 | γ: Solubility range: 86.4-92.3 at.% Sn (310 K) (b) | experimental | [1] Yen 2003; _cites Aldinger 1976_ | Table 2, p. 4, row 48 |  |
| Phase transition | 331 K | 331 | other: ε: Formation temperature: 331 K (42.0-88.5 at.% Sn) (a); _alloy: Hg 0.58, Sn 0.42_ | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 2, p. 4, row 62 |  |
| Phase transition | 333 K | 333 | ε: Solubility range: 85.5-86.5 at.% Sn (333 K) (b) | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 2, p. 4, row 61 |  |
| Phase transition | 346.5 K | 346.5 | γ: Solubility range: 88-88.8 at.% Sn (310-383 K) (b) | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 2, p. 4, row 47 |  |
| Phase transition | 353 K | 353 | other: δ: Formation temperature: 353 K (10 at.% Sn) (a); _alloy: Hg 0.9, Sn 0.1_ | experimental | [1] Yen 2003; _cites Sarkar 1985_ | Table 2, p. 4, row 60 |  |
| Phase transition | 353 K | 353 | γ: Solubility range: 87-94 at.% Sn (353 K) (b) | experimental | [1] Yen 2003; _cites Claeson 1968_ [doi](https://doi.org/10.1002/pssb.19680250241) | Table 2, p. 4, row 46 |  |
| Phase transition | 358 K | 358 | other: δ: Formation temperature: 358 K | experimental | [1] Yen 2003; _cites ref. 1984Eih_ | Table 2, p. 4, row 59 |  |
| Phase transition | 363 K | 363 | other: δ: Formation temperature: 363 K (19.2-89.4 at.% Sn) (a); _alloy: Hg 0.808, Sn 0.192_ | experimental | [1] Yen 2003; _cites Prytherch 1937_ | Table 2, p. 4, row 56 |  |
| Phase transition | 364.4 K | 364.4 | other: δ: Formation temperature: 364.4 K (29.7-88.5 at.% Sn) (a); _alloy: Hg 0.703, Sn 0.297_ | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 2, p. 4, row 57 |  |
| Phase transition | 368 K | 368 | other: δ: Formation temperature: 368 K (30-80 at.% Sn) (a); _alloy: Hg 0.7, Sn 0.3_ | experimental | [1] Yen 2003; _cites Yan-Sho-Syan 1969_ | Table 2, p. 4, row 58 |  |
| Phase transition | 453 K | 453 | β: Existence of β phase: 93.5-98.5 at.% Sn (453 K) (b) | experimental | [1] Yen 2003; _cites Calvo 1987_ | Table 2, p. 4, row 40 |  |
| Phase transition | 470 K | 470 | other: β: Decomposition temperature: 470 K (93.8-98.8 at.% Sn) (a); _alloy: Hg 0.062, Sn 0.938_ | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 2, p. 4, row 39 |  |
| Phase transition | 471 K | 471 | other: β: Decomposition temperature: 471 K | experimental | [1] Yen 2003; _cites Gayler 1937_ | Table 2, p. 4, row 38 |  |
| Phase transition | 486 K | 486 | peritectic: γ: Formation temperature: 486 K | experimental | [1] Yen 2003; _cites Sarkar 1985_ | Table 2, p. 4, row 52 |  |
| Phase transition | 486.9 K | 486.9 | peritectic: γ: Formation temperature: 486.9 K | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 2, p. 4, row 49 |  |
| Phase transition | 487 K | 487 | peritectic: γ: Formation temperature: 487 K | experimental | [1] Yen 2003; _cites Yan-Sho-Syan 1969_ | Table 2, p. 4, row 51 |  |
| Phase transition | 496 K | 496 | other: β: Formation temperature: 496 K (93.8-98.8 at.% Sn) (a); _alloy: Hg 0.062, Sn 0.938_ | experimental | [1] Yen 2003; _cites Taylor 1963_ [doi](https://doi.org/10.6028/jres.067a.008) | Table 2, p. 4, row 37 |  |
| Phase transition | 497 K | 497 | other: β: Formation temperature: 497 K (96.6-99.3 at.% Sn) (a); _alloy: Hg 0.034, Sn 0.966_ | experimental | [1] Yen 2003; _cites ref. 1973Pry_ | Table 2, p. 4, row 36 |  |
| Phase transition | 497.6 K | 497.6 | peritectic: γ: Formation temperature: 497.6 K | experimental | [1] Yen 2003; _cites Predel 1969_ [doi](https://doi.org/10.1016/0001-6160%2869%2990085-6) | Table 2, p. 4, row 50 |  |
| Phase transition | 505 K | 505 | other | experimental | [1] Yen 2003 | p. 9 | “When the temperature is lower than 505 K (the melting temperature of Sn) the activity of tin, aSn, is converted to the reference state of pure solid Sn in the present assessment.” |

### Mixing / partial (1)

Table: Mixing / partial, Hg–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Partial enthalpy; _printed: ⌬H ⬁ Sn_ | 14 kJ/mol (basis unstated) | 293.15 |  | experimental | [1] Yen 2003; _cites Marco 1975_ [doi](https://doi.org/10.1016/0021-9614%2875%2990239-6) | p. 5 | “\[1975Mar\] reported the enthalpy of the Hg-Sn solution at infinite dilution of Sn (⌬H ⬁ Sn) at 293.15 K as 14.0 kJ/mol referred to liquid Hg and solid ␣Sn.” |

### Activity / EMF / Gibbs energy (2)

Table: Activity / EMF / Gibbs energy, Hg–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity; _printed: aSn_ | 0.927 unspecified | 298 |  | model | [1] Yen 2003 | p. 10 | “At 298 K for instance, aSn rises to 0.927 and then remains constant from xSn⳱ 0.027-0.923.” |
| Vapour pressure; _printed: vapor pressure_ | 7.502e-4 bar | 344 | ␥ | experimental | [1] Yen 2003; _cites Reynolds 1974_ [doi](https://doi.org/10.1002/jbm.820080604) | p. 4 | “Reynolds also determined the vapor pressure of ␥ phase from weight loss data and gave this value as 7.502 × 10-4 bar at 344 K \[1974Rey\].” |

### Crystal structure (14)

Table: Crystal structure, Hg–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.3005 nm | 234.3 (\<) | (Hg); _alloy: Sn 0_ | model | [1] Yen 2003 | Table 3, p. 6, row 1 |  |
| Lattice a | 0.64892 nm | 286.2 (\<) | (αSn); _(αSn): Hg 0, Sn 1_ | model | [1] Yen 2003 | Table 3, p. 6, row 4 |  |
| Lattice a | 0.58286 nm | 298 | (βSn); _(βSn): Hg 0.0072, Sn 0.9928_ | model | [1] Yen 2003 | Table 3, p. 6, row 3 |  |
| Lattice a | 0.555104 nm | 363.5 (\<) | δ, HgSn7; _δ, HgSn7: Hg 0.1288, Sn 0.8712_ | model | [1] Yen 2003 | Table 3, p. 6, row 8 |  |
| Lattice a | 0.32109 nm | 376.55 | γ, HgSn12; _alloy: Sn 0.923077_ | model | [1] Yen 2003 | Table 3, p. 6, row 6 |  |
| Lattice a | 0.58317 nm | 395.634 | (βSn); _(βSn): Hg 0, Sn 1_ | model | [1] Yen 2003 | Table 3, p. 6, row 2 |  |
| Lattice a | 0.32415 nm | 485.25 | β, HgSn38; _alloy: Sn 0.974359_ | model | [1] Yen 2003 | Table 3, p. 6, row 5 |  |
| Lattice b | 0.31791 nm | 363.5 (\<) | δ, HgSn7; _δ, HgSn7: Hg 0.1288, Sn 0.8712_ | model | [1] Yen 2003 | Table 3, p. 6, row 8 |  |
| Lattice c | 0.31805 nm | 298 | (βSn); _(βSn): Hg 0.0072, Sn 0.9928_ | model | [1] Yen 2003 | Table 3, p. 6, row 3 |  |
| Lattice c | 0.298311 nm | 363.5 (\<) | δ, HgSn7; _δ, HgSn7: Hg 0.1288, Sn 0.8712_ | model | [1] Yen 2003 | Table 3, p. 6, row 8 |  |
| Lattice c | 0.29888 nm | 376.55 | γ, HgSn12; _alloy: Sn 0.923077_ | model | [1] Yen 2003 | Table 3, p. 6, row 6 |  |
| Lattice c | 0.31813 nm | 395.634 | (βSn); _(βSn): Hg 0, Sn 1_ | model | [1] Yen 2003 | Table 3, p. 6, row 2 |  |
| Lattice c | 0.30065 nm | 485.25 | β, HgSn38; _alloy: Sn 0.974359_ | model | [1] Yen 2003 | Table 3, p. 6, row 5 |  |
| lattice alpha | 70.53 ° | 234.3 (\<) | (Hg); _alloy: Sn 0_ | model | [1] Yen 2003 | Table 3, p. 6, row 1 |  |

### Other property (1)

Table: Other property, Hg–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: heat of vaporization_ | 59.09 kJ/mol-atoms | 629.88 |  | experimental | [1] Yen 2003; _cites Elliott 1960_ | p. 1 | “Elliott and Gleiser \[1960Ell\] reported the heat of vaporization of Hg to be 59.09 kJ/mol-atoms at 629.88 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003). [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
