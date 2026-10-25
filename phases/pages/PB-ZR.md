# Pb–Zr phases

> Pb–Zr system: 7 phases (tier A 4, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/PB-ZR.md

7 phases (tier A 4, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/PB-ZR.json) · [Pb–Zr system page](https://data.orchid-project.org/systems/PB-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Zr system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pb-zr-bcc-a2); _phase:pb-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1135.28–3662.85 K, x(Zr) 0.87036–1 | 10 | 1 |
| [FCC_A1](#phase-pb-zr-fcc-a1); _phase:pb-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–631 K, x(Zr) 0–0.03331 | 0 | 1 |
| [HCP_A3](#phase-pb-zr-hcp-a3); _phase:pb-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1210.28 K, x(Zr) 0.94268–1 | 5 | 1 |
| [LIQUID](#phase-pb-zr-liquid); _phase:pb-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 571–4000 K, x(Zr) 0–1 | 5 | 1 |
| [PB2ZR](#phase-pb-zr-pb2zr); _phase:pb-zr:pb2zr_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1546.68 K, x(Zr) 0.33333–0.33333 | 0 | 1 |
| [PB3ZR5_D88](#phase-pb-zr-pb3zr5-d88); _phase:pb-zr:pb3zr5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 770.7–2242.22 K, x(Zr) 0.625–0.625 | 5 | 1 |
| [PBZR4_A15](#phase-pb-zr-pbzr4-a15); _phase:pb-zr:pbzr4-a15_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1516.79 K, x(Zr) 0.8–0.8 | 7 | 1 |

## BCC_A2 (Pb–Zr)

- Id: `phase:pb-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1135.28–3662.85 K, x(Zr) 0.87036–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zr:bcc-a2)

Names (3): _corpus: _corpus:phase:pb-zr:bcc-a2  
_paper: _paper:10.1016/s0364-5916(98)00039-x:β  
_tdb: _tdb:PbZr-98Dix.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PbZr-98Dix.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZr-98Dix.tdb): BCC_A2, type code %B, sha256 `1620ca23b0d702d2…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : PB ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00039-X](https://doi.org/10.1016/S0364-5916%2898%2900039-X) P.R. Dixon, B.B. Argent, T.G. Chart, Calphad, 22, 397-416(1998).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Pb–Zr)

- Id: `phase:pb-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–631 K, x(Zr) 0–0.03331
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zr:fcc-a1)

Names (2): _corpus: _corpus:phase:pb-zr:fcc-a1  
_tdb: _tdb:PbZr-98Dix.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PbZr-98Dix.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZr-98Dix.tdb): FCC_A1, type code %A, sha256 `1620ca23b0d702d2…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : PB% ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00039-X](https://doi.org/10.1016/S0364-5916%2898%2900039-X) P.R. Dixon, B.B. Argent, T.G. Chart, Calphad, 22, 397-416(1998).  
_assessment that models this phase_

## HCP_A3 (Pb–Zr)

- Id: `phase:pb-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1210.28 K, x(Zr) 0.94268–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zr:hcp-a3)

Names (3): _corpus: _corpus:phase:pb-zr:hcp-a3  
_paper: _paper:10.1016/s0364-5916(98)00039-x:α  
_tdb: _tdb:PbZr-98Dix.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PbZr-98Dix.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZr-98Dix.tdb): HCP_A3, type code %A, sha256 `1620ca23b0d702d2…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : PB ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00039-X](https://doi.org/10.1016/S0364-5916%2898%2900039-X) P.R. Dixon, B.B. Argent, T.G. Chart, Calphad, 22, 397-416(1998).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Pb–Zr)

- Id: `phase:pb-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 571–4000 K, x(Zr) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zr:liquid)

Names (3): _corpus: _corpus:phase:pb-zr:liquid  
_paper: _paper:10.1016/s0364-5916(98)00039-x:liquid  
_tdb: _tdb:PbZr-98Dix.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PbZr-98Dix.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZr-98Dix.tdb): LIQUID, type code %, sha256 `1620ca23b0d702d2…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : PB ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00039-X](https://doi.org/10.1016/S0364-5916%2898%2900039-X) P.R. Dixon, B.B. Argent, T.G. Chart, Calphad, 22, 397-416(1998).  
_assessment that models this phase; reports values for this phase_

## PB2ZR (Pb–Zr)

- Id: `phase:pb-zr:pb2zr`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Pb2Zr) — Hallstedt 2025 mmc2 row for PB2ZR: Pb2Zr
- Stoichiometry: Pb 0.6667, Zr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1546.68 K, x(Zr) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zr:pb2zr)

Names (2): _corpus: _corpus:phase:pb-zr:pb2zr  
_tdb: _tdb:PbZr-98Dix.tdb:PB2ZR  


### TDB models of PB2ZR (1): PHASE and CONSTITUENT statements as written

[PbZr-98Dix.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZr-98Dix.tdb): PB2ZR, type code %, sha256 `1620ca23b0d702d2…`

~~~~text
46: PHASE PB2ZR % 2 2 1 !
47: CONST PB2ZR : PB : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00039-X](https://doi.org/10.1016/S0364-5916%2898%2900039-X) P.R. Dixon, B.B. Argent, T.G. Chart, Calphad, 22, 397-416(1998).  
_assessment that models this phase_

## PB3ZR5_D88 (Pb–Zr)

- Id: `phase:pb-zr:pb3zr5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.3750, Zr 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 770.7–2242.22 K, x(Zr) 0.625–0.625
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zr:pb3zr5-d88)

Names (3): _corpus: _corpus:phase:pb-zr:pb3zr5-d88  
_paper: _paper:10.1016/s0364-5916(98)00039-x:Zr5Pb3  
_tdb: _tdb:PbZr-98Dix.tdb:PB3ZR5_D88  


### TDB models of PB3ZR5_D88 (1): PHASE and CONSTITUENT statements as written

[PbZr-98Dix.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZr-98Dix.tdb): PB3ZR5_D88, type code %, sha256 `1620ca23b0d702d2…`

~~~~text
51: PHASE PB3ZR5_D88 % 2 3 5 !
52: CONST PB3ZR5_D88 : PB : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00039-X](https://doi.org/10.1016/S0364-5916%2898%2900039-X) P.R. Dixon, B.B. Argent, T.G. Chart, Calphad, 22, 397-416(1998).  
_assessment that models this phase; reports values for this phase_

## PBZR4_A15 (Pb–Zr)

- Id: `phase:pb-zr:pbzr4-a15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_A15; stoichiometry_contradicts_A15:PbZr-98Dix.tdb
- Candidate (literature_printed): Cr3Si · cP8 — printed with a label mapped to this phase
- Candidate (name_token): Cr3Si · A15 · cP8 · Pm-3n (223) — Strukturbericht/word 'A15' in the TDB name
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for PBZR4_A15: PbZr4
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — PbZr-98Dix.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Stoichiometry: Pb 0.2000, Zr 0.8000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1516.79 K, x(Zr) 0.8–0.8
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-zr:pbzr4-a15)

Names (3): _corpus: _corpus:phase:pb-zr:pbzr4-a15  
_paper: _paper:10.1016/s0364-5916(98)00039-x:Zr4Pb  
_tdb: _tdb:PbZr-98Dix.tdb:PBZR4_A15  


### TDB models of PBZR4_A15 (1): PHASE and CONSTITUENT statements as written

[PbZr-98Dix.tdb](https://orchid-project.org/data/databases/sgte-binary/PbZr-98Dix.tdb): PBZR4_A15, type code %, sha256 `1620ca23b0d702d2…`

~~~~text
56: PHASE PBZR4_A15 % 2 1 4 !
57: CONST PBZR4_A15 : PB : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00039-X](https://doi.org/10.1016/S0364-5916%2898%2900039-X) P.R. Dixon, B.B. Argent, T.G. Chart, Calphad, 22, 397-416(1998).  
_assessment that models this phase; reports values for this phase_

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
