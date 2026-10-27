# Cr–Ge phases

> Cr–Ge system: 11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-GE.html · Markdown: https://data.orchid-project.org/phases/pages/CR-GE.md

11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-GE) · [full JSON](https://data.orchid-project.org/phases/systems/CR-GE.json) · [Cr–Ge system page](https://data.orchid-project.org/systems/CR-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Ge system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-cr-ge-a4-diamond); _phase:cr-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(Ge) 0.99413–1 | 9 | 3 |
| [BCC_A2](#phase-cr-ge-bcc-a2); _phase:cr-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2179.98 K, x(Ge) 0–0.11906 | 8 | 3 |
| [CR11GE19](#phase-cr-ge-cr11ge19); _phase:cr-ge:cr11ge19_ | Mn11Si19 · tP120 · P-4n2 (118) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1201.42 K, x(Ge) 0.63333–0.63333 | 27 | 3 |
| [CR11GE8](#phase-cr-ge-cr11ge8); _phase:cr-ge:cr11ge8_ | Cr11Ge8 · oP76 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1459.64 K, x(Ge) 0.42105–0.42105 | 31 | 3 |
| [CR3GE_A15](#phase-cr-ge-cr3ge-a15); _phase:cr-ge:cr3ge-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1842.19 K, x(Ge) 0.20096–0.25258 | 22 | 3 |
| [CR5GE3_LT](#phase-cr-ge-cr5ge3); _phase:cr-ge:cr5ge3_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1275.13 K, x(Ge) 0.37497–0.38218 | 11 | 2 |
| [CR5GE3_D8M](#phase-cr-ge-cr5ge3-d8m); _phase:cr-ge:cr5ge3-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1274.97–1535.51 K, x(Ge) 0.37229–0.39556 | 19 | 3 |
| [CRGE_B20](#phase-cr-ge-crge-b20); _phase:cr-ge:crge-b20_ | FeSi · B20 · cP8 · P2_13 (198) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1271.38 K, x(Ge) 0.5–0.5 | 22 | 3 |
| [FCC_A1](#phase-cr-ge-fcc-a1); _phase:cr-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-cr-ge-hcp-a3); _phase:cr-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-cr-ge-liquid); _phase:cr-ge:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1167.91–4000 K, x(Ge) 0–1 | 58 | 3 |

## DIAMOND_A4 (Cr–Ge)

- Id: `phase:cr-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(Ge) 0.99413–1
- Literature: 9 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:a4-diamond)

Names (7): _corpus: _corpus:phase:cr-ge:a4-diamond, corpus:phase:cr-ge:diamond-a4  
_paper: _paper:10.1016/j.calphad.2009.11.001:(Ge), paper:10.1016/j.jallcom.2009.03.113:diamond  
_tdb: _tdb:CrGe-09Li.tdb:DIAMOND_A4, tdb:CrGe-10Liu.tdb:DIAMOND_A4, tdb:CrGe-15Ber.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): DIAMOND_A4, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : CR GE% : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): DIAMOND_A4, type code %, sha256 `b68d91b4d452158f…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : GE : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): DIAMOND_A4, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : GE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf01140038](https://doi.org/10.1007/bf01140038) V. L. Zagryazhskii, A. K. Shtol'ts, P. V. Gel'd, N. V. Kuz'menko, Phase diagram of the system chromium-germanium, Powder Metall Met Ceram 5, 639-642 (1966).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_

## BCC_A2 (Cr–Ge)

- Id: `phase:cr-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2179.98 K, x(Ge) 0–0.11906
- Literature: 8 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:bcc-a2)

Names (6): _corpus: _corpus:phase:cr-ge:bcc-a2  
_paper: _paper:10.1016/j.calphad.2009.11.001:(Cr), paper:10.1016/j.jallcom.2009.03.113:bcc  
_tdb: _tdb:CrGe-09Li.tdb:BCC_A2, tdb:CrGe-10Liu.tdb:BCC_A2, tdb:CrGe-15Ber.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): BCC_A2, type code %B, sha256 `aedc0d72de39cc0c…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CR% GE : VA : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): BCC_A2, type code %B, sha256 `b68d91b4d452158f…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CR% GE : VA : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): BCC_A2, type code %B, sha256 `78ffe8b34babcfc8…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : CR% GE : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_

## CR11GE19 (Cr–Ge)

- Id: `phase:cr-ge:cr11ge19`; status `assigned`
- Structure: Mn11Si19 · tP120 · P-4n2 (118); type `st:mn11si19-tp120`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cr 0.3667, Ge 0.6333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1201.42 K, x(Ge) 0.63333–0.63333
- Literature: 27 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:cr11ge19)

Names (6): _corpus: _corpus:phase:cr-ge:cr11ge19  
_paper: _paper:10.1016/j.calphad.2009.11.001:Cr11Ge19, paper:10.1016/j.jallcom.2009.03.113:Cr11Ge19  
_tdb: _tdb:CrGe-09Li.tdb:CR11GE19, tdb:CrGe-10Liu.tdb:CR11GE19, tdb:CrGe-15Ber.tdb:CR11GE19  


### TDB models of CR11GE19 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): CR11GE19, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
76: PHASE CR11GE19 % 2 11 19 !
77: CONST CR11GE19 : CR : GE : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): CR11GE19, type code %, sha256 `b68d91b4d452158f…`

~~~~text
78: PHASE CR11GE19 % 2 11 19 !
79: CONST CR11GE19 : CR : GE : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): CR11GE19, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
77: PHASE CR11GE19 % 2 11 19 !
78: CONST CR11GE19 : CR : GE : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1007/bf01140038](https://doi.org/10.1007/bf01140038) V. L. Zagryazhskii, A. K. Shtol'ts, P. V. Gel'd, N. V. Kuz'menko, Phase diagram of the system chromium-germanium, Powder Metall Met Ceram 5, 639-642 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1143/jjap.17.2173](https://doi.org/10.1143/jjap.17.2173) Iwao Kawasumi, Satoshi Konishi, Masayoshi Kubota, Makoto Sakata, Phase Analysis and Some Physical Properties of the Higher Chromium Germanides, Jpn. J. Appl. Phys. 17, 2173-2174 (1978).  
_cited as the source of values for this phase_

## CR11GE8 (Cr–Ge)

- Id: `phase:cr-ge:cr11ge8`; status `assigned`
- Structure: Cr11Ge8 · oP76 · Pnma (62); type `st:cr11ge8-op76`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cr 0.5789, Ge 0.4211
- Stability: stable in 3 of 3 calculated diagram(s): 300–1459.64 K, x(Ge) 0.42105–0.42105
- Literature: 31 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:cr11ge8)

Names (6): _corpus: _corpus:phase:cr-ge:cr11ge8  
_paper: _paper:10.1016/j.calphad.2009.11.001:Cr11Ge8, paper:10.1016/j.jallcom.2009.03.113:Cr11Ge8  
_tdb: _tdb:CrGe-09Li.tdb:CR11GE8, tdb:CrGe-10Liu.tdb:CR11GE8, tdb:CrGe-15Ber.tdb:CR11GE8  


### TDB models of CR11GE8 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): CR11GE8, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
66: PHASE CR11GE8 % 2 11 8 !
67: CONST CR11GE8 : CR : GE : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): CR11GE8, type code %, sha256 `b68d91b4d452158f…`

~~~~text
68: PHASE CR11GE8 % 2 11 8 !
69: CONST CR11GE8 : CR : GE : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): CR11GE8, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
67: PHASE CR11GE8 % 2 11 8 !
68: CONST CR11GE8 : CR : GE : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1007/bf01140038](https://doi.org/10.1007/bf01140038) V. L. Zagryazhskii, A. K. Shtol'ts, P. V. Gel'd, N. V. Kuz'menko, Phase diagram of the system chromium-germanium, Powder Metall Met Ceram 5, 639-642 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(98)00011-9](https://doi.org/10.1016/s0966-9795%2898%2900011-9) A Yassin, R Castanet, Calorimetric study of Cr-Ge alloys, Intermetallics 7, 79-82 (1999).  
_cited as the source of values for this phase_
- [doi:10.1143/jjap.17.2173](https://doi.org/10.1143/jjap.17.2173) Iwao Kawasumi, Satoshi Konishi, Masayoshi Kubota, Makoto Sakata, Phase Analysis and Some Physical Properties of the Higher Chromium Germanides, Jpn. J. Appl. Phys. 17, 2173-2174 (1978).  
_cited as the source of values for this phase_

## CR3GE_A15 (Cr–Ge)

- Id: `phase:cr-ge:cr3ge-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrGe-10Liu.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1842.19 K, x(Ge) 0.20096–0.25258
- Literature: 22 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:cr3ge-a15)

Names (7): _corpus: _corpus:phase:cr-ge:cr3ge-a15  
_paper: _paper:10.1016/j.calphad.2009.11.001:Cr3Ge, paper:10.1016/j.jallcom.2009.03.113:Cr3G, paper:10.1016/j.jallcom.2009.03.113:Cr3Ge  
_tdb: _tdb:CrGe-09Li.tdb:CR3GE_A15, tdb:CrGe-10Liu.tdb:CR3GE_A15, tdb:CrGe-15Ber.tdb:CR3GE_A15  


### TDB models of CR3GE_A15 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): CR3GE_A15, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
51: PHASE CR3GE_A15 % 2 3 1 !
52: CONST CR3GE_A15 : CR : CR GE% : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): CR3GE_A15, type code %, sha256 `b68d91b4d452158f…`

~~~~text
53: PHASE CR3GE_A15 % 2 3 1 !
54: CONST CR3GE_A15 : CR% GE : CR GE% : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): CR3GE_A15, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
57: PHASE CR3GE_A15 % 2 3 1 !
58: CONST CR3GE_A15 : CR : CR GE% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1007/bf01140038](https://doi.org/10.1007/bf01140038) V. L. Zagryazhskii, A. K. Shtol'ts, P. V. Gel'd, N. V. Kuz'menko, Phase diagram of the system chromium-germanium, Powder Metall Met Ceram 5, 639-642 (1966).  
_cited as the source of values for this phase_

## CR5GE3_LT (Cr–Ge)

- Id: `phase:cr-ge:cr5ge3`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cr5Ge3) · - — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cr5Ge3) · - — Hallstedt 2025 mmc2 row for CR5GE3_LT: Cr5Ge3 (low T, probably does not exist)
- Stability: stable in 2 of 2 calculated diagram(s): 300–1275.13 K, x(Ge) 0.37497–0.38218
- Literature: 11 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:cr5ge3)

Names (6): _corpus: _corpus:phase:cr-ge:cr5ge3, corpus:phase:cr-ge:cr5ge3-lt  
_paper: _paper:10.1016/j.calphad.2009.11.001:αCr5Ge3, paper:10.1016/j.jallcom.2009.03.113:αCr5Ge3  
_tdb: _tdb:CrGe-09Li.tdb:CR5GE3_LT, tdb:CrGe-10Liu.tdb:CR5GE3_LT  


### TDB models of CR5GE3_LT (2): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): CR5GE3_LT, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
56: PHASE CR5GE3_LT % 2 5 3 !
57: CONST CR5GE3_LT : CR% GE : GE : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): CR5GE3_LT, type code %, sha256 `b68d91b4d452158f…`

~~~~text
63: PHASE CR5GE3_LT % 2 5 3 !
64: CONST CR5GE3_LT : CR% GE : CR GE% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_

## CR5GE3_D8M (Cr–Ge)

- Id: `phase:cr-ge:cr5ge3-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrGe-10Liu.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 1274.97–1535.51 K, x(Ge) 0.37229–0.39556
- Literature: 19 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:cr5ge3-d8m)

Names (5): _corpus: _corpus:phase:cr-ge:cr5ge3-d8m  
_paper: _paper:10.1016/j.jallcom.2009.03.113:βCr5Ge3  
_tdb: _tdb:CrGe-09Li.tdb:CR5GE3_D8M, tdb:CrGe-10Liu.tdb:CR5GE3_D8M, tdb:CrGe-15Ber.tdb:CR5GE3_D8M  


### TDB models of CR5GE3_D8M (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): CR5GE3_D8M, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
61: PHASE CR5GE3_D8M % 2 5 3 !
62: CONST CR5GE3_D8M : CR% GE : GE : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): CR5GE3_D8M, type code %, sha256 `b68d91b4d452158f…`

