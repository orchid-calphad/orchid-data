# Pb–Tl system

> Pb–Tl system: 6 accepted literature values (invariant reaction 4, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-TL.html · Markdown: https://data.orchid-project.org/systems/PB-TL.md

6 accepted literature values from 1 paper(s) (model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-TL.json) · [CSV](https://data.orchid-project.org/systems/PB-TL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-TL) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-TL/PbTl-01Fri-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/PB-TL.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PB-TL.html) · [Markdown](https://data.orchid-project.org/systems/PB-TL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbTl-01Fri-LB.tdb | S.G. Fries, I. Ansara, H.L. Lukas, J. Alloys Compd., 320, 228-33(2001). [doi:10.1016/S0925-8388(00)01492-4](https://doi.org/10.1016/S0925-8388%2800%2901492-4) | `dd4f1c557a9b7253b2c666451e38a35788a38a484aa4f26c801c826da1f05449` | [viewer](https://orchid-project.org/phase-diagrams/#PB-TL/PbTl-01Fri-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbTl-01Fri-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbTl-01Fri-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbTl-01Fri-LB.tdb | 585.03 | FCC_A1 (x(Tl) 0.88918) + BCC_A2 (x(Tl) 0.93658) + LIQUID (x(Tl) 0.9437) |
| PbTl-01Fri-LB.tdb | 443.19 | FCC_A1 (x(Tl) 0.90208) + BCC_A2 (x(Tl) 0.94939) + HCP_A3 (x(Tl) 0.95712) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-TL.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-TL.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pb–Tl system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 585 | peritectic |  | model | [1] Fries 2001 | p. 1; `ORC-2TLWAZB2OX.d1f6f3` | “The bcc solid solution forms peritectically at 585 K from Tl-rich liquid and fcc phases and decomposes eutectoidally at about 453 K into Tl-rich fcc and hcp phases.” |
| 585 | peritectic: liquid+fcc⇌bcc | liquid: Tl 0.944; fcc: Tl 0.889; bcc: Tl 0.937 | model | [1] Fries 2001 | Table 4, p. 4, row 2; `ORC-VOUAKGHASI` |  |
| 453 | eutectoid |  | model | [1] Fries 2001 | p. 1; `ORC-2TLWAZB2OX.4e3999` | “The bcc solid solution forms peritectically at 585 K from Tl-rich liquid and fcc phases and decomposes eutectoidally at about 453 K into Tl-rich fcc and hcp phases.” |
| 443.2 | eutectoid: bcc⇌hcp+fcc | bcc: Tl 0.949; hcp: Tl 0.957; fcc: Tl 0.902 | model | [1] Fries 2001 | Table 4, p. 4, row 3; `ORC-PHFXKS5MVM` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Pb–Tl system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 651.1 K | 651.1 | congruent melting: liquid⇌fcc; _liquid: Tl 0.625; fcc: Tl 0.625_ | model | [1] Fries 2001 | Table 4, p. 4, row 1; `ORC-J74RTKVZPR` |  |
| Phase transition | 653 K | 653 | congruent transformation | model | [1] Fries 2001 | p. 1; `ORC-TFA644YZ47` | “The liquidus presents a maximum, where the fcc phase melts congruently at 653 K and x Tl 50.625.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.G Fries, I Ansara, H.L Lukas, Thermodynamic optimisation of the Pb–Tl binary system, Journal of Alloys and Compounds 320, 228-233 (2001). [doi:10.1016/s0925-8388(00)01492-4](https://doi.org/10.1016/s0925-8388%2800%2901492-4)

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
