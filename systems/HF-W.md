# Hf–W system

> Hf–W system: 5 accepted literature values (formation 3, crystal structure 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-W.html · Markdown: https://data.orchid-project.org/systems/HF-W.md

5 accepted literature values from 2 paper(s) (experimental 1, model 3, DFT 1); 2 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-W.json) · [CSV](https://data.orchid-project.org/systems/HF-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-W/HfW-02Sha-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/HF-W.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HF-W.html) · [Markdown](https://data.orchid-project.org/systems/HF-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 3 |
| DFT | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 3 |
| crystal structure | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfW-02Sha-LB.tdb | G. Shao, Intermetallics, 10, 429-34(2002). [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) | `078db40d3d1acdff57b462f15eac22fc75242db8dadb9a6a27c002a3104918d9` | [viewer](https://orchid-project.org/phase-diagrams/#HF-W/HfW-02Sha-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfW-02Sha-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfW-02Sha-LB.json) |
| HfW-12Lie.tdb | A.C. Lieser, C.L. Zacherl, A. Saengdeejing, Z.-K. Liu, L.J. Kecskes, Calphad, 38, 92-99(2012). [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005) | `8ac53fc523b760014d23a34f80e81c70ad549946918cba3eee6db63198df4f78` | [viewer](https://orchid-project.org/phase-diagrams/#HF-W/HfW-12Lie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfW-12Lie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfW-12Lie.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfW-02Sha-LB.tdb | 2771.05 | LIQUID (x(W) 0.52741) + C15_LAVES (x(W) 0.6662) + BCC_A2 (x(W) 0.8924) |
| HfW-02Sha-LB.tdb | 2213.68 | BCC_A2 (x(W) 0.13032) + LIQUID (x(W) 0.21697) + C15_LAVES (x(W) 0.64708) |
| HfW-02Sha-LB.tdb | 1718.04 | HCP_A3 (x(W) 0.01514) + BCC_A2 (x(W) 0.07512) + C15_LAVES (x(W) 0.64626) |
| HfW-12Lie.tdb | 2806.23 | LIQUID (x(W) 0.56433) + C15_LAVES (x(W) 0.66291) + BCC_A2 (x(W) 0.92394) |
| HfW-12Lie.tdb | 2222.06 | BCC_A2 (x(W) 0.12949) + LIQUID (x(W) 0.20418) + C15_LAVES (x(W) 0.65502) |
| HfW-12Lie.tdb | 1826.4 | HCP_A3 (x(W) 3.500e-4) + BCC_A2 (x(W) 0.04381) + C15_LAVES (x(W) 0.65916) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-W.json) · [CALPHAD hull HfW-02Sha-LB](https://data.orchid-project.org/hulls/calphad-sgte/HF/HF-W--HfW-02Sha-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Hf–W system (3)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| HfW2–15 | [HfW2](https://data.orchid-project.org/compounds/HfW2.html) | -14.1 kJ/mol-atom |  | model | -16.679 (mp-aaaaacbw) | -16.555 (oqmd-17394) | [1] Shao 2002 | Table 1, p. 5, row 3; `ORC-ERH43UKWJO` |  |
| HfW2–15 | [HfW2](https://data.orchid-project.org/compounds/HfW2.html) | -8 kJ/mol-atom |  | model | -16.679 (mp-aaaaacbw) | -16.555 (oqmd-17394) | [1] Shao 2002; _cites de Boer FR 1989_ | Table 1, p. 5, row 2; `ORC-G4IYWBQVPV` |  |
| HfW2–15 | [HfW2](https://data.orchid-project.org/compounds/HfW2.html) | -3 kJ/mol-atom |  | model | -16.679 (mp-aaaaacbw) | -16.555 (oqmd-17394) | [1] Shao 2002; _cites Lee 1986_ [doi](https://doi.org/10.1016/0364-5916%2886%2990010-6) | Table 1, p. 5, row 1; `ORC-R3ASY5BJKP` |  |

## Other properties

### Crystal structure (2)

Table: Crystal structure, Hf–W system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 7.617 Å |  | HfW2; _alloy: W 0.666667_ | DFT | [2] Lieser 2012 | Table 1, p. 4, row 10; `ORC-EHQ7B7BI7N` |  |
| Lattice a | 7.593 Å | 298.15 | HfW2; _alloy: W 0.666667_ | experimental | [2] Lieser 2012; _cites Braun 1960_ | Table 1, p. 4, row 11; `ORC-G4UU5D4VX4` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. G. Shao, Thermodynamic assessment of the Hf–Mo and Hf–W systems, Intermetallics 10, 429-434 (2002). [doi:10.1016/s0966-9795(02)00017-1](https://doi.org/10.1016/s0966-9795%2802%2900017-1)
2. Alyson C. Lieser, Chelsey L. Zacherl, Arkapol Saengdeejing, Zi-Kui Liu, Laszlo J. Kecskes, First-principles calculations and thermodynamic re-modeling of the Hf–W system, Calphad 38, 92-99 (2012). [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005)

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
