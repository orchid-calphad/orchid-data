# Ge–Nb phases

> Ge–Nb system: 9 phases (tier A 8, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-NB.html · Markdown: https://data.orchid-project.org/phases/pages/GE-NB.md

9 phases (tier A 8, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-NB) · [full JSON](https://data.orchid-project.org/phases/systems/GE-NB.json) · [Ge–Nb system page](https://data.orchid-project.org/systems/GE-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Nb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-nb-a4-diamond); _phase:ge-nb:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Nb) 0–0.00315 | 4 | 2 |
| [BCC_A2](#phase-ge-nb-bcc-a2); _phase:ge-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(Nb) 0.88885–1 | 5 | 2 |
| [FCC_A1](#phase-ge-nb-fcc-a1); _phase:ge-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GE2NB_C40](#phase-ge-nb-ge2nb-c40); _phase:ge-nb:ge2nb-c40_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1951.79 K, x(Nb) 0.3283–0.34016 | 13 | 2 |
| [GE2NB3_D88](#phase-ge-nb-ge2nb3-d88); _phase:ge-nb:ge2nb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2291.56 K, x(Nb) 0.56993–0.58988 | 4 | 1 |
| [GE3NB5_D8M](#phase-ge-nb-ge3nb5-d8m); _phase:ge-nb:ge3nb5-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2453.08 K, x(Nb) 0.60395–0.63035 | 15 | 2 |
| [GENB3_A15](#phase-ge-nb-genb3-a15); _phase:ge-nb:genb3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2176.65 K, x(Nb) 0.76095–0.82046 | 10 | 2 |
| [HCP_A3](#phase-ge-nb-hcp-a3); _phase:ge-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ge-nb-liquid); _phase:ge-nb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1210.78–4000 K, x(Nb) 0–1 | 30 | 2 |

## DIAMOND_A4 (Ge–Nb)

- Id: `phase:ge-nb:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Nb) 0–0.00315
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:a4-diamond)

Names (4): _corpus: _corpus:phase:ge-nb:a4-diamond  
_paper: _paper:10.1016/j.jallcom.2010.12.005:Diamond-(Ge)  
_tdb: _tdb:GeNb-11Gen.tdb:DIAMOND_A4, tdb:GeNb-17Utt.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): DIAMOND_A4, type code %, sha256 `55314e2cadc330d9…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : GE% NB : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): DIAMOND_A4, type code %, sha256 `0c86fa883ab70ed8…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : GE% NB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_

## BCC_A2 (Ge–Nb)

- Id: `phase:ge-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(Nb) 0.88885–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:bcc-a2)

Names (4): _corpus: _corpus:phase:ge-nb:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2010.12.005:Bcc-(Nb)  
_tdb: _tdb:GeNb-11Gen.tdb:BCC_A2, tdb:GeNb-17Utt.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): BCC_A2, type code %B, sha256 `55314e2cadc330d9…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : GE NB% : VA : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): BCC_A2, type code %B, sha256 `0c86fa883ab70ed8…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : GE NB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90013-9](https://doi.org/10.1016/0022-5088%2878%2990013-9) J.L Jorda, R Flükiger, J Müller, The phase diagram of the niobium-germanium system, Journal of the Less Common Metals 62, 25-37 (1978).  
_cited as the source of values for this phase_

## FCC_A1 (Ge–Nb)

- Id: `phase:ge-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:fcc-a1)

Names (3): _corpus: _corpus:phase:ge-nb:fcc-a1  
_tdb: _tdb:GeNb-11Gen.tdb:FCC_A1, tdb:GeNb-17Utt.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): FCC_A1, type code %A, sha256 `55314e2cadc330d9…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : GE NB : VA : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): FCC_A1, type code %A, sha256 `0c86fa883ab70ed8…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : GE NB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_

## GE2NB_C40 (Ge–Nb)

- Id: `phase:ge-nb:ge2nb-c40`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in GeNb-11Gen.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in GeNb-17Utt.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1951.79 K, x(Nb) 0.3283–0.34016
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:ge2nb-c40)

Names (4): _corpus: _corpus:phase:ge-nb:ge2nb-c40  
_paper: _paper:10.1016/j.jallcom.2010.12.005:(NbGe2)  
_tdb: _tdb:GeNb-11Gen.tdb:GE2NB_C40, tdb:GeNb-17Utt.tdb:GE2NB_C40  


### TDB models of GE2NB_C40 (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): GE2NB_C40, type code %, sha256 `55314e2cadc330d9…`

~~~~text
53: PHASE GE2NB_C40 % 2 2 1 !
54: CONST GE2NB_C40 : GE% NB : GE NB% : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): GE2NB_C40, type code %, sha256 `0c86fa883ab70ed8…`

~~~~text
49: PHASE GE2NB_C40 % 2 2 1 !
50: CONST GE2NB_C40 : GE% NB : GE NB% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90013-9](https://doi.org/10.1016/0022-5088%2878%2990013-9) J.L Jorda, R Flükiger, J Müller, The phase diagram of the niobium-germanium system, Journal of the Less Common Metals 62, 25-37 (1978).  
_cited as the source of values for this phase_

## GE2NB3_D88 (Ge–Nb)

- Id: `phase:ge-nb:ge2nb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in GeNb-11Gen.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2291.56 K, x(Nb) 0.56993–0.58988
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:ge2nb3-d88)

Names (3): _corpus: _corpus:phase:ge-nb:ge2nb3-d88  
_paper: _paper:10.1016/j.jallcom.2010.12.005:(Nb3Ge2)  
_tdb: _tdb:GeNb-11Gen.tdb:GE2NB3_D88  


### TDB models of GE2NB3_D88 (1): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): GE2NB3_D88, type code %, sha256 `55314e2cadc330d9…`

~~~~text
58: PHASE GE2NB3_D88 % 4 2 3 3 1 !
59: CONST GE2NB3_D88 : GE NB% : GE% NB : NB : GE VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase; reports values for this phase_

## GE3NB5_D8M (Ge–Nb)

- Id: `phase:ge-nb:ge3nb5-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2453.08 K, x(Nb) 0.60395–0.63035
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:ge3nb5-d8m)

Names (4): _corpus: _corpus:phase:ge-nb:ge3nb5-d8m  
_paper: _paper:10.1016/j.jallcom.2010.12.005:(Nb5Ge3)  
_tdb: _tdb:GeNb-11Gen.tdb:GE3NB5_D8M, tdb:GeNb-17Utt.tdb:GE3NB5_D8M  


### TDB models of GE3NB5_D8M (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): GE3NB5_D8M, type code %, sha256 `55314e2cadc330d9…`

~~~~text
63: PHASE GE3NB5_D8M % 3 4 1 3 !
64: CONST GE3NB5_D8M : NB : GE NB% : GE% VA : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): GE3NB5_D8M, type code %, sha256 `0c86fa883ab70ed8…`

~~~~text
54: PHASE GE3NB5_D8M % 3 4 1 3 !
55: CONST GE3NB5_D8M : NB : GE NB% : GE% VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90013-9](https://doi.org/10.1016/0022-5088%2878%2990013-9) J.L Jorda, R Flükiger, J Müller, The phase diagram of the niobium-germanium system, Journal of the Less Common Metals 62, 25-37 (1978).  
_cited as the source of values for this phase_

## GENB3_A15 (Ge–Nb)

- Id: `phase:ge-nb:genb3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2176.65 K, x(Nb) 0.76095–0.82046
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:genb3-a15)

Names (4): _corpus: _corpus:phase:ge-nb:genb3-a15  
_paper: _paper:10.1016/j.jallcom.2010.12.005:(Nb3Ge)  
_tdb: _tdb:GeNb-11Gen.tdb:GENB3_A15, tdb:GeNb-17Utt.tdb:GENB3_A15  


### TDB models of GENB3_A15 (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): GENB3_A15, type code %, sha256 `55314e2cadc330d9…`

~~~~text
68: PHASE GENB3_A15 % 2 1 3 !
69: CONST GENB3_A15 : GE% NB VA : NB : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): GENB3_A15, type code %, sha256 `0c86fa883ab70ed8…`

~~~~text
59: PHASE GENB3_A15 % 2 1 3 !
60: CONST GENB3_A15 : GE% NB : NB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90013-9](https://doi.org/10.1016/0022-5088%2878%2990013-9) J.L Jorda, R Flükiger, J Müller, The phase diagram of the niobium-germanium system, Journal of the Less Common Metals 62, 25-37 (1978).  
_cited as the source of values for this phase_

## HCP_A3 (Ge–Nb)

- Id: `phase:ge-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:hcp-a3)

Names (3): _corpus: _corpus:phase:ge-nb:hcp-a3  
_tdb: _tdb:GeNb-11Gen.tdb:HCP_A3, tdb:GeNb-17Utt.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): HCP_A3, type code %, sha256 `55314e2cadc330d9…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : GE NB : VA : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): HCP_A3, type code %, sha256 `0c86fa883ab70ed8…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : GE NB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_

## LIQUID (Ge–Nb)

- Id: `phase:ge-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1210.78–4000 K, x(Nb) 0–1
- Literature: 30 values (30 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-nb:liquid)

Names (4): _corpus: _corpus:phase:ge-nb:liquid  
_paper: _paper:10.1016/j.jallcom.2010.12.005:L  
_tdb: _tdb:GeNb-11Gen.tdb:LIQUID, tdb:GeNb-17Utt.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GeNb-11Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb): LIQUID, type code %, sha256 `55314e2cadc330d9…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : GE NB : !
~~~~

[GeNb-17Utt.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb): LIQUID, type code %, sha256 `0c86fa883ab70ed8…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GE NB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90013-9](https://doi.org/10.1016/0022-5088%2878%2990013-9) J.L Jorda, R Flükiger, J Müller, The phase diagram of the niobium-germanium system, Journal of the Less Common Metals 62, 25-37 (1978).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
