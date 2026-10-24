# Nd–Sr system

> Nd–Sr system: 4 accepted literature values (phase transition 2, invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ND-SR.html · Markdown: https://data.orchid-project.org/systems/ND-SR.md

4 accepted literature values from 1 paper(s) (experimental 1, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ND-SR.json) · [CSV](https://data.orchid-project.org/systems/ND-SR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ND-SR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ND-SR/NdSr-13Xu.json) · [phases (5)](https://data.orchid-project.org/phases/pages/ND-SR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ND-SR.html) · [Markdown](https://data.orchid-project.org/systems/ND-SR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NdSr-13Xu.tdb | G. Xu, Y. Cui, L. Zeng, X. Tao, L. Liu, Z. Jin, Metall. Mater. Trans. A, 44A, 5634-41(2013). [doi:10.1007/s11661-013-2038-7](https://doi.org/10.1007/s11661-013-2038-7) | `0c77639bdc407da20d8a0638d5f908a92898e6697ee6116d56f438deb995031d` | [viewer](https://orchid-project.org/phase-diagrams/#ND-SR/NdSr-13Xu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NdSr-13Xu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NdSr-13Xu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NdSr-13Xu.tdb | 1219.57 | BCC_A2 (x(Sr) 0.05) + LIQUID#2 (x(Sr) 0.08907) + LIQUID (x(Sr) 0.99604) |
| NdSr-13Xu.tdb | 1169.13 | BCC_A2 (x(Sr) 0.04548) + DHCP (x(Sr) 0.06227) + LIQUID (x(Sr) 0.99712) |
| NdSr-13Xu.tdb | 1048.95 | DHCP (x(Sr) 0.04689) + LIQUID (x(Sr) 0.99882) + BCC_A2 (x(Sr) 0.99969) |
| NdSr-13Xu.tdb | 819.82 | DHCP (x(Sr) 0.01696) + BCC_A2 (x(Sr) 0.99997) + FCC_A1 (x(Sr) 1) |
| NdSr-13Xu.tdb | 819.82 | DHCP (x(Sr) 0.01696) + BCC_A2 (x(Sr) 0.99997) + FCC_A1 (x(Sr) 1) |
| NdSr-13Xu.tdb | 819.82 | DHCP (x(Sr) 0.01695) + BCC_A2 (x(Sr) 0.99997) + FCC_A1 (x(Sr) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ND/ND-SR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ND/ND-SR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nd–Sr system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1048 | eutectic: Liq fi DHCP + BCC_A2 |  | model | [1] Xu 2013 | p. 5 | “The reaction Liq fi DHCP + BCC_A2 is predicted to occur at 1048 K (775 C) rather than 1013 K (740 C) in order to avoid an ''improper'' deep eutectic valley\[13\] lying extremely close to pure Sr in view of an updated melting temperature of 1050 K (777 C) for Sr.\[14\]” |
| 1013 | eutectic: Liq fi DHCP + BCC_A2 |  | model | [1] Xu 2013; _cites Okamoto 1993_ [doi](https://doi.org/10.1007/bf02668229) | p. 5 | “The reaction Liq fi DHCP + BCC_A2 is predicted to occur at 1048 K (775 C) rather than 1013 K (740 C) in order to avoid an ''improper'' deep eutectic valley\[13\] lying extremely close to pure Sr in view of an updated melting temperature of 1050 K (777 C) for Sr.\[14\]” |

## Other properties

### Phase transition (2)

Table: Phase transition, Nd–Sr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 860 K | 860 |  | experimental | [1] Xu 2013 | p. 3 | “The DSC curve in Figure 3(b) confirms that this alloy starts to melt at 860 K (587 C) higher than the melting temperature 839 K (566 C) of Alloy” |
| Phase transition | 1050 K | 1050 |  | model | [1] Xu 2013; _cites SGTE 2001_ | p. 5 | “The reaction Liq fi DHCP + BCC_A2 is predicted to occur at 1048 K (775 C) rather than 1013 K (740 C) in order to avoid an ''improper'' deep eutectic valley\[13\] lying extremely close to pure Sr in view of an updated melting temperature of 1050 K (777 C) for Sr.\[14\]” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Guanglong Xu, Yuwen Cui, Lijun Zeng, Xiaoma Tao, Libin Liu, Zhanpeng Jin, Experimental Investigation and Thermodynamic Modeling for the Mg-Nd-Sr System, Metall Mater Trans A 44, 5634-5641 (2013). [doi:10.1007/s11661-013-2038-7](https://doi.org/10.1007/s11661-013-2038-7)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
