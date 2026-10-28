# Al system

> Al system: 45 accepted literature values (crystal structure 22, heat capacity / entropy / enthalpy 14, formation 3, mixing / partial 2) and 0 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL.html · Markdown: https://data.orchid-project.org/systems/AL.md

45 accepted literature values from 18 paper(s) (experimental 13, model 9, DFT 9, unspecified 14); 0 calculated phase diagram(s). 9 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL.json) · [CSV](https://data.orchid-project.org/systems/AL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL.html) · [Markdown](https://data.orchid-project.org/systems/AL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 13 |
| model | 9 |
| DFT | 9 |
| unspecified | 14 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 2 |
| formation | 3 |
| mixing / partial | 2 |
| heat capacity / entropy / enthalpy | 14 |
| activity / EMF / Gibbs energy | 2 |
| crystal structure | 22 |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al system (3)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| A2-Al |  | 60.2 kJ/mol-atom | 0 | model |  |  | [1] Abe 2008 | Table 2, p. 3, row 23; `ORC-KMC3ISMFEM` |  |
| Al |  | 0 kJ/mol-atom | 0 | DFT |  |  | [2] Zhou 2006 | Table 3, p. 6, row 27; `ORC-X2WBMXYDLJ` |  |
| fcc-Al |  | 0 kJ/mol-atom | 0 | DFT |  |  | [3] Zhong 2005 | Table 3, p. 4, row 1; `ORC-UR7LCFHVIW.276c54` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Al system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 933.15 K | 933.15 | α-Al | model | [4] Perron 2016; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 1, p. 3, row 1; `ORC-KGCO74AKCQ` |  |
| Phase transition | 933.47 K | 933.47 | Al(l) = Al(fcc); _Al(l): _ | unspecified | [5] Taylor 1992 | Table 2, p. 7, row 3; `ORC-CYIC7PVBWL` |  |

### Mixing / partial (2)

Table: Mixing / partial, Al system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔH_ | 0 kJ/mol (basis unstated) | 1257 | liquid; _alloy: Al 1_ | experimental | [6] Witusiewicz 2004 | Table 2, p. 4, row 32; `ORC-B4KB6D5M4Q.d212bf` |  |
| Enthalpy of mixing; _printed: ΔH_ | 0 kJ/mol (basis unstated) | 1373 | liquid; _alloy: Al 1_ | experimental | [6] Witusiewicz 2004 | Table 2, p. 4, row 12; `ORC-A457RLOQUZ.937344` |  |

### Heat capacity / entropy / enthalpy (14)

Table: Heat capacity / entropy / enthalpy, Al system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S_Al^liq(Tm) − S_Al^FCC(Tm)_ | 11.334 J/mol (basis unstated)/K |  | liquid | unspecified | [7] He 2021 | Table 1, p. 3, row 10; `ORC-7SRX4WPQIV.be8720` |  |
| Entropy; _printed: S_Al^liq(Tm) − S_Al^FCC(Tm)_ | 11.332 J/mol (basis unstated)/K |  | liquid | experimental | [7] He 2021; _cites Desai 1987_ [doi](https://doi.org/10.1007/bf00503647) | Table 1, p. 3, row 9; `ORC-QDJQTPYND3.644282` |  |
| Entropy; _printed: S_Al^liq(T_m) - S_Al^FCC(T_m)_ | 11.334 J/mol (basis unstated)/K |  | liquid + FCC | unspecified | [7] He 2021 | Table 1, p. 3, row 10; `ORC-7SRX4WPQIV.d2cb02` |  |
| Entropy; _printed: S_Al^liq(T_m) - S_Al^FCC(T_m)_ | 11.332 J/mol (basis unstated)/K |  | liquid + FCC | experimental | [7] He 2021; _cites Desai 1987_ [doi](https://doi.org/10.1007/bf00503647) | Table 1, p. 3, row 9; `ORC-QDJQTPYND3.f15799` |  |
| Entropy; _printed: S_Al^FCC(298) − S_Al^FCC(0)_ | 28.25 J/mol (basis unstated)/K | 298.15 | FCC | unspecified | [7] He 2021 | Table 1, p. 3, row 4; `ORC-275NXIDZEC.65afa3` |  |
| Entropy; _printed: S_Al^FCC(298) - S_Al^FCC(0)_ | 28.25 J/mol (basis unstated)/K | 298.15 | FCC | unspecified | [7] He 2021 | Table 1, p. 3, row 4; `ORC-275NXIDZEC.96108b` |  |
| Entropy; _printed: S_Al^FCC(298) − S_Al^FCC(0)_ | 28.25 J/mol (basis unstated)/K | 298.15 | FCC | experimental | [7] He 2021; _cites Desai 1987_ [doi](https://doi.org/10.1007/bf00503647) | Table 1, p. 3, row 3; `ORC-GR6A3LBK5X.34d12f` |  |
| Entropy; _printed: S_Al^FCC(298) - S_Al^FCC(0)_ | 28.25 J/mol (basis unstated)/K | 298.15 | FCC | experimental | [7] He 2021; _cites Desai 1987_ [doi](https://doi.org/10.1007/bf00503647) | Table 1, p. 3, row 3; `ORC-GR6A3LBK5X.6de0da` |  |
| Heat capacity; _printed: C_P^liq(Tm)_ | 31.757 J/mol (basis unstated)/K |  | liquid | experimental | [7] He 2021; _cites Desai 1987_ [doi](https://doi.org/10.1007/bf00503647) | Table 1, p. 3, row 11; `ORC-L5BLUQ5SRZ.09cc4b` |  |
| Heat capacity; _printed: C_P^liq(T_m)_ | 31.757 J/mol (basis unstated)/K |  | liquid | experimental | [7] He 2021; _cites Desai 1987_ [doi](https://doi.org/10.1007/bf00503647) | Table 1, p. 3, row 11; `ORC-L5BLUQ5SRZ.99c1f7` |  |
| Heat capacity; _printed: C_P^liq(T_m)_ | 31.507 J/mol (basis unstated)/K |  | liquid | unspecified | [7] He 2021 | Table 1, p. 3, row 12; `ORC-OKYWDRN6KZ.7d9cb7` |  |
| Heat capacity; _printed: C_P^liq(Tm)_ | 31.507 J/mol (basis unstated)/K |  | liquid | unspecified | [7] He 2021 | Table 1, p. 3, row 12; `ORC-OKYWDRN6KZ.c90269` |  |
| hm lattice stability; _printed: H_Al^liq(T_m) - H_Al^FCC(T_m)_ | 10.58 kJ/mol (basis unstated) |  | liquid + FCC | unspecified | [7] He 2021 | Table 1, p. 3, row 8; `ORC-KGPZNS677U` |  |
| hm lattice stability; _printed: H_Al^liq(T_m) - H_Al^FCC(T_m)_ | 10.58 kJ/mol (basis unstated) | 933.61 | liquid + FCC | experimental | [7] He 2021; _cites Desai 1987_ [doi](https://doi.org/10.1007/bf00503647) | Table 1, p. 3, row 7; `ORC-XXBZRK4NEQ` |  |

### Activity / EMF / Gibbs energy (2)

Table: Activity / EMF / Gibbs energy, Al system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy; _printed: Gm(ω)-Gm(β)_ | 1606 J/mol | 0 | UNKNOWN; _alloy: Al 1_ | model | [8] Yan 2016 | Table 4, p. 5, row 12; `ORC-7UXUOXRBC6` |  |
| Gibbs energy; _printed: Gm(ω)-Gm(β)_ | 1606 J/mol | 0 | UNKNOWN; _alloy: Al 1_ | DFT | [8] Yan 2016 | Table 4, p. 5, row 11; `ORC-KMIG3J6C56` |  |

### Crystal structure (22)

Table: Crystal structure, Al system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.049 Å | 0 | (Al); _(Al): Al 1_ | DFT | [9] Benhafid 2019 | Table 1, p. 2, row 2; `ORC-GRPKO3U3M4.f27d03` |  |
| Lattice a; _printed: a_ | 4.041 Å |  | A1-Al | experimental | [1] Abe 2008; _cites King 1981_ [doi](https://doi.org/10.1007/bf02868307) | Table 2, p. 3, row 2; `ORC-E4QPNGMG2H.70e321` |  |
| Lattice a; _printed: a_ | 4.056 Å | 0 | A1-Al | model | [1] Abe 2008 | Table 2, p. 3, row 1; `ORC-YMZGKTNVIU.32c0e2` |  |
| Lattice a; _printed: a_ | 3.242 Å | 0 | A2-Al | model | [1] Abe 2008 | Table 2, p. 3, row 23; `ORC-PUHBWVJERU.cc8146` |  |
| Lattice a; _printed: a_ | 4.041 Å | 0 | fcc-Al | DFT | [3] Zhong 2005 | Table 3, p. 4, row 1; `ORC-FQHD3UBOWV.0dd352` |  |
| Lattice a | 4.0414 Å | 298.15 | (Al); _(Al): Al 1_ | unspecified | [10] McAlister 1989 | Table 3, p. 2, row 1; `ORC-2AHICSJKON` |  |
| Lattice a | 4.2906 Å | 298.15 | (Al); _(Al): Al 1_ | experimental | [11] Murray 1987; _cites ref. 1_ | Table 3, p. 6, row 42; `ORC-SQKLNA5IP3.95f123` |  |
| Lattice a | 4.049 Å | 298.15 | (Al); _(Al): Al 1_ | experimental | [9] Benhafid 2019; _cites Otte 1963_ [doi](https://doi.org/10.1063/1.1729148) | Table 1, p. 2, row 1; `ORC-WJOJ2SL2Q2.2e4d6f` |  |
| Lattice a | 4.0497 Å | 298.15 | Al | model | [12] Shao 2004; _cites Villars 1991_ | Table 1, p. 2, row 1; `ORC-KSJXIFYV7S` |  |
| Lattice a | 4.0496 Å | 298.15 | Al; _Al: Al 1_ | unspecified | [13] Murray 1998 | Table 3, p. 1, row 1; `ORC-OYKXDZO6DR` |  |
| Lattice a | 4.0496 Å | 298.15 | Al; _Al: Al 1_ | unspecified | [14] Murray 1998; _cites ref. 2_ | Table 3, p. 5, row 1; `ORC-PUC2XPM7OU` |  |
| Lattice a | 4.0496 Å | 298.15 | Al; _Al: Al 1_ | unspecified | [15] Ltd. 1997 | Table 5, p. 5, row 1; `ORC-UHBZI5I2SH` |  |
| Lattice a | 4.0495 Å | 298.15 | Al | unspecified | [16] Saccone 1998 | Table 1, p. 8, row 15; `ORC-UQLHTIR7CP` |  |
| Lattice a | 4.05 Å | 298.15 | Al | model | [17] Hu 2018; _cites Villars 1997_ | Table 1, p. 2, row 1; `ORC-VFHA3ARVTS.e22eec` |  |
| Lattice a | 4.0496 Å | 298.15 | fcc(Al) | unspecified | [18] Long 2020 | Table 1, p. 2, row 1; `ORC-ZR6WGI326A` |  |
| Lattice b | 4.049 Å | 0 | (Al); _(Al): Al 1_ | DFT | [9] Benhafid 2019 | Table 1, p. 2, row 2; `ORC-GRPKO3U3M4.d056dc` |  |
| Lattice b; _printed: b_ | 4.041 Å | 0 | fcc-Al | DFT | [3] Zhong 2005 | Table 3, p. 4, row 1; `ORC-FQHD3UBOWV.1cc83c` |  |
| Lattice b | 4.049 Å | 298.15 | (Al); _(Al): Al 1_ | experimental | [9] Benhafid 2019; _cites Otte 1963_ [doi](https://doi.org/10.1063/1.1729148) | Table 1, p. 2, row 1; `ORC-WJOJ2SL2Q2.af6be2` |  |
| Lattice b | 4.05 Å | 298.15 | Al | model | [17] Hu 2018; _cites Villars 1997_ | Table 1, p. 2, row 1; `ORC-VFHA3ARVTS.4311cd` |  |
| Lattice c; _printed: c_ | 4.041 Å | 0 | fcc-Al | DFT | [3] Zhong 2005 | Table 3, p. 4, row 1; `ORC-FQHD3UBOWV.405635` |  |
| Lattice c | 4.05 Å | 298.15 | Al | model | [17] Hu 2018; _cites Villars 1997_ | Table 1, p. 2, row 1; `ORC-VFHA3ARVTS.ea2408` |  |
| lattice unspecified axis; _printed: a = b = c_ | 4.041 Å | 0 | fcc-Al | DFT | [3] Zhong 2005 | Table 3, p. 4, row 1; `ORC-FQHD3UBOWV.45b57c` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. T. Abe, C. Kocer, M. Ode, H. Murakami, Y. Yamabe-Mitarai, K. Hashimoto et al., Thermodynamic re-assessment of the Al–Ir system, Calphad 32, 686-692 (2008). [doi:10.1016/j.calphad.2008.09.014](https://doi.org/10.1016/j.calphad.2008.09.014)
2. S.H. Zhou, R.E. Napolitano, Phase equilibria and thermodynamic limits for partitionless crystallization in the Al–La binary system, Acta Materialia 54, 831-840 (2006). [doi:10.1016/j.actamat.2005.10.013](https://doi.org/10.1016/j.actamat.2005.10.013)
3. Yu Zhong, Mei Yang, Zi-Kui Liu, Contribution of first-principles energetics to Al–Mg thermodynamic modeling, Calphad 29, 303-311 (2005). [doi:10.1016/j.calphad.2005.08.004](https://doi.org/10.1016/j.calphad.2005.08.004)
4. A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016). [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012)
5. J R Taylor, A T Dinsdale, M Hilleit, M Selleby, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Al-O System, Calphad 16, 173-179 (1992). [doi:10.1016/0364-5916(92)90005-i](https://doi.org/10.1016/0364-5916%2892%2990005-i)
6. V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004). [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126)
7. Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021). [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250)
8. Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016). [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251)
9. R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019). [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2)
10. A. J. McAlister, The Al-Tl (Aluminum-Thallium) system, Bulletin of Alloy Phase Diagrams 10, 112-114 (1989). [doi:10.1007/bf02881414](https://doi.org/10.1007/bf02881414)
11. J. L. Murray, H. Okamoto, T. B. Massalski, The Al−Au (Aluminum-gold) system, Bulletin of Alloy Phase Diagrams 8, 20-30 (1987). [doi:10.1007/bf02868887](https://doi.org/10.1007/bf02868887)
12. G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004). [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011)
13. J. L. Murray, The Al-Sc (aluminum-scandium) system, JPE 19, 380-384 (1998). [doi:10.1361/105497198770342120](https://doi.org/10.1361/105497198770342120)
14. J. L. Murray, The Al-Cr (aluminum-chromium) system, JPE 19, 367-375 (1998). [doi:10.1007/bf02735058](https://doi.org/10.1007/bf02735058)
15. Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997). [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1)
16. A. Saccone, G. Cacciamani, D. Macciò, G. Borzone, R. Ferro, Contribution to the study of the alloys and intermetallic compounds of aluminium with the rare-earth metals, Intermetallics 6, 201-215 (1998). [doi:10.1016/s0966-9795(97)00066-6](https://doi.org/10.1016/s0966-9795%2897%2900066-6)
17. J.L. Hu, H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic study of the Al-Sc-Y system, Thermochimica Acta 661, 147-159 (2018). [doi:10.1016/j.tca.2018.01.018](https://doi.org/10.1016/j.tca.2018.01.018)
18. Zhaohui Long, Dongyu Cui, Hongxing Hu, Zhi Li, Fucheng Yin, Touwen Fan, Thermodynamic Modeling of the Al-Li-Zr Ternary System, J. Phase Equilib. Diffus. 41, 623-641 (2020). [doi:10.1007/s11669-020-00827-z](https://doi.org/10.1007/s11669-020-00827-z)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
