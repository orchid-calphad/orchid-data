# Hg–Te system

> Hg–Te system: 36 accepted literature values (phase equilibrium 11, formation 10, invariant reaction 8, phase transition 5) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HG-TE.html · Markdown: https://data.orchid-project.org/systems/HG-TE.md

36 accepted literature values from 2 paper(s) (experimental 21, model 10, unspecified 5); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HG-TE.json) · [CSV](https://data.orchid-project.org/systems/HG-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HG-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HG-TE/HgTe-10Gie.json) · [phases (7)](https://data.orchid-project.org/phases/pages/HG-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HG-TE.html) · [Markdown](https://data.orchid-project.org/systems/HG-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 21 |
| model | 10 |
| unspecified | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 5 |
| phase equilibrium | 11 |
| formation | 10 |
| mixing / partial | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HgTe-10Gie.tdb | W. Gierlotka, J. Alloys Compd., 494, 102-8(2010). [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) | `c1efc80be4426d7d90ed54d3813099f9aefae229ba3411c64d411a6e9c9ecdca` | [viewer](https://orchid-project.org/phase-diagrams/#HG-TE/HgTe-10Gie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgTe-10Gie.json) |
| HgTe-95Yan-LB.tdb | J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995). [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) | `d35628e6d9da010c601e3659dc676c9d84d2543881647cac6ce6fc7d5612f0bf` | [viewer](https://orchid-project.org/phase-diagrams/#HG-TE/HgTe-95Yan-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgTe-95Yan-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HgTe-10Gie.tdb | 940.55 | ZINCBLENDE_B3 (x(Te) 0.5) + LIQUID (x(Te) 0.52155) + ION (x(Te) 0.52677) |
| HgTe-10Gie.tdb | 762.92 | ION (x(Te) 0.09121) + LIQUID (x(Te) 0.09145) + ZINCBLENDE_B3 (x(Te) 0.5) |
| HgTe-10Gie.tdb | 682.81 | ZINCBLENDE_B3 (x(Te) 0.5) + ION (x(Te) 0.84299) + HEXAGONAL_A8 (x(Te) 1) |
| HgTe-95Yan-LB.tdb | 686.29 | ZINCBLENDE_B3 (x(Te) 0.5) + LIQUID (x(Te) 0.85286) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HG/HG-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HG/HG-TE.json) · [CALPHAD hull HgTe-95Yan-LB](https://data.orchid-project.org/hulls/calphad-sgte/HG/HG-TE--HgTe-95Yan-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hg–Te system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 684 | HgTe + Te = L | HgTe: Te 0.5; Te: Te 1 | experimental | [1] Gierlotka 2010; _cites Massalski 1986_ | Table 3, p. 4, row 9; `ORC-3WUBYWUD2R` |  |
| 684 | eutectic |  | experimental | [1] Gierlotka 2010 | p. 2; `ORC-OFQFGWZRJU.7ee0a8` | “The system shows 2 invariant reactions: eutectic reaction between liquid, solid Hg and intermetallic compound HgTe at temperature 233 K and another eutectic between liquid, solid tellurium and intermetallic compound at 684 K.” |
| 683 | HgTe + Te = L | HgTe: Te 0.5; Te: Te 1 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 11; `ORC-GKCKR43FBI` |  |
| 675 | HgTe + Te = L | HgTe: Te 0.5; Te: Te 1 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 12; `ORC-7HKZ6QY3BD` |  |
| 234 | Hg + HgTe = L | Hg: Te 0; HgTe: Te 0.5 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 2; `ORC-6VZTYAT7X5` |  |
| 233 | eutectic |  | experimental | [1] Gierlotka 2010 | p. 2; `ORC-OFQFGWZRJU.61020f` | “The system shows 2 invariant reactions: eutectic reaction between liquid, solid Hg and intermetallic compound HgTe at temperature 233 K and another eutectic between liquid, solid tellurium and intermetallic compound at 684 K.” |
| 233 | Hg + HgTe = L | Hg: Te 0; HgTe: Te 0.5 | experimental | [1] Gierlotka 2010; _cites Massalski 1986_ | Table 3, p. 4, row 1; `ORC-QUH6KVSAB4` |  |
| 233 | Hg + HgTe = L | Hg: Te 0; HgTe: Te 0.5 | model | [1] Gierlotka 2010 | Table 3, p. 4, row 4; `ORC-ZEDGTT3OAD` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Hg–Te system (10)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| HgTe |  | -44.02 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Gierlotka 2010; _cites Yang 1995_ [doi](https://doi.org/10.1016/0364-5916%2895%2900039-h) | Table 4, p. 4, row 7; `ORC-OEJNTMATEJ` |  |
| HgTe |  | -44.002 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [2] Jianrong 1995; _cites ref. 13_ | Table 4, p. 13, row 1; `ORC-S6377M3I2P.a5a2d6` |  |
| HgTe |  | -43.802 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Gierlotka 2010; _cites Su 1981_ | Table 4, p. 4, row 4; `ORC-PYTM5LPW4L` |  |
| HgTe |  | -43.69 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Gierlotka 2010; _cites Brebrick 1991_ | Table 4, p. 4, row 6; `ORC-HJSAMN7EKC` |  |
| HgTe |  | -43.648 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Gierlotka 2010 | Table 4, p. 4, row 8; `ORC-XKDATEYW7N` |  |
| HgTe |  | -43.538 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Jianrong 1995 | Table 4, p. 13, row 2; `ORC-D3QUZ7OGYZ.41f6eb` |  |
| HgTe |  | -41.2 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Gierlotka 2010; _cites Sha 1989_ [doi](https://doi.org/10.1149/1.2096558) | Table 4, p. 4, row 3; `ORC-PX3Z37VCT4` |  |
| HgTe |  | -36.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Gierlotka 2010; _cites Nasar 1990_ [doi](https://doi.org/10.1016/0022-5088%2890%2990316-c) | Table 4, p. 4, row 5; `ORC-NFHRK2IB4Q` |  |
| HgTe |  | -33.9 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Gierlotka 2010; _cites Ratajczak 1969_ | Table 4, p. 4, row 1; `ORC-EEZQZUHVX2` |  |
| HgTe |  | -31.8 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Gierlotka 2010; _cites Mills 1974_ | Table 4, p. 4, row 2; `ORC-67ZTLGAVJG` |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Hg–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 942 K | 942 | L = HgTe; _L: Te 0.5; HgTe: Te 0.5_ | model | [1] Gierlotka 2010 | Table 3, p. 4, row 8; `ORC-OXRNDSNLCN` |  |
| Phase transition | 942.65 K | 942.65 | HgTe | experimental | [2] Jianrong 1995; _cites ref. 31_ | p. 2; `ORC-5OCPAQBWPA` | “The melting point of HgTe has been measured by Strauss (3 1) Asadov (34) Delves and Lewis (36) Vanyukov et al. (32), Harman (35) Levitskaya et al. (37) Steininger (38) Blair and New&m (39), Ray and Spencer (26), Szofran and Lehoczky (40), Harman and Strauss (41), Tung et al.. (5)and Gromakov et al. (42) with general agreement and a mean value of 669.5"C.” |
| Phase transition | 943 K | 943 | L = HgTe; _L: Te 0.5; HgTe: Te 0.5_ | experimental | [1] Gierlotka 2010; _cites Massalski 1986_ | Table 3, p. 4, row 5; `ORC-WGMFDCVXWT` |  |
| Phase transition | 943 K | 943 | congruent transformation | experimental | [1] Gierlotka 2010 | p. 2; `ORC-7TXCRVBBOG` | “Temperature of congruent melting of HgTe intermetallic compound is 943 K.” |
| Phase transition | 944 K | 944 | L = HgTe; _L: Te 0.5; HgTe: Te 0.5_ | model | [1] Gierlotka 2010 | Table 3, p. 4, row 6; `ORC-HGF4PWW2QQ` |  |

### Phase equilibrium (11)

Table: Phase equilibrium, Hg–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 936.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 32_ | Table 1B, p. 4, row 5; `ORC-MLSK6MMBJC` |  |
| Phase composition |  | 940.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 5_ | Table 1B, p. 4, row 6; `ORC-XZ7XUQ522T` |  |
| Phase composition |  | 941.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 38_ | Table 1B, p. 4, row 11; `ORC-VHNCQGF5GA` |  |
| Phase composition |  | 941.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 37_ | Table 1B, p. 4, row 12; `ORC-ZJGWCO5MLR` |  |
| Phase composition |  | 942.65 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 39_ | Table 1B, p. 4, row 7; `ORC-WUYRVPCPLX` |  |
| Phase composition |  | 943.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 32_ | Table 1B, p. 4, row 4; `ORC-7ZOZ2GZTE5` |  |
| Phase composition |  | 943.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 36_ | Table 1B, p. 4, row 9; `ORC-K5QGC6YQ5G` |  |
| Phase composition |  | 943.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 26_ | Table 1B, p. 4, row 8; `ORC-MGVAA6OOWR` |  |
| Phase composition |  | 943.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 34_ | Table 1B, p. 4, row 2; `ORC-XTDALXGAQQ` |  |
| Phase composition |  | 943.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 31_ | Table 1B, p. 4, row 1; `ORC-ZX6XFLKEAJ` |  |
| Phase composition |  | 958.15 | other: Melting Point of HgTe; _liquid: Te 0.5_ | experimental | [2] Jianrong 1995; _cites ref. 42_ | Table 1B, p. 4, row 10; `ORC-G7QFOD2PDW` |  |

### Mixing / partial (2)

Table: Mixing / partial, Hg–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of mixing; _printed: S°298(HgTe)_ | 103.83 J/mol (basis unstated)/K | 298.15 | HgTe; _alloy: Hg 0.5, Te 0.5_ | model | [2] Jianrong 1995 | Table 4, p. 13, row 2; `ORC-D3QUZ7OGYZ.06b0fe` |  |
| Entropy of mixing; _printed: S°298(HgTe)_ | 104.6 J/mol (basis unstated)/K | 298.15 | HgTe; _alloy: Hg 0.5, Te 0.5_ | unspecified | [2] Jianrong 1995; _cites ref. 13_ | Table 4, p. 13, row 1; `ORC-S6377M3I2P.e4c60f` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010). [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003)
2. Yang Jianrong, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Thermodynamic and phase diagram assessment of the Cd-Te and Hg-Te systems, Calphad 19, 399-414 (1995). [doi:10.1016/0364-5916(95)00038-g](https://doi.org/10.1016/0364-5916%2895%2900038-g)

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
