# Bi–K phases

> Bi–K system: 10 phases (tier A 7, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-K.html · Markdown: https://data.orchid-project.org/phases/pages/BI-K.md

10 phases (tier A 7, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-K) · [full JSON](https://data.orchid-project.org/phases/systems/BI-K.json) · [Bi–K system page](https://data.orchid-project.org/systems/BI-K.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-K.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–K system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-k-a7-rhombohedral); _phase:bi-k:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(K) 0–0 | 4 | 3 |
| [BCC_A2](#phase-bi-k-bcc-a2); _phase:bi-k:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–336.53 K, x(K) 1–1 | 4 | 3 |
| [BI2K_C15](#phase-bi-k-bi2k-c15); _phase:bi-k:bi2k-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–837.91 K, x(K) 0.33333–0.33333 | 12 | 3 |
| [BI2K3](#phase-bi-k-bi2k3); _phase:bi-k:bi2k3_ | Eu3Ga2 · mC20 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–720 K, x(K) 0.6–0.6 | 17 | 3 |
| [BI4K5](#phase-bi-k-bi4k5); _phase:bi-k:bi4k5_ | Bi4K5 · mC18 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–656.4 K, x(K) 0.55556–0.55556 | 21 | 3 |
| [BIK3_D021](#phase-bi-k-bik3-d021); _phase:bi-k:bik3-d021_ | Cu3P · D0_21 · hP24 · P6_3cm (185) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–555.33 K, x(K) 0.75–0.75 | 7 | 3 |
| [BIK3_D03](#phase-bi-k-bik3-d03); _phase:bi-k:bik3-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 553–990 K, x(K) 0.75–0.75 | 10 | 3 |
| [FCC_A1](#phase-bi-k-fcc-a1); _phase:bi-k:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-bi-k-hcp-a3); _phase:bi-k:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-bi-k-liquid); _phase:bi-k:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 336.32–2500 K, x(K) 0–1 | 29 | 3 |

## RHOMBOHEDRAL_A7 (Bi–K)

- Id: `phase:bi-k:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(K) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:bi-k:a7-rhombohedral, corpus:phase:bi-k:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2011.10.032:Rhom  
_tdb: _tdb:BiK-12Niu.tdb:RHOMBOHEDRAL_A7, tdb:BiK-15Gie.tdb:RHOMBOHEDRAL_A7, tdb:BiK-80Che-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `3ce72b86413e842a…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `530ca2f96b764f0e…`

~~~~text
49: PHASE RHOMBOHEDRAL_A7 % 1 1 !
50: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `e6d765540ed2fd20…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–K)

- Id: `phase:bi-k:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–336.53 K, x(K) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:bcc-a2)

Names (5): _corpus: _corpus:phase:bi-k:bcc-a2  
_paper: _paper:10.1016/j.tca.2011.10.032:BCC_A2  
_tdb: _tdb:BiK-12Niu.tdb:BCC_A2, tdb:BiK-15Gie.tdb:BCC_A2, tdb:BiK-80Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): BCC_A2, type code %B, sha256 `3ce72b86413e842a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI K : VA : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): BCC_A2, type code %B, sha256 `530ca2f96b764f0e…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : BI K : VA : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): BCC_A2, type code %B, sha256 `e6d765540ed2fd20…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BI K : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
_cited as the source of values for this phase_

## BI2K_C15 (Bi–K)

- Id: `phase:bi-k:bi2k-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabilj and oqmd-647551, space group 227
- Stoichiometry: Bi 0.6667, K 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–837.91 K, x(K) 0.33333–0.33333
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:bi2k-c15)

Names (7): _corpus: _corpus:phase:bi-k:bi2k-c15  
_mp: _mp:mp-aaaabilj  
_oqmd: _oqmd:oqmd-647551  
_paper: _paper:10.1016/j.tca.2011.10.032:Bi2K  
_tdb: _tdb:BiK-12Niu.tdb:BI2K_C15, tdb:BiK-15Gie.tdb:BI2K_C15, tdb:BiK-80Che-LB.tdb:BI2K_C15  


### TDB models of BI2K_C15 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): BI2K_C15, type code %, sha256 `3ce72b86413e842a…`

~~~~text
50: PHASE BI2K_C15 % 2 2 1 !
51: CONST BI2K_C15 : BI : K : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): BI2K_C15, type code %, sha256 `530ca2f96b764f0e…`

~~~~text
54: PHASE BI2K_C15 % 2 2 1 !
55: CONST BI2K_C15 : BI : K : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): BI2K_C15, type code %, sha256 `e6d765540ed2fd20…`

~~~~text
48: PHASE BI2K_C15 % 2 2 1 !
49: CONST BI2K_C15 : BI : K : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
_cited as the source of values for this phase_

## BI2K3 (Bi–K)

- Id: `phase:bi-k:bi2k3`; status `assigned`
- Structure: Eu3Ga2 · mC20 · C2/c (15); type `st:eu3ga2-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4000, K 0.6000
- Stability: stable in 3 of 3 calculated diagram(s): 300–720 K, x(K) 0.6–0.6
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:bi2k3)

Names (5): _corpus: _corpus:phase:bi-k:bi2k3  
_paper: _paper:10.1016/j.tca.2011.10.032:Bi2K3  
_tdb: _tdb:BiK-12Niu.tdb:BI2K3, tdb:BiK-15Gie.tdb:BI2K3, tdb:BiK-80Che-LB.tdb:BI2K3  


### TDB models of BI2K3 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): BI2K3, type code %, sha256 `3ce72b86413e842a…`

~~~~text
60: PHASE BI2K3 % 2 2 3 !
61: CONST BI2K3 : BI : K : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): BI2K3, type code %, sha256 `530ca2f96b764f0e…`

~~~~text
64: PHASE BI2K3 % 2 2 3 !
65: CONST BI2K3 : BI : K : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): BI2K3, type code %, sha256 `e6d765540ed2fd20…`

~~~~text
58: PHASE BI2K3 % 2 2 3 !
59: CONST BI2K3 : BI : K : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
_cited as the source of values for this phase_

## BI4K5 (Bi–K)

- Id: `phase:bi-k:bi4k5`; status `assigned`
- Structure: Bi4K5 · mC18 · C2/m (12); type `st:bi4k5-mc18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4444, K 0.5556
- Stability: stable in 3 of 3 calculated diagram(s): 300–656.4 K, x(K) 0.55556–0.55556
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:bi4k5)

Names (5): _corpus: _corpus:phase:bi-k:bi4k5  
_paper: _paper:10.1016/j.tca.2011.10.032:Bi4K5  
_tdb: _tdb:BiK-12Niu.tdb:BI4K5, tdb:BiK-15Gie.tdb:BI4K5, tdb:BiK-80Che-LB.tdb:BI4K5  


### TDB models of BI4K5 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): BI4K5, type code %, sha256 `3ce72b86413e842a…`

~~~~text
55: PHASE BI4K5 % 2 4 5 !
56: CONST BI4K5 : BI : K : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): BI4K5, type code %, sha256 `530ca2f96b764f0e…`

~~~~text
59: PHASE BI4K5 % 2 4 5 !
60: CONST BI4K5 : BI : K : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): BI4K5, type code %, sha256 `e6d765540ed2fd20…`

