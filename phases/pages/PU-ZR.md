# Pu–Zr phases

> Pu–Zr system: 9 phases (tier A 4, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PU-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/PU-ZR.md

9 phases (tier A 4, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PU-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/PU-ZR.json) · [Pu–Zr system page](https://data.orchid-project.org/systems/PU-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/PU-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pu–Zr system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-pu-zr-a6-tetragonal); _phase:pu-zr:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 740–750 K, x(Zr) 0–0 | 0 | 2 |
| [BCC_A2](#phase-pu-zr-bcc-a2); _phase:pu-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 754.9–3999.25 K, x(Zr) 0–1 | 2 | 2 |
| [FCC_A1](#phase-pu-zr-fcc-a1); _phase:pu-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 506.77–1179.2 K, x(Zr) 0–0.65231 | 0 | 2 |
| [HCP_A3](#phase-pu-zr-hcp-a3); _phase:pu-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2124 K, x(Zr) 0.85656–1 | 3 | 2 |
| [LIQUID](#phase-pu-zr-liquid); _phase:pu-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 910–4000 K, x(Zr) 0–1 | 0 | 2 |
| [ALPHA_PU](#phase-pu-zr-pu-alpha); _phase:pu-zr:pu-alpha_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–397.62 K, x(Zr) 0–0.00094 | 0 | 2 |
| [BETA_PU](#phase-pu-zr-pu-beta); _phase:pu-zr:pu-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 397.42–514.61 K, x(Zr) 0–0.01408 | 8 | 2 |
| [GAMMA_PU](#phase-pu-zr-pu-gamma); _phase:pu-zr:pu-gamma_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 484.91–599.35 K, x(Zr) 0–0.01746 | 8 | 2 |
| [PU4ZR](#phase-pu-zr-pu4zr); _phase:pu-zr:pu4zr_ | Pu4Zr · tP80 · P4/ncc (130) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–650.42 K, x(Zr) 0.12719–0.2 | 0 | 2 |

## TETRAGONAL_A6 (Pu–Zr)

- Id: `phase:pu-zr:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 740–750 K, x(Zr) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:a6-tetragonal)

Names (3): _corpus: _corpus:phase:pu-zr:a6-tetragonal  
_tdb: _tdb:PuZr-10Kur.tdb:TETRAGONAL_A6, tdb:PuZr-99Kur.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): TETRAGONAL_A6, type code %, sha256 `b56cc08b0fcadc13…`

~~~~text
43: PHASE TETRAGONAL_A6 % 1 1 !
44: CONST TETRAGONAL_A6 : PU% ZR : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): TETRAGONAL_A6, type code %, sha256 `c511e212529d822f…`

~~~~text
44: PHASE TETRAGONAL_A6 % 1 1 !
45: CONST TETRAGONAL_A6 : PU% ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## BCC_A2 (Pu–Zr)

- Id: `phase:pu-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 754.9–3999.25 K, x(Zr) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:bcc-a2)

Names (4): _corpus: _corpus:phase:pu-zr:bcc-a2  
_paper: _paper:10.1016/s0364-5916(00)00004-3:δ-Pu  
_tdb: _tdb:PuZr-10Kur.tdb:BCC_A2, tdb:PuZr-99Kur.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): BCC_A2, type code %B, sha256 `b56cc08b0fcadc13…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : PU% ZR% : VA : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): BCC_A2, type code %B, sha256 `c511e212529d822f…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : PU% ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Pu–Zr)

- Id: `phase:pu-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 506.77–1179.2 K, x(Zr) 0–0.65231
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:pu-zr:fcc-a1  
_tdb: _tdb:PuZr-10Kur.tdb:FCC_A1, tdb:PuZr-99Kur.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): FCC_A1, type code %A, sha256 `b56cc08b0fcadc13…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : PU% ZR : VA : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): FCC_A1, type code %A, sha256 `c511e212529d822f…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : PU% ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## HCP_A3 (Pu–Zr)

- Id: `phase:pu-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2124 K, x(Zr) 0.85656–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:hcp-a3)

Names (4): _corpus: _corpus:phase:pu-zr:hcp-a3  
_paper: _paper:10.1016/s0364-5916(00)00004-3:α-Zr  
_tdb: _tdb:PuZr-10Kur.tdb:HCP_A3, tdb:PuZr-99Kur.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): HCP_A3, type code %A, sha256 `b56cc08b0fcadc13…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : PU ZR% : VA : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): HCP_A3, type code %A, sha256 `c511e212529d822f…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : PU ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Pu–Zr)

- Id: `phase:pu-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 910–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:liquid)

Names (3): _corpus: _corpus:phase:pu-zr:liquid  
_tdb: _tdb:PuZr-10Kur.tdb:LIQUID, tdb:PuZr-99Kur.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): LIQUID, type code %, sha256 `b56cc08b0fcadc13…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : PU ZR : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): LIQUID, type code %, sha256 `c511e212529d822f…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : PU ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## ALPHA_PU (Pu–Zr)

- Id: `phase:pu-zr:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuZr-10Kur.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuZr-99Kur.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–397.62 K, x(Zr) 0–0.00094
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:pu-alpha)

Names (3): _corpus: _corpus:phase:pu-zr:pu-alpha  
_tdb: _tdb:PuZr-10Kur.tdb:ALPHA_PU, tdb:PuZr-99Kur.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): ALPHA_PU, type code %, sha256 `b56cc08b0fcadc13…`

