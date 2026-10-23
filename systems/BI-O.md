# Bi–O system

> Bi–O system: 86 accepted literature values (activity / EMF / Gibbs energy 38, invariant reaction 21, formation 13, phase transition 8) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-O.html · Markdown: https://data.orchid-project.org/systems/BI-O.md

86 accepted literature values from 1 paper(s) (experimental 77, model 8, unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-O.json) · [CSV](https://data.orchid-project.org/systems/BI-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-O/BiO-95Ris-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/BI-O.html) · [Markdown](https://data.orchid-project.org/systems/BI-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 77 |
| model | 8 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 21 |
| phase transition | 8 |
| formation | 13 |
| heat capacity / entropy / enthalpy | 6 |
| activity / EMF / Gibbs energy | 38 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiO-95Ris-LB.tdb | D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, J. Phase Equilib., 16, 223-34(1995). [doi:10.1007/BF02667306](https://doi.org/10.1007/BF02667306) | `77661bfd1c983207a3cf6a8d0a28007fb87424f1838742298c5fd6ec93295bfa` | [viewer](https://orchid-project.org/phase-diagrams/#BI-O/BiO-95Ris-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiO-95Ris-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiO-95Ris-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiO-95Ris-LB.tdb | 1060.59 | ION#2 (x(O) 0.0053) + ION (x(O) 0.5921) + BI2O3_C1 (x(O) 0.6) |
| BiO-95Ris-LB.tdb | 1002.13 | ION (x(O) 0.00307) + BI2O3_ALPHA (x(O) 0.6) + BI2O3_C1 (x(O) 0.6) |
| BiO-95Ris-LB.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(O) 0) + ION (x(O) 0) + BI2O3_ALPHA (x(O) 0.6) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–O system (21)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1095 | monotectic: L2 -> L1 + δ-Bi2O3 (monotectic) | δ-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Mehrotra 1995_ | Table I, p. 3, row 7 |  |
| 1093 | monotectic: L2 -> L1 + δ-Bi2O3 (monotectic) | δ-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Rao 1975_ | Table I, p. 3, row 6 |  |
| 1090 | monotectic: L2 -> L1 + δ-Bi2O3 (monotectic) | δ-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites B 1979_ | Table I, p. 3, row 8 |  |
| 1077 | monotectic: L2 -> L1 + δ-Bi2O3 (monotectic) | δ-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites S 1984_ | Table I, p. 3, row 9 |  |
| 1061 | monotectic: L2 -> L1 + δ-Bi2O3 (monotectic) | L2: O 0.592; L1: O 0.005; δ-Bi2O3: O 0.6 | model | [1] Risold 1995 | Table I, p. 3, row 10 |  |
| 1003 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites ref. 79Har_ | Table I, p. 3, row 16 |  |
| 1003 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Levin 1965_ [doi](https://doi.org/10.6028/jres.069a.023) | Table I, p. 3, row 12 |  |
| 1003 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Korobeinikova 1976_ | Table I, p. 3, row 15 |  |
| 1003 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Cubicciotti 1967_ [doi](https://doi.org/10.1021/je60035a021) | Table I, p. 3, row 13 |  |
| 1002 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites ref. 79Har_ | Table I, p. 3, row 17 |  |
| 1002 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6; L1: O 0.003 | model | [1] Risold 1995 | Table I, p. 3, row 25 |  |
| 1000 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Rao 1969_ [doi](https://doi.org/10.1021/j100723a031) | Table I, p. 3, row 14 |  |
| 997 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Kameda 1991_ [doi](https://doi.org/10.2320/jinstmet1952.55.5_536) | Table I, p. 3, row 23 |  |
| 997 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Kameda 1992_ [doi](https://doi.org/10.2320/jinstmet1952.56.8_900) | Table I, p. 3, row 24 |  |
| 997 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Fitzner 1980_ [doi](https://doi.org/10.1016/0040-6031%2880%2987127-9) | Table I, p. 3, row 21 |  |
| 991 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Mehrotra 1995_ | Table I, p. 3, row 19 |  |
| 990 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Gattow 1962_ [doi](https://doi.org/10.1002/zaac.19623180307) | Table I, p. 3, row 11 |  |
| 980 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites B 1979_ | Table I, p. 3, row 20 |  |
| 978 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Rao 1971_ [doi](https://doi.org/10.1016/0036-9748%2871%2990168-2) | Table I, p. 3, row 18 |  |
| 974 | polymorphic: δ-Bi2O3 -> α-Bi2O3 (+ L1) (solid state transition) | δ-Bi2O3: O 0.6; α-Bi2O3: O 0.6 | experimental | [1] Risold 1995; _cites Schaefer 1985_ | Table I, p. 3, row 22 |  |
| 544 | eutectic: L1 -> Bi + α-Bi2O3 (eutectic) | L1: O 4.000e-7; Bi: O 0; α-Bi2O3: O 0.6 | model | [1] Risold 1995 | Table I, p. 3, row 26 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Bi–O system (13)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -573.2 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Ditte 1892_ | p. 5 | “The enthalpy of formation of t~-Bi20 3 at 298 K was determined by solution calorimetry \[1892Dit, 09Mix\] and more recently by combustion calorimetry \[61Mah\]. It also was derived from emf measurements \[71Rao, 73Cha, 78Cah, 84Ito, 84Sch\] and mass spectrometry data \[80Sid\]. These results are listed in Table 6. The values from measurements at higher temperatures are relatively scattered, but they are…” |
| — |  | -570.2 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Rao 1971_ [doi](https://doi.org/10.1016/0036-9748%2871%2990168-2) | p. 5 | “The enthalpy of formation of t~-Bi20 3 at 298 K was determined by solution calorimetry \[1892Dit, 09Mix\] and more recently by combustion calorimetry \[61Mah\]. It also was derived from emf measurements \[71Rao, 73Cha, 78Cah, 84Ito, 84Sch\] and mass spectrometry data \[80Sid\]. These results are listed in Table 6. The values from measurements at higher temperatures are relatively scattered, but they are…” |
| α-Bi2O3 |  | -590.2 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites S 1984_ | Table 6, p. 5, row 8 |  |
| α-Bi2O3 |  | -587.5 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Sidorov 1980_ | Table 6, p. 5, row 4 |  |
| α-Bi2O3 |  | -581.6 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Cahen 1979_ | Table 6, p. 5, row 7 |  |
| α-Bi2O3 |  | -576.6 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Ditte 1892_ | Table 6, p. 5, row 1 |  |
| α-Bi2O3 |  | -573.9 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Mah 1961_ | Table 6, p. 5, row 3 |  |
| α-Bi2O3 |  | -570.3 kJ/mol (basis unstated) | 298 | unspecified |  |  | [1] Risold 1995 | Table 6, p. 5, row 11 |  |
| α-Bi2O3 |  | -569 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Mixter 1909_ [doi](https://doi.org/10.2475/ajs.s4-28.164.103) | Table 6, p. 5, row 2 |  |
| α-Bi2O3 |  | -567.8 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Schaefer 1985_ | Table 6, p. 5, row 10 |  |
| α-Bi2O3 |  | -567.4 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Rao 1971_ [doi](https://doi.org/10.1016/0036-9748%2871%2990168-2) | Table 6, p. 5, row 5 |  |
| α-Bi2O3 |  | -563.4 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites S 1984_ | Table 6, p. 5, row 9 |  |
| α-Bi2O3 |  | -550.6 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Risold 1995; _cites Chatterji 1973_ [doi](https://doi.org/10.1149/1.2403593) | Table 6, p. 5, row 6 |  |

## Other properties

### Phase transition (8)

Table: Phase transition, Bi–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1097 K | 1097 | congruent melting: L2 -> δ-Bi2O3 (melting point of Bi2O3); _L2: O 0.6; δ-Bi2O3: O 0.6_ | experimental | [1] Risold 1995; _cites ref. 79Har_ | Table I, p. 3, row 4 |  |
| Phase transition | 1097 K | 1097 | congruent melting: L2 -> δ-Bi2O3 (melting point of Bi2O3); _L2: O 0.6; δ-Bi2O3: O 0.6_ | experimental | [1] Risold 1995; _cites Gattow 1964_ [doi](https://doi.org/10.1002/zaac.19643280106) | Table I, p. 3, row 1 |  |
| Phase transition | 1098 K | 1098 | congruent melting: L2 -> δ-Bi2O3 (melting point of Bi2O3); _L2: O 0.6; δ-Bi2O3: O 0.6_ | experimental | [1] Risold 1995; _cites Levin 1965_ [doi](https://doi.org/10.6028/jres.069a.023) | Table I, p. 3, row 2 |  |
| Phase transition | 1098 K | 1098 | congruent melting: L2 -> δ-Bi2O3 (melting point of Bi2O3); _L2: O 0.6; δ-Bi2O3: O 0.6_ | model | [1] Risold 1995 | Table I, p. 3, row 5 |  |
| Phase transition | 1101 K | 1101 | congruent melting: L2 -> δ-Bi2O3 (melting point of Bi2O3); _L2: O 0.6; δ-Bi2O3: O 0.6_ | experimental | [1] Risold 1995; _cites Cubicciotti 1967_ [doi](https://doi.org/10.1021/je60035a021) | Table I, p. 3, row 3 |  |
| Phase transition | 1668 K | 1668 | Critical point | experimental | [1] Risold 1995; _cites B 1979_ | Table I, p. 3, row 27 |  |
| Phase transition | 1677 K | 1677 | Critical point | model | [1] Risold 1995 | Table I, p. 3, row 28 |  |
| Phase transition | 1950 K | 1950 | other | model | [1] Risold 1995 | p. 11 | “An experimental verification of the azeotropic boiling point at 1950 K is desirable.” |

### Heat capacity / entropy / enthalpy (6)

Table: Heat capacity / entropy / enthalpy, Bi–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S298_ | 30 J/mol-atom/K | 298 | α-Bi2O3; _alloy: O 0.6_ | experimental | [1] Risold 1995; _cites ref. 81Gor_ | Table 3, p. 4, row 2 |  |
| Entropy; _printed: S298_ | 30.2 J/mol-atom/K | 298 | α-Bi2O3; _alloy: O 0.6_ | experimental | [1] Risold 1995; _cites C 1937_ | Table 3, p. 4, row 1 |  |
| Entropy; _printed: S298_ | 29.7 J/mol-atom/K | 298 | α-Bi2O3; _alloy: O 0.6_ | model | [1] Risold 1995 | Table 3, p. 4, row 3 |  |
| Heat capacity; _printed: Cp_ | 22.68 J/mol-atom/K | 298 | α-Bi2O3; _alloy: O 0.6_ | experimental | [1] Risold 1995; _cites ref. 81Gor_ | Table 3, p. 4, row 2 |  |
| Heat capacity; _printed: Cp_ | 22.4 J/mol-atom/K | 298 | α-Bi2O3; _alloy: O 0.6_ | experimental | [1] Risold 1995; _cites C 1937_ | Table 3, p. 4, row 1 |  |
| Heat capacity; _printed: Cp_ | 22.42 J/mol-atom/K | 298 | α-Bi2O3; _alloy: O 0.6_ | model | [1] Risold 1995 | Table 3, p. 4, row 3 |  |

### Activity / EMF / Gibbs energy (38)

Table: Activity / EMF / Gibbs energy, Bi–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy; _printed: ΔG (A)_ | -581994 J/mol | 858 | α | experimental | [1] Risold 1995; _cites Schaefer 1985_ | Table 7, p. 6, row 41 |  |
| Gibbs energy; _printed: ΔG (A)_ | -629608 J/mol | 875.5 | α | experimental | [1] Risold 1995; _cites Rao 1971_ [doi](https://doi.org/10.1016/0036-9748%2871%2990168-2) | Table 7, p. 6, row 24 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 334.5 J/mol/K | 875.5 | α | experimental | [1] Risold 1995; _cites Rao 1971_ [doi](https://doi.org/10.1016/0036-9748%2871%2990168-2) | Table 7, p. 6, row 24 |  |
| Gibbs energy; _printed: ΔG (A)_ | -583592 J/mol | 901.5 | α | experimental | [1] Risold 1995; _cites B 1979_ | Table 7, p. 6, row 34 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 293.9 J/mol/K | 901.5 | α | experimental | [1] Risold 1995; _cites B 1979_ | Table 7, p. 6, row 34 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 293.4 J/mol/K | 917.5 | α | experimental | [1] Risold 1995; _cites Kameda 1992_ [doi](https://doi.org/10.2320/jinstmet1952.56.8_900) | Table 7, p. 6, row 45 |  |
| Gibbs energy; _printed: ΔG (A)_ | -600990 J/mol | 938 | α | experimental | [1] Risold 1995; _cites Mehrotra 1995_ | Table 7, p. 6, row 29 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 315.2 J/mol/K | 938 | α | experimental | [1] Risold 1995; _cites Mehrotra 1995_ | Table 7, p. 6, row 29 |  |
| Gibbs energy; _printed: ΔG (A)_ | -582520 J/mol | 942.5 | α | experimental | [1] Risold 1995; _cites Kameda 1991_ [doi](https://doi.org/10.2320/jinstmet1952.55.5_536) | Table 7, p. 6, row 43 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 265.4 J/mol/K | 945 | α, δ | experimental | [1] Risold 1995; _cites Chatterji 1973_ [doi](https://doi.org/10.1149/1.2403593) | Table 7, p. 6, row 28 |  |
| Gibbs energy; _printed: ΔG (A)_ | -560196 J/mol | 945 | α, δ | experimental | [1] Risold 1995; _cites Chatterji 1973_ [doi](https://doi.org/10.1149/1.2403593) | Table 7, p. 6, row 28 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 314.42 J/mol/K | 974 | α | experimental | [1] Risold 1995; _cites Fitzner 1980_ [doi](https://doi.org/10.1016/0040-6031%2880%2987127-9) | Table 7, p. 6, row 37 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 267.8 J/mol/K | 1012.5 | δ | experimental | [1] Risold 1995; _cites Cahen 1979_ | Table 7, p. 6, row 32 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 261.06 J/mol/K | 1031 | δ | experimental | [1] Risold 1995; _cites Kameda 1991_ [doi](https://doi.org/10.2320/jinstmet1952.55.5_536) | Table 7, p. 6, row 44 |  |
| Gibbs energy; _printed: ΔG (A)_ | -549700 J/mol | 1031 | δ | experimental | [1] Risold 1995; _cites Kameda 1991_ [doi](https://doi.org/10.2320/jinstmet1952.55.5_536) | Table 7, p. 6, row 44 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 261.1 J/mol/K | 1033.5 | δ | experimental | [1] Risold 1995; _cites Kameda 1992_ [doi](https://doi.org/10.2320/jinstmet1952.56.8_900) | Table 7, p. 6, row 46 |  |
| Gibbs energy; _printed: ΔG (A)_ | -549700 J/mol | 1033.5 | δ | experimental | [1] Risold 1995; _cites Kameda 1992_ [doi](https://doi.org/10.2320/jinstmet1952.56.8_900) | Table 7, p. 6, row 46 |  |
| Gibbs energy; _printed: ΔG (A)_ | -543905 J/mol | 1035 | δ | experimental | [1] Risold 1995; _cites B 1979_ | Table 7, p. 6, row 35 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 253.4 J/mol/K | 1035 | δ | experimental | [1] Risold 1995; _cites B 1979_ | Table 7, p. 6, row 35 |  |
| Gibbs energy; _printed: ΔG (A)_ | -572613 J/mol | 1035.5 | δ | experimental | [1] Risold 1995; _cites Rao 1975_ | Table 7, p. 6, row 26 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 227.3 J/mol/K | 1035.5 | δ | experimental | [1] Risold 1995; _cites Rao 1975_ | Table 7, p. 6, row 26 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 271.5 J/mol/K | 1043 | δ | experimental | [1] Risold 1995; _cites Mehrotra 1995_ | Table 7, p. 6, row 30 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 270.3 J/mol/K | 1048.5 | δ | experimental | [1] Risold 1995; _cites Fitzner 1980_ [doi](https://doi.org/10.1016/0040-6031%2880%2987127-9) | Table 7, p. 6, row 38 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 241.8 J/mol/K | 1049 | δ | experimental | [1] Risold 1995; _cites Schaefer 1985_ | Table 7, p. 6, row 42 |  |
| Gibbs energy; _printed: ΔG (A)_ | -532247 J/mol | 1049 | δ | experimental | [1] Risold 1995; _cites Schaefer 1985_ | Table 7, p. 6, row 42 |  |
| Gibbs energy; _printed: ΔG (A)_ | -545681 J/mol | 1121.5 | L | experimental | [1] Risold 1995; _cites Rao 1975_ | Table 7, p. 6, row 27 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 252.8 J/mol/K | 1121.5 | L | experimental | [1] Risold 1995; _cites Rao 1975_ | Table 7, p. 6, row 27 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 129.7 J/mol/K | 1148 | L | experimental | [1] Risold 1995; _cites ref. 79Hah_ | Table 7, p. 6, row 33 |  |
| Gibbs energy; _printed: ΔG (A)_ | -415471 J/mol | 1148 | L | experimental | [1] Risold 1995; _cites ref. 79Hah_ | Table 7, p. 6, row 33 |  |
| Gibbs energy; _printed: ΔG (A)_ | -373422 J/mol | 1150 | L | experimental | [1] Risold 1995; _cites Codron 1972_ | Table 7, p. 6, row 25 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 156.9 J/mol/K | 1150 | L | experimental | [1] Risold 1995; _cites Codron 1972_ | Table 7, p. 6, row 25 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 217.8 J/mol/K | 1159 | L | experimental | [1] Risold 1995; _cites Mehrotra 1995_ | Table 7, p. 6, row 31 |  |
| Gibbs energy; _printed: ΔG (A)_ | -498900 J/mol | 1159 | L | experimental | [1] Risold 1995; _cites Mehrotra 1995_ | Table 7, p. 6, row 31 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 235.91 J/mol/K | 1237 | L | experimental | [1] Risold 1995; _cites S 1984_ | Table 7, p. 6, row 40 |  |
| Gibbs energy; _printed: ΔG (A)_ | -520840 J/mol | 1237 | L | experimental | [1] Risold 1995; _cites S 1984_ | Table 7, p. 6, row 40 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 229.7 J/mol/K | 1356.5 | L | experimental | [1] Risold 1995; _cites B 1979_ | Table 7, p. 6, row 36 |  |
| Gibbs energy; _printed: ΔG (A)_ | -518007 J/mol | 1356.5 | L | experimental | [1] Risold 1995; _cites B 1979_ | Table 7, p. 6, row 36 |  |
| Gibbs energy; _printed: ΔG (B, coefficient of T)_ | 253.72 J/mol/K | 1475 | δ | experimental | [1] Risold 1995; _cites S 1984_ | Table 7, p. 6, row 39 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Risold, B. Hallstedt, L. J. Gauckler, H. L. Lukas, S. G. Fries, The bismuth-oxygen system, JPE 16 (1995). [doi:10.1007/bf02667306](https://doi.org/10.1007/bf02667306)

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
