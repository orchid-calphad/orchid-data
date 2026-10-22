# Nd–Zr system

> Nd–Zr system: 38 accepted literature values (phase transition 26, invariant reaction 9, phase equilibrium 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ND-ZR.html · Markdown: https://data.orchid-project.org/systems/ND-ZR.md

38 accepted literature values from 2 paper(s) (experimental 32, model 3, unspecified 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ND-ZR.json) · [CSV](https://data.orchid-project.org/systems/ND-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ND-ZR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ND-ZR/NdZr-14Che.json) · [Markdown](https://data.orchid-project.org/systems/ND-ZR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 32 |
| model | 3 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |
| phase transition | 26 |
| phase equilibrium | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NdZr-14Che.tdb | K. Cheng, H. Zhou, B. Hu, Y. Du, L. Zhang, S. Liu, H. Xu, L. Liu, Metall. Mater. Trans. A, 45A, 2708-18(2014). [doi:10.1007/s11661-014-2209-1](https://doi.org/10.1007/s11661-014-2209-1) | `5b20a92a0ab14f26f99f9c5ae58972d6c2946d1f7a9a69daff2e98a511c2b495` | [viewer](https://orchid-project.org/phase-diagrams/#ND-ZR/NdZr-14Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NdZr-14Che.json) |
| NdZr-14Mat.tdb | N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada, S. Kohara, J. Eckert, Calphad, 46, 103-7(2014). [doi:10.1016/j.calphad.2014.02.008](https://doi.org/10.1016/j.calphad.2014.02.008) | `3f1e2816e533b3fb8a36461e09af7bbb63a59b41bfd4e3d9b742374d00541c85` | [viewer](https://orchid-project.org/phase-diagrams/#ND-ZR/NdZr-14Mat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Mat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NdZr-14Mat.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NdZr-14Che.tdb | 1953.85 | LIQUID (x(Zr) 0.38306) + LIQUID#2 (x(Zr) 0.61694) + BCC_A2 (x(Zr) 0.91984) |
| NdZr-14Che.tdb | 1267.2 | LIQUID (x(Zr) 0.02529) + DHCP (x(Zr) 0.05141) + BCC_A2 (x(Zr) 0.97741) |
| NdZr-14Che.tdb | 1258.1 | BCC_A2 (x(Zr) 6.200e-4) + LIQUID (x(Zr) 0.01766) + DHCP (x(Zr) 0.03494) |
| NdZr-14Che.tdb | 1112.49 | DHCP (x(Zr) 0.03143) + BCC_A2 (x(Zr) 0.98873) + HCP_A3 (x(Zr) 0.99931) |
| NdZr-14Mat.tdb | 1271.4 | BCC_A2 (x(Zr) 0.02977) + LIQUID (x(Zr) 0.04013) + BCC_A2#2 (x(Zr) 0.97023) |
| NdZr-14Mat.tdb | 1167.1 | BCC_A2#2 (x(Zr) 0.02234) + HCP_A3 (x(Zr) 0.96568) + BCC_A2 (x(Zr) 0.97766) |
| NdZr-14Mat.tdb | 1116.24 | DHCP (x(Zr) 0.01487) + BCC_A2 (x(Zr) 0.01872) + HCP_A3 (x(Zr) 0.97122) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ND/ND-ZR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ND/ND-ZR.json) · [CALPHAD hull NdZr-14Mat](https://data.orchid-project.org/hulls/calphad-sgte/ND/ND-ZR--NdZr-14Mat.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nd–Zr system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1274 | L -> bcc-Nd + bcc-Zr |  | experimental | [1] Mattern 2014 | Table 3, p. 4, row 2 |  |
| 1274 | eutectic: L2bcc-Nd(Zr)þbcc-Zr(Nd) |  | experimental | [1] Mattern 2014 | p. 2 | “The DSC event (3) at T1⁄4 1274 K corresponds to the eutectic reaction L2bcc-Nd(Zr)þbcc-Zr(Nd).” |
| 1271 | L -> bcc-Nd + bcc-Zr | L: Zr 0.04; bcc-Nd: Zr 0.03; bcc-Zr: Zr 0.97 | model | [1] Mattern 2014 | Table 3, p. 4, row 1 |  |
| 1268 | peritectic: Liquid + (bZr) M (aNd) |  | experimental | [2] Cheng 2014 | p. 8 | “Since the Nd-rich end has a peritectic type reaction as investigated in the SEM images of the as-cast alloy 2, which exhibit the dissolution of primary Zr into liquid phase to form Nd, the invariant reaction of Liquid + (bZr) M (aNd) is adjusted to the thermal signal at 1268 K (995 °C).” |
| 1167 | bcc-Nd + bcc-Zr -> hcp-Zr | bcc-Nd: Zr 0.022; bcc-Zr: Zr 0.978; hcp-Zr: Zr 0.966 | model | [1] Mattern 2014 | Table 3, p. 4, row 3 |  |
| 1167 | bcc-Nd + bcc-Zr -> hcp-Zr |  | experimental | [1] Mattern 2014 | Table 3, p. 4, row 4 |  |
| 1118 | bcc-Nd -> hcp-Zr + dhcp-Nd |  | experimental | [1] Mattern 2014 | Table 3, p. 4, row 6 |  |
| 1116 | bcc-Nd -> hcp-Zr + dhcp-Nd | bcc-Nd: Zr 0.019; hcp-Zr: Zr 0.971; dhcp-Nd: Zr 0.015 | model | [1] Mattern 2014 | Table 3, p. 4, row 5 |  |
| 1112 | eutectic: (bZr) M (aNd) + (aZr) |  | experimental | [2] Cheng 2014 | p. 8 | “The eutectic reaction of (bZr) M (aNd) + (aZr) is assigned to be at 1112 K (839 °C), and the solid solubility at 1268 K (1050 °C) is determined to be more than 2.5 at. pct Nd based on the results obtained from the Nd-Zr alloys in the group 3.” |

## Other properties

### Phase transition (26)

Table: Phase transition, Nd–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1106.1 K | 1106.1 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 1 |  |
| Phase transition | 1108.6 K | 1108.6 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 11 |  |
| Phase transition | 1108.7 K | 1108.7 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 31 |  |
| Phase transition | 1109.4 K | 1109.4 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 23 |  |
| Phase transition | 1111.9 K | 1111.9 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 19 |  |
| Phase transition | 1112 K | 1112 | other | experimental | [2] Cheng 2014 | p. 6 | “There are two thermal signals in most of the Nd-Zr alloys, indicating two invariant reactions at 1268 K and 1112 K (995 °C and 839 °C), while the overlapped peaks are detected in the alloy 1 when comparing the DSC curves with a heating rate of 5 K/min to that of 2 K/min, as shown in Figure 10.” |
| Phase transition | 1112.7 K | 1112.7 | (βZr) ↔ (αNd) + (αZr) | unspecified | [2] Cheng 2014 | Table III, p. 7, row 8 |  |
| Phase transition | 1114 K | 1114 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 27 |  |
| Phase transition | 1114.3 K | 1114.3 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 7 |  |
| Phase transition | 1114.6 K | 1114.6 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 15 |  |
| Phase transition | 1115.1 K | 1115.1 | (βZr) ↔ (αNd) + (αZr) | experimental | [2] Cheng 2014 | Table III, p. 7, row 35 |  |
| Phase transition | 1118 K | 1118 | dhcp-Nd(Zr)þhcp-Zr(Nd)2bcc-Nd(Zr) | experimental | [1] Mattern 2014 | p. 2 | “The reaction (1) of the DSC curve at T1⁄4 1118 K corresponds to the transformation dhcp-Nd(Zr)þhcp-Zr(Nd)2bcc-Nd(Zr).” |
| Phase transition | 1167 K | 1167 | hcp Zr(Nd)2bcc-Zr(Nd)þ bcc-Nd(Zr) | experimental | [1] Mattern 2014 | p. 2 | “At T1⁄4 1167 K, DSC event (2), the transformation hcp Zr(Nd)2bcc-Zr(Nd)þ bcc-Nd(Zr) takes place.” |
| Phase transition | 1256.2 K | 1256.2 | Liquid + (αNd)/(αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 3 |  |
| Phase transition | 1260 K | 1260 | Liquid + (αNd)/(αNd) | unspecified | [2] Cheng 2014 | Table III, p. 7, row 4 |  |
| Phase transition | 1263 K | 1263 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 9 |  |
| Phase transition | 1265.9 K | 1265.9 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 17 |  |
| Phase transition | 1266 K | 1266 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 13 |  |
| Phase transition | 1266.3 K | 1266.3 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 5 |  |
| Phase transition | 1266.4 K | 1266.4 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 37 |  |
| Phase transition | 1266.6 K | 1266.6 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 29 |  |
| Phase transition | 1268 K | 1268 | Liquid + (βZr) ↔ (αNd) | unspecified | [2] Cheng 2014 | Table III, p. 7, row 22 |  |
| Phase transition | 1268 K | 1268 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 21 |  |
| Phase transition | 1268 K | 1268 | other | experimental | [2] Cheng 2014 | p. 6 | “There are two thermal signals in most of the Nd-Zr alloys, indicating two invariant reactions at 1268 K and 1112 K (995 °C and 839 °C), while the overlapped peaks are detected in the alloy 1 when comparing the DSC curves with a heating rate of 5 K/min to that of 2 K/min, as shown in Figure 10.” |
| Phase transition | 1269.5 K | 1269.5 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 25 |  |
| Phase transition | 1270.3 K | 1270.3 | Liquid + (βZr) ↔ (αNd) | experimental | [2] Cheng 2014 | Table III, p. 7, row 33 |  |

### Phase equilibrium (3)

Table: Phase equilibrium, Nd–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  |  | Nd-dendrite + Eutectic; _Nd-dendrite: Nd 0.96, Zr 0.04; Eutectic: Nd 0.924, Zr 0.076_ | experimental | [1] Mattern 2014 | Table 1, p. 4, row 1 |  |
| Phase composition |  |  | Zr-dendrites + Nd-dendrite + Eutectic; _Zr-dendrites: Nd 0.044, Zr 0.956; Nd-dendrite: Nd 0.952, Zr 0.048; Eutectic: Nd 0.923, Zr 0.077_ | experimental | [1] Mattern 2014 | Table 1, p. 4, row 2 |  |
| Phase composition |  |  | Zr-dendrites + Nd-dendrite + Eutectic; _Zr-dendrites: Nd 0.05, Zr 0.95; Nd-dendrite: Nd 0.945, Zr 0.055; Eutectic: Nd 0.92, Zr 0.08_ | experimental | [1] Mattern 2014 | Table 1, p. 4, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Zr system, Calphad 46, 103-107 (2014). [doi:10.1016/j.calphad.2014.02.008](https://doi.org/10.1016/j.calphad.2014.02.008)
2. Kaiming Cheng, Hua Zhou, Biao Hu, Yong Du, Lijun Zhang, Shuhong Liu et al., Experimental Investigation and Thermodynamic Modeling of the Nd-Zr and the Mg-Nd-Zr Systems, Metall Mater Trans A 45, 2708-2718 (2014). [doi:10.1007/s11661-014-2209-1](https://doi.org/10.1007/s11661-014-2209-1)

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
