# In–Mn system

> In–Mn system: 60 accepted literature values (phase transition 28, invariant reaction 17, phase equilibrium 14, formation 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-MN.html · Markdown: https://data.orchid-project.org/systems/IN-MN.md

60 accepted literature values from 1 paper(s) (experimental 54, model 6); 1 calculated phase diagram(s). 16 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-MN.json) · [CSV](https://data.orchid-project.org/systems/IN-MN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-MN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-MN/InMn-15Wan.json) · [phases (8)](https://data.orchid-project.org/phases/pages/IN-MN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/IN-MN.html) · [Markdown](https://data.orchid-project.org/systems/IN-MN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 54 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 28 |
| phase equilibrium | 14 |
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InMn-15Wan.tdb | L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao, H.Y. Zhou, Thermochim. Acta, 607, 74-81(2015). [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) | `213bd22e68c918e1d82b67797f37b7f51e43957bb8eeb8ab117064c191d6fdcf` | [viewer](https://orchid-project.org/phase-diagrams/#IN-MN/InMn-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InMn-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InMn-15Wan.tdb | 1466.33 | LIQUID (x(Mn) 0.95099) + FCC_A1 (x(Mn) 0.98292) + BCC_A2 (x(Mn) 0.98942) |
| InMn-15Wan.tdb | 1293.26 | LIQUID (x(Mn) 0.69897) + FCC_A1 (x(Mn) 0.92218) + CUB_A13 (x(Mn) 0.93401) |
| InMn-15Wan.tdb | 1181.8 | LIQUID (x(Mn) 0.51841) + INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.91042) |
| InMn-15Wan.tdb | 1181.8 | LIQUID (x(Mn) 0.51859) + INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.91043) |
| InMn-15Wan.tdb | 908 | INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.96292) + CBCC_A12 (x(Mn) 0.98687) |
| InMn-15Wan.tdb | 908 | INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.96297) + CBCC_A12 (x(Mn) 0.98688) |
| InMn-15Wan.tdb | 429.6 | TETRAGONAL_A6 (x(Mn) 0) + LIQUID (x(Mn) 3.200e-4) + INMN3_D83 (x(Mn) 0.75) |
| InMn-15Wan.tdb | 429.6 | TETRAGONAL_A6 (x(Mn) 0) + LIQUID (x(Mn) 3.200e-4) + INMN3_D83 (x(Mn) 0.75) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-MN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-MN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the In–Mn system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1485 | peritectic: L+δ-Mn ↔ γ-Mn |  | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 2; `ORC-XWFEC3C6DN` |  |
| 1466.3 | peritectic: L+δ-Mn ↔ γ-Mn | L: Mn 0.951; δ-Mn: Mn 0.9894; γ-Mn: Mn 0.9829 | model | [1] Wang 2015 | Table 3, p. 5, row 3; `ORC-MLSHCWK5GX` |  |
| 1445 | peritectic: L+δ-Mn ↔ γ-Mn | L: Mn 0.95 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 1; `ORC-BMEFFYVQFM` |  |
| 1293.2 | metatectic/catatectic: γ-Mn ↔ L+β-Mn | γ-Mn: Mn 0.9222; L: Mn 0.699; β-Mn: Mn 0.934 | model | [1] Wang 2015 | Table 3, p. 5, row 7; `ORC-E4PS3VFVBD` |  |
| 1293 | metatectic/catatectic: γ-Mn ↔ L+β-Mn | L: Mn 0.72 | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 5; `ORC-QSKAKBRZGC` |  |
| 1292.7 | metatectic/catatectic: γ-Mn ↔ L+β-Mn |  | experimental | [1] Wang 2015 | Table 3, p. 5, row 6; `ORC-YAEW3YAOLQ` |  |
| 1248 | metatectic/catatectic: γ-Mn ↔ L+β-Mn | L: Mn 0.79 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 4; `ORC-FKM4NQHHLK` |  |
| 1183 | peritectic: L+β-Mn ↔ InMn3 | L: Mn 0.52; InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 9; `ORC-ESGRS54V7M` |  |
| 1181.8 | peritectic: L+β-Mn ↔ InMn3 | L: Mn 0.5186; β-Mn: Mn 0.9104; InMn3: Mn 0.75 | model | [1] Wang 2015 | Table 3, p. 5, row 11; `ORC-Q2UMAQVZDU` |  |
| 1181.5 | peritectic: L+β-Mn ↔ InMn3 | InMn3: Mn 0.75 | experimental | [1] Wang 2015 | Table 3, p. 5, row 10; `ORC-XL5L5ZMJ53` |  |
| 1145 | peritectic: L+β-Mn ↔ InMn3 | L: Mn 0.54; β-Mn: Mn 0.86; InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 8; `ORC-3B6H5NTQY7` |  |
| 908 | eutectoid: β-Mn ↔ InMn3+α-Mn | β-Mn: Mn 0.963; InMn3: Mn 0.75; α-Mn: Mn 0.9873 | model | [1] Wang 2015 | Table 3, p. 5, row 14; `ORC-GURSKUDPIA` |  |
| 908 | eutectoid: β-Mn ↔ InMn3+α-Mn | InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 13; `ORC-RXYGOTWELV` |  |
| 863 | eutectoid: β-Mn ↔ InMn3+α-Mn | InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 12; `ORC-V6Q4LBNNKD` |  |
| 429.6 | eutectic: L ↔ InMn3+(In) | L: Mn 3.000e-4; InMn3: Mn 0.75; (In): Mn 1.000e-4 | model | [1] Wang 2015 | Table 3, p. 5, row 17; `ORC-76N26PXTCV` |  |
| 429 | eutectic: L ↔ InMn3+(In) | InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 15; `ORC-32R3ITJ3DC` |  |
| 429 | eutectic: L ↔ InMn3+(In) | InMn3: Mn 0.75 | experimental | [1] Wang 2015 | Table 3, p. 5, row 16; `ORC-JKNBWHURAG` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, In–Mn system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| InMn3 |  | 0.67 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Wang 2015 | p. 6; `ORC-QAO6NCYVDO` | “The enthalpy of formation of InMn3 at 298 K was calculated to be 670 J/mol and compared with the experimental data \[31\] as shown in Fig. 10.” |

