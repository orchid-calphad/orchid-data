# Ba–O system

> Ba–O system: 36 accepted literature values (formation 14, heat capacity / entropy / enthalpy 12, phase transition 6, invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-O.html · Markdown: https://data.orchid-project.org/systems/BA-O.md

36 accepted literature values from 2 paper(s) (experimental 17, model 19); 1 calculated phase diagram(s). 43 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-O.json) · [CSV](https://data.orchid-project.org/systems/BA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-O/BaO-95Zim.json) · [phases (10)](https://data.orchid-project.org/phases/pages/BA-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BA-O.html) · [Markdown](https://data.orchid-project.org/systems/BA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 17 |
| model | 19 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 6 |
| formation | 14 |
| heat capacity / entropy / enthalpy | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaO-95Zim.tdb | E. Zimmermann, K. Hack, D. Neuschutz, Calphad, 19, 119-27(1995). [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) | `a0f7658f38a4a7d7eb4fba12550e7fb56477c73cbf19cc89076a0a1247457773` | [viewer](https://orchid-project.org/phase-diagrams/#BA-O/BaO-95Zim.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaO-95Zim.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaO-95Zim.tdb | 1962.85 | BAO (x(O) 0.50109) + LIQUID (x(O) 0.56843) + GAS (x(O) 0.99993) |
| BaO-95Zim.tdb | 1096.02 | BAO#2 (x(O) 0.5158) + BAO (x(O) 0.61991) + GAS (x(O) 1) |
| BaO-95Zim.tdb | 1096.02 | BAO (x(O) 0.5158) + BAO#2 (x(O) 0.61991) + O2GAS (x(O) 1) |
| BaO-95Zim.tdb | 854.47 | BCC_A2 (x(O) 0) + LIQUID (x(O) 0.09782) + BAO (x(O) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ba–O system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1630 | eutectic: Liquid -> BaO + gas | L: O 0.575; BaO: O 0.506; gas: O 1 | model | [1] Zhou 2005 | Table III, p. 6, row 4; `ORC-5VOTELIQUU.05c48a` |  |
| 1096 | peritectic: BaO + gas -> BaO2 | BaO: O 0.509; gas: O 1; BaO2: O 0.618 | model | [1] Zhou 2005 | Table III, p. 6, row 6; `ORC-VIJAKKUMXZ.63c195` |  |
| 1096 | peritectic: BaO + gas -> BaO2 | BaO: O 0.509; gas: O 1; BaO2: O 0.624 | model | [1] Zhou 2005 | Table III, p. 6, row 5; `ORC-VIJAKKUMXZ.d1d903` |  |
| 842 | eutectic: Liquid -> bcc + BaO | L: O 0.1; bcc: O 0; BaO: O 0.5 | model | [1] Zhou 2005 | Table III, p. 6, row 7; `ORC-NPVYXNYEIF` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ba–O system (14)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ba2O2(G) |  | -125.9 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 9; `ORC-4YNEHQ5EIR.2dc640` |  |
| Ba2O3(G) |  | -100.72 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 9; `ORC-4YNEHQ5EIR.a11b60` |  |
| BaO |  | -274.03 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Zhou 2005; _cites Hedvall 1918_ | Table I, p. 3, row 2; `ORC-VUULNG2P7H.06351a` |  |
| BaO(G) |  | -60.45 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 6; `ORC-TSAWQE6B7D.67270d` |  |
| BaO(L) |  | -250.138 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 3; `ORC-ZTEM7HIHVT.1cef31` |  |
| BaO(S) | [BaO](https://data.orchid-project.org/compounds/BaO.html) | -276.68 kJ/mol-atom | 298.15 | model | -272.439 (mp-aaaaabzq) | -259.209 (oqmd-1343705) | [2] Zimmermann 1995 | Table 2, p. 5, row 1; `ORC-6UBIDCFIOR.411216` |  |
| BaO2(S) | [BaO2](https://data.orchid-project.org/compounds/BaO2.html) | -211.9 kJ/mol-atom | 298.15 | model | -209.391 (mp-aaaaabqn) | -205.059 (oqmd-1984787) | [2] Zimmermann 1995 | Table 2, p. 5, row 5; `ORC-FZDHSR2W56.243809` |  |
| BaO^s |  | -581.83 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 52Mah_ | Table 1, p. 3, row 4; `ORC-YKJN32MT5L` |  |
| BaO^s |  | -560.82 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 23Gun_ | Table 1, p. 3, row 2; `ORC-UMGELNRKO4` |  |
| BaO^s |  | -556.47 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 56Zai_ | Table 1, p. 3, row 3; `ORC-FT2GQX5YP6` |  |
| BaO^s |  | -552.71 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 66Fli_ | Table 1, p. 3, row 5; `ORC-QN4AUCYWOO` |  |
| BaO^s |  | -548.02 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 73Fit_ | Table 1, p. 3, row 6; `ORC-4X2KRBUUIB` |  |
| BaO^s |  | -548.02 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 90Cor_ | Table 1, p. 3, row 7; `ORC-RCEC6OJ3SP` |  |
| BaO^s |  | -526.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 08For_ | Table 1, p. 3, row 1; `ORC-DBGM6GQXAO` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Ba–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2197 K | 2197 | liquid | experimental | [1] Zhou 2005; _cites Schriel 1937_ | p. 1; `ORC-K6V2TQFZQZ.eb7d6f` | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 2273 K | 2273 | liquid | experimental | [1] Zhou 2005; _cites Foex 1965_ | p. 1; `ORC-K6V2TQFZQZ.c0f4b7` | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 2286 K | 2286 | liquid | experimental | [1] Zhou 2005; _cites Schumacher 1926_ | p. 1; `ORC-K6V2TQFZQZ.90116d` | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 2287 K | 2287 | congruent melting: Liquid -> BaO; _L: O 0.5; BaO: O 0.5_ | model | [1] Zhou 2005 | Table III, p. 6, row 2; `ORC-IGD53MEIHM` |  |
| Phase transition | 2290 K | 2290 | liquid | experimental | [1] Zhou 2005; _cites Moissan 1902_ | p. 1; `ORC-K6V2TQFZQZ.1fb732` | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 3249 K | 3249 | congruent melting: Gas -> liquid; _Gas: O 0.539; L: O 0.539_ | model | [1] Zhou 2005 | Table III, p. 6, row 1; `ORC-3FGO3YWNY6` |  |

### Heat capacity / entropy / enthalpy (12)

Table: Heat capacity / entropy / enthalpy, Ba–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: entropy_ | 35.01 J/K/mole of atoms | 298.15 |  | experimental | [1] Zhou 2005; _cites Cordfunke 1994_ | p. 3; `ORC-EV4OVDHGTX` | “Its heat capacity, as measured by different authors 32,33,34 using an adiabatic calorimeter, was plotted in Fig. 2, and was used to calculate the entropy32 at 298K to be 35.01 J/K/mole of atoms.” |
| Entropy; _printed: entropy_ | 29.18 J/K/mole of atoms | 298.15 |  | experimental | [1] Zhou 2005; _cites Gavrichev_ | p. 3; `ORC-S5EXAT6KUE` | “The heat capacity of the BaO2 phase was measured by Gavrichev et al.35 by means of a calorimeter (see Fig. 2) and was used to calculate its entropy35 as 29.18 J/K/mole of atoms at 298K.” |
| Entropy; _printed: S298_ | 89.475 J/mol-atom/K | 298.15 | Ba2O2(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9; `ORC-4YNEHQ5EIR.5723ae` |  |
| Entropy; _printed: S298_ | 71.58 J/mol-atom/K | 298.15 | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9; `ORC-4YNEHQ5EIR.27a3fa` |  |
| Entropy; _printed: Entropy of formation at 298 K_ | 34.99 J/mol (basis unstated)/K | 298.15 | BaO; _alloy: O 0.5_ | model | [1] Zhou 2005 | Table I, p. 3, row 10; `ORC-UNJ4JE2XVU` |  |
| Entropy; _printed: Entropy of formation at 298 K_ | 35.01 J/mol (basis unstated)/K | 298.15 | BaO; _alloy: O 0.5_ | experimental | [1] Zhou 2005; _cites Zaitseva 1956_ | Table I, p. 3, row 3; `ORC-V2WKUCX6FJ` |  |
| Entropy; _printed: Entropy of formation_ | 35.01 J/mol (basis unstated)/K | 298.15 | BaO; _alloy: O 0.5_ | experimental | [1] Zhou 2005; _cites Hedvall 1918_ | Table I, p. 3, row 2; `ORC-VUULNG2P7H.02f999` |  |
| Entropy; _printed: S298_ | 117.73 J/mol-atom/K | 298.15 | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 6; `ORC-TSAWQE6B7D.162732` |  |
| Entropy; _printed: S298_ | 47.438 J/mol-atom/K | 298.15 | BaO(L); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 3; `ORC-ZTEM7HIHVT.a25906` |  |
| Entropy; _printed: S298_ | 36.035 J/mol-atom/K | 298.15 | BaO(S); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 1; `ORC-6UBIDCFIOR.57e037` |  |
| Entropy; _printed: Entropy of formation_ | 29.18 J/mol (basis unstated)/K | 298.15 | BaO2; _alloy: O 0.666667_ | experimental | [1] Zhou 2005 | Table I, p. 3, row 8; `ORC-DMABJ7FDWX` |  |
| Entropy; _printed: S298_ | 30.9167 J/mol-atom/K | 298.15 | BaO2(S); _alloy: O 0.666667_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 5; `ORC-FZDHSR2W56.9603d3` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005). [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x)
2. E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995). [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
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

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
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