~~~~text
58: PHASE CR5GE3_D8M % 2 5 3 !
59: CONST CR5GE3_D8M : CR% GE : CR GE% : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): CR5GE3_D8M, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
62: PHASE CR5GE3_D8M % 2 5 3 !
63: CONST CR5GE3_D8M : CR% GE : GE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_

## CRGE_B20 (Cr–Ge)

- Id: `phase:cr-ge:crge-b20`; status `assigned`
- Structure: FeSi · B20 · cP8 · P2_13 (198); type `st:b20-fesi-cp8`; tier A: standard phase name; confidence high
- Stoichiometry: Cr 0.5000, Ge 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1271.38 K, x(Ge) 0.5–0.5
- Literature: 22 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:crge-b20)

Names (6): _corpus: _corpus:phase:cr-ge:crge-b20  
_paper: _paper:10.1016/j.calphad.2009.11.001:CrGe, paper:10.1016/j.jallcom.2009.03.113:CrGe  
_tdb: _tdb:CrGe-09Li.tdb:CRGE_B20, tdb:CrGe-10Liu.tdb:CRGE_B20, tdb:CrGe-15Ber.tdb:CRGE_B20  


### TDB models of CRGE_B20 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): CRGE_B20, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
71: PHASE CRGE_B20 % 2 1 1 !
72: CONST CRGE_B20 : CR : GE : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): CRGE_B20, type code %, sha256 `b68d91b4d452158f…`

