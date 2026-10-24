# Cr–N system

> Cr–N system: 6 accepted literature values (formation 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-N.html · Markdown: https://data.orchid-project.org/systems/CR-N.md

6 accepted literature values from 1 paper(s) (model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-N.json) · [CSV](https://data.orchid-project.org/systems/CR-N.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-N) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-N/CrN-91Fri-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CR-N.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-N.html) · [Markdown](https://data.orchid-project.org/systems/CR-N.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrN-91Fri-LB.tdb | K. Frisk, Calphad, 15, 79-106(1991). [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) | `ca92d72cc42438d4e7672b18c158d23b7b5f71937b69c4c3ab0f5e4d0a117ae2` | [viewer](https://orchid-project.org/phase-diagrams/#CR-N/CrN-91Fri-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrN-91Fri-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrN-91Fri-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrN-91Fri-LB.tdb | 1956.58 | LIQUID (x(N) 0.18115) + HCP_A3 (x(N) 0.24082) + N2GAS (x(N) 1) |
| CrN-91Fri-LB.tdb | 1956.58 | LIQUID (x(N) 0.1814) + HCP_A3 (x(N) 0.24095) + N2GAS (x(N) 1) |
| CrN-91Fri-LB.tdb | 1920.54 | BCC_A2 (x(N) 0.04835) + LIQUID (x(N) 0.15328) + HCP_A3 (x(N) 0.22559) |
| CrN-91Fri-LB.tdb | 1318.13 | HCP_A3 (x(N) 0.33027) + FCC_A1 (x(N) 0.49571) + N2GAS (x(N) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-N.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-N.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cr–N system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CrN | [CrN](https://data.orchid-project.org/compounds/CrN.html) | -58.6 kJ/mol-atom |  | model | -66.723 (mp-aaacpjap) | -59.652 (oqmd-1229033) | [1] Frisk 1991; _cites Chase 1985_ | Table I, p. 6, row 6; `ORC-UEW4XK4I2V` |  |
| CrN | [CrN](https://data.orchid-project.org/compounds/CrN.html) | -57.3 kJ/mol-atom |  | model | -66.723 (mp-aaacpjap) | -59.652 (oqmd-1229033) | [1] Frisk 1991 | Table I, p. 6, row 8; `ORC-JPD7Y6YZHI` |  |
| ε(Cr2N) | [Cr2N](https://data.orchid-project.org/compounds/Cr2N.html) | -43.1 kJ/mol-atom | 298.15 | model | -48.833 (mp-aaaaamzs) | -43.69 (oqmd-12301) | [1] Frisk 1991 | Table I, p. 6, row 7; `ORC-X5DNFQO4Z2` |  |
| ε(Cr2N) | [Cr2N](https://data.orchid-project.org/compounds/Cr2N.html) | 41.8 kJ/mol-atom | 298.15 | model | -48.833 (mp-aaaaamzs) | -43.69 (oqmd-12301) | [1] Frisk 1991; _cites Chase 1985_ | Table I, p. 6, row 5; `ORC-E4DHBOCKS5` |  |

## Other properties

### Formation (2)

Table: Formation, Cr–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropy of Formation_ | -42.6 J/mol-atom/K | 298.15 | CrN; _alloy: N 0.5_ | model | [1] Frisk 1991 | Table I, p. 6, row 11; `ORC-LLLEMUND23` |  |
| Entropy of formation; _printed: Entropy of Formation_ | -25.7 J/mol-atom/K | 298.15 | ε(Cr2N); _alloy: N 0.333333_ | model | [1] Frisk 1991 | Table I, p. 6, row 10; `ORC-XOXS4E4OI6` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Karin Frisk, A thermodynamic evaluation of the Cr-N, Fe-N, Mo-N and Cr-Mo-N systems, Calphad 15, 79-106 (1991). [doi:10.1016/0364-5916(91)90028-i](https://doi.org/10.1016/0364-5916%2891%2990028-i)

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
