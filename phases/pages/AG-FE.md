# Ag–Fe phases

> Ag–Fe system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-FE.html · Markdown: https://data.orchid-project.org/phases/pages/AG-FE.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-FE) · [full JSON](https://data.orchid-project.org/phases/systems/AG-FE.json) · [Ag–Fe system page](https://data.orchid-project.org/systems/AG-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Fe system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-fe-bcc-a2); _phase:ag-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.7 K, x(Fe) 0.07–1 | 4 | 2 |
| [FCC_A1](#phase-ag-fe-fcc-a1); _phase:ag-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1671.2 K, x(Fe) 0–1 | 2 | 2 |
| [HCP_A3](#phase-ag-fe-hcp-a3); _phase:ag-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ag-fe-liquid); _phase:ag-fe:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1234.3–2500 K, x(Fe) 0–1 | 4 | 2 |

## BCC_A2 (Ag–Fe)

- Id: `phase:ag-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.7 K, x(Fe) 0.07–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-fe:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-fe:bcc-a2  
_paper: _paper:10.1007/s11669-020-00813-5:(δFe)  
_tdb: _tdb:AgFe-04Kor-LB.tdb:BCC_A2, tdb:AgFe-20Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgFe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-04Kor-LB.tdb): BCC_A2, type code %B, sha256 `6c8fc844a70bdb21…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG FE% : VA : !
~~~~

[AgFe-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-20Zho.tdb): BCC_A2, type code %B, sha256 `677fab8182cdea2b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG FE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868316](https://doi.org/10.1007/bf02868316) L.J. Swartzendruber, The Ag-Fe (Silver-Iron) System, J. Phase Equilib., 1984, 5(6), p 560-564  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Fe)

- Id: `phase:ag-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1671.2 K, x(Fe) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-fe:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-fe:fcc-a1  
_paper: _paper:10.1007/s11669-020-00813-5:(γFe)  
_tdb: _tdb:AgFe-04Kor-LB.tdb:FCC_A1, tdb:AgFe-20Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgFe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-04Kor-LB.tdb): FCC_A1, type code %A, sha256 `6c8fc844a70bdb21…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% FE% : VA : !
~~~~

[AgFe-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-20Zho.tdb): FCC_A1, type code %A, sha256 `677fab8182cdea2b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% FE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868316](https://doi.org/10.1007/bf02868316) L.J. Swartzendruber, The Ag-Fe (Silver-Iron) System, J. Phase Equilib., 1984, 5(6), p 560-564  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Fe)

- Id: `phase:ag-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-fe:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-fe:hcp-a3  
_tdb: _tdb:AgFe-04Kor-LB.tdb:HCP_A3, tdb:AgFe-20Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgFe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-04Kor-LB.tdb): HCP_A3, type code %A, sha256 `6c8fc844a70bdb21…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG FE : VA : !
~~~~

[AgFe-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-20Zho.tdb): HCP_A3, type code %A, sha256 `677fab8182cdea2b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase_

## LIQUID (Ag–Fe)

- Id: `phase:ag-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1234.3–2500 K, x(Fe) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-fe:liquid)

Names (5): _corpus: _corpus:phase:ag-fe:liquid  
_paper: _paper:10.1007/s11669-020-00813-5:Liquid#1, paper:10.1007/s11669-020-00813-5:Liquid#2  
_tdb: _tdb:AgFe-04Kor-LB.tdb:LIQUID, tdb:AgFe-20Zho.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgFe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-04Kor-LB.tdb): LIQUID, type code %, sha256 `6c8fc844a70bdb21…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG FE : !
~~~~

[AgFe-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgFe-20Zho.tdb): LIQUID, type code %, sha256 `677fab8182cdea2b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG FE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868316](https://doi.org/10.1007/bf02868316) L.J. Swartzendruber, The Ag-Fe (Silver-Iron) System, J. Phase Equilib., 1984, 5(6), p 560-564  
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