~~~~text
73: PHASE CRGE_B20 % 2 1 1 !
74: CONST CRGE_B20 : CR : GE : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): CRGE_B20, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
72: PHASE CRGE_B20 % 2 1 1 !
73: CONST CRGE_B20 : CR : GE : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf01140038](https://doi.org/10.1007/bf01140038) V. L. Zagryazhskii, A. K. Shtol'ts, P. V. Gel'd, N. V. Kuz'menko, Phase diagram of the system chromium-germanium, Powder Metall Met Ceram 5, 639-642 (1966).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1143/jjap.17.2173](https://doi.org/10.1143/jjap.17.2173) Iwao Kawasumi, Satoshi Konishi, Masayoshi Kubota, Makoto Sakata, Phase Analysis and Some Physical Properties of the Higher Chromium Germanides, Jpn. J. Appl. Phys. 17, 2173-2174 (1978).  
_cited as the source of values for this phase_

## FCC_A1 (Cr–Ge)

- Id: `phase:cr-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:fcc-a1)

Names (4): _corpus: _corpus:phase:cr-ge:fcc-a1  
_tdb: _tdb:CrGe-09Li.tdb:FCC_A1, tdb:CrGe-10Liu.tdb:FCC_A1, tdb:CrGe-15Ber.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): FCC_A1, type code %A, sha256 `aedc0d72de39cc0c…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CR GE : VA : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): FCC_A1, type code %A, sha256 `b68d91b4d452158f…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CR GE : VA : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): FCC_A1, type code %A, sha256 `78ffe8b34babcfc8…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : CR GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase_

