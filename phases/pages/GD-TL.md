# Gd–Tl phases

> Gd–Tl system: 9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-TL.html · Markdown: https://data.orchid-project.org/phases/pages/GD-TL.md

9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-TL) · [full JSON](https://data.orchid-project.org/phases/systems/GD-TL.json) · [Gd–Tl system page](https://data.orchid-project.org/systems/GD-TL.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-TL.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–Tl system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-gd-tl-bcc-a2); _phase:gd-tl:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1143.02–1588.13 K, x(Tl) 0–0.13927 | 16 | 2 |
| [B2_BCC](#phase-gd-tl-bcc-b2); _phase:gd-tl:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.5 K, x(Tl) 0–1 | 12 | 1 |
| [FCC_A1](#phase-gd-tl-fcc-a1); _phase:gd-tl:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GD2TL_B82](#phase-gd-tl-gd2tl-b82); _phase:gd-tl:gd2tl-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1327.69 K, x(Tl) 0.33333–0.33333 | 12 | 1 |
| [GD3TL5](#phase-gd-tl-gd3tl5); _phase:gd-tl:gd3tl5_ | Pd5Pu3 · oC32 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1322.75 K, x(Tl) 0.625–0.625 | 9 | 1 |
| [GD5TL3_D88](#phase-gd-tl-gd5tl3-d88); _phase:gd-tl:gd5tl3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1492.69 K, x(Tl) 0.375–0.39564 | 12 | 1 |
| [GDTL3_L12](#phase-gd-tl-gdtl3-l12); _phase:gd-tl:gdtl3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1263.11 K, x(Tl) 0.75–0.75 | 9 | 1 |
| [HCP_A3](#phase-gd-tl-hcp-a3); _phase:gd-tl:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1518.02 K, x(Tl) 0–1 | 8 | 1 |
| [LIQUID](#phase-gd-tl-liquid); _phase:gd-tl:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 576.23–2500 K, x(Tl) 0–1 | 36 | 1 |

## BCC_A2 (Gd–Tl)

- Id: `phase:gd-tl:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1143.02–1588.13 K, x(Tl) 0–0.13927
- Literature: 16 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:bcc-a2)

Names (4): _corpus: _corpus:phase:gd-tl:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2009.11.101:bcc  
_tdb: _tdb:GdTl-10Guo.tdb:A2_BCC, tdb:GdTl-10Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): A2_BCC, type code %B, sha256 `81d605effa4ab98f…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : GD TL : VA : !
~~~~

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): BCC_A2, type code %B, sha256 `81d605effa4ab98f…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : GD% TL% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_

## B2_BCC (Gd–Tl)

- Id: `phase:gd-tl:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: GdTl-10Guo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in GdTl-10Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.5 K, x(Tl) 0–1
- Literature: 12 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:bcc-b2)

Names (4): _corpus: _corpus:phase:gd-tl:bcc-b2, corpus:phase:gd-tl:b2-bcc  
_paper: _paper:10.1016/j.jallcom.2009.11.101:GdTl  
_tdb: _tdb:GdTl-10Guo.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): B2_BCC, type code %BO, sha256 `81d605effa4ab98f…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : GD% TL : GD TL% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
_cited as the source of values for this phase_

## FCC_A1 (Gd–Tl)

- Id: `phase:gd-tl:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:fcc-a1)

Names (2): _corpus: _corpus:phase:gd-tl:fcc-a1  
_tdb: _tdb:GdTl-10Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): FCC_A1, type code %A, sha256 `81d605effa4ab98f…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : GD TL : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase_

## GD2TL_B82 (Gd–Tl)

- Id: `phase:gd-tl:gd2tl-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 0.6667, Tl 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1327.69 K, x(Tl) 0.33333–0.33333
- Literature: 12 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:gd2tl-b82)

Names (3): _corpus: _corpus:phase:gd-tl:gd2tl-b82  
_paper: _paper:10.1016/j.jallcom.2009.11.101:Gd2Tl  
_tdb: _tdb:GdTl-10Guo.tdb:GD2TL_B82  


### TDB models of GD2TL_B82 (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): GD2TL_B82, type code %, sha256 `81d605effa4ab98f…`

~~~~text
55: PHASE GD2TL_B82 % 2 2 1 !
56: CONST GD2TL_B82 : GD : TL : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
_cited as the source of values for this phase_

## GD3TL5 (Gd–Tl)

- Id: `phase:gd-tl:gd3tl5`; status `assigned`
- Structure: Pd5Pu3 · oC32 · Cmcm (63); type `st:pd5pu3-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.3750, Tl 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1322.75 K, x(Tl) 0.625–0.625
- Literature: 9 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:gd3tl5)

Names (3): _corpus: _corpus:phase:gd-tl:gd3tl5  
_paper: _paper:10.1016/j.jallcom.2009.11.101:Gd3Tl5  
_tdb: _tdb:GdTl-10Guo.tdb:GD3TL5  


### TDB models of GD3TL5 (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): GD3TL5, type code %, sha256 `81d605effa4ab98f…`

~~~~text
65: PHASE GD3TL5 % 2 3 5 !
66: CONST GD3TL5 : GD : TL : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
_cited as the source of values for this phase_

## GD5TL3_D88 (Gd–Tl)

- Id: `phase:gd-tl:gd5tl3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1492.69 K, x(Tl) 0.375–0.39564
- Literature: 12 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:gd5tl3-d88)

Names (3): _corpus: _corpus:phase:gd-tl:gd5tl3-d88  
_paper: _paper:10.1016/j.jallcom.2009.11.101:Gd5Tl3  
_tdb: _tdb:GdTl-10Guo.tdb:GD5TL3_D88  


### TDB models of GD5TL3_D88 (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): GD5TL3_D88, type code %, sha256 `81d605effa4ab98f…`

~~~~text
60: PHASE GD5TL3_D88 % 2 5 3 !
61: CONST GD5TL3_D88 : GD% TL : TL : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
_cited as the source of values for this phase_

## GDTL3_L12 (Gd–Tl)

- Id: `phase:gd-tl:gdtl3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabeip and oqmd-30424, space group 221
- Stoichiometry: Gd 0.2500, Tl 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1263.11 K, x(Tl) 0.75–0.75
- Literature: 9 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:gdtl3-l12)

Names (5): _corpus: _corpus:phase:gd-tl:gdtl3-l12  
_mp: _mp:mp-aaaabeip  
_oqmd: _oqmd:oqmd-30424  
_paper: _paper:10.1016/j.jallcom.2009.11.101:GdTl3  
_tdb: _tdb:GdTl-10Guo.tdb:GDTL3_L12  


### TDB models of GDTL3_L12 (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): GDTL3_L12, type code %, sha256 `81d605effa4ab98f…`

~~~~text
70: PHASE GDTL3_L12 % 2 1 3 !
71: CONST GDTL3_L12 : GD : TL : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
_cited as the source of values for this phase_

## HCP_A3 (Gd–Tl)

- Id: `phase:gd-tl:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1518.02 K, x(Tl) 0–1
- Literature: 8 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:hcp-a3)

