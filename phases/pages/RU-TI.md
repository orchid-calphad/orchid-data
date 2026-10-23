# Ru–Ti phases

> Ru–Ti system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RU-TI.html · Markdown: https://data.orchid-project.org/phases/pages/RU-TI.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RU-TI) · [full JSON](https://data.orchid-project.org/phases/systems/RU-TI.json) · [Ru–Ti system page](https://data.orchid-project.org/systems/RU-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/RU-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ru–Ti system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [A2_BCC](#phase-ru-ti-bcc-a2); _phase:ru-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 4 calculated diagram(s): 300–3999.73 K, x(Ti) 0.76–1 | 6 | 4 |
| [B2_BCC](#phase-ru-ti-bcc-b2); _phase:ru-ti:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2569.99 K, x(Ti) 0.48872–1 | 9 | 2 |
| [FCC_A1](#phase-ru-ti-fcc-a1); _phase:ru-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ru-ti-hcp-a3); _phase:ru-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2608.93 K, x(Ti) 0–1 | 3 | 2 |
| [LIQUID](#phase-ru-ti-liquid); _phase:ru-ti:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1822.69–4000 K, x(Ti) 0–1 | 12 | 2 |

## A2_BCC (Ru–Ti)

- Id: `phase:ru-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 4 calculated diagram(s): 300–3999.73 K, x(Ti) 0.76–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-ti:bcc-a2)

Names (6): _corpus: _corpus:phase:ru-ti:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.12.059:bcc (Ti)  
_tdb: _tdb:RuTi-09Gao.tdb:A2_BCC, tdb:RuTi-09Gao.tdb:BCC_A2, tdb:RuTi-21Liu.tdb:A2_BCC, tdb:RuTi-21Liu.tdb:BCC_A2  


### TDB models of A2_BCC (4): PHASE and CONSTITUENT statements as written

[RuTi-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-09Gao.tdb): A2_BCC, type code %B, sha256 `097c7c25748fe9a9…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : RU TI% : VA : !
~~~~

[RuTi-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-09Gao.tdb): BCC_A2, type code %B, sha256 `097c7c25748fe9a9…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : RU TI% : VA : !
~~~~

[RuTi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-21Liu.tdb): A2_BCC, type code %B, sha256 `2b03d8352e5d1f7f…`

~~~~text
41: PHASE A2_BCC %B 2 1 3 !
42: CONST A2_BCC : RU TI% : VA : !
~~~~

[RuTi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-21Liu.tdb): BCC_A2, type code %B, sha256 `2b03d8352e5d1f7f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : RU TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059) Yongliang Gao, Cuiping Guo, Changrong Li, Shaohua Cui, Zhenmin Du, Thermodynamic modeling of the Ru–Ti system, Journal of Alloys and Compounds 479, 148-151 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1021/ie50458a036](https://doi.org/10.1021/ie50458a036) Otto Redlich, A. T. Kister, Algebraic Representation of Thermodynamic Properties and the Classification of Solutions, Ind. Eng. Chem. 40, 345-348 (1948).  
_cited as the source of values for this phase_

## B2_BCC (Ru–Ti)

- Id: `phase:ru-ti:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: RuTi-09Gao.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: RuTi-21Liu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in RuTi-09Gao.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in RuTi-21Liu.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–2569.99 K, x(Ti) 0.48872–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-ti:bcc-b2)

Names (5): _corpus: _corpus:phase:ru-ti:bcc-b2, corpus:phase:ru-ti:b2-bcc  
_paper: _paper:10.1016/j.jallcom.2008.12.059:RuTi  
_tdb: _tdb:RuTi-09Gao.tdb:B2_BCC, tdb:RuTi-21Liu.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[RuTi-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-09Gao.tdb): B2_BCC, type code %BO, sha256 `097c7c25748fe9a9…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : RU% TI : RU TI% : VA : !
~~~~

[RuTi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-21Liu.tdb): B2_BCC, type code %BO, sha256 `2b03d8352e5d1f7f…`

~~~~text
46: PHASE B2_BCC %BO 3 0.5 0.5 3 !
47: CONST B2_BCC : RU% TI : RU TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059) Yongliang Gao, Cuiping Guo, Changrong Li, Shaohua Cui, Zhenmin Du, Thermodynamic modeling of the Ru–Ti system, Journal of Alloys and Compounds 479, 148-151 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1021/ie50458a036](https://doi.org/10.1021/ie50458a036) Otto Redlich, A. T. Kister, Algebraic Representation of Thermodynamic Properties and the Classification of Solutions, Ind. Eng. Chem. 40, 345-348 (1948).  
_cited as the source of values for this phase_

## FCC_A1 (Ru–Ti)

- Id: `phase:ru-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:ru-ti:fcc-a1  
_tdb: _tdb:RuTi-09Gao.tdb:FCC_A1, tdb:RuTi-21Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[RuTi-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-09Gao.tdb): FCC_A1, type code %A, sha256 `097c7c25748fe9a9…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : RU TI : VA : !
~~~~

[RuTi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-21Liu.tdb): FCC_A1, type code %A, sha256 `2b03d8352e5d1f7f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : RU TI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059) Yongliang Gao, Cuiping Guo, Changrong Li, Shaohua Cui, Zhenmin Du, Thermodynamic modeling of the Ru–Ti system, Journal of Alloys and Compounds 479, 148-151 (2009).  
_assessment that models this phase_

## HCP_A3 (Ru–Ti)

- Id: `phase:ru-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2608.93 K, x(Ti) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-ti:hcp-a3)