## Other properties

### Phase transition (28)

Table: Phase transition, In–Mn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 428.1 K | 428.1 | Mn7In93; _alloy: In 0.93, Mn 0.07_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 1; `ORC-H5VSOZHHFC` |  |
| Phase transition | 428.5 K | 428.5 | Mn50In50; _alloy: In 0.5, Mn 0.5_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 11; `ORC-EOD63JAWY2` |  |
| Phase transition | 428.6 K | 428.6 | Mn35In65; _alloy: In 0.65, Mn 0.35_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 7; `ORC-KGUZUEXLGT` |  |
| Phase transition | 428.7 K | 428.7 | Mn55In45; _alloy: In 0.45, Mn 0.55_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 13; `ORC-4CVR7UAEE7` |  |
| Phase transition | 428.8 K | 428.8 | Mn70In30; _alloy: In 0.3, Mn 0.7_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 22; `ORC-PDTR7KQEIQ` |  |
| Phase transition | 428.9 K | 428.9 | Mn60In40; _alloy: In 0.4, Mn 0.6_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 16; `ORC-L76L6CWPBY` |  |
| Phase transition | 428.9 K | 428.9 | Mn73In27; _alloy: In 0.27, Mn 0.73_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 25; `ORC-7B5NU5QE3K` |  |
| Phase transition | 429.2 K | 429.2 | Mn45In55; _alloy: In 0.55, Mn 0.45_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 9; `ORC-DR4BKB5TS6` |  |
| Phase transition | 429.3 K | 429.3 | Mn15In85; _alloy: In 0.85, Mn 0.15_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 3; `ORC-KC4ZCOWOVS` |  |
| Phase transition | 429.3 K | 429.3 | Mn25In75; _alloy: In 0.75, Mn 0.25_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 5; `ORC-CNCA7WCCSK` |  |
| Phase transition | 429.6 K | 429.6 | Mn75In25; _alloy: In 0.25, Mn 0.75_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 28; `ORC-Y72GT5C2WP` |  |
| Phase transition | 429.7 K | 429.7 | Mn77In23; _alloy: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 31; `ORC-RLCXSESBSN` |  |
| Phase transition | 429.8 K | 429.8 | Mn65In35; _alloy: In 0.35, Mn 0.65_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 19; `ORC-W5VUGND57J` |  |
| Phase transition | 1179.7 K | 1179.7 | Mn55In45; _alloy: In 0.45, Mn 0.55_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 14; `ORC-ZVFY3ARHIB` |  |
| Phase transition | 1180.5 K | 1180.5 | Mn60In40; _alloy: In 0.4, Mn 0.6_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 17; `ORC-X2YHMINQ2A` |  |
| Phase transition | 1180.6 K | 1180.6 | Mn85In15 (1123 K, 360 h); _alloy: In 0.15, Mn 0.85_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 38; `ORC-U3WBBT6RLH` |  |
| Phase transition | 1180.9 K | 1180.9 | Mn70In30; _alloy: In 0.3, Mn 0.7_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 23; `ORC-IWCBYONCZJ` |  |
| Phase transition | 1181 K | 1181 | Mn80In20 (873 K,720 h); _alloy: In 0.2, Mn 0.8_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 35; `ORC-2VNJGITS3I` |  |
| Phase transition | 1181.6 K | 1181.6 | Mn77In23; _alloy: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 32; `ORC-BBQS6LGIRF` |  |
| Phase transition | 1182.1 K | 1182.1 | Mn75In25; _alloy: In 0.25, Mn 0.75_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 29; `ORC-5X5CGDDD4Q` |  |
| Phase transition | 1183 K | 1183 | Mn65In35; _alloy: In 0.35, Mn 0.65_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 20; `ORC-CNNISUM476` |  |
| Phase transition | 1183.6 K | 1183.6 | Mn73In27; _alloy: In 0.27, Mn 0.73_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 26; `ORC-JSRF7CMSA6` |  |
| Phase transition | 1289.2 K | 1289.2 | Mn73In27; _alloy: In 0.27, Mn 0.73_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 27; `ORC-BNOYK75NKX` |  |
| Phase transition | 1291.5 K | 1291.5 | Mn85In15 (1123 K, 360 h); _alloy: In 0.15, Mn 0.85_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 39; `ORC-VHOBJYCOAC` |  |
| Phase transition | 1293.2 K | 1293.2 | Mn90In10 (1123 K, 360 h); _alloy: In 0.1, Mn 0.9_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 41; `ORC-LCR45MT7NZ` |  |
| Phase transition | 1293.4 K | 1293.4 | Mn80In20 (873 K,720 h); _alloy: In 0.2, Mn 0.8_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 36; `ORC-QZWFCMTQU4` |  |
| Phase transition | 1294.2 K | 1294.2 | Mn75In25; _alloy: In 0.25, Mn 0.75_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 30; `ORC-X3KSYBWIUZ` |  |
| Phase transition | 1294.4 K | 1294.4 | Mn77In23; _alloy: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 33; `ORC-UEKPLRHF6Q` |  |

