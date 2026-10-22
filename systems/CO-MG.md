# Co–Mg system

> Co–Mg system: 18 accepted literature values (invariant reaction 12, phase equilibrium 5, formation 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-MG.html · Markdown: https://data.orchid-project.org/systems/CO-MG.md

18 accepted literature values from 2 paper(s) (experimental 14, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-MG.json) · [CSV](https://data.orchid-project.org/systems/CO-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-MG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-MG/CoMg-22Yan.json) · [Markdown](https://data.orchid-project.org/systems/CO-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase equilibrium | 5 |
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoMg-22Yan.tdb | L.-F. Yang, X.-D. Si, H.-Q. Zhang, F.-Y. Gao, Y.-P. Zheng, Y.-L. Liu, Y.-R. Wang, Y. Du, J. Min. Metall. B, 58, 109-15(2022). [doi:10.2298/JMMB210606051Y](https://doi.org/10.2298/JMMB210606051Y) | `edaa24ff0861bcf5be4019caf839f602c299f43fa30a18bd3d37c0d0523c0974` | [viewer](https://orchid-project.org/phase-diagrams/#CO-MG/CoMg-22Yan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoMg-22Yan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoMg-22Yan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoMg-22Yan.tdb | 1242.77 | FCC_A1 (x(Mg) 0.00272) + CO2MG_C14 (x(Mg) 0.33333) + LIQUID (x(Mg) 0.72271) |
| CoMg-22Yan.tdb | 1242.77 | FCC_A1 (x(Mg) 0.00272) + CO2MG_C14 (x(Mg) 0.33333) + LIQUID (x(Mg) 0.7225) |
| CoMg-22Yan.tdb | 909.23 | CO2MG_C14 (x(Mg) 0.33333) + LIQUID (x(Mg) 0.98193) + HCP_A3 (x(Mg) 0.99928) |
| CoMg-22Yan.tdb | 909.23 | CO2MG_C14 (x(Mg) 0.33333) + LIQUID (x(Mg) 0.98198) + HCP_A3 (x(Mg) 0.99928) |
| CoMg-22Yan.tdb | 695.06 | FCC_A1 (x(Mg) 1.000e-5) + HCP_A3 (x(Mg) 2.000e-5) + CO2MG_C14 (x(Mg) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-MG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Co–Mg system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1243.15 | peritectic: Liquid + (aCo) « MgCo2 |  | experimental | [1] Yang 2022; _cites Smith 1964_ | p. 1 | “Smith and Smith \[13\] also studied the peritectic reaction Liquid + (aCo) « MgCo2 by analyzing the heating and cooling curves of alloys with the compositions from 9 to 82.6 at.% Co and the peritectic temperature was determined to be 1243.15 K.” |
| 1243.15 | peritectic |  | experimental | [2] Sheldon 1987; _cites ref. 64Smi_ | p. 6 | “\[47Cra\] predicted, from i n s u f f i c i e n t t h e r m a l and X-ray analysis, the existence of a Mg2Co compound, formed by a peritectic reaction in the neighborhood of 689 ~ \[64Smi\], from t h e i r diffusion couple, t h e r m a l , metallographic, and X-ray a n a l y s e s , could not confirm the existence of the Mg2Co compound and its corresponding peritectic reaction at 689 ~ \[64Smi\] confir…” |
| 1243.15 | L + (αCo) -> MgCo2 | MgCo2: Mg 0.333333 | experimental | [1] Yang 2022; _cites Smith 1964_ | Table 3, p. 4, row 4 |  |
| 1243.01 | L + (αCo) -> MgCo2 | MgCo2: Mg 0.333333 | model | [1] Yang 2022 | Table 3, p. 4, row 5 |  |
| 908.15 | eutectic |  | model | [1] Yang 2022; _cites Smith 1964_ | p. 1 | “In the assessed Co-Mg binary phase diagram reported by Smith and Smith \[13\], which is shown in Fig. 1, the eutectic point was placed at 1.91 at.% Co and 908.15 K.” |
| 908.15 | L -> (Mg) + MgCo2 | MgCo2: Mg 0.333333 | experimental | [1] Yang 2022; _cites Wetherill 1935_ | Table 3, p. 4, row 1 |  |
| 908.15 | eutectic |  | experimental | [1] Yang 2022; _cites Smith 1964_ | p. 1 | “Besides, Smith and Smith \[13\] reported that the eutectic reaction temperature was 908.15 K, which agreed well with that reported by Wetherill \[10\] and Cramer et al. \[11\].” |
| 908.15 | eutectic: Liquid « (Mg) + MgCo2 |  | experimental | [1] Yang 2022; _cites Wetherill 1935_ | p. 1 | “According to the experimental results from Wetherill \[10\], the eutectic reaction of Liquid « (Mg) + MgCo2 was determined to occur at 908.15 K with the eutectic composition of 2.12 at.% Co by using thermal analysis.” |
| 908.15 | eutectic |  | model | [1] Yang 2022; _cites Nayeb-Hashemi 1987_ [doi](https://doi.org/10.1007/bf02869272) | p. 1 | “Nayeb-Hashemi and Clark \[15\] critically assessed the works of Wetherill \[10\], Cramer et al. \[11\], Raynor \[12\], and Smith and Smith \[13\]. They placed the eutectic point at 1.91 at% Co and 908.15 K, which was reliable and was considered in the present optimization.” |
| 908.07 | L -> (Mg) + MgCo2 | MgCo2: Mg 0.333333 | model | [1] Yang 2022 | Table 3, p. 4, row 3 |  |
| 906.15 | L -> (Mg) + MgCo2 | MgCo2: Mg 0.333333 | experimental | [1] Yang 2022; _cites Cramer 1947_ | Table 3, p. 4, row 2 |  |
| 905.15 | eutectic |  | experimental | [1] Yang 2022; _cites Cramer 1947_ | p. 1 | “Cramer et al. \[11\] also studied this eutectic reaction by means of thermal analysis and this eutectic point was placed at 1.91 at.% Co and 905.15 K, which is close to the eutectic point reported by Wetherill \[10\].” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Co–Mg system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -8 kJ/mol-atom | 800 | experimental |  |  | [1] Yang 2022; _cites Hultgren 1973_ | p. 2 | “According to Hultgren et al. \[25\], the enthalpy of formation of MgCo2 was determined to be -8 kJ/mole·atoms at 800 K by vapor-pressure measurement.” |

## Other properties

### Phase equilibrium (5)

Table: Phase equilibrium, Co–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 911.35 | other; _liquid: Co 0.0165, Mg 0.9835_ | experimental | [2] Sheldon 1987; _cites ref. 35Wet_ | Table 1, p. 6, row 13 |  |
| Phase composition |  | 911.65 | other; _liquid: Co 0.0199, Mg 0.9801_ | experimental | [2] Sheldon 1987; _cites ref. 35Wet_ | Table 1, p. 6, row 14 |  |
| Phase composition |  | 916.95 | other; _liquid: Co 0.0077, Mg 0.9923_ | experimental | [2] Sheldon 1987; _cites ref. 35Wet_ | Table 1, p. 6, row 12 |  |
| Phase composition |  | 920.15 | other; _liquid: Co 0.0042, Mg 0.9958_ | experimental | [2] Sheldon 1987; _cites ref. 47Cra_ | Table 1, p. 6, row 15 |  |
| Phase composition |  | 923.65 | other; _liquid: Co 0.0013, Mg 0.9987_ | experimental | [2] Sheldon 1987; _cites ref. 35Wet_ | Table 1, p. 6, row 11 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. L.-F. Yang, X-D. Si, H.-D. Zhang, F.-G. Gao, Y.-P. Zeng, Y.-L. Liu et al., Thermodynamic assessment of the Co-Mg binary system, J min metall B Metall 58, 109-115 (2022). [doi:10.2298/jmmb210606051y](https://doi.org/10.2298/jmmb210606051y)
2. R. I. Sheldon, E. M. Foltyn, D. E. Peterson, The Sn-U (Tin-Uranium) system, Bulletin of Alloy Phase Diagrams 8, 347-352 (1987). [doi:10.1007/bf02869271](https://doi.org/10.1007/bf02869271)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
