# N–Si phases

> N–Si system: 8 phases (tier A 1, tier C 2, liquid 2, gas 2, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-SI.html · Markdown: https://data.orchid-project.org/phases/pages/N-SI.md

8 phases (tier A 1, tier C 2, liquid 2, gas 2, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-SI) · [full JSON](https://data.orchid-project.org/phases/systems/N-SI.json) · [N–Si system page](https://data.orchid-project.org/systems/N-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–Si system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-n-si-a4-diamond); _phase:n-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1687 K, x(N) 0–0 | 3 | 3 |
| [GAS](#phase-n-si-gas); _phase:n-si:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300.67–2500 K, x(N) 0.99643–1 | 4 | 3 |
| [ION](#phase-n-si-ion); _phase:n-si:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1687–1974.95 K, x(N) 0–0.46 | 0 | 1 |
| [LIQUID](#phase-n-si-liquid); _phase:n-si:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1686.94–2500 K, x(N) 0–0.00388 | 8 | 3 |
| [N2GAS](#phase-n-si-n2gas); _phase:n-si:n2gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300–1725 K, x(N) 1–1 | 0 | 3 |
| [SI3N4](#phase-n-si-si3n4); _phase:n-si:si3n4_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2153.21 K, x(N) 0.57143–0.57143 | 8 | 2 |
| [SI3N4_A](#phase-n-si-si3n4-a); _phase:n-si:si3n4-a_ | Si3N4-alpha · hP28 · P31c (159) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [SI3N4_B](#phase-n-si-si3n4-b); _phase:n-si:si3n4-b_ | Si3N4-beta · hP14 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2213.83 K, x(N) 0.57143–0.57143 | 0 | 1 |

## DIAMOND_A4 (N–Si)

- Id: `phase:n-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1687 K, x(N) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:a4-diamond)

Names (6): _corpus: _corpus:phase:n-si:a4-diamond, corpus:phase:n-si:diamond-a4  
_paper: _paper:10.1016/j.calphad.2003.12.005:diamond_Si  
_tdb: _tdb:SiN-03Ma-LB.tdb:DIAMOND_A4, tdb:SiN-18Sri.tdb:DIAMOND_A4, tdb:SiN-92Hil.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[SiN-03Ma-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-03Ma-LB.tdb): DIAMOND_A4, type code %, sha256 `82df19923aefac84…`

~~~~text
36: PHASE DIAMOND_A4 % 1 1 !
37: CONST DIAMOND_A4 : SI : !
~~~~

[SiN-18Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-18Sri.tdb): DIAMOND_A4, type code %, sha256 `05fdadd753872c55…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[SiN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-92Hil.tdb): DIAMOND_A4, type code %, sha256 `f49087962923feaa…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2003.12.005](https://doi.org/10.1016/j.calphad.2003.12.005) Xiaoyan Ma, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic assessment of the Si–N system, Calphad 27, 383-388 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.004](https://doi.org/10.1016/j.calphad.2018.06.004) S. Sridar, R. Kumar, K. C. Hari Kumar, Calphad, 62, 148-53(2018).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830902](https://doi.org/10.1515/ijmr-1992-830902) M. Hillert, S. Jonsson, B. Sundman, Z. Metallkd., 83, 648-54(1992).  
_assessment that models this phase_
- [doi:10.1063/1.1735180](https://doi.org/10.1063/1.1735180) W. Kaiser, C. D. Thurmond, Nitrogen in Silicon, Journal of Applied Physics 30, 427-431 (1959).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2403610](https://doi.org/10.1149/1.2403610) Y. Yatsurugi, N. Akiyama, Y. Endo, T. Nozaki, Concentration, Solubility, and Equilibrium Distribution Coefficient of Nitrogen and Oxygen in Semiconductor Silicon, J. Electrochem. Soc. 120, 975 (1973).  
_cited as the source of values for this phase_

## GAS (N–Si)

- Id: `phase:n-si:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300.67–2500 K, x(N) 0.99643–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:gas)

Names (5): _corpus: _corpus:phase:n-si:gas  
_paper: _paper:10.1016/j.calphad.2003.12.005:gas  
_tdb: _tdb:SiN-03Ma-LB.tdb:GAS, tdb:SiN-18Sri.tdb:GAS, tdb:SiN-92Hil.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[SiN-03Ma-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-03Ma-LB.tdb): GAS, type code %, sha256 `82df19923aefac84…`

~~~~text
44: PHASE GAS:G % 1 1 !
45: CONST GAS:G : N N2 N3 SI SI2 SI3 SIN SI2N : !
~~~~

[SiN-18Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-18Sri.tdb): GAS, type code %, sha256 `05fdadd753872c55…`

~~~~text
56: PHASE GAS:G % 1 1 !
57: CONST GAS:G : N N2 N3 SI SI2 SI3 SIN SI2N : !
~~~~

[SiN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-92Hil.tdb): GAS, type code %, sha256 `f49087962923feaa…`

~~~~text
53: PHASE GAS:G % 1 1 !
54: CONST GAS:G : N N2 N3 SI SI2 SI3 SIN SI2N : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2003.12.005](https://doi.org/10.1016/j.calphad.2003.12.005) Xiaoyan Ma, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic assessment of the Si–N system, Calphad 27, 383-388 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.004](https://doi.org/10.1016/j.calphad.2018.06.004) S. Sridar, R. Kumar, K. C. Hari Kumar, Calphad, 62, 148-53(2018).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830902](https://doi.org/10.1515/ijmr-1992-830902) M. Hillert, S. Jonsson, B. Sundman, Z. Metallkd., 83, 648-54(1992).  
_assessment that models this phase_
- [doi:10.1007/bf00542737](https://doi.org/10.1007/bf00542737) P. Dörner, L. J. Gauckler, H. Krieg, H. L. Lukas, G. Petzow, J. Weiss, Calculation of heterogeneous phase equilibria in the SiAlON system, J Mater Sci 16, 935-943 (1981).  
_cited as the source of values for this phase_
- [doi:10.1063/1.1735180](https://doi.org/10.1063/1.1735180) W. Kaiser, C. D. Thurmond, Nitrogen in Silicon, Journal of Applied Physics 30, 427-431 (1959).  
_cited as the source of values for this phase_

## ION (N–Si)

- Id: `phase:n-si:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1687–1974.95 K, x(N) 0–0.46
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:ion)

Names (2): _corpus: _corpus:phase:n-si:ion  
_tdb: _tdb:SiN-92Hil.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[SiN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-92Hil.tdb): ION, type code %, sha256 `f49087962923feaa…`

~~~~text
40: PHASE ION:Y % 2 1 1 !
41: CONST ION:Y : SI+4 : N-3 SIN1_3 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830902](https://doi.org/10.1515/ijmr-1992-830902) M. Hillert, S. Jonsson, B. Sundman, Z. Metallkd., 83, 648-54(1992).  
_assessment that models this phase_

## LIQUID (N–Si)

- Id: `phase:n-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1686.94–2500 K, x(N) 0–0.00388
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:liquid)

Names (6): _corpus: _corpus:phase:n-si:liquid  
_paper: _paper:10.1016/j.calphad.2003.12.005:L, paper:10.1016/j.calphad.2003.12.005:liquid  
_tdb: _tdb:SiN-03Ma-LB.tdb:LIQUID, tdb:SiN-18Sri.tdb:LIQUID, tdb:SiN-92Hil.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[SiN-03Ma-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-03Ma-LB.tdb): LIQUID, type code %, sha256 `82df19923aefac84…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : N SI : !
~~~~

[SiN-18Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-18Sri.tdb): LIQUID, type code %, sha256 `05fdadd753872c55…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : N SI : !
~~~~

[SiN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-92Hil.tdb): LIQUID, type code %, sha256 `f49087962923feaa…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : N SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2003.12.005](https://doi.org/10.1016/j.calphad.2003.12.005) Xiaoyan Ma, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic assessment of the Si–N system, Calphad 27, 383-388 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.06.004](https://doi.org/10.1016/j.calphad.2018.06.004) S. Sridar, R. Kumar, K. C. Hari Kumar, Calphad, 62, 148-53(2018).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830902](https://doi.org/10.1515/ijmr-1992-830902) M. Hillert, S. Jonsson, B. Sundman, Z. Metallkd., 83, 648-54(1992).  
_assessment that models this phase_
- [doi:10.1063/1.1735180](https://doi.org/10.1063/1.1735180) W. Kaiser, C. D. Thurmond, Nitrogen in Silicon, Journal of Applied Physics 30, 427-431 (1959).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2403610](https://doi.org/10.1149/1.2403610) Y. Yatsurugi, N. Akiyama, Y. Endo, T. Nozaki, Concentration, Solubility, and Equilibrium Distribution Coefficient of Nitrogen and Oxygen in Semiconductor Silicon, J. Electrochem. Soc. 120, 975 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00542737](https://doi.org/10.1007/bf00542737) P. Dörner, L. J. Gauckler, H. Krieg, H. L. Lukas, G. Petzow, J. Weiss, Calculation of heterogeneous phase equilibria in the SiAlON system, J Mater Sci 16, 935-943 (1981).  
_cited as the source of values for this phase_

## N2GAS (N–Si)

- Id: `phase:n-si:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1725 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:n2gas)

Names (4): _corpus: _corpus:phase:n-si:n2gas  
_tdb: _tdb:SiN-03Ma-LB.tdb:N2GAS, tdb:SiN-18Sri.tdb:N2GAS, tdb:SiN-92Hil.tdb:N2GAS  


### TDB models of N2GAS (3): PHASE and CONSTITUENT statements as written

[SiN-03Ma-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-03Ma-LB.tdb): N2GAS, type code %, sha256 `82df19923aefac84…`

~~~~text
47: PHASE N2GAS % 1 1 !
48: CONST N2GAS : N2 : !
~~~~

[SiN-18Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-18Sri.tdb): N2GAS, type code %, sha256 `05fdadd753872c55…`

~~~~text
59: PHASE N2GAS % 1 1 !
60: CONST N2GAS : N2 : !
~~~~

[SiN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-92Hil.tdb): N2GAS, type code %, sha256 `f49087962923feaa…`

~~~~text
56: PHASE N2GAS % 1 1 !
57: CONST N2GAS : N2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2003.12.005](https://doi.org/10.1016/j.calphad.2003.12.005) Xiaoyan Ma, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic assessment of the Si–N system, Calphad 27, 383-388 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.06.004](https://doi.org/10.1016/j.calphad.2018.06.004) S. Sridar, R. Kumar, K. C. Hari Kumar, Calphad, 62, 148-53(2018).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830902](https://doi.org/10.1515/ijmr-1992-830902) M. Hillert, S. Jonsson, B. Sundman, Z. Metallkd., 83, 648-54(1992).  
_assessment that models this phase_

## SI3N4 (N–Si)

- Id: `phase:n-si:si3n4`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P6_3/m (176) — on-hull MP Si3N4 at x(SI)=0.4286
- Candidate (dft_oqmd): P63/m (176) — on-hull OQMD N4 Si3 at x(SI)=0.4286
- Candidate (literature_printed): Si3N4-alpha · hP28 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Si3N4-alpha · hP28 · P31c (159) — Hallstedt 2025 mmc2 row for SI3N4: Si3N4
- Candidate (sgte_mmc2): Si3N4-beta · hP14 · R-3c (167) — Hallstedt 2025 mmc2 row for SI3N4: Si3N4
- Candidate (tdb_comment): Si3N4; alpha: · hP28 · p31c — SiN-03Ma-LB.tdb: 'Prototype Si3N4; alpha: (hP28, p31c), beta: (hP14, P6_3)'
- Candidate (tdb_comment): Si3N4; alpha: · hP28 · p31c — SiN-92Hil.tdb: 'Prototype Si3N4; alpha: (hP28, p31c), beta: (hP14, P6_3)'
- Stoichiometry: N 0.5714, Si 0.4286
- Stability: stable in 2 of 2 calculated diagram(s): 300–2153.21 K, x(N) 0.57143–0.57143
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:si3n4)

Names (4): _corpus: _corpus:phase:n-si:si3n4  
_paper: _paper:10.1016/j.calphad.2003.12.005:Si3N4  
_tdb: _tdb:SiN-03Ma-LB.tdb:SI3N4, tdb:SiN-92Hil.tdb:SI3N4  


### TDB models of SI3N4 (2): PHASE and CONSTITUENT statements as written

[SiN-03Ma-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-03Ma-LB.tdb): SI3N4, type code %, sha256 `82df19923aefac84…`

~~~~text
41: PHASE SI3N4 % 2 3 4 !
42: CONST SI3N4 : SI : N : !
~~~~

[SiN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-92Hil.tdb): SI3N4, type code %, sha256 `f49087962923feaa…`

~~~~text
50: PHASE SI3N4 % 2 3 4 !
51: CONST SI3N4 : SI : N : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2003.12.005](https://doi.org/10.1016/j.calphad.2003.12.005) Xiaoyan Ma, Changrong Li, Fuming Wang, Weijing Zhang, Thermodynamic assessment of the Si–N system, Calphad 27, 383-388 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1992-830902](https://doi.org/10.1515/ijmr-1992-830902) M. Hillert, S. Jonsson, B. Sundman, Z. Metallkd., 83, 648-54(1992).  
_assessment that models this phase_
- [doi:10.1063/1.1735180](https://doi.org/10.1063/1.1735180) W. Kaiser, C. D. Thurmond, Nitrogen in Silicon, Journal of Applied Physics 30, 427-431 (1959).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00542737](https://doi.org/10.1007/bf00542737) P. Dörner, L. J. Gauckler, H. Krieg, H. L. Lukas, G. Petzow, J. Weiss, Calculation of heterogeneous phase equilibria in the SiAlON system, J Mater Sci 16, 935-943 (1981).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2403610](https://doi.org/10.1149/1.2403610) Y. Yatsurugi, N. Akiyama, Y. Endo, T. Nozaki, Concentration, Solubility, and Equilibrium Distribution Coefficient of Nitrogen and Oxygen in Semiconductor Silicon, J. Electrochem. Soc. 120, 975 (1973).  
_cited as the source of values for this phase_

## SI3N4_A (N–Si)

- Id: `phase:n-si:si3n4-a`; status `assigned`
- Structure: Si3N4-alpha · hP28 · P31c (159); type `st:si3n4-alpha-hp28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:A, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: N 0.5714, Si 0.4286
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:si3n4-a)

Names (2): _corpus: _corpus:phase:n-si:si3n4-a  
_tdb: _tdb:SiN-18Sri.tdb:SI3N4_A  


### TDB models of SI3N4_A (1): PHASE and CONSTITUENT statements as written

[SiN-18Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-18Sri.tdb): SI3N4_A, type code %, sha256 `05fdadd753872c55…`

~~~~text
48: PHASE SI3N4_A % 2 3 4 !
49: CONST SI3N4_A : SI : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.06.004](https://doi.org/10.1016/j.calphad.2018.06.004) S. Sridar, R. Kumar, K. C. Hari Kumar, Calphad, 62, 148-53(2018).  
_assessment that models this phase_

## SI3N4_B (N–Si)

- Id: `phase:n-si:si3n4-b`; status `assigned`
- Structure: Si3N4-beta · hP14 · R-3c (167); type `st:si3n4-beta-hp14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:B, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: N 0.5714, Si 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–2213.83 K, x(N) 0.57143–0.57143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-si:si3n4-b)

Names (2): _corpus: _corpus:phase:n-si:si3n4-b  
_tdb: _tdb:SiN-18Sri.tdb:SI3N4_B  


### TDB models of SI3N4_B (1): PHASE and CONSTITUENT statements as written

[SiN-18Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SiN-18Sri.tdb): SI3N4_B, type code %, sha256 `05fdadd753872c55…`

~~~~text
53: PHASE SI3N4_B % 2 3 4 !
54: CONST SI3N4_B : SI : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.06.004](https://doi.org/10.1016/j.calphad.2018.06.004) S. Sridar, R. Kumar, K. C. Hari Kumar, Calphad, 62, 148-53(2018).  
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
