# Ag–Pt system

> Ag–Pt system: 68 accepted literature values (phase equilibrium 43, crystal structure 20, invariant reaction 5) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-PT.html · Markdown: https://data.orchid-project.org/systems/AG-PT.md

68 accepted literature values from 1 paper(s) (experimental 28, model 40); 2 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-PT.json) · [CSV](https://data.orchid-project.org/systems/AG-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-PT/AgPt-87Kar.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AG-PT.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-PT.html) · [Markdown](https://data.orchid-project.org/systems/AG-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 28 |
| model | 40 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase equilibrium | 43 |
| crystal structure | 20 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgPt-87Kar.tdb | I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 8, 334-40(1987). [doi:10.1007/BF02869269](https://doi.org/10.1007/BF02869269) | `8f1b7c8efd759d85fd7f42982ce1b6a6f8ef476b2a97b7f64c034036e47e3405` | [viewer](https://orchid-project.org/phase-diagrams/#AG-PT/AgPt-87Kar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgPt-87Kar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgPt-87Kar.json) |
| AgPt-98Spe-LB.tdb | P.J. Spencer, unpublished, 1998. | `8e3cf7fc3b829b06ed29e597b3366d293b13a00dcf5b62c6efadb94a7beb5f2a` | [viewer](https://orchid-project.org/phase-diagrams/#AG-PT/AgPt-98Spe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgPt-98Spe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgPt-98Spe-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgPt-87Kar.tdb | 1472.28 | LIQUID (x(Pt) 0.19403) + FCC_A1#2 (x(Pt) 0.40847) + FCC_A1 (x(Pt) 0.7764) |
| AgPt-98Spe-LB.tdb | 1459.08 | LIQUID (x(Pt) 0.25107) + FCC_A1#2 (x(Pt) 0.44126) + FCC_A1 (x(Pt) 0.76073) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-PT.json) · [CALPHAD hull AgPt-87Kar](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-PT--AgPt-87Kar.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Pt system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1459.15 | peritectic: L + (Pt) -> (Ag) | L: Pt 0.201; (Pt): Pt 0.779; (Ag): Pt 0.406 | model | [1] Karakaya 1987 | Table 1, p. 1, row 1; `ORC-DQN7ZTJ7KH` |  |
| 1173.15 | eutectoid: (Ag) -> α' + (Pt) | (Ag): Pt 0.344; α': Pt 0.325; (Pt): Pt 0.843; α′: Pt 0.325 | model | [1] Karakaya 1987 | Table 1, p. 1, row 2; `ORC-QLHRIVOBWI` |  |
| 1013.15 | peritectoid: α' + (Pt) -> β | α': Pt 0.31; (Pt): Pt 0.85; β: Pt 0.5; α′: Pt 0.31 | model | [1] Karakaya 1987 | Table 1, p. 1, row 3; `ORC-O3CIA4ZH6U` |  |
| 973.15 | peritectoid: β + (Pt) -> γ | β: Pt 0.53; (Pt): Pt 0.915; γ: Pt 0.75 | model | [1] Karakaya 1987 | Table 1, p. 1, row 4; `ORC-4VPLKQ6YIY` |  |
| 943.15 | peritectoid: α" + β -> β' | α": Pt 0.275; β: Pt 0.465; β': Pt 0.445; α″: Pt 0.275; β′: Pt 0.445 | model | [1] Karakaya 1987 | Table 1, p. 1, row 5; `ORC-APB2CUPC3G` |  |

## Other properties

### Phase equilibrium (43)

Table: Phase equilibrium, Ag–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1173.15 | (Ag) + (Pt); _(Ag): Ag 0.656, Pt 0.344; (Pt): Ag 0.157, Pt 0.843_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 13; `ORC-WMFUCC5K76` |  |
| Phase composition |  | 1223.15 | (Ag) + (Pt); _(Ag): Ag 0.646, Pt 0.354; (Pt): Ag 0.167, Pt 0.833_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 12; `ORC-Q32ZB3A72R` |  |
| Phase composition |  | 1235.05 | L + (Ag); _L: Ag 1, Pt 0; (Ag): Ag 1, Pt 0_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 1; `ORC-NXWWDQAEKE` |  |
| Phase composition |  | 1263.15 | liquid + L; _liquid: Ag 0.98, Pt 0.02; L: Ag 0.98, Pt 0.02_ | experimental | [1] Karakaya 1987; _cites Heycock 1907_ | Table 2, p. 3, row 2; `ORC-CW5RT3OWJD` |  |
| Phase composition |  | 1263.15 | liquid + L; _liquid: Ag 0.986, Pt 0.014; L: Ag 0.986, Pt 0.014_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 1; `ORC-J6L4OUO2KN` |  |
| Phase composition |  | 1273.15 | (Ag) + (Pt); _(Ag): Ag 0.635, Pt 0.365; (Pt): Ag 0.178, Pt 0.822_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 11; `ORC-LUK7JYQLQU` |  |
| Phase composition |  | 1273.15 | L + (Ag); _L: Ag 0.98, Pt 0.02; (Ag): Ag 0.952, Pt 0.048_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 2; `ORC-BNHHQLYCRS` |  |
| Phase composition |  | 1318.15 | liquid + L; _liquid: Ag 0.944, Pt 0.056; L: Ag 0.944, Pt 0.056_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 3; `ORC-GQSR4DMQ2O` |  |
| Phase composition |  | 1318.15 | liquid + L; _liquid: Ag 0.942, Pt 0.058; L: Ag 0.942, Pt 0.058_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 4; `ORC-YWL3T7PG3X` |  |
| Phase composition |  | 1323.15 | (Ag) + (Pt); _(Ag): Ag 0.625, Pt 0.375; (Pt): Ag 0.189, Pt 0.811_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 10; `ORC-2FIKQUMJ6H` |  |
| Phase composition |  | 1323.15 | L + (Ag); _L: Ag 0.94, Pt 0.06; (Ag): Ag 0.885, Pt 0.115_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 3; `ORC-HS3GIQDJ7P` |  |
| Phase composition |  | 1373.15 | (Ag) + (Pt); _(Ag): Ag 0.614, Pt 0.386; (Pt): Ag 0.2, Pt 0.8_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 9; `ORC-OOIK64GZWD` |  |
| Phase composition |  | 1373.15 | L + (Ag); _L: Ag 0.888, Pt 0.112; (Ag): Ag 0.806, Pt 0.194_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 4; `ORC-XE3E5Z36UC` |  |
| Phase composition |  | 1393.15 | liquid + L; _liquid: Ag 0.867, Pt 0.133; L: Ag 0.867, Pt 0.133_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 5; `ORC-535YVXSQNK` |  |
| Phase composition |  | 1393.15 | liquid + L; _liquid: Ag 0.878, Pt 0.122; L: Ag 0.878, Pt 0.122_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 6; `ORC-FJ3EQ5NTTF` |  |
| Phase composition |  | 1423.15 | (Ag) + (Pt); _(Ag): Ag 0.603, Pt 0.397; (Pt): Ag 0.212, Pt 0.788_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 8; `ORC-6WHX5TI7TX` |  |
| Phase composition |  | 1423.15 | L + (Ag); _L: Ag 0.833, Pt 0.167; (Ag): Ag 0.706, Pt 0.294_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 5; `ORC-GHFUGDAAIU` |  |
| Phase composition |  | 1454.15 | liquid + L; _liquid: Ag 0.803, Pt 0.197; L: Ag 0.803, Pt 0.197_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 7; `ORC-OTFX7V25YX` |  |
| Phase composition |  | 1454.15 | liquid + L; _liquid: Ag 0.808, Pt 0.192; L: Ag 0.808, Pt 0.192_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 8; `ORC-VNNGJVYICD` |  |
| Phase composition |  | 1459.15 | (Ag) + (Pt); _(Ag): Ag 0.594, Pt 0.406; (Pt): Ag 0.221, Pt 0.779_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 7; `ORC-PTHBFDK7KE` |  |
| Phase composition |  | 1459.15 | L + (Ag); _L: Ag 0.799, Pt 0.201; (Ag): Ag 0.594, Pt 0.406_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 6; `ORC-JJWXWMJJP6` |  |
| Phase composition |  | 1459.15 | L + (Pt); _L: Ag 0.799, Pt 0.201; (Pt): Ag 0.221, Pt 0.779_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 14; `ORC-5ABM4TBWO7` |  |
| Phase composition |  | 1473.15 | L + (Pt); _L: Ag 0.793, Pt 0.207; (Pt): Ag 0.208, Pt 0.792_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 15; `ORC-6N7ARXPZKA` |  |
| Phase composition |  | 1523.15 | L + (Pt); _L: Ag 0.772, Pt 0.228; (Pt): Ag 0.178, Pt 0.822_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 16; `ORC-6CHNP7J75B` |  |
| Phase composition |  | 1573.15 | L + (Pt); _L: Ag 0.748, Pt 0.252; (Pt): Ag 0.159, Pt 0.841_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 17; `ORC-ZEVJTFJLBE` |  |
| Phase composition |  | 1623.15 | L + (Pt); _L: Ag 0.721, Pt 0.279; (Pt): Ag 0.145, Pt 0.855_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 18; `ORC-ZH7NC7RCVD` |  |
| Phase composition |  | 1673.15 | L + (Pt); _L: Ag 0.69, Pt 0.31; (Pt): Ag 0.132, Pt 0.868_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 19; `ORC-6DZKUAIZQP` |  |
| Phase composition |  | 1723.15 | L + (Pt); _L: Ag 0.652, Pt 0.348; (Pt): Ag 0.122, Pt 0.878_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 20; `ORC-SA6372PCWW` |  |
| Phase composition |  | 1736.15 | liquid + L; _liquid: Ag 0.64, Pt 0.36; L: Ag 0.64, Pt 0.36_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 9; `ORC-2SDUABR2DE` |  |
| Phase composition |  | 1736.15 | liquid + L; _liquid: Ag 0.643, Pt 0.357; L: Ag 0.643, Pt 0.357_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 10; `ORC-KRHMMN5XDP` |  |
| Phase composition |  | 1773.15 | L + (Pt); _L: Ag 0.601, Pt 0.399; (Pt): Ag 0.112, Pt 0.888_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 21; `ORC-ZLPLE2QSSY` |  |
| Phase composition |  | 1808.15 | liquid + L; _liquid: Ag 0.545, Pt 0.455; L: Ag 0.545, Pt 0.455_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 11; `ORC-BC3NEZ5E5Q` |  |
| Phase composition |  | 1808.15 | liquid + L; _liquid: Ag 0.545, Pt 0.455; L: Ag 0.545, Pt 0.455_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 12; `ORC-YIZIPEKAKK` |  |
| Phase composition |  | 1823.15 | L + (Pt); _L: Ag 0.508, Pt 0.492; (Pt): Ag 0.102, Pt 0.898_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 22; `ORC-3ZE76DGHTA` |  |
| Phase composition |  | 1832.15 | liquid + L; _liquid: Ag 0.435, Pt 0.565; L: Ag 0.435, Pt 0.565_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 14; `ORC-EJYMJSFLDQ` |  |
| Phase composition |  | 1832.15 | liquid + L; _liquid: Ag 0.475, Pt 0.525; L: Ag 0.475, Pt 0.525_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 13; `ORC-OECBDUB3MT` |  |
| Phase composition |  | 1861.15 | liquid + L; _liquid: Ag 0.31, Pt 0.69; L: Ag 0.31, Pt 0.69_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 16; `ORC-O7KMW4O26Y` |  |
| Phase composition |  | 1861.15 | liquid + L; _liquid: Ag 0.306, Pt 0.694; L: Ag 0.306, Pt 0.694_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 15; `ORC-Z4BHOEP5TU` |  |
| Phase composition |  | 1873.15 | L + (Pt); _L: Ag 0.265, Pt 0.735; (Pt): Ag 0.086, Pt 0.914_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 23; `ORC-A4BP2Z5YUP` |  |
| Phase composition |  | 1923.15 | L + (Pt); _L: Ag 0.157, Pt 0.843; (Pt): Ag 0.062, Pt 0.938_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 24; `ORC-G4YMVDD4JP` |  |
| Phase composition |  | 1973.15 | L + (Pt); _L: Ag 0.083, Pt 0.917; (Pt): Ag 0.036, Pt 0.964_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 25; `ORC-NMKODNARMQ` |  |
| Phase composition |  | 2023.15 | L + (Pt); _L: Ag 0.019, Pt 0.981; (Pt): Ag 0.008, Pt 0.992_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 26; `ORC-UPTSN2EGNR` |  |
| Phase composition |  | 2042.15 | L + (Pt); _L: Ag 0, Pt 1; (Pt): Ag 0, Pt 1_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 27; `ORC-FJQVIX6RRR` |  |

### Crystal structure (20)

Table: Crystal structure, Ag–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.067 Å |  | (Ag); _(Ag): Ag 0.946, Pt 0.054_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 3; `ORC-2CU6AV67AS.97975c` |  |
| Lattice a | 3.895 Å |  | α″; _α″: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 11; `ORC-G4A2BVBUDI.e4a009` |  |
| Lattice a | 3.89 Å | 298.15 | γ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 12; `ORC-Y7YAZS2EN7.ca0e7b` |  |
| Lattice a | 4.061 Å | 1023.15 | (Ag); _(Ag): Ag 0.93, Pt 0.07_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 4; `ORC-AWMTEO5IVA.3cb055` |  |
| Lattice a | 4.068 Å | 1073.15 | (Ag); _(Ag): Ag 0.972, Pt 0.028_ | experimental | [1] Karakaya 1987; _cites Novikova 1957_ | Table 4, p. 4, row 2; `ORC-F3OCR2Q2RI.b70615` |  |
| Lattice a | 3.91 Å | 1093.15 | α′; _α′: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 10; `ORC-JI7DCF6UXP.e0dcda` |  |
| Lattice a | 3.932 Å | 1403.15 | (Pt); _(Pt): Ag 0.2, Pt 0.8_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 5; `ORC-37IEKJHCNH.f88fbe` |  |
| Lattice a | 3.921 Å | 1403.15 | (Pt); _(Pt): Ag 0.08, Pt 0.92_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 7; `ORC-7723WY7YCG.677ea7` |  |
| Lattice a | 3.917 Å | 1403.15 | (Pt); _(Pt): Ag 0.06, Pt 0.94_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 8; `ORC-P5HCQ3FO47.6feb09` |  |
| Lattice a | 3.928 Å | 1403.15 | (Pt); _(Pt): Ag 0.14, Pt 0.86_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 6; `ORC-PCOEWFJY3J.dff252` |  |
| lattice unspecified axis | 3.89 Å | 298.15 | γ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 12; `ORC-Y7YAZS2EN7.bea494` |  |
| lattice unspecified axis | 4.061 Å | 1023.15 | (Ag); _(Ag): Ag 0.93, Pt 0.07_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 4; `ORC-AWMTEO5IVA.812853` |  |
| lattice unspecified axis | 4.068 Å | 1073.15 | (Ag); _(Ag): Ag 0.972, Pt 0.028_ | experimental | [1] Karakaya 1987; _cites Novikova 1957_ | Table 4, p. 4, row 2; `ORC-F3OCR2Q2RI.5fa150` |  |
| lattice unspecified axis | 3.895 Å | 1073.15 | α″; _α″: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 11; `ORC-G4A2BVBUDI.5151f3` |  |
| lattice unspecified axis | 3.91 Å | 1093.15 | α′; _α′: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 10; `ORC-JI7DCF6UXP.2d20ee` |  |
| lattice unspecified axis | 4.067 Å | 1173.15 | (Ag); _(Ag): Ag 0.946, Pt 0.054_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 3; `ORC-2CU6AV67AS.f528d0` |  |
| lattice unspecified axis | 3.932 Å | 1403.15 | (Pt); _(Pt): Ag 0.2, Pt 0.8_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 5; `ORC-37IEKJHCNH.920ff1` |  |
| lattice unspecified axis | 3.921 Å | 1403.15 | (Pt); _(Pt): Ag 0.08, Pt 0.92_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 7; `ORC-7723WY7YCG.d09ba3` |  |
| lattice unspecified axis | 3.917 Å | 1403.15 | (Pt); _(Pt): Ag 0.06, Pt 0.94_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 8; `ORC-P5HCQ3FO47.cc4d5b` |  |
| lattice unspecified axis | 3.928 Å | 1403.15 | (Pt); _(Pt): Ag 0.14, Pt 0.86_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 6; `ORC-PCOEWFJY3J.f1e992` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Karakaya, W. T. Thompson, The Ag-Pt (Silver-Platinum) system, Bulletin of Alloy Phase Diagrams 8, 334-340 (1987). [doi:10.1007/bf02869269](https://doi.org/10.1007/bf02869269)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
