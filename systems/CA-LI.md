# Ca–Li system

> Ca–Li system: 8 accepted literature values (invariant reaction 6, formation 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-LI.html · Markdown: https://data.orchid-project.org/systems/CA-LI.md

8 accepted literature values from 1 paper(s) (experimental 4, model 3, unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-LI.json) · [CSV](https://data.orchid-project.org/systems/CA-LI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-LI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-LI/CaLi-02Gro-LB.json) · [Markdown](https://data.orchid-project.org/systems/CA-LI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 3 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| formation | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaLi-02Gro-LB.tdb | J. Groebner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv, D.G. Kevorkov, O.I. Bodak, Thermochim. Acta, 389, 85-94(2002). [doi:10.1016/S0040-6031(01)00842-5](https://doi.org/10.1016/S0040-6031%2801%2900842-5) | `91ea24f374ce086f3997f8e274d9fa664d5ab91fbc512955fafff8bce4cf8642` | [viewer](https://orchid-project.org/phase-diagrams/#CA-LI/CaLi-02Gro-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaLi-02Gro-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaLi-02Gro-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaLi-02Gro-LB.tdb | 642.54 | FCC_A1 (x(Li) 0.06614) + BCC_A2 (x(Li) 0.08624) + LIQUID (x(Li) 0.43535) |
| CaLi-02Gro-LB.tdb | 506.46 | FCC_A1 (x(Li) 0.09604) + LIQUID (x(Li) 0.57162) + CALI2_C14 (x(Li) 0.66667) |
| CaLi-02Gro-LB.tdb | 506.46 | FCC_A1 (x(Li) 0.09611) + LIQUID (x(Li) 0.57192) + CALI2_C14 (x(Li) 0.66667) |
| CaLi-02Gro-LB.tdb | 418.05 | CALI2_C14 (x(Li) 0.66667) + LIQUID (x(Li) 0.9318) + BCC_A2 (x(Li) 0.98724) |
| CaLi-02Gro-LB.tdb | 418.05 | CALI2_C14 (x(Li) 0.66667) + LIQUID (x(Li) 0.93203) + BCC_A2 (x(Li) 0.98729) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-LI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-LI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Li system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 643.15 | βCa = αCa + liquid | βCa: Li 0.09; αCa: Li 0.08; liquid: Li 0.43 | experimental | [1] Gröbner 2002; _cites Bale 1987_ [doi](https://doi.org/10.1007/bf02873196) | Table 1, p. 2, row 1 |  |
| 642.65 | βCa = αCa + liquid | βCa: Li 0.086; αCa: Li 0.066; liquid: Li 0.435 | model | [1] Gröbner 2002 | Table 1, p. 2, row 2 |  |
| 506.55 | Liquid = αCa + CaLi2 | αCa: Li 0.096; CaLi2: Li 0.6667; Liquid: Li 0.571 | model | [1] Gröbner 2002 | Table 1, p. 2, row 4 |  |
| 503.15 | Liquid = αCa + CaLi2 | αCa: Li 0.105; CaLi2: Li 0.6667; Liquid: Li 0.59 | experimental | [1] Gröbner 2002; _cites Bale 1987_ [doi](https://doi.org/10.1007/bf02873196) | Table 1, p. 2, row 3 |  |
| 418.15 | Liquid = CaLi2 + (Li) | CaLi2: Li 0.6667; (Li): Li 0.987; Liquid: Li 0.932 | model | [1] Gröbner 2002 | Table 1, p. 2, row 6 |  |
| 414.15 | Liquid = CaLi2 + (Li) | CaLi2: Li 0.6667; (Li): Li 0.98; Liquid: Li 0.92 | experimental | [1] Gröbner 2002; _cites Bale 1987_ [doi](https://doi.org/10.1007/bf02873196) | Table 1, p. 2, row 5 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ca–Li system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CaLi2 |  | -4.5 kJ/mol (basis unstated) ± 1.6 | 298.15 | experimental |  |  | [1] Gröbner 2002 | Table 2, p. 3, row 1 |  |
| CaLi2 |  | -3.89 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Gröbner 2002 | Table 2, p. 3, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Gröbner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv et al., Phase equilibria, calorimetric study and thermodynamic modeling of Mg–Li–Ca alloys, Thermochimica Acta 389, 85-94 (2002). [doi:10.1016/s0040-6031(01)00842-5](https://doi.org/10.1016/s0040-6031%2801%2900842-5)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
