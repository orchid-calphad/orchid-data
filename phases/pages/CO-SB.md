# Co–Sb phases

> Co–Sb system: 8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-SB.html · Markdown: https://data.orchid-project.org/phases/pages/CO-SB.md

8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-SB) · [full JSON](https://data.orchid-project.org/phases/systems/CO-SB.json) · [Co–Sb system page](https://data.orchid-project.org/systems/CO-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Sb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-co-sb-a7-rhombohedral); _phase:co-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 8 | 4 |
| [BCC_A2](#phase-co-sb-bcc-a2); _phase:co-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [COSB_B81](#phase-co-sb-cosb-b81); _phase:co-sb:cosb-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1492.54 K, x(Sb) 0.45876–0.52523 | 0 | 4 |
| [COSB2_C18](#phase-co-sb-cosb2-c18); _phase:co-sb:cosb2-c18_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1208.97 K, x(Sb) 0.66667–0.6667 | 15 | 4 |
| [COSB3_D02](#phase-co-sb-cosb3-d02); _phase:co-sb:cosb3-d02_ | CoAs3 · D0_2 · cI32 · Im-3 (204) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1147.13 K, x(Sb) 0.75–0.75 | 14 | 4 |
| [FCC_A1](#phase-co-sb-fcc-a1); _phase:co-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 620–1772.98 K, x(Sb) 0–0.03902 | 9 | 4 |
| [HCP_A3](#phase-co-sb-hcp-a3); _phase:co-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–695.24 K, x(Sb) 0–6e-05 | 0 | 4 |
| [LIQUID](#phase-co-sb-liquid); _phase:co-sb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 901.33–2500 K, x(Sb) 0–1 | 41 | 4 |

## RHOMBOHEDRAL_A7 (Co–Sb)

- Id: `phase:co-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:co-sb:a7-rhombohedral  
_paper: _paper:10.1016/j.calphad.2007.11.001:(Sb)  
_tdb: _tdb:CoSb-08Zha.tdb:RHOMBOHEDRAL_A7, tdb:CoSb-09Zha.tdb:RHOMBOHEDRAL_A7, tdb:CoSb-19Gie.tdb:RHOMBOHEDRAL_A7, tdb:CoSb-20Bro.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `877e8f1ac13a2869…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `1d903c43e17f1a21…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `73b6e1ed6d86564b…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `bdb612f140be29a9…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080590131](https://doi.org/10.1002/zaac.19080590131) Kurt Lewkonja, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXV. Über die Legierungen des Kobalts mit Zinn, Antimon, Blei, Wismut, Thallium, Zink, Cadmium, Chrom und Silicium, Z. Anorg. Chem. 59, 293-345 (1908).  
_cited as the source of values for this phase_
- [doi:10.1007/bf03029292](https://doi.org/10.1007/bf03029292) K. Ishida, T. Nishizawa, Bull. Alloy Phase Diagrams 11 (1990) 243–248.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_

## BCC_A2 (Co–Sb)

- Id: `phase:co-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:bcc-a2)

Names (5): _corpus: _corpus:phase:co-sb:bcc-a2  
_tdb: _tdb:CoSb-08Zha.tdb:BCC_A2, tdb:CoSb-09Zha.tdb:BCC_A2, tdb:CoSb-19Gie.tdb:BCC_A2, tdb:CoSb-20Bro.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): BCC_A2, type code %B, sha256 `877e8f1ac13a2869…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CO SB : VA : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): BCC_A2, type code %B, sha256 `1d903c43e17f1a21…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO SB : VA : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): BCC_A2, type code %B, sha256 `73b6e1ed6d86564b…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO SB : VA : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): BCC_A2, type code %B, sha256 `bdb612f140be29a9…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_

## COSB_B81 (Co–Sb)

- Id: `phase:co-sb:cosb-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1492.54 K, x(Sb) 0.45876–0.52523
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:cosb-b81)

Names (5): _corpus: _corpus:phase:co-sb:cosb-b81  
_tdb: _tdb:CoSb-08Zha.tdb:COSB_B81, tdb:CoSb-09Zha.tdb:COSB_B81, tdb:CoSb-19Gie.tdb:COSB_B81, tdb:CoSb-20Bro.tdb:COSB_B81  


### TDB models of COSB_B81 (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): COSB_B81, type code %, sha256 `877e8f1ac13a2869…`

~~~~text
45: PHASE COSB_B81 % 3 0.3333 0.3333 0.3333 !
46: CONST COSB_B81 : CO% VA : CO VA% : SB : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): COSB_B81, type code %, sha256 `1d903c43e17f1a21…`

~~~~text
48: PHASE COSB_B81 % 3 0.3333 0.3333 0.3333 !
49: CONST COSB_B81 : CO% VA : CO VA% : SB : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): COSB_B81, type code %, sha256 `73b6e1ed6d86564b…`

~~~~text
47: PHASE COSB_B81 % 4 1 1 2 2 !
48: CONST COSB_B81 : CO : CO% VA : CO VA% : SB : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): COSB_B81, type code %, sha256 `bdb612f140be29a9…`

~~~~text
47: PHASE COSB_B81 % 3 0.3333 0.3333 0.3333 !
48: CONST COSB_B81 : CO% VA : CO VA% : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_

## COSB2_C18 (Co–Sb)

- Id: `phase:co-sb:cosb2-c18`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_C18:CoSb-08Zha.tdb; stoichiometry_contradicts_C18:CoSb-09Zha.tdb; stoichiometry_contradicts_C18:CoSb-20Bro.tdb
- Candidate (literature_printed): alpha-FeS2 · oP6 — printed with a label mapped to this phase
- Candidate (name_token): alpha-FeS2 · C18 · oP6 · Pnnm (58) — Strukturbericht/word 'C18' in the TDB name
- Candidate (sgte_mmc2): alpha-FeS2 · C18 · oP6 · Pnnm (58) — Hallstedt 2025 mmc2 row for COSB2_C18: CoSb2 (gamma)
- Candidate (tdb_comment): FeS2 · marcasite · oP6, Pnnm — CoSb-08Zha.tdb: 'Prototype FeS2 (marcasite, oP6, Pnnm)'
- Candidate (tdb_comment): FeS2 · marcasite · oP6, Pnnm — CoSb-09Zha.tdb: 'Prototype FeS2 (marcasite, oP6, Pnnm)'
- Candidate (tdb_comment): FeS2 · marcasite · oP6, Pnnm — CoSb-19Gie.tdb: 'Prototype FeS2 (marcasite, oP6, Pnnm)'
- Candidate (tdb_comment): FeS2 · marcasite · oP6, Pnnm — CoSb-20Bro.tdb: 'Prototype FeS2 (marcasite, oP6, Pnnm)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–1208.97 K, x(Sb) 0.66667–0.6667
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:cosb2-c18)

Names (6): _corpus: _corpus:phase:co-sb:cosb2-c18  
_paper: _paper:10.1016/j.calphad.2007.11.001:γCoSb2  
_tdb: _tdb:CoSb-08Zha.tdb:COSB2_C18, tdb:CoSb-09Zha.tdb:COSB2_C18, tdb:CoSb-19Gie.tdb:COSB2_C18, tdb:CoSb-20Bro.tdb:COSB2_C18  


### TDB models of COSB2_C18 (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): COSB2_C18, type code %, sha256 `877e8f1ac13a2869…`

~~~~text
50: PHASE COSB2_C18 % 2 0.3333 0.6667 !
51: CONST COSB2_C18 : CO : SB : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): COSB2_C18, type code %, sha256 `1d903c43e17f1a21…`

~~~~text
53: PHASE COSB2_C18 % 2 0.3333 0.6667 !
54: CONST COSB2_C18 : CO : SB : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): COSB2_C18, type code %, sha256 `73b6e1ed6d86564b…`

~~~~text
52: PHASE COSB2_C18 % 2 1 2 !
53: CONST COSB2_C18 : CO : SB : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): COSB2_C18, type code %, sha256 `bdb612f140be29a9…`

~~~~text
52: PHASE COSB2_C18 % 2 0.3333 0.6667 !
53: CONST COSB2_C18 : CO : SB : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080590131](https://doi.org/10.1002/zaac.19080590131) Kurt Lewkonja, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXV. Über die Legierungen des Kobalts mit Zinn, Antimon, Blei, Wismut, Thallium, Zink, Cadmium, Chrom und Silicium, Z. Anorg. Chem. 59, 293-345 (1908).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645725](https://doi.org/10.1007/bf02645725) H Okamoto, Co-Sb (Cobalt-Antimony), JPE 12, 244-245 (1991).  
_cited as the source of values for this phase_
- [doi:10.1007/bf03029292](https://doi.org/10.1007/bf03029292) K. Ishida, T. Nishizawa, Bull. Alloy Phase Diagrams 11 (1990) 243–248.  
_cited as the source of values for this phase_

## COSB3_D02 (Co–Sb)

- Id: `phase:co-sb:cosb3-d02`; status `assigned`
- Structure: CoAs3 · D0_2 · cI32 · Im-3 (204); type `st:d0-2-coas3-ci32`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabyr and oqmd-6414, space group 204
- Stoichiometry: Co 0.2500, Sb 0.7500
- Stability: stable in 4 of 4 calculated diagram(s): 300–1147.13 K, x(Sb) 0.75–0.75
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:cosb3-d02)

Names (8): _corpus: _corpus:phase:co-sb:cosb3-d02  
_mp: _mp:mp-aaaaabyr  
_oqmd: _oqmd:oqmd-6414  
_paper: _paper:10.1016/j.calphad.2007.11.001:δCoSb3  
_tdb: _tdb:CoSb-08Zha.tdb:COSB3_D02, tdb:CoSb-09Zha.tdb:COSB3_D02, tdb:CoSb-19Gie.tdb:COSB3_D02, tdb:CoSb-20Bro.tdb:COSB3_D02  


### TDB models of COSB3_D02 (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): COSB3_D02, type code %, sha256 `877e8f1ac13a2869…`

~~~~text
60: PHASE COSB3_D02 % 2 0.25 0.75 !
61: CONST COSB3_D02 : CO : SB : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): COSB3_D02, type code %, sha256 `1d903c43e17f1a21…`

~~~~text
63: PHASE COSB3_D02 % 2 0.25 0.75 !
64: CONST COSB3_D02 : CO : SB : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): COSB3_D02, type code %, sha256 `73b6e1ed6d86564b…`

~~~~text
62: PHASE COSB3_D02 % 2 1 3 !
63: CONST COSB3_D02 : CO : SB : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): COSB3_D02, type code %, sha256 `bdb612f140be29a9…`

~~~~text
62: PHASE COSB3_D02 % 2 0.25 0.75 !
63: CONST COSB3_D02 : CO : SB : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_
- [doi:10.1007/bf03029292](https://doi.org/10.1007/bf03029292) K. Ishida, T. Nishizawa, Bull. Alloy Phase Diagrams 11 (1990) 243–248.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080590131](https://doi.org/10.1002/zaac.19080590131) Kurt Lewkonja, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXV. Über die Legierungen des Kobalts mit Zinn, Antimon, Blei, Wismut, Thallium, Zink, Cadmium, Chrom und Silicium, Z. Anorg. Chem. 59, 293-345 (1908).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
_cited as the source of values for this phase_

## FCC_A1 (Co–Sb)

- Id: `phase:co-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 620–1772.98 K, x(Sb) 0–0.03902
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:fcc-a1)

Names (6): _corpus: _corpus:phase:co-sb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2007.11.001:(αCo)  
_tdb: _tdb:CoSb-08Zha.tdb:FCC_A1, tdb:CoSb-09Zha.tdb:FCC_A1, tdb:CoSb-19Gie.tdb:FCC_A1, tdb:CoSb-20Bro.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): FCC_A1, type code %A, sha256 `877e8f1ac13a2869…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% SB : VA : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): FCC_A1, type code %A, sha256 `1d903c43e17f1a21…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% SB : VA : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): FCC_A1, type code %A, sha256 `73b6e1ed6d86564b…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% SB : VA : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): FCC_A1, type code %A, sha256 `bdb612f140be29a9…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% SB : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080590131](https://doi.org/10.1002/zaac.19080590131) Kurt Lewkonja, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXV. Über die Legierungen des Kobalts mit Zinn, Antimon, Blei, Wismut, Thallium, Zink, Cadmium, Chrom und Silicium, Z. Anorg. Chem. 59, 293-345 (1908).  
_cited as the source of values for this phase_
- [doi:10.1007/bf03029292](https://doi.org/10.1007/bf03029292) K. Ishida, T. Nishizawa, Bull. Alloy Phase Diagrams 11 (1990) 243–248.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1937.1.5_177](https://doi.org/10.2320/jinstmet1937.1.5_177) Uichi Haschimoto, Relation between the Allotropic Transformation of Cobalt and Some Additional Elements, J.Japan Inst.Metals 1, 177-190 (1937).  
_cited as the source of values for this phase_

## HCP_A3 (Co–Sb)

- Id: `phase:co-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–695.24 K, x(Sb) 0–6e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:hcp-a3)

Names (5): _corpus: _corpus:phase:co-sb:hcp-a3  
_tdb: _tdb:CoSb-08Zha.tdb:HCP_A3, tdb:CoSb-09Zha.tdb:HCP_A3, tdb:CoSb-19Gie.tdb:HCP_A3, tdb:CoSb-20Bro.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): HCP_A3, type code %A, sha256 `877e8f1ac13a2869…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CO% SB : VA : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): HCP_A3, type code %A, sha256 `1d903c43e17f1a21…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% SB : VA : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): HCP_A3, type code %A, sha256 `73b6e1ed6d86564b…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CO% SB : VA : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): HCP_A3, type code %A, sha256 `bdb612f140be29a9…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CO% SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_

## LIQUID (Co–Sb)

- Id: `phase:co-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 901.33–2500 K, x(Sb) 0–1
- Literature: 41 values (41 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sb:liquid)

