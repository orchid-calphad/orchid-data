# Nb–Sn phases

> Nb–Sn system: 9 phases (tier A 7, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-SN.html · Markdown: https://data.orchid-project.org/phases/pages/NB-SN.md

9 phases (tier A 7, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-SN) · [full JSON](https://data.orchid-project.org/phases/systems/NB-SN.json) · [Nb–Sn system page](https://data.orchid-project.org/systems/NB-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Sn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-nb-sn-a4-diamond); _phase:nb-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [BCT_A5](#phase-nb-sn-a5-bct); _phase:nb-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 11 | 3 |
| [BCC_A2](#phase-nb-sn-bcc-a2); _phase:nb-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2751 K, x(Sn) 0–0.12045 | 17 | 3 |
| [FCC_A1](#phase-nb-sn-fcc-a1); _phase:nb-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-nb-sn-hcp-a3); _phase:nb-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-nb-sn-liquid); _phase:nb-sn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1 | 52 | 3 |
| [NB3SN_A15](#phase-nb-sn-nb3sn-a15); _phase:nb-sn:nb3sn-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2425.38 K, x(Sn) 0.14315–0.33288 | 38 | 3 |
| [NB6SN5](#phase-nb-sn-nb6sn5); _phase:nb-sn:nb6sn5_ | Sn5Ti6-alpha · oI44 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 992.31–1296.88 K, x(Sn) 0.44957–0.45455 | 37 | 3 |
| [NBSN2_CB](#phase-nb-sn-nbsn2-cb); _phase:nb-sn:nbsn2-cb_ | CuMg2 · C_b · oF48 · Fddd (70) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1141.38 K, x(Sn) 0.66667–0.66667 | 32 | 3 |

## DIAMOND_A4 (Nb–Sn)

- Id: `phase:nb-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:a4-diamond)

Names (4): _corpus: _corpus:phase:nb-sn:a4-diamond  
_tdb: _tdb:NbSn-02Tof.tdb:DIAMOND_A4, tdb:NbSn-17Laf.tdb:DIAMOND_A4, tdb:NbSn-98Tof.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): DIAMOND_A4, type code %, sha256 `28d911b942daf434…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): DIAMOND_A4, type code %, sha256 `fe83573ddf9ba2bf…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): DIAMOND_A4, type code %, sha256 `7c50a914635b9aaf…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase_

## BCT_A5 (Nb–Sn)

- Id: `phase:nb-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:a5-bct)

Names (7): _corpus: _corpus:phase:nb-sn:a5-bct, corpus:phase:nb-sn:bct-a5  
_paper: _paper:10.1361/1054971023604071:Snbct_A5, paper:10.1361/105497198770341978:Snbct_A5  
_tdb: _tdb:NbSn-02Tof.tdb:BCT_A5, tdb:NbSn-17Laf.tdb:BCT_A5, tdb:NbSn-98Tof.tdb:BCT_A5  


### TDB models of BCT_A5 (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): BCT_A5, type code %, sha256 `28d911b942daf434…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : SN : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): BCT_A5, type code %, sha256 `fe83573ddf9ba2bf…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : SN : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): BCT_A5, type code %, sha256 `7c50a914635b9aaf…`

~~~~text
54: PHASE BCT_A5 % 1 1 !
55: CONST BCT_A5 : SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1007/bf00554367](https://doi.org/10.1007/bf00554367) J. P. Charlesworth, I. Macphail, P. E. Madsen, Experimental work on the niobium-tin constitution diagram and related studies, J Mater Sci 5, 580-603 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90018-9](https://doi.org/10.1016/0022-5088%2864%2990018-9) Thomas G Ellis, Harley A Wilhelm, Phase equilibria and crystallography for the niobium-tin system, Journal of the Less Common Metals 7, 67-83 (1964).  
_cited as the source of values for this phase_

## BCC_A2 (Nb–Sn)

- Id: `phase:nb-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2751 K, x(Sn) 0–0.12045
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:bcc-a2)

Names (6): _corpus: _corpus:phase:nb-sn:bcc-a2  
_paper: _paper:10.1361/1054971023604071:Nb(bcc), paper:10.1361/105497198770341978:Nbbcc_A2  
_tdb: _tdb:NbSn-02Tof.tdb:BCC_A2, tdb:NbSn-17Laf.tdb:BCC_A2, tdb:NbSn-98Tof.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): BCC_A2, type code %B, sha256 `28d911b942daf434…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NB% SN : VA : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): BCC_A2, type code %B, sha256 `fe83573ddf9ba2bf…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% SN : VA : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): BCC_A2, type code %B, sha256 `7c50a914635b9aaf…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : NB% SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1007/bf00554367](https://doi.org/10.1007/bf00554367) J. P. Charlesworth, I. Macphail, P. E. Madsen, Experimental work on the niobium-tin constitution diagram and related studies, J Mater Sci 5, 580-603 (1970).  
_cited as the source of values for this phase_

## FCC_A1 (Nb–Sn)

- Id: `phase:nb-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:fcc-a1)

Names (4): _corpus: _corpus:phase:nb-sn:fcc-a1  
_tdb: _tdb:NbSn-02Tof.tdb:FCC_A1, tdb:NbSn-17Laf.tdb:FCC_A1, tdb:NbSn-98Tof.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): FCC_A1, type code %A, sha256 `28d911b942daf434…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NB SN : VA : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): FCC_A1, type code %A, sha256 `fe83573ddf9ba2bf…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB SN : VA : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): FCC_A1, type code %A, sha256 `7c50a914635b9aaf…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : NB SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase_

## HCP_A3 (Nb–Sn)

- Id: `phase:nb-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:hcp-a3)

