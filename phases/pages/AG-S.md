# Ag–S phases

> Ag–S system: 9 phases (tier A 4, liquid 1, needs_review 4); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-S.html · Markdown: https://data.orchid-project.org/phases/pages/AG-S.md

9 phases (tier A 4, liquid 1, needs_review 4); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-S) · [full JSON](https://data.orchid-project.org/phases/systems/AG-S.json) · [Ag–S system page](https://data.orchid-project.org/systems/AG-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–S system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-ag-s-a16-orthorhombic); _phase:ag-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–385.34 K, x(S) 1–1 | 0 | 1 |
| [AG2S_ALPHA](#phase-ag-s-ag2s-alpha); _phase:ag-s:ag2s-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–450.75 K, x(S) 0.33333–0.33333 | 0 | 1 |
| [AG2S_BETA](#phase-ag-s-ag2s-beta); _phase:ag-s:ag2s-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 441.92–897.41 K, x(S) 0.33333–0.33551 | 0 | 1 |
| [AG2S_GAMMA](#phase-ag-s-ag2s-gamma); _phase:ag-s:ag2s-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 851.43–1099.34 K, x(S) 0.33333–0.33333 | 0 | 1 |
| [BCC_A2](#phase-ag-s-bcc-a2); _phase:ag-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ag-s-fcc-a1); _phase:ag-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1234.93 K, x(S) 0–0 | 0 | 1 |
| [HCP_A3](#phase-ag-s-hcp-a3); _phase:ag-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-s-liquid); _phase:ag-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.29–2500 K, x(S) 0–1 | 0 | 1 |
| [MONOCLINIC_S](#phase-ag-s-s-monoclinic); _phase:ag-s:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## ORTHORHOMBIC_A16 (Ag–S)

- Id: `phase:ag-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–385.34 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:ag-s:a16-orthorhombic  
_tdb: _tdb:AgS-18Shi.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): ORTHORHOMBIC_A16, type code %, sha256 `88ca76a77dda3d77…`

~~~~text
49: PHASE ORTHORHOMBIC_A16 % 1 1 !
50: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## AG2S_ALPHA (Ag–S)

- Id: `phase:ag-s:ag2s-alpha`; status `needs_review`
- No structure assigned. Why: mp_oqmd_space_groups_differ; no_structure_token
- Candidate (dft_mp): P2_1/m (11) — on-hull MP Ag2S at x(S)=0.3333
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Ag2 S1 at x(S)=0.3333
- Candidate (sgte_mmc2): Ag2S-alpha · mP12 · P2_1/c (14) — Hallstedt 2025 mmc2 row for AG2S_ALPHA: Ag2S-alpha
- Candidate (tdb_comment): Ag2S-alpha · mP12 · P2_1/c — AgS-18Shi.tdb: 'Prototype Ag2S-alpha (mP12, P2_1/c)'
- Stoichiometry: Ag 0.6667, S 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–450.75 K, x(S) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:ag2s-alpha)

Names (2): _corpus: _corpus:phase:ag-s:ag2s-alpha  
_tdb: _tdb:AgS-18Shi.tdb:AG2S_ALPHA  


### TDB models of AG2S_ALPHA (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): AG2S_ALPHA, type code %, sha256 `88ca76a77dda3d77…`

~~~~text
59: PHASE AG2S_ALPHA % 2 2 1 !
60: CONST AG2S_ALPHA : AG : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## AG2S_BETA (Ag–S)

- Id: `phase:ag-s:ag2s-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): P2_1/m (11) — on-hull MP Ag2S at x(S)=0.3333
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Ag2 S1 at x(S)=0.3333
- Candidate (sgte_mmc2): Ag2S-beta · cI20 · Im-3m (229) — Hallstedt 2025 mmc2 row for AG2S_BETA: Ag2S-beta
- Candidate (tdb_comment): Ag2S-beta · cI20 · Im-3m — AgS-18Shi.tdb: 'Prototype Ag2S-beta (cI20, Im-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 441.92–897.41 K, x(S) 0.33333–0.33551
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:ag2s-beta)

Names (2): _corpus: _corpus:phase:ag-s:ag2s-beta  
_tdb: _tdb:AgS-18Shi.tdb:AG2S_BETA  


### TDB models of AG2S_BETA (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): AG2S_BETA, type code %, sha256 `88ca76a77dda3d77…`

~~~~text
64: PHASE AG2S_BETA % 2 2 1 !
65: CONST AG2S_BETA : AG% S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## AG2S_GAMMA (Ag–S)

- Id: `phase:ag-s:ag2s-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): Cu2Se-beta · cF44 · Fm-3m (225) — Hallstedt 2025 mmc2 row for AG2S_GAMMA: Ag2S-gamma
- Candidate (tdb_comment): Cu2Se-beta · cF44 · Fm-3m — AgS-18Shi.tdb: 'Prototype Cu2Se-beta (cF44, Fm-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 851.43–1099.34 K, x(S) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:ag2s-gamma)

Names (2): _corpus: _corpus:phase:ag-s:ag2s-gamma  
_tdb: _tdb:AgS-18Shi.tdb:AG2S_GAMMA  


### TDB models of AG2S_GAMMA (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): AG2S_GAMMA, type code %, sha256 `88ca76a77dda3d77…`

~~~~text
69: PHASE AG2S_GAMMA % 2 2 1 !
70: CONST AG2S_GAMMA : AG% S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## BCC_A2 (Ag–S)

- Id: `phase:ag-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-s:bcc-a2  
_tdb: _tdb:AgS-18Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): BCC_A2, type code %B, sha256 `88ca76a77dda3d77…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## FCC_A1 (Ag–S)

- Id: `phase:ag-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1234.93 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:fcc-a1)

Names (2): _corpus: _corpus:phase:ag-s:fcc-a1  
_tdb: _tdb:AgS-18Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): FCC_A1, type code %A, sha256 `88ca76a77dda3d77…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## HCP_A3 (Ag–S)

- Id: `phase:ag-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-s:hcp-a3  
_tdb: _tdb:AgS-18Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): HCP_A3, type code %A, sha256 `88ca76a77dda3d77…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : AG : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## LIQUID (Ag–S)

- Id: `phase:ag-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.29–2500 K, x(S) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:liquid)

Names (2): _corpus: _corpus:phase:ag-s:liquid  
_tdb: _tdb:AgS-18Shi.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): LIQUID, type code %, sha256 `88ca76a77dda3d77…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AG AG2S S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
_assessment that models this phase_

## MONOCLINIC_S (Ag–S)

- Id: `phase:ag-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — AgS-18Shi.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-s:s-monoclinic)

Names (2): _corpus: _corpus:phase:ag-s:s-monoclinic  
_tdb: _tdb:AgS-18Shi.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[AgS-18Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgS-18Shi.tdb): MONOCLINIC_S, type code %, sha256 `88ca76a77dda3d77…`

~~~~text
54: PHASE MONOCLINIC_S % 1 1 !
55: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018).  
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
