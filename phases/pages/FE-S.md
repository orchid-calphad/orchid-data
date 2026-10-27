# Fe–S phases

> Fe–S system: 9 phases (tier A 3, liquid 2, needs_review 4); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-S.html · Markdown: https://data.orchid-project.org/phases/pages/FE-S.md

9 phases (tier A 3, liquid 2, needs_review 4); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-S) · [full JSON](https://data.orchid-project.org/phases/systems/FE-S.json) · [Fe–S system page](https://data.orchid-project.org/systems/FE-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–S system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-s-bcc-a2); _phase:fe-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1837.15 K, x(S) 0–0.00207 | 0 | 4 |
| [FCC_A1](#phase-fe-s-fcc-a1); _phase:fe-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1167.53–1674.43 K, x(S) 0–0.00108 | 0 | 4 |
| [FES](#phase-fe-s-fes); _phase:fe-s:fes_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1461.08 K, x(S) 0.5–0.55135 | 0 | 4 |
| [FES2](#phase-fe-s-fes2); _phase:fe-s:fes2_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1016.08 K, x(S) 0.66667–0.66667 | 0 | 4 |
| [HCP_A3](#phase-fe-s-hcp-a3); _phase:fe-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [ION](#phase-fe-s-ion); _phase:fe-s:ion_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 388.35–2500 K, x(S) 0–1 | 0 | 4 |
| [LIQUID](#phase-fe-s-liquid); _phase:fe-s:liquid_ | liquid | liquid | stable in 2 of 4 calculated diagram(s): 406.89–2500 K, x(S) 0–1 | 0 | 4 |
| [MONOCLINIC_S](#phase-fe-s-s-monoclinic); _phase:fe-s:s-monoclinic_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 368.3–406.89 K, x(S) 1–1 | 0 | 4 |
| [ORTHORHOMBIC_S](#phase-fe-s-s-orthorhombic); _phase:fe-s:s-orthorhombic_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–368.33 K, x(S) 1–1 | 0 | 4 |

## BCC_A2 (Fe–S)

- Id: `phase:fe-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1837.15 K, x(S) 0–0.00207
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:bcc-a2)

Names (5): _corpus: _corpus:phase:fe-s:bcc-a2  
_tdb: _tdb:FeS-07Lee.tdb:BCC_A2, tdb:FeS-81Fer.tdb:BCC_A2, tdb:FeS-92Sun-LB.tdb:BCC_A2, tdb:FeS-92Sun-newS.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): BCC_A2, type code %B, sha256 `32e151f596ad0bb2…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : FE% S : VA : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): BCC_A2, type code %B, sha256 `d7057d101d1e0124…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : FE% S : VA : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): BCC_A2, type code %B, sha256 `ec87bc1d4573e3cc…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : FE% S : VA : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): BCC_A2, type code %B, sha256 `716d81dd825b248d…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : FE% S : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## FCC_A1 (Fe–S)

- Id: `phase:fe-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1167.53–1674.43 K, x(S) 0–0.00108
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:fcc-a1)

Names (5): _corpus: _corpus:phase:fe-s:fcc-a1  
_tdb: _tdb:FeS-07Lee.tdb:FCC_A1, tdb:FeS-81Fer.tdb:FCC_A1, tdb:FeS-92Sun-LB.tdb:FCC_A1, tdb:FeS-92Sun-newS.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): FCC_A1, type code %A, sha256 `32e151f596ad0bb2…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : FE% S : VA : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): FCC_A1, type code %A, sha256 `d7057d101d1e0124…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : FE% S : VA : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): FCC_A1, type code %A, sha256 `ec87bc1d4573e3cc…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : FE% S : VA : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): FCC_A1, type code %A, sha256 `716d81dd825b248d…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : FE% S : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## FES (Fe–S)

- Id: `phase:fe-s:fes`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P4/nmm (129) — on-hull MP FeS at x(S)=0.5000
- Candidate (dft_oqmd): Cmca (64) — on-hull OQMD Fe1 S1 at x(S)=0.5000
- Candidate (sgte_mmc2): alpha-FeS · hP24 · P-62c (190) — Hallstedt 2025 mmc2 row for FES: FeS (alpha)
- Candidate (sgte_mmc2): NiAs · B8_1 · hP4 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for FES: FeS (gamma, pyrrhotite)
- Candidate (sgte_mmc2): NbS · hP16 · P6_3mc (186) — Hallstedt 2025 mmc2 row for FES: FeS (beta)
- Candidate (tdb_comment): FeS · hP24 · P-62c — FeS-07Lee.tdb: 'Prototype FeS (hP24, P-62c), alpha'
- Candidate (tdb_comment): NbS · hP16 · P6_3mc — FeS-07Lee.tdb: 'Prototype NbS (hP16, P6_3mc), beta'
- Candidate (tdb_comment): NiAs · hP4 · P6_3/mmc — FeS-07Lee.tdb: 'Prototype NiAs (hP4, P6_3/mmc), B8_1, gamma (pyrrhotite)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–1461.08 K, x(S) 0.5–0.55135
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:fes)

Names (5): _corpus: _corpus:phase:fe-s:fes  
_tdb: _tdb:FeS-07Lee.tdb:FES, tdb:FeS-81Fer.tdb:FES, tdb:FeS-92Sun-LB.tdb:FES, tdb:FeS-92Sun-newS.tdb:FES  


### TDB models of FES (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): FES, type code %, sha256 `32e151f596ad0bb2…`

~~~~text
71: PHASE FES % 2 1 1 !
72: CONST FES : FE VA : S : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): FES, type code %, sha256 `d7057d101d1e0124…`

~~~~text
72: PHASE FES % 2 1 1 !
73: CONST FES : FE VA : S : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): FES, type code %, sha256 `ec87bc1d4573e3cc…`

