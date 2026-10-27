# Bi–Ce phases

> Bi–Ce system: 11 phases (tier A 8, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-CE.html · Markdown: https://data.orchid-project.org/phases/pages/BI-CE.md

11 phases (tier A 8, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-CE) · [full JSON](https://data.orchid-project.org/phases/systems/BI-CE.json) · [Bi–Ce system page](https://data.orchid-project.org/systems/BI-CE.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-CE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Ce system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-ce-a7-rhombohedral); _phase:bi-ce:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.53 K, x(Ce) 0–0 | 4 | 2 |
| [BCC_A2](#phase-bi-ce-bcc-a2); _phase:bi-ce:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 975.52–1653.71 K, x(Ce) 0.97–1 | 6 | 2 |
| [BI2CE](#phase-bi-ce-bi2ce); _phase:bi-ce:bi2ce_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1186.89 K, x(Ce) 0.33333–0.33333 | 10 | 2 |
| [BI3CE4_D73](#phase-bi-ce-bi3ce4-d73); _phase:bi-ce:bi3ce4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2013.04 K, x(Ce) 0.57143–0.57143 | 10 | 2 |
| [BI3CE5_D88](#phase-bi-ce-bi3ce5-d88); _phase:bi-ce:bi3ce5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1674.81 K, x(Ce) 0.625–0.625 | 8 | 2 |
| [BICE_B1](#phase-bi-ce-bice-b1); _phase:bi-ce:bice-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1901.02 K, x(Ce) 0.5–0.5 | 8 | 2 |
| [BICE2](#phase-bi-ce-bice2); _phase:bi-ce:bice2_ | La2Sb · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1520.33 K, x(Ce) 0.66667–0.66667 | 8 | 2 |
| [DHCP](#phase-bi-ce-dhcp-a3); _phase:bi-ce:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-bi-ce-fcc-a1); _phase:bi-ce:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1070.52 K, x(Ce) 1–1 | 2 | 2 |
| [HCP_A3](#phase-bi-ce-hcp-a3); _phase:bi-ce:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-bi-ce-liquid); _phase:bi-ce:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 544.44–2500 K, x(Ce) 0–1 | 28 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Ce)

- Id: `phase:bi-ce:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.53 K, x(Ce) 0–0
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:bi-ce:a7-rhombohedral, corpus:phase:bi-ce:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2012.05.004:Rhombo_A7, paper:10.1016/j.jnucmat.2017.08.016:rhombohedral (Bi)  
_tdb: _tdb:BiCe-12Li.tdb:RHOMBOHEDRAL_A7, tdb:BiCe-17Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `a261b33b47f12b95…`

~~~~text
54: PHASE RHOMBOHEDRAL_A7 % 1 1 !
55: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Bi–Ce)

- Id: `phase:bi-ce:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 975.52–1653.71 K, x(Ce) 0.97–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:bcc-a2)

Names (5): _corpus: _corpus:phase:bi-ce:bcc-a2  
_paper: _paper:10.1016/j.calphad.2012.05.004:BCC_A2, paper:10.1016/j.jnucmat.2017.08.016:BCC_A2 (Ce)  
_tdb: _tdb:BiCe-12Li.tdb:BCC_A2, tdb:BiCe-17Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): BCC_A2, type code %B, sha256 `a261b33b47f12b95…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : BI CE% : VA : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): BCC_A2, type code %B, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BI CE% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(78)90067-x](https://doi.org/10.1016/0022-5088%2878%2990067-x) G Borzone, A Borsese, A Calabretta, R Ferro, Heats of formation of cerium-bismuth alloys, Journal of the Less Common Metals 58, 31-36 (1978).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02882364](https://doi.org/10.1007/bf02882364) K.A. Gschneidner, F.W. Calderwood, Bull. Alloy Phase Diagr. 10 (1989) 427e430.  
_cited as the source of values for this phase_

## BI2CE (Bi–Ce)

- Id: `phase:bi-ce:bi2ce`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Bi2 Ce1 at x(CE)=0.3333
- Candidate (literature_printed): Bi2Ce · aP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Bi2Ce — Hallstedt 2025 mmc2 row for BI2CE: Bi2Ce
- Stoichiometry: Bi 0.6667, Ce 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1186.89 K, x(Ce) 0.33333–0.33333
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:bi2ce)

Names (6): _corpus: _corpus:phase:bi-ce:bi2ce  
_paper: _paper:10.1016/j.calphad.2012.05.004:Bi2Ce, paper:10.1016/j.calphad.2012.05.004:CeBi2, paper:10.1016/j.jnucmat.2017.08.016:CeBi2  
_tdb: _tdb:BiCe-12Li.tdb:BI2CE, tdb:BiCe-17Wan.tdb:BI2CE  


### TDB models of BI2CE (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): BI2CE, type code %, sha256 `a261b33b47f12b95…`

~~~~text
59: PHASE BI2CE % 2 2 1 !
60: CONST BI2CE : BI : CE : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): BI2CE, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
53: PHASE BI2CE % 2 2 1 !
54: CONST BI2CE : BI : CE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19130840125](https://doi.org/10.1002/zaac.19130840125) Rudolf Vogel, Über die Legierungen des Cers mit Silicium und Wismut, Z. Anorg. Chem. 84, 323-339 (1913).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90067-x](https://doi.org/10.1016/0022-5088%2878%2990067-x) G Borzone, A Borsese, A Calabretta, R Ferro, Heats of formation of cerium-bismuth alloys, Journal of the Less Common Metals 58, 31-36 (1978).  
_cited as the source of values for this phase_

## BI3CE4_D73 (Bi–Ce)

- Id: `phase:bi-ce:bi3ce4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.4286, Ce 0.5714
- Stability: stable in 2 of 2 calculated diagram(s): 300–2013.04 K, x(Ce) 0.57143–0.57143
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:bi3ce4-d73)

Names (5): _corpus: _corpus:phase:bi-ce:bi3ce4-d73  
_paper: _paper:10.1016/j.calphad.2012.05.004:Ce4Bi3, paper:10.1016/j.jnucmat.2017.08.016:Ce4Bi3  
_tdb: _tdb:BiCe-12Li.tdb:BI3CE4_D73, tdb:BiCe-17Wan.tdb:BI3CE4_D73  


### TDB models of BI3CE4_D73 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): BI3CE4_D73, type code %, sha256 `a261b33b47f12b95…`

~~~~text
69: PHASE BI3CE4_D73 % 2 3 4 !
70: CONST BI3CE4_D73 : BI : CE : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): BI3CE4_D73, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
63: PHASE BI3CE4_D73 % 2 3 4 !
64: CONST BI3CE4_D73 : BI : CE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19130840125](https://doi.org/10.1002/zaac.19130840125) Rudolf Vogel, Über die Legierungen des Cers mit Silicium und Wismut, Z. Anorg. Chem. 84, 323-339 (1913).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90038-7](https://doi.org/10.1016/0022-5088%2875%2990038-7) K. Yoshihara, J.B. Taylor, L.D. Calvert, J.G. Despault, Rare-earth bismuthides, Journal of the Less Common Metals 41, 329-337 (1975).  
_cited as the source of values for this phase_

## BI3CE5_D88 (Bi–Ce)

- Id: `phase:bi-ce:bi3ce5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.3750, Ce 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–1674.81 K, x(Ce) 0.625–0.625
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:bi3ce5-d88)

Names (5): _corpus: _corpus:phase:bi-ce:bi3ce5-d88  
_paper: _paper:10.1016/j.calphad.2012.05.004:Ce5Bi3, paper:10.1016/j.jnucmat.2017.08.016:Ce5Bi3  
_tdb: _tdb:BiCe-12Li.tdb:BI3CE5_D88, tdb:BiCe-17Wan.tdb:BI3CE5_D88  


### TDB models of BI3CE5_D88 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): BI3CE5_D88, type code %, sha256 `a261b33b47f12b95…`

~~~~text
74: PHASE BI3CE5_D88 % 2 3 5 !
75: CONST BI3CE5_D88 : BI : CE : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): BI3CE5_D88, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
68: PHASE BI3CE5_D88 % 2 3 5 !
69: CONST BI3CE5_D88 : BI : CE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(75)90038-7](https://doi.org/10.1016/0022-5088%2875%2990038-7) K. Yoshihara, J.B. Taylor, L.D. Calvert, J.G. Despault, Rare-earth bismuthides, Journal of the Less Common Metals 41, 329-337 (1975).  
_cited as the source of values for this phase_

## BICE_B1 (Bi–Ce)

- Id: `phase:bi-ce:bice-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabilp and oqmd-10917, space group 225
- Stoichiometry: Bi 0.5000, Ce 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1901.02 K, x(Ce) 0.5–0.5
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:bice-b1)

Names (7): _corpus: _corpus:phase:bi-ce:bice-b1  
_mp: _mp:mp-aaaabilp  
_oqmd: _oqmd:oqmd-10917  
_paper: _paper:10.1016/j.calphad.2012.05.004:CeBi, paper:10.1016/j.jnucmat.2017.08.016:CeBi  
_tdb: _tdb:BiCe-12Li.tdb:BICE_B1, tdb:BiCe-17Wan.tdb:BICE_B1  


### TDB models of BICE_B1 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): BICE_B1, type code %, sha256 `a261b33b47f12b95…`

~~~~text
64: PHASE BICE_B1 % 2 1 1 !
65: CONST BICE_B1 : BI : CE : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): BICE_B1, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
58: PHASE BICE_B1 % 2 1 1 !
59: CONST BICE_B1 : BI : CE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19130840125](https://doi.org/10.1002/zaac.19130840125) Rudolf Vogel, Über die Legierungen des Cers mit Silicium und Wismut, Z. Anorg. Chem. 84, 323-339 (1913).  
_cited as the source of values for this phase_

## BICE2 (Bi–Ce)

- Id: `phase:bi-ce:bice2`; status `assigned`
- Structure: La2Sb · tI12 · I4/mmm (139); type `st:la2sb-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3333, Ce 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1520.33 K, x(Ce) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:bice2)

Names (5): _corpus: _corpus:phase:bi-ce:bice2  
_paper: _paper:10.1016/j.calphad.2012.05.004:Ce2Bi, paper:10.1016/j.jnucmat.2017.08.016:Ce2Bi  
_tdb: _tdb:BiCe-12Li.tdb:BICE2, tdb:BiCe-17Wan.tdb:BICE2  


### TDB models of BICE2 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): BICE2, type code %, sha256 `a261b33b47f12b95…`

~~~~text
79: PHASE BICE2 % 2 1 2 !
80: CONST BICE2 : BI : CE : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): BICE2, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
73: PHASE BICE2 % 2 1 2 !
74: CONST BICE2 : BI : CE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02882364](https://doi.org/10.1007/bf02882364) K.A. Gschneidner, F.W. Calderwood, Bull. Alloy Phase Diagr. 10 (1989) 427e430.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90038-7](https://doi.org/10.1016/0022-5088%2875%2990038-7) K. Yoshihara, J.B. Taylor, L.D. Calvert, J.G. Despault, Rare-earth bismuthides, Journal of the Less Common Metals 41, 329-337 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90067-x](https://doi.org/10.1016/0022-5088%2878%2990067-x) G Borzone, A Borsese, A Calabretta, R Ferro, Heats of formation of cerium-bismuth alloys, Journal of the Less Common Metals 58, 31-36 (1978).  
_cited as the source of values for this phase_

## DHCP (Bi–Ce)

- Id: `phase:bi-ce:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:dhcp-a3)

Names (2): _corpus: _corpus:phase:bi-ce:dhcp-a3  
_tdb: _tdb:BiCe-17Wan.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): DHCP, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
43: PHASE DHCP % 1 1 !
44: CONST DHCP : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase_

## FCC_A1 (Bi–Ce)

- Id: `phase:bi-ce:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1070.52 K, x(Ce) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:fcc-a1)

Names (4): _corpus: _corpus:phase:bi-ce:fcc-a1  
_paper: _paper:10.1016/j.calphad.2012.05.004:FCC_A1  
_tdb: _tdb:BiCe-12Li.tdb:FCC_A1, tdb:BiCe-17Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): FCC_A1, type code %A, sha256 `a261b33b47f12b95…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : BI CE% : VA : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): FCC_A1, type code %A, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BI CE% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90067-x](https://doi.org/10.1016/0022-5088%2878%2990067-x) G Borzone, A Borsese, A Calabretta, R Ferro, Heats of formation of cerium-bismuth alloys, Journal of the Less Common Metals 58, 31-36 (1978).  
_cited as the source of values for this phase_

## HCP_A3 (Bi–Ce)

- Id: `phase:bi-ce:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-ce:hcp-a3  
_tdb: _tdb:BiCe-12Li.tdb:HCP_A3, tdb:BiCe-17Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): HCP_A3, type code %A, sha256 `a261b33b47f12b95…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : BI CE : VA: !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): HCP_A3, type code %A, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BI CE : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase_

