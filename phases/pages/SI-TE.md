# Si–Te phases

> Si–Te system: 11 phases (tier A 6, liquid 1, gas 1, needs_review 3); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-TE.html · Markdown: https://data.orchid-project.org/phases/pages/SI-TE.md

11 phases (tier A 6, liquid 1, gas 1, needs_review 3); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-TE) · [full JSON](https://data.orchid-project.org/phases/systems/SI-TE.json) · [Si–Te system page](https://data.orchid-project.org/systems/SI-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–Te system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-te-a4-diamond); _phase:si-te:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Te) 0–0 | 0 | 2 |
| [HEXAGONAL_A8](#phase-si-te-a8-hexagonal); _phase:si-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 2 |
| [BCC_A2](#phase-si-te-bcc-a2); _phase:si-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-si-te-fcc-a1); _phase:si-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-si-te-gas); _phase:si-te:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1267.25–2500 K, x(Te) 0.99577–1 | 0 | 1 |
| [HCP_A3](#phase-si-te-hcp-a3); _phase:si-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-si-te-liquid); _phase:si-te:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 673.75–2500 K, x(Te) 0–1 | 0 | 2 |
| [SI2TE3_HT](#phase-si-te-si2te3-ht); _phase:si-te:si2te3-ht_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 674–1165.1 K, x(Te) 0.6–0.6 | 0 | 2 |
| [SI2TE3_LT](#phase-si-te-si2te3-lt); _phase:si-te:si2te3-lt_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–713.91 K, x(Te) 0.6–0.6 | 5 | 2 |
| [SITE2_HT](#phase-si-te-site2); _phase:si-te:site2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 663.64–707.55 K, x(Te) 0.66667–0.66667 | 0 | 1 |
| [SITE2_C6](#phase-si-te-site2-c6); _phase:si-te:site2-c6_ | CdI2 · C6 · hP3 · P-3m1 (164) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–663.64 K, x(Te) 0.66667–0.66667 | 0 | 1 |

## DIAMOND_A4 (Si–Te)

- Id: `phase:si-te:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:a4-diamond)

Names (3): _corpus: _corpus:phase:si-te:a4-diamond  
_tdb: _tdb:SiTe-20Yua.tdb:DIAMOND_A4, tdb:SiTe-99Feu-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): DIAMOND_A4, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
54: PHASE DIAMOND_A4 % 1 1 !
55: CONST DIAMOND_A4 : SI : !
~~~~

[SiTe-99Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-99Feu-LB.tdb): DIAMOND_A4, type code %, sha256 `0d62124cd250a55a…`

~~~~text
29: PHASE DIAMOND_A4 % 1 1 !
30: CONST DIAMOND_A4 : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00007-9](https://doi.org/10.1016/S0364-5916%2800%2900007-9) Y. Feutelais, A. Schlieper, S.G. Fries, Calphad, 23, 365-78(1999).  
_assessment that models this phase_

## HEXAGONAL_A8 (Si–Te)

- Id: `phase:si-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:a8-hexagonal)

Names (3): _corpus: _corpus:phase:si-te:a8-hexagonal  
_tdb: _tdb:SiTe-20Yua.tdb:HEXAGONAL_A8, tdb:SiTe-99Feu-LB.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): HEXAGONAL_A8, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
61: PHASE HEXAGONAL_A8 % 1 1 !
62: CONST HEXAGONAL_A8 : TE : !
~~~~

[SiTe-99Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-99Feu-LB.tdb): HEXAGONAL_A8, type code %, sha256 `0d62124cd250a55a…`

~~~~text
34: PHASE HEXAGONAL_A8 % 1 1 !
35: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00007-9](https://doi.org/10.1016/S0364-5916%2800%2900007-9) Y. Feutelais, A. Schlieper, S.G. Fries, Calphad, 23, 365-78(1999).  
_assessment that models this phase_

## BCC_A2 (Si–Te)

- Id: `phase:si-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:bcc-a2)

Names (2): _corpus: _corpus:phase:si-te:bcc-a2  
_tdb: _tdb:SiTe-20Yua.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): BCC_A2, type code %B, sha256 `788eb4e0fb22d784…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## FCC_A1 (Si–Te)

- Id: `phase:si-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:fcc-a1)

Names (2): _corpus: _corpus:phase:si-te:fcc-a1  
_tdb: _tdb:SiTe-20Yua.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): FCC_A1, type code %A, sha256 `788eb4e0fb22d784…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## GAS (Si–Te)

- Id: `phase:si-te:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1267.25–2500 K, x(Te) 0.99577–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:gas)

Names (2): _corpus: _corpus:phase:si-te:gas  
_tdb: _tdb:SiTe-20Yua.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): GAS, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
84: PHASE GAS:G % 1 1 !
85: CONST GAS:G : SI SI2 SI3 TE TE2 TE3 TE4 TE5 TE6 TE7 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## HCP_A3 (Si–Te)

- Id: `phase:si-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:hcp-a3)

Names (2): _corpus: _corpus:phase:si-te:hcp-a3  
_tdb: _tdb:SiTe-20Yua.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): HCP_A3, type code %A, sha256 `788eb4e0fb22d784…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## LIQUID (Si–Te)

- Id: `phase:si-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 673.75–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:liquid)

Names (3): _corpus: _corpus:phase:si-te:liquid  
_tdb: _tdb:SiTe-20Yua.tdb:LIQUID, tdb:SiTe-99Feu-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): LIQUID, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : SI SI2TE3 TE : !
~~~~

[SiTe-99Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-99Feu-LB.tdb): LIQUID, type code %, sha256 `0d62124cd250a55a…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SI SI2TE3 TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00007-9](https://doi.org/10.1016/S0364-5916%2800%2900007-9) Y. Feutelais, A. Schlieper, S.G. Fries, Calphad, 23, 365-78(1999).  
_assessment that models this phase_

## SI2TE3_HT (Si–Te)

- Id: `phase:si-te:si2te3-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (sgte_mmc2): (Si2Te3) — Hallstedt 2025 mmc2 row for SI2TE3_HT: Si2Te3-beta
- Stoichiometry: Si 0.4000, Te 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 674–1165.1 K, x(Te) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:si2te3-ht)

Names (3): _corpus: _corpus:phase:si-te:si2te3-ht  
_tdb: _tdb:SiTe-20Yua.tdb:SI2TE3_HT, tdb:SiTe-99Feu-LB.tdb:SI2TE3_HT  


### TDB models of SI2TE3_HT (2): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): SI2TE3_HT, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
71: PHASE SI2TE3_HT % 2 2 3 !
72: CONST SI2TE3_HT : SI : TE : !
~~~~

[SiTe-99Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-99Feu-LB.tdb): SI2TE3_HT, type code %, sha256 `0d62124cd250a55a…`

~~~~text
44: PHASE SI2TE3_HT % 2 2 3 !
45: CONST SI2TE3_HT : SI : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00007-9](https://doi.org/10.1016/S0364-5916%2800%2900007-9) Y. Feutelais, A. Schlieper, S.G. Fries, Calphad, 23, 365-78(1999).  
_assessment that models this phase_

## SI2TE3_LT (Si–Te)

- Id: `phase:si-te:si2te3-lt`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (sgte_mmc2): Si2Te3-alpha · hP40 · P-31c (163) — Hallstedt 2025 mmc2 row for SI2TE3_LT: Si2Te3-alpha
- Candidate (tdb_comment): Si2Te3 · hP40 · P-31c, 163 — SiTe-20Yua.tdb: 'Prototype Si2Te3 (hP40, P-31c, 163)'
- Candidate (tdb_comment): alpha-Si2Te3 · hP40 · P-31c — SiTe-99Feu-LB.tdb: 'Prototype alpha-Si2Te3 (hP40, P-31c)'
- Stoichiometry: Si 0.4000, Te 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–713.91 K, x(Te) 0.6–0.6
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:si2te3-lt)