~~~~text
64: PHASE FES % 2 1 1 !
65: CONST FES : FE VA : S : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): FES, type code %, sha256 `716d81dd825b248d…`

~~~~text
68: PHASE FES % 2 1 1 !
69: CONST FES : FE VA : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## FES2 (Fe–S)

- Id: `phase:fe-s:fes2`; status `needs_review`
- No structure assigned. Why: dft_space_group_58_matches_3_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Pnnm (58) — on-hull MP FeS2 at x(S)=0.6667
- Candidate (dft_oqmd): Pnnm (58) — on-hull OQMD Fe1 S2 at x(S)=0.6667
- Candidate (dft_space_group_and_stoichiometry): alpha-FeS2 · C18 · oP6 · Pnnm (58) — space group 58 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): CaCl2 · (C35) · oP6 · Pnnm (58) — space group 58 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): FeAs2 · oP6 · Pnnm (58) — space group 58 and stoichiometry match
- Candidate (sgte_mmc2): alpha-FeS2 · C18 · oP6 · Pnnm (58) — Hallstedt 2025 mmc2 row for FES2: FeS2 (alpha, marcasite)
- Candidate (sgte_mmc2): beta-FeS2 · C2 · cP12 · Pa-3 (205) — Hallstedt 2025 mmc2 row for FES2: FeS2 (beta, pyrite)
- Candidate (tdb_comment): alpha-FeS2 · oP6 · Pnnm — FeS-07Lee.tdb: 'Prototype alpha-FeS2 (oP6, Pnnm), C18, alpha (marcasite)'
- Stoichiometry: Fe 0.3333, S 0.6667
- Stability: stable in 4 of 4 calculated diagram(s): 300–1016.08 K, x(S) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:fes2)

Names (5): _corpus: _corpus:phase:fe-s:fes2  
_tdb: _tdb:FeS-07Lee.tdb:FES2, tdb:FeS-81Fer.tdb:FES2, tdb:FeS-92Sun-LB.tdb:FES2, tdb:FeS-92Sun-newS.tdb:FES2  


