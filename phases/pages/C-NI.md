# C–Ni phases

> C–Ni system: 7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-NI.html · Markdown: https://data.orchid-project.org/phases/pages/C-NI.md

7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-NI) · [full JSON](https://data.orchid-project.org/phases/systems/C-NI.json) · [C–Ni system page](https://data.orchid-project.org/systems/C-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Ni system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-ni-a4-diamond); _phase:c-ni:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [GRAPHITE_A9](#phase-c-ni-a9-graphite); _phase:c-ni:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 4 |
| [BCC_A2](#phase-c-ni-bcc-a2); _phase:c-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 4 calculated diagram(s): 3008.4–4000 K, x(C) 0.35583–0.59326 | 0 | 4 |
| [CEMENTITE_D011](#phase-c-ni-cementite-d011); _phase:c-ni:cementite-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-c-ni-fcc-a1); _phase:c-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2974.54 K, x(C) 0–0.02743 | 0 | 4 |
| [HCP_A3](#phase-c-ni-hcp-a3); _phase:c-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-c-ni-liquid); _phase:c-ni:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1597.57–4000 K, x(C) 0–0.55948 | 0 | 4 |

## DIAMOND_A4 (C–Ni)

- Id: `phase:c-ni:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ni:a4-diamond)

Names (5): _corpus: _corpus:phase:c-ni:a4-diamond  
_tdb: _tdb:NiC-06Hal.tdb:DIAMOND_A4, tdb:NiC-22Oik.tdb:DIAMOND_A4, tdb:NiC-87Gab-LB.tdb:DIAMOND_A4, tdb:NiC-92Lee.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[NiC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-06Hal.tdb): DIAMOND_A4, type code %, sha256 `9c685cddb0304c2f…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

[NiC-22Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-22Oik.tdb): DIAMOND_A4, type code %, sha256 `10d4397973f84604…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : C : !
~~~~

[NiC-87Gab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-87Gab-LB.tdb): DIAMOND_A4, type code %, sha256 `c412cb38ff96497c…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : C : !
~~~~

[NiC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-92Lee.tdb): DIAMOND_A4, type code %, sha256 `d316a2888dd883af…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00995-0](https://doi.org/10.1007/s11669-022-00995-0) Katsunari Oikawa, Nobufumi Ueshima, Experimental Investigation and Thermodynamic Assessment of Ni–B and Ni–B–C Systems, J. Phase Equilib. Diffus. 43, 814-826 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90039-3](https://doi.org/10.1016/0364-5916%2887%2990039-3) Armand Gabriel, Per Gustafson, Ibrahim Ansara, A thermodynamic evaluation of the C-Fe-Ni system, Calphad 11, 203-218 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Ni)

- Id: `phase:c-ni:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ni:a9-graphite)

Names (5): _corpus: _corpus:phase:c-ni:a9-graphite  
_tdb: _tdb:NiC-06Hal.tdb:GRAPHITE_A9, tdb:NiC-22Oik.tdb:GRAPHITE_A9, tdb:NiC-87Gab-LB.tdb:GRAPHITE_A9, tdb:NiC-92Lee.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (4): PHASE and CONSTITUENT statements as written

[NiC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-06Hal.tdb): GRAPHITE_A9, type code %, sha256 `9c685cddb0304c2f…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

[NiC-22Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-22Oik.tdb): GRAPHITE_A9, type code %, sha256 `10d4397973f84604…`

~~~~text
48: PHASE GRAPHITE_A9 % 1 1 !
49: CONST GRAPHITE_A9 : C : !
~~~~

[NiC-87Gab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-87Gab-LB.tdb): GRAPHITE_A9, type code %, sha256 `c412cb38ff96497c…`

~~~~text
54: PHASE GRAPHITE_A9 % 1 1 !
55: CONST GRAPHITE_A9 : C : !
~~~~

[NiC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-92Lee.tdb): GRAPHITE_A9, type code %, sha256 `d316a2888dd883af…`

~~~~text
47: PHASE GRAPHITE_A9 % 1 1 !
48: CONST GRAPHITE_A9 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00995-0](https://doi.org/10.1007/s11669-022-00995-0) Katsunari Oikawa, Nobufumi Ueshima, Experimental Investigation and Thermodynamic Assessment of Ni–B and Ni–B–C Systems, J. Phase Equilib. Diffus. 43, 814-826 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90039-3](https://doi.org/10.1016/0364-5916%2887%2990039-3) Armand Gabriel, Per Gustafson, Ibrahim Ansara, A thermodynamic evaluation of the C-Fe-Ni system, Calphad 11, 203-218 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_

## BCC_A2 (C–Ni)

- Id: `phase:c-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 4 calculated diagram(s): 3008.4–4000 K, x(C) 0.35583–0.59326
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ni:bcc-a2)

Names (5): _corpus: _corpus:phase:c-ni:bcc-a2  
_tdb: _tdb:NiC-06Hal.tdb:BCC_A2, tdb:NiC-22Oik.tdb:BCC_A2, tdb:NiC-87Gab-LB.tdb:BCC_A2, tdb:NiC-92Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[NiC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-06Hal.tdb): BCC_A2, type code %B, sha256 `9c685cddb0304c2f…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NI : C VA% : !
~~~~

[NiC-22Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-22Oik.tdb): BCC_A2, type code %B, sha256 `10d4397973f84604…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI : C VA% : !
~~~~

[NiC-87Gab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-87Gab-LB.tdb): BCC_A2, type code %B, sha256 `c412cb38ff96497c…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : NI : C VA% : !
~~~~

[NiC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-92Lee.tdb): BCC_A2, type code %B, sha256 `d316a2888dd883af…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NI : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00995-0](https://doi.org/10.1007/s11669-022-00995-0) Katsunari Oikawa, Nobufumi Ueshima, Experimental Investigation and Thermodynamic Assessment of Ni–B and Ni–B–C Systems, J. Phase Equilib. Diffus. 43, 814-826 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90039-3](https://doi.org/10.1016/0364-5916%2887%2990039-3) Armand Gabriel, Per Gustafson, Ibrahim Ansara, A thermodynamic evaluation of the C-Fe-Ni system, Calphad 11, 203-218 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_

## CEMENTITE_D011 (C–Ni)

- Id: `phase:c-ni:cementite-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Stoichiometry: C 0.2500, Ni 0.7500
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ni:cementite-d011)

Names (5): _corpus: _corpus:phase:c-ni:cementite-d011  
_tdb: _tdb:NiC-06Hal.tdb:CEMENTITE_D011, tdb:NiC-22Oik.tdb:CEMENTITE_D011, tdb:NiC-87Gab-LB.tdb:CEMENTITE_D011, tdb:NiC-92Lee.tdb:CEMENTITE_D011  


### TDB models of CEMENTITE_D011 (4): PHASE and CONSTITUENT statements as written

[NiC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-06Hal.tdb): CEMENTITE_D011, type code %, sha256 `9c685cddb0304c2f…`

~~~~text
55: PHASE CEMENTITE_D011 % 2 3 1 !
56: CONST CEMENTITE_D011 : NI : C : !
~~~~

[NiC-22Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-22Oik.tdb): CEMENTITE_D011, type code %, sha256 `10d4397973f84604…`

~~~~text
53: PHASE CEMENTITE_D011 % 2 3 1 !
54: CONST CEMENTITE_D011 : NI : C : !
~~~~

[NiC-87Gab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-87Gab-LB.tdb): CEMENTITE_D011, type code %, sha256 `c412cb38ff96497c…`

~~~~text
59: PHASE CEMENTITE_D011 % 2 3 1 !
60: CONST CEMENTITE_D011 : NI : C : !
~~~~

[NiC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-92Lee.tdb): CEMENTITE_D011, type code %, sha256 `d316a2888dd883af…`

~~~~text
52: PHASE CEMENTITE_D011 % 2 3 1 !
53: CONST CEMENTITE_D011 : NI : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00995-0](https://doi.org/10.1007/s11669-022-00995-0) Katsunari Oikawa, Nobufumi Ueshima, Experimental Investigation and Thermodynamic Assessment of Ni–B and Ni–B–C Systems, J. Phase Equilib. Diffus. 43, 814-826 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90039-3](https://doi.org/10.1016/0364-5916%2887%2990039-3) Armand Gabriel, Per Gustafson, Ibrahim Ansara, A thermodynamic evaluation of the C-Fe-Ni system, Calphad 11, 203-218 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_

## FCC_A1 (C–Ni)

- Id: `phase:c-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2974.54 K, x(C) 0–0.02743
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ni:fcc-a1)

Names (5): _corpus: _corpus:phase:c-ni:fcc-a1  
_tdb: _tdb:NiC-06Hal.tdb:FCC_A1, tdb:NiC-22Oik.tdb:FCC_A1, tdb:NiC-87Gab-LB.tdb:FCC_A1, tdb:NiC-92Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[NiC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-06Hal.tdb): FCC_A1, type code %A, sha256 `9c685cddb0304c2f…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NI : C VA% : !
~~~~

[NiC-22Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-22Oik.tdb): FCC_A1, type code %A, sha256 `10d4397973f84604…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI : C VA% : !
~~~~

[NiC-87Gab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-87Gab-LB.tdb): FCC_A1, type code %A, sha256 `c412cb38ff96497c…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : NI : C VA% : !
~~~~

[NiC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-92Lee.tdb): FCC_A1, type code %A, sha256 `d316a2888dd883af…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NI : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00995-0](https://doi.org/10.1007/s11669-022-00995-0) Katsunari Oikawa, Nobufumi Ueshima, Experimental Investigation and Thermodynamic Assessment of Ni–B and Ni–B–C Systems, J. Phase Equilib. Diffus. 43, 814-826 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90039-3](https://doi.org/10.1016/0364-5916%2887%2990039-3) Armand Gabriel, Per Gustafson, Ibrahim Ansara, A thermodynamic evaluation of the C-Fe-Ni system, Calphad 11, 203-218 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_

## HCP_A3 (C–Ni)

- Id: `phase:c-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ni:hcp-a3)

Names (5): _corpus: _corpus:phase:c-ni:hcp-a3  
_tdb: _tdb:NiC-06Hal.tdb:HCP_A3, tdb:NiC-22Oik.tdb:HCP_A3, tdb:NiC-87Gab-LB.tdb:HCP_A3, tdb:NiC-92Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[NiC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-06Hal.tdb): HCP_A3, type code %A, sha256 `9c685cddb0304c2f…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NI : C VA% : !
~~~~

[NiC-22Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-22Oik.tdb): HCP_A3, type code %A, sha256 `10d4397973f84604…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI : C VA% : !
~~~~

[NiC-87Gab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-87Gab-LB.tdb): HCP_A3, type code %A, sha256 `c412cb38ff96497c…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : NI : C VA% : !
~~~~

[NiC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-92Lee.tdb): HCP_A3, type code %A, sha256 `d316a2888dd883af…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NI : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00995-0](https://doi.org/10.1007/s11669-022-00995-0) Katsunari Oikawa, Nobufumi Ueshima, Experimental Investigation and Thermodynamic Assessment of Ni–B and Ni–B–C Systems, J. Phase Equilib. Diffus. 43, 814-826 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90039-3](https://doi.org/10.1016/0364-5916%2887%2990039-3) Armand Gabriel, Per Gustafson, Ibrahim Ansara, A thermodynamic evaluation of the C-Fe-Ni system, Calphad 11, 203-218 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_

## LIQUID (C–Ni)

- Id: `phase:c-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1597.57–4000 K, x(C) 0–0.55948
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ni:liquid)