## LIQUID (Bi–Ce)

- Id: `phase:bi-ce:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 544.44–2500 K, x(Ce) 0–1
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ce:liquid)

Names (6): _corpus: _corpus:phase:bi-ce:liquid  
_paper: _paper:10.1016/j.calphad.2012.05.004:Liquid, paper:10.1016/j.jnucmat.2017.08.016:L, paper:10.1016/j.jnucmat.2017.08.016:liquid  
_tdb: _tdb:BiCe-12Li.tdb:LIQUID, tdb:BiCe-17Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiCe-12Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-12Li.tdb): LIQUID, type code %, sha256 `a261b33b47f12b95…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : BI CE : !
~~~~

[BiCe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCe-17Wan.tdb): LIQUID, type code %, sha256 `7b39a0f2a6bf4ab9…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BI CE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2012.05.004](https://doi.org/10.1016/j.calphad.2012.05.004) Juan Li, Yu Cai, Qiang Chen, Hang Zhang, HuaShan Liu, ZhanPeng Jin, Thermodynamic modeling of Fe–Ce–Bi system and explanation of interfacial reaction in Fe-45at%–Ce/Bi couple, Calphad 38, 133-139 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19130840125](https://doi.org/10.1002/zaac.19130840125) Rudolf Vogel, Über die Legierungen des Cers mit Silicium und Wismut, Z. Anorg. Chem. 84, 323-339 (1913).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90038-7](https://doi.org/10.1016/0022-5088%2875%2990038-7) K. Yoshihara, J.B. Taylor, L.D. Calvert, J.G. Despault, Rare-earth bismuthides, Journal of the Less Common Metals 41, 329-337 (1975).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02882364](https://doi.org/10.1007/bf02882364) K.A. Gschneidner, F.W. Calderwood, Bull. Alloy Phase Diagr. 10 (1989) 427e430.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90067-x](https://doi.org/10.1016/0022-5088%2878%2990067-x) G Borzone, A Borsese, A Calabretta, R Ferro, Heats of formation of cerium-bismuth alloys, Journal of the Less Common Metals 58, 31-36 (1978).  
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
