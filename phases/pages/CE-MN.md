# Ce–Mn phases

> Ce–Mn system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-MN.html · Markdown: https://data.orchid-project.org/phases/pages/CE-MN.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-MN) · [full JSON](https://data.orchid-project.org/phases/systems/CE-MN.json) · [Ce–Mn system page](https://data.orchid-project.org/systems/CE-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Mn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-mn-bcc-a2); _phase:ce-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 911.37–2498.99 K, x(Mn) 0–1 | 5 | 2 |
| [CBCC_A12](#phase-ce-mn-cbcc-a12); _phase:ce-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1355 K, x(Mn) 1–1 | 5 | 2 |
| [CUB_A13](#phase-ce-mn-cub-a13); _phase:ce-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 898.39–1404.99 K, x(Mn) 0.97167–1 | 4 | 2 |
| [FCC_A1](#phase-ce-mn-fcc-a1); _phase:ce-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1418 K, x(Mn) 0–1 | 10 | 2 |
| [HCP_A3](#phase-ce-mn-hcp-a3); _phase:ce-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ce-mn-liquid); _phase:ce-mn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 894–2500 K, x(Mn) 0–1 | 15 | 2 |

## BCC_A2 (Ce–Mn)

- Id: `phase:ce-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 911.37–2498.99 K, x(Mn) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-mn:bcc-a2)

Names (5): _corpus: _corpus:phase:ce-mn:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2006.07.071:(δCe), paper:10.1016/j.jallcom.2006.07.071:(δMn)  
_tdb: _tdb:CeMn-07Tan.tdb:BCC_A2, tdb:CeMn-24Ye.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CeMn-07Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-07Tan.tdb): BCC_A2, type code %B, sha256 `1d3e4632db5ba67e…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CE% MN% : VA : !
~~~~

[CeMn-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-24Ye.tdb): BCC_A2, type code %B, sha256 `cd632a2aefd27880…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CE% MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.071](https://doi.org/10.1016/j.jallcom.2006.07.071) Chengying Tang, Yong Du, Lijun Zhang, Honghui Xu, Zhijun Zhu, Thermodynamic assessment of the Ce–Mn system, Journal of Alloys and Compounds 437, 102-106 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(64)90078-5](https://doi.org/10.1016/0022-5088%2864%2990078-5) B.J Thamer, The system cerium-manganese in the range of 0–20 atomic per cent manganese, Journal of the Less Common Metals 7, 341-346 (1964).  
_cited as the source of values for this phase_

## CBCC_A12 (Ce–Mn)

- Id: `phase:ce-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1355 K, x(Mn) 1–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-mn:cbcc-a12)

Names (4): _corpus: _corpus:phase:ce-mn:cbcc-a12  
_paper: _paper:10.1016/j.jallcom.2006.07.071:(αMn)  
_tdb: _tdb:CeMn-07Tan.tdb:CBCC_A12, tdb:CeMn-24Ye.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[CeMn-07Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-07Tan.tdb): CBCC_A12, type code %A, sha256 `1d3e4632db5ba67e…`

~~~~text
41: PHASE CBCC_A12 %A 2 1 1 !
42: CONST CBCC_A12 : MN% : VA : !
~~~~

[CeMn-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-24Ye.tdb): CBCC_A12, type code %A, sha256 `cd632a2aefd27880…`

~~~~text
44: PHASE CBCC_A12 %A 2 1 1 !
45: CONST CBCC_A12 : MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.071](https://doi.org/10.1016/j.jallcom.2006.07.071) Chengying Tang, Yong Du, Lijun Zhang, Honghui Xu, Zhijun Zhu, Thermodynamic assessment of the Ce–Mn system, Journal of Alloys and Compounds 437, 102-106 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(64)90078-5](https://doi.org/10.1016/0022-5088%2864%2990078-5) B.J Thamer, The system cerium-manganese in the range of 0–20 atomic per cent manganese, Journal of the Less Common Metals 7, 341-346 (1964).  
_cited as the source of values for this phase_

## CUB_A13 (Ce–Mn)

- Id: `phase:ce-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 898.39–1404.99 K, x(Mn) 0.97167–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-mn:cub-a13)

Names (4): _corpus: _corpus:phase:ce-mn:cub-a13  
_paper: _paper:10.1016/j.jallcom.2006.07.071:(βMn)  
_tdb: _tdb:CeMn-07Tan.tdb:CUB_A13, tdb:CeMn-24Ye.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[CeMn-07Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-07Tan.tdb): CUB_A13, type code %, sha256 `1d3e4632db5ba67e…`

~~~~text
46: PHASE CUB_A13 % 2 1 1 !
47: CONST CUB_A13 : CE MN% : VA : !
~~~~

[CeMn-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-24Ye.tdb): CUB_A13, type code %, sha256 `cd632a2aefd27880…`

~~~~text
49: PHASE CUB_A13 % 2 1 1 !
50: CONST CUB_A13 : CE MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.071](https://doi.org/10.1016/j.jallcom.2006.07.071) Chengying Tang, Yong Du, Lijun Zhang, Honghui Xu, Zhijun Zhu, Thermodynamic assessment of the Ce–Mn system, Journal of Alloys and Compounds 437, 102-106 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(64)90078-5](https://doi.org/10.1016/0022-5088%2864%2990078-5) B.J Thamer, The system cerium-manganese in the range of 0–20 atomic per cent manganese, Journal of the Less Common Metals 7, 341-346 (1964).  
_cited as the source of values for this phase_

## FCC_A1 (Ce–Mn)

- Id: `phase:ce-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1418 K, x(Mn) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-mn:fcc-a1)

Names (5): _corpus: _corpus:phase:ce-mn:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2006.07.071:(γCe), paper:10.1016/j.jallcom.2006.07.071:(γMn)  
_tdb: _tdb:CeMn-07Tan.tdb:FCC_A1, tdb:CeMn-24Ye.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CeMn-07Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-07Tan.tdb): FCC_A1, type code %A, sha256 `1d3e4632db5ba67e…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CE% MN% : VA : !
~~~~

[CeMn-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-24Ye.tdb): FCC_A1, type code %A, sha256 `cd632a2aefd27880…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CE% MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.071](https://doi.org/10.1016/j.jallcom.2006.07.071) Chengying Tang, Yong Du, Lijun Zhang, Honghui Xu, Zhijun Zhu, Thermodynamic assessment of the Ce–Mn system, Journal of Alloys and Compounds 437, 102-106 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(64)90078-5](https://doi.org/10.1016/0022-5088%2864%2990078-5) B.J Thamer, The system cerium-manganese in the range of 0–20 atomic per cent manganese, Journal of the Less Common Metals 7, 341-346 (1964).  
_cited as the source of values for this phase_

## HCP_A3 (Ce–Mn)

- Id: `phase:ce-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-mn:hcp-a3)

Names (3): _corpus: _corpus:phase:ce-mn:hcp-a3  
_tdb: _tdb:CeMn-07Tan.tdb:HCP_A3, tdb:CeMn-24Ye.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CeMn-07Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-07Tan.tdb): HCP_A3, type code %A, sha256 `1d3e4632db5ba67e…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CE MN : VA : !
~~~~

[CeMn-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-24Ye.tdb): HCP_A3, type code %A, sha256 `cd632a2aefd27880…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CE MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.07.071](https://doi.org/10.1016/j.jallcom.2006.07.071) Chengying Tang, Yong Du, Lijun Zhang, Honghui Xu, Zhijun Zhu, Thermodynamic assessment of the Ce–Mn system, Journal of Alloys and Compounds 437, 102-106 (2007).  
_assessment that models this phase_

## LIQUID (Ce–Mn)

- Id: `phase:ce-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 894–2500 K, x(Mn) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-mn:liquid)

Names (4): _corpus: _corpus:phase:ce-mn:liquid  
_paper: _paper:10.1016/j.jallcom.2006.07.071:Liquid  
_tdb: _tdb:CeMn-07Tan.tdb:LIQUID, tdb:CeMn-24Ye.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CeMn-07Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-07Tan.tdb): LIQUID, type code %, sha256 `1d3e4632db5ba67e…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CE MN : !
~~~~

[CeMn-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/CeMn-24Ye.tdb): LIQUID, type code %, sha256 `cd632a2aefd27880…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CE MN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.071](https://doi.org/10.1016/j.jallcom.2006.07.071) Chengying Tang, Yong Du, Lijun Zhang, Honghui Xu, Zhijun Zhu, Thermodynamic assessment of the Ce–Mn system, Journal of Alloys and Compounds 437, 102-106 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(64)90078-5](https://doi.org/10.1016/0022-5088%2864%2990078-5) B.J Thamer, The system cerium-manganese in the range of 0–20 atomic per cent manganese, Journal of the Less Common Metals 7, 341-346 (1964).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
