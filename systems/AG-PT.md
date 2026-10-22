# Ag–Pt system

> Ag–Pt system: 74 accepted literature values (phase equilibrium 43, crystal structure 24, invariant reaction 7) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-PT.html · Markdown: https://data.orchid-project.org/systems/AG-PT.md

74 accepted literature values from 1 paper(s) (experimental 33, model 41); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-PT.json) · [CSV](https://data.orchid-project.org/systems/AG-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-PT/AgPt-87Kar.json) · [Markdown](https://data.orchid-project.org/systems/AG-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 33 |
| model | 41 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase equilibrium | 43 |
| crystal structure | 24 |

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

Table: Invariant reactions reported in the literature for the Ag–Pt system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1459.15 | peritectic: L + (Pt) -> (Ag) | L: Pt 0.201; (Pt): Pt 0.779; (Ag): Pt 0.406 | model | [1] Karakaya 1987 | Table 1, p. 1, row 1 |  |
| 1459.15 | peritectic |  | model | [1] Karakaya 1987 | p. 3 | “The assessed peritectic is between liquid with 20.1 at.% Pt a n d fcc solid solutions of 40.6 at.% Pt a n d 77.9 at.% Pt at 1186 ~” |
| 1457.15 | peritectic: liquid + Pt-rich solid solution -> Ag-rich solid solution |  | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | p. 3 | “The measured peritectic t e m p e r a t u r e is 1184 ~ \[07Doe\[, b u t this has a precision of only -+5 ~” |
| 1173.15 | eutectoid: (Ag) -> α' + (Pt) | (Ag): Pt 0.344; α': Pt 0.325; (Pt): Pt 0.843; α′: Pt 0.325 | model | [1] Karakaya 1987 | Table 1, p. 1, row 2 |  |
| 1013.15 | peritectoid: α' + (Pt) -> β | α': Pt 0.31; (Pt): Pt 0.85; β: Pt 0.5; α′: Pt 0.31 | model | [1] Karakaya 1987 | Table 1, p. 1, row 3 |  |
| 973.15 | peritectoid: β + (Pt) -> γ | β: Pt 0.53; (Pt): Pt 0.915; γ: Pt 0.75 | model | [1] Karakaya 1987 | Table 1, p. 1, row 4 |  |
| 943.15 | peritectoid: α" + β -> β' | α": Pt 0.275; β: Pt 0.465; β': Pt 0.445; α″: Pt 0.275; β′: Pt 0.445 | model | [1] Karakaya 1987 | Table 1, p. 1, row 5 |  |

## Other properties

### Phase equilibrium (43)

Table: Phase equilibrium, Ag–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 900 | (Ag) + (Pt); _(Ag): Ag 0.656, Pt 0.344; (Pt): Ag 0.157, Pt 0.843_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 13 |  |
| Phase composition |  | 950 | (Ag) + (Pt); _(Ag): Ag 0.646, Pt 0.354; (Pt): Ag 0.167, Pt 0.833_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 12 |  |
| Phase composition |  | 961.9 | L + (Ag); _L: Ag 1, Pt 0; (Ag): Ag 1, Pt 0_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 1 |  |
| Phase composition |  | 1000 | (Ag) + (Pt); _(Ag): Ag 0.635, Pt 0.365; (Pt): Ag 0.178, Pt 0.822_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 11 |  |
| Phase composition |  | 1000 | L + (Ag); _L: Ag 0.98, Pt 0.02; (Ag): Ag 0.952, Pt 0.048_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 2 |  |
| Phase composition |  | 1050 | (Ag) + (Pt); _(Ag): Ag 0.625, Pt 0.375; (Pt): Ag 0.189, Pt 0.811_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 10 |  |
| Phase composition |  | 1050 | L + (Ag); _L: Ag 0.94, Pt 0.06; (Ag): Ag 0.885, Pt 0.115_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 3 |  |
| Phase composition |  | 1100 | (Ag) + (Pt); _(Ag): Ag 0.614, Pt 0.386; (Pt): Ag 0.2, Pt 0.8_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 9 |  |
| Phase composition |  | 1100 | L + (Ag); _L: Ag 0.888, Pt 0.112; (Ag): Ag 0.806, Pt 0.194_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 4 |  |
| Phase composition |  | 1150 | (Ag) + (Pt); _(Ag): Ag 0.603, Pt 0.397; (Pt): Ag 0.212, Pt 0.788_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 8 |  |
| Phase composition |  | 1150 | L + (Ag); _L: Ag 0.833, Pt 0.167; (Ag): Ag 0.706, Pt 0.294_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 5 |  |
| Phase composition |  | 1186 | (Ag) + (Pt); _(Ag): Ag 0.594, Pt 0.406; (Pt): Ag 0.221, Pt 0.779_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 7 |  |
| Phase composition |  | 1186 | L + (Ag); _L: Ag 0.799, Pt 0.201; (Ag): Ag 0.594, Pt 0.406_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 6 |  |
| Phase composition |  | 1186 | L + (Pt); _L: Ag 0.799, Pt 0.201; (Pt): Ag 0.221, Pt 0.779_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 14 |  |
| Phase composition |  | 1200 | L + (Pt); _L: Ag 0.793, Pt 0.207; (Pt): Ag 0.208, Pt 0.792_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 15 |  |
| Phase composition |  | 1250 | L + (Pt); _L: Ag 0.772, Pt 0.228; (Pt): Ag 0.178, Pt 0.822_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 16 |  |
| Phase composition |  | 1263.15 | liquid + L; _liquid: Ag 0.98, Pt 0.02; L: Ag 0.98, Pt 0.02_ | experimental | [1] Karakaya 1987; _cites Heycock 1907_ | Table 2, p. 3, row 2 |  |
| Phase composition |  | 1263.15 | liquid + L; _liquid: Ag 0.986, Pt 0.014; L: Ag 0.986, Pt 0.014_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 1 |  |
| Phase composition |  | 1300 | L + (Pt); _L: Ag 0.748, Pt 0.252; (Pt): Ag 0.159, Pt 0.841_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 17 |  |
| Phase composition |  | 1318.15 | liquid + L; _liquid: Ag 0.944, Pt 0.056; L: Ag 0.944, Pt 0.056_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 3 |  |
| Phase composition |  | 1318.15 | liquid + L; _liquid: Ag 0.942, Pt 0.058; L: Ag 0.942, Pt 0.058_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 4 |  |
| Phase composition |  | 1350 | L + (Pt); _L: Ag 0.721, Pt 0.279; (Pt): Ag 0.145, Pt 0.855_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 18 |  |
| Phase composition |  | 1393.15 | liquid + L; _liquid: Ag 0.867, Pt 0.133; L: Ag 0.867, Pt 0.133_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 5 |  |
| Phase composition |  | 1393.15 | liquid + L; _liquid: Ag 0.878, Pt 0.122; L: Ag 0.878, Pt 0.122_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 6 |  |
| Phase composition |  | 1400 | L + (Pt); _L: Ag 0.69, Pt 0.31; (Pt): Ag 0.132, Pt 0.868_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 19 |  |
| Phase composition |  | 1450 | L + (Pt); _L: Ag 0.652, Pt 0.348; (Pt): Ag 0.122, Pt 0.878_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 20 |  |
| Phase composition |  | 1454.15 | liquid + L; _liquid: Ag 0.803, Pt 0.197; L: Ag 0.803, Pt 0.197_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 7 |  |
| Phase composition |  | 1454.15 | liquid + L; _liquid: Ag 0.808, Pt 0.192; L: Ag 0.808, Pt 0.192_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 8 |  |
| Phase composition |  | 1500 | L + (Pt); _L: Ag 0.601, Pt 0.399; (Pt): Ag 0.112, Pt 0.888_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 21 |  |
| Phase composition |  | 1550 | L + (Pt); _L: Ag 0.508, Pt 0.492; (Pt): Ag 0.102, Pt 0.898_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 22 |  |
| Phase composition |  | 1600 | L + (Pt); _L: Ag 0.265, Pt 0.735; (Pt): Ag 0.086, Pt 0.914_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 23 |  |
| Phase composition |  | 1650 | L + (Pt); _L: Ag 0.157, Pt 0.843; (Pt): Ag 0.062, Pt 0.938_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 24 |  |
| Phase composition |  | 1700 | L + (Pt); _L: Ag 0.083, Pt 0.917; (Pt): Ag 0.036, Pt 0.964_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 25 |  |
| Phase composition |  | 1736.15 | liquid + L; _liquid: Ag 0.64, Pt 0.36; L: Ag 0.64, Pt 0.36_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 9 |  |
| Phase composition |  | 1736.15 | liquid + L; _liquid: Ag 0.643, Pt 0.357; L: Ag 0.643, Pt 0.357_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 10 |  |
| Phase composition |  | 1750 | L + (Pt); _L: Ag 0.019, Pt 0.981; (Pt): Ag 0.008, Pt 0.992_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 26 |  |
| Phase composition |  | 1769 | L + (Pt); _L: Ag 0, Pt 1; (Pt): Ag 0, Pt 1_ | model | [1] Karakaya 1987 | Table 6, p. 7, row 27 |  |
| Phase composition |  | 1808.15 | liquid + L; _liquid: Ag 0.545, Pt 0.455; L: Ag 0.545, Pt 0.455_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 11 |  |
| Phase composition |  | 1808.15 | liquid + L; _liquid: Ag 0.545, Pt 0.455; L: Ag 0.545, Pt 0.455_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 12 |  |
| Phase composition |  | 1832.15 | liquid + L; _liquid: Ag 0.435, Pt 0.565; L: Ag 0.435, Pt 0.565_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 14 |  |
| Phase composition |  | 1832.15 | liquid + L; _liquid: Ag 0.475, Pt 0.525; L: Ag 0.475, Pt 0.525_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 13 |  |
| Phase composition |  | 1861.15 | liquid + L; _liquid: Ag 0.31, Pt 0.69; L: Ag 0.31, Pt 0.69_ | experimental | [1] Karakaya 1987; _cites ref. 07Doe_ | Table 2, p. 3, row 16 |  |
| Phase composition |  | 1861.15 | liquid + L; _liquid: Ag 0.306, Pt 0.694; L: Ag 0.306, Pt 0.694_ | model | [1] Karakaya 1987 | Table 2, p. 3, row 15 |  |

### Crystal structure (24)

Table: Crystal structure, Ag–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.40861 nm | 298.15 | (Ag); _(Ag): Ag 1, Pt 0_ | experimental | [1] Karakaya 1987; _cites ref. 1_ | Table 4, p. 4, row 1 |  |
| Lattice a | 0.389 nm | 298.15 | γ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 12 |  |
| Lattice a | 0.4061 nm | 1023.15 | (Ag); _(Ag): Ag 0.93, Pt 0.07_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 4 |  |
| Lattice a | 0.4068 nm | 1073.15 | (Ag); _(Ag): Ag 0.972, Pt 0.028_ | experimental | [1] Karakaya 1987; _cites Novikova 1987_ | Table 4, p. 4, row 2 |  |
| Lattice a | 0.3895 nm | 1073.15 | α″; _α″: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 11 |  |
| Lattice a | 0.391 nm | 1093.15 | α′; _α′: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 10 |  |
| Lattice a | 0.4067 nm | 1173.15 | (Ag); _(Ag): Ag 0.946, Pt 0.054_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 3 |  |
| Lattice a | 0.3932 nm | 1403.15 | (Pt); _(Pt): Ag 0.2, Pt 0.8_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 5 |  |
| Lattice a | 0.3921 nm | 1403.15 | (Pt); _(Pt): Ag 0.08, Pt 0.92_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 7 |  |
| Lattice a | 0.3913 nm | 1403.15 | (Pt); _(Pt): Ag 0, Pt 1_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 9 |  |
| Lattice a | 0.3917 nm | 1403.15 | (Pt); _(Pt): Ag 0.06, Pt 0.94_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 8 |  |
| Lattice a | 0.3928 nm | 1403.15 | (Pt); _(Pt): Ag 0.14, Pt 0.86_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 6 |  |
| lattice unspecified axis | 0.40861 nm | 298.15 | (Ag); _(Ag): Ag 1, Pt 0_ | experimental | [1] Karakaya 1987; _cites ref. 1_ | Table 4, p. 4, row 1 |  |
| lattice unspecified axis | 0.389 nm | 298.15 | γ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 12 |  |
| lattice unspecified axis | 0.4061 nm | 1023.15 | (Ag); _(Ag): Ag 0.93, Pt 0.07_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 4 |  |
| lattice unspecified axis | 0.4068 nm | 1073.15 | (Ag); _(Ag): Ag 0.972, Pt 0.028_ | experimental | [1] Karakaya 1987; _cites Novikova 1987_ | Table 4, p. 4, row 2 |  |
| lattice unspecified axis | 0.3895 nm | 1073.15 | α″; _α″: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 11 |  |
| lattice unspecified axis | 0.391 nm | 1093.15 | α′; _α′: Ag 0.75, Pt 0.25_ | experimental | [1] Karakaya 1987; _cites ref. 2_ | Table 4, p. 4, row 10 |  |
| lattice unspecified axis | 0.4067 nm | 1173.15 | (Ag); _(Ag): Ag 0.946, Pt 0.054_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 3 |  |
| lattice unspecified axis | 0.3932 nm | 1403.15 | (Pt); _(Pt): Ag 0.2, Pt 0.8_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 5 |  |
| lattice unspecified axis | 0.3921 nm | 1403.15 | (Pt); _(Pt): Ag 0.08, Pt 0.92_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 7 |  |
| lattice unspecified axis | 0.3913 nm | 1403.15 | (Pt); _(Pt): Ag 0, Pt 1_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 9 |  |
| lattice unspecified axis | 0.3917 nm | 1403.15 | (Pt); _(Pt): Ag 0.06, Pt 0.94_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 8 |  |
| lattice unspecified axis | 0.3928 nm | 1403.15 | (Pt); _(Pt): Ag 0.14, Pt 0.86_ | experimental | [1] Karakaya 1987; _cites ref. 43Sch_ | Table 4, p. 4, row 6 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Karakaya, W. T. Thompson, The Ag-Pt (Silver-Platinum) system, Bulletin of Alloy Phase Diagrams 8, 334-340 (1987). [doi:10.1007/bf02869269](https://doi.org/10.1007/bf02869269)

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