Names (5): _corpus: _corpus:phase:c-ni:liquid  
_tdb: _tdb:NiC-06Hal.tdb:LIQUID, tdb:NiC-22Oik.tdb:LIQUID, tdb:NiC-87Gab-LB.tdb:LIQUID, tdb:NiC-92Lee.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[NiC-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-06Hal.tdb): LIQUID, type code %, sha256 `9c685cddb0304c2f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C NI : !
~~~~

[NiC-22Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-22Oik.tdb): LIQUID, type code %, sha256 `10d4397973f84604…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : C NI : !
~~~~

[NiC-87Gab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-87Gab-LB.tdb): LIQUID, type code %, sha256 `c412cb38ff96497c…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : C NI : !
~~~~

[NiC-92Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NiC-92Lee.tdb): LIQUID, type code %, sha256 `d316a2888dd883af…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : C NI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00995-0](https://doi.org/10.1007/s11669-022-00995-0) Katsunari Oikawa, Nobufumi Ueshima, Experimental Investigation and Thermodynamic Assessment of Ni–B and Ni–B–C Systems, J. Phase Equilib. Diffus. 43, 814-826 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(87)90039-3](https://doi.org/10.1016/0364-5916%2887%2990039-3) Armand Gabriel, Per Gustafson, Ibrahim Ansara, A thermodynamic evaluation of the C-Fe-Ni system, Calphad 11, 203-218 (1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
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
