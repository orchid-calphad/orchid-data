# Fe–N phases

> Fe–N system: 6 phases (tier A 3, tier C 1, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-N.html · Markdown: https://data.orchid-project.org/phases/pages/FE-N.md

6 phases (tier A 3, tier C 1, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-N) · [full JSON](https://data.orchid-project.org/phases/systems/FE-N.json) · [Fe–N system page](https://data.orchid-project.org/systems/FE-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–N system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-n-bcc-a2); _phase:fe-n:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2499.79 K, x(N) 0–0.00058 | 0 | 6 |
| [FCC_A1](#phase-fe-n-fcc-a1); _phase:fe-n:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 1172.13–1680.35 K, x(N) 0–0.00134 | 0 | 6 |
| [FE4N_L1](#phase-fe-n-fe4n-l1); _phase:fe-n:fe4n-l1_ | Fe4N · L'1 · cP5 · Pm-3m (221) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 6 calculated diagram(s) | 0 | 6 |
| [HCP_A3](#phase-fe-n-hcp-a3); _phase:fe-n:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-fe-n-liquid); _phase:fe-n:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1808.38–2500 K, x(N) 0–0.00216 | 0 | 6 |
| [N2GAS](#phase-fe-n-n2gas); _phase:fe-n:n2gas_ | gas | gas | stable in 6 of 6 calculated diagram(s): 300–2500 K, x(N) 1–1 | 0 | 6 |

## BCC_A2 (Fe–N)

- Id: `phase:fe-n:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2499.79 K, x(N) 0–0.00058
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-n:bcc-a2)

Names (7): _corpus: _corpus:phase:fe-n:bcc-a2  
_tdb: _tdb:FeN-16Goe.tdb:BCC_A2, tdb:FeN-20Kou.tdb:BCC_A2, tdb:FeN-87Fri.tdb:BCC_A2, tdb:FeN-91Fri-LB.tdb:BCC_A2, tdb:FeN-93Du-mod.tdb:BCC_A2, tdb:FeN-93Du.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[FeN-16Goe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-16Goe.tdb): BCC_A2, type code %B, sha256 `eddeea978f7c05e4…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE : N VA% : !
~~~~

[FeN-20Kou.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-20Kou.tdb): BCC_A2, type code %B, sha256 `37f1edb7a040f1d2…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : FE : N VA% : !
~~~~

[FeN-87Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-87Fri.tdb): BCC_A2, type code %B, sha256 `b38a41b18e42bbef…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE : N VA% : !
~~~~

[FeN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-91Fri-LB.tdb): BCC_A2, type code %B, sha256 `dd61cb0ecd6570c0…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : FE : N VA% : !
~~~~

[FeN-93Du-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du-mod.tdb): BCC_A2, type code %B, sha256 `73a8d69e4021ea32…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : FE : N VA% : !
~~~~

[FeN-93Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du.tdb): BCC_A2, type code %B, sha256 `d651be243743cfad…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE : N VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667880](https://doi.org/10.1007/BF02667880) H. Du, J. Phase Equilib., 14, 682-93(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90004-6](https://doi.org/10.1016/0364-5916%2887%2990004-6) K. Frisk, Calphad, 11, 127-34(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102197](https://doi.org/10.1016/j.calphad.2020.102197) R. Kouba, K. Rayane, M. Keddam, Calphad, 71, 1ß2197(2020).  
_assessment that models this phase_

## FCC_A1 (Fe–N)

- Id: `phase:fe-n:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1172.13–1680.35 K, x(N) 0–0.00134
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-n:fcc-a1)

Names (7): _corpus: _corpus:phase:fe-n:fcc-a1  
_tdb: _tdb:FeN-16Goe.tdb:FCC_A1, tdb:FeN-20Kou.tdb:FCC_A1, tdb:FeN-87Fri.tdb:FCC_A1, tdb:FeN-91Fri-LB.tdb:FCC_A1, tdb:FeN-93Du-mod.tdb:FCC_A1, tdb:FeN-93Du.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[FeN-16Goe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-16Goe.tdb): FCC_A1, type code %A, sha256 `eddeea978f7c05e4…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE : N VA% : !
~~~~

[FeN-20Kou.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-20Kou.tdb): FCC_A1, type code %A, sha256 `37f1edb7a040f1d2…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : FE : N VA% : !
~~~~

[FeN-87Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-87Fri.tdb): FCC_A1, type code %A, sha256 `b38a41b18e42bbef…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE : N VA% : !
~~~~

[FeN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-91Fri-LB.tdb): FCC_A1, type code %A, sha256 `dd61cb0ecd6570c0…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : FE : N VA% : !
~~~~

[FeN-93Du-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du-mod.tdb): FCC_A1, type code %A, sha256 `73a8d69e4021ea32…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : FE : N VA% : !
~~~~

[FeN-93Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du.tdb): FCC_A1, type code %A, sha256 `d651be243743cfad…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE : N VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667880](https://doi.org/10.1007/BF02667880) H. Du, J. Phase Equilib., 14, 682-93(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90004-6](https://doi.org/10.1016/0364-5916%2887%2990004-6) K. Frisk, Calphad, 11, 127-34(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102197](https://doi.org/10.1016/j.calphad.2020.102197) R. Kouba, K. Rayane, M. Keddam, Calphad, 71, 1ß2197(2020).  
_assessment that models this phase_

## FE4N_L1 (Fe–N)

- Id: `phase:fe-n:fe4n-l1`; status `assigned`
- Structure: Fe4N · L'1 · cP5 · Pm-3m (221); type `st:l-1-fe4n-cp5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:L1, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-n:fe4n-l1)

Names (7): _corpus: _corpus:phase:fe-n:fe4n-l1  
_tdb: _tdb:FeN-16Goe.tdb:FE4N_L1, tdb:FeN-20Kou.tdb:FE4N_L1, tdb:FeN-87Fri.tdb:FE4N_L1, tdb:FeN-91Fri-LB.tdb:FE4N_L1, tdb:FeN-93Du-mod.tdb:FE4N_L1, tdb:FeN-93Du.tdb:FE4N_L1  


### TDB models of FE4N_L1 (6): PHASE and CONSTITUENT statements as written

[FeN-16Goe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-16Goe.tdb): FE4N_L1, type code %, sha256 `eddeea978f7c05e4…`

~~~~text
49: PHASE FE4N_L1 % 2 4 1 !
50: CONST FE4N_L1 : FE : N VA :!
~~~~

[FeN-20Kou.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-20Kou.tdb): FE4N_L1, type code %, sha256 `37f1edb7a040f1d2…`

~~~~text
47: PHASE FE4N_L1 % 2 4 1 !
48: CONST FE4N_L1 : FE : N VA :!
~~~~

[FeN-87Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-87Fri.tdb): FE4N_L1, type code %, sha256 `b38a41b18e42bbef…`

~~~~text
45: PHASE FE4N_L1 % 2 4 1 !
46: CONST FE4N_L1 : FE : N :!
~~~~

[FeN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-91Fri-LB.tdb): FE4N_L1, type code %, sha256 `dd61cb0ecd6570c0…`

~~~~text
53: PHASE FE4N_L1 % 2 4 1 !
54: CONST FE4N_L1 : FE : N :!
~~~~

[FeN-93Du-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du-mod.tdb): FE4N_L1, type code %, sha256 `73a8d69e4021ea32…`

~~~~text
51: PHASE FE4N_L1 % 2 4 1 !
52: CONST FE4N_L1 : FE : N VA :!
~~~~

[FeN-93Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du.tdb): FE4N_L1, type code %, sha256 `d651be243743cfad…`

~~~~text
46: PHASE FE4N_L1 % 2 4 1 !
47: CONST FE4N_L1 : FE : N VA :!
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667880](https://doi.org/10.1007/BF02667880) H. Du, J. Phase Equilib., 14, 682-93(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90004-6](https://doi.org/10.1016/0364-5916%2887%2990004-6) K. Frisk, Calphad, 11, 127-34(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102197](https://doi.org/10.1016/j.calphad.2020.102197) R. Kouba, K. Rayane, M. Keddam, Calphad, 71, 1ß2197(2020).  
_assessment that models this phase_

## HCP_A3 (Fe–N)

- Id: `phase:fe-n:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-n:hcp-a3)

Names (7): _corpus: _corpus:phase:fe-n:hcp-a3  
_tdb: _tdb:FeN-16Goe.tdb:HCP_A3, tdb:FeN-20Kou.tdb:HCP_A3, tdb:FeN-87Fri.tdb:HCP_A3, tdb:FeN-91Fri-LB.tdb:HCP_A3, tdb:FeN-93Du-mod.tdb:HCP_A3, tdb:FeN-93Du.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[FeN-16Goe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-16Goe.tdb): HCP_A3, type code %, sha256 `eddeea978f7c05e4…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : FE : N VA% : !
~~~~

[FeN-20Kou.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-20Kou.tdb): HCP_A3, type code %, sha256 `37f1edb7a040f1d2…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : FE : N VA% : !
~~~~

[FeN-87Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-87Fri.tdb): HCP_A3, type code %, sha256 `b38a41b18e42bbef…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : FE : N VA% : !
~~~~

[FeN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-91Fri-LB.tdb): HCP_A3, type code %, sha256 `dd61cb0ecd6570c0…`

~~~~text
48: PHASE HCP_A3 % 2 1 0.5 !
49: CONST HCP_A3 : FE : N VA% : !
~~~~

[FeN-93Du-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du-mod.tdb): HCP_A3, type code %, sha256 `73a8d69e4021ea32…`

~~~~text
46: PHASE HCP_A3 % 2 1 0.5 !
47: CONST HCP_A3 : FE : N VA% : !
~~~~

[FeN-93Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du.tdb): HCP_A3, type code %, sha256 `d651be243743cfad…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : FE : N VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667880](https://doi.org/10.1007/BF02667880) H. Du, J. Phase Equilib., 14, 682-93(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90004-6](https://doi.org/10.1016/0364-5916%2887%2990004-6) K. Frisk, Calphad, 11, 127-34(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102197](https://doi.org/10.1016/j.calphad.2020.102197) R. Kouba, K. Rayane, M. Keddam, Calphad, 71, 1ß2197(2020).  
_assessment that models this phase_

## LIQUID (Fe–N)

- Id: `phase:fe-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1808.38–2500 K, x(N) 0–0.00216
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-n:liquid)

Names (7): _corpus: _corpus:phase:fe-n:liquid  
_tdb: _tdb:FeN-16Goe.tdb:LIQUID, tdb:FeN-20Kou.tdb:LIQUID, tdb:FeN-87Fri.tdb:LIQUID, tdb:FeN-91Fri-LB.tdb:LIQUID, tdb:FeN-93Du-mod.tdb:LIQUID, tdb:FeN-93Du.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[FeN-16Goe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-16Goe.tdb): LIQUID, type code %, sha256 `eddeea978f7c05e4…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : FE N : !
~~~~

[FeN-20Kou.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-20Kou.tdb): LIQUID, type code %, sha256 `37f1edb7a040f1d2…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : FE N : !
~~~~

[FeN-87Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-87Fri.tdb): LIQUID, type code %, sha256 `b38a41b18e42bbef…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE N : !
~~~~

[FeN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-91Fri-LB.tdb): LIQUID, type code %, sha256 `dd61cb0ecd6570c0…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : FE N : !
~~~~

[FeN-93Du-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du-mod.tdb): LIQUID, type code %, sha256 `73a8d69e4021ea32…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : FE N : !
~~~~

[FeN-93Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du.tdb): LIQUID, type code %, sha256 `d651be243743cfad…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE N : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667880](https://doi.org/10.1007/BF02667880) H. Du, J. Phase Equilib., 14, 682-93(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90004-6](https://doi.org/10.1016/0364-5916%2887%2990004-6) K. Frisk, Calphad, 11, 127-34(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102197](https://doi.org/10.1016/j.calphad.2020.102197) R. Kouba, K. Rayane, M. Keddam, Calphad, 71, 1ß2197(2020).  
_assessment that models this phase_

## N2GAS (Fe–N)

- Id: `phase:fe-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2500 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-n:n2gas)

Names (7): _corpus: _corpus:phase:fe-n:n2gas  
_tdb: _tdb:FeN-16Goe.tdb:N2GAS, tdb:FeN-20Kou.tdb:N2GAS, tdb:FeN-87Fri.tdb:N2GAS, tdb:FeN-91Fri-LB.tdb:N2GAS, tdb:FeN-93Du-mod.tdb:N2GAS, tdb:FeN-93Du.tdb:N2GAS  


### TDB models of N2GAS (6): PHASE and CONSTITUENT statements as written

[FeN-16Goe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-16Goe.tdb): N2GAS, type code %, sha256 `eddeea978f7c05e4…`

~~~~text
52: PHASE N2GAS % 1 1 !
53: CONST N2GAS : N2 : !
~~~~

[FeN-20Kou.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-20Kou.tdb): N2GAS, type code %, sha256 `37f1edb7a040f1d2…`

~~~~text
50: PHASE N2GAS % 1 1 !
51: CONST N2GAS : N2 : !
~~~~

[FeN-87Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-87Fri.tdb): N2GAS, type code %, sha256 `b38a41b18e42bbef…`

~~~~text
48: PHASE N2GAS % 1 1 !
49: CONST N2GAS : N2 : !
~~~~

[FeN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-91Fri-LB.tdb): N2GAS, type code %, sha256 `dd61cb0ecd6570c0…`

~~~~text
56: PHASE N2GAS % 1 1 !
57: CONST N2GAS : N2 : !
~~~~

[FeN-93Du-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du-mod.tdb): N2GAS, type code %, sha256 `73a8d69e4021ea32…`

~~~~text
54: PHASE N2GAS % 1 1 !
55: CONST N2GAS : N2 : !
~~~~

[FeN-93Du.tdb](https://orchid-project.org/data/databases/sgte-binary/FeN-93Du.tdb): N2GAS, type code %, sha256 `d651be243743cfad…`

~~~~text
49: PHASE N2GAS % 1 1 !
50: CONST N2GAS : N2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02667880](https://doi.org/10.1007/BF02667880) H. Du, J. Phase Equilib., 14, 682-93(1993).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90004-6](https://doi.org/10.1016/0364-5916%2887%2990004-6) K. Frisk, Calphad, 11, 127-34(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102197](https://doi.org/10.1016/j.calphad.2020.102197) R. Kouba, K. Rayane, M. Keddam, Calphad, 71, 1ß2197(2020).  
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
