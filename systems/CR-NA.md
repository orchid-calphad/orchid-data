# Cr–Na system

> Cr–Na system: 1 accepted literature values (phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-NA.html · Markdown: https://data.orchid-project.org/systems/CR-NA.md

1 accepted literature values from 1 paper(s) (model 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-NA.json) · [CSV](https://data.orchid-project.org/systems/CR-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-NA/CrNa-12Hao.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CR-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-NA.html) · [Markdown](https://data.orchid-project.org/systems/CR-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrNa-12Hao.tdb | D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang, B. Hu, Y. Du, J. Mining Metall. B, 48, 273-82(2012). [doi:10.2298/JMMB120113024H](https://doi.org/10.2298/JMMB120113024H) | `aa6902c8b70420ae90e93782ed8f3c73bd70663537d2b743f04de81c91a24e4f` | [viewer](https://orchid-project.org/phase-diagrams/#CR-NA/CrNa-12Hao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrNa-12Hao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrNa-12Hao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrNa-12Hao.tdb | 2150.45 | BCC_A2 (x(Na) 0.03587) + LIQUID#2 (x(Na) 0.05779) + LIQUID (x(Na) 0.94221) |
| CrNa-12Hao.tdb | 370.87 | BCC_A2#2 (x(Na) 0) + LIQUID (x(Na) 1) + BCC_A2 (x(Na) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-NA.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Cr–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 371.05 K | 371.05 | Liquid ↔ Bcc_A2(Na) + Bcc_A2(Cr) | model | [1] Hao 2012 | p. 8; `ORC-PIVY3TBVFS` | “The temperatures of the three invariant reactions, Acknowledgements Liquid(Cr) ↔ Gas + Bcc_A2(Cr), Gas + Bcc_A2(Cr) ↔ Liquid, and Liquid ↔ The financial support from the National Basic Bcc_A2(Na) + Bcc_A2(Cr), are calculated Research Program of China (Grant No. to be 1906 °C, 886 °C, and 97.9 °C 2011CB610401) and the National Natural respectively.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang et al., Thermodynamic modeling of the Na-X (X = Si, Ag, Cu, Cr) systems, J min metall B Metall 48, 273-282 (2012). [doi:10.2298/jmmb120113024h](https://doi.org/10.2298/jmmb120113024h)

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
