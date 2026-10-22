# Mg–Ti system

> Mg–Ti system: 7 accepted literature values (phase transition 4, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-TI.html · Markdown: https://data.orchid-project.org/systems/MG-TI.md

7 accepted literature values from 1 paper(s) (experimental 1, model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-TI.json) · [CSV](https://data.orchid-project.org/systems/MG-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-TI/MgTi-86Mur.json) · [Markdown](https://data.orchid-project.org/systems/MG-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgTi-86Mur.tdb | J.L. Murray, Bull. Alloy Phase Diagrams, 7, 245-48(1986). [doi:10.1007/BF02868999](https://doi.org/10.1007/BF02868999) | `f80e2adcacb6b13d5c4fb55cd9f677865697ac52de15813bc2126c426ca56bfd` | [viewer](https://orchid-project.org/phase-diagrams/#MG-TI/MgTi-86Mur.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgTi-86Mur.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgTi-86Mur.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MgTi-86Mur.tdb | 2178.17 | LIQUID#2 (x(Ti) 0.01604) + BCC_A2 (x(Ti) 0.85738) + LIQUID (x(Ti) 0.98396) |
| MgTi-86Mur.tdb | 1135.22 | LIQUID (x(Ti) 1.800e-4) + BCC_A2 (x(Ti) 0.97442) + HCP_A3 (x(Ti) 0.98366) |
| MgTi-86Mur.tdb | 923.98 | LIQUID (x(Ti) 2.000e-5) + HCP_A3 (x(Ti) 0.0012) + HCP_A3#2 (x(Ti) 0.98523) |
| MgTi-86Mur.tdb | 923.98 | LIQUID (x(Ti) 2.000e-5) + HCP_A3 (x(Ti) 0.0012) + HCP_A3#2 (x(Ti) 0.98523) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MG/MG-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mg–Ti system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1163.15 | peritectic |  | experimental | [1] Murray 1986; _cites ref. 59Obi_ | p. 3 | “\[59Obi\] r e p o r t e d a p e r i t e c t i c - t y p e r e a c t i o n a t a b o u t 890 ~ and reported solubilities of Mg in (flTi) between 0.6 and 1.2 at.% in the range 900 to 1200 ~” |
| 1138.15 | Catatectic(a): (βTi) -> (αTi) + (LMg) | (βTi): Ti 0.976; (αTi): Ti 0.984; (LMg): Ti 1.400e-4 | model | [1] Murray 1986 | Table 1, p. 2, row 2 |  |
| 924.15 | Peritectic: L + (αTi) -> (Mg) | L: Ti 1.000e-5; (αTi): Ti 0.985; (Mg): Ti 0.0012 | model | [1] Murray 1986 | Table 1, p. 2, row 1 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Mg–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 923.15 K | 923.15 | Melting point: L -> (Mg); _(Mg): Ti 0_ | model | [1] Murray 1986 | Table 1, p. 2, row 5 |  |
| Phase transition | 1138.15 K | 1138.15 | other: (/3Ti) ~ (aTi) + (LMg) | model | [1] Murray 1986 | p. 3 | “The catatectic (inverted peritectic) reaction (/3Ti) ~ (aTi) + (LMg) is shown in the assessed diagram at 865 ~” |
| Phase transition | 1155.15 K | 1155.15 | Allotropic transformation: (βTi) -> (αTi); _(βTi): Ti 1_ | model | [1] Murray 1986 | Table 1, p. 2, row 4 |  |
| Phase transition | 1943.15 K | 1943.15 | Melting point: L -> (βTi); _(βTi): Ti 1_ | model | [1] Murray 1986 | Table 1, p. 2, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. L. Murray, The Mg−Ti (Magnesium-Titanium) system, Bulletin of Alloy Phase Diagrams 7, 245-248 (1986). [doi:10.1007/bf02868999](https://doi.org/10.1007/bf02868999)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
