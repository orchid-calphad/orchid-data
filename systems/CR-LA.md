# Cr–La system

> Cr–La system: 34 accepted literature values (invariant reaction 17, phase transition 16, other property 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-LA.html · Markdown: https://data.orchid-project.org/systems/CR-LA.md

34 accepted literature values from 2 paper(s) (experimental 19, model 15); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-LA.json) · [CSV](https://data.orchid-project.org/systems/CR-LA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-LA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-LA/CrLa-09Cha.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CR-LA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-LA.html) · [Markdown](https://data.orchid-project.org/systems/CR-LA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 15 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 16 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrLa-09Cha.tdb | W. Chan, C. Gao, O.N. Dogan, P. King, A.D. Rollett, J. Phase Equilib. Diffus., 30, 578-86(2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) | `7eae47ddc2ae31cacba91eb581a06d8c4a493fafda31e53de4e901b25a137d70` | [viewer](https://orchid-project.org/phase-diagrams/#CR-LA/CrLa-09Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrLa-09Cha.json) |
| CrLa-09Pov.tdb | E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, J. Phase Equilib. Diffus., 30, 12-27(2009). [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0) | `af1685101b0145ad083258c09bda4e082c1a4e1a0e44f11a98444c43ca655fba` | [viewer](https://orchid-project.org/phase-diagrams/#CR-LA/CrLa-09Pov.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Pov.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrLa-09Pov.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrLa-09Cha.tdb | 2101.7 | BCC_A2 (x(La) 0.02155) + LIQUID#2 (x(La) 0.07873) + LIQUID (x(La) 0.73847) |
| CrLa-09Cha.tdb | 1142.91 | LIQUID (x(La) 0.97333) + FCC_A1 (x(La) 0.9963) + BCC_A2 (x(La) 0.99909) |
| CrLa-09Cha.tdb | 1138.03 | BCC_A2 (x(La) 0.00108) + LIQUID (x(La) 0.96903) + FCC_A1 (x(La) 0.99553) |
| CrLa-09Cha.tdb | 549.93 | BCC_A2 (x(La) 0) + FCC_A1 (x(La) 0.99999) + DHCP (x(La) 1) |
| CrLa-09Pov.tdb | 2142.42 | BCC_A2 (x(La) 0.00263) + LIQUID#2 (x(La) 0.02661) + LIQUID (x(La) 0.83326) |
| CrLa-09Pov.tdb | 1133.96 | LIQUID (x(La) 0.97187) + BCC_A2 (x(La) 0.99998) + FCC_A1 (x(La) 0.99999) |
| CrLa-09Pov.tdb | 1126.03 | BCC_A2 (x(La) 2.000e-5) + LIQUID (x(La) 0.96675) + FCC_A1 (x(La) 0.99999) |
| CrLa-09Pov.tdb | 1126.03 | BCC_A2 (x(La) 2.000e-5) + LIQUID (x(La) 0.96675) + FCC_A1 (x(La) 0.99999) |
| CrLa-09Pov.tdb | 550 | BCC_A2 (x(La) 0) + FCC_A1 (x(La) 1) + DHCP (x(La) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-LA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-LA.json) · [CALPHAD hull CrLa-09Pov](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-LA--CrLa-09Pov.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–La system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2248 | eutectic |  | experimental | [1] Povoden 2009; _cites Tresvjatskiy 1968_ | p. 2 | “In the LaO1.5-CrO1.5 system two eutectics were found at 19 at.% Cr2O3 (T = 2243 K)\[18\] or 12 at.% Cr2O3 (T = 2323 ± 20 K),\[19\] and at 84 at.% Cr2O3 (T = 2248 K)\[18\] or 80 at.% Cr2O3 (T = 2473 ± 20 K)\[19\] in argon atmosphere on either side of the congruently melting perovskitestructured lanthanum chromite\[18-20\] (in this study oxides containing Cr(III) and Cr with higher valencies than three are d…” |
| 2243 | eutectic |  | experimental | [1] Povoden 2009; _cites Tresvjatskiy 1968_ | p. 2 | “In the LaO1.5-CrO1.5 system two eutectics were found at 19 at.% Cr2O3 (T = 2243 K)\[18\] or 12 at.% Cr2O3 (T = 2323 ± 20 K),\[19\] and at 84 at.% Cr2O3 (T = 2248 K)\[18\] or 80 at.% Cr2O3 (T = 2473 ± 20 K)\[19\] in argon atmosphere on either side of the congruently melting perovskitestructured lanthanum chromite\[18-20\] (in this study oxides containing Cr(III) and Cr with higher valencies than three are d…” |
| 2108.25 | L1 -> L2 + Cr | L1: La 0.024; L2: La 0.976 | model | [2] Chan 2009; _cites Ray 2009_ | Table 3, p. 7, row 3 |  |
| 2103.15 | L1 -> L2 + Cr | L1: La 0.009; L2: La 0.82; Cr: La 0 | experimental | [2] Chan 2009; _cites Massalski 1990_ | Table 3, p. 7, row 2 |  |
| 2102.15 | L1 -> L2 + Cr | L1: La 0.0787; L2: La 0.739; Cr: La 0.0215 | model | [2] Chan 2009 | Table 3, p. 7, row 4 |  |
| 1983.15 | L1 -> L2 + Cr | L1: La 0.0399; Cr: La 0.0246 | experimental | [2] Chan 2009; _cites Savitskii 1960_ | Table 3, p. 7, row 1 |  |
| 1190.45 | L2 -> Cr + βLa | L2: La 0.9997 | model | [2] Chan 2009; _cites Ray 2009_ | Table 3, p. 7, row 9 |  |
| 1143.15 | L2 + γLa -> βLa | L2: La 0.973; γLa: La 0.999; βLa: La 0.996 | model | [2] Chan 2009 | Table 3, p. 7, row 5 |  |
| 1140.75 | L2 -> Cr + βLa | L2: La 0.97026 | model | [2] Chan 2009; _cites Terekhova 1990_ | Table 3, p. 7, row 8 |  |
| 1138.15 | L2 -> Cr + βLa |  | experimental | [2] Chan 2009; _cites Savitskii 1960_ | Table 3, p. 7, row 6 |  |
| 1138.15 | eutectic: L M Cr + cLa |  | experimental | [2] Chan 2009; _cites Savitskii 1960_ | p. 2 | “A eutectic reaction is reported by Savitskii et al.\[12\] that occurs at 865 °C ± 5 °C,\[12\] and it is presumed to be L M Cr + cLa, while Gschneider\[13\] assessed it at 900 °C instead.” |
| 1138.15 | L2 -> Cr + βLa | L2: La 0.966; Cr: La 0; βLa: La 1 | experimental | [2] Chan 2009; _cites Massalski 1990_ | Table 3, p. 7, row 7 |  |
| 1138.15 | eutectic: L M Cr + bLa |  | model | [2] Chan 2009; _cites Massalski 1990_ | p. 2 | “However, the handbook\[4\] assessed this eutectic reaction as L M Cr + bLa at 865 °C.” |
| 1138.15 | L2 -> Cr + βLa | L2: La 0.969; Cr: La 0.0011; βLa: La 0.996 | model | [2] Chan 2009 | Table 3, p. 7, row 10 |  |
| 1138 | eutectic |  | experimental | [1] Povoden 2009; _cites Savitskii 1960_ | p. 1 | “The La-Cr system has a eutectic at 1138 K\[12,13\] and 3.4 at.% Cr\[13\] and a monotectic at 1983 K\[12\] or 2103 K\[14\] and 96 at.%\[12\] or 99.1 at.%\[14\] Cr, as well as a large liquidliquid miscibility gap.\[12,13\]” |
| 978.15 | eutectoid: cLa M Cr + bLa |  | experimental | [2] Chan 2009; _cites Savitskii 1960_ | p. 2 | “Another invariant reaction is reported at around 705 °C by Savitskii et al.\[12\] whose reaction type is presumed to be eutectoid (cLa M Cr + bLa), while Gschneider\[13\] assessed it at 730 °C instead.” |
| 550.15 | βLa -> Cr + αLa | βLa: La 1; Cr: La 0; αLa: La 1 | model | [2] Chan 2009 | Table 3, p. 7, row 11 |  |

## Other properties

### Phase transition (16)

Table: Phase transition, Cr–La system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 287 K | 287 | magnetic | model | [1] Povoden 2009; _cites Sakai 1995_ [doi](https://doi.org/10.1006/jcht.1995.0051) | p. 3 | “A magnetic order-disorder transition was documented to occur at T 287 K,\[35\] 289 K,\[45\] or 295 K.\[46\]” |
| Phase transition | 289 K | 289 | magnetic | experimental | [1] Povoden 2009; _cites Weinberg 1961_ | p. 3 | “A magnetic order-disorder transition was documented to occur at T 287 K,\[35\] 289 K,\[45\] or 295 K.\[46\]” |
| Phase transition | 290 K | 290 | magnetic | model | [1] Povoden 2009 | p. 11 | “The calculated Cp-peak at 290 K reflects the temperature of the magnetic orderdisorder transition, the transition temperature being in agreement with the experiments.” |
| Phase transition | 295 K | 295 | magnetic | experimental | [1] Povoden 2009; _cites Cheng 2005_ [doi](https://doi.org/10.1557/jmr.2005.0018) | p. 3 | “A magnetic order-disorder transition was documented to occur at T 287 K,\[35\] 289 K,\[45\] or 295 K.\[46\]” |
| Phase transition | 540 K | 540 | o-prv -> r-prv | model | [1] Povoden 2009 | p. 11 | “The calculated transition temperature of 540 K is shown by the broken line in Fig. 6.” |
| Phase transition | 545 K | 545 | o-prv -> r-prv | experimental | [1] Povoden 2009 | p. 11 | “The experimentally determined Cp-peak around 545 K caused by the first-order transition o-prv M r-prv is in fact a discontinuity which cannot be implemented in the model.” |
| Phase transition | 855 K | 855 | other | model | [1] Povoden 2009; _cites Sakai 1995_ [doi](https://doi.org/10.1006/jcht.1995.0051) | p. 11 | “A small peak which was found around 855 K can be explained most likely by the decomposition of an undetected impurity phase.\[35\]” |
| Phase transition | 1983 K | 1983 | other | experimental | [1] Povoden 2009; _cites Savitskii 1960_ | p. 1 | “The La-Cr system has a eutectic at 1138 K\[12,13\] and 3.4 at.% Cr\[13\] and a monotectic at 1983 K\[12\] or 2103 K\[14\] and 96 at.%\[12\] or 99.1 at.%\[14\] Cr, as well as a large liquidliquid miscibility gap.\[12,13\]” |
| Phase transition | 1983.15 K | 1983.15 | other | experimental | [2] Chan 2009; _cites Savitskii 1960_ | p. 2 | “Savitskii et al.\[12\] reported that the monotectic temperature is 1710 °C, but it is considered inaccurate by the currently accepted phase diagram\[4\] that uses 1830 °C instead.” |
| Phase transition | 2103 K | 2103 | other | experimental | [1] Povoden 2009; _cites Svechnikov 1973_ | p. 1 | “The La-Cr system has a eutectic at 1138 K\[12,13\] and 3.4 at.% Cr\[13\] and a monotectic at 1983 K\[12\] or 2103 K\[14\] and 96 at.%\[12\] or 99.1 at.%\[14\] Cr, as well as a large liquidliquid miscibility gap.\[12,13\]” |
| Phase transition | 2103.15 K | 2103.15 | other | model | [2] Chan 2009; _cites Massalski 1990_ | p. 2 | “Savitskii et al.\[12\] reported that the monotectic temperature is 1710 °C, but it is considered inaccurate by the currently accepted phase diagram\[4\] that uses 1830 °C instead.” |
| Phase transition | 2130 K | 2130 | Cr + liquid | experimental | [1] Povoden 2009; _cites Savitskii 1960_ | p. 8 | “Considerable deviations of the calculated liquidus from experiments at the Cr-rich side of the system can be ascribed to the problem of two different melting temperatures for Cr cited in the literature, which are 2180 and 2130 K. The higher value was favored by Dinsdale\[10\] and is adopted in this study, whereas the lower melting temperature was chosen by Savitskii et al.\[12\] and Svechnikov et al.…” |
| Phase transition | 2180 K | 2180 | Cr + liquid | model | [1] Povoden 2009; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | p. 8 | “Considerable deviations of the calculated liquidus from experiments at the Cr-rich side of the system can be ascribed to the problem of two different melting temperatures for Cr cited in the literature, which are 2180 and 2130 K. The higher value was favored by Dinsdale\[10\] and is adopted in this study, whereas the lower melting temperature was chosen by Savitskii et al.\[12\] and Svechnikov et al.…” |
| Phase transition | 2703 K | 2703 |  | experimental | [1] Povoden 2009; _cites Tresvjatskiy 1968_ | p. 2 | “Tm(argon) = 2703 K was reported by Tresvjatskiy et al.,\[18\] but in the graphic presentation of the phase diagram in the same paper Tm(argon) 2600 K, and the exact value of the oxygen partial pressure was not specified.” |
| Phase transition | 2773 K | 2773 |  | experimental | [1] Povoden 2009; _cites Coutures 1980_ | p. 2 | “The melting temperature of lanthanum chromite in air, Tm(air) = 2773 K was determined by Foëx\[21\] and by Coutures et al.\[20\] using a thermal analysis technique described in more detail in earlier publications.\[22-24\]” |
| Phase transition | 2967.15 K | 2967.15 | other | model | [2] Chan 2009 | p. 7 | “The gap is broadest for Cr-La system and the critical point is about 2694 °C.” |

### Other property (1)

Table: Other property, Cr–La system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: enthalpy change_ | 231 unspecified | 960 |  | experimental | [1] Povoden 2009; _cites Yu 2005_ | p. 2 | “An enthalpy change of 231 kJ mol-1 was determined for this reaction at the average temperature of 960 K.\[30\]” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, Thermodynamic Assessment of the La-Cr-O System, J. Phase Equilib. Diffus. 30, 12-27 (2009). [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0)
2. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
