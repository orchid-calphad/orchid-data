# In–Ir system

> In–Ir system: 44 accepted literature values (invariant reaction 35, phase transition 8, mixing / partial 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-IR.html · Markdown: https://data.orchid-project.org/systems/IN-IR.md

44 accepted literature values from 1 paper(s) (experimental 19, model 17, unspecified 8); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-IR.json) · [CSV](https://data.orchid-project.org/systems/IN-IR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-IR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-IR/InIr-11Ser.json) · [phases (9)](https://data.orchid-project.org/phases/pages/IN-IR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/IN-IR.html) · [Markdown](https://data.orchid-project.org/systems/IN-IR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 17 |
| unspecified | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 35 |
| phase transition | 8 |
| mixing / partial | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InIr-11Ser.tdb | C. Servant, M. Idbenali, Thermochim. Acta, 517, 1-8(2011). [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) | `08d4e25130797918e03f7a335e97e6a40dcd96678f151c1146ed0f4f1d957cc0` | [viewer](https://orchid-project.org/phase-diagrams/#IN-IR/InIr-11Ser.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InIr-11Ser.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InIr-11Ser.tdb | 1461.07 | LIQUID (x(Ir) 0.30592) + IN2IR_CB (x(Ir) 0.38395) + FCC_A1 (x(Ir) 0.96302) |
| InIr-11Ser.tdb | 1254.08 | LIQUID (x(Ir) 0.10124) + IN3IR_HT (x(Ir) 0.24523) + IN2IR_CB (x(Ir) 0.30808) |
| InIr-11Ser.tdb | 634 | IN3IR_HT (x(Ir) 0.24999) + IN3IR_D011 (x(Ir) 0.25) + IN2IR_CB (x(Ir) 0.3209) |
| InIr-11Ser.tdb | 620.57 | LIQUID (x(Ir) 2.000e-5) + IN3IR_HT (x(Ir) 0.23657) + IN3IR_D011 (x(Ir) 0.24001) |
| InIr-11Ser.tdb | 620.57 | LIQUID (x(Ir) 2.000e-5) + IN3IR_HT (x(Ir) 0.23657) + IN3IR_D011 (x(Ir) 0.24001) |
| InIr-11Ser.tdb | 429.75 | LIQUID (x(Ir) 0) + TETRAGONAL_A6 (x(Ir) 0) + IN3IR_D011 (x(Ir) 0.23823) |
| InIr-11Ser.tdb | 429.75 | TETRAGONAL_A6 (x(Ir) 0) + LIQUID (x(Ir) 0) + IN3IR_D011 (x(Ir) 0.23822) |
| InIr-11Ser.tdb | 429.75 | LIQUID (x(Ir) 0) + TETRAGONAL_A6 (x(Ir) 0) + IN3IR_D011 (x(Ir) 0.23823) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-IR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-IR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the In–Ir system (35)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1463.15 | Liq ⇔ In2Ir + (Ir) | In2Ir: In 0.666667, Ir 0.333333 | unspecified | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | Table 5, p. 6, row 12 |  |
| 1463.15 | Liq -> In2 Ir + (Ir) | In2 Ir: In 0.666667, Ir 0.333333 | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | Table 3, p. 5, row 14 |  |
| 1463.15 | Liq -> In2 Ir | Liq: Ir 0.33; In2 Ir: Ir 0.33; In2Ir: Ir 0.33 | model | [1] Servant 2011 | Table 3, p. 5, row 12 |  |
| 1463 | peritectic |  | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | p. 6 | “In2 Ir shows a congruent melting at 1463 K.” |
| 1461.15 | Liq ⇔ In2Ir + (Ir) | In2Ir: In 0.666667, Ir 0.333333 | unspecified | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 5, p. 6, row 11 |  |
| 1461.15 | Liq -> In2 Ir + (Ir) | In2 Ir: In 0.666667, Ir 0.333333 | experimental | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 3, p. 5, row 13 |  |
| 1461.15 | Liq ⇔ In2Ir + (Ir) | Liq: Ir 0.3057; In2Ir: Ir 0.3837; (Ir): Ir 0.9621 | model | [1] Servant 2011 | Table 5, p. 6, row 13 |  |
| 1461 | peritectic: Liq + (Ir) ↔ In2 Ir |  | model | [1] Servant 2011 | p. 7 | “The calculated peritectic reaction (Liq + (Ir) ↔ In2 Ir) at 1461 K is in” |
| 1258.15 | Liq + In2Ir ⇔ In3Ir_HT | In2Ir: In 0.666667, Ir 0.333333; In3Ir_HT: In 0.75, Ir 0.25 | unspecified | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | Table 5, p. 6, row 9 |  |
| 1258.15 | Liq + In2 Ir -> In3 Ir_HT | In2 Ir: In 0.666667, Ir 0.333333; In3 Ir_HT: In 0.75, Ir 0.25 | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | Table 3, p. 5, row 10 |  |
| 1258 | peritectic: Liq + In2 Ir ↔ In3 Ir HT |  | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | p. 6 | “Thus the calculated temperature 1254 K of the peritectic invariant reaction Liq + In2 Ir ↔ In3 Ir HT is also in good agreement with the experimental 1254 ± 3 K \[12\] or 1258 K one \[11\]; the Ir composition of the liquid phase (0.097 Ir) is quite in agreement with the one (0.10 Ir) mentioned in \[12\], Table 3.” |
| 1258 | eutectic |  | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | p. 1 | “By differential thermal analysis Anres et al. \[11\] measured the temperatures of the eutectic (about 1258 K) and peritectic” |
| 1254.15 | Liq + In2Ir ⇔ In3Ir_HT | In2Ir: In 0.666667, Ir 0.333333; In3Ir_HT: In 0.75, Ir 0.25 | unspecified | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 5, p. 6, row 8 |  |
| 1254.15 | Liq + In2 Ir -> In3 Ir_HT | Liq: Ir 0.0976; In2 Ir: Ir 0.2934; In3 Ir_HT: Ir 0.2442; In2Ir: Ir 0.2934; In3Ir_HT: Ir 0.2442 | model | [1] Servant 2011 | Table 3, p. 5, row 11 |  |
| 1254.15 | Liq + In2 Ir -> In3 Ir_HT | In2 Ir: In 0.666667, Ir 0.333333; In3 Ir_HT: In 0.75, Ir 0.25 | experimental | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 3, p. 5, row 9 |  |
| 1254.15 | Liq + In2Ir ⇔ In3Ir_HT | Liq: Ir 0.1012; In2Ir: Ir 0.308; In3Ir_HT: Ir 0.2452 | model | [1] Servant 2011 | Table 5, p. 6, row 10 |  |
| 1254 | peritectic: Liq + In2 Ir ↔ In3 Ir HT |  | model | [1] Servant 2011 | p. 6 | “Thus the calculated temperature 1254 K of the peritectic invariant reaction Liq + In2 Ir ↔ In3 Ir HT is also in good agreement with the experimental 1254 ± 3 K \[12\] or 1258 K one \[11\]; the Ir composition of the liquid phase (0.097 Ir) is quite in agreement with the one (0.10 Ir) mentioned in \[12\], Table 3.” |
| 1254 | peritectic: Liq + In2 Ir ↔ In3 Ir HT |  | experimental | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | p. 6 | “Thus the calculated temperature 1254 K of the peritectic invariant reaction Liq + In2 Ir ↔ In3 Ir HT is also in good agreement with the experimental 1254 ± 3 K \[12\] or 1258 K one \[11\]; the Ir composition of the liquid phase (0.097 Ir) is quite in agreement with the one (0.10 Ir) mentioned in \[12\], Table 3.” |
| 894.25 | Liq -> In2 Ir + (Ir) | Liq: Ir 0.5984; In2 Ir: Ir 0.3414; (Ir): Ir 0.9752; In2Ir: Ir 0.3414 | model | [1] Servant 2011 | Table 3, p. 5, row 15 |  |
| 894.1 | eutectic: Liq ↔ In2 Ir + (Ir) |  | model | [1] Servant 2011 | p. 6 | “In fact in the composition range 0.35 ≤ x(Ir) ≤ 1, instead of the peritectic reaction Liq + (Ir) ↔ In2 Ir a eutectic reaction (Liq ↔ In2 Ir + (Ir)) was observed at T = 894.1 K for x(Liq,Ir) = 0.598, Fig. 4 and Table 3.” |
| 636.15 | In2 Ir + In3 Ir-HT -> In3 Ir-LT | In2 Ir: In 0.666667, Ir 0.333333; In3 Ir-HT: In 0.75, Ir 0.25; In3 Ir-LT: In 0.75, Ir 0.25 | experimental | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 3, p. 5, row 7 |  |
| 636.15 | In2Ir + In3Ir_HT ⇔ In3Ir_LT | In2Ir: In 0.666667, Ir 0.333333; In3Ir_HT: In 0.75, Ir 0.25; In3Ir_LT: In 0.75, Ir 0.25 | unspecified | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 5, p. 6, row 6 |  |
| 634.85 | In2 Ir + In3 Ir-HT -> In3 Ir-LT | In2 Ir: Ir 0.3278; In3 Ir-HT: In 0.75, Ir 0.25; In3 Ir-LT: In 0.75, Ir 0.25; In3 Ir_HT: Ir 0.25; In3 Ir_LT: Ir 0.25; In2Ir: Ir 0.3278; In3Ir_HT: Ir 0.25; In3Ir_LT: Ir 0.25 | model | [1] Servant 2011 | Table 3, p. 5, row 8 |  |
| 634.15 | In2Ir + In3Ir_HT ⇔ In3Ir_LT | In2Ir: Ir 0.3208; In3Ir_HT: Ir 0.25; In3Ir_LT: Ir 0.25 | model | [1] Servant 2011 | Table 5, p. 6, row 7 |  |
| 625.15 | In3 Ir-HT -> Liq + In3 Ir-LT | In3 Ir-HT: In 0.75, Ir 0.25; In3 Ir-LT: In 0.75, Ir 0.25 | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | Table 3, p. 5, row 5 |  |
| 620.75 | In3Ir-HT ⇔ Liq + In3Ir-LT | Liq: Ir 1.800e-5; In3Ir-LT: Ir 0.24; In3Ir_HT: Ir 0.2366; In3Ir_LT: Ir 0.24 | model | [1] Servant 2011 | Table 5, p. 6, row 5 |  |
| 620.15 | In3 Ir-HT -> Liq + In3 Ir-LT | In3 Ir-HT: Ir 0.2386; Liq: Ir 3.700e-5; In3 Ir-LT: Ir 0.2425; In3Ir_LT: Ir 0.2425; In3Ir_HT: Ir 0.2386 | model | [1] Servant 2011 | Table 3, p. 5, row 6 |  |
| 620.15 | In3 Ir-HT -> Liq + In3 Ir-LT | In3 Ir-HT: In 0.75, Ir 0.25; In3 Ir-LT: In 0.75, Ir 0.25 | experimental | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 3, p. 5, row 4 |  |
| 620.15 | In3Ir-HT ⇔ Liq + In3Ir-LT | In3Ir-HT: In 0.75, Ir 0.25; In3Ir-LT: In 0.75, Ir 0.25 | unspecified | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 5, p. 6, row 4 |  |
| 429.95 | Liq ⇔ In + In3Ir-LT | Liq: Ir 0; In: Ir 0; In3Ir-LT: Ir 0.2382; In3Ir_LT: Ir 0.2382 | model | [1] Servant 2011 | Table 5, p. 6, row 3 |  |
| 429.95 | Liq -> In + In3 Ir-LT | Liq: Ir 0; In: Ir 0; In3 Ir-LT: Ir 0.2424; In3Ir_LT: Ir 0.2424 | model | [1] Servant 2011 | Table 3, p. 5, row 3 |  |
| 429.79 | Liq ⇔ In + In3Ir-LT | In3Ir-LT: In 0.75, Ir 0.25 | unspecified | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | Table 5, p. 6, row 2 |  |
| 429.79 | Liq -> In + In3 Ir-LT | In3 Ir-LT: In 0.75, Ir 0.25 | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | Table 3, p. 5, row 2 |  |
| 429.15 | Liq ⇔ In + In3Ir-LT |  | unspecified | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 5, p. 6, row 1 |  |
| 429.15 | Liq -> In + In3 Ir-LT |  | experimental | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | Table 3, p. 5, row 1 |  |

## Other properties

### Phase transition (8)

Table: Phase transition, In–Ir system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 429 K | 429 |  | experimental | [1] Servant 2011 | p. 1 | “Because of the large differences in the melting temperatures of In (429 K) and Ir (2723 K), the evaporation of In must be accurately controlled” |
| Phase transition | 429 K | 429 | Liq ↔ In + In3 Ir LT | experimental | [1] Servant 2011; _cites Flandorfer 2002_ [doi](https://doi.org/10.1016/s0925-8388%2802%2900287-6) | p. 6 | “Its temperature 429.8 K is within the error bar 429 ± 2 K given by Flandorfer et al. \[12\].” |
| Phase transition | 429.8 K | 429.8 | Liq ↔ In + In3 Ir LT | model | [1] Servant 2011 | p. 6 | “Its temperature 429.8 K is within the error bar 429 ± 2 K given by Flandorfer et al. \[12\].” |
| Phase transition | 620 K | 620 | Liq + In3 Ir LT ↔ In3 Ir HT | model | [1] Servant 2011 | p. 6 | “It will be noted that the transformation Liq + In3 Ir LT ↔ In3 Ir HT occurs at 620.0 K while the In2 Ir + In3 Ir HT ↔ In3 Ir LT reaction takes place at 634.7 K.” |
| Phase transition | 625 K | 625 |  | experimental | [1] Servant 2011 | p. 2 | “A change of structure LT ↔ HT was noticed at 625 K for In3 Ir.” |
| Phase transition | 625 K | 625 | In3 Ir LT ↔ In3 Ir HT | experimental | [1] Servant 2011 | p. 5 | “In addition, the experimental structural transformation In3 Ir LT ↔ In3 Ir HT at 625 K was assumed.” |
| Phase transition | 634.7 K | 634.7 | In2 Ir + In3 Ir HT ↔ In3 Ir LT | model | [1] Servant 2011 | p. 6 | “It will be noted that the transformation Liq + In3 Ir LT ↔ In3 Ir HT occurs at 620.0 K while the In2 Ir + In3 Ir HT ↔ In3 Ir LT reaction takes place at 634.7 K.” |
| Phase transition | 2723 K | 2723 |  | experimental | [1] Servant 2011 | p. 1 | “Because of the large differences in the melting temperatures of In (429 K) and Ir (2723 K), the evaporation of In must be accurately controlled” |

### Mixing / partial (1)

Table: Mixing / partial, In–Ir system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Partial enthalpy; _printed: partial molar enthalpy of mixing_ | -50 unspecified ± 2 | 1154 | liquid | experimental | [1] Servant 2011; _cites Anres 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900507-1) | p. 2 | “They found that at 1154 K the limiting partial molar enthalpy of mixing of hypothetically supercooled liquid iridium in liquid indium is equal to -50 ± 2 kJ/mol.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011). [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019)

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