Names (4): _corpus: _corpus:phase:si-te:si2te3-lt  
_paper: _paper:10.1016/s0364-5916(00)00007-9:α-Si2Te3  
_tdb: _tdb:SiTe-20Yua.tdb:SI2TE3_LT, tdb:SiTe-99Feu-LB.tdb:SI2TE3_LT  


### TDB models of SI2TE3_LT (2): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): SI2TE3_LT, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
66: PHASE SI2TE3_LT % 2 2 3 !
67: CONST SI2TE3_LT : SI : TE : !
~~~~

[SiTe-99Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-99Feu-LB.tdb): SI2TE3_LT, type code %, sha256 `0d62124cd250a55a…`

~~~~text
39: PHASE SI2TE3_LT % 2 2 3 !
40: CONST SI2TE3_LT : SI : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(00)00007-9](https://doi.org/10.1016/S0364-5916%2800%2900007-9) Y. Feutelais, A. Schlieper, S.G. Fries, Calphad, 23, 365-78(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## SITE2_HT (Si–Te)

- Id: `phase:si-te:site2`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P-3m1 (164) — on-hull MP SiTe2 at x(TE)=0.6667
- Candidate (dft_oqmd): I-42d (122) — on-hull OQMD Si1 Te2 at x(TE)=0.6667
- Candidate (sgte_mmc2): (SiTe2-beta) — Hallstedt 2025 mmc2 row for SITE2_HT: SiTe2-beta
- Stoichiometry: Si 0.3333, Te 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 663.64–707.55 K, x(Te) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:site2)

Names (2): _corpus: _corpus:phase:si-te:site2  
_tdb: _tdb:SiTe-20Yua.tdb:SITE2_HT  


### TDB models of SITE2_HT (1): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): SITE2_HT, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
81: PHASE SITE2_HT % 2 1 2 !
82: CONST SITE2_HT : SI : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## SITE2_C6 (Si–Te)

- Id: `phase:si-te:site2-c6`; status `assigned`
- Structure: CdI2 · C6 · hP3 · P-3m1 (164); type `st:c6-cdi2-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.3333, Te 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–663.64 K, x(Te) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-te:site2-c6)

Names (2): _corpus: _corpus:phase:si-te:site2-c6  
_tdb: _tdb:SiTe-20Yua.tdb:SITE2_C6  


### TDB models of SITE2_C6 (1): PHASE and CONSTITUENT statements as written

[SiTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb): SITE2_C6, type code %, sha256 `788eb4e0fb22d784…`

~~~~text
76: PHASE SITE2_C6 % 2 1 2 !
77: CONST SITE2_C6 : SI : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
