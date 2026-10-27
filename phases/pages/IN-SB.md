# In–Sb phases

> In–Sb system: 7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-SB.html · Markdown: https://data.orchid-project.org/phases/pages/IN-SB.md

7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-SB) · [full JSON](https://data.orchid-project.org/phases/systems/IN-SB.json) · [In–Sb system page](https://data.orchid-project.org/systems/IN-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Sb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-sb-a6-tetragonal); _phase:in-sb:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–429.91 K, x(Sb) 0–0 | 0 | 5 |
| [RHOMBOHEDRAL_A7](#phase-in-sb-a7-rhombohedral); _phase:in-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–903.78 K, x(Sb) 0.99239–1 | 0 | 5 |
| [ZINCBLENDE_B3](#phase-in-sb-b3-zincblende); _phase:in-sb:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–810.39 K, x(Sb) 0.5–0.5 | 0 | 5 |
| [BCC_A2](#phase-in-sb-bcc-a2); _phase:in-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-in-sb-fcc-a1); _phase:in-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-in-sb-hcp-a3); _phase:in-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-in-sb-liquid); _phase:in-sb:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 426.32–2500 K, x(Sb) 0–1 | 1 | 5 |

## TETRAGONAL_A6 (In–Sb)

- Id: `phase:in-sb:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–429.91 K, x(Sb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sb:a6-tetragonal)

Names (6): _corpus: _corpus:phase:in-sb:a6-tetragonal  
_tdb: _tdb:InSb-03Liu.tdb:TETRAGONAL_A6, tdb:InSb-13Cao.tdb:TETRAGONAL_A6, tdb:InSb-19Gie.tdb:TETRAGONAL_A6, tdb:InSb-94Ans-LB.tdb:TETRAGONAL_A6, tdb:InSb-97Xie.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (5): PHASE and CONSTITUENT statements as written

[InSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-03Liu.tdb): TETRAGONAL_A6, type code %, sha256 `8e3372858668e0fe…`

~~~~text
51: PHASE TETRAGONAL_A6 % 1 1 !
52: CONST TETRAGONAL_A6 : IN% SB : !
~~~~

[InSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-13Cao.tdb): TETRAGONAL_A6, type code %, sha256 `462ef51afa935db9…`

~~~~text
46: PHASE TETRAGONAL_A6 % 1 1 !
47: CONST TETRAGONAL_A6 : IN : !
~~~~

[InSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-19Gie.tdb): TETRAGONAL_A6, type code %, sha256 `ad0e725af0bc5e36…`

~~~~text
51: PHASE TETRAGONAL_A6 % 1 1 !
52: CONST TETRAGONAL_A6 : IN : !
~~~~

[InSb-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-94Ans-LB.tdb): TETRAGONAL_A6, type code %, sha256 `00dc9a7748d98148…`

~~~~text
46: PHASE TETRAGONAL_A6 % 1 1 !
47: CONST TETRAGONAL_A6 : IN : !
~~~~

[InSb-97Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-97Xie.tdb): TETRAGONAL_A6, type code %, sha256 `7b7c5eb7b886d1e5…`

~~~~text
39: PHASE TETRAGONAL_A6 % 1 1 !
40: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (In–Sb)

- Id: `phase:in-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–903.78 K, x(Sb) 0.99239–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:in-sb:a7-rhombohedral  
_tdb: _tdb:InSb-03Liu.tdb:RHOMBOHEDRAL_A7, tdb:InSb-13Cao.tdb:RHOMBOHEDRAL_A7, tdb:InSb-19Gie.tdb:RHOMBOHEDRAL_A7, tdb:InSb-94Ans-LB.tdb:RHOMBOHEDRAL_A7, tdb:InSb-97Xie.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (5): PHASE and CONSTITUENT statements as written

[InSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-03Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8e3372858668e0fe…`

~~~~text
56: PHASE RHOMBOHEDRAL_A7 % 1 1 !
57: CONST RHOMBOHEDRAL_A7 : IN SB% : !
~~~~

[InSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-13Cao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `462ef51afa935db9…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : IN SB% : !
~~~~

[InSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-19Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `ad0e725af0bc5e36…`

~~~~text
56: PHASE RHOMBOHEDRAL_A7 % 1 1 !
57: CONST RHOMBOHEDRAL_A7 : IN SB% : !
~~~~

[InSb-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-94Ans-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `00dc9a7748d98148…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : IN SB% : !
~~~~

[InSb-97Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-97Xie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `7b7c5eb7b886d1e5…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## ZINCBLENDE_B3 (In–Sb)

- Id: `phase:in-sb:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdps and oqmd-4657, space group 216
- Stoichiometry: In 0.5000, Sb 0.5000
- Stability: stable in 5 of 5 calculated diagram(s): 300–810.39 K, x(Sb) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sb:b3-zincblende)

Names (8): _corpus: _corpus:phase:in-sb:b3-zincblende  
_mp: _mp:mp-aaaabdps  
_oqmd: _oqmd:oqmd-4657  
_tdb: _tdb:InSb-03Liu.tdb:ZINCBLENDE_B3, tdb:InSb-13Cao.tdb:ZINCBLENDE_B3, tdb:InSb-19Gie.tdb:ZINCBLENDE_B3, tdb:InSb-94Ans-LB.tdb:ZINCBLENDE_B3, tdb:InSb-97Xie.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (5): PHASE and CONSTITUENT statements as written

[InSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-03Liu.tdb): ZINCBLENDE_B3, type code %, sha256 `8e3372858668e0fe…`

~~~~text
61: PHASE ZINCBLENDE_B3 % 2 1 1 !
62: CONST ZINCBLENDE_B3 : IN : SB : !
~~~~

[InSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-13Cao.tdb): ZINCBLENDE_B3, type code %, sha256 `462ef51afa935db9…`

~~~~text
56: PHASE ZINCBLENDE_B3 % 2 1 1 !
57: CONST ZINCBLENDE_B3 : IN : SB : !
~~~~

[InSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-19Gie.tdb): ZINCBLENDE_B3, type code %, sha256 `ad0e725af0bc5e36…`

~~~~text
61: PHASE ZINCBLENDE_B3 % 2 1 1 !
62: CONST ZINCBLENDE_B3 : IN : SB : !
~~~~

[InSb-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-94Ans-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `00dc9a7748d98148…`

~~~~text
56: PHASE ZINCBLENDE_B3 % 2 1 1 !
57: CONST ZINCBLENDE_B3 : IN : SB : !
~~~~

[InSb-97Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-97Xie.tdb): ZINCBLENDE_B3, type code %, sha256 `7b7c5eb7b886d1e5…`

~~~~text
49: PHASE ZINCBLENDE_B3 % 2 1 1 !
50: CONST ZINCBLENDE_B3 : IN : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## BCC_A2 (In–Sb)

- Id: `phase:in-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sb:bcc-a2)

Names (6): _corpus: _corpus:phase:in-sb:bcc-a2  
_tdb: _tdb:InSb-03Liu.tdb:BCC_A2, tdb:InSb-13Cao.tdb:BCC_A2, tdb:InSb-19Gie.tdb:BCC_A2, tdb:InSb-94Ans-LB.tdb:BCC_A2, tdb:InSb-97Xie.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[InSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-03Liu.tdb): BCC_A2, type code %B, sha256 `8e3372858668e0fe…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : IN SB : VA : !
~~~~

[InSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-13Cao.tdb): BCC_A2, type code %B, sha256 `462ef51afa935db9…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : IN SB : VA : !
~~~~

[InSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-19Gie.tdb): BCC_A2, type code %B, sha256 `ad0e725af0bc5e36…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : IN SB : VA : !
~~~~

[InSb-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-94Ans-LB.tdb): BCC_A2, type code %B, sha256 `00dc9a7748d98148…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : IN SB : VA : !
~~~~

[InSb-97Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-97Xie.tdb): BCC_A2, type code %B, sha256 `7b7c5eb7b886d1e5…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : IN SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## FCC_A1 (In–Sb)

- Id: `phase:in-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sb:fcc-a1)

Names (6): _corpus: _corpus:phase:in-sb:fcc-a1  
_tdb: _tdb:InSb-03Liu.tdb:FCC_A1, tdb:InSb-13Cao.tdb:FCC_A1, tdb:InSb-19Gie.tdb:FCC_A1, tdb:InSb-94Ans-LB.tdb:FCC_A1, tdb:InSb-97Xie.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[InSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-03Liu.tdb): FCC_A1, type code %A, sha256 `8e3372858668e0fe…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : IN SB : VA : !
~~~~

[InSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-13Cao.tdb): FCC_A1, type code %A, sha256 `462ef51afa935db9…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : IN SB : VA : !
~~~~

[InSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-19Gie.tdb): FCC_A1, type code %A, sha256 `ad0e725af0bc5e36…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : IN SB : VA : !
~~~~

[InSb-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-94Ans-LB.tdb): FCC_A1, type code %A, sha256 `00dc9a7748d98148…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : IN SB : VA : !
~~~~

[InSb-97Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-97Xie.tdb): FCC_A1, type code %A, sha256 `7b7c5eb7b886d1e5…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : IN SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## HCP_A3 (In–Sb)

- Id: `phase:in-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sb:hcp-a3)

Names (6): _corpus: _corpus:phase:in-sb:hcp-a3  
_tdb: _tdb:InSb-03Liu.tdb:HCP_A3, tdb:InSb-13Cao.tdb:HCP_A3, tdb:InSb-19Gie.tdb:HCP_A3, tdb:InSb-94Ans-LB.tdb:HCP_A3, tdb:InSb-97Xie.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[InSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-03Liu.tdb): HCP_A3, type code %A, sha256 `8e3372858668e0fe…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : IN SB : VA : !
~~~~

[InSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-13Cao.tdb): HCP_A3, type code %A, sha256 `462ef51afa935db9…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : IN SB : VA : !
~~~~

[InSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-19Gie.tdb): HCP_A3, type code %A, sha256 `ad0e725af0bc5e36…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : IN SB : VA : !
~~~~

[InSb-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-94Ans-LB.tdb): HCP_A3, type code %A, sha256 `00dc9a7748d98148…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : IN SB : VA : !
~~~~

[InSb-97Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-97Xie.tdb): HCP_A3, type code %A, sha256 `7b7c5eb7b886d1e5…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : IN SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## LIQUID (In–Sb)

- Id: `phase:in-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 426.32–2500 K, x(Sb) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sb:liquid)

Names (7): _corpus: _corpus:phase:in-sb:liquid  
_paper: _paper:10.1007/s11661-019-05288-9:liquid  
_tdb: _tdb:InSb-03Liu.tdb:LIQUID, tdb:InSb-13Cao.tdb:LIQUID, tdb:InSb-19Gie.tdb:LIQUID, tdb:InSb-94Ans-LB.tdb:LIQUID, tdb:InSb-97Xie.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[InSb-03Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-03Liu.tdb): LIQUID, type code %, sha256 `8e3372858668e0fe…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : IN SB : !
~~~~

[InSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-13Cao.tdb): LIQUID, type code %, sha256 `462ef51afa935db9…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : IN SB : !
~~~~

[InSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-19Gie.tdb): LIQUID, type code %, sha256 `ad0e725af0bc5e36…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : IN SB : !
~~~~

[InSb-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-94Ans-LB.tdb): LIQUID, type code %, sha256 `00dc9a7748d98148…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : IN SB : !
~~~~

[InSb-97Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/InSb-97Xie.tdb): LIQUID, type code %, sha256 `7b7c5eb7b886d1e5…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : IN SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-003-0240-x](https://doi.org/10.1007/s11664-003-0240-x) H. S. Liu, C. L. Liu, C. Wang, Z. P. Jin, K. Ishida, Thermodynamic modeling of the Au-In-Sb ternary system, Journal of Elec Materi 32, 81-88 (2003).  
_assessment that models this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
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
