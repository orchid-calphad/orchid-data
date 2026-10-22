# Hf–W system

> Hf–W system: 17 accepted literature values (crystal structure 14, invariant reaction 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-W.html · Markdown: https://data.orchid-project.org/systems/HF-W.md

17 accepted literature values from 1 paper(s) (experimental 7, model 5, DFT 5); 2 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-W.json) · [CSV](https://data.orchid-project.org/systems/HF-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-W/HfW-02Sha-LB.json) · [Markdown](https://data.orchid-project.org/systems/HF-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 5 |
| DFT | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| crystal structure | 14 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfW-02Sha-LB.tdb | G. Shao, Intermetallics, 10, 429-34(2002). [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) | `078db40d3d1acdff57b462f15eac22fc75242db8dadb9a6a27c002a3104918d9` | [viewer](https://orchid-project.org/phase-diagrams/#HF-W/HfW-02Sha-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfW-02Sha-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfW-02Sha-LB.json) |
| HfW-12Lie.tdb | A.C. Lieser, C.L. Zacherl, A. Saengdeejing, Z.-K. Liu, L.J. Kecskes, Calphad, 38, 92-99(2012). [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005) | `8ac53fc523b760014d23a34f80e81c70ad549946918cba3eee6db63198df4f78` | [viewer](https://orchid-project.org/phase-diagrams/#HF-W/HfW-12Lie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfW-12Lie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfW-12Lie.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfW-02Sha-LB.tdb | 2771.05 | LIQUID (x(W) 0.52741) + C15_LAVES (x(W) 0.6662) + BCC_A2 (x(W) 0.8924) |
| HfW-02Sha-LB.tdb | 2213.68 | BCC_A2 (x(W) 0.13032) + LIQUID (x(W) 0.21697) + C15_LAVES (x(W) 0.64708) |
| HfW-02Sha-LB.tdb | 1718.04 | HCP_A3 (x(W) 0.01514) + BCC_A2 (x(W) 0.07512) + C15_LAVES (x(W) 0.64626) |
| HfW-12Lie.tdb | 2806.23 | LIQUID (x(W) 0.56433) + C15_LAVES (x(W) 0.66291) + BCC_A2 (x(W) 0.92394) |
| HfW-12Lie.tdb | 2222.06 | BCC_A2 (x(W) 0.12949) + LIQUID (x(W) 0.20418) + C15_LAVES (x(W) 0.65502) |
| HfW-12Lie.tdb | 1826.4 | HCP_A3 (x(W) 3.500e-4) + BCC_A2 (x(W) 0.04381) + C15_LAVES (x(W) 0.65916) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-W.json) · [CALPHAD hull HfW-02Sha-LB](https://data.orchid-project.org/hulls/calphad-sgte/HF/HF-W--HfW-02Sha-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hf–W system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2785 | peritectic |  | experimental | [1] Lieser 2012; _cites Rudy 1969_ | p. 1 | “The Laves phase forms peritectically at 2785 K \[6\].” |
| 2222 | eutectic |  | model | [1] Lieser 2012 | p. 6 | “A subregular solution model is necessary to reproduce the eutectic reaction at 2222 K and 20.42 at% W.” |
| 2222 | eutectic |  | experimental | [1] Lieser 2012; _cites Ackerman 1972_ | p. 2 | “The eutectic reaction happens at 2222 K and 18 at% W \[8\], and the eutectoid occurs at 7-8 at% W with a disagreement of 90 K about the reaction temperature \[6-7\].” |

## Other properties

### Crystal structure (14)

Table: Crystal structure, Hf–W system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 3.537 Å |  | Hf (bcc); _alloy: W 0_ | DFT | [1] Lieser 2012 | Table 1, p. 4, row 1 |  |
| Lattice a | 3.538 Å |  | Hf (bcc); _alloy: W 0_ | model | [1] Lieser 2012; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.calphad.2004.05.002) | Table 1, p. 4, row 3 |  |
| Lattice a | 3.2 Å |  | Hf (hcp); _alloy: W 0_ | model | [1] Lieser 2012; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.calphad.2004.05.002) | Table 1, p. 4, row 6 |  |
| Lattice a | 3.2 Å |  | Hf (hcp); _alloy: W 0_ | DFT | [1] Lieser 2012 | Table 1, p. 4, row 4 |  |
| Lattice a | 7.617 Å |  | HfW2; _alloy: W 0.666667_ | DFT | [1] Lieser 2012 | Table 1, p. 4, row 10 |  |
| Lattice a | 3.185 Å |  | W; _alloy: W 1_ | DFT | [1] Lieser 2012 | Table 1, p. 4, row 7 |  |
| Lattice a | 3.19 Å |  | W; _alloy: W 1_ | model | [1] Lieser 2012; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.calphad.2004.05.002) | Table 1, p. 4, row 9 |  |
| Lattice a | 3.5 Å | 298.15 | Hf (bcc); _alloy: W 0_ | experimental | [1] Lieser 2012; _cites Duwez 1951_ [doi](https://doi.org/10.1063/1.1700127) | Table 1, p. 4, row 2 |  |
| Lattice a | 3.1952 Å | 298.15 | Hf (hcp); _alloy: W 0_ | experimental | [1] Lieser 2012; _cites Duwez 1951_ [doi](https://doi.org/10.1063/1.1700127) | Table 1, p. 4, row 5 |  |
| Lattice a | 7.593 Å | 298.15 | HfW2; _alloy: W 0.666667_ | experimental | [1] Lieser 2012; _cites Braun 1960_ | Table 1, p. 4, row 11 |  |
| Lattice a | 3.166 Å | 298.15 | W; _alloy: W 1_ | experimental | [1] Lieser 2012; _cites Braun 1960_ | Table 1, p. 4, row 8 |  |
| lattice c a | 1.58 not_printed |  | Hf (hcp); _alloy: W 0_ | model | [1] Lieser 2012; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.calphad.2004.05.002) | Table 1, p. 4, row 6 |  |
| lattice c a | 1.58 not_printed |  | Hf (hcp); _alloy: W 0_ | DFT | [1] Lieser 2012 | Table 1, p. 4, row 4 |  |
| lattice c a | 1.5827 not_printed | 298.15 | Hf (hcp); _alloy: W 0_ | experimental | [1] Lieser 2012; _cites Duwez 1951_ [doi](https://doi.org/10.1063/1.1700127) | Table 1, p. 4, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Alyson C. Lieser, Chelsey L. Zacherl, Arkapol Saengdeejing, Zi-Kui Liu, Laszlo J. Kecskes, First-principles calculations and thermodynamic re-modeling of the Hf–W system, Calphad 38, 92-99 (2012). [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
