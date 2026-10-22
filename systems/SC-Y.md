# Sc–Y system

> Sc–Y system: 20 accepted literature values (phase transition 20) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SC-Y.html · Markdown: https://data.orchid-project.org/systems/SC-Y.md

20 accepted literature values from 2 paper(s) (experimental 10, model 6, unspecified 4); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SC-Y.json) · [CSV](https://data.orchid-project.org/systems/SC-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SC-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SC-Y/ScY-00Nor.json) · [Markdown](https://data.orchid-project.org/systems/SC-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 10 |
| model | 6 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 20 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ScY-00Nor.tdb | S. Norgren, PhD thesis, KTH, Stockholm, 2000. | `244681b40e3620924487fc2ae9f80553596a2b1ca69fd729a9f6bcd59b471742` | [viewer](https://orchid-project.org/phase-diagrams/#SC-Y/ScY-00Nor.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScY-00Nor.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScY-00Nor.json) |
| ScY-09Wan.tdb | S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, J. Alloys Compd., 476, 187-92(2009). [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053) | `45f44917339661b3ad1f36616a2ad59ad82df3fe0c159fb0ad1a9e26c12359cc` | [viewer](https://orchid-project.org/phase-diagrams/#SC-Y/ScY-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScY-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScY-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ScY-00Nor.tdb | 1784.13 | HCP_A3 (x(Y) 1) + LIQUID (x(Y) 1) + BCC_A2 (x(Y) 1) |
| ScY-09Wan.tdb | 1784.13 | HCP_A3 (x(Y) 1) + LIQUID (x(Y) 1) + BCC_A2 (x(Y) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SC/SC-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SC/SC-Y.json) · [CALPHAD hull ScY-00Nor](https://data.orchid-project.org/hulls/calphad-sgte/SC/SC-Y--ScY-00Nor.json)

## Other properties

### Phase transition (20)

Table: Phase transition, Sc–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1448.15 K | 1448.15 | congruent transformation: (βSc, βY) \<-> (αSc, αY); _(βSc, βY): Y 0.43; (αSc, αY): Y 0.5_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 16 |  |
| Phase transition | 1453 K | 1453 |  | experimental | [2] Hu 2018 | p. 2 | “The phase transition lines of β↔α reach a common minimum at 1453 K, 43 at.% Y.” |
| Phase transition | 1453.15 K | 1453.15 | congruent transformation: (βSc, βY) \<-> (αSc, αY); _(βSc, βY): Y 0.42; (αSc, αY): Y 0.5_ | model | [1] Wang 2009 | Table 5, p. 5, row 18 |  |
| Phase transition | 1453.15 K | 1453.15 | congruent transformation: (βSc, βY) \<-> (αSc, αY); _(βSc, βY): Y 0.43; (αSc, αY): Y 0.5_ | experimental | [1] Wang 2009; _cites Gschneidner 1983_ [doi](https://doi.org/10.1007/bf02868085) | Table 5, p. 5, row 17 |  |
| Phase transition | 1607.15 K | 1607.15 | polymorphic: βSc \<-> αSc; _βSc: Y 0_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 4 |  |
| Phase transition | 1610.15 K | 1610.15 | polymorphic: βSc \<-> αSc; _βSc: Y 0_ | unspecified | [1] Wang 2009; _cites Beaudry 1978_ | Table 5, p. 5, row 5 |  |
| Phase transition | 1610.15 K | 1610.15 | polymorphic: βSc \<-> αSc; _βSc: Y 0_ | model | [1] Wang 2009 | Table 5, p. 5, row 6 |  |
| Phase transition | 1638 K | 1638 | other | experimental | [2] Hu 2018 | p. 2 | “The liquidus and solidus reach a common minimum at 1638 K, 50 at.% Y.” |
| Phase transition | 1638.15 K | 1638.15 | congruent melting: L \<-> (βSc, βY); _(βSc, βY): Y 0.5_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 7 |  |
| Phase transition | 1645.15 K | 1645.15 | congruent melting: L \<-> (βSc, βY); _(βSc, βY): Y 0.5_ | model | [1] Wang 2009 | Table 5, p. 5, row 9 |  |
| Phase transition | 1645.15 K | 1645.15 | congruent melting: L \<-> (βSc, βY); _(βSc, βY): Y 0.5_ | experimental | [1] Wang 2009; _cites Gschneidner 1983_ [doi](https://doi.org/10.1007/bf02868085) | Table 5, p. 5, row 8 |  |
| Phase transition | 1733.15 K | 1733.15 | polymorphic: βY \<-> αY; _βY: Y 1_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 13 |  |
| Phase transition | 1751.15 K | 1751.15 | polymorphic: βY \<-> αY; _βY: Y 1_ | unspecified | [1] Wang 2009; _cites Beaudry 1978_ | Table 5, p. 5, row 14 |  |
| Phase transition | 1751.15 K | 1751.15 | polymorphic: βY \<-> αY; _βY: Y 1_ | model | [1] Wang 2009 | Table 5, p. 5, row 15 |  |
| Phase transition | 1783.15 K | 1783.15 | congruent melting: L \<-> βY; _βY: Y 1_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 10 |  |
| Phase transition | 1795.15 K | 1795.15 | congruent melting: L \<-> βY; _βY: Y 1_ | unspecified | [1] Wang 2009; _cites Beaudry 1978_ | Table 5, p. 5, row 11 |  |
| Phase transition | 1795.15 K | 1795.15 | congruent melting: L \<-> βY; _βY: Y 1_ | model | [1] Wang 2009 | Table 5, p. 5, row 12 |  |
| Phase transition | 1812.15 K | 1812.15 | congruent melting: L \<-> βSc; _βSc: Y 0_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 1 |  |
| Phase transition | 1814.15 K | 1814.15 | congruent melting: L \<-> βSc; _βSc: Y 0_ | unspecified | [1] Wang 2009; _cites Beaudry 1978_ | Table 5, p. 5, row 2 |  |
| Phase transition | 1814.15 K | 1814.15 | congruent melting: L \<-> βSc; _βSc: Y 0_ | model | [1] Wang 2009 | Table 5, p. 5, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Y and Sc–Y systems, Journal of Alloys and Compounds 476, 187-192 (2009). [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053)
2. J.L. Hu, H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic study of the Al-Sc-Y system, Thermochimica Acta 661, 147-159 (2018). [doi:10.1016/j.tca.2018.01.018](https://doi.org/10.1016/j.tca.2018.01.018)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