## HCP_A3 (Cr–Ge)

- Id: `phase:cr-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:hcp-a3)

Names (4): _corpus: _corpus:phase:cr-ge:hcp-a3  
_tdb: _tdb:CrGe-09Li.tdb:HCP_A3, tdb:CrGe-10Liu.tdb:HCP_A3, tdb:CrGe-15Ber.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): HCP_A3, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : CR GE : VA : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): HCP_A3, type code %, sha256 `b68d91b4d452158f…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : CR GE : VA : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): HCP_A3, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
47: PHASE HCP_A3 % 2 1 0.5 !
48: CONST HCP_A3 : CR GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase_

## LIQUID (Cr–Ge)

- Id: `phase:cr-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1167.91–4000 K, x(Ge) 0–1
- Literature: 58 values (43 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ge:liquid)

Names (6): _corpus: _corpus:phase:cr-ge:liquid  
_paper: _paper:10.1016/j.calphad.2009.11.001:L, paper:10.1016/j.jallcom.2009.03.113:liq  
_tdb: _tdb:CrGe-09Li.tdb:LIQUID, tdb:CrGe-10Liu.tdb:LIQUID, tdb:CrGe-15Ber.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CrGe-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-09Li.tdb): LIQUID, type code %, sha256 `aedc0d72de39cc0c…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CR GE : !
~~~~

[CrGe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-10Liu.tdb): LIQUID, type code %, sha256 `b68d91b4d452158f…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CR GE CR3GE : !
~~~~

[CrGe-15Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGe-15Ber.tdb): LIQUID, type code %, sha256 `78ffe8b34babcfc8…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : CR GE CR3GE : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.113](https://doi.org/10.1016/j.jallcom.2009.03.113) Mei Li, Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic description of the Cr–Ge system, Journal of Alloys and Compounds 481, 283-290 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.11.001](https://doi.org/10.1016/j.calphad.2009.11.001) Y.Q. Liu, Y. Du, Thermodynamic description of the Cr–Ge system, Calphad 34, 26-35 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.02.004](https://doi.org/10.1016/j.calphad.2015.02.004) A. Berche, J.C. Tédenac, P. Jund, Ab-initio calculations and CALPHAD description of Cr–Ge–Mn and Cr–Ge–Si, Calphad 49, 50-57 (2015).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(80)90248-9](https://doi.org/10.1016/0022-5088%2880%2990248-9) D. Godat, P. Feschotte, Diagramme de phase du système chrome-germanium, Journal of the Less Common Metals 72, 7-22 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02867813](https://doi.org/10.1007/bf02867813) A.B. Gokhale, G.J. Abbaschian, Bull. Alloy Phase Diagram 7 (1986) 477.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1007/bf01140038](https://doi.org/10.1007/bf01140038) V. L. Zagryazhskii, A. K. Shtol'ts, P. V. Gel'd, N. V. Kuz'menko, Phase diagram of the system chromium-germanium, Powder Metall Met Ceram 5, 639-642 (1966).  
_cited as the source of values for this phase_
- [doi:10.1143/jjap.17.2173](https://doi.org/10.1143/jjap.17.2173) Iwao Kawasumi, Satoshi Konishi, Masayoshi Kubota, Makoto Sakata, Phase Analysis and Some Physical Properties of the Higher Chromium Germanides, Jpn. J. Appl. Phys. 17, 2173-2174 (1978).  
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
