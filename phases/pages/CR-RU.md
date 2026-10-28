# Cr–Ru phases

> Cr–Ru system: 7 phases (tier A 4, liquid 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-RU.html · Markdown: https://data.orchid-project.org/phases/pages/CR-RU.md

7 phases (tier A 4, liquid 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-RU) · [full JSON](https://data.orchid-project.org/phases/systems/CR-RU.json) · [Cr–Ru system page](https://data.orchid-project.org/systems/CR-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Ru system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-ru-bcc-a2); _phase:cr-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2180.98 K, x(Ru) 0–0.32063 | 13 | 2 |
| [CR2RU_D8B](#phase-cr-ru-cr2ru-d8b); _phase:cr-ru:cr2ru-d8b_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1106.06–1841.2 K, x(Ru) 0.33333–0.33333 | 6 | 1 |
| [CR3RU_A15](#phase-cr-ru-cr3ru-a15); _phase:cr-ru:cr3ru-a15_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1022.26–1272.95 K, x(Ru) 0.25–0.315 | 15 | 2 |
| [SIGMA_D8B](#phase-cr-ru-d8b-sigma); _phase:cr-ru:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1072.87–1852.76 K, x(Ru) 0.31166–0.35329 | 9 | 1 |
| [FCC_A1](#phase-cr-ru-fcc-a1); _phase:cr-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-cr-ru-hcp-a3); _phase:cr-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.5 K, x(Ru) 0.46554–1 | 13 | 2 |
| [LIQUID](#phase-cr-ru-liquid); _phase:cr-ru:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1880.45–4000 K, x(Ru) 0–1 | 4 | 2 |

## BCC_A2 (Cr–Ru)

- Id: `phase:cr-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2180.98 K, x(Ru) 0–0.32063
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ru:bcc-a2)

Names (5): _corpus: _corpus:phase:cr-ru:bcc-a2  
_paper: _paper:10.1016/j.intermet.2015.04.011:bcc (Cr), paper:10.1016/j.intermet.2015.04.011:bcc(Cr)  
_tdb: _tdb:CrRu-05Che-LB.tdb:BCC_A2, tdb:CrRu-15Zhu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CrRu-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-05Che-LB.tdb): BCC_A2, type code %B, sha256 `6aaa1a7c6fe998e3…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR% RU : VA : !
~~~~

[CrRu-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-15Zhu.tdb): BCC_A2, type code %B, sha256 `8548a182cf1b5ea4…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% RU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2015.04.011](https://doi.org/10.1016/j.intermet.2015.04.011) L.L. Zhu, H.Y. Qi, L. Jiang, Z.P. Jin, J.-C. Zhao, Experimental determination of the Ni–Cr–Ru phase diagram and thermodynamic reassessments of the Cr–Ru and Ni–Cr–Ru systems, Intermetallics 64, 86-95 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873189](https://doi.org/10.1007/bf02873189) M. Venkatraman, J. P. Neumann, The Cr−Ru (chromium-ruthenium) system, JPE 8, 109-112 (1987).  
_cited as the source of values for this phase_

## CR2RU_D8B (Cr–Ru)

- Id: `phase:cr-ru:cr2ru-d8b`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D8_b; stoichiometry_contradicts_D8_b:CrRu-05Che-LB.tdb
- Candidate (literature_printed): CrFe · tP30 — printed with a label mapped to this phase
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (sgte_mmc2): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for CR2RU_D8B: Cr2Ru
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — CrRu-05Che-LB.tdb: 'Prototype CrFe (tP30, P4_2/mnm) sigma'
- Stoichiometry: Cr 0.6667, Ru 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1106.06–1841.2 K, x(Ru) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ru:cr2ru-d8b)

Names (3): _corpus: _corpus:phase:cr-ru:cr2ru-d8b  
_paper: _paper:10.1016/s1001-0521(06)60106-x:Cr2Ru  
_tdb: _tdb:CrRu-05Che-LB.tdb:CR2RU_D8B  


### TDB models of CR2RU_D8B (1): PHASE and CONSTITUENT statements as written

[CrRu-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-05Che-LB.tdb): CR2RU_D8B, type code %, sha256 `6aaa1a7c6fe998e3…`

~~~~text
46: PHASE CR2RU_D8B % 2 2 1 !
47: CONST CR2RU_D8B : CR : RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/s1001-0521(06)60106-x](https://doi.org/10.1016/s1001-0521%2806%2960106-x) A WATSON, L CORNISH, R SUSS, Development of a database for the prediction of phases in Pt-based Superalloys: Cr-Pt-Ru, Rare Metals 25, 597-607 (2006).  
_reports values for this phase_

## CR3RU_A15 (Cr–Ru)

- Id: `phase:cr-ru:cr3ru-a15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_A15:CrRu-15Zhu.tdb
- Candidate (literature_printed): Cr3Si · cP8 — printed with a label mapped to this phase
- Candidate (name_token): Cr3Si · A15 · cP8 · Pm-3n (223) — Strukturbericht/word 'A15' in the TDB name
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for CR3RU_A15: Cr3Ru
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — CrRu-05Che-LB.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — CrRu-15Zhu.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Stability: stable in 2 of 2 calculated diagram(s): 1022.26–1272.95 K, x(Ru) 0.25–0.315
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ru:cr3ru-a15)

Names (5): _corpus: _corpus:phase:cr-ru:cr3ru-a15  
_paper: _paper:10.1016/j.intermet.2015.04.011:Cr3Ru, paper:10.1016/s1001-0521(06)60106-x:Cr3Ru  
_tdb: _tdb:CrRu-05Che-LB.tdb:CR3RU_A15, tdb:CrRu-15Zhu.tdb:CR3RU_A15  


### TDB models of CR3RU_A15 (2): PHASE and CONSTITUENT statements as written

[CrRu-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-05Che-LB.tdb): CR3RU_A15, type code %, sha256 `6aaa1a7c6fe998e3…`

~~~~text
41: PHASE CR3RU_A15 % 2 3 1 !
42: CONST CR3RU_A15 : CR : RU : !
~~~~

[CrRu-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-15Zhu.tdb): CR3RU_A15, type code %, sha256 `8548a182cf1b5ea4…`

~~~~text
40: PHASE CR3RU_A15 % 2 0.685 0.315 !
41: CONST CR3RU_A15 : CR : RU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.intermet.2015.04.011](https://doi.org/10.1016/j.intermet.2015.04.011) L.L. Zhu, H.Y. Qi, L. Jiang, Z.P. Jin, J.-C. Zhao, Experimental determination of the Ni–Cr–Ru phase diagram and thermodynamic reassessments of the Cr–Ru and Ni–Cr–Ru systems, Intermetallics 64, 86-95 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s1001-0521(06)60106-x](https://doi.org/10.1016/s1001-0521%2806%2960106-x) A WATSON, L CORNISH, R SUSS, Development of a database for the prediction of phases in Pt-based Superalloys: Cr-Pt-Ru, Rare Metals 25, 597-607 (2006).  
_reports values for this phase_
- [doi:10.1007/bf02873189](https://doi.org/10.1007/bf02873189) M. Venkatraman, J. P. Neumann, The Cr−Ru (chromium-ruthenium) system, JPE 8, 109-112 (1987).  
_cited as the source of values for this phase_

## SIGMA_D8B (Cr–Ru)

- Id: `phase:cr-ru:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrRu-15Zhu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1072.87–1852.76 K, x(Ru) 0.31166–0.35329
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ru:d8b-sigma)

Names (4): _corpus: _corpus:phase:cr-ru:d8b-sigma, corpus:phase:cr-ru:sigma-d8b  
_paper: _paper:10.1016/j.intermet.2015.04.011:σ  
_tdb: _tdb:CrRu-15Zhu.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (1): PHASE and CONSTITUENT statements as written

[CrRu-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-15Zhu.tdb): SIGMA_D8B, type code %, sha256 `8548a182cf1b5ea4…`

~~~~text
45: PHASE SIGMA_D8B % 2 20 10 !
46: CONST SIGMA_D8B : CR% RU : CR RU% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2015.04.011](https://doi.org/10.1016/j.intermet.2015.04.011) L.L. Zhu, H.Y. Qi, L. Jiang, Z.P. Jin, J.-C. Zhao, Experimental determination of the Ni–Cr–Ru phase diagram and thermodynamic reassessments of the Cr–Ru and Ni–Cr–Ru systems, Intermetallics 64, 86-95 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873189](https://doi.org/10.1007/bf02873189) M. Venkatraman, J. P. Neumann, The Cr−Ru (chromium-ruthenium) system, JPE 8, 109-112 (1987).  
_cited as the source of values for this phase_

## FCC_A1 (Cr–Ru)

- Id: `phase:cr-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ru:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-ru:fcc-a1  
_tdb: _tdb:CrRu-05Che-LB.tdb:FCC_A1, tdb:CrRu-15Zhu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CrRu-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-05Che-LB.tdb): FCC_A1, type code %A, sha256 `6aaa1a7c6fe998e3…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR RU : VA : !
~~~~

[CrRu-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-15Zhu.tdb): FCC_A1, type code %A, sha256 `8548a182cf1b5ea4…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2015.04.011](https://doi.org/10.1016/j.intermet.2015.04.011) L.L. Zhu, H.Y. Qi, L. Jiang, Z.P. Jin, J.-C. Zhao, Experimental determination of the Ni–Cr–Ru phase diagram and thermodynamic reassessments of the Cr–Ru and Ni–Cr–Ru systems, Intermetallics 64, 86-95 (2015).  
_assessment that models this phase_

## HCP_A3 (Cr–Ru)

- Id: `phase:cr-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.5 K, x(Ru) 0.46554–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ru:hcp-a3)

Names (4): _corpus: _corpus:phase:cr-ru:hcp-a3  
_paper: _paper:10.1016/j.intermet.2015.04.011:hcp (Ru)  
_tdb: _tdb:CrRu-05Che-LB.tdb:HCP_A3, tdb:CrRu-15Zhu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CrRu-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-05Che-LB.tdb): HCP_A3, type code %A, sha256 `6aaa1a7c6fe998e3…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR RU% : VA : !
~~~~

[CrRu-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-15Zhu.tdb): HCP_A3, type code %A, sha256 `8548a182cf1b5ea4…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR RU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2015.04.011](https://doi.org/10.1016/j.intermet.2015.04.011) L.L. Zhu, H.Y. Qi, L. Jiang, Z.P. Jin, J.-C. Zhao, Experimental determination of the Ni–Cr–Ru phase diagram and thermodynamic reassessments of the Cr–Ru and Ni–Cr–Ru systems, Intermetallics 64, 86-95 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873189](https://doi.org/10.1007/bf02873189) M. Venkatraman, J. P. Neumann, The Cr−Ru (chromium-ruthenium) system, JPE 8, 109-112 (1987).  
_cited as the source of values for this phase_

## LIQUID (Cr–Ru)

- Id: `phase:cr-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1880.45–4000 K, x(Ru) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ru:liquid)

Names (4): _corpus: _corpus:phase:cr-ru:liquid  
_paper: _paper:10.1016/j.intermet.2015.04.011:L  
_tdb: _tdb:CrRu-05Che-LB.tdb:LIQUID, tdb:CrRu-15Zhu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CrRu-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-05Che-LB.tdb): LIQUID, type code %, sha256 `6aaa1a7c6fe998e3…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR RU : !
~~~~

[CrRu-15Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRu-15Zhu.tdb): LIQUID, type code %, sha256 `8548a182cf1b5ea4…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR RU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2015.04.011](https://doi.org/10.1016/j.intermet.2015.04.011) L.L. Zhu, H.Y. Qi, L. Jiang, Z.P. Jin, J.-C. Zhao, Experimental determination of the Ni–Cr–Ru phase diagram and thermodynamic reassessments of the Cr–Ru and Ni–Cr–Ru systems, Intermetallics 64, 86-95 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873189](https://doi.org/10.1007/bf02873189) M. Venkatraman, J. P. Neumann, The Cr−Ru (chromium-ruthenium) system, JPE 8, 109-112 (1987).  
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
