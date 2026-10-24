# Ga–N system

> Ga–N system: 8 accepted literature values (phase transition 7, formation 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-N.html · Markdown: https://data.orchid-project.org/systems/GA-N.md

8 accepted literature values from 1 paper(s) (experimental 5, model 3); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-N.json) · [CSV](https://data.orchid-project.org/systems/GA-N.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-N) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-N/GaN-03Unl.json) · [phases (5)](https://data.orchid-project.org/phases/pages/GA-N.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-N.html) · [Markdown](https://data.orchid-project.org/systems/GA-N.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 7 |
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaN-03Unl.tdb | J. Unland, B. Onderka, A. Davydov, R. Schmid-Fetzer, J. Cryst. Growth, 256, 33-51(2003). [doi:10.1016/S0022-0248(03)01352-6](https://doi.org/10.1016/S0022-0248%2803%2901352-6) | `eb023f7ceb4ad845c783c44fc3241e37e257661ace881cd9ac75f7bf8666187a` | [viewer](https://orchid-project.org/phase-diagrams/#GA-N/GaN-03Unl.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaN-03Unl.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaN-03Unl.json) |
| GaN-98Dav.tdb | A.V. Davydov, T.J. Anderson, Electrochem. Soc. Proc. 98-18, 38-49(1998). | `879d60b9d25803c8732ebeef5da64d4598900a0604a8b9ffa51df68f2d52f070` | [viewer](https://orchid-project.org/phase-diagrams/#GA-N/GaN-98Dav.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaN-98Dav.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaN-98Dav.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaN-03Unl.tdb | 1117.53 | LIQUID (x(N) 0) + GAN_B4 (x(N) 0.5) + GAS (x(N) 1) |
| GaN-03Unl.tdb | 302.91 | LIQUID (x(N) 0) + ORTHORHOMBIC_A11 (x(N) 0) + GAN_B4 (x(N) 0.5) |
| GaN-98Dav.tdb | 1052.57 | LIQUID (x(N) 0) + GAN_B4 (x(N) 0.5) + GAS (x(N) 1) |
| GaN-98Dav.tdb | 302.91 | LIQUID (x(N) 0) + ORTHORHOMBIC_A11 (x(N) 0) + GAN_B4 (x(N) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-N.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-N.json) · [CALPHAD hull GaN-98Dav](https://data.orchid-project.org/hulls/calphad-sgte/GA/GA-N--GaN-98Dav.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ga–N system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| GaN | [GaN](https://data.orchid-project.org/compounds/GaN.html) | -52.1 kJ/mol-atom ± 4 | 298.15 | experimental | -63.373 (mp-aaaaabey) | -55.891 (oqmd-6450) | [1] Unland 2003; _cites Hahn 1940_ [doi](https://doi.org/10.1002/zaac.19402440203) | Table 2, p. 3, row 1 |  |

## Other properties

### Phase transition (7)

Table: Phase transition, Ga–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1043 K | 1043 | other: GaN, Dynamic oscillation TGA, first heating cycle; _alloy: N 0.5_ | experimental | [1] Unland 2003 | Table 4, p. 5, row 1 |  |
| Phase transition | 1085 K | 1085 | other: GaN, fast heating TGA (in ramp before 1275 K, 24 h); _alloy: N 0.5_ | experimental | [1] Unland 2003 | Table 4, p. 5, row 2 |  |
| Phase transition | 1110 K | 1110 | other | experimental | [1] Unland 2003 | p. 1 | “A reproducible mass gain at slightly lower temperature suggests the equilibrium temperature to be at 1110710 K under 1 bar of nitrogen.” |
| Phase transition | 1110 K | 1110 | other: GaN (+ in situ Ga) Isothermal stepping TGA, samples #1, #2, #3, assessed value; _alloy: N 0.5_ | experimental | [1] Unland 2003 | Table 4, p. 5, row 4 |  |
| Phase transition | 2700 K | 2700 |  | model | [1] Unland 2003 | p. 13 | “The finally assessed value of Tm=2700 K agrees with all three constraints and the resulting value of 0;L Ga;N is given in Table 5.” |
| Phase transition | 2700 K | 2700 | liquid | model | [1] Unland 2003 | p. 15 | “The experimental solubility data are compared to the calculated phase boundary based on Tm=2700 K in Fig. 8.” |
| Phase transition | 2791 K | 2791 |  | model | [1] Unland 2003; _cites Van 1973_ [doi](https://doi.org/10.1103/physrevb.7.1479) | p. 13 | “It is also in reasonable agreement with the melting point at 2791 K predicted from the semi-empirical theory of electronegativity \[53\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Unland, B. Onderka, A. Davydov, R. Schmid-Fetzer, Thermodynamics and Phase Stability in the Ga–N System, Journal of Crystal Growth 256, 33-51 (2003). [doi:10.1016/s0022-0248(03)01352-6](https://doi.org/10.1016/s0022-0248%2803%2901352-6)

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