### TDB models of FES2 (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): FES2, type code %, sha256 `32e151f596ad0bb2…`

~~~~text
77: PHASE FES2 % 2 1 2 !
78: CONST FES2 : FE : S : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): FES2, type code %, sha256 `d7057d101d1e0124…`

~~~~text
78: PHASE FES2 % 2 1 2 !
79: CONST FES2 : FE : S : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): FES2, type code %, sha256 `ec87bc1d4573e3cc…`

~~~~text
70: PHASE FES2 % 2 1 2 !
71: CONST FES2 : FE : S : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): FES2, type code %, sha256 `716d81dd825b248d…`

~~~~text
74: PHASE FES2 % 2 1 2 !
75: CONST FES2 : FE : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## HCP_A3 (Fe–S)

- Id: `phase:fe-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:hcp-a3)

Names (5): _corpus: _corpus:phase:fe-s:hcp-a3  
_tdb: _tdb:FeS-07Lee.tdb:HCP_A3, tdb:FeS-81Fer.tdb:HCP_A3, tdb:FeS-92Sun-LB.tdb:HCP_A3, tdb:FeS-92Sun-newS.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): HCP_A3, type code %A, sha256 `32e151f596ad0bb2…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : FE : VA : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): HCP_A3, type code %A, sha256 `d7057d101d1e0124…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : FE : VA : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): HCP_A3, type code %A, sha256 `ec87bc1d4573e3cc…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : FE S : VA : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): HCP_A3, type code %A, sha256 `716d81dd825b248d…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : FE S : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## ION (Fe–S)

- Id: `phase:fe-s:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 388.35–2500 K, x(S) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:ion)

Names (5): _corpus: _corpus:phase:fe-s:ion  
_tdb: _tdb:FeS-07Lee.tdb:ION, tdb:FeS-81Fer.tdb:ION, tdb:FeS-92Sun-LB.tdb:ION, tdb:FeS-92Sun-newS.tdb:ION  


### TDB models of ION (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): ION, type code %, sha256 `32e151f596ad0bb2…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : FE+2 : S-2 VA S : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): ION, type code %, sha256 `d7057d101d1e0124…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : FE+2 : S-2 VA S : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): ION, type code %, sha256 `ec87bc1d4573e3cc…`

~~~~text
29: PHASE ION:Y % 2 1 1 !
30: CONST ION:Y : FE+2 : S-2 VA S : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): ION, type code %, sha256 `716d81dd825b248d…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : FE+2 : S-2 VA S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## LIQUID (Fe–S)

- Id: `phase:fe-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 4 calculated diagram(s): 406.89–2500 K, x(S) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:liquid)

Names (5): _corpus: _corpus:phase:fe-s:liquid  
_tdb: _tdb:FeS-07Lee.tdb:LIQUID, tdb:FeS-81Fer.tdb:LIQUID, tdb:FeS-92Sun-LB.tdb:LIQUID, tdb:FeS-92Sun-newS.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): LIQUID, type code %, sha256 `32e151f596ad0bb2…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : FE FES S : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): LIQUID, type code %, sha256 `d7057d101d1e0124…`

~~~~text
40: PHASE LIQUID:L % 2 1 1 !
41: CONST LIQUID:L : FE VA : VA S : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): LIQUID, type code %, sha256 `ec87bc1d4573e3cc…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : FE S : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): LIQUID, type code %, sha256 `716d81dd825b248d…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : FE S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## MONOCLINIC_S (Fe–S)

- Id: `phase:fe-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — FeS-07Lee.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — FeS-81Fer.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — FeS-92Sun-LB.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — FeS-92Sun-newS.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 368.3–406.89 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:s-monoclinic)

