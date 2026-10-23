# Cd–Se phases

> Cd–Se system: 6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-SE.html · Markdown: https://data.orchid-project.org/phases/pages/CD-SE.md

6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-SE) · [full JSON](https://data.orchid-project.org/phases/systems/CD-SE.json) · [Cd–Se system page](https://data.orchid-project.org/systems/CD-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Se system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-cd-se-a8-hexagonal); _phase:cd-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1 | 1 | 1 |
| [BCC_A2](#phase-cd-se-bcc-a2); _phase:cd-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CDSE_B4](#phase-cd-se-cdse-b4); _phase:cd-se:cdse-b4_ | ZnS (wurtzite) · B4 · hP4 · P6_3mc (186) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1888.5 K, x(Se) 0.5–0.5 | 11 | 1 |
| [FCC_A1](#phase-cd-se-fcc-a1); _phase:cd-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cd-se-hcp-a3); _phase:cd-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–594.18 K, x(Se) 0–0 | 1 | 1 |
| [LIQUID](#phase-cd-se-liquid); _phase:cd-se:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 494–2500 K, x(Se) 0–1 | 9 | 1 |

## HEXAGONAL_A8 (Cd–Se)

- Id: `phase:cd-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-se:a8-hexagonal)

Names (4): _corpus: _corpus:phase:cd-se:a8-hexagonal, corpus:phase:cd-se:hexagonal-a8  
_paper: _paper:10.1007/s11664-012-2016-7:(Se)  
_tdb: _tdb:CdSe-12Liu.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[CdSe-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSe-12Liu.tdb): HEXAGONAL_A8, type code %, sha256 `4520cb9d35761d8f…`

~~~~text
45: PHASE HEXAGONAL_A8 % 1 1 !
46: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Cd–Se)

- Id: `phase:cd-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-se:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-se:bcc-a2  
_tdb: _tdb:CdSe-12Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdSe-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSe-12Liu.tdb): BCC_A2, type code %B, sha256 `4520cb9d35761d8f…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012).  
_assessment that models this phase_

## CDSE_B4 (Cd–Se)

- Id: `phase:cd-se:cdse-b4`; status `assigned`
- Structure: ZnS (wurtzite) · B4 · hP4 · P6_3mc (186); type `st:b4-zns-wurtzite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.5000, Se 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1888.5 K, x(Se) 0.5–0.5
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-se:cdse-b4)

Names (3): _corpus: _corpus:phase:cd-se:cdse-b4  
_paper: _paper:10.1007/s11664-012-2016-7:CdSe  
_tdb: _tdb:CdSe-12Liu.tdb:CDSE_B4  


### TDB models of CDSE_B4 (1): PHASE and CONSTITUENT statements as written

[CdSe-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSe-12Liu.tdb): CDSE_B4, type code %, sha256 `4520cb9d35761d8f…`

~~~~text
50: PHASE CDSE_B4 % 2 1 1 !
51: CONST CDSE_B4 : CD : SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j100817a032](https://doi.org/10.1021/j100817a032) A. Reisman, M. Berkenblit, M. Witzen, NON-STOICHIOMETRY IN CADMIUM SELENIDE AND EQUILIBRIA IN THE SYSTEM CADMIUM-SELENIUM\<sup>1\</sup>, J. Phys. Chem. 66, 2210-2214 (1962).  
_cited as the source of values for this phase_
- [doi:10.1039/tf9635902851](https://doi.org/10.1039/tf9635902851) P. Goldfinger, M. Jeunehomme, Mass spectrometric and Knudsen-cell vaporization studies of group 2B-6B compounds, Trans. Faraday Soc. 59, 2851 (1963).  
_cited as the source of values for this phase_

## FCC_A1 (Cd–Se)

- Id: `phase:cd-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-se:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-se:fcc-a1  
_tdb: _tdb:CdSe-12Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdSe-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSe-12Liu.tdb): FCC_A1, type code %A, sha256 `4520cb9d35761d8f…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012).  
_assessment that models this phase_

## HCP_A3 (Cd–Se)

- Id: `phase:cd-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–594.18 K, x(Se) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-se:hcp-a3)

Names (3): _corpus: _corpus:phase:cd-se:hcp-a3  
_paper: _paper:10.1007/s11664-012-2016-7:(Cd)  
_tdb: _tdb:CdSe-12Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdSe-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSe-12Liu.tdb): HCP_A3, type code %A, sha256 `4520cb9d35761d8f…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Cd–Se)

- Id: `phase:cd-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 494–2500 K, x(Se) 0–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-se:liquid)

Names (6): _corpus: _corpus:phase:cd-se:liquid  
_paper: _paper:10.1007/s11664-012-2016-7:L, paper:10.1007/s11664-012-2016-7:liq#1, paper:10.1007/s11664-012-2016-7:liq#2, paper:10.1007/s11664-012-2016-7:liquid  
_tdb: _tdb:CdSe-12Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdSe-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSe-12Liu.tdb): LIQUID, type code %, sha256 `4520cb9d35761d8f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CD CDSE SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j100817a032](https://doi.org/10.1021/j100817a032) A. Reisman, M. Berkenblit, M. Witzen, NON-STOICHIOMETRY IN CADMIUM SELENIDE AND EQUILIBRIA IN THE SYSTEM CADMIUM-SELENIUM\<sup>1\</sup>, J. Phys. Chem. 66, 2210-2214 (1962).  
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
