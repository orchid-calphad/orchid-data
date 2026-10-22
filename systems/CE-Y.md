# Ce–Y system

> Ce–Y system: 14 accepted literature values (invariant reaction 14) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-Y.html · Markdown: https://data.orchid-project.org/systems/CE-Y.md

14 accepted literature values from 2 paper(s) (experimental 8, model 5, unspecified 1); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-Y.json) · [CSV](https://data.orchid-project.org/systems/CE-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-Y/CeY-06Men.json) · [Markdown](https://data.orchid-project.org/systems/CE-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 5 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeY-06Men.tdb | F.G. Meng, L.B. Liu, H.S. Liu, Z.P. Jin, Calphad, 30, 323-25(2006). [doi:10.1016/j.calphad.2006.02.002](https://doi.org/10.1016/j.calphad.2006.02.002) | `1ae8c2335e970ff1b7c70ba6ae4540bdd4e12dc61c195e1a8b309d26e446c90e` | [viewer](https://orchid-project.org/phase-diagrams/#CE-Y/CeY-06Men.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeY-06Men.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeY-06Men.json) |
| CeY-08Dju.tdb | D. Djurovic, M. Zinkevich, F. Aldinger, Solid State Ionics, 179, 1902-11(2008). [doi:10.1016/j.ssi.2008.06.011](https://doi.org/10.1016/j.ssi.2008.06.011) | `dec06e9f8d832c2240cd684e45787948da7a668c9a915d0c5fc23473b32ca544` | [viewer](https://orchid-project.org/phase-diagrams/#CE-Y/CeY-08Dju.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeY-08Dju.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeY-08Dju.json) |
| CeY-08Guo.tdb | C. Guo, Z. Du, C. Li, Int. J. Mater. Res., 99, 650-68(2008). [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) | `6052d6790f767fada26e701d3c4015f202f29a4013b1cde4443f031aeb318641` | [viewer](https://orchid-project.org/phase-diagrams/#CE-Y/CeY-08Guo.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeY-08Guo.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeY-08Guo.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeY-06Men.tdb | 1055.23 | BCC_A2 (x(Y) 0.3102) + DHCP (x(Y) 0.40402) + HCP_A3 (x(Y) 0.70099) |
| CeY-06Men.tdb | 967.32 | FCC_A1 (x(Y) 0.12683) + BCC_A2 (x(Y) 0.16072) + DHCP (x(Y) 0.28371) |
| CeY-08Dju.tdb | 1046.19 | BCC_A2 (x(Y) 0.28516) + DHCP (x(Y) 0.42157) + HCP_A3 (x(Y) 0.65299) |
| CeY-08Dju.tdb | 954.4 | FCC_A1 (x(Y) 0.08025) + BCC_A2 (x(Y) 0.09732) + DHCP (x(Y) 0.30659) |
| CeY-08Guo.tdb | 1053.2 | BCC_A2 (x(Y) 0.35998) + DHCP (x(Y) 0.39546) + HCP_A3 (x(Y) 0.6283) |
| CeY-08Guo.tdb | 970.83 | FCC_A1 (x(Y) 0.12587) + BCC_A2 (x(Y) 0.14204) + DHCP (x(Y) 0.24772) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-Y.json) · [CALPHAD hull CeY-06Men](https://data.orchid-project.org/hulls/calphad-sgte/CE/CE-Y--CeY-06Men.json) · [CALPHAD hull CeY-08Guo](https://data.orchid-project.org/hulls/calphad-sgte/CE/CE-Y--CeY-08Guo.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–Y system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1055 | bcc_a2 + hcp -> dhcp | bcc_a2: Y 0.31; hcp: Y 0.701; dhcp: Y 0.404 | model | [1] Meng 2006 | Table 2, p. 3, row 1 |  |
| 1053 | Peritectoid: bcc+hcp->dhcp |  | experimental | [2] DJUROVIC 2008; _cites Flandorfer 1997_ [doi](https://doi.org/10.1007/s11661-997-0129-z) | Table 5, p. 8, row 2 |  |
| 1053 (none) | peritectic: bcc + hcp → dhcp |  | experimental | [1] Meng 2006 | p. 2 | “Additionally they proposed the occurrence of a peritectic reaction, bcc + hcp → dhcp, at about 1053 K.” |
| 1053 | bcc_a2 + hcp -> dhcp |  | experimental | [1] Meng 2006; _cites Flandorfer 1997_ [doi](https://doi.org/10.1007/s11661-997-0129-z) | Table 2, p. 3, row 2 |  |
| 1040 | Peritectoid: bcc+hcp->dhcp | bcc: Y 0.279; hcp: Y 0.65; dhcp: Y 0.433 | model | [2] DJUROVIC 2008 | Table 5, p. 8, row 1 |  |
| 978 | Eutectoid: bcc->fcc+dhcp | bcc: Y 0.1 | experimental | [2] DJUROVIC 2008; _cites Flandorfer 1997_ [doi](https://doi.org/10.1007/s11661-997-0129-z) | Table 5, p. 8, row 4 |  |
| 978 (none) | eutectic |  | experimental | [1] Meng 2006; _cites Flandorfer 1997_ [doi](https://doi.org/10.1007/s11661-997-0129-z) | p. 2 | “They determined the location of the eutectic decomposition of the bcc phase at about 978 K and 10 at.% Y, which compares well with the data shown in Fig. 1.” |
| 978 | bcc_a2 -> fcc_a1 + dhcp | bcc_a2: Y 0.1 | experimental | [1] Meng 2006; _cites Flandorfer 1997_ [doi](https://doi.org/10.1007/s11661-997-0129-z) | Table 2, p. 3, row 4 |  |
| 973 | bcc_a2 -> fcc_a1 + dhcp |  | experimental | [1] Meng 2006; _cites Gschneidner 1982_ [doi](https://doi.org/10.1007/bf02892383) | Table 2, p. 3, row 5 |  |
| 973 | Eutectoid: bcc->fcc+dhcp |  | unspecified | [2] DJUROVIC 2008; _cites Gschneidner 1982_ [doi](https://doi.org/10.1007/bf02892383) | Table 5, p. 8, row 5 |  |
| 973 | eutectoid: bcc → fcc + dhcp |  | experimental | [1] Meng 2006; _cites Gschneidner 1982_ [doi](https://doi.org/10.1007/bf02892383) | p. 1 | “It was believed that there are five solution phases, liquid, bcc, hcp, fcc and dhcp, in the Ce-Y binary system, and the bcc phase transforms into the fcc phase and the dhcp phase at 973 K by the eutectoid reaction, bcc → fcc + dhcp \[3\].” |
| 967 | eutectoid |  | model | [1] Meng 2006 | p. 3 | “The calculated results show that the eutectoid decomposition of the bcc phase occurs at 967 K and 16.1 at.% Y.” |
| 967 | bcc_a2 -> fcc_a1 + dhcp | bcc_a2: Y 0.161; fcc_a1: Y 0.127; dhcp: Y 0.283 | model | [1] Meng 2006 | Table 2, p. 3, row 3 |  |
| 953 | Eutectoid: bcc->fcc+dhcp | bcc: Y 0.107; fcc: Y 0.089; dhcp: Y 0.339 | model | [2] DJUROVIC 2008 | Table 5, p. 8, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. F.G. Meng, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ce–Y system, Calphad 30, 323-325 (2006). [doi:10.1016/j.calphad.2006.02.002](https://doi.org/10.1016/j.calphad.2006.02.002)
2. D DJUROVIC, M ZINKEVICH, F ALDINGER, Thermodynamic modeling of the cerium–yttrium–oxygen system, Solid State Ionics 179, 1902-1911 (2008). [doi:10.1016/j.ssi.2008.06.011](https://doi.org/10.1016/j.ssi.2008.06.011)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
