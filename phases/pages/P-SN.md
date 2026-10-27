# P–Sn phases

> P–Sn system: 12 phases (tier A 5, tier C 3, liquid 1, gas 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/P-SN.html · Markdown: https://data.orchid-project.org/phases/pages/P-SN.md

12 phases (tier A 5, tier C 3, liquid 1, gas 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=P-SN) · [full JSON](https://data.orchid-project.org/phases/systems/P-SN.json) · [P–Sn system page](https://data.orchid-project.org/systems/P-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/P-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the P–Sn system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-p-sn-a4-diamond); _phase:p-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BCT_A5](#phase-p-sn-a5-bct); _phase:p-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(P) 0–0 | 0 | 3 |
| [BCC_A2](#phase-p-sn-bcc-a2); _phase:p-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-p-sn-fcc-a1); _phase:p-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-p-sn-gas); _phase:p-sn:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 704.7–2500 K, x(P) 0.91327–1 | 0 | 1 |
| [HCP_A3](#phase-p-sn-hcp-a3); _phase:p-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-p-sn-liquid); _phase:p-sn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 503.9–2500 K, x(P) 0–1 | 0 | 3 |
| [RED_P](#phase-p-sn-p-red); _phase:p-sn:p-red_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–852.48 K, x(P) 1–1 | 0 | 3 |
| [WHITE_P](#phase-p-sn-p-white); _phase:p-sn:p-white_ |  | needs_review | not stable in 3 calculated diagram(s) | 0 | 3 |
| [SN3P4](#phase-p-sn-sn3p4); _phase:p-sn:sn3p4_ | Sn3P4 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–833.73 K, x(P) 0.57143–0.57143 | 0 | 2 |
| [SN4P3](#phase-p-sn-sn4p3); _phase:p-sn:sn4p3_ | Sn4As3 · hR7 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–833.06 K, x(P) 0.42857–0.42857 | 0 | 3 |
| [SNP3](#phase-p-sn-snp3); _phase:p-sn:snp3_ | SnP3 · hR8 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–853.04 K, x(P) 0.75–0.75 | 0 | 2 |

## DIAMOND_A4 (P–Sn)

- Id: `phase:p-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:a4-diamond)

Names (3): _corpus: _corpus:phase:p-sn:a4-diamond  
_tdb: _tdb:SnP-11Hin.tdb:DIAMOND_A4, tdb:SnP-24Oik.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): DIAMOND_A4, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : SN : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): DIAMOND_A4, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## BCT_A5 (P–Sn)

- Id: `phase:p-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(P) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:a5-bct)

Names (4): _corpus: _corpus:phase:p-sn:a5-bct  
_tdb: _tdb:SnP-01Mie.tdb:BCT_A5, tdb:SnP-11Hin.tdb:BCT_A5, tdb:SnP-24Oik.tdb:BCT_A5  


### TDB models of BCT_A5 (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): BCT_A5, type code %, sha256 `d3822dd98636448a…`

~~~~text
40: PHASE BCT_A5 % 1 1 !
41: CONST BCT_A5 : SN : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): BCT_A5, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
44: PHASE BCT_A5 % 1 1 !
45: CONST BCT_A5 : SN : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): BCT_A5, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
54: PHASE BCT_A5 % 1 1 !
55: CONST BCT_A5 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## BCC_A2 (P–Sn)

- Id: `phase:p-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:bcc-a2)

Names (4): _corpus: _corpus:phase:p-sn:bcc-a2  
_tdb: _tdb:SnP-01Mie.tdb:BCC_A2, tdb:SnP-11Hin.tdb:BCC_A2, tdb:SnP-24Oik.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): BCC_A2, type code %B, sha256 `d3822dd98636448a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : P SN : VA : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): BCC_A2, type code %B, sha256 `a6b5bd1aae15dd8a…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : P SN : VA : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): BCC_A2, type code %B, sha256 `efdb620aa2bffd9c…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : P SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## FCC_A1 (P–Sn)

- Id: `phase:p-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:fcc-a1)

Names (4): _corpus: _corpus:phase:p-sn:fcc-a1  
_tdb: _tdb:SnP-01Mie.tdb:FCC_A1, tdb:SnP-11Hin.tdb:FCC_A1, tdb:SnP-24Oik.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): FCC_A1, type code %A, sha256 `d3822dd98636448a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : P SN : VA : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): FCC_A1, type code %A, sha256 `a6b5bd1aae15dd8a…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : P SN : VA : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): FCC_A1, type code %A, sha256 `efdb620aa2bffd9c…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : P SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## GAS (P–Sn)

- Id: `phase:p-sn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 704.7–2500 K, x(P) 0.91327–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:gas)

Names (2): _corpus: _corpus:phase:p-sn:gas  
_tdb: _tdb:SnP-24Oik.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): GAS, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
82: PHASE GAS:G % 1 1 !
83: CONST GAS:G : P P2 P3 P4 SN SN2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_

## HCP_A3 (P–Sn)

- Id: `phase:p-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:hcp-a3)

Names (4): _corpus: _corpus:phase:p-sn:hcp-a3  
_tdb: _tdb:SnP-01Mie.tdb:HCP_A3, tdb:SnP-11Hin.tdb:HCP_A3, tdb:SnP-24Oik.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): HCP_A3, type code %A, sha256 `d3822dd98636448a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SN : VA : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): HCP_A3, type code %A, sha256 `a6b5bd1aae15dd8a…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : SN : VA : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): HCP_A3, type code %A, sha256 `efdb620aa2bffd9c…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## LIQUID (P–Sn)

- Id: `phase:p-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 503.9–2500 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:liquid)

