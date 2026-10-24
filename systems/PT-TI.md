# Pt–Ti system

> Pt–Ti system: 38 accepted literature values (invariant reaction 31, phase transition 6, activity / EMF / Gibbs energy 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PT-TI.html · Markdown: https://data.orchid-project.org/systems/PT-TI.md

38 accepted literature values from 1 paper(s) (experimental 25, model 13); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PT-TI.json) · [CSV](https://data.orchid-project.org/systems/PT-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PT-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PT-TI/PtTi-08Li.json) · [phases (10)](https://data.orchid-project.org/phases/pages/PT-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PT-TI.html) · [Markdown](https://data.orchid-project.org/systems/PT-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 25 |
| model | 13 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 31 |
| phase transition | 6 |
| activity / EMF / Gibbs energy | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PtTi-08Li.tdb | M. Li, W. Han, C. Li, J. Alloys Compd., 461, 189-94(2008). [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) | `225d207ff370fad5f2424732156ead08728f17d5382c43193d57fe77c3031724` | [viewer](https://orchid-project.org/phase-diagrams/#PT-TI/PtTi-08Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PtTi-08Li.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PtTi-08Li.tdb | 2073.38 | LIQUID (x(Ti) 0.11551) + FCC_A1 (x(Ti) 0.11595) + PT3TI_D024 (x(Ti) 0.21782) |
| PtTi-08Li.tdb | 2045.06 | PT3TI_D024 (x(Ti) 0.24987) + LIQUID (x(Ti) 0.39095) + PTTI_B2 (x(Ti) 0.43883) |
| PtTi-08Li.tdb | 1698.47 | PTTI_B2 (x(Ti) 0.51961) + LIQUID (x(Ti) 0.66898) + PTTI3_A15 (x(Ti) 0.73275) |
| PtTi-08Li.tdb | 1583.06 | PTTI3_A15 (x(Ti) 0.7638) + LIQUID (x(Ti) 0.86609) + BCC_A2 (x(Ti) 0.91726) |
| PtTi-08Li.tdb | 1478.17 | PTTI_B2 (x(Ti) 0.517) + PT3TI4 (x(Ti) 0.57143) + PTTI3_A15 (x(Ti) 0.73616) |
| PtTi-08Li.tdb | 1353.05 | FCC_A1 (x(Ti) 0.01568) + PT8TI (x(Ti) 0.11111) + PT3TI_D024 (x(Ti) 0.20221) |
| PtTi-08Li.tdb | 1353.05 | FCC_A1 (x(Ti) 0.01567) + PT8TI (x(Ti) 0.11111) + PT3TI_D024 (x(Ti) 0.20222) |
| PtTi-08Li.tdb | 1312.19 | PTTI_B19 (x(Ti) 0.50116) + PTTI_B2 (x(Ti) 0.50224) + PT3TI4 (x(Ti) 0.57143) |
| PtTi-08Li.tdb | 1312.19 | PTTI_B19 (x(Ti) 0.50121) + PTTI_B2 (x(Ti) 0.50231) + PT3TI4 (x(Ti) 0.57143) |
| PtTi-08Li.tdb | 1306.87 | PT3TI_D024 (x(Ti) 0.25) + PTTI_B2 (x(Ti) 0.47503) + PTTI_B19 (x(Ti) 0.47823) |
| PtTi-08Li.tdb | 1112.87 | PTTI3_A15 (x(Ti) 0.78201) + BCC_A2 (x(Ti) 0.96895) + HCP_A3 (x(Ti) 0.97816) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PT/PT-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PT/PT-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pt–Ti system (31)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2224 | congruent melting: L → γ | L: Pt 0.754; γ: Pt 0.754 | model | [1] Li 2008 | Table 1, p. 2, row 14; `ORC-YTYHP2TMGA` |  |
| 2223 | congruent melting: L → γ | L: Pt 0.75; γ: Pt 0.75 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 13; `ORC-3JTYOO4SYG` |  |
| 2106 | congruent melting: L → βTiPt | L: Pt 0.522; βTiPt: Pt 0.522 | model | [1] Li 2008 | Table 1, p. 2, row 10; `ORC-RTDJ63KUN2` |  |
| 2103 | congruent melting: L → βTiPt | L: Pt 0.5; βTiPt: Pt 0.5 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 9; `ORC-TH522HMOQL` |  |
| 2073 | peritectic: L + γ → Fcc | L: Pt 0.885; γ: Pt 0.782; Fcc: Pt 0.884 | model | [1] Li 2008 | Table 1, p. 2, row 16; `ORC-5ANFA6LTE3` |  |
| 2073 | peritectic: L + γ → Fcc | L: Pt 0.9; γ: Pt 0.8; Fcc: Pt 0.88 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 15; `ORC-R3O5U22RBX` |  |
| 2053 | eutectic: L → βTiPt + γ | L: Pt 0.58; βTiPt: Pt 0.526; γ: Pt 0.75 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 11; `ORC-JAKMSHM377` |  |
| 2053 | eutectic |  | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 1; `ORC-MEMNAUK7DD.c92389` | “Nishimura and Hiramatsu \[6\] also reported three eutectic reactions: the first forming bcc and Ti3 Pt at ∼15 at.% Pt and 1588 K; the second forming Ti3 Pt and TiPt at ∼34 at.% Pt and 1593 K, and the third producing TiPt and TiPt3 at ∼58 at.% Pt and 2053 K.” |
| 2045 | eutectic: L → βTiPt + γ | L: Pt 0.613; βTiPt: Pt 0.574; γ: Pt 0.75 | model | [1] Li 2008 | Table 1, p. 2, row 12; `ORC-3DYOEKKFDL` |  |
| 1773 | congruent melting: L → Ti3Pt | L: Pt 0.25; Ti3Pt: Pt 0.25 | experimental | [1] Li 2008; _cites Biggs 2004_ [doi](https://doi.org/10.1016/j.jallcom.2003.12.001) | Table 1, p. 2, row 4; `ORC-RNT7HWZ7XP` |  |
| 1771 | congruent melting: L → Ti3Pt | L: Pt 0.253; Ti3Pt: Pt 0.253 | model | [1] Li 2008 | Table 1, p. 2, row 5; `ORC-GUJNWAQXLZ` |  |
| 1698 | eutectic: L → βTiPt + Ti3Pt | L: Pt 0.331; βTiPt: Pt 0.481; Ti3Pt: Pt 0.267 | model | [1] Li 2008 | Table 1, p. 2, row 8; `ORC-AF3PXXO3AE` |  |
| 1697 | eutectic: L → βTiPt + Ti3Pt | L: Pt 0.34; βTiPt: Pt 0.45; Ti3Pt: Pt 0.28 | experimental | [1] Li 2008; _cites Biggs 2004_ [doi](https://doi.org/10.1016/j.jallcom.2003.12.001) | Table 1, p. 2, row 7; `ORC-MO5PXWOU2Q` |  |
| 1643 | congruent melting: L → Ti3Pt | L: Pt 0.25; Ti3Pt: Pt 0.25 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 3; `ORC-7KW2N53V2L` |  |
| 1593 | eutectic |  | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 1; `ORC-MEMNAUK7DD.464dbf` | “Nishimura and Hiramatsu \[6\] also reported three eutectic reactions: the first forming bcc and Ti3 Pt at ∼15 at.% Pt and 1588 K; the second forming Ti3 Pt and TiPt at ∼34 at.% Pt and 1593 K, and the third producing TiPt and TiPt3 at ∼58 at.% Pt and 2053 K.” |
| 1593 | eutectic: L → βTiPt + Ti3Pt | L: Pt 0.34; βTiPt: Pt 0.5; Ti3Pt: Pt 0.25 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 6; `ORC-UR3XSNOLYL` |  |
| 1588 | eutectic |  | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 1; `ORC-MEMNAUK7DD.d6a9e6` | “Nishimura and Hiramatsu \[6\] also reported three eutectic reactions: the first forming bcc and Ti3 Pt at ∼15 at.% Pt and 1588 K; the second forming Ti3 Pt and TiPt at ∼34 at.% Pt and 1593 K, and the third producing TiPt and TiPt3 at ∼58 at.% Pt and 2053 K.” |
| 1583 | eutectic: L → Bcc + Ti3Pt | L: Pt 0.16; Bcc: Pt 0.094; Ti3Pt: Pt 0.25 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 1; `ORC-HQPHKVARMS` |  |
| 1583 | eutectic: L → Bcc + Ti3Pt | L: Pt 0.134; Bcc: Pt 0.083; Ti3Pt: Pt 0.236 | model | [1] Li 2008 | Table 1, p. 2, row 2; `ORC-X6GAT7ARXO` |  |
| 1478 | peritectoid: Ti3Pt + βTiPt → Ti4Pt3 | Ti3Pt: Pt 0.27; βTiPt: Pt 0.45; Ti4Pt3: Pt 0.428 | experimental | [1] Li 2008; _cites Biggs 2004_ [doi](https://doi.org/10.1016/j.jallcom.2003.12.001) | Table 1, p. 2, row 19; `ORC-K5HWH472BM` |  |
| 1478 | peritectoid: Ti3Pt + βTiPt → Ti4Pt3 | Ti3Pt: Pt 0.264; βTiPt: Pt 0.483; Ti4Pt3: Pt 0.428 | model | [1] Li 2008 | Table 1, p. 2, row 20; `ORC-TAPCNLLA5D` |  |
| 1353 | peritectoid: γ + Fcc → TiPt8 | γ: Pt 0.8; Fcc: Pt 0.9; TiPt8: Pt 0.889 | experimental | [1] Li 2008; _cites Meschter 1976_ [doi](https://doi.org/10.1007/bf02644471) | Table 1, p. 2, row 27; `ORC-KXJ2ECLRQX` |  |
| 1353 | peritectoid: γ + Fcc → TiPt8 | γ: Pt 0.798; Fcc: Pt 0.984; TiPt8: Pt 0.889 | model | [1] Li 2008 | Table 1, p. 2, row 28; `ORC-YN6PJPEO5U` |  |
| 1313 | congruent transformation: βTiPt → αTiPt | βTiPt: Pt 0.502; αTiPt: Pt 0.502 | model | [1] Li 2008 | Table 1, p. 2, row 24; `ORC-62NEH4N7K4` |  |
| 1313 | congruent transformation: βTiPt → αTiPt | βTiPt: Pt 0.5; αTiPt: Pt 0.5 | experimental | [1] Li 2008; _cites Murray 1982_ [doi](https://doi.org/10.1007/bf02869304) | Table 1, p. 2, row 23; `ORC-LZYEQ27FPD` |  |
| 1312 | peritectoid: Ti4Pt3 + βTiPt → αTiPt | Ti4Pt3: Pt 0.428; βTiPt: Pt 0.497; αTiPt: Pt 0.499 | model | [1] Li 2008 | Table 1, p. 2, row 26; `ORC-WEBEJ66T55` |  |
| 1308 | peritectoid: Ti3Pt + βTiPt → αTiPt | Ti3Pt: Pt 0.28; βTiPt: Pt 0.46; αTiPt: Pt 0.46 | experimental | [1] Li 2008; _cites Murray 1982_ [doi](https://doi.org/10.1007/bf02869304) | Table 1, p. 2, row 25; `ORC-337LEGG3IW` |  |
| 1297 | peritectoid: γ + βTiPt → αTiPt | γ: Pt 0.75; βTiPt: Pt 0.522; αTiPt: Pt 0.525 | model | [1] Li 2008 | Table 1, p. 2, row 22; `ORC-MUMUEFUL2J` |  |
| 1273 | peritectoid: TiPt3- + βTiPt → αTiPt | TiPt3-: Pt 0.73; βTiPt: Pt 0.53; αTiPt: Pt 0.53 | experimental | [1] Li 2008; _cites Murray 1982_ [doi](https://doi.org/10.1007/bf02869304) | Table 1, p. 2, row 21; `ORC-CNX5ZRB2IJ` |  |
| 1113 | eutectoid: Bcc → Hcp + Ti3Pt | Bcc: Pt 0.03; Hcp: Pt 0.015; Ti3Pt: Pt 0.25 | experimental | [1] Li 2008; _cites Nishimura 1957_ | Table 1, p. 2, row 17; `ORC-E36XERUP3M` |  |
| 1113 | eutectoid: Bcc → Hcp + Ti3Pt | Bcc: Pt 0.031; Hcp: Pt 0.022; Ti3Pt: Pt 0.22 | model | [1] Li 2008 | Table 1, p. 2, row 18; `ORC-YYLJKDBDEX` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Pt–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1113 K | 1113 | (␤Ti) = (␣Ti) + Ti3Pt | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 2; `ORC-XY22RCB6U3` | “The eutectiod reaction of (␣Ti), (␤Ti), and Ti3 Pt at 1113 K was proposed by Nishimura and Hiramatsu \[6\].” |
| Phase transition | 1643 K | 1643 | congruent transformation | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 1; `ORC-VMOLKSAV3V.35ad78` | “Nishimura and Hiramatsu \[6\] found three intermetallic phases: Ti3 Pt, TiPt and TiPt3 , which they reported as melting congruently at the respective temperatures of 1643, 2103 and 2223 K.” |
| Phase transition | 1773 K | 1773 |  | experimental | [1] Li 2008; _cites Biggs 2004_ [doi](https://doi.org/10.1016/j.jallcom.2003.12.001) | p. 1; `ORC-WLXF2KU6N6` | “The intermetallic phase Ti3 Pt was found to melt at 1773 K \[8\], not 1643 K as previously reported by Nishimura and Hiramatsu \[6\].” |
| Phase transition | 1993 K | 1993 |  | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 5; `ORC-BCKF4JAUD2` | “Nishimura and Hiramatsu \[6\] determined the melting point of bcc (Ti) at 1993 K, but the true melting point at 1941 \[7\].” |
| Phase transition | 2103 K | 2103 | congruent transformation | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 1; `ORC-VMOLKSAV3V.9ea414` | “Nishimura and Hiramatsu \[6\] found three intermetallic phases: Ti3 Pt, TiPt and TiPt3 , which they reported as melting congruently at the respective temperatures of 1643, 2103 and 2223 K.” |
| Phase transition | 2223 K | 2223 | congruent transformation | experimental | [1] Li 2008; _cites Nishimura 1957_ | p. 1; `ORC-VMOLKSAV3V.05e5f6` | “Nishimura and Hiramatsu \[6\] found three intermetallic phases: Ti3 Pt, TiPt and TiPt3 , which they reported as melting congruently at the respective temperatures of 1643, 2103 and 2223 K.” |

### Activity / EMF / Gibbs energy (1)

Table: Activity / EMF / Gibbs energy, Pt–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy; _printed: standard Gibbs energy of formation_ | -282.57 unspecified ± 4 | 1573 |  | experimental | [1] Li 2008; _cites Jacob 2000_ [doi](https://doi.org/10.1179/026708300101507947) | p. 2; `ORC-5QG5MR7WNR` | “And the standard Gibbs energy of formation of TiPt3 is -282.57 ± 4 kJ/mol at 1573 K \[18\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008). [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
