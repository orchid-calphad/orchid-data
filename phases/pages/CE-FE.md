# Ce–Fe phases

> Ce–Fe system: 6 phases (tier A 4, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-FE.html · Markdown: https://data.orchid-project.org/phases/pages/CE-FE.md

6 phases (tier A 4, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-FE) · [full JSON](https://data.orchid-project.org/phases/systems/CE-FE.json) · [Ce–Fe system page](https://data.orchid-project.org/systems/CE-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Fe system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-fe-bcc-a2); _phase:ce-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.67 K, x(Fe) 0–1 | 7 | 3 |
| [CE2FE17](#phase-ce-fe-ce2fe17); _phase:ce-fe:ce2fe17_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1344.81 K, x(Fe) 0.89474–0.89474 | 12 | 3 |
| [CEFE2_C15](#phase-ce-fe-cefe2-c15); _phase:ce-fe:cefe2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1205.9 K, x(Fe) 0.66667–0.66667 | 3 | 3 |
| [FCC_A1](#phase-ce-fe-fcc-a1); _phase:ce-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1690 K, x(Fe) 0–1 | 14 | 3 |
| [HCP_A3](#phase-ce-fe-hcp-a3); _phase:ce-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ce-fe-liquid); _phase:ce-fe:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 864.63–2500 K, x(Fe) 0–1 | 14 | 3 |

## BCC_A2 (Ce–Fe)

- Id: `phase:ce-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.67 K, x(Fe) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-fe:bcc-a2)

Names (7): _corpus: _corpus:phase:ce-fe:bcc-a2  
_paper: _paper:10.1016/j.calphad.2006.06.003:(αFe), paper:10.1016/j.calphad.2006.06.003:(δCe), paper:10.1016/j.calphad.2006.06.003:(δFe)  
_tdb: _tdb:CeFe-06Su.tdb:BCC_A2, tdb:CeFe-19Zhu.tdb:BCC_A2, tdb:CeFe-23Su.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CeFe-06Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-06Su.tdb): BCC_A2, type code %B, sha256 `a87f5d2608ea5fa6…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CE% FE% : VA : !
~~~~

[CeFe-19Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-19Zhu.tdb): BCC_A2, type code %B, sha256 `060cbd7329e66774…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CE% FE% : VA : !
~~~~

[CeFe-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-23Su.tdb): BCC_A2, type code %B, sha256 `6da70d9310da78a2…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CE% FE% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.003](https://doi.org/10.1016/j.calphad.2006.06.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the ternary Ce–Fe–Sb system: Assessment of the Ce–Sb and Ce–Fe systems, Calphad 30, 455-460 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.009](https://doi.org/10.1016/j.calphad.2018.11.009) D. Zhu, C. Xu, C. Li, C. Guo, Z. Du, Calphad, 64, 23-36(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## CE2FE17 (Ce–Fe)

- Id: `phase:ce-fe:ce2fe17`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Ni17Th2 · hP38 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ni17Th2 · hP38 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CE2FE17: Ce2Fe17 (alpha), see also Th2Zn17
- Candidate (sgte_mmc2): Th2Zn17 · hR19 · R-3m (166) — Hallstedt 2025 mmc2 row for CE2FE17: Ce2Fe17 (beta), see also Ni17Th2
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — CeFe-06Su.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), alpha'
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — CeFe-06Su.tdb: 'Prototype Th2Zn17 (hR19, R-3m), beta'
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — CeFe-19Zhu.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), alpha'
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — CeFe-19Zhu.tdb: 'Prototype Th2Zn17 (hR19, R-3m), beta'
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc — CeFe-23Su.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc), alpha'
- Stoichiometry: Ce 0.1053, Fe 0.8947
- Stability: stable in 3 of 3 calculated diagram(s): 300–1344.81 K, x(Fe) 0.89474–0.89474
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-fe:ce2fe17)

Names (5): _corpus: _corpus:phase:ce-fe:ce2fe17  
_paper: _paper:10.1016/j.calphad.2006.06.003:Ce2Fe17  
_tdb: _tdb:CeFe-06Su.tdb:CE2FE17, tdb:CeFe-19Zhu.tdb:CE2FE17, tdb:CeFe-23Su.tdb:CE2FE17  


### TDB models of CE2FE17 (3): PHASE and CONSTITUENT statements as written

[CeFe-06Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-06Su.tdb): CE2FE17, type code %, sha256 `a87f5d2608ea5fa6…`

~~~~text
51: PHASE CE2FE17 % 2 2 17 !
52: CONST CE2FE17 : CE : FE : !
~~~~

[CeFe-19Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-19Zhu.tdb): CE2FE17, type code %, sha256 `060cbd7329e66774…`

~~~~text
48: PHASE CE2FE17 % 2 2 17 !
49: CONST CE2FE17 : CE : FE : !
~~~~

[CeFe-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-23Su.tdb): CE2FE17, type code %A, sha256 `6da70d9310da78a2…`

~~~~text
48: PHASE CE2FE17 %A 2 0.105263 0.894737 !
49: CONST CE2FE17 : CE : FE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.003](https://doi.org/10.1016/j.calphad.2006.06.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the ternary Ce–Fe–Sb system: Assessment of the Ce–Sb and Ce–Fe systems, Calphad 30, 455-460 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.009](https://doi.org/10.1016/j.calphad.2018.11.009) D. Zhu, C. Xu, C. Li, C. Guo, Z. Du, Calphad, 64, 23-36(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## CEFE2_C15 (Ce–Fe)

- Id: `phase:ce-fe:cefe2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.3333, Fe 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1205.9 K, x(Fe) 0.66667–0.66667
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-fe:cefe2-c15)

Names (5): _corpus: _corpus:phase:ce-fe:cefe2-c15  
_paper: _paper:10.1016/j.calphad.2006.06.003:CeFe2  
_tdb: _tdb:CeFe-06Su.tdb:CEFE2_C15, tdb:CeFe-19Zhu.tdb:CEFE2_C15, tdb:CeFe-23Su.tdb:CEFE2_C15  


### TDB models of CEFE2_C15 (3): PHASE and CONSTITUENT statements as written

[CeFe-06Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-06Su.tdb): CEFE2_C15, type code %, sha256 `a87f5d2608ea5fa6…`

~~~~text
45: PHASE CEFE2_C15 % 2 1 2 !
46: CONST CEFE2_C15 : CE : FE : !
~~~~

[CeFe-19Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-19Zhu.tdb): CEFE2_C15, type code %, sha256 `060cbd7329e66774…`

~~~~text
42: PHASE CEFE2_C15 % 2 1 2 !
43: CONST CEFE2_C15 : CE : FE : !
~~~~

[CeFe-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-23Su.tdb): CEFE2_C15, type code %A, sha256 `6da70d9310da78a2…`

~~~~text
42: PHASE CEFE2_C15 %A 2 0.333333 0.666667 !
43: CONST CEFE2_C15 : CE : FE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.003](https://doi.org/10.1016/j.calphad.2006.06.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the ternary Ce–Fe–Sb system: Assessment of the Ce–Sb and Ce–Fe systems, Calphad 30, 455-460 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.009](https://doi.org/10.1016/j.calphad.2018.11.009) D. Zhu, C. Xu, C. Li, C. Guo, Z. Du, Calphad, 64, 23-36(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## FCC_A1 (Ce–Fe)

- Id: `phase:ce-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1690 K, x(Fe) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-fe:fcc-a1)

Names (6): _corpus: _corpus:phase:ce-fe:fcc-a1  
_paper: _paper:10.1016/j.calphad.2006.06.003:(γCe), paper:10.1016/j.calphad.2006.06.003:(γFe)  
_tdb: _tdb:CeFe-06Su.tdb:FCC_A1, tdb:CeFe-19Zhu.tdb:FCC_A1, tdb:CeFe-23Su.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CeFe-06Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-06Su.tdb): FCC_A1, type code %A, sha256 `a87f5d2608ea5fa6…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CE% FE% : VA : !
~~~~

[CeFe-19Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-19Zhu.tdb): FCC_A1, type code %A, sha256 `060cbd7329e66774…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CE% FE% : VA : !
~~~~

