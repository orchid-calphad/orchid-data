# Hg–Sn phases

> Hg–Sn system: 8 phases (tier A 3, tier C 1, liquid 1, needs_review 3); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HG-SN.html · Markdown: https://data.orchid-project.org/phases/pages/HG-SN.md

8 phases (tier A 3, tier C 1, liquid 1, needs_review 3); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HG-SN) · [full JSON](https://data.orchid-project.org/phases/systems/HG-SN.json) · [Hg–Sn system page](https://data.orchid-project.org/systems/HG-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/HG-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hg–Sn system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBO_A10](#phase-hg-sn-a10-rhombo); _phase:hg-sn:a10-rhombo_ | alpha-Hg · A10 · hR1 · R-3m (166) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 2 | 1 |
| [DIAMOND_A4](#phase-hg-sn-a4-diamond); _phase:hg-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 6 | 1 |
| [BCT_A5](#phase-hg-sn-a5-bct); _phase:hg-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 15 | 1 |
| [HGSN12_AF](#phase-hg-sn-hgsn12-af); _phase:hg-sn:hgsn12-af_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–484.23 K, x(Sn) 0.88285–0.94493 | 11 | 1 |
| [HGSN38](#phase-hg-sn-hgsn38); _phase:hg-sn:hgsn38_ | HgSn38 · hP1 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 472.06–497.11 K, x(Sn) 0.97436–0.97436 | 0 | 1 |
| [HGSN4](#phase-hg-sn-hgsn4); _phase:hg-sn:hgsn4_ |  | needs_review | not stable in 1 calculated diagram(s) | 9 | 1 |
| [HGSN7](#phase-hg-sn-hgsn7); _phase:hg-sn:hgsn7_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–362.08 K, x(Sn) 0.875–0.875 | 3 | 1 |
| [LIQUID](#phase-hg-sn-liquid); _phase:hg-sn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Sn) 0–1 | 14 | 1 |

## RHOMBO_A10 (Hg–Sn)

- Id: `phase:hg-sn:a10-rhombo`; status `assigned`
- Structure: alpha-Hg · A10 · hR1 · R-3m (166); type `st:a10-alpha-hg-hr1`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:a10-rhombo)

Names (4): _corpus: _corpus:phase:hg-sn:a10-rhombo, corpus:phase:hg-sn:rhombo-a10  
_paper: _paper:10.1361/105497103770330776:(Hg)  
_tdb: _tdb:HgSn-03Yen-LB.tdb:RHOMBO_A10  


### TDB models of RHOMBO_A10 (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): RHOMBO_A10, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
36: PHASE RHOMBO_A10 % 1 1 !
37: CONST RHOMBO_A10 : HG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase; reports values for this phase_

## DIAMOND_A4 (Hg–Sn)

- Id: `phase:hg-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:a4-diamond)

Names (4): _corpus: _corpus:phase:hg-sn:a4-diamond, corpus:phase:hg-sn:diamond-a4  
_paper: _paper:10.1361/105497103770330776:αSn  
_tdb: _tdb:HgSn-03Yen-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): DIAMOND_A4, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
26: PHASE DIAMOND_A4 % 1 1 !
27: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/cmq.1969.8.2.127](https://doi.org/10.1179/cmq.1969.8.2.127) R.W. Smith, The constitution of tin-mercury alloys at lower temperatures, Canadian Metallurgical Quarterly 8, 127-129 (1969).  
_cited as the source of values for this phase_

## BCT_A5 (Hg–Sn)

- Id: `phase:hg-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:a5-bct)

Names (6): _corpus: _corpus:phase:hg-sn:a5-bct, corpus:phase:hg-sn:bct-a5  
_paper: _paper:10.1361/105497103770330776:(βSn), paper:10.1361/105497103770330776:β, paper:10.1361/105497103770330776:βSn  
_tdb: _tdb:HgSn-03Yen-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): BCT_A5, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
31: PHASE BCT_A5 % 1 1 !
32: CONST BCT_A5 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.6028/jres.067a.008](https://doi.org/10.6028/jres.067a.008) Duane F. Taylor, Claire L. Burns, An investigation of the constitution of the mercury-tin system, J. RES. NATL. BUR. STAN. SECT. A. 67A, 55 (1963).  
_cited as the source of values for this phase_

## HGSN12_AF (Hg–Sn)

- Id: `phase:hg-sn:hgsn12-af`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_A_f; site_ratios_contradict_A_f:HgSn-03Yen-LB.tdb
- Candidate (literature_printed): HgSn12 · hP1 — printed with a label mapped to this phase
- Candidate (name_token): HgSn12 · A_f · hP1 · P6/mmm (191) — Strukturbericht/word 'AF' in the TDB name
- Candidate (sgte_mmc2): HgSn12 · A_f · hP1 · P6/mmm (191) — Hallstedt 2025 mmc2 row for HGSN12_AF: HgSn12
- Candidate (tdb_comment): HgSn12 · hP1 · P6/mmm — HgSn-03Yen-LB.tdb: 'Prototype HgSn12 (hP1, P6/mmm)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–484.23 K, x(Sn) 0.88285–0.94493
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:hgsn12-af)

Names (3): _corpus: _corpus:phase:hg-sn:hgsn12-af  
_paper: _paper:10.1361/105497103770330776:γ  
_tdb: _tdb:HgSn-03Yen-LB.tdb:HGSN12_AF  


### TDB models of HGSN12_AF (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): HGSN12_AF, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
51: PHASE HGSN12_AF % 2 1 6 !
52: CONST HGSN12_AF : HG VA : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/cmq.1969.8.2.127](https://doi.org/10.1179/cmq.1969.8.2.127) R.W. Smith, The constitution of tin-mercury alloys at lower temperatures, Canadian Metallurgical Quarterly 8, 127-129 (1969).  
_cited as the source of values for this phase_
- [doi:10.6028/jres.067a.008](https://doi.org/10.6028/jres.067a.008) Duane F. Taylor, Claire L. Burns, An investigation of the constitution of the mercury-tin system, J. RES. NATL. BUR. STAN. SECT. A. 67A, 55 (1963).  
_cited as the source of values for this phase_

## HGSN38 (Hg–Sn)

- Id: `phase:hg-sn:hgsn38`; status `assigned`
- Structure: HgSn38 · hP1 · P6/mmm (191); type `st:hgsn38-hp1`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hg 0.0256, Sn 0.9744
- Stability: stable in 1 of 1 calculated diagram(s): 472.06–497.11 K, x(Sn) 0.97436–0.97436
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:hgsn38)

Names (2): _corpus: _corpus:phase:hg-sn:hgsn38  
_tdb: _tdb:HgSn-03Yen-LB.tdb:HGSN38  


### TDB models of HGSN38 (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): HGSN38, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
56: PHASE HGSN38 % 2 1 38 !
57: CONST HGSN38 : HG : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase_

## HGSN4 (Hg–Sn)

- Id: `phase:hg-sn:hgsn4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (HgSn4) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (HgSn4) — Hallstedt 2025 mmc2 row for HGSN4: HgSn4
- Stoichiometry: Hg 0.2000, Sn 0.8000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:hgsn4)

Names (3): _corpus: _corpus:phase:hg-sn:hgsn4  
_paper: _paper:10.1361/105497103770330776:HgSn4  
_tdb: _tdb:HgSn-03Yen-LB.tdb:HGSN4  


### TDB models of HGSN4 (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): HGSN4, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
41: PHASE HGSN4 % 2 1 4 !
42: CONST HGSN4 : HG : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase; reports values for this phase_

## HGSN7 (Hg–Sn)

- Id: `phase:hg-sn:hgsn7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (HgSn7) — Hallstedt 2025 mmc2 row for HGSN7: HgSn7
- Stoichiometry: Hg 0.1250, Sn 0.8750
- Stability: stable in 1 of 1 calculated diagram(s): 300–362.08 K, x(Sn) 0.875–0.875
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:hgsn7)

Names (3): _corpus: _corpus:phase:hg-sn:hgsn7  
_paper: _paper:10.1361/105497103770330776:δ, HgSn7  
_tdb: _tdb:HgSn-03Yen-LB.tdb:HGSN7  


### TDB models of HGSN7 (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): HGSN7, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
46: PHASE HGSN7 % 2 1 7 !
47: CONST HGSN7 : HG : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Hg–Sn)

- Id: `phase:hg-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Sn) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-sn:liquid)

Names (3): _corpus: _corpus:phase:hg-sn:liquid  
_paper: _paper:10.1361/105497103770330776:L  
_tdb: _tdb:HgSn-03Yen-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HgSn-03Yen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgSn-03Yen-LB.tdb): LIQUID, type code %, sha256 `c2b9fce680ecdfc1…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : HG SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497103770330776](https://doi.org/10.1361/105497103770330776) Yee-Wen Yen, Joachim Gröbner, Rainer Schmid-Fetzer, Yee-Wen Yen, Steve C. Hansen, Thermodynamic assessment of the Hg-Sn system, JPE 24, 151-167 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.6028/jres.067a.008](https://doi.org/10.6028/jres.067a.008) Duane F. Taylor, Claire L. Burns, An investigation of the constitution of the mercury-tin system, J. RES. NATL. BUR. STAN. SECT. A. 67A, 55 (1963).  
_cited as the source of values for this phase_
- [doi:10.1179/cmq.1969.8.2.127](https://doi.org/10.1179/cmq.1969.8.2.127) R.W. Smith, The constitution of tin-mercury alloys at lower temperatures, Canadian Metallurgical Quarterly 8, 127-129 (1969).  
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
