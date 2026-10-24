# H–Ti phases

> H–Ti system: 7 phases (tier A 3, liquid 1, gas 1, needs_review 1, interstitial_fcc_a1_compound 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-TI.html · Markdown: https://data.orchid-project.org/phases/pages/H-TI.md

7 phases (tier A 3, liquid 1, gas 1, needs_review 1, interstitial_fcc_a1_compound 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-TI) · [full JSON](https://data.orchid-project.org/phases/systems/H-TI.json) · [H–Ti system page](https://data.orchid-project.org/systems/H-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Ti system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-ti-bcc-a2); _phase:h-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 561.33–2259.99 K, x(H) 0–0.52817 | 8 | 5 |
| [FCC_A1](#phase-h-ti-fcc-a1); _phase:h-ti:fcc-a1_ | CaF2 · C1 · cF12 · Fm-3m (225) | assigned | stable in 5 of 5 calculated diagram(s): 300–948.24 K, x(H) 0.50248–0.66667 | 0 | 5 |
| [GAS](#phase-h-ti-gas); _phase:h-ti:gas_ | gas | gas | stable in 5 of 5 calculated diagram(s): 300–2500 K, x(H) 1–1 | 0 | 5 |
| [HCP_A3](#phase-h-ti-hcp-a3); _phase:h-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2259.99 K, x(H) 0–0.10002 | 6 | 5 |
| [LIQUID](#phase-h-ti-liquid); _phase:h-ti:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1486–2500 K, x(H) 0–0.09203 | 5 | 5 |
| [TIH_B17](#phase-h-ti-tih-b17); _phase:h-ti:tih-b17_ | PtS · B17 · tP4 · P4_2/mmc (131) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–440.98 K, x(H) 0.5–0.5 | 0 | 1 |
| [TIH2_L2B](#phase-h-ti-tih2-l2b); _phase:h-ti:tih2-l2b_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–333.32 K, x(H) 0.66667–0.66667 | 0 | 1 |

## BCC_A2 (H–Ti)

- Id: `phase:h-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 561.33–2259.99 K, x(H) 0–0.52817
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ti:bcc-a2)

Names (7): _corpus: _corpus:phase:h-ti:bcc-a2  
_paper: _paper:10.1016/j.calphad.2010.07.001:β  
_tdb: _tdb:TiH-00Koe.tdb:BCC_A2, tdb:TiH-07Uki.tdb:BCC_A2, tdb:TiH-08Qiu.tdb:BCC_A2, tdb:TiH-10Wan.tdb:BCC_A2, tdb:TiH-87Kiv.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[TiH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-00Koe.tdb): BCC_A2, type code %B, sha256 `f6ece47290a9e8df…`

~~~~text
36: PHASE BCC_A2 %B 2 1 1.5 !
37: CONST BCC_A2 : TI : H VA% : !
~~~~

[TiH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-07Uki.tdb): BCC_A2, type code %B, sha256 `9f0b5aca2ec52585…`

~~~~text
35: PHASE BCC_A2 %B 2 1 6 !
36: CONST BCC_A2 : TI : H VA% : !
~~~~

[TiH-08Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-08Qiu.tdb): BCC_A2, type code %B, sha256 `dc2ff19793b3ae2f…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : TI : H VA% : !
~~~~

[TiH-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-10Wan.tdb): BCC_A2, type code %B, sha256 `4d284f0864b71b93…`

~~~~text
39: PHASE BCC_A2 %B 2 1 1.5 !
40: CONST BCC_A2 : TI : H VA% : !
~~~~

[TiH-87Kiv.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-87Kiv.tdb): BCC_A2, type code %B, sha256 `0ea0e065649731f5…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : TI : H VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2010.07.001](https://doi.org/10.1016/j.calphad.2010.07.001) Kun Wang, Xiangcheng Kong, Junlin Du, Chonghe Li, Zhilin Li, Zhu Wu, Thermodynamic description of the Ti–H system, Calphad 34, 317-323 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90014-9](https://doi.org/10.1016/0364-5916%2887%2990014-9) J.K. Kivilahti, J.M. Miettinen, A thermodynamic analysis of the ti-h system, Calphad 11, 187-199 (1987).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2008.08.005](https://doi.org/10.1016/j.calphad.2008.08.005) Caian Qiu, Susanne M. Opalka, Ole M. Løvvik, Gregory B. Olson, Thermodynamic modeling of the Na–Al–Ti–H system and Ti dissolution in sodium alanates, Calphad 32, 624-636 (2008).  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## FCC_A1 (H–Ti)

- Id: `phase:h-ti:fcc-a1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–948.24 K, x(H) 0.50248–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ti:fcc-a1)

Names (6): _corpus: _corpus:phase:h-ti:fcc-a1  
_tdb: _tdb:TiH-00Koe.tdb:FCC_A1, tdb:TiH-07Uki.tdb:FCC_A1, tdb:TiH-08Qiu.tdb:FCC_A1, tdb:TiH-10Wan.tdb:FCC_A1, tdb:TiH-87Kiv.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[TiH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-00Koe.tdb): FCC_A1, type code %A, sha256 `f6ece47290a9e8df…`

~~~~text
31: PHASE FCC_A1 %A 2 1 2 !
32: CONST FCC_A1 : TI : H% VA : !
~~~~

[TiH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-07Uki.tdb): FCC_A1, type code %A, sha256 `9f0b5aca2ec52585…`

~~~~text
30: PHASE FCC_A1 %A 2 1 2 !
31: CONST FCC_A1 : TI : H% VA : !
~~~~

[TiH-08Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-08Qiu.tdb): FCC_A1, type code %A, sha256 `dc2ff19793b3ae2f…`

~~~~text
32: PHASE FCC_A1 %A 2 1 2 !
33: CONST FCC_A1 : TI : H% VA : !
~~~~

[TiH-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-10Wan.tdb): FCC_A1, type code %A, sha256 `4d284f0864b71b93…`

~~~~text
34: PHASE FCC_A1 %A 2 1 2 !
35: CONST FCC_A1 : TI : H% VA : !
~~~~

[TiH-87Kiv.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-87Kiv.tdb): FCC_A1, type code %A, sha256 `0ea0e065649731f5…`

~~~~text
34: PHASE FCC_A1 %A 2 1 2 !
35: CONST FCC_A1 : TI : H% VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(87)90014-9](https://doi.org/10.1016/0364-5916%2887%2990014-9) J.K. Kivilahti, J.M. Miettinen, A thermodynamic analysis of the ti-h system, Calphad 11, 187-199 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.08.005](https://doi.org/10.1016/j.calphad.2008.08.005) Caian Qiu, Susanne M. Opalka, Ole M. Løvvik, Gregory B. Olson, Thermodynamic modeling of the Na–Al–Ti–H system and Ti dissolution in sodium alanates, Calphad 32, 624-636 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.07.001](https://doi.org/10.1016/j.calphad.2010.07.001) Kun Wang, Xiangcheng Kong, Junlin Du, Chonghe Li, Zhilin Li, Zhu Wu, Thermodynamic description of the Ti–H system, Calphad 34, 317-323 (2010).  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## GAS (H–Ti)

- Id: `phase:h-ti:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2500 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ti:gas)

Names (6): _corpus: _corpus:phase:h-ti:gas  
_tdb: _tdb:TiH-00Koe.tdb:GAS, tdb:TiH-07Uki.tdb:GAS, tdb:TiH-08Qiu.tdb:GAS, tdb:TiH-10Wan.tdb:GAS, tdb:TiH-87Kiv.tdb:GAS  


### TDB models of GAS (5): PHASE and CONSTITUENT statements as written

[TiH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-00Koe.tdb): GAS, type code %, sha256 `f6ece47290a9e8df…`

~~~~text
44: PHASE GAS:G % 1 1 !
45: CONST GAS:G : H H2 : !
~~~~

[TiH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-07Uki.tdb): GAS, type code %, sha256 `9f0b5aca2ec52585…`

~~~~text
53: PHASE GAS:G % 1 1 !
54: CONST GAS:G : H H2 : !
~~~~

[TiH-08Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-08Qiu.tdb): GAS, type code %, sha256 `dc2ff19793b3ae2f…`

~~~~text
45: PHASE GAS:G % 1 1 !
46: CONST GAS:G : H H2 : !
~~~~

[TiH-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-10Wan.tdb): GAS, type code %, sha256 `4d284f0864b71b93…`

~~~~text
47: PHASE GAS:G % 1 1 !
48: CONST GAS:G : H H2 : !
~~~~

[TiH-87Kiv.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-87Kiv.tdb): GAS, type code %, sha256 `0ea0e065649731f5…`

~~~~text
47: PHASE GAS:G % 1 1 !
48: CONST GAS:G : H H2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(87)90014-9](https://doi.org/10.1016/0364-5916%2887%2990014-9) J.K. Kivilahti, J.M. Miettinen, A thermodynamic analysis of the ti-h system, Calphad 11, 187-199 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.08.005](https://doi.org/10.1016/j.calphad.2008.08.005) Caian Qiu, Susanne M. Opalka, Ole M. Løvvik, Gregory B. Olson, Thermodynamic modeling of the Na–Al–Ti–H system and Ti dissolution in sodium alanates, Calphad 32, 624-636 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.07.001](https://doi.org/10.1016/j.calphad.2010.07.001) Kun Wang, Xiangcheng Kong, Junlin Du, Chonghe Li, Zhilin Li, Zhu Wu, Thermodynamic description of the Ti–H system, Calphad 34, 317-323 (2010).  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## HCP_A3 (H–Ti)

- Id: `phase:h-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2259.99 K, x(H) 0–0.10002
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ti:hcp-a3)

Names (7): _corpus: _corpus:phase:h-ti:hcp-a3  
_paper: _paper:10.1016/j.calphad.2010.07.001:α  
_tdb: _tdb:TiH-00Koe.tdb:HCP_A3, tdb:TiH-07Uki.tdb:HCP_A3, tdb:TiH-08Qiu.tdb:HCP_A3, tdb:TiH-10Wan.tdb:HCP_A3, tdb:TiH-87Kiv.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[TiH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-00Koe.tdb): HCP_A3, type code %A, sha256 `f6ece47290a9e8df…`

~~~~text
41: PHASE HCP_A3 %A 2 1 1 !
42: CONST HCP_A3 : TI : H VA% : !
~~~~

[TiH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-07Uki.tdb): HCP_A3, type code %A, sha256 `9f0b5aca2ec52585…`

~~~~text
40: PHASE HCP_A3 %A 2 1 2 !
41: CONST HCP_A3 : TI : H VA% : !
~~~~

[TiH-08Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-08Qiu.tdb): HCP_A3, type code %A, sha256 `dc2ff19793b3ae2f…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : TI : H VA% : !
~~~~

[TiH-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-10Wan.tdb): HCP_A3, type code %A, sha256 `4d284f0864b71b93…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : TI : H VA% : !
~~~~

[TiH-87Kiv.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-87Kiv.tdb): HCP_A3, type code %A, sha256 `0ea0e065649731f5…`

~~~~text
44: PHASE HCP_A3 %A 2 1 1 !
45: CONST HCP_A3 : TI : H VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2010.07.001](https://doi.org/10.1016/j.calphad.2010.07.001) Kun Wang, Xiangcheng Kong, Junlin Du, Chonghe Li, Zhilin Li, Zhu Wu, Thermodynamic description of the Ti–H system, Calphad 34, 317-323 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90014-9](https://doi.org/10.1016/0364-5916%2887%2990014-9) J.K. Kivilahti, J.M. Miettinen, A thermodynamic analysis of the ti-h system, Calphad 11, 187-199 (1987).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2008.08.005](https://doi.org/10.1016/j.calphad.2008.08.005) Caian Qiu, Susanne M. Opalka, Ole M. Løvvik, Gregory B. Olson, Thermodynamic modeling of the Na–Al–Ti–H system and Ti dissolution in sodium alanates, Calphad 32, 624-636 (2008).  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## LIQUID (H–Ti)

- Id: `phase:h-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1486–2500 K, x(H) 0–0.09203
- Literature: 5 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ti:liquid)

Names (8): _corpus: _corpus:phase:h-ti:liquid  
_paper: _paper:10.1016/j.calphad.2010.07.001:L1, paper:10.1016/j.calphad.2010.07.001:liquid  
_tdb: _tdb:TiH-00Koe.tdb:LIQUID, tdb:TiH-07Uki.tdb:LIQUID, tdb:TiH-08Qiu.tdb:LIQUID, tdb:TiH-10Wan.tdb:LIQUID, tdb:TiH-87Kiv.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[TiH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-00Koe.tdb): LIQUID, type code %, sha256 `f6ece47290a9e8df…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : TI : !
~~~~

[TiH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-07Uki.tdb): LIQUID, type code %, sha256 `9f0b5aca2ec52585…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : TI : !
~~~~

[TiH-08Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-08Qiu.tdb): LIQUID, type code %, sha256 `dc2ff19793b3ae2f…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : H TI : !
~~~~

[TiH-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-10Wan.tdb): LIQUID, type code %, sha256 `4d284f0864b71b93…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : H TI TIH2 : !
~~~~

[TiH-87Kiv.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-87Kiv.tdb): LIQUID, type code %, sha256 `0ea0e065649731f5…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2010.07.001](https://doi.org/10.1016/j.calphad.2010.07.001) Kun Wang, Xiangcheng Kong, Junlin Du, Chonghe Li, Zhilin Li, Zhu Wu, Thermodynamic description of the Ti–H system, Calphad 34, 317-323 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90014-9](https://doi.org/10.1016/0364-5916%2887%2990014-9) J.K. Kivilahti, J.M. Miettinen, A thermodynamic analysis of the ti-h system, Calphad 11, 187-199 (1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.08.005](https://doi.org/10.1016/j.calphad.2008.08.005) Caian Qiu, Susanne M. Opalka, Ole M. Løvvik, Gregory B. Olson, Thermodynamic modeling of the Na–Al–Ti–H system and Ti dissolution in sodium alanates, Calphad 32, 624-636 (2008).  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## TIH_B17 (H–Ti)

- Id: `phase:h-ti:tih-b17`; status `assigned`
- Structure: PtS · B17 · tP4 · P4_2/mmc (131); type `st:b17-pts-tp4`; tier A: standard phase name; confidence high
- Stoichiometry: H 0.5000, Ti 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–440.98 K, x(H) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ti:tih-b17)

Names (2): _corpus: _corpus:phase:h-ti:tih-b17  
_tdb: _tdb:TiH-07Uki.tdb:TIH_B17  


### TDB models of TIH_B17 (1): PHASE and CONSTITUENT statements as written

[TiH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-07Uki.tdb): TIH_B17, type code %, sha256 `9f0b5aca2ec52585…`

~~~~text
45: PHASE TIH_B17 % 2 1 1 !
46: CONST TIH_B17 : TI : H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## TIH2_L2B (H–Ti)

- Id: `phase:h-ti:tih2-l2b`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:L2B; no_structure_token
- Candidate (sgte_mmc2): ThH2 · L'2_b · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for TIH2_L2B: TiH2-epsilon
- Candidate (tdb_comment): ThH2 · tI6 · I4/mmm — TiH-07Uki.tdb: 'Prototype ThH2 (tI6, I4/mmm), epsilon'
- Stability: stable in 1 of 1 calculated diagram(s): 300–333.32 K, x(H) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ti:tih2-l2b)

Names (2): _corpus: _corpus:phase:h-ti:tih2-l2b  
_tdb: _tdb:TiH-07Uki.tdb:TIH2_L2B  


### TDB models of TIH2_L2B (1): PHASE and CONSTITUENT statements as written

[TiH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/TiH-07Uki.tdb): TIH2_L2B, type code %, sha256 `9f0b5aca2ec52585…`

~~~~text
50: PHASE TIH2_L2B % 2 1 2 !
51: CONST TIH2_L2B : TI : H% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
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
