# Cr–Sc system

> Cr–Sc system: 6 accepted literature values (invariant reaction 5, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-SC.html · Markdown: https://data.orchid-project.org/systems/CR-SC.md

6 accepted literature values from 2 paper(s) (experimental 4, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-SC.json) · [CSV](https://data.orchid-project.org/systems/CR-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-SC) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-SC/CrSc-12Bu.json) · [Markdown](https://data.orchid-project.org/systems/CR-SC.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrSc-12Bu.tdb | M.J. Bu, Y.B. Peng, M. Wang, Y. Du, H.H. Xu, D.D. Zhao, C.S. Sha, J. Phase Equilib. Diffus., 33, 40-45(2012). [doi:10.1007/s11669-011-9978-7](https://doi.org/10.1007/s11669-011-9978-7) | `255c2195d566a2929e7470af4ce93837a83ebe40e63894a80057222163a3289c` | [viewer](https://orchid-project.org/phase-diagrams/#CR-SC/CrSc-12Bu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrSc-12Bu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrSc-12Bu.json) |
| CrSc-15Wan.tdb | S.L. Wang, L.J. Zhou, Y. Ye, X.H. Wang, Y.H. Lin, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 36, 3-9(2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) | `a5b5b3689bf2cb9849c8644e9ec276fc33324f156c9246cca4fc702a7121e407` | [viewer](https://orchid-project.org/phase-diagrams/#CR-SC/CrSc-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrSc-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrSc-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrSc-12Bu.tdb | 1367.78 | BCC_A2 (x(Sc) 0.01323) + LIQUID (x(Sc) 0.65074) + BCC_A2#2 (x(Sc) 0.90507) |
| CrSc-12Bu.tdb | 1265.05 | BCC_A2 (x(Sc) 0.00914) + BCC_A2#2 (x(Sc) 0.92353) + HCP_A3 (x(Sc) 0.98822) |
| CrSc-15Wan.tdb | 1363.17 | BCC_A2 (x(Sc) 9.800e-4) + LIQUID (x(Sc) 0.6515) + BCC_A2#2 (x(Sc) 0.92319) |
| CrSc-15Wan.tdb | 1263.22 | BCC_A2 (x(Sc) 5.900e-4) + BCC_A2#2 (x(Sc) 0.93392) + HCP_A3 (x(Sc) 0.98615) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-SC.json) · [CALPHAD hull CrSc-12Bu](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-SC--CrSc-12Bu.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–Sc system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1363.15 | eutectic: L (65.2 at.% Sc) M (Cr) + bSc (92.3 at.% Sc) |  | model | [1] Wang 2015 | p. 2 | “The calculated eutectoid reaction (bSc(93.4 at.% Sc) M (Cr) + aSc(98.62 at.% Sc)) occurs at 990.1 °C, and the calculated eutectic reaction (L (65.2 at.% Sc) M (Cr) + bSc (92.3 at.% Sc)) is located at 1090 °C.” |
| 1363.15 | eutectic: Liquid (bCr) + (bSc) |  | experimental | [2] Bu 2012; _cites Svechnikov 1972_ | p. 2 | “The eutectoid reaction temperature for (bSc) (bCr) + (aSc) and the eutectic reaction temperature for Liquid (bCr) + (bSc) were determined by Svechnikov et al.\[18\] to be 990 °C at 60-65 at.% Sc and to be 1090 °C, respectively.” |
| 1363.15 | eutectic: L -> (Cr) + bSc |  | experimental | [1] Wang 2015; _cites Svechnikov 1972_ | p. 1 | “Based on differential thermal analysis (DTA), microhardness measurements, x-ray diffraction (XRD) and metallographic methods, the Sc-Cr system was investigated by Svechnikov et al.,\[8\] who determined a eutectic reaction (L (65 at.% Sc) M (Cr) + bSc at 1090 °C) and a eutectoid reaction (bSc M (Cr) + aSc at 990 °C).” |
| 1263.25 | eutectoid: bSc(93.4 at.% Sc) M (Cr) + aSc(98.62 at.% Sc) |  | model | [1] Wang 2015 | p. 2 | “The calculated eutectoid reaction (bSc(93.4 at.% Sc) M (Cr) + aSc(98.62 at.% Sc)) occurs at 990.1 °C, and the calculated eutectic reaction (L (65.2 at.% Sc) M (Cr) + bSc (92.3 at.% Sc)) is located at 1090 °C.” |
| 1263.15 | eutectoid: bSc -> (Cr) + aSc |  | experimental | [1] Wang 2015; _cites Svechnikov 1972_ | p. 1 | “Based on differential thermal analysis (DTA), microhardness measurements, x-ray diffraction (XRD) and metallographic methods, the Sc-Cr system was investigated by Svechnikov et al.,\[8\] who determined a eutectic reaction (L (65 at.% Sc) M (Cr) + bSc at 1090 °C) and a eutectoid reaction (bSc M (Cr) + aSc at 990 °C).” |

## Other properties

### Phase transition (1)

Table: Phase transition, Cr–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1263.15 K | 1263.15 | (bSc) (bCr) + (aSc) | experimental | [2] Bu 2012; _cites Svechnikov 1972_ | p. 2 | “The eutectoid reaction temperature for (bSc) (bCr) + (aSc) and the eutectic reaction temperature for Liquid (bCr) + (bSc) were determined by Svechnikov et al.\[18\] to be 990 °C at 60-65 at.% Sc and to be 1090 °C, respectively.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8)
2. M. J. Bu, Y. B. Peng, M. Wang, Y. Du, H. H. Xu, D. D. Zhao et al., Thermodynamic Optimization of the Sc-X (X = La, Li, Ca, Cr) Systems, J. Phase Equilib. Diffus. 33, 40-45 (2012). [doi:10.1007/s11669-011-9978-7](https://doi.org/10.1007/s11669-011-9978-7)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
