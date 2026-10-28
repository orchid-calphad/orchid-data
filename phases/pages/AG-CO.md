# Ag–Co phases

> Ag–Co system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-CO.html · Markdown: https://data.orchid-project.org/phases/pages/AG-CO.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-CO) · [full JSON](https://data.orchid-project.org/phases/systems/AG-CO.json) · [Ag–Co system page](https://data.orchid-project.org/systems/AG-CO.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-CO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Co system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-co-bcc-a2); _phase:ag-co:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ag-co-fcc-a1); _phase:ag-co:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.22 K, x(Co) 0–1 | 12 | 2 |
| [HCP_A3](#phase-ag-co-hcp-a3); _phase:ag-co:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–695.31 K, x(Co) 0.99997–1 | 2 | 2 |
| [LIQUID](#phase-ag-co-liquid); _phase:ag-co:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1086.48–2500 K, x(Co) 0–1 | 8 | 2 |

## BCC_A2 (Ag–Co)

- Id: `phase:ag-co:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-co:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-co:bcc-a2  
_tdb: _tdb:AgCo-09Zhu.tdb:BCC_A2, tdb:AgCo-21Den.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgCo-09Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-09Zhu.tdb): BCC_A2, type code %B, sha256 `0227ed7caa6041c2…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG CO : VA : !
~~~~

[AgCo-21Den.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-21Den.tdb): BCC_A2, type code %B, sha256 `6ef85141f4640306…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG CO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-020-05431-7](https://doi.org/10.1007/s10853-020-05431-7) Congkun Deng, Hongxiang Jiang, Jiuzhou Zhao, Lili Zhang, Jie He, Thermodynamics and solidification kinetics of Ag–Ni–Co immiscible alloys, J Mater Sci 56, 3455-3471 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.03.025](https://doi.org/10.1016/j.jallcom.2009.03.025) WenJun Zhu, HuaShan Liu, JinSan Wang, HongQun Dong, ZhanPeng Jin, Thermodynamic assessment of the Sn–Ag–Co system and solidification simulation of the ternary alloy, Journal of Alloys and Compounds 481, 503-508 (2009).  
_assessment that models this phase_

## FCC_A1 (Ag–Co)

- Id: `phase:ag-co:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.22 K, x(Co) 0–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-co:fcc-a1)

Names (7): _corpus: _corpus:phase:ag-co:fcc-a1  
_paper: _paper:10.1007/s10853-020-05431-7:fcc (Ag), paper:10.1007/s10853-020-05431-7:fcc (Co), paper:10.1016/j.jallcom.2009.03.025:FCC(Ag), paper:10.1016/j.jallcom.2009.03.025:FCC(Co)  
_tdb: _tdb:AgCo-09Zhu.tdb:FCC_A1, tdb:AgCo-21Den.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgCo-09Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-09Zhu.tdb): FCC_A1, type code %A, sha256 `0227ed7caa6041c2…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% CO% : VA : !
~~~~

[AgCo-21Den.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-21Den.tdb): FCC_A1, type code %A, sha256 `6ef85141f4640306…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% CO% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10853-020-05431-7](https://doi.org/10.1007/s10853-020-05431-7) Congkun Deng, Hongxiang Jiang, Jiuzhou Zhao, Lili Zhang, Jie He, Thermodynamics and solidification kinetics of Ag–Ni–Co immiscible alloys, J Mater Sci 56, 3455-3471 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.03.025](https://doi.org/10.1016/j.jallcom.2009.03.025) WenJun Zhu, HuaShan Liu, JinSan Wang, HongQun Dong, ZhanPeng Jin, Thermodynamic assessment of the Sn–Ag–Co system and solidification simulation of the ternary alloy, Journal of Alloys and Compounds 481, 503-508 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869002](https://doi.org/10.1007/bf02869002) Karakaya I, Thompson WT (1986) The Ag-Co (silvercobalt) system. Bull Alloy Phase Diagrams 7:259–263. h ttps://doi.org/10.1007/BF02869002  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Co)

- Id: `phase:ag-co:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–695.31 K, x(Co) 0.99997–1
- Literature: 2 values (2 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-co:hcp-a3)

Names (5): _corpus: _corpus:phase:ag-co:hcp-a3  
_paper: _paper:10.1007/s10853-020-05431-7:hcp (Co), paper:10.1016/j.jallcom.2009.03.025:HCP(Co)  
_tdb: _tdb:AgCo-09Zhu.tdb:HCP_A3, tdb:AgCo-21Den.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgCo-09Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-09Zhu.tdb): HCP_A3, type code %A, sha256 `0227ed7caa6041c2…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG CO% : VA : !
~~~~

[AgCo-21Den.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-21Den.tdb): HCP_A3, type code %A, sha256 `6ef85141f4640306…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG CO% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-020-05431-7](https://doi.org/10.1007/s10853-020-05431-7) Congkun Deng, Hongxiang Jiang, Jiuzhou Zhao, Lili Zhang, Jie He, Thermodynamics and solidification kinetics of Ag–Ni–Co immiscible alloys, J Mater Sci 56, 3455-3471 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.03.025](https://doi.org/10.1016/j.jallcom.2009.03.025) WenJun Zhu, HuaShan Liu, JinSan Wang, HongQun Dong, ZhanPeng Jin, Thermodynamic assessment of the Sn–Ag–Co system and solidification simulation of the ternary alloy, Journal of Alloys and Compounds 481, 503-508 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ag–Co)

- Id: `phase:ag-co:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1086.48–2500 K, x(Co) 0–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-co:liquid)

Names (7): _corpus: _corpus:phase:ag-co:liquid  
_paper: _paper:10.1007/s10853-020-05431-7:L, paper:10.1007/s10853-020-05431-7:L1, paper:10.1016/j.jallcom.2009.03.025:L, paper:10.1016/j.jallcom.2009.03.025:L2  
_tdb: _tdb:AgCo-09Zhu.tdb:LIQUID, tdb:AgCo-21Den.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgCo-09Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-09Zhu.tdb): LIQUID, type code %, sha256 `0227ed7caa6041c2…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG CO : !
~~~~

[AgCo-21Den.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCo-21Den.tdb): LIQUID, type code %, sha256 `6ef85141f4640306…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG CO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10853-020-05431-7](https://doi.org/10.1007/s10853-020-05431-7) Congkun Deng, Hongxiang Jiang, Jiuzhou Zhao, Lili Zhang, Jie He, Thermodynamics and solidification kinetics of Ag–Ni–Co immiscible alloys, J Mater Sci 56, 3455-3471 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.03.025](https://doi.org/10.1016/j.jallcom.2009.03.025) WenJun Zhu, HuaShan Liu, JinSan Wang, HongQun Dong, ZhanPeng Jin, Thermodynamic assessment of the Sn–Ag–Co system and solidification simulation of the ternary alloy, Journal of Alloys and Compounds 481, 503-508 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869002](https://doi.org/10.1007/bf02869002) Karakaya I, Thompson WT (1986) The Ag-Co (silvercobalt) system. Bull Alloy Phase Diagrams 7:259–263. h ttps://doi.org/10.1007/BF02869002  
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
