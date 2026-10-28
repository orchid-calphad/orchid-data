# Na–Zn phases

> Na–Zn system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NA-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/NA-ZN.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NA-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/NA-ZN.json) · [Na–Zn system page](https://data.orchid-project.org/systems/NA-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/NA-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Na–Zn system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-na-zn-bcc-a2); _phase:na-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–370.83 K, x(Zn) 0–0 | 4 | 1 |
| [FCC_A1](#phase-na-zn-fcc-a1); _phase:na-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-na-zn-hcp-a3); _phase:na-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Zn) 1–1 | 2 | 1 |
| [LIQUID](#phase-na-zn-liquid); _phase:na-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 370.83–2500 K, x(Zn) 0–1 | 10 | 1 |
| [NAZN13_D23](#phase-na-zn-nazn13-d23); _phase:na-zn:nazn13-d23_ | NaZn13 · D2_3 · cF112 · Fm-3c (226) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–830.01 K, x(Zn) 0.92857–0.92857 | 10 | 1 |

## BCC_A2 (Na–Zn)

- Id: `phase:na-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–370.83 K, x(Zn) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-zn:bcc-a2)

Names (3): _corpus: _corpus:phase:na-zn:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.09.012:bcc  
_tdb: _tdb:NaZn-09Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NaZn-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaZn-09Liu.tdb): BCC_A2, type code %B, sha256 `837dc17668b272cc…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NA% ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02663664](https://doi.org/10.1007/bf02663664) H. Çetin, R. G. Ross, The phase diagram of Na-Zn alloys, JPE 12, 6-9 (1991).  
_cited as the source of values for this phase_

## FCC_A1 (Na–Zn)

- Id: `phase:na-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-zn:fcc-a1)

Names (2): _corpus: _corpus:phase:na-zn:fcc-a1  
_tdb: _tdb:NaZn-09Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NaZn-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaZn-09Liu.tdb): FCC_A1, type code %A, sha256 `837dc17668b272cc…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NA ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009).  
_assessment that models this phase_

## HCP_A3 (Na–Zn)

- Id: `phase:na-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Zn) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-zn:hcp-a3)

Names (3): _corpus: _corpus:phase:na-zn:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.09.012:hcp  
_tdb: _tdb:NaZn-09Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NaZn-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaZn-09Liu.tdb): HCP_A3, type code %A, sha256 `837dc17668b272cc…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NA ZN% : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Na–Zn)

- Id: `phase:na-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 370.83–2500 K, x(Zn) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-zn:liquid)

Names (4): _corpus: _corpus:phase:na-zn:liquid  
_paper: _paper:10.1016/j.jallcom.2008.09.012:L, paper:10.1016/j.jallcom.2008.09.012:liq  
_tdb: _tdb:NaZn-09Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NaZn-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaZn-09Liu.tdb): LIQUID, type code %, sha256 `837dc17668b272cc…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NA ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02663664](https://doi.org/10.1007/bf02663664) H. Çetin, R. G. Ross, The phase diagram of Na-Zn alloys, JPE 12, 6-9 (1991).  
_cited as the source of values for this phase_

## NAZN13_D23 (Na–Zn)

- Id: `phase:na-zn:nazn13-d23`; status `assigned`
- Structure: NaZn13 · D2_3 · cF112 · Fm-3c (226); type `st:d2-3-nazn13-cf112`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabko and oqmd-17734, space group 226
- Stoichiometry: Na 0.0714, Zn 0.9286
- Stability: stable in 1 of 1 calculated diagram(s): 300–830.01 K, x(Zn) 0.92857–0.92857
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-zn:nazn13-d23)

Names (5): _corpus: _corpus:phase:na-zn:nazn13-d23  
_mp: _mp:mp-aaaaabko  
_oqmd: _oqmd:oqmd-17734  
_paper: _paper:10.1016/j.jallcom.2008.09.012:NaZn13  
_tdb: _tdb:NaZn-09Liu.tdb:NAZN13_D23  


### TDB models of NAZN13_D23 (1): PHASE and CONSTITUENT statements as written

[NaZn-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaZn-09Liu.tdb): NAZN13_D23, type code %, sha256 `837dc17668b272cc…`

~~~~text
42: PHASE NAZN13_D23 % 2 1 13 !
43: CONST NAZN13_D23 : NA : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02663664](https://doi.org/10.1007/bf02663664) H. Çetin, R. G. Ross, The phase diagram of Na-Zn alloys, JPE 12, 6-9 (1991).  
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
