# Ti–W system

> Ti–W system: 14 accepted literature values (invariant reaction 9, phase transition 5) and 4 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TI-W.html · Markdown: https://data.orchid-project.org/systems/TI-W.md

14 accepted literature values from 2 paper(s) (experimental 8, model 6); 4 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/TI-W.json) · [CSV](https://data.orchid-project.org/systems/TI-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#TI-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#TI-W/TiW-93Jin.json) · [Markdown](https://data.orchid-project.org/systems/TI-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |
| phase transition | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| TiW-93Jin.tdb | Z. Jin, C. Qiu, Mater. Sci. Technol., 9, 378-83(1993). [doi:10.1179/mst.1993.9.5.378](https://doi.org/10.1179/mst.1993.9.5.378) | `95099e4555c37256bf55761f3b77cd43b393e1389a58ca6eb28f7050c98fd7b8` | [viewer](https://orchid-project.org/phase-diagrams/#TI-W/TiW-93Jin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/TiW-93Jin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/TiW-93Jin.json) |
| TiW-93Jon.tdb | S. Jonsson, TRITA-MAC 518, KTH Stockholm, 1993. | `b6e1ce9b615db11c30a6827bfbf89b5bd84ec05270b73d668b7f55c02e9dba06` | [viewer](https://orchid-project.org/phase-diagrams/#TI-W/TiW-93Jon.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/TiW-93Jon.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/TiW-93Jon.json) |
| TiW-96Jon-LB.tdb | S. Jonsson, Z. Metallkd., 87, 784-87(1996). [doi:10.1515/ijmr-1996-871008](https://doi.org/10.1515/ijmr-1996-871008) | `be3e187f7db1011473e5e102681c012bbe29ed45c61bc1bec681032cbdd7b838` | [viewer](https://orchid-project.org/phase-diagrams/#TI-W/TiW-96Jon-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/TiW-96Jon-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/TiW-96Jon-LB.json) |
| TiW-98Sau.tdb | N. Saunders, COST 507, Final report round 2, 1998. | `36471f2901b23e3cefb92e30cefeb1f4fcae95bae44b56af32f3f3508c8a988b` | [viewer](https://orchid-project.org/phase-diagrams/#TI-W/TiW-98Sau.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/TiW-98Sau.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/TiW-98Sau.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| TiW-93Jin.tdb | 1012.92 | HCP_A3 (x(W) 0.00201) + BCC_A2#2 (x(W) 0.08754) + BCC_A2 (x(W) 0.64029) |
| TiW-93Jon.tdb | 993.77 | HCP_A3 (x(W) 0.0023) + BCC_A2#2 (x(W) 0.10077) + BCC_A2 (x(W) 0.57042) |
| TiW-96Jon-LB.tdb | 1017.76 | HCP_A3 (x(W) 0.00208) + BCC_A2#2 (x(W) 0.09656) + BCC_A2 (x(W) 0.64757) |
| TiW-98Sau.tdb | 1019.53 | HCP_A3 (x(W) 0.00189) + BCC_A2#2 (x(W) 0.09449) + BCC_A2 (x(W) 0.64547) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/TI/TI-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/TI/TI-W.json) · [CALPHAD hull TiW-93Jin](https://data.orchid-project.org/hulls/calphad-sgte/TI/TI-W--TiW-93Jin.json) · [CALPHAD hull TiW-93Jon](https://data.orchid-project.org/hulls/calphad-sgte/TI/TI-W--TiW-93Jon.json) · [CALPHAD hull TiW-96Jon-LB](https://data.orchid-project.org/hulls/calphad-sgte/TI/TI-W--TiW-96Jon-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ti–W system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1033.15 | monotectoid: bcc -> hcp -> bcc |  | experimental | [1] Jin 1993; _cites s 1971_ | Table 2, p. 6, row 4 |  |
| 1030.15 | monotectoid: bcc -> hcp -> bcc | bcc: W 0.76; hcp: W 0.009 | model | [1] Jin 1993; _cites KAUFMAN 1975_ | Table 2, p. 6, row 6 |  |
| 1019.5 | Monotectoid: hcp-A3 bcc-A2' -> bcc-A2" | hcp-A3: W 0.002; bcc-A2': W 0.645; bcc-A2": W 0.095 | model | [2] Hämäläinen 1998 | Table I, p. 318, row 1 |  |
| 1013.15 | monotectoid: bcc -> hcp -> bcc | bcc: W 0.6403; hcp: W 0.002 | model | [1] Jin 1993 | Table 2, p. 6, row 12 |  |
| 1010.15 | monotectoid: bcc -> hcp -> bcc | bcc: W 0.72; hcp: W 0.002 | model | [1] Jin 1993; _cites MURRAY 1981_ | Table 2, p. 6, row 8 |  |
| 1008.15 | monotectoid: bcc -> hcp -> bcc | bcc: W 0.723; hcp: W 7.000e-4 | model | [1] Jin 1993; _cites s 1985_ | Table 2, p. 6, row 10 |  |
| 1008.15 | monotectoid: bcc -> hcp -> bcc | bcc: W 0.087 | experimental | [1] Jin 1993; _cites IMGRAM 1961_ | Table 2, p. 6, row 3 |  |
| 998.15 | monotectoid: bcc -> hcp -> bcc | bcc: W 0.09 | experimental | [1] Jin 1993; _cites Yu 1958_ | Table 2, p. 6, row 2 |  |
| 988.15 | monotectoid: bcc -> hcp -> bcc | bcc: W 0.09; hcp: W 0.002 | experimental | [1] Jin 1993; _cites MAYKUTH 1953_ | Table 2, p. 6, row 1 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Ti–W system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 988.15 K | 988.15 | other | experimental | [1] Jin 1993; _cites MAYKUTH 1953_ | p. 4 | “Maykuth et ai.3 reported that the maximum solubility is about 0·20/0 W at the monotectoid temperature (about 715°C).” |
| Phase transition | 1008.15 K | 1008.15 | other | experimental | [1] Jin 1993; _cites DOUGLASS 1960_ | p. 3 | “However, based on metallographic observation from a previous work,20 Imgram et at.21 suggested an approximately straight boundary between the bcc ~ hcp transformation of pure Ti (882°C) and the monotectoid (about 8'70/0W at 735°C).” |
| Phase transition | 1013.15 K | 1013.15 | monotectoid | model | [1] Jin 1993 | p. 6 | “The calculated monotectoid temperature (740°C) and composition (8'750/0W) are close to the results reported by Imgram et al.21” |
| Phase transition | 1155.15 K | 1155.15 |  | experimental | [1] Jin 1993; _cites DOUGLASS 1960_ | p. 3 | “However, based on metallographic observation from a previous work,20 Imgram et at.21 suggested an approximately straight boundary between the bcc ~ hcp transformation of pure Ti (882°C) and the monotectoid (about 8'70/0W at 735°C).” |
| Phase transition | 1523.15 K | 1523.15 | other | experimental | [1] Jin 1993; _cites RUDY 1968_ | p. 2 | “However, Rudy and Windisch4 found that a single solid solution phase was formed at temperatures above 1300°C and, thus, suggested that the critical temperature of the miscibility gap is about 1250°C, above which bcc exhibits complete mutual solid solubility.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zhan-peng Jin, Caian Qiu, Thermodynamic evaluation of Ti–W system, Materials Science and Technology 9, 378-383 (1993). [doi:10.1179/mst.1993.9.5.378](https://doi.org/10.1179/mst.1993.9.5.378)
2. M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998). [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
