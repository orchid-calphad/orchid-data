# Se–Zn phases

> Se–Zn system: 5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SE-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/SE-ZN.md

5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SE-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/SE-ZN.json) · [Se–Zn system page](https://data.orchid-project.org/systems/SE-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SE-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Se–Zn system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-se-zn-a8-hexagonal); _phase:se-zn:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1 | 1 | 1 |
| [GAS](#phase-se-zn-gas); _phase:se-zn:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 989.69–2500 K, x(Se) 0–1 | 0 | 1 |
| [HCP_A3](#phase-se-zn-hcp-a3); _phase:se-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Se) 0–0 | 1 | 1 |
| [LIQUID](#phase-se-zn-liquid); _phase:se-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Se) 0–1 | 7 | 1 |
| [ZNSE_B3](#phase-se-zn-znse-b3); _phase:se-zn:znse-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 15 | 1 |

## HEXAGONAL_A8 (Se–Zn)

- Id: `phase:se-zn:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-zn:a8-hexagonal)

Names (4): _corpus: _corpus:phase:se-zn:a8-hexagonal, corpus:phase:se-zn:hexagonal-a8  
_paper: _paper:10.1016/j.jallcom.2014.08.001:(Se)  
_tdb: _tdb:ZnSe-14Che.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[ZnSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnSe-14Che.tdb): HEXAGONAL_A8, type code %, sha256 `7827c472586d3aba…`

~~~~text
43: PHASE HEXAGONAL_A8 % 1 1 !
44: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_

## GAS (Se–Zn)

- Id: `phase:se-zn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 989.69–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-zn:gas)

Names (2): _corpus: _corpus:phase:se-zn:gas  
_tdb: _tdb:ZnSe-14Che.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[ZnSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnSe-14Che.tdb): GAS, type code %, sha256 `7827c472586d3aba…`

~~~~text
51: PHASE GAS:G % 1 1 !
52: CONST GAS:G : SE SE2 SE3 SE4 SE5 SE6 SE7 SE8 ZNSE ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase_

## HCP_A3 (Se–Zn)

- Id: `phase:se-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Zn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Se) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-zn:hcp-a3)

Names (3): _corpus: _corpus:phase:se-zn:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2014.08.001:(Zn)  
_tdb: _tdb:ZnSe-14Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ZnSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnSe-14Che.tdb): HCP_A3, type code %A, sha256 `7827c472586d3aba…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Se–Zn)

- Id: `phase:se-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Se) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-zn:liquid)

Names (5): _corpus: _corpus:phase:se-zn:liquid  
_paper: _paper:10.1016/j.jallcom.2014.08.001:Liq, paper:10.1016/j.jallcom.2014.08.001:liq, paper:10.1016/j.jallcom.2014.08.001:liquid  
_tdb: _tdb:ZnSe-14Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ZnSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnSe-14Che.tdb): LIQUID, type code %, sha256 `7827c472586d3aba…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : SE ZN ZNSE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2427507](https://doi.org/10.1149/1.2427507) Albrecht G. Fischer, Preparation and Properties of ZnS-Type Crystals from the Melt, J. Electrochem. Soc. 106, 838 (1959).  
_cited as the source of values for this phase_

## ZNSE_B3 (Se–Zn)

- Id: `phase:se-zn:znse-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Se 0.5000, Zn 0.5000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-zn:znse-b3)

Names (3): _corpus: _corpus:phase:se-zn:znse-b3  
_paper: _paper:10.1016/j.jallcom.2014.08.001:ZnSe  
_tdb: _tdb:ZnSe-14Che.tdb:ZNSE_B3  


### TDB models of ZNSE_B3 (1): PHASE and CONSTITUENT statements as written

[ZnSe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnSe-14Che.tdb): ZNSE_B3, type code %, sha256 `7827c472586d3aba…`

~~~~text
48: PHASE ZNSE_B3 % 2 1 1 !
49: CONST ZNSE_B3 : ZN : SE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.08.001](https://doi.org/10.1016/j.jallcom.2014.08.001) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for the Bi–Se and Zn–Se binary systems, Journal of Alloys and Compounds 617, 423-428 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j100813a010](https://doi.org/10.1021/j100813a010) W. J. Wösten, M. G. Geers, THE VAPOR PRESSURE OF ZINC SELENIDE, J. Phys. Chem. 66, 1252-1253 (1962).  
_cited as the source of values for this phase_
- [doi:10.1039/tf9635902851](https://doi.org/10.1039/tf9635902851) P. Goldfinger, M. Jeunehomme, Mass spectrometric and Knudsen-cell vaporization studies of group 2B-6B compounds, Trans. Faraday Soc. 59, 2851 (1963).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2427507](https://doi.org/10.1149/1.2427507) Albrecht G. Fischer, Preparation and Properties of ZnS-Type Crystals from the Melt, J. Electrochem. Soc. 106, 838 (1959).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
