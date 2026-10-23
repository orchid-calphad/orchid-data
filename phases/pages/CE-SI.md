# Ce–Si phases

> Ce–Si system: 13 phases (tier A 9, tier C 1, liquid 1, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-SI.html · Markdown: https://data.orchid-project.org/phases/pages/CE-SI.md

13 phases (tier A 9, tier C 1, liquid 1, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-SI) · [full JSON](https://data.orchid-project.org/phases/systems/CE-SI.json) · [Ce–Si system page](https://data.orchid-project.org/systems/CE-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Si system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ce-si-a4-diamond); _phase:ce-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.97 K, x(Si) 1–1 | 7 | 2 |
| [BCC_A2](#phase-ce-si-bcc-a2); _phase:ce-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1000–1075 K, x(Si) 0–0 | 0 | 2 |
| [CE3SI2_D5A](#phase-ce-si-ce3si2-d5a); _phase:ce-si:ce3si2-d5a_ | Si2U3 · D5_a · tP10 · P4/mbm (127) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1665.73 K, x(Si) 0.4–0.4 | 14 | 2 |
| [CE3SI4](#phase-ce-si-ce3si4); _phase:ce-si:ce3si4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1471.38 K, x(Si) 0.57265–0.57265 | 2 | 1 |
| [CE3SI5](#phase-ce-si-ce3si5); _phase:ce-si:ce3si5_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1992.02 K, x(Si) 0.625–0.63 | 17 | 2 |
| [CE5SI3_D8L](#phase-ce-si-ce5si3-d8l); _phase:ce-si:ce5si3-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1643.64 K, x(Si) 0.375–0.375 | 15 | 2 |
| [CE5SI4](#phase-ce-si-ce5si4); _phase:ce-si:ce5si4_ | Si4Zr5 · tP36 · P4_12_12 (92) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1772.89 K, x(Si) 0.44444–0.44444 | 19 | 2 |
| [CESI_B27](#phase-ce-si-cesi-b27); _phase:ce-si:cesi-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1899.45 K, x(Si) 0.5–0.5 | 27 | 2 |
| [CESI2_CC](#phase-ce-si-cesi2-cc); _phase:ce-si:cesi2-cc_ | Si2Th · C_c · tI12 · I4_1/amd (141) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1883.47 K, x(Si) 0.66667–0.66667 | 20 | 2 |
| [DHCP](#phase-ce-si-dhcp-a3); _phase:ce-si:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ce-si-fcc-a1); _phase:ce-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1000 K, x(Si) 0–0 | 4 | 2 |
| [HCP_A3](#phase-ce-si-hcp-a3); _phase:ce-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ce-si-liquid); _phase:ce-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 900.07–2500 K, x(Si) 0–1 | 139 | 2 |

## DIAMOND_A4 (Ce–Si)

- Id: `phase:ce-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.97 K, x(Si) 1–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:a4-diamond)

Names (5): _corpus: _corpus:phase:ce-si:a4-diamond, corpus:phase:ce-si:diamond-a4  
_paper: _paper:10.1016/j.tca.2016.11.003:(Si)  
_tdb: _tdb:CeSi-04Gro.tdb:DIAMOND_A4, tdb:CeSi-16Hua.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): DIAMOND_A4, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): DIAMOND_A4, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase_
- [doi:10.1002/zaac.19130840125](https://doi.org/10.1002/zaac.19130840125) Rudolf Vogel, Über die Legierungen des Cers mit Silicium und Wismut, Z. Anorg. Chem. 84, 323-339 (1913).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00905509](https://doi.org/10.1007/bf00905509) F. Benesovsky, H. Nowotny, W. Rieger, H. Rassaerts, Untersuchungen in den Dreistoffen Cer-Thorium(Uran)-Silicium, Monatshefte für Chemie 97, 221-229 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_

## BCC_A2 (Ce–Si)

- Id: `phase:ce-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1000–1075 K, x(Si) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:bcc-a2)

Names (3): _corpus: _corpus:phase:ce-si:bcc-a2  
_tdb: _tdb:CeSi-04Gro.tdb:BCC_A2, tdb:CeSi-16Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): BCC_A2, type code %B, sha256 `1de57b4b73d0894d…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CE% SI : VA : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): BCC_A2, type code %B, sha256 `bf95d2efc0a2b00b…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CE% SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase_

## CE3SI2_D5A (Ce–Si)

- Id: `phase:ce-si:ce3si2-d5a`; status `assigned`
- Structure: Si2U3 · D5_a · tP10 · P4/mbm (127); type `st:d5-a-si2u3-tp10`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.6000, Si 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1665.73 K, x(Si) 0.4–0.4
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:ce3si2-d5a)

Names (4): _corpus: _corpus:phase:ce-si:ce3si2-d5a  
_paper: _paper:10.1016/j.tca.2016.11.003:Ce3Si2  
_tdb: _tdb:CeSi-04Gro.tdb:CE3SI2_D5A, tdb:CeSi-16Hua.tdb:CE3SI2_D5A  


### TDB models of CE3SI2_D5A (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): CE3SI2_D5A, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
56: PHASE CE3SI2_D5A % 2 3 2 !
57: CONST CE3SI2_D5A : CE : SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): CE3SI2_D5A, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
56: PHASE CE3SI2_D5A % 2 3 2 !
57: CONST CE3SI2_D5A : CE : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_

## CE3SI4 (Ce–Si)

- Id: `phase:ce-si:ce3si4`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (literature_printed): V2B3 · oC20 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): V2B3 · oC20 · Cmcm (63) — Hallstedt 2025 mmc2 row for CE3SI4: Ce3Si4
- Candidate (tdb_comment): V2B3 · oC20 · Cmcm — CeSi-16Hua.tdb: 'Prototype V2B3 (oC20, Cmcm)'
- Stoichiometry: Ce 0.4274, Si 0.5726
- Stability: stable in 1 of 1 calculated diagram(s): 300–1471.38 K, x(Si) 0.57265–0.57265
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:ce3si4)

Names (3): _corpus: _corpus:phase:ce-si:ce3si4  
_paper: _paper:10.1016/j.tca.2016.11.003:CeSi1.34  
_tdb: _tdb:CeSi-16Hua.tdb:CE3SI4  


### TDB models of CE3SI4 (1): PHASE and CONSTITUENT statements as written

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): CE3SI4, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
71: PHASE CE3SI4 % 2 1 1.34 !
72: CONST CE3SI4 : CE : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_

## CE3SI5 (Ce–Si)

- Id: `phase:ce-si:ce3si5`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; no_structure_token
- Candidate (literature_printed): GdSi1.4 · oI12 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): GdSi1.4 · oI12 · Imma (74) — Hallstedt 2025 mmc2 row for CE3SI5: Ce3Si5
- Candidate (tdb_comment): GdSi1.4 · oI12 · Imma — CeSi-04Gro.tdb: 'Prototype GdSi1.4 (oI12, Imma)'
- Candidate (tdb_comment): GdSi1.4 · oI12 · Imma — CeSi-16Hua.tdb: 'Prototype GdSi1.4 (oI12, Imma)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1992.02 K, x(Si) 0.625–0.63
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:ce3si5)

Names (5): _corpus: _corpus:phase:ce-si:ce3si5  
_paper: _paper:10.1007/s11661-004-0172-y:Ce3Si5, paper:10.1016/j.tca.2016.11.003:CeSi1.68  
_tdb: _tdb:CeSi-04Gro.tdb:CE3SI5, tdb:CeSi-16Hua.tdb:CE3SI5  


### TDB models of CE3SI5 (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): CE3SI5, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
71: PHASE CE3SI5 % 2 3 5 !
72: CONST CE3SI5 : CE : SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): CE3SI5, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
76: PHASE CE3SI5 % 2 0.37 0.63 !
77: CONST CE3SI5 : CE : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_

## CE5SI3_D8L (Ce–Si)

- Id: `phase:ce-si:ce5si3-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.6250, Si 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–1643.64 K, x(Si) 0.375–0.375
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:ce5si3-d8l)

Names (5): _corpus: _corpus:phase:ce-si:ce5si3-d8l  
_paper: _paper:10.1016/j.tca.2016.11.003:Ce5Si3, paper:10.1016/j.tca.2016.11.003:Ce5Si3 + (Ce)  
_tdb: _tdb:CeSi-04Gro.tdb:CE5SI3_D8L, tdb:CeSi-16Hua.tdb:CE5SI3_D8L  


### TDB models of CE5SI3_D8L (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): CE5SI3_D8L, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
51: PHASE CE5SI3_D8L % 2 5 3 !
52: CONST CE5SI3_D8L : CE : SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): CE5SI3_D8L, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
51: PHASE CE5SI3_D8L % 2 5 3 !
52: CONST CE5SI3_D8L : CE : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02400-0](https://doi.org/10.1016/s0925-8388%2896%2902400-0) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of some carbides, silicides, germanides and stannides of samarium by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 243, 186-193 (1996).  
_cited as the source of values for this phase_

## CE5SI4 (Ce–Si)

- Id: `phase:ce-si:ce5si4`; status `assigned`
- Structure: Si4Zr5 · tP36 · P4_12_12 (92); type `st:si4zr5-tp36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.5556, Si 0.4444
- Stability: stable in 2 of 2 calculated diagram(s): 300–1772.89 K, x(Si) 0.44444–0.44444
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:ce5si4)

Names (5): _corpus: _corpus:phase:ce-si:ce5si4  
_paper: _paper:10.1007/s11661-004-0172-y:Ce5Si4, paper:10.1016/j.tca.2016.11.003:Ce5Si4  
_tdb: _tdb:CeSi-04Gro.tdb:CE5SI4, tdb:CeSi-16Hua.tdb:CE5SI4  


### TDB models of CE5SI4 (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): CE5SI4, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
61: PHASE CE5SI4 % 2 5 4 !
62: CONST CE5SI4 : CE : SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): CE5SI4, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
61: PHASE CE5SI4 % 2 5 4 !
62: CONST CE5SI4 : CE : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_