Names (7): _corpus: _corpus:phase:co-sb:liquid  
_paper: _paper:10.1007/s11661-019-05288-9:Liquid, paper:10.1016/j.calphad.2007.11.001:Liq  
_tdb: _tdb:CoSb-08Zha.tdb:LIQUID, tdb:CoSb-09Zha.tdb:LIQUID, tdb:CoSb-19Gie.tdb:LIQUID, tdb:CoSb-20Bro.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CoSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-08Zha.tdb): LIQUID, type code %, sha256 `877e8f1ac13a2869…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO SB : !
~~~~

[CoSb-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-09Zha.tdb): LIQUID, type code %, sha256 `1d903c43e17f1a21…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO SB : !
~~~~

[CoSb-19Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-19Gie.tdb): LIQUID, type code %, sha256 `73b6e1ed6d86564b…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO SB : !
~~~~

[CoSb-20Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSb-20Bro.tdb): LIQUID, type code %, sha256 `bdb612f140be29a9…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO SB : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.calphad.2007.11.001](https://doi.org/10.1016/j.calphad.2007.11.001) Yubi Zhang, Changrong Li, Zhenmin Du, Tai Geng, The thermodynamic assessment of the Co–Sb system, Calphad 32, 56-63 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-019-05288-9](https://doi.org/10.1007/s11661-019-05288-9) Wojciech Gierlotka, Sinn-wen Chen, Ssu-ming Tseng, Po-han Lin, Co-In-Sb Ternary System (II): Isoplethal Section and Thermodynamic Modeling, Metall Mater Trans A 50, 3891-3902 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.12.004](https://doi.org/10.1016/j.calphad.2008.12.004) Y. Zhang, C. Li, Z. Du, C. Guo, J.-C. Tedenac, Calphad, 33, 405-14(2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101694](https://doi.org/10.1016/j.calphad.2019.101694) P. Broz, F. Zelenka, J. Vrestal, A. Zemanova, A. Kroupa, J. Bursik, M. Svoboda, L. Simonikova, T. Pokorny, Calphad, 68, 101694(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1002/srin.193900887](https://doi.org/10.1002/srin.193900887) Werner Geller, Das System Eisen‐Kobalt‐Antimon, Steel Research Intl 13, 263-266 (1939).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080590131](https://doi.org/10.1002/zaac.19080590131) Kurt Lewkonja, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXV. Über die Legierungen des Kobalts mit Zinn, Antimon, Blei, Wismut, Thallium, Zink, Cadmium, Chrom und Silicium, Z. Anorg. Chem. 59, 293-345 (1908).  
_cited as the source of values for this phase_
- [doi:10.1007/bf03029292](https://doi.org/10.1007/bf03029292) K. Ishida, T. Nishizawa, Bull. Alloy Phase Diagrams 11 (1990) 243–248.  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645725](https://doi.org/10.1007/bf02645725) H Okamoto, Co-Sb (Cobalt-Antimony), JPE 12, 244-245 (1991).  
_cited as the source of values for this phase_

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