Names (4): _corpus: _corpus:phase:p-sn:liquid  
_tdb: _tdb:SnP-01Mie.tdb:LIQUID, tdb:SnP-11Hin.tdb:LIQUID, tdb:SnP-24Oik.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): LIQUID, type code %, sha256 `d3822dd98636448a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : P SN : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): LIQUID, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : P SN : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): LIQUID, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : P SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## RED_P (P–Sn)

- Id: `phase:p-sn:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–852.48 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:p-red)

Names (4): _corpus: _corpus:phase:p-sn:p-red  
_tdb: _tdb:SnP-01Mie.tdb:RED_P, tdb:SnP-11Hin.tdb:RED_P, tdb:SnP-24Oik.tdb:RED_P  


### TDB models of RED_P (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): RED_P, type code %, sha256 `d3822dd98636448a…`

~~~~text
50: PHASE RED_P % 1 1 !
51: CONST RED_P : P : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): RED_P, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
54: PHASE RED_P % 1 1 !
55: CONST RED_P : P : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): RED_P, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
64: PHASE RED_P % 1 1 !
65: CONST RED_P : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## WHITE_P (P–Sn)

- Id: `phase:p-sn:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:p-white)

Names (4): _corpus: _corpus:phase:p-sn:p-white  
_tdb: _tdb:SnP-01Mie.tdb:WHITE_P, tdb:SnP-11Hin.tdb:WHITE_P, tdb:SnP-24Oik.tdb:WHITE_P  


### TDB models of WHITE_P (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): WHITE_P, type code %, sha256 `d3822dd98636448a…`

~~~~text
45: PHASE WHITE_P % 1 1 !
46: CONST WHITE_P : P : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): WHITE_P, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
49: PHASE WHITE_P % 1 1 !
50: CONST WHITE_P : P : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): WHITE_P, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
59: PHASE WHITE_P % 1 1 !
60: CONST WHITE_P : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## SN3P4 (P–Sn)

- Id: `phase:p-sn:sn3p4`; status `assigned`
- Structure: Sn3P4 · hR19 · R-3m (166); type `st:sn3p4-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: P 0.5714, Sn 0.4286
- Stability: stable in 2 of 2 calculated diagram(s): 300–833.73 K, x(P) 0.57143–0.57143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:sn3p4)

Names (3): _corpus: _corpus:phase:p-sn:sn3p4  
_tdb: _tdb:SnP-11Hin.tdb:SN3P4, tdb:SnP-24Oik.tdb:SN3P4  


### TDB models of SN3P4 (2): PHASE and CONSTITUENT statements as written

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): SN3P4, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
64: PHASE SN3P4 % 2 3 4 !
65: CONST SN3P4 : SN : P : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): SN3P4, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
74: PHASE SN3P4 % 2 3 4 !
75: CONST SN3P4 : SN : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## SN4P3 (P–Sn)

- Id: `phase:p-sn:sn4p3`; status `assigned`
- Structure: Sn4As3 · hR7 · R-3m (166); type `st:sn4as3-hr7`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_6_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: P 0.4286, Sn 0.5714
- Stability: stable in 3 of 3 calculated diagram(s): 300–833.06 K, x(P) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:sn4p3)

Names (4): _corpus: _corpus:phase:p-sn:sn4p3  
_tdb: _tdb:SnP-01Mie.tdb:SN4P3, tdb:SnP-11Hin.tdb:SN4P3, tdb:SnP-24Oik.tdb:SN4P3  


### TDB models of SN4P3 (3): PHASE and CONSTITUENT statements as written

[SnP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-01Mie.tdb): SN4P3, type code %, sha256 `d3822dd98636448a…`

~~~~text
55: PHASE SN4P3 % 2 4 3 !
56: CONST SN4P3 : SN : P : !
~~~~

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): SN4P3, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
59: PHASE SN4P3 % 2 4 3 !
60: CONST SN4P3 : SN : P : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): SN4P3, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
69: PHASE SN4P3 % 2 4 3 !
70: CONST SN4P3 : SN : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## SNP3 (P–Sn)

- Id: `phase:p-sn:snp3`; status `assigned`
- Structure: SnP3 · hR8 · R-3m (166); type `st:snp3-hr8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: P 0.7500, Sn 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–853.04 K, x(P) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sn:snp3)

Names (3): _corpus: _corpus:phase:p-sn:snp3  
_tdb: _tdb:SnP-11Hin.tdb:SNP3, tdb:SnP-24Oik.tdb:SNP3  


### TDB models of SNP3 (2): PHASE and CONSTITUENT statements as written

[SnP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-11Hin.tdb): SNP3, type code %, sha256 `a6b5bd1aae15dd8a…`

~~~~text
69: PHASE SNP3 % 2 1 3 !
70: CONST SNP3 : SN : P : !
~~~~

[SnP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/SnP-24Oik.tdb): SNP3, type code %, sha256 `efdb620aa2bffd9c…`

~~~~text
79: PHASE SNP3 % 2 1 3 !
80: CONST SNP3 : SN : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
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
