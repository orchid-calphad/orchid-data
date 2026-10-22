# Bi–Cr system

> Bi–Cr system: 3 accepted literature values (phase transition 2, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-CR.html · Markdown: https://data.orchid-project.org/systems/BI-CR.md

3 accepted literature values from 2 paper(s) (experimental 1, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-CR.json) · [CSV](https://data.orchid-project.org/systems/BI-CR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-CR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-CR/BiCr-13Cao.json) · [Markdown](https://data.orchid-project.org/systems/BI-CR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiCr-13Cao.tdb | Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang, Y. Du, J. Mining Metall. B, 49, 307-13(2013). [doi:10.2298/JMMB130127033C](https://doi.org/10.2298/JMMB130127033C) | `29ce6447bfe477c23626e12b83f63dfb13455691fd22a8dfbe548c134c5384c6` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CR/BiCr-13Cao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCr-13Cao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCr-13Cao.json) |
| BiCr-14Gos.tdb | S. Gosse, J. Nucl. Mater., 449, 122-31(2014). [doi:10.1016/j.jnucmat.2014.03.011](https://doi.org/10.1016/j.jnucmat.2014.03.011) | `836782b2e86fed0fbfd21aaa358ac16d69b07e6c3f9e13acc3421347434a198f` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CR/BiCr-14Gos.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCr-14Gos.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCr-14Gos.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiCr-13Cao.tdb | 1832.11 | LIQUID (x(Cr) 0.06217) + LIQUID#2 (x(Cr) 0.84962) + BCC_A2 (x(Cr) 0.99988) |
| BiCr-13Cao.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(Cr) 0) + LIQUID (x(Cr) 0) + BCC_A2 (x(Cr) 1) |
| BiCr-13Cao.tdb | 544.55 | LIQUID (x(Cr) 0) + RHOMBOHEDRAL_A7 (x(Cr) 0) + BCC_A2 (x(Cr) 1) |
| BiCr-14Gos.tdb | 2095.46 | LIQUID (x(Cr) 0.21948) + LIQUID#2 (x(Cr) 0.93275) + BCC_A2 (x(Cr) 0.9962) |
| BiCr-14Gos.tdb | 2095.46 | LIQUID#2 (x(Cr) 0.21948) + LIQUID (x(Cr) 0.93275) + BCC_A2 (x(Cr) 0.9962) |
| BiCr-14Gos.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(Cr) 0) + LIQUID (x(Cr) 0) + BCC_A2 (x(Cr) 1) |
| BiCr-14Gos.tdb | 544.55 | LIQUID (x(Cr) 0) + RHOMBOHEDRAL_A7 (x(Cr) 0) + BCC_A2 (x(Cr) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-CR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-CR.json) · [CALPHAD hull BiCr-13Cao](https://data.orchid-project.org/hulls/calphad-sgte/BI/BI-CR--BiCr-13Cao.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Cr system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2095 | monotectic |  | model | [1] Gossé 2014 | p. 4 | “The monotectic reaction is calculated at 2095 K and the critical point of the liquid miscibility gap is 3091 K for a 67 at.% Cr composition (Fig. 2(a)).” |

## Other properties

### Phase transition (2)

Table: Phase transition, Bi–Cr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1826.15 K | 1826.15 | Liquid#2 = (Cr) + (Bi) | experimental | [2] Cao 2013; _cites Williams 1907_ | p. 2 | “at 268 °C and Liquid#2 = (Cr) + (Bi) at 1553 °C were investigated by Williams \[24\] via continuous cooling of melting alloys of Bi and Cr.” |
| Phase transition | 3091 K | 3091 | other | model | [1] Gossé 2014 | p. 4 | “The monotectic reaction is calculated at 2095 K and the critical point of the liquid miscibility gap is 3091 K for a 67 at.% Cr composition (Fig. 2(a)).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Stéphane Gossé, Thermodynamic assessment of solubility and activity of iron, chromium, and nickel in lead bismuth eutectic, Journal of Nuclear Materials 449, 122-131 (2014). [doi:10.1016/j.jnucmat.2014.03.011](https://doi.org/10.1016/j.jnucmat.2014.03.011)
2. Z. Cao, J. Xin, C. Chen, S. Liu, B. Hu, C. Tang et al., Thermodynamic modeling of the Bi-M (M = Ti, Cr, V) systems, J min metall B Metall 49, 307-313 (2013). [doi:10.2298/jmmb130127033c](https://doi.org/10.2298/jmmb130127033c)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
