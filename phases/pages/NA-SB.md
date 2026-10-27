# Na–Sb phases

> Na–Sb system: 7 phases (tier A 5, tier B 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NA-SB.html · Markdown: https://data.orchid-project.org/phases/pages/NA-SB.md

7 phases (tier A 5, tier B 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NA-SB) · [full JSON](https://data.orchid-project.org/phases/systems/NA-SB.json) · [Na–Sb system page](https://data.orchid-project.org/systems/NA-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/NA-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Na–Sb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-na-sb-a7-rhombohedral); _phase:na-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 2 | 2 |
| [BCC_A2](#phase-na-sb-bcc-a2); _phase:na-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–370.87 K, x(Sb) 0–0 | 0 | 2 |
| [FCC_A1](#phase-na-sb-fcc-a1); _phase:na-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-na-sb-hcp-a3); _phase:na-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-na-sb-liquid); _phase:na-sb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 370.87–2500 K, x(Sb) 0–1 | 14 | 2 |
| [NA3SB_D018](#phase-na-sb-na3sb-d018); _phase:na-sb:na3sb-d018_ | Na3As · D0_18 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1168.13 K, x(Sb) 0.25–0.25 | 13 | 2 |
| [NASB](#phase-na-sb-nasb); _phase:na-sb:nasb_ | LiAs · mP16 · P2_1/c (14) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–744.86 K, x(Sb) 0.5–0.5 | 20 | 2 |

## RHOMBOHEDRAL_A7 (Na–Sb)

- Id: `phase:na-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 2 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-sb:a7-rhombohedral)

Names (5): _corpus: _corpus:phase:na-sb:a7-rhombohedral, corpus:phase:na-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2013.07.009:Sb  
_tdb: _tdb:NaSb-13Liu.tdb:RHOMBOHEDRAL_A7, tdb:NaSb-17Dre.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[NaSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `35a80346e37417b2…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[NaSb-17Dre.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `b4cfe0c128f39fbc…`

~~~~text
52: PHASE RHOMBOHEDRAL_A7 % 1 1 !
53: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_

## BCC_A2 (Na–Sb)

- Id: `phase:na-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–370.87 K, x(Sb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-sb:bcc-a2)

Names (3): _corpus: _corpus:phase:na-sb:bcc-a2  
_tdb: _tdb:NaSb-13Liu.tdb:BCC_A2, tdb:NaSb-17Dre.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NaSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb): BCC_A2, type code %B, sha256 `35a80346e37417b2…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : NA% SB : VA : !
~~~~

[NaSb-17Dre.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb): BCC_A2, type code %B, sha256 `b4cfe0c128f39fbc…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : NA% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase_

## FCC_A1 (Na–Sb)

- Id: `phase:na-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-sb:fcc-a1)

Names (3): _corpus: _corpus:phase:na-sb:fcc-a1  
_tdb: _tdb:NaSb-13Liu.tdb:FCC_A1, tdb:NaSb-17Dre.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NaSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb): FCC_A1, type code %A, sha256 `35a80346e37417b2…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : NA SB : VA : !
~~~~

[NaSb-17Dre.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb): FCC_A1, type code %A, sha256 `b4cfe0c128f39fbc…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : NA SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase_

## HCP_A3 (Na–Sb)

- Id: `phase:na-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:na-sb:hcp-a3  
_tdb: _tdb:NaSb-13Liu.tdb:HCP_A3, tdb:NaSb-17Dre.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NaSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb): HCP_A3, type code %A, sha256 `35a80346e37417b2…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : NA SB : VA : !
~~~~

[NaSb-17Dre.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb): HCP_A3, type code %A, sha256 `b4cfe0c128f39fbc…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : NA SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase_

## LIQUID (Na–Sb)

- Id: `phase:na-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 370.87–2500 K, x(Sb) 0–1
- Literature: 14 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-sb:liquid)

Names (5): _corpus: _corpus:phase:na-sb:liquid  
_paper: _paper:10.1016/j.jallcom.2016.11.003:liquid, paper:10.1016/j.tca.2013.07.009:liq  
_tdb: _tdb:NaSb-13Liu.tdb:LIQUID, tdb:NaSb-17Dre.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NaSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb): LIQUID, type code %, sha256 `35a80346e37417b2…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : NA NA3SB SB : !
~~~~

[NaSb-17Dre.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb): LIQUID, type code %, sha256 `b4cfe0c128f39fbc…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : NA NA3SB SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-1982-0612](https://doi.org/10.1515/zna-1982-0612) H. Redslob, G. Steinleitner, W. Freyland, Transition to Semiconducting Characteristics in Liquid Alkalimetal-Antimony-Alloys, Zeitschrift für Naturforschung A 37, 587-593 (1982).  
_cited as the source of values for this phase_

## NA3SB_D018 (Na–Sb)

- Id: `phase:na-sb:na3sb-d018`; status `assigned`
- Structure: Na3As · D0_18 · hP8 · P6_3/mmc (194); type `st:d0-18-na3as-hp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaalua and oqmd-5156, space group 194
- Stoichiometry: Na 0.7500, Sb 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1168.13 K, x(Sb) 0.25–0.25
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-sb:na3sb-d018)

Names (7): _corpus: _corpus:phase:na-sb:na3sb-d018  
_mp: _mp:mp-aaaaalua  
_oqmd: _oqmd:oqmd-5156  
_paper: _paper:10.1016/j.jallcom.2016.11.003:Na3Sb, paper:10.1016/j.tca.2013.07.009:Na3Sb  
_tdb: _tdb:NaSb-13Liu.tdb:NA3SB_D018, tdb:NaSb-17Dre.tdb:NA3SB_D018  


### TDB models of NA3SB_D018 (2): PHASE and CONSTITUENT statements as written

[NaSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb): NA3SB_D018, type code %, sha256 `35a80346e37417b2…`

~~~~text
49: PHASE NA3SB_D018 % 2 3 1 !
50: CONST NA3SB_D018 : NA : SB : !
~~~~

[NaSb-17Dre.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb): NA3SB_D018, type code %, sha256 `b4cfe0c128f39fbc…`

~~~~text
57: PHASE NA3SB_D018 % 2 3 1 !
58: CONST NA3SB_D018 : NA : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_

## NASB (Na–Sb)

- Id: `phase:na-sb:nasb`; status `assigned`
- Structure: LiAs · mP16 · P2_1/c (14); type `st:lias-mp16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Na 0.5000, Sb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–744.86 K, x(Sb) 0.5–0.5
- Literature: 20 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-sb:nasb)

Names (7): _corpus: _corpus:phase:na-sb:nasb  
_mp: _mp:mp-aaaaalto  
_oqmd: _oqmd:oqmd-5018  
_paper: _paper:10.1016/j.jallcom.2016.11.003:NaSb, paper:10.1016/j.tca.2013.07.009:NaSb  
_tdb: _tdb:NaSb-13Liu.tdb:NASB, tdb:NaSb-17Dre.tdb:NASB  


### TDB models of NASB (2): PHASE and CONSTITUENT statements as written

[NaSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-13Liu.tdb): NASB, type code %, sha256 `35a80346e37417b2…`

~~~~text
54: PHASE NASB % 2 1 1 !
55: CONST NASB : NA : SB : !
~~~~

[NaSb-17Dre.tdb](https://orchid-project.org/data/databases/sgte-binary/NaSb-17Dre.tdb): NASB, type code %, sha256 `b4cfe0c128f39fbc…`

~~~~text
62: PHASE NASB % 2 1 1 !
63: CONST NASB : NA : SB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2016.11.003](https://doi.org/10.1016/j.jallcom.2016.11.003) Liya Dreval, Matthias Zschornak, Wolfram Münchgesang, Olga Fabrichnaya, David Rafaja, Miléna L. Martine et al., Thermodynamic assessment and first principle calculations of the Na Sb Sn system, Journal of Alloys and Compounds 695, 1725-1742 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-1982-0612](https://doi.org/10.1515/zna-1982-0612) H. Redslob, G. Steinleitner, W. Freyland, Transition to Semiconducting Characteristics in Liquid Alkalimetal-Antimony-Alloys, Zeitschrift für Naturforschung A 37, 587-593 (1982).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667822](https://doi.org/10.1007/bf02667822) J. Sangster, A.D. Pelton, The Na–Sb (sodium–antimony) system, Journal of Phase Equilibria 14 (2) (1993) 250–255.  
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
