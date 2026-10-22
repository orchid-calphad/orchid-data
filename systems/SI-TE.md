# Si–Te system

> Si–Te system: 24 accepted literature values (phase transition 18, formation 5, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SI-TE.html · Markdown: https://data.orchid-project.org/systems/SI-TE.md

24 accepted literature values from 1 paper(s) (experimental 17, model 7); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SI-TE.json) · [CSV](https://data.orchid-project.org/systems/SI-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SI-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SI-TE/SiTe-20Yua.json) · [Markdown](https://data.orchid-project.org/systems/SI-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 17 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 18 |
| formation | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SiTe-20Yua.tdb | H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020). [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) | `788eb4e0fb22d784b89158925eeda6927b682a3e46b84f4c0af29c586b90d6b5` | [viewer](https://orchid-project.org/phase-diagrams/#SI-TE/SiTe-20Yua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiTe-20Yua.json) |
| SiTe-99Feu-LB.tdb | Y. Feutelais, A. Schlieper, S.G. Fries, Calphad, 23, 365-78(1999). [doi:10.1016/S0364-5916(00)00007-9](https://doi.org/10.1016/S0364-5916%2800%2900007-9) | `0d62124cd250a55a5554101c3b5f31292094d5a990a1b3e8e227e9fa23feeb44` | [viewer](https://orchid-project.org/phase-diagrams/#SI-TE/SiTe-99Feu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiTe-99Feu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiTe-99Feu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SiTe-20Yua.tdb | 956.01 | DIAMOND_A4 (x(Te) 0) + SI2TE3_HT (x(Te) 0.6) + LIQUID (x(Te) 0.65859) |
| SiTe-20Yua.tdb | 713.91 | DIAMOND_A4 (x(Te) 0) + SI2TE3_LT (x(Te) 0.6) + SI2TE3_HT (x(Te) 0.6) |
| SiTe-20Yua.tdb | 713.91 | SI2TE3_HT (x(Te) 0.6) + SI2TE3_LT (x(Te) 0.6) + LIQUID (x(Te) 0.80186) |
| SiTe-20Yua.tdb | 707.55 | SI2TE3_LT (x(Te) 0.6) + SITE2_HT (x(Te) 0.66667) + LIQUID (x(Te) 0.80693) |
| SiTe-20Yua.tdb | 673.75 | SITE2_HT (x(Te) 0.66667) + LIQUID (x(Te) 0.8465) + HEXAGONAL_A8 (x(Te) 1) |
| SiTe-20Yua.tdb | 663.64 | SI2TE3_LT (x(Te) 0.6) + SITE2_C6 (x(Te) 0.66667) + SITE2_HT (x(Te) 0.66667) |
| SiTe-20Yua.tdb | 663.64 | SITE2_HT (x(Te) 0.66667) + SITE2_C6 (x(Te) 0.66667) + HEXAGONAL_A8 (x(Te) 1) |
| SiTe-99Feu-LB.tdb | 1165.1 | DIAMOND_A4 (x(Te) 0) + SI2TE3_HT (x(Te) 0.6) + LIQUID (x(Te) 0.6039) |
| SiTe-99Feu-LB.tdb | 680.17 | SI2TE3_HT (x(Te) 0.6) + LIQUID (x(Te) 0.86539) + HEXAGONAL_A8 (x(Te) 1) |
| SiTe-99Feu-LB.tdb | 674 | DIAMOND_A4 (x(Te) 0) + SI2TE3_LT (x(Te) 0.6) + SI2TE3_HT (x(Te) 0.6) |
| SiTe-99Feu-LB.tdb | 674 | SI2TE3_HT (x(Te) 0.6) + SI2TE3_LT (x(Te) 0.6) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SI/SI-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SI/SI-TE.json) · [CALPHAD hull SiTe-99Feu-LB](https://data.orchid-project.org/hulls/calphad-sgte/SI/SI-TE--SiTe-99Feu-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Si–Te system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1158.15 | peritectic |  | experimental | [1] Feutelais 1999; _cites ref. 16_ | p. 5 | “The reported values of \[16\] being measured on cooling, we may expect some delay in the observation of the peritectic invariant which explains the low observed temperature of 885°C.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Si–Te system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| α-Si2Te3 |  | -18.4 kJ/mol-atom ± 13 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites EXSTEEN 1967_ | Table 2, p. 9, row 3 |  |
| α-Si2Te3 |  | -17.8 kJ/mol-atom ± 19 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites EXSTEEN 1967_ | Table 2, p. 9, row 4 |  |
| α-Si2Te3 |  | -14.4 kJ/mol-atom ± 5 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites ref. 13_ | Table 2, p. 9, row 6 |  |
| α-Si2Te3 |  | -14.2 kJ/mol-atom ± 6 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites OHARE 1993_ | Table 2, p. 9, row 7 |  |
| α-Si2Te3 |  | -13.8 kJ/mol-atom ± 7 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites ref. 13_ | Table 2, p. 9, row 5 |  |

## Other properties

### Phase transition (18)

Table: Phase transition, Si–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 674.15 K | 674.15 |  | model | [1] Feutelais 1999 | p. 4 | “Thus we defined a hypothetical transformation temperature Ttrans = 401°C as being the average value of the reported measurements of \[17\].” |
| Phase transition | 674.15 K | 674.15 |  | model | [1] Feutelais 1999 | p. 6 | “As explained above, the temperature of transition of silicon sesquitelluride is 401°C and corresponds, according to our assumption, to equilibria between Si, (Y- SiaTes and ,B- S&Tea on the one hand and Q - S&Tea, p - SizTes and Te on the other hand.” |
| Phase transition | 679.15 K | 679.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 14_ | Table 1, p. 9, row 5 |  |
| Phase transition | 680.15 K | 680.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 16_ | Table 1, p. 9, row 8 |  |
| Phase transition | 680.15 K | 680.15 | peritectic | model | [1] Feutelais 1999 | Table 1, p. 9, row 12 |  |
| Phase transition | 682.15 K | 682.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 12_ | Table 1, p. 9, row 2 |  |
| Phase transition | 687.15 K | 687.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 17_ | Table 1, p. 9, row 10 |  |
| Phase transition | 1158.15 K | 1158.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 16_ | Table 1, p. 9, row 7 |  |
| Phase transition | 1159.15 K | 1159.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 17_ | Table 1, p. 9, row 9 |  |
| Phase transition | 1162.15 K | 1162.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 19_ | Table 1, p. 9, row 6 |  |
| Phase transition | 1165.15 K | 1165.15 |  | model | [1] Feutelais 1999 | p. 5 | “This confirms our choice of 892°C for this invariant temperature, as 7°C seems a realistic value for the temperature shift.” |
| Phase transition | 1165.15 K | 1165.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 13_ | Table 1, p. 9, row 3 |  |
| Phase transition | 1165.15 K | 1165.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 12_ | Table 1, p. 9, row 1 |  |
| Phase transition | 1165.25 K | 1165.25 | Si + L + p-SisTes | model | [1] Feutelais 1999 | p. 6 | “The calculated invariants are : T = 892.1"C Si + L + p-SisTes with zke = 0.604 T = 407.O"C L + ,&SisTes + Te with zTe L - 0.865” |
| Phase transition | 1165.25 K | 1165.25 | peritectic | model | [1] Feutelais 1999 | Table 1, p. 9, row 11 |  |
| Phase transition | 1168.15 K | 1168.15 | peritectic | experimental | [1] Feutelais 1999; _cites ref. 14_ | Table 1, p. 9, row 4 |  |
| Phase transition | 1406 K | 1406 | liquidus | model | [1] Feutelais 1999; _cites ref. 14_ | p. 5 | “As shown in the Figure 1, the liquidus data reported by \[14\] (1406 K, XT= = 0.4) was not used in the final optimization data file because it is in complete disagreement with other results.” |
| Phase transition | 1684.15 K | 1684.15 |  | experimental | [1] Feutelais 1999; _cites ref. 16_ | p. 5 | “On thte contrary, \[16\] reported an observed melting point of pure silicon at 1411°C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Y. Feutelais, A. Schlieper, S.G. Fries, Thermodynamic evaluation of the system silicon — Tellurium, Calphad 23, 365-378 (1999). [doi:10.1016/s0364-5916(00)00007-9](https://doi.org/10.1016/s0364-5916%2800%2900007-9)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
