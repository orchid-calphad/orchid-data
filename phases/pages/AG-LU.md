# Ag–Lu phases

> Ag–Lu system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-LU.html · Markdown: https://data.orchid-project.org/phases/pages/AG-LU.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-LU) · [full JSON](https://data.orchid-project.org/phases/systems/AG-LU.json) · [Ag–Lu system page](https://data.orchid-project.org/systems/AG-LU.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-LU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Lu system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2LU_C11B](#phase-ag-lu-ag2lu-c11b); _phase:ag-lu:ag2lu-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1372.23 K, x(Lu) 0.33333–0.33333 | 0 | 1 |
| [AG4LU_D1A](#phase-ag-lu-ag4lu-d1a); _phase:ag-lu:ag4lu-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1195.01 K, x(Lu) 0.2–0.2 | 0 | 1 |
| [AGLU_B2](#phase-ag-lu-aglu-b2); _phase:ag-lu:aglu-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1396.82 K, x(Lu) 0.5–0.5 | 0 | 1 |
| [BCC_A2](#phase-ag-lu-bcc-a2); _phase:ag-lu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ag-lu-fcc-a1); _phase:ag-lu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Lu) 0–0.35158 | 0 | 1 |
| [HCP_A3](#phase-ag-lu-hcp-a3); _phase:ag-lu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2016.99 K, x(Lu) 0.97813–1 | 0 | 1 |
| [LIQUID](#phase-ag-lu-liquid); _phase:ag-lu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1088.01–2500 K, x(Lu) 0–1 | 0 | 1 |

## AG2LU_C11B (Ag–Lu)

- Id: `phase:ag-lu:ag2lu-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfycx and oqmd-27616, space group 139
- Stoichiometry: Ag 0.6667, Lu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1372.23 K, x(Lu) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-lu:ag2lu-c11b)

Names (4): _corpus: _corpus:phase:ag-lu:ag2lu-c11b  
_mp: _mp:mp-aaacfycx  
_oqmd: _oqmd:oqmd-27616  
_tdb: _tdb:AgLu-18Shi.tdb:AG2LU_C11B  


### TDB models of AG2LU_C11B (1): PHASE and CONSTITUENT statements as written

[AgLu-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLu-18Shi.tdb): AG2LU_C11B, type code %, sha256 `be02bf2c5df06dfd…`

~~~~text
53: PHASE AG2LU_C11B % 2 2 1 !
54: CONST AG2LU_C11B : AG : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## AG4LU_D1A (Ag–Lu)

- Id: `phase:ag-lu:ag4lu-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgjqv and oqmd-10654, space group 87
- Stoichiometry: Ag 0.8000, Lu 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1195.01 K, x(Lu) 0.2–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-lu:ag4lu-d1a)

Names (4): _corpus: _corpus:phase:ag-lu:ag4lu-d1a  
_mp: _mp:mp-aaabgjqv  
_oqmd: _oqmd:oqmd-10654  
_tdb: _tdb:AgLu-18Shi.tdb:AG4LU_D1A  


### TDB models of AG4LU_D1A (1): PHASE and CONSTITUENT statements as written

[AgLu-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLu-18Shi.tdb): AG4LU_D1A, type code %, sha256 `be02bf2c5df06dfd…`

~~~~text
48: PHASE AG4LU_D1A % 2 4 1 !
49: CONST AG4LU_D1A : AG : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## AGLU_B2 (Ag–Lu)

- Id: `phase:ag-lu:aglu-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.5000, Lu 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1396.82 K, x(Lu) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-lu:aglu-b2)

Names (2): _corpus: _corpus:phase:ag-lu:aglu-b2  
_tdb: _tdb:AgLu-18Shi.tdb:AGLU_B2  


### TDB models of AGLU_B2 (1): PHASE and CONSTITUENT statements as written

[AgLu-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLu-18Shi.tdb): AGLU_B2, type code %A, sha256 `be02bf2c5df06dfd…`

~~~~text
58: PHASE AGLU_B2 %A 2 1 1 !
59: CONST AGLU_B2 : AG : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## BCC_A2 (Ag–Lu)

- Id: `phase:ag-lu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-lu:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-lu:bcc-a2  
_tdb: _tdb:AgLu-18Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgLu-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLu-18Shi.tdb): BCC_A2, type code %B, sha256 `be02bf2c5df06dfd…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## FCC_A1 (Ag–Lu)

- Id: `phase:ag-lu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Lu) 0–0.35158
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-lu:fcc-a1)

Names (2): _corpus: _corpus:phase:ag-lu:fcc-a1  
_tdb: _tdb:AgLu-18Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgLu-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLu-18Shi.tdb): FCC_A1, type code %A, sha256 `be02bf2c5df06dfd…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AG% LU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## HCP_A3 (Ag–Lu)

- Id: `phase:ag-lu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2016.99 K, x(Lu) 0.97813–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-lu:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-lu:hcp-a3  
_tdb: _tdb:AgLu-18Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgLu-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLu-18Shi.tdb): HCP_A3, type code %A, sha256 `be02bf2c5df06dfd…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AG LU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## LIQUID (Ag–Lu)

- Id: `phase:ag-lu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1088.01–2500 K, x(Lu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-lu:liquid)

Names (2): _corpus: _corpus:phase:ag-lu:liquid  
_tdb: _tdb:AgLu-18Shi.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgLu-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLu-18Shi.tdb): LIQUID, type code %, sha256 `be02bf2c5df06dfd…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AG LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

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
