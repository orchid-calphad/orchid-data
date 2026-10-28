# Pd–Sc system

> Pd–Sc system: 9 accepted literature values (formation 7, heat capacity / entropy / enthalpy 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PD-SC.html · Markdown: https://data.orchid-project.org/systems/PD-SC.md

9 accepted literature values from 1 paper(s) (model 9); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PD-SC.json) · [CSV](https://data.orchid-project.org/systems/PD-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PD-SC) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PD-SC/PdSc-02Du.json) · [phases (9)](https://data.orchid-project.org/phases/pages/PD-SC.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PD-SC.html) · [Markdown](https://data.orchid-project.org/systems/PD-SC.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 7 |
| heat capacity / entropy / enthalpy | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PdSc-02Du.tdb | Z. Du, C. Li, L. Lu, Z. Metallkd., 93, 277-80(2002). [doi:10.3139/146.020277](https://doi.org/10.3139/146.020277) | `63a13cc650067f3a320c12c6072729e5e1185cd540abf9504938b019c918cded` | [viewer](https://orchid-project.org/phase-diagrams/#PD-SC/PdSc-02Du.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PdSc-02Du.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PdSc-02Du.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PdSc-02Du.tdb | 1722.69 | FCC_A1 (x(Sc) 0.14915) + LIQUID (x(Sc) 0.17997) + PD3SC_L12 (x(Sc) 0.25) |
| PdSc-02Du.tdb | 1702.45 | PD3SC_L12 (x(Sc) 0.25) + PD2SC (x(Sc) 0.33333) + LIQUID (x(Sc) 0.33672) |
| PdSc-02Du.tdb | 1702.45 | PD3SC_L12 (x(Sc) 0.25) + PD2SC (x(Sc) 0.33333) + LIQUID (x(Sc) 0.33643) |
| PdSc-02Du.tdb | 1687.38 | PD2SC (x(Sc) 0.33333) + LIQUID (x(Sc) 0.37235) + PDSC_B2 (x(Sc) 0.50006) |
| PdSc-02Du.tdb | 1687.38 | PD2SC (x(Sc) 0.33333) + LIQUID (x(Sc) 0.37227) + PDSC_B2 (x(Sc) 0.50006) |
| PdSc-02Du.tdb | 1608 | LIQUID (x(Sc) 0.9335) + BCC_A2 (x(Sc) 1) + HCP_A3 (x(Sc) 1) |
| PdSc-02Du.tdb | 1608 | LIQUID (x(Sc) 0.93357) + HCP_A3 (x(Sc) 1) + BCC_A2 (x(Sc) 1) |
| PdSc-02Du.tdb | 1472.82 | PDSC_B2 (x(Sc) 0.50869) + PDSC2 (x(Sc) 0.66667) + LIQUID (x(Sc) 0.69881) |
| PdSc-02Du.tdb | 1312.84 | PDSC2 (x(Sc) 0.66667) + PDSC4 (x(Sc) 0.8) + LIQUID (x(Sc) 0.80266) |
| PdSc-02Du.tdb | 1312.83 | PDSC2 (x(Sc) 0.66667) + PDSC4 (x(Sc) 0.8) + LIQUID (x(Sc) 0.80291) |
| PdSc-02Du.tdb | 1312.83 | PDSC2 (x(Sc) 0.66667) + PDSC4 (x(Sc) 0.8) + LIQUID (x(Sc) 0.80297) |
| PdSc-02Du.tdb | 1273.15 | PDSC4 (x(Sc) 0.8) + LIQUID (x(Sc) 0.86669) + HCP_A3 (x(Sc) 1) |
| PdSc-02Du.tdb | 1273.15 | PDSC4 (x(Sc) 0.8) + LIQUID (x(Sc) 0.86682) + HCP_A3 (x(Sc) 1) |
| PdSc-02Du.tdb | 1273.15 | PDSC4 (x(Sc) 0.8) + LIQUID (x(Sc) 0.86682) + HCP_A3 (x(Sc) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PD/PD-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PD/PD-SC.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Pd–Sc system (3)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Pd2Sc | [Pd2Sc](https://data.orchid-project.org/compounds/Pd2Sc.html) | -84.788 kJ/mol-atom | 298.15 | model |  | -85.935 (oqmd-1339201) | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 59; `ORC-SOFT6TG2IB.394726` |  |
| Pd3Sc | [Pd3Sc](https://data.orchid-project.org/compounds/Pd3Sc.html) | -82.174 kJ/mol-atom | 298.15 | model | -82.551 (mp-aaaaadyz) | -82.436 (oqmd-17945) | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 1; `ORC-EGYHIUQGCT.70c09b` |  |
| PdSc | [PdSc](https://data.orchid-project.org/compounds/PdSc.html) | -89.25 kJ/mol-atom | 298.15 | model | -87.586 (mp-aaaaaecz) | -87.551 (oqmd-17944) | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 21; `ORC-7KZ3MPNZND.80afe6` |  |

## Other properties

### Formation (4)

Table: Formation, Pd–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation | 13.61 J/mol-atom/K | 298.15 | PdSc; _alloy: Pd 0.5, Sc 0.5_ | model | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 21; `ORC-7KZ3MPNZND.aef6d4` |  |
| Gibbs energy of formation; _printed: ΔfG_ | -89.6106 kJ/mol-atom | 298.15 | Pd2Sc; _alloy: Pd 0.666667, Sc 0.333333_ | model | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 59; `ORC-SOFT6TG2IB.13af41` |  |
| Gibbs energy of formation; _printed: Gibbs free energy of formation_ | -87.5794 kJ/mol-atom | 298.15 | Pd3Sc; _alloy: Pd 0.75, Sc 0.25_ | model | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 1; `ORC-EGYHIUQGCT.61f570` |  |
| Gibbs energy of formation; _printed: ΔfG_ | -93.3078 kJ/mol-atom | 298.15 | PdSc; _alloy: Pd 0.5, Sc 0.5_ | model | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 21; `ORC-7KZ3MPNZND.74d024` |  |

### Heat capacity / entropy / enthalpy (2)

Table: Heat capacity / entropy / enthalpy, Pd–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: ΔfS_ | 16.175 J/mol-atom/K | 298.15 | Pd2Sc; _alloy: Pd 0.666667, Sc 0.333333_ | model | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 59; `ORC-SOFT6TG2IB.c2a796` |  |
| Entropy; _printed: Entropy of formation_ | 18.13 J/mol-atom/K | 298.15 | Pd3Sc; _alloy: Pd 0.75, Sc 0.25_ | model | [1] Kardellass 2020; _cites Du 2002_ | Table 3, p. 5, row 1; `ORC-EGYHIUQGCT.60d469` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Said Kardellass, Colette Servant, Isabelle Drouelle, Fatima Zahra Chrifi-Alaoui, Mohamed Idbenali, Alyen Abahazem et al., Calphad-type assessment of the Pd-Yb binary system supported by first-principles calculations – Part II: Results, Materials Today: Proceedings 24, 140-150 (2020). [doi:10.1016/j.matpr.2019.08.196](https://doi.org/10.1016/j.matpr.2019.08.196)

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
