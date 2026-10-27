# Ca–Li system

> Ca–Li system: 8 accepted literature values (invariant reaction 6, formation 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-LI.html · Markdown: https://data.orchid-project.org/systems/CA-LI.md

8 accepted literature values from 1 paper(s) (experimental 4, model 3, unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-LI.json) · [CSV](https://data.orchid-project.org/systems/CA-LI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-LI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-LI/CaLi-02Gro-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CA-LI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CA-LI.html) · [Markdown](https://data.orchid-project.org/systems/CA-LI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 3 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| formation | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaLi-02Gro-LB.tdb | J. Groebner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv, D.G. Kevorkov, O.I. Bodak, Thermochim. Acta, 389, 85-94(2002). [doi:10.1016/S0040-6031(01)00842-5](https://doi.org/10.1016/S0040-6031%2801%2900842-5) | `91ea24f374ce086f3997f8e274d9fa664d5ab91fbc512955fafff8bce4cf8642` | [viewer](https://orchid-project.org/phase-diagrams/#CA-LI/CaLi-02Gro-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaLi-02Gro-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaLi-02Gro-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaLi-02Gro-LB.tdb | 642.54 | FCC_A1 (x(Li) 0.06614) + BCC_A2 (x(Li) 0.08624) + LIQUID (x(Li) 0.43535) |
| CaLi-02Gro-LB.tdb | 506.46 | FCC_A1 (x(Li) 0.09604) + LIQUID (x(Li) 0.57162) + CALI2_C14 (x(Li) 0.66667) |
| CaLi-02Gro-LB.tdb | 506.46 | FCC_A1 (x(Li) 0.09611) + LIQUID (x(Li) 0.57192) + CALI2_C14 (x(Li) 0.66667) |
| CaLi-02Gro-LB.tdb | 418.05 | CALI2_C14 (x(Li) 0.66667) + LIQUID (x(Li) 0.9318) + BCC_A2 (x(Li) 0.98724) |
| CaLi-02Gro-LB.tdb | 418.05 | CALI2_C14 (x(Li) 0.66667) + LIQUID (x(Li) 0.93203) + BCC_A2 (x(Li) 0.98729) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-LI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-LI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Li system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 643.15 | βCa = αCa + liquid | βCa: Li 0.09; αCa: Li 0.08; liquid: Li 0.43 | experimental | [1] Gröbner 2002; _cites Bale 1987_ [doi](https://doi.org/10.1007/bf02873196) | Table 1, p. 2, row 1; `ORC-74ZISW3DST` |  |
| 642.65 | βCa = αCa + liquid | βCa: Li 0.086; αCa: Li 0.066; liquid: Li 0.435 | model | [1] Gröbner 2002 | Table 1, p. 2, row 2; `ORC-CFFIWGCX6V` |  |
| 506.55 | Liquid = αCa + CaLi2 | αCa: Li 0.096; CaLi2: Li 0.6667; Liquid: Li 0.571 | model | [1] Gröbner 2002 | Table 1, p. 2, row 4; `ORC-U6JN55NWD3` |  |
| 503.15 | Liquid = αCa + CaLi2 | αCa: Li 0.105; CaLi2: Li 0.6667; Liquid: Li 0.59 | experimental | [1] Gröbner 2002; _cites Bale 1987_ [doi](https://doi.org/10.1007/bf02873196) | Table 1, p. 2, row 3; `ORC-SAN4RXU25Q` |  |
| 418.15 | Liquid = CaLi2 + (Li) | CaLi2: Li 0.6667; (Li): Li 0.987; Liquid: Li 0.932 | model | [1] Gröbner 2002 | Table 1, p. 2, row 6; `ORC-KFHQVSIBMQ` |  |
| 414.15 | Liquid = CaLi2 + (Li) | CaLi2: Li 0.6667; (Li): Li 0.98; Liquid: Li 0.92 | experimental | [1] Gröbner 2002; _cites Bale 1987_ [doi](https://doi.org/10.1007/bf02873196) | Table 1, p. 2, row 5; `ORC-WXIRJKKLXQ` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ca–Li system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CaLi2 |  | -4.5 kJ/mol (basis unstated) ± 1.6 | 298.15 | experimental |  |  | [1] Gröbner 2002 | Table 2, p. 3, row 1; `ORC-CFC6RUPTP5` |  |
| CaLi2 |  | -3.89 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Gröbner 2002 | Table 2, p. 3, row 2; `ORC-IPLMBPCTHB` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Gröbner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv et al., Phase equilibria, calorimetric study and thermodynamic modeling of Mg–Li–Ca alloys, Thermochimica Acta 389, 85-94 (2002). [doi:10.1016/s0040-6031(01)00842-5](https://doi.org/10.1016/s0040-6031%2801%2900842-5)

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