Names (3): _corpus: _corpus:phase:gd-tl:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.11.101:hcp  
_tdb: _tdb:GdTl-10Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): HCP_A3, type code %A, sha256 `81d605effa4ab98f…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : GD% TL% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_

## LIQUID (Gd–Tl)

- Id: `phase:gd-tl:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 576.23–2500 K, x(Tl) 0–1
- Literature: 36 values (27 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-tl:liquid)

Names (3): _corpus: _corpus:phase:gd-tl:liquid  
_paper: _paper:10.1016/j.jallcom.2009.11.101:L  
_tdb: _tdb:GdTl-10Guo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GdTl-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTl-10Guo.tdb): LIQUID, type code %, sha256 `81d605effa4ab98f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : GD TL : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.101](https://doi.org/10.1016/j.jallcom.2009.11.101) Cuiping Guo, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Gd–Tl system, Journal of Alloys and Compounds 492, 122-127 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90428-6](https://doi.org/10.1016/0022-5088%2888%2990428-6) A. Saccone, S. Delfino, G. Cacciamani, R. Ferro, The binary phase diagrams of thallium with gadolinium, terbium and dysprosium, Journal of the Less Common Metals 136, 249-259 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2004.08.005](https://doi.org/10.1016/j.calphad.2004.08.005) G. Kaptay, Calphad 28 (2004) 115.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1983-741007](https://doi.org/10.1515/ijmr-1983-741007) S. Delﬁno, A. Saccone, R. Ferro, Z. Metallkd. 74 (1983) 674.  
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
