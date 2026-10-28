# Al–Sn phases

> Al–Sn system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-SN.html · Markdown: https://data.orchid-project.org/phases/pages/AL-SN.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-SN) · [full JSON](https://data.orchid-project.org/phases/systems/AL-SN.json) · [Al–Sn system page](https://data.orchid-project.org/systems/AL-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Sn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-al-sn-a4-diamond); _phase:al-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCT_A5](#phase-al-sn-a5-bct); _phase:al-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 0.98945–1 | 1 | 3 |
| [BCC_A2](#phase-al-sn-bcc-a2); _phase:al-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-al-sn-fcc-a1); _phase:al-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–941.38 K, x(Sn) 0–0.00041 | 1 | 3 |
| [HCP_A3](#phase-al-sn-hcp-a3); _phase:al-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-al-sn-liquid); _phase:al-sn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 499.85–2500 K, x(Sn) 0–1 | 1 | 3 |

## DIAMOND_A4 (Al–Sn)

- Id: `phase:al-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sn:a4-diamond)

Names (2): _corpus: _corpus:phase:al-sn:a4-diamond  
_tdb: _tdb:AlSn-98Fri-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[AlSn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-98Fri-LB.tdb): DIAMOND_A4, type code %, sha256 `1102d78dab680fb9…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

## BCT_A5 (Al–Sn)

- Id: `phase:al-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 0.98945–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sn:a5-bct)

Names (6): _corpus: _corpus:phase:al-sn:a5-bct, corpus:phase:al-sn:bct-a5  
_paper: _paper:sha256-85fd53a1a176b694:bct-A5  
_tdb: _tdb:AlSn-19Che.tdb:BCT_A5, tdb:AlSn-79Ans.tdb:BCT_A5, tdb:AlSn-98Fri-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (3): PHASE and CONSTITUENT statements as written

[AlSn-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-19Che.tdb): BCT_A5, type code %, sha256 `434b627f2d64558b…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : AL SN% : !
~~~~

[AlSn-79Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-79Ans.tdb): BCT_A5, type code %, sha256 `72b5c10a35428d7e…`

~~~~text
45: PHASE BCT_A5 % 1 1 !
46: CONST BCT_A5 : SN : !
~~~~

[AlSn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-98Fri-LB.tdb): BCT_A5, type code %, sha256 `1102d78dab680fb9…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : AL SN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.005](https://doi.org/10.1016/j.calphad.2019.01.005) T. Cheng, Y. Tang, L. Zhang, Calphad, 64, 354-63(2019).  
_assessment that models this phase_

## BCC_A2 (Al–Sn)

- Id: `phase:al-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sn:bcc-a2)

Names (4): _corpus: _corpus:phase:al-sn:bcc-a2  
_tdb: _tdb:AlSn-19Che.tdb:BCC_A2, tdb:AlSn-79Ans.tdb:BCC_A2, tdb:AlSn-98Fri-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlSn-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-19Che.tdb): BCC_A2, type code %B, sha256 `434b627f2d64558b…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL SN : VA : !
~~~~

[AlSn-79Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-79Ans.tdb): BCC_A2, type code %B, sha256 `72b5c10a35428d7e…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL SN : VA : !
~~~~

[AlSn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-98Fri-LB.tdb): BCC_A2, type code %B, sha256 `1102d78dab680fb9…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.005](https://doi.org/10.1016/j.calphad.2019.01.005) T. Cheng, Y. Tang, L. Zhang, Calphad, 64, 354-63(2019).  
_assessment that models this phase_

## FCC_A1 (Al–Sn)

- Id: `phase:al-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–941.38 K, x(Sn) 0–0.00041
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sn:fcc-a1)

Names (5): _corpus: _corpus:phase:al-sn:fcc-a1  
_paper: _paper:sha256-85fd53a1a176b694:fcc-A1  
_tdb: _tdb:AlSn-19Che.tdb:FCC_A1, tdb:AlSn-79Ans.tdb:FCC_A1, tdb:AlSn-98Fri-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlSn-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-19Che.tdb): FCC_A1, type code %A, sha256 `434b627f2d64558b…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL% SN : VA : !
~~~~

[AlSn-79Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-79Ans.tdb): FCC_A1, type code %A, sha256 `72b5c10a35428d7e…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% SN : VA : !
~~~~

[AlSn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-98Fri-LB.tdb): FCC_A1, type code %A, sha256 `1102d78dab680fb9…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL% SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.005](https://doi.org/10.1016/j.calphad.2019.01.005) T. Cheng, Y. Tang, L. Zhang, Calphad, 64, 354-63(2019).  
_assessment that models this phase_

## HCP_A3 (Al–Sn)

- Id: `phase:al-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sn:hcp-a3)

Names (4): _corpus: _corpus:phase:al-sn:hcp-a3  
_tdb: _tdb:AlSn-19Che.tdb:HCP_A3, tdb:AlSn-79Ans.tdb:HCP_A3, tdb:AlSn-98Fri-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlSn-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-19Che.tdb): HCP_A3, type code %A, sha256 `434b627f2d64558b…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AL SN : VA : !
~~~~

[AlSn-79Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-79Ans.tdb): HCP_A3, type code %A, sha256 `72b5c10a35428d7e…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL SN : VA : !
~~~~

[AlSn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-98Fri-LB.tdb): HCP_A3, type code %A, sha256 `1102d78dab680fb9…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.005](https://doi.org/10.1016/j.calphad.2019.01.005) T. Cheng, Y. Tang, L. Zhang, Calphad, 64, 354-63(2019).  
_assessment that models this phase_

## LIQUID (Al–Sn)

- Id: `phase:al-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 499.85–2500 K, x(Sn) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sn:liquid)

Names (5): _corpus: _corpus:phase:al-sn:liquid  
_paper: _paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:AlSn-19Che.tdb:LIQUID, tdb:AlSn-79Ans.tdb:LIQUID, tdb:AlSn-98Fri-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlSn-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-19Che.tdb): LIQUID, type code %, sha256 `434b627f2d64558b…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL SN : !
~~~~

[AlSn-79Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-79Ans.tdb): LIQUID, type code %, sha256 `72b5c10a35428d7e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL SN : !
~~~~

[AlSn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSn-98Fri-LB.tdb): LIQUID, type code %, sha256 `1102d78dab680fb9…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.005](https://doi.org/10.1016/j.calphad.2019.01.005) T. Cheng, Y. Tang, L. Zhang, Calphad, 64, 354-63(2019).  
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