Names (4): _corpus: _corpus:phase:nb-sn:hcp-a3  
_tdb: _tdb:NbSn-02Tof.tdb:HCP_A3, tdb:NbSn-17Laf.tdb:HCP_A3, tdb:NbSn-98Tof.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): HCP_A3, type code %A, sha256 `28d911b942daf434…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NB SN : VA: !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): HCP_A3, type code %A, sha256 `fe83573ddf9ba2bf…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB SN : VA: !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): HCP_A3, type code %A, sha256 `7c50a914635b9aaf…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : NB SN : VA: !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase_

## LIQUID (Nb–Sn)

- Id: `phase:nb-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1
- Literature: 52 values (52 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:liquid)

Names (6): _corpus: _corpus:phase:nb-sn:liquid  
_paper: _paper:10.1361/1054971023604071:L, paper:10.1361/105497198770341978:L  
_tdb: _tdb:NbSn-02Tof.tdb:LIQUID, tdb:NbSn-17Laf.tdb:LIQUID, tdb:NbSn-98Tof.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): LIQUID, type code %, sha256 `28d911b942daf434…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NB SN : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): LIQUID, type code %, sha256 `fe83573ddf9ba2bf…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB SN : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): LIQUID, type code %, sha256 `7c50a914635b9aaf…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : NB SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1007/bf00554367](https://doi.org/10.1007/bf00554367) J. P. Charlesworth, I. Macphail, P. E. Madsen, Experimental work on the niobium-tin constitution diagram and related studies, J Mater Sci 5, 580-603 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90018-9](https://doi.org/10.1016/0022-5088%2864%2990018-9) Thomas G Ellis, Harley A Wilhelm, Phase equilibria and crystallography for the niobium-tin system, Journal of the Less Common Metals 7, 67-83 (1964).  
_cited as the source of values for this phase_

## NB3SN_A15 (Nb–Sn)

- Id: `phase:nb-sn:nb3sn-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbSn-02Tof.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbSn-17Laf.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbSn-98Tof.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–2425.38 K, x(Sn) 0.14315–0.33288
- Literature: 38 values (38 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:nb3sn-a15)

Names (6): _corpus: _corpus:phase:nb-sn:nb3sn-a15  
_paper: _paper:10.1361/1054971023604071:Nb3Sn, paper:10.1361/105497198770341978:Nb3Sn  
_tdb: _tdb:NbSn-02Tof.tdb:NB3SN_A15, tdb:NbSn-17Laf.tdb:NB3SN_A15, tdb:NbSn-98Tof.tdb:NB3SN_A15  


### TDB models of NB3SN_A15 (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): NB3SN_A15, type code %, sha256 `28d911b942daf434…`

~~~~text
56: PHASE NB3SN_A15 %  2 3 1 !
57: CONST NB3SN_A15 : NB% SN : NB SN% : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): NB3SN_A15, type code %, sha256 `fe83573ddf9ba2bf…`

~~~~text
52: PHASE NB3SN_A15 %  2 3 1 !
53: CONST NB3SN_A15 : NB% SN : NB SN% : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): NB3SN_A15, type code %, sha256 `7c50a914635b9aaf…`