~~~~text
53: PHASE BI4K5 % 2 4 5 !
54: CONST BI4K5 : BI : K : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
_cited as the source of values for this phase_

## BIK3_D021 (Bi–K)

- Id: `phase:bi-k:bik3-d021`; status `assigned`
- Structure: Cu3P · D0_21 · hP24 · P6_3cm (185); type `st:d0-21-cu3p-hp24`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.2500, K 0.7500
- Stability: stable in 3 of 3 calculated diagram(s): 300–555.33 K, x(K) 0.75–0.75
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:bik3-d021)

Names (5): _corpus: _corpus:phase:bi-k:bik3-d021  
_paper: _paper:10.1016/j.tca.2011.10.032:α-BiK3  
_tdb: _tdb:BiK-12Niu.tdb:BIK3_D021, tdb:BiK-15Gie.tdb:BIK3_D021, tdb:BiK-80Che-LB.tdb:BIK3_D021  


### TDB models of BIK3_D021 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): BIK3_D021, type code %, sha256 `3ce72b86413e842a…`

~~~~text
65: PHASE BIK3_D021 % 2 1 3 !
66: CONST BIK3_D021 : BI : K : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): BIK3_D021, type code %, sha256 `530ca2f96b764f0e…`

~~~~text
69: PHASE BIK3_D021 % 2 1 3 !
70: CONST BIK3_D021 : BI : K : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): BIK3_D021, type code %, sha256 `e6d765540ed2fd20…`

~~~~text
63: PHASE BIK3_D021 % 2 1 3 !
64: CONST BIK3_D021 : BI : K : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
_cited as the source of values for this phase_

