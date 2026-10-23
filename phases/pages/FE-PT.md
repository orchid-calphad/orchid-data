# Fe–Pt phases

> Fe–Pt system: 5 phases (tier A 3, liquid 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-PT.html · Markdown: https://data.orchid-project.org/phases/pages/FE-PT.md

5 phases (tier A 3, liquid 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-PT) · [full JSON](https://data.orchid-project.org/phases/systems/FE-PT.json) · [Fe–Pt system page](https://data.orchid-project.org/systems/FE-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Pt system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-pt-bcc-a2); _phase:fe-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1818.78 K, x(Pt) 0–0.04262 | 0 | 2 |
| [FCC_4SL](#phase-fe-pt-fcc-4sl); _phase:fe-pt:fcc-4sl_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2499 K, x(Pt) 0–1 | 0 | 2 |
| [A1_FCC](#phase-fe-pt-fcc-a1); _phase:fe-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 4 calculated diagram(s): 300–2020 K, x(Pt) 0–0.98 | 0 | 4 |
| [HCP_A3](#phase-fe-pt-hcp-a3); _phase:fe-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-fe-pt-liquid); _phase:fe-pt:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1772.02–2500 K, x(Pt) 0–1 | 0 | 2 |

## BCC_A2 (Fe–Pt)

- Id: `phase:fe-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1818.78 K, x(Pt) 0–0.04262
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pt:bcc-a2)

Names (3): _corpus: _corpus:phase:fe-pt:bcc-a2  
_tdb: _tdb:FePt-01Fre-LB.tdb:BCC_A2, tdb:FePt-01Fre-orig.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FePt-01Fre-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-LB.tdb): BCC_A2, type code %B, sha256 `1c359cccce909a24…`

~~~~text
53: PHASE BCC_A2 %B 2 1 3 !
54: CONST BCC_A2 : FE% PT : VA : !
~~~~

[FePt-01Fre-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-orig.tdb): BCC_A2, type code %B, sha256 `a5386a32fd8404bf…`

~~~~text
52: PHASE BCC_A2 %B 2 1 3 !
53: CONST BCC_A2 : FE% PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00006-8](https://doi.org/10.1016/S0364-5916%2802%2900006-8) P. Fredriksson, B. Sundman, Calphad, 25, 535-48(2001).  
_assessment that models this phase_

## FCC_4SL (Fe–Pt)

- Id: `phase:fe-pt:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:FePt-01Fre-LB.tdb_model_is_partitioned; order_disorder_ambiguity:FePt-01Fre-orig.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; sgte_mmc2_rows_disagree; unrecognised_name_tokens:4SL
- Candidate (dft_mp): P4/mmm (123) — on-hull MP FePt at x(PT)=0.5000
- Candidate (dft_mp): Pm-3m (221) — on-hull MP FePt3 at x(PT)=0.7500
- Candidate (dft_oqmd): P4/mmm (123) — on-hull OQMD Fe1 Pt1 at x(PT)=0.5000
- Candidate (dft_oqmd): P4/mbm (127) — on-hull OQMD Fe1 Pt3 at x(PT)=0.7500
- Candidate (dft_oqmd): Cmmm (65) — on-hull OQMD Fe1 Pt5 at x(PT)=0.8333
- Candidate (dft_oqmd): P2/m (10) — on-hull OQMD Fe5 Pt11 at x(PT)=0.6875
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (sgte_mmc2): AuCu · L1_0 · tP4 · P4/mmm (123) — Hallstedt 2025 mmc2 row for FCC_4SL: AlTi, AuCu, CoPt, CrPt, FeNi, FePt, MnNi
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pt:fcc-4sl)

Names (3): _corpus: _corpus:phase:fe-pt:fcc-4sl  
_tdb: _tdb:FePt-01Fre-LB.tdb:FCC_4SL, tdb:FePt-01Fre-orig.tdb:FCC_4SL  


### TDB models of FCC_4SL (2): PHASE and CONSTITUENT statements as written

[FePt-01Fre-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-LB.tdb): FCC_4SL, type code %AY, sha256 `1c359cccce909a24…`

~~~~text
48: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
49: CONST FCC_4SL:F : FE PT : FE PT : FE PT : FE PT : VA :  !
~~~~

[FePt-01Fre-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-orig.tdb): FCC_4SL, type code %AY, sha256 `a5386a32fd8404bf…`

~~~~text
47: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
48: CONST FCC_4SL:F : FE PT : FE PT : FE PT : FE PT : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00006-8](https://doi.org/10.1016/S0364-5916%2802%2900006-8) P. Fredriksson, B. Sundman, Calphad, 25, 535-48(2001).  
_assessment that models this phase_

## A1_FCC (Fe–Pt)

- Id: `phase:fe-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 4 calculated diagram(s): 300–2020 K, x(Pt) 0–0.98
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pt:fcc-a1)

Names (5): _corpus: _corpus:phase:fe-pt:fcc-a1  
_tdb: _tdb:FePt-01Fre-LB.tdb:A1_FCC, tdb:FePt-01Fre-LB.tdb:FCC_A1, tdb:FePt-01Fre-orig.tdb:A1_FCC, tdb:FePt-01Fre-orig.tdb:FCC_A1  


### TDB models of A1_FCC (4): PHASE and CONSTITUENT statements as written

[FePt-01Fre-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-LB.tdb): A1_FCC, type code %A, sha256 `1c359cccce909a24…`

~~~~text
43: PHASE A1_FCC %A 2 1 1 !
44: CONST A1_FCC : FE PT : VA : !
~~~~

[FePt-01Fre-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-LB.tdb): FCC_A1, type code %A, sha256 `1c359cccce909a24…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : FE PT : VA : !
~~~~

[FePt-01Fre-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-orig.tdb): A1_FCC, type code %A, sha256 `a5386a32fd8404bf…`

~~~~text
42: PHASE A1_FCC %A 2 1 1 !
43: CONST A1_FCC : FE PT : VA : !
~~~~

[FePt-01Fre-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-orig.tdb): FCC_A1, type code %A, sha256 `a5386a32fd8404bf…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : FE PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00006-8](https://doi.org/10.1016/S0364-5916%2802%2900006-8) P. Fredriksson, B. Sundman, Calphad, 25, 535-48(2001).  
_assessment that models this phase_

## HCP_A3 (Fe–Pt)

- Id: `phase:fe-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pt:hcp-a3)

Names (3): _corpus: _corpus:phase:fe-pt:hcp-a3  
_tdb: _tdb:FePt-01Fre-LB.tdb:HCP_A3, tdb:FePt-01Fre-orig.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FePt-01Fre-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-LB.tdb): HCP_A3, type code %A, sha256 `1c359cccce909a24…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : FE PT : VA : !
~~~~

[FePt-01Fre-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-orig.tdb): HCP_A3, type code %A, sha256 `a5386a32fd8404bf…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : FE PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00006-8](https://doi.org/10.1016/S0364-5916%2802%2900006-8) P. Fredriksson, B. Sundman, Calphad, 25, 535-48(2001).  
_assessment that models this phase_

## LIQUID (Fe–Pt)

- Id: `phase:fe-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1772.02–2500 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pt:liquid)

Names (3): _corpus: _corpus:phase:fe-pt:liquid  
_tdb: _tdb:FePt-01Fre-LB.tdb:LIQUID, tdb:FePt-01Fre-orig.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FePt-01Fre-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-LB.tdb): LIQUID, type code %, sha256 `1c359cccce909a24…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : FE PT : !
~~~~

[FePt-01Fre-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/FePt-01Fre-orig.tdb): LIQUID, type code %, sha256 `a5386a32fd8404bf…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : FE PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00006-8](https://doi.org/10.1016/S0364-5916%2802%2900006-8) P. Fredriksson, B. Sundman, Calphad, 25, 535-48(2001).  
_assessment that models this phase_

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