[CeFe-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-23Su.tdb): FCC_A1, type code %A, sha256 `6da70d9310da78a2…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CE% FE% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.003](https://doi.org/10.1016/j.calphad.2006.06.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the ternary Ce–Fe–Sb system: Assessment of the Ce–Sb and Ce–Fe systems, Calphad 30, 455-460 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.009](https://doi.org/10.1016/j.calphad.2018.11.009) D. Zhu, C. Xu, C. Li, C. Guo, Z. Du, Calphad, 64, 23-36(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## HCP_A3 (Ce–Fe)

- Id: `phase:ce-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-fe:hcp-a3)

Names (4): _corpus: _corpus:phase:ce-fe:hcp-a3  
_tdb: _tdb:CeFe-06Su.tdb:HCP_A3, tdb:CeFe-19Zhu.tdb:HCP_A3, tdb:CeFe-23Su.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CeFe-06Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-06Su.tdb): HCP_A3, type code %A, sha256 `a87f5d2608ea5fa6…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CE FE : VA : !
~~~~

[CeFe-19Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-19Zhu.tdb): HCP_A3, type code %A, sha256 `060cbd7329e66774…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CE FE : VA : !
~~~~

[CeFe-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-23Su.tdb): HCP_A3, type code %A, sha256 `6da70d9310da78a2…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CE FE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.003](https://doi.org/10.1016/j.calphad.2006.06.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the ternary Ce–Fe–Sb system: Assessment of the Ce–Sb and Ce–Fe systems, Calphad 30, 455-460 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.009](https://doi.org/10.1016/j.calphad.2018.11.009) D. Zhu, C. Xu, C. Li, C. Guo, Z. Du, Calphad, 64, 23-36(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## LIQUID (Ce–Fe)

- Id: `phase:ce-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 864.63–2500 K, x(Fe) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-fe:liquid)

Names (5): _corpus: _corpus:phase:ce-fe:liquid  
_paper: _paper:10.1016/j.calphad.2006.06.003:Liq.  
_tdb: _tdb:CeFe-06Su.tdb:LIQUID, tdb:CeFe-19Zhu.tdb:LIQUID, tdb:CeFe-23Su.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CeFe-06Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-06Su.tdb): LIQUID, type code %, sha256 `a87f5d2608ea5fa6…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CE FE : !
~~~~

[CeFe-19Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-19Zhu.tdb): LIQUID, type code %, sha256 `060cbd7329e66774…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CE FE : !
~~~~

[CeFe-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeFe-23Su.tdb): LIQUID, type code %, sha256 `6da70d9310da78a2…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CE FE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.06.003](https://doi.org/10.1016/j.calphad.2006.06.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the ternary Ce–Fe–Sb system: Assessment of the Ce–Sb and Ce–Fe systems, Calphad 30, 455-460 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.009](https://doi.org/10.1016/j.calphad.2018.11.009) D. Zhu, C. Xu, C. Li, C. Guo, Z. Du, Calphad, 64, 23-36(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
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