## BIK3_D03 (Bi–K)

- Id: `phase:bi-k:bik3-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.2500, K 0.7500
- Stability: stable in 3 of 3 calculated diagram(s): 553–990 K, x(K) 0.75–0.75
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:bik3-d03)

Names (5): _corpus: _corpus:phase:bi-k:bik3-d03  
_paper: _paper:10.1016/j.tca.2011.10.032:β-BiK3  
_tdb: _tdb:BiK-12Niu.tdb:BIK3_D03, tdb:BiK-15Gie.tdb:BIK3_D03, tdb:BiK-80Che-LB.tdb:BIK3_D03  


### TDB models of BIK3_D03 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): BIK3_D03, type code %, sha256 `3ce72b86413e842a…`

~~~~text
70: PHASE BIK3_D03 % 2 1 3 !
71: CONST BIK3_D03 : BI : K : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): BIK3_D03, type code %, sha256 `530ca2f96b764f0e…`

~~~~text
74: PHASE BIK3_D03 % 2 1 3 !
75: CONST BIK3_D03 : BI : K : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): BIK3_D03, type code %, sha256 `e6d765540ed2fd20…`

~~~~text
68: PHASE BIK3_D03 % 2 1 3 !
69: CONST BIK3_D03 : BI : K : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–K)

- Id: `phase:bi-k:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:fcc-a1)

Names (4): _corpus: _corpus:phase:bi-k:fcc-a1  
_tdb: _tdb:BiK-12Niu.tdb:FCC_A1, tdb:BiK-15Gie.tdb:FCC_A1, tdb:BiK-80Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): FCC_A1, type code %A, sha256 `3ce72b86413e842a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI K : VA : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): FCC_A1, type code %A, sha256 `530ca2f96b764f0e…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : BI K : VA : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): FCC_A1, type code %A, sha256 `e6d765540ed2fd20…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BI K : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_

## HCP_A3 (Bi–K)

- Id: `phase:bi-k:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:hcp-a3)

Names (4): _corpus: _corpus:phase:bi-k:hcp-a3  
_tdb: _tdb:BiK-12Niu.tdb:HCP_A3, tdb:BiK-15Gie.tdb:HCP_A3, tdb:BiK-80Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): HCP_A3, type code %A, sha256 `3ce72b86413e842a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI K : VA: !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): HCP_A3, type code %A, sha256 `530ca2f96b764f0e…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : BI K : VA: !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): HCP_A3, type code %A, sha256 `e6d765540ed2fd20…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BI K : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_

## LIQUID (Bi–K)

- Id: `phase:bi-k:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 336.32–2500 K, x(K) 0–1
- Literature: 29 values (29 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-k:liquid)

Names (5): _corpus: _corpus:phase:bi-k:liquid  
_paper: _paper:10.1016/j.tca.2011.10.032:L  
_tdb: _tdb:BiK-12Niu.tdb:LIQUID, tdb:BiK-15Gie.tdb:LIQUID, tdb:BiK-80Che-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[BiK-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-12Niu.tdb): LIQUID, type code %, sha256 `3ce72b86413e842a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI BIK BIK3 K : !
~~~~

[BiK-15Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-15Gie.tdb): LIQUID, type code %, sha256 `530ca2f96b764f0e…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : BI BIK3 K : !
~~~~

[BiK-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiK-80Che-LB.tdb): LIQUID, type code %, sha256 `e6d765540ed2fd20…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BI K : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.10.032](https://doi.org/10.1016/j.tca.2011.10.032) Chunju Niu, Changrong Li, Zhenmin Du, Cuiping Guo, Miao Liu, Thermodynamic assessment of the Bi–K binary system, Thermochimica Acta 528, 9-14 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.12.006](https://doi.org/10.1016/j.tca.2014.12.006) W. Gierlotka, Thermochim. Acta, 604, 137-39(2015).  
_assessment that models this phase_
- [doi:10.1007/bf02663669](https://doi.org/10.1007/bf02663669) A. Petric, A.D. Pelton, The Bi–K (bismuth–potassium) system, J. Phase Equilib. 12 (1) (1991) 29–33.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1088/0305-4608/18/7/015](https://doi.org/10.1088/0305-4608/18/7/015) A Petric, A D Pelton, M L Saboungi, Thermodynamic properties of liquid K-Bi alloys by electromotive force measurements, J. Phys. F: Met. Phys. 18, 1473-1489 (1988).  
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