~~~~text
48: PHASE ALPHA_PU % 1 1 !
49: CONST ALPHA_PU : PU% ZR : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): ALPHA_PU, type code %, sha256 `c511e212529d822f…`

~~~~text
49: PHASE ALPHA_PU % 1 1 !
50: CONST ALPHA_PU : PU% ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## BETA_PU (Pu–Zr)

- Id: `phase:pu-zr:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): beta-Pu · mC34 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuZr-10Kur.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuZr-99Kur.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stability: stable in 2 of 2 calculated diagram(s): 397.42–514.61 K, x(Zr) 0–0.01408
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:pu-beta)

Names (4): _corpus: _corpus:phase:pu-zr:pu-beta  
_paper: _paper:10.1016/s0364-5916(00)00004-3:(ε-Pu,β-Zr)  
_tdb: _tdb:PuZr-10Kur.tdb:BETA_PU, tdb:PuZr-99Kur.tdb:BETA_PU  


### TDB models of BETA_PU (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): BETA_PU, type code %, sha256 `b56cc08b0fcadc13…`

~~~~text
53: PHASE BETA_PU % 1 1 !
54: CONST BETA_PU : PU% ZR : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): BETA_PU, type code %, sha256 `c511e212529d822f…`

~~~~text
54: PHASE BETA_PU % 1 1 !
55: CONST BETA_PU : PU% ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase; reports values for this phase_

## GAMMA_PU (Pu–Zr)

- Id: `phase:pu-zr:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): gamma-Pu · oF8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuZr-10Kur.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuZr-99Kur.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stability: stable in 2 of 2 calculated diagram(s): 484.91–599.35 K, x(Zr) 0–0.01746
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:pu-gamma)

Names (4): _corpus: _corpus:phase:pu-zr:pu-gamma  
_paper: _paper:10.1016/s0364-5916(00)00004-3:(δ-Pu,γ-Zr)  
_tdb: _tdb:PuZr-10Kur.tdb:GAMMA_PU, tdb:PuZr-99Kur.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): GAMMA_PU, type code %, sha256 `b56cc08b0fcadc13…`

~~~~text
58: PHASE GAMMA_PU % 1 1 !
59: CONST GAMMA_PU : PU% ZR : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): GAMMA_PU, type code %, sha256 `c511e212529d822f…`

~~~~text
59: PHASE GAMMA_PU % 1 1 !
60: CONST GAMMA_PU : PU% ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase; reports values for this phase_

## PU4ZR (Pu–Zr)

- Id: `phase:pu-zr:pu4zr`; status `assigned`
- Structure: Pu4Zr · tP80 · P4/ncc (130); type `st:pu4zr-tp80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–650.42 K, x(Zr) 0.12719–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-zr:pu4zr)

Names (3): _corpus: _corpus:phase:pu-zr:pu4zr  
_tdb: _tdb:PuZr-10Kur.tdb:PU4ZR, tdb:PuZr-99Kur.tdb:PU4ZR  


### TDB models of PU4ZR (2): PHASE and CONSTITUENT statements as written

[PuZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-10Kur.tdb): PU4ZR, type code %, sha256 `b56cc08b0fcadc13…`

~~~~text
63: PHASE PU4ZR % 2 4 1 !
64: CONST PU4ZR : PU : ZR : !
~~~~

[PuZr-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuZr-99Kur.tdb): PU4ZR, type code %, sha256 `c511e212529d822f…`

~~~~text
64: PHASE PU4ZR % 2 6 1 !
65: CONST PU4ZR : PU ZR : PU ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
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
