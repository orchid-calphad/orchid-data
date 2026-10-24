# Ba–Ti system

> Ba–Ti system: 29 accepted literature values (crystal structure 15, mixing / partial 11, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-TI.html · Markdown: https://data.orchid-project.org/systems/BA-TI.md

29 accepted literature values from 1 paper(s) (experimental 1, model 2, DFT 26); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-TI.json) · [CSV](https://data.orchid-project.org/systems/BA-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-TI/BaTi-07Sha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/BA-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BA-TI.html) · [Markdown](https://data.orchid-project.org/systems/BA-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |
| DFT | 26 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| mixing / partial | 11 |
| crystal structure | 15 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaTi-07Sha.tdb | S. Shang, Z.-J. Liu, Z.-K. Liu, J. Alloys Compd., 430, 188-93(2007). [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096) | `c2404dc113a3c952165d38dca9b48a2e6e34224410c55f5760d5ef9b9273279d` | [viewer](https://orchid-project.org/phase-diagrams/#BA-TI/BaTi-07Sha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaTi-07Sha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaTi-07Sha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaTi-07Sha.tdb | 1929.11 | LIQUID (x(Ti) 0.00552) + LIQUID#2 (x(Ti) 0.99448) + BCC_A2 (x(Ti) 1) |
| BaTi-07Sha.tdb | 1929.11 | LIQUID#2 (x(Ti) 0.00552) + LIQUID (x(Ti) 0.99448) + BCC_A2 (x(Ti) 1) |
| BaTi-07Sha.tdb | 1154.99 | LIQUID (x(Ti) 2.300e-4) + HCP_A3 (x(Ti) 1) + BCC_A2 (x(Ti) 1) |
| BaTi-07Sha.tdb | 1154.99 | LIQUID (x(Ti) 2.300e-4) + BCC_A2 (x(Ti) 1) + HCP_A3 (x(Ti) 1) |
| BaTi-07Sha.tdb | 1154.99 | LIQUID (x(Ti) 2.300e-4) + HCP_A3 (x(Ti) 1) + BCC_A2 (x(Ti) 1) |
| BaTi-07Sha.tdb | 1000 | BCC_A2 (x(Ti) 0) + LIQUID (x(Ti) 0) + HCP_A3 (x(Ti) 1) |
| BaTi-07Sha.tdb | 999.92 | BCC_A2 (x(Ti) 0) + LIQUID (x(Ti) 7.000e-5) + HCP_A3 (x(Ti) 1) |
| BaTi-07Sha.tdb | 999.92 | BCC_A2 (x(Ti) 0) + LIQUID (x(Ti) 6.000e-5) + HCP_A3 (x(Ti) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ba–Ti system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1155 | peritectic: bcc (Ti) + liquid → hcp (Ti) |  | model | [1] Shang 2007 | p. 5; `ORC-7HBDVQOSYT.9b5a7b` | “The invariant reactions in the Ba-Ti system are also listed in Table 4 with the eutectic temperature of the reaction liquid → hcp (Ti) + bcc (Ba) at 1000 K close to the estimation of 1002 K from Chase \[12\], the peritectic point of the reaction bcc (Ti) + liquid → hcp (Ti) of 1155 K at the allotropic transformation point between bcc (Ti) and hcp (Ti).” |
| 1155 | peritectic: bcc (Ti) + liquid → hcp (Ti) |  | experimental | [1] Shang 2007; _cites Alidzhanov 1978_ | p. 1; `ORC-OW64X6QP5W` | “The peritectic point of the reaction bcc (Ti) + liquid → hcp (Ti) was measured approximately at 1155 K \[11\], which is close to the allotropic transformation point of bcc (Ti) ↔ hcp (Ti).” |
| 1000 | eutectic: liquid → hcp (Ti) + bcc (Ba) |  | model | [1] Shang 2007 | p. 5; `ORC-7HBDVQOSYT.c0e3a2` | “The invariant reactions in the Ba-Ti system are also listed in Table 4 with the eutectic temperature of the reaction liquid → hcp (Ti) + bcc (Ba) at 1000 K close to the estimation of 1002 K from Chase \[12\], the peritectic point of the reaction bcc (Ti) + liquid → hcp (Ti) of 1155 K at the allotropic transformation point between bcc (Ti) and hcp (Ti).” |

## Other properties

### Mixing / partial (11)

Table: Mixing / partial, Ba–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔH_ | 101.736 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ti 0.5_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 18; `ORC-YYVHXL2OKB` |  |
| Enthalpy of mixing; _printed: ΔH_ | 76.684 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 24; `ORC-3KOGNBPLVY` |  |
| Enthalpy of mixing; _printed: ΔH_ | 67.674 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 33; `ORC-4FQVJUILNX` |  |
| Enthalpy of mixing; _printed: ΔH_ | 67.674 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 22; `ORC-GICCBXPIHT` |  |
| Enthalpy of mixing; _printed: ΔH_ | 95.688 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ti 0.5_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 23; `ORC-JKMQLRBPSY` |  |
| Enthalpy of mixing; _printed: ΔH_ | 76.684 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 34; `ORC-MOVG7JCBYW` |  |
| Enthalpy of mixing; _printed: ΔH_ | 99.832 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ti 0.5_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 28; `ORC-37UKO6JZMI` |  |
| Enthalpy of mixing; _printed: ΔH_ | 68.979 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 35; `ORC-DEJ64IFSTL` |  |
| Enthalpy of mixing; _printed: ΔH_ | 81.87 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 29; `ORC-J366A25WGD` |  |
| Enthalpy of mixing; _printed: ΔH_ | 68.979 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 27; `ORC-L43MJTV7TE` |  |
| Enthalpy of mixing; _printed: ΔH_ | 81.87 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 36; `ORC-SMVMFG276I` |  |

### Crystal structure (15)

Table: Crystal structure, Ba–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 4.454 Å | 0 | Bcc; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 17; `ORC-4GKQFHU5NQ` |  |
| Lattice a; _printed: a_ | 3.517 Å | 0 | Bcc; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 32; `ORC-LNCLUDTOKS` |  |
| Lattice a; _printed: a_ | 3.517 Å | 0 | Bcc; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 19; `ORC-LX6XBE3LQ6` |  |
| Lattice a; _printed: a_ | 4.454 Å | 0 | Bcc; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 31; `ORC-QWYJQLVSPQ` |  |
| Lattice a; _printed: a_ | 3.923 Å | 0 | Bcc; _alloy: Ti 0.5_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 18; `ORC-VCNM3JOHBI` |  |
| Lattice a; _printed: a_ | 4.917 Å | 0 | Fcc; _alloy: Ti 0.5_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 23; `ORC-5F5QLQLPH6` |  |
| Lattice a; _printed: a_ | 4.434 Å | 0 | Fcc; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 24; `ORC-BDFKLHHOH7` |  |
| Lattice a; _printed: a_ | 5.564 Å | 0 | Fcc; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 33; `ORC-HZZVSOQ6BP` |  |
| Lattice a; _printed: a_ | 5.564 Å | 0 | Fcc; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 22; `ORC-ODCYK7VZVB` |  |
| Lattice a; _printed: a_ | 4.434 Å | 0 | Fcc; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 34; `ORC-RZNO5PKBNQ` |  |
| Lattice a; _printed: a_ | 3.143 Å | 0 | Hcp; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 29; `ORC-7WEXOUDGNT` |  |
| Lattice a; _printed: a_ | 3.954 Å | 0 | Hcp; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 27; `ORC-M5KZXC45XP` |  |
| Lattice a; _printed: a_ | 3.529 Å | 0 | Hcp; _alloy: Ti 0.5_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 28; `ORC-NVDZCBLY5E` |  |
| Lattice a; _printed: a_ | 3.143 Å | 0 | Hcp; _alloy: Ti 0.75_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 36; `ORC-PS4WV4ACJO` |  |
| Lattice a; _printed: a_ | 3.954 Å | 0 | Hcp; _alloy: Ti 0.25_ | DFT | [1] Shang 2007 | Table 2, p. 2, row 35; `ORC-U23IZG4OHJ` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shunli Shang, Zhi-Jie Liu, Zi-Kui Liu, Thermodynamic modeling of the Ba–Ni–Ti system, Journal of Alloys and Compounds 430, 188-193 (2007). [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096)

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
