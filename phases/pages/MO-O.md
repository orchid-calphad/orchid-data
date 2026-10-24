# Mo–O phases

> Mo–O system: 13 phases (tier A 3, tier C 3, liquid 3, gas 2, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-O.html · Markdown: https://data.orchid-project.org/phases/pages/MO-O.md

13 phases (tier A 3, tier C 3, liquid 3, gas 2, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-O) · [full JSON](https://data.orchid-project.org/phases/systems/MO-O.json) · [Mo–O system page](https://data.orchid-project.org/systems/MO-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–O system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-o-bcc-a2); _phase:mo-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2897 K, x(O) 0–0.00922 | 2 | 2 |
| [FCC_A1](#phase-mo-o-fcc-a1); _phase:mo-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-mo-o-gas); _phase:mo-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300.22–4000 K, x(O) 0.65995–1 | 0 | 2 |
| [HCP_A3](#phase-mo-o-hcp-a3); _phase:mo-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-mo-o-ion); _phase:mo-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1055.64–4000 K, x(O) 0–0.75189 | 0 | 1 |
| [OXIDE_L](#phase-mo-o-l-oxide); _phase:mo-o:l-oxide_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1070.09–1576.58 K, x(O) 0.73644–0.74999 | 0 | 1 |
| [LIQUID](#phase-mo-o-liquid); _phase:mo-o:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2481.38–4000 K, x(O) 0–0.1831 | 9 | 1 |
| [MO4O11](#phase-mo-o-mo4o11); _phase:mo-o:mo4o11_ | Mo4O11 · oP60 · Pna2_1 (33) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1093.72 K, x(O) 0.73333–0.73333 | 18 | 2 |
| [MO8O23](#phase-mo-o-mo8o23); _phase:mo-o:mo8o23_ | Mo8O23 · mP62 · P2/c (13) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1070.09 K, x(O) 0.74194–0.74194 | 42 | 2 |
| [MO9O26](#phase-mo-o-mo9o26); _phase:mo-o:mo9o26_ |  | needs_review | stable in 1 of 2 calculated diagram(s): 300.64–1063.67 K, x(O) 0.74286–0.74286 | 44 | 2 |
| [MOO2](#phase-mo-o-moo2); _phase:mo-o:moo2_ | VO2 · mP12 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2570 K, x(O) 0.6549–0.66667 | 23 | 2 |
| [MOO3](#phase-mo-o-moo3); _phase:mo-o:moo3_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1074.98 K, x(O) 0.75–0.75 | 60 | 2 |
| [O2GAS](#phase-mo-o-o2gas); _phase:mo-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–795 K, x(O) 1–1 | 0 | 2 |

## BCC_A2 (Mo–O)

- Id: `phase:mo-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2897 K, x(O) 0–0.00922
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:bcc-a2)

Names (4): _corpus: _corpus:phase:mo-o:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.12.006:(Mo)  
_tdb: _tdb:MoO-14Zha.tdb:BCC_A2, tdb:MoO-18Cor.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): BCC_A2, type code %B, sha256 `8676113eb7b6a334…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : MO% O : VA : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): BCC_A2, type code %B, sha256 `ed619144ab732e61…`

~~~~text
56: PHASE BCC_A2 %B 2 1 3 !
57: CONST BCC_A2 : MO : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_

## FCC_A1 (Mo–O)

- Id: `phase:mo-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:fcc-a1)

Names (3): _corpus: _corpus:phase:mo-o:fcc-a1  
_tdb: _tdb:MoO-14Zha.tdb:FCC_A1, tdb:MoO-18Cor.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): FCC_A1, type code %A, sha256 `8676113eb7b6a334…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : MO : VA : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): FCC_A1, type code %A, sha256 `ed619144ab732e61…`

~~~~text
51: PHASE FCC_A1 %A 2 1 1 !
52: CONST FCC_A1 : MO : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_

## GAS (Mo–O)

- Id: `phase:mo-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.22–4000 K, x(O) 0.65995–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:gas)

Names (3): _corpus: _corpus:phase:mo-o:gas  
_tdb: _tdb:MoO-14Zha.tdb:GAS, tdb:MoO-18Cor.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): GAS, type code %, sha256 `8676113eb7b6a334…`

~~~~text
86: PHASE GAS:G % 1 1 !
87: CONST GAS:G : MO MO2 MOO MOO2 MOO3 MO2O6 MO3O9 MO4O12 MO5O15 O O2 O3 : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): GAS, type code %, sha256 `ed619144ab732e61…`

~~~~text
94: PHASE GAS:G % 1 1 !
95: CONST GAS:G : MO MO2 MOO MOO2 MOO3 MO2O6 MO3O9 MO4O12 MO5O15 O O2 O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_

## HCP_A3 (Mo–O)

- Id: `phase:mo-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mo 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:hcp-a3)

Names (3): _corpus: _corpus:phase:mo-o:hcp-a3  
_tdb: _tdb:MoO-14Zha.tdb:HCP_A3, tdb:MoO-18Cor.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): HCP_A3, type code %A, sha256 `8676113eb7b6a334…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : MO : VA : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): HCP_A3, type code %A, sha256 `ed619144ab732e61…`

~~~~text
61: PHASE HCP_A3 %A 2 1 0.5 !
62: CONST HCP_A3 : MO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_

## ION (Mo–O)

- Id: `phase:mo-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1055.64–4000 K, x(O) 0–0.75189
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:ion)

Names (2): _corpus: _corpus:phase:mo-o:ion  
_tdb: _tdb:MoO-18Cor.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): ION, type code %, sha256 `ed619144ab732e61…`

~~~~text
46: PHASE ION:Y % 2 1 1 !
47: CONST ION:Y : MO+4 : MOO4-2 O-2 VA MOO3 O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_

## OXIDE_L (Mo–O)

- Id: `phase:mo-o:l-oxide`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1070.09–1576.58 K, x(O) 0.73644–0.74999
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:l-oxide)

Names (2): _corpus: _corpus:phase:mo-o:l-oxide  
_tdb: _tdb:MoO-14Zha.tdb:OXIDE_L  


### TDB models of OXIDE_L (1): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): OXIDE_L, type code %, sha256 `8676113eb7b6a334…`

~~~~text
38: PHASE OXIDE_L % 1 1 !
39: CONST OXIDE_L : MOO2 MOO3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase_

## LIQUID (Mo–O)

- Id: `phase:mo-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2481.38–4000 K, x(O) 0–0.1831
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:liquid)

Names (3): _corpus: _corpus:phase:mo-o:liquid  
_paper: _paper:10.1016/j.calphad.2013.12.006:L  
_tdb: _tdb:MoO-14Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): LIQUID, type code %, sha256 `8676113eb7b6a334…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : MO O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase; reports values for this phase_

## MO4O11 (Mo–O)

- Id: `phase:mo-o:mo4o11`; status `assigned`
- Structure: Mo4O11 · oP60 · Pna2_1 (33); type `st:mo4o11-op60`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mo 0.2667, O 0.7333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1093.72 K, x(O) 0.73333–0.73333
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:mo4o11)

Names (4): _corpus: _corpus:phase:mo-o:mo4o11  
_paper: _paper:10.1016/j.calphad.2013.12.006:Mo4O11  
_tdb: _tdb:MoO-14Zha.tdb:MO4O11, tdb:MoO-18Cor.tdb:MO4O11  


### TDB models of MO4O11 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): MO4O11, type code %, sha256 `8676113eb7b6a334…`

~~~~text
63: PHASE MO4O11 % 2 1 2.75 !
64: CONST MO4O11 : MO : O : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): MO4O11, type code %, sha256 `ed619144ab732e61…`

~~~~text
71: PHASE MO4O11 % 2 1 2.75 !
72: CONST MO4O11 : MO : O : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(85)90253-1](https://doi.org/10.1016/0022-4596%2885%2990253-1) M. Ghedira, H. Vincent, M. Marezio, J. Marcus, G. Furcaudot, Structure cristalline du conducteur me´tallique bidimensionnel Mo4O11-γ, Journal of Solid State Chemistry 56, 66-73 (1985).  
_cited as the source of values for this phase_

## MO8O23 (Mo–O)

- Id: `phase:mo-o:mo8o23`; status `assigned`
- Structure: Mo8O23 · mP62 · P2/c (13); type `st:mo8o23-mp62`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mo 0.2581, O 0.7419
- Stability: stable in 2 of 2 calculated diagram(s): 300–1070.09 K, x(O) 0.74194–0.74194
- Literature: 42 values (42 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:mo8o23)

Names (4): _corpus: _corpus:phase:mo-o:mo8o23  
_paper: _paper:10.1016/j.calphad.2013.12.006:Mo8O23  
_tdb: _tdb:MoO-14Zha.tdb:MO8O23, tdb:MoO-18Cor.tdb:MO8O23  


### TDB models of MO8O23 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): MO8O23, type code %, sha256 `8676113eb7b6a334…`

~~~~text
68: PHASE MO8O23 % 2 1 2.875 !
69: CONST MO8O23 : MO : O : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): MO8O23, type code %, sha256 `ed619144ab732e61…`

~~~~text
76: PHASE MO8O23 % 2 1 2.875 !
77: CONST MO8O23 : MO : O : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(87)90218-0](https://doi.org/10.1016/0022-4596%2887%2990218-0) H. Fujishita, M. Sato, S. Sato, S. Hoshino, Structure determination of low-dimensional conductor Mo8O23, Journal of Solid State Chemistry 66, 40-46 (1987).  
_cited as the source of values for this phase_

## MO9O26 (Mo–O)

- Id: `phase:mo-o:mo9o26`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (literature_printed): Mo9O26 · mP70 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Mo9O26 · mP70 · P2/c (13) — Hallstedt 2025 mmc2 row for MO9O26: Mo9O26
- Candidate (tdb_comment): Mo9O26 · mP70 · P2/c — MoO-14Zha.tdb: 'Prototype Mo9O26 (mP70, P2/c)'
- Candidate (tdb_comment): Mo9O26 · mP70 · P2/c — MoO-18Cor.tdb: 'Prototype Mo9O26 (mP70, P2/c)'
- Stoichiometry: Mo 0.2571, O 0.7429
- Stability: stable in 1 of 2 calculated diagram(s): 300.64–1063.67 K, x(O) 0.74286–0.74286
- Literature: 44 values (44 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:mo9o26)

Names (4): _corpus: _corpus:phase:mo-o:mo9o26  
_paper: _paper:10.1016/j.calphad.2013.12.006:Mo9O26  
_tdb: _tdb:MoO-14Zha.tdb:MO9O26, tdb:MoO-18Cor.tdb:MO9O26  


### TDB models of MO9O26 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): MO9O26, type code %, sha256 `8676113eb7b6a334…`

~~~~text
73: PHASE MO9O26 % 2 1 2.889 !
74: CONST MO9O26 : MO : O : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): MO9O26, type code %, sha256 `ed619144ab732e61…`

~~~~text
81: PHASE MO9O26 % 2 1 2.889 !
82: CONST MO9O26 : MO : O : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1088/0022-3719/20/29/013](https://doi.org/10.1088/0022-3719/20/29/013) M Sato, M Onoda, Y Matsuda, Structural transitions in Mo\<sub>n\</sub>O\<sub>3n-1\</sub>(n=9 and 10), J. Phys. C: Solid State Phys. 20, 4763-4771 (1987).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.02-0501](https://doi.org/10.3891/acta.chem.scand.02-0501) Arne Magnéli, Niels Hofman-Bang, Poul Gjertsen, The Crystal Structures of Mo9O26 (beta'-Molybdenum Oxide) and Mo8O23 (beta-molybdenum Oxide)., Acta Chem. Scand. 2, 501-517 (1948).  
_cited as the source of values for this phase_

## MOO2 (Mo–O)

- Id: `phase:mo-o:moo2`; status `assigned`
- Structure: VO2 · mP12 · P2_1/c (14); type `st:vo2-mp12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–2570 K, x(O) 0.6549–0.66667
- Literature: 23 values (23 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:moo2)

Names (4): _corpus: _corpus:phase:mo-o:moo2  
_paper: _paper:10.1016/j.calphad.2013.12.006:MoO2  
_tdb: _tdb:MoO-14Zha.tdb:MOO2, tdb:MoO-18Cor.tdb:MOO2  


### TDB models of MOO2 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): MOO2, type code %, sha256 `8676113eb7b6a334…`

~~~~text
58: PHASE MOO2 % 2 1 2 !
59: CONST MOO2 : MO% O : MO O% : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): MOO2, type code %, sha256 `ed619144ab732e61…`

~~~~text
66: PHASE MOO2 % 2 1 2 !
67: CONST MOO2 : MO : O : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.3891/acta.chem.scand.21-0661](https://doi.org/10.3891/acta.chem.scand.21-0661) Björn G. Brandt, A. C. Skapski, Erling Thom, E. Stoll, G. Eriksson, R. Blinc et al., A Refinement of the Crystal Structure of Molybdenum Dioxide., Acta Chem. Scand. 21, 661-672 (1967).  
_cited as the source of values for this phase_

## MOO3 (Mo–O)

- Id: `phase:mo-o:moo3`; status `needs_review`
- No structure assigned. Why: no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P2_1/c (14) — on-hull MP MoO3 at x(O)=0.7500
- Candidate (dft_oqmd): P21/c (14) — on-hull OQMD Mo1 O3 at x(O)=0.7500
- Candidate (literature_printed): alpha-MoO3 · oP16 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): alpha-MoO3 · oP16 · Pnma (62) — Hallstedt 2025 mmc2 row for MOO3: MoO3 (alpha)
- Candidate (sgte_mmc2): beta-MoO3 · mP22 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MOO3: MoO3 (beta)
- Candidate (sgte_mmc2): WO3 · mP32 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MOO3: MoO3 (beta-prime)
- Candidate (tdb_comment): MoO3 · mP22 · P2_1/c — MoO-14Zha.tdb: 'Prototype MoO3 (mP22, P2_1/c) beta'
- Candidate (tdb_comment): MoO3 · oP16 · Pnma — MoO-14Zha.tdb: 'Prototype MoO3 (oP16, Pnma) alpha'
- Stoichiometry: Mo 0.2500, O 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1074.98 K, x(O) 0.75–0.75
- Literature: 60 values (60 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:moo3)

Names (4): _corpus: _corpus:phase:mo-o:moo3  
_paper: _paper:10.1016/j.calphad.2013.12.006:MoO3  
_tdb: _tdb:MoO-14Zha.tdb:MOO3, tdb:MoO-18Cor.tdb:MOO3  


### TDB models of MOO3 (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): MOO3, type code %, sha256 `8676113eb7b6a334…`

~~~~text
80: PHASE MOO3 % 2 1 3 !
81: CONST MOO3 : MO : O : !
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): MOO3, type code %, sha256 `ed619144ab732e61…`

~~~~text
88: PHASE MOO3 % 2 1 3 !
89: CONST MOO3 : MO : O : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(91)90064-o](https://doi.org/10.1016/0022-4596%2891%2990064-o) E.M. McCarron, J.C. Calabrese, The growth and single crystal structure of a high pressure phase of molybdenum trioxide: MoO3-II, Journal of Solid State Chemistry 91, 121-125 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(87)90035-3](https://doi.org/10.1016/0025-5408%2887%2990035-3) John B. Parise, Eugene.M. McCarron, Arthur W. Sleight, A new modification of ReO3-type MoO3 and the deuterated intercalation compound from which it is derived: D0.99M0O3, Materials Research Bulletin 22, 803-811 (1987).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.85.012104](https://doi.org/10.1103/physrevb.85.012104) Hong Ding, Keith G. Ray, Vidvuds Ozolins, Mark Asta, Structural and vibrational properties of \<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline"> \<mml:mi>α\</mml:mi> \</mml:math> -MoO \<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline"> \<mml:msub> \<mml:mrow/> \<mml:mn>3\</mml:mn> \</mml:msub> \</mml:math> from van der Waals corrected density functional theory calculations, Phys. Rev. B 85 (2012).  
_cited as the source of values for this phase_

## O2GAS (Mo–O)

- Id: `phase:mo-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–795 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-o:o2gas)

Names (3): _corpus: _corpus:phase:mo-o:o2gas  
_tdb: _tdb:MoO-14Zha.tdb:O2GAS, tdb:MoO-18Cor.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[MoO-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-14Zha.tdb): O2GAS, type code %, sha256 `8676113eb7b6a334…`

~~~~text
83: PHASE O2GAS % 1 1 !
84: CONST O2GAS : O2 :!
~~~~

[MoO-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoO-18Cor.tdb): O2GAS, type code %, sha256 `ed619144ab732e61…`

~~~~text
91: PHASE O2GAS % 1 1 !
92: CONST O2GAS : O2 :!
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.12.006](https://doi.org/10.1016/j.calphad.2013.12.006) C. Zhang, M.C. Gao, Y. Yang, F. Zhang, Thermodynamic modeling and first-principles calculations of the Mo–O system, Calphad 45, 178-187 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
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