Names (5): _corpus: _corpus:phase:fe-s:s-monoclinic  
_tdb: _tdb:FeS-07Lee.tdb:MONOCLINIC_S, tdb:FeS-81Fer.tdb:MONOCLINIC_S, tdb:FeS-92Sun-LB.tdb:MONOCLINIC_S, tdb:FeS-92Sun-newS.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): MONOCLINIC_S, type code %, sha256 `32e151f596ad0bb2…`

~~~~text
64: PHASE MONOCLINIC_S % 1 1 !
65: CONST MONOCLINIC_S : S : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): MONOCLINIC_S, type code %, sha256 `d7057d101d1e0124…`

~~~~text
65: PHASE MONOCLINIC_S % 1 1 !
66: CONST MONOCLINIC_S : S : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): MONOCLINIC_S, type code %, sha256 `ec87bc1d4573e3cc…`

~~~~text
57: PHASE MONOCLINIC_S % 1 1 !
58: CONST MONOCLINIC_S : S : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): MONOCLINIC_S, type code %, sha256 `716d81dd825b248d…`

~~~~text
61: PHASE MONOCLINIC_S % 1 1 !
62: CONST MONOCLINIC_S : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
_assessment that models this phase_

## ORTHORHOMBIC_S (Fe–S)

- Id: `phase:fe-s:s-orthorhombic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:ORTHORHOMBIC; no_structure_token
- Candidate (sgte_mmc2): alpha-S · A16 · oF128 · Fddd (70) — Hallstedt 2025 mmc2 row for ORTHORHOMBIC_S: alpha-S
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — FeS-07Lee.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — FeS-81Fer.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — FeS-92Sun-LB.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — FeS-92Sun-newS.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Stoichiometry: S 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–368.33 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-s:s-orthorhombic)

Names (5): _corpus: _corpus:phase:fe-s:s-orthorhombic  
_tdb: _tdb:FeS-07Lee.tdb:ORTHORHOMBIC_S, tdb:FeS-81Fer.tdb:ORTHORHOMBIC_S, tdb:FeS-92Sun-LB.tdb:ORTHORHOMBIC_S, tdb:FeS-92Sun-newS.tdb:ORTHORHOMBIC_S  


### TDB models of ORTHORHOMBIC_S (4): PHASE and CONSTITUENT statements as written

[FeS-07Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-07Lee.tdb): ORTHORHOMBIC_S, type code %, sha256 `32e151f596ad0bb2…`

~~~~text
59: PHASE ORTHORHOMBIC_S % 1 1 !
60: CONST ORTHORHOMBIC_S : S : !
~~~~

[FeS-81Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-81Fer.tdb): ORTHORHOMBIC_S, type code %, sha256 `d7057d101d1e0124…`

~~~~text
60: PHASE ORTHORHOMBIC_S % 1 1 !
61: CONST ORTHORHOMBIC_S : S : !
~~~~

[FeS-92Sun-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-LB.tdb): ORTHORHOMBIC_S, type code %, sha256 `ec87bc1d4573e3cc…`

~~~~text
52: PHASE ORTHORHOMBIC_S % 1 1 !
53: CONST ORTHORHOMBIC_S : S : !
~~~~

[FeS-92Sun-newS.tdb](https://orchid-project.org/data/databases/sgte-binary/FeS-92Sun-newS.tdb): ORTHORHOMBIC_S, type code %, sha256 `716d81dd825b248d…`

~~~~text
56: PHASE ORTHORHOMBIC_S % 1 1 !
57: CONST ORTHORHOMBIC_S : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02654144](https://doi.org/10.1007/BF02654144) A. Fernandez Guillermet, M. Hillert, B. Jansson, B. Sundman, Metall. Trans. B, 12B, 745-54(1981).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.47.163](https://doi.org/10.2355/isijinternational.47.163) Byeong-Joo Lee, Bo Sundman, Sung Il Kim, Kwang-Geun Chin, Thermodynamic Calculations on the Stability of Cu2S in Low Carbon Steels, ISIJ Int. 47, 163-171 (2007).  
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