### Phase equilibrium (14)

Table: Phase equilibrium, In–Mn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 928.6 | other: Mn7In93; _liquid: In 0.93, Mn 0.07_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 2; `ORC-XCC5GDNAHZ` |  |
| Phase composition |  | 1005.5 | other: Mn15In85; _liquid: In 0.85, Mn 0.15_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 4; `ORC-QPOCTEEXH5` |  |
| Phase composition |  | 1070.5 | other: Mn25In75; _liquid: In 0.75, Mn 0.25_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 6; `ORC-YBXDDV7RV3` |  |
| Phase composition |  | 1111.2 | other: Mn35In65; _liquid: In 0.65, Mn 0.35_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 8; `ORC-BVNLAO3M52` |  |
| Phase composition |  | 1155.8 | other: Mn45In55; _liquid: In 0.55, Mn 0.45_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 10; `ORC-C5HIUUVRNA` |  |
| Phase composition |  | 1161.4 | other: Mn50In50; _liquid: In 0.5, Mn 0.5_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 12; `ORC-B3FECRCEIK` |  |
| Phase composition |  | 1210.1 | other: Mn60In40; _liquid: In 0.4, Mn 0.6_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 18; `ORC-TTE46CB34G` |  |
| Phase composition |  | 1211.3 | other: Mn55In45; _liquid: In 0.45, Mn 0.55_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 15; `ORC-EEOCJ7LWHU` |  |
| Phase composition |  | 1245.8 | other: Mn65In35; _liquid: In 0.35, Mn 0.65_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 21; `ORC-X3TDO7RPZI` |  |
| Phase composition |  | 1261.1 | other: Mn70In30; _liquid: In 0.3, Mn 0.7_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 24; `ORC-E6YW2AH5F6` |  |
| Phase composition |  | 1321.5 | other: Mn77In23; _liquid: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 34; `ORC-JW7RA4T4FZ` |  |
| Phase composition |  | 1369.8 | other: Mn80In20 (873 K,720 h); _liquid: In 0.2, Mn 0.8_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 37; `ORC-3GARODJKLE` |  |
| Phase composition |  | 1389.7 | other: Mn85In15 (1123 K, 360 h); _liquid: In 0.15, Mn 0.85_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 40; `ORC-LXAERLLXEI` |  |
| Phase composition |  | 1429.3 | other: Mn90In10 (1123 K, 360 h); _liquid: In 0.1, Mn 0.9_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 42; `ORC-I2KSKQG2AD` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015). [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
