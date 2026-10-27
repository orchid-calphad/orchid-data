# N–Ti phases

> N–Ti system: 10 phases (tier A 3, tier C 1, liquid 1, gas 1, needs_review 3, interstitial_fcc_a1_compound 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-TI.html · Markdown: https://data.orchid-project.org/phases/pages/N-TI.md

10 phases (tier A 3, tier C 1, liquid 1, gas 1, needs_review 3, interstitial_fcc_a1_compound 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-TI) · [full JSON](https://data.orchid-project.org/phases/systems/N-TI.json) · [N–Ti system page](https://data.orchid-project.org/systems/N-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–Ti system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-n-ti-bcc-a2); _phase:n-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 1149.79–2294.45 K, x(N) 0–0.10059 | 0 | 6 |
| [FCC_7SL](#phase-n-ti-fcc-7sl); _phase:n-ti:fcc-7sl_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(N) 0.29898–0.5 | 0 | 2 |
| [FCC_A1](#phase-n-ti-fcc-a1); _phase:n-ti:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(N) 0.25211–0.5 | 0 | 4 |
| [HCP_A3](#phase-n-ti-hcp-a3); _phase:n-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2500 K, x(N) 0–0.27537 | 0 | 6 |
| [LIQUID](#phase-n-ti-liquid); _phase:n-ti:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1774.79–2500 K, x(N) 0–0.08388 | 1 | 6 |
| [N2GAS](#phase-n-ti-n2gas); _phase:n-ti:n2gas_ | gas | gas | stable in 6 of 6 calculated diagram(s): 300–2500 K, x(N) 1–1 | 0 | 6 |
| [TI2N_C4](#phase-n-ti-ti2n-c4); _phase:n-ti:ti2n-c4_ | TiO2 · C4 · tP6 · P4_2/mnm (136) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1863.72 K, x(N) 0.33333–0.33333 | 0 | 6 |
| [TI3N2](#phase-n-ti-ti3n2); _phase:n-ti:ti3n2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1336.19–1376.83 K, x(N) 0.29–0.29 | 4 | 1 |
| [TI4N3](#phase-n-ti-ti4n3); _phase:n-ti:ti4n3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1348.48–1551.12 K, x(N) 0.315–0.315 | 3 | 1 |
| [TI5N3](#phase-n-ti-ti5n3); _phase:n-ti:ti5n3_ | Ti5N3 · tI16 · I4_1/amd (141) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–906.16 K, x(N) 0.375–0.375 | 0 | 1 |

## BCC_A2 (N–Ti)

- Id: `phase:n-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1149.79–2294.45 K, x(N) 0–0.10059
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:bcc-a2)

Names (7): _corpus: _corpus:phase:n-ti:bcc-a2  
_tdb: _tdb:TiN-08And-A.tdb:BCC_A2, tdb:TiN-08And-B.tdb:BCC_A2, tdb:TiN-90Oht.tdb:BCC_A2, tdb:TiN-91Vah.tdb:BCC_A2, tdb:TiN-96Jon-LB.tdb:BCC_A2, tdb:TiN-96Zen.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[TiN-08And-A.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-A.tdb): BCC_A2, type code %B, sha256 `677b1d1dc9679528…`

~~~~text
55: PHASE BCC_A2 %B 2 1 3 !
56: CONST BCC_A2 : TI% : N VA% : !
~~~~

[TiN-08And-B.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-B.tdb): BCC_A2, type code %B, sha256 `a4fad23290e68306…`

~~~~text
55: PHASE BCC_A2 %B 2 1 3 !
56: CONST BCC_A2 : TI% : N VA% : !
~~~~

[TiN-90Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-90Oht.tdb): BCC_A2, type code %B, sha256 `0e8332731a96995e…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : TI% : N VA% : !
~~~~

[TiN-91Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-91Vah.tdb): BCC_A2, type code %B, sha256 `181cd051fbfbd3a1…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : TI% : N VA% : !
~~~~

[TiN-96Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Jon-LB.tdb): BCC_A2, type code %B, sha256 `6ad25e1ff3582dfd…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : TI% : N VA% : !
~~~~

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): BCC_A2, type code %B, sha256 `fdb82ad3502481f6…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : TI% : N VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0040-6031(91)80371-O](https://doi.org/10.1016/0040-6031%2891%2980371-O) C. Vahlas, B. Drouin Ladouce, P.Y. Chevalier, C. Bernard, L. Vandenbulcke, Thermochim. Acta, 180, 23-37(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90029-Y](https://doi.org/10.1016/0364-5916%2890%2990029-Y) H. Ohtani, M. Hillert, Calphad, 14, 289-306(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.007](https://doi.org/10.1016/j.calphad.2008.04.007) D.A. Andersson, P.A. Korzhavyi, B. Johansson, First-principles based calculation of binary and multicomponent phase diagrams for titanium carbonitride, Calphad 32, 543-565 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870903](https://doi.org/10.1515/ijmr-1996-870903) S. Jonsson, Z. Metallkd., 87, 691-702(1996).  
_assessment that models this phase_

## FCC_7SL (N–Ti)

- Id: `phase:n-ti:fcc-7sl`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:7SL
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(N) 0.29898–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:fcc-7sl)

Names (3): _corpus: _corpus:phase:n-ti:fcc-7sl  
_tdb: _tdb:TiN-08And-A.tdb:FCC_7SL, tdb:TiN-08And-B.tdb:FCC_7SL  


### TDB models of FCC_7SL (2): PHASE and CONSTITUENT statements as written

[TiN-08And-A.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-A.tdb): FCC_7SL, type code %A, sha256 `677b1d1dc9679528…`

~~~~text
50: PHASE FCC_7SL %A 7 6 1 1 1 1 1 1 !
51: CONST FCC_7SL : TI : N VA : N VA : N VA : N VA : N VA : N VA : !
~~~~

[TiN-08And-B.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-B.tdb): FCC_7SL, type code %A, sha256 `a4fad23290e68306…`

~~~~text
50: PHASE FCC_7SL %A 7 6 1 1 1 1 1 1 !
51: CONST FCC_7SL : TI : N VA : N VA : N VA : N VA : N VA : N VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.04.007](https://doi.org/10.1016/j.calphad.2008.04.007) D.A. Andersson, P.A. Korzhavyi, B. Johansson, First-principles based calculation of binary and multicomponent phase diagrams for titanium carbonitride, Calphad 32, 543-565 (2008).  
_assessment that models this phase_

## FCC_A1 (N–Ti)

- Id: `phase:n-ti:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(N) 0.25211–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:fcc-a1)

Names (5): _corpus: _corpus:phase:n-ti:fcc-a1  
_tdb: _tdb:TiN-90Oht.tdb:FCC_A1, tdb:TiN-91Vah.tdb:FCC_A1, tdb:TiN-96Jon-LB.tdb:FCC_A1, tdb:TiN-96Zen.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[TiN-90Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-90Oht.tdb): FCC_A1, type code %A, sha256 `0e8332731a96995e…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : TI : N VA% : !
~~~~

[TiN-91Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-91Vah.tdb): FCC_A1, type code %A, sha256 `181cd051fbfbd3a1…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : TI : N VA% : !
~~~~

[TiN-96Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Jon-LB.tdb): FCC_A1, type code %A, sha256 `6ad25e1ff3582dfd…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : TI : N VA% : !
~~~~

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): FCC_A1, type code %A, sha256 `fdb82ad3502481f6…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : TI : N VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0040-6031(91)80371-O](https://doi.org/10.1016/0040-6031%2891%2980371-O) C. Vahlas, B. Drouin Ladouce, P.Y. Chevalier, C. Bernard, L. Vandenbulcke, Thermochim. Acta, 180, 23-37(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90029-Y](https://doi.org/10.1016/0364-5916%2890%2990029-Y) H. Ohtani, M. Hillert, Calphad, 14, 289-306(1990).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870903](https://doi.org/10.1515/ijmr-1996-870903) S. Jonsson, Z. Metallkd., 87, 691-702(1996).  
_assessment that models this phase_

## HCP_A3 (N–Ti)

- Id: `phase:n-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2500 K, x(N) 0–0.27537
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:hcp-a3)

Names (7): _corpus: _corpus:phase:n-ti:hcp-a3  
_tdb: _tdb:TiN-08And-A.tdb:HCP_A3, tdb:TiN-08And-B.tdb:HCP_A3, tdb:TiN-90Oht.tdb:HCP_A3, tdb:TiN-91Vah.tdb:HCP_A3, tdb:TiN-96Jon-LB.tdb:HCP_A3, tdb:TiN-96Zen.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[TiN-08And-A.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-A.tdb): HCP_A3, type code %A, sha256 `677b1d1dc9679528…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : TI% : N VA% : !
~~~~

[TiN-08And-B.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-B.tdb): HCP_A3, type code %A, sha256 `a4fad23290e68306…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : TI% : N VA% : !
~~~~

[TiN-90Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-90Oht.tdb): HCP_A3, type code %A, sha256 `0e8332731a96995e…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : TI% : N VA% : !
~~~~

[TiN-91Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-91Vah.tdb): HCP_A3, type code %A, sha256 `181cd051fbfbd3a1…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : TI% : N VA% : !
~~~~

[TiN-96Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Jon-LB.tdb): HCP_A3, type code %A, sha256 `6ad25e1ff3582dfd…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : TI% : N VA% : !
~~~~

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): HCP_A3, type code %A, sha256 `fdb82ad3502481f6…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : TI% : N VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0040-6031(91)80371-O](https://doi.org/10.1016/0040-6031%2891%2980371-O) C. Vahlas, B. Drouin Ladouce, P.Y. Chevalier, C. Bernard, L. Vandenbulcke, Thermochim. Acta, 180, 23-37(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90029-Y](https://doi.org/10.1016/0364-5916%2890%2990029-Y) H. Ohtani, M. Hillert, Calphad, 14, 289-306(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.007](https://doi.org/10.1016/j.calphad.2008.04.007) D.A. Andersson, P.A. Korzhavyi, B. Johansson, First-principles based calculation of binary and multicomponent phase diagrams for titanium carbonitride, Calphad 32, 543-565 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870903](https://doi.org/10.1515/ijmr-1996-870903) S. Jonsson, Z. Metallkd., 87, 691-702(1996).  
_assessment that models this phase_

## LIQUID (N–Ti)

- Id: `phase:n-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1774.79–2500 K, x(N) 0–0.08388
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:liquid)

Names (8): _corpus: _corpus:phase:n-ti:liquid  
_paper: _paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:TiN-08And-A.tdb:LIQUID, tdb:TiN-08And-B.tdb:LIQUID, tdb:TiN-90Oht.tdb:LIQUID, tdb:TiN-91Vah.tdb:LIQUID, tdb:TiN-96Jon-LB.tdb:LIQUID, tdb:TiN-96Zen.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[TiN-08And-A.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-A.tdb): LIQUID, type code %, sha256 `677b1d1dc9679528…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : N TI : !
~~~~

[TiN-08And-B.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-B.tdb): LIQUID, type code %, sha256 `a4fad23290e68306…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : N TI : !
~~~~

[TiN-90Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-90Oht.tdb): LIQUID, type code %, sha256 `0e8332731a96995e…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : N TI : !
~~~~

[TiN-91Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-91Vah.tdb): LIQUID, type code %, sha256 `181cd051fbfbd3a1…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : N TI : !
~~~~

[TiN-96Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Jon-LB.tdb): LIQUID, type code %, sha256 `6ad25e1ff3582dfd…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : N TI : !
~~~~

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): LIQUID, type code %, sha256 `fdb82ad3502481f6…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : N TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0040-6031(91)80371-O](https://doi.org/10.1016/0040-6031%2891%2980371-O) C. Vahlas, B. Drouin Ladouce, P.Y. Chevalier, C. Bernard, L. Vandenbulcke, Thermochim. Acta, 180, 23-37(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90029-Y](https://doi.org/10.1016/0364-5916%2890%2990029-Y) H. Ohtani, M. Hillert, Calphad, 14, 289-306(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.007](https://doi.org/10.1016/j.calphad.2008.04.007) D.A. Andersson, P.A. Korzhavyi, B. Johansson, First-principles based calculation of binary and multicomponent phase diagrams for titanium carbonitride, Calphad 32, 543-565 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870903](https://doi.org/10.1515/ijmr-1996-870903) S. Jonsson, Z. Metallkd., 87, 691-702(1996).  
_assessment that models this phase_

## N2GAS (N–Ti)

- Id: `phase:n-ti:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2500 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:n2gas)

Names (7): _corpus: _corpus:phase:n-ti:n2gas  
_tdb: _tdb:TiN-08And-A.tdb:N2GAS, tdb:TiN-08And-B.tdb:N2GAS, tdb:TiN-90Oht.tdb:N2GAS, tdb:TiN-91Vah.tdb:N2GAS, tdb:TiN-96Jon-LB.tdb:N2GAS, tdb:TiN-96Zen.tdb:N2GAS  


### TDB models of N2GAS (6): PHASE and CONSTITUENT statements as written

[TiN-08And-A.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-A.tdb): N2GAS, type code %, sha256 `677b1d1dc9679528…`

~~~~text
68: PHASE N2GAS % 1 1 !
69: CONST N2GAS : N2 : !
~~~~

[TiN-08And-B.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-B.tdb): N2GAS, type code %, sha256 `a4fad23290e68306…`

~~~~text
68: PHASE N2GAS % 1 1 !
69: CONST N2GAS : N2 : !
~~~~

[TiN-90Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-90Oht.tdb): N2GAS, type code %, sha256 `0e8332731a96995e…`

~~~~text
51: PHASE N2GAS % 1 1 !
52: CONST N2GAS : N2 : !
~~~~

[TiN-91Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-91Vah.tdb): N2GAS, type code %, sha256 `181cd051fbfbd3a1…`

~~~~text
56: PHASE N2GAS % 1 1 !
57: CONST N2GAS : N2 : !
~~~~

[TiN-96Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Jon-LB.tdb): N2GAS, type code %, sha256 `6ad25e1ff3582dfd…`

~~~~text
47: PHASE N2GAS % 1 1 !
48: CONST N2GAS : N2 : !
~~~~

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): N2GAS, type code %, sha256 `fdb82ad3502481f6…`

~~~~text
57: PHASE N2GAS % 1 1 !
58: CONST N2GAS : N2 : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0040-6031(91)80371-O](https://doi.org/10.1016/0040-6031%2891%2980371-O) C. Vahlas, B. Drouin Ladouce, P.Y. Chevalier, C. Bernard, L. Vandenbulcke, Thermochim. Acta, 180, 23-37(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90029-Y](https://doi.org/10.1016/0364-5916%2890%2990029-Y) H. Ohtani, M. Hillert, Calphad, 14, 289-306(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.007](https://doi.org/10.1016/j.calphad.2008.04.007) D.A. Andersson, P.A. Korzhavyi, B. Johansson, First-principles based calculation of binary and multicomponent phase diagrams for titanium carbonitride, Calphad 32, 543-565 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870903](https://doi.org/10.1515/ijmr-1996-870903) S. Jonsson, Z. Metallkd., 87, 691-702(1996).  
_assessment that models this phase_

## TI2N_C4 (N–Ti)

- Id: `phase:n-ti:ti2n-c4`; status `assigned`
- Structure: TiO2 · C4 · tP6 · P4_2/mnm (136); type `st:c4-tio2-tp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaamgo and oqmd-6327, space group 136
- Stoichiometry: N 0.3333, Ti 0.6667
- Stability: stable in 6 of 6 calculated diagram(s): 300–1863.72 K, x(N) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:ti2n-c4)

Names (9): _corpus: _corpus:phase:n-ti:ti2n-c4  
_mp: _mp:mp-aaaaamgo  
_oqmd: _oqmd:oqmd-6327  
_tdb: _tdb:TiN-08And-A.tdb:TI2N_C4, tdb:TiN-08And-B.tdb:TI2N_C4, tdb:TiN-90Oht.tdb:TI2N_C4, tdb:TiN-91Vah.tdb:TI2N_C4, tdb:TiN-96Jon-LB.tdb:TI2N_C4, tdb:TiN-96Zen.tdb:TI2N_C4  


### TDB models of TI2N_C4 (6): PHASE and CONSTITUENT statements as written

[TiN-08And-A.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-A.tdb): TI2N_C4, type code %, sha256 `677b1d1dc9679528…`

~~~~text
65: PHASE TI2N_C4 % 2 2 1 !
66: CONST TI2N_C4 : TI : N : !
~~~~

[TiN-08And-B.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-08And-B.tdb): TI2N_C4, type code %, sha256 `a4fad23290e68306…`

~~~~text
65: PHASE TI2N_C4 % 2 2 1 !
66: CONST TI2N_C4 : TI : N : !
~~~~

[TiN-90Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-90Oht.tdb): TI2N_C4, type code %, sha256 `0e8332731a96995e…`

~~~~text
48: PHASE TI2N_C4 % 2 2 1 !
49: CONST TI2N_C4 : TI : N : !
~~~~

[TiN-91Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-91Vah.tdb): TI2N_C4, type code %, sha256 `181cd051fbfbd3a1…`

~~~~text
48: PHASE TI2N_C4 % 2 2 1 !
49: CONST TI2N_C4 : TI : N : !
~~~~

[TiN-96Jon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Jon-LB.tdb): TI2N_C4, type code %, sha256 `6ad25e1ff3582dfd…`

~~~~text
44: PHASE TI2N_C4 % 2 2 1 !
45: CONST TI2N_C4 : TI : N : !
~~~~

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): TI2N_C4, type code %, sha256 `fdb82ad3502481f6…`

~~~~text
44: PHASE TI2N_C4 % 2 2 1 !
45: CONST TI2N_C4 : TI : N : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0040-6031(91)80371-O](https://doi.org/10.1016/0040-6031%2891%2980371-O) C. Vahlas, B. Drouin Ladouce, P.Y. Chevalier, C. Bernard, L. Vandenbulcke, Thermochim. Acta, 180, 23-37(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90029-Y](https://doi.org/10.1016/0364-5916%2890%2990029-Y) H. Ohtani, M. Hillert, Calphad, 14, 289-306(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.007](https://doi.org/10.1016/j.calphad.2008.04.007) D.A. Andersson, P.A. Korzhavyi, B. Johansson, First-principles based calculation of binary and multicomponent phase diagrams for titanium carbonitride, Calphad 32, 543-565 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870903](https://doi.org/10.1515/ijmr-1996-870903) S. Jonsson, Z. Metallkd., 87, 691-702(1996).  
_assessment that models this phase_

## TI3N2 (N–Ti)

- Id: `phase:n-ti:ti3n2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Ti3N2) — Hallstedt 2025 mmc2 row for TI3N2: Ti0.71N0.29
- Stoichiometry: N 0.2900, Ti 0.7100
- Stability: stable in 1 of 1 calculated diagram(s): 1336.19–1376.83 K, x(N) 0.29–0.29
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:ti3n2)

Names (3): _corpus: _corpus:phase:n-ti:ti3n2  
_paper: _paper:sha256-85fd53a1a176b694:Ti3N2  
_tdb: _tdb:TiN-96Zen.tdb:TI3N2  


### TDB models of TI3N2 (1): PHASE and CONSTITUENT statements as written

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): TI3N2, type code %, sha256 `fdb82ad3502481f6…`

~~~~text
49: PHASE TI3N2 % 2 0.71 0.29 !
50: CONST TI3N2 : TI : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_

## TI4N3 (N–Ti)

- Id: `phase:n-ti:ti4n3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Ti4N3) — Hallstedt 2025 mmc2 row for TI4N3: Ti0.685N0.315
- Stoichiometry: N 0.3150, Ti 0.6850
- Stability: stable in 1 of 1 calculated diagram(s): 1348.48–1551.12 K, x(N) 0.315–0.315
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:ti4n3)

Names (3): _corpus: _corpus:phase:n-ti:ti4n3  
_paper: _paper:sha256-85fd53a1a176b694:Ti4N3  
_tdb: _tdb:TiN-96Zen.tdb:TI4N3  


### TDB models of TI4N3 (1): PHASE and CONSTITUENT statements as written

[TiN-96Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-96Zen.tdb): TI4N3, type code %, sha256 `fdb82ad3502481f6…`

~~~~text
54: PHASE TI4N3 % 2 0.685 0.315 !
55: CONST TI4N3 : TI : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1996-870706](https://doi.org/10.1515/ijmr-1996-870706) K. Zeng, R. Schmid-Fetzer, Z. Metallkd., 87, 540-54(1996).  
_assessment that models this phase_

## TI5N3 (N–Ti)

- Id: `phase:n-ti:ti5n3`; status `assigned`
- Structure: Ti5N3 · tI16 · I4_1/amd (141); type `st:ti5n3-ti16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: N 0.3750, Ti 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–906.16 K, x(N) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ti:ti5n3)

Names (2): _corpus: _corpus:phase:n-ti:ti5n3  
_tdb: _tdb:TiN-91Vah.tdb:TI5N3  


### TDB models of TI5N3 (1): PHASE and CONSTITUENT statements as written

[TiN-91Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/TiN-91Vah.tdb): TI5N3, type code %, sha256 `181cd051fbfbd3a1…`

~~~~text
53: PHASE TI5N3 % 2 5 3 !
54: CONST TI5N3 : TI : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0040-6031(91)80371-O](https://doi.org/10.1016/0040-6031%2891%2980371-O) C. Vahlas, B. Drouin Ladouce, P.Y. Chevalier, C. Bernard, L. Vandenbulcke, Thermochim. Acta, 180, 23-37(1991).  
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