## CESI_B27 (Ce–Si)

- Id: `phase:ce-si:cesi-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabfgd and oqmd-18278, space group 62
- Stoichiometry: Ce 0.5000, Si 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1899.45 K, x(Si) 0.5–0.5
- Literature: 27 values (27 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:cesi-b27)

Names (7): _corpus: _corpus:phase:ce-si:cesi-b27  
_mp: _mp:mp-aaaabfgd  
_oqmd: _oqmd:oqmd-18278  
_paper: _paper:10.1016/j.tca.2016.11.003:CeSi, paper:10.1016/j.tca.2016.11.003:CeSi (trace)  
_tdb: _tdb:CeSi-04Gro.tdb:CESI_B27, tdb:CeSi-16Hua.tdb:CESI_B27  


### TDB models of CESI_B27 (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): CESI_B27, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
66: PHASE CESI_B27 % 2 1 1 !
67: CONST CESI_B27 : CE : SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): CESI_B27, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
66: PHASE CESI_B27 % 2 1 1 !
67: CONST CESI_B27 : CE : SI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)06009-6](https://doi.org/10.1016/0925-8388%2894%2906009-6) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of some carbides, silicides and germanides of cerium and praseodymium, Journal of Alloys and Compounds 220, 88-93 (1995).  
_cited as the source of values for this phase_

## CESI2_CC (Ce–Si)

- Id: `phase:ce-si:cesi2-cc`; status `assigned`
- Structure: Si2Th · C_c · tI12 · I4_1/amd (141); type `st:c-c-si2th-ti12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacva and oqmd-6060, space group 141
- Stoichiometry: Ce 0.3333, Si 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1883.47 K, x(Si) 0.66667–0.66667
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:cesi2-cc)

