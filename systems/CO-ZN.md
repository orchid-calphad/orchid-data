# Co–Zn system

> Co–Zn system: 171 accepted literature values (heat capacity / entropy / enthalpy 71, invariant reaction 50, activity / EMF / Gibbs energy 31, crystal structure 11) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-ZN.html · Markdown: https://data.orchid-project.org/systems/CO-ZN.md

171 accepted literature values from 3 paper(s) (experimental 31, model 133, unspecified 7); 2 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-ZN.json) · [CSV](https://data.orchid-project.org/systems/CO-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-ZN/CoZn-04Iso.json) · [phases (11)](https://data.orchid-project.org/phases/pages/CO-ZN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CO-ZN.html) · [Markdown](https://data.orchid-project.org/systems/CO-ZN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 31 |
| model | 133 |
| unspecified | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 50 |
| phase transition | 7 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 71 |
| activity / EMF / Gibbs energy | 31 |
| crystal structure | 11 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoZn-04Iso.tdb | I. Isomaki, M. Hamalainen, J. Alloys Compd., 375, 191-95(2004). [doi:10.1016/j.jallcom.2003.12.002](https://doi.org/10.1016/j.jallcom.2003.12.002) | `97df739c925a45d73399da0ace5613907a1163adc8c9c1156a33887d24047c68` | [viewer](https://orchid-project.org/phase-diagrams/#CO-ZN/CoZn-04Iso.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoZn-04Iso.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoZn-04Iso.json) |
| CoZn-04Vas-LB.tdb | G.P. Vassilev, M. Jiang, J. Phase Equilib. Diffus., 25, 259-68(2004). [doi:10.1361/15477030419522](https://doi.org/10.1361/15477030419522) | `d5353920b632f1aefcf74117ee09772c9e9c51dfafbd906be2684535a59fb413` | [viewer](https://orchid-project.org/phase-diagrams/#CO-ZN/CoZn-04Vas-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoZn-04Vas-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoZn-04Vas-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoZn-04Iso.tdb | 1233.14 | FCC_A1 (x(Zn) 0.36965) + COZN_A13 (x(Zn) 0.50256) + LIQUID (x(Zn) 0.60169) |
| CoZn-04Iso.tdb | 1147.69 | COZN_A13 (x(Zn) 0.5699) + CO5ZN21_D83 (x(Zn) 0.6858) + LIQUID (x(Zn) 0.76351) |
| CoZn-04Iso.tdb | 1017.46 | CO5ZN21_D83 (x(Zn) 0.79955) + CO3ZN22 (x(Zn) 0.88) + LIQUID (x(Zn) 0.94818) |
| CoZn-04Iso.tdb | 1017.46 | CO5ZN21_D83 (x(Zn) 0.79961) + CO3ZN22 (x(Zn) 0.88) + LIQUID (x(Zn) 0.94828) |
| CoZn-04Iso.tdb | 850.44 | CO3ZN22 (x(Zn) 0.88) + CO2ZN28 (x(Zn) 0.93333) + LIQUID (x(Zn) 0.99761) |
| CoZn-04Iso.tdb | 850.44 | CO3ZN22 (x(Zn) 0.88) + CO2ZN28 (x(Zn) 0.93333) + LIQUID (x(Zn) 0.9976) |
| CoZn-04Iso.tdb | 850.44 | CO3ZN22 (x(Zn) 0.88) + CO2ZN28 (x(Zn) 0.93333) + LIQUID (x(Zn) 0.99763) |
| CoZn-04Iso.tdb | 692.69 | CO2ZN28 (x(Zn) 0.93333) + HCP_A3 (x(Zn) 0.99996) + LIQUID (x(Zn) 0.99999) |
| CoZn-04Iso.tdb | 692.69 | CO2ZN28 (x(Zn) 0.93333) + HCP_A3 (x(Zn) 0.99996) + LIQUID (x(Zn) 0.99999) |
| CoZn-04Iso.tdb | 594.01 | HCP_A3 (x(Zn) 0.04023) + FCC_A1 (x(Zn) 0.05102) + COZN_A13 (x(Zn) 0.49304) |
| CoZn-04Vas-LB.tdb | 1246.52 | FCC_A1 (x(Zn) 0.3524) + BCC_A2 (x(Zn) 0.49323) + LIQUID (x(Zn) 0.66052) |
| CoZn-04Vas-LB.tdb | 1193.9 | BCC_A2 (x(Zn) 0.53266) + COZN_A13 (x(Zn) 0.53367) + LIQUID (x(Zn) 0.69768) |
| CoZn-04Vas-LB.tdb | 1193.31 | FCC_A1 (x(Zn) 0.36444) + BCC_A2 (x(Zn) 0.49806) + COZN_A13 (x(Zn) 0.5004) |
| CoZn-04Vas-LB.tdb | 1176.77 | COZN_A13 (x(Zn) 0.5576) + CO5ZN21_D83 (x(Zn) 0.69099) + LIQUID (x(Zn) 0.71556) |
| CoZn-04Vas-LB.tdb | 1016.39 | CO5ZN21_D83 (x(Zn) 0.79771) + CO2ZN15 (x(Zn) 0.88235) + LIQUID (x(Zn) 0.92129) |
| CoZn-04Vas-LB.tdb | 1016.39 | CO5ZN21_D83 (x(Zn) 0.79768) + CO2ZN15 (x(Zn) 0.88235) + LIQUID (x(Zn) 0.92123) |
| CoZn-04Vas-LB.tdb | 1014.74 | FCC_A1 (x(Zn) 0.20042) + FCC_A1#2 (x(Zn) 0.2335) + COZN_A13 (x(Zn) 0.46737) |
| CoZn-04Vas-LB.tdb | 961.13 | CO5ZN21_D83 (x(Zn) 0.80554) + COZN7 (x(Zn) 0.875) + CO2ZN15 (x(Zn) 0.88235) |
| CoZn-04Vas-LB.tdb | 961.13 | CO5ZN21_D83 (x(Zn) 0.80559) + COZN7 (x(Zn) 0.875) + CO2ZN15 (x(Zn) 0.88235) |
| CoZn-04Vas-LB.tdb | 961.13 | CO5ZN21_D83 (x(Zn) 0.80554) + COZN7 (x(Zn) 0.875) + CO2ZN15 (x(Zn) 0.88235) |
| CoZn-04Vas-LB.tdb | 948.09 | COZN7 (x(Zn) 0.875) + CO2ZN15 (x(Zn) 0.88235) + LIQUID (x(Zn) 0.96117) |
| CoZn-04Vas-LB.tdb | 948.09 | COZN7 (x(Zn) 0.875) + CO2ZN15 (x(Zn) 0.88235) + LIQUID (x(Zn) 0.96106) |
| CoZn-04Vas-LB.tdb | 948.09 | COZN7 (x(Zn) 0.875) + CO2ZN15 (x(Zn) 0.88235) + LIQUID (x(Zn) 0.96125) |
| CoZn-04Vas-LB.tdb | 840.18 | COZN7 (x(Zn) 0.875) + COZN13 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.99056) |
| CoZn-04Vas-LB.tdb | 840.18 | COZN7 (x(Zn) 0.875) + COZN13 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.99051) |
| CoZn-04Vas-LB.tdb | 840.18 | COZN7 (x(Zn) 0.875) + COZN13 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.9906) |
| CoZn-04Vas-LB.tdb | 692.6 | COZN13 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.99985) + HCP_A3 (x(Zn) 1) |
| CoZn-04Vas-LB.tdb | 692.6 | COZN13 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.99985) + HCP_A3 (x(Zn) 1) |
| CoZn-04Vas-LB.tdb | 658.52 | HCP_A3 (x(Zn) 0.02803) + FCC_A1 (x(Zn) 0.037) + COZN_A13 (x(Zn) 0.52497) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-ZN.json) · [CALPHAD hull CoZn-04Vas-LB](https://data.orchid-project.org/hulls/calphad-sgte/CO/CO-ZN--CoZn-04Vas-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Co–Zn system (50)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1768 | congruent melting: (αCo) ↔ Co(L) |  | model | [1] Vassilev 2004 | Table 4, p. 7, row 24 |  |
| 1768 | congruent melting: (αCo) ↔ Co(L) |  | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 23 |  |
| 1246 | Liquid -> β1 + Fcc_A1 | β1: Zn 0.5 | experimental | [2] Isomäki 2004; _cites Takayama 1995_ [doi](https://doi.org/10.1007/bf02645345) | Table 1, p. 2, row 2 |  |
| 1239 | peritectic: α + L \<-> β | α: Zn 0.358; L: Zn 0.664; β: Zn 0.495 | model | [1] Vassilev 2004 | Table 3, p. 6, row 3 |  |
| 1239 | peritectic: α + L ↔ β |  | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 21 |  |
| 1239 | peritectic: α + L \<-> β | α: Zn 0.375; L: Zn 0.64; β: Zn 0.495 | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | Table 3, p. 6, row 2 |  |
| 1238.95 | peritectic: α + L ↔ β |  | model | [1] Vassilev 2004 | Table 4, p. 7, row 22 |  |
| 1233 | Liquid -> β1 + Fcc_A1 | β1: Zn 0.5 | model | [2] Isomäki 2004 | Table 1, p. 2, row 1 |  |
| 1198 | peritectoid: α + β ↔ β1 | β1: Co 0.5, Zn 0.5 | model | [1] Vassilev 2004 | Table 4, p. 7, row 20 |  |
| 1198 | peritectoid: α + β \<-> β1 | α: Zn 0.368; β: Zn 0.506; β1: Zn 0.502 | model | [1] Vassilev 2004 | Table 3, p. 6, row 5 |  |
| 1198 | peritectoid: α + β ↔ β1 | β1: Co 0.5, Zn 0.5 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 19 |  |
| 1198 | peritectoid: α + β \<-> β1 | α: Zn 0.375; β: Zn 0.495; β1: Zn 0.475 | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | Table 3, p. 6, row 4 |  |
| 1197 | eutectoid: β ↔ β1 + γ | β1: Co 0.5, Zn 0.5; γ: Co 0.192308, Zn 0.807692 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 17 |  |
| 1197 | peritectic: L + β1 \<-> β | L: Zn 0.694; β1: Zn 0.529; β: Zn 0.532 | model | [1] Vassilev 2004 | Table 3, p. 6, row 7 |  |
| 1197 | peritectic: L + β1 \<-> β | L: Zn 0.665; β1: Zn 0.515; β: Zn 0.535 | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | Table 3, p. 6, row 6 |  |
| 1197 | eutectoid: β ↔ β1 + γ | β1: Co 0.5, Zn 0.5; γ: Co 0.192308, Zn 0.807692 | model | [1] Vassilev 2004 | Table 4, p. 7, row 18 |  |
| 1177 | peritectic: L + β1 \<-> γ | L: Zn 0.716; β1: Zn 0.557; γ: Zn 0.691 | model | [1] Vassilev 2004 | Table 3, p. 6, row 10 |  |
| 1176.82 | peritectic: L + β1 ↔ γ | β1: Co 0.5, Zn 0.5; γ: Co 0.192308, Zn 0.807692 | model | [1] Vassilev 2004 | Table 4, p. 7, row 16 |  |
| 1168 | peritectic: L + β1 ↔ γ | β1: Co 0.5, Zn 0.5; γ: Co 0.192308, Zn 0.807692 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 15 |  |
| 1168 | peritectic: L + β1 \<-> γ | L: Zn 0.71; β1: Zn 0.538; γ: Zn 0.69 | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | Table 3, p. 6, row 8 |  |
| 1168 | peritectic: L + β1 \<-> γ | β1: Zn 0.54; γ: Zn 0.66 | unspecified | [1] Vassilev 2004; _cites Takayama 1995_ | Table 3, p. 6, row 9 |  |
| 1168 | Liquid -> β1 + γ | β1: Zn 0.5; γ: Zn 0.807692 | experimental | [2] Isomäki 2004; _cites Takayama 1995_ [doi](https://doi.org/10.1007/bf02645345) | Table 1, p. 2, row 4 |  |
| 1168 | peritectic: L + γ \<-> δ | L: Zn 0.921; γ: Zn 0.798; δ: Zn 0.882 | model | [1] Vassilev 2004 | Table 3, p. 6, row 12 |  |
| 1148 | Liquid -> β1 + γ | β1: Zn 0.5; γ: Zn 0.807692 | model | [2] Isomäki 2004 | Table 1, p. 2, row 3 |  |
| 1019 | peritectic: L + γ \<-> δ | L: Zn 0.931; γ: Zn 0.845; δ: Zn 0.875 | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | Table 3, p. 6, row 11 |  |
| 1019 | peritectic: L + γ ↔ δ | γ: Co 0.192308, Zn 0.807692; δ: Co 0.117647, Zn 0.882353 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 13 |  |
| 1016.49 | peritectic: L + γ ↔ δ | γ: Co 0.192308, Zn 0.807692; δ: Co 0.117647, Zn 0.882353 | model | [1] Vassilev 2004 | Table 4, p. 7, row 14 |  |
| 1015 | monotectoid: (αCo) (b) \<-> (αCo) (c) + β1 | β1: Zn 0.467 | model | [1] Vassilev 2004 | Table 3, p. 6, row 23 |  |
| 1014.7 | monotectic: (αCo) (c) ↔ (αCo) (d) + β1 | β1: Co 0.5, Zn 0.5 | model | [1] Vassilev 2004 | Table 4, p. 7, row 4 |  |
| 963 | peritectoid: γ + δ ↔ γ1 | γ: Co 0.192308, Zn 0.807692; δ: Co 0.117647, Zn 0.882353; γ1: Co 0.125, Zn 0.875 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 11 |  |
| 963 | peritectoid: γ + δ \<-> γ1 | γ: Zn 0.854; δ: Zn 0.88; γ1: Zn 0.875 | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | Table 3, p. 6, row 13 |  |
| 961.13 | peritectoid: γ + δ ↔ γ1 | γ: Co 0.192308, Zn 0.807692; δ: Co 0.117647, Zn 0.882353; γ1: Co 0.125, Zn 0.875 | model | [1] Vassilev 2004 | Table 4, p. 7, row 12 |  |
| 961 | peritectoid: γ + δ \<-> γ1 | γ: Zn 0.806; δ: Zn 0.882; γ1: Zn 0.875 | model | [1] Vassilev 2004 | Table 3, p. 6, row 14 |  |
| 948.07 | peritectic: δ ↔ L + γ1 | δ: Co 0.117647, Zn 0.882353; γ1: Co 0.125, Zn 0.875 | model | [1] Vassilev 2004 | Table 4, p. 7, row 10 |  |
| 948 | peritectic |  | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | p. 2 | “The ␦-phase decomposes peritectically (Table 3) at 948 K \[1958Han, 1996Mas\], and no information about its structure could be found.” |
| 948 | peritectic: δ \<-> L + γ1 | δ: Co 0.117647, Zn 0.882353; L: Zn 0.961; γ1: Zn 0.875 | model | [1] Vassilev 2004 | Table 3, p. 6, row 16 |  |
| 948 | peritectic: δ \<-> L + γ1 | δ: Zn 0.9; L: Zn 0.97; γ1: Zn 0.875 | experimental | [1] Vassilev 2004; _cites Pierce 1923_ | Table 3, p. 6, row 15 |  |
| 948 | peritectic: δ ↔ L + γ1 | δ: Co 0.117647, Zn 0.882353; γ1: Co 0.125, Zn 0.875 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 9 |  |
| 840.25 | peritectic: L + γ1 ↔ γ2 | γ1: Co 0.125, Zn 0.875; γ2: Co 0.071429, Zn 0.928571 | model | [1] Vassilev 2004 | Table 4, p. 7, row 8 |  |
| 840 | peritectic: γ1 + L \<-> γ2 | γ1: Zn 0.875; L: Zn 0.991; γ2: Zn 0.9285 | model | [1] Vassilev 2004 | Table 3, p. 6, row 18 |  |
| 839 | peritectic: γ1 + L \<-> γ2 | γ1: Zn 0.9; L: Zn 0.991; γ2: Zn 0.917 | experimental | [1] Vassilev 2004; _cites Hansen 1958_ | Table 3, p. 6, row 17 |  |
| 839 | peritectic: L + γ1 ↔ γ2 | γ1: Co 0.125, Zn 0.875; γ2: Co 0.071429, Zn 0.928571 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 7 |  |
| 692.66 | eutectic: L ↔ γ2 + (Zn) | γ2: Co 0.071429, Zn 0.928571 | model | [1] Vassilev 2004 | Table 4, p. 7, row 6 |  |
| 692.65 | eutectic: L \<-> γ2 + (Zn) | L: Zn 0.9998; γ2: Co 0.071429, Zn 0.928571; (Zn): Zn 1 | model | [1] Vassilev 2004 | Table 3, p. 6, row 20 |  |
| 692.6 | eutectic: L \<-> γ2 + (Zn) | γ2: Co 0.071429, Zn 0.928571; (Zn): Zn 1 | experimental | [1] Vassilev 2004; _cites Pierce 1923_ | Table 3, p. 6, row 19 |  |
| 692.6 | eutectic: L ↔ γ2 + (Zn) | γ2: Co 0.071429, Zn 0.928571 | experimental | [1] Vassilev 2004 | Table 4, p. 7, row 5 |  |
| 692 | eutectic |  | experimental | [1] Vassilev 2004; _cites Pierce 1923_ | p. 1 | “Lewkonja \[1908Lew\] as well as Pierce and Palmerton \[1923Pie\] were the first to study the equilibrium between the liquid and the solid phases in the Zn-rich region; they found eutectic invariants at 686 K and at 692 K, respectively.” |
| 686 | eutectic |  | experimental | [1] Vassilev 2004; _cites Lewkonja 1908_ | p. 1 | “Lewkonja \[1908Lew\] as well as Pierce and Palmerton \[1923Pie\] were the first to study the equilibrium between the liquid and the solid phases in the Zn-rich region; they found eutectic invariants at 686 K and at 692 K, respectively.” |
| 658.48 | eutectoid: (αCo) ↔ (εCo) + β1 | β1: Co 0.5, Zn 0.5 | model | [1] Vassilev 2004 | Table 4, p. 7, row 3 |  |
| 658 | eutectoid: (αCo) \<-> (εCo) + β1 | (αCo): Zn 0.037; (εCo): Zn 0.028; β1: Zn 0.525 | model | [1] Vassilev 2004 | Table 3, p. 6, row 24 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Co–Zn system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -8 kJ/mol (basis unstated) | 1750 | model |  |  | [1] Vassilev 2004 | p. 7 | “The pertinent values calculated with the optimized coefficients, however, are -13 and -8 kJ mol-1 (at 1750 K), respectively.” |

## Other properties

### Phase transition (7)

Table: Phase transition, Co–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 398 K | 398 | magnetic | experimental | [1] Vassilev 2004; _cites Schramm 1938_ | p. 1 | “The ␤ 1 -phase is ferromagnetic below 398 K \[1938Sch3, 1941Sch, 1958Han, 1951Mey\], but no details about the concentration dependence of the TC are known.” |
| Phase transition | 410 K | 410 | magnetic | model | [1] Vassilev 2004 | p. 7 | “The calculations show (Fig. 7) that the magnetic transition in the ␤1-phase occurs at temperatures between 454 K (53.9 at.% Zn) and 410 K (57.1 at.% Zn).” |
| Phase transition | 454 K | 454 | magnetic | model | [1] Vassilev 2004 | p. 7 | “The calculations show (Fig. 7) that the magnetic transition in the ␤1-phase occurs at temperatures between 454 K (53.9 at.% Zn) and 410 K (57.1 at.% Zn).” |
| Phase transition | 658 K | 658 | other | model | [1] Vassilev 2004 | p. 1 | “For the first time, a eutectoid decomposition (at around 658 K) of the fcc solutions has been predicted.” |
| Phase transition | 692.68 K | 692.68 | other | model | [2] Isomäki 2004; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | p. 1 | “The melting point of cobalt was evaluated as 1768.00 K and for the zinc as 692.68 K, Dinsdale \[11\].” |
| Phase transition | 695 K | 695 | polymorphic | experimental | [1] Vassilev 2004; _cites Guillermet 1987_ | p. 1 | “It is known \[1987Gui, 1990Nis, 1991Ray\] that, during heating, the pure hexagonal close-packed Co (HCP-Co or ␧-Co) undergoes a polymorphic transition at about 695 K and converts to its high-temperature form \[face-centeredcubic (fcc)-Co or ␣-Co\].” |
| Phase transition | 1768 K | 1768 | other | model | [2] Isomäki 2004; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | p. 1 | “The melting point of cobalt was evaluated as 1768.00 K and for the zinc as 692.68 K, Dinsdale \[11\].” |

### Heat capacity / entropy / enthalpy (71)

Table: Heat capacity / entropy / enthalpy, Co–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy | 36.5 J/mol-atom/K | 298.15 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 11 |  |
| Entropy | 39.8 J/mol-atom/K | 298.15 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 1 |  |
| Entropy | 41.1 J/mol-atom/K | 298.15 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 21 |  |
| Entropy | 44.5 J/mol-atom/K | 358.38 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 2 |  |
| Entropy | 42.2 J/mol-atom/K | 371.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 12 |  |
| Entropy | 47.2 J/mol-atom/K | 377.97 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 22 |  |
| Entropy | 48.6 J/mol-atom/K | 418.62 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 3 |  |
| Entropy | 47 J/mol-atom/K | 445.48 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 13 |  |
| Entropy | 52.3 J/mol-atom/K | 457.78 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 23 |  |
| Entropy | 52.2 J/mol-atom/K | 478.85 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 4 |  |
| Entropy | 51.1 J/mol-atom/K | 519.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 14 |  |
| Entropy | 56.7 J/mol-atom/K | 537.6 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 24 |  |
| Entropy | 55.4 J/mol-atom/K | 539.08 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 5 |  |
| Entropy | 54.8 J/mol-atom/K | 592.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 15 |  |
| Entropy | 58.4 J/mol-atom/K | 599.32 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 6 |  |
| Entropy | 60.6 J/mol-atom/K | 617.41 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 25 |  |
| Entropy | 61.1 J/mol-atom/K | 659.55 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 7 |  |
| Entropy | 58.2 J/mol-atom/K | 666.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 16 |  |
| Entropy | 64.1 J/mol-atom/K | 697.23 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 26 |  |
| Entropy | 63.7 J/mol-atom/K | 719.78 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 8 |  |
| Entropy | 61.3 J/mol-atom/K | 740.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 17 |  |
| Entropy | 67.4 J/mol-atom/K | 777.04 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 27 |  |
| Entropy | 66.2 J/mol-atom/K | 780.02 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 9 |  |
| Entropy | 64.3 J/mol-atom/K | 813.8 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 18 |  |
| Entropy | 68.5 J/mol-atom/K | 840.25 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 10 |  |
| Entropy | 70.4 J/mol-atom/K | 856.86 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 28 |  |
| Entropy | 66.9 J/mol-atom/K | 887.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 19 |  |
| Entropy | 73.2 J/mol-atom/K | 936.67 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 29 |  |
| Entropy | 69.4 J/mol-atom/K | 961.13 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 20 |  |
| Entropy | 75.7 J/mol-atom/K | 1016.49 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 30 |  |
| Heat capacity; _printed: Cp_ | 31.1 J/mol-atom/K | 298.15 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 19 |  |
| Heat capacity; _printed: Cp_ | 25.4 J/mol-atom/K | 298.15 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 11 |  |
| Heat capacity; _printed: Cp_ | 25.4 J/mol-atom/K | 298.15 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 1 |  |
| Heat capacity; _printed: Cp_ | 31.1 J/mol-atom/K | 298.15 | γ2 | model | [1] Vassilev 2004 | Table 7, p. 9, row 10 |  |
| Heat capacity; _printed: Cp_ | 25.4 J/mol-atom/K | 298.15 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 21 |  |
| Heat capacity; _printed: Cp_ | 25.9 J/mol-atom/K | 358.38 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 2 |  |
| Heat capacity; _printed: Cp_ | 26 J/mol-atom/K | 371.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 12 |  |
| Heat capacity; _printed: Cp_ | 26.1 J/mol-atom/K | 377.97 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 22 |  |
| Heat capacity; _printed: Cp_ | 26.5 J/mol-atom/K | 418.62 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 3 |  |
| Heat capacity; _printed: Cp_ | 26.8 J/mol-atom/K | 445.48 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 13 |  |
| Heat capacity; _printed: Cp_ | 26.9 J/mol-atom/K | 457.78 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 23 |  |
| Heat capacity; _printed: Cp_ | 27.1 J/mol-atom/K | 478.85 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 4 |  |
| Heat capacity; _printed: Cp_ | 27.5 J/mol-atom/K | 519.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 14 |  |
| Heat capacity; _printed: Cp_ | 27.7 J/mol-atom/K | 537.6 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 24 |  |
| Heat capacity; _printed: Cp_ | 27.8 J/mol-atom/K | 539.08 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 5 |  |
| Heat capacity; _printed: Cp_ | 28.4 J/mol-atom/K | 592.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 15 |  |
| Heat capacity; _printed: Cp_ | 28.5 J/mol-atom/K | 599.32 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 6 |  |
| Heat capacity; _printed: Cp_ | 28.7 J/mol-atom/K | 617.41 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 25 |  |
| Heat capacity; _printed: Cp_ | 29.2 J/mol-atom/K | 659.55 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 7 |  |
| Heat capacity; _printed: Cp_ | 29.3 J/mol-atom/K | 666.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 16 |  |
| Heat capacity; _printed: Cp_ | 29.7 J/mol-atom/K | 697.23 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 26 |  |
| Heat capacity; _printed: Cp_ | 30.2 J/mol-atom/K | 719.78 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 8 |  |
| Heat capacity; _printed: Cp_ | 30.4 J/mol-atom/K | 740.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 17 |  |
| Heat capacity; _printed: Cp_ | 30.7 J/mol-atom/K | 777.04 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 27 |  |
| Heat capacity; _printed: Cp_ | 30.8 J/mol-atom/K | 780.02 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 9 |  |
| Heat capacity; _printed: Cp_ | 30.9 J/mol-atom/K | 813.8 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 18 |  |
| Heat capacity; _printed: Cp_ | 31.1 J/mol-atom/K | 840.25 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 10 |  |
| Heat capacity; _printed: Cp_ | 31.1 J/mol-atom/K | 856.86 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 28 |  |
| Heat capacity; _printed: Cp_ | 31.1 J/mol-atom/K | 887.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 19 |  |
| Heat capacity; _printed: Cp_ | 31.2 J/mol-atom/K | 936.67 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 29 |  |
| Heat capacity; _printed: Cp_ | 31.3 J/mol-atom/K | 961.13 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 20 |  |
| Heat capacity; _printed: Cp_ | 31.4 J/mol-atom/K | 1016.49 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 30 |  |
| Heat content; _printed: Enthalpy_ | -9100 J·mol−1 per mol-atom | 371.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 12 |  |
| Heat content; _printed: Enthalpy_ | -7100 J·mol−1 per mol-atom | 445.48 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 13 |  |
| Heat content; _printed: Enthalpy_ | -5100 J·mol−1 per mol-atom | 519.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 14 |  |
| Heat content; _printed: Enthalpy_ | -3100 J·mol−1 per mol-atom | 592.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 15 |  |
| Heat content; _printed: Enthalpy_ | -1000 J·mol−1 per mol-atom | 666.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 16 |  |
| Heat content; _printed: Enthalpy_ | 1200 J·mol−1 per mol-atom | 740.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 17 |  |
| Heat content; _printed: Enthalpy_ | 3500 J·mol−1 per mol-atom | 813.8 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 18 |  |
| Heat content; _printed: Enthalpy_ | 5800 J·mol−1 per mol-atom | 887.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 19 |  |
| Heat content; _printed: Enthalpy_ | 8100 J·mol−1 per mol-atom | 961.13 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 20 |  |

### Activity / EMF / Gibbs energy (31)

Table: Activity / EMF / Gibbs energy, Co–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy; _printed: G_ | -21900 J·mol−1 per mol-atom | 298.15 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 11 |  |
| Gibbs energy; _printed: G_ | -26300 J · mol^-1 per mol-atom | 298.15 | γ2 | model | [1] Vassilev 2004 | Table 7, p. 9, row 4 |  |
| Gibbs energy; _printed: G_ | -18000 J · mol^-1 per mol-atom | 298.15 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 1 |  |
| Gibbs energy; _printed: G_ | -18700 J mol-1 per mol-atom | 298.15 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 21 |  |
| Gibbs energy; _printed: G_ | -20500 J · mol^-1 per mol-atom | 358.38 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 2 |  |
| Gibbs energy; _printed: G_ | -24800 J·mol−1 per mol-atom | 371.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 12 |  |
| Gibbs energy; _printed: G_ | -22300 J mol-1 per mol-atom | 377.97 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 22 |  |
| Gibbs energy; _printed: G_ | -23300 J · mol^-1 per mol-atom | 418.62 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 3 |  |
| Gibbs energy; _printed: G_ | -28100 J·mol−1 per mol-atom | 445.48 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 13 |  |
| Gibbs energy; _printed: G_ | -26300 J mol-1 per mol-atom | 457.78 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 23 |  |
| Gibbs energy; _printed: G_ | -26300 J · mol^-1 per mol-atom | 478.85 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 4 |  |
| Gibbs energy; _printed: G_ | -31700 J·mol−1 per mol-atom | 519.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 14 |  |
| Gibbs energy; _printed: G_ | -30600 J mol-1 per mol-atom | 537.6 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 24 |  |
| Gibbs energy; _printed: G_ | -29600 J · mol^-1 per mol-atom | 539.08 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 5 |  |
| Gibbs energy; _printed: G_ | -35600 J·mol−1 per mol-atom | 592.81 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 5, p. 9, row 15 |  |
| Gibbs energy; _printed: G_ | -33000 J · mol^-1 per mol-atom | 599.32 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 6 |  |
| Gibbs energy; _printed: G_ | -35300 J mol-1 per mol-atom | 617.41 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 25 |  |
| Gibbs energy; _printed: G_ | -36600 J · mol^-1 per mol-atom | 659.55 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 7 |  |
| Gibbs energy; _printed: G_ | -39800 J·mol−1 per mol-atom | 666.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 16 |  |
| Gibbs energy; _printed: G_ | -40300 J mol-1 per mol-atom | 697.23 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 26 |  |
| Gibbs energy; _printed: G_ | -40400 J · mol^-1 per mol-atom | 719.78 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 8 |  |
| Gibbs energy; _printed: G_ | -44200 J·mol−1 per mol-atom | 740.14 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 17 |  |
| Gibbs energy; _printed: G_ | -45500 J mol-1 per mol-atom | 777.04 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 27 |  |
| Gibbs energy; _printed: G_ | -44300 J · mol^-1 per mol-atom | 780.02 | γ2 | model | [1] Vassilev 2004 | Table 5, p. 9, row 9 |  |
| Gibbs energy; _printed: G_ | -48800 J·mol−1 per mol-atom | 813.8 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 18 |  |
| Gibbs energy; _printed: G_ | -48300 J · mol^-1 per mol-atom | 840.25 | γ2 | model | [1] Vassilev 2004 | Table 6, p. 9, row 10 |  |
| Gibbs energy; _printed: G_ | -51000 J mol-1 per mol-atom | 856.86 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 28 |  |
| Gibbs energy; _printed: G_ | -53600 J·mol−1 per mol-atom | 887.47 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 19 |  |
| Gibbs energy; _printed: G_ | -56700 J mol-1 per mol-atom | 936.67 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 29 |  |
| Gibbs energy; _printed: G_ | -58700 J·mol−1 per mol-atom | 961.13 | γ1-phase (CoZn7); _alloy: Zn 0.875_ | model | [1] Vassilev 2004 | Table 6, p. 9, row 20 |  |
| Gibbs energy; _printed: G_ | -62700 J mol-1 per mol-atom | 1016.49 | δ-Phase (Co2Zn15); _alloy: Zn 0.882353_ | model | [1] Vassilev 2004 | Table 7, p. 9, row 30 |  |

### Crystal structure (11)

Table: Crystal structure, Co–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 6.345 Å | 298.15 | β1-CoZn; _alloy: Co 0.5, Zn 0.5_ | unspecified | [3] Chen 2013; _cites Lihl 1955_ | Table 1, p. 3, row 1 |  |
| Lattice a | 8.9525 Å | 298.15 | γ-Co5Zn21; _alloy: Co 0.192308, Zn 0.807692_ | experimental | [3] Chen 2013; _cites Lihl 1955_ | Table 1, p. 3, row 2 |  |
| Lattice a | 8.927 Å | 298.15 | γ-Co5Zn21; _alloy: Co 0.192308, Zn 0.807692_ | unspecified | [3] Chen 2013; _cites Zhao 2012_ [doi](https://doi.org/10.1016/j.tca.2012.07.002) | Table 1, p. 3, row 3 |  |
| Lattice a | 9.03 Å | 298.15 | γ1-CoZn7.8; _alloy: Co 0.113636, Zn 0.886364_ | unspecified | [3] Chen 2013; _cites Lind 2003_ [doi](https://doi.org/10.1107/s0108768103019694) | Table 1, p. 3, row 4 |  |
| Lattice a | 13.306 Å | 298.15 | γ2-CoZn13; _alloy: Co 0.071429, Zn 0.928571_ | experimental | [3] Chen 2013; _cites Lihl 1955_ | Table 1, p. 3, row 5 |  |
| Lattice b | 4.338 Å | 298.15 | γ1-CoZn7.8; _alloy: Co 0.113636, Zn 0.886364_ | unspecified | [3] Chen 2013; _cites Lind 2003_ [doi](https://doi.org/10.1107/s0108768103019694) | Table 1, p. 3, row 4 |  |
| Lattice b | 7.535 Å | 298.15 | γ2-CoZn13; _alloy: Co 0.071429, Zn 0.928571_ | experimental | [3] Chen 2013; _cites Lihl 1955_ | Table 1, p. 3, row 5 |  |
| Lattice c | 12.511 Å | 298.15 | γ1-CoZn7.8; _alloy: Co 0.113636, Zn 0.886364_ | unspecified | [3] Chen 2013; _cites Lind 2003_ [doi](https://doi.org/10.1107/s0108768103019694) | Table 1, p. 3, row 4 |  |
| Lattice c | 4.992 Å | 298.15 | γ2-CoZn13; _alloy: Co 0.071429, Zn 0.928571_ | experimental | [3] Chen 2013; _cites Lihl 1955_ | Table 1, p. 3, row 5 |  |
| lattice beta | 89.9 ° | 298.15 | γ1-CoZn7.8; _alloy: Co 0.113636, Zn 0.886364_ | unspecified | [3] Chen 2013; _cites Lind 2003_ [doi](https://doi.org/10.1107/s0108768103019694) | Table 1, p. 3, row 4 |  |
| lattice beta | 126.47 ° | 298.15 | γ2-CoZn13; _alloy: Co 0.071429, Zn 0.928571_ | experimental | [3] Chen 2013; _cites Lihl 1955_ | Table 1, p. 3, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. George Penev Vassilev, Min Jiang, Thermodynamic Optimization of the Co-Zn System, Journal of Phase Equilibria &amp; Diffusion 25, 259-268 (2004). [doi:10.1361/15477030419522](https://doi.org/10.1361/15477030419522)
2. I Isomäki, M Hämäläinen, Thermodynamic evaluation of the Co–Zn system, Journal of Alloys and Compounds 375, 191-195 (2004). [doi:10.1016/j.jallcom.2003.12.002](https://doi.org/10.1016/j.jallcom.2003.12.002)
3. Zhu Chen, Fucheng Yin, Manxiu Zhao, Zhi Li, Experimental Investigation and Thermodynamic Calculation of the B-Co-Zn Ternary System, J. Phase Equilib. Diffus. 34, 366-374 (2013). [doi:10.1007/s11669-013-0245-y](https://doi.org/10.1007/s11669-013-0245-y)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
