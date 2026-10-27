# Ba–Bi phases

> Ba–Bi system: 10 phases (tier A 6, tier C 3, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-BI.html · Markdown: https://data.orchid-project.org/phases/pages/BA-BI.md

10 phases (tier A 6, tier C 3, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-BI) · [full JSON](https://data.orchid-project.org/phases/systems/BA-BI.json) · [Ba–Bi system page](https://data.orchid-project.org/systems/BA-BI.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-BI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–Bi system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-ba-bi-a7-rhombohedral); _phase:ba-bi:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Bi) 1–1 | 3 | 1 |
| [BA11BI10](#phase-ba-bi-ba11bi10); _phase:ba-bi:ba11bi10_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1017.89 K, x(Bi) 0.47619–0.47619 | 11 | 1 |
| [BA2BI](#phase-ba-bi-ba2bi); _phase:ba-bi:ba2bi_ | La2Sb · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–800 K, x(Bi) 0.33333–0.33333 | 9 | 1 |
| [BA4BI3_D73](#phase-ba-bi-ba4bi3-d73); _phase:ba-bi:ba4bi3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1077.97 K, x(Bi) 0.42857–0.42857 | 6 | 1 |
| [BA5BI3_D88](#phase-ba-bi-ba5bi3-d88); _phase:ba-bi:ba5bi3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–997.97 K, x(Bi) 0.375–0.375 | 5 | 1 |
| [BABI3](#phase-ba-bi-babi3); _phase:ba-bi:babi3_ | Pb3Sr · tP4 · P4/mmm (123) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–910 K, x(Bi) 0.75–0.75 | 14 | 1 |
| [BCC_A2](#phase-ba-bi-bcc-a2); _phase:ba-bi:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Bi) 0–0 | 2 | 1 |
| [FCC_A1](#phase-ba-bi-fcc-a1); _phase:ba-bi:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ba-bi-hcp-a3); _phase:ba-bi:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ba-bi-liquid); _phase:ba-bi:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 535.97–2500 K, x(Bi) 0–1 | 11 | 1 |

## RHOMBOHEDRAL_A7 (Ba–Bi)

- Id: `phase:ba-bi:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Bi) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:ba-bi:a7-rhombohedral, corpus:phase:ba-bi:rhombohedral-a7  
_paper: _paper:10.1016/j.jallcom.2018.08.324:Rhom_A7(Bi)  
_tdb: _tdb:BaBi-19Liu.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `3c64df6c93728519…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : BA BI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.electacta.2016.12.141](https://doi.org/10.1016/j.electacta.2016.12.141) Timothy Lichtenstein, Nathan D. Smith, Jarrod Gesualdi, Kuldeep Kumar, Hojong Kim, Thermodynamic properties of Barium-Bismuth alloys determined by emf measurements, Electrochimica Acta 228, 628-635 (2017).  
_cited as the source of values for this phase_

## BA11BI10 (Ba–Bi)

- Id: `phase:ba-bi:ba11bi10`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ba 0.5238, Bi 0.4762
- Stability: stable in 1 of 1 calculated diagram(s): 300–1017.89 K, x(Bi) 0.47619–0.47619
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:ba11bi10)

Names (3): _corpus: _corpus:phase:ba-bi:ba11bi10  
_paper: _paper:10.1016/j.jallcom.2018.08.324:Ba11Bi10  
_tdb: _tdb:BaBi-19Liu.tdb:BA11BI10  


### TDB models of BA11BI10 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): BA11BI10, type code %, sha256 `3c64df6c93728519…`

~~~~text
68: PHASE BA11BI10 % 2 11 10 !
69: CONST BA11BI10 : BA : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.2001.9470](https://doi.org/10.1006/jssc.2001.9470) Gaëlle Derrien, Monique Tillard-Charbonnel, Alain Manteghetti, Laure Monconduit, Claude Belin, Synthesis and Crystal Structure of M11X10 Compounds, M=Sr, Ba and X=Bi, Sb. Electronic Requirements and Chemical Bonding, Journal of Solid State Chemistry 164, 169-175 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/j.electacta.2016.12.141](https://doi.org/10.1016/j.electacta.2016.12.141) Timothy Lichtenstein, Nathan D. Smith, Jarrod Gesualdi, Kuldeep Kumar, Hojong Kim, Thermodynamic properties of Barium-Bismuth alloys determined by emf measurements, Electrochimica Acta 228, 628-635 (2017).  
_cited as the source of values for this phase_

## BA2BI (Ba–Bi)

- Id: `phase:ba-bi:ba2bi`; status `assigned`
- Structure: La2Sb · tI12 · I4/mmm (139); type `st:la2sb-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ba 0.6667, Bi 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–800 K, x(Bi) 0.33333–0.33333
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:ba2bi)

Names (3): _corpus: _corpus:phase:ba-bi:ba2bi  
_paper: _paper:10.1016/j.jallcom.2018.08.324:Ba2Bi  
_tdb: _tdb:BaBi-19Liu.tdb:BA2BI  


### TDB models of BA2BI (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): BA2BI, type code %, sha256 `3c64df6c93728519…`

~~~~text
53: PHASE BA2BI % 2 2 1 !
54: CONST BA2BI : BA : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1107/s0567740874006261](https://doi.org/10.1107/s0567740874006261) M. Martinez-Ripoll, A. Haase, G. Brauer, The crystal structure of Ba\<sub>2\</sub>Bi, Acta Crystallogr B Struct Sci 30, 2003-2004 (1974).  
_cited as the source of values for this phase_
- [doi:10.1002/ange.19610730505](https://doi.org/10.1002/ange.19610730505) G. Brauer, Otto Müller, Intermetallische Verbindungen der höheren Erdalkalimetalle mit Antimon und Wismut, Angewandte Chemie 73, 169-169 (1961).  
_cited as the source of values for this phase_

## BA4BI3_D73 (Ba–Bi)

- Id: `phase:ba-bi:ba4bi3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Ba 0.5714, Bi 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–1077.97 K, x(Bi) 0.42857–0.42857
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:ba4bi3-d73)

Names (3): _corpus: _corpus:phase:ba-bi:ba4bi3-d73  
_paper: _paper:10.1016/j.jallcom.2018.08.324:Ba4Bi3  
_tdb: _tdb:BaBi-19Liu.tdb:BA4BI3_D73  


### TDB models of BA4BI3_D73 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): BA4BI3_D73, type code %, sha256 `3c64df6c93728519…`

~~~~text
63: PHASE BA4BI3_D73 % 2 4 3 !
64: CONST BA4BI3_D73 : BA : BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.electacta.2016.12.141](https://doi.org/10.1016/j.electacta.2016.12.141) Timothy Lichtenstein, Nathan D. Smith, Jarrod Gesualdi, Kuldeep Kumar, Hojong Kim, Thermodynamic properties of Barium-Bismuth alloys determined by emf measurements, Electrochimica Acta 228, 628-635 (2017).  
_cited as the source of values for this phase_

## BA5BI3_D88 (Ba–Bi)

- Id: `phase:ba-bi:ba5bi3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabrvh and oqmd-7613, space group 193
- Stoichiometry: Ba 0.6250, Bi 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–997.97 K, x(Bi) 0.375–0.375
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:ba5bi3-d88)

Names (5): _corpus: _corpus:phase:ba-bi:ba5bi3-d88  
_mp: _mp:mp-aaaabrvh  
_oqmd: _oqmd:oqmd-7613  
_paper: _paper:10.1016/j.jallcom.2018.08.324:Ba5Bi3  
_tdb: _tdb:BaBi-19Liu.tdb:BA5BI3_D88  


### TDB models of BA5BI3_D88 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): BA5BI3_D88, type code %, sha256 `3c64df6c93728519…`

~~~~text
58: PHASE BA5BI3_D88 % 2 5 3 !
59: CONST BA5BI3_D88 : BA : BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/znb-1975-1-218](https://doi.org/10.1515/znb-1975-1-218) Brigitte Eisenmann, Klaus Deller, Zur Kenntnis der Erdalkaliantimonide und -wismutide Sr \<sub>2\</sub> Bi, Ba \<sub>2\</sub> Sb, Sr \<sub>5\</sub> Bi \<sub>3\</sub> , Ba \<sub>5\</sub> Sb \<sub>3\</sub> und Ba \<sub>5\</sub> Bi \<sub>3\</sub> / On the Earth-Alkali-Antimonides and Bismutides Sr \<sub>2\</sub> Bi, Ba \<sub>2\</sub> Sb, Sr \<sub>5\</sub> Bi \<sub>3\</sub> , Ba \<sub>5\</sub> Sb \<sub>3\</sub> and Ba \<sub>5\</sub> Bi \<sub>3\</sub>, Zeitschrift für Naturforschung B 30, 66-72 (1975).  
_cited as the source of values for this phase_

## BABI3 (Ba–Bi)

- Id: `phase:ba-bi:babi3`; status `assigned`
- Structure: Pb3Sr · tP4 · P4/mmm (123); type `st:pb3sr-tp4`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ba 0.2500, Bi 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–910 K, x(Bi) 0.75–0.75
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:babi3)

Names (3): _corpus: _corpus:phase:ba-bi:babi3  
_paper: _paper:10.1016/j.jallcom.2018.08.324:BaBi3  
_tdb: _tdb:BaBi-19Liu.tdb:BABI3  


### TDB models of BABI3 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): BABI3, type code %, sha256 `3c64df6c93728519…`

~~~~text
73: PHASE BABI3 % 2 1 3 !
74: CONST BABI3 : BA : BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.electacta.2016.12.141](https://doi.org/10.1016/j.electacta.2016.12.141) Timothy Lichtenstein, Nathan D. Smith, Jarrod Gesualdi, Kuldeep Kumar, Hojong Kim, Thermodynamic properties of Barium-Bismuth alloys determined by emf measurements, Electrochimica Acta 228, 628-635 (2017).  
_cited as the source of values for this phase_

## BCC_A2 (Ba–Bi)

- Id: `phase:ba-bi:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Bi) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:bcc-a2)

Names (3): _corpus: _corpus:phase:ba-bi:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2018.08.324:Bcc  
_tdb: _tdb:BaBi-19Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): BCC_A2, type code %B, sha256 `3c64df6c93728519…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : BA% BI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ba–Bi)

- Id: `phase:ba-bi:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:fcc-a1)

Names (2): _corpus: _corpus:phase:ba-bi:fcc-a1  
_tdb: _tdb:BaBi-19Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): FCC_A1, type code %A, sha256 `3c64df6c93728519…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : BA BI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase_

## HCP_A3 (Ba–Bi)

- Id: `phase:ba-bi:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:hcp-a3)

Names (2): _corpus: _corpus:phase:ba-bi:hcp-a3  
_tdb: _tdb:BaBi-19Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): HCP_A3, type code %A, sha256 `3c64df6c93728519…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : BA BI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase_

## LIQUID (Ba–Bi)

- Id: `phase:ba-bi:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 535.97–2500 K, x(Bi) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-bi:liquid)

Names (3): _corpus: _corpus:phase:ba-bi:liquid  
_paper: _paper:10.1016/j.jallcom.2018.08.324:L  
_tdb: _tdb:BaBi-19Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BaBi-19Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb): LIQUID, type code %, sha256 `3c64df6c93728519…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : BA BA4BI3 BABI3 BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.electacta.2016.12.141](https://doi.org/10.1016/j.electacta.2016.12.141) Timothy Lichtenstein, Nathan D. Smith, Jarrod Gesualdi, Kuldeep Kumar, Hojong Kim, Thermodynamic properties of Barium-Bismuth alloys determined by emf measurements, Electrochimica Acta 228, 628-635 (2017).  
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