Names (4): _corpus: _corpus:phase:ru-ti:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.12.059:hcp (Ru)  
_tdb: _tdb:RuTi-09Gao.tdb:HCP_A3, tdb:RuTi-21Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[RuTi-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-09Gao.tdb): HCP_A3, type code %A, sha256 `097c7c25748fe9a9…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : RU% TI% : VA : !
~~~~

[RuTi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-21Liu.tdb): HCP_A3, type code %A, sha256 `2b03d8352e5d1f7f…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : RU% TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059) Yongliang Gao, Cuiping Guo, Changrong Li, Shaohua Cui, Zhenmin Du, Thermodynamic modeling of the Ru–Ti system, Journal of Alloys and Compounds 479, 148-151 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1021/ie50458a036](https://doi.org/10.1021/ie50458a036) Otto Redlich, A. T. Kister, Algebraic Representation of Thermodynamic Properties and the Classification of Solutions, Ind. Eng. Chem. 40, 345-348 (1948).  
_cited as the source of values for this phase_

## LIQUID (Ru–Ti)

- Id: `phase:ru-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1822.69–4000 K, x(Ti) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-ti:liquid)

Names (4): _corpus: _corpus:phase:ru-ti:liquid  
_paper: _paper:10.1016/j.jallcom.2008.12.059:Liquid  
_tdb: _tdb:RuTi-09Gao.tdb:LIQUID, tdb:RuTi-21Liu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[RuTi-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-09Gao.tdb): LIQUID, type code %, sha256 `097c7c25748fe9a9…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : RU TI : !
~~~~

[RuTi-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/RuTi-21Liu.tdb): LIQUID, type code %, sha256 `2b03d8352e5d1f7f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : RU TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059) Yongliang Gao, Cuiping Guo, Changrong Li, Shaohua Cui, Zhenmin Du, Thermodynamic modeling of the Ru–Ti system, Journal of Alloys and Compounds 479, 148-151 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1021/ie50458a036](https://doi.org/10.1021/ie50458a036) Otto Redlich, A. T. Kister, Algebraic Representation of Thermodynamic Properties and the Classification of Solutions, Ind. Eng. Chem. 40, 345-348 (1948).  
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