Names (6): _corpus: _corpus:phase:ce-si:cesi2-cc  
_mp: _mp:mp-aaaaacva  
_oqmd: _oqmd:oqmd-6060  
_paper: _paper:10.1016/j.tca.2016.11.003:CeSi2  
_tdb: _tdb:CeSi-04Gro.tdb:CESI2_CC, tdb:CeSi-16Hua.tdb:CESI2_CC  


### TDB models of CESI2_CC (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): CESI2_CC, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
76: PHASE CESI2_CC % 2 1 2 !
77: CONST CESI2_CC : CE : SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): CESI2_CC, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
81: PHASE CESI2_CC % 2 1 2 !
82: CONST CESI2_CC : CE : SI : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19130840125](https://doi.org/10.1002/zaac.19130840125) Rudolf Vogel, Über die Legierungen des Cers mit Silicium und Wismut, Z. Anorg. Chem. 84, 323-339 (1913).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00905509](https://doi.org/10.1007/bf00905509) F. Benesovsky, H. Nowotny, W. Rieger, H. Rassaerts, Untersuchungen in den Dreistoffen Cer-Thorium(Uran)-Silicium, Monatshefte für Chemie 97, 221-229 (1966).  
_cited as the source of values for this phase_

## DHCP (Ce–Si)

- Id: `phase:ce-si:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:dhcp-a3)

Names (2): _corpus: _corpus:phase:ce-si:dhcp-a3  
_tdb: _tdb:CeSi-16Hua.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): DHCP, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase_

## FCC_A1 (Ce–Si)

- Id: `phase:ce-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1000 K, x(Si) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:fcc-a1)

