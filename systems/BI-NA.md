# Bi–Na system

> Bi–Na system: 45 accepted literature values (phase transition 19, formation 13, invariant reaction 12, phase equilibrium 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-NA.html · Markdown: https://data.orchid-project.org/systems/BI-NA.md

45 accepted literature values from 1 paper(s) (experimental 36, model 9); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-NA.json) · [CSV](https://data.orchid-project.org/systems/BI-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-NA/BiNa-13Liu.json) · [phases (7)](https://data.orchid-project.org/phases/pages/BI-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-NA.html) · [Markdown](https://data.orchid-project.org/systems/BI-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 36 |
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 19 |
| phase equilibrium | 1 |
| formation | 13 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiNa-13Liu.tdb | Y. Liu, Z. Kang, J. Wang, Thermochim. Acta, 558, 53-60(2013). [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) | `8c20e65805717473a5c270c44e46b8eccc86c838e41714931b086efad6c92640` | [viewer](https://orchid-project.org/phase-diagrams/#BI-NA/BiNa-13Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiNa-13Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiNa-13Liu.tdb | 717.64 | LIQUID (x(Na) 0.4673) + BINA_L10 (x(Na) 0.5) + BINA3_D018 (x(Na) 0.75) |
| BiNa-13Liu.tdb | 490.91 | RHOMBOHEDRAL_A7 (x(Na) 0) + LIQUID (x(Na) 0.19993) + BINA_L10 (x(Na) 0.5) |
| BiNa-13Liu.tdb | 370.87 | BINA3_D018 (x(Na) 0.75) + BCC_A2 (x(Na) 1) + LIQUID (x(Na) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Na system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 719 | liq + BiNa3 -> BiNa | BiNa3: Na 0.75; BiNa: Na 0.5 | experimental | [1] Liu 2013; _cites Klebanov 1985_ | Table 6, p. 7, row 9; `ORC-B6VTPGPUDT` |  |
| 718 | liq + BiNa3 -> BiNa | liq: Na 0.46; BiNa3: Na 0.75; BiNa: Na 0.5 | model | [1] Liu 2013 | Table 6, p. 7, row 5; `ORC-IJ2MLIL7GC` |  |
| 718 | liq + BiNa3 -> BiNa | BiNa3: Na 0.75; BiNa: Na 0.5 | experimental | [1] Liu 2013; _cites Vournasos 1944_ | Table 6, p. 7, row 8; `ORC-KGYVLGKMWM` |  |
| 718 | liq + BiNa3 -> BiNa | liq: Na 0.469; BiNa3: Na 0.75; BiNa: Na 0.5 | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 6, p. 7, row 6; `ORC-VOW35PW5PX` |  |
| 717 | liq + BiNa3 -> BiNa | liq: Na 0.48; BiNa3: Na 0.75; BiNa: Na 0.5 | experimental | [1] Liu 2013; _cites Johnson 1970_ [doi](https://doi.org/10.1016/0022-5088%2870%2990008-1) | Table 6, p. 7, row 7; `ORC-RANBVQKT5J` |  |
| 491 | eutectic: liq -> Bi + BiNa | Bi: Na 0; BiNa: Na 0.5 | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 6, p. 7, row 2; `ORC-GNV72U5O3Z` |  |
| 490.9 | eutectic: liq -> Bi + BiNa | liq: Na 0.2; Bi: Na 0; BiNa: Na 0.5 | model | [1] Liu 2013 | Table 6, p. 7, row 1; `ORC-GNEHTRTSEF` |  |
| 489 | eutectic: liq -> Bi + BiNa | Bi: Na 0; BiNa: Na 0.5 | experimental | [1] Liu 2013; _cites Johnson 1970_ [doi](https://doi.org/10.1016/0022-5088%2870%2990008-1) | Table 6, p. 7, row 3; `ORC-CFP2OWKT55` |  |
| 487 | eutectic: liq -> Bi + BiNa | Bi: Na 0; BiNa: Na 0.5 | experimental | [1] Liu 2013; _cites Vournasos 1944_ | Table 6, p. 7, row 4; `ORC-NQJE7RHRPU` |  |
| 370.9 | eutectic: liq -> BiNa3 + Na | liq: Na 0.999; BiNa3: Na 0.75 | model | [1] Liu 2013 | Table 6, p. 7, row 17; `ORC-6FQWRPDTAP` |  |
| 370.7 | eutectic: liq -> BiNa3 + Na | BiNa3: Na 0.75 | experimental | [1] Liu 2013; _cites Johnson 1970_ [doi](https://doi.org/10.1016/0022-5088%2870%2990008-1) | Table 6, p. 7, row 19; `ORC-6ZY7QZMGSD` |  |
| 370 | eutectic: liq -> BiNa3 + Na | BiNa3: Na 0.75 | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 6, p. 7, row 18; `ORC-NTFMYECH55` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Bi–Na system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| BiNa |  | -78.3 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2013; _cites Seith 1937_ | p. 2; `ORC-AFWGZ62NH7` | “The enthalpies of formation of BiNa at 298 K were reported to be -78.3 kJ/mol, relative to pure liquids, from direct reaction calorimetry by Seith and Kubaschewski \[43\] and Kubaschewski and Catterall \[44\].” |
| BiNa(s) | [BiNa](https://data.orchid-project.org/compounds/BiNa.html) | -42.45 kJ/mol-atom |  | model | -28.197 (mp-aaaabhxs) | -35.373 (oqmd-28744) | [1] Liu 2013 | Table 5, p. 7, row 1; `ORC-7JGVTMWUUH.f4f997` |  |
| BiNa(s) | [BiNa](https://data.orchid-project.org/compounds/BiNa.html) | -41.6 kJ/mol-atom | 298.15 | experimental | -28.197 (mp-aaaabhxs) | -35.373 (oqmd-28744) | [1] Liu 2013; _cites Iwase 1984_ | Table 5, p. 7, row 3; `ORC-UEPHMZJM2I.1d2afe` |  |
| BiNa(s) | [BiNa](https://data.orchid-project.org/compounds/BiNa.html) | -39.75 kJ/mol-atom | 298.15 | experimental | -28.197 (mp-aaaabhxs) | -35.373 (oqmd-28744) | [1] Liu 2013; _cites Foster 1967_ | Table 5, p. 7, row 2; `ORC-AYCTBZFQZB.949bd5` |  |
| BiNa(s) | [BiNa](https://data.orchid-project.org/compounds/BiNa.html) | -39.15 kJ/mol-atom | 298.15 | experimental | -28.197 (mp-aaaabhxs) | -35.373 (oqmd-28744) | [1] Liu 2013; _cites Seith 1937_ | Table 5, p. 7, row 4; `ORC-QYSC64K2CE` |  |
| BiNa3(s) | [BiNa3](https://data.orchid-project.org/compounds/BiNa3.html) | -57.325 kJ/mol-atom |  | model | -35.636 (mp-aaaabpes) | -45.638 (oqmd-2053479) | [1] Liu 2013 | Table 5, p. 7, row 5; `ORC-QKX6N5FT3Q.529b1e` |  |
| BiNa3(s) | [BiNa3](https://data.orchid-project.org/compounds/BiNa3.html) | -56 kJ/mol-atom | 298.15 | experimental | -35.636 (mp-aaaabpes) | -45.638 (oqmd-2053479) | [1] Liu 2013; _cites Foster 1967_ | Table 5, p. 7, row 6; `ORC-L4NZDUJQDH.f56d78` |  |
| BiNa3(s) | [BiNa3](https://data.orchid-project.org/compounds/BiNa3.html) | -52.5 kJ/mol-atom | 298.15 | experimental | -35.636 (mp-aaaabpes) | -45.638 (oqmd-2053479) | [1] Liu 2013; _cites Seith 1937_ | Table 5, p. 7, row 7; `ORC-KWFFGC4AC3` |  |

## Other properties

### Phase transition (19)

Table: Phase transition, Bi–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 717 K | 717 | BiNa | experimental | [1] Liu 2013; _cites Zintl 1932_ [doi](https://doi.org/10.1515/zpch-1932-1615) | p. 2; `ORC-KSWKF56FTN` | “Zintl and Dullenkopf \[26\] studied the BiNa solid phase with XRD (X-ray diffraction), the results of which showed that this compound melts incongruently at 717 K.” |
| Phase transition | 717 K | 717 | BiNa + BiNa3 + liquid | experimental | [1] Liu 2013 | p. 2; `ORC-OGZHQRPYYH` | “BiNa melts incongruently, with the formation of Bi-Na melts and BiNa3 when the temperature is raised above 717 K.” |
| Phase transition | 718 K | 718 | BiNa | experimental | [1] Liu 2013; _cites Vournasos 1944_ | p. 2; `ORC-VKM5VG5DH6.059cab` | “Such an invariant reaction was reported to be around 46.9 at.% Na at 718 K by Mathewson \[19\], at 718 K by Vournasos \[27,28\], and at 719 K by Klebanov et al. \[29\].” |
| Phase transition | 719 K | 719 | BiNa | experimental | [1] Liu 2013; _cites Klebanov 1985_ | p. 2; `ORC-VKM5VG5DH6.43063e` | “Such an invariant reaction was reported to be around 46.9 at.% Na at 718 K by Mathewson \[19\], at 718 K by Vournasos \[27,28\], and at 719 K by Klebanov et al. \[29\].” |
| Phase transition | 993 K | 993 | congruent transformation | experimental | [1] Liu 2013; _cites Kurnakow 1900_ [doi](https://doi.org/10.1002/zaac.19000230136) | p. 2; `ORC-LUFS5WX2Z5.2c9063` | “The BiNa3 solid phase was reported to melt congruently, the melting temperature of which was characterized by thermal analysis at 993 K by Kurnakow \[18\], 1048 K by Mathewson \[19\], 1121 K by Johnson and Fischer \[23\] and 1049 K by Vournasos \[27,28\].” |
| Phase transition | 993 K | 993 | liq -> BiNa3; _liq: Na 0.75; BiNa3: Na 0.75_ | experimental | [1] Liu 2013; _cites Kurnakow 1900_ [doi](https://doi.org/10.1002/zaac.19000230136) | Table 6, p. 7, row 11; `ORC-MDIWLN43G2` |  |
| Phase transition | 1048 K | 1048 | congruent transformation | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | p. 2; `ORC-LUFS5WX2Z5.81c5ef` | “The BiNa3 solid phase was reported to melt congruently, the melting temperature of which was characterized by thermal analysis at 993 K by Kurnakow \[18\], 1048 K by Mathewson \[19\], 1121 K by Johnson and Fischer \[23\] and 1049 K by Vournasos \[27,28\].” |
| Phase transition | 1048 K | 1048 | liq -> BiNa3; _liq: Na 0.75; BiNa3: Na 0.75_ | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 6, p. 7, row 12; `ORC-5I3UNRRYGL` |  |
| Phase transition | 1049 K | 1049 | congruent transformation | experimental | [1] Liu 2013; _cites Vournasos 1944_ | p. 2; `ORC-LUFS5WX2Z5.9d52d4` | “The BiNa3 solid phase was reported to melt congruently, the melting temperature of which was characterized by thermal analysis at 993 K by Kurnakow \[18\], 1048 K by Mathewson \[19\], 1121 K by Johnson and Fischer \[23\] and 1049 K by Vournasos \[27,28\].” |
| Phase transition | 1049 K | 1049 | liq -> BiNa3; _liq: Na 0.75; BiNa3: Na 0.75_ | experimental | [1] Liu 2013; _cites Vournasos 1944_ | Table 6, p. 7, row 15; `ORC-QIOIRUJC66` |  |
| Phase transition | 1115 K | 1115 | BiNa3 | experimental | [1] Liu 2013; _cites Fischer 1967_ [doi](https://doi.org/10.1021/j100864a043) | p. 2; `ORC-ZTC7FPCBH4.03c726` | “Other reports include 1115 K from change of slope in the vapor pressure against temperature relations by Fischer et al. \[20\], 1121 K by electrochemical measurements of Klebanov et al. \[29\], and 1123.4 K identified by enthalpy measurements by Frederickson et al. \[30\].” |
| Phase transition | 1118 K | 1118 | congruent melting | model | [1] Liu 2013; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645966) | p. 2; `ORC-RVWNDYOF52` | “According to the assessed phase diagram, there exist two binary intermetallic phases, i.e. BiNa3 and BiNa. BiNa3 melts congruently around 1118 K, and the liquidus around BiNa3 shows a certain degree of steepness, indicating the presence of short-range ordering for the melts around such a composition.” |
| Phase transition | 1118 K | 1118 | liq -> BiNa3; _liq: Na 0.75; BiNa3: Na 0.75_ | model | [1] Liu 2013 | Table 6, p. 7, row 10; `ORC-JXL7OPQDZG` |  |
| Phase transition | 1121 K | 1121 | BiNa3 | experimental | [1] Liu 2013; _cites Klebanov 1985_ | p. 2; `ORC-ZTC7FPCBH4.54241e` | “Other reports include 1115 K from change of slope in the vapor pressure against temperature relations by Fischer et al. \[20\], 1121 K by electrochemical measurements of Klebanov et al. \[29\], and 1123.4 K identified by enthalpy measurements by Frederickson et al. \[30\].” |
| Phase transition | 1121 K | 1121 | congruent transformation | experimental | [1] Liu 2013; _cites Johnson 1970_ [doi](https://doi.org/10.1016/0022-5088%2870%2990008-1) | p. 2; `ORC-LUFS5WX2Z5.c5490d` | “The BiNa3 solid phase was reported to melt congruently, the melting temperature of which was characterized by thermal analysis at 993 K by Kurnakow \[18\], 1048 K by Mathewson \[19\], 1121 K by Johnson and Fischer \[23\] and 1049 K by Vournasos \[27,28\].” |
| Phase transition | 1121 K | 1121 | liq -> BiNa3; _liq: Na 0.75; BiNa3: Na 0.75_ | experimental | [1] Liu 2013; _cites Egan 1985_ | Table 6, p. 7, row 14; `ORC-3PNQKBT7F3` |  |
| Phase transition | 1121 K | 1121 | liq -> BiNa3; _liq: Na 0.75; BiNa3: Na 0.75_ | experimental | [1] Liu 2013; _cites Johnson 1970_ [doi](https://doi.org/10.1016/0022-5088%2870%2990008-1) | Table 6, p. 7, row 13; `ORC-5RI3HOD5YM` |  |
| Phase transition | 1123.4 K | 1123.4 | BiNa3 | experimental | [1] Liu 2013; _cites Frederickson 1970_ | p. 2; `ORC-ZTC7FPCBH4.ab9b84` | “Other reports include 1115 K from change of slope in the vapor pressure against temperature relations by Fischer et al. \[20\], 1121 K by electrochemical measurements of Klebanov et al. \[29\], and 1123.4 K identified by enthalpy measurements by Frederickson et al. \[30\].” |
| Phase transition | 1123.4 K | 1123.4 | liq -> BiNa3; _liq: Na 0.75; BiNa3: Na 0.75_ | experimental | [1] Liu 2013; _cites Frederickson 1970_ | Table 6, p. 7, row 16; `ORC-QAETT4RSNQ` |  |

### Phase equilibrium (1)

Table: Phase equilibrium, Bi–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  | 718 | BiNa; _alloy: Na 0.469_ | experimental | [1] Liu 2013; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | p. 2; `ORC-NBZOGLMS5B` | “Such an invariant reaction was reported to be around 46.9 at.% Na at 718 K by Mathewson \[19\], at 718 K by Vournasos \[27,28\], and at 719 K by Klebanov et al. \[29\].” |

### Formation (5)

Table: Formation, Bi–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔfS_ | -14.7 J/mol-atom/K |  | BiNa(s); _alloy: Na 0.5_ | model | [1] Liu 2013 | Table 5, p. 7, row 1; `ORC-7JGVTMWUUH.79b0f6` |  |
| Entropy of formation; _printed: ΔfS_ | -19.725 J/mol-atom/K |  | BiNa3(s); _alloy: Na 0.75_ | model | [1] Liu 2013 | Table 5, p. 7, row 5; `ORC-QKX6N5FT3Q.3f6aa9` |  |
| Entropy of formation; _printed: ΔfS_ | -13.8 J/mol-atom/K | 298.15 | BiNa(s); _alloy: Na 0.5_ | experimental | [1] Liu 2013; _cites Foster 1967_ | Table 5, p. 7, row 2; `ORC-AYCTBZFQZB.ba63d7` |  |
| Entropy of formation; _printed: ΔfS_ | -15.45 J/mol-atom/K | 298.15 | BiNa(s); _alloy: Na 0.5_ | experimental | [1] Liu 2013; _cites Iwase 1984_ | Table 5, p. 7, row 3; `ORC-UEPHMZJM2I.f706c7` |  |
| Entropy of formation; _printed: ΔfS_ | -24.5 J/mol-atom/K | 298.15 | BiNa3(s); _alloy: Na 0.75_ | experimental | [1] Liu 2013; _cites Foster 1967_ | Table 5, p. 7, row 6; `ORC-L4NZDUJQDH.ce5935` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013). [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
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
