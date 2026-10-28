# Al–S phases

> Al–S system: 9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-S.html · Markdown: https://data.orchid-project.org/phases/pages/AL-S.md

9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-S) · [full JSON](https://data.orchid-project.org/phases/systems/AL-S.json) · [Al–S system page](https://data.orchid-project.org/systems/AL-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–S system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-al-s-a16-orthorhombic); _phase:al-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(S) 1–1 | 0 | 1 |
| [AL2S3_ALPHA](#phase-al-s-al2s3-alpha); _phase:al-s:al2s3-alpha_ | Al2S3-alpha · hP30 · P6_1 (169) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1273.69 K, x(S) 0.6–0.6 | 6 | 1 |
| [AL2S3_D51](#phase-al-s-al2s3-d51); _phase:al-s:al2s3-d51_ | alpha-Al2O3 · D5_1 · hR10 · R-3c (167) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1273.69–1363.53 K, x(S) 0.6–0.6 | 9 | 1 |
| [ALS](#phase-al-s-als); _phase:al-s:als_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1284.46–1332.74 K, x(S) 0.5–0.5 | 10 | 1 |
| [BCC_A2](#phase-al-s-bcc-a2); _phase:al-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 4 | 1 |
| [FCC_A1](#phase-al-s-fcc-a1); _phase:al-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–933.47 K, x(S) 0–0 | 2 | 1 |
| [HCP_A3](#phase-al-s-hcp-a3); _phase:al-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-al-s-liquid); _phase:al-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1 | 16 | 1 |
| [MONOCLINIC_S](#phase-al-s-s-monoclinic); _phase:al-s:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## ORTHORHOMBIC_A16 (Al–S)

- Id: `phase:al-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:al-s:a16-orthorhombic  
_tdb: _tdb:AlS-19Shi.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): ORTHORHOMBIC_A16, type code %, sha256 `4298f9d489e1f952…`

~~~~text
51: PHASE ORTHORHOMBIC_A16 % 1 1 !
52: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase_

## AL2S3_ALPHA (Al–S)

- Id: `phase:al-s:al2s3-alpha`; status `assigned`
- Structure: Al2S3-alpha · hP30 · P6_1 (169); type `st:al2s3-alpha-hp30`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, S 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1273.69 K, x(S) 0.6–0.6
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:al2s3-alpha)

Names (3): _corpus: _corpus:phase:al-s:al2s3-alpha  
_paper: _paper:10.1007/s11669-019-00733-z:αAl2S3  
_tdb: _tdb:AlS-19Shi.tdb:AL2S3_ALPHA  


### TDB models of AL2S3_ALPHA (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): AL2S3_ALPHA, type code %, sha256 `4298f9d489e1f952…`

~~~~text
66: PHASE AL2S3_ALPHA % 2 2 3 !
67: CONST AL2S3_ALPHA : AL : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873197](https://doi.org/10.1007/bf02873197) R. C. Sharma, Y. A. Chang, The Al−S (Aluminum-Sulfur) system, JPE 8 (1987).  
_cited as the source of values for this phase_

## AL2S3_D51 (Al–S)

- Id: `phase:al-s:al2s3-d51`; status `assigned`
- Structure: alpha-Al2O3 · D5_1 · hR10 · R-3c (167); type `st:d5-1-alpha-al2o3-hr10`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.4000, S 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 1273.69–1363.53 K, x(S) 0.6–0.6
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:al2s3-d51)

Names (3): _corpus: _corpus:phase:al-s:al2s3-d51  
_paper: _paper:10.1007/s11669-019-00733-z:γAl2S3  
_tdb: _tdb:AlS-19Shi.tdb:AL2S3_D51  


### TDB models of AL2S3_D51 (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): AL2S3_D51, type code %, sha256 `4298f9d489e1f952…`

~~~~text
71: PHASE AL2S3_D51 % 2 2 3 !
72: CONST AL2S3_D51 : AL : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873197](https://doi.org/10.1007/bf02873197) R. C. Sharma, Y. A. Chang, The Al−S (Aluminum-Sulfur) system, JPE 8 (1987).  
_cited as the source of values for this phase_

## ALS (Al–S)

- Id: `phase:al-s:als`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (AlS) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (AlS) — Hallstedt 2025 mmc2 row for ALS: AlS
- Stoichiometry: Al 0.5000, S 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 1284.46–1332.74 K, x(S) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:als)

Names (3): _corpus: _corpus:phase:al-s:als  
_paper: _paper:10.1007/s11669-019-00733-z:AlS  
_tdb: _tdb:AlS-19Shi.tdb:ALS  


### TDB models of ALS (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): ALS, type code %, sha256 `4298f9d489e1f952…`

~~~~text
61: PHASE ALS % 2 1 1 !
62: CONST ALS : AL : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873197](https://doi.org/10.1007/bf02873197) R. C. Sharma, Y. A. Chang, The Al−S (Aluminum-Sulfur) system, JPE 8 (1987).  
_cited as the source of values for this phase_

## BCC_A2 (Al–S)

- Id: `phase:al-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:bcc-a2)

Names (3): _corpus: _corpus:phase:al-s:bcc-a2  
_paper: _paper:10.1007/s11669-019-00733-z:(βS)  
_tdb: _tdb:AlS-19Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): BCC_A2, type code %B, sha256 `4298f9d489e1f952…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : AL S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Al–S)

- Id: `phase:al-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–933.47 K, x(S) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:fcc-a1)

Names (3): _corpus: _corpus:phase:al-s:fcc-a1  
_paper: _paper:10.1007/s11669-019-00733-z:(Al)  
_tdb: _tdb:AlS-19Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): FCC_A1, type code %A, sha256 `4298f9d489e1f952…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AL% S : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873197](https://doi.org/10.1007/bf02873197) R. C. Sharma, Y. A. Chang, The Al−S (Aluminum-Sulfur) system, JPE 8 (1987).  
_cited as the source of values for this phase_

## HCP_A3 (Al–S)

- Id: `phase:al-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:hcp-a3)

Names (2): _corpus: _corpus:phase:al-s:hcp-a3  
_tdb: _tdb:AlS-19Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): HCP_A3, type code %A, sha256 `4298f9d489e1f952…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : AL : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase_

## LIQUID (Al–S)

- Id: `phase:al-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:liquid)

Names (5): _corpus: _corpus:phase:al-s:liquid  
_paper: _paper:10.1007/s11669-019-00733-z:L1, paper:10.1007/s11669-019-00733-z:L2, paper:10.1007/s11669-019-00733-z:L3  
_tdb: _tdb:AlS-19Shi.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): LIQUID, type code %, sha256 `4298f9d489e1f952…`

~~~~text
31: PHASE LIQUID % 1 1 !
32: CONST LIQUID : AL AL2S3 S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873197](https://doi.org/10.1007/bf02873197) R. C. Sharma, Y. A. Chang, The Al−S (Aluminum-Sulfur) system, JPE 8 (1987).  
_cited as the source of values for this phase_

## MONOCLINIC_S (Al–S)

- Id: `phase:al-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — AlS-19Shi.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-s:s-monoclinic)

Names (3): _corpus: _corpus:phase:al-s:s-monoclinic, corpus:phase:al-s:monoclinic-s  
_tdb: _tdb:AlS-19Shi.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[AlS-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb): MONOCLINIC_S, type code %, sha256 `4298f9d489e1f952…`

~~~~text
56: PHASE MONOCLINIC_S % 1 1 !
57: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
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
