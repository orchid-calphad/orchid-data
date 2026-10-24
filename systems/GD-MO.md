# Gd–Mo system

> Gd–Mo system: 20 accepted literature values (invariant reaction 11, phase equilibrium 5, phase transition 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GD-MO.html · Markdown: https://data.orchid-project.org/systems/GD-MO.md

20 accepted literature values from 2 paper(s) (experimental 12, model 7, unspecified 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GD-MO.json) · [CSV](https://data.orchid-project.org/systems/GD-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GD-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GD-MO/GdMo-01Zin-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/GD-MO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GD-MO.html) · [Markdown](https://data.orchid-project.org/systems/GD-MO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 7 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 11 |
| phase transition | 4 |
| phase equilibrium | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GdMo-01Zin-LB.tdb | M. Zinkevich, N. Mattern, H.J. Seifert, J. Phase Equilib, 22, 43-50(2001). [doi:10.1361/105497101770339283](https://doi.org/10.1361/105497101770339283) | `4b52fdb3b73f0b2a83faa8b952f9280bbdfecafa6119b86e3ea9167aebaa26bf` | [viewer](https://orchid-project.org/phase-diagrams/#GD-MO/GdMo-01Zin-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdMo-01Zin-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdMo-01Zin-LB.json) |
| GdMo-02Zin.tdb | M. Zinkevich, N. Mattern, H.-J. Seifert, E. Gmelin, Scand. J. Metall., 31, 34-51(2002). [doi:10.1034/j.1600-0692.2002.311310106.x](https://doi.org/10.1034/j.1600-0692.2002.311310106.x) | `f92d0b1a1c5e7b57c05e2112491316f9a1defaebd7921a57c5557293ae3d1015` | [viewer](https://orchid-project.org/phase-diagrams/#GD-MO/GdMo-02Zin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdMo-02Zin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdMo-02Zin.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GdMo-01Zin-LB.tdb | 2745.15 | LIQUID (x(Mo) 0.32477) + LIQUID#2 (x(Mo) 0.85296) + BCC_A2 (x(Mo) 0.99498) |
| GdMo-01Zin-LB.tdb | 1571.83 | BCC_A2#2 (x(Mo) 0.00482) + LIQUID (x(Mo) 0.01161) + BCC_A2 (x(Mo) 0.99978) |
| GdMo-01Zin-LB.tdb | 1489.35 | HCP_A3 (x(Mo) 0) + BCC_A2#2 (x(Mo) 0.00357) + BCC_A2 (x(Mo) 0.99986) |
| GdMo-02Zin.tdb | 2745.15 | LIQUID (x(Mo) 0.32477) + LIQUID#2 (x(Mo) 0.85296) + BCC_A2 (x(Mo) 0.99498) |
| GdMo-02Zin.tdb | 1571.83 | BCC_A2#2 (x(Mo) 0.00482) + LIQUID (x(Mo) 0.01161) + BCC_A2 (x(Mo) 0.99978) |
| GdMo-02Zin.tdb | 1507.35 | HCP_A3 (x(Mo) 0.00372) + BCC_A2 (x(Mo) 0.00382) + BCC_A2#2 (x(Mo) 0.99985) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GD/GD-MO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GD/GD-MO.json) · [CALPHAD hull GdMo-01Zin-LB](https://data.orchid-project.org/hulls/calphad-sgte/GD/GD-MO--GdMo-01Zin-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Gd–Mo system (11)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2745 | monotectic: Liquid I -> Liquid II + bcc-Mo | Liquid I: Mo 0.853; Liquid II: Mo 0.325; bcc-Mo: Mo 0.995 | model | [1] Zinkevich 2001 | Table 5, p. 7, row 2; `ORC-FMPPI34O4X` |  |
| 2745 | monotectic: liquid I -> liquid II + (Mo) | liquid I: Mo 0.853; liquid II: Mo 0.325; (Mo): Mo 0.995 | model | [2] Zinkevich 2002; _cites Zinkevich 1999_ | Table 4, p. 5, row 2; `ORC-MLUADCKNQ5` |  |
| 2743 | monotectic: liquid I -> liquid II + (Mo) | liquid I: Mo 0.9; (Mo): Mo 0.9906 | experimental | [2] Zinkevich 2002; _cites Brewer 1980_ | Table 4, p. 5, row 1; `ORC-4P6D5GUGG2` |  |
| 2737 | monotectic: Liquid I -> Liquid II + bcc-Mo | Liquid I: Mo 0.9; bcc-Mo: Mo 0.9906 | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | Table 5, p. 7, row 1; `ORC-TOM5CE3V7R` |  |
| 1573 | eutectic: liquid II -> (Mo) + bccGd | liquid II: Mo 0.0117; (Mo): Mo 0.99978; bccGd: Mo 0.0048 | model | [2] Zinkevich 2002; _cites Zinkevich 1999_ | Table 4, p. 5, row 4; `ORC-ILOFHVN564` |  |
| 1573 | eutectic: liquid II -> (Mo) + bccGd | liquid II: Mo 0.03; (Mo): Mo 0.999; bccGd: Mo 0.001 | experimental | [2] Zinkevich 2002; _cites Brewer 1980_ | Table 4, p. 5, row 3; `ORC-QWJNUPIIGN` |  |
| 1572 | eutectic: Liquid II -> bcc-Mo + bcc-Gd | Liquid II: Mo 0.0116; bcc-Mo: Mo 0.99978; bcc-Gd: Mo 0.0048 | model | [1] Zinkevich 2001 | Table 5, p. 7, row 4; `ORC-FDX7GT2QY2` |  |
| 1572 | eutectic: Liquid II -> bcc-Mo + bcc-Gd | Liquid II: Mo 0.03 | unspecified | [1] Zinkevich 2001; _cites Chuang 1966_ | Table 5, p. 7, row 3; `ORC-IK662HFORS` |  |
| 1534 | peritectoid: bccGd + (Mo) -> hcpGd | bccGd: Mo 0.0042; (Mo): Mo 0.99982; hcpGd: Mo 0.0041 | model | [2] Zinkevich 2002; _cites Zinkevich 1999_ | Table 4, p. 5, row 6; `ORC-TJJPONQ4TU` |  |
| 1530 | peritectoid: bccGd + (Mo) -> hcpGd |  | experimental | [2] Zinkevich 2002; _cites Brewer 1980_ | Table 4, p. 5, row 5; `ORC-LPWXLE2QJW` |  |
| 1489 | eutectoid: bcc-Gd + bcc-Mo -> hcp-Gd | bcc-Gd: Mo 0.0036; bcc-Mo: Mo 0.99986; hcp-Gd: Mo 0 | model | [1] Zinkevich 2001 | Table 5, p. 7, row 5; `ORC-HJMLKH6BIQ` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Gd–Mo system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1489 K | 1489 | other: bcc-Gd ⫹ bcc-Mo ⇔ hcp-Gd | model | [1] Zinkevich 2001 | p. 7; `ORC-TTLMUDTGRV` | “A eutectoid invariant reaction bcc-Gd ⫹ bcc-Mo ⇔ hcp-Gd has been predicted at T ⫽ 1489 K (Fig. 2b, Table 5).” |
| Phase transition | 1873 K | 1873 | other | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | p. 2; `ORC-FCT4EHHLP2.af2d9b` | “The bcc-Mo solidus composition increases from 0.09 at.% Gd at 1873 K to 0.94 at.% Gd at 2783 K and then decreases to 0.05 at.% Gd at 2843 K.” |
| Phase transition | 2783 K | 2783 | other | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | p. 2; `ORC-FCT4EHHLP2.b7e8b1` | “The bcc-Mo solidus composition increases from 0.09 at.% Gd at 1873 K to 0.94 at.% Gd at 2783 K and then decreases to 0.05 at.% Gd at 2843 K.” |
| Phase transition | 2843 K | 2843 | other | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | p. 2; `ORC-FCT4EHHLP2.861725` | “The bcc-Mo solidus composition increases from 0.09 at.% Gd at 1873 K to 0.94 at.% Gd at 2783 K and then decreases to 0.05 at.% Gd at 2843 K.” |

### Phase equilibrium (5)

Table: Phase equilibrium, Gd–Mo system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1572 | Liquid II; _Liquid II: Gd 0.97, Mo 0.03_ | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | Table 2, p. 3, row 2; `ORC-USLOFB5ZKR` |  |
| Phase composition |  | 1873 | bcc-Mo; _bcc-Mo: Gd 9.000e-4, Mo 0.9991_ | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | Table 2, p. 3, row 3; `ORC-Q5HKM7WB2H` |  |
| Phase composition |  | 2737 | Liquid I + bcc-Mo; _Liquid I: Gd 0.1, Mo 0.9; bcc-Mo: Gd 0.0094, Mo 0.9906_ | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | Table 2, p. 3, row 1; `ORC-RJYO6DSFXG` |  |
| Phase composition |  | 2783 | bcc-Mo; _bcc-Mo: Gd 0.0094, Mo 0.9906_ | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | Table 2, p. 3, row 4; `ORC-SDFS6VTJXC` |  |
| Phase composition |  | 2843 | bcc-Mo; _bcc-Mo: Gd 5.000e-4, Mo 0.9995_ | experimental | [1] Zinkevich 2001; _cites Chuang 1966_ | Table 2, p. 3, row 5; `ORC-54EL7CGPEA` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. Zinkevich, N. Mattern, H. J. Seifer, Thermodynamic assessment of Gd-Zr and Gd-Mo systems, JPE 22, 43-50 (2001). [doi:10.1361/105497101770339283](https://doi.org/10.1361/105497101770339283)
2. Matvei Zinkevich, Norbert Mattern, Hans‐Jürgen Seifert, Eberhard Gmelin, A thermodynamic assessment of the Fe‐Gd‐Mo system, Scand Jof Metallurgy 31, 34-51 (2002). [doi:10.1034/j.1600-0692.2002.311310106.x](https://doi.org/10.1034/j.1600-0692.2002.311310106.x)

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
