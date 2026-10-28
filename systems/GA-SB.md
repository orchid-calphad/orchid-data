# Ga–Sb system

> Ga–Sb system: 8 accepted literature values (heat capacity / entropy / enthalpy 4, formation 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-SB.html · Markdown: https://data.orchid-project.org/systems/GA-SB.md

8 accepted literature values from 1 paper(s) (model 6, unspecified 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-SB.json) · [CSV](https://data.orchid-project.org/systems/GA-SB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-SB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-SB/GaSb-94Ans-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/GA-SB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-SB.html) · [Markdown](https://data.orchid-project.org/systems/GA-SB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 6 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 4 |
| heat capacity / entropy / enthalpy | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaSb-94Ans-LB.tdb | I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida, M. Hillert, B. Sundman, B.B. Argent, A. Watson, T.G. Chart, T. Anderson, Calphad, 18, 177-222(1994). [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) | `e8edb2feeeca4f9a25d7f513537763e26a48e59b60a644e0fe4fbfe3aabf8157` | [viewer](https://orchid-project.org/phase-diagrams/#GA-SB/GaSb-94Ans-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaSb-94Ans-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaSb-94Ans-LB.json) |
| GaSb-97Xie.tdb | Y. Xie, Z. Qiao, X. Xing, C. Wang, J. Shen, Rare Met., 16, 81-89(1997). | `acd6f8f0fe5b754fa92920979c58b851cb791e354b3e8ccad7a0ec95571ce5cb` | [viewer](https://orchid-project.org/phase-diagrams/#GA-SB/GaSb-97Xie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaSb-97Xie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaSb-97Xie.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaSb-94Ans-LB.tdb | 862.12 | ZINCBLENDE_B3 (x(Sb) 0.5) + LIQUID (x(Sb) 0.88359) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| GaSb-94Ans-LB.tdb | 862.12 | ZINCBLENDE_B3 (x(Sb) 0.5) + LIQUID (x(Sb) 0.88284) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| GaSb-94Ans-LB.tdb | 862.12 | ZINCBLENDE_B3 (x(Sb) 0.5) + LIQUID (x(Sb) 0.88326) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| GaSb-94Ans-LB.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Sb) 0) + LIQUID (x(Sb) 0) + ZINCBLENDE_B3 (x(Sb) 0.5) |
| GaSb-97Xie.tdb | 857.49 | ZINCBLENDE_B3 (x(Sb) 0.5) + LIQUID (x(Sb) 0.88677) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| GaSb-97Xie.tdb | 857.49 | ZINCBLENDE_B3 (x(Sb) 0.5) + LIQUID (x(Sb) 0.88621) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| GaSb-97Xie.tdb | 857.49 | ZINCBLENDE_B3 (x(Sb) 0.5) + LIQUID (x(Sb) 0.88672) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| GaSb-97Xie.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Sb) 0) + LIQUID (x(Sb) 0) + ZINCBLENDE_B3 (x(Sb) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-SB.json) · [CALPHAD hull GaSb-94Ans-LB](https://data.orchid-project.org/hulls/calphad-sgte/GA/GA-SB--GaSb-94Ans-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ga–Sb system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| GaSb |  | -44.84 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 19, row 22; `ORC-JR6EHAD7OF.083dad` |  |
| GaSb |  | -42.8 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Hultgren 1973_ | Table AI, p. 19, row 24; `ORC-WRLF6MZNU2` |  |
| GaSb |  | -41.8 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Wagman 1968_ | Table AI, p. 19, row 23; `ORC-PJY4ZQYYI4` |  |
| GaSb |  | -41.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Onderka 2002; _cites Kaufman 1981_ | Table AI, p. 19, row 21; `ORC-PKBXETSVCR.75bc22` |  |

## Other properties

### Heat capacity / entropy / enthalpy (4)

Table: Heat capacity / entropy / enthalpy, Ga–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S°298_ | 72.89 J/mol-formula K | 298.15 | GaSb | model | [1] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 19, row 22; `ORC-JR6EHAD7OF.fe2fe8` |  |
| Heat capacity; _printed: Cp,298_ | 47.61 J/mol (basis unstated)/K | 298.15 | GaSb | model | [1] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 19, row 22; `ORC-JR6EHAD7OF.99fc29` |  |
| sm fusion; _printed: ΔmS_ | 67.1 J/mol-formula K | 981 | GaSb; _alloy: Ga 0.5, Sb 0.5_ | model | [1] Onderka 2002; _cites Kaufman 1981_ | Table AI, p. 19, row 21; `ORC-PKBXETSVCR.4084f0` |  |
| sm fusion; _printed: ΔmS_ | 70.55 J/mol-formula K | 982.6 | GaSb; _alloy: Ga 0.5, Sb 0.5_ | model | [1] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 19, row 22; `ORC-JR6EHAD7OF.aceb96` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. B. Onderka, J. Unland, R. Schmid-Fetzer, Thermodynamics and phase stability in the In–N system, J. Mater. Res. 17, 3065-3083 (2002). [doi:10.1557/jmr.2002.0445](https://doi.org/10.1557/jmr.2002.0445)

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