~~~~text
59: PHASE NB3SN_A15 %  2 3 1 !
60: CONST NB3SN_A15 : NB% SN : NB SN% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1007/bf00554367](https://doi.org/10.1007/bf00554367) J. P. Charlesworth, I. Macphail, P. E. Madsen, Experimental work on the niobium-tin constitution diagram and related studies, J Mater Sci 5, 580-603 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90018-9](https://doi.org/10.1016/0022-5088%2864%2990018-9) Thomas G Ellis, Harley A Wilhelm, Phase equilibria and crystallography for the niobium-tin system, Journal of the Less Common Metals 7, 67-83 (1964).  
_cited as the source of values for this phase_

## NB6SN5 (Nb–Sn)

- Id: `phase:nb-sn:nb6sn5`; status `assigned`
- Structure: Sn5Ti6-alpha · oI44 · Immm (71); type `st:sn5ti6-alpha-oi44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 992.31–1296.88 K, x(Sn) 0.44957–0.45455
- Literature: 37 values (37 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:nb6sn5)

Names (6): _corpus: _corpus:phase:nb-sn:nb6sn5  
_paper: _paper:10.1361/1054971023604071:Nb6Sn5, paper:10.1361/105497198770341978:Nb6Sn5  
_tdb: _tdb:NbSn-02Tof.tdb:NB6SN5, tdb:NbSn-17Laf.tdb:NB6SN5, tdb:NbSn-98Tof.tdb:NB6SN5  


### TDB models of NB6SN5 (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): NB6SN5, type code %, sha256 `28d911b942daf434…`

~~~~text
61: PHASE NB6SN5 %  3 24 16 4 !
62: CONST NB6SN5 : NB : SN : NB SN : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): NB6SN5, type code %, sha256 `fe83573ddf9ba2bf…`

~~~~text
57: PHASE NB6SN5 %  2 6 5 !
58: CONST NB6SN5 : NB : SN : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): NB6SN5, type code %, sha256 `7c50a914635b9aaf…`

~~~~text
64: PHASE NB6SN5 %  3 24 16 4 !
65: CONST NB6SN5 : NB : SN : NB SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1007/bf00554367](https://doi.org/10.1007/bf00554367) J. P. Charlesworth, I. Macphail, P. E. Madsen, Experimental work on the niobium-tin constitution diagram and related studies, J Mater Sci 5, 580-603 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90018-9](https://doi.org/10.1016/0022-5088%2864%2990018-9) Thomas G Ellis, Harley A Wilhelm, Phase equilibria and crystallography for the niobium-tin system, Journal of the Less Common Metals 7, 67-83 (1964).  
_cited as the source of values for this phase_

## NBSN2_CB (Nb–Sn)

- Id: `phase:nb-sn:nbsn2-cb`; status `assigned`
- Structure: CuMg2 · C_b · oF48 · Fddd (70); type `st:c-b-cumg2-of48`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabog and oqmd-17753, space group 70
- Stoichiometry: Nb 0.3333, Sn 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1141.38 K, x(Sn) 0.66667–0.66667
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-sn:nbsn2-cb)

Names (8): _corpus: _corpus:phase:nb-sn:nbsn2-cb  
_mp: _mp:mp-aaaaabog  
_oqmd: _oqmd:oqmd-17753  
_paper: _paper:10.1361/1054971023604071:NbSn2, paper:10.1361/105497198770341978:NbSn2  
_tdb: _tdb:NbSn-02Tof.tdb:NBSN2_CB, tdb:NbSn-17Laf.tdb:NBSN2_CB, tdb:NbSn-98Tof.tdb:NBSN2_CB  


### TDB models of NBSN2_CB (3): PHASE and CONSTITUENT statements as written

[NbSn-02Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-02Tof.tdb): NBSN2_CB, type code %, sha256 `28d911b942daf434…`

~~~~text
66: PHASE NBSN2_CB %  2 1 2 !
67: CONST NBSN2_CB : NB : SN : !
~~~~

[NbSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-17Laf.tdb): NBSN2_CB, type code %, sha256 `fe83573ddf9ba2bf…`

~~~~text
62: PHASE NBSN2_CB %  2 1 2 !
63: CONST NBSN2_CB : NB : SN : !
~~~~

[NbSn-98Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSn-98Tof.tdb): NBSN2_CB, type code %, sha256 `7c50a914635b9aaf…`

~~~~text
69: PHASE NBSN2_CB %  2 1 2 !
70: CONST NBSN2_CB : NB : SN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/1054971023604071](https://doi.org/10.1361/1054971023604071) C. Toffolon, C. Servant, J. C. Gachon, B. Sundman, Reassessment of the Nb-Sn system, JPE 23, 134-139 (2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770341978](https://doi.org/10.1361/105497198770341978) C. Toffolon, C. Servant, B. Sundman, Thermodynamic assessment of the Nb-Sn system, JPE 19, 479-485 (1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1007/bf00554367](https://doi.org/10.1007/bf00554367) J. P. Charlesworth, I. Macphail, P. E. Madsen, Experimental work on the niobium-tin constitution diagram and related studies, J Mater Sci 5, 580-603 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(64)90018-9](https://doi.org/10.1016/0022-5088%2864%2990018-9) Thomas G Ellis, Harley A Wilhelm, Phase equilibria and crystallography for the niobium-tin system, Journal of the Less Common Metals 7, 67-83 (1964).  
_cited as the source of values for this phase_

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