Names (4): _corpus: _corpus:phase:ce-si:fcc-a1  
_paper: _paper:10.1016/j.tca.2016.11.003:(γCe)  
_tdb: _tdb:CeSi-04Gro.tdb:FCC_A1, tdb:CeSi-16Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): FCC_A1, type code %A, sha256 `1de57b4b73d0894d…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CE% SI : VA : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): FCC_A1, type code %A, sha256 `bf95d2efc0a2b00b…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CE% SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_

## HCP_A3 (Ce–Si)

- Id: `phase:ce-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:hcp-a3)

Names (3): _corpus: _corpus:phase:ce-si:hcp-a3  
_tdb: _tdb:CeSi-04Gro.tdb:HCP_A3, tdb:CeSi-16Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): HCP_A3, type code %A, sha256 `1de57b4b73d0894d…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CE SI : VA: !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): HCP_A3, type code %A, sha256 `bf95d2efc0a2b00b…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CE SI : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase_

## LIQUID (Ce–Si)

- Id: `phase:ce-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 900.07–2500 K, x(Si) 0–1
- Literature: 139 values (139 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-si:liquid)

Names (6): _corpus: _corpus:phase:ce-si:liquid  
_paper: _paper:10.1007/s11661-004-0172-y:Liquid, paper:10.1007/s11661-004-0172-y:liquid, paper:10.1016/j.tca.2016.11.003:L  
_tdb: _tdb:CeSi-04Gro.tdb:LIQUID, tdb:CeSi-16Hua.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CeSi-04Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-04Gro.tdb): LIQUID, type code %, sha256 `1de57b4b73d0894d…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CE SI : !
~~~~

[CeSi-16Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CeSi-16Hua.tdb): LIQUID, type code %, sha256 `bf95d2efc0a2b00b…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CE SI : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11661-004-0172-y](https://doi.org/10.1007/s11661-004-0172-y) Joachim Gröbner, Djordje Mirković, Rainer Schmid-Fetzer, Thermodynamic aspects of the constitution, grain refining, and solidification enthalpies of Al-Ce-Si alloys, Metall Mater Trans A 35, 3349-3362 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2016.11.003](https://doi.org/10.1016/j.tca.2016.11.003) Dandan Huang, Shuhong Liu, Ying Tang, Yong Du, Philip Nash, Bo Sundman, Experimental investigation and thermodynamic modeling of the Ce-Si system, Thermochimica Acta 646, 49-58 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jct.2014.08.015](https://doi.org/10.1016/j.jct.2014.08.015) J. Kim, I.-H. Jung, Critical evaluation and thermodynamic optimization of the Si-RE systems: Part I. Si-RE system (RE = La, Ce, Pr, Nd and Sm), J. Chem. Thermodyn. 81 (2015) 253–272.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(02)00409-7](https://doi.org/10.1016/s0925-8388%2802%2900409-7) M.V. Bulanova, P.N. Zheltov, K.A. Meleshevich, P.A. Saltykov, G. Effenberg, Cerium–silicon system, Journal of Alloys and Compounds 345, 110-115 (2002).  
_cited as the source of values for this phase_
- [doi:10.3139/146.110003](https://doi.org/10.3139/146.110003) A. Shukla, Y.-B. Kang, A.D. Pelton, Thermodynamic assessment of the ce-Si, Y-Si mg-Ce-Si and Mg-Y-Si systems, Int. J. Mater. Res. 100 (2009) 208–217.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19130840125](https://doi.org/10.1002/zaac.19130840125) Rudolf Vogel, Über die Legierungen des Cers mit Silicium und Wismut, Z. Anorg. Chem. 84, 323-339 (1913).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00905509](https://doi.org/10.1007/bf00905509) F. Benesovsky, H. Nowotny, W. Rieger, H. Rassaerts, Untersuchungen in den Dreistoffen Cer-Thorium(Uran)-Silicium, Monatshefte für Chemie 97, 221-229 (1966).  
_cited as the source of values for this phase_

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
